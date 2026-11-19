#!/usr/bin/env python3
"""Exact normal-link residues of compact interior fixed components.

The input is the executed regular-fan fixed-chart export.  Each interior
minimal-face component is unwrapped using its recorded period.  Two
independent auxiliary circle choices evaluate the same localized
characteristic number.  No boundary component, global source-family
return, or orientation comparison to the Jin manifold is inferred.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
from collections import Counter,defaultdict
from math import prod
import argparse,json,gc

ROOT=Path(__file__).resolve().parents[2]

def matvec(A,v):
    return [sum(x*y for x,y in zip(row,v)) for row in A]

def transported_aux(eps,n,sector,a,b,N):
    H=((2,b),(-a,N-2))
    P0={'I':((1,0),(0,0)),
        'W':((1,b),(-a,-2)),
        'E':((0,0),(0,N))}[sector]
    r,s=eps[2:]
    return [eps[i]+sum((r*P0[i][j]+s*H[i][j])*n[j]
                       for j in range(2)) for i in range(2)]+eps[2:]

def residue_at_chart(w,beta):
    inds=[i for i,x in enumerate(w) if x]
    tangent=[i for i,x in enumerate(w) if not x]
    weights=[Q(w[i]) for i in inds]
    roots=[Q(beta[i]) for i in inds]
    tang=[Q(beta[i]) for i in tangent]
    assert all(tang)
    P=prod(weights)
    c=4-sum(x*x for x in weights)
    if len(inds)==4:
        numerator=c
    elif len(inds)==3:
        numerator=-sum((c/x+2*x)*z for x,z in zip(weights,roots))
    elif len(inds)==2:
        x,y=roots
        u,v=weights
        A=x/u+y/v
        B=x*x/(u*u)+x*y/(u*v)+y*y/(v*v)
        S=u*x+v*y
        numerator=c*B+2*S*A-(sum(t*t for t in tang)+x*x+y*y)
    else:
        raise AssertionError("Unexpected fixed dimension")
    return numerator/(24*P*prod(tang))

def as_json(q):
    return {'numerator':q.numerator,'denominator':q.denominator,
            'rational':str(q)}

def do_case(a,b,N):
    src=ROOT/'code/part3_fourfold'/f'source_infinity_fixed_charts_{a}_{b}_{N}.json'
    with (ROOT/'records/literature_fourfold.md').open('a') as f:
        f.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened '
                +str(src.relative_to(ROOT))+'. Reason: exact compact-interior '
                'normal-link residues by the actual cone/period matrices. '
                'Material: dual characters, physical weights, minimal faces '
                'and recorded unwrapping periods; no global return assigned.\n')
    d=json.loads(src.read_text())
    components={c['id']:c for c in d['components']}
    interior={k:c for k,c in components.items() if c['boundary_tag'] is None}
    charts=[c for c in d['charts'] if c['component'] in interior]
    tests=0
    for c in charts:
        assert sum(w*o for w,o in zip(c['physical_weights'],
                                     c['source_parameter_orders']))==0
        tests+=1
    # A finite collection of hyperplanes is avoided by the integer moment curve.
    aux=[]
    trial=2
    while len(aux)<2:
        eps=[1,trial,trial**2,trial**3]
        good=True
        for c in charts:
            e=transported_aux(eps,c['period_from_canonical'],c['sector'],a,b,N)
            beta=matvec(c['dual_character_rows'],e)
            if any(beta[j]==0 for j in c['zero_weight_columns']):
                good=False
                break
        if good:
            aux.append(eps)
        trial+=1
        assert trial<1000
    values=[]
    for eps in aux:
        sums=defaultdict(Q)
        for c in charts:
            e=transported_aux(eps,c['period_from_canonical'],c['sector'],a,b,N)
            beta=matvec(c['dual_character_rows'],e)
            sums[c['component']]+=residue_at_chart(c['physical_weights'],beta)
        values.append(sums)
    rows=[]
    total=Q(0)
    dimtot=defaultdict(Q)
    sector_tot=defaultdict(Q)
    distributions=Counter()
    for fid,c in interior.items():
        x=values[0][fid]
        assert x==values[1][fid],(fid,x,values[1][fid])
        assert not c['period_stabilizer_basis']
        if c['complex_dimension']==1:
            assert len(c['charts'])==2
        tests+=3
        total+=x
        dimtot[c['complex_dimension']]+=x
        sector_tot[c['orbit_sector']]+=x
        distributions[(c['complex_dimension'],str(x))]+=1
        rows.append({'id':fid,'complex_dimension':c['complex_dimension'],
                     'sector':c['orbit_sector'],
                     'chart_count':len(c['charts']),
                     'normal_weights':c['normal_weights_canonical_order'],
                     'residue':as_json(x)})
    summary={
       'utc':datetime.now(timezone.utc).isoformat(),
       'parameters':{'a':a,'b':b,'N':N},
       'status':'PASS: compact interior normal-link residue and auxiliary-circle independence',
       'source':str(src.relative_to(ROOT)),
       'auxiliary_cocharacters':aux,
       'checks':tests,'interior_component_count':len(rows),
       'interior_chart_count':len(charts),
       'total_normal_link_residue':as_json(total),
       'dimension_totals':{str(k):as_json(v) for k,v in sorted(dimtot.items())},
       'sector_totals':{str(k):as_json(v) for k,v in sorted(sector_tot.items())},
       'residue_distribution':[{'complex_dimension':k[0],'residue':k[1],'count':v}
                                for k,v in sorted(distributions.items())],
       'scope':'The displayed residue uses complex normal orientations and the '
               'physical circle variable. Boundary-tag I,W,E,H components, '
               'ordinary/cap continuation, all global orientation maps, and '
               'the completed-family return remain separate.'}
    stem=ROOT/'code/part3_fourfold'/f'source_infinity_interior_residues_{a}_{b}_{N}'
    Path(str(stem)+'.json').write_text(json.dumps(
        {'summary':summary,'components':rows},separators=(',',':'))+'\n')
    Path(str(stem)+'_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items()
                      if k!='residue_distribution'},indent=2),flush=True)
    del d,components,interior,charts
    gc.collect()

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--case',choices=['2,1,6','1,2,8','all'],default='all')
    args=p.parse_args()
    cases=[(2,1,6),(1,2,8)] if args.case=='all' else [tuple(map(int,args.case.split(',')))]
    for case in cases:
        do_case(*case)
