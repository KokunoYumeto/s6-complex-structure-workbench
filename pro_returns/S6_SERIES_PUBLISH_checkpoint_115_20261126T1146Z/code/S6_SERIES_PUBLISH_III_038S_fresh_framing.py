#!/usr/bin/env python3
"""Exact polynomial check of the ordered toric normal framing and its dual.

Variables a,b,c,d are the entries of Y0. Variables z1,z2 are the
radial shear coefficients (B0 u0)/(2 pi r0). This verifies the sign
and both inverse identities for the cap frame, before target exposure.
It asserts no chart embedding or topological classification.
"""
from datetime import datetime, timezone
from fractions import Fraction

N = 6
ZERO = {}


def const(n):
    return {} if n == 0 else {(0,)*N: Fraction(n)}


def variable(i):
    e = [0]*N
    e[i] = 1
    return {tuple(e): Fraction(1)}


def add(*polys):
    result = {}
    for p in polys:
        for monomial, coefficient in p.items():
            result[monomial] = result.get(monomial, 0)+coefficient
    return {m: c for m, c in result.items() if c}


def neg(p):
    return {m: -c for m, c in p.items()}


def mul(p, q):
    result = {}
    for m, a in p.items():
        for n, b in q.items():
            t = tuple(x+y for x, y in zip(m, n))
            result[t] = result.get(t, 0)+a*b
    return {m: c for m, c in result.items() if c}


def mmul(A, B):
    return [[add(*(mul(A[i][k], B[k][j]) for k in range(3)))
             for j in range(3)] for i in range(3)]


a, b, c, d, z1, z2 = [variable(i) for i in range(N)]
one = const(1)
delta = add(mul(a, d), neg(mul(b, c)))
frame = [[one, ZERO, ZERO], [neg(z1), a, b], [neg(z2), c, d]]
scaled_coframe = [
    [delta, ZERO, ZERO],
    [add(mul(d, z1), neg(mul(b, z2))), d, neg(b)],
    [add(neg(mul(c, z1)), mul(a, z2)), neg(c), a],
]
target = [[delta if i == j else ZERO for j in range(3)] for i in range(3)]
assert mmul(scaled_coframe, frame) == target
assert mmul(frame, scaled_coframe) == target

# Determinant expansion uses the actual ordered three columns.
det = add(mul(frame[0][0], add(mul(frame[1][1], frame[2][2]),
                                  neg(mul(frame[1][2], frame[2][1])))),
          neg(mul(frame[0][1], add(mul(frame[1][0], frame[2][2]),
                                   neg(mul(frame[1][2], frame[2][0]))))),
          mul(frame[0][2], add(mul(frame[1][0], frame[2][1]),
                              neg(mul(frame[1][1], frame[2][0])))))
assert det == delta

B0 = ((0, 1), (-1, 0))
u0 = (Fraction(-1, 4), Fraction(1, 4))
p0 = tuple(sum(Fraction(B0[i][j])*u0[j] for j in range(2)) for i in range(2))
assert p0 == (Fraction(1, 4), Fraction(1, 4))
assert B0[0][0]*B0[1][1]-B0[0][1]*B0[1][0] == 1

print('UTC:', datetime.now(timezone.utc).isoformat())
print('Exact coefficient ring: Q[a,b,c,d,z1,z2]')
print('Delta = a*d-b*c')
print('Frame columns: (1,-z1,-z2), (0,a,c), (0,b,d)')
print('Scaled coframe times frame = Delta I3: all nine polynomial entries verified')
print('Frame times scaled coframe = Delta I3: all nine polynomial entries verified')
print('Ordered determinant of frame = Delta: verified as a polynomial identity')
print('B0(-1/4,1/4)=(1/4,1/4); det B0=1: exact rational check')
print('No numerical sampling, chart-embedding claim, or extra required-check event.')
