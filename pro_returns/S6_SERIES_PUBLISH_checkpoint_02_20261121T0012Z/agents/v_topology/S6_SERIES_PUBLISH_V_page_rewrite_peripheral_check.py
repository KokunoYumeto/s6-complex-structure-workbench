#!/usr/bin/env python3
"""Post-proof-read verification of the prose replacement of three boolean flags.

This uses the same exact Smith-transform method as the topology checker. It is
not claimed as an independent pre-read check or as a full homology rerun.
"""
import itertools
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

def smith(A):
    d,u,v=smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(sp.ZZ))
    d,u,v=(x.to_Matrix() for x in (d,u,v))
    assert d==u*A*v and abs(u.det())==abs(v.det())==1
    rank=sum(d[i,i]!=0 for i in range(min(d.shape)))
    return d,u,v,rank

def exterior(A,k):
    ids=list(itertools.combinations(range(A.rows),k))
    return sp.Matrix(len(ids),len(ids),lambda i,j:A.extract(ids[i],ids[j]).det())

def zero_in_cokernel(D,c):
    d,u,v,rank=smith(D)
    y=u*c
    return all(y[i]%d[i,i]==0 for i in range(rank)) and all(y[i]==0 for i in range(rank,D.rows))

A=sp.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=sp.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,-1],[0,0,-1,0,0,0],[0,0,-2,0,1,-2],[0,1,-2,0,1,-3],[0,0,-1,1,0,-1]])
assert A**5==B**4==sp.eye(6)
print('Input: displayed A and B_1 of maps:src:F.2.18; peripheral order=(order5,order4,cusp).')
for q in [2,3,4]:
    P,Q=exterior(A,q),exterior(B,q)
    n=P.rows
    delta=(P-sp.eye(n)).col_join(Q-sp.eye(n))
    d,u,v,rank=smith(delta)
    assert rank==n
    torsion_indices=[i for i in range(rank) if abs(d[i,i])>1]
    assert len(torsion_indices)==1 and abs(d[torsion_indices[0],torsion_indices[0]])==2
    z=v[:,torsion_indices[0]]
    cocycle=delta*z/2
    assert all(c.q==1 for c in cocycle)
    c1,c2=cocycle[:n,:],cocycle[n:,:]
    T=(P*Q).inv()
    c0=-T*(c1+P*c2)
    assert c0==(T-sp.eye(n))*z/2
    flags=[zero_in_cokernel(D,c) for D,c in [(P-sp.eye(n),c1),(Q-sp.eye(n),c2),(T-sp.eye(n),c0)]]
    assert flags==[True,False,True]
    print('degree',q,'global torsion=Z/2; restrictions zero=',flags)
    print('Exact torsion witness: z=',list(z))
    print('Cocycle is delta(z)/2; cusp cocycle is -T(c1+P*c2)=(T-I)z/2.')
print('The prose replacement matches all three original peripheral flags in degrees2,3,4.')
