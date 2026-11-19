"""Exact periodic common refinement of three exceptional-end fans.

All polygon operations use Fraction. A deterministic stellar algorithm makes
the resulting three-cones regular, retaining primitive ray heights, original
parent cones, both monomial morphisms and the complete p,b unit exponents.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
from math import floor,ceil,gcd,lcm
import json,time
ROOT=Path(__file__).resolve().parents[2]
M=((5,1),(1,2));started=time.monotonic()
H=[(F(x),F(y)) for x,y in [(0,0),(-4,0),(-5,-1),(-5,-2),(-1,-2),(0,-1)]]
upper_raw=json.loads((ROOT/'code/part3/e6_p_infinity_fan.json').read_text())['upper_triangles']
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def area(poly):return sum((cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly))),F(0))/2
def ccw(poly):return list(poly) if area(poly)>0 else list(reversed(poly))
upper=[ccw(tri) for tri in upper_raw]
upper_permutations=[([0,1,2] if area(tri)>0 else [2,1,0]) for tri in upper_raw]
def clean(poly):
 out=[]
 for p in poly:
  if not out or p!=out[-1]:out.append(p)
 if len(out)>1 and out[0]==out[-1]:out.pop()
 return out
def clip(poly,triangle):
 for c,d in zip(triangle,triangle[1:]+triangle[:1]):
  edge=sub(d,c);out=[]
  if not poly:return []
  for a,b in zip(poly,poly[1:]+poly[:1]):
   sa=cross(edge,sub(a,c));sb=cross(edge,sub(b,c));ina=sa>=0;inb=sb>=0
   if ina:out.append(a)
   if ina!=inb:
    t=sa/(sa-sb);out.append((a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1])))
  poly=clean(out)
 return poly
def periods(p):return ((2*p[0]-p[1])/9,(-p[0]+5*p[1])/9)
def shift(p,i,j):return (p[0]+5*i+j,p[1]+i+2*j)
def inH(p):return all(cross(sub(b,a),sub(p,a))>=0 for a,b in zip(H,H[1:]+H[:1]))
hcoords=[periods(p) for p in H]
hlo=[min(p[i] for p in hcoords) for i in range(2)];hhi=[max(p[i] for p in hcoords) for i in range(2)]
def images(p):
 c=periods(p);out=[]
 for i in range(ceil(hlo[0]-c[0]),floor(hhi[0]-c[0])+1):
  for j in range(ceil(hlo[1]-c[1]),floor(hhi[1]-c[1])+1):
   q=shift(p,i,j)
   if inH(q):out.append((q,i,j))
 return out
def matcols(cols):return [[cols[j][i] for j in range(3)] for i in range(3)]
def detcols(a,b,c):
 return a[0]*(b[1]*c[2]-b[2]*c[1])-b[0]*(a[1]*c[2]-a[2]*c[1])+c[0]*(a[1]*b[2]-a[2]*b[1])
def determinant(cols):return detcols(*cols)
def coordinates(cols,v):
 d=determinant(cols)
 return (F(detcols(v,cols[1],cols[2]),d),F(detcols(cols[0],v,cols[2]),d),F(detcols(cols[0],cols[1],v),d))
def ray(p):
 d=lcm(p[0].denominator,p[1].denominator);v=(int(p[0]*d),int(p[1]*d),d)
 g=gcd(gcd(abs(v[0]),abs(v[1])),v[2]);return tuple(x//g for x in v)
def point(v):return (F(v[0],v[2]),F(v[1],v[2]))
def orient(cols):
 cols=tuple(cols)
 return cols if determinant(cols)>0 else (cols[0],cols[2],cols[1])
def encode(q):
 if isinstance(q,F):return [q.numerator,q.denominator]
 if isinstance(q,(tuple,list)):return [encode(x) for x in q]
 if isinstance(q,dict):return {k:encode(v) for k,v in q.items()}
 return q

parents=[]
zero_upper=json.loads((ROOT/'code/part3/e6_p_zero_semifree_fan.json').read_text())['upper_triangles']
for index,triangle in enumerate(zero_upper):
 cols=tuple((a,b,1) for a,b in triangle)
 transformed=tuple((-4*a-3*b,a+b,h) for a,b,h in cols)
 parents.append({'kind':'semifree_grid','k':index,'matrix':transformed,'order':['theta_1','theta_2','theta_3'],'polygon':ccw([point(v) for v in transformed])})
polys=[];parent_instances={}
for index,parent in enumerate(parents):
 ps=[periods(p) for p in parent['polygon']]
 lo=[min(p[i] for p in ps) for i in range(2)];hi=[max(p[i] for p in ps) for i in range(2)]
 for i in range(ceil(hlo[0]-hi[0]),floor(hhi[0]-lo[0])+1):
  for j in range(ceil(hlo[1]-hi[1]),floor(hhi[1]-lo[1])+1):
   shifted=[shift(p,i,j) for p in parent['polygon']]
   key=f'{index}:{i}:{j}'
   actual=tuple((v[0]+(5*i+j)*v[2],v[1]+(i+2*j)*v[2],v[2]) for v in parent['matrix'])
   for ti,tri in enumerate(upper):
    tri=[tuple(map(F,p)) for p in tri]
    poly=clip(shifted.copy(),tri)
    if len(poly)<3 or area(poly)<=0:continue
    parent_instances[key]={'kind':parent['kind'],'k':parent['k'],'free_coordinate_order':parent['order'],'rays':actual,'shift':[i,j],'common_character_units':{'p':[-6-3*i-3*j,i+j,0],'b':[-2*i-j,0,0]}}
    polys.append({'polygon':poly,'zero_parent':key,'infinity_parent':ti})
assert sum(area(p['polygon']) for p in polys)==9
print(json.dumps({'stage':'two_fan_intersections','polygons':len(polys)}),flush=True)
def bounds(poly):return (min(p[0] for p in poly),max(p[0] for p in poly),min(p[1] for p in poly),max(p[1] for p in poly))
def meets(a,b):return a[0]<b[1] and b[0]<a[1] and a[2]<b[3] and b[2]<a[3]
one_instances={};one_clips=[]
for cell in range(3):
 for k in range(3):
  choices=[('x',((cell+1,k+1),(cell+1,k),(cell,0)),['a','b','y']),('y',((cell+1,3),(cell,k+1),(cell,k)),['x','a','b'])]
  for kind,coords,order in choices:
   matrix=tuple((-a+b,a,1) for a,b in coords)
   polygon=ccw([point(v) for v in matrix]);ps=[periods(p) for p in polygon]
   lo=[min(p[a] for p in ps) for a in range(2)];hi=[max(p[a] for p in ps) for a in range(2)]
   for i in range(ceil(hlo[0]-hi[0]),floor(hhi[0]-lo[0])+1):
    for j in range(ceil(hlo[1]-hi[1]),floor(hhi[1]-lo[1])+1):
     triangle=[shift(p,i,j) for p in polygon]
     if not meets(bounds(triangle),bounds(H)):continue
     key=f'{cell}:{kind}:{k}:{i}:{j}'
     actual=tuple((v[0]+(5*i+j)*v[2],v[1]+(i+2*j)*v[2],v[2]) for v in matrix)
     one_instances[key]={'kind':kind,'source_cell':cell,'k':k,'free_coordinate_order':order,'rays':actual,'shift':[i,j],'common_character_units':{'p':[-6-3*i-3*j,i+j,0],'b':[-2*i-j,0,0]}}
     one_clips.append((key,triangle,bounds(triangle)))
newpolys=[]
for item in polys:
 bbox=bounds(item['polygon'])
 for key,triangle,tbox in one_clips:
  if not meets(bbox,tbox):continue
  poly=clip(item['polygon'].copy(),triangle)
  if len(poly)>=3 and area(poly)>0:newpolys.append({**item,'polygon':poly,'one_parent':key})
polys=newpolys
assert sum(area(p['polygon']) for p in polys)==9
print(json.dumps({'stage':'three_fan_intersections','polygons':len(polys),'seconds':round(time.monotonic()-started,1)}),flush=True)
allpoints={p for item in polys for p in item['polygon']}
for p in list(allpoints):allpoints.update(q for q,i,j in images(p))
def onsegment(p,a,b):
 return cross(sub(b,a),sub(p,a))==0 and all(min(a[i],b[i])<=p[i]<=max(a[i],b[i]) for i in range(2))
def refine_boundary(poly):
 out=[]
 for a,b in zip(poly,poly[1:]+poly[:1]):
  axis=0 if a[0]!=b[0] else 1
  pts=[p for p in allpoints if p!=b and onsegment(p,a,b)]
  pts.sort(key=lambda p:(p[axis]-a[axis])/(b[axis]-a[axis]));out+=pts
 return clean(out)
def intriangle(p,t):return all(cross(sub(b,a),sub(p,a))>=0 for a,b in zip(t,t[1:]+t[:1]))
def triangulate(poly):
 poly=poly.copy();out=[]
 while len(poly)>3:
  for i in range(len(poly)):
   prev=(i-1)%len(poly);nxt=(i+1)%len(poly);t=[poly[prev],poly[i],poly[nxt]]
   if area(t)<=0:continue
   if any(intriangle(q,t) for k,q in enumerate(poly) if k not in (prev,i,nxt)):continue
   out.append(t);poly.pop(i);break
  else:raise AssertionError(('No exact ear',poly))
 assert area(poly)>0;out.append(poly);return out
cones={}
for item in polys:
 poly=refine_boundary(item['polygon'])
 for tri in triangulate(poly):
  cols=orient(tuple(ray(p) for p in tri));key=tuple(sorted(cols))
  assert key not in cones
  cones[key]={'rays':cols,'zero_parent':item['zero_parent'],'one_parent':item['one_parent'],'infinity_parent':item['infinity_parent']}
assert sum(F(determinant(c['rays']),2*c['rays'][0][2]*c['rays'][1][2]*c['rays'][2][2]) for c in cones.values())==9
history=[]
def face_set(row):
 out=set()
 for c in cones.values():
  for face in combinations(c['rays'],2):
   if all(sum(a*b for a,b in zip(row,v))==0 for v in face):out.add(tuple(sorted(face)))
 return out
def period_faces():
 for name,target,source,delta in [('K',(1,0,0),(1,0,5),(5,1)),('J',(0,1,0),(0,1,2),(1,2)),('KJinv',(1,-1,-1),(1,-1,4),(4,-1))]:
  lhs=face_set(target)
  rhs={tuple(sorted((v[0]+delta[0]*v[2],v[1]+delta[1]*v[2],v[2]) for v in face)) for face in face_set(source)}
  assert lhs==rhs,(name,lhs-rhs,rhs-lhs)
period_faces()
print(json.dumps({'stage':'initial_cones','cones':len(cones),'max_det':max(determinant(c['rays']) for c in cones.values())}),flush=True)
while True:
 bad=[c for c in cones.values() if determinant(c['rays'])>1]
 if not bad:break
 selected=max(bad,key=lambda c:determinant(c['rays']));cols=selected['rays'];oldmax=determinant(cols)
 generators=[]
 for e in [(1,0,0),(0,1,0),(0,0,1)]:
  generators.append(tuple(int(q*oldmax)%oldmax for q in coordinates(cols,e)))
 residues={(0,0,0)};queue=[(0,0,0)]
 for residue in queue:
  for generator in generators:
   nxt=tuple((x+y)%oldmax for x,y in zip(residue,generator))
   if nxt not in residues:residues.add(nxt);queue.append(nxt)
 assert len(residues)==oldmax
 candidates=[]
 for residue in sorted(residues-{(0,0,0)}):
  raw=tuple(sum(cols[j][i]*residue[j] for j in range(3)) for i in range(3))
  assert all(x%oldmax==0 for x in raw)
  raw=tuple(x//oldmax for x in raw);g=gcd(gcd(abs(raw[0]),abs(raw[1])),raw[2])
  candidate=tuple(x//g for x in raw);fraction=tuple(F(x,oldmax*g) for x in residue)
  candidates.append(((max(fraction),sum(fraction),candidate[2],candidate),candidate))
 _,v=min(candidates);assert v[2]>0
 lifted=[(v[0]+(5*i+j)*v[2],v[1]+(i+2*j)*v[2],v[2]) for q,i,j in images(point(v))]
 removed=set();added=[]
 for key,item in list(cones.items()):
  for nv in lifted:
   co=coordinates(item['rays'],nv)
   if any(x<0 for x in co):continue
   positive=[i for i,x in enumerate(co) if x>0]
   if len(positive)<=1:continue
   assert all(co[i]<1 for i in positive),(item,nv,co)
   removed.add(key)
   for i in positive:
    new=list(item['rays']);new[i]=nv;new=orient(new)
    assert 0<determinant(new)<determinant(item['rays'])
    added.append({'rays':new,'zero_parent':item['zero_parent'],'one_parent':item['one_parent'],'infinity_parent':item['infinity_parent']})
   break
 assert removed
 for key in removed:del cones[key]
 for item in added:
  key=tuple(sorted(item['rays']));assert key not in cones;cones[key]=item
 history.append({'primitive_ray':v,'periodic_images':lifted,'removed_cones':len(removed),'added_cones':len(added),'selected_determinant':oldmax})
 if len(history)%50==0:
  period_faces();print(json.dumps({'stage':'regularizing','steps':len(history),'cones':len(cones),'max_det':max(determinant(c['rays']) for c in cones.values()),'seconds':round(time.monotonic()-started,1)}),flush=True)
 assert len(history)<20000
period_faces()
assert all(determinant(c['rays'])==1 for c in cones.values())
assert sum(F(1,2*c['rays'][0][2]*c['rays'][1][2]*c['rays'][2][2]) for c in cones.values())==9
edge_incidence={}
for item in cones.values():
 for edge in combinations(item['rays'],2):
  key=tuple(sorted(edge));edge_incidence[key]=edge_incidence.get(key,0)+1
for edge,count in edge_incidence.items():
 boundary=any(all(cross(sub(b,a),sub(point(v),a))==0 for v in edge) for a,b in zip(H,H[1:]+H[:1]))
 assert count==(1 if boundary else 2),(edge,count,boundary)
data=[]
for item in cones.values():
 cols=item['rays'];p0=parent_instances[item['zero_parent']];p1=one_instances[item['one_parent']];pi=tuple((int(x),int(y),1) for x,y in upper[item['infinity_parent']])
 E0=[coordinates(p0['rays'],v) for v in cols];E1=[coordinates(p1['rays'],v) for v in cols];Ei=[coordinates(pi,v) for v in cols]
 assert all(q.denominator==1 and q>=0 for col in E0+E1+Ei for q in col)
 E0=tuple(tuple(int(q) for q in col) for col in E0);E1=tuple(tuple(int(q) for q in col) for col in E1);Ei=tuple(tuple(int(q) for q in col) for col in Ei)
 assert abs(determinant(E0))==1 and abs(determinant(E1))==1 and determinant(Ei)==1
 weights=coordinates(cols,(1,0,0));assert all(q.denominator==1 for q in weights)
 unit={}
 for name,exponents in p0['common_character_units'].items():
  u=coordinates(p0['rays'],exponents);assert all(q.denominator==1 for q in u)
  unit[name]=[-int(q) for q in u]
 unit1={}
 for name,exponents in p1['common_character_units'].items():
  u=coordinates(p1['rays'],exponents);assert all(q.denominator==1 for q in u)
  unit1[name]=[-int(q) for q in u]
 ui=coordinates(pi,(0,0,1));assert all(q.denominator==1 for q in ui)
 source_z=[v[1]+3*v[2] for v in cols];source_w=[-v[1] for v in cols]
 assert all(q>=0 for q in source_z+source_w)
 assert [a+b for a,b in zip(source_z,source_w)]==[3*v[2] for v in cols]
 data.append({**item,'zero_monomial_matrix':matcols(E0),'zero_unit_exponents':unit,'one_monomial_matrix':matcols(E1),'one_unit_exponents':unit1,'infinity_monomial_matrix':matcols(Ei),'infinity_unit_exponents':{'p':[int(q) for q in ui]},'physical_weights':[int(q) for q in weights],'base_multiplicities':[v[2] for v in cols],'original_canonical_orders':[2*v[2]-1 for v in cols],'source_Z1':{'p_power':1,'exponents':source_z},'source_W1':{'p_power':0,'exponents':source_w}})
out={'status':'PASS','scope':'Generic p-zero/p-one/p-infinity exceptional overlap with p and b units; exact periodic toric common regular refinement, all three full monomial/unit arrows, literal R=pP reframe, source Z1=pP^3 Z,W1=Z^-1 and inherited canonical orders. Full four-cone corner graph extension, determinant-line attachment and compact global boundary remain open; no return or Spin extension is assigned.','intersection_polygons':len(polys),'initial_vertices':len(allpoints),'regular_cones':len(data),'stellar_steps':len(history),'period_matrix':M,'normalized_area':9,'edge_incidence_counts':{'interior':sum(n==2 for n in edge_incidence.values()),'boundary':sum(n==1 for n in edge_incidence.values())},'parent_zero_instances':parent_instances,'parent_one_instances':one_instances,'parent_infinity_triangles':upper,'parent_infinity_order_permutations':upper_permutations,'stellar_history':history,'cones':data,'seconds':round(time.monotonic()-started,1)}
Path(__file__).with_suffix('.json').write_text(json.dumps(encode(out),indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('parent_zero_instances','parent_one_instances','parent_infinity_triangles','stellar_history','cones')},indent=2),flush=True)
