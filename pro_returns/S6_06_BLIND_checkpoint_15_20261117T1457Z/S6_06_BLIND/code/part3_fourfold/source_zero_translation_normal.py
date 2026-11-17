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
expected=-((z*z+1)*B-2*z*D)/((z*z+1)*D-2*z*B)
assert S.factor(normal-expected)==0
assert S.factor((normal-1)/(normal+1)-((z-1)/(z+1))**2*(B+D)/(B-D))==0
vlin=(B-D*z)/2
Tlin=D-B*z
Blin=S.factor((2*vlin+Tlin*normal)/(1-normal**2))
Dlin=S.factor((Tlin+2*vlin*normal)/(1-normal**2))
eta_out=S.factor((Blin+Dlin)/(Blin-Dlin))
assert S.factor(eta_out-(z+1)/(z-1))==0
lam=S.symbols('lambda')
qbase=T-v*v+2*v
line_B=S.factor(-2*lam*qbase/(x1*x2))
line_normal=S.factor(S.limit(line_B.subs({B:eps*B,D:eps*D}),eps,0))
# The regular O(1) frame over C1 has coefficient w_cartier*z.
regular_ratio=S.factor(line_normal*normal/z)
wsource=(z-1)/(z+1)
wtarget=(normal-1)/(normal+1)
psource=S.factor(wsource*(B+D)/(B-D))
# Node-adapted line frame Vhat=(1-w)*V_regular.
hat_ratio=S.factor((1-wtarget)*regular_ratio/(1-wsource))
assert S.factor(hat_ratio+2*lam*psource)==0
nscale=B-D
nscale_out=S.factor(Blin-Dlin)
rscale=nscale/(1-wsource)
rscale_out=S.factor(nscale_out/(1-wtarget))
assert S.factor(rscale_out-rscale)==0
assert S.factor(2*vlin-rscale*(1-psource))==0
assert S.factor(Tlin+rscale*(1+psource))==0
normal_matrix=S.Matrix([[2,1],[-1,0]])
assert normal_matrix.det()==1
assert (normal_matrix-S.eye(2))**2==S.zeros(2)
uu,hh=S.symbols('u h')
num=-((z*z+1)*B-2*z*D)
den=(z*z+1)*D-2*z*B
np=S.expand(num.subs({z:1+uu,B:1+hh,D:1}))
dp=S.expand(den.subs({z:1+uu,B:1+hh,D:1}))
assert S.expand(np+dp+(uu+2)**2*hh)==0
assert S.expand(dp+2*(1+uu)*hh-uu**2)==0
nm=S.expand(num.subs({z:-1+uu,B:-1+hh,D:1}))
dm=S.expand(den.subs({z:-1+uu,B:-1+hh,D:1}))
assert S.expand(nm-dm+(uu-2)**2*hh)==0
assert S.expand(dm+2*(uu-1)*hh-uu**2)==0
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
 'meaning':'The second translation retains the quadratic old-curve factor: chi(z_target)=chi(z)^2*(B+D)/(B-D). It cannot be replaced by the identity or a bare exchange of rulings.',
 'normal_direction_matrix':[['-(z^2+1)','2z'],['-2z','z^2+1']],
 'normal_direction_determinant':'-(z^2-1)^2',
 'node_base_ideals':{'plus':'(numerator,denominator)=(h,u^2), because N+D=-(u+2)^2*h','minus':'(numerator,denominator)=(h,u^2), because N-D=-(u-2)^2*h'},
 'both_normal_cone_coordinates':{
   'w':'(z-1)/(z+1)','eta':'(B+D)/(B-D)',
   'w_out':'w^2*eta','eta_out':'w^(-1)',
   'exponent_matrix':[[int(e) for e in normal_matrix.row(i)] for i in range(2)],
   'invariant':'w*eta'
 },
 'actual_line_normal_cone':{
   'canonical_multiplier':str(line_normal),
   'regular_O1_frame_ratio':str(regular_ratio),
   'node_frame':'Vhat=(1-w)*V_regular',
   'node_frame_ratio':str(hat_ratio),
   'p':'w*eta',
   'r':'(B-D)/(1-w)',
   'full_map':'(w,p,r,Vhat)->(p*w,p,r,-2*lambda*p*Vhat)',
   'retained_base':'2v=r*(1-p), T=-r*(1+p)',
   'diagonal_Hopf_coordinates':'A=1/Vhat, C=w/Vhat: (A,C)->((-2lambda p)^(-1)A,(-2lambda)^(-1)C)',
   'scope':'normal-cone map with actual node divisor frame; global periodic quotient not inferred'
 },
 'remaining':'identify the full real-normal quaternion clutch and its period reset, including the line multiplier'
}
(ROOT/'code/part3_fourfold/source_zero_translation_normal.json').write_text(json.dumps(data,indent=2)+'\n')
with (ROOT/'records/literature_fourfold.md').open('a') as f:
    f.write('\n- '+data['utc']+' — Executed own source_zero_translation_normal.py. Material: exact two-step normal-cone map chi(z_target)=chi(z)^2*(B+D)/(B-D), retaining the first C1-to-C0 map s=-1/z. A proposed bare ruling exchange failed and is preserved in attempts/source_zero_normal_simple_guess; no return class assigned.\n')
print(json.dumps(data,indent=2))
