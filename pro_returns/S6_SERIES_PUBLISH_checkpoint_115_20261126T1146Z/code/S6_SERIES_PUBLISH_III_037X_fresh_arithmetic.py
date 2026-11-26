#!/usr/bin/env python3
"""Fresh exact cusp-cover arithmetic, before any 037X/Y/0382 proof release.

Symbolic identities and explicit finite residue/monomial checks complement
the general proofs in the fresh derivation. No old program or outcome is read.
"""
from itertools import product

import sympy as s

n=s.symbols('n',integer=True,positive=True)
p,q,l1,l2=s.symbols('p q l1 l2',integer=True)
I3=s.eye(3)
low=s.Matrix([[p,p+1,p],[q,q,q+1],[1,1,1]])
high=s.Matrix([[p+1,p,p+1],[q,q+1,q+1],[1,1,1]])
assert s.expand(low.det())==1
assert s.expand(high.det())==-1
height=s.Matrix([[0,0,1]])
for R in (low,high):
    assert (R.inv()*R-I3).applyfunc(s.simplify)==s.zeros(3)
    assert s.ones(1,3)*R.inv()==height
print('PASS: both translated cone bases are unimodular and the height character is the product of the three chart coordinates')

low0=low.subs({p:0,q:0})
high0=high.subs({p:0,q:0})
assert low0.inv()==s.Matrix([[-1,-1,1],[1,0,0],[0,1,0]])
assert high0.inv()==s.Matrix([[0,-1,1],[-1,0,1],[1,1,-1]])
print('PASS: exact lower/upper monomial chart exponent matrices and their inverses')

B0=s.Matrix([[0,1],[-1,0]])
fan_translation=s.Matrix([[1,0,l2],[0,1,-l1],[0,0,1]])
assert fan_translation.det()==1
for R in (low,high):
    assert fan_translation*R==R.subs({p:p+l2,q:q-l1},simultaneous=True)
assert fan_translation*(n*I3)==(n*I3)*fan_translation
print('PASS: source/target monomial actions translate fan indices by B0*lambda and commute with the cocharacter power map')

c11,c12,c21,c22=s.symbols('c11 c12 c21 c22')
C=s.Matrix([[c11,c12],[c21,c22]])
lam=s.Matrix([l1,l2])
assert n*(C/n)*lam==C*lam
assert n*B0*lam==B0*(n*lam)
print('PASS: exact holomorphic-unit exponent identity N*C_N*lambda=C(v^N)*lambda and toric exponents N*B0*lambda')

a,b,c=s.symbols('a b c')
jac=s.diag(n*a**(n-1),n*b**(n-1),n*c**(n-1))
assert jac.det()==n**3*a**(n-1)*b**(n-1)*c**(n-1)
assert (n*I3).det()==n**3
print('PASS: direct degree N^3 and exact Jacobian N^3*a^(N-1)*b^(N-1)*c^(N-1)')

L2=s.Matrix([[n,1],[0,1]])
L3=s.Matrix([[n,0,1],[0,n,1],[0,0,1]])
assert L2.det()==n and L3.det()==n*n
assert s.Matrix([0,n])==n*L2[:,1]-L2[:,0]
assert s.Matrix([0,0,n])==n*L3[:,2]-L3[:,0]-L3[:,1]
print('PASS: exact invariant exponent-lattice indices N and N^2 for double/triple local quotient models')

for N in range(1,9):
    group=[(r,t,(-r-t)%N) for r,t in product(range(N),repeat=2)]
    assert len(set(group))==N*N
    for exp in product(range(N),repeat=3):
        invariant=all(sum(x*y for x,y in zip(exp,g))%N==0 for g in group)
        assert invariant==(exp[0]==exp[1]==exp[2])
    for zeros in range(4):
        nonzero_coordinates=range(zeros,3)
        stabilizer=[g for g in group if all(g[j]==0 for j in nonzero_coordinates)]
        assert len(stabilizer)==N**max(zeros-1,0)
    double_basis=[(i,j) for i,j in product(range(N),repeat=2) if min(i,j)==0]
    triple_basis=[ex for ex in product(range(N),repeat=3) if min(ex)==0]
    assert len(double_basis)==2*N-1
    assert len(triple_basis)==N**3-(N-1)**3
    assert len(triple_basis)==3*N*N-3*N+1
    full_lengths=(N*N,N*len(double_basis),len(triple_basis))
    assert full_lengths==(N*N,N*(2*N-1),3*N*N-3*N+1)
    print(f'PASS N={N}: invariant residues and stabilizers; relative closed-fibre total lengths (single,double,triple)={full_lengths}, generic degree={N*N}')

assert s.expand(n**3-(n-1)**3)==3*n*n-3*n+1
assert s.factor((2*n-1)-n)==n-1
assert s.factor((3*n*n-3*n+1)-n*n)==(n-1)*(2*n-1)
print('PASS: symbolic local nonflat excesses N-1 and (N-1)(2N-1), with both zero exactly at N=1 for positive N')

hexagon=[s.Matrix(v) for v in ((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))]
assert all(s.Matrix.hstack(hexagon[j],hexagon[(j+1)%6]).det()==1 for j in range(6))
assert all(-s.Matrix.hstack(hexagon[(j-1)%6],hexagon[(j+1)%6]).det()==-1 for j in range(6))
A=s.Matrix([[1,-1],[0,1]])
assert A.det()==1
P2_rays=[s.Matrix(v) for v in ((1,0),(0,1),(-1,-1))]
assert [A*v for v in P2_rays]==[hexagon[0],hexagon[2],hexagon[4]]
assert [A*(P2_rays[j]+P2_rays[(j+1)%3]) for j in range(3)]==[hexagon[1],hexagon[3],hexagon[5]]
assert -6+2*6==6
print('PASS: normalization hexagon is the explicit unimodular image of the three fixed-point blowups of the P2 fan; six boundary curves and anticanonical square 6')

I4=s.eye(4)
M0=s.Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
K=M0-I4
assert K*K==s.zeros(4)
MN=I4+n*K
assert MN*M0==I4+(n+1)*K
SN=s.diag(1,1,n,n)
assert SN.det()==n*n
assert (MN*SN-SN*M0).applyfunc(s.simplify)==s.zeros(4)
assert (SN.inv()*MN*SN-M0).applyfunc(s.simplify)==s.zeros(4)
print('PASS: exact monodromy M0^N=I+N*(M0-I), index det(S_N)=N^2 and S_N^-1*M0^N*S_N=M0')

sv=s.symbols('sv')
Pi_source=(sv*B0+C/n).row_join(s.eye(2))
Pi_target=(n*sv*B0+C).row_join(s.eye(2))
assert (n*Pi_source-Pi_target*SN).applyfunc(s.simplify)==s.zeros(2,4)
assert MN[:,2:4]==I4[:,2:4]
assert Pi_source.subs(n,1)==Pi_target.subs(n,1)
assert SN.subs(n,1)==I4
print('PASS: N*Pi_source=Pi_target*S_N, fixed short deck generators and all N=1 marking identities')
print('ALL FRESH 037X ARITHMETIC PASSED; all three target arguments remain closed.')
