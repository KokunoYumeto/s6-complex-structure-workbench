"""Exact relative periodic regularization of the fresh common auxiliary fan.

The input is the six-cell overlay of the original convex periodic cells,
not the absent immutable 72-triangle array. All affine parent ownership
and actual period words are retained through every stellar subdivision.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import deque
from functools import reduce
from itertools import product
from math import gcd, floor, ceil
import json

root=Path(__file__).resolve().parents[1]
src=json.loads((root/'K111_new_common_auxiliary_fan.json').read_text())
checks=0
def ck(x,m):
 global checks
 checks+=1
 if not x:raise AssertionError(m)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def det(c):return dot(c[0],cross(c[1],c[2]))
def adj(c):return (cross(c[1],c[2]),cross(c[2],c[0]),cross(c[0],c[1]))
def bary_num(c,v):return tuple(dot(x,v) for x in adj(c))
def prim(v):
 d=reduce(gcd,map(abs,v));return tuple(x//d for x in v)
def period(v,i,j):return (v[0]+(23*i+11*j)*v[2],v[1]+3*(i+j)*v[2],v[2])
def period_coord(v):return (F(3*v[0]-11*v[1],36*v[2]),F(-3*v[0]+23*v[1],36*v[2]))
# The actual H domain has period-coordinate ranges [-1,0] and [0,1].
H=[tuple(map(F,x)) for x in src['common_domain']]
hc=[period_coord((x,y,F(1))) for x,y in H]
lo=[min(v[k] for v in hc) for k in range(2)]
hi=[max(v[k] for v in hc) for k in range(2)]
def in_domain(v):
 a,b=period_coord(v)
 return lo[0]<=a<=hi[0] and lo[1]<=b<=hi[1]
def periodic_copies(v):
 a=period_coord(v)
 return sorted({period(v,i,j) for i in range(ceil(lo[0]-a[0]),floor(hi[0]-a[0])+1)
                for j in range(ceil(lo[1]-a[1]),floor(hi[1]-a[1])+1)})
def quotient_ray(c):
 d=det(c);A=adj(c);zero=(0,0,0)
 gens=[tuple(A[i][j]%d for i in range(3)) for j in range(3)]
 seen={zero};q=deque([zero])
 while q:
  x=q.popleft()
  for y in gens:
   z=tuple((a+b)%d for a,b in zip(x,y))
   if z not in seen:seen.add(z);q.append(z)
 ck(len(seen)==d,'exact original-lattice quotient order')
 rays=set()
 for a in seen-{zero}:
  vv=[sum(c[i][k]*a[i] for i in range(3)) for k in range(3)]
  ck(all(x%d==0 for x in vv),'whole quotient representative is integral')
  v=prim(tuple(x//d for x in vv))
  ck(v[2]>0,'new auxiliary ray lies over the collision divisor')
  rays.add(v)
 return min(rays,key=lambda v:(v[2],sum(abs(x) for x in v),v))
fan=[dict(x,rays=tuple(tuple(v) for v in x['rays'])) for x in src['initial_triangles']]
history=[]
while True:
 bad=[x for x in fan if det(x['rays'])>1]
 if not bad:break
 chosen=min(bad,key=lambda x:(-det(x['rays']),x['rays']))
 v=quotient_ray(chosen['rays']);copies=periodic_copies(v)
 ck(bool(copies),'entire new period orbit meets the fundamental domain')
 step=dict(original_ray=v,orbit=copies,changes=[])
 for w in copies:
  new=[]
  for rec in fan:
   c=rec['rays'];a=bary_num(c,w);d=det(c)
   if min(a)<0 or sum(x>0 for x in a)<=1:
    new.append(rec);continue
   children=[]
   for i,x in enumerate(a):
    if x<=0:continue
    cc=list(c);cc[i]=w;cc=tuple(cc);dd=det(cc)
    ck(0<dd<d,'strict determinant decrease on each full incident star')
    # Replacing a positive column preserves its ordered orientation.
    children.append(cc);new.append(dict(rec,rays=cc))
   step['changes'].append(dict(ray=w,parent=c,owner=rec['owner'],zero_word=rec['zero_word'],
                               one_word=rec['one_word'],barycentric=[str(F(x,d)) for x in a],children=children))
  fan=new
 ck(bool(step['changes']),'stellar morphism changes its actual containing cones')
 history.append(step)
 if len(history)%25==0:print('stellar orbits',len(history),'cones',len(fan),'remaining max',max(det(x['rays']) for x in fan),flush=True)

ck(all(det(x['rays'])==1 for x in fan),'all final cones are regular in the original lattice')
ck(len({tuple(sorted(x['rays'])) for x in fan})==len(fan),'no duplicate full cones')
ck(sum(F(det(x['rays']),2*reduce(lambda a,b:a*b,(v[2] for v in x['rays']),1)) for x in fan)==36,
   'complete exact fundamental-domain area after every stellar map')
def facet(v,k):
 a,b,h=v
 return [b,b+3*h,3*a-11*b,3*a-11*b+36*h][k]
edges=[]
for k in range(4):
 ee=set()
 for rec in fan:
  vv=[v for v in rec['rays'] if facet(v,k)==0]
  if len(vv)==2:ee.add(tuple(sorted(vv)))
 edges.append(ee)
ck({tuple(sorted(period(v,0,1) for v in e)) for e in edges[1]}==edges[0],
   'whole T boundary edge set agrees under the actual period')
ck({tuple(sorted(period(v,1,-1) for v in e)) for e in edges[3]}==edges[2],
   'whole L/T boundary edge set agrees under the actual period')

# Exact parent maps use inverse lattice maps after removing the stored
# period word. Their character maps are transposes; unit columns are
# retained below, not discarded as numerical constants.
parent_maps=[];one_edge=set()
for rec in fan:
 for parent in ['zero','one']:
  i,j=rec[parent+'_word'];rays=[]
  for a,b,h in rec['rays']:
   a-= (23*i+11*j)*h;b-=3*(i+j)*h
   ray=(-a-b,b,h) if parent=='zero' else (-b,a,h)
   rays.append(ray)
   if parent=='one':
    x,y,r=ray
    if 3*y-x==0: y+=12*r
    if 3*y-x-36*r==0:
     ck(x%3==0,'native boundary first coordinate is divisible by three')
     q=(x//3,r);g=gcd(*map(abs,q));q=tuple(z//g for z in q)
     if 0<=q[0]<=q[1]:one_edge.add(q)
  # Every original cell is evaluated by exact rational containment.
  poly=[tuple(map(F,z)) for z in (src['zero_cell'] if parent=='zero' else src['one_cell'])]
  # The displayed original cells here are in common coordinates.
  for a,b,h in rec['rays']:
   vv=(F(a,h)-(23*i+11*j),F(b,h)-3*(i+j))
   for p,q in zip(poly,poly[1:]+poly[:1]):
    ck((q[0]-p[0])*(vv[1]-p[1])-(q[1]-p[1])*(vv[0]-p[0])>=0,
       'all final rays map to the recorded original parent cell')
  parent_maps.append(dict(cone=rec['rays'],parent=parent,period_word=[i,j],native_rays=rays,
                         common_period_p_exponents=[-i-j,3*i+2*j,0],
                         common_period_f0_exponents=[2*i+j,0,0]))
chain=sorted(one_edge,key=lambda q:F(*q))
ck(chain[0]==(0,1) and chain[-1]==(1,1),'actual new one-edge chain has both marked endpoints')
for a,b in zip(chain,chain[1:]):ck(a[0]*b[1]-a[1]*b[0]==-1,'all actual native boundary intervals are regular')

out=dict(scope='New regular common auxiliary fan from the original convex periodic cells; all stellar maps, owner period words, exact parent maps, full boundary edge identifications and the new native one-edge chain are supplied. This does not recreate the unavailable old72-triangle fan and does not by itself identify completed physical boundaries.',
         checks=checks,initial_overlay_checks=src['checks'],regular_cones=len(fan),stellar_orbits=len(history),
         maximum_height=max(v[2] for rec in fan for v in rec['rays']),cones=fan,stellar_history=history,
         parent_maps=parent_maps,boundary_edges=[sorted(x) for x in edges],ordered_native_edge_chain=chain)
(root/'K111_new_regular_common_fan.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['checks','initial_overlay_checks','regular_cones','stellar_orbits','maximum_height','ordered_native_edge_chain','scope']},indent=2))
