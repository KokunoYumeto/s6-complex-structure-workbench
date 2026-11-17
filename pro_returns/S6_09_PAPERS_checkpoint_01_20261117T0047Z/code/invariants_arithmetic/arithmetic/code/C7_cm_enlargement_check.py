#!/usr/bin/env python3
"""Exact checks of the CM extension matrix and Gaussian eigencomponent."""
import sympy as s

beta = s.I*s.sqrt(19)
a,u,D,k = s.symbols('a u D k')
B = s.Matrix([[beta,0,0],[a,0,-1],[beta*a,19,0]])
U = s.Matrix([u,u*D-k*u**2,-beta*u*D+a*u])
projection = (s.eye(3)-B/beta)/2
expected = -k*u**2/2*s.Matrix([0,1,beta])
square_residual = s.simplify(B*B+19*s.eye(3))
projector_residual = s.simplify(projection**2-projection)
value_residual = s.simplify(projection*U-expected)
assert square_residual == s.zeros(3)
assert projector_residual == s.zeros(3)
assert value_residual == s.zeros(3,1)
print('B^2 + 19 I =', square_residual)
print('Projection idempotence residual =', projector_residual)
print('Projected Gaussian residual =', value_residual)
print('Projector =', s.simplify(projection))
print('Projected logarithm =', s.simplify(projection*U))
alpha = (1+beta)/2
assert s.simplify(alpha**2-alpha+5) == 0
assert s.simplify(alpha*s.conjugate(alpha)) == 5
print('alpha^2 - alpha + 5 = 0; alpha*conjugate(alpha) = 5')
print('ALL EXACT MATRIX IDENTITIES PASSED')
