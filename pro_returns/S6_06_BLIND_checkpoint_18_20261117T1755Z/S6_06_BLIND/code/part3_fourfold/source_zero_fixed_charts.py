#!/usr/bin/env python3
"""Exact physical-delta charts of the exported regular K39 fans.

Every entry comes from the literal determinant-one cone matrix.  This
does not replace analytic base-unit transitions by monomials, compute
normal Chern classes, or assign a completed-family return.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter,defaultdict
import argparse,json,gc

ROOT=Path(__file__).resolve().parents[2]
def det3(m):
 return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
         -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
         +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
def inverse_det1(C):
 A=[[0]*4 for _ in range(4)]
 for i in range(4):
  for j in range(4):
   A[i][j]=(-1)**(i+j)*det3(
       [[C[r][c] for c in range(4) if c!=i]
                    for r in range(4) if r!=j])
 assert all(sum(C[i][k]*A[k][j] for k in range(4))==int(i==j)
            for i in range(4) for j in range(4))
 return A
def do_case(a,b,N):
 src=ROOT/'code/part3'/f'source_zero_regular_fan_{a}_{b}_{N}.json'
 with (ROOT/'records/literature_fourfold.md').open('a') as f:
  f.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened '
          +str(src.relative_to(ROOT))+'. Reason: exact fixed-chart and '
          'normal-weight calculation from actual regular cone data. Material: '
          'primitive vectors, ordered cone matrices, canonical face periods '
          'and vertex permutations; no characteristic value inferred.\n')
 d=json.loads(src.read_text())
 assert d['physical_delta']==[0,1,0,0]
 ray={z['id']:z for sec in d['literal_rays'].values() for z in sec}
 face={z['id']:z for z in d['face_orbits']}
 lookup={}
 for f in d['face_orbits']:
  for occ in f['occurrences']:
   key=(occ['cone'],tuple(occ['local_columns']))
   assert key not in lookup
   lookup[key]=(f['id'],occ['vertex_permutation_to_canonical'],
                occ['period_from_canonical'])
 components={}
 charts=[]
 checks=0
 weight_types=Counter()
 dimension_charts=Counter()
 for c in d['maximal_cones']:
  vec=[ray[k]['vector'] for k in c['ordered_rays']]
  C=[[vec[j][i] for j in range(4)] for i in range(4)]
  A=inverse_det1(C); checks+=16
  weights=[A[i][1] for i in range(4)]
  assert [sum(C[i][j]*weights[j] for j in range(4))
          for i in range(4)]==[0,1,0,0]; checks+=4
  nonzero=tuple(i for i,w in enumerate(weights) if w)
  zeros=tuple(i for i,w in enumerate(weights) if not w)
  rank=len(nonzero)
  assert 2<=rank<=4
  if rank<4:
   fid,perm,period=lookup[(c['id'],nonzero)]
   f=face[fid]
   assert f['dimension']==rank
   nw=[0]*rank
   for j,idx in enumerate(nonzero): nw[perm[j]]=weights[idx]
   fv=f['canonical_vectors']
   assert [sum(fv[j][i]*nw[j] for j in range(rank))
           for i in range(4)]==[0,1,0,0]; checks+=4
   tag=f['boundary_tag']; stab=f['period_stabilizer_basis']
   sector=f['orbit_sector']
   face_period={'period_from_canonical':period,
                'vertex_permutation_to_canonical':perm}
  else:
   fid='point_'+c['id']; nw=weights[:]; tag=None;stab=[];sector=c['sector']
   fv=vec;face_period={'period_from_canonical':[0,0],
                      'vertex_permutation_to_canonical':list(range(4))}
  if fid not in components:
   components[fid]={
      'id':fid,'complex_dimension':4-rank,
      'minimal_face_dimension':rank,
      'normal_weights_canonical_order':nw,
      'boundary_tag':tag,'orbit_sector':sector,
      'canonical_vectors':fv,'period_stabilizer_basis':stab,
      'charts':[]}
  else:
   assert components[fid]['normal_weights_canonical_order']==nw
   assert components[fid]['complex_dimension']==4-rank
   checks+=2
  components[fid]['charts'].append(c['id'])
  dimension_charts[4-rank]+=1
  weight_types[tuple(sorted(weights))]+=1
  charts.append({
     'id':c['id'],'sector':c['sector'],'component':fid,
     'ordered_rays':c['ordered_rays'],'matrix':C,
     'dual_character_rows':A,'physical_weights':weights,
     'zero_weight_columns':zeros,'normal_columns':nonzero,
     'source_parameter_orders':[ray[k]['source_parameter_order']
                                for k in c['ordered_rays']],
     **face_period})
 compdim=Counter(c['complex_dimension'] for c in components.values())
 tags=Counter((c['complex_dimension'],str(c['boundary_tag']))
              for c in components.values())
 normal_types=Counter((c['complex_dimension'],
                       tuple(sorted(c['normal_weights_canonical_order'])))
                      for c in components.values())
 summary={
   'utc':datetime.now(timezone.utc).isoformat(),
   'status':'PASS: exact fixed-chart weights and minimal-face orbit identifications',
   'parameters':d['parameters'],'source':str(src.relative_to(ROOT)),
   'checks':checks,'chart_count':len(charts),
   'component_count_in_local_fan_quotient':len(components),
   'complex_dimension_component_counts':dict(sorted(compdim.items())),
   'complex_dimension_chart_counts':dict(sorted(dimension_charts.items())),
   'boundary_tag_component_counts':[
       {'complex_dimension':dim,'tag':tag,'count':n}
       for (dim,tag),n in sorted(tags.items())],
   'normal_weight_types':[
       {'complex_dimension':dim,'weights':w,'count':n}
       for (dim,w),n in sorted(normal_types.items())],
   'scope':'Local regular-fan fixed components with exact period identifications. '
           'Ordinary-source/cap continuation and full analytic base-unit normal '
           'transitions remain to be glued before normal Chern classes or return.'
 }
 stem=ROOT/'code/part3_fourfold'/f'source_zero_fixed_charts_{a}_{b}_{N}'
 Path(str(stem)+'.json').write_text(json.dumps(
    {'summary':summary,'components':list(components.values()),'charts':charts},
    separators=(',',':'))+'\n')
 Path(str(stem)+'_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
 print(json.dumps({k:v for k,v in summary.items()
                   if k!='normal_weight_types'},indent=2),flush=True)
 del d,ray,face,lookup,components,charts
 gc.collect()
 return summary
if __name__=='__main__':
 p=argparse.ArgumentParser()
 p.add_argument('--case',choices=['2,1,6','1,2,8','all'],default='all')
 args=p.parse_args()
 cases=[(2,1,6),(1,2,8)] if args.case=='all' else [tuple(map(int,args.case.split(',')))]
 for case in cases: do_case(*case)
