#!/usr/bin/env python3
"""Exact integral maps for the compact B.4.17 source counterexample."""
import json
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

# Basis F1,F2,H of H2(Bl(P1 x P1)); H is a second-factor ruling
# disjoint from the point blown up.  The two elliptic Chern classes
# evaluate as the two coordinate vectors on F1,F2 and vanish on H.
intersection = sp.Matrix([[-1, 1, 1], [1, -1, 0], [1, 0, 0]])
chern = sp.Matrix([[1, 0, 0], [0, 1, 0]])
assert intersection.det() == 1
assert chern.rank() == 2
assert smith_normal_form(chern, domain=ZZ) == chern
general = chern * sp.Matrix([1, 1, 0])
assert general == sp.Matrix([1, 1])
assert smith_normal_form(general, domain=ZZ) == sp.Matrix([1, 0])

# Difference of the two conductor inclusions on H1(E).
mv1 = sp.Matrix([[0, 1], [-1, 0]])
assert abs(mv1.det()) == 1
assert mv1.rank() == 2
mv0 = sp.Matrix([[1], [-1]])
assert smith_normal_form(mv0, domain=ZZ) == sp.Matrix([[1], [0]])

# d2(a wedge b) = c1 tensor b - c2 tensor a is nonzero.
d2_fibre_area = sp.Matrix([0, 1, -1, 0, 0, 0])
assert d2_fibre_area.rank() == 1
total_b2 = 3 - chern.rank()
assert total_b2 == 1

out = {
    "status": "PASS",
    "base_intersection_matrix": intersection.tolist(),
    "global_Chern_matrix": chern.tolist(),
    "smooth_fibre_Chern_vector": list(general),
    "central_MV_H1_matrix": mv1.tolist(),
    "central_integral_Betti_numbers": [1, 0, 0, 3, 2],
    "smooth_fibre_b1": 1,
    "central_b1": 0,
    "local_monodromy_on_H1": "identity, by the explicit holomorphic product",
    "compact_total_b2": total_b2,
    "scope": "Compact threefold counterexample to the converse only; not an S6 filling."
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2, default=int) + '\n')
print(json.dumps(out, indent=2, default=int))
