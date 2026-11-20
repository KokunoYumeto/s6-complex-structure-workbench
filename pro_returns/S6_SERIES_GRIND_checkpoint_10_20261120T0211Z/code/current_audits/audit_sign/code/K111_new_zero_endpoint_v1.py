"""Fresh zero endpoint, with exact source bands and periodic completion.

This uses the freshly constructed common fan and the original convex
zero cell and lower rays. Every mutation is an actual stellar morphism.
The generic boundary remains protected throughout the source cuts.
"""
from pathlib import Path
from collections import defaultdict,deque
from fractions import Fraction as F
from itertools import combinations
from math import gcd,ceil,floor
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
A=(0,0,0,1);B1=(-1,0,0,1);B2=(-2,-1,0,1);B3=(-1,-1,0,1)
U3=(-13,-6,1,0);delta=(-1,0,0,0)
def ell(v):return v[1]+3*v[2]+v[3]
fan={};byray=defaultdict(set);nextid=0;history=[]
def put(rec):
 global nextid
 k=nextid;nextid+=1;fan[k]=rec
 for v in rec['rays']:byray[v].add(k)
 return k
def remove(k):
 rec=fan.pop(k)
 for v in rec['rays']:
  byray[v].remove(k)
  if not byray[v]:del byray[v]
 return rec
def incident(support):
 if any(v not in byray for v in support):return set()
 return set.intersection(*(byray[v] for v in support))
def star(v,support,kind):
 owners=incident(support);ck(bool(owners),'actual stellar centre has its whole incident star')
 ck(v not in byray,'new ray is not already a fan vertex')
 changes=[];newids=[]
 for k in sorted(owners):
  rec=remove(k);c=rec['rays'];bb=bary(c,v)
  ck(min(bb)>=0 and {c[i] for i,x in enumerate(bb) if x>0}==set(support),'whole containing star has exact positive support')
  children=[]
  for i,x in enumerate(bb):
   if not x:continue
   cc=list(c);cc[i]=v;cc=tuple(cc)
   ck(det(cc)>0,'stellar child orientation remains positive')
   children.append(cc);newids.append(put(dict(rec,rays=cc)))
  changes.append(dict(parent=c,barycentric=bb,children=children))
 history.append(dict(kind=kind,ray=v,support=support,changes=changes))
 return newids
def ordinary_target(v,kind):
 if v in byray:return []
 owner=None
 for k,rec in fan.items():
  bb=bary(rec['rays'],v)
  if min(bb)>=0:owner=k;break
 ck(owner is not None,'desired exact period/overlay ray belongs to the actual support')
 created=[]
 while v not in byray:
  c=fan[owner]['rays'];bb=bary(c,v)
  ck(all(x.denominator==1 and x>=0 for x in bb),'desired ray has integral nonnegative coordinates in regular owner')
  support=tuple(c[i] for i,x in enumerate(bb) if x>0)
  w=tuple(sum(q[j] for q in support) for j in range(4))
  oldsum=sum(bb);children=star(w,support,kind);created.append(w)
  if w==v:break
  owner=next(k for k in children if min(bary(fan[k]['rays'],v))>=0)
  ck(sum(bary(fan[owner]['rays'],v))<oldsum,'ordinary coordinate blowups strictly decrease desired coefficient sum')
 return created

upper=[]
for k,rec in enumerate(src['cones']):
 i,j=rec['zero_word'];vv=[(-a-b+(26*i+14*j)*h,b-3*(i+j)*h,h,0) for a,b,h in rec['rays']]
 c=orient((*vv,A));ck(det(c)==1,'actual zero upper pullback is regular in original lattice')
 ck(min(ell(v) for v in vv)>=0 or max(ell(v) for v in vv)<=0,'complete generic cone already obeys its source band')
 upper.append(tuple(vv));put(dict(rays=c,kind='upper',generic_owner=k,zero_word=[i,j]))
edgecounts=defaultdict(int)
for c in upper:
 for edge in combinations(c,2):edgecounts[tuple(sorted(edge))]+=1
edges=[e for e,n in edgecounts.items() if n==1]
sideforms=[lambda v:3*v[0]-5*v[1]+15*v[2],lambda v:v[0]-v[1]+7*v[2],
           lambda v:v[1]+6*v[2],lambda v:3*v[0]-5*v[1]-6*v[2]]
