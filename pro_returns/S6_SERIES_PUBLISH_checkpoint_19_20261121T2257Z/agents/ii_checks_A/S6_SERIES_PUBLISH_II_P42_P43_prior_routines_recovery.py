#!/usr/bin/env python3
"""Exact integral Mayer--Vietoris computation for the Part 4 example.

Basis conventions and the geometric derivation of these matrices are in
notes/part4.md.  This program prints every nonzero differential used.
The only external dependency is SymPy.  All arithmetic is integral/rational.
"""
from itertools import combinations
from pathlib import Path
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

HERE = Path(__file__).resolve().parent
E = S.eye(4)
pairs = list(combinations(range(4), 2))

def wedge(x, y):
    return S.Matrix([x[i]*y[j]-x[j]*y[i] for i,j in pairs])

def wedge2(A):
    return S.Matrix.hstack(*(wedge(A[:,i], A[:,j]) for i,j in pairs))

def smith(A):
    D=smith_normal_form(A,domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]

def show(name,A):
    print(name, 'shape=',A.shape)
    print(A)
    if A.rows and A.cols:
        print('rank=',A.rank(),'Smith=',smith(A))
    print()

# Local ordered lattice coordinates are (a,c,b,d): the two C cycles first,
# then the two B cycles. Columns of S_i express them in (e1,e2,e3,e4).
markings=[
    S.Matrix.hstack(E[:,2],E[:,3],E[:,0],E[:,1]),
    S.Matrix.hstack(E[:,1]+E[:,3],-E[:,0]-E[:,2],E[:,2],E[:,3]),
    S.Matrix.hstack(E[:,0]+E[:,3],E[:,1]-E[:,2],E[:,2],E[:,3]),
]
local_H1=[]
local_H2=[]
for i,A in enumerate(markings,1):
    assert abs(A.det())==1
    Q=A.inv()
    # H1(U_i) basis (c,b,d); H2(U_i) basis (ab,ad,cb,cd,bd).
    R1=Q[[1,2,3],:]
    R2=wedge2(Q)[[1,2,3,4,5],:]
    local_H1.append(R1)
    local_H2.append(R2)
    show(f'S_{i}',A)
    show(f'R1_{i}',R1)
    show(f'R2_{i}',R2)

# Local cellular chain model: T^4 plus r in degree2, rc and h in degree3,
# hc in degree4. d(r)=a, d(rc)=a wedge c; all other boundaries vanish.
# Ordered torus cells use (a,c,b,d) and lexicographic wedge bases.
local_d1=S.zeros(1,4)
local_d2=S.zeros(4,7); local_d2[0,6]=1
local_d3=S.zeros(7,6); local_d3[0,4]=1
local_d4=S.zeros(6,2)
for k,D in enumerate([local_d1,local_d2,local_d3,local_d4],1):
    show(f'local_d{k}',D)
assert local_d1*local_d2==S.zeros(1,7)
assert local_d2*local_d3==S.zeros(4,6)
assert local_d3*local_d4==S.zeros(7,2)
print('Local U Betti numbers: [1,3,5,5,2] (all integral groups free).\n')

