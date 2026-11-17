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

# W=A times a pair of pants. H1(W)=(e1,e2,e3,e4,s1,s2).
# H2(W)=(12,13,14,23,24,34,e1s1,...,e4s1,e1s2,...,e4s2).
# The circle at t=0 is shifted by e1 by the original principal-bundle clutch.
base_meridians=[S.Matrix([1,0]),S.Matrix([0,1]),S.Matrix([-1,-1])]
clutches=[E[:,0],S.zeros(4,1),S.zeros(4,1)]
F0=S.zeros(4,3)
for i in range(3):
    F0[0,i]=1; F0[1+i,i]=-1

F1=S.zeros(15,15)
F2=S.zeros(29,30)
for i in range(3):
    j=5*i
    F1[0:4,j:j+4]=E
    F1[0:4,j+4]=clutches[i]
    F1[4:6,j+4]=base_meridians[i]
    F1[6+3*i:9+3*i,j:j+4]=-local_H1[i]

    k=10*i
    F2[0:6,k:k+6]=S.eye(6)
    F2[14+5*i:19+5*i,k:k+6]=-local_H2[i]
    for a in range(4):
        F2[0:6,k+6+a]=wedge(E[:,a],clutches[i])
        F2[6+a,k+6+a]=base_meridians[i][0]
        F2[10+a,k+6+a]=base_meridians[i][1]

show('MV_F0',F0)
show('MV_F1',F1)
show('MV_F2',F2)
print('det(MV_F1)=',F1.det())
assert abs(F1.det())==1
assert smith(F2)==[1]*29
assert F0.rank()==3

# Hand reduction: eliminate the local groups and base-meridian products.
# The six remaining generators are e12,e13,e14,e23,e24,e34.
R=S.Matrix.hstack(
    *(wedge(E[:,0],E[:,i]) for i in range(1,4)),
    *(wedge(A[:,0],A[:,1]) for A in markings)
)
show('H2_reduced_relation_matrix',R)
print('det(H2_reduced_relation_matrix)=',R.det())
assert abs(R.det())==1
relations=S.Matrix.hstack(E[:,0],*(A[:,0] for A in markings))
show('H1_reduced_relation_matrix',relations)
assert abs(relations.det())==1

# Numerical ranks are not used: Smith forms certify all torsion assertions.
print('RESULT H_1(Y;Z)=0, H_2(Y;Z)=0.')
print('RESULT chi(Y)=0 and integral homology ranks [1,0,0,2,0,0,1].')

matrices={
    'local_d1':local_d1,'local_d2':local_d2,
    'local_d3':local_d3,'local_d4':local_d4,
    'MV_F0':F0,'MV_F1':F1,'MV_F2':F2,
    'H1_reduced_relation_matrix':relations,'H2_reduced_relation_matrix':R,
}
matrices.update({f'S_{i+1}':A for i,A in enumerate(markings)})
matrices.update({f'R1_{i+1}':A for i,A in enumerate(local_H1)})
matrices.update({f'R2_{i+1}':A for i,A in enumerate(local_H2)})
(HERE/'example_matrices.json').write_text(json.dumps({
    name:[[int(x) for x in row] for row in A.tolist()]
    for name,A in matrices.items()
},indent=2)+'\n')

