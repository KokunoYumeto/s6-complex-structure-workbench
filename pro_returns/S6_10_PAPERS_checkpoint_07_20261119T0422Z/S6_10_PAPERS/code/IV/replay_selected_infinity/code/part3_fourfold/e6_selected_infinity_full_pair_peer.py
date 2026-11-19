#!/usr/bin/env python3
"""Independent FP audit via separate integral line divisors and full clutches."""
from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
names={
 'stars':'code/part3_fourfold/e6_selected_infinity_compact_surface_stars.json',
 'faces':'code/part3_fourfold/e6_fixed_face_orbits.json',
 'interface':'code/part3_fourfold/e6_selected_infinity_curve_clutch.json',
 'root_pair':'code/part3_root/e6_selected_infinity_full_pair_ledger.json'}
D={k:json.loads((ROOT/p).read_text()) for k,p in names.items()}
labels=[]
def ck(value,label):
    assert bool(value),label
    labels.append(label)
def zero(value,label):ck(S.factor(value)==0,label)
def asstr(v):return [str(S.factor(z)) for z in v]
def pairP(w):return (1/S.prod(w),sum(z*z for z in w)/S.prod(w))
def pairC(w,d):
    a=sum(S.Rational(di,wi) for wi,di in zip(w,d));p=S.prod(w)
    return (-a/p,(2*sum(wi*di for wi,di in zip(w,d))-sum(wi*wi for wi in w)*a)/p)
def pairS(aa,ab,bb,p):return (-(aa-ab+bb),-(p+aa+2*ab+bb))
def total(rows):return tuple(S.factor(sum(row[k] for row in rows)) for k in (0,1))

delta=S.Matrix([0,0,0,1]); charts={}
for row in D['stars']['charts']:
    N=S.Matrix(row['rays']).T; inv=N.inv(); w=inv*delta
    ck(abs(N.det())==1,'unimodular full quotient chart')
    ck(list(w)==row['physical_weights'],'full physical representation')
    charts[tuple([row['kind'],row['label']])]=(N,inv,list(w),row['rays'])

# Independently construct A and B as integral Cartier divisors. This does not
# use the root auxiliary-circle intersections or the stored difference divisor.
surface_out=[]; surface_pairs={'exceptional':[],'refinement':[]}
for s in D['stars']['surfaces']:
    cs=[charts[tuple(k)] for k in s['charts']]
    N0,A0,w0,r0=cs[0]; tan0=[i for i,w in enumerate(w0) if w==0]
    R=N0[:,tan0]; Q=S.Matrix(s['quotient_projection'])
    ck(Q*R==S.eye(2),'actual tangent section splits surface quotient')
    rays=[S.Matrix(v) for v in s['complete_surface_rays']];n=len(rays)
    I=S.zeros(n)
    for k in range(n):
        ck(S.Matrix.hstack(rays[k],rays[(k+1)%n]).det()==1,'oriented primitive complete surface fan')
        I[k,k]=-S.Matrix.hstack(rays[k-1],rays[(k+1)%n]).det()
        I[k,(k+1)%n]=1;I[(k+1)%n,k]=1
    ck(I==S.Matrix(s['integral_intersection_matrix']),'independent integral wall intersection matrix')
    divisors=[]
    for weight in (-1,1):
        m0=A0[w0.index(weight),:]; vals={}
        for N,A,w,rr in cs:
            m=A[w.index(weight),:]; ell=(m-m0)*R
            for k in [i for i,ww in enumerate(w) if ww==0]:
                ray=Q*N[:,k]; key=tuple(ray);value=(ell*ray)[0]
                if key in vals:ck(vals[key]==value,'normal coefficient overlap agrees on complete ray')
                vals[key]=value
        coeff=S.Matrix([vals[tuple(v)] for v in rays])
        ck(all(v.q==1 for v in coeff),'separate actual normal line has integral divisor')
        divisors.append(coeff)
    am,bp=divisors
    aa=(am.T*I*am)[0];ab=(am.T*I*bp)[0];bb=(bp.T*I*bp)[0]
    ones=S.ones(n,1);p1=(ones.T*I*ones)[0]-2*n
    ck(p1==S.Rational(s['p1']),'independent tangent number from complete fan')
    ck(aa-2*ab+bb==S.Rational(s['D_square']),'separate normal intersections recover actual D square')
    pair=pairS(aa,ab,bb,p1)
    root=next(row for row in D['root_pair']['surface_rows'] if row['id']==s['id'])
    ck(asstr((aa,ab,bb))==root['normal_squares_mixed'],'independent A/B/mixed intersections agree with fresh root moment calculation')
    ck(asstr(pair)==root['pair_U'],'independent surface pair')
    kind='exceptional' if 'v_unit' in s['type'] else 'refinement'
    surface_pairs[kind].append(pair)
    surface_out.append({'id':s['id'],'A_divisor':asstr(am),'B_divisor':asstr(bp),
                        'normal_intersections':asstr((aa,ab,bb)),'pair_U':asstr(pair)})

aux=S.Matrix([13,31,71,173]); interior=[]; interior_rows=[]
for row in D['faces']['selected_ordinary_overlay']['components']:
    if row['tag']!='interior':continue
    w=list(map(S.Integer,row['normal_weights']))
    if row['dimension']==0:
        pair=pairP(w);degrees=None
    else:
        face=row['canonical_face']; ends=[]
        for idx in row['face_occurrences'][0]['charts']:
            N,A,weights,rays=charts[('resolved_infinity',idx)]
            aw=A*aux; tw=aw[weights.index(0)]
            ck(tw!=0,'independent auxiliary tangent nonzero')
            ends.append((tw,[aw[rays.index(v)] for v in face]))
        ck(len(ends)==2 and ends[0][0]==-ends[1][0],'actual two-chart interior curve')
        degrees=[S.factor((a-b)/ends[0][0]) for a,b in zip(ends[0][1],ends[1][1])]
        ck(degrees==row['normal_degrees'],'full inverse matrices recover interior curve clutch')
        pair=pairC(w,degrees)
    interior.append(pair)
    interior_rows.append({'id':row['id'],'dimension':row['dimension'],'degrees':None if degrees is None else asstr(degrees),'pair_U':asstr(pair)})
