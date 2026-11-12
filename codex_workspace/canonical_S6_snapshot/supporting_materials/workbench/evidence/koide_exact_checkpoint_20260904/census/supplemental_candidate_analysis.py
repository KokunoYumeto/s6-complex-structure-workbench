#!/usr/bin/env python3
"""Reanalyse a coordinate census with a finer grid of stated sqrt constants."""

from __future__ import annotations

import argparse
import csv
import gzip
import json
from array import array
from fractions import Fraction
from pathlib import Path

import koide_fast_enum as fast


FINE_CANDIDATES = (
    Fraction(4, 25),       # 0.160
    Fraction(17, 100),     # 0.170
    Fraction(171, 1000),   # 0.171
    Fraction(43, 250),     # 0.172
    Fraction(7, 40),       # 0.175
    Fraction(9, 50),       # 0.180
    Fraction(37, 200),     # 0.185
    Fraction(19, 100),     # 0.190
    Fraction(1, 5),        # 0.200
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("coordinate_file", type=Path)
    parser.add_argument("result_file", type=Path)
    parser.add_argument("output_file", type=Path)
    args = parser.parse_args()
    source_result = json.loads(args.result_file.read_text(encoding="utf-8"))
    heights = array("Q")
    with gzip.open(args.coordinate_file, "rt", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            heights.append(int(row["z"]))
    if len(heights) != int(source_result["count"]):
        raise AssertionError((len(heights), source_result["count"]))
    fast.sort_heights_in_place(heights)
    c_lower, c_upper, c_mid = fast.constant_interval()
    max_height = int(source_result["max_height"])
    analyses = {
        "all_tested_integers": fast.analyze_domain(
            heights, 1, max_height, c_lower, c_upper, c_mid, FINE_CANDIDATES
        ),
        "tail_from_10000": fast.analyze_domain(
            heights, 10_000, max_height, c_lower, c_upper, c_mid, FINE_CANDIDATES
        ),
    }
    # Avoid duplicating the long sign-run arrays already present in the main
    # result.  This supplement is only the finer candidate-constant audit.
    for analysis in analyses.values():
        analysis.pop("sign_runs")
    payload = {
        "schema_version": 1,
        "status": "PASS",
        "source_result": str(args.result_file.resolve()),
        "source_result_sha256": fast.sha256_file(args.result_file),
        "coordinate_file": str(args.coordinate_file.resolve()),
        "coordinate_file_sha256": fast.sha256_file(args.coordinate_file),
        "count": len(heights),
        "max_height": max_height,
        "candidate_constants": [f"{c.numerator}/{c.denominator}" for c in FINE_CANDIDATES],
        "analyses": analyses,
        "script_sha256": fast.sha256_file(Path(__file__).resolve()),
    }
    args.output_file.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "PASS",
                "output_file": str(args.output_file.resolve()),
                "output_sha256": fast.sha256_file(args.output_file),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
