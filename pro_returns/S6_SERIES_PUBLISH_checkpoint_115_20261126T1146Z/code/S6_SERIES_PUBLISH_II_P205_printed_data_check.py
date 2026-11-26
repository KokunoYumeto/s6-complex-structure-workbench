#!/usr/bin/env python3
"""Verify the exact matrix data printed in the P205 publication proposal.

This is a check of an already derived construction, with no new proof event.
"""
from itertools import combinations
import sympy as S

A = [
    S.Matrix([[1,0,0,0],[0,-1,2,0],[0,0,-1,0],[0,1,0,1]]),
    S.Matrix([[-1,0,0,0],[0,1,0,0],[2,0,-1,0],[0,0,1,1]]),
    S.Matrix([[-1,0,0,0],[0,-1,-2,0],[-2,0,1,0],[2,1,1,1]])]
C = [
    S.Matrix([[0,-1,0,0],[-1,0,-2,-1],[0,0,0,1],[0,0,1,0]]),
    S.Matrix([[0,0,0,1],[0,-1,0,0],[-1,0,-2,-1],[0,0,1,0]]),
    S.Matrix([[0,0,0,1],[1,-1,2,-2],[0,1,0,1],[0,0,-1,0]])]
L = S.Matrix([[1,0,0,0],[0,1,0,0],[-1,0,-1,-1],[0,0,0,-1]])
assert A[0]*A[1]*A[2] == S.eye(4)
assert all(a.det()==c.det()==1 and a*c==c*L for a,c in zip(A,C))
print("A1 A2 A3 = I; det Ai = det Ci = 1; Ai Ci = Ci Aloc: verified")
epsilon = S.symbols('epsilon', positive=True)
B = [
    S.Matrix([[1,0,0],[0,-1,epsilon],[0,0,-1]]),
    S.Matrix([[-1,0,0],[0,1,0],[epsilon,0,-1]]),
    S.Matrix([[-1,0,0],[0,-1,-epsilon],[-epsilon,0,1]])]
P = S.Matrix([[S.Rational(1,2),S.Rational(1,2),S.Rational(1,2),1],
              [S.Rational(1,2),0,0,0],[0,S.Rational(1,2),0,0],
              [0,0,S.Rational(1,2),0]])
D = S.diag(1,1,epsilon**2/4,epsilon/2)
assert B[0]*B[1]*B[2] == S.eye(3)
for i,b in enumerate(B):
    n = b*b-S.eye(3)
    assert n*n == S.zeros(3) and n.rank()==1
    expected = S.zeros(3)
    row,col,coef = [(1,2,-2*epsilon),(2,0,-2*epsilon),(1,0,epsilon**2)][i]
    expected[row,col] = coef
    assert n == expected
    assert S.simplify((D*P).inv()*S.diag(1,b)*(D*P)) == A[i]
assert P.det() == -S.Rational(1,8)
assert all(S.simplify((D*P*c).det()+epsilon**3/64)==0 for c in C)
print("Bi product, exact nilpotents, integral conjugacy and local orientation determinant: verified")
hom = S.Matrix.vstack(*(a-S.eye(4) for a in A)).rref()[0]
coh = S.Matrix.vstack(*(a.T-S.eye(4) for a in A)).rref()[0]
expected_hom = S.eye(4)[:3,:]
expected_coh = expected_hom.copy()
for k in range(3): expected_coh[k,3] = -S.Rational(1,2)
assert hom[:3,:] == expected_hom and hom[3:,:] == S.zeros(9,4)
assert coh[:3,:] == expected_coh and coh[3:,:] == S.zeros(9,4)
alpha = S.Matrix([1,1,1,2])
pullbacks = [c.T*alpha for c in C]
assert pullbacks == [S.Matrix([-1,-1,0,0]),S.Matrix([-1,-1,0,0]),S.Matrix([1,0,0,0])]
assert all((a.T-S.eye(4))*alpha == S.zeros(4,1) for a in A)
assert (L.T-S.eye(4)).rank()==2
print("Printed homology/cohomology row reductions and Ci^t alpha:", pullbacks)
pairs = list(combinations(range(4),2))
def exterior2(matrix):
    return S.Matrix([[matrix.extract(rows,cols).det() for cols in pairs] for rows in pairs])
W1,W2 = [exterior2(a.T)-S.eye(6) for a in A[:2]]
minor = S.Matrix.vstack(*(W1.row(k) for k in [0,1,3,4]),W2.row(0),W2.row(1))
expected = S.Matrix([[-2,0,1,0,0,0],[2,-2,0,0,0,0],
                     [0,0,0,0,-2,1],[0,0,0,0,-2,0],
                     [-2,0,0,-2,0,0],[0,0,-1,0,0,2]])
assert minor == expected and minor.det() == -16
print("Exterior pair order:", [(i+1,j+1) for i,j in pairs])
print("Printed exterior-power minor:", minor)
print("Exterior minor determinant:", minor.det())
loop_values = [v[0]/2 for v in pullbacks]
assert loop_values == [-S.Rational(1,2),-S.Rational(1,2),S.Rational(1,2)]
assert sum(loop_values)==-S.Rational(1,2)
print("Rational local loop values:", loop_values, "; sum:", sum(loop_values))
print("Integral 2alpha values:", [2*x for x in loop_values], "; sum:", 2*sum(loop_values))
zeta = S.symbols('zeta', nonzero=True)
def twistor(z):
    return S.Matrix([[1,S.I,-z,S.I*z],[z,-S.I*z,1,S.I]])
characters = [S.diag(1,1,-1,-1),S.diag(1,-1,1,-1),S.diag(1,-1,-1,1)]
row_maps = [S.diag(1,-1),S.Matrix([[0,-zeta],[zeta,0]]),S.Matrix([[0,zeta],[zeta,0]])]
for character, row_map, image in zip(characters,row_maps,[-zeta,-1/zeta,1/zeta]):
    assert S.simplify(twistor(zeta)*character-row_map*twistor(image))==S.zeros(2,4)
x,y = S.symbols('x y', real=True)
plane = twistor(x+S.I*y)
assert S.simplify(plane.col_join(S.conjugate(plane)).det()-4*(1+x*x+y*y)**2)==0
print("Exact equivariant row maps K1, K2, K3 and determinant 4(1+|zeta|^2)^2: verified")
print("All printed exact-data checks passed; no analytic realization claim is inferred from this script alone.")
