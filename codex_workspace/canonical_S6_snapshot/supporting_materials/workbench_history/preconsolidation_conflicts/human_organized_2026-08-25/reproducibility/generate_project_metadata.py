#!/usr/bin/env python3
"""Regenerate the human tree, machine manifest, and SHA-256 ledger."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
METADATA = ROOT / "supporting_materials" / "metadata"
TREE = METADATA / "FILE_TREE.txt"
MANIFEST = METADATA / "PROJECT_MANIFEST.json"
CHECKSUMS = METADATA / "SHA256SUMS.txt"

GENERATED = {TREE, MANIFEST, CHECKSUMS}


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def all_files() -> list[Path]:
    priority = {"main.tex": 0, "original_clean_transcription.tex": 1, "README.md": 2}
    files = (
        p
        for p in ROOT.rglob("*")
        if p.is_file() and "$out" not in p.relative_to(ROOT).parts
    )
    return sorted(files, key=lambda p: (priority.get(relative(p), 3), relative(p)))


def write_tree(files: list[Path]) -> None:
    lines = [
        "S6 annotated proof-audit public tree",
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
        "schema_version": 2,
        "release_date": "2026-08-25",
        "project": "S6 annotated mathematical proof audit - public Overleaf edition",
        "root_documents": {
            "annotated": "main.tex",
            "raw_transcription": "original_clean_transcription.tex",
        },
        "expected_pages": {"annotated": 123, "raw_transcription": 108},
        "project_file_count_including_generated_metadata": len(files),
        "payload_entry_count": len(entries),
        "payload_total_bytes": sum(entry["bytes"] for entry in entries),
        "generated_metadata_excluded_from_entries": sorted(relative(path) for path in GENERATED),
        "entries": entries,
    }
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
