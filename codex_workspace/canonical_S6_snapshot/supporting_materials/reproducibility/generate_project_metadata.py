#!/usr/bin/env python3
"""Regenerate the human tree, machine manifest, and SHA-256 ledger."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import fitz


ROOT = Path(__file__).resolve().parents[2]
METADATA = ROOT / "supporting_materials" / "metadata"
TREE = METADATA / "FILE_TREE.txt"
MANIFEST = METADATA / "PROJECT_MANIFEST.json"
CHECKSUMS = METADATA / "SHA256SUMS.txt"

GENERATED = {TREE, MANIFEST, CHECKSUMS}

# TeX engines write these disposable files beside a root document.  They are
# intentionally absent from the Overleaf mirror and from release metadata;
# build logs and recorder files that form evidence are preserved separately
# below supporting_materials/build_artifacts.
ROOT_TRANSIENT_SUFFIXES = {
    ".aux",
    ".bbl",
    ".blg",
    ".fdb_latexmk",
    ".fls",
    ".log",
    ".out",
    ".toc",
    ".synctex.gz",
}


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def all_files() -> list[Path]:
    def retained(path: Path) -> bool:
        if not path.is_file():
            return False
        if '__pycache__' in path.parts or path.suffix == '.pyc':
            return False
        if path.parent != ROOT:
            return True
        return not any(path.name.endswith(suffix) for suffix in ROOT_TRANSIENT_SUFFIXES)

    return sorted((p for p in ROOT.rglob("*") if retained(p)), key=relative)


def write_tree(files: list[Path]) -> None:
    lines = [
        "S6 consolidated annotated proof-audit and mathematical workbench tree",
        f"Files: {len(files)}",
        "",
    ]
    lines.extend(relative(path) for path in files)
    TREE.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def write_manifest(files: list[Path]) -> None:
    payload = [path for path in files if path not in GENERATED]
    entries = [
        {
            "path": relative(path),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in payload
    ]
    record = {
        "schema_version": 3,
        "release_date": "2026-09-05",
        "inventory_scope": "Canonical source workspace inventory, not a new Zenodo publication or a claim that every cached PDF matches current TeX. Remote synchronization is recorded separately.",
        "project": "S6 annotated mathematical proof audit and validate/repair/disprove workbench",
        "root_documents": {
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
            "divisor_extension_draft": "s6_koide_es_divisor_extension_audit.tex",
            "quaternionic_draft": "s6_quaternionic_4441_reconciliation.tex",
            "homogeneous_quantum_draft": "s6_homogeneous_quantum_confinement.tex",
            "higher_torus_24d_draft": "s6_higher_rung_24d_preprint.tex",
        },
        "historical_expected_pages_2026_09_04": {
            "annotated": 129,
            "raw_transcription": 108,
            "workbench": 495,
            "mathematical_overview": 23,
            "koide_arithmetic_draft": 66,
            "spectral_degeneration_draft": 87,
            "compact_link_gaussian_draft": 28,
            "cone_sphere_routes_draft": 46,
            "erdos_straus_koide_bridge_draft": 12,
            "higher_rung_su3_gram_cone_draft": 17,
            "worldline_presymplectic_reduction_draft": 14,
            "publication_monograph": 520,
        },
        "project_file_count_including_generated_metadata": len(files),
        "payload_entry_count": len(entries),
        "payload_total_bytes": sum(entry["bytes"] for entry in entries),
        "generated_metadata_excluded_from_entries": sorted(relative(path) for path in GENERATED),
        "entries": entries,
        "current_verified_build_receipts": [
            "supporting_materials/workbench/evidence/finite_coupling_20260905/FINAL_BUILD_RECEIPT.json",
            "supporting_materials/workbench/evidence/retained_angle_20260905/FINAL_BUILD_RECEIPT.json",
        ],
    }
    record['cached_pdf_pages'] = {}
    for role, tex in record['root_documents'].items():
        pdf = (ROOT / tex).with_suffix('.pdf')
        if pdf.is_file():
            with fitz.open(pdf) as doc:
                record['cached_pdf_pages'][role] = {'pdf':relative(pdf), 'pages':len(doc),
                    'sha256':sha256(pdf), 'scope':'Measured cached PDF; use its dated build receipt for source correspondence.'}
    MANIFEST.write_text(
        json.dumps(record, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def write_checksums(files: list[Path]) -> None:
    lines = [
        f"{sha256(path)}  {relative(path)}"
        for path in files
        if path != CHECKSUMS
    ]
    CHECKSUMS.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    METADATA.mkdir(parents=True, exist_ok=True)
    files = all_files()
    write_tree(files)
    write_manifest(files)
    # Re-list after the first two writes so the checksum ledger sees their final bytes.
    files = all_files()
    write_checksums(files)
    print(f"files={len(files)} payload={len(files) - len(GENERATED)} checksums={len(files) - 1}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
