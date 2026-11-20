"""Complete one endpoint for the fresh 1926-cone common auxiliary fan.

This retains the exact original lattice, L/T units, physical cocharacter,
point/O source arrows, every generic owner and the full lower quotient
charts. It does not claim the unavailable original I2F atlas reproduced.
"""
from pathlib import Path
from collections import defaultdict,Counter
from itertools import combinations
from fractions import Fraction as F
import json
from K111_fan4_exact import *

root=Path(__file__).resolve().parents[1]
src=json.loads((root/'K111_new_regular_common_fan.json').read_text())
lower=json.loads((root/'K111_lower_parent_reconstruction.json').read_text())
checks=0
def ck(x,m):
 global checks
 checks+=1
 if not x:raise AssertionError(m)
fan=[];E0=(0,0,0,1)
for k,rec in enumerate(src['cones']):
 i,j=rec['one_word']
 upper=[(-b+3*(i+j)*h,a-(23*i+11*j)*h,h,0) for a,b,h in rec['rays']]
 c=orient((*upper,E0))
 ck(det(c)==1,'new common cone has integral original-lattice upper lift')
 fan.append(dict(rays=c,kind='upper',generic_owner=k,one_word=[i,j]))
for rec in lower['labels']:
 for c in rec['all_regular_cones']:
  fan.append(dict(rays=orient(c),kind='lower',label=rec['label'],raw_parent=rec['raw_cone']))
ck(len({tuple(sorted(x['rays'])) for x in fan})==len(fan),'whole one atlas has no duplicate four-cones')
ck(sum(volume(x['rays']) for x in fan)==18,'complete original one-parent slice volume')
L=((1,0,3,0),(0,1,1,0),(0,0,1,0),(0,0,0,1))
T=((1,0,0,0),(0,1,12,12),(0,0,1,0),(0,0,0,1))
Linv=((1,0,-3,0),(0,1,-1,0),(0,0,1,0),(0,0,0,1))
Tinv=((1,0,0,0),(0,1,-12,-12),(0,0,1,0),(0,0,0,1))
delta=(0,1,0,0)
incidence=defaultdict(list)
fixed=defaultdict(list)
for k,rec in enumerate(fan):
 c=rec['rays'];d=det(c);ck(d==1,'every full cone is regular')
 inv=adj(c);ck(mm(inv,matrix(c))==tuple(tuple(int(i==j) for j in range(4)) for i in range(4)),'exact inverse ray matrix')
 weights=mv(inv,delta);rec['inverse']=inv;rec['physical_weights']=weights
 rec['source_rows']=[[3*v[2]-v[0] for v in c],[v[0] for v in c]]
 ck(all(n>=0 for row in rec['source_rows'] for n in row),'both entire original source rows nonnegative')
 rec['canonical_orders']=[2*v[2]+v[3]-1 for v in c]
 for face in facets(c):incidence[face].append(k)
 face=tuple(sorted(v for v,w in zip(c,weights) if w))
 fixed[face].append(k)
boundaries=defaultdict(list)
for face,owners in incidence.items():
 ck(len(owners) in [1,2],'complete facet incidence is one or two')
 if len(owners)==2:continue
 forms=[lambda v:v[3],lambda v:v[0],lambda v:v[0]-3*v[2],
        lambda v:3*v[1]-v[0],lambda v:3*v[1]-v[0]-36*v[2]-36*v[3]]
 hits=[i for i,f in enumerate(forms) if all(f(v)==0 for v in face)]
 ck(len(hits)==1,'every complete boundary facet has its unique prescribed type')
 boundaries[hits[0]].append(face)
