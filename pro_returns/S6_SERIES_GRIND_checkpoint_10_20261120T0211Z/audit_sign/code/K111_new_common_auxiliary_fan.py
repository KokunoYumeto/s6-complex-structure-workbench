"""Fresh compatible common fan from the original periodic convex cells.

This constructs a new auxiliary subdivision, not the absent immutable
72-triangle/common-fan array. All original lattices and period words
are retained. Identifying its completed boundary with the original
marked family requires the accompanying relative comparison.
"""
from pathlib import Path
from fractions import Fraction as F
from math import floor,ceil,gcd
from functools import reduce
from itertools import combinations
import json

checks=0
def ck(x,m):
 global checks
 checks+=1
 if not x:raise AssertionError(m)
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def area(poly):return sum(cross(a,b) for a,b in zip(poly,poly[1:]+poly[:1]))/2
def orient(poly):
 p=[tuple(map(F,v)) for v in poly]
 return p if area(p)>0 else p[::-1]
def clean(poly):
 p=[]
 for v in poly:
  if not p or v!=p[-1]:p.append(v)
 if len(p)>1 and p[-1]==p[0]:p.pop()
 return p
def clip(poly,container):
 p=list(poly)
 for a,b in zip(container,container[1:]+container[:1]):
  if not p:return []
  vec=sub(b,a);q=[]
  for s,t in zip(p,p[1:]+p[:1]):
   fs=cross(vec,sub(s,a));ft=cross(vec,sub(t,a))
   if fs>=0:q.append(s)
   if (fs<0<ft) or (ft<0<fs):
    lam=fs/(fs-ft);q.append(tuple(s[i]+lam*(t[i]-s[i]) for i in range(2)))
  p=clean(q)
 return p if len(p)>=3 and area(p)>0 else []
def period(v,i,j):return(v[0]+23*i+11*j,v[1]+3*i+3*j)
def inverse_period(v):return(F(3*v[0]-11*v[1],36),F(-3*v[0]+23*v[1],36))
def translate_bounds(shape,target):
 a=list(map(inverse_period,shape));b=list(map(inverse_period,target))
 ranges=[]
 for k in range(2):
  ranges.append(range(ceil(min(v[k] for v in b)-max(v[k] for v in a)),floor(max(v[k] for v in b)-min(v[k] for v in a))+1))
 return[(i,j) for i in ranges[0] for j in ranges[1]]
def contained(p,poly):return all(cross(sub(b,a),sub(p,a))>=0 for a,b in zip(poly,poly[1:]+poly[:1]))
def on_segment(v,a,b):
 return cross(sub(b,a),sub(v,a))==0 and all(min(a[k],b[k])<=v[k]<=max(a[k],b[k]) for k in range(2))
def primitive(v):
 den=1
 for x in v:den=den*x.denominator//gcd(den,x.denominator)
 q=[int(x*den) for x in v]+[den];d=reduce(gcd,map(abs,q));return tuple(x//d for x in q)
H=orient([(0,0),(-12,0),(-23,-3),(-11,-3)])
Z=orient([(0,0),(5,0),(13,-3),(19,-6),(14,-6),(6,-3)])
O=orient([(0,0),(1,-3),(13,-3),(12,0)])
for cell in [H,Z,O]:ck(area(cell)==36,'original periodic cell has area36')
zpieces=[]
for i,j in translate_bounds(Z,H):
 piece=clip([period(v,i,j) for v in Z],H)
 if piece:zpieces.append((piece,(i,j)))
ck(sum(area(p) for p,w in zpieces)==36,'complete original zero-cell overlay')
pieces=[]
for zp,zw in zpieces:
 for i,j in translate_bounds(O,zp):
  piece=clip(zp,[period(v,i,j) for v in O])
  if piece:pieces.append(dict(polygon=piece,zero_word=zw,one_word=(i,j)))
ck(sum(area(x['polygon']) for x in pieces)==36,'complete three-parent convex-cell overlay')
for a,b in combinations(pieces,2):ck(not clip(a['polygon'],b['polygon']),'distinct overlay interiors disjoint')
# Insert every vertex in every incident edge, including exact period images.
vertices={v for x in pieces for v in x['polygon']}
for v in list(vertices):
 for i,j in translate_bounds([v],H):
  w=period(v,i,j)
  if contained(w,H):vertices.add(w)
for rec in pieces:
 old=rec['polygon'];new=[]
 for a,b in zip(old,old[1:]+old[:1]):
  vv=[v for v in vertices if on_segment(v,a,b)]
  k=0 if b[0]!=a[0] else 1
  vv.sort(key=lambda v:(v[k]-a[k])/(b[k]-a[k]))
  new.extend(vv[:-1])
 rec['polygon']=clean(new)

def in_triangle(v,a,b,c):return all(cross(sub(q,p),sub(v,p))>=0 for p,q in [(a,b),(b,c),(c,a)])
triangles=[]
for number,rec in enumerate(pieces):
 poly=list(rec['polygon']);ears=[]
 while len(poly)>3:
  choices=[]
  for i,b in enumerate(poly):
   a=poly[i-1];c=poly[(i+1)%len(poly)]
   if cross(sub(b,a),sub(c,b))<=0:continue
   others=[v for j,v in enumerate(poly) if j not in {(i-1)%len(poly),i,(i+1)%len(poly)}]
   if any(in_triangle(v,a,b,c) for v in others):continue
   choices.append(i)
  ck(bool(choices),'exact ordered ear exists')
  i=min(choices,key=lambda k:poly[k]);ear=[poly[i-1],poly[i],poly[(i+1)%len(poly)]]
  ears.append(ear);poly.pop(i)
 ears.append(poly)
 ck(sum(area(x) for x in ears)==area(rec['polygon']),'all rational ears partition the whole parent polygon')
 for ear in ears:
  triangles.append(dict(rays=[primitive(v) for v in ear],owner=number,zero_word=rec['zero_word'],one_word=rec['one_word']))

def det3(c):
 a,b,c=c
 return a[0]*(b[1]*c[2]-b[2]*c[1])-b[0]*(a[1]*c[2]-a[2]*c[1])+c[0]*(a[1]*b[2]-a[2]*b[1])
ck(all(det3(t['rays'])>0 for t in triangles),'all initial cone orientations positive')
ck(sum(F(det3(t['rays']),2*reduce(lambda a,b:a*b,(v[2] for v in t['rays']),1)) for t in triangles)==36,'all initial cone slice volumes exact')

def serial(rec):
 if isinstance(rec,F):return str(rec)
 if isinstance(rec,dict):return {k:serial(v) for k,v in rec.items()}
 if isinstance(rec,(list,tuple)):return[serial(v) for v in rec]
 return rec
out=dict(scope='Fresh common auxiliary cell overlay and exact triangulation from the original periodic convex cells. No old72-triangle array is used or claimed to be reproduced. Relative regularization and endpoint completion remain subsequent gates.',checks=checks,common_period_matrix=[[23,11],[3,3]],common_domain=H,zero_cell=Z,one_cell=O,polygons=pieces,initial_triangles=triangles,initial_determinants=sorted([det3(t['rays']) for t in triangles]))
p=Path(__file__).resolve().parents[1]
(p/'K111_new_common_auxiliary_fan.json').write_text(json.dumps(serial(out),indent=2)+'\n')
print(json.dumps(dict(checks=checks,overlay_polygons=len(pieces),vertices=len(vertices),initial_cones=len(triangles),maximum_determinant=max(out['initial_determinants']),sum_determinants=sum(out['initial_determinants']),scope=out['scope']),indent=2))
