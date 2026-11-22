"""Exact formal contraction on all sixteen exterior basis vectors.

This code is written before opening the target proof.  It proves the
identity for generic symbolic monodromy differences, with a0 invertible.
Any nonzero character coordinate is moved to position zero by permutation.
"""
import json
import sympy as s
a = s.symbols('a0:4')

def add(out, key, val):
    out[key] = s.expand(out.get(key, 0) + val)

def d(v):
    out = {}
    for mask, c in v.items():
        for j in range(4):
            if not mask & (1 << j):
                sign = (-1)**sum(bool(mask & (1 << k)) for k in range(j))
                add(out, mask | (1 << j), c * sign * a[j])
    return out

def h(v):
    return {mask ^ 1: c / a[0] for mask, c in v.items() if mask & 1}

for mask in range(16):
    lhs = d(h({mask: 1}))
    for key, val in h(d({mask: 1})).items():
        add(lhs, key, val)
    assert all(s.cancel(lhs.get(key, 0) - int(key == mask)) == 0 for key in range(16))

print(json.dumps({"method": "formal exterior-basis operator identity",
 "coefficient_field": "Q(a0,a1,a2,a3)", "identity": "d h + h d = identity",
 "basis_vectors_checked_exhaustively": 16,
 "homotopy": "interior_product_e0 / a0",
 "transport": "permute any nonzero monodromy-difference coordinate into position zero",
 "cohomology_dimensions": [0, 0, 0, 0, 0]}, indent=2))
