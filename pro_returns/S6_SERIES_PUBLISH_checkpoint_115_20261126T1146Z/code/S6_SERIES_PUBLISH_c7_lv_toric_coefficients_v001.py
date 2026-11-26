#!/usr/bin/env python3
"""Fresh LV toric and finite-coefficient calculation, with all coordinates.

Only the newly derived literal lattice data is read. The target original
and its historical auxiliaries remain closed. Missing cubic entries in
the printed sparse table mean exactly zero; its index set is all680
weakly increasing triples in the fifteen displayed primitive variables.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from itertools import combinations_with_replacement
from collections import Counter
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'agents/continuation7_iii_weighted_os45_fresh/S6_SERIES_PUBLISH_III_02LV_fresh_lattices_v001.json'
assert sha256(path.read_bytes()).hexdigest()=='09fafbdee1170304a81f481c71de0f88360d617b2db3ff16b5dd82c67f2014e6'
data=json.loads(path.read_text())
U=S.Matrix(data['H2quotient']['U']);M=S.Matrix(data['H2quotient']['M'])
reader=S.Matrix(data['graph_reader'])
u=U[22,:]
assert all(x%8==0 for x in u*M) and u[0]==1
linear=u[:,6:]*reader
assert list(linear[:,:4])==[0,388,0,1164]

rays=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
vertices=[(r,s) for r in range(8) for s in range(2)]
def add(v,w): return (v[0]+w[0],v[1]+w[1])
def index(v): return 2*(v[0]%8)+(v[1]%2)
def phi(v):
    r,s=v
    return 4*(r//8)+3*(s//2)*(r%8)
def degree(v,j):
    return phi(v)+phi(add(v,rays[j]))-phi(add(v,rays[(j-1)%6]))-phi(add(v,rays[(j+1)%6]))
def pair(x,y):return x[0]*y[0]-sum(x[i]*y[i] for i in range(1,4))
curves=[(1,-1,0,-1),(0,1,0,0),(1,-1,-1,0),(0,0,1,0),(1,0,-1,-1),(0,0,0,1)]
K=(-3,1,1,1);f=(1,0,-1,0)
etas=[];degrees=[];fixed=[]
for r,s in vertices:
    eps=4 if r==0 else -4 if r==7 else 0
    eta=(3*r+eps,-eps,-3*r,3) if s==0 else (3-3*r+eps,-3-eps,3*r-3,0)
    deg=[pair(eta,c) for c in curves]
    assert all((deg[j]-degree((r,s),j))%8==0 for j in range(6))
    assert pair(eta,eta)%16==(7 if r<7 else 15)
    assert pair(eta,f)==eps
    assert deg[1]==(eps if s==0 else 3+eps)
    etas.append(eta);degrees.append(deg)
    fixed.append(dict(r=r,s=s,d=deg[1],lam=0 if s==0 else -3*r,w=1 if s==0 else 0))
    for b,g in [(1,0),(0,1),(-8,3),(-3,1)]:
        Cstep=(8*b+24*g,-6*b-16*g)
        assert (phi(add((r,s),Cstep))-phi((r,s))+r*b-4*b-4*g)%8==0

edges=Counter();triangles=Counter()
for v in vertices:
    i=index(v)
    for d in rays[:3]:
        edges[tuple(sorted((i,index(add(v,d)))))]+=1
    a=index(v);b=index(add(v,(1,0)));c=index(add(v,(0,1)));d=index(add(v,(1,1)))
    triangles[tuple(sorted((a,b,c)))]+=1
    triangles[tuple(sorted((b,c,d)))]+=1
assert sum(edges.values())==48 and sum(triangles.values())==32
def cubic(i,j,k):
    a,b,c=sorted((i,j,k))
    if a==c:return 6
    if a==b:return -edges[a,c]
    if b==c:return -edges[a,b]
    return triangles[a,b,c]
for i in range(16):
    for j in range(16):
        assert sum(cubic(i,j,k) for k in range(16))==0

E=S.eye(16)
basis=[E[:,i]-E[:,14 if i%2==0 else 15] for i in range(14)]
basis.append(2*E[:,15]-2*E[:,14]);basis=S.Matrix.hstack(*basis)
dual=S.eye(16)[:14,:].col_join(S.Matrix([[S.Rational(i%2,2) for i in range(16)]]))
assert dual*basis==S.eye(15)
assert S.ones(1,16)*basis==S.zeros(1,15)
assert all(x%2==0 for x in S.Matrix([[i%2 for i in range(16)]])*basis)
forms=[{i:S.Integer(1)} for i in range(14)]+[{i:S.Rational(1,2) for i in range(1,16,2)}]
ctable=[]
for i,j,k in combinations_with_replacement(range(15),3):
    val=sum(x*y*z*cubic(a,b,c) for a,x in forms[i].items() for b,y in forms[j].items() for c,z in forms[k].items())
    assert val.q==1
    if j==k==14:assert val==0
    if val:ctable.append([i,j,k,int(val)])
assert len(list(combinations_with_replacement(range(15),3)))==680

mixed=S.zeros(16)
for i,v in enumerate(vertices):
    mixed[i,i]=pair(etas[i],K)
    for j,d in enumerate(rays):
        q=index(add(v,d))
        assert (degrees[i][j]-degrees[q][(j+3)%6])%8==0
        mixed[i,q]+=degrees[i][j]
assert all((mixed[i,j]-mixed[j,i])%8==0 for i in range(16) for j in range(16))
assert all(x%8==0 for x in mixed*S.ones(16,1))
prim=S.zeros(15)
prim[:14,:14]=mixed[:14,:14]
for i,(r,s) in enumerate(vertices[:14]):
    eps=4 if r==0 else -4 if r==7 else 0
    prim[i,14]=prim[14,i]=(-1)**s*eps
prim=prim.applyfunc(lambda x:int(x)%8)
assert prim[14,14]==0
quadratic=[pair(eta,eta)%16 for eta in etas]
assert sum(quadratic)%16==0 and sum(quadratic[1::2])%16==0
assert sum(sum(d) for d in degrees)==48
assert sum(x['d'] for x in fixed)==24
assert sum(x['d']*x['lam'] for x in fixed)==-168
assert sum(x['d']*x['lam']**2 for x in fixed)==2016
for h in range(16):
    for j in range(16):
        uy2=-sum(x['d']*(x['w']+j)**2 for x in fixed)
        puy=-2*sum(x['d']*(x['lam']+h)*(x['w']+j) for x in fixed)
        u3=-3*sum(x['d']*(x['lam']+h)**2 for x in fixed)
        assert uy2%8==puy%16==u3%8==0

print('START',datetime.now(timezone.utc).isoformat())
print('CYCLIC_FIBRE_ROW',list(u[:,:6]),'ALL_GRAPH_LINEAR_ROWS',linear.tolist())
print('RELATIVE_BASIS',basis.tolist(),'DUAL',[[str(x) for x in dual.row(i)] for i in range(15)])
for i,v in enumerate(vertices):
    print('COMPONENT',i,list(v),'ETA',list(etas[i]),'SIX_DEGREES',degrees[i],
          'SQUARE',pair(etas[i],etas[i]),'P2_MOD16',quadratic[i],'UYD_MOD8',((-1)**v[1]*pair(etas[i],f))%8)
print('EDGES_WITH_MULTIPLICITY',[[*key,val] for key,val in sorted(edges.items())])
print('TRIANGLES_WITH_MULTIPLICITY',[[*key,val] for key,val in sorted(triangles.items())])
print('ALL680_CUBIC_COORDINATES_NONZERO_OTHERS_ZERO',ctable)
for i in range(15):print('ALL120_MIXED_SYMMETRIC_ROW',i,list(prim.row(i)))
for record in fixed:print('FIXED_CURVE',record)
print('P2_COORDINATES_MOD16',[7]*14+[0],'PURE_CUBE_MOD8',0)
print('LOCALIZATION_SUMS',24,-168,2016,'UY2_MOD8',0,'P2UY_MOD16',0,'U3_MOD8',0)
print('COMPLETE full period/wall maps,48 edges,32 triangles,680 cubics,120 mixed coordinates,15 full quadratic coordinates; all256 common-character pairs checked.')
out=ROOT/'agents/continuation7_iii_weighted_os45_fresh/S6_SERIES_PUBLISH_III_02LV_toric_coefficients_v001.json'
assert not out.exists()
out.write_text(json.dumps(dict(etas=etas,degrees=degrees,cubic_nonzero=ctable,mixed=prim.tolist(),quadratic=[7]*14+[0],pure=0,fixed=fixed),default=int,indent=2)+'\n')
print('DATA',out,'SHA256',sha256(out.read_bytes()).hexdigest())
print('END',datetime.now(timezone.utc).isoformat())
