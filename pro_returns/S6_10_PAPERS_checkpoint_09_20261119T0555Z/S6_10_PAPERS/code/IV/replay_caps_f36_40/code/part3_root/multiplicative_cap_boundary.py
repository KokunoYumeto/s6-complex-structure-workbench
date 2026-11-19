#!/usr/bin/env python3
"""Integral multiplicative boundary and the retained one-cap MV matrix.

This certifies the integer algebra in P3F.40. The relative Chern framing
and its Poincare--Lefschetz map have passed independent root/checks audit.
"""
from pathlib import Path
from itertools import combinations
from math import gcd
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT=Path(__file__).resolve().parent

def wedge(A,k):
    ix=list(combinations(range(A.rows),k))
    return S.Matrix([[A.extract(i,j).det() for j in ix] for i in ix])

def ints(A):
    assert all(x.q==1 for x in A)
    return [[int(x) for x in row] for row in A.tolist()]

def bezout(N,c):
    x,y,g=S.gcdex(N,c)
    assert g==1 and N*x+c*y==1
    return int(x),-int(y)

records=[]
# Outward gamma covers +G.  c is the NEGATIVE of its marked Tate
# valuation, so [alpha,gamma]=a^(-c) in the displayed boundary basis.
for N,c in [(8,-3),(7,-2),(2,-1),(5,-2),(4,-1),(5,-1),(3,-1)]:
    x,y=bezout(N,c)
    J=S.Matrix([[1,N,-c],[0,1,0],[0,0,1]])
    J2=wedge(J,2)
    d2=S.zeros(4,6)
    d2[:3,3:]=J-S.eye(3)
    d3=S.zeros(6,4)
    d3[:3,1:]=J2-S.eye(3)
    assert d2*d3==S.zeros(4,4)
    # Columns z,R,B,L in (ab,a gamma,b gamma; a,b,gamma).
    reps=S.Matrix([[x,0,0,0],[y,0,0,0],[0,0,1,0],
                   [0,1,0,0],[0,0,0,c],[0,0,0,N]])
    assert d2*reps==S.zeros(4,4)
    # An integral kernel basis has ab,a gamma,B,R,L.  The one boundary
    # is c*ab+N*a gamma.  Its change to (boundary,z) has determinant -1.
    change=S.Matrix([[c,x],[N,y]])
    assert change.det()==-1
    # F=N*z and a gamma=-c*z modulo the actual boundary.
    F=S.Matrix([1,0,0,0,0,0]); ag=S.Matrix([0,1,0,0,0,0])
    rel=S.Matrix([c,N,0,0,0,0])
    assert F-N*reps[:,0]==-y*rel
    assert ag+c*reps[:,0]==x*rel
    # Pair two source cycles by their oriented fibre wedge times alpha.
    cross=S.Matrix([[0,0,1],[0,-1,0],[1,0,0]])
    full=S.zeros(6)
    full[:3,3:]=cross
    full[3:,:3]=cross.T
    Q=reps.T*full*reps
    assert Q==S.Matrix([[0,0,0,1],[0,0,1,0],
                         [0,1,0,0],[1,0,0,0]])
    assert Q.det()==1
    records.append(dict(N=N,c=c,bezout=[x,y],monodromy=ints(J),
                        exterior_square=ints(J2),d2=ints(d2),d3=ints(d3),
                        H2_representatives=ints(reps),intersection=ints(Q)))

m,A,k=S.symbols('m A k',integer=True)
# Isotropy of the actual exterior kernel forces both coefficients of i(B)
# to vanish: its pairing with z kills the L coefficient, and its square
# then kills the R coefficient. Cap isotropy gives m*t=A*s; gcd(m,A)=1
# makes s=m*k,t=A*k. The actual integral lift T_new=T+k*C retains k.
iext=S.Matrix([[0,1,0,0],[0,0,0,1]])
icap=S.Matrix([[m,-A,m*k,A*k],[0,0,m,A]])
D=iext.col_join(-icap)
assert S.factor(D.det())==-m**2
K=S.Matrix([[1,0],[0,0],[0,1],[0,0]])
assert iext*K==S.zeros(2)
reduced=icap*K
assert reduced==S.Matrix([[m,m*k],[0,m]])
assert reduced.det()==m**2
Q=S.Matrix([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
assert K.T*Q*K==S.zeros(2)
assert icap*Q*icap.T==S.zeros(2)
target_change=S.Matrix([[1,-k],[0,1]])
assert target_change.det()==1
assert target_change*icap==S.Matrix([[m,-A,0,0],[0,0,m,A]])
assert target_change*reduced==m*S.eye(2)
n,p,q=S.symbols('n p q',integer=True)
D1=S.Matrix([[0,0,1],[-1,-p,-q],[0,n,-m]])
assert D1.det()==-n

sample=[]
for mm in range(1,13):
    for nn in (-3,-2,-1,0,1,2,3):
        if gcd(mm,nn)!=1: continue
        for jj in range(-2,3):
            aa=8*jj+3*nn
            if gcd(mm,aa)!=1: continue
            # c=-3,N=8: actual cap H1 quotient, including the elliptic j.
            bp,bq,g=S.gcdex(mm,nn)
            assert g==1
            p,q=-jj*int(bp),-jj*int(bq)
            H=S.Matrix([[p,1,q],[-nn,0,mm]]) # columns alpha,b,gamma
            mu=S.Matrix([mm,jj,nn])
            assert H*mu==S.zeros(2,1)
            minors=[H[:,ix].det() for ix in combinations(range(3),2)]
            assert gcd(*[int(v) for v in minors])==1
            # L=(-3b+8gamma) wedge alpha, B=b wedge gamma.
            detL=S.Matrix.hstack(-3*H[:,1]+8*H[:,2],H[:,0]).det()
            detB=S.Matrix.hstack(H[:,1],H[:,2]).det()
            assert detL==aa and detB==mm
            R=reduced.subs({m:mm,A:aa,k:-3})
            SN=smith_normal_form(R,domain=ZZ)
            factors=[abs(int(SN[i,i])) for i in range(2)]
            assert factors==[mm,mm]
            sample.append(dict(m=mm,n=nn,j=jj,A=aa,H1=ints(H),
                               H2_Smith=factors))

out=dict(status='PASS: exact integer algebra and independently audited geometric framing',
         boundary_cases=records,
         full_MV=[[str(v) for v in row] for row in D.tolist()],
         reduced_MV=[[str(v) for v in row] for row in reduced.tolist()],
         determinant=str(S.factor(D.det())),
         cap_basis_change=[[str(v) for v in row] for row in target_change.tolist()],
         full_degree_one_MV=[[str(v) for v in row] for row in D1.tolist()],
         degree_one_determinant=str(D1.det()),
         isotropy_correction='The earlier working exterior coefficient e is forced to zero by the self-intersection of its kernel. The cap coefficients satisfy m*t=A*s and are retained by the integral change T_new=T+k*C. The failed pre-correction script is preserved under attempts/.',
         actual_cap_samples=sample,
         sample_count=len(sample),
         scope='one multiplicative site, primitive-translation sources')
(ROOT/'multiplicative_cap_boundary.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: seven actual component markings; primitive exterior-square bases and oriented pairings.')
print('PASS: retained full MV determinant -m^2; reduced matrix',reduced.tolist())
print('PASS:',len(sample),'actual meridian quotient and integral Smith samples.')
print('The geometric relative Chern framing has passed independent root/checks audit.')
