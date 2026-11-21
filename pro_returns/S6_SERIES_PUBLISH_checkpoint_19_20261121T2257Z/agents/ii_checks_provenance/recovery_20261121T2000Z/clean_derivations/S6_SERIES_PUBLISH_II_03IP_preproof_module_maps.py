"""Exact graded coefficient maps, authored before releasing 03IP.

This computes homogeneous coefficient-map ranks by rational elimination.
It is finite corroboration; the separate analytic divisibility proof proves
the asserted kernels in the convergent power-series rings in every degree.
No target proof or prior computational routine was read for this program.
"""
from fractions import Fraction
from math import comb
import json


def mons(d):
    return [(a, b, d-a-b) for a in range(d+1) for b in range(d-a+1)]


def rank(matrix):
    a = [[Fraction(v) for v in row] for row in matrix]
    h = 0
    for k in range(len(a[0]) if a else 0):
        p = next((j for j in range(h, len(a)) if a[j][k]), None)
        if p is None:
            continue
        a[h], a[p] = a[p], a[h]
        v = a[h][k]
        a[h] = [x/v for x in a[h]]
        for j in range(h+1, len(a)):
            v = a[j][k]
            if v:
                a[j] = [x-v*y for x, y in zip(a[j], a[h])]
        h += 1
        if h == len(a):
            break
    return h


def matrix(d, triple):
    domain = mons(d)
    codomain = mons(d+1)
    lookup = {m: i for i, m in enumerate(codomain)}
    components = 2 if triple else 1
    generators = 3 if triple else 2
    a = [[0]*(generators*len(domain)) for _ in range(components*len(codomain))]
    for j, m in enumerate(domain):
        for g in range(generators):
            axis = g
            n = list(m)
            n[axis] += 1
            k = lookup[tuple(n)]
            if not triple:
                a[k][g*len(domain)+j] += 1 if g == 0 else -1
            elif g < 2:
                a[g*len(codomain)+k][g*len(domain)+j] += 1
            else:
                for component in range(2):
                    a[component*len(codomain)+k][g*len(domain)+j] -= 1
    return a, generators*len(domain)


out = []
for d in range(8):
    a, n = matrix(d, False)
    double_kernel = n-rank(a)
    a, n = matrix(d, True)
    triple_kernel = n-rank(a)
    expected_double = comb(d+1, 2) if d >= 1 else 0
    expected_triple = comb(d, 2) if d >= 2 else 0
    assert double_kernel == expected_double
    assert triple_kernel == expected_triple
    out.append({"coefficient_degree": d,
                "double_kernel_dimension": double_kernel,
                "double_generator": "(y,x) times degree d-1",
                "triple_kernel_dimension": triple_kernel,
                "triple_generator": "(yz,xz,xy) times degree d-2"})

multiple = []
for m in range(2, 10):
    # Multiplication by m*s^(m-1) on C[s]/s^N, N >= 2m.
    N = 2*m+1
    a = [[0]*N for _ in range(N)]
    for j in range(N-m+1):
        a[j+m-1][j] = m
    coker = N-rank(a)
    assert coker == m-1
    multiple.append({"m": m, "truncation": N,
                     "ds_quotient_basis": list(range(m-1)),
                     "cokernel_dimension": coker})

print(json.dumps({"method": "homogeneous coefficient matrices and exact Fraction elimination",
                  "timing": "before 03IP target-proof release",
                  "crossing_maps": out,
                  "multiple_fibre_truncations": multiple,
                  "all_degree_and_all_m_scope": "proved by analytic divisibility in the frozen derivation; finite output is corroboration"}, indent=2))
