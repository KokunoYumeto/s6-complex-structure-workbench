"""Exact eight-residue-type replay for the K111 lower physical star.

The eight possibilities for (b0,b1) modulo3, other than(0,0),
exhaust adjacent primitive common-edge rays U(a,b), because their
(a,b) determinant is one. Both orders of the two nonzero quotient
rays are executed. This program verifies the local reduction; it
does not supply the missing actual ordered common-edge chain.
"""
from pathlib import Path
from itertools import product
from math import gcd
import json
import sympy as S

checks=0
def ck(x,m):
 global checks
 checks+=1
 if not x:raise AssertionError(m)
def matrix(c):return S.Matrix.hstack(*map(S.Matrix,c))
def U(a,b):return (3*a,a+12*b,b,0)
def frac(x):return x-S.floor(x)
def lift(x,r,l=0):
 z=int(S.ceiling(S.Rational(x,3))-S.floor(S.Rational(x,3)))
 return (x,int(S.ceiling(S.Rational(x,3)))+12*r+l*z,r,z)
e0=(0,0,0,1);e1=(0,1,0,1);delta=S.Matrix([0,1,0,0])
examples=[((0,1),(1,1)),((0,1),(1,2)),((1,2),(1,1)),
          ((1,2),(3,5)),((0,1),(1,3)),((2,3),(1,1)),
          ((1,2),(2,3)),((1,3),(1,2))]
