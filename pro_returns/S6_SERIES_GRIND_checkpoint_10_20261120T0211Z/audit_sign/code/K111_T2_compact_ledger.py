"""Physical-component-by-component T2 localization on the fresh K111 atlas.

Physical delta-fixed ownership is determined first from complete normal
faces and actual periods. Only then is the second action localized inside
each compact physical component. Every epsilon pole must cancel per owner.
"""
from pathlib import Path
from collections import defaultdict,deque,Counter
from fractions import Fraction as F
from functools import cmp_to_key
from math import comb
import json,gc
from K111_fan4_exact import *

root=Path(__file__).resolve().parents[1]
checks=0
def ck(x,m):
 global checks
 checks+=1
 if not x:raise AssertionError(m)
I=tuple(tuple(int(i==j) for j in range(4)) for i in range(4))
def cross3(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def adj3(c):return(cross3(c[1],c[2]),cross3(c[2],c[0]),cross3(c[0],c[1]))
common=json.loads((root/'K111_new_regular_common_fan.json').read_text())
common.pop('stellar_history',None);common.pop('parent_maps',None)
cones3=[tuple(tuple(v) for v in c['rays']) for c in common['cones']]
J3=[adj3(c) for c in cones3]
gpfaces=defaultdict(list)
for k,c in enumerate(cones3):
 ck(det3(*c)==1,'common chart ordered original-lattice determinant')
 face=tuple(sorted(v for v,row in zip(c,J3[k]) if row[0]));gpfaces[face].append(k)
ggraph=defaultdict(list)
for source,target,shift in [(1,0,(11,3)),(3,2,(12,0))]:
 for edge in common['boundary_edges'][source]:
  f=tuple(sorted(tuple(v) for v in edge))
  if f in gpfaces:
   g=tuple(sorted((a+shift[0]*h,b+shift[1]*h,h) for a,b,h in f))
   ck(g in gpfaces,'generic physical face has its whole actual period partner')
   ggraph[f].append(g);ggraph[g].append(f)
generic=[];face_owner={};common_owner={}
for f in gpfaces:
 if f in face_owner:continue
 owner='generic:'+str(len(generic));todo=[f];keys=[];ids=[];face_owner[f]=owner
 while todo:
  a=todo.pop();keys.append(a);ids.extend(gpfaces[a])
  for b in ggraph[a]:
   if b not in face_owner:face_owner[b]=owner;todo.append(b)
 ck(len(ids)==(1 if len(f)==3 else 2),'complete generic physical component has its full one- or two-chart star')
 for k in ids:common_owner[k]=owner
 generic.append(dict(owner=owner,dimension=4-len(f),faces=keys,common_charts=ids))

native_lookup={};native_generic_cone={}
for end in ['zero','one','infinity']:
 look={};look3={}
 for k,c in enumerate(cones3):
  rec=common['cones'][k]
  if end=='zero':
   i,j=rec['zero_word'];n=[(-a-b+(26*i+14*j)*h,b-3*(i+j)*h,h,0) for a,b,h in c]
  elif end=='one':
   i,j=rec['one_word'];n=[(-b+3*(i+j)*h,a-(23*i+11*j)*h,h,0) for a,b,h in c]
  else:n=[(*v,0) for v in c]
  f=tuple(sorted(v for v,row in zip(n,J3[k]) if row[0]));g=tuple(sorted(n))
  if f in look:ck(look[f]==common_owner[k],'all native generic face owners agree')
  look[f]=common_owner[k]
  ck(g not in look3,'full native generic three-cone has one actual common owner')
  look3[g]=k
 native_lookup[end]=look;native_generic_cone[end]=look3

def inverse_unimod(c):
 d=det(c);ck(abs(d)==1,'aligned full original-lattice chart is unimodular')
 return tuple(tuple(x//d for x in row) for row in adj(c))
def angular(a,b):
 half=lambda v:0 if v[1]>0 or (v[1]==0 and v[0]>0) else 1
 if half(a)!=half(b):return -1 if half(a)<half(b) else 1
 cr=a[0]*b[1]-a[1]*b[0]
 return -1 if cr>0 else 1 if cr<0 else 0
def orbit_faces(faces,graph,allow_lower_stabilizer=False):
 seen=set();out=[]
 for face in faces:
  if face in seen:continue
  align={face:I};seen.add(face);todo=deque([face]);loops=[]
  while todo:
   f=todo.popleft()
   for g,H,Hi in graph[f]:
    A=mm(align[f],Hi)
    if g in align:
     if align[g]!=A:
      ck(allow_lower_stabilizer and all(v[2]==0 for v in face),'only the prescribed pure-lower physical star has a period stabilizer')
      loops.append(dict(face=f,matrix=mm(A,matrix(tuple(zip(*align[g])))) if False else A))
    else:align[g]=A;seen.add(g);todo.append(g)
  ids=[]
  for f,A in align.items():
   ck(tuple(sorted(mv(A,v) for v in f))==face,'whole fixed-component normal face aligns by the actual period matrix')
   ids.extend((k,A) for k in faces[f])
  out.append(dict(face=face,align=align,ids=ids,stabilizers=loops))
 return out

owners={x['owner']:dict(x,kind='compact generic',endpoints={}) for x in generic}
enddata={};corner_pieces=[];excluded=[];clutches=defaultdict(dict)
for end,filename,delta,aux in [
 ('zero','K111_new_zero_endpoint_v2.json',(-1,0,0,0),(-1,1,0,0)),
 ('one','K111_new_one_endpoint.json',(0,1,0,0),(-1,0,0,0)),
 ('infinity','K111_new_infinity_endpoint.json',(1,0,0,0),(0,1,0,0))]:
 d=json.loads((root/filename).read_text());d.pop('stellar_history',None);d.pop('corner_components',None);d.pop('compact_corner_points',None);gc.collect()
 fan={rec.get('id',k):rec for k,rec in enumerate(d['cones'])}
 pf=defaultdict(list);tf=defaultdict(list);pkey={};tkey={}
 for k,rec in fan.items():
  c=tuple(tuple(v) for v in rec['rays']);rec['rays']=c;J=tuple(tuple(v) for v in rec['inverse']);rec['inverse']=J
  w=mv(J,delta);a=mv(J,aux);rec['w']=w;rec['a']=a
  p=tuple(sorted(v for v,x in zip(c,w) if x));t=tuple(sorted(v for v,x,y in zip(c,w,a) if x or y))
  ck(len(t)>=3,'no two positive-total-height rays span the original two-torus plane')
  pkey[k]=p;tkey[k]=t;pf[p].append(k);tf[t].append(k)
 pg=defaultdict(list);tg=defaultdict(list)
 for m in d['period_maps']:
  s=m['source_chart'];t=m['target_chart'];face=tuple(tuple(v) for v in m['source_face'])
  if end=='zero':H=tuple(tuple(v) for v in m['lattice_matrix']);Hi=tuple(tuple(v) for v in m['inverse_lattice_matrix'])
  elif end=='one':
   if all(v[0]==0 for v in face):H=((1,0,3,0),(0,1,1,0),(0,0,1,0),(0,0,0,1));Hi=((1,0,-3,0),(0,1,-1,0),(0,0,1,0),(0,0,0,1))
   else:H=((1,0,0,0),(0,1,12,12),(0,0,1,0),(0,0,0,1));Hi=((1,0,0,0),(0,1,-12,-12),(0,0,1,0),(0,0,0,1))
  else:
   shifts={'L':(23,3,0),'T':(11,3,1),'L/T':(12,0,-1)};x,y,z=shifts[m['name']]
   H=((1,0,x,0),(0,1,y,z),(0,0,1,0),(0,0,0,1));Hi=((1,0,-x,0),(0,1,-y,-z),(0,0,1,0),(0,0,0,1))
  ck(mv(H,delta)==delta and mv(H,aux)==aux,'both original torus cocharacters fixed by the full period lattice map')
  for keys,graph in [(pkey,pg),(tkey,tg)]:
   f=keys[s]
   if set(f)<=set(face):
    g=tuple(sorted(mv(H,v) for v in f));ck(g==keys[t],'complete fixed face matches the actual target chart')
    graph[f].append((g,H,Hi));graph[g].append((f,Hi,H))
 phys=orbit_faces(pf,pg,True);chart_owner={};local_counts=Counter()
 for num,comp in enumerate(phys):
  face=comp['face'];ids=comp['ids'];dim=4-len(face)
  if all(v[3]==0 for v in face):
   gg={native_lookup[end][f] for f in comp['align']};ck(len(gg)==1,'entire endpoint generic physical star has one completed generic owner');owner=gg.pop();kind='compact generic'
  elif all(v[2]==0 for v in face):
   if end=='zero':
    allowed={tuple(sorted(((0,0,0,1),(-1,0,0,1)))),tuple(sorted(((-2,-1,0,1),(-1,-1,0,1))))}
    ck(set(comp['align'])<=allowed,'actual moving lower component has precisely its named zero-end normal faces')
   elif end=='one':
    allowed={tuple(sorted(((0,l,0,1),(0,l+1,0,1)))) for l in range(12)}
    ck(set(comp['align'])<=allowed,'actual one-end lower component has its named E_l face')
   else:raise AssertionError('unexpected infinity physical lower face')
   owner=end+':lower:'+str(num);kind='noncompact lower'
   owners[owner]=dict(owner=owner,kind=kind,dimension=dim,faces=list(comp['align']),stabilizers=comp['stabilizers'])
  else:
   owner=end+':corner:'+str(num);kind='compact corner';owners[owner]=dict(owner=owner,kind=kind,dimension=dim,faces=list(comp['align']))
  local_counts[kind]+=1
  for k,A in ids:
   ck(k not in chart_owner,'every endpoint chart receives one physical owner before localization');chart_owner[k]=owner
  if kind=='noncompact lower':continue
  ck(not comp['stabilizers'],'complete compact physical star has trivial period stabilizer')
  aligned=[tuple(mv(A,v) for v in fan[k]['rays']) for k,A in ids]
  if kind=='compact corner':ck(any(v[2]>0 for v in face) and any(v[3]>0 for v in face),'both base functions vanish on the compact corner physical component')
  if dim==0:ck(len(aligned)==1,'compact physical isolated point has one full chart')
  elif dim==1:
   if kind=='compact generic':ck(len(aligned)==1,'generic physical curve has exactly one endpoint-disc chart')
   else:
    ck(len(aligned)==2,'compact physical corner curve has its whole two-chart star')
    tang=[next(v for v in c if v not in face) for c in aligned];C=(*face,tang[0]);J=inverse_unimod(C);z=mv(J,tuple(-a-b for a,b in zip(*tang)))
    ck(z[3]==0,'compact physical curve tangent rays are opposite primitive quotient rays')
  elif dim==2:
   if kind=='compact generic':
    base=next(c for c in aligned if sum(v[3]==0 for v in c)==3)
    tangent=sorted((v for v in base if v not in face),key=lambda v:v[3])
    ck(tangent[0][3]==0 and tangent[1][3]==1,'actual endpoint surface has one marked section ray and base multiplicity one')
   else:base=aligned[0];tangent=[v for v in base if v not in face]
   C=(*face,*tangent);J=inverse_unimod(C);edges=set();rays=set()
   for c in aligned:
    pp=[tuple(mv(J,v)[2:]) for v in c if v not in face]
    dd=pp[0][0]*pp[1][1]-pp[0][1]*pp[1][0];ck(abs(dd)==1,'whole physical surface quotient fan saturated and regular')
    if dd<0:pp.reverse()
    ck(tuple(pp) not in edges,'no repeated projected physical surface chart')
    edges.add(tuple(pp));rays.update(pp)
   ordered=sorted(rays,key=cmp_to_key(angular))
   if kind=='compact generic':
    ck(all(v[1]>=0 for v in rays),'entire generic surface endpoint fan lies in the actual base half-plane')
    ck(ordered[0]==(1,0) and ordered[-1]==(-1,0),'the two original section rays close the actual endpoint half-plane')
    expected=set(zip(ordered,ordered[1:]))
   else:expected=set(zip(ordered,ordered[1:]+ordered[:1]))
   ck(edges==expected,'full physical surface star covers its plane or marked half-plane exactly once')
   owners[owner].setdefault('endpoint_fan_counts',{})[end]=dict(charts=len(aligned),rays=len(rays),kind='half-plane' if kind=='compact generic' else 'complete plane')
  else:raise AssertionError('unexpected physical fixed dimension')
  if kind=='compact generic':owners[owner]['endpoints'][end]=dict(charts=len(ids),normal_faces=len(comp['align']))

 ck(len(chart_owner)==len(fan),'complete physical ownership exhausts every endpoint chart')
 tcomps=orbit_faces(tf,tg)
 for comp in tcomps:
  face=comp['face'];ids=comp['ids'];gg={chart_owner[k] for k,A in ids}
  ck(len(gg)==1,'whole second-fixed piece lies in its single already established physical component');owner=gg.pop()
  if all(v[3]==0 for v in face):
   gg={native_generic_cone[end][f] for f in comp['align']};ck(len(gg)==1 and len(ids)==1,'generic T2 curve has exactly one full endpoint owner');g=gg.pop();k,Aalign=ids[0];B=fan[k]['rays'];lo=next(v for v in B if v[3]>0)
   ck(lo[3]==1,'generic curve transverse base multiplicity exactly one')
   rec=common['cones'][g]
   if end=='zero':
    i,j=rec['zero_word'];Fe=((-1,-1,23*i+11*j,-i-j),(0,1,3*i+3*j,3*i+2*j),(0,0,1,0));units={'f0':[2*i+j,0,0]}
   elif end=='one':
    i,j=rec['one_word'];Fe=((0,1,23*i+11*j,12*(2*i+j)),(-1,0,3*i+3*j,0),(0,0,1,0));units={'p':[-i-j,3*i+2*j,0],'c12':[2*i+j,0,0]}
   else:Fe=((1,0,0,0),(0,1,0,0),(0,0,1,1));units={'P=R*u':'full equality'}
   ck(mv(Fe,delta)==(1,0,0) and mv(Fe,aux)==(0,1,0),'actual endpoint character arrow carries both torus cocharacters')
   cc=mv(J3[g],mv(Fe,lo));columns=[mv(J3[g],mv(Fe,v)) for v in B if v[3]==0]
   ck(set(columns)=={(1,0,0),(0,1,0),(0,0,1)},'generic normal coefficient columns are the actual permutation')
   clutches[g][end]=dict(chart=k,transverse_ray=lo,character_matrix=Fe,coefficient_orders=cc,full_units=units,native_height=lo[2],physical_owner=owner)
   continue
  if owners[owner]['kind']=='noncompact lower':
   excluded.append(dict(endpoint=end,normal_face=face,physical_owner=owner,chart_ids=[k for k,A in ids],reason='already assigned to the prescribed noncompact physical lower component'))
   continue
  ck(not comp['stabilizers'],'compact second-fixed star has trivial full period cycle')
  aligned=[tuple(mv(A,v) for v in fan[k]['rays']) for k,A in ids]
  if len(face)==4:
   ck(len(aligned)==1,'compact T2 point has its complete single chart');J=inverse_unimod(aligned[0]);weights=mv(J,delta);auxweights=mv(J,aux);degrees=None
  else:
   ck(len(face)==3 and len(aligned)==2,'compact T2 curve has its complete two-chart star')
   tang=[next(v for v in c if v not in face) for c in aligned];C=(*face,tang[0]);J=inverse_unimod(C);relation=mv(J,tuple(-a-b for a,b in zip(*tang)))
   ck(relation[3]==0,'T2 curve has opposite saturated tangent quotient rays')
   weights=mv(J,delta)[:3];auxweights=mv(J,aux)[:3];degrees=relation[:3]
  corner_pieces.append(dict(endpoint=end,physical_owner=owner,normal_face=face,chart_ids=[k for k,A in ids],physical_weights=weights,second_weights=auxweights,degrees=degrees))
 enddata[end]=dict(full_charts=len(fan),physical_components=dict(local_counts),two_torus_components=len(tcomps))
 print('owned endpoint',end,'charts',len(fan),'physical',dict(local_counts),'T2',len(tcomps),'checks',checks,flush=True)
 del d,fan,phys,tcomps;gc.collect()

generic_curves=[]
for g,c in enumerate(cones3):
 ck(set(clutches[g])=={'zero','one','infinity'},'every actual generic T2 curve has all three endpoint restrictions')
 deg=tuple(-sum(clutches[g][e]['coefficient_orders'][i] for e in clutches[g]) for i in range(3))
 ck(sum(v[2]*d for v,d in zip(c,deg))+sum(x['native_height'] for x in clutches[g].values())==-1,'full original-height adjunction identity including infinity P=Ru')
 generic_curves.append(dict(common_cone=g,physical_owner=common_owner[g],physical_weights=tuple(r[0] for r in J3[g]),second_weights=tuple(r[1] for r in J3[g]),degrees=deg,clutches=clutches[g]))

def invseries(weights,mult):
 z=sum(n for (w,a),n in zip(weights,mult) if w==0);out=[F(1)]+[F(0)]*z
 for (w,a),n in zip(weights,mult):
  if not n:continue
  if w==0:
   ck(a!=0,'every second normal character is nonzero when its physical weight vanishes')
   out=[x/F(a**n) for x in out]
  else:
   factor=[F((-1)**j*comb(n+j-1,j)*a**j,w**(n+j)) for j in range(z+1)]
   out=[sum(out[k]*factor[j-k] for k in range(j+1)) for j in range(z+1)]
 return {j-z:x for j,x in enumerate(out)}
def addpoly(out,series,poly,scale=1):
 for p,x in series.items():
  for j,y in enumerate(poly):
   if p+j<=0:out[p+j]+=scale*x*y
def mulpoly(a,b):return [sum(a[k]*b[j-k] for k in range(max(0,j-len(b)+1),min(j+1,len(a)))) for j in range(len(a)+len(b)-1)]
def contribution(rec,s,t):
 w=rec['physical_weights'];a=rec['second_weights'];wa=[(x,s*x+t*y) for x,y in zip(w,a)];n=len(w)
 u=[1,s];u3=[1,3*s,3*s*s,s*s*s];Q=[sum(x*x for x,y in wa),2*sum(x*y for x,y in wa),sum(y*y for x,y in wa)]
 K=defaultdict(F);L=defaultdict(F);base=invseries(wa,[1]*n)
 if rec['degrees'] is None:
  addpoly(K,base,u3,-1);addpoly(L,base,mulpoly(u,Q),-1)
 else:
  degrees=rec['degrees']
  for i,d in enumerate(degrees):
   if not d:continue
   mm0=[1]*n;mm0[i]+=1;term=invseries(wa,mm0)
   addpoly(K,term,u3,d);addpoly(L,term,mulpoly(u,Q),d)
  T0=[sum(d*x for d,(x,y) in zip(degrees,wa)),sum(d*y for d,(x,y) in zip(degrees,wa))]
  addpoly(L,base,mulpoly(u,T0),-2)
 return {p:(K[p],L[p]) for p in set(K)|set(L)}

ledgers=[]
for s,t in [(0,1),(1,2)]:
 sums=defaultdict(lambda:defaultdict(lambda:[F(0),F(0)]));counts=Counter()
 for rec in generic_curves+corner_pieces:
  owner=rec['physical_owner'];ck(owners[owner]['kind'].startswith('compact'),'localization occurs only after compact physical ownership is proved')
  ser=contribution(rec,s,t)
  for p,pair in ser.items():
   for k in range(2):sums[owner][p][k]+=pair[k]
  counts[owner]+=1
 ledger={}
 for owner,rec in owners.items():
  if not rec['kind'].startswith('compact'):continue
  ck(owner in sums,'every complete compact physical component has its full second-fixed inventory')
  ck(all(pair==[0,0] for power,pair in sums[owner].items() if power<0),'all epsilon poles cancel inside this actual compact physical component')
  ledger[owner]=dict(pair=sums[owner][0],second_fixed_pieces=counts[owner],kind=rec['kind'],dimension=rec['dimension'])
 ledgers.append(ledger)
ck(ledgers[0]==ledgers[1],'the two original-lattice auxiliary evaluations agree for every physical component')
total=[sum(rec['pair'][k] for rec in ledgers[0].values()) for k in range(2)]
parts=defaultdict(lambda:[F(0),F(0)])
for owner,rec in ledgers[0].items():
 key='generic' if owner.startswith('generic:') else owner.split(':')[0]
 for k in range(2):parts[key][k]+=rec['pair'][k]
out=dict(scope='Fresh compact ledger of the newly constructed marked toric atlas. Every physical fixed component is assigned from full normal-face/period data before second-action localization. Each compact owner has its whole generic endpoint half-plane or compact corner fan verified; epsilon poles cancel per owner and two original-lattice auxiliary evaluations agree. The prescribed noncompact physical lower components are retained separately for their own cap comparisons.',
         checks=checks,endpoints=enddata,physical_owners=owners,generic_curve_clutches=generic_curves,compact_corner_second_fixed_pieces=corner_pieces,excluded_second_fixed_pieces=excluded,
         physical_component_ledger=ledgers[0],parts=dict(parts),compact_pair=total)
(root/'K111_T2_compact_ledger.json').write_text(json.dumps(serial(out),indent=2)+'\n')
print(json.dumps(dict(checks=checks,physical_compact_components=len(ledgers[0]),generic_curves=len(generic_curves),corner_second_fixed_pieces=len(corner_pieces),excluded_pieces=len(excluded),parts=serial(dict(parts)),compact_pair=serial(total)),indent=2))
