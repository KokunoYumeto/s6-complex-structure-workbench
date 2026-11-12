#!/usr/bin/env python3
"""Build and fail-closed audit the curated S6 Zenodo release.

The canonical Overleaf tree intentionally preserves historical and private
workflow evidence that does not belong in a DOI payload.  This program copies
an explicit public subset into an external staging directory, generates the
release metadata and inventories there, privacy-scans ordinary text and PDFs,
and creates a deterministic source ZIP whose extracted inventory is proved
identical to the staging inventory.

Run with ``--prepare-only`` before the depositor has chosen a creator and
license.  A final release refuses placeholders.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
import zipfile
from typing import Iterable

from pypdf import PdfReader


VERSION = "1.0.0"
ZIP_TIME = (2026, 9, 1, 0, 0, 0)
ROOT_FILES = {
    "koide_arithmetic_preprint.tex",
    "main.tex",
    "original_clean_transcription.tex",
    "references.bib",
    "s6_compact_link_gaussian_preprint.tex",
    "s6_cone_sphere_routes_companion.bib",
    "s6_cone_sphere_routes_preprint.tex",
    "s6_spectral_degeneration_preprint.tex",
    "workbench.tex",
    "workbench_and_manuscript_overview.tex",
}
PUBLIC_PREFIXES = (
    "supporting_materials/audit_annotation_sources/",
    "supporting_materials/manuscript_sources/",
    "supporting_materials/peer_reviews/",
    "supporting_materials/publication/",
    "supporting_materials/reference_pdfs/",
    "supporting_materials/reproducibility/",
    "supporting_materials/workbench/",
)
PROJECT_DOCUMENTS = {
    "supporting_materials/project_documentation/BUILD.md",
    "supporting_materials/project_documentation/EXACT_CHECK_RERUN_2026-08-28.md",
    "supporting_materials/project_documentation/EXCLUSIONS.md",
    "supporting_materials/project_documentation/PUBLIC_PROVENANCE_POLICY.md",
    "supporting_materials/project_documentation/PUBLICATION_WORKFLOW.md",
    "supporting_materials/project_documentation/RIGHTS_AND_PROVENANCE.md",
}
EXACT_EXCLUSIONS = {
    "supporting_materials/manuscript_sources/reconstruction_audit/BUILD_ENVIRONMENT.txt",
    "supporting_materials/peer_reviews/superseded_packet_06/review_receipt.json",
}
EXCLUDED_PARTS = {
    "archive",
    "workbench_history",
    "source_record",
    "session",
    "__pycache__",
    ".pytest_cache",
}
EXCLUDED_NAME_FRAGMENTS = {
    "assistant_visible_outputs",
    "product_progress_record",
    "integration_visible_summary",
    "integration_session_visible_outputs",
    "preflight",
    "render_log",
    "compile_failure",
    "source_inventory",
    "build_environment",
}
EXCLUDED_SUFFIXES = {
    ".aux",
    ".fls",
    ".fdb_latexmk",
    ".synctex",
    ".synctex.gz",
    ".toc",
    ".out",
    ".log",
    ".zip",
    ".pyc",
}
TEXT_SUFFIXES = {
    ".bib", ".cff", ".csv", ".json", ".jsonl", ".md", ".py", ".sh",
    ".tex", ".tsv", ".txt", ".yaml", ".yml", ".sha256",
}
EXPECTED_PDFS = {
    "supporting_materials/reference_pdfs/s6_canonical_annotated_peer_review.pdf": 128,
    "supporting_materials/reference_pdfs/s6_canonical_clean.pdf": 108,
    "supporting_materials/reference_pdfs/s6_validate_repair_disprove_workbench.pdf": 283,
    "supporting_materials/reference_pdfs/s6_mathematical_overview.pdf": 10,
    "supporting_materials/reference_pdfs/s6_peer_verification_monograph.pdf": 294,
}


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def safe_relative(value: str) -> bool:
    p = PurePosixPath(value)
    return bool(value) and not p.is_absolute() and ".." not in p.parts and "\\" not in value


def selected(rel: str) -> bool:
    if rel in ROOT_FILES or rel in PROJECT_DOCUMENTS:
        return True
    if rel in EXACT_EXCLUSIONS:
        return False
    if not rel.startswith(PUBLIC_PREFIXES):
        return False
    parts = {part.casefold() for part in PurePosixPath(rel).parts}
    if parts & EXCLUDED_PARTS:
        return False
    name = PurePosixPath(rel).name.casefold()
    if any(fragment in name for fragment in EXCLUDED_NAME_FRAGMENTS):
        return False
    if any(name.endswith(suffix) for suffix in EXCLUDED_SUFFIXES):
        return False
    # Raw execution chatter is redundant with deterministic result JSON.
    if "execution.log" in name or name.endswith(".stdout.txt"):
        return False
    return True


def inventory(root: Path) -> list[dict[str, object]]:
    rows = []
    for path in sorted((p for p in root.rglob("*") if p.is_file()), key=lambda p: relative(root, p)):
        rel = relative(root, path)
        rows.append({"path": rel, "bytes": path.stat().st_size, "sha256": digest_file(path)})
    return rows


def inventory_digest(rows: Iterable[dict[str, object]]) -> str:
    encoded = json.dumps(list(rows), ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode()
    return digest_bytes(encoded)


def copy_public_subset(source: Path, staging: Path) -> tuple[list[dict[str, object]], list[str]]:
    copied: list[dict[str, object]] = []
    excluded: list[str] = []
    casefolded: dict[str, str] = {}
    for src in sorted((p for p in source.rglob("*") if p.is_file()), key=lambda p: relative(source, p)):
        rel = relative(source, src)
        if src.is_symlink() or src.is_mount():
            raise RuntimeError(f"symbolic link or mount point rejected: {rel}")
        if not safe_relative(rel):
            raise RuntimeError(f"unsafe source path: {rel}")
        folded = rel.casefold()
        if folded in casefolded and casefolded[folded] != rel:
            raise RuntimeError(f"case-fold path collision: {casefolded[folded]} / {rel}")
        casefolded[folded] = rel
        if not selected(rel):
            excluded.append(rel)
            continue
        dst = staging / PurePosixPath(rel)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        source_hash = digest_file(src)
        copied_hash = digest_file(dst)
        if source_hash != copied_hash or src.stat().st_size != dst.stat().st_size:
            raise RuntimeError(f"copy verification failed: {rel}")
        copied.append({"path": rel, "bytes": dst.stat().st_size, "sha256": copied_hash})
    return copied, excluded


def release_description() -> str:
    return (
        "This record presents an AI-produced mathematical verification and reconstruction audit "
        "of a reported candidate compact complex threefold diffeomorphic to the six-sphere. "
        "The primary monograph combines a mathematical orientation with the complete "
        "validate/repair/disprove workbench; supplements provide the source reconstruction, "
        "review records, exact certificates, reproducibility materials, a curated mathematical "
        "chronology, a separately validated complete sanitized human/assistant conversation "
        "record, and an optional privacy-checked full typed workflow annex. "
        "Claims are labelled VERIFIED, OPEN, or REFUTED according to the proofs and "
        "counterexamples recorded in the monograph. Those labels do not constitute conventional "
        "journal peer review, independent specialist certification, or community acceptance. "
        "The candidate and its original claims remain attributed to their reported Claude/Fabel "
        "source, and this deposit makes no priority claim. Independent specialist replication "
        "and external adjudication remain open. Third-party literature is cited but not bundled; "
        "the private raw session record is not deposited."
    )


def generate_release_files(staging: Path, creator: str, license_id: str, date: str, prepare_only: bool) -> None:
    title = "Verification and Reconstruction of a Claimed Complex Structure on S6: An AI-Produced Validate/Repair/Disprove Record"
    creator_value = creator if creator else "CREATOR_DECISION_PENDING"
    license_value = license_id if license_id else "LICENSE_DECISION_PENDING"
    metadata = {
        "title": title,
        "upload_type": "publication",
        "publication_type": "other",
        "publication_date": date,
        "version": "1.0",
        "description": release_description(),
        "creators": [{"name": creator_value}],
        "keywords": [
            "six-sphere (S6)", "complex threefold", "claimed complex structure",
            "mathematical proof audit", "proof verification", "validate/repair/disprove",
            "AI-generated mathematics", "nearby cycles", "Leray spectral sequence",
            "Hodge theory", "Bott-Chern and Aeppli cohomology", "reproducible research",
            "mathematical provenance", "CDP20",
        ],
        "access_right": "open",
        "license": license_value,
        "notes": (
            "Third-party literature is cited but not bundled. The file-level rights boundary is "
            "stated in RIGHTS_AND_PROVENANCE.md and LICENSE_SCOPE.md. The theorem-status labels "
            "record an internal proof audit; independent specialist adjudication remains open."
        ),
        "release_ready": not prepare_only,
    }
    metadata_path = staging / "supporting_materials/metadata/zenodo_metadata.v1.json"
    metadata_path.parent.mkdir(parents=True, exist_ok=True)
    metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")

    readme = f"""# Verification and Reconstruction of a Claimed Complex Structure on S6

