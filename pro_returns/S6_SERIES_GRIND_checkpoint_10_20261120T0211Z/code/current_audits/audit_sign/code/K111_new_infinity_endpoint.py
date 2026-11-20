"""Fresh complete infinity lift of the constructed common auxiliary fan.

All subdivision maps use the original four-lattice. Full periodic face
maps, source/point characters and physical fixed-star owners are retained.
The compact residue calculation below uses only complete aligned stars.
"""
from pathlib import Path
from collections import defaultdict,deque,Counter
from fractions import Fraction as F
from itertools import product
from functools import cmp_to_key
import json
from K111_fan4_exact import *

root=Path(__file__).resolve().parents[1]
src=json.loads((root/'K111_new_regular_common_fan.json').read_text())
checks=0
def ck(x,m):
 global checks
 checks+=1
 if not x:raise AssertionError(m)
I=tuple(tuple(int(i==j) for j in range(4)) for i in range(4))
A0=(0,0,0,1);A1=(0,-1,0,1);delta=(1,0,0,0)
upper=[dict(rays=orient([(*v,0) for v in rec['rays']]+[A0]),kind='upper',generic_owner=k) for k,rec in enumerate(src['cones'])]
lower=[]
for facet in [1,2]:
 for k,edge in enumerate(src['boundary_edges'][facet]):
  c=orient([A0,A1,*[(*v,0) for v in edge]])
  ck(det(c)==(1 if facet==1 else 11),'actual raw lower determinant from saturated boundary interval')
  lower.append(dict(rays=c,kind='lower',raw_parent=c,facet=facet,edge=k))
