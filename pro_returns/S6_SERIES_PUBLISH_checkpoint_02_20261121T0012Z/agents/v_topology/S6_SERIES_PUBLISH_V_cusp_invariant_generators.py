#!/usr/bin/env python3
"""Fresh exact exterior-algebra check of the restored Kuhn Chern generators."""
from itertools import combinations, combinations_with_replacement
from math import comb
from datetime import datetime,timezone
import json
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

def wedge(f,g):
    out={}
    for I,a in f.items():
        for J,b in g.items():
            if set(I)&set(J):continue
            sign=(-1)**sum(i>j for i in I for j in J)
            K=tuple(sorted(I+J));out[K]=out.get(K,0)+sign*a*b
    return {I:a for I,a in out.items() if a}

def smith(A):
    D,L,R=smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(sp.ZZ))
    D,L,R=(x.to_Matrix() for x in (D,L,R))
    assert D==L*A*R
    return D,L,R

records=[]
for n in (2,3):
    d=2*n
    U=sp.eye(d)
    for i in range(n):U[n+i,i]=1
    b=[{(n+i,):1} for i in range(n)]
    even=[{(i,n+i):1} for i in range(n)]
    even += [{(i,n+j):1,(j,n+i):1} for i in range(n) for j in range(i+1,n)]
    candidates={k:[] for k in range(d+1)}
    for r in range(n+1):
        for B in combinations(range(n),r):
            f={():1}
            for j in B:f=wedge(f,b[j])
            for s in range((d-r)//2+1):
                for E in combinations_with_replacement(range(len(even)),s):
                    g=f
                    for j in E:g=wedge(g,even[j])
                    if g:candidates[r+2*s].append(g)
    rows=[]
    for k in range(d+1):
        basis=list(combinations(range(d),k));size=len(basis)
        W=sp.Matrix([[U.extract(I,J).det() for J in basis] for I in basis])
        R=W-sp.eye(size)
        D,L,T=smith(R);rank=sum(D[i,i]!=0 for i in range(size))
        K=T[:,rank:]
        G=sp.Matrix([[f.get(I,0) for f in candidates[k]] for I in basis])
        assert R*G==sp.zeros(size,G.cols)
        coordinates=T.inv()*G
        assert coordinates[:rank,:]==sp.zeros(rank,G.cols)
        C=coordinates[rank:,:]
        DD,LL,TT=smith(C)
        factors=[abs(int(DD[i,i])) for i in range(min(DD.rows,DD.cols)) if DD[i,i]]
        assert factors==[1]*K.cols
        rows.append({'degree':k,'invariant_rank':K.cols,'generated_columns':G.cols,'nonzero_smith_factors':factors})
    records.append({'n':n,'degrees':rows,'all_invariant_lattices_generated_integrally':True})
print(json.dumps({'computed_utc':datetime.now(timezone.utc).isoformat(),'checks':records},indent=2))
