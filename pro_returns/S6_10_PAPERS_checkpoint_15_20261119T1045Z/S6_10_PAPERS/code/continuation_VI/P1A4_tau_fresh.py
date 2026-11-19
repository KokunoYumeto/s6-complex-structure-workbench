#!/usr/bin/env python3
"""Independent exact representative and toric-character checks from clean data."""
from itertools import permutations
from pathlib import Path
import json

M1=[[1,0,0,0,0,0],[0,1,1,2,2,1],[0,-1,0,-1,0,1],[1,-1,-1,-1,-1,-1],[-1,1,0,0,0,0],[1,0,0,1,0,0]]
M2=[[1,0,0,0,0,0],[0,0,0,0,1,0],[0,-1,-1,-1,-1,-1],[0,0,0,0,0,1],[0,1,0,0,0,0],[0,0,1,0,0,0]]
S=[[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[-1,0,0,0,1,0],[1,0,0,0,0,1],[-1,0,0,0,0,0]]
w=[0,1,1,1,1,1];u2=[1,1,1,0,0,0]
def mv(A,v):return [sum(a*b for a,b in zip(r,v)) for r in A]
def mm(A,B):return [[sum(a*b for a,b in zip(r,c)) for c in zip(*B)] for r in A]
def determinant(A):
    total=0
    for p in permutations(range(len(A))):
        value=(-1)**sum(p[i]>p[j] for i in range(len(A)) for j in range(i+1,len(A)))
        for i,j in enumerate(p):value*=A[i][j]
        total+=value
    return total
def inverse_unimodular(A):
    d=determinant(A);assert abs(d)==1;n=len(A)
    return [[((-1)**(i+j))*determinant([[A[r][c] for c in range(n) if c!=i] for r in range(n) if r!=j])//d for j in range(n)] for i in range(n)]

diff=[]
for M in [M1,M2]:
    d=[a-b for a,b in zip(mv(M,w),w)]
    assert all(x%2==0 for x in d)
    diff.append([x//2 for x in d])
assert diff==[[0,3,-1,-3,0,0],[0,0,-3,0,0,0]]
assert [a-b for a,b in zip(mv(S,u2),w)]==[0,0,0,-2,0,-2]
assert abs(determinant(S))==1 and any(x%2 for x in w)
charts=[]
for order in permutations(range(3)):
    p=[0,0,0];vertices=[p[:]]
    for j in order:p[j]+=1;vertices.append(p[:])
    N=[list(r) for r in zip(*(v+[1] for v in vertices))]
    U=inverse_unimodular(N)
    assert mm(U,N)==[[int(i==j) for j in range(4)] for i in range(4)]
    assert [sum(U[i][j] for i in range(4)) for j in range(4)]==[0,0,0,1]
    parities=[sum(r[:3])%2 for r in U]
    assert sum(parities)%2==0
    charts.append((N,U,parities))
for N,U,parity in charts:
 for N2,U2,parity2 in charts:
    transition=mm(U2,N)
    assert [x%2 for x in mv(transition,parity)]==parity2
out={'status':'all assertions passed','finite_chart_differences':diff,'cusp_representative':'(1/2,1/2,1/2;0,0,0) modulo the supplied lattice','S_determinant':determinant(S),'fundamental_Kuhn_charts':len(charts),'character_transition_checks':len(charts)**2,'global_order':2}
Path(__file__).with_name('P1A4_tau_fresh.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
