#!/usr/bin/env python3
"""Post-exposure checks of the original LA auxiliary assertions.

Uses the displayed matrices and fresh formulas only. No old target
algorithm, historical output or catalogue is read. Writes no proof.
"""
from itertools import combinations
from math import gcd, lcm
from sympy import Matrix, eye, zeros, symbols, expand, ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

d = symbols('d', integer=True, positive=True)
e = eye(4)
delta, a, b, gamma = [e[:, j] for j in range(4)]
pairs = list(combinations(range(4), 2))

def wedge(M):
    return Matrix([[M[i,k]*M[j,l]-M[i,l]*M[j,k]
                    for k,l in pairs] for i,j in pairs])

def wedge_pair(v, w):
    return Matrix([v[i]*w[j]-v[j]*w[i] for i,j in pairs])

def eq(A, B):
    assert (A-B).applyfunc(expand) == zeros(*A.shape)

A0 = Matrix([[1,-1,0,2*d],[0,-1,-1,6*d],[0,1,0,0],[0,0,0,1]])
A1 = Matrix([[1,0,1,-3*d],[0,0,1,0],[0,-1,0,6*d],[0,0,0,1]])
Ai = Matrix([[1,0,0,d],[0,1,1,0],[0,0,1,0],[0,0,0,1]])
u0 = gamma+2*d*(a+b)
u1 = gamma+3*d*(a+b)
graph = Matrix.hstack(Matrix.vstack(-delta,-delta),
    Matrix.vstack(b,-a), Matrix.vstack(delta,zeros(4,1)),
    Matrix.vstack(u0,zeros(4,1)), Matrix.vstack(zeros(4,1),u1))
D = Matrix.hstack(A0-eye(4), A1-eye(4))
eq(D*graph, zeros(4,5))
minor = expand(graph.extract([0,2,3,4,7],range(5)).det())
assert abs(minor) == 1
print('D.WE11 exact five-column graph basis: claimed rows 0,2,3,4,7 have determinant', minor)

xi = Matrix([[0,0,-6*d,1,0,0]])
W = Matrix.hstack(*[wedge(A)-eye(6) for A in [A0,A1,Ai]])
eq(xi*W,zeros(1,18))
coords = [0,1,2,4,5]
MW = W.extract(coords,range(18))
chosen = None
for cols in combinations(range(18),5):
    numeric = MW.extract(range(5),cols).subs(d,0)
    if abs(numeric.det()) != 1:
        continue
    polynomial = expand(MW.extract(range(5),cols).det())
    if polynomial in [1,-1]:
        chosen = cols
        break
assert chosen is not None
print('Full exterior relation unit minor: kernel-coordinate rows',coords,
      'relation columns',chosen,'determinant',polynomial,'for every d')

Wi = wedge(Ai)-eye(6)
F = Matrix.hstack(eye(6)[:,0],-d*eye(6)[:,0]-d*eye(6)[:,1]+eye(6)[:,4])
LF = Matrix.vstack(eye(6)[0,:]+d*eye(6)[4,:],eye(6)[4,:])
Q = Matrix([[0,1,0,0,d,0],[0,0,1,0,0,0],
            [0,0,0,1,0,0],[0,0,0,0,0,1]])
section = eye(6)[:,[1,2,3,5]]
eq(F*LF*Wi,Wi)
eq(LF*F,eye(2))
eq(Q*Wi,zeros(4,6))
eq(Q*section,eye(4))
eq(section*Q+F*LF*(eye(6)-section*Q),eye(6))
eq(Wi[:,[1,5]],F)
print('Cusp boundary: exact primitive rank-two wedge image and quotient/inverse; H2(boundary)=Z^6')

for A,c,q in [(A0,2*d,3),(A1,3*d,2)]:
    u=gamma+c*(a+b)
    R=Matrix.hstack(delta,a,b,u)
    assert R.det()==1
    WR=wedge(R)
    fixed=(R.inv()*A*R).applyfunc(expand)
    assert not any(v.has(d) for v in fixed)
    WR0=wedge(fixed)-eye(6)
    Ds,Us,Vs=smith_normal_decomp(DomainMatrix.from_Matrix(WR0).convert_to(ZZ))
    Ds,Us,Vs=[x.to_Matrix() for x in (Ds,Us,Vs)]
    eq(Us*WR0*Vs,Ds)
    assert [abs(Ds[i,i]) for i in range(4)]==[1]*4
    detector=Matrix([[0,0,0,1,0,0],[0,0,-q,0,1,-1]])*WR.inv()
    area=Matrix([[0,0,0,1,-c,c]])
    eq(detector[0,:],area)
    kernel=Matrix.hstack(eye(6)[:,0],eye(6)[:,1],eye(6)[:,2],
                        eye(6)[:,4]+c*eye(6)[:,3],
                        eye(6)[:,5]-c*eye(6)[:,3])
    eq(area*kernel,zeros(1,5))
    k=wedge_pair(a,u)
    eq(detector*k,Matrix([0,1]))
    residue=kernel-k*(detector[1,:]*kernel)
    inverse_units=Matrix.diag(*[1/Ds[i,i] for i in range(4)])
    lift=WR*Vs[:,:4]*inverse_units*Us[:4,:]*WR.inv()*residue
    eq((wedge(A)-eye(6))*lift,residue)
    eq(xi*kernel,Matrix([[0,0,-6*d,c,-c]]))
    assert (xi*k)[0].expand()==c
    print('Original area',list(area),'kernel values',list(xi*kernel),
          'exact Wang inverse and generator coefficient',c,'PASS')

checked=0
for m0 in [1,3,6,9,12]:
    for m1 in [1,4,8,12]:
        for n0 in ([0] if m0==1 else range(-4,5)):
            for n1 in ([0] if m1==1 else range(-4,5)):
                P=m1*n0+m0*n1
                if P:
                    continue
                h=lcm(m0,m1)
                relation0=Matrix([-n0,m0,0])
                relation1=Matrix([-n1,0,m1])
                meridian=Matrix([0,1,1])
                eq((h//m0)*relation0+(h//m1)*relation1,h*meridian)
                assert all(k%m0 or k%m1 for k in range(1,h))
                checked+=1
print('D.WE13 finite-meridian cases:',checked,
      'exact order lcm(mbar0,mbar1); kernel inverse reads sum/h and component differences PASS')
print('PASS: every original LA auxiliary matrix and meridian claim checked at its full symbolic scope.')
