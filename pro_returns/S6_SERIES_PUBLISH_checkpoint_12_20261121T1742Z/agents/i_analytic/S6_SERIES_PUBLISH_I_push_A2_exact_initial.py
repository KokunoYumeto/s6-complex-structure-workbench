"""Fresh exact enumeration of prism triangulations and explicit local charts.

Method: enumerate all tetrahedra, compute pairwise intersections by exact
active-facet vertex enumeration, and use volume + face matching. No historical
fan program is imported or executed.
"""
from itertools import combinations
from pathlib import Path
import json,hashlib,datetime
import sympy as S
B=Path(__file__).parent
names='abcdef'
rays={
 'a':(0,0,1,0),'b':(1,0,1,0),'c':(0,1,1,0),'d':(1,1,1,0),
 'e':(0,0,0,1),'f':(0,1,0,1)}
pts={k:S.Matrix(v[:3]) for k,v in rays.items()}
tetra={}
for t in combinations(names,4):
 M=S.Matrix.hstack(*(S.Matrix(rays[k]) for k in t));det=M.det()
 if det:
  A=S.Matrix.hstack(*(pts[k].col_join(S.Matrix([1])) for k in t))
  tetra[t]={'det':det,'bary':A.inv()}

def intersection_vertices(t,u):
 H=S.Matrix.vstack(tetra[t]['bary'],tetra[u]['bary'])
 vertices=set()
 for idx in combinations(range(8),3):
  C=H[list(idx),:3];b=-H[list(idx),3]
  if not C.det():continue
  p=C.inv()*b
  if all(v>=0 for v in H*p.col_join(S.Matrix([1]))):
   vertices.add(tuple(p))
 return vertices

compatible={}
for t,u in combinations(tetra,2):
 vv=intersection_vertices(t,u)
 common={tuple(pts[k]) for k in set(t)&set(u)}
 compatible[frozenset((t,u))]=vv==common

def exterior_faces(ts):
 counts={}
 for t in ts:
  for f in combinations(t,3):counts[f]=counts.get(f,0)+1
 assert all(v<=2 for v in counts.values())
 return [f for f,n in counts.items() if n==1]

def boundary_face(f):
 pp=[pts[x] for x in f]
 return any(all(expr(p)==0 for p in pp) for expr in (
  lambda p:p[2]-1,lambda p:p[0],lambda p:p[0]-p[2],
  lambda p:p[1],lambda p:p[1]-1))

all_tris=[]
for ts in combinations(tetra,3):
 if sum(abs(tetra[t]['det']) for t in ts)!=3:continue
 if not all(compatible[frozenset((t,u))] for t,u in combinations(ts,2)):continue
 faces=exterior_faces(ts)
 if not all(boundary_face(f) for f in faces):continue
 all_tris.append(ts)

bottom={tuple(sorted(x)) for x in ['abc','bcd']}
with_bottom=[];invariant=[]
G1={'a':'b','c':'d','e':'e','f':'f'}
for ts in all_tris:
 faces=exterior_faces(ts)
 bb={f for f in faces if set(f)<=set('abcd')}
 if bb!=bottom:continue
 with_bottom.append(ts)
 left={f for f in faces if set(f)<=set('acef')}
 right={f for f in faces if set(f)<=set('bdef')}
 if {tuple(sorted(G1[x] for x in f)) for f in left}==right:
  invariant.append(ts)

assert len(all_tris)==6
assert len(with_bottom)==3
assert len(invariant)==2
assert all(abs(v['det'])==1 for v in tetra.values())

chart_rows=[]
for ts in invariant:
 rows=[]
 for t in ts:
  qexp=[rays[x][2] for x in t];uexp=[rays[x][3] for x in t]
  assert all(q*u==0 for q,u in zip(qexp,uexp))
  assert sum(uexp) in (1,2)
  rows.append({'rays':''.join(t),'det':int(tetra[t]['det']),
    'q_exponents':qexp,'u_exponents':uexp})
 chart_rows.append(rows)

# Repeated star subdivisions of the orbit of a maximal cone with exactly one
# u-ray. r_n = top + n*(sum of three bottom rays). Each determinant is symbolic.
n=S.symbols('n',integer=True,positive=True)
base=next(t for t in invariant[0] if sum(rays[x][3] for x in t)==1)
qcols=[S.Matrix(rays[x]) for x in base if rays[x][3]==0]
top=next(S.Matrix(rays[x]) for x in base if rays[x][3]==1)
rn=top+n*sum(qcols,S.zeros(4,1))
assert rn[3]==1
assert abs(S.Matrix.hstack(*qcols,rn).det())==1
star_dets=[]
current=qcols+[rn]
rnext=sum(current,S.zeros(4,1))
for j in range(4):
 cols=current[:];cols[j]=rnext;d=S.Matrix.hstack(*cols).det()
 assert abs(d)==1;star_dets.append(str(d))

# Blow-up and conifold charts, independently obtained by substitution.
x,y,z,v,u,a,b,r,t=S.symbols('x y z v u a b r t')
F=x*y-u*z*v
assert S.expand(F.subs({u:a*x,y:a*z*v},simultaneous=True))==0
assert S.expand(F.subs({x:t*u},simultaneous=True))==u*(t*y-z*v)
node=t*y-z*v
assert [S.diff(node,k) for k in [t,y,z,v]]==[y,t,-v,-z]
assert S.expand(node.subs({t:z*r,v:y*r},simultaneous=True))==0
assert S.expand(node.subs({z:t*b,y:v*b},simultaneous=True))==0
local_charts=[
 {'coordinates':['x','a','z','v'],'map':{'u':'a*x','y':'a*z*v','q':'z*v'},'central_equation':'x*a=0'},
 {'coordinates':['u','z','y','r'],'map':{'t':'z*r','v':'y*r','q':'z*y*r'},'central_equation':'u=0'},
 {'coordinates':['u','t','v','b'],'map':{'z':'t*b','y':'v*b','q':'t*v*b'},'central_equation':'u=0'}]
out=dict(computed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 method='Exhaustive exact active-facet intersection/volume/face enumeration; symbolic blow-up substitution. Target proofs unopened.',
 rays=rays,nondegenerate_tetrahedra=len(tetra),
 all_triangulations=[[''.join(t) for t in ts] for ts in all_tris],
 bottom_triangulations=[[''.join(t) for t in ts] for ts in with_bottom],
 invariant_triangulations=[[''.join(t) for t in ts] for ts in invariant],
 toric_charts=chart_rows,
 infinite_star_family={'base_tetrahedron':''.join(base),'r_n':[str(x) for x in rn],
  'u_height':1,'new_star_determinants':star_dets},
 local_blowup_and_resolution_charts=local_charts,
 scope_limit='No historical program executed. Algebraic and toric local calculations only; global compact gluing uses the explicit dependency A1.2 plumbing and covering proof.')
(B/'S6_SERIES_PUBLISH_I_push_A2_exact.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
