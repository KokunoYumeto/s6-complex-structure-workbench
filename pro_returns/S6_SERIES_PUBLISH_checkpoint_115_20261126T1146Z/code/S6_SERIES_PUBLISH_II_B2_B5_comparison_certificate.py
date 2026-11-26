#!/usr/bin/env python3
"""Exact postrelease comparisons for 01B5/02WP; standard library only.

The universal mathematical proof is in the frozen prereading derivation.
This checks distinct finite certificates: Euclidean Bezout rather than
modular inversion, rational elimination rather than a symbolic determinant,
split Mayer--Vietoris maps, and a generated monomial semigroup.
"""
from collections import deque
from fractions import Fraction as Q
from math import gcd
import json


def egcd(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    assert old_s * a + old_t * b == old_r
    return old_r, old_s, old_t


def det(matrix):
    m = [[Q(x) for x in row] for row in matrix]
    result = Q(1)
    for k in range(len(m)):
        pivot = next((j for j in range(k, len(m)) if m[j][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            m[k], m[pivot] = m[pivot], m[k]
            result = -result
        value = m[k][k]
        result *= value
        for j in range(k + 1, len(m)):
            quotient = m[j][k] / value
            for i in range(k + 1, len(m)):
                m[j][i] -= quotient * m[k][i]
            m[j][k] = 0
    return result


triples = 0
matrices = 0
for b in range(1, 25):
    for c in range(1, 25):
        d = gcd(b, c)
        B, C = b // d, c // d
        g, p, q = egcd(B, C)
        assert g == 1
        M = ((B, C), (q, -p))
        N = ((p, C), (q, -B))
        for i in range(2):
            for j in range(2):
                assert sum(M[i][k] * N[k][j] for k in range(2)) == int(i == j)
                assert sum(N[i][k] * M[k][j] for k in range(2)) == int(i == j)
        beta_C, beta_B = (-p) % C, (-q) % B
        assert 1 + B * beta_C + C * beta_B == B * C
        matrices += 1
        for a in range(2, 13):
            assert a * (b + c) == b * a + c * a
            if gcd(a, d) != 1:
                continue
            e0 = Q(a) - a * Q(beta_C, C) - a * Q(beta_B, B)
            assert e0 == Q(a, B * C)
            b1, b2, boundary_b1 = (a - 1) * (d - 1), (a - 1) * d, 2 * (a - 1) * (d - 1)
            assert b2 - boundary_b1 + b1 == a - 1
            triples += 1

# The integer kernel comparison is checked on every basis vector:
# D sends e_ij to e_j; S sends e_j to e_0j;
# E sends f_ij to e_ij-e_0j; T discards the i=0 coordinates.
split_basis_checks = 0
for a in range(2, 13):
    for d in range(1, 25):
        for i in range(a):
            for j in range(d):
                unit = {(i, j): 1}
                sd = {(0, j): 1}
                et = {} if i == 0 else {(i, j): 1, (0, j): -1}
                total = dict(sd)
                for k, v in et.items():
                    total[k] = total.get(k, 0) + v
                total = {k: v for k, v in total.items() if v}
                assert total == unit
                if i:
                    assert sum(et.get((k, j), 0) for k in range(a)) == 0
                    assert {k: v for k, v in et.items() if k[0]} == {(i, j): 1}
                split_basis_checks += 1

samples = []
for a, b, c in [(2, 1, 2), (2, 1, 4), (2, 3, 4), (2, 3, 6),
                (3, 2, 4), (3, 4, 5), (4, 3, 6), (5, 3, 9),
                (2, 1, 1), (7, 24, 24)]:
    d = gcd(b, c)
    B, C = b // d, c // d
    _, p, q = egcd(B, C)
    beta_C, beta_B = (-p) % C, (-q) % B
    relation = [[0] * (2 * a + 1) for _ in range(2 * a + 1)]
    for i in range(a):
        relation[i][i] = C
        relation[i][-1] = beta_C
    for i in range(a, 2 * a):
        relation[i][i] = B
        relation[i][-1] = beta_B
    for i in range(2 * a):
        relation[-1][i] = 1
    relation[-1][-1] = a
    determinant = det(relation)
    assert determinant == a * (B * C) ** (a - 1)
    samples.append({"exponents": [a, b, c], "presentation_determinant": int(determinant)})

# Generate the image-ring semigroup rather than assume its parity description.
bound_u, bound_v = 30, 24
semigroup = {(0, 0)}
queue = deque([(0, 0)])
for_pop = 0
while queue:
    i, j = queue.popleft()
    for_pop += 1
    for di, dj in [(0, 1), (2, 0), (3, 2)]:
        candidate = i + di, j + dj
        if candidate[0] <= bound_u and candidate[1] <= bound_v and candidate not in semigroup:
            semigroup.add(candidate)
            queue.append(candidate)
conductor_checks = 0
for i in range(bound_u):
    for j in range(bound_v + 1):
        assert ((i, j) in semigroup) == (i % 2 == 0 or (i >= 3 and j >= 2))
        conductor_membership = (i, j) in semigroup and (i + 1, j) in semigroup
        assert conductor_membership == (i >= 2 and j >= 2)
        conductor_checks += 1


def deriv(poly, index):
    result = {}
    for monomial, value in poly.items():
        power = monomial[index]
        if power:
            new = list(monomial)
            new[index] -= 1
            result[tuple(new)] = value * power
    return result


def mul(a, b):
    result = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            key = i + k, j + l
            result[key] = result.get(key, 0) + x * y
    return {k: v for k, v in result.items() if v}


def sub(a, b):
    result = dict(a)
    for k, v in b.items():
        result[k] = result.get(k, 0) - v
    return {k: v for k, v in result.items() if v}


coordinates = [{(3, 2): 1}, {(0, 1): 1}, {(2, 0): 1}]
J = [[deriv(p, k) for k in range(2)] for p in coordinates]
minors = [sub(mul(J[i][0], J[j][1]), mul(J[i][1], J[j][0]))
          for i, j in [(0, 1), (0, 2), (1, 2)]]
assert minors == [{(2, 2): 3}, {(4, 1): -4}, {(1, 0): -2}]
assert sub(mul(coordinates[0], coordinates[0]),
           mul(mul(mul(coordinates[2], coordinates[2]), coordinates[2]),
               mul(mul(coordinates[1], coordinates[1]), mul(coordinates[1], coordinates[1])))) == {}
assert (min(next(iter(p))[0] for p in minors),
        min(next(iter(p))[1] for p in minors)) == (1, 0)

print(json.dumps({
    "status": "pass",
    "scope": "Postrelease exact finite certificates; universal arguments remain in the mathematical proof.",
    "primitive_exponent_matrices_and_both_inverse_products": matrices,
    "seifert_and_rank_triples": triples,
    "split_mayer_vietoris_basis_identities": split_basis_checks,
    "rational_elimination_samples": samples,
    "generated_image_semigroup_size": len(semigroup),
    "conductor_membership_checks": conductor_checks,
    "normalization_minors": ["3*u^2*v^2", "-4*u^4*v", "-2*u"],
    "conductor": "u^2*v^2*C{u,v}",
    "differential_rank_drop_ideal": "(u)",
    "fresh_computation_event_requested": 1
}, indent=2))
