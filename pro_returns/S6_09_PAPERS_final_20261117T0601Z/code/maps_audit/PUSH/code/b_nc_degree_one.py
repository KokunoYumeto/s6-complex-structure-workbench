#!/usr/bin/env python3
"""Exact branch-simplex identities used in the analytic degree-one proof.

For a monomial on z1...zk=0 only its zero-exponent set matters.
The proof for arbitrary convergent series is in the paper; this program
checks every such support set through k=4 and all branch permutations.
"""
from pathlib import Path
from itertools import combinations, permutations
import json
import sympy as sp


def basis(vertices, degree):
    if degree == -1:
        return [()]
    return list(combinations(sorted(vertices), degree + 1))


def differential(vertices, degree):
    old, new = basis(vertices, degree), basis(vertices, degree + 1)
    matrix = sp.zeros(len(new), len(old))
    lookup = {face: i for i, face in enumerate(old)}
    for j, face in enumerate(new):
        for k in range(len(face)):
            matrix[j, lookup[face[:k] + face[k + 1:]]] = (-1) ** k
    return matrix


def permutation_matrix(vertices, degree, permutation):
    target = tuple(permutation[i] for i in vertices)
    old, new = basis(vertices, degree), basis(target, degree)
    matrix = sp.zeros(len(new), len(old))
    lookup = {face: i for i, face in enumerate(new)}
    for j, face in enumerate(old):
        mapped = tuple(permutation[i] for i in face)
        inversions = sum(mapped[a] > mapped[b]
                         for a in range(len(mapped))
                         for b in range(a + 1, len(mapped)))
        matrix[lookup[tuple(sorted(mapped))], j] = (-1) ** inversions
    return matrix


records = []
permutation_checks = 0
for k in range(1, 5):
    for mask in range(1, 1 << k):
        vertices = tuple(i for i in range(k) if mask & (1 << i))
        m = len(vertices)
        maps = [differential(vertices, p) for p in range(-1, m)]
        ranks = [int(a.rank()) for a in maps]
        for p in range(-1, m):
            previous = 0 if p == -1 else ranks[p]
            following = ranks[p + 1]
            assert previous + following == len(basis(vertices, p))
        for a, b in zip(maps, maps[1:]):
            assert b * a == sp.zeros(b.rows, a.cols)
        for permutation in permutations(range(k)):
            target = tuple(permutation[i] for i in vertices)
            for p in range(-1, m):
                left = differential(target, p) * permutation_matrix(vertices, p, permutation)
                right = permutation_matrix(vertices, p + 1, permutation) * differential(vertices, p)
                assert left == right
                permutation_checks += 1
        records.append({"branches": k, "zero_exponent_indices": vertices,
                        "augmented_differential_ranks": ranks, "exact": True})

result = {"support_cases": len(records), "signed_permutation_checks": permutation_checks,
          "all_exact": True, "records": records,
          "scope": "Finite local simplex identities only; analytic and ddbar arguments are proved in B.4.5."}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k != "records"}, indent=2))
print("PASS: every branch-support complex is exact and all alternating face maps are permutation-equivariant.")
