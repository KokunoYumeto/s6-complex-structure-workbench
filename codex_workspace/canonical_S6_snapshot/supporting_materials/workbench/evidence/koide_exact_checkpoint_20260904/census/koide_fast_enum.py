#!/usr/bin/env python3
"""Exact subquadratic enumeration of Koide reduced roots.

The enumerated objects are exactly

    a^2 - 3 q^2 - 18 n^2 = -2,
    a > 0, q >= 0, n >= 0, a + 4 n > q, 4 a + 17 n <= X.

For each fixed n >= 1 this is the generalized Pell equation

    a^2 - 3 q^2 = N_n,   N_n = 18 n^2 - 2.

The code uses the integer Lagrange--Mollin--Matthews continued-fraction
algorithm to obtain the finite set of unit orbits for N_n.  Every orbit is
put into the unique reduced form A > 2 Q >= 0 and is then traversed by the
totally positive unit 2 + sqrt(3).  The factors of N_n are obtained from

    N_n = 2 (3 n - 1) (3 n + 1),

using a compact smallest-prime-factor sieve.  No floating-point operation is
used to propose or accept a lattice point.  Every emitted point is checked in
both the ternary equation and the original Delta polynomial.

Floating/interval arithmetic is confined to the discrepancy report for the
transcendental main-term constant.  Counts and coordinates remain integers.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import gzip
import hashlib
import io
import json
import math
import os
import platform
import sys
import time
from array import array
from collections import Counter
from dataclasses import asdict, dataclass
from fractions import Fraction
from itertools import groupby
from pathlib import Path
from typing import Callable, Iterable, Iterator, Sequence

import mpmath as mp
import numpy as np


CANONICAL_CHECKPOINTS = (
    10_000,
    20_000,
    30_000,
    40_000,
    50_000,
    75_000,
    100_000,
    125_000,
    150_000,
    175_000,
    200_000,
)

EXTRA_CHECKPOINTS = (
    250_000,
    500_000,
    1_000_000,
    2_000_000,
    5_000_000,
    10_000_000,
    20_000_000,
    50_000_000,
    100_000_000,
)


@dataclass(frozen=True, order=True)
class Root:
    """One point in both exact coordinate systems."""

    z: int
    x: int
    y: int
    a: int
    q: int
    n: int


@dataclass
class EnumerationStats:
    max_height: int
    n_max: int
    emitted_roots: int = 0
    fixed_n_values: int = 0
    pell_modular_starts: int = 0
    raw_lmm_solutions: int = 0
    canonical_unit_orbits: int = 0
    duplicate_lmm_orbit_descriptions_removed: int = 0
    maximum_orbits_for_one_n: int = 0
    n_at_maximum_orbits: int = 0
    character_sum_orbit_checks: int = 0
    split_factor_character_product_checks: int = 0
    spf_limit: int = 0
    spf_bytes: int = 0
    sieve_seconds: float = 0.0
    enumeration_seconds: float = 0.0


def defect(x: int, y: int, z: int) -> int:
    return 4 * (x * y + x * z + y * z) - (x * x + y * y + z * z)


def ternary_form(a: int, q: int, n: int) -> int:
    return a * a - 3 * q * q - 18 * n * n


def inverse_coordinates(a: int, q: int, n: int) -> tuple[int, int, int]:
    xn = a + 4 * n - q
    yn = a + 4 * n + q
    if xn % 2 or yn % 2:
        raise ArithmeticError(("nonintegral inverse", a, q, n))
    return xn // 2, yn // 2, 4 * a + 17 * n


def forward_coordinates(x: int, y: int, z: int) -> tuple[int, int, int]:
    n = z - 4 * (x + y)
    q = y - x
    a = x + y - 4 * n
    return a, q, n


def ceil_sqrt(value: int) -> int:
    if value < 0:
        raise ValueError(value)
    root = math.isqrt(value)
    return root if root * root == value else root + 1


def minimum_possible_height(n: int) -> int:
    """A necessary lower height bound at fixed n (exact, not sufficient)."""

    if n == 0:
        return 4
    return 17 * n + 4 * ceil_sqrt(18 * n * n - 2)


def maximum_relevant_n(max_height: int) -> int:
    """Largest n not excluded by a >= ceil(sqrt(18 n^2-2))."""

    if max_height < 0:
        return -1
    lo, hi = 0, max_height // 17 + 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if minimum_possible_height(mid) <= max_height:
            lo = mid
        else:
            hi = mid - 1
    return lo


def build_smallest_prime_factor(limit: int) -> array:
    """Return a compact uint32 smallest-prime-factor table through limit."""

    if limit >= 2**32:
        raise ValueError("uint32 SPF table limit exceeded")
    spf = array("I", [0]) * (limit + 1)
    for prime in range(2, math.isqrt(limit) + 1):
        if spf[prime] != 0:
            continue
        for multiple in range(prime * prime, limit + 1, prime):
            if spf[multiple] == 0:
                spf[multiple] = prime
    return spf


def factor_with_spf(value: int, spf: array) -> dict[int, int]:
    """Factor 1 <= value < len(spf), interpreting SPF zero as prime."""

    if not (1 <= value < len(spf)):
        raise ValueError((value, len(spf)))
    factors: dict[int, int] = {}
    remaining = value
    while remaining > 1:
        prime = int(spf[remaining]) or remaining
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        factors[prime] = exponent
    return factors


def factor_N(n: int, spf: array) -> dict[int, int]:
    """Factor N_n = 2(3n-1)(3n+1) using only SPF-sized operands."""

    if n < 1:
        raise ValueError(n)
    factors: dict[int, int] = {2: 1}
    for value in (3 * n - 1, 3 * n + 1):
        for prime, exponent in factor_with_spf(value, spf).items():
            factors[prime] = factors.get(prime, 0) + exponent
    expected = 18 * n * n - 2
    reconstructed = math.prod(p**e for p, e in factors.items())
    if reconstructed != expected:
        raise ArithmeticError(("factorization identity", n, reconstructed, expected))
    return dict(sorted(factors.items()))


def character_sum_rho(factors: dict[int, int]) -> int:
    """Compute rho(m)=sum_{d|m} chi_12(d) multiplicatively.

    Here chi_12 is the primitive real character modulo 12: it vanishes on
    primes 2 and 3, is +1 for p=1,11 (mod 12), and is -1 for p=5,7
    (mod 12).  The local divisor sums are therefore 1, e+1, or the
    alternating sum 1-1+...+(-1)^e.
    """

    result = 1
    for prime, exponent in factors.items():
        if prime in (2, 3):
            local = 1
        elif prime % 12 in (1, 11):
            local = exponent + 1
        elif prime % 12 in (5, 7):
            local = 1 if exponent % 2 == 0 else 0
        else:
            raise ArithmeticError(("unexpected prime residue", prime, exponent))
        result *= local
    return result


_TONELLI_ROOT_CACHE: dict[int, int] = {}


def tonelli_shanks_three(prime: int) -> int:
    """One square root of 3 modulo an odd prime known to split."""

    cached = _TONELLI_ROOT_CACHE.get(prime)
    if cached is not None:
        return cached
    if prime <= 3 or prime % 2 == 0:
        raise ValueError(prime)
    if pow(3, (prime - 1) // 2, prime) != 1:
        raise ArithmeticError(("3 is not a square", prime))
    if prime % 4 == 3:
        root = pow(3, (prime + 1) // 4, prime)
    else:
        odd_part = prime - 1
        two_power = 0
        while odd_part % 2 == 0:
            odd_part //= 2
            two_power += 1
        nonresidue = 2
        while pow(nonresidue, (prime - 1) // 2, prime) != prime - 1:
            nonresidue += 1
        m = two_power
        c = pow(nonresidue, odd_part, prime)
        t = pow(3, odd_part, prime)
        root = pow(3, (odd_part + 1) // 2, prime)
        while t != 1:
            i = 1
            t_power = t * t % prime
            while t_power != 1:
                t_power = t_power * t_power % prime
                i += 1
                if i >= m:
                    raise ArithmeticError(("Tonelli-Shanks failed", prime))
            b = pow(c, 1 << (m - i - 1), prime)
            root = root * b % prime
            t = t * b * b % prime
            c = b * b % prime
            m = i
    if root * root % prime != 3 % prime:
        raise ArithmeticError(("bad Tonelli root", prime, root))
    _TONELLI_ROOT_CACHE[prime] = root
    return root


def square_roots_three_prime_power(prime: int, exponent: int) -> tuple[tuple[int, ...], int]:
    """All roots of r^2 = 3 modulo p^e, and the modulus p^e."""

    modulus = prime**exponent
    if exponent == 0:
        return (0,), 1
    if prime == 2:
        return ((1,), 2) if exponent == 1 else ((), modulus)
    if prime == 3:
        return ((0,), 3) if exponent == 1 else ((), modulus)
    # Quadratic reciprocity gives (3/p)=1 exactly for p = +/-1 (mod 12).
    if prime % 12 not in (1, 11):
        return (), modulus
    root = tonelli_shanks_three(prime)
    lifted_modulus = prime
    for _ in range(1, exponent):
        quotient = (root * root - 3) // lifted_modulus
        correction = (-quotient * pow(2 * root, -1, prime)) % prime
        root += correction * lifted_modulus
        lifted_modulus *= prime
    if lifted_modulus != modulus or root * root % modulus != 3 % modulus:
        raise ArithmeticError(("bad Hensel lift", prime, exponent, root))
    other = (-root) % modulus
    return ((root,) if other == root else (root, other)), modulus


def square_roots_three(factors: dict[int, int]) -> tuple[int, list[int]]:
    """All roots of r^2 = 3 modulo m from the supplied factorization."""

    roots = (0,)
    modulus = 1
    for prime, exponent in sorted(factors.items()):
        local_roots, local_modulus = square_roots_three_prime_power(prime, exponent)
        if not local_roots:
            return math.prod(p**e for p, e in factors.items()), []
        inverse = pow(modulus, -1, local_modulus)
        roots = tuple(
            root + modulus * (((local_root - root) * inverse) % local_modulus)
            for root in roots
            for local_root in local_roots
        )
        modulus *= local_modulus
    roots_out = sorted(set(roots))
    if any((root * root - 3) % modulus for root in roots_out):
        raise ArithmeticError(("CRT square root check", modulus, roots_out))
    return modulus, roots_out


def admissible_square_divisor_cases(
    factors: dict[int, int],
) -> Iterator[tuple[int, dict[int, int]]]:
    """Yield f and factorization of m=N/f^2 only when sqrt(3 mod m) can exist."""

    states: list[tuple[int, dict[int, int]]] = [(1, {})]
    for prime, exponent in sorted(factors.items()):
        next_states: list[tuple[int, dict[int, int]]] = []
        for removed_half in range(exponent // 2 + 1):
            remaining_exponent = exponent - 2 * removed_half
            locally_possible = True
            if prime in (2, 3):
                locally_possible = remaining_exponent <= 1
            elif prime % 12 not in (1, 11):
                locally_possible = remaining_exponent == 0
            if not locally_possible:
                continue
            multiplier = prime**removed_half
            for f_value, m_factors in states:
                updated = dict(m_factors)
                if remaining_exponent:
                    updated[prime] = remaining_exponent
                next_states.append((f_value * multiplier, updated))
        states = next_states
        if not states:
            return
    yield from states


def lmm_candidate(m: int, square_root: int) -> tuple[int, int] | None:
    """Specialized exact LMM test for x^2-3y^2=m from one modular root.

    This mirrors the P,Q continued-fraction recurrence but uses Python
    integers only.  The negative Pell alternative in the general LMM
    algorithm cannot occur here because x^2-3y^2=-1 is impossible modulo 3.
    """

    if m <= 0 or (square_root * square_root - 3) % m:
        raise ValueError((m, square_root))
    z = square_root - m if 2 * square_root > m else square_root
    p_value = z
    q_value = m
    b_old = 0
    b_older = 1
    g_old = q_value
    g_older = -p_value

    # First P,Q yield; the LMM candidate is always the preceding (G,B)
    # when a subsequent Q becomes +/-1.
    partial = (p_value + 1) // q_value  # floor(sqrt(3)) = 1
    b_old, b_older = partial * b_old + b_older, b_old
    g_old, g_older = partial * g_old + g_older, g_old
    previous_b, previous_g = b_old, g_old
    p_value = partial * q_value - p_value
    q_value = (3 - p_value * p_value) // q_value
    seen = {(z, m)}

    while (p_value, q_value) not in seen:
        seen.add((p_value, q_value))
        partial = (p_value + 1) // q_value
        b_old, b_older = partial * b_old + b_older, b_old
        g_old, g_older = partial * g_old + g_older, g_old
        if abs(q_value) == 1:
            if previous_g * previous_g - 3 * previous_b * previous_b == m:
                return previous_g, previous_b
            return None
        previous_b, previous_g = b_old, g_old
        p_value = partial * q_value - p_value
        q_value = (3 - p_value * p_value) // q_value
    return None


def fundamental_lmm_solutions(
    factors: dict[int, int], stats: EnumerationStats | None = None
) -> set[tuple[int, int]]:
    """Finite LMM representatives for x^2-3y^2=N."""

    N = math.prod(prime**exponent for prime, exponent in factors.items())
    solutions: set[tuple[int, int]] = set()
    for square_factor, m_factors in admissible_square_divisor_cases(factors):
        m, roots = square_roots_three(m_factors)
        if N != square_factor * square_factor * m:
            raise ArithmeticError(("square divisor decomposition", N, square_factor, m))
        if stats is not None:
            stats.pell_modular_starts += len(roots)
        for root in roots:
            candidate = lmm_candidate(m, root)
            if candidate is None:
                continue
            x_value = square_factor * candidate[0]
            y_value = square_factor * candidate[1]
            if x_value * x_value - 3 * y_value * y_value != N:
                raise ArithmeticError(("LMM norm", N, x_value, y_value))
            solutions.add((x_value, y_value))
    if stats is not None:
        stats.raw_lmm_solutions += len(solutions)
    return solutions


def multiply_unit(a: int, q: int) -> tuple[int, int]:
    """Multiply a+q sqrt(3) by 2+sqrt(3)."""

    return 2 * a + 3 * q, a + 2 * q


def multiply_inverse_unit(a: int, q: int) -> tuple[int, int]:
    """Multiply a+q sqrt(3) by 2-sqrt(3)."""

    return 2 * a - 3 * q, 2 * q - a


def canonical_positive_orbit_seed(N: int, a: int, q: int) -> tuple[int, int]:
    """Unique representative A>2Q>=0 in a positive-norm unit orbit."""

    a = abs(a)
    if a * a - 3 * q * q != N or N <= 0:
        raise ValueError((N, a, q))
    # Since N>0 and a>0, a>sqrt(3)|q|.  Forward multiplication therefore
    # eventually makes q nonnegative without making a nonpositive.
    while q < 0:
        a, q = multiply_unit(a, q)
    # In the positive quadrant, inverse multiplication remains there exactly
    # while 2q-a >= 0.  It strictly decreases a on that range.
    while 2 * q >= a:
        a, q = multiply_inverse_unit(a, q)
    if not (a > 2 * q >= 0 and a * a - 3 * q * q == N):
        raise ArithmeticError(("canonical Pell seed", N, a, q))
    return a, q


def canonical_unit_orbits(
    N: int, factors: dict[int, int], stats: EnumerationStats | None = None
) -> list[tuple[int, int]]:
    """All distinct positive unit orbits, represented by A>2Q>=0."""

    seeds: set[tuple[int, int]] = set()
    raw = fundamental_lmm_solutions(factors, stats)
    descriptions = 0
    for a, q in raw:
        q_abs = abs(q)
        signs = (q_abs,) if q_abs == 0 else (q_abs, -q_abs)
        for signed_q in signs:
            descriptions += 1
            seeds.add(canonical_positive_orbit_seed(N, a, signed_q))
    if stats is not None:
        stats.canonical_unit_orbits += len(seeds)
        stats.duplicate_lmm_orbit_descriptions_removed += descriptions - len(seeds)
    return sorted(seeds)


def validate_root(a: int, q: int, n: int, max_height: int) -> Root:
    """Reconstruct and rigorously check one retained root in both systems."""

    if not (a > 0 and q >= 0 and n >= 0 and a + 4 * n > q):
        raise ArithmeticError(("ternary chamber", a, q, n))
    if ternary_form(a, q, n) != -2:
        raise ArithmeticError(("ternary equation", a, q, n))
    x, y, z = inverse_coordinates(a, q, n)
    if z != 4 * a + 17 * n or z > max_height:
        raise ArithmeticError(("height", a, q, n, z, max_height))
    if not (0 < x <= y <= z and z >= 4 * (x + y)):
        raise ArithmeticError(("original chamber", x, y, z, a, q, n))
    if z - 4 * (x + y) != n:
        raise ArithmeticError(("wall coordinate", x, y, z, n))
    if forward_coordinates(x, y, z) != (a, q, n):
        raise ArithmeticError(("forward inverse", x, y, z, a, q, n))
    if 2 * defect(x, y, z) != ternary_form(a, q, n):
        raise ArithmeticError(("polynomial identity", x, y, z, a, q, n))
    if defect(x, y, z) != -1:
        raise ArithmeticError(("original Delta", x, y, z, a, q, n))
    return Root(z=z, x=x, y=y, a=a, q=q, n=n)


def enumerate_roots(
    max_height: int,
    emit: Callable[[Root], None],
    stats: EnumerationStats | None = None,
) -> EnumerationStats:
    """Enumerate every retained root, in deterministic (n, orbit, k) order."""

    if max_height < 0:
        raise ValueError(max_height)
    n_max = maximum_relevant_n(max_height)
    if stats is None:
        stats = EnumerationStats(max_height=max_height, n_max=n_max)
    elif stats.max_height != max_height or stats.n_max != n_max:
        raise ValueError((stats, max_height, n_max))

    sieve_start = time.perf_counter()
    spf_limit = max(2, 3 * n_max + 1)
    spf = build_smallest_prime_factor(spf_limit)
    stats.spf_limit = spf_limit
    stats.spf_bytes = len(spf) * spf.itemsize
    stats.sieve_seconds = time.perf_counter() - sieve_start

    enumeration_start = time.perf_counter()
    # The exceptional negative-norm face n=0 is one orbit.  (1,1) itself
    # fails a>q; every subsequent forward iterate satisfies the chamber.
    a, q = 1, 1
    while 4 * a <= max_height:
        if a > q:
            root = validate_root(a, q, 0, max_height)
            emit(root)
            stats.emitted_roots += 1
        a, q = multiply_unit(a, q)

    for n in range(1, n_max + 1):
        stats.fixed_n_values += 1
        N = 18 * n * n - 2
        a_max = (max_height - 17 * n) // 4
        factors = factor_N(n, spf)
        seeds = canonical_unit_orbits(N, factors, stats)
        expected_orbits = character_sum_rho(factors)
        if len(seeds) != expected_orbits:
            raise ArithmeticError(("character-sum orbit count", n, len(seeds), expected_orbits))
        stats.character_sum_orbit_checks += 1
        minus_factors = factor_with_spf(3 * n - 1, spf)
        plus_factors = factor_with_spf(3 * n + 1, spf)
        split_product = character_sum_rho(minus_factors) * character_sum_rho(plus_factors)
        if split_product != expected_orbits:
            raise ArithmeticError(
                ("rho(3n-1)rho(3n+1)", n, split_product, expected_orbits)
            )
        stats.split_factor_character_product_checks += 1
        if len(seeds) > stats.maximum_orbits_for_one_n:
            stats.maximum_orbits_for_one_n = len(seeds)
            stats.n_at_maximum_orbits = n
        for seed_a, seed_q in seeds:
            a, q = seed_a, seed_q
            while a <= a_max:
                root = validate_root(a, q, n, max_height)
                # Re-reduction proves at run time that this generated point
                # belongs to the orbit currently being emitted.
                if canonical_positive_orbit_seed(N, a, q) != (seed_a, seed_q):
                    raise ArithmeticError(("orbit identity", n, seed_a, seed_q, a, q))
                emit(root)
                stats.emitted_roots += 1
                a, q = multiply_unit(a, q)

    stats.enumeration_seconds = time.perf_counter() - enumeration_start
    return stats


class RootSink:
    """Low-memory sink: gzip all coordinates, retain only uint64 heights."""

    def __init__(self, path: Path | None):
        self.path = path
        self.heights = array("Q")
        self.coordinate_sha256 = hashlib.sha256()
        self._raw = None
        self._text = None
        self._writer = None
        self.count = 0

    def __enter__(self) -> "RootSink":
        if self.path is not None:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self._raw = gzip.GzipFile(
                filename=str(self.path), mode="wb", compresslevel=6, mtime=0
            )
            self._text = io.TextIOWrapper(self._raw, encoding="utf-8", newline="")
            self._writer = csv.writer(self._text, lineterminator="\n")
            self._writer.writerow(("enumeration_index", "z", "x", "y", "a", "q", "n"))
        return self

    def emit(self, root: Root) -> None:
        if not (0 <= root.z < 2**64):
            raise OverflowError(root.z)
        self.count += 1
        self.heights.append(root.z)
        line = f"{root.z},{root.x},{root.y},{root.a},{root.q},{root.n}\n".encode()
        self.coordinate_sha256.update(line)
        if self._writer is not None:
            self._writer.writerow((self.count, root.z, root.x, root.y, root.a, root.q, root.n))

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if self._text is not None:
            self._text.flush()
            self._text.close()
        elif self._raw is not None:
            self._raw.close()


def sort_heights_in_place(heights: array) -> None:
    if not heights:
        return
    view = np.frombuffer(heights, dtype=np.uint64)
    view.sort(kind="quicksort")


def mpf_tuple_to_fraction(value: tuple[int, int, int, int]) -> Fraction:
    sign, mantissa, exponent, _bit_count = value
    magnitude = Fraction(int(mantissa))
    if exponent >= 0:
        magnitude *= 2**exponent
    else:
        magnitude /= 2 ** (-exponent)
    return -magnitude if sign else magnitude


def constant_interval(decimal_digits: int = 90) -> tuple[Fraction, Fraction, mp.mpf]:
    """Outward-rounded mpmath interval and a higher-precision display midpoint."""

    mp.iv.dps = decimal_digits
    interval = (
        mp.iv.mpf(9)
        / (2 * mp.iv.pi**2)
        * mp.iv.log(2 + mp.iv.sqrt(3))
        * mp.iv.log(3 / (2 * mp.iv.sqrt(2)))
    )
    lower, upper = (mpf_tuple_to_fraction(endpoint) for endpoint in interval._mpi_)
    if not lower < upper:
        raise ArithmeticError(("constant interval", lower, upper))
    mp.mp.dps = decimal_digits + 20
    midpoint = (
        mp.mpf(9)
        / (2 * mp.pi**2)
        * mp.log(2 + mp.sqrt(3))
        * mp.log(mp.mpf(3) / (2 * mp.sqrt(2)))
    )
    if not mp.mpf(lower.numerator) / lower.denominator < midpoint < mp.mpf(upper.numerator) / upper.denominator:
        raise ArithmeticError("display midpoint escaped certified interval")
    return lower, upper, midpoint


def residual_interval(
    count: int, x_value: int, c_lower: Fraction, c_upper: Fraction
) -> tuple[Fraction, Fraction]:
    return Fraction(count) - c_upper * x_value, Fraction(count) - c_lower * x_value


def residual_sign(
    count: int, x_value: int, c_lower: Fraction, c_upper: Fraction
) -> int:
    # Compare against the certified rational endpoints by cross
    # multiplication.  Avoiding Fraction construction here matters because
    # this predicate is called at every occupied-height interval.
    lower_numerator = count * c_upper.denominator - c_upper.numerator * x_value
    upper_numerator = count * c_lower.denominator - c_lower.numerator * x_value
    if lower_numerator > 0:
        return 1
    if upper_numerator < 0:
        return -1
    if lower_numerator == upper_numerator == 0:
        return 0
    raise ArithmeticError(
        ("constant interval too wide for sign", count, x_value, lower_numerator, upper_numerator)
    )


def certified_violation(
    count: int,
    x_value: int,
    candidate: Fraction,
    c_lower: Fraction,
    c_upper: Fraction,
) -> bool:
    positive_numerator = count * c_upper.denominator - c_upper.numerator * x_value
    negative_numerator = c_lower.numerator * x_value - count * c_lower.denominator
    if positive_numerator > 0:
        absolute_numerator = positive_numerator
        absolute_denominator = c_upper.denominator
    elif negative_numerator > 0:
        absolute_numerator = negative_numerator
        absolute_denominator = c_lower.denominator
    else:
        return False
    return (
        absolute_numerator
        * absolute_numerator
        * candidate.denominator
        * candidate.denominator
        > candidate.numerator
        * candidate.numerator
        * x_value
        * absolute_denominator
        * absolute_denominator
    )


def height_segments(
    sorted_heights: Sequence[int], domain_start: int, domain_end: int
) -> Iterator[tuple[int, int, int]]:
    """Maximal integer intervals [L,U] on which R(X) is constant."""

    if domain_end < domain_start:
        return
    count_before = bisect.bisect_left(sorted_heights, domain_start)
    index = count_before
    cursor = domain_start
    length = len(sorted_heights)
    while index < length:
        height = int(sorted_heights[index])
        if height > domain_end:
            break
        if cursor <= height - 1:
            yield cursor, height - 1, count_before
        next_index = bisect.bisect_right(sorted_heights, height, lo=index)
        count_before = next_index
        cursor = height
        index = next_index
    if cursor <= domain_end:
        yield cursor, domain_end, count_before


def decimal_residual(count: int, x_value: int, c_mid: mp.mpf) -> mp.mpf:
    return mp.mpf(count) - c_mid * x_value


def metric_record(count: int, x_value: int, c_mid: mp.mpf) -> dict[str, object]:
    residual = decimal_residual(count, x_value, c_mid)
    sqrt_x = mp.sqrt(x_value)
    return {
        "X": x_value,
        "R": count,
        "residual": mp.nstr(residual, 40),
        "residual_over_sqrt_X": mp.nstr(residual / sqrt_x, 40),
        "absolute_residual_over_sqrt_X": mp.nstr(abs(residual) / sqrt_x, 40),
        "residual_over_sqrt_X_log_2X": mp.nstr(
            residual / (sqrt_x * mp.log(2 * x_value)), 40
        ),
    }


def analyze_domain(
    sorted_heights: Sequence[int],
    domain_start: int,
    domain_end: int,
    c_lower: Fraction,
    c_upper: Fraction,
    c_mid: mp.mpf,
    candidates: Sequence[Fraction],
) -> dict[str, object]:
    """Exact-count residual extrema, sign runs, and candidate tests."""

    if domain_start < 1 or domain_end < domain_start:
        raise ValueError((domain_start, domain_end))
    sign_runs: list[dict[str, object]] = []
    max_raw: tuple[mp.mpf, int, int] | None = None
    min_raw: tuple[mp.mpf, int, int] | None = None
    max_norm: tuple[mp.mpf, int, int] | None = None
    min_norm: tuple[mp.mpf, int, int] | None = None
    max_abs_norm: tuple[mp.mpf, int, int] | None = None
    first_violations: dict[Fraction, tuple[int, int] | None] = {c: None for c in candidates}

    def append_run(start: int, end: int, sign: int) -> None:
        if start > end:
            return
        label = "positive" if sign > 0 else "negative" if sign < 0 else "zero"
        if sign_runs and sign_runs[-1]["sign"] == label and sign_runs[-1]["end_X"] + 1 == start:
            sign_runs[-1]["end_X"] = end
            sign_runs[-1]["length"] = end - sign_runs[-1]["start_X"] + 1
        else:
            sign_runs.append(
                {"sign": label, "start_X": start, "end_X": end, "length": end - start + 1}
            )

    for left, right, count in height_segments(sorted_heights, domain_start, domain_end):
        for x_value in (left,) if left == right else (left, right):
            residual = decimal_residual(count, x_value, c_mid)
            normalized = residual / mp.sqrt(x_value)
            raw_item = (residual, x_value, count)
            norm_item = (normalized, x_value, count)
            if max_raw is None or residual > max_raw[0]:
                max_raw = raw_item
            if min_raw is None or residual < min_raw[0]:
                min_raw = raw_item
            if max_norm is None or normalized > max_norm[0]:
                max_norm = norm_item
            if min_norm is None or normalized < min_norm[0]:
                min_norm = norm_item
            if max_abs_norm is None or abs(normalized) > abs(max_abs_norm[0]):
                max_abs_norm = norm_item

        sign_left = residual_sign(count, left, c_lower, c_upper)
        sign_right = residual_sign(count, right, c_lower, c_upper)
        if sign_left == sign_right:
            append_run(left, right, sign_left)
        else:
            if not (sign_left > 0 and sign_right < 0):
                raise ArithmeticError(("unexpected flat-segment signs", left, right, count))
            low, high = left, right
            while low < high:
                middle = (low + high + 1) // 2
                if residual_sign(count, middle, c_lower, c_upper) > 0:
                    low = middle
                else:
                    high = middle - 1
            append_run(left, low, 1)
            append_run(low + 1, right, -1)

        for candidate in candidates:
            if first_violations[candidate] is not None:
                continue
            if certified_violation(count, left, candidate, c_lower, c_upper):
                first_violations[candidate] = (left, count)
                continue
            if left < right and certified_violation(count, right, candidate, c_lower, c_upper):
                low, high = left + 1, right
                while low < high:
                    middle = (low + high) // 2
                    if certified_violation(count, middle, candidate, c_lower, c_upper):
                        high = middle
                    else:
                        low = middle + 1
                first_violations[candidate] = (low, count)

    if None in (max_raw, min_raw, max_norm, min_norm, max_abs_norm):
        raise ArithmeticError("empty residual domain")

    def tuple_metric(item: tuple[mp.mpf, int, int]) -> dict[str, object]:
        _, x_value, count = item
        return metric_record(count, x_value, c_mid)

    max_abs_raw = max((max_raw, min_raw), key=lambda item: abs(item[0]))
    maximum_positive_run = max(
        (run for run in sign_runs if run["sign"] == "positive"),
        key=lambda run: run["length"],
        default=None,
    )
    maximum_negative_run = max(
        (run for run in sign_runs if run["sign"] == "negative"),
        key=lambda run: run["length"],
        default=None,
    )
    candidate_records: dict[str, object] = {}
    for candidate, violation in first_violations.items():
        label = f"{candidate.numerator}/{candidate.denominator}"
        if violation is None:
            candidate_records[label] = {
                "candidate_bound": f"abs(E(X)) <= ({label})*sqrt(X)",
                "tested_domain": [domain_start, domain_end],
                "first_certified_counterexample": None,
            }
        else:
            x_value, count = violation
            candidate_records[label] = {
                "candidate_bound": f"abs(E(X)) <= ({label})*sqrt(X)",
                "tested_domain": [domain_start, domain_end],
                "first_certified_counterexample": metric_record(count, x_value, c_mid),
            }

    return {
        "domain": [domain_start, domain_end],
        "maximum_signed_residual": tuple_metric(max_raw),
        "minimum_signed_residual": tuple_metric(min_raw),
        "maximum_absolute_residual": tuple_metric(max_abs_raw),
        "maximum_signed_residual_over_sqrt_X": tuple_metric(max_norm),
        "minimum_signed_residual_over_sqrt_X": tuple_metric(min_norm),
        "maximum_absolute_residual_over_sqrt_X": tuple_metric(max_abs_norm),
        "sign_run_count": len(sign_runs),
        "sign_change_count": max(0, len(sign_runs) - 1),
        "longest_positive_run": maximum_positive_run,
        "longest_negative_run": maximum_negative_run,
        "sign_runs": sign_runs,
        "candidate_square_root_envelopes": candidate_records,
    }


def shell_statistics(sorted_heights: Sequence[int]) -> dict[str, object]:
    occupied = 0
    maximum_multiplicity = 0
    maximum_heights: list[int] = []
    multiplicity_histogram: Counter[int] = Counter()
    previous_height: int | None = None
    largest_gap = -1
    largest_gap_pair: tuple[int, int] | None = None
    for height_value, group in groupby(sorted_heights, key=int):
        multiplicity = sum(1 for _ in group)
        occupied += 1
        multiplicity_histogram[multiplicity] += 1
        if multiplicity > maximum_multiplicity:
            maximum_multiplicity = multiplicity
            maximum_heights = [height_value]
        elif multiplicity == maximum_multiplicity:
            maximum_heights.append(height_value)
        if previous_height is not None:
            gap = height_value - previous_height
            if gap > largest_gap:
                largest_gap = gap
                largest_gap_pair = (previous_height, height_value)
        previous_height = height_value
    return {
        "occupied_heights": occupied,
        "maximum_shell_multiplicity": maximum_multiplicity,
        "heights_with_maximum_multiplicity": maximum_heights,
        "multiplicity_histogram": {
            str(key): multiplicity_histogram[key] for key in sorted(multiplicity_histogram)
        },
        "largest_gap_between_occupied_heights": largest_gap if largest_gap >= 0 else None,
        "largest_gap_endpoint_heights": list(largest_gap_pair) if largest_gap_pair else None,
    }


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def produce_report(
    max_height: int,
    output_directory: Path,
    checkpoints: Sequence[int],
    write_roots: bool,
) -> dict[str, object]:
    output_directory.mkdir(parents=True, exist_ok=True)
    roots_path = output_directory / f"koide_roots_through_{max_height}.csv.gz" if write_roots else None
    stats = EnumerationStats(max_height=max_height, n_max=maximum_relevant_n(max_height))
    wall_start = time.perf_counter()
    with RootSink(roots_path) as sink:
        enumerate_roots(max_height, sink.emit, stats)
    if sink.count != stats.emitted_roots:
        raise ArithmeticError((sink.count, stats.emitted_roots))
    sort_start = time.perf_counter()
    sort_heights_in_place(sink.heights)
    sort_seconds = time.perf_counter() - sort_start

    c_lower, c_upper, c_mid = constant_interval()
    checkpoint_values = sorted(set(x for x in checkpoints if 1 <= x <= max_height) | {max_height})
    checkpoint_records = []
    for x_value in checkpoint_values:
        count = bisect.bisect_right(sink.heights, x_value)
        record = metric_record(count, x_value, c_mid)
        record["certified_sign"] = (
            "positive"
            if residual_sign(count, x_value, c_lower, c_upper) > 0
            else "negative"
        )
        checkpoint_records.append(record)

    candidate_constants = (
        Fraction(1, 10),
        Fraction(3, 20),
        Fraction(1, 5),
        Fraction(1, 4),
        Fraction(1, 2),
        Fraction(1, 1),
    )
    domains = {
        "all_tested_integers": analyze_domain(
            sink.heights, 1, max_height, c_lower, c_upper, c_mid, candidate_constants
        )
    }
    if max_height >= 10_000:
        domains["tail_from_10000"] = analyze_domain(
            sink.heights,
            10_000,
            max_height,
            c_lower,
            c_upper,
            c_mid,
            candidate_constants,
        )

    source_path = Path(__file__).resolve()
    payload: dict[str, object] = {
        "schema_version": 1,
        "claim_scope": (
            "finite exact enumeration and numerical evidence only; no discrepancy "
            "asymptotic is inferred or proved"
        ),
        "max_height": max_height,
        "count": sink.count,
        "equations": {
            "ternary": "a^2-3*q^2-18*n^2=-2",
            "chamber": "a>0, q>=0, n>=0, a+4*n>q",
            "height": "z=4*a+17*n<=X",
            "inverse": "x=(a+4*n-q)/2, y=(a+4*n+q)/2, z=4*a+17*n",
            "original": "Delta=4*(x*y+x*z+y*z)-(x^2+y^2+z^2)=-1",
        },
        "algorithm": {
            "fixed_n_norm": "N_n=18*n^2-2=2*(3*n-1)*(3*n+1)",
            "unit_recurrence": "(a,q)->(2*a+3*q,a+2*q)",
            "canonical_orbit_seed": "A>2*Q>=0",
            "orbit_source": "specialized exact Lagrange-Mollin-Matthews P,Q algorithm",
            "integer_candidate_generation_only": True,
            "every_emitted_root_rechecked_in_both_coordinate_systems": True,
        },
        "enumeration_statistics": asdict(stats),
        "sort_seconds": sort_seconds,
        "total_wall_seconds": time.perf_counter() - wall_start,
        "coordinate_stream_sha256_uncompressed_data_rows": sink.coordinate_sha256.hexdigest(),
        "coordinate_file": str(roots_path.resolve()) if roots_path else None,
        "coordinate_file_sha256": sha256_file(roots_path) if roots_path else None,
        "height_storage_bytes": len(sink.heights) * sink.heights.itemsize,
        "shell_statistics": shell_statistics(sink.heights),
        "main_term_constant": {
            "expression": "9*log(2+sqrt(3))*log(3/(2*sqrt(2)))/(2*pi^2)",
            "display_value": mp.nstr(c_mid, 100),
            "certified_binary_interval_lower": f"{c_lower.numerator}/{c_lower.denominator}",
            "certified_binary_interval_upper": f"{c_upper.numerator}/{c_upper.denominator}",
            "interval_decimal_digits_requested": 90,
        },
        "checkpoints": checkpoint_records,
        "residual_domains": domains,
        "runtime": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "mpmath": mp.__version__,
            "pid": os.getpid(),
        },
        "source": str(source_path),
        "source_sha256": sha256_file(source_path),
    }
    return payload


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-height", type=int, default=10_000_000)
    parser.add_argument(
        "--output-directory", type=Path, default=Path(__file__).resolve().parent
    )
    parser.add_argument(
        "--result-json",
        type=Path,
        help="default: OUTPUT_DIRECTORY/koide_discrepancy_MAX.json",
    )
    parser.add_argument("--no-roots-file", action="store_true")
    parser.add_argument("--checkpoints", type=int, nargs="*")
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    if args.max_height < 1:
        raise SystemExit("--max-height must be positive")
    checkpoints = (
        args.checkpoints
        if args.checkpoints is not None
        else CANONICAL_CHECKPOINTS + EXTRA_CHECKPOINTS
    )
    payload = produce_report(
        max_height=args.max_height,
        output_directory=args.output_directory.resolve(),
        checkpoints=checkpoints,
        write_roots=not args.no_roots_file,
    )
    result_path = (
        args.result_json.resolve()
        if args.result_json
        else args.output_directory.resolve()
        / f"koide_discrepancy_{args.max_height}.json"
    )
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "result_json": str(result_path),
        "result_json_sha256": sha256_file(result_path),
        "max_height": payload["max_height"],
        "count": payload["count"],
        "total_wall_seconds": payload["total_wall_seconds"],
        "coordinate_file": payload["coordinate_file"],
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
