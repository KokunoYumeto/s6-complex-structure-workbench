"""Exact-integer checks for the HNF/Pell parametrization in the memo.

This is verification evidence, not a substitute for the proofs in the TeX file.
It uses no floating-point arithmetic.
"""

from collections import Counter
from math import gcd, isqrt


def chi12(d: int) -> int:
    r = d % 12
    if r in (1, 11):
        return 1
    if r in (5, 7):
        return -1
    return 0


def divisors(m: int):
    lo = []
    hi = []
    for d in range(1, isqrt(m) + 1):
        if m % d == 0:
            lo.append(d)
            if d * d != m:
                hi.append(m // d)
    return lo + hi[::-1]


def rho(m: int) -> int:
    return sum(chi12(d) for d in divisors(m))


def hnf_parameters(m: int):
    out = []
    for c in range(1, isqrt(m) + 1):
        if m % (c * c):
            continue
        d = m // (c * c)
        for e in range(d):
            if (e * e - 3) % d == 0:
                out.append((c, d, e))
    return out


def hnf_seed(parameter):
    c, d, e = parameter
    candidates = []
    for b in range(isqrt(d - 1) + 1):
        a2 = d + 3 * b * b
        a = isqrt(a2)
        if a * a == a2 and a > 2 * b and (a - e * b) % d == 0:
            candidates.append((c * a, c * b))
    assert len(candidates) == 1, (parameter, candidates)
    return candidates[0]


def forward_hnf(a: int, q: int):
    c = gcd(a, q)
    aa, bb = a // c, q // c
    d = aa * aa - 3 * bb * bb
    if d == 1:
        e = 0
    else:
        assert gcd(bb, d) == 1
        e = aa * pow(bb, -1, d) % d
    return c, d, e


def descend(a: int, q: int):
    steps = 0
    norm = a * a - 3 * q * q
    while a <= 2 * q:
        a, q = 2 * a - 3 * q, 2 * q - a
        steps += 1
        assert a > 0 and q >= 0 and a * a - 3 * q * q == norm
    return a, q, steps


def orbit_count(X: int) -> int:
    total = 0
    # The n=0 seed (1,1) starts at k=1, namely (5,3).
    a, q = 5, 3
    while 4 * a <= X:
        total += 1
        a, q = 2 * a + 3 * q, a + 2 * q
    for n in range(1, X // 17 + 1):
        m = 18 * n * n - 2
        for parameter in hnf_parameters(m):
            a, q = hnf_seed(parameter)
            while 4 * a + 17 * n <= X:
                assert a + 4 * n > q
                total += 1
                a, q = 2 * a + 3 * q, a + 2 * q
    return total


def brute_count(X: int) -> int:
    total = 0
    for n in range(X // 17 + 1):
        y = (X - 17 * n) // 4
        for q in range(y + 1):
            a2 = 3 * q * q + 18 * n * n - 2
            if a2 <= 0:
                continue
            a = isqrt(a2)
            if a * a == a2 and a <= y and a + 4 * n > q:
                total += 1
    return total


def main():
    for n in range(1, 201):
        m = 18 * n * n - 2
        params = hnf_parameters(m)
        assert len(params) == rho(m)
        assert rho(m) == rho(3 * n - 1) * rho(3 * n + 1)
        seeds = [hnf_seed(p) for p in params]
        assert len(seeds) == len(set(seeds))
        for p, (a, q) in zip(params, seeds):
            assert a * a - 3 * q * q == m
            assert a > 2 * q >= 0
            assert forward_hnf(a, q) == p
            aa, qq = 2 * a + 3 * q, a + 2 * q
            assert descend(aa, qq) == (a, q, 1)

    values = {}
    for X in (0, 19, 20, 50, 160, 1000, 5000):
        via_orbits = orbit_count(X)
        via_brute = brute_count(X)
        assert via_orbits == via_brute, (X, via_orbits, via_brute)
        values[X] = via_orbits

    print("verified n=1..200: HNF count, divisor factorization, seeds, inverse")
    print("verified exact counts:", values)


if __name__ == "__main__":
    main()