records=[]
seen=set()
for ab0,ab1 in examples:
 a0,b0=ab0;a1,b1=ab1
 D=a0*b1-a1*b0
 ck(D==-1,'ordered boundary interval has determinant minus one')
 residue=(b0%3,b1%3);seen.add(residue)
 raw=(e0,e1,U(a0,b0),U(a1,b1));B=matrix(raw)
 ck(abs(B.det())==3,'full raw quotient has exact order three')
 quotient=[]
 for k in [1,2]:
  coeff=S.Matrix([S.Rational(k,3),frac(-S.Rational(k,3)),frac(S.Rational(k*b1,3*D)),frac(-S.Rational(k*b0,3*D))])
  v=B*coeff
  ck(all(x.q==1 for x in v),'actual nonzero quotient residue is integral')
  v=tuple(map(int,v))
  ck(v[0]%3==k and v[3]==1,'normal residues and source first coordinate agree')
  ck(v==lift(v[0],v[2]),'entire residue vector is the written native lift')
  quotient.append(v)
 order_records=[]
 for order in [(0,1),(1,0)]:
  fan=[raw];steps=[]
  for position,pick in enumerate(order):
   v=quotient[pick];new=[];maps=[]
   for c in fan:
    M=matrix(c);bb=M.inv()*S.Matrix(v)
    if min(bb)<0 or sum(bool(x>0) for x in bb)<=1:
     new.append(c);continue
    children=[]
    for j,x in enumerate(bb):
     if x>0:
      cc=list(c);cc[j]=v;cc=tuple(cc)
      ck(0<abs(matrix(cc).det())<abs(M.det()),'actual whole-star determinant descent')
      children.append(cc);new.append(cc)
    maps.append(dict(parent=c,barycentric=list(map(str,bb)),children=children))
   ck(bool(maps),'each nonzero residue gives its actual stellar morphism')
   steps.append(dict(ray=v,maps=maps));fan=new
   if position==0:
    for cc in fan:
     C=matrix(cc);dd=abs(C.det())
     ck(dd in [1,2],'first quotient ray leaves only regular or determinant-two children')
     if dd==2:
      gen=next(C.inv()[:,j].applyfunc(frac) for j in range(4) if any(frac(z) for z in C.inv()[:,j]))
      remaining=C*gen;gg=S.igcd(*list(map(int,remaining)))
      remaining=tuple(int(z/gg) for z in remaining)
      ck(remaining==quotient[order[1]],'unique remaining singular quotient ray is the other original residue')
  ck(all(abs(matrix(c).det())==1 for c in fan),'entire four-dimensional resolution is regular')
  ck(len(set(tuple(sorted(c)) for c in fan))==len(fan),'no repeated four-cone')
  invariants=[]
  for a in product(range(4),repeat=4):
   if not 0<sum(a)<=3:continue
   m=S.Matrix([a])*B.inv()
   if all(x.q==1 for x in m):invariants.append((a,m))
  for c in fan:
   for a,m in invariants:
    ex=m*matrix(c)
    ck(all(x.q==1 and x>=0 for x in ex),'complete raw quotient semigroup pullback')
  physical=[c for c in fan if e0 in c and e1 in c]
  source_rays={v for c in physical for v in c if v not in (e0,e1)}
  source_rays=sorted(source_rays,key=lambda v:S.Rational(v[0],v[2]))
  for v in source_rays:
   ck(gcd(v[0],v[2])==1,'physical source ray is primitive in original source lattice')
   ck(v==lift(v[0],v[2]),'all surviving physical tangent rays have exact floor/ceiling lift')
  chart_records=[]
  for c in physical:
   tang=sorted((v for v in c if v not in (e0,e1)),key=lambda v:S.Rational(v[0],v[2]))
   C=matrix((e0,e1,*tang));w=C.inv()*delta
   ck(w==S.Matrix([-1,1,0,0]),'ordered physical normal weights')
   ck(abs(tang[0][0]*tang[1][2]-tang[1][0]*tang[0][2])==1,'regular quotient source chart')
   rminus=S.Matrix([[0,-1,0,1]])*C;rplus=S.Matrix([[0,1,0,0]])*C
   for i,v in enumerate(tang,2):
    ck(rminus[i]==-S.floor(S.Rational(v[0],3))-12*v[2],'negative native order from actual derivative')
    ck(rplus[i]==S.ceiling(S.Rational(v[0],3))+12*v[2],'positive native order from actual derivative')
   chart_records.append(dict(rays=(e0,e1,*tang),inverse=[list(map(int,C.inv().row(i))) for i in range(4)],negative_row=list(map(int,rminus)),positive_row=list(map(int,rplus))))
  # Derive the projected minimal fan directly from the three quotient types.
  p0=(3*a0//gcd(3*a0,b0),b0//gcd(3*a0,b0))
  p1=(3*a1//gcd(3*a1,b1),b1//gcd(3*a1,b1))
  expected={p0,p1}
  if b0%3 and b1%3:
   if b0%3==b1%3:
    expected.add((2*a0+a1,(2*b0+b1)//3))
    expected.add((a0+2*a1,(b0+2*b1)//3))
   else:
    expected.add((a0+a1,(b0+b1)//3))
  ck({(v[0],v[2]) for v in source_rays}==expected,'exact finite-type projected source fan')
  order_records.append(dict(order=order,regular_cones=len(fan),stellar_maps=steps,physical_source_rays=source_rays,physical_charts=chart_records))
 ck(order_records[0]['physical_source_rays']==order_records[1]['physical_source_rays'],'both quotient insertion orders give the same complete physical star')
 # The exact label change has an integral inverse and retains source x,r,z.
 for l in range(12):
  H=S.eye(4);H[1,3]=l
  ck(H.det()==1 and H.inv()[1,3]==-l,'actual label lattice isomorphism and inverse')
  ck(H*delta==delta,'label change retains physical cocharacter')
  for v in order_records[0]['physical_source_rays']:
   ck(tuple(map(int,H*S.Matrix(v)))==lift(v[0],v[2],l),'all twelve exact native lifts')
 records.append(dict(boundary_vectors=[ab0,ab1],b_residues=residue,raw=raw,quotient_rays=quotient,orders=order_records))
ck(seen==set(product(range(3),repeat=2))-{(0,0)},'all eight possible residue types exhausted')
contractions=[]
for i,j in product(range(3),repeat=2):
 dm=S.floor(S.Rational(i,3))+S.floor(S.Rational(j,3))-S.floor(S.Rational(i+j,3))
 dp=S.ceiling(S.Rational(i+j,3))-S.ceiling(S.Rational(i,3))-S.ceiling(S.Rational(j,3))
 expected=(0,-1) if (i,j)==(1,1) else (-1,0) if (i,j)==(2,2) else (-1,-1) if {i,j}=={1,2} else (0,0)
 ck((dm,dp)==expected,'exact floor/ceiling contraction residue table')
 contractions.append(dict(residues=[i,j],negative_degree=int(dm),positive_degree=int(dp)))
out=dict(scope='All eight determinant-three lower quotient types, both insertion orders, all twelve exact label maps, complete raw invariant-semigroup arrows and native normal rows. The actual ordered common-edge chain and its global324-chart histogram remain absent.',checks=checks,types=records,contraction_table=contractions)
p=Path(__file__).resolve().parents[1]
(p/'K111_lower_finite_types.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(checks=checks,types=len(records),orders=2,actual_edge_chain_loaded=False,summary=[dict(residue=x['b_residues'],regular_cones=x['orders'][0]['regular_cones'],physical_charts=len(x['orders'][0]['physical_charts'])) for x in records]),indent=2))