Version 1.0; release date {date}.

The primary artifact is the 294-page peer-verification monograph.  It joins a
ten-page mathematical orientation to the complete 283-page
validate/repair/disprove paper.  The 128-page annotated edition preserves the
independent review record around the 108-page reconstructed manuscript; the
clean transcription is supplied separately for editing and recompilation.

The internal ledger at this freeze records 65 VERIFIED, zero CONDITIONAL, four
OPEN, and six REFUTED claims.  The OPEN mathematical rows concern independent
specialist replication and external adjudication, not missing internal proof
premises.  These labels do not constitute journal certification or community
acceptance.

The optional machine-readable conversation annex contains 976 actual
human/assistant natural-language events.  It excludes 166 platform-injected
context-only records, preserves 940 events verbatim after privacy redaction,
and replaces 36 profane or abusive user turns with neutral source-hash-anchored
summaries.  Its independent deterministic replay reports zero unresolved
events and zero privacy findings.  The private 1.4 GB raw session JSONL is not
deposited.

A second optional provenance annex represents a later frozen
1,483,338,786-byte source prefix as 20,977 ordered typed events: 1,011
conversation messages, 9,570 tool calls, 9,567 tool outputs, and 829
metadata-only internal-agent markers.  Thirty-seven user turns are neutral,
source-hash-anchored summaries.  Tool bodies are omitted, but type, ordering,
pairing, sizes, hashes, structural profiles, and safe status scalars are
retained.  Its deterministic 2,746,333-byte gzip expands byte-for-byte to the
15,175,531-byte JSONL.  The automated derivation and the parent rerun both
report zero unresolved events and zero privacy findings.

