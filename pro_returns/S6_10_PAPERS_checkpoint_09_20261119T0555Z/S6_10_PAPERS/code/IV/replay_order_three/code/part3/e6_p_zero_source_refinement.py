"""Periodic coordinate blowups making the actual p-zero Tate source map regular.
Every new ray is the sum of the two primitive rays of an actual regular
2-face, and all its H1/K0 boundary partners are inserted in the same step.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from math import floor,ceil
import json,time,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
input_path=ROOT/'code/part3/e6_common_corner_lift.json'
original=json.loads(input_path.read_text())['ends']['zero']['cones']
started=time.monotonic();history=[];checks=[]
def ck(value,name):
 assert value,name
 checks.append(name)
def canonical(rays):return tuple(sorted(map(tuple,rays)))
def matrix(rays):return s.Matrix.hstack(*map(s.Matrix,rays))
def source_k(rays):
 return [k for k in range(5) if all(0<=v[0]+v[1]+k*(3*v[2]+v[3])<=3*v[2]+v[3] for v in rays)]
def primitive_period_images(u,v):
 z=tuple(a+b for a,b in zip(u,v));X,Y,r,t=z;S=9*r+t
 ii=range(ceil(F(-r-X,r)),floor(F(-X,r))+1) if r else [0]
 jj=range(ceil(F(-S-Y,S)),floor(F(-Y,S))+1)
 out={}
 for i in ii:
  for j in jj:
   def T(a):return (a[0]+i*a[2],a[1]+j*(9*a[2]+a[3]),a[2],a[3])
   U,V=T(u),T(v);pair=canonical([U,V]);out[pair]={'shift':[i,j],'ray':tuple(a+b for a,b in zip(U,V))}
 return out
cones={canonical(c['rays']):{'rays':tuple(map(tuple,c['rays'])),'original_cone':i} for i,c in enumerate(original)}
print(json.dumps({'stage':'start','cones':len(cones),'source_regular':sum(bool(source_k(c['rays'])) for c in cones.values())}),flush=True)
while True:
 bad=[c for c in cones.values() if not source_k(c['rays'])]
 if not bad:break
 candidates={}
 for c in bad:
  for k in range(5):
   L=lambda v:v[0]+v[1]+k*(3*v[2]+v[3])
   for u,v in combinations(c['rays'],2):
    a,b=L(u),L(v)
    if a*b<0:
     pair=canonical([u,v]);priority=(abs(a)+abs(b),max(abs(a),abs(b)),max(u[2]+u[3],v[2]+v[3]),pair,k)
     if pair not in candidates or priority<candidates[pair][0]:candidates[pair]=(priority,k)
 ck(bool(candidates),'every bad cone has a mixed integral source height')
 pair,(priority,k)=min(candidates.items(),key=lambda p:p[1][0]);u,v=pair
 images=primitive_period_images(u,v);moves=[]
 for edge,data in images.items():
  hit=[key for key,c in cones.items() if set(edge)<=set(c['rays'])]
  ck(bool(hit),'period partner is an actual 2-face')
  newray=data['ray'];removed=[];added=[]
  for key in hit:
   c=cones.pop(key);rays=c['rays'];removed.append(rays)
   for oldray in edge:
    nxt=list(rays);nxt[nxt.index(oldray)]=newray;nxt=tuple(nxt)
    newkey=canonical(nxt);ck(newkey not in cones,'stellar child is new')
    cones[newkey]={**c,'rays':nxt};added.append(nxt)
  moves.append({'edge':edge,'ray':newray,'period_shift':data['shift'],'removed':removed,'added':added})
 history.append({'source_height_k':k,'selected_edge':pair,'periodic_moves':moves})
 if len(history)%25==0:print(json.dumps({'stage':'blowups','steps':len(history),'cones':len(cones),'remaining_bad':len(bad),'seconds':round(time.monotonic()-started,1)}),flush=True)
 if len(history)>=3000:
  (ROOT/'code/part3/e6_p_zero_source_refinement_attempt.json').write_text(json.dumps({'status':'INCOMPLETE_STEP_BOUND','history':history,'cones':list(cones.values())},indent=2)+'\n')
  raise RuntimeError('3000-step working bound; incomplete attempt preserved')

def facets(row):
 out=set()
 for c in cones.values():
  for face in combinations(c['rays'],3):
   if all(sum(a*b for a,b in zip(row,v))==0 for v in face):out.add(canonical(face))
 return out
period_maps=[('H1',(1,0,0,0),(1,0,1,0),s.Matrix([[1,0,1,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])),('K0',(0,1,0,0),(0,1,9,1),s.Matrix([[1,0,0,0],[0,1,9,1],[0,0,1,0],[0,0,0,1]]))]
for name,target,start,T in period_maps:
 ck(facets(target)=={canonical(tuple(map(int,T*s.Matrix(v))) for v in face) for face in facets(start)},'full periodic source-refined facet '+name)
records=[];old_vol=Counter();new_vol=Counter()
for i,c in enumerate(original):
 den=6
 for v in c['rays']:den*=v[2]+v[3]
 old_vol[i]=F(1,den)
for num,c in enumerate(cones.values()):
 N=matrix(c['rays']);ck(abs(int(N.det()))==1,'regular final four-cone')
 Nold=matrix(original[c['original_cone']]['rays']);m=Nold.inv()*N
 ck(all(x.is_Integer and x>=0 for x in m),'exact parent semigroup morphism')
 ks=source_k(c['rays']);ck(bool(ks),'whole-cone actual source chart')
 k=ks[0];rz=(1,1,3*k,k);rw=(-1,-1,3*(1-k),1-k)
 ez=[sum(a*b for a,b in zip(rz,v)) for v in c['rays']];ew=[sum(a*b for a,b in zip(rw,v)) for v in c['rays']]
 ck(all(a+b==3*v[2]+v[3] for a,b,v in zip(ez,ew,c['rays'])),'literal source ZW=Q')
 weights=list(map(int,N.inv()*s.Matrix([-1,1,0,0])))
 ck(sum(a*b for a,b in zip(weights,ez))==0 and sum(a*b for a,b in zip(weights,ew))==0,'source physical-circle invariance')
 den=6
 for v in c['rays']:den*=v[2]+v[3]
 new_vol[c['original_cone']]+=F(1,den)
 records.append({**c,'parent_monomial_matrix':[[int(x) for x in row] for row in m.tolist()],'source_k':ks,'source_Z_exponents':ez,'source_W_exponents':ew,'physical_weights':weights,'original_canonical_orders':[2*v[2]+v[3]-1 for v in c['rays']]})
ck(old_vol==new_vol,'exact support volume in all520 input cones')
inc=Counter(canonical(face) for c in cones.values() for face in combinations(c['rays'],3))
ck(all(n in (1,2) for n in inc.values()),'facet incidence1or2')
report={'status':'PASS','checks':len(checks),'check_labels':checks,'input_sha256':hashlib.sha256(input_path.read_bytes()).hexdigest(),'coordinate_blowups':len(history),'history':history,'cones':records,'facet_incidence':dict(Counter(inc.values())),'scope':'Actual periodic regular zero-corner modification and literal source Z_k,W_k; full point-line graph, inherited spin and compact boundary remain open.','seconds':round(time.monotonic()-started,2)}
(ROOT/'code/part3/e6_p_zero_source_refinement.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'steps':len(history),'cones':len(records),'facets':report['facet_incidence'],'seconds':report['seconds']}),flush=True)