history=[]
def quotient(c):
 d=det(c);J=adj(c);zero=(0,0,0,0)
 gens=[tuple(J[i][j]%d for i in range(4)) for j in range(4)]
 seen={zero};q=deque([zero])
 while q:
  a=q.popleft()
  for b in gens:
   z=tuple((x+y)%d for x,y in zip(a,b))
   if z not in seen:seen.add(z);q.append(z)
 ck(len(seen)==d,'entire singular lower quotient enumerated')
 rays=[]
 for a in seen-{zero}:
  v=[sum(c[i][k]*a[i] for i in range(4)) for k in range(4)]
  ck(all(x%d==0 for x in v),'whole quotient vector integral')
  rays.append(prim(tuple(x//d for x in v)))
 return min(set(rays),key=lambda v:(v[2]+v[3],v[2],sum(map(abs,v)),v))
while any(det(x['rays'])>1 for x in lower):
 rec=max(lower,key=lambda x:det(x['rays']));v=quotient(rec['rays'])
 ck(v[2]>0 and v[3]>0,'new lower ray maps to the original collision')
 ck(v[1]<-3*v[2] or 3*v[0]-11*v[1]>0,'new lower ray is outside every upper star')
 out=[];changes=[]
 for old in lower:
  c=old['rays'];a=bary(c,v)
  if min(a)<0 or sum(x>0 for x in a)<=1:out.append(old);continue
  children=[]
  for k,x in enumerate(a):
   if x<=0:continue
   cc=list(c);cc[k]=v;cc=tuple(cc)
   ck(0<det(cc)<det(c),'strict quotient determinant descent on every incident cone')
   children.append(cc);out.append(dict(old,rays=cc))
  changes.append(dict(parent=c,barycentric=a,children=children))
 ck(bool(changes),'actual entire lower incident star subdivided')
 history.append(dict(ray=v,changes=changes));lower=out

fan=upper+lower
ck(len({tuple(sorted(x['rays'])) for x in fan})==len(fan),'no duplicate complete infinity cones')
ck(sum(volume(x['rays']) for x in fan)==F(95,6),'whole original infinity slice volume')
L=((1,0,23,0),(0,1,3,0),(0,0,1,0),(0,0,0,1))
T=((1,0,11,0),(0,1,3,1),(0,0,1,0),(0,0,0,1))
Li=((1,0,-23,0),(0,1,-3,0),(0,0,1,0),(0,0,0,1))
Ti=((1,0,-11,0),(0,1,-3,-1),(0,0,1,0),(0,0,0,1))
LT=mm(L,Ti);LTi=mm(T,Li)
incidence=defaultdict(list);fixed=defaultdict(list)
for k,rec in enumerate(fan):
 c=rec['rays'];ck(det(c)==1,'all full infinity cones regular in original lattice')
 inv=adj(c);ck(mm(inv,matrix(c))==I,'exact whole inverse matrix')
 rec['inverse']=inv;rec['physical_weights']=mv(inv,delta)
 rec['source_rows']=[[v[1]+3*v[2]+2*v[3] for v in c],[-v[1] for v in c]]
 ck(all(x>=0 for row in rec['source_rows'] for x in row),'both original source rows nonnegative')
 rec['canonical_orders']=[2*v[2]+v[3]-1 for v in c]
 for face in facets(c):incidence[face].append(k)
 ff=tuple(sorted(v for v,w in zip(c,rec['physical_weights']) if w));fixed[ff].append(k)
forms=[lambda v:v[3],lambda v:v[0]+23*v[2],lambda v:v[0],
       lambda v:v[1]+3*v[2]+v[3],lambda v:v[1],
       lambda v:3*v[0]-11*v[1]+36*v[2],lambda v:3*v[0]-11*v[1]-11*v[3]]
boundary=defaultdict(list)
for face,owners in incidence.items():
 ck(len(owners) in [1,2],'every full facet occurs once or twice')
 if len(owners)==2:continue
 hit=[k for k,f in enumerate(forms) if all(f(v)==0 for v in face)]
 ck(len(hit)==1,'every boundary facet has its unique original source type')
 boundary[hit[0]].append(face)
ck(len(boundary[0])==len(src['cones']),'generic boundary is exactly the new common fan')
maps=[];face_graph=defaultdict(list)
for source,target,H,Hi,u,name in [(1,2,L,Li,(2,0,0,0),'L'),(3,4,T,Ti,(1,0,0,0),'T'),(5,6,LT,LTi,(1,0,0,0),'L/T')]:
 images={tuple(sorted(mv(H,v) for v in f)) for f in boundary[source]}
 ck(images==set(boundary[target]),'entire original period facet pairing')
 for face in boundary[source]:
  image=tuple(sorted(mv(H,v) for v in face));si=incidence[face][0];ti=incidence[image][0]
  Bs=matrix(fan[si]['rays']);Bt=matrix(fan[ti]['rays']);Is=fan[si]['inverse'];It=fan[ti]['inverse']
  E=mm(mm(It,H),Bs);Ei=mm(mm(Is,Hi),Bt)
  ck(mm(E,Ei)==I,'full period chart inverse')
  fwd=mv(It,u);back=tuple(-x for x in mv(mm(Is,Hi),u))
  ck(tuple(x+y for x,y in zip(mv(Ei,fwd),back))==(0,0,0,0),'whole f_infinity coefficient and reciprocal cancel')
  for v in face:
   a=fan[si]['rays'].index(v);b=fan[ti]['rays'].index(mv(H,v))
   ck(tuple(E[k][a] for k in range(4))==tuple(int(k==b) for k in range(4)),'localized vanishing coordinate maps to its actual target')
  maps.append(dict(name=name,source_face=face,target_face=image,source_chart=si,target_chart=ti,matrix=E,inverse=Ei,full_f_unit=fwd,inverse_f_unit=back))
  for ff in fixed:
   if set(ff)<=set(face):
    gg=tuple(sorted(mv(H,v) for v in ff))
    ck(gg in fixed,'whole physical fixed-face period image retained')
    face_graph[ff].append((gg,H,Hi));face_graph[gg].append((ff,Hi,H))

# Complete corner physical stars are aligned by their exact inverse period
# matrices. The products around every cycle are verified literally.
seen=set();components=[]
for face in fixed:
 if face in seen:continue
 align={face:I};q=deque([face]);seen.add(face)
 while q:
  f=q.popleft()
  for g,H,Hi in face_graph[f]:
   A=mm(align[f],Hi)
   if g in align:ck(align[g]==A,'complete fixed-star period cycle is trivial')
   else:align[g]=A;seen.add(g);q.append(g)
 charts=[]
 for f,A in align.items():
  ck(tuple(sorted(mv(A,v) for v in f))==face,'all actual normal rays align exactly')
  for owner in fixed[f]:charts.append(dict(owner=owner,rays=tuple(mv(A,v) for v in fan[owner]['rays']),alignment=A))
 generic=all(v[3]==0 for v in face)
 components.append(dict(face=face,dimension=4-len(face),generic=generic,charts=charts))

def residue_series(c,a):
 J=adj(c);w=mv(J,delta);v=mv(J,a);zeros=sum(x==0 for x in w)
 # Expand inverse product through the constant term after eps^-zeros.
 coeff=[F(1)]+[F(0)]*zeros
 for x,y in zip(w,v):
  if x==0:
   ck(y!=0,'auxiliary tangent weight nonzero')
   coeff=[z/F(y) for z in coeff]
  else:
   factor=[(-F(y,x))**j/F(x) for j in range(zeros+1)]
   coeff=[sum(coeff[k]*factor[j-k] for k in range(j+1)) for j in range(zeros+1)]
 q=[sum(x*x for x in w),2*sum(x*y for x,y in zip(w,v)),sum(y*y for y in v)]
 return {j-zeros:(-coeff[j],-sum(q[k]*coeff[j-k] for k in range(min(2,j)+1))) for j in range(zeros+1)}

corner=[];total=[F(0),F(0)];choices=[(1,11,103,1009),(2,17,89,701),(5,13,29,53),(7,31,113,809)]
for comp in components:
 if comp['generic']:continue
 n=len(comp['face']);charts=comp['charts']
 ck(any(v[2]>0 for v in comp['face']) and any(v[3]>0 for v in comp['face']),
    'both original endpoint base functions vanish on every corner component')
 geometry={};geometric_pair=None
 if n==4:ck(len(charts)==1,'compact isolated point has its one full chart')
 elif n==3:
  ck(len(charts)==2,'compact corner curve has its entire two-chart star')
  tang=[next(v for v in rec['rays'] if v not in comp['face']) for rec in charts]
  C=orient((*comp['face'],tang[0]));z=bary(C,tuple(-a-b for a,b in zip(*tang)))
  ck(z[C.index(tang[0])]==0,'both actual tangent rays are opposite modulo saturated normal lattice')
  degrees=[z[C.index(v)] for v in comp['face']];weights=[mv(adj(C),delta)[C.index(v)] for v in comp['face']]
  W=reduce(lambda a,b:a*b,weights,1);S=sum(F(d,w) for d,w in zip(degrees,weights));Q=sum(w*w for w in weights);T0=sum(w*d for w,d in zip(weights,degrees))
  geometric_pair=[S/W,(Q*S-2*T0)/W]
  geometry=dict(normal_degrees=degrees,physical_normal_weights=weights,full_tangent_relation=z,geometric_pair=geometric_pair)
 elif n==2:
  # The complete cyclic quotient fan is verified by its directed ray links.
  base=charts[0]['rays'];normal=[base.index(v) for v in comp['face']];tan=[i for i in range(4) if i not in normal]
  J=adj(base);edges=[];lifts={}
  for rec in charts:
   vv=[mv(J,v) for v in rec['rays'] if v not in comp['face']]
   pp=[tuple(v[i] for i in tan) for v in vv]
   for q,v in zip(pp,vv):
    if q in lifts:ck(lifts[q]==v,'actual full normal support lift agrees on repeated tangent ray')
    lifts[q]=v
   dd=pp[0][0]*pp[1][1]-pp[0][1]*pp[1][0]
   ck(abs(dd)==1,'complete corner surface quotient cone saturated and regular')
   if dd<0:pp.reverse()
   edges.append(tuple(pp))
  nxt={a:b for a,b in edges};ck(len(nxt)==len(edges),'corner surface each ray has one successor')
  start=next(iter(nxt));walk=[start]
  while nxt[walk[-1]]!=start:
   walk.append(nxt[walk[-1]]);ck(len(walk)<=len(nxt),'corner surface cyclic fan traversal terminates')
  ck(len(walk)==len(edges),'corner surface cycle visits the whole fan')
  def compare(a,b):
   half=lambda v:0 if v[1]>0 or (v[1]==0 and v[0]>0) else 1
   if half(a)!=half(b):return -1 if half(a)<half(b) else 1
   cr=a[0]*b[1]-a[1]*b[0]
   return -1 if cr>0 else 1 if cr<0 else 0
  rays=sorted(lifts,key=cmp_to_key(compare));nr=len(rays)
  ck(set(edges)==set(zip(rays,rays[1:]+rays[:1])),'angularly ordered quotient fan covers the plane exactly once')
  intersection=[[F(0) for j in range(nr)] for i in range(nr)]
  for i,r in enumerate(rays):
   left=rays[i-1];right=rays[(i+1)%nr]
   idx=0 if r[0] else 1;s=-F(left[idx]+right[idx],r[idx])
   ck(all(left[k]+right[k]+s*r[k]==0 for k in range(2)) and s.denominator==1,'full toric divisor wall equality')
   intersection[i][i]=s;intersection[i][(i-1)%nr]=1;intersection[i][(i+1)%nr]=1
  Ds=[[-lifts[r][k] for r in rays] for k in normal]
  pairing=lambda a,b:sum(a[i]*intersection[i][j]*b[j] for i in range(nr) for j in range(nr))
  xyz=[pairing(Ds[0],Ds[0]),pairing(Ds[0],Ds[1]),pairing(Ds[1],Ds[1])]
  p1=pairing([1]*nr,[1]*nr)-2*nr
  ck(p1==12-3*nr,'actual cyclic divisor matrix gives toric tangent p1')
  aa,bb=[mv(J,delta)[k] for k in normal];xx,yy,zz=xyz
  B2=xx/F(aa*aa)+yy/F(aa*bb)+zz/F(bb*bb)
  geometric_pair=[-B2/F(aa*bb),-(p1-xx-zz-2*(F(aa,bb)+F(bb,aa))*yy+(aa*aa+bb*bb)*B2)/F(aa*bb)]
  geometry=dict(quotient_rays=rays,normal_support_divisors=Ds,divisor_intersection_matrix=intersection,normal_intersections=xyz,tangent_p1=p1,physical_normal_weights=[aa,bb],geometric_pair=geometric_pair)
 else:raise AssertionError('new fixed dimension needs explicit completion')
 answers=[]
 for a in choices:
  if any(any(w==0 and v==0 for w,v in zip(mv(adj(rec['rays']),delta),mv(adj(rec['rays']),a))) for rec in charts):continue
  sums=defaultdict(lambda:[F(0),F(0)])
  for rec in charts:
   for power,pair in residue_series(rec['rays'],a).items():
    for k in range(2):sums[power][k]+=pair[k]
  ck(all(pair==[0,0] for power,pair in sums.items() if power<0),'whole compact-star equivariant poles cancel')
  answers.append(sums[0])
  if len(answers)==2:break
 ck(len(answers)==2 and answers[0]==answers[1],'two original-lattice auxiliary cocharacters agree on compact residue')
 pair=answers[0]
 if geometric_pair is not None:ck(pair==geometric_pair,'complete divisor/wall route agrees with auxiliary localization')
 for k in range(2):total[k]+=pair[k]
 corner.append(dict(comp,pair=pair,geometry=geometry))

out=dict(scope='Complete fresh infinity endpoint over the original raw cell, with full1926-cone common boundary, lower quotient subdivisions, all period/source/point maps and complete aligned corner fixed stars. Its compact residue is computed only on those verified complete stars. This remains part of the new auxiliary construction; the fresh zero endpoint and full generic compact ledger remain separate.',
         checks=checks,cones=fan,stellar_history=history,boundary_facets={str(k):len(v) for k,v in boundary.items()},internal_facets=sum(len(v)==2 for v in incidence.values()),period_maps=maps,
         corner_components=corner,corner_counts=dict(Counter(x['dimension'] for x in corner)),compact_pair=total,
         source_functions={'x':'R^3*u^2*Z','y':'Z^-1','product':'Q=R^3*u^2'},
         original_point_module={'forward':'v2=eta*(R*u)^2*X*Z/f_{(R*u)^2}(R^3*u^2*Z)','inverse':'X=eta^-1*(R*u)^-2*Z^-1*f_{(R*u)^2}(R^3*u^2*Z)*v2','point_graph':'Bl_(R^3*u^2*Z,(R*u)^2)'},
         original_volume='+(2*J_ts/a_T)*R*dR wedge du wedge dlogX wedge dlogZ')
(root/'K111_new_infinity_endpoint.json').write_text(json.dumps(serial(out),indent=2)+'\n')
print(json.dumps(dict(checks=checks,full_cones=len(fan),lower_cones=len(lower),stellar_insertions=len(history),boundary_facets=out['boundary_facets'],internal_facets=out['internal_facets'],period_maps=len(maps),corner_counts=out['corner_counts'],compact_pair=serial(total)),indent=2))
