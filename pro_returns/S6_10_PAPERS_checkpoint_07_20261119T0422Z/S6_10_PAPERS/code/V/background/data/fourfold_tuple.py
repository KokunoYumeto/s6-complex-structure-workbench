"""Printed fourfold tuple, transcribed for current replays.

The night checkpoint omits its background/data/fourfold_tuple.py input.
These are the literal MAPS F.2.5/F.3.5 and night P1.1/P1.2 matrices;
audit_fourfold_linear.py independently verifies their printed identities.
This file is a documented reconstruction, not a recovered original input.
"""
import sympy as s
A=s.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],
            [0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=s.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],
            [0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
M1=A.T
M2=B.T
M0=(M1*M2).inv()
v1=s.Matrix([1,3,-2,-1,2,0])
v2=s.Matrix([-1,0,0,0,0,0])
ell=s.Matrix([[1,0,0,0,0,0]])
Cf=s.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
Cg=s.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
Q=s.eye(6)
Q[:,0]=s.ones(6,1)
