"""Exact audits of the original homological marking. Python 3 + SymPy.
No floating-point arithmetic is used. All assertions must pass.
"""
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
I=s.eye(4)
A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
g,u,w,d=[I[:,i] for i in range(4)]
E=d*g.T
eps1=s.Matrix([1,2,-4,0]); eps2=s.Matrix([1,3,-3,0])
N1=sum((A1**i for i in range(3)),s.zeros(4)); N2=sum((A2**i for i in range(4)),s.zeros(4))
assert A1**3==I and A2**4==I and E**2==s.zeros(4)
assert all(A*E==E*A==E for A in [A1,A2])
print('orders: A1^3=I, A2^4=I; E^2=0; Aj E=E Aj=E')
print('A0=',(A1*A2).inv().tolist())
for j,A,N,eps in [(1,A1,N1,eps1),(2,A2,N2,eps2)]:
    F=s.Matrix.hstack(eps,d)
    assert (A-I)*F==s.zeros(4,2)
    C=s.Matrix.hstack(*[F.gauss_jordan_solve(N[:,i])[0] for i in range(4)])
    print(f'N{j}=',N.tolist())
    print(f'norm coordinates {j}=',C.tolist())
    print(f'Smith {j}=',smith_normal_form(C,domain=s.ZZ).tolist())
    for n in [-3,-2,-1,0,1,2,3]:
        hnf_in=hermite_normal_form(N)==hermite_normal_form(N.row_join(n*d))
        direct_in=True if j==1 else n%2==0
        assert hnf_in==direct_in
    print(f'independent HNF membership checks for n delta, -3<=n<=3: passed')
xs=s.symbols('h0:16'); H=s.Matrix(4,4,xs)
eqs=list(H*A1-A1*H)+list(H*A2-A2*H)
sol=s.linsolve(eqs,xs)
print('centralizer symbolic linear system=',sol)
assert len(next(iter(sol)).free_symbols)==2
assert all(x==0 for x in list((s.Symbol('a')*I+s.Symbol('b')*E)*A1-A1*(s.Symbol('a')*I+s.Symbol('b')*E)))
# Product-cover and saturated moving-lattice certificates.
e1=s.Matrix([0,1,-2,0]); f1=s.Matrix([0,0,-3,1]); e2=s.Matrix([0,1,-1,0]); f2=s.Matrix([0,0,-2,1])
for j,A,eps,e,f in [(1,A1,eps1,e1,f1),(2,A2,eps2,e2,f2)]:
    B=s.Matrix.hstack(e,f)
    assert hermite_normal_form(A-I)==hermite_normal_form(B)
    print(f'fixed+moving determinant {j}=',s.Matrix.hstack(eps,d,e,f).det())
    assert smith_normal_form(B,domain=s.ZZ)[0,0] in [1,-1]
# Original even-shift local equations, checked as polynomial identities.
n=s.symbols('n',integer=True)
r1=-n*(u+w)/3; r2=n*(u+w)/4
assert (I-A1)*r1==n*d/3-n*w
assert (I-A2)*r2==-n*d/4+n*u/2
L1=-n*w;L2=n*u/2
L0=-(A1*A2).inv()*(L1+A1*L2)
print('even-shift cusp cocycle=',list(L0))
assert L0==3*n*w/2-n*d/2
# Integral automorphism cocycles. Coordinates (a,b,c,d) in e1,f1,e2,f2.
C=[]
for i in range(4):
    C.append(list(s.Matrix.hstack(e1,f1).gauss_jordan_solve((I-A1)[:,i])[0])+list(s.Matrix.hstack(e2,f2).gauss_jordan_solve((I-A2)[:,i])[0]))
C=s.Matrix(C).T
K=s.Matrix([[0,1,2],[1,0,0],[0,1,0],[0,0,1]])
assert s.Matrix([[1,0,-1,-2]])*C==s.zeros(1,4)
assert hermite_normal_form(C)==K
print('automorphism coboundary matrix=',C.tolist())
print('integral kernel basis=HNF(coboundaries)=',K.tolist())
# Independent constructive verification that every kernel vector is a coboundary.
b,c0,d0=s.symbols('b c d',integer=True)
# Solve C*l=(c+2d,b,c,d). Its last column is zero; first three columns unimodular onto K.
coords=K.gauss_jordan_solve(C[:,0:3])[0]
assert abs(coords.det())==1
print('kernel-coordinate coboundary determinant=',coords.det())
# General finite data: direct congruences versus HNF membership over a finite exhaustive range.
checks=0
for aa in [-1,1]:
  for r in [-2,-1,1,2]:
   if r%3==0: continue
   for rp in [-2,-1,1,2]:
    for k in [-1,0,1]:
     for kp in [-1,0,1]:
      for shift in [-2,-1,0,1,2]:
       rhs=aa*(r*eps1+k*d)-(I+shift*E)*(rp*eps1+kp*d)
       yes=hermite_normal_form(N1)==hermite_normal_form(N1.row_join(rhs))
       assert yes==((aa*r-rp)%3==0);checks+=1
  for r in [-3,-1,1,3]:
   for rp in [-3,-1,1,3]:
    for k in [-1,0,1]:
     for kp in [-1,0,1]:
      for shift in [-2,-1,0,1,2]:
       rhs=aa*(r*eps2+k*d)-(I+shift*E)*(rp*eps2+kp*d)
       yes=hermite_normal_form(N2)==hermite_normal_form(N2.row_join(rhs))
       assert yes==((aa*r-rp)%4==0 and (aa*k-kp-shift*rp)%2==0);checks+=1
print('general finite-data HNF versus congruence checks=',checks)
for k,l in [(1,1),(3,1),(1,5),(5,7),(7,5)]:
    assert s.gcd(3*k,4*l)==1
    n1=sum((A1**i for i in range(3*k)),s.zeros(4)); n2=sum((A2**i for i in range(4*l)),s.zeros(4))
    assert n1==k*N1 and n2==l*N2
    assert s.ilcm(k,2*l)==2*k*l
    print(f'higher norms (k,l)=({k},{l}): N_3k=kN1, N_4l=lN2; shift step={2*k*l}')
print('ALL EXACT CHECKS PASSED')
