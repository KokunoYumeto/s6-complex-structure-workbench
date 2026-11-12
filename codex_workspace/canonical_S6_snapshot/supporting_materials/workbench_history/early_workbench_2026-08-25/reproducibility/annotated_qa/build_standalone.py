#!/usr/bin/env python3
"""Inline the three annotation inputs into the archival one-file edition."""

from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
MAIN = PROJECT_ROOT / "annotated_audit.tex"
OUTPUT = PROJECT_ROOT / "manuscript" / "s6_canonical_annotated_standalone.tex"

INPUTS = (
    "annotations/audit_annotation_layer.tex",
    "annotations/reader_guide.tex",
    "annotations/audit_annotations_appendix.tex",
)


def inline_input(source: str, relative_path: str) -> str:
    marker = rf"\input{{{relative_path}}}"
    if source.count(marker) != 1:
        raise RuntimeError(f"expected exactly one {marker!r} in annotated_audit.tex")
    payload = (PROJECT_ROOT / relative_path).read_text(encoding="utf-8")
    block = (
        f"% ===== BEGIN INLINED {relative_path} =====\n"
        f"{payload.rstrip()}\n"
        f"% ===== END INLINED {relative_path} ====="
    )
    return source.replace(marker, block)


def main() -> int:
    source = MAIN.read_text(encoding="utf-8")
    for relative_path in INPUTS:
        source = inline_input(source, relative_path)
    OUTPUT.write_text(source, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