ck(len(boundaries[0])==len(src['cones']),'generic boundary is exactly the new whole common fan')
maps=[]
for source,target,H,Hinv,up,uc in [(1,2,L,Linv,(1,1,0,0),(0,0,0,0)),(3,4,T,Tinv,(-1,0,0,0),(0,1,0,0))]:
 targets=set(boundaries[target]);images={tuple(sorted(mv(H,v) for v in face)) for face in boundaries[source]}
 ck(images==targets,'entire original period facet set agrees')
 for face in boundaries[source]:
  image=tuple(sorted(mv(H,v) for v in face));si=incidence[face][0];ti=incidence[image][0]
  Bs=matrix(fan[si]['rays']);Bt=matrix(fan[ti]['rays']);Is=fan[si]['inverse'];It=fan[ti]['inverse']
  E=mm(mm(It,H),Bs);Ei=mm(mm(Is,Hinv),Bt)
  ck(mm(E,Ei)==tuple(tuple(int(i==j) for j in range(4)) for i in range(4)),'localized period matrices are reciprocal')
  units=[]
  for u in [up,uc]:
   fwd=mv(It,u);back=tuple(-x for x in mv(mm(Is,Hinv),u))
   ck(tuple(a+b for a,b in zip(mv(Ei,fwd),back))==(0,0,0,0),'full p/c12 columns cancel at actual inverse point')
   units.append(dict(forward=fwd,inverse=back))
  for v in face:
   si0=fan[si]['rays'].index(v);ti0=fan[ti]['rays'].index(mv(H,v))
   ck(tuple(E[i][si0] for i in range(4))==tuple(int(i==ti0) for i in range(4)),'every vanishing face coordinate has the actual target coordinate')
  maps.append(dict(source_face=face,target_face=image,source_chart=si,target_chart=ti,matrix=E,inverse=Ei,units=units))
lower_faces={tuple(sorted([(0,l,0,1),(0,l+1,0,1)])) for l in range(12)}
point_pairs=[];corners=[]
for face,charts in fixed.items():
 if all(v[3]==0 for v in face):continue
 if face in lower_faces:continue
 if len(face)==4:
  ck(len(charts)==1,'each compact corner point has one entire regular chart')
  w=fan[charts[0]]['physical_weights'];prodw=reduce(lambda a,b:a*b,w,1)
  pair=[-F(1,prodw),-F(sum(x*x for x in w),prodw)]
  point_pairs.append(pair);corners.append(dict(face=face,charts=charts,pair=pair))
 else:ck(False,'unexpected fresh one-corner fixed component requires its own complete star')
ck(len(corners)==60,'new one endpoint has the complete sixty compact points')
compact=[sum(x[k] for x in point_pairs) for k in range(2)]
ck(compact==[12,88],'fresh full one-atlas compact sum')
out=dict(scope='Complete fresh one-end atlas over the original raw cell, with the1926-cone common boundary, all twelve minimal lower stars, entire facet inventory and full L/T p,c12 maps. This auxiliary atlas is distinct from the unavailable original149774-cone file; the remaining three-end boundary comparison is separate.',
         checks=checks,cones=fan,facet_counts={str(k):len(v) for k,v in boundaries.items()},internal_facets=sum(len(v)==2 for v in incidence.values()),period_maps=maps,
         compact_corner_points=corners,compact_pair=compact,lower_labels=12,lower_completed_pair_each=[1,-2],
         source_functions={'x':'p*P^3/X1','y':'X1','product':'Q=p*P^3'},
         original_point_module={'forward':'v2=eta*P^2*Y1/(X1*f_{P^2}(p*P^3/X1))','inverse':'Y1=eta^-1*P^-2*X1*f_{P^2}(p*P^3/X1)*v2',
                                'point_graph':'Bl_(p*P^3/X1,P^2)','eta':'a_T*Theta_Q_prime(1)*Theta_Q(P^2)/Theta_Q(P)^2'},
         original_volume='-(2*J_ts/a_T)*P*dP wedge dv wedge dlogX1 wedge dlogY1')
(root/'K111_new_one_endpoint.json').write_text(json.dumps(serial(out),indent=2)+'\n')
print(json.dumps(dict(checks=checks,full_cones=len(fan),boundary_facets=out['facet_counts'],internal_facets=out['internal_facets'],period_maps=len(maps),compact_points=len(corners),compact_pair=serial(compact)),indent=2))