## Navigation

1. `supporting_materials/reference_pdfs/s6_peer_verification_monograph.pdf`
2. `supporting_materials/reference_pdfs/s6_canonical_annotated_peer_review.pdf`
3. `supporting_materials/reference_pdfs/s6_canonical_clean.pdf`
4. project-root `workbench.tex`, `main.tex`,
   `original_clean_transcription.tex`, and
   `workbench_and_manuscript_overview.tex`
5. project-root specialist drafts:
   `koide_arithmetic_preprint.tex`,
   `s6_spectral_degeneration_preprint.tex`,
   `s6_compact_link_gaussian_preprint.tex`, and
   `s6_cone_sphere_routes_preprint.tex`
6. `supporting_materials/publication/public_mathematical_provenance_v1.md`
7. `supporting_materials/publication/complete_sanitized_conversation_v1.jsonl`
   (optional machine-readable audit trail; independently replayed and
   privacy-validated)
8. `supporting_materials/publication/full_record_public_annex_v2/`
   (optional full typed workflow provenance; use the `.jsonl.gz` for download)

The reported candidate and its original claims remain attributed to their
reported Claude/Fabel source.  The present record is an AI-produced
verification aid and makes no priority claim.  Third-party mathematical
literature is cited but not bundled.
"""
    (staging / "README.md").write_text(readme, encoding="utf-8", newline="\n")

    citation = f"""cff-version: 1.2.0
message: "If you use this verification record, please cite this release."
title: "{title}"
type: report
version: "1.0"
date-released: "{date}"
authors:
  - name: "{creator_value}"
abstract: >-
  {release_description()}
license: "{license_value}"
"""
    (staging / "CITATION.cff").write_text(citation, encoding="utf-8", newline="\n")

    scope = f"""# License scope

Selected record-level license: `{license_value}`.

