"""Exact transcription checks for the nonspectral carrier prerequisites.

This checks matrix identities only.  Compactness, quotient exactness,
systolic estimates, continuity and homotopy arguments are separately read
and rederived in carrier_integration_audit.json.
"""
from pathlib import Path
import json
import sympy as S

a, eta, c, m, L, q = S.symbols("a eta c m L q")
D = L*q + 6*m*m
P = S.Matrix([[6*a, eta, 1, 0], [6*m, L, 0, 0],
              [c, a, 0, 1], [-q, m, 0, 0]])
PinvT = S.Matrix([
    [0, 0, 1, 0],
    [m/D, q/D, (-6*m*a-q*eta)/D, (-m*c-q*a)/D],
    [0, 0, 0, 1],
    [-L/D, 6*m/D, 6*(L*a-m*eta)/D, (L*c-6*m*a)/D],
])
Y = S.Matrix([[6*m, L], [-q, m]])
assert S.simplify(P.det()+D) == 0
assert (P.T*PinvT-S.eye(4)).applyfunc(S.simplify) == S.zeros(4)
assert Y.det() == D
assert P.extract([1,3], [0,1]) == Y
assert P.extract([1,3], [2,3]) == S.zeros(2)
report = {
    "det_P": "-D", "det_Y": "D", "P_transpose_times_inverse_transpose": "identity",
    "projected_long_columns": "Y", "projected_kernel_columns": "zero",
    "outcome": "all exact symbolic identities passed",
    "scope_limit": "This is not a substitute for the printed geometric and analytic proofs.",
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps(report, indent=2))
