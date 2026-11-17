#!/usr/bin/env python3
"""Exact normal-cone action of successive marked translations near C1."""
from pathlib import Path
from datetime import datetime, timezone
import sympy as S
import json
ROOT=Path(__file__).resolve().parents[2]
B,D,z,eps=S.symbols('B D z epsilon')
v=(B-D*z)/2
X=B*z
Y=(B+D*z)/2
T=D-X**2-(1-2*v)*X
def minus_G(x,y):
    slope=(y+v)/x
    xx=S.factor(slope**2-(1-2*v)-x)
    yy=S.factor(v-slope*xx)
    return xx,yy
x1,y1=minus_G(X,Y)
x2,y2=minus_G(x1,y1)
z2=S.factor(x2/(y2+v))
normal=S.factor(S.limit(z2.subs({B:eps*B,D:eps*D}),eps,0))
print('normal_cone_target_z =',normal)
assert S.factor(normal-B/D)==0
# The first translation sends C1 regularly to C0 with s=-1/z.
s1=S.factor(S.limit((y1/x1).subs({B:eps*B,D:eps*D}),eps,0))
assert S.factor(s1+1/z)==0
# The direction of 2G in the identity component yields the same fractional map.
s_twoG=-(D-B*z)/(B-D*z)
chi2=S.factor((s_twoG-1)/(s_twoG+1))
assert S.factor(chi2-((z-1)/(z+1))*((B+D)/(B-D)))==0
data={
 'utc':datetime.now(timezone.utc).isoformat(),
 'status':'PASS: exact normal-cone action; periodic quotient still working',
 'translation_minus_G':{'X':str(x1),'Y':str(y1),'C1_to_C0_normalization':'s=-1/z'},
 'translation_minus_2G_target_z':str(z2),
 'normal_cone_target_z':str(normal),
 'domain_C1_parameter':'z',
 'domain_normal_directions':['B','D'],
 'meaning':'The second translation exchanges the old curve parameter with the normal projective direction; it cannot be replaced by the identity using only its central punctured-fibre limit.',
 'remaining':'identify the full real-normal quaternion clutch and its period reset, including the line multiplier'
}
(ROOT/'code/part3_fourfold/source_zero_translation_normal.json').write_text(json.dumps(data,indent=2)+'\n')
with (ROOT/'records/literature_fourfold.md').open('a') as f:
    f.write('\n- '+data['utc']+' — Executed own source_zero_translation_normal.py. Material: exact two-step translation and its normal-cone map z_target=B/D, retaining the first C1-to-C0 map s=-1/z; no return class assigned.\n')
print(json.dumps(data,indent=2))
