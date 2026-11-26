#!/usr/bin/env python3
"""Fresh LV source-sphere link algebra; no target original/history input.

This records the exact vertical critical-cycle preimage and tests candidate
intersection functionals on the integral relation kernel.  A failed
functional test is retained as an obstruction, not promoted to a link.
"""
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
from hashlib import sha256
import json
import sympy as S
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

print('START', datetime.now(timezone.utc).isoformat())
root=Path(__file__).resolve().parents[1]
e=S.eye(4)
pairs=list(combinations(range(4),2))
def wedge(x,y):
    return S.Matrix([x[i]*y[j]-x[j]*y[i] for i,j in pairs])
def exterior(A):
    return S.Matrix.hstack(*(wedge(A[:,i],A[:,j]) for i,j in pairs))
def smith(M):
    d,u,v=smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(ZZ))
    D,U,V=(q.to_Matrix() for q in (d,u,v))
    assert U*M*V==D and abs(U.det())==abs(V.det())==1
    rank=sum(D[i,i]!=0 for i in range(min(D.shape)))
    return D,U,V,rank
As=[
S.Matrix([[1,8,0,24],[0,1,0,0],[0,-6,1,-16],[0,0,0,1]]),
S.Matrix([[1,1,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]),
S.Matrix([[3,4,0,16],[-1,-1,0,-8],[-2,-4,1,-16],[0,0,0,1]]),
S.Matrix([[3,1,0,8],[-4,-1,0,-16],[-4,-2,1,-16],[0,0,0,1]]),
S.Matrix([[0,1,0,0],[-1,2,0,0],[0,0,1,0],[0,0,0,1]])]
assert S.prod(As)==S.eye(4)
a,b,d,g=(e[:,i] for i in range(4))
B1=-8*b+3*g;B2=-3*b+g
vc=2*wedge(a,B1)+2*wedge(B1,d)+8*wedge(d,B2)
others=[wedge(d,g),wedge(d,g-8*(-a+b)),wedge(d,g-8*b),wedge(d,g)]
vtotal=vc+sum(others,S.zeros(6,1))
xi=S.Matrix([[1,0,0,0,0,-4]])
assert list(vc)==[-16,0,6,8,0,2]
assert list(vtotal)==[-16,-8,6,24,0,6]
assert (xi*vtotal)[0]==-40
R=S.Matrix.hstack(*(exterior(A)-S.eye(6) for A in As))
assert xi*R==S.zeros(1,30)
ordinary=wedge(d,g)
M=R.row_join(ordinary)
D,U,V,rank=smith(M)
assert rank==6
uv=U*vtotal
y=S.zeros(M.cols,1)
for i in range(rank):
    assert uv[i]%D[i,i]==0
    y[i]=uv[i]/D[i,i]
solution=V*y
assert M*solution==vtotal and solution[-1]==10
kernel=V[:,rank:]
assert M*kernel==S.zeros(6,kernel.cols)

print('WEDGE_ORDER',pairs)
print('CUSP_PREIMAGE',list(vc))
for i,x in enumerate(others,1):print('RANK_ONE_PREIMAGE',i,list(x))
print('TOTAL_PREIMAGE',list(vtotal),'XI_VALUE',(xi*vtotal)[0])
print('RELATION_MATRIX',M.tolist())
print('SMITH_DIAGONAL',[D[i,i] for i in range(6)])
print('CRITICAL_BOUNDING_COEFFICIENTS',list(solution))
print('U',U.tolist(),'U_INVERSE',U.inv().tolist())
records=[]
for name,sign0,sign1 in [('I8_ONLY',1,0),('I1_ONLY',0,1),('PATH_DIFFERENCE',1,-1),('PATH_SUM',1,1)]:
    f=S.zeros(1,M.cols);f[0,4]=sign0;f[0,10]=sign1
    values=f*kernel
    witness=next((j for j,x in enumerate(values) if x%2),None)
    print('CANDIDATE',name,'CRITICAL_VALUE',(f*solution)[0],
          'KERNEL_MOD2',[int(x)%2 for x in values],
          'DESCENDS_MOD2',witness is None)
    record=dict(name=name,critical=int((f*solution)[0]),kernel_mod2=[int(x)%2 for x in values])
    if witness is not None:
        z=kernel[:,witness]
        assert M*z==S.zeros(6,1)
        print('NON_DESCENT_WITNESS',name,list(z),'VALUE',(f*z)[0])
        record['witness']=list(z)
    records.append(record)

R0=exterior(As[0])-S.eye(6)
assert all(x%2==0 for x in R0)
short=wedge(a,d)
bezout=S.zeros(6,1);bezout[0]=1;bezout[3]=1
assert R0*bezout==2*short
print('BOUNDARY_SHORT_TORUS',[int(x) for x in short],
      'TWICE_BOUNDING_PRISM',[int(x) for x in bezout],
      'MOD2_DETECTOR',[0,1,0,0,0,0])

out=root/'agents/continuation7_iii_weighted_os45_graph/S6_SERIES_PUBLISH_III_02LV_graph_link_v001.json'
assert not out.exists()
out.write_text(json.dumps(dict(M=M.tolist(),D=D.tolist(),U=U.tolist(),V=V.tolist(),
    solution=list(solution),kernel=kernel.tolist(),cusp=list(vc),others=[list(x) for x in others],
    total=list(vtotal),candidates=records),default=int,indent=2)+'\n')
print('DATA',str(out),'SHA256',sha256(out.read_bytes()).hexdigest())
print('END',datetime.now(timezone.utc).isoformat())
