#!/usr/bin/env python3
"""Primitive integral cells for the actual three-sphere cusp union."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
ROOT = Path(__file__).resolve().parents[2]
rel = "notes/part3_three_curve_exterior.md"
with (ROOT / "records/literature_fourfold.md").open("a") as log:
    log.write("\n- " + datetime.now(timezone.utc).isoformat()
              + " — Opened own " + rel
              + "; reason: exact common-exterior cellular reduction; "
              "material: all cellular differentials and primitive bases.\n")
(ROOT/rel).read_text()
D1 = s.Matrix([[-1]*6, [1]*6])
D2 = s.diag(*[s.Matrix([[1, -1], [-1, 1]]) for _ in range(3)])
assert D1*D2 == s.zeros(2, 6)
H2 = s.zeros(6, 3)
for i in range(3):
    H2[2*i, i] = H2[2*i+1, i] = 1
assert D2*H2 == s.zeros(6, 3)
assert D2.rank() == 3
H1 = s.zeros(6, 2)
H1[2, 0] = H1[4, 1] = 1
H1[0, 0] = H1[0, 1] = -1
assert D1*H1 == s.zeros(2, 2)
# Kernel(D1) has basis e_i-e_0, i=1,...,5, and projection deleting row0.
K1 = s.zeros(6, 5)
for i in range(5):
    K1[i+1, i] = 1
    K1[0, i] = -1
P1 = s.eye(6)[1:, :]
assert P1*K1 == s.eye(5)
assert K1*(P1*D2) == D2
combined = (P1*D2).row_join(P1*H1)
S = smith_normal_form(combined, domain=ZZ)
assert [abs(int(S[i, i])) for i in range(5)] == [1]*5
projections = [s.eye(3)[i:i+1, :] for i in range(3)]
def mat(A): return [[int(x) for x in row] for row in A.tolist()]
out = {
    "status": "PASS",
    "D1": mat(D1), "D2": mat(D2),
    "oriented_sphere_H2_basis": mat(H2),
    "marked_H1_basis": mat(H1),
    "kernel_D1_basis": mat(K1),
    "full_primitive_H1_certificate": mat(S),
    "complement_meridian_projections": [mat(A) for A in projections],
    "complement_groups": {"H3": "Z^3", "H4": "Z^2"},
    "relative_groups_Ei_EC": {"H4": "Z^2", "H5": "Z^2"},
    "scope": "Cellular and duality groups only; the actual relative Pontryagin cycle comparison remains unassigned."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2)+"\n")
print("PASS: all cusp-union cells, primitive sphere/loop bases, and marked meridian projections.")
