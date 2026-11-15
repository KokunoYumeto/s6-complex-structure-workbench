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
Scusp=S.Matrix.hstack(Hs[0]*K1,Hs[0]*Hs[1]*K2,Hs[0]*Hs[1]*Hs[2]*K31,Hs[0]*Hs[1]*Hs[2]*K32)
print('Conjugated cusp-defect columns:',Scusp.tolist())
print('Their HNF:',hermite_normal_form(Scusp).tolist())
print('Finite norm of these columns:',(N*Scusp).tolist())
print('Integer h=2 correction:',Scusp.gauss_jordan_solve(S.Matrix([0,1,0,0]))[0])
h=S.symbols('h')
broot=-h*S.Matrix([0,1,1,0])/4
lroot=-h*S.Matrix([0,1,0,0])/2
l1=S.zeros(4,1);l2=h*S.Matrix([0,1,0,0])/2;l3=-h*S.Matrix([0,0,1,0])/2
assert (I-Hs[0])*broot == h*d/4+lroot
assert N*lroot == -h*d
sphere_defect=lroot+Hs[0]*l1+Hs[0]*Hs[1]*l2+Hs[0]*Hs[1]*Hs[2]*l3
assert sphere_defect==S.zeros(4,1)
print('Root b_h:',list(broot),'root integral defect:',list(lroot))
print('Nodal defects:',list(l1),list(l2),list(l3))
print('Sphere cocycle defect:',list(sphere_defect))
tau,z,beta,c=S.symbols('tau z beta c')
P=lambda tt,zz,bb:S.Matrix([[2*zz,tt,1,0],[bb+c,zz,0,1]])
P0=P(tau,z,beta)
transformations=[(-1/tau,(z-1)/tau,beta-1-2*(z-1)**2/tau),
                 (tau+1,z+1,beta+2),
                 (tau/(1-tau),z/(1-tau),beta+2*z*z/(1-tau)),
                 (tau+1,z,beta-1)]
for j,(H,(tt,zz,bb)) in enumerate(zip(Hs,transformations)):
    Pg=P(tt,zz,bb)
    R=S.Matrix.hstack(Pg*H[:,2],S.Matrix([0,1]))
    diff=(Pg*H-R*P0).applyfunc(S.simplify)
    assert diff==S.zeros(2,4)
    print('Period covariance',j,'R=',R.tolist(),'PASS')
t,mu,s=S.symbols('t mu s')
disc=4*t**3+27*(mu*t+1)**2
discdisc=S.discriminant(disc,t)
assert S.expand(discdisc-314928*(mu**3-1))==0
print('Discriminant of cubic:',S.factor(discdisc))
print('At infinity coefficients:',s**3,mu*s**5+s**6)
print('Discriminant at infinity:',S.factor(4*s**9+27*(mu*s**5+s**6)**2))
rho=S.exp(2*S.pi*S.I/3)
print('At mu=0 finite roots satisfy 4 a^3+27=0; dp/dmu=-9/(2a).')
print('Nilpotent ranks =',[int((T-I).rank()) for T in Ts[1:]])
print('All identities exact: PASS')
