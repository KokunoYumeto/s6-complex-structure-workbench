"""Post-exposure LS auxiliary verification from exact affine root lattices.

No historical program is executed.  The historical local/global JSON is
checked in every field against explicit matrices and the raw fixture.
The integer Smith routine is this lane's already read fresh routine.
"""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from math import gcd, lcm
import ast
import json
import sympy as S

W=Path(__file__).resolve().parents[1]
LANE=W/'agents/continuation7_iii_vertical_correction_receiving'
source=W/'code/S6_SERIES_PUBLISH_c7_ls_os45_bar_v001.py'
selected={'ints','sparse','bezout','smith','solve_from_factor','factor_record'}
tree=ast.parse(source.read_text())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in selected],type_ignores=[]),str(source),'exec'))
raw=json.loads((W/'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json').read_text())['rows']
old=json.loads((LANE/'S6_SERIES_PUBLISH_root_vertical_corrections.json').read_text())

def emit(label,obj):
    print(label+'='+json.dumps(obj,separators=(',',':')),flush=True)

def geometry(kind):
    if kind in ('I1','II'):
        return S.zeros(1),S.eye(1),[0],S.Matrix([1])
    if kind in ('III','IV') or (kind.startswith('I') and kind[1:].isdigit()):
        n={'III':2,'IV':3}.get(kind,int(kind[1:]) if kind[1:].isdigit() else 0)
        C=S.zeros(n)
        for i in range(n):
            C[i,i]-=2;C[i,(i-1)%n]+=1;C[i,(i+1)%n]+=1
        perm=[(i+1)%n for i in range(n)];labels=list(range(n));mu=S.ones(n,1)
    elif kind=='IV*':
        C=-2*S.eye(7);mu=S.Matrix([1,1,1,2,2,2,3])
        perm=[1,2,0,4,5,3,6];labels=[0,1,2]
        for i,j in [(0,3),(1,4),(2,5),(3,6),(4,6),(5,6)]:C[i,j]=C[j,i]=1
    elif kind=='III*':
        C=-2*S.eye(8);mu=S.Matrix([1,1,2,2,3,3,4,2])
        perm=[1,0,3,2,5,4,6,7];labels=[0,1]
        chain=[0,2,4,6,5,3,1]
        for i,j in list(zip(chain,chain[1:]))+[(6,7)]:C[i,j]=C[j,i]=1
    else:
        assert kind in ('I1*','I3*')
        n=int(kind[1:-1]);C=-2*S.eye(n+5);mu=S.Matrix([1]*4+[2]*(n+1))
        perm=[2,3,1,0]+[n+8-j for j in range(4,n+5)];labels=[0,2,1,3]
        for i,j in [(0,4),(1,4),(2,n+4),(3,n+4)]+[(i,i+1) for i in range(4,n+4)]:C[i,j]=C[j,i]=1
    T=S.zeros(C.rows)
    for j,i in enumerate(perm):T[i,j]=1
    assert C*mu==S.zeros(C.rows,1) and T*mu==mu and C*T==T*C
    assert C.rank()==C.rows-1 and T**len(labels)==S.eye(C.rows)
    return C,T,labels,mu

print('START',datetime.now(timezone.utc).isoformat(),flush=True)
print('HISTORICAL_INPUT_SHA256',sha256((LANE/'S6_SERIES_PUBLISH_root_vertical_corrections.json').read_bytes()).hexdigest(),flush=True)
kinds=sorted({kind for row in raw for kind in row['fibers']})
geos={kind:geometry(kind) for kind in kinds}
local={};certificates=[]
for kind,(C,T,labels,mu) in geos.items():
    emit('GEOMETRY',dict(kind=kind,C=sparse(C),T=sparse(T),T_inverse=sparse(T.T),labels=labels,mu=list(map(int,mu))))
    for q in range(len(labels)):
        delta=T**q-S.eye(C.rows);A=delta*C;fact=smith(A)
        D,U,V,Ui,Vi,ds=fact
        orbits=[];seen=set();Tq=T**q
        for start in range(C.rows):
            if start in seen:continue
            orbit=[];i=start
            while i not in seen:
                seen.add(i);orbit.append(i);i=next(j for j in range(C.rows) if Tq[j,i])
            orbits.append(orbit)
        O=S.Matrix([[int(i in orb) for orb in orbits] for i in range(C.rows)])
        P=S.Matrix([[int(i==orb[0]) for i in range(C.rows)] for orb in orbits])
        assert P*O==S.eye(len(orbits)) and A*O==S.zeros(C.rows,len(orbits))
        assert O*P*V[:,len(ds):]==V[:,len(ds):]
        emit('LOCAL_OPERATOR',dict(kind=kind,q=q,orbits=orbits,smith=factor_record(fact),orbit_basis=sparse(O),orbit_inverse=sparse(P)))
        for p in range(len(labels)):
            c=S.eye(C.rows)[:,labels[p]]-S.eye(C.rows)[:,labels[0]];rhs=-delta*c;ur=U*rhs
            ok=all(ur[i]%ds[i]==0 for i in range(len(ds))) and all(ur[i]==0 for i in range(len(ds),C.rows))
            assert ok==(p*q%len(labels)==0)
            local[kind,p,q]=ok
            cert=dict(kind=kind,p=p,q=q,exists=ok,rhs=list(map(int,rhs)),transformed_rhs=list(map(int,ur)))
            if ok:
                z=solve_from_factor(A,rhs,fact);m=c+C*z
                assert delta*m==S.zeros(C.rows,1) and (mu.T*m)[0]==0
                fq=S.zeros(C.rows,1)
                fq[1:,0]=C[1:,1:].inv()*(S.eye(C.rows)[:,labels[q]]-S.eye(C.rows)[:,0])[1:,0]
                assert C*fq==S.eye(C.rows)[:,labels[q]]-S.eye(C.rows)[:,0]
                assert (m.T*fq)[0]==0 and z[labels[q]]-z[0]==-fq[labels[p]]
                cert.update(d=list(map(int,z)),m=list(map(int,m)),height_inverse=list(map(str,fq)))
            certificates.append(cert)
            emit('LOCAL_RESULT',cert)

