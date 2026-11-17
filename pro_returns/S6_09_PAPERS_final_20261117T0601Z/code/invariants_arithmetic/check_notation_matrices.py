#!/usr/bin/env python3
"""Exact checks of the nontrivial matrix and origin adapters in the dictionary."""
from pathlib import Path
import json
import sympy as s

PACKAGE = Path(__file__).resolve().parents[2]
P = s.Matrix([[0,-2,-1,-2],[2,-1,0,-1],[0,2,1,3],[-1,0,0,0]])
S = s.Matrix([[-1,0,0,0],[-6,0,-1,0],[6,-1,0,0],[2,1,1,1]])
Q = s.Matrix([[2,-1,0,-2],[2,-1,0,-1],[0,2,1,3],[1,0,0,0]])
A1 = s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
assert P*S == Q
assert abs(P.det()) == abs(Q.det()) == abs(S.det()) == 1
assert A1**3 == s.eye(4) and A2**4 == s.eye(4)
assert A1*S == S*A1.inv() and A2*S == S*A2.inv()

alpha, eta, cc, m, L, q = s.symbols("alpha eta c m L q", real=True)
D = L*q+6*m*m
PT = s.Matrix([[6*alpha,eta,1,0],[6*m,L,0,0],[cc,alpha,0,1],[-q,m,0,0]])
inverse_transpose = s.Matrix([
    [0,0,1,0],
    [m/D,q/D,(-6*m*alpha-q*eta)/D,(-m*cc-q*alpha)/D],
    [0,0,0,1],
    [-L/D,6*m/D,6*(L*alpha-m*eta)/D,(L*cc-6*m*alpha)/D],
])
assert s.simplify(PT.det()+D) == 0
assert (PT.T*inverse_transpose-s.eye(4)).applyfunc(s.simplify) == s.zeros(4)
YT = s.Matrix([[6*m,L],[-q,m]])
assert s.simplify(YT.det()-D) == 0
assert s.simplify((-q-6*m*m/L)+D/L) == 0

c, h, mu, d0 = s.symbols("c h mu d0")
sigma = lambda x: s.Matrix([-x*mu/2,-x*x/24-x*d0/12])
bar_b = s.Matrix([-h*mu/2,-h*(c+d0)/12-h*h/24])
assert (sigma(c+h)-sigma(c)-bar_b).applyfunc(s.simplify) == s.zeros(2,1)

record = {
    "exact_coefficient_ring": "integers and rational functions over Q",
    "P_mark_S_rev_equals_Q_mark": True,
    "marking_determinants": {"P": int(P.det()), "S": int(S.det()), "Q": int(Q.det())},
    "finite_orders_A1_cubed_A2_fourth_identity": True,
    "S_conjugates_each_finite_action_to_its_inverse": True,
    "real_period_determinant": "-(L*q+6*m^2)",
    "printed_inverse_transpose_multiplies_to_identity": True,
    "imaginary_quotient_determinant": "L*q+6*m^2",
    "D_family_equals_minus_D_T_over_L_T": True,
    "coherent_cusp_translation_equals_sigma_difference": True,
    "scope": "Exact adapter arithmetic only; geometric existence and source hypotheses retain their complete proof audits.",
}
out = PACKAGE / "work/invariants_arithmetic/notation_matrix_checks.json"
out.write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