lower_raw=[]
for side,f in enumerate(sideforms):
 for e in edges:
  if all(f(v)==0 for v in e):lower_raw.append(orient((A,B1 if side<2 else B3,*e)))
lower_raw.extend([orient((A,B1,U3,B2)),orient((A,B3,U3,B2))])
for c in lower_raw:put(dict(rays=c,kind='lower',raw_parent=c))
ck(sum(volume(x['rays']) for x in fan.values())==F(29,2),'full original zero-cell slice volume before resolution')
def quotient(c):
 d=det(c);J=adj(c);zero=(0,0,0,0);seen={zero};q=deque([zero])
 gens=[tuple(J[i][j]%d for i in range(4)) for j in range(4)]
 while q:
  a=q.popleft()
  for b in gens:
   z=tuple((x+y)%d for x,y in zip(a,b))
   if z not in seen:seen.add(z);q.append(z)
 ck(len(seen)==d,'whole original lower quotient enumerated')
 rays=[]
 for a in seen-{zero}:
  w=[sum(c[i][k]*a[i] for i in range(4)) for k in range(4)]
  ck(all(x%d==0 for x in w),'entire quotient vector is integral')
  rays.append(prim(tuple(x//d for x in w)))
 return min(set(rays),key=lambda v:(v[2]+v[3],v[2],sum(map(abs,v)),v))
while True:
 bad=next((rec for rec in fan.values() if det(rec['rays'])>1),None)
 if bad is None:break
 c=bad['rays'];v=quotient(c);bb=bary(c,v);support=tuple(c[i] for i,x in enumerate(bb) if x>0)
 ck(v[3]>0,'quotient regularization protects the complete generic fan')
 olddet={k:det(fan[k]['rays']) for k in incident(support)}
 children=star(v,support,'original-lattice quotient regularization')
 for change in history[-1]['changes']:
  ck(all(det(cc)<det(change['parent']) for cc in change['children']),'strict determinant decrease on the whole singular incident star')

# Every crossing edge is an actual ordinary two-coordinate blowup.
queue=deque();queued=set()
def add_cross(c):
 for a,b in combinations(c,2):
  if ell(a)*ell(b)<0:
   e=tuple(sorted((a,b)))
   if e not in queued:queued.add(e);queue.append(e)
for rec in fan.values():add_cross(rec['rays'])
source_steps=0
while queue:
 e=queue.popleft();queued.remove(e)
 if not incident(e):continue
 a,b=e;v=tuple(x+y for x,y in zip(a,b))
 children=star(v,e,'ordinary source-band edge blowup');source_steps+=1
 ck(v[3]>0,'source-band cut retains the whole generic boundary')
 for k in children:
  ck(det(fan[k]['rays'])==1,'ordinary source cut stays regular')
  add_cross(fan[k]['rays'])
 if source_steps%500==0:print('source stars',source_steps,'cones',len(fan),'crossing queue',len(queue),flush=True)
ck(all(min(map(ell,x['rays']))>=0 or max(map(ell,x['rays']))<=0 for x in fan.values()),'entire new zero fan lies in its actual source bands')
print('source-compatible cones',len(fan),'source stars',source_steps,flush=True)

HL=((1,0,10,1),(0,1,3,0),(0,0,1,0),(0,0,0,1))
HT=((1,0,8,1),(0,1,6,1),(0,0,1,0),(0,0,0,1))
HLi=((1,0,-10,-1),(0,1,-3,0),(0,0,1,0),(0,0,0,1))
HTi=((1,0,-8,-1),(0,1,-6,-1),(0,0,1,0),(0,0,0,1))
HLT=mm(HL,HTi);HLTi=mm(HT,HLi)
forms=[lambda v:v[3],lambda v:v[2],lambda v:v[0]-v[1]+7*v[2]+v[3],lambda v:v[0]-v[1],
       lambda v:v[1]+6*v[2]+v[3],lambda v:v[1],lambda v:3*v[0]-5*v[1]+15*v[2]+3*v[3],lambda v:3*v[0]-5*v[1]-6*v[2]-2*v[3]]
def periodic_copies(v):
 x,y,r,z=v;N=((10*r+z,8*r+z),(3*r,6*r+z));d=N[0][0]*N[1][1]-N[0][1]*N[1][0]
 ck(d>0,'original zero period lattice has full rank at every nonzero base ray')
 verts=[(0,0),(-5*r-z,0),(-10*r-z,-3*r),(-13*r-2*z,-6*r-z),(-8*r-z,-6*r-z),(-3*r-z,-3*r-z)]
 def coord(p):return (F(N[1][1]*p[0]-N[0][1]*p[1],d),F(-N[1][0]*p[0]+N[0][0]*p[1],d))
 vv=list(map(coord,verts));a=coord((x,y));out=[]
 ranges=[range(ceil(min(q[k] for q in vv)-a[k]),floor(max(q[k] for q in vv)-a[k])+1) for k in range(2)]
 for i in ranges[0]:
  for j in ranges[1]:
   w=(x+N[0][0]*i+N[0][1]*j,y+N[1][0]*i+N[1][1]*j,r,z)
   if forms[2](w)>=0 and forms[3](w)<=0 and forms[4](w)>=0 and forms[5](w)<=0 and forms[6](w)>=0 and forms[7](w)<=0:out.append(w)
 return sorted(set(out))
def is_period_boundary(v):return any(f(v)==0 for f in forms[2:])
def close_ray_orbits():
 todo=deque(v for v in byray if is_period_boundary(v));done=set();n=0
 while todo:
  v=todo.popleft()
  if v in done:continue
  done.add(v)
  for w in periodic_copies(v):
   created=ordinary_target(w,'ordinary full-period ray completion')
   n+=len(created)
   for q in created:
    ck(q[3]>0,'period completion leaves original generic triangulation intact')
    if is_period_boundary(q):todo.append(q)
 return n
def boundary_inventory():
 inc=defaultdict(list);bnd=defaultdict(list)
 for k,rec in fan.items():
  for f in facets(rec['rays']):inc[f].append(k)
 for f,owners in inc.items():
  ck(len(owners) in [1,2],'whole zero facet incidence is one or two')
  if len(owners)==2:continue
  hits=[k for k,g in enumerate(forms) if all(g(v)==0 for v in f)]
  ck(len(hits)==1,'every zero boundary facet has its unique prescribed type')
  bnd[hits[0]].append(f)
 return inc,bnd
def point(v,which):
 x,y,r,z=v;s=r+z
 return (F(x if which==4 else y,s),F(r,s))
def unpoint(p,which):
 a,r=p;z=1-r
 if which==2:x,y=a-7*r-z,a
 elif which==4:x,y=a,-6*r-z
 else:x,y=(5*a-15*r-3*z)/3,a
 q=(x,y,r,z);den=1
 for t in q:den=den*t.denominator//gcd(den,t.denominator)
 return prim(tuple(int(t*den) for t in q))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def intersections(source,target,which):
 es={tuple(sorted((point(a,which),point(b,which)))) for f in source for a,b in combinations(f,2)}
 et={tuple(sorted((point(a,which),point(b,which)))) for f in target for a,b in combinations(f,2)}
 new=set()
 for a,b in es:
  for c,d in et:
   u=sub(b,a);v=sub(d,c);dd=cross(u,v)
   if not dd:continue
   t=cross(sub(c,a),v)/dd;s=cross(sub(c,a),u)/dd
   if 0<=t<=1 and 0<=s<=1:
    p=(a[0]+t*u[0],a[1]+t*u[1]);w=unpoint(p,which)
    if w not in byray:new.add(w)
 return new
rounds=[]
for roundno in range(12):
 orbitstars=close_ray_orbits();inc,bnd=boundary_inventory();new=set();mismatched=[]
 for sf,tf,H,Hi in [(2,3,HL,HLi),(4,5,HT,HTi),(6,7,HLT,HLTi)]:
  target=[tuple(sorted(mv(Hi,v) for v in f)) for f in bnd[tf]]
  if set(bnd[sf])!=set(target):
   mismatched.append(sf);new.update(intersections(bnd[sf],target,sf))
 rounds.append(dict(round=roundno,period_stars=orbitstars,mismatched_facets=mismatched,new_intersection_rays=sorted(new)))
 print('period overlay round',roundno,'cones',len(fan),'orbit stars',orbitstars,'mismatch',mismatched,'intersection rays',len(new),flush=True)
 if not mismatched:break
 ck(bool(new),'every unmatched triangulation has an actual new crossing ray')
 for v in sorted(new):ordinary_target(v,'ordinary exact period-facet edge overlay')
else:raise AssertionError('period completion did not close in recorded finite execution')

ck(len(bnd[0])==len(src['cones']),'whole protected generic common fan remains exact')
ck(len(bnd[1])==2,'both original lower facets retained')
ck(sum(volume(x['rays']) for x in fan.values())==F(29,2),'complete final zero support volume')
maps=[]
for sf,tf,H,Hi,u,name in [(2,3,HL,HLi,(1,0,0,0),'L0'),(4,5,HT,HTi,(1,0,0,0),'T0'),(6,7,HLT,HLTi,(0,0,0,0),'L0/T0')]:
 ck({tuple(sorted(mv(H,v) for v in f)) for f in bnd[sf]}==set(bnd[tf]),'entire zero period facet pairing')
 for face in bnd[sf]:
  target=tuple(sorted(mv(H,v) for v in face));si=inc[face][0];ti=inc[target][0]
  cs=fan[si]['rays'];ct=fan[ti]['rays'];Js=adj(cs);Jt=adj(ct)
  E=mm(mm(Jt,H),matrix(cs));Ei=mm(mm(Js,Hi),matrix(ct));fwd=mv(Jt,u);back=tuple(-x for x in mv(mm(Js,Hi),u))
  ck(mm(E,Ei)==I,'complete period chart matrices reciprocal')
  ck(tuple(x+y for x,y in zip(mv(Ei,fwd),back))==(0,0,0,0),'entire f0 column and inverse cancel')
  for v in face:
   a=cs.index(v);b=ct.index(mv(H,v));ck(tuple(E[k][a] for k in range(4))==tuple(int(k==b) for k in range(4)),'full localized period map on each vanishing coordinate')
  maps.append(dict(name=name,source_face=face,target_face=target,source_chart=si,target_chart=ti,lattice_matrix=H,inverse_lattice_matrix=Hi,matrix=E,inverse=Ei,full_f0_unit=fwd,inverse_f0_unit=back))
for k,rec in fan.items():
 c=rec['rays'];ck(det(c)==1,'every completed zero cone regular')
 j=1 if min(map(ell,c))>=0 else 2
 ck(j==1 or max(map(ell,c))<=0,'whole completed zero chart retains one actual source band')
 rows=[[v[1]+3*j*v[2]+j*v[3] for v in c],[-v[1]+3*(1-j)*v[2]+(1-j)*v[3] for v in c]]
 ck(all(x>=0 for row in rows for x in row),'actual original node source rows nonnegative')
 rec.update(id=k,inverse=adj(c),physical_weights=mv(adj(c),delta),source_band=j,source_rows=rows,canonical_orders=[2*v[2]+v[3]-1 for v in c])
out=dict(scope='Complete freshly constructed zero-end fan with exact1926-cone generic boundary, full original convex-cell support, both actual source bands, entire period facet gluing and all reciprocal source/point functions. Whole fixed-stratum and marked completed-family calculations are subsequent scopes.',
         checks=checks,cones=list(fan.values()),stellar_history=history,source_stars=source_steps,period_overlay_rounds=rounds,boundary_facets={str(k):len(v) for k,v in bnd.items()},internal_facets=sum(len(v)==2 for v in inc.values()),period_maps=maps,
         original_source={'s':'P*(p-1)/u_s','t':'P*u_t','Q':'P^3*p','x_j':'Q^j*Y0','y_j':'Q^(1-j)/Y0'},
         original_point_module={'forward':'v2=eta*P^(2*j)/(X0*f_{P^2}(Q^j*Y0))','inverse':'X0=eta*P^(2*j)/(v2*f_{P^2}(Q^j*Y0))','graph':'Bl_(Q^j*Y0,P^2)','point_generators':['(a-1)^-1','(c-1)^-1'],'zero_generator':'x_j-1','full_coefficients':['Vreg=-eta^-1*P^(-2*j)*E*A','Vreg=eta^-1*P^(-2*j)*c^-1*E*C','C=-c*A','Vreg=eta^-1*P^(-2*j-2)*(x_j-P^2)*E_O*C_O']},
         original_volume='+(2*J_ts/a_T)*P*dP wedge dp wedge dlogX0 wedge dlogY0')
(root/'K111_new_zero_endpoint.json').write_text(json.dumps(serial(out),indent=2)+'\n')
print(json.dumps(dict(checks=checks,full_cones=len(fan),source_stars=source_steps,all_stellar_steps=len(history),boundary_facets=out['boundary_facets'],period_maps=len(maps)),indent=2))