assert len(local)==227
assert len(old['local_component_pair_cases'])==227
for record in old['local_component_pair_cases']:
    kind,p,q=record['kind'],record['p'],record['q'];C,T,labels,mu=geos[kind]
    assert record['exists']==local[kind,p,q]
    c=S.eye(C.rows)[:,labels[p]]-S.eye(C.rows)[:,0];delta=T**q-S.eye(C.rows)
    if record['exists']:
        z=S.Matrix(record['vertical_coefficients']);m=S.Matrix(record['corrected_multidegree'])
        K=S.Matrix.hstack(*map(S.Matrix,record['all_correction_kernel_columns']))
        assert S.Matrix(record['initial_multidegree'])==c and m==c+C*z and delta*m==S.zeros(C.rows,1)
        kfact=smith(K);assert all(d==1 for d in kfact[-1])
        assert delta*K==S.zeros(C.rows,K.cols) and K.cols==C.rows-delta.rank()
    else:
        assert record['integer_smith_obstruction']
        assert all(o['diagonal']==0 and o['transformed_rhs'] or o['diagonal'] and o['transformed_rhs']%o['diagonal'] for o in record['integer_smith_obstruction'])
    emit('HISTORICAL_LOCAL_EXACT',record)

global_records=[];actual=[];initial=[]
for row in sorted(raw,key=lambda r:(r['OS'],r['profile'])):
    d0=int(S.Rational(row['height_of_generator']).q);orders=[]
    for i,(kind,cc,bb,gg) in enumerate(zip(row['fibers'],row['component_coordinates'],row['elliptic_matrices'],row['generator_section_cocycle'])):
        n=int(cc['moduli'][0]) if cc['moduli'] else 1;k=int(cc['rows'][0][0]) if cc['rows'] else 0
        assert gcd(n,k)==1;orders.append(n);B=S.Matrix(bb);g=S.Matrix(gg);fact=smith(B-S.eye(2));D,U,V,Ui,Vi,ds=fact;ug=U*g
        assert all(ug[j]==0 for j in range(len(ds),2))
        order=lcm(*(d//gcd(d,int(ug[j])) for j,d in enumerate(ds)))
        assert order==n
        pre=solve_from_factor(B-S.eye(2),n*g,fact)
        record=dict(OS=row['OS'],profile=row['profile'],site=i,kind=kind,recorded_order=n,raw_residue=k,B=bb,g=gg,smith=factor_record(fact),Ug=list(map(int,ug)),order=order,order_multiple_preimage=list(map(int,pre)))
        actual.append(record);emit('ACTUAL_COCYCLE',record)
    assert lcm(*orders)==d0
    valid=0;extra=[]
    for a in range(d0):
        for b in range(d0):
            values=[(kind,(a*(int(c['rows'][0][0]) if c['rows'] else 0))%n,(b*(int(c['rows'][0][0]) if c['rows'] else 0))%n) for kind,c,n in zip(row['fibers'],row['component_coordinates'],orders)]
            ok=all(local[v] for v in values);narrow=all(p==0 or q==0 for _,p,q in values)
            assert ok==(a*b%d0==0)
            valid+=ok
            if ok and not narrow:extra.append([a,b])
    for a in range(1,d0+1):
        if d0%a:continue
        b=d0//a
        if any(a*(int(c['rows'][0][0]) if c['rows'] else 0)%n and b*(int(c['rows'][0][0]) if c['rows'] else 0)%n for c,n in zip(row['component_coordinates'],orders)):
            initial.append(dict(OS=row['OS'],profile=row['profile'],a=a,b=b,height=1))
    record=dict(os_entry=row['OS'],profile=row['profile'],height_denominator=d0,component_group_orders=orders,generator_component_maps_are_units=True,component_order_lcm_equals_height_denominator=True,all_residue_pairs_checked=d0*d0,number_admitting_component_corrections=valid,new_pairs_beyond_narrowness_OR=extra,discrepancies_with_integral_height_criterion=[])
    global_records.append(record);emit('GLOBAL_EXACT',record)
assert global_records==old['global_profile_residue_cases']
assert old['integral_height_criterion_discrepancies']==[]
assert old['example_I4_P2_Q2']==next(r for r in old['local_component_pair_cases'] if (r['kind'],r['p'],r['q'])==('I4',2,2))
emit('HISTORICAL_SCOPE',old['scope'])
assert len(actual)==82 and sum(r['all_residue_pairs_checked'] for r in global_records)==5696 and len(initial)==16
emit('ADDITIONAL_HEIGHT_ONE',initial)
print('PASS 227 local pairs, 5696 global residues, 82 actual cocycles, 16 additional height-one initial pairs; every historical local/global JSON field checked.',flush=True)
out=LANE/'S6_SERIES_PUBLISH_III_02LS_post_local_data_v001.json'
out.write_text(json.dumps(dict(local=certificates,global_records=global_records,actual=actual,additional_height_one=initial),indent=2)+'\n')
print('DATA',out.relative_to(W),'SHA256',sha256(out.read_bytes()).hexdigest(),flush=True)
print('COMPLETE',datetime.now(timezone.utc).isoformat(),flush=True)
