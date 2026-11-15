"""Exact integral checks for E19 and the arbitrary nonzero-p gluing audit."""
from itertools import combinations
from functools import reduce
from math import gcd
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

A0=s.Matrix([[1,-1,0,2],[0,-1,-1,6],[0,1,0,0],[0,0,0,1]])
A1=s.Matrix([[1,0,1,-3],[0,0,1,0],[0,-1,0,6],[0,0,0,1]])
Ainf=s.Matrix([[1,0,0,1],[0,1,1,0],[0,0,1,0],[0,0,0,1]])
assert A0*A1*Ainf == s.eye(4)
Ac0=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
Ac1=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
R=s.Matrix([[-2,1,0,1],[-6,0,-1,0],[0,-1,0,0],[-1,0,0,0]])
assert R.det()==-1
assert A0*R==R*Ac0 and A1*R==R*Ac1
gamma=s.Matrix([[1,0,0,0]])
psi=s.Matrix([[0,0,0,1]])
assert psi*R == -gamma
delt,a,b,d=[s.eye(4)[:,j] for j in range(4)]
u0=d+2*a+2*b;u1=d+3*a+3*b
eps0=s.Matrix([1,2,-4,0]);eps1=s.Matrix([1,3,-3,0])
assert -R*eps0==u0 and -R*eps1==u1-delt
print('E19 marking comparison R, det R =', R, R.det())
print('E19 affine inversion sends epsilon0 to u0, epsilon1 to u1-delta')

pairs=list(combinations(range(4),2))
def wedge2(A):
    return s.Matrix([[A.extract(I,J).det() for J in pairs] for I in pairs])
coinv=(wedge2(A0)-s.eye(6)).row_join(wedge2(A1)-s.eye(6))
snf=smith_normal_form(coinv,domain=ZZ)
diag=[abs(int(snf[j,j])) for j in range(6)]
assert diag==[1,1,1,1,1,0]
D=(A0-s.eye(4)).row_join(A1-s.eye(4))
assert D.rank()==3
columns=[(-A1*delt).col_join(-delt),(-A1*a).col_join(-a),
         delt.col_join(s.zeros(4,1)),u0.col_join(s.zeros(4,1)),
         s.zeros(4,1).col_join(u1)]
K=s.Matrix.hstack(*columns)
assert D*K == s.zeros(4,5)
minor_gcd=reduce(gcd,(abs(int(K.extract(I,range(5)).det()))
                       for I in combinations(range(8),5)))
assert minor_gcd==1
print('E19 exterior-square coinvariant Smith diagonal:',diag)
print('E19 smooth-part edge rank and primitive kernel-basis minor gcd:',D.rank(),minor_gcd)

N0=s.eye(4)+A0+A0**2
N1=s.eye(4)+A1+A1**2+A1**3
assert N0*a==-delt and N1*a==-2*delt
assert N0*d==3*u0 and N1*d==4*u1
J=s.Matrix([[0,0,0,-6],[0,0,1,0],[0,-1,0,0],[6,0,0,0]])
assert A0.T*J*A0==J and A1.T*J*A1==J
assert (a.T*J*u0)[0]==2 and (a.T*J*u1)[0]==3
print('E19 normal-circle norm and alternating-pairing identities: passed')

n0,n1,rho0,rho1,al0,al1,be0,be1=s.symbols('n0 n1 rho0 rho1 alpha0 alpha1 beta0 beta1')
B=s.Matrix([[-2*n0,-6*rho0*al0,-3*n1,-6*rho1*al1],
            [-1,rho0*be0,2,-rho1*be1],[0,1,0,0],[0,0,0,1]])
assert s.factor(B.det())==4*n0+3*n1
r1,r2,ell=s.symbols('r1 r2 ell')
p=12*ell-4*r1-3*r2
assert s.expand(B.det().subs({n0:r1,n1:r2-4*ell})+p)==0
print('E19 gluing determinant:',s.factor(B.det()),'= -p after cusp comparison')

count=0
for a0 in range(-5,6):
    if gcd(a0,3)!=1:continue
    for a1 in range(-5,6):
        if gcd(a1,4)!=1:continue
        for l0 in range(-3,4):
            nn0=a0;nn1=a1-4*l0
            pp=12*l0-4*a0-3*a1
            assert pp!=0
            bb0=next(j for j in range(3) if (1-nn0*j)%3==0)
            aa0=(1-nn0*bb0)//3
            bb1=next(j for j in range(4) if (1-nn1*j)%4==0)
            aa1=(1-nn1*bb1)//4
            BB=B.subs({n0:nn0,n1:nn1,rho0:a0-2,rho1:a1+3,
                       al0:aa0,al1:aa1,be0:bb0,be1:bb1})
            SS=smith_normal_form(BB,domain=ZZ)
            assert [abs(int(SS[j,j])) for j in range(4)]==[1,1,1,abs(pp)]
            count+=1
print('E19 exact admissible sample Smith forms checked:',count)
print('E19 integral homology H0,...,H6: Z, Z/|p|, Z/|p|, Z/|p|, Z/|p|, 0, Z')
