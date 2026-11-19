"""Exact native Cayley corner lifts of the generic common fan.

This certificate retains the actual native domain first. The common-coordinate
matrix includes all p powers; no corner factor is declared a unit.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'code/part3_root/e6_common_period_fan.json'
d=json.loads(source.read_text());check=[]
def ck(v,msg):
 assert v,msg
 check.append(msg)
def matrix(rays):return s.Matrix.hstack(*map(s.Matrix,rays))
def asint(M):return [[int(x) for x in row] for row in M.tolist()]
def canon(rays):return tuple(sorted(map(tuple,rays)))
def area(rays):
 M=matrix(rays);return F(abs(int(M.det())),2*int(rays[0][2])*int(rays[1][2])*int(rays[2][2]))
def faces(cones,row):
 out=set()
 for c in cones:
  for face in combinations(c['rays'],3):
   if all(sum(a*b for a,b in zip(row,v))==0 for v in face):out.add(canon(face))
 return out
A=(0,0,0,1);B=(0,-1,0,1)
outputs={}
for end in ('zero','infinity'):
 old=json.loads((ROOT/('code/part3/e6_p_zero_semifree_fan.json' if end=='zero' else 'code/part3/e6_p_infinity_fan.json')).read_text())
 uppers={}
 for number,c in enumerate(d['cones']):
  if end=='zero':
   parent=d['parent_zero_instances'][c['zero_parent']];i,j=parent['shift'];rays=[]
   for X,Y,h in c['rays']:
    X-=(5*i+j)*h;Y-=(i+2*j)*h
    rays.append((-X-3*Y,X+4*Y,h))
   pi=parent['k']
   full=[[ -4,-3,5*i+j,-6-3*i-3*j],[1,1,i+2*j,i+j],[0,0,1,0],[0,0,0,1]]
   bunit=[-2*i-j,0,0,0]
  else:
   rays=list(map(tuple,c['rays']));pi=c['infinity_parent']
   full=[[1,0,0,0],[0,1,0,0],[0,0,1,1],[0,0,0,-1]];bunit=[0,0,0,0]
  ck(abs(int(matrix(rays).det()))==1,f'{end} upper regular {number}')
  key=canon(rays)
  item=uppers.setdefault(key,{'rays':rays,'parent':pi,'generic_references':[]})
  ck(item['parent']==pi,f'{end} consistent native parent {number}')
  item['generic_references'].append({'common_cone':number,'common_character_matrix':full,'common_b_unit':bunit})
 ck(sum(area(c['rays']) for c in uppers.values())==9,f'{end} exact upper area9')
 cones=[]
 for c in uppers.values():
  rays=[A]+[tuple(v)+(0,) for v in c['rays']]
  cones.append({'rays':rays,'parent':c['parent'],'kind':'upper_star','generic_references':c['generic_references']})
 # Lower strips are exactly the old AB stars. Use their native upper edge.
 lower_counts=[]
 for pi,pc in enumerate(old['cones']):
  if len([v for v in pc['rays'] if v[2]==0])!=2:continue
  er=[tuple(v[:3]) for v in pc['rays'] if v[2]>0];u,v=er
  n=s.Matrix(u).cross(s.Matrix(v));n=tuple(int(x) for x in n)
  pairs=set()
  for c in uppers.values():
   for edge in combinations(c['rays'],2):
    if all(sum(a*b for a,b in zip(n,w))==0 for w in edge):
     # The old strip is a single old edge. Endpoint coefficients must be nonnegative.
     good=True
     for w in edge:
      sol=matrix([u,v]).gauss_jordan_solve(s.Matrix(w))[0]
      good &= all(x>=0 for x in sol)
     if good:pairs.add(canon(edge))
  ck(bool(pairs),f'{end} lower strip {pi} nonempty')
  for edge in sorted(pairs):cones.append({'rays':[A,B]+[tuple(w)+(0,) for w in edge],'parent':pi,'kind':'lower_strip','generic_references':[]})
  lower_counts.append(len(pairs))
 for n,c in enumerate(cones):
  N=matrix(c['rays']);Np=matrix(old['cones'][c['parent']]['rays']);mon=Np.inv()*N
  ck(abs(int(N.det()))==1,f'{end} 4cone regular {n}')
  ck(all(x.is_Integer and x>=0 for x in mon),f'{end} proper parent semigroup {n}')
  delta=s.Matrix([-1,1,0,0] if end=='zero' else [1,0,0,0]);weights=N.inv()*delta
  ck(all(x.is_Integer for x in weights),f'{end} physical weights {n}')
  c.update(parent_monomial_matrix=asint(mon),dual_characters=asint(N.inv()),physical_weights=list(map(int,weights)),base_multiplicities={'first':[v[2] for v in c['rays']],'second':[v[3] for v in c['rays']]})
  # Inherited original volume is P or R times the logarithmic form.
  c['original_canonical_orders']=[2*v[2]+v[3]-1 for v in c['rays']]
  qr=(0,0,3,1) if end=='zero' else (0,0,3,2)
  zr=(1,1,0,0) if end=='zero' else (0,1,0,0)
  source_charts=[]
  for k in (range(5) if end=='zero' else [1]):
   rowZ=tuple(zr[a]+k*qr[a] for a in range(4))
   rowW=tuple(-zr[a]+(1-k)*qr[a] for a in range(4))
   ez=[sum(a*b for a,b in zip(rowZ,v)) for v in c['rays']]
   ew=[sum(a*b for a,b in zip(rowW,v)) for v in c['rays']]
   if min(ez+ew)>=0:source_charts.append({'k':k,'Z_exponents':ez,'W_exponents':ew})
  c['whole_cone_source_charts']=source_charts
  if end=='infinity':ck(bool(source_charts),f'infinity actual source projection {n}')
  for v in c['rays']:
   qv=sum(a*b for a,b in zip(qr,v));zv=sum(a*b for a,b in zip(zr,v))
   ck(any(0<=zv+k*qv<=qv for k in (range(5) if end=='zero' else [1])),f'{end} finite source-height range {n}')
 # Exact positive-height volumes are checked separately in every old chart.
 def volume(rays):
  value=F(abs(int(matrix(rays).det())),6)
  for v in rays:value/=v[2]+v[3]
  return value
 for pi,pc in enumerate(old['cones']):
  ck(sum((volume(c['rays']) for c in cones if c['parent']==pi),F(0))==volume(pc['rays']),f'{end} exact old-chart coverage {pi}')
 incidence=Counter(canon(face) for c in cones for face in combinations(c['rays'],3))
 ck(all(n in (1,2) for n in incidence.values()),f'{end} facet incidence1or2')
 if end=='zero':
  maps=[('H1',(1,0,0,0),(1,0,1,0),s.Matrix([[1,0,1,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])),('K0',(0,1,0,0),(0,1,9,1),s.Matrix([[1,0,0,0],[0,1,9,1],[0,0,1,0],[0,0,0,1]]))]
 else:
  maps=[('K',(1,0,0,0),(1,0,5,0),s.Matrix([[1,0,5,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]])),('J',(0,1,0,0),(0,1,2,1),s.Matrix([[1,0,1,0],[0,1,2,1],[0,0,1,0],[0,0,0,1]])),('KJinv',(1,-1,-1,-1),(1,-1,4,0),s.Matrix([[1,0,4,0],[0,1,-1,-1],[0,0,1,0],[0,0,0,1]]))]
 for name,target,start,T in maps:
  left=faces(cones,target);right={canon([tuple(map(int,T*s.Matrix(v))) for v in face]) for face in faces(cones,start)}
  ck(left==right,f'{end} full 4D periodic face {name}')
 outputs[end]={'upper_cones':len(uppers),'lower_strip_counts':lower_counts,'cones':cones,'facet_incidence':dict(Counter(incidence.values())),'whole_cone_source_count':sum(bool(c['whole_cone_source_charts']) for c in cones),'period_matrices':{name:asint(T) for name,_,_,T in maps},'scope':'Native corner refinement with exact proper monomial arrows and full periodic facets. Remaining source-height cuts and total point-line graph refinement are explicitly retained.'}
report={'status':'PASS','checks':len(check),'check_labels':check,'generic_certificate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'ends':outputs,'scope':'Actual native p0 and p-infinity Cayley corner refinements; inherited divisor factors and finite isotropy retained. No global compact attachment, spin extension or return.'}
(ROOT/'code/part3/e6_common_corner_lift.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(check),'ends':{k:{'upper':v['upper_cones'],'lower':v['lower_strip_counts'],'total':len(v['cones'])} for k,v in outputs.items()}}))
