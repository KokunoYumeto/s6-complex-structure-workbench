"""Exact monodromy, fixed-lattice, norm, and Weierstrass checks for E.5."""
import sympy as S
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy.polys.domains import ZZ

Ts=[S.Matrix(x) for x in [
 [[1,0,-2,-1],[0,0,-1,0],[0,1,0,-1],[0,0,0,1]],
 [[1,0,2,2],[0,1,1,1],[0,0,1,0],[0,0,0,1]],
 [[1,0,0,0],[0,1,0,0],[0,-1,1,0],[0,0,0,1]],
 [[1,0,0,-1],[0,1,1,0],[0,0,1,0],[0,0,0,1]]]]
Hs=[T.inv().T for T in Ts]
I=S.eye(4)
assert Ts[0]*Ts[1]*Ts[2]*Ts[3]==I
assert Hs[0]*Hs[1]*Hs[2]*Hs[3]==I
assert Ts[0]**4==I
ell=S.Matrix([1,-1,-1,0]);d=S.Matrix([0,0,0,1])
print('Cohomological matrices, order *,1,2,3:')
for T in Ts:print(T.tolist())
print('Homological matrices H=(T^{-1})^t:')
for H in Hs:print(H.tolist())
variables=S.symbols('x0:16');C=S.Matrix(4,4,variables)
comm=S.linear_eq_to_matrix(sum((list(C*H-H*C) for H in Hs),[]),variables)[0]
basis=comm.nullspace()
assert len(basis)==2
print('Rational homological centralizer basis:')
for b in basis:print(S.Matrix(4,4,b))
fixed=Hs[0]-I
assert fixed*ell==S.zeros(4,1) and fixed*d==S.zeros(4,1)
print('Finite fixed lattice equations:',list(fixed*S.Matrix(S.symbols('a b c d'))))
N=sum((Hs[0]**j for j in range(4)),S.zeros(4))
print('Finite norm matrix:',N.tolist())
coordinates=S.Matrix.hstack(ell,d)
NC=coordinates.gauss_jordan_solve(N)[0]
print('Norm columns in (ell,d) basis:',NC.tolist())
print('Norm image HNF:',hermite_normal_form(NC).tolist())
print('Norm image SNF:',smith_normal_form(NC,domain=ZZ).tolist())
for j in range(1,4):
    B=Hs[j]-I
    print('Node',j,'nilpotent rank',B.rank(),'image HNF',hermite_normal_form(B).tolist(),
          'kernel basis',[list(v) for v in B.nullspace()])
    assert B*B==S.zeros(4)
    print('Image SNF',smith_normal_form(B,domain=ZZ).tolist())
K1=S.Matrix([0,0,1,1]);K2=S.Matrix([0,1,0,0]);K31=S.Matrix([0,0,1,0]);K32=d
