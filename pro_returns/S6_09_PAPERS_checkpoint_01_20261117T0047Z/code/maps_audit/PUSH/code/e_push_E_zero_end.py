"""Exact H1 cancellation audit for E.2.7; no geometric claim is automated."""
from pathlib import Path
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
I = sp.eye(4)
delta = sp.Matrix([0, 0, 0, 1])
gamma = sp.Matrix([[1, 0, 0, 0]])
E = delta * gamma
A1 = sp.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = sp.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
A0 = sp.Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
h, n = sp.symbols("h n", integer=True)
N = A0-I
assert E*E == sp.zeros(4)
assert N*N == sp.zeros(4)
assert E*N == N*E == sp.zeros(4)
assert A1**3 == I
assert A2**4 == I
for A in (A0, A1, A2):
    assert A*E == E*A == E
    assert A*delta == delta
    assert gamma*A == gamma

finite_checks = []
for name, A, order in (("A1", A1, 3), ("A2", A2, 4)):
    for residue in range(order):
        M = (I-h*E)*A**residue
        assert sp.expand(M**order) == I-order*h*E
        finite_checks.append({"matrix":name, "base_winding_residue":residue,
                              "power":order, "result":"I-"+str(order)+"*h*E"})

cusp = (I-h*E)*(I+n*N)
assert cusp == I+n*N-h*E
assert (cusp-I)[2,1] == n
assert (cusp-I)[3,0] == -n-h
assert sp.solve([(cusp-I)[2,1], (cusp-I)[3,0]], [n,h]) == {n:0,h:0}

k, ell, degree = sp.symbols("k ell degree", integer=True, positive=True)
# z=exp(-pi*i*c/(k*ell)); log(z) changes by 2*pi*i*degree.
dc = sp.simplify(-k*ell/(sp.pi*sp.I)*(2*sp.pi*sp.I*degree))
assert dc == -2*k*ell*degree
report = {
    "status":"PASS",
    "scope":"Exact linear monodromy and parameter-winding identities only",
    "basis":["gamma","u","w","delta"],
    "A1":A1.tolist(), "A2":A2.tolist(), "A0_cusp":A0.tolist(),
    "E":E.tolist(),
    "finite_checks":finite_checks,
    "cusp_identity_solution":{"base_winding":0,"parameter_shift":0},
    "positive_parameter_loop_c_shift":str(dc),
    "unproved_by_program":["relative fibration persistence", "critical-value extension",
                           "smooth-completion separatedness", "arbitrary deformation chains"]
}
def serial(value):
    if isinstance(value, sp.Integer):
        return int(value)
    raise TypeError(type(value).__name__)
payload = json.dumps(report, indent=2, default=serial)
(HERE/"e_push_E_zero_end.json").write_text(payload+"\n")
print(payload)
