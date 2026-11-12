#!/usr/bin/env python3
"""Independent validation harness for koide_fast_enum.py.

The checks deliberately use several different routes:

* a literal exact (n,a) scan through a bounded height;
* SymPy's public generalized-Pell implementation for a bounded n range;
* the canonical NumPy proposal/recheck implementation through height 200000;
* the released JSON checkpoints and first-root list.

This file does not modify any canonical artifact.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
import time
from dataclasses import asdict
from pathlib import Path
from typing import Iterable

from sympy.solvers.diophantine.diophantine import diop_DN

import koide_fast_enum as fast


WORKSPACE = Path(r"C:\Users\user\Documents\math")
CANONICAL_DIRECTORY = (
    WORKSPACE
    / "output"
    / "s6_consolidated_canonical_2026-08-26"
    / "supporting_materials"
    / "workbench"
    / "reproduction"
    / "t1_koide_exact"
)
CANONICAL_SCRIPT = CANONICAL_DIRECTORY / "verify_koide_narain_root_density.py"
CANONICAL_JSON = CANONICAL_DIRECTORY / "koide_verification_200000.json"
CANONICAL_TEX = (
    WORKSPACE
    / "output"
    / "s6_consolidated_canonical_2026-08-26"
    / "supporting_materials"
    / "workbench"
    / "research"
    / "koide_counting_repair.tex"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def collect_fast(max_height: int) -> list[fast.Root]:
    roots: list[fast.Root] = []
    fast.enumerate_roots(max_height, roots.append)
    return roots


def literal_naive_scan(max_height: int) -> list[fast.Root]:
    """Exact O(X^2)-style reference, intentionally unlike the fast method."""

    roots: list[fast.Root] = []
    n = 0
    while 17 * n <= max_height:
        a_max = (max_height - 17 * n) // 4
        for a in range(1, a_max + 1):
            numerator = a * a - 18 * n * n + 2
            if numerator < 0 or numerator % 3:
                continue
            q_square = numerator // 3
            q = math.isqrt(q_square)
            if q * q != q_square or a + 4 * n <= q:
                continue
            roots.append(fast.validate_root(a, q, n, max_height))
        n += 1
    return sorted(roots)


def load_canonical_module():
    spec = importlib.util.spec_from_file_location("canonical_koide", CANONICAL_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(CANONICAL_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def canonicalize_sympy_representatives(N: int, pairs: Iterable[tuple[int, int]]) -> set[tuple[int, int]]:
    seeds: set[tuple[int, int]] = set()
    for a, q in pairs:
        q_abs = abs(int(q))
        signs = (q_abs,) if q_abs == 0 else (q_abs, -q_abs)
        for signed_q in signs:
            seeds.add(fast.canonical_positive_orbit_seed(N, int(a), signed_q))
    return seeds


def validate(max_literal_height: int, pell_n_max: int, canonical_height: int) -> dict[str, object]:
    canonical_hashes_before = {
        str(path): sha256_file(path) for path in (CANONICAL_SCRIPT, CANONICAL_JSON, CANONICAL_TEX)
    }
    started = time.perf_counter()

    literal_started = time.perf_counter()
    fast_literal = sorted(collect_fast(max_literal_height))
    naive_literal = literal_naive_scan(max_literal_height)
    if fast_literal != naive_literal:
        fast_set, naive_set = set(fast_literal), set(naive_literal)
        raise AssertionError(
            {
                "fast_only": [asdict(root) for root in sorted(fast_set - naive_set)[:20]],
                "naive_only": [asdict(root) for root in sorted(naive_set - fast_set)[:20]],
            }
        )
    literal_seconds = time.perf_counter() - literal_started

    pell_started = time.perf_counter()
    spf = fast.build_smallest_prime_factor(3 * pell_n_max + 1)
    pell_class_count = 0
    for n in range(1, pell_n_max + 1):
        N = 18 * n * n - 2
        factors = fast.factor_N(n, spf)
        custom = set(fast.canonical_unit_orbits(N, factors))
        sympy = canonicalize_sympy_representatives(N, diop_DN(3, N))
        if custom != sympy:
            raise AssertionError(
                {
                    "n": n,
                    "N": N,
                    "custom_only": sorted(custom - sympy),
                    "sympy_only": sorted(sympy - custom),
                }
            )
        pell_class_count += len(custom)
    pell_seconds = time.perf_counter() - pell_started

    canonical_started = time.perf_counter()
    canonical_module = load_canonical_module()
    canonical_roots = canonical_module.enumerate_reduced_roots(canonical_height)
    canonical_records = {
        fast.Root(z=r.z, x=r.x, y=r.y, a=r.a, q=r.q, n=r.n) for r in canonical_roots
    }
    independent_records = set(collect_fast(canonical_height))
    if len(independent_records) != len(canonical_roots):
        raise AssertionError((len(independent_records), len(canonical_roots)))
    if independent_records != canonical_records:
        raise AssertionError(
            {
                "fast_only": [asdict(root) for root in sorted(independent_records - canonical_records)[:20]],
                "canonical_only": [asdict(root) for root in sorted(canonical_records - independent_records)[:20]],
            }
        )
    canonical_seconds = time.perf_counter() - canonical_started

    released = json.loads(CANONICAL_JSON.read_text(encoding="utf-8"))
    independent_sorted = sorted(independent_records)
    heights = sorted(root.z for root in independent_sorted)
    checkpoint_comparisons: dict[str, dict[str, int | bool]] = {}
    for checkpoint_text, expected in released["counts"].items():
        checkpoint = int(checkpoint_text)
        if checkpoint > canonical_height:
            continue
        actual = sum(height <= checkpoint for height in heights)
        checkpoint_comparisons[checkpoint_text] = {
            "expected": int(expected),
            "actual": actual,
            "equal": actual == int(expected),
        }
        if actual != int(expected):
            raise AssertionError((checkpoint, actual, expected))

    first_expected = [tuple(values) for values in released["first_roots"]]
    first_actual = [(root.x, root.y, root.z) for root in independent_sorted[: len(first_expected)]]
    if first_actual != first_expected:
        raise AssertionError((first_actual, first_expected))

    # An independently stated polynomial-identity audit on every point in the
    # full canonical comparison range.
    for root in independent_records:
        lhs = 2 * fast.defect(root.x, root.y, root.z)
        rhs = fast.ternary_form(root.a, root.q, root.n)
        if lhs != rhs or lhs != -2:
            raise AssertionError((root, lhs, rhs))
        if fast.forward_coordinates(root.x, root.y, root.z) != (root.a, root.q, root.n):
            raise AssertionError(root)
        if fast.inverse_coordinates(root.a, root.q, root.n) != (root.x, root.y, root.z):
            raise AssertionError(root)

    canonical_hashes_after = {
        str(path): sha256_file(path) for path in (CANONICAL_SCRIPT, CANONICAL_JSON, CANONICAL_TEX)
    }
    if canonical_hashes_before != canonical_hashes_after:
        raise AssertionError("a canonical input changed during read-only validation")

    return {
        "schema_version": 1,
        "status": "PASS",
        "all_arithmetic_candidate_checks_exact_integer": True,
        "literal_scan": {
            "max_height": max_literal_height,
            "count": len(naive_literal),
            "fast_point_set_equals_literal_point_set": True,
            "seconds": literal_seconds,
        },
        "sympy_generalized_pell_crosscheck": {
            "n_range": [1, pell_n_max],
            "canonical_unit_orbits_compared": pell_class_count,
            "all_orbit_seed_sets_equal": True,
            "seconds": pell_seconds,
        },
        "canonical_full_point_set_crosscheck": {
            "max_height": canonical_height,
            "count": len(canonical_records),
            "all_six_coordinates_equal_as_sets": True,
            "all_original_polynomial_rechecks_pass": True,
            "seconds": canonical_seconds,
        },
        "released_checkpoint_comparisons": checkpoint_comparisons,
        "released_first_roots_equal": True,
        "canonical_read_only_hashes_before": canonical_hashes_before,
        "canonical_read_only_hashes_after": canonical_hashes_after,
        "canonical_inputs_unchanged": True,
        "total_seconds": time.perf_counter() - started,
        "runtime": {"python": sys.version},
        "fast_source_sha256": sha256_file(Path(fast.__file__).resolve()),
        "validation_source_sha256": sha256_file(Path(__file__).resolve()),
    }


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--literal-height", type=int, default=20_000)
    parser.add_argument("--pell-n-max", type=int, default=1_000)
    parser.add_argument("--canonical-height", type=int, default=200_000)
    parser.add_argument(
        "--receipt",
        type=Path,
        default=Path(__file__).resolve().parent / "validation_receipt.json",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    payload = validate(args.literal_height, args.pell_n_max, args.canonical_height)
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": payload["status"],
                "receipt": str(args.receipt.resolve()),
                "receipt_sha256": sha256_file(args.receipt),
                "total_seconds": payload["total_seconds"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