The selected license applies only to package-created material to the extent
the depositor holds or may exercise the relevant rights.  It does not place
third-party journal articles, books, citations, trademarks, or other external
works under that license.  Third-party literature is cited but not bundled.
The reconstructed manuscript and its PDFs are included on the depositor's
representation that their reported AI provenance permits public redistribution.
See `supporting_materials/project_documentation/RIGHTS_AND_PROVENANCE.md`.
"""
    (staging / "LICENSE_SCOPE.md").write_text(scope, encoding="utf-8", newline="\n")
    rights = staging / "supporting_materials/project_documentation/RIGHTS_AND_PROVENANCE.md"
    if rights.exists():
        shutil.copyfile(rights, staging / "RIGHTS_AND_PROVENANCE.md")


def write_generated_metadata(staging: Path, copied: list[dict[str, object]], excluded: list[str]) -> None:
    metadata_dir = staging / "supporting_materials/metadata"
    metadata_dir.mkdir(parents=True, exist_ok=True)
    generated_names = {
        "supporting_materials/metadata/FILE_TREE.txt",
        "supporting_materials/metadata/PROJECT_MANIFEST.json",
        "supporting_materials/metadata/SHA256SUMS.txt",
    }
    files = [p for p in staging.rglob("*") if p.is_file()]
    rels = sorted(relative(staging, p) for p in files)
    final_rels = sorted(set(rels) | generated_names)
    tree = ["S6 peer-verification Zenodo source tree", f"Files: {len(final_rels)}", "", *final_rels]
    (metadata_dir / "FILE_TREE.txt").write_text("\n".join(tree) + "\n", encoding="utf-8", newline="\n")

    payload = []
    for path in sorted((p for p in staging.rglob("*") if p.is_file()), key=lambda p: relative(staging, p)):
        rel = relative(staging, path)
        if rel in generated_names:
            continue
        payload.append({"path": rel, "bytes": path.stat().st_size, "sha256": digest_file(path)})
    manifest = {
        "schema": "s6-zenodo-source-manifest-v1",
        "builder_version": VERSION,
        "selected_source_files": len(copied),
        "excluded_source_files": len(excluded),
        "payload_entries": len(payload),
        "payload_bytes": sum(int(row["bytes"]) for row in payload),
        "expected_pdf_pages": EXPECTED_PDFS,
        "entries": payload,
    }
    (metadata_dir / "PROJECT_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n"
    )
    checksum_rows = []
    for path in sorted((p for p in staging.rglob("*") if p.is_file()), key=lambda p: relative(staging, p)):
        rel = relative(staging, path)
        if rel == "supporting_materials/metadata/SHA256SUMS.txt":
            continue
        checksum_rows.append(f"{digest_file(path)}  {rel}")
    (metadata_dir / "SHA256SUMS.txt").write_text("\n".join(checksum_rows) + "\n", encoding="utf-8", newline="\n")


def scan_text(text: str, rel: str) -> list[str]:
    checks = {
        "user_first_name": r"(?i)\buser\b",
        "windows_absolute_path": r"(?i)\b[a-z]:[\\/](?:users|documents|downloads|windows|program files|programdata|temp|appdata)(?:[\\/]|\b)",
        "private_posix_path": r"/(?:Users|home|mnt/data)/",
        "overleaf_access_endpoint": r"(?i)overleaf\.com/(?:project|read)/",
        "credential_assignment": r"(?i)(?:bearer|api[_ -]?key|password|secret)\s*[:=]",
        "private_key_header": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
        "informal_abuse": r"(?i)\b(?:fuck|fucking|retard|retarded|shit)\b",
        "raw_chat_marker": r"(?i)(?:<codex_delegation>|<codex_internal_context|custom_tool_call_output)",
    }
    hits = [name for name, pattern in checks.items() if re.search(pattern, text)]
    # These two scripts necessarily contain protocol strings as patterns to
    # reject; the scanner vocabulary is not copied conversation content.
    scanner_source = rel.endswith((
        "extract_public_provenance.py",
        "build_zenodo_release.py",
        "generate_complete_conversation_provenance.py",
        "validate_complete_conversation_provenance.py",
        "generate_s6_full_record_public_annex.py",
        "validate_s6_full_record_public_annex.py",
    ))
    if scanner_source:
        hits = [hit for hit in hits if hit not in {"informal_abuse", "raw_chat_marker"}]
    elif "/full_record_public_annex_v2/" in "/" + rel.replace("\\", "/"):
        # The independently parsed and replayed annex legitimately records the
        # literal typed tool-output class name; it does not reproduce a raw
        # platform record. All other generic privacy gates remain active.
        hits = [hit for hit in hits if hit != "raw_chat_marker"]
    else:
        if re.search(r"(?i)(?:sandbox:|codex://)", text):
            hits.append("agent_or_sandbox_uri")
    return sorted(set(hits))


def privacy_audit(staging: Path) -> dict[str, object]:
    hits: list[dict[str, object]] = []
    scanned_text = 0
    scanned_pdfs = 0
    for path in sorted((p for p in staging.rglob("*") if p.is_file()), key=lambda p: relative(staging, p)):
        rel = relative(staging, path)
        suffix = path.suffix.casefold()
        if suffix in TEXT_SUFFIXES or path.name.casefold() in {"license", "notice", "copying"}:
            scanned_text += 1
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                hits.append({"path": rel, "findings": ["non_utf8_public_text"]})
                continue
            findings = scan_text(text, rel)
            if findings:
                hits.append({"path": rel, "findings": findings})
        elif suffix == ".pdf":
            scanned_pdfs += 1
            try:
                reader = PdfReader(path, strict=True)
                text = "\n".join(page.extract_text() or "" for page in reader.pages)
                findings = scan_text(text, rel)
                if findings:
                    hits.append({"path": rel, "findings": findings})
            except Exception as exc:
                hits.append({"path": rel, "findings": [f"pdf_scan_error:{type(exc).__name__}"]})
    return {
        "scanned_text_files": scanned_text,
        "scanned_pdfs": scanned_pdfs,
        "findings": hits,
        "passed": not hits,
    }


def validate_pdfs(staging: Path) -> dict[str, object]:
    rows = []
    for rel, expected_pages in EXPECTED_PDFS.items():
        path = staging / PurePosixPath(rel)
        if not path.exists():
            raise RuntimeError(f"required PDF absent: {rel}")
        reader = PdfReader(path, strict=True)
        pages = len(reader.pages)
        if pages != expected_pages:
            raise RuntimeError(f"PDF page mismatch for {rel}: {pages} != {expected_pages}")
        rows.append({"path": rel, "pages": pages, "bytes": path.stat().st_size, "sha256": digest_file(path)})
    return {"passed": True, "pdfs": rows}


def deterministic_zip(staging: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    temp = output.with_suffix(output.suffix + ".tmp")
    if temp.exists():
        temp.unlink()
    with zipfile.ZipFile(temp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted((p for p in staging.rglob("*") if p.is_file()), key=lambda p: relative(staging, p)):
            rel = relative(staging, path)
            info = zipfile.ZipInfo(rel, ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    temp.replace(output)


def verify_zip(staging: Path, archive_path: Path) -> dict[str, object]:
    source_rows = inventory(staging)
    with tempfile.TemporaryDirectory(prefix="s6_zenodo_roundtrip_") as td:
        extracted = Path(td)
        with zipfile.ZipFile(archive_path, "r") as archive:
            seen: set[str] = set()
            for info in archive.infolist():
                if info.is_dir():
                    continue
                if not safe_relative(info.filename):
                    raise RuntimeError(f"unsafe ZIP member: {info.filename}")
                folded = info.filename.casefold()
                if folded in seen:
                    raise RuntimeError(f"duplicate/case-fold ZIP member: {info.filename}")
                seen.add(folded)
                target = extracted / PurePosixPath(info.filename)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(archive.read(info))
        extracted_rows = inventory(extracted)
        if source_rows != extracted_rows:
            raise RuntimeError("round-trip inventory differs from staging")
    # Byte determinism is checked with a second independent sibling pack.
    second_path = archive_path.with_suffix(archive_path.suffix + ".second")
    deterministic_zip(staging, second_path)
    same = archive_path.read_bytes() == second_path.read_bytes()
    second_path.unlink()
    if not same:
        raise RuntimeError("deterministic second pack is not byte-identical")
    return {
        "passed": True,
        "entries": len(source_rows),
        "payload_bytes": sum(int(row["bytes"]) for row in source_rows),
        "inventory_sha256": inventory_digest(source_rows),
        "zip_bytes": archive_path.stat().st_size,
        "zip_sha256": digest_file(archive_path),
        "byte_identical_second_pack": True,
    }


def validate_complete_conversation_publication(staging: Path) -> dict[str, object]:
    """Fail closed on the optional sanitized conversation publication set."""

    base = staging / "supporting_materials/publication"
    names = {
        "candidate": "complete_sanitized_conversation_v1.jsonl",
        "receipt": "complete_sanitized_conversation_receipt_v1.json",
        "validation": "complete_sanitized_conversation_validation_v1.json",
        "summaries": "complete_sanitized_conversation_editorial_summaries_v1.json",
        "status": "complete_sanitized_conversation_release_status_v1.txt",
        "queue": "complete_sanitized_conversation_unresolved_queue_v1.jsonl",
    }
    paths = {key: base / name for key, name in names.items()}
    present = {key for key, path in paths.items() if path.exists()}
    if not present:
        return {"included": False, "passed": True}
    if present != set(paths):
        missing = sorted(set(paths) - present)
        raise RuntimeError(f"optional complete-conversation set is incomplete: {missing}")

    receipt = json.loads(paths["receipt"].read_text(encoding="utf-8"))
    validation = json.loads(paths["validation"].read_text(encoding="utf-8"))
    summaries = json.loads(paths["summaries"].read_text(encoding="utf-8"))
    if receipt.get("schema") != "s6-complete-conversation-provenance-receipt-v1":
        raise RuntimeError("unexpected complete-conversation receipt schema")
    if validation.get("schema") != "s6-complete-conversation-validation-report-v1":
        raise RuntimeError("unexpected complete-conversation validation schema")
    if summaries.get("schema") != "s6-complete-conversation-editorial-summaries-v1":
        raise RuntimeError("unexpected complete-conversation summary schema")
    if receipt.get("release") != {
        "safe_to_include": True,
        "status": "RELEASE_READY",
        "unresolved_event_count": 0,
        "validator_must_pass_before_inclusion": True,
    }:
        raise RuntimeError("complete-conversation receipt is not RELEASE_READY")
    if validation.get("release") != {
        "safe_to_include": True,
        "status": "RELEASE_READY",
        "unresolved_event_count": 0,
    }:
        raise RuntimeError("complete-conversation independent validation is not RELEASE_READY")
    if not validation.get("privacy_scan", {}).get("passed"):
        raise RuntimeError("complete-conversation validation privacy scan did not pass")
    if not all(validation.get("validation", {}).values()):
        raise RuntimeError("complete-conversation replay validation contains a false gate")

    descriptors = receipt.get("outputs", {})
    for key, receipt_key in (("candidate", "candidate"), ("status", "release_status"), ("queue", "unresolved_queue")):
        descriptor = descriptors.get(receipt_key, {})
        path = paths[key]
        expected = {
            "bytes": path.stat().st_size,
            "filename": path.name,
            "sha256": digest_file(path),
        }
        if descriptor != expected:
            raise RuntimeError(f"complete-conversation descriptor mismatch: {receipt_key}")
    if digest_file(paths["summaries"]) != receipt.get("editorial_summaries", {}).get("sha256"):
        raise RuntimeError("complete-conversation summary hash mismatch")
    if paths["queue"].stat().st_size != 0:
        raise RuntimeError("complete-conversation unresolved queue is not empty")

    repro = staging / "supporting_materials/reproducibility"
    script_checks = {
        "generator": repro / receipt.get("generator", {}).get("filename", ""),
        "validator": repro / receipt.get("validator", {}).get("filename", ""),
    }
    for key, path in script_checks.items():
        if not path.is_file() or digest_file(path) != receipt.get(key, {}).get("sha256"):
            raise RuntimeError(f"complete-conversation {key} script hash mismatch")

    return {
        "included": True,
        "passed": True,
        "natural_language_events": receipt.get("counts", {}).get("natural_language_events"),
        "summarized_redacted": receipt.get("counts", {}).get("modes", {}).get("summarized-redacted"),
        "verbatim_redacted": receipt.get("counts", {}).get("modes", {}).get("verbatim-redacted"),
        "candidate_sha256": digest_file(paths["candidate"]),
        "validation_report_sha256": digest_file(paths["validation"]),
    }


def validate_full_record_publication(staging: Path) -> dict[str, object]:
    """Fail closed on the optional full typed-record provenance annex."""

    base = staging / "supporting_materials/publication/full_record_public_annex_v2"
    names = {
        "readme": "README.md",
        "candidate_readme": "README_PUBLIC_ANNEX_V2.md",
        "parent": "PARENT_REVIEW.json",
        "generator": "generate_s6_full_record_public_annex.py",
        "jsonl": "s6_full_record_public_annex_v2.jsonl",
        "gzip": "s6_full_record_public_annex_v2.jsonl.gz",
        "summaries": "s6_full_record_public_annex_v2_editorial_summaries.json",
        "inventory": "s6_full_record_public_annex_v2_inventory.json",
        "receipt": "s6_full_record_public_annex_v2_receipt.json",
        "status": "s6_full_record_public_annex_v2_status.txt",
        "queue": "s6_full_record_public_annex_v2_unresolved_queue.jsonl",
        "validation": "s6_full_record_public_annex_v2_validation_report.json",
        "validator": "validate_s6_full_record_public_annex.py",
        "checksums": "SHA256SUMS.txt",
    }
    paths = {key: base / name for key, name in names.items()}
    present = {key for key, path in paths.items() if path.exists()}
    if not present:
        return {"included": False, "passed": True}
    if present != set(paths):
        raise RuntimeError(f"optional full-record annex is incomplete: {sorted(set(paths) - present)}")

    receipt = json.loads(paths["receipt"].read_text(encoding="utf-8"))
    validation = json.loads(paths["validation"].read_text(encoding="utf-8"))
    parent = json.loads(paths["parent"].read_text(encoding="utf-8"))
    inventory_data = json.loads(paths["inventory"].read_text(encoding="utf-8"))
    if receipt.get("schema") != "s6-full-record-public-annex-receipt-v2":
        raise RuntimeError("unexpected full-record receipt schema")
    if validation.get("schema") != "s6-full-record-public-annex-validation-v2":
        raise RuntimeError("unexpected full-record validation schema")
    if parent.get("schema") != "s6-full-record-public-annex-parent-review-v1":
        raise RuntimeError("unexpected full-record parent-review schema")
    if inventory_data.get("schema") != "s6-full-record-public-annex-inventory-v2":
        raise RuntimeError("unexpected full-record inventory schema")
    if not all(value is True for value in validation.get("checks", {}).values()):
        raise RuntimeError("full-record automated validation contains a false gate")
    if validation.get("counts", {}).get("privacy_findings") != 0:
        raise RuntimeError("full-record privacy validation did not pass")
    if validation.get("counts", {}).get("unresolved_events") != 0 or paths["queue"].stat().st_size != 0:
        raise RuntimeError("full-record unresolved queue is not empty")
    if parent.get("decision") != "INCLUDE_AS_OPTIONAL_PROVENANCE_SUPPLEMENT" or not parent.get("publication_authorized"):
        raise RuntimeError("full-record parent review has not authorized inclusion")

    prefix = receipt.get("source", {})
    for source in (validation.get("source", {}), parent.get("source_scope", {})):
        if source.get("prefix_bytes") != prefix.get("prefix_bytes") or source.get("prefix_sha256") != prefix.get("prefix_sha256"):
            raise RuntimeError("full-record frozen-prefix identity mismatch")

    checksum_rows: dict[str, str] = {}
    for line in paths["checksums"].read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^/\\]+)", line)
        if not match or match.group(2) in checksum_rows:
            raise RuntimeError("invalid or duplicate full-record checksum row")
        checksum_rows[match.group(2)] = match.group(1)
    if len(checksum_rows) != 11:
        raise RuntimeError("full-record checksum ledger must contain exactly 11 rows")
    for name, expected in checksum_rows.items():
        path = base / name
        if not path.is_file() or digest_file(path) != expected:
            raise RuntimeError(f"full-record checksum mismatch: {name}")

    compressed = paths["gzip"].read_bytes()
    if len(compressed) < 10 or int.from_bytes(compressed[4:8], "little") != 0:
        raise RuntimeError("full-record gzip is not deterministically timestamped")
    if gzip.decompress(compressed) != paths["jsonl"].read_bytes():
        raise RuntimeError("full-record gzip does not reproduce the JSONL")

    stream = parent.get("public_stream", {})
    if stream.get("events") != 20977 or stream.get("jsonl_sha256") != digest_file(paths["jsonl"]):
        raise RuntimeError("full-record parent-review stream descriptor mismatch")
    if stream.get("gzip_sha256") != digest_file(paths["gzip"]):
        raise RuntimeError("full-record parent-review gzip descriptor mismatch")
    return {
        "included": True,
        "passed": True,
        "events": stream.get("events"),
        "conversation_messages": stream.get("conversation_messages"),
        "tool_calls": stream.get("tool_calls"),
        "tool_outputs": stream.get("tool_outputs"),
        "summarized_user_turns": stream.get("summarized_user_turns"),
        "gzip_sha256": digest_file(paths["gzip"]),
        "validation_report_sha256": digest_file(paths["validation"]),
        "parent_review_sha256": digest_file(paths["parent"]),
    }


def copy_outer_files(staging: Path, output: Path, zip_path: Path, prepare_only: bool) -> list[Path]:
    output.mkdir(parents=True, exist_ok=True)
    mapping = {
        "01_s6_peer_verification_monograph_v1.0.pdf": "supporting_materials/reference_pdfs/s6_peer_verification_monograph.pdf",
        "02_s6_annotated_manuscript_v1.0.pdf": "supporting_materials/reference_pdfs/s6_canonical_annotated_peer_review.pdf",
        "03_s6_clean_latex_reconstruction_v1.0.pdf": "supporting_materials/reference_pdfs/s6_canonical_clean.pdf",
        "05_s6_public_mathematical_provenance_v1.0.md": "supporting_materials/publication/public_mathematical_provenance_v1.md",
        "06_s6_public_provenance_receipt_v1.0.json": "supporting_materials/publication/public_provenance_receipt_v1.json",
        "README.md": "README.md",
        "CITATION.cff": "CITATION.cff",
        "RIGHTS_AND_PROVENANCE.md": "RIGHTS_AND_PROVENANCE.md",
        "LICENSE_SCOPE.md": "LICENSE_SCOPE.md",
        "zenodo_metadata.v1.json": "supporting_materials/metadata/zenodo_metadata.v1.json",
    }
    optional_conversation = {
        "07_s6_complete_sanitized_conversation_v1.0.jsonl": "supporting_materials/publication/complete_sanitized_conversation_v1.jsonl",
        "08_s6_complete_sanitized_conversation_receipt_v1.0.json": "supporting_materials/publication/complete_sanitized_conversation_receipt_v1.json",
        "09_s6_complete_sanitized_conversation_validation_v1.0.json": "supporting_materials/publication/complete_sanitized_conversation_validation_v1.json",
    }
    present = [name for name, rel in optional_conversation.items() if (staging / PurePosixPath(rel)).exists()]
    if present and len(present) != len(optional_conversation):
        raise RuntimeError("optional complete-conversation outer publication set is incomplete")
    if len(present) == len(optional_conversation):
        mapping.update(optional_conversation)
    optional_full_record = {
        "10_s6_full_typed_record_annex_v2.0.jsonl.gz": "supporting_materials/publication/full_record_public_annex_v2/s6_full_record_public_annex_v2.jsonl.gz",
        "11_s6_full_typed_record_receipt_v2.0.json": "supporting_materials/publication/full_record_public_annex_v2/s6_full_record_public_annex_v2_receipt.json",
        "12_s6_full_typed_record_validation_v2.0.json": "supporting_materials/publication/full_record_public_annex_v2/s6_full_record_public_annex_v2_validation_report.json",
        "13_s6_full_typed_record_parent_review_v1.0.json": "supporting_materials/publication/full_record_public_annex_v2/PARENT_REVIEW.json",
    }
    present_full = [name for name, rel in optional_full_record.items() if (staging / PurePosixPath(rel)).exists()]
    if present_full and len(present_full) != len(optional_full_record):
        raise RuntimeError("optional full-record outer publication set is incomplete")
    if len(present_full) == len(optional_full_record):
        mapping.update(optional_full_record)
    outputs: list[Path] = []
    for name, rel in mapping.items():
        target = output / name
        shutil.copyfile(staging / PurePosixPath(rel), target)
        outputs.append(target)
    zip_target = output / "04_s6_peer_verification_sources_and_evidence_v1.0.zip"
    shutil.copyfile(zip_path, zip_target)
    outputs.append(zip_target)
    if prepare_only:
        marker = output / "NOT_RELEASE_READY.txt"
        marker.write_text(
            "Creator and license decisions remain pending. This directory is a packaging preview and must not be deposited.\n",
            encoding="utf-8", newline="\n"
        )
        outputs.append(marker)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--canonical-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--staging-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--creator", default="")
    parser.add_argument("--license", dest="license_id", default="")
    parser.add_argument("--publication-date", default="2026-09-01")
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()

    source = args.canonical_root.resolve()
    staging = args.staging_dir.resolve()
    output = args.output_dir.resolve()
    if source == staging or source in staging.parents or staging in source.parents:
        raise RuntimeError("staging must be outside the canonical tree")
    if output == source or source in output.parents or output in source.parents:
        raise RuntimeError("outer output must be outside the canonical tree")
    if not args.prepare_only and (not args.creator.strip() or not args.license_id.strip()):
        raise RuntimeError("final release requires nonempty --creator and --license")
    if staging.exists():
        shutil.rmtree(staging)
    if output.exists():
        shutil.rmtree(output)
    staging.mkdir(parents=True)

    source_before = inventory(source)
    source_before_digest = inventory_digest(source_before)
    copied, excluded = copy_public_subset(source, staging)
    source_after = inventory(source)
    source_after_digest = inventory_digest(source_after)
    if source_before_digest != source_after_digest:
        raise RuntimeError("canonical tree changed while staging was copied")

    generate_release_files(staging, args.creator.strip(), args.license_id.strip(), args.publication_date, args.prepare_only)
    conversation_audit = validate_complete_conversation_publication(staging)
    full_record_audit = validate_full_record_publication(staging)
    pdf_audit = validate_pdfs(staging)
    privacy = privacy_audit(staging)
    if not privacy["passed"]:
        report = output.parent / (output.name + "_privacy_failure.json")
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(json.dumps(privacy, indent=2) + "\n", encoding="utf-8")
        raise RuntimeError(f"privacy audit failed; see {report}")

    write_generated_metadata(staging, copied, excluded)
    # Re-audit generated text as part of the public boundary.
    privacy = privacy_audit(staging)
    if not privacy["passed"]:
        raise RuntimeError(f"privacy audit failed after metadata generation: {privacy['findings']}")

    zip_path = output.parent / (output.name + "_sources.zip")
    deterministic_zip(staging, zip_path)
    roundtrip = verify_zip(staging, zip_path)
    outer = copy_outer_files(staging, output, zip_path, args.prepare_only)
    receipt = {
        "schema": "s6-zenodo-release-build-receipt-v1",
        "builder_version": VERSION,
        "prepare_only": args.prepare_only,
        "release_ready": not args.prepare_only,
        "canonical_inventory_before_sha256": source_before_digest,
        "canonical_inventory_after_sha256": source_after_digest,
        "canonical_inventory_unchanged": True,
        "selected_source_files": len(copied),
        "excluded_source_files": len(excluded),
        "privacy_audit": privacy,
        "complete_conversation_audit": conversation_audit,
        "full_record_public_annex_audit": full_record_audit,
        "pdf_audit": pdf_audit,
        "roundtrip": roundtrip,
        "outer_inventory_scope": "Every uploaded file except this receipt and the self-excluded SHA256SUMS ledger; the final SHA256SUMS ledger covers the receipt.",
        "outer_files": [
            {"name": path.name, "bytes": path.stat().st_size, "sha256": digest_file(path)}
            for path in sorted(outer, key=lambda p: p.name)
        ],
    }
    receipt_path = output / "s6_peer_verification_v1.0_ROUNDTRIP_RECEIPT.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    # Refresh the outer checksum ledger after adding the receipt.
    outer_files = sorted((p for p in output.iterdir() if p.is_file() and p.name != "s6_peer_verification_v1.0_SHA256SUMS.txt"), key=lambda p: p.name)
    (output / "s6_peer_verification_v1.0_SHA256SUMS.txt").write_text(
        "\n".join(f"{digest_file(path)}  {path.name}" for path in outer_files) + "\n",
        encoding="utf-8", newline="\n"
    )
    print(json.dumps({
        "staging": str(staging),
        "outer": str(output),
        "prepare_only": args.prepare_only,
        "selected": len(copied),
        "excluded": len(excluded),
        "privacy_passed": privacy["passed"],
        "zip_sha256": roundtrip["zip_sha256"],
        "zip_entries": roundtrip["entries"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
