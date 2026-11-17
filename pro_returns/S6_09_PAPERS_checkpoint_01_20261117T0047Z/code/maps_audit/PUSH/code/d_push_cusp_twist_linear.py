"""Exact cusp monodromy and the quotient lattice relevant to the residual twist."""
import sympy as s
A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
A0=(A1*A2).inv()
g=s.Matrix([1,0,0,0]);d=s.Matrix([0,0,0,1])
assert A0*g==g-d
print('A0=',A0)
print('quotient modulo delta=',A0[:3,:3])
print('fixed lattice kernel quotient=',(A0[:3,:3]-s.eye(3)).nullspace())
print('rank(A0-I)=', (A0-s.eye(4)).rank())
print('rank((A0-I)^2)=', ((A0-s.eye(4))**2).rank())
