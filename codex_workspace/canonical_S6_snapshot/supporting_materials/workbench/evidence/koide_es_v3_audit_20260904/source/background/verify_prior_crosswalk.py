#!/usr/bin/env python3
"""Exact bounded verification for the Erdős--Straus / Koide / S6 crosswalk.

All arithmetic assertions use Python integers and fractions.  The bound is not
part of any theorem; it is a reproducibility check for the symbolic formulas.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def factor(n: int) -> Dict[int, int]:
    out: Dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors(n: int) -> List[int]:
    ds = [1]
    for p, e in factor(n).items():
        ds = [d * p**k for d in ds for k in range(e + 1)]
    return sorted(ds)


def primitive_rank_one(a: int, u: int) -> Tuple[int, int, int, int]:
    """Return h,r,s,v with u=h r^2, a=h r s, v=h s^2, gcd(r,s)=1."""
    assert a > 0 and u > 0 and a * a % u == 0
    g = math.gcd(a, u)
    r = u // g
    s = a // g
    assert math.gcd(r, s) == 1
    assert g % r == 0
    h = g // r
    v = a * a // u
    assert u == h * r * r
    assert a == h * r * s
    assert v == h * s * s
    return h, r, s, v


def matmul2(A: Tuple[Tuple[int, int], Tuple[int, int]],
            B: Tuple[Tuple[int, int], Tuple[int, int]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    return (
        (A[0][0] * B[0][0] + A[0][1] * B[1][0],
         A[0][0] * B[0][1] + A[0][1] * B[1][1]),
        (A[1][0] * B[0][0] + A[1][1] * B[1][0],
         A[1][0] * B[0][1] + A[1][1] * B[1][1]),
    )


def det2(A: Tuple[Tuple[int, int], Tuple[int, int]]) -> int:
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def matmul3(A, B):
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def transpose3(A):
    return tuple(tuple(A[j][i] for j in range(3)) for i in range(3))


def det3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def verify_state(p: int, eps: int, j: int, u: int) -> dict:
    R = 4 * j + 3
    a = (p + R) // 4
    pe = p**eps
    assert (p + R) % 4 == 0
    assert math.gcd(R, p) == math.gcd(R, a) == math.gcd(p, a) == 1
    assert u > 0 and a * a % u == 0
    assert (4 * u + pe) % R == 0

    T = (4 * u + pe) // R
    assert T > 0 and T % 4 == 3
    ell0 = (T + 1) // 4
    ell1 = u - j * T
    ell2 = 1
    lam = 12 * ell0 - 4 * ell1 - 3 * ell2
    assert lam == pe
    assert ell2 % 2 == 1
    assert ell1 % 3 != 0

    A = ((R, -u), (4, -T))
    Uj = ((1, -j), (0, 1))
    Rterm = ((3, -ell1), (4, 1 - 4 * ell0))
    assert matmul2(Uj, A) == Rterm
    assert det2(A) == det2(Rterm) == -pe
    assert math.gcd(*(abs(x) for row in Rterm for x in row), pe) == 1

    h, r, s, v = primitive_rank_one(a, u)
    Gamma = ((u, a), (a, v))
    assert det2(Gamma) == 0
    assert Gamma == ((h * r * r, h * r * s), (h * r * s, h * s * s))

    # Native S6 Gram coefficient map: (t,m,b)=(u/2,a/2,3v).
    t = Fraction(u, 2)
    m = Fraction(a, 2)
    b_s6 = 3 * v
    G = ((2 * t, 2 * m), (2 * m, Fraction(b_s6, 3)))
    assert G == ((Fraction(u), Fraction(a)), (Fraction(a), Fraction(v)))
    assert t * b_s6 - 6 * m * m == 0

    # Raw-period dictionary: (Traw,Mraw,Braw)=(u,a/sqrt(6),v).
    # We check the rational discriminant after storing Mraw^2=a^2/6.
    assert u * v - 6 * Fraction(a * a, 6) == 0

    # Exact primitive channel congruences.
    E = (4 * u + 1) % R == 0
    M = (4 * u + p) % R == 0
    assert E == ((p * r + s) % R == 0)
    assert M == ((r + s) % R == 0)
    assert (eps == 0 and E) or (eps == 1 and M)

    N = p * a
    if eps == 0:
        kappa_num = p * r + s
        assert kappa_num % R == 0
        kappa = kappa_num // R
        den = (a, p * h * r * kappa, h * s * kappa)
        d = p * p * u
        e = v
        shell = ((d, N), (N, e))
        C = ((p, 0), (0, 1))
        assert matmul2(matmul2(C, Gamma), C) == shell
        zeta_expected = -Fraction(p * r * s, (p * r + s) ** 2)
    else:
        kappa_num = r + s
        assert kappa_num % R == 0
        kappa = kappa_num // R
        den = (a, p * h * r * kappa, p * h * s * kappa)
        d = p * u
        e = p * v
        shell = ((d, N), (N, e))
        assert shell == tuple(tuple(p * x for x in row) for row in Gamma)
        zeta_expected = -Fraction(r * s, (r + s) ** 2)

    assert det2(shell) == d * e - N * N == 0
    bden, cden = den[1], den[2]
    assert Fraction(4, p) == Fraction(1, den[0]) + Fraction(1, bden) + Fraction(1, cden)
    assert bden == (N + d) // R or bden == (N + e) // R
    assert cden == (N + e) // R or cden == (N + d) // R
    assert {bden, cden} == {(N + d) // R, (N + e) // R}

    # Sarnak null coordinates and quarter coordinate.
    Ts = Fraction(d + e, 2)
    Xs = N
    Ws = Fraction(d - e, 2)
    assert Xs * Xs + Ws * Ws - Ts * Ts == 0
    zeta = -Fraction(bden * cden, (bden + cden) ** 2)
    assert zeta == -Fraction(1, 4) + Fraction(1, 4) * (Ws / (Ts + Xs)) ** 2
    assert zeta == zeta_expected
    assert zeta != -Fraction(1, 4)

    # Source K formula.
    K = (p ** (1 - eps) * T + 1) // 4
    assert (p ** (1 - eps) * T + 1) % 4 == 0
    source_den = (a, pe * a * K // u, p * K)
    assert sorted(source_den[1:]) == sorted(den[1:])

    # Double-certificate inverse.
    u2 = Gamma[0][0]
    a2 = Gamma[0][1]
    T2 = -Rterm[1][1]
    ell12 = -Rterm[0][1]
    assert T2 == T and u2 == u and a2 == a and ell12 == ell1
    assert (u2 - ell12) % T2 == 0
    j2 = (u2 - ell12) // T2
    p2 = 4 * a2 - (4 * j2 + 3)
    lam2 = -det2(Rterm)
    eps2 = 0 if lam2 == 1 else 1
    assert (p2, eps2, j2, u2) == (p, eps, j, u)
    assert lam2 == p2**eps2

    return {
        'p': p, 'epsilon': eps, 'j': j, 'R': R, 'a': a, 'u': u, 'v': v,
        'h': h, 'r': r, 's': s, 'T': T,
        'ell': [ell0, ell1, ell2],
        'terminal_matrix': [list(Rterm[0]), list(Rterm[1])],
        'gamma': [list(Gamma[0]), list(Gamma[1])],
        'denominators': list(den),
        'quarter_coordinate': str(zeta),
        'overlap': E and M,
    }


def selector_solution_set(p: int) -> set[tuple[int, int, int]]:
    out: set[tuple[int, int, int]] = set()
    for j in range((p - 1) // 4):
        R = 4 * j + 3
        a = (p + R) // 4
        for u in divisors(a * a):
            if (4 * u + 1) % R == 0:
                out.add(tuple(sorted(verify_state(p, 0, j, u)['denominators'])))
            if (4 * u + p) % R == 0:
                out.add(tuple(sorted(verify_state(p, 1, j, u)['denominators'])))
    return out


def direct_factor_shell_solution_set(p: int) -> set[tuple[int, int, int]]:
    out: set[tuple[int, int, int]] = set()
    for j in range((p - 1) // 4):
        R = 4 * j + 3
        a = (p + R) // 4
        N = p * a
        for d in divisors(N * N):
            if (d + N) % R != 0:
                continue
            e = N * N // d
            assert (e + N) % R == 0
            y = (N + d) // R
            z = (N + e) // R
            triple = tuple(sorted((a, y, z)))
            assert triple[0] == a
            assert Fraction(4, p) == sum(Fraction(1, x) for x in triple)
            out.add(triple)
    return out


def run(bound: int) -> dict:
    # Rational Koide reflection W_K and its exact quadratic-form invariance.
    W = (
        (Fraction(2, 3), Fraction(2, 3), Fraction(-1, 3)),
        (Fraction(2, 3), Fraction(-1, 3), Fraction(2, 3)),
        (Fraction(-1, 3), Fraction(2, 3), Fraction(2, 3)),
    )
    I3 = tuple(tuple(Fraction(int(i == j)) for j in range(3)) for i in range(3))
    AQ = tuple(
        tuple(Fraction(2, 3) - Fraction(int(i == j)) for j in range(3))
        for i in range(3)
    )
    assert matmul3(W, W) == I3
    assert matmul3(transpose3(W), W) == I3
    assert det3(W) == -1
    assert matmul3(matmul3(transpose3(W), AQ), W) == AQ

    primes = [p for p in range(5, bound + 1) if p % 4 == 1 and is_prime(p)]
    states: List[dict] = []
    counts_by_prime = {}
    extension_primes = []
    terminal_collisions = defaultdict(list)
    pair_seen = {}

    for p in primes:
        L = (p - 1) // 4
        pc = {'E': 0, 'M': 0, 'overlap': 0}
        shell_sets = {}
        if p % 12 == 5:
            extension_primes.append(p)
        for j in range(L):
            R = 4 * j + 3
            a = (p + R) // 4
            for u in divisors(a * a):
                E = (4 * u + 1) % R == 0
                M = (4 * u + p) % R == 0
                if not (E or M):
                    continue
                if E:
                    st = verify_state(p, 0, j, u)
                    states.append(st); pc['E'] += 1
                if M:
                    st = verify_state(p, 1, j, u)
                    states.append(st); pc['M'] += 1
                if E and M:
                    pc['overlap'] += 1
                    h, r, s, _ = primitive_rank_one(a, u)
                    assert (p - 1) % R == 0
                    assert (r + s) % R == 0

            Eset = {u for u in divisors(a * a) if (4 * u + 1) % R == 0}
            Mset = {u for u in divisors(a * a) if (4 * u + p) % R == 0}
            shell_sets[j] = (Eset, Mset)
            for u in Mset:
                vv = a * a // u
                assert vv in Mset
                assert vv != u
            for u in Eset:
                vv = a * a // u
                assert (vv in Eset) == ((p * p - 1) % R == 0)
            assert ((a in Eset) == ((p + 1) % R == 0))
        counts_by_prime[str(p)] = pc

    for st in states:
        term = tuple(tuple(row) for row in st['terminal_matrix'])
        gamma = tuple(tuple(row) for row in st['gamma'])
        key = (gamma, term)
        state_key = (st['p'], st['epsilon'], st['j'], st['u'])
        assert key not in pair_seen or pair_seen[key] == state_key
        pair_seen[key] = state_key
        terminal_collisions[term].append(state_key)

    collisions = {
        str(k): v for k, v in terminal_collisions.items()
        if len(set(v)) > 1
    }

    sorted_solutions = {
        (st['p'], tuple(sorted(st['denominators'])))
        for st in states
    }
    quotient_count = sum(
        c['E'] + c['M'] // 2 for c in counts_by_prime.values()
    )
    assert all(c['M'] % 2 == 0 for c in counts_by_prime.values())
    assert len(sorted_solutions) == quotient_count

    # Required worked examples.
    examples = {}
    for target in [(13, 0, 0, 2), (13, 0, 1, 5), (13, 1, 0, 2), (5, 0, 0, 2)]:
        match = next(st for st in states if (st['p'], st['epsilon'], st['j'], st['u']) == target)
        examples['-'.join(map(str, target))] = match

    independent_bound = min(bound, 1000)
    independent_primes = [
        p for p in range(5, independent_bound + 1)
        if p % 4 == 1 and is_prime(p)
    ]
    for p in independent_primes:
        assert selector_solution_set(p) == direct_factor_shell_solution_set(p)

    hard_primes_without_selector = [
        p for p in primes
        if p % 12 == 1 and counts_by_prime[str(p)]['E'] + counts_by_prime[str(p)]['M'] == 0
    ]

    # Integer anisotropy check is only a bounded receipt; the paper contains the proof.
    anisotropic_nonzero = []
    for ss in range(-100, 101):
        for uu in range(-100, 101):
            rhs = 2 * ss * ss - 3 * uu * uu
            if rhs < 0:
                continue
            vv = math.isqrt(rhs)
            if vv * vv == rhs and (ss, uu, vv) != (0, 0, 0):
                anisotropic_nonzero.append([ss, uu, vv])
    assert not anisotropic_nonzero

    return {
        'bound': bound,
        'prime_count_p_1_mod_4': len(primes),
        'state_count_with_channel_tags': len(states),
        'distinct_double_certificates': len(pair_seen),
        'distinct_sorted_solution_triples': len(sorted_solutions),
        'selector_quotient_count_E_plus_M_over_2': quotient_count,
        'terminal_matrix_collision_classes': len(collisions),
        'koide_reflection_matrix': [[str(x) for x in row] for row in W],
        'koide_reflection_exact_checks': {
            'W_squared_is_identity': True,
            'W_orthogonal': True,
            'determinant': -1,
            'preserves_QK_matrix': True,
        },
        'primes_p_5_mod_12_checked': extension_primes,
        'hard_primes_p_1_mod_12_without_selector_through_bound': hard_primes_without_selector,
        'independent_factor_shell_crosscheck_bound': independent_bound,
        'independent_factor_shell_primes_checked': len(independent_primes),
        'independent_factor_shell_crosscheck': 'PASS',
        'counts_by_prime': counts_by_prime,
        'examples': examples,
        'bounded_rational_anisotropy_search_box': 100,
        'bounded_nonzero_solutions_to_2s2_3u2_v2': anisotropic_nonzero,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--bound', type=int, default=2000)
    ap.add_argument('--output', type=Path, default=Path('verification_results.json'))
    args = ap.parse_args()
    result = run(args.bound)
    args.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({
        'bound': result['bound'],
        'prime_count': result['prime_count_p_1_mod_4'],
        'state_count': result['state_count_with_channel_tags'],
        'double_certificates': result['distinct_double_certificates'],
        'sorted_solution_triples': result['distinct_sorted_solution_triples'],
        'terminal_collision_classes': result['terminal_matrix_collision_classes'],
    }, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
