#!/usr/bin/env python3
"""Exact rational-function certificates for the maps in E.2.20.

The proof establishes existence and holomorphy of the unit functions and maps.
This program verifies the displayed algebra of those maps with symbolic units.
"""
from pathlib import Path
import json
import sympy as sp

q, a0, b0, z0 = sp.symbols("q a0 b0 z0", nonzero=True)
lam = a0 * b0 / q
first = (q / b0, b0, z0)
second = (a0, q / a0, z0)
translated = (lam * first[0], first[1] / lam, first[2])
assert all(sp.cancel(a - b) == 0 for a, b in zip(translated, second))
assert sp.cancel(first[0] * first[1] - q) == 0
assert sp.cancel(second[0] * second[1] - q) == 0

# Both directions of each standard toric coordinate map are checked as
# rational maps, independently of a ray-matrix inversion.
x, y, z = sp.symbols("x y z", nonzero=True)
X0, X1, X2 = sp.symbols("X0 X1 X2", nonzero=True)
toric_records = []
for forward, inverse in [
    ((q / (x * y), x, y), (X1, X2, X0 * X1 * X2)),
    ((q / y, q / x, x * y / q), (X0 * X2, X1 * X2, X0 * X1 * X2)),
]:
    backwards = [sp.cancel(a.subs(dict(zip((X0, X1, X2), forward)), simultaneous=True))
                 for a in inverse]
    forwards = [sp.cancel(a.subs(dict(zip((x, y, q), inverse)), simultaneous=True))
                for a in forward]
    assert backwards == [x, y, q]
    assert forwards == [X0, X1, X2]
    assert sp.cancel(sp.prod(forward) - q) == 0
    toric_records.append({"forward": [str(a) for a in forward],
                          "inverse": [str(a) for a in inverse],
                          "both_compositions": "identity"})

# The chart-unit change fixes the product q and has the exact displayed
# inverse, even when its units depend on q and on the deformation parameter.
s = sp.symbols("s")
Q = x * y * z
U = sp.Function("U")(Q, s)
V = sp.Function("V")(Q, s)
F = sp.Matrix([x * U, y * V, z / (U * V)])
assert sp.simplify(sp.prod(F) - Q) == 0
determinant = sp.simplify(F.jacobian([x, y, z]).det())
assert determinant == 1
actual_Q = sp.simplify(sp.prod(F))
inverse = [F[0] / sp.Function("U")(actual_Q, s),
           F[1] / sp.Function("V")(actual_Q, s),
           F[2] * sp.Function("U")(actual_Q, s) * sp.Function("V")(actual_Q, s)]
assert all(sp.simplify(a - b) == 0 for a, b in zip(inverse, (x, y, z)))

# The marked Grassmannian comparison uses the quotient by ker[Z|I].
# This is an exact kernel description for arbitrary four entries of Z.
z00, z01, z10, z11 = sp.symbols("z00 z01 z10 z11")
Z = sp.Matrix([[z00, z01], [z10, z11]])
P = Z.row_join(sp.eye(2))
kernel_columns = sp.eye(2).col_join(-Z)
assert P * kernel_columns == sp.zeros(2)
assert P[:, 2:4] == sp.eye(2)
assert kernel_columns[:2, :] == sp.eye(2)

# The integer equations for either triple's invariant monomials are explicit.
n0, n1, n2 = sp.symbols("n0 n1 n2", integer=True)
invariant_weight = sp.Matrix([[-1, 1, 0], [-1, 0, 1]]) * sp.Matrix([n0, n1, n2])
assert invariant_weight == sp.Matrix([n1 - n0, n2 - n0])
assert -invariant_weight == sp.Matrix([n0 - n1, n0 - n2])

result = {
    "status": "PASS",
    "method": "Symbolic rational-map compositions and Jacobian differentiation with arbitrary holomorphic unit functions",
    "adjacent_origin_multiplier": str(lam),
    "adjacent_origin_identity": True,
    "toric_maps": toric_records,
    "unit_change_preserves_product": True,
    "unit_change_jacobian": str(determinant),
    "unit_change_inverse_composition": "identity",
    "period_kernel_columns": [[str(a) for a in kernel_columns.row(i)] for i in range(4)],
    "period_identity_columns": True,
    "invariant_monomial_equations": [str(a) for a in invariant_weight],
    "scope": "Exact algebra of the stated morphisms; topology, existence of holomorphic units, analytic continuation and properness are proved in the written derivation and comparison.",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
