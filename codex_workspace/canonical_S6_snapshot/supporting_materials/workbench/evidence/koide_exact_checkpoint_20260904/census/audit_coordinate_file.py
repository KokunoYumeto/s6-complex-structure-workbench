#!/usr/bin/env python3
"""Stream-audit a produced Koide coordinate CSV.gz with bounded memory."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import time
from collections import Counter
from pathlib import Path

import koide_fast_enum as fast


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def audit(coordinate_path: Path, result_path: Path) -> dict[str, object]:
    result = json.loads(result_path.read_text(encoding="utf-8"))
    max_height = int(result["max_height"])
    checkpoints = sorted(int(row["X"]) for row in result["checkpoints"])
    expected_counts = {int(row["X"]): int(row["R"]) for row in result["checkpoints"]}
    actual_counts = {checkpoint: 0 for checkpoint in checkpoints}
    row_digest = hashlib.sha256()
    rows = 0
    previous_n = -1
    seen_at_current_n: set[tuple[int, int]] = set()
    n_group_maximum_size = 0
    n_group_maximum_at = None
    current_n_rows = 0
    sampled_first: list[dict[str, int]] = []
    sampled_last: list[dict[str, int]] = []
    started = time.perf_counter()

    with gzip.open(coordinate_path, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        expected_fields = ["enumeration_index", "z", "x", "y", "a", "q", "n"]
        if reader.fieldnames != expected_fields:
            raise AssertionError((reader.fieldnames, expected_fields))
        for source in reader:
            row = {key: int(value) for key, value in source.items()}
            rows += 1
            if row["enumeration_index"] != rows:
                raise AssertionError(("enumeration index", rows, row))
            z, x, y, a, q, n = (row[key] for key in ("z", "x", "y", "a", "q", "n"))
            row_digest.update(f"{z},{x},{y},{a},{q},{n}\n".encode())
            if n < previous_n:
                raise AssertionError(("n order", previous_n, n, rows))
            if n != previous_n:
                if current_n_rows > n_group_maximum_size:
                    n_group_maximum_size = current_n_rows
                    n_group_maximum_at = previous_n
                seen_at_current_n.clear()
                current_n_rows = 0
                previous_n = n
            pair = (a, q)
            if pair in seen_at_current_n:
                raise AssertionError(("duplicate ternary point", a, q, n))
            seen_at_current_n.add(pair)
            current_n_rows += 1
            checked = fast.validate_root(a, q, n, max_height)
            if checked != fast.Root(z=z, x=x, y=y, a=a, q=q, n=n):
                raise AssertionError((checked, row))
            for checkpoint in checkpoints:
                if z <= checkpoint:
                    actual_counts[checkpoint] += 1
            if len(sampled_first) < 20:
                sampled_first.append(row)
            sampled_last.append(row)
            if len(sampled_last) > 20:
                sampled_last.pop(0)

    if current_n_rows > n_group_maximum_size:
        n_group_maximum_size = current_n_rows
        n_group_maximum_at = previous_n
    if rows != int(result["count"]):
        raise AssertionError(("row count", rows, result["count"]))
    if actual_counts != expected_counts:
        raise AssertionError(("checkpoint counts", actual_counts, expected_counts))
    if row_digest.hexdigest() != result["coordinate_stream_sha256_uncompressed_data_rows"]:
        raise AssertionError(("row digest", row_digest.hexdigest()))
    compressed_digest = sha256_file(coordinate_path)
    if compressed_digest != result["coordinate_file_sha256"]:
        raise AssertionError(("compressed digest", compressed_digest))

    return {
        "schema_version": 1,
        "status": "PASS",
        "coordinate_file": str(coordinate_path.resolve()),
        "coordinate_file_sha256": compressed_digest,
        "result_file": str(result_path.resolve()),
        "result_file_sha256": sha256_file(result_path),
        "rows": rows,
        "max_height": max_height,
        "all_rows_rechecked_in_ternary_and_original_coordinates": True,
        "no_duplicate_a_q_within_any_n_group": True,
        "n_groups_monotone": True,
        "largest_emitted_n_group_size": n_group_maximum_size,
        "largest_emitted_n_group_at_n": n_group_maximum_at,
        "checkpoint_counts": {str(key): actual_counts[key] for key in checkpoints},
        "uncompressed_data_row_sha256": row_digest.hexdigest(),
        "first_20_rows_in_enumeration_order": sampled_first,
        "last_20_rows_in_enumeration_order": sampled_last,
        "seconds": time.perf_counter() - started,
        "audit_source_sha256": sha256_file(Path(__file__).resolve()),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("coordinate_file", type=Path)
    parser.add_argument("result_file", type=Path)
    parser.add_argument("receipt", type=Path)
    args = parser.parse_args()
    payload = audit(args.coordinate_file, args.result_file)
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": payload["status"],
                "rows": payload["rows"],
                "seconds": payload["seconds"],
                "receipt": str(args.receipt.resolve()),
                "receipt_sha256": sha256_file(args.receipt),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
