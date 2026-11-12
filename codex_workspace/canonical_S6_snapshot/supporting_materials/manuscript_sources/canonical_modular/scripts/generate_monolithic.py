#!/usr/bin/env python3
"""Expand the canonical modular LaTeX tree into one self-contained .tex file."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

INPUT_RE = re.compile(
    r"^[ \t]*\\input\{(parts/packet_(\d{2})_body\.tex)\}"
    r"[ \t]*(?:%[^\r\n]*)?$",
    re.MULTILINE,
)


def expand(root: Path, source_name: str, output_name: str) -> Path:
    source = root / source_name
    output = root / output_name
    text = source.read_text(encoding="utf-8")
    seen: list[int] = []

    def replace(match: re.Match[str]) -> str:
        rel = match.group(1)
        packet = int(match.group(2))
        seen.append(packet)
        body = (root / rel).read_text(encoding="utf-8").rstrip("\n") + "\n"

        # In the modular form, the endline after packet 07's \input contributes
        # one ordinary space token. Retain it so both forms emit identical bytes.
        boundary_token = "\\ \n" if packet == 7 else ""
        return (
            f"% ===== BEGIN INLINED {rel} =====\n"
            f"{body}"
            f"{boundary_token}"
            f"% ===== END INLINED {rel} ====="
        )

    expanded = INPUT_RE.sub(replace, text)
    expected = list(range(1, 11))
    if seen != expected:
        raise SystemExit(f"expected packet inputs {expected}, found {seen}")
    if re.search(r"\\(?:input|include|includegraphics)\b", expanded):
        raise SystemExit("monolithic source still contains an external-input command")

    # Keep the generated source byte-stable across Windows, Unix, and Overleaf.
    output.write_text(expanded, encoding="utf-8", newline="\n")
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--source", default="s6_canonical.tex")
    parser.add_argument("--output", default="s6_canonical_full.tex")
    args = parser.parse_args()
    path = expand(args.root.resolve(), args.source, args.output)
    print(path)


if __name__ == "__main__":
    main()
