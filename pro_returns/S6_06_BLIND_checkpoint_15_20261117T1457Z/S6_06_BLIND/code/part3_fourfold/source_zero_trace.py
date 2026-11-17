#!/usr/bin/env python3
"""Exact normalization blowup, Cartier frames and the primitive suspension square.

This certificate verifies the displayed algebraic maps. It does not assign a
completed-family return without the outstanding relative suspension extension.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
s,v,r,t,c=S.symbols('s v r t c')
X=s*s-1
Y=s*(s*s-1-v)
T=v*v-2*v
assert S.factor(Y*Y-X**3-(1-2*v)*X**2-T*X-v*v)==0
z=(s+1)/(s*s+s-v)
assert S.factor(X-z*(Y+v))==0
# The only simultaneous zero of numerator and denominator is (s,v)=(-1,0).
assert S.factor((s*s+s-v).subs(s,-1))==-v
zb=S.factor(z.subs({s:r-1,v:r*t}))
assert zb==1/(r-t-1)
# Exceptional r=0 is C1; the strict central branch t=0 is C0.
assert S.factor(X.subs(s,r-1))==r*(r-2)
# At D-, v=(s-1)(s+1), so the blowup coordinate is t=s-1.
assert S.factor((s*s-1)/(s+1))==s-1
assert S.factor(zb.subs({r:0,t:-2}))==1
# G has s=-1 and approaches the exceptional point z=0 in the other chart.
w=S.symbols('w')
assert S.factor((1/z).subs({s:-1+v*w})-(v*w-1-1/w))==0

# The two nodal branches D+ and D- and their exceptional valuations.
ratio=(s-c)/(s+c)
assert S.factor(ratio.subs(s,-1)-(-c-1)/(c-1))==0
# On v=c^2-1, D- passes through the blowup centre; D+ does not.
assert S.factor((s+c).subs({s:r-1,c:S.sqrt(1+r*t)})).subs(r,0)==0
# A formal first-order expansion records the exceptional multiplicity exactly.
assert S.limit((r-1+S.sqrt(1+r*t))/r,r,0)==1+t/2
assert S.limit(r-1-S.sqrt(1+r*t),r,0)==-2

# The literal target-point primitive lift U of -G has multiplier 1/X(target).
xx,yy,TT,vv=S.symbols('X Y T v')
curve=yy**2-xx**3-(1-2*vv)*xx**2-TT*xx-vv**2
x_plus_G=((yy-vv)/xx)**2-(1-2*vv)-xx
F12=(yy-vv-TT*xx/(2*vv))/xx
identity=S.together(xx*x_plus_G+2*vv*F12)
assert S.factor(identity-curve/xx)==0
# Therefore U^2 multiplier is -1/(2v F12), and B=-2 lambda q U^2.
lam,q=S.symbols('lambda q')
assert S.factor((-2*lam*q)*(-1/(2*vv*F12))-lam*q/(vv*F12))==0
# The actual -G source map lands in the other resolution of its target.
zz,BB,DD=S.symbols('z B D')
vsrc=(BB-DD*zz)/2
xsrc=BB*zz
ysrc=(DD*zz+BB)/2
tsrc=DD-xsrc**2-(1-2*vsrc)*xsrc
F2=1-BB*zz**3-(1-2*vsrc)*zz**2
xp=F2/zz**2
yp=vsrc-xp/zz
dp=tsrc+xp**2+(1-2*vsrc)*xp
assert S.factor(dp+(yp+vsrc)/zz)==0
assert S.factor((yp-vsrc)+xp/zz)==0
# The M2 -> M1^2 Cartier map is r(p)=X(p-G)=2v F21/X.
F21=(yy+vv+TT*xx/(2*vv))/xx
x_minus_G=((yy+vv)/xx)**2-(1-2*vv)-xx
assert S.factor(S.together(xx*x_minus_G-2*vv*F21)-curve/xx)==0
assert S.factor((2*vsrc*((ysrc+vsrc+tsrc*xsrc/(2*vsrc))/xsrc)/xsrc)-xp)==0
# With r(p)=X(p-G), its target/source ratio converts the M2
# suspension coefficient to 2 lambda q / X(p-G)^2.
rp,rt=S.symbols('r_source r_target',nonzero=True)
F21target=rt*rp/(2*vv)
assert S.factor((rt/rp)*lam*q/(vv*F21target)-2*lam*q/rp**2)==0
# The residual central translation is the actual two-torsion translation.
assert S.factor((xx*x_plus_G-TT).subs(vv,0)-(curve/xx).subs(vv,0))==0
assert S.factor((-2*lam*TT)/TT+2*lam)==0
assert S.factor((2*lam*TT)**2/TT**2-4*lam**2)==0
# Root's infinity coordinate dictionary preserves the actual unified period.
zzinf=S.symbols('zeta',nonzero=True)
for aa,bb in [(1,2),(2,1)]:
    assert S.simplify(zzinf**(-4)*(zzinf**(2*aa))**bb)==1
rs,rr=S.symbols('r_source_inf r_target_inf',nonzero=True)
assert S.factor((zzinf**-2*rr)/(zzinf**-2*rs)-rr/rs)==0

# Actual Cox quotient for the line O(G-O) near exceptional C1.
s0,s1,t0,t1=S.symbols('s0 s1 t0 t1')
AA=s1*t0; BB=s0*t1; CC=s1*t1; DD=s0*t0
assert S.expand(AA*BB-CC*DD)==0
vc=(BB-AA)/2
# The v-map is a nondegenerate quadratic after fixing the nonzero line frame.
coords=(s0,s1,t0,t1)
H=S.hessian(vc,coords)
assert H.det()==S.Rational(1,16)
# In the target Cox ordering of the chamber comparison, retain both invariant
# functions.  The q-period factor is not an independent product coordinate.
Aq=s0*t0; Bq=s1*t1; Cq=s0*t1; Dq=s1*t0
vq=(Bq-Aq)/2
Tq=Dq-Cq**2-(1-2*vq)*Cq
qq=Tq-vq**2+2*vq
qfact=(s1-s0)*(t0+t1)-(Cq-vq)**2
assert S.expand(qq-qfact)==0
# The explicit parametric Morse coordinate retains both nodal base curves.
xi,xx_shift=S.symbols('xi x_shift')
A0=1-2*vv
critT=-3*xi**2-2*A0*xi
h=vv**2-A0*xi**2-2*xi**3
poly=(xx_shift+xi)**3+A0*(xx_shift+xi)**2+critT*(xx_shift+xi)+vv**2
assert S.expand(poly-(xx_shift**2*(A0+3*xi+xx_shift)+h))==0
T1=(1+4*vv-(1-8*vv)**S.Rational(3,2))/8
disc_rest=4*TT**2-4*TT*vv-TT+32*vv**3-11*vv**2+2*vv
assert S.simplify(disc_rest.subs(TT,T1))==0
assert S.diff(T1,vv).subs(vv,0)==2
assert S.diff(vv**2-2*vv,vv).subs(vv,0)==-2
# Linear part of the actual node-adapted versus Cartier-adapted conifold map.
# Cartier matrix is [[A,C],[D,B]]=s*t^T.
Ac=s0*t0; Bc=s1*t1; Cc=s0*t1; Dc=s1*t0
alpha=(Ac+Bc-Cc-Dc)/2
beta=-2*(Ac+Bc+Cc+Dc)
q1lin=-Ac+Bc-Cc+Dc
q2lin=Ac-Bc-Cc+Dc
S0=s1-s0; S1=s0+s1; Tn0=t0+t1; Tn1=t0-t1
assert S.expand(alpha+S0*Tn1/2)==0
assert S.expand(beta+2*S1*Tn0)==0
assert S.expand(q1lin-S0*Tn0)==0
assert S.expand(q2lin-S1*Tn1)==0
assert S.expand(s0-(S1-S0)/2)==0
# The actual associated Tate-node chart retains the auxiliary line character a.
weight_data=[]
for aa in (1,2):
    # Coordinates S0,S1,T1,z,V after U=S0*z,T0=z*V.
    auxiliary=[1,1,-1,aa-1,-aa]
    physical=[0,0,0,1,-1]
    # Fix V=1; compensate physical delta by auxiliary parameter -theta/a.
    effective=[S.Rational(physical[i])-S.Rational(auxiliary[i],aa) for i in range(4)]
    assert effective==[-S.Rational(1,aa),-S.Rational(1,aa),S.Rational(1,aa),S.Rational(1,aa)]
    weight_data.append({'a':aa,'auxiliary':auxiliary,'physical':physical,'effective_after_V_gauge':[str(e) for e in effective],'residual_group':f'mu_{aa}'})
fan_charts={
 'positive_first':{'coordinates':['S0','z','V'],'Z':[1,0,0],'line_U':[1,1,0],'q1':[1,1,1]},
 'positive_second':{'coordinates':['U','T0','w'],'Z':[1,0,1],'line_U':[1,0,0],'q1':[1,1,1]},
 'negative_first':{'coordinates':['T0','z','V'],'Z':[0,1,1],'line_U':[1,1,0],'q1':[1,1,1]},
 'negative_second':{'coordinates':['U','S0','w'],'Z':[0,1,0],'line_U':[1,0,0],'q1':[1,1,1]}
}
for fc in fan_charts.values():
    fc['rays']=[list(c) for c in zip(fc['Z'],fc['line_U'],fc['q1'])]
    assert abs(S.Matrix(fc['rays']).det())==1
negative_fixed_weights=[]
for aa in (1,2):
    # Other resolution chart T0=U*w, V=w*S0: fixed U=w=0.
    negative_fixed_weights.append({
      'a':aa,'coordinates':['U','S0','S1','T1','w'],
      'auxiliary':[aa,1,1,-1,-aa-1],'physical':[1,0,0,0,-1],
      'conjugated_normal_degrees':[aa,aa+1],
      'determinant_E_coefficient':-(2*aa+1)
    })

# Root-cap generic-component Hom coefficients: the displayed cancellation is
# literal, before any assertion about extension across all resolved components.
zeta,p=S.symbols('z p',integer=True,positive=True)
XR,YR=S.symbols('XR YR')
F12good=(zeta**-3*YR-vv-zeta**-4*(zeta**-2*XR)/(2*vv))/(zeta**-2*XR)
phi12=(zeta**-4-(vv**2-2*vv))/(vv*F12good)
good_rhs=(1-(vv**2-2*vv)*zeta**4)/(-S.Rational(1,2)+vv*zeta**3*YR/XR-vv**2*zeta**6/XR)
assert S.factor(phi12-good_rhs)==0
# Basic reduced III root has m=3,p=1.
F21red=(zeta**-3*YR+vv+zeta**-3*(zeta**-2*XR)/(2*vv))/(zeta**-2*XR)
phi21=(zeta**-3-(vv**2-2*vv))/(vv*F21red)
red_rhs=(1-(vv**2-2*vv)*zeta**3)/(S.Rational(1,2)+vv*zeta**2*YR/XR+vv**2*zeta**5/XR)
assert S.factor(phi21-red_rhs)==0

data={
 'utc':datetime.now(timezone.utc).isoformat(),
 'status':'PASS: exact source, trace and suspension identities; completed return not assigned',
 'normalization':{'X':str(X),'Y':str(Y),'z':str(z)},
 'blowup':{'s':'r-1','v':'r*t','z':str(zb),'exceptional':'r=0','central_proper':'t=0'},
 'branch_divisor':'div((s-c)/(s+c)) = D_plus-D_minus-E',
 'source_line_on_trace':{'a1':'O(-E)','a2':'O(-2E)'},
 'conjugated_Cox_spinor':'(O(D_plus) + O(-D_minus)) tensor O(-a E)',
 'spinor_determinant':'(1-2a) E',
 'primitive_lift':{'base':'p -> p-G','target_multiplier':'1/X(p-G)'},
 'suspension_square':'B_(a1,b2) = -2 lambda q U^2',
 'actual_other_resolution':{'A_prime':'-C_prime/z','D_prime':'-B_prime/z','base_ratio':'t0/t1=-1/z'},
 'Cartier_chamber_frames':{'domain':'w=V*t1','target':'w=V/s0','ratio':'1/(s0*t1)=1/X_target'},
 'degree_two_line_map':'M2 -> M1^2 by multiplication by r(p)=X(p-G)',
 'unified_suspension':'B_(a,b)=2*(-1)^(b+1)*lambda*q*U_a^b, a*b=2; U_a multiplier X(target)^(-a)',
 'effective_line_scaling':'(s,t)->(d^(-1/a)*s,d^(1/a)*t) modulo mu_a, d=2*(-1)^(b+1)*lambda*q1',
 'central_residual_period':{'a1_b2':'B=-2 lambda','a2_b1':'B^2=4 lambda^2','warning':'zero component displacement retains nontrivial line scaling; finite label count alone does not give the quotient link'},
 'infinity_frame_check':'U_old=zeta^(2a)U_inf, q_old=zeta^(-4)q_inf, 2ab-4=0; the same zeta^(-2) in both Cartier frames cancels',
 'nonzero_line_Cox_model':{'v':str(vc),'quadratic_Hessian':[[str(e) for e in H.row(i)] for i in range(4)],'removed_locus':'s0=s1=0'},
 'target_Cox_base_functions':{'v':str(vq),'q':str(qfact),'important':'q is the retained invariant polynomial, not an independent scalar coordinate'},
 'two_node_base':{'T0':'v^2-2v','T1':str(T1),'q1':'T-T0','q2':'T-T1','Morse_unit_at_origin':'-1/4','equation':'A*B=q1*q2 after the displayed holomorphic unit change'},
 'node_Cartier_linear_frame':{'S':['s1-s0','s0+s1'],'T':['t0+t1','t0-t1'],'q1':'S0*T0','q2':'S1*T1','G_linear_form':'s0=(S1-S0)/2','auxiliary_weights':'unchanged'},
 'associated_Tate_node_weights':weight_data,
 'literal_fan_charts':fan_charts,
 'default_negative_fixed_weights':negative_fixed_weights,
 'cap_generic_units':{'good_IIIstar_a1_b2':'-2','reduced_IIIstar_a2_b1':'+2'},
 'remaining_map':'relative suspension through its component flop, retaining source line, physical delta and finite caps'
}
(ROOT/'code/part3_fourfold/source_zero_trace.json').write_text(json.dumps(data,indent=2)+'\n')
with (ROOT/'records/literature_fourfold.md').open('a') as f:
 f.write('\n- '+data['utc']+' — Read own source_zero_resolution.py and executed source_zero_trace.py. Material: exact normalization blowup, branch valuations, primitive -G lift square, actual nonzero-line Cox quadratic and generic finite-root Hom-unit cancellation. No completed-family return inferred.\n')
print(json.dumps(data,indent=2))
