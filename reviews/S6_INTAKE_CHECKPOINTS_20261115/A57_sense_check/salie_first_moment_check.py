"""Sense check of S6_05 Statement A.5.7 (15 Nov 2026, main session, Claude Opus 5.5 at effort max): do sums of
Salie sums T(1,1;c)/sqrt(c) over c = 1 mod 4 grow linearly, as Louvel's Theorem 1.1 (D = f = m = n = 1) predicts
((4/pi^2) U for c = 1 mod 4; (8/pi^2) U for all odd c with the factor conj(eps_c)), and is T(4, 4bar; c) = T(1,1;c)?
Biro's conventions: T(m,n;c) = sum over x mod c, gcd(x,c)=1, of (x/c) e((m xbar + n x)/c), c odd.
Direct computation, no closed formula used. usage: python -I -B salie_first_moment_check.py [U]"""
import math
import sys

import numpy as np


def factor(c):
    f, d = {}, 3
    while d * d <= c:
        while c % d == 0:
            f[d] = f.get(d, 0) + 1
            c //= d
        d += 2
    if c > 1:
        f[c] = f.get(c, 0) + 1
    return f


def powmod(a, e, m):
    a = a.astype(np.int64) % m
    r = np.ones_like(a)
    while e:
        if e & 1:
            r = (r * a) % m
        a = (a * a) % m
        e >>= 1
    return r


def T(m, n, c):
    if c == 1:
        return 1.0 + 0j
    f = factor(c)
    x = np.arange(c, dtype=np.int64)
    jac = np.ones(c, dtype=np.int64)
    for p, k in f.items():
        leg = powmod(x % p, (p - 1) // 2, p)
        leg = np.where(leg == 1, 1, np.where(leg == 0, 0, -1))
        jac = jac * (leg ** k)
    units = np.gcd(x, c) == 1
    phi = c
    for p in f:
        phi = phi // p * (p - 1)
    xs = x[units]
    xbar = powmod(xs, phi - 1, c)
    return complex(np.sum(jac[units] * np.exp(2j * np.pi * ((m * xbar + n * xs) % c) / c)))


U = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
# 1. T(4, 4bar; c) = T(1,1;c) for odd c
worst = 0.0
for c in range(3, 400, 2):
    i4 = pow(4, -1, c)
    worst = max(worst, abs(T(4, i4, c) - T(1, 1, c)))
print(f"max |T(4,4bar;c) - T(1,1;c)| over odd 3 <= c < 400: {worst:.2e}")
# 2. first moments
a1 = 0.0 + 0j      # sum over c = 1 mod 4 of T(1,1;c)/sqrt(c)
aodd = 0.0 + 0j    # sum over odd c of T(1,1;c) conj(eps_c)/sqrt(c)
marks = {U // 8, U // 4, U // 2, U}
for c in range(1, U + 1, 2):
    t = T(1, 1, c) / math.sqrt(c)
    eps = 1 if c % 4 == 1 else 1j
    aodd += t * np.conj(eps)
    if c % 4 == 1:
        a1 += t
    for u in marks:
        if c in (u, u - 1):
            print(f"U={u:6d}  A_1/U = {a1.real / u:.4f} (imag {a1.imag:.1e})   A_odd/U = {aodd.real / u:.4f} "
                  f"(imag {aodd.imag:.1e})")
print(f"Louvel: A_1/U -> 4/pi^2 = {4 / math.pi ** 2:.4f}, A_odd/U -> 8/pi^2 = {8 / math.pi ** 2:.4f}; "
      f"Biro's conjecture would force A_1 = O(U^(1/2+e)), i.e. A_1/U -> 0")
