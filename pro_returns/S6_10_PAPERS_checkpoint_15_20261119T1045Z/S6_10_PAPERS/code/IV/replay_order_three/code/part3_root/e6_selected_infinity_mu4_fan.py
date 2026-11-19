"""Exact periodic resolution of the actual ordinary O/T mu4 quotient fan."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
from math import gcd,floor,ceil
import sympy as sp
import json,time
started=time.monotonic()
ROOT=Path(__file__).resolve().parents[2]
def matrix(cols):return sp.Matrix.hstack(*[sp.Matrix(v) for v in cols])
def det(cols):return int(matrix(cols).det())
def coords(cols,v):return tuple(F(q) for q in matrix(cols).inv()*sp.Matrix(v))
def orient(cols):
 cols=tuple(cols)
 return cols if det(cols)>0 else (cols[0],cols[1],cols[3],cols[2])
def primitive(v):
 g=0
 for x in v:g=gcd(g,abs(x))
 return tuple(x//g for x in v)
def shifted(v,k):return (v[0],v[1],v[2],v[3]+k*(-v[0]+4*v[1]+4*v[2]))
def images(v):
 width=-v[0]+4*v[1]+4*v[2]
 assert width>=0
 if width==0:
  assert v[3]==0
  return [v]
 return [shifted(v,k) for k in range(ceil(F(-v[3],width)),floor(F(width-v[3],width))+1)]
def encode(x):
 if isinstance(x,F):return [x.numerator,x.denominator]
 if isinstance(x,(tuple,list)):return [encode(v) for v in x]
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 return x
echi=(4,1,0,0)
def reta(j):return (0,1,0,j)
def rv(j):return (0,0,1,j)
parents={};cones={}
for j in range(4):
 for kind,rays,weights,order in [
  (1,(echi,rv(j),reta(j+1),reta(j)),(1,0,j,-j-1),('chi','v','s','t')),
  (2,(echi,reta(j+1),rv(j+1),rv(j)),(1,-1,j+1,-j-1),('chi','eta','s','t'))]:
  key=f'{j}:{kind}';assert abs(det(rays))==4
  invariant=[u for u in product(range(5),repeat=4) if 1<=sum(u)<=4 and sum(a*b for a,b in zip(u,weights))%4==0]
  parents[key]={'j':j,'chart':kind,'rays':rays,'cover_coordinate_order':order,'mu4_weights':weights,'invariant_monomial_generators':invariant}
  oriented=orient(rays);cones[tuple(sorted(oriented))]={'rays':oriented,'parent':key}
history=[]
while True:
 bad=[c for c in cones.values() if det(c['rays'])>1]
 if not bad:break
 selected=max(bad,key=lambda c:det(c['rays']));cols=selected['rays'];d=det(cols)
 generators=[tuple(int(q*d)%d for q in coords(cols,e)) for e in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]]
 residues={(0,0,0,0)};queue=[(0,0,0,0)]
 for r in queue:
  for gen in generators:
   t=tuple((a+b)%d for a,b in zip(r,gen))
   if t not in residues:residues.add(t);queue.append(t)
 assert len(residues)==d
 candidates=[]
 for residue in sorted(residues-{(0,0,0,0)}):
  raw=tuple(sum(cols[j][i]*residue[j] for j in range(4)) for i in range(4))
  assert all(x%d==0 for x in raw)
  raw=tuple(x//d for x in raw);v=primitive(raw);co=coords(cols,v)
  candidates.append(((max(co),sum(co),sum(abs(x) for x in v),v),v))
 _,v=min(candidates);lifts=images(v);removed=set();added=[]
 for key,item in list(cones.items()):
  for nv in lifts:
   co=coords(item['rays'],nv)
   if any(x<0 for x in co):continue
   positive=[i for i,x in enumerate(co) if x>0]
   if len(positive)<=1:continue
   assert all(co[i]<1 for i in positive),(item,nv,co)
   removed.add(key)
   for i in positive:
    new=list(item['rays']);new[i]=nv;new=orient(new)
    assert 0<det(new)<det(item['rays'])
    added.append({'rays':new,'parent':item['parent']})
   break
 assert removed
 for key in removed:del cones[key]
 for item in added:
  key=tuple(sorted(item['rays']));assert key not in cones;cones[key]=item
 history.append({'ray':v,'period_images':lifts,'removed':len(removed),'added':len(added),'old_det':d})
 assert len(history)<1000
assert all(det(c['rays'])==1 for c in cones.values())
def faces(row):
 return {tuple(sorted(face)) for c in cones.values() for face in combinations(c['rays'],3) if all(sum(a*b for a,b in zip(row,v))==0 for v in face)}
lower=faces((0,0,0,1));upper=faces((1,-4,-4,1))
assert {tuple(sorted(shifted(v,1) for v in face)) for face in lower}==upper
outcones=[]
for item in cones.values():
 cols=item['rays'];parent=parents[item['parent']]
 C=matrix(parent['rays']).inv()*matrix(cols)
 assert all(q>=0 for q in C)
 invariant_matrix=[]
 for u in parent['invariant_monomial_generators']:
  row=sp.Matrix([u])*C
  assert all(q.q==1 and q>=0 for q in row)
  invariant_matrix.append([int(q) for q in row])
 physical=coords(cols,(0,0,0,1));assert all(q.denominator==1 for q in physical)
 canon=[v[1]+v[2]-1 for v in cols];assert all(q>=0 for q in canon)
 original=[-v[0]+5*v[1]+4*v[2]-1 for v in cols]
 frame_difference=[-v[0]+4*v[1]+3*v[2] for v in cols]
 assert all(q>=0 for q in original+frame_difference)
 assert original==[a+b for a,b in zip(canon,frame_difference)]
 source_e=[v[1]+v[2] for v in cols]
 source_q=[v[0] for v in cols]
 source_sigma4=[-v[0]+4*v[1]+4*v[2] for v in cols]
 assert all(q>=0 for q in source_e+source_q+source_sigma4)
 target=tuple(shifted(v,1) for v in cols)
 source_unit=coords(target,(0,1,-1,0));line_unit=coords(target,(0,0,0,1))
 assert all(q.denominator==1 for q in source_unit+line_unit)
 outcones.append({**item,'quotient_invariant_monomial_matrix':invariant_matrix,'physical_weights':[int(q) for q in physical],'canonical_orders':canon,'original_marked_family_volume_orders':original,'original_to_local_frame_exponents':frame_difference,'epsilon_exponents':source_e,'q_new_exponents':source_q,'sigma_fourth_exponents':source_sigma4,'B_target_rays':target,'B_source_unit_exponents':[int(q) for q in source_unit],'B_full_Hom_unit_exponents':[int(q) for q in line_unit]})
out={
 'status':'PASS','scope':'Actual ordinary O/T graph coarse mu4 quotient, resolved in its integral invariant lattice; full source and invariant-ring morphisms, physical weights, canonical divisor and B period/unit lift. This certificate assigns no Spin extension, closed boundary, characteristic number or return.',
 'quotient_torus_characters':['chi^4','chi*eta','v','V_phys'],
 'cover_to_quotient_character_matrix':[[4,0,0,0],[1,1,0,0],[0,0,1,0],[0,0,0,1]],
 'quotient_cocharacter_basis_in_cover':[[[1,4],[0,1],[0,1],[0,1]],[[-1,4],[1,1],[0,1],[0,1]],[[0,1],[0,1],[1,1],[0,1]],[[0,1],[0,1],[0,1],[1,1]]],
 'B_cocharacter_matrix':[[1,0,0,0],[0,1,0,0],[0,0,1,0],[-1,4,4,1]],
 'canonical_character':[0,1,1,0],
 'canonical_frame':'Local Omega_loc=dchi wedge deta wedge dv wedge dlog V; original marked-family volume has its separately retained full factor.',
 'original_marked_family_canonical_character':[-1,5,4,0],
 'original_to_local_frame_character':[-1,4,3,0],
 'original_to_local_frame_full_unit':'8*d(epsilon)^(-2)*u_O_or_T; u_O=U^2/(U^3-d U eta^4-2 sigma^2 eta^6), u_T=(d+2a2 X+3X^2)^(-1)',
 'source_Jacobian_unit':'J_b=1+eta*d_eta(log c_b)-v*d_v(log c_b); u_source=u_target*c_b*J_b',
 'parents':parents,'stellar_history':history,'cones':outcones,
 'initial_cones':8,'regular_cones':len(outcones),'stellar_steps':len(history),
 'paired_period_facets':len(lower),'seconds':round(time.monotonic()-started,2)}
Path(__file__).with_suffix('.json').write_text(json.dumps(encode(out),indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('parents','stellar_history','cones')},indent=2))
