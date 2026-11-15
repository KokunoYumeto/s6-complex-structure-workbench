"""Exact matrix, genus, and rational Leray checks used in Parts E--F."""
from sympy import Matrix, eye, zeros, diag, symbols, Rational, expand, simplify, ZZ
from sympy.matrices.normalforms import smith_normal_form
from math import comb

A1=Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
M0=Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
C1=Matrix([[-1,-1],[1,0]]);C2=Matrix([[0,1],[-1,0]]);C0=Matrix([[1,1],[0,1]])
J=Matrix([[0,0,0,6],[0,0,1,0],[0,-1,0,0],[-6,0,0,0]])
assert A1.T*J*A1==J and A2.T*J*A2==J and J.det()==36
assert C1*C2*C0==eye(2)
coinv=Matrix.hstack(C1-eye(2),C2-eye(2))
print('Elliptic coinvariant Smith form:',smith_normal_form(coinv,domain=ZZ))
for A,C,m,v in [(A1,C1,3,Matrix([1,2,-4,0])),
                 (A2,C2,4,Matrix([-1,-3,3,0]))]:
    T=diag(A,C)
    assert T**m==eye(6)
    R=zeros(7,7);R[:6,:6]=T-eye(6)
    R[:,6]=Matrix(list(-v)+[0,0,m])
    print('Finite fourfold filling H1, order',m,':',smith_normal_form(R,domain=ZZ))

# Abelianization of the shifted fibre product's exact pi1 presentation.
R=Matrix([[3,0,0,0,-1,0],[0,4,0,0,1,0],
          [0,0,3,0,0,-1],[0,0,0,4,0,1],[1,1,1,1,0,0]])
print('Shifted product abelianization Smith form:',smith_normal_form(R,domain=ZZ))

# Genus identities, with c1=c3=0 rationally.
u,e,s=symbols('u e s')
td=(3*u-e)/720
chi1=(3*u-31*e)/180
assert simplify(chi1-4*td)==-e/6
assert simplify(td.subs(u,(45*s-14*e)/3))==(3*s-e)/48
print('chi^1-4 Td =',simplify(chi1-4*td))
print('chi=6, rank H4=4 possible signatures:',
      [v for v in range(-4,5,2) if (3*v-6)%48==0])
print('Root-stack line degrees:',
      {k:Rational(k,12)-Rational(k%3,3)-Rational((-k)%4,4)
       for k in [0,1,-1,-2,-5,-6]})

# Rational Leray page of the shifted product: each puncture acts on one factor.
x=symbols('x')
fin=1+2*x+2*x*x+2*x**3+x**4
cusp=fin+2*x*x
euler=expand(-4*(1+x)**8+(4*fin+2*cusp)*(1+x)**4)
h0=[1,2,3,4,5,4,3,2,1]
h1=[int(2*h0[q]-euler.coeff(x,q)) for q in range(9)]
ranks=[0]
for q in range(1,9):
    src=[(a,b) for a in range(5) for b in range(5) if a+b==q]
    tgt=[(a,b) for a in range(5) for b in range(5) if a+b==q-1]
    differential=zeros(len(tgt),len(src))
    for col,(a,b) in enumerate(src):
        # Every nonzero scalar may be replaced by 1 for the rank calculation:
        # the nonzero columns have disjoint support except for single-row pairs.
        if a>0 and b%2==0:differential[tgt.index((a-1,b)),col]+=1
        if b>0 and a%2==0:differential[tgt.index((a,b-1)),col]+=(-1)**a
    ranks.append(differential.rank())
ranks += [0,0]
betti=[]
for n in range(11):
    betti.append((h0[n]-ranks[n] if n<=8 else 0)
                 +(h1[n-1] if 1<=n<=9 else 0)
                 +(h0[n-2]-ranks[n-1] if 2<=n<=10 else 0))
print('Shifted product E2 H0=H2:',h0)
print('Shifted product E2 H1:',h1)
print('Shifted product d2 ranks q=1..8:',ranks[1:9])
print('Shifted product rational Betti numbers:',betti)
assert betti==list(reversed(betti))
assert sum((-1)**k*v for k,v in enumerate(betti))==0
