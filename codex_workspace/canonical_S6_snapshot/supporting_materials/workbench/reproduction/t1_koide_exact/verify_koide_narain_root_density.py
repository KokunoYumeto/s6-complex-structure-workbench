#!/usr/bin/env python3
"""Exact bounded enumeration for the reduced Koide--Narain root shell.

The script retains the original polynomial

    Delta(x,y,z) = 4(xy+xz+yz) - (x^2+y^2+z^2)

and checks Delta(x,y,z) = -1 for every reported root.  Enumeration is routed
through the exact integral coordinate bijection

    n = z - 4(x+y),  q = y-x,  a = x+y-4n,

whose inverse is

    x = (a+4n-q)/2,
    y = (a+4n+q)/2,
    z = 4a+17n.

In these coordinates the unchanged equation is equivalent, term by term, to

    a^2 - 3q^2 - 18n^2 = -2.

NumPy is used only to locate square candidates efficiently.  Every candidate
is then rechecked with Python integers in both coordinate systems.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction

import numpy as np


DEFAULT_CHECKPOINTS = (10_000, 20_000, 30_000, 40_000, 50_000, 75_000, 100_000)


def defect(x: int, y: int, z: int) -> int:
    return 4 * (x * y + x * z + y * z) - (x * x + y * y + z * z)


def ternary_form(a: int, q: int, n: int) -> int:
    return a * a - 3 * q * q - 18 * n * n


def forward_coordinates(x: int, y: int, z: int) -> tuple[int, int, int]:
    n = z - 4 * (x + y)
    q = y - x
    a = x + y - 4 * n
    return (a, q, n)


def inverse_coordinates(a: int, q: int, n: int) -> tuple[int, int, int]:
    x_numerator = a + 4 * n - q
    y_numerator = a + 4 * n + q
    if x_numerator % 2 or y_numerator % 2:
        raise AssertionError(("nonintegral inverse", a, q, n))
    return (x_numerator // 2, y_numerator // 2, 4 * a + 17 * n)


def local_congruence_count(prime: int, exponent: int) -> int:
    modulus = prime**exponent
    square_multiplicity = Counter((a * a) % modulus for a in range(modulus))
    total = 0
    for q in range(modulus):
        q_term = 3 * q * q
        for n in range(modulus):
            required_square = (-2 + q_term + 18 * n * n) % modulus
            total += square_multiplicity.get(required_square, 0)
    return total


def legendre_three(prime: int) -> int:
    residue = pow(3, (prime - 1) // 2, prime)
    if residue == 1:
        return 1
    if residue == prime - 1:
        return -1
    raise AssertionError(("prime divides three", prime))


def matmul(
    left: tuple[tuple[Fraction, ...], ...],
    right: tuple[tuple[Fraction, ...], ...],
) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(3)), Fraction(0))
            for j in range(3)
        )
        for i in range(3)
    )


def transpose(
    matrix: tuple[tuple[Fraction, ...], ...],
) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(tuple(matrix[j][i] for j in range(3)) for i in range(3))


def determinant_three(matrix: tuple[tuple[Fraction, ...], ...]) -> Fraction:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def two_adic_isometry_certificate() -> dict[str, object]:
    zero = Fraction(0)
    one = Fraction(1)
    quadratic_matrix = (
        (one, zero, zero),
        (zero, Fraction(-3), zero),
        (zero, zero, Fraction(-18)),
    )
    g = (
        (Fraction(-19, 17), zero, Fraction(-36, 17)),
        (zero, one, zero),
        (Fraction(-2, 17), zero, Fraction(-19, 17)),
    )
    preserved = matmul(matmul(transpose(g), quadratic_matrix), g)
    if preserved != quadratic_matrix:
        raise AssertionError(("two-adic matrix did not preserve F", preserved))
    determinant = determinant_three(g)
    if determinant != 1:
        raise AssertionError(("two-adic matrix determinant", determinant))
    # Voight (12.4.14): for odd u,w, (u,w)_2=(-1)^((u-1)(w-1)/4).
    hilbert_exponent = ((-17 - 1) * (3 - 1) // 4) % 2
    hilbert_symbol = -1 if hilbert_exponent else 1
    if hilbert_symbol != -1:
        raise AssertionError(("unexpected Hilbert symbol", hilbert_symbol))
    return {
        "matrix": [
            [f"{entry.numerator}/{entry.denominator}" for entry in row] for row in g
        ],
        "g_transpose_A_g_equals_A": True,
        "determinant": 1,
        "denominator_17_is_a_two_adic_unit": True,
        "spinor_norm_square_class": "-17",
        "hilbert_symbol_minus_17_three_at_2": hilbert_symbol,
        "minus_17_is_not_a_norm_from_Q2_sqrt3": True,
    }


def local_density_certificate() -> dict[str, object]:
    counts_two: dict[str, int] = {}
    for exponent in range(3, 9):
        count = local_congruence_count(2, exponent)
        expected = 3 * 2 ** (2 * exponent - 1)
        if count != expected:
            raise AssertionError(("two-adic count", exponent, count, expected))
        counts_two[str(exponent)] = count

    counts_three: dict[str, int] = {}
    for exponent in range(1, 6):
        count = local_congruence_count(3, exponent)
        expected = 2 * 3 ** (2 * exponent)
        if count != expected:
            raise AssertionError(("three-adic count", exponent, count, expected))
        counts_three[str(exponent)] = count

    good_prime_counts: dict[str, dict[str, int]] = {}
    for prime in (5, 7, 11, 13):
        chi = legendre_three(prime)
        prime_counts: dict[str, int] = {}
        for exponent in (1, 2):
            count = local_congruence_count(prime, exponent)
            expected_numerator = (prime * prime - 1) * prime ** (2 * exponent - 1)
            expected = expected_numerator // (prime - chi)
            if expected * (prime - chi) != expected_numerator:
                raise AssertionError(("nonintegral good-prime formula", prime, exponent))
            if count != expected:
                raise AssertionError(
                    ("good-prime count", prime, exponent, count, expected, chi)
                )
            prime_counts[str(exponent)] = count
        good_prime_counts[str(prime)] = prime_counts

    return {
        "p_2_counts": counts_two,
        "p_2_density": "3/2",
        "p_3_counts": counts_three,
        "p_3_density": "2",
        "good_prime_counts": good_prime_counts,
        "good_prime_density": "(1-p^-2)/(1-(3|p)*p^-1)",
    }


@dataclass(frozen=True, order=True)
class Root:
    z: int
    x: int
    y: int
    a: int
    q: int
    n: int

    def ordered_triple(self) -> tuple[int, int, int]:
        return (self.x, self.y, self.z)


def enumerate_reduced_roots(max_z: int) -> list[Root]:
    if max_z < 1:
        return []

    roots: list[Root] = []
    # From z=4a+17n and a^2 >= 18n^2-2, no solution remains once
    # floor((max_z-17n)/4)^2 < 18n^2-2.
    n = 0
    while 17 * n <= max_z:
        a_max = (max_z - 17 * n) // 4
        if a_max < 1:
            break
        q_square_bound = a_max * a_max - 18 * n * n + 2
        if q_square_bound < 0:
            n += 1
            continue
        q_max = math.isqrt(q_square_bound // 3)

        q_values = np.arange(q_max + 1, dtype=np.int64)
        radicands = 3 * q_values * q_values + (18 * n * n - 2)
        nonnegative = radicands >= 0
        if np.any(nonnegative):
            candidate_q = q_values[nonnegative]
            candidate_radicands = radicands[nonnegative]
            candidate_a = np.floor(np.sqrt(candidate_radicands)).astype(np.int64)
            exact = candidate_a * candidate_a == candidate_radicands
            for q_np, a_np in zip(candidate_q[exact], candidate_a[exact], strict=True):
                q = int(q_np)
                a = int(a_np)
                p = a + 4 * n
                if p <= q:
                    continue
                # The shell equation forces a and q to have the same parity:
                # modulo 2 it reads a^2-q^2=0, and r^2=r modulo 2.
                if (a - q) % 2:
                    raise AssertionError(("shell did not force parity", a, q, n))
                x, y, z = inverse_coordinates(a, q, n)
                if not (0 < x <= y <= z <= max_z):
                    raise AssertionError(("inverse inequalities", a, q, n, x, y, z))
                if forward_coordinates(x, y, z) != (a, q, n):
                    raise AssertionError(("forward-after-inverse", a, q, n, x, y, z))
                if inverse_coordinates(*forward_coordinates(x, y, z)) != (x, y, z):
                    raise AssertionError(("inverse-after-forward", a, q, n, x, y, z))
                if ternary_form(a, q, n) != -2:
                    raise AssertionError(("transformed equation", a, q, n))
                if 2 * defect(x, y, z) != ternary_form(a, q, n):
                    raise AssertionError(("polynomial identity", a, q, n, x, y, z))
                if defect(x, y, z) != -1:
                    raise AssertionError(("original defect", a, q, n, x, y, z))
                roots.append(Root(z=z, x=x, y=y, a=a, q=q, n=n))
        n += 1

    roots.sort()
    triples = [root.ordered_triple() for root in roots]
    if len(triples) != len(set(triples)):
        raise AssertionError("the inverse coordinate map produced duplicate roots")
    return roots


def count_at(roots: list[Root], checkpoint: int) -> int:
    # roots are sorted first by z
    lo = 0
    hi = len(roots)
    while lo < hi:
        mid = (lo + hi) // 2
        if roots[mid].z <= checkpoint:
            lo = mid + 1
        else:
            hi = mid
    return lo


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-z", type=int, default=100_000)
    parser.add_argument("--checkpoints", type=int, nargs="*", default=list(DEFAULT_CHECKPOINTS))
    parser.add_argument("--first", type=int, default=12)
    args = parser.parse_args()

    checkpoints = sorted(set(c for c in args.checkpoints if 0 <= c <= args.max_z))
    if args.max_z not in checkpoints:
        checkpoints.append(args.max_z)
    roots = enumerate_reduced_roots(args.max_z)
    singular_series = (
        9
        / 2
        * math.log(2 + math.sqrt(3))
        / (math.sqrt(3) * (math.pi * math.pi / 6))
    )
    archimedean_factor = (
        math.log(3 / (2 * math.sqrt(2))) / (2 * math.sqrt(3))
    )
    density_constant = singular_series * archimedean_factor
    former_guess = 1 / (9 * math.pi)
    counts = {str(c): count_at(roots, c) for c in checkpoints}
    payload = {
        "schema_version": 2,
        "original_equation": "4*(x*y+x*z+y*z)-(x*x+y*y+z*z)=-1",
        "reduced_chamber": "0<x<=y<=z and z>=4*(x+y)",
        "forward_map": {
            "n": "z-4*(x+y)",
            "q": "y-x",
            "a": "x+y-4*n",
        },
        "inverse_map": {
            "x": "(a+4*n-q)/2",
            "y": "(a+4*n+q)/2",
            "z": "4*a+17*n",
        },
        "transformed_equation": "a*a-3*q*q-18*n*n=-2",
        "exact_height": "z=4*a+17*n",
        "target_domain": "a>0, q>=0, n>=0, a+4*n>q, a*a-3*q*q-18*n*n=-2",
        "coordinate_certificate": {
            "polynomial_identity": (
                "2*(4*(x*y+x*z+y*z)-(x*x+y*y+z*z))="
                "a*a-3*q*q-18*n*n"
            ),
            "parity_is_forced_by_shell_equation": True,
            "forward_after_inverse_checked_for_every_candidate": True,
            "inverse_after_forward_checked_for_every_candidate": True,
            "all_fibres_among_enumerated_candidates_are_singletons": True,
        },
        "local_density_certificate": local_density_certificate(),
        "two_adic_orbit_exchange_certificate": two_adic_isometry_certificate(),
        "proved_main_term": {
            "singular_series_expression": (
                "(9/2)*log(2+sqrt(3))/(sqrt(3)*zeta(2))"
            ),
            "singular_series_value": singular_series,
            "archimedean_factor_expression": (
                "log(3/(2*sqrt(2)))/(2*sqrt(3))"
            ),
            "archimedean_factor_value": archimedean_factor,
            "finite_adelic_coefficient": 1,
            "density_constant_expression": (
                "9*log(2+sqrt(3))*log(3/(2*sqrt(2)))/(2*pi^2)"
            ),
            "density_constant_value": density_constant,
            "former_guess_value": former_guess,
            "density_minus_former_guess": density_constant - former_guess,
            "relative_difference_from_former_guess": (
                density_constant / former_guess - 1
            ),
        },
        "max_z": args.max_z,
        "counts": counts,
        "residuals_from_proved_main_term": {
            str(c): counts[str(c)] - density_constant * c for c in checkpoints
        },
        "first_roots": [root.ordered_triple() for root in roots[: args.first]],
        "last_root": roots[-1].ordered_triple() if roots else None,
        "comparison_at_max_z": {
            "count": len(roots),
            "proved_main_term": density_constant * args.max_z,
            "residual_from_proved_main_term": (
                len(roots) - density_constant * args.max_z
            ),
            "max_z_over_9pi": args.max_z / (9 * math.pi),
            "ratio_to_max_z_over_9pi": (
                len(roots) / (args.max_z / (9 * math.pi)) if args.max_z else None
            ),
        },
        "candidate_count": len(roots),
        "all_candidates_rechecked_in_original_equation": True,
        "duplicate_original_roots": 0,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
