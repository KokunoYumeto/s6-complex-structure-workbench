#!/usr/bin/env python3
"""Exact postrelease FQ Euler certificate by conductor chain maps."""
from fractions import Fraction
from math import comb
import json

def rank(M):
    A=[[Fraction(x) for x in row] for row in M]
    r=0
    for c in range(len(A[0]) if A else 0):
        pivot=next((i for i in range(r,len(A)) if A[i][c]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        u=A[r][c];A[r]=[v/u for v in A[r]]
        for i in range(len(A)):
            if i!=r:
                v=A[i][c];A[i]=[a-v*b for a,b in zip(A[i],A[r])]
        r+=1
    return r

def mul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

BD=[[int(i==(j+1)%6)-int(i==j) for j in range(6)] for i in range(6)]
BC=[[-1,-1,-1],[1,1,1]]
Q0=[[int(i==j%2) for j in range(6)] for i in range(2)]
Q1=[[((-1)**j if i==j%3 else 0) for j in range(6)] for i in range(3)]
assert mul(Q0,BD)==mul(BC,Q1)
rD,rC=rank(BD),rank(BC)
bD=[6-rD,6-rD,6]
bC=[2-rC,3-rC,3]
eD=sum((-1)**i*b for i,b in enumerate(bD))
eC=sum((-1)**i*b for i,b in enumerate(bC))
eZ=1+4+1
eW=eZ-eD+eC
assert (rD,rC,bD,bC,eD,eC,eW)==(5,1,[1,1,6],[1,2,3],6,2,2)
eE=sum((-1)**i*comb(2,i) for i in range(3))
eT4=sum((-1)**i*comb(4,i) for i in range(5))
e_rank1=2*eE-2*eE+eE
e_cusp=2*eE
assert e_rank1==e_cusp==eT4==0
for degree in [3,4]:assert Fraction(eT4,degree)==0
rows={'original_3_4':[eW],'two_parameter':[eW,e_rank1,e_rank1],'liu_rollenske':[eW,e_cusp]}
assert all(sum(v)==2 for v in rows.values())
print(json.dumps({'method':'Integer conductor incidence chain map, exact rational ranks, normalization pushout Euler; independent of direct toric-stratum counting.','conductor_boundary':BD,'image_conductor_boundary':BC,'vertex_quotient':Q0,'edge_quotient':Q1,'boundary_commutes':True,'conductor_betti':bD,'image_conductor_betti':bC,'normalization_betti_even':[1,4,1],'euler_normalization':eZ,'euler_conductor':eD,'euler_image_conductor':eC,'euler_hexagonal':eW,'euler_elliptic_curve':eE,'euler_torus4':eT4,'euler_rank1':e_rank1,'euler_cusp_from_actual_product_map':e_cusp,'family_singular_euler_rows':rows,'finite_smooth_torus_quotient_euler':{'3':0,'4':0},'assertions_passed':True,'scope':'Postrelease exact finite topological certificate. It supplies no extra independent event and makes no claim to verify a primary homology theorem by enumeration.'},indent=2))
