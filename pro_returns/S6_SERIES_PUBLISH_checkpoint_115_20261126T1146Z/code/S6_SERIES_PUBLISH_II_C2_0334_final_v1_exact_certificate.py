#!/usr/bin/env python3
"""Integral splitting and Laurent-monomial certificates for E.2.19.

This certificate uses integer compositions and explicit inverse monomials.
It does not solve a rational nullspace or invert a matrix by an algorithm.
The analytic descent, base change and flow arguments are proved in the paper.
"""
import json
from pathlib import Path


def multiply(a, b):
    assert len(a[0]) == len(b)
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


# Coordinates are (gamma,u,w,delta).  N(v)=J(K(v)); the maps J,L,K,S
# exhibit Z^4 = im(J) direct-sum im(S), rather than just a Q-basis.
J = [[0, 0], [0, 0], [1, 0], [0, 1]]
L = [[0, 0, 1, 0], [0, 0, 0, 1]]
K = [[0, 1, 0, 0], [-1, 0, 0, 0]]
S = [[0, -1], [1, 0], [0, 0], [0, 0]]
N = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [-1, 0, 0, 0]]
assert multiply(L, J) == identity(2)
assert multiply(K, S) == identity(2)
assert multiply(K, J) == [[0, 0], [0, 0]]
assert multiply(L, S) == [[0, 0], [0, 0]]
assert add(multiply(J, L), multiply(S, K)) == identity(4)
assert multiply(J, K) == N

# Rows of X give the three chart coordinates as Laurent monomials in
# (z,w,q). Rows of Y give (z,w,q) as monomials in the chart coordinates.
cones = [
    {
        "rays": [[0, 0, 1], [1, 0, 1], [0, 1, 1]],
        "chart_coordinate_monomials": ["q/(z*w)", "z", "w"],
        "inverse_monomials": ["X1", "X2", "X0*X1*X2"],
        "X": [[-1, -1, 1], [1, 0, 0], [0, 1, 0]],
        "Y": [[0, 1, 0], [0, 0, 1], [1, 1, 1]],
        "expected_weights": [[1, 0], [0, 1], [-1, -1]],
    },
    {
        "rays": [[1, 0, 1], [0, 1, 1], [1, 1, 1]],
        "chart_coordinate_monomials": ["q/w", "q/z", "z*w/q"],
        "inverse_monomials": ["X0*X2", "X1*X2", "X0*X1*X2"],
        "X": [[0, -1, 1], [-1, 0, 1], [1, 1, -1]],
        "Y": [[1, 0, 1], [0, 1, 1], [1, 1, 1]],
        "expected_weights": [[-1, 0], [0, -1], [1, 1]],
    },
]
records = []
for cone in cones:
    X, Y = cone["X"], cone["Y"]
    # These are both exact monomial compositions. Integral inverses prove
    # lattice isomorphism and determinant +/-1 without a matrix inversion.
    assert multiply(X, Y) == identity(3)
    assert multiply(Y, X) == identity(3)
    ray_columns = [list(row) for row in zip(*cone["rays"])]
    assert Y == ray_columns
    assert multiply(X, ray_columns) == identity(3)
    assert [sum(row[j] for row in X) for j in range(3)] == [0, 0, 1]
    weights = [row[:2] for row in X]
    assert sorted(weights) == sorted(cone["expected_weights"])
    assert all(weight != [0, 0] for weight in weights)
    assert [sum(weight[j] for weight in weights) for j in range(2)] == [0, 0]
    pair_inverse_witnesses = []
    for i in range(3):
        for j in range(i + 1, 3):
            a, b = weights[i]
            c, d = weights[j]
            determinant = a * d - b * c
            assert determinant in (-1, 1)
            inverse = [[d * determinant, -b * determinant],
                       [-c * determinant, a * determinant]]
            assert multiply([weights[i], weights[j]], inverse) == identity(2)
            assert multiply(inverse, [weights[i], weights[j]]) == identity(2)
            pair_inverse_witnesses.append({"indices": [i, j], "inverse": inverse})
    records.append({key: value for key, value in cone.items() if key != "expected_weights"}
                   | {"vertical_characters": weights,
                      "pair_inverse_witnesses": pair_inverse_witnesses})

result = {
    "status": "PASS",
    "method": "Explicit Z-module splitting and two-sided Laurent-monomial compositions",
    "integral_splitting": {"J": J, "L": L, "K": K, "S": S, "N": N},
    "invariant_period_basis_gamma_u_w_delta": [[0, 0, 1, 0], [0, 0, 0, 1]],
    "conclusion": "ker(N)=im(J)=Z*w direct-sum Z*delta, primitive in Z^4",
    "triple_point_character_records": records,
    "scope": "Exact integral lattice and toric characters; analytic assertions are checked in the written proof comparison.",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
