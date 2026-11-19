#!/usr/bin/env python3
"""Actual H-unit normal degrees and compact H fixed-component residues.

Uses w=q2/q1 on the exceptional base P1, with marked points 0,1,infinity.
The exact q1-period units are w^(n1+b*n2) on Z and
w^(-a*n1-2*n2)(1-w)^(N*n2) on V.  All original-polydisc units
restrict to nonzero constants.  This retains the cap-independent H
transition data, rather than replacing three base charts by a toric P1.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from collections import defaultdict,Counter
import argparse,json,gc
from source_zero_interior_residues import residue_at_chart,as_json

ROOT=Path(__file__).resolve().parents[2]

def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
           -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
           +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def inverse3(B):
    D=det3(B)
    assert abs(D)==1
    A=[]
    for i in range(3):
        row=[]
        for j in range(3):
            m=[[B[r][c] for c in range(3) if c!=i]
                           for r in range(3) if r!=j]
            row.append(((-1)**(i+j)*(m[0][0]*m[1][1]-m[0][1]*m[1][0]))//D)
        A.append(row)
    assert all(sum(B[i][k]*A[k][j] for k in range(3))==int(i==j)
               for i in range(3) for j in range(3))
    return A

def log_open(path,material):
    with (ROOT/'records/literature_fourfold.md').open('a') as f:
        f.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened '
                +str(path.relative_to(ROOT))+'. Reason: actual H-base normal '
                'transition and characteristic calculation. Material: '
                +material+'; no global source return assigned.\n')

def surface_poly(w,x,p1):
    u,v=map(Q,w);x,y=map(Q,x)
    c=4-u*u-v*v
    A=x/u+y/v
    B=x*x/(u*u)+x*y/(u*v)+y*y/(v*v)
    return (c*B+2*(u*x+v*y)*A-(p1+x*x+y*y))/(24*u*v)

def surface_curve_term(w,beta,degrees,eta,dt):
    # A quadratic polynomial's exact first-order coefficient on h^2=0.
    R0=surface_poly(w,beta,Q(eta*eta))
    plus=surface_poly(w,[beta[i]+degrees[i] for i in range(2)],
                      Q(eta*eta+2*eta*dt))
    minus=surface_poly(w,[beta[i]-degrees[i] for i in range(2)],
                       Q(eta*eta-2*eta*dt))
    Rh=(plus-minus)/2
    return Rh/eta-R0*dt/(eta*eta)

def do_case(a,b,N):
    fanpath=ROOT/'code/part3'/f'source_zero_regular_fan_{a}_{b}_{N}.json'
    log_open(fanpath,'common-H rank-three faces, actual periods and permutations')
    fan=json.loads(fanpath.read_text())
    hfaces=[f for f in fan['face_orbits']
             if f['dimension']==3 and f['boundary_tag']=='H']
    del fan
    gc.collect()
    chartpath=ROOT/'code/part3_fourfold'/f'source_zero_fixed_charts_{a}_{b}_{N}.json'
    log_open(chartpath,'ordered dual characters and physical fixed-component IDs')
    d=json.loads(chartpath.read_text())
    charts={c['id']:c for c in d['charts']}
    components={c['id']:c for c in d['components']}
    hcomp={k:c for k,c in components.items() if c['boundary_tag']=='H'}
    hrows=[]
    checks=0
    for f in hfaces:
        vec=f['canonical_vectors']
        assert all(v[2]==0 for v in vec)
        B=[[vec[j][i] for j in range(3)] for i in (0,1,3)]
        A=inverse3(B)
        degrees=[0]*3
        contributions=[]
        sectors=[]
        cid=None
        for occ in f['occurrences']:
            c=charts[occ['cone']]
            sectors.append(c['sector'])
            if cid is None: cid=c['component']
            assert cid==c['component']
            assert cid in hcomp
            n1,n2=occ['period_from_canonical']
            hn=[2*n1+b*n2,-a*n1+(N-1)*n2]
            ds=[None]*3
            for k,i in enumerate(occ['local_columns']):
                j=occ['vertex_permutation_to_canonical'][k]
                p,q,r,s=c['dual_character_rows'][i]
                assert [p,q]==A[j][:2]
                assert s+p*hn[0]+q*hn[1]==A[j][2]
                aw=p*(n1+b*n2)+q*(-a*n1-2*n2)
                ao=N*n2*q
                if c['sector']=='W':
                    degree=aw+r
                elif c['sector']=='E':
                    degree=ao+r
                else:
                    assert c['sector']=='I'
                    degree=-aw+r-s-ao
                degrees[j]+=degree
                ds[j]=degree
                checks+=3
            contributions.append({'sector':c['sector'],'cone':c['id'],
                                  'period':[n1,n2],
                                  'orders_at_marked_point':ds})
        assert sorted(sectors)==['E','I','W'],(f['id'],sectors)
        hrows.append({'id':f['id'],'component':cid,'normal_dual_rows':A,
                      'normal_degrees':degrees,
                      'physical_weights':[row[1] for row in A],
                      'marked_point_orders':contributions})
        checks+=4
    bycomp=defaultdict(list)
    for row in hrows: bycomp[row['component']].append(row)
    aux=[]
    K=2
    while len(aux)<2:
        good=True
        for cid,c in hcomp.items():
            if c['complex_dimension']==1: continue
            for h in bycomp[cid]:
                w=h['physical_weights']
                zero=[i for i,v in enumerate(w) if not v]
                assert len(zero)==1
                i=zero[0]
                p,q,_=h['normal_dual_rows'][i]
                if p+K*q==0: good=False
            for name in c['charts']:
                ch=charts[name]
                bt=[ch['dual_character_rows'][i][0]+K*ch['dual_character_rows'][i][1]
                    for i in ch['zero_weight_columns']]
                # Two zero tangent weights would make the auxiliary circle trivial
                # on the surface; one is precisely a common-H fixed-curve chart.
                if all(x==0 for x in bt): good=False
        if good: aux.append(K)
        K+=1
        assert K<1000
    vals=[]
    topologies=[]
    for K in aux:
        sums={}
        topo={}
        for cid,c in hcomp.items():
            value=Q(0)
            if c['complex_dimension']==1:
                assert len(bycomp[cid])==1
                h=bycomp[cid][0]
                w=list(map(Q,h['physical_weights']))
                deg=h['normal_degrees']
                assert all(w)
                c0=4-sum(z*z for z in w)
                from math import prod
                value=-sum((c0/z+2*z)*r for z,r in zip(w,deg))/(24*prod(w))
            else:
                assert c['complex_dimension']==2
                euler=0
                c1square=Q(0)
                fixed_point_count=0
                for name in c['charts']:
                    ch=charts[name]
                    beta=[r[0]+K*r[1] for r in ch['dual_character_rows']]
                    bt=[beta[i] for i in ch['zero_weight_columns']]
                    if all(bt):
                        value+=residue_at_chart(ch['physical_weights'],beta)
                        euler+=1
                        fixed_point_count+=1
                        c1square+=Q(sum(bt)**2,bt[0]*bt[1])
                    else:
                        assert bt.count(0)==1
                for h in bycomp[cid]:
                    w=h['physical_weights']
                    beta=[r[0]+K*r[1] for r in h['normal_dual_rows']]
                    deg=h['normal_degrees']
                    nz=[i for i,v in enumerate(w) if v]
                    iz=[i for i,v in enumerate(w) if not v]
                    assert len(nz)==2 and len(iz)==1
                    j=iz[0]
                    value+=surface_curve_term([w[i] for i in nz],
                       [beta[i] for i in nz],[deg[i] for i in nz],
                       beta[j],deg[j])
                    euler+=2
                    c1square+=deg[j]+4
                p1=c1square-2*euler
                assert p1.denominator==1 and p1.numerator%3==0
                assert (c1square+euler).denominator==1
                assert (c1square+euler).numerator%12==0
                topo[cid]={'euler':euler,'c1_square':as_json(c1square),
                           'p1':as_json(p1),'signature':int(p1/3),
                           'holomorphic_euler':int((c1square+euler)/12),
                           'aux_fixed_points':fixed_point_count,
                           'aux_fixed_curves':len(bycomp[cid])}
            sums[cid]=value
        vals.append(sums);topologies.append(topo)
    rows=[]
    total=Q(0)
    dims=defaultdict(Q)
    for cid,c in hcomp.items():
        assert vals[0][cid]==vals[1][cid],(cid,vals[0][cid],vals[1][cid])
        assert topologies[0].get(cid)==topologies[1].get(cid)
        value=vals[0][cid]
        total+=value;dims[c['complex_dimension']]+=value
        rows.append({'id':cid,'complex_dimension':c['complex_dimension'],
                     'residue':as_json(value),
                     'topology':topologies[0].get(cid)})
        checks+=2
    summary={
       'utc':datetime.now(timezone.utc).isoformat(),
       'parameters':{'a':a,'b':b,'N':N},
       'status':'PASS: exact three-point H-unit degrees and two-circle localization',
       'checks':checks,'H_component_count':len(rows),
       'H_full_fibre_torus_fixed_curves':len(hrows),
       'auxiliary_fibre_cocharacters':[[1,K,0,0] for K in aux],
       'H_normal_link_residue':as_json(total),
       'dimension_totals':{str(k):as_json(v) for k,v in sorted(dims.items())},
       'scope':'Compact H fixed components with the actual w,1-w transition '
               'units, complex normal orientations and physical delta. '
               'I/E continuation and global return remain separate.'}
    stem=ROOT/'code/part3_fourfold'/f'source_zero_h_residues_{a}_{b}_{N}'
    Path(str(stem)+'.json').write_text(json.dumps(
        {'summary':summary,'H_fixed_curves':hrows,'components':rows},
        separators=(',',':'))+'\n')
    Path(str(stem)+'_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2),flush=True)
    del d,charts,components,hcomp,hrows
    gc.collect()

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--case',choices=['2,1,6','1,2,8','all'],default='all')
    args=p.parse_args()
    cases=[(2,1,6),(1,2,8)] if args.case=='all' else [tuple(map(int,args.case.split(',')))]
    for case in cases: do_case(*case)
