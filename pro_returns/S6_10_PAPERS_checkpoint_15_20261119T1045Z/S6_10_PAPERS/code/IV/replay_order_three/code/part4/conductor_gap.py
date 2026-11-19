"""Exact curve-defect examples and the permitted nodal-A3 warning model."""
from pathlib import Path
from math import gcd
import json
import sympy as sp

t,x,y,z,s,U,V=sp.symbols('t x y z s U V')
plane=[]
for p in range(2,8):
 for q in range(p+1,11):
  if gcd(p,q)!=1:continue
  delta=(p-1)*(q-1)//2
  r=p-1
  v=q*(p-1)
  tau=v+2*delta
  defect=delta+tau-r
  assert defect==5*delta
  plane.append({'p':p,'q':q,'delta':delta,'r':r,'v':v,'tau':tau,'defect':defect})
tangent=[]
for k in range(1,9):
 h=y*(y-x**k)
 vals=[]
 for yi in (0,t**k):
  entries=[sp.expand(sp.diff(h,u).subs({x:t,y:yi})) for u in (x,y)]
  orders=[min(mon[0] for mon,c in sp.Poly(e,t).terms()) for e in entries if e!=0]
  vals.append(min(orders))
 assert vals==[k,k]
 tau=sum(vals)+2*k
 assert k+tau==5*k
 tangent.append({'contact':k,'delta':k,'gradient_orders':vals,'tau':tau,'defect':k+tau})

f=x*z*z+x*x*y**4
cover=sp.expand(f.subs({x:s*s,z:U/s,y:V/s}))
assert cover==U*U+V**4
normal=sp.expand(f.subs({x:-U*U,z:U*y*y}))
assert normal==0
assert sp.expand(f.subs({x:s*s,z:(-U)/(-s),y:(-V)/(-s)})-cover)==0
weights={x:4,y:1,z:4}
weighted=sum(weights[a]*a*sp.diff(f,a) for a in (x,y,z))
assert sp.expand(weighted-12*f)==0

result={'proof':'P4.34','coprime_plane_branch_examples':plane,
        'two_smooth_plane_branch_examples':tangent,
        'node_A3_warning':{'equation':str(f),'cover':str(cover),
          'normalization_nonplane':{'x':'-u^2','y':'y','z':'u*y^2'},
          'weighted_degree':12,'weights':[4,1,4],
          'global_counterexample_claim':False},'all_checks_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('P4.34 plane conductor-defect checks: PASS')
print('Coprime unibranch examples:',len(plane))
print('Two smooth branch contact orders:',list(range(1,9)))
print('Every computed planar local defect equals 5 delta.')
print('Allowed nodal-A3 warning cover: f(s^2,V/s,U/s) =',cover)
print('Weights (4,1,4), degree 12; nonplane normalization identity: PASS')
