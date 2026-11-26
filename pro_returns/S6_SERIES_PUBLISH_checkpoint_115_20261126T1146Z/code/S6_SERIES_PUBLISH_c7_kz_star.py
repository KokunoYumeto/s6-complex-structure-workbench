#!/usr/bin/env python3
"""Fresh I3-star exclusion constants and reflection-quotient calculation.

The inputs are the admitted KY local matrices and root's freshly derived
KX initial rows. No KZ original proof or old KZ program is read.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
import json

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02KX_fresh_candidate_data.json'


def mul(A,B):
    return [[sum(x*y for x,y in zip(r,c)) for c in zip(*B)] for r in A]


def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def sub(A,B):
    return [[x-y for x,y in zip(r,s)] for r,s in zip(A,B)]


def rank(A):
    B=[list(map(Fraction,r)) for r in A]
    k=0
    for j in range(len(B[0])):
        p=next((i for i in range(k,len(B)) if B[i][j]),None)
        if p is None: continue
        B[k],B[p]=B[p],B[k]
        q=B[k][j]; B[k]=[x/q for x in B[k]]
        for i in range(len(B)):
            if i!=k:
                q=B[i][j]; B[i]=[x-q*y for x,y in zip(B[i],B[k])]
        k+=1
    return k


def wedge(A):
    pairs=list(combinations(range(4),2))
    return [[A[i][k]*A[j][l]-A[i][l]*A[j][k]
             for k,l in pairs] for i,j in pairs]


rows=[r for r in json.loads(DATA.read_text())['natural'] if r['OS']==46]
assert len(rows)==8
for r in rows:
    assert (r['a'],r['b']) in ((1,4),(4,1))
    print('INITIAL',r['OS'],r['profile'],r['a'],r['b'],r['zero_index'],'PASS')
assert sum(r['profile']=='default' for r in rows)==6
assert sum(r['profile']=='II' for r in rows)==2

inputs=[
 (1,[[ -1,-3,0,4],[0,-1,0,4],[-1,-2,1,3],[0,0,0,1]],
  [[2],[0],[1],[0]],
  [[2,0,-1,0],[0,1,0,2],[1,0,0,0],[0,0,0,1]],
  [[0,0,1,0],[0,1,0,-2],[-1,0,2,0],[0,0,0,1]]),
 (4,[[-1,-3,0,1],[0,-1,0,1],[-4,-8,1,3],[0,0,0,1]],
  [[1],[0],[2],[0]],
  [[1,0,0,0],[0,0,0,1],[2,0,1,0],[0,-1,0,2]],
  [[1,0,0,0],[0,2,0,-1],[-2,0,1,0],[0,1,0,0]])]
for a,T,w,H,Hi in inputs:
    assert mul(H,Hi)==eye(4)==mul(Hi,H)
    S=sub(mul(T,T),eye(4))
    assert mul(S,S)==[[0]*4 for _ in range(4)]
    expected=eye(4);expected[0][1]=3
    assert mul(mul(Hi,mul(T,T)),H)==expected
    assert mul(T,w)==[[-x[0]] for x in w]
    f=4-rank(sub(T,eye(4)))
    g=6-rank(sub(wedge(T),eye(6)))
    assert (f,g)==(2,2)
    print('LOCAL',a,'fixed',f,'degree2_coinvariants',g,
          'boundary_b2',f+g,'square Jordan coefficient',3,
          'nilpotent square zero and vanishing-circle sign -1 PASS')

# The affine D7 marking has outer classes 0,G,2G,3G at 0,6,1,7.
edges=[(0,2),(1,2),(2,3),(3,4),(4,5),(5,6),(5,7)]
C=[[-2*int(i==j) for j in range(8)] for i in range(8)]
for i,j in edges:C[i][j]=C[j][i]=1
perm=[6,7,5,4,3,2,1,0]
P=[[int(i==perm[j]) for j in range(8)] for i in range(8)]
assert mul(mul(mul(P,P),P),P)==eye(8)
assert mul([list(x) for x in zip(*P)],mul(C,P))==C
mult=[[x] for x in [1,1,2,2,2,2,1,1]]
assert mul(C,mult)==[[0] for _ in range(8)] and rank(C)==7
orbits=[{0,1,6,7},{2,5},{3,4}]
B=[[int(j in o) for o in orbits] for j in range(8)]
restricted=mul([list(x) for x in zip(*B)],mul(C,B))
assert rank(restricted)==2
kernel=[[int(i==j)+(int(i==6) if j==0 else 0)
         for j in [0,1,2,3,4,5,7]] for i in range(8)]
chern=[[int(i==6)-int(i==0) for i in range(8)]]
assert mul(chern,kernel)==[[0]*7] and rank(kernel)==7
print('ORIGINAL D7 multiplicity kernel rank7; generator orbits3;')
print('ORIGINAL zero-Chern restricted intersection rank2; nonzero-Chern kernel rank7 PASS')

for ell in range(1,13):
    N=3*ell
    values=[]
    for c in range(N):
        perm=[(c-j)%N for j in range(N)]
        assert all(perm[perm[j]]==j for j in range(N))
        seen=set();orbits=[]
        for j in range(N):
            if j in seen:continue
            orbit={j,perm[j]};seen.update(orbit);orbits.append(orbit)
        fixed=sum(perm[j]==j for j in range(N))
        expected=(N+fixed)//2
        assert len(orbits)==expected and expected>=2
        # Orbit sums form the invariant component lattice; the total
        # fibre has coefficient one on each orbit sum.
        B=[[int(j in o) for o in orbits] for j in range(N)]
        assert rank(B)==expected
        assert all(sum(r)==1 for r in B)
        values.append(expected-1)
    print('COVER',2*ell,'COMPONENTS',N,'ALL_REFLECTION_OFFSETS',N,
          'LOCAL_DEFECT_RANGE',min(values),max(values),'PASS')
print('PASS 8 natural initial rows; both exact marked star matrices;')
print('PASS complete tested reflection quotients, with positive component defect.')
