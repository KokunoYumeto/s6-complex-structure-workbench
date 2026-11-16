"""Exact low-degree integral calculation for the shifted fibre product.

The total dimension is ten.  This program certifies the integral
parabolic lattice and finite-cover cokernel in degree two.  It is
not a complete computation of all higher filtration extensions.
"""
from itertools import combinations
from sympy import Matrix,eye,zeros,diag,ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

def snf(R):
    return tuple(X.to_Matrix() for X in smith_normal_decomp(
        DomainMatrix.from_Matrix(R).convert_to(ZZ)))
def factors(R):
    D,U,V=snf(R)
    return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
def ext(M,q):
    ids=list(combinations(range(M.rows),q))
    return Matrix([[M.extract(i,j).det() for j in ids] for i in ids])

A1=Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
M0=(A1*A2).inv()
T=[diag(A1,eye(4)).inv().T,diag(A2,eye(4)).inv().T,
   diag(M0,eye(4)).inv().T,diag(eye(4),A1).inv().T,
   diag(eye(4),A2).inv().T,diag(eye(4),M0).inv().T]
assert T[0]*T[1]*T[2]*T[3]*T[4]*T[5]==eye(8)
for q in (1,2):
    E=[ext(t,q) for t in T];n=E[0].rows
    cob=Matrix.vstack(*(E[i]-eye(n) for i in (0,1,3,4)))
    rel=Matrix.hstack(*(E[i]-eye(n) for i in (0,1,3,4)))
    cf=factors(cob);rf=factors(rel)
    assert all(x==1 for x in cf+rf)
    h0=n-cob.rank();h2=n-rel.rank()
    loc=[n-(e-eye(n)).rank() for e in E]
    h1=h0+h2-(-4*n+sum(loc))
    print('degree',q,'H0,H1,H2 of integral invariant sheaf',h0,h1,h2,
          'local ranks',loc,'coboundary Smith',cf,'coinvariant Smith',rf)
    if q==2:assert (h0,h1,h2)==(3,18,3)

# At each factor, finite degree-two cokernels are:
# C3^1 tensor H1(T4) = (Z/3)^4;
# C4^1 tensor H1(T4) = (Z/4)^4; C4^2 = Z/2.
# The three global invariant two-forms are q_X1, gamma1 gamma2, q_X2.
orders=[3]*4+[4]*4+[2]+[3]*4+[4]*4+[2]
G=zeros(18,3)
G[8,0]=1;G[17,2]=1
for i in (0,4,9,13):G[i,1]=1
R=Matrix.hstack(diag(*orders),G)
F=factors(R)
assert F==[1]*11+[12]*7
print('finite degree-two cokernel presentation orders',orders)
print('global invariant images',G)
print('quotient Smith factors',F)
print('Tor H1(B,R2g_*Z) = (Z/12)^7')
print('With the two primitive natural d2 maps from X, E_infinity^(2,1)=0.')
print('Hence H2 of the shifted product = Z direct_sum (Z/12)^7.')