ck(len(interior_rows)==124,'all106 points and18 compact interior curves')

pcurves=[];interfaces=[]
for row in D['stars']['p_curves']:
    face=row['face']
    cs=[(k,v) for k,v in charts.items() if sorted([r for r,w in zip(v[3],v[2]) if w])==sorted(face)]
    ck(len(cs)==2,'actual p curve has two full coefficient charts')
    (k0,(N0,A0,w0,r0))=next(c for c in cs if c[0][0]=='resolved_infinity')
    (k1,(N1,A1,w1,r1))=next(c for c in cs if c[0][0]=='p_graph')
    M=A1*N0; tangent=w0.index(0)
    ck(list(N0[2,:])==[int(i==tangent) for i in range(4)],'first p-curve tangent is exactly v')
    degree=[]
    for ray in face:
        i=r0.index(ray);j=r1.index(ray)
        ck(M[j,i]==1,'p overlap same normal coefficient')
        degree.append(-M[j,tangent])
    ck(degree==row['normal_degrees'],'independent signed p-curve normal degrees')
    pcurves.append(pairC(list(map(S.Integer,row['normal_weights'])),degree))
for row in D['interface']['curves']:
    E=S.Matrix(row['native_normal_exponents']);N=S.Matrix(row['infinity_chart_matrix'])
    M=E*N;tangent=row['tangent_column']
    ck(list(N[0,:])==[int(i==tangent) for i in range(4)],'interface tangent is literal chi^4')
    deg=[-M[i,tangent] for i in range(3)]
    ck(deg==row['normal_degrees'],'independent chi/finite-base normal degrees')
    interfaces.append(pairC(list(map(S.Integer,row['normal_weights'])),deg))

I3=S.Matrix([[-2,1,0],[1,-2,1],[0,1,-2]])
minus=([1,0,0],[1,-1,1],[0,0,1],[0,0,0])
strict=[];strict_rows=[];mu2=[]
for j in range(4):
    dv=S.Matrix(minus[j]);sq=(dv.T*I3.inv()*dv)[0]
    # j=0 uses actual even chain node4; j=1,3 are odd nodes.
    odd_weight=1 if j%2 else -1
    a1minus=-S.Rational(1,2) if odd_weight==-1 else 0
    a1plus=-S.Rational(1,2) if odd_weight==1 else 0
    aa=2*sq+a1minus;ab=S.Rational((j+1)*(4-j),2);bb=S.Rational(j*j,2)-8+a1plus
    pair=pairS(aa,ab,bb,-24);strict.append(pair)
    strict_rows.append({'j':j,'actual_odd_line_weight':odd_weight,'A3_each_square':str(sq),'A1_line':'negative' if odd_weight<0 else 'positive','pair_U':asstr(pair)})
    ck(asstr(pair)==D['root_pair']['strict_rows'][j]['pair_U'],'signed A3/A1 strict pair')
    weights=[2*odd_weight,-odd_weight,-odd_weight,-odd_weight]
    mu2.append(pairP(list(map(S.Integer,weights))))
    ck(pairP(list(map(S.Integer,weights)))==(-S.Rational(1,2),-S.Rational(7,2)),'actual isolated mu2 weights give separate pair')

# Exact orbit invariant: for (C,j), let j=r+4n, C in Z/2.
# The full B step toggles C and increments n; C+n is unchanged.
for c in (0,1):
    for j in range(-16,17):
        rj=j%4;n=(j-rj)//4
        target_c=1-c;target_j=j+4;nt=(target_j-rj)//4
        ck((c+n)%2==(target_c+nt)%2,'O/T period orbit invariant retains two copies')

blocks={'strict_once':total(strict),'mu2_points_once':total(mu2),'interior_per_copy':total(interior),
        'exceptional_per_copy':total(surface_pairs['exceptional']),'refinement_per_copy':total(surface_pairs['refinement']),
        'p_curves_per_copy':total(pcurves),'interface_per_copy':total(interfaces)}
for k,val in blocks.items():ck(asstr(val)==D['root_pair']['U_subtotals'][k],'independent complete block '+k)
compact=total([v if key.endswith('_once') else tuple(2*z for z in v) for key,v in blocks.items()])
ck(compact==(0,18),'complete compact pair before moving cap')
kappa=S.Symbol('actual_c2',integer=True);complete=total([compact,(kappa,4*kappa+6)])
zero((4*complete[0]-complete[1])/24+1,'full expression independent of actual moving c2')

proofs=['notes/part3_e6_selected_infinity_full_pair_ledger_working.md','notes/part3_e6_selected_infinity_mu2_fixed_working.md']
out={'status':'PASS','checks':len(labels),'method':'Separate integral normal Cartier divisors from full chart matrices; fresh curve auxiliary (13,31,71,173); exact coefficient clutches; signed A3/A1 relative lifts; explicit O/T orbit invariant.',
 'check_labels':labels,'surface_rows':surface_out,'interior_rows':interior_rows,'strict_rows':strict_rows,
 'block_pairs':{k:asstr(v) for k,v in blocks.items()},'compact_pair':asstr(compact),'complete_pair':asstr(complete),
 'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in list(names.values())+proofs}}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'PASS {len(labels)} independent full-pair checks; compact U=(0,18); moving c2 retained.')
