#!/usr/bin/env python3
"""Fresh exact boundary arithmetic before opening the eight target proofs.

Fraction elimination and coefficient-grid interpolation are used here. The
written derivations prove the analytic and all-degree assertions. This program
does not certify an analytic descent by finite sampling.
"""
from fractions import Fraction as F
from itertools import product
import json

def tr(a): return list(map(list, zip(*a)))
def mul(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def inv(a):
    n=len(a); z=[[F(x) for x in row]+e for row,e in zip(a,eye(n))]
    for j in range(n):
        k=next(k for k in range(j,n) if z[k][j]);z[j],z[k]=z[k],z[j]
        c=z[j][j];z[j]=[x/c for x in z[j]]
        for k in range(n):
            if k!=j:
                c=z[k][j];z[k]=[x-c*y for x,y in zip(z[k],z[j])]
    return [r[n:] for r in z]
def power(a,n):
    b=eye(len(a))
    for _ in range(n): b=mul(b,a)
    return b
def mv(a,v): return [sum(x*y for x,y in zip(r,v)) for r in a]
def dot(v,w): return sum(x*y for x,y in zip(v,w))
def plus(v,w): return tuple(x+y for x,y in zip(v,w))
def minus(v,w): return tuple(x-y for x,y in zip(v,w))
def q(a,v): return dot(v,mv(a,v))

A1=[[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]
A2=[[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]]
v1=[1,2,-4,0];v2=[-1,-3,3,0];delta=[0,0,0,1]
Q=[[0,0,0,6],[0,0,1,0],[0,-1,0,0],[-6,0,0,0]]
finite=[]
for a,v,m in [(A1,v1,3),(A2,v2,4)]:
    t=tr(inv(a));ti=inv(t)
    n=[[F(0)]*4 for _ in range(4)];ni=[[F(0)]*4 for _ in range(4)]
    for k in range(m): n=add(n,power(t,k));ni=add(ni,power(ti,k))
    assert power(a,m)==eye(4) and mv(a,v)==v and mv(a,delta)==delta
    assert mul(mul(tr(a),Q),a)==Q and n==ni
    assert t[-1]==[0,0,0,1]
    contraction=[sum(v[k]*Q[k][j] for k in range(4)) for j in range(4)]
    finite.append({'order':m,'contraction':contraction,'norm_invariant_under_inverse':True})
assert finite[0]['contraction']==[0,4,2,6]
assert finite[1]['contraction']==[0,-3,-3,-6]
boundary_coefficient=F(6,3)-F(6,4)
assert boundary_coefficient==F(1,2)

H=[[1,0],[0,-6]];B0=[[0,1],[-1,0]];HB=mul(H,B0)
C_basis=[[[6,0],[0,1]],[[0,1],[-1,0]],[[0,0],[1,0]]]
assert all((s:=mul(tr(c),HB))==tr(s) for c in C_basis)
grid=list(product([-1,0,1],repeat=2)); shift_checks=0
for v,lam in product(grid,repeat=2):
    b=mv(B0,lam)
    assert q(H,plus(v,b))-q(H,v)==2*dot(mv(H,b),v)+q(H,b)
    shift_checks+=1
for lam,mu in product(grid,repeat=2):
    for c in C_basis:
        s=mul(tr(c),HB)
        assert q(s,plus(lam,mu))-q(s,lam)-q(s,mu)==2*dot(lam,mv(s,mu))

rays=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
qvals=[q(H,a) for a in rays]
degrees=[qvals[(i-1)%6]+qvals[(i+1)%6]-qvals[i] for i in range(6)]
assert qvals==[1,-6,-5,1,-6,-5]
assert degrees==[-12,2,0,-12,2,0]
# Actual bundle action is inverse to the multiplier Psi^*O(D)->O(D).
cross=mul(tr(B0),H)
chern=[[0]*4 for _ in range(4)]
for i in range(2):
    for j in range(2):
        chern[i][j+2]=-2*cross[i][j];chern[j+2][i]=2*cross[i][j]
assert chern==[[-2*x for x in r] for r in Q]

def support(b,v):
    x,y=v
    return b[0][0]*x*(x-1)//2+b[0][1]*x*y+b[1][1]*y*(y-1)//2
def degs(b,v):
    return [support(b,plus(v,rays[(i-1)%6]))+support(b,plus(v,rays[(i+1)%6]))
            -support(b,plus(v,rays[i]))-support(b,v) for i in range(6)]
support_checks=0
for b in [[[1,0],[0,0]],[[0,1],[1,0]],[[0,0],[0,1]]]:
    expected=[b[1][1]-b[0][1],b[0][0]-b[0][1],b[0][1]]*2
    for v in grid:
        d=degs(b,v);assert d==expected
        assert [[d[1]+d[2],d[2]],[d[2],d[0]+d[2]]]==b
        support_checks+=1
    for lam,v in product(grid,repeat=2):
        a=mv(B0,lam)
        # Removing the value at the origin leaves exactly the linear part.
        lhs=support(b,plus(v,a))-support(b,v)-support(b,a)+support(b,(0,0))
        assert lhs==dot(mv(b,a),v)

print(json.dumps({'status':'passed','method':'Fraction elimination; integer coefficient basis and bounded-degree interpolation',
 'scope':'Finite identities corroborate the separately written analytic proofs; no unknown prior program is compared.',
 'finite_norms':finite,'boundary_coefficient':str(boundary_coefficient),
 'quadratic_shift_grid_checks':shift_checks,'quadratic_values':qvals,'central_degrees':degrees,
 'chern_matrix_minus_2q':chern,'support_basis_checks':support_checks,
 'polynomial_completeness':'Each shift identity has degree at most two in each of its four variables; the three-point tensor grid determines every coefficient. Support identities are linear in the three symmetric-matrix coefficients; each basis is checked. General analytic claims are proved in the derivation.'},indent=2))
