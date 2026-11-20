"""Explicit two-fan witness for the unspecified zero-upper input.

Creates two72-triangle periodic original-lattice fans, both satisfying
the printed hexagon/source-band constraints. They differ by one actual
unit-square diagonal flop. Computes the exact zero-parent contribution
to the one-end edge subdivision. Neither fan is asserted to be the
absent immutable source file or substituted into the seed calculation.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import json
import numpy as np
from scipy.spatial import Delaunay

checks=0
def ck(x,m):
 global checks
 checks+=1
 if not x:raise AssertionError(m)
def cross(u,v):return u[0]*v[1]-u[1]*v[0]
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def canonical(t):return tuple(sorted(map(tuple,t)))
H=[(0,0),(-5,0),(-10,-3),(-13,-6),(-8,-6),(-3,-3)]
inside=lambda p:all(cross(sub(b,a),sub(p,a))>=0 for a,b in zip(H,H[1:]+H[:1]))
points=[(x,y) for x in range(-13,1) for y in range(-6,1) if inside((x,y))]
ck(len(points)==46,'exact lattice-point count in original hexagon')
triangles=set()
for side in [1,-1]:
 pp=[p for p in points if side*(p[1]+3)>=0]
 dd=Delaunay(np.array(pp))
 triangles.update(canonical([pp[int(i)] for i in t]) for t in dd.simplices)
A=(-10,-5);B=(-9,-5);C=(-9,-4);D=(-10,-4)
AC={canonical((A,B,C)),canonical((A,C,D))}
BD={canonical((A,B,D)),canonical((B,C,D))}
ck(AC<=triangles or BD<=triangles,'the actual interior unit square has one complete diagonal triangulation')
outside=triangles-(AC|BD)
fans={'AC':outside|AC,'BD':outside|BD}

def validate(name,fan):
 ck(len(fan)==72,'all72 original-lattice upper triangles')
 ck(all(abs(cross(sub(t[1],t[0]),sub(t[2],t[0])))==1 for t in fan),'all upper determinants one')
 ck(all(min(v[1]+3 for v in t)>=0 or max(v[1]+3 for v in t)<=0 for t in fan),'entire source-band line retained')
 edge_count=Counter(tuple(sorted((t[i],t[(i+1)%3]))) for t in fan for i in range(3))
 ck(all(n in [1,2] for n in edge_count.values()),'complete triangle incidence')
 boundary={e for e,n in edge_count.items() if n==1}
 ck(len(boundary)==18,'exact subdivided original boundary')
 periods=[('L',(10,3),lambda v:v[0]-v[1]+7,lambda v:v[0]-v[1]),
          ('T',(8,6),lambda v:v[1]+6,lambda v:v[1]),
          ('L/T',(2,-3),lambda v:3*v[0]-5*v[1]+15,lambda v:3*v[0]-5*v[1]-6)]
 for pname,shift,src,tgt in periods:
  ss={e for e in boundary if all(src(v)==0 for v in e)}
  tt={e for e in boundary if all(tgt(v)==0 for v in e)}
  mapped={tuple(sorted(tuple(v[j]+shift[j] for j in range(2)) for v in e)) for e in ss}
  ck(bool(ss) and mapped==tt,'entire actual period boundary chain '+pname)
 # The actual one-edge maps through L0/T0 to gamma(t)=(-10+2t,-3-3t).
 origin=(-10,-3);direction=(2,-3)
 parameters={F(0),F(1)}
 crossings=[]
 for e in edge_count:
  q,r=e;edge=sub(r,q);den=cross(direction,edge)
  if den:
   t=F(cross(sub(q,origin),edge),den)
   u=F(cross(sub(q,origin),direction),den)
   if 0<=t<=1 and 0<=u<=1:
    parameters.add(t);crossings.append(dict(edge=e,t=str(t),u=str(u)))
  elif cross(sub(q,origin),direction)==0:
   for v in e:
    t=F(v[0]-origin[0],direction[0])
    if 0<=t<=1:parameters.add(t)
 return dict(triangles=sorted(fan),boundary_edges=sorted(boundary),one_edge_parameters=list(map(str,sorted(parameters))),one_edge_native_upper_rays=[(3*t.numerator,t.numerator+12*t.denominator,t.denominator,0) for t in sorted(parameters)],crossings=crossings)

records={name:validate(name,fan) for name,fan in fans.items()}
pa={F(x) for x in records['AC']['one_edge_parameters']}
pb={F(x) for x in records['BD']['one_edge_parameters']}
ck(pa-pb=={F(2,5)} and not pb-pa,'exact changed zero-parent edge crossing')
ck(tuple(A[i]+C[i] for i in range(2))==tuple(B[i]+D[i] for i in range(2)),'actual conifold ray relation for the periodic flop')
# Original one-to-zero coefficient arrow, retaining the entire p factor:
# X0'=P^2 X1/Y1; Y0'=P^-3 p^-1/X1.
M=np.array([[1,-1,2,0],[-1,0,-3,-1],[0,0,1,0],[0,0,0,1]],dtype=int)
Minv=np.array([[0,-1,-3,-1],[-1,-1,-1,-1],[0,0,1,0],[0,0,0,1]],dtype=int)
ck(np.array_equal(M@Minv,np.eye(4,dtype=int)) and np.array_equal(Minv@M,np.eye(4,dtype=int)),'full four-character arrow and reciprocal')
ck(tuple(M@np.array([6,62,5,0]))==(-46,-21,5,0),'t=2/5 ray transported by actual full map')
out=dict(scope='Two explicitly related allowable upper fans witness the missing source-file choice. They are not asserted to equal the immutable original fan, and their zero-parent edge subdivisions are not the full three-parent common subdivision.',checks=checks,periods={'L':[10,3],'T':[8,6],'L/T':[2,-3]},unit_square=[A,B,C,D],full_character_matrix=M.tolist(),full_inverse_matrix=Minv.tolist(),zero_parent_crossing_difference={'AC_only':['2/5'],'BD_only':[]},fans=records)
p=Path(__file__).resolve().parents[1]
(p/'K111_zero_upper_flop_witness.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(checks=checks,triangles=[len(records[k]['triangles']) for k in records],zero_parent_one_edge_counts={k:len(v['one_edge_parameters'])-1 for k,v in records.items()},difference=out['zero_parent_crossing_difference'],scope=out['scope']),indent=2))
