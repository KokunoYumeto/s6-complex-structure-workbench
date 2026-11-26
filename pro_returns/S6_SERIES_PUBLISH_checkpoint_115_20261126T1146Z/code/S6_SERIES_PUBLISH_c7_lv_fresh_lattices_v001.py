#!/usr/bin/env python3
"""Fresh LV marked lattices, using only the admitted LN definitions/fixture.

The target proof and its historical calculations remain closed.  The
printed matrices specify the two-way Smith maps; no table is inferred
from an invariant-factor list alone.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
dependency = ROOT/'code/S6_SERIES_PUBLISH_c7_ln_integral_gluing_v001.py'
assert sha256(dependency.read_bytes()).hexdigest() == '9639dd5997dd9868224ca1ac308d286642f008f975fc6911af7fd52583413f26'
source = dependency.read_text().split("print('LN INTEGRAL GLUING v001:", 1)[0]
ns = {'__file__': str(dependency), '__name__': 'admitted_ln_definitions'}
exec(compile(source, str(dependency), 'exec'), ns)
E4, E6 = sp.eye(4), sp.eye(6)
integer, smith, kernel = (ns[n] for n in ('integer', 'smith', 'kernel'))
wedge, wedge_matrix = (ns[n] for n in ('wedge', 'wedge_matrix'))
row = next(r for r in ns['ROWS'] if (r['OS'],r['profile']) == (45,'default'))
caps = ns['make_local'](row, 2, 8, {0:2}, 'exception')
caps.append(ns['regular_log'](1,[0,0,0,-1],'ordinary'))
As = [c['A'] for c in caps]
n = len(As)
product = E4
for A in As:
    product *= A
assert product == E4
Dgraph = sp.Matrix.hstack(*(A-E4 for A in As[:-1]))
K, Kread = kernel(Dgraph)
suffix = []
for i in range(n-1):
    P = E4
    for A in As[i+1:]:
        P *= A
    suffix.append(P)
Js = []
for i in range(n):
    Q = sp.zeros(4*(n-1),4)
    if i < n-1:
        Q[4*i:4*i+4,:] = E4
    else:
        for j in range(n-1):
            Q[4*j:4*j+4,:] = -suffix[j]
    assert Dgraph*Q == As[i]-E4
    Js.append(Q)
fs = [ns['quadratic_correction'](A) for A in As]
def cv(i,x):
    if i < n-1:
        return fs[i](x)
    return -sum((fs[j](suffix[j]*x) for j in range(n-1)),sp.zeros(6,1))
def col(i,f,x):
    g = Js[i]*x
    assert Dgraph*g == sp.zeros(4,1)
    assert K*Kread*g == g
    return f.col_join(Kread*g)
columns = []
groups = []
for i,A in enumerate(As):
    R = wedge_matrix(A)-E6
    columns.extend(R[:,j].col_join(sp.zeros(K.cols,1)) for j in range(6))
    groups.extend([f'return_{i}_{j}' for j in range(6)])
H1columns = [(A-E4)[:,j].col_join(sp.zeros(n,1)) for A in As for j in range(4)]
H1columns.append(sp.zeros(4,1).col_join(sp.ones(n,1)))
capblocks = []
for i,c in enumerate(caps):
    local = []
    if c['cap'] == 'log':
        v = c['v']
        assert c['m'] == 1 and c['A'] == E4
        local = [col(i,cv(i,E4[:,j])-wedge(E4[:,j],v),E4[:,j]) for j in range(4)]
        local.append(col(i,cv(i,v),v))
        z = (-v).col_join(sp.zeros(n,1)); z[4+i] = 1
        H1columns.append(z)
    else:
        F,fixed,killed,h4,s = ns['cap_data'](c)
        local = [F[:,j].col_join(sp.zeros(K.cols,1)) for j in range(F.cols)]
        local += [col(i,cv(i,fixed[:,j]),fixed[:,j]) for j in range(fixed.cols)]
        if i:
            H1columns.extend(killed[:,j].col_join(sp.zeros(n,1)) for j in range(killed.cols))
            z = sp.zeros(4+n,1); z[4+i] = 1; H1columns.append(z)
    capblocks.append(sp.Matrix.hstack(*local))
    if i:
        columns.extend(local)
        groups.extend([f'cap_{i}_{j}' for j in range(len(local))])
MW = sp.Matrix.hstack(*columns)
MX = MW.row_join(capblocks[0])
H1W = sp.Matrix.hstack(*H1columns)

def certificate(M):
    D,U,V,Ui,Vi,r = smith(M)
    assert U*M*V == D
    return dict(shape=list(M.shape),rank=r,diagonal=[int(D[i,i]) for i in range(r)],
                M=M.tolist(),U=U.tolist(),Ui=Ui.tolist(),V=V.tolist(),Vi=Vi.tolist())

print('START',datetime.now(timezone.utc).isoformat(),flush=True)
print('RAW_PROFILE',json.dumps(row,separators=(',',':')),flush=True)
for i,A in enumerate(As):
    print('MONODROMY',i,A.tolist(),flush=True)
invariant_matrix = sp.Matrix.vstack(*[(wedge_matrix(A)-E6).T for A in As])
inv,invread = kernel(invariant_matrix)
print('INTEGRAL_INVARIANT_FORMS',inv.tolist(),'READER',invread.tolist(),flush=True)
print('DGRAPH',Dgraph.tolist(),flush=True)
print('GRAPH_K',K.tolist(),'READER',Kread.tolist(),flush=True)
for name,M in [('H1_EXTERIOR',H1W),('H2_EXTERIOR',MW),('H2_FILLED_QUOTIENT',MX)]:
    D,U,V,Ui,Vi,r = smith(M)
    print(name,'SHAPE',list(M.shape),'RANK',r,'DIAGONAL',[int(D[i,i]) for i in range(r)],flush=True)
    print(name,'U',U.tolist(),'UI',Ui.tolist(),flush=True)
    for j in range(r,M.rows):
        print(name,'FREE_ROW',j,list(U[j,:]),'INVERSE',list(Ui[:,j]),flush=True)
    for j in range(r):
        if abs(D[j,j]) > 1:
            print(name,'TORSION_ROW',j,int(D[j,j]),list(U[j,:]),'INVERSE',list(Ui[:,j]),
                  'BOUNDING',list(V[:,j]),flush=True)
    if name == 'H1_EXTERIOR':
        for r0,s0 in [(0,0),(1,0),(0,1)]:
            z = sp.zeros(4+n,1); z[0]=r0; z[2]=s0; z[4]=1
            print('CUSP_NORMAL',r0,s0,list(U*z),flush=True)
print('FULL_LN_RUN',ns['run'](caps),flush=True)
C = sp.Matrix([[8,24],[-6,-16]])
T = sp.Matrix([[1,3],[-3,-8]])
assert C == sp.diag(8,2)*T and T.det()==1
print('PERIOD_C',C.tolist(),'RIGHT_MAP',T.tolist(),'RIGHT_INVERSE',T.inv().tolist(),flush=True)
data = dict(profile=row,monodromies=[A.tolist() for A in As],Dgraph=Dgraph.tolist(),
            graph=K.tolist(),graph_reader=Kread.tolist(),H1W=certificate(H1W),
            H2W=certificate(MW),H2quotient=certificate(MX),column_labels=groups,
            capblocks=[B.tolist() for B in capblocks])
out=ROOT/'agents/continuation7_iii_weighted_os45_fresh/S6_SERIES_PUBLISH_III_02LV_fresh_lattices_v001.json'
out.parent.mkdir(exist_ok=True)
assert not out.exists()
out.write_text(json.dumps(data,default=int,indent=2)+'\n')
print('DATA',out,'SHA256',sha256(out.read_bytes()).hexdigest(),flush=True)
print('END',datetime.now(timezone.utc).isoformat(),flush=True)
