#!/usr/bin/env python3
"""Post-release exact coordinate transport, independently authored.

Inputs are the printed B matrix and the independently frozen P,J construction.
No program from the paper or an earlier check is imported or read.
"""
import json
import sympy as s
z=s.symbols('z');i=s.I
P=s.Matrix([[1,i,z,i*z],[-z,i*z,1,-i]])
J=s.diag(s.Matrix([[0,1],[-1,0]]),s.Matrix([[0,1],[-1,0]]))
B=s.Matrix([[-i*z,-z,i,1],[-i,1,-i*z,z]])
S=s.Matrix([[0,1],[1,0]])
residual=s.simplify(B-S*P*J)
assert residual==s.zeros(2,4)
assert S.det()==-1
assert s.simplify(B*P.T)==s.zeros(2)
print(json.dumps({'exact_transport':'B = S P J','S':str(S),'det_S':-1,
 'residual':str(residual),'BP_transpose':str(s.simplify(B*P.T))},indent=2))
