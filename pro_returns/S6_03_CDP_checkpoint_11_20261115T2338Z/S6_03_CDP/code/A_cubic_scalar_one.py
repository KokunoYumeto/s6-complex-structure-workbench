"""Exact Newton and attachment budgets for C.2.RAT.8.

The non-ADE local branch is a cusp with two transverse smooth branches.
The two compact Newton facets of its cubic suspension are checked exactly.
"""
from fractions import Fraction as Q
from itertools import product

support = [(0, 0, 3), (3, 1, 0), (2, 2, 0), (1, 4, 0), (0, 5, 0)]
facets = [(Q(1, 4), Q(1, 4), Q(1, 3)),
          (Q(3, 10), Q(1, 5), Q(1, 3))]


def weight(point, normal):
    return sum(a * b for a, b in zip(point, normal))


for normal in facets:
    assert all(weight(point, normal) >= 1 for point in support)
    face = [point for point in support if weight(point, normal) == 1]
    assert len(face) == 3
    print("Facet weights:", normal, "vertices:", face)

lower = [point for point in product(range(1, 13), repeat=3)
         if any(weight(point, normal) <= 1 for normal in facets)]
assert lower == [(1, 1, 1)]
noncompact = (Q(0), Q(1), Q(1, 3))
assert all(weight(point, noncompact) >= 1 for point in support)
assert weight((1, 1, 1), noncompact) > 1
print("Cusp plus two transverse branches: positive lower lattice points", lower)

ordinary_four = (Q(1, 4), Q(1, 4), Q(1, 3))
lower_four = [point for point in product(range(1, 13), repeat=3)
              if weight(point, ordinary_four) <= 1]
assert lower_four == [(1, 1, 1)]
print("Ordinary four branches: positive lower lattice points", lower_four)

print("Attachment budgets: (number of C-preimages at scalar zero, nu_out, total nu, maximum loss)")
for c_preimages in (1, 2):
    nu_fibre = 1 + c_preimages
    for nu_out in range(4):
        nu = nu_fibre + nu_out
        if nu <= 3:
            loss = (c_preimages - 1) + nu_out
            assert loss == nu - 2 <= 1
            print((c_preimages, nu_out, nu, loss))
print("PASS")
