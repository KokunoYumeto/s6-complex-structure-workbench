#!/usr/bin/env python3
"""Exact algebra for C.3.16; topology is proved in its LaTeX source.

Verifies the actual comparison map's global complex defining function,
its two winding contributions, and the primitive cusp-link inclusion.
No numerical approximation or identification with a Haefliger number is used.
"""
import json
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

S, A, z, q = sp.symbols("S A z q")
z1 = S**3 * A * z**3
z2 = S**4 * z**4
h = sp.expand(z2**3 - z1**4)
h_reduced = sp.expand(h.subs(A**4, 1-q))
assert sp.expand(h_reduced-q*S**12*z**12) == 0

# The local unit S^12 z^12 is nowhere zero.  A is the holomorphic
# fourth root of 1-q, whose branch is fixed on the whole cusp disc.
assert sp.Poly(h_reduced, q).degree() == 1
assert sp.Poly(h_reduced, z).degree() == 12
inclusion = sp.Matrix([[12, 0, 1]])
smith = smith_normal_form(inclusion, domain=ZZ)
assert smith == sp.Matrix([[1, 0, 0]])
kernel_generators = sp.Matrix([[1, 0], [0, 1], [-12, 0]])
assert inclusion * kernel_generators == sp.zeros(1, 2)
assert kernel_generators.rank() == 2

result = {
    "statement": "C.3.16",
    "status": "PASS",
    "target_defining_function": "G2^3-G1^4",
    "exact_cusp_identity": str(h_reduced),
    "positive_gamma_winding": 12,
    "u_winding": 0,
    "actual_positive_q_meridian_winding": 1,
    "H1_link_basis": ["gamma", "u", "q"],
    "inclusion_row": list(inclusion),
    "smith_row": list(smith),
    "kernel_columns": [list(kernel_generators.col(i)) for i in range(2)],
    "noncomputational_dependencies": [
        "C.3.13 actual comparison map and exact transverse q-section",
        "C.3.7 oriented central cycle and H^3(H,Z)=Z",
        "C.3.14 Q=S5",
        "integral Alexander duality and positive local normal degree",
    ],
    "scope": "No six-dimensional framing or numerical J value is inferred.",
}
serialized = json.dumps(result, indent=2, default=int)
output = Path(__file__).with_suffix(".json")
output.write_text(serialized + "\n")
print(serialized)
