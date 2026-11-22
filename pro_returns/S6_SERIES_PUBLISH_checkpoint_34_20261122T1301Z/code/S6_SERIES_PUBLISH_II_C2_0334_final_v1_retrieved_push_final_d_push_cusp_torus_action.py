#!/usr/bin/env python3
"""Exact lattice checks for E.2.19; analytic extension is proved in the text."""
import json
from pathlib import Path
import sympy as sp

A0 = sp.Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
fixed = (A0-sp.eye(4)).nullspace()
assert fixed == [sp.Matrix([0,0,1,0]), sp.Matrix([0,0,0,1])]
triangles = [
    [(0,0,1),(1,0,1),(0,1,1)],
    [(1,0,1),(0,1,1),(1,1,1)],
]
records = []
for rays in triangles:
    matrix = sp.Matrix.hstack(*(sp.Matrix(v) for v in rays))
    assert abs(matrix.det()) == 1
    dual = matrix.inv()
    weights = [[int(dual[i,j]) for j in range(2)] for i in range(3)]
    assert [sum(w[j] for w in weights) for j in range(2)] == [0,0]
    assert all(abs(sp.Matrix([weights[i],weights[j]]).det()) == 1
               for i in range(3) for j in range(i+1,3))
    records.append({"rays": rays, "determinant": int(matrix.det()),
                    "dual_rows": [[int(x) for x in dual.row(i)] for i in range(3)],
                    "vertical_characters": weights})
out = {
    "status": "PASS",
    "invariant_period_basis_gamma_u_w_delta": [[int(x) for x in v] for v in fixed],
    "triple_point_character_records": records,
    "scope": "Exact invariant lattice and character matrices only; Grauert, descent, completeness and period extension are analytic arguments in E.2.19."
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
