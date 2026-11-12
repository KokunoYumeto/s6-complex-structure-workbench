#!/usr/bin/env python3
"""Inline the live annotation input into the archival one-file edition."""

from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
MAIN = PROJECT_ROOT / "main.tex"
OUTPUT = (
    PROJECT_ROOT
    / "supporting_materials"
    / "manuscript_sources"
    / "s6_canonical_annotated_standalone.tex"
)

INPUTS = (
    "supporting_materials/audit_annotation_sources/corrective_results_addendum.tex",
)


def inline_input(source: str, relative_path: str) -> str:
    marker = rf"\input{{{relative_path}}}"
    if source.count(marker) != 1:
        raise RuntimeError(f"expected exactly one {marker!r} in main.tex")
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
