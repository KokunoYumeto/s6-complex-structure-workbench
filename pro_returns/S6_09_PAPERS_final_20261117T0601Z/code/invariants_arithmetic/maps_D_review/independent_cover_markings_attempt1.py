"""Independent all-parameter identities in the MAPS D.1 covering marking."""
import sympy as S
from itertools import combinations

d = S.symbols('d', integer=True, positive=True)
A = S.Matrix([[1,0,0,0],[6*d,0,1,0],[-6*d,-1,-1,0],[-2*d,1,0,1]])
B = S.Matrix([[1,0,0,0],[0,0,-1,0],[-6*d,1,0,0],[3*d,0,1,1]])
M = (A*B).inv()
pairs = list(combinations(range(4),2))
W = S.Matrix([[M.extract(i,j).det() for j in pairs] for i in pairs])
N = W-S.eye(6)
# The angular w-delta torus and the mixed gamma-w + d*u-delta torus.
G = S.zeros(6,2)
G[5,0] = 1
G[1,1] = 1
G[4,1] = d
coordinates = S.Matrix.vstack(N[5,:],N[1,:])
assert G*coordinates == N
# The explicit unit columns prove equality of these integral lattices, not just ranks.
assert any(coordinates[:,j] == S.Matrix([1,0]) or coordinates[:,j] == S.Matrix([-1,0]) for j in range(6))
assert any(coordinates[:,j] == S.Matrix([0,1]) or coordinates[:,j] == S.Matrix([0,-1]) for j in range(6))
assert A**3 == S.eye(4) and B**4 == S.eye(4)
assert A*S.Matrix([-1,-2*d,4*d,0]) == S.Matrix([-1,-2*d,4*d,0])
assert B*S.Matrix([1,3*d,-3*d,0]) == S.Matrix([1,3*d,-3*d,0])
deck = S.Matrix([1/d,0,0,0])
assert A*deck-deck == S.Matrix([0,6,-6,-2])
assert B*deck-deck == S.Matrix([0,0,-6,3])
print('Cusp monodromy:',M)
print('Exterior difference:',N)
print('Primitive image generators:',G)
print('Integral unit-column coordinates:',coordinates)
print('All symbolic identities hold for every positive integer d.')
