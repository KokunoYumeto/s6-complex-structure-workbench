#!/usr/bin/env python3
"""Static verification for the canonical LaTeX source tree."""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

START_RE = re.compile(r"%\s*=+\s*SOURCE PDF PAGE (\d{3}) START\s*=+")
END_RE = re.compile(r"%\s*=+\s*SOURCE PDF PAGE (\d{3}) END\s*=+")
ANCHOR_RE = re.compile(r"(?:\\srcpage\{|\\hypertarget\{s6-source-page-)(\d{3})")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER|SCAFFOLD|OMITTED|UNRESOLVED)\b|\?\?\?", re.IGNORECASE)
EXTERNAL_RE = re.compile(r"\\(?:input|include|includegraphics)\b")


def duplicate_values(values: list[int]) -> list[int]:
    return sorted(value for value, count in Counter(values).items() if count > 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json-output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()

    part_paths = sorted((root / "parts").glob("packet_*_body.tex"))
    if len(part_paths) != 10:
        raise SystemExit(f"expected 10 packet body files, found {len(part_paths)}")
    combined = "\n".join(path.read_text(encoding="utf-8") for path in part_paths)
    starts = [int(x) for x in START_RE.findall(combined)]
    ends = [int(x) for x in END_RE.findall(combined)]
    anchors = [int(x) for x in ANCHOR_RE.findall(combined)]
    expected = list(range(1, 109))

    full_path = root / "s6_canonical_full.tex"
    full = full_path.read_text(encoding="utf-8")
    placeholder_hits = [m.group(0) for m in PLACEHOLDER_RE.finditer(combined)]
    external_hits = [m.group(0) for m in EXTERNAL_RE.finditer(full)]

    report = {
        "packet_body_file_count": len(part_paths),
        "start_marker_count": len(starts),
        "end_marker_count": len(ends),
        "anchor_count": len(anchors),
        "start_markers_exact_1_to_108": starts == expected,
        "end_markers_exact_1_to_108": ends == expected,
        "anchors_exact_1_to_108": anchors == expected,
        "start_duplicates": duplicate_values(starts),
        "end_duplicates": duplicate_values(ends),
        "anchor_duplicates": duplicate_values(anchors),
        "missing_starts": sorted(set(expected) - set(starts)),
        "missing_ends": sorted(set(expected) - set(ends)),
        "missing_anchors": sorted(set(expected) - set(anchors)),
        "placeholder_hits": placeholder_hits,
        "monolithic_external_input_hits": external_hits,
    }
    ok = (
        starts == expected
        and ends == expected
        and anchors == expected
        and not placeholder_hits
        and not external_hits
    )
    report["ok"] = ok

    rendered = json.dumps(report, indent=2) + "\n"
    if args.json_output:
        target = args.json_output if args.json_output.is_absolute() else root / args.json_output
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
