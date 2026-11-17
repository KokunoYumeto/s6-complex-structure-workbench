#!/usr/bin/env python3
"""Exact source resolution, section Cartier closure, and Hom units at v=0."""
from pathlib import Path
from datetime import datetime, timezone
import sympy as S
import json
ROOT=Path(__file__).resolve().parents[2]
X,Y,T,v,u=S.symbols('X Y T v u')
F=Y**2-X**3-(1-2*v)*X**2-T*X-v**2
A=Y-v; B=Y+v; C=X; D=T+X**2+(1-2*v)*X
assert S.expand(A*B-C*D-F)==0
b,d,z=S.symbols('B D z')
vr=(b-d*z)/2
xr=b*z; yr=(d*z+b)/2
tr=d-xr**2-(1-2*vr)*xr
assert S.expand(F.subs({X:xr,Y:yr,T:tr,v:vr}))==0
assert S.diff(vr,b)==S.Rational(1,2)
assert S.simplify(tr.subs(b,d*z)-d*(1-z**2-d*z**4))==0
assert S.simplify(tr.subs({z:1,b:v,d:-v})-(v**2-2*v))==0
assert S.simplify(vr.subs({z:1,b:v,d:-v})-v)==0
# The actual G section and the doubling formula.
assert S.simplify(xr.subs({z:0,b:2*v,d:T}))==0
assert S.simplify(yr.subs({z:0,b:2*v,d:T})-v)==0
slope=T/(2*v)
x2=slope**2-(1-2*v)
y2=-v-slope*x2
assert S.factor(F.subs({X:x2,Y:y2}))==0
assert S.simplify(x2/(y2+v)+2*v/T)==0
cartier=1-b*z**3-(1-2*vr)*z**2
assert S.factor(z*tr+2*vr-b*cartier)==0
z2=-2*v/T
b2=y2+v
d2=(y2-v)/z2
assert S.factor(cartier.subs({b:b2,d:d2,z:z2}))==0
assert S.factor(cartier.subs(b,d*z))==1-z**2-d*z**4
assert cartier.subs(z,0)==1
# The two actual chord ratios in the original source coordinate.
r=(1-2*u**3)/(3*u**2)
xo=X/u**2; yo=Y/u**3; to=T/u**4
fold_minus=(yo+1+to*xo/2)/xo
fold_plus=(yo-1-to*xo/2)/xo
fminus=(Y+v+T*X/(2*v))/X
fplus=(Y-v-T*X/(2*v))/X
assert S.factor((u*fold_minus-fminus).subs(v,u**3))==0
assert S.factor((u*fold_plus-fplus).subs(v,u**3))==0
t0=(v**2-2*v)
node={X:v,Y:0,T:t0}
assert S.factor(fminus.subs(node))==v/2
assert S.factor(fplus.subs(node))==-v/2
q=S.symbols('q')
assert S.factor((q/u**4/fold_minus-q/(v*fminus)).subs(v,u**3))==0
assert S.factor((q/u**4/fold_plus-q/(v*fplus)).subs(v,u**3))==0
# Parameter winding of the actual selected Tate and suspension units.
a,bw=S.symbols('a b',integer=True)
W=S.Matrix([[1,bw],[-a,-2]])
assert W.det()==a*bw-2
assert W==S.Matrix([1,-a])*S.Matrix([[1,bw]])+S.Matrix([[0,0],[0,a*bw-2]])
data=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS: source/Cartier/unit identities; completed-family return remains working',
 conifold_coordinates={str(k):str(val) for k,val in [('A',A),('B',B),('C',C),('D',D)]},
 chosen_resolution={'A':'D*z','C':'B*z','v':str(vr),'X':str(xr),'Y':str(yr),'T':str(tr)},
 central_I2={'C1':'D=0','C0':'1-z^2-D*z^4=0','selected_node':'z=1,D=-v','other_central_node':'z=-1,D=0'},
 twoG={'X':str(x2),'Y':str(y2),'z':str(z2),'Cartier_equation':str(cartier),'central_component':'C0'},
 chord_ratios={'a2_b1':str(fminus),'a1_b2':str(fplus)},
 canonical_Hom_coefficient={'a2_b1':str(q/(v*fminus)),'a1_b2':str(q/(v*fplus))},
 selected_node_Hom_units={'a2_b1':'2/v^2','a1_b2':'-2/v^2'},
 source_parameter_windings={'qT/q':1,'Z(G)':-1,'Hom/q':-2},
 period_unit_winding_matrix=[[str(e) for e in W.row(i)] for i in range(2)])
(ROOT/'code/part3_fourfold/source_zero_resolution.json').write_text(json.dumps(data,indent=2)+'\n')
with (ROOT/'records/literature_fourfold.md').open('a') as f:
 f.write('\n- '+data['utc']+' — Executed own source_zero_resolution.py. Material: exact AB=CD map, marked-G small resolution, both I2 components, 2G Cartier closure and both actual chord/Hom coefficient transformations; no completed-family source-loop index inferred.\n')
print(json.dumps(data,indent=2))
