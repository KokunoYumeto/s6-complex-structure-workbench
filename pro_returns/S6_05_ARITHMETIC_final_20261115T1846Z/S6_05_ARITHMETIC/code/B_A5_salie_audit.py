#!/usr/bin/env python3
"""Exact normalization checks and Arb first moments for the A.5 source audit.

The asymptotic refutation of Biro's printed Conjecture 1 is proved in
records/B_A5_salie_counterexample.tex using Louvel's published Theorem 1.
Finite data here check the changes of variables and the Salié normalization;
they are not offered as a refutation of a big-O statement by themselves.
"""
from math import gcd
from pathlib import Path
import json
import sympy as sp
from flint import arb, ctx

ctx.prec = 192
BASE = Path(__file__).resolve().parents[1]


def jacobi(a, n):
    assert n > 0 and n % 2
    a %= n
    ans = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                ans = -ans
        a, n = n, a
        if a % 4 == n % 4 == 3:
            ans = -ans
        a %= n
    return ans if n == 1 else 0


def salie_coeffs(m, n, c):
    # Biro convention: m*x^{-1}+n*x.
    coeff = [0] * c
    for x in range(c):
        if gcd(x, c) == 1:
            coeff[(m * pow(x, -1, c) + n * x) % c] += jacobi(x, c)
    return coeff


def spf_sieve(N):
    spf = list(range(N + 1))
    for p in range(2, int(N**0.5) + 1):
        if spf[p] == p:
            for n in range(p * p, N + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def roots4(c, spf):
    """All square roots of 4 modulo odd c, using exact CRT."""
    left = c
    modulus = 1
    roots = [0]
    while left > 1:
        p = spf[left]
        pp = 1
        while left % p == 0:
            pp *= p
            left //= p
        inv = pow(modulus, -1, pp)
        roots = [r + modulus * (((s - r) * inv) % pp)
                 for r in roots for s in (2 % pp, (-2) % pp)]
        modulus *= pp
    assert modulus == c
    assert len(roots) == len(set(roots))
    assert all((r * r - 4) % c == 0 for r in roots)
    return roots


def main():
    max_c = 128000
    spf = spf_sieve(max_c)
    # The equality is checked as an equality of integer coefficient vectors,
    # before any root of unity is substituted.
    for c in range(3, 1002, 2):
        assert salie_coeffs(4, pow(4, -1, c), c) == salie_coeffs(1, 1, c)
        assert salie_coeffs(-1,-1,c) == [jacobi(-1,c)*a for a in salie_coeffs(1,1,c)]
        if c <= 501:
            assert sorted(roots4(c, spf)) == [x for x in range(c) if (x*x-4) % c == 0]
    print('PASS: T(4, inverse(4); c)=T(1,1;c), exact cyclic coefficient vectors, all odd 3<=c<=1001')
    print('PASS: T(-1,-1;c)=Jacobi(-1,c)*T(1,1;c), exact cyclic coefficient vectors, all odd 3<=c<=1001')
    print('PASS: CRT roots exhaustive, all odd 3<=c<=501')

    # Exact cyclotomic check T(1,1;c) = G(1;c) sum_{v^2=4(c)} e(v/c).
    X = sp.Symbol('X')
    for c in range(3, 200, 2):
        G = [0] * c
        for y in range(c):
            G[y*y % c] += 1
        product = [0] * c
        for v in roots4(c, spf):
            for k, a in enumerate(G):
                product[(k + v) % c] += a
        delta = [a-b for a,b in zip(product, salie_coeffs(1,1,c))]
        P = sp.Poly.from_list(list(reversed(delta)), X, domain=sp.ZZ)
        Phi = sp.Poly(sp.cyclotomic_poly(c, X), X, domain=sp.ZZ)
        assert P.rem(Phi).is_zero
    print('PASS: Salie/Gauss root formula in Z[X]/Phi_c, all odd 3<=c<=199')

    # g(u)=exp(4-1/((u-1)(2-u))) on (1,2), zero outside.
    # It is a fixed nonnegative C-infinity bump; no floating point input.
    result = []
    twopi = 2 * arb.pi()
    for C in (100, 1000, 10000, 64000):
        sr = {1:arb(0), 3:arb(0)}
        for c in range(C + 1, 2*C):
            if not c % 2:
                continue
            u = arb(c) / C
            g = (4 - 1 / ((u-1)*(2-u))).exp()
            real_normalized_T = sum(((twopi*r/c).cos() for r in roots4(c,spf)), arb(0))
            sr[c % 4] += g * real_normalized_T
        combined = sr[1] + sr[3]
        row = {'C':C,
               'sum_g_T_epsbar_over_sqrtc':str(combined),
               'moment_divided_by_C':str(combined/C),
               'Biro_LHS_r1_real':str(sr[1]/arb(C).sqrt()),
               'Biro_LHS_r3_imag':str(sr[3]/arb(C).sqrt())}
        result.append(row)
        print(json.dumps(row, sort_keys=True))
    (BASE/'records'/'B_A5_salie_audit.json').write_text(json.dumps({
        'precision_bits':ctx.prec,
        'exact_normalization_checks':'PASS',
        'interpretation':'Finite consistency checks only; asymptotic contradiction proved from Louvel Theorem 1.',
        'bump':'exp(4 - 1/((u-1)*(2-u))) for 1<u<2, else 0',
        'data':result},indent=2)+'\n')


if __name__ == '__main__':
    main()
