#!/usr/bin/env python3
"""Build and round-trip-verify the canonical deterministic release ZIP.

The default source root is derived from this script's location.  ``--check-only``
performs every source-tree, metadata, and reference-PDF check without writing an
archive, sidecar, receipt, or temporary extraction.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
import platform
import re
import shutil
import stat
import sys
import tempfile
import uuid
import zipfile
from pathlib import Path, PurePosixPath

from pypdf import PdfReader


DEFAULT_SOURCE = Path(__file__).resolve().parents[2]

GENERATED_METADATA = {
    "supporting_materials/metadata/FILE_TREE.txt",
    "supporting_materials/metadata/PROJECT_MANIFEST.json",
    "supporting_materials/metadata/SHA256SUMS.txt",
}

ROOT_ENTRIES = {
    "S6_CURRENT_FULL_TEX_FOR_AI.md",
    "S6_WORKBENCH_FULL_TEX_FOR_AI.md",
    "koide_arithmetic_preprint.pdf",
    "koide_arithmetic_preprint.tex",
    "main.tex",
    "original_clean_transcription.tex",
    "references.bib",
    "s6_compact_link_gaussian_preprint.pdf",
    "s6_compact_link_gaussian_preprint.tex",
    "s6_cone_sphere_routes_companion.bib",
    "s6_cone_sphere_routes_preprint.pdf",
    "s6_cone_sphere_routes_preprint.tex",
    "s6_erdos_straus_koide_bridge_preprint.pdf",
    "s6_erdos_straus_koide_bridge_preprint.tex",
    "s6_higher_rung_su3_gram_cone_preprint.pdf",
    "s6_higher_rung_su3_gram_cone_preprint.tex",
    "s6_spectral_degeneration_preprint.pdf",
    "s6_spectral_degeneration_preprint.tex",
    "s6_worldline_presymplectic_reduction_preprint.pdf",
    "s6_worldline_presymplectic_reduction_preprint.tex",
    "workbench.pdf",
    "workbench.tex",
    "workbench_and_manuscript_overview.pdf",
    "workbench_and_manuscript_overview.tex",
    "supporting_materials",
}

ROOT_DOCUMENTS = {
    "annotated": "main.tex",
    "raw_transcription": "original_clean_transcription.tex",
    "workbench": "workbench.tex",
    "mathematical_overview": "workbench_and_manuscript_overview.tex",
    "koide_arithmetic_draft": "koide_arithmetic_preprint.tex",
    "spectral_degeneration_draft": "s6_spectral_degeneration_preprint.tex",
    "compact_link_gaussian_draft": "s6_compact_link_gaussian_preprint.tex",
    "cone_sphere_routes_draft": "s6_cone_sphere_routes_preprint.tex",
    "erdos_straus_koide_bridge_draft": "s6_erdos_straus_koide_bridge_preprint.tex",
    "higher_rung_su3_gram_cone_draft": "s6_higher_rung_su3_gram_cone_preprint.tex",
    "worldline_presymplectic_reduction_draft": "s6_worldline_presymplectic_reduction_preprint.tex",
    "publication_monograph": "supporting_materials/publication/s6_peer_verification_monograph.tex",
}

EXPECTED_PAGES = {
    "annotated": 129,
    "raw_transcription": 108,
    "workbench": 449,
    "mathematical_overview": 21,
    "koide_arithmetic_draft": 18,
    "spectral_degeneration_draft": 87,
    "compact_link_gaussian_draft": 28,
    "cone_sphere_routes_draft": 46,
    "erdos_straus_koide_bridge_draft": 12,
    "higher_rung_su3_gram_cone_draft": 17,
    "worldline_presymplectic_reduction_draft": 14,
    "publication_monograph": 471,
}

PDF_EXPECTATIONS = {
    "supporting_materials/reference_pdfs/s6_canonical_annotated_peer_review.pdf": 129,
    "supporting_materials/reference_pdfs/s6_canonical_clean.pdf": 108,
    "supporting_materials/reference_pdfs/s6_validate_repair_disprove_workbench.pdf": 449,
    "supporting_materials/reference_pdfs/s6_mathematical_overview.pdf": 21,
    "supporting_materials/reference_pdfs/s6_peer_verification_monograph.pdf": 471,
}

LETTER = (612.0, 792.0)
CHECKSUM_PATTERN = re.compile(r"^([0-9a-f]{64})  (.+)$")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def unsafe_name(name: str) -> bool:
    if not name or "\x00" in name or "\\" in name:
        return True
    if name.startswith(("/", "//")) or re.match(r"^[A-Za-z]:", name):
        return True
    parts = PurePosixPath(name).parts
    return any(part in {"", ".", ".."} for part in parts)


def validate_source_tree(root: Path) -> dict[str, int | bool]:
    if not root.is_dir():
        raise RuntimeError(f"source root is not a directory: {root}")

    actual_root = {path.name for path in root.iterdir()}
    if actual_root != ROOT_ENTRIES:
        difference = sorted(actual_root ^ ROOT_ENTRIES)
        raise RuntimeError(f"unexpected canonical-root entries: {difference}")

    names: list[str] = []
    symlinks: list[str] = []
    unsafe: list[str] = []
    for path in root.rglob("*"):
        name = relative(root, path)
        if unsafe_name(name):
            unsafe.append(name)
        if path.is_symlink():
            symlinks.append(name)
        if path.is_file():
            names.append(name)

    counts = Counter(names)
    duplicates = sorted(name for name, count in counts.items() if count > 1)
    folded: dict[str, list[str]] = {}
    for name in names:
        folded.setdefault(name.casefold(), []).append(name)
    casefold_duplicates = sorted(group for group in folded.values() if len(group) > 1)

    if unsafe or symlinks or duplicates or casefold_duplicates:
        raise RuntimeError(
            "unsafe source tree: "
            f"unsafe={unsafe}, symlinks={symlinks}, duplicates={duplicates}, "
            f"casefold={casefold_duplicates}"
        )

    return {
        "files": len(names),
        "unsafe_paths": 0,
        "symlinks": 0,
        "duplicates": 0,
        "casefold_duplicates": 0,
        "root_layout_valid": True,
    }


def inventory(root: Path) -> list[dict[str, object]]:
    paths = sorted(
        (path for path in root.rglob("*") if path.is_file()),
        key=lambda path: relative(root, path),
    )
    return [
        {
            "path": relative(root, path),
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in paths
    ]


def inventory_digest(rows: list[dict[str, object]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update(str(row["path"]).encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(row["bytes"]).encode("ascii"))
        digest.update(b"\0")
        digest.update(str(row["sha256"]).encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def source_path(root: Path, posix_name: str) -> Path:
    return root.joinpath(*PurePosixPath(posix_name).parts)


def make_zip(root: Path, rows: list[dict[str, object]], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        destination,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        strict_timestamps=True,
    ) as archive:
        archive.comment = b""
        for row in rows:
            name = str(row["path"])
            data = source_path(root, name).read_bytes()
            if len(data) != row["bytes"] or sha256_bytes(data) != row["sha256"]:
                raise RuntimeError(f"source changed during packaging: {name}")

            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.internal_attr = 0
            info.extra = b""
            info.comment = b""
            archive.writestr(
                info,
                data,
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )


def inspect_and_extract(archive_path: Path, destination: Path) -> dict[str, object]:
    destination.mkdir(parents=True, exist_ok=False)
    unsafe: list[str] = []
    symlinks: list[str] = []
    metadata_errors: list[str] = []
    names: list[str] = []

    with zipfile.ZipFile(archive_path, "r") as archive:
        if archive.comment:
            metadata_errors.append("archive-comment")
        infos = archive.infolist()
        for info in infos:
            name = info.filename
            names.append(name)
            if unsafe_name(name) or info.is_dir():
                unsafe.append(name)
            mode = (info.external_attr >> 16) & 0xFFFF
            if stat.S_ISLNK(mode):
                symlinks.append(name)
            if info.date_time != (1980, 1, 1, 0, 0, 0):
                metadata_errors.append(f"timestamp:{name}")
            if mode != (stat.S_IFREG | 0o644):
                metadata_errors.append(f"mode:{name}")
            if info.compress_type != zipfile.ZIP_DEFLATED:
                metadata_errors.append(f"compression:{name}")
            if info.extra or info.comment:
                metadata_errors.append(f"extra-or-comment:{name}")

        counts = Counter(names)
        duplicates = sorted(name for name, count in counts.items() if count > 1)
        folded: dict[str, list[str]] = {}
        for name in names:
            folded.setdefault(name.casefold(), []).append(name)
        casefold_duplicates = sorted(group for group in folded.values() if len(group) > 1)

        if names != sorted(names):
            metadata_errors.append("entry-order")

        if unsafe or symlinks or duplicates or casefold_duplicates or metadata_errors:
            raise RuntimeError(
                "unsafe archive: "
                f"unsafe={unsafe}, symlinks={symlinks}, duplicates={duplicates}, "
                f"casefold={casefold_duplicates}, metadata={metadata_errors}"
            )

        for info in infos:
            data = archive.read(info)  # Reading every member verifies its CRC.
            target = destination.joinpath(*PurePosixPath(info.filename).parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)

    return {
        "entries": len(names),
        "unsafe_paths": 0,
        "symlinks": 0,
        "duplicates": 0,
        "casefold_duplicates": 0,
        "crc_read_complete": True,
        "deterministic_metadata_valid": True,
    }


def validate_checksum_ledger(
    root: Path, rows: list[dict[str, object]]
) -> dict[str, object]:
    actual = {str(row["path"]): row for row in rows}
    ledger_path = root / "supporting_materials" / "metadata" / "SHA256SUMS.txt"
    parsed: dict[str, str] = {}
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        match = CHECKSUM_PATTERN.fullmatch(line)
        if not match:
            raise RuntimeError(f"malformed checksum row: {line!r}")
        digest, name = match.groups()
        if name in parsed:
            raise RuntimeError(f"duplicate checksum row: {name}")
        parsed[name] = digest

    expected = set(actual) - {"supporting_materials/metadata/SHA256SUMS.txt"}
    if set(parsed) != expected:
        missing = sorted(expected - set(parsed))
        extra = sorted(set(parsed) - expected)
        raise RuntimeError(f"checksum path set mismatch: missing={missing}, extra={extra}")

    mismatches = [name for name, digest in parsed.items() if actual[name]["sha256"] != digest]
    if mismatches:
        raise RuntimeError(f"checksum mismatches: {mismatches}")

    return {"rows": len(parsed), "valid": len(parsed), "mismatches": 0}


def validate_manifest(
    root: Path, rows: list[dict[str, object]]
) -> tuple[dict[str, object], dict[str, object]]:
    actual = {str(row["path"]): row for row in rows}
    manifest_path = root / "supporting_materials" / "metadata" / "PROJECT_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = manifest["entries"]
    expected = set(actual) - GENERATED_METADATA
    listed_paths = [entry["path"] for entry in entries]
    entry_paths = set(listed_paths)
    if len(entry_paths) != len(listed_paths):
        duplicates = sorted(
            name for name, count in Counter(listed_paths).items() if count > 1
        )
        raise RuntimeError(f"duplicate manifest paths: {duplicates}")
    if entry_paths != expected:
        missing = sorted(expected - entry_paths)
        extra = sorted(entry_paths - expected)
        raise RuntimeError(f"manifest path set mismatch: missing={missing}, extra={extra}")

    mismatches = []
    for entry in entries:
        current = actual[entry["path"]]
        if entry["bytes"] != current["bytes"] or entry["sha256"] != current["sha256"]:
            mismatches.append(entry["path"])
    if mismatches:
        raise RuntimeError(f"manifest mismatches: {mismatches}")

    if manifest.get("root_documents") != ROOT_DOCUMENTS:
        raise RuntimeError(f"manifest root documents mismatch: {manifest.get('root_documents')}")
    if manifest.get("expected_pages") != EXPECTED_PAGES:
        raise RuntimeError(f"manifest page expectations mismatch: {manifest.get('expected_pages')}")
    if set(manifest.get("generated_metadata_excluded_from_entries", [])) != GENERATED_METADATA:
        raise RuntimeError("manifest generated-metadata exclusion policy mismatch")
    if manifest["project_file_count_including_generated_metadata"] != len(rows):
        raise RuntimeError("manifest project file count mismatch")
    if manifest["payload_entry_count"] != len(entries):
        raise RuntimeError("manifest payload count mismatch")
    if manifest["payload_total_bytes"] != sum(int(entry["bytes"]) for entry in entries):
        raise RuntimeError("manifest payload-byte total mismatch")

    result = {"entries": len(entries), "valid": len(entries), "mismatches": 0}
    return result, manifest


def validate_tree_file(root: Path, rows: list[dict[str, object]]) -> dict[str, object]:
    tree_path = root / "supporting_materials" / "metadata" / "FILE_TREE.txt"
    lines = tree_path.read_text(encoding="utf-8").splitlines()
    if len(lines) < 3 or lines[1] != f"Files: {len(rows)}" or lines[2] != "":
        raise RuntimeError("FILE_TREE header mismatch")
    expected = [str(row["path"]) for row in rows]
    if lines[3:] != expected:
        raise RuntimeError("FILE_TREE path set/order mismatch")
    return {"entries": len(expected), "valid": len(expected), "mismatches": 0}


def validate_pdfs(
    root: Path, rows: list[dict[str, object]]
) -> dict[str, dict[str, object]]:
    actual = {str(row["path"]): row for row in rows}
    result: dict[str, dict[str, object]] = {}
    for name, expected_pages in PDF_EXPECTATIONS.items():
        if name not in actual:
            raise RuntimeError(f"reference PDF is absent from inventory: {name}")
        path = source_path(root, name)
        reader = PdfReader(path)
        pages = len(reader.pages)
        if pages != expected_pages:
            raise RuntimeError(f"PDF page mismatch for {name}: {pages} != {expected_pages}")
        for index, page in enumerate(reader.pages, start=1):
            width = float(page.mediabox.width)
            height = float(page.mediabox.height)
            if abs(width - LETTER[0]) > 0.1 or abs(height - LETTER[1]) > 0.1:
                raise RuntimeError(f"non-letter page {name}:{index}: {width}x{height}")
        result[name] = {
            "pages": pages,
            "bytes": actual[name]["bytes"],
            "sha256": actual[name]["sha256"],
            "all_pages_us_letter": True,
        }
    return result


def validate_release_state(
    root: Path,
) -> tuple[
    list[dict[str, object]],
    dict[str, int | bool],
    dict[str, object],
    dict[str, object],
    dict[str, object],
    dict[str, dict[str, object]],
    dict[str, object],
]:
    source_safety = validate_source_tree(root)
    rows = inventory(root)
    if source_safety["files"] != len(rows):
        raise RuntimeError("source-tree inventory count changed during validation")
    checksum_result = validate_checksum_ledger(root, rows)
    manifest_result, manifest = validate_manifest(root, rows)
    tree_result = validate_tree_file(root, rows)
    pdf_result = validate_pdfs(root, rows)
    return (
        rows,
        source_safety,
        checksum_result,
        manifest_result,
        tree_result,
        pdf_result,
        manifest,
    )


def atomic_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".building-" + uuid.uuid4().hex)
    temporary.write_text(content, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def assert_outside_source(root: Path, path: Path, label: str) -> None:
    resolved_root = root.resolve()
    resolved_path = path.resolve(strict=False)
    try:
        resolved_path.relative_to(resolved_root)
    except ValueError:
        return
    raise RuntimeError(f"{label} must be outside the canonical source tree")


def parse_args() -> argparse.Namespace:
    default_archive = DEFAULT_SOURCE.parent / f"{DEFAULT_SOURCE.name}.zip"
    parser = argparse.ArgumentParser(
        description=(
            "Create a sorted, fixed-timestamp deterministic ZIP; safely extract it; "
            "validate paths, hashes, metadata and reference PDFs; and require a "
            "byte-identical second pack."
        )
    )
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--archive", type=Path, default=default_archive)
    parser.add_argument("--sidecar", type=Path)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument(
        "--temp-parent",
        type=Path,
        help="Optional parent for the unique temporary round-trip directory.",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Validate the live tree, ledgers, manifest, file tree and PDFs without writing anything.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.source.resolve()
    archive = args.archive.resolve(strict=False)
    sidecar = (
        args.sidecar.resolve(strict=False)
        if args.sidecar
        else Path(str(archive) + ".sha256")
    )
    receipt = (
        args.receipt.resolve(strict=False)
        if args.receipt
        else archive.with_name(archive.stem + ".roundtrip.json")
    )

    for path, label in ((archive, "archive"), (sidecar, "sidecar"), (receipt, "receipt")):
        assert_outside_source(root, path, label)
    if len({archive, sidecar, receipt}) != 3:
        raise RuntimeError("archive, sidecar, and receipt paths must be distinct")
    if args.temp_parent:
        temp_parent = args.temp_parent.resolve(strict=False)
        assert_outside_source(root, temp_parent, "temporary parent")
    else:
        temp_parent = None

    (
        before,
        source_safety,
        checksum_result,
        manifest_result,
        tree_result,
        pdf_result,
        manifest,
    ) = validate_release_state(root)
    before_digest = inventory_digest(before)

    validation_summary = {
        "schema_version": 1,
        "mode": "check-only" if args.check_only else "package",
        "source_label": root.name,
        "source_files": len(before),
        "source_inventory_sha256": before_digest,
        "source_tree_safety": source_safety,
        "checksum_ledger": checksum_result,
        "project_manifest": manifest_result,
        "file_tree": tree_result,
        "reference_pdfs": pdf_result,
    }
    if args.check_only:
        print(json.dumps(validation_summary, indent=2, sort_keys=True))
        return 0

    if temp_parent:
        temp_parent.mkdir(parents=True, exist_ok=True)
    work = Path(
        tempfile.mkdtemp(
            prefix="s6_release_roundtrip_",
            dir=str(temp_parent) if temp_parent else None,
        )
    )
    first_zip = work / "first.zip"
    second_zip = work / "second.zip"
    extracted = work / "extracted"
    cleanup_complete = False

    try:
        make_zip(root, before, first_zip)
        after = inventory(root)
        if after != before:
            raise RuntimeError("source tree changed during packaging")

        archive_inspection = inspect_and_extract(first_zip, extracted)
        extracted_rows = inventory(extracted)
        if extracted_rows != before:
            raise RuntimeError("round-trip path, byte-count, or SHA-256 inventory mismatch")

        extracted_checksum = validate_checksum_ledger(extracted, extracted_rows)
        extracted_manifest, _ = validate_manifest(extracted, extracted_rows)
        extracted_tree = validate_tree_file(extracted, extracted_rows)
        extracted_pdfs = validate_pdfs(extracted, extracted_rows)

        make_zip(extracted, extracted_rows, second_zip)
        if first_zip.read_bytes() != second_zip.read_bytes():
            raise RuntimeError("deterministic repack is not byte-identical")

        archive_hash = sha256_file(first_zip)
        archive_bytes = first_zip.stat().st_size
        building_archive = archive.with_name(
            archive.name + ".building-" + uuid.uuid4().hex
        )
        archive.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(first_zip, building_archive)
        if sha256_file(building_archive) != archive_hash:
            raise RuntimeError("archive changed during final copy")
        os.replace(building_archive, archive)
    finally:
        shutil.rmtree(work)
        cleanup_complete = not work.exists()

    receipt_payload = {
        "schema_version": 2,
        "release_date": manifest.get("release_date"),
        "source_label": root.name,
        "archive_name": archive.name,
        "archive_bytes": archive_bytes,
        "archive_sha256": archive_hash,
        "source_files": len(before),
        "source_inventory_sha256": before_digest,
        "source_pre_post_identical": True,
        "source_tree_safety": source_safety,
        "archive_inspection": archive_inspection,
        "roundtrip_inventory": {
            "entries": len(extracted_rows),
            "valid": len(extracted_rows),
            "mismatches": 0,
        },
        "checksum_ledger": extracted_checksum,
        "project_manifest": extracted_manifest,
        "file_tree": extracted_tree,
        "reference_pdfs": extracted_pdfs,
        "deterministic_repack_byte_identical": True,
        "temporary_extraction_removed": cleanup_complete,
        "python": platform.python_version(),
        "zlib_runtime": (
            zipfile.zlib.ZLIB_RUNTIME_VERSION if zipfile.zlib is not None else None
        ),
    }
    atomic_text(sidecar, f"{archive_hash}  {archive.name}\n")
    atomic_text(receipt, json.dumps(receipt_payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(receipt_payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
