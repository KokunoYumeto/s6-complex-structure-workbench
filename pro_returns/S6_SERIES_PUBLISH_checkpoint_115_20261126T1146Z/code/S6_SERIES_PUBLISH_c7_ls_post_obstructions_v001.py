"""Check the literal historical obstruction integers at their exact Smith scope.

The previous new solver proved every existence assertion independently.
This bounded supplement verifies the recorded numerical obstruction fields
using precisely the disclosed generic DomainMatrix Smith convention.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as S
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

W=Path(__file__).resolve().parents[1]
LANE=W/'agents/continuation7_iii_vertical_correction_receiving'
old=json.loads((LANE/'S6_SERIES_PUBLISH_root_vertical_corrections.json').read_text())
geometry={}
for line in (W/'code/S6_SERIES_PUBLISH_c7_ls_post_local_v001.out').read_text().splitlines():
    if line.startswith('GEOMETRY='):
        row=json.loads(line.split('=',1)[1]);geometry[row['kind']]=row
def matrix(data):
    A=S.zeros(*data['shape'])
    for i,j,x in data['entries']:A[i,j]=x
    return A
def sparse(A):
    return dict(shape=list(A.shape),entries=[[i,j,int(A[i,j])] for i in range(A.rows) for j in range(A.cols) if A[i,j]])
print('START',datetime.now(timezone.utc).isoformat(),flush=True)
count=0
for row in old['local_component_pair_cases']:
    if row['p']==0:assert row['exists'] and not any(row['vertical_coefficients'])
    if row['exists']:continue
    geo=geometry[row['kind']];C,T=matrix(geo['C']),matrix(geo['T']);n=C.rows
    c=S.eye(n)[:,geo['labels'][row['p']]]-S.eye(n)[:,0];delta=T**row['q']-S.eye(n)
    A=delta*C;rhs=-delta*c
    D,U,V=smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(S.ZZ));D,U,V=[x.to_Matrix() for x in (D,U,V)]
    assert U*A*V==D and abs(U.det())==abs(V.det())==1
    rank=sum(bool(D[i,i]) for i in range(n));r=U*rhs
    obstruction=[dict(row=j,diagonal=int(D[j,j]),transformed_rhs=int(r[j])) for j in range(rank) if r[j]%D[j,j]]
    obstruction += [dict(row=j,diagonal=0,transformed_rhs=int(r[j])) for j in range(rank,n) if r[j]]
    assert obstruction==row['integer_smith_obstruction'];count+=1
    print('LITERAL_OBSTRUCTION='+json.dumps(dict(kind=row['kind'],p=row['p'],q=row['q'],D=sparse(D),U=sparse(U),V=sparse(V),U_inverse=sparse(U.inv()),V_inverse=sparse(V.inv()),rhs=list(map(int,rhs)),transformed_rhs=list(map(int,r)),obstruction=obstruction),separators=(',',':')),flush=True)
print('PASS literal historical obstruction fields',count,'and all p=0 selector vectors are zero.',flush=True)
print('COMPLETE',datetime.now(timezone.utc).isoformat(),flush=True)
