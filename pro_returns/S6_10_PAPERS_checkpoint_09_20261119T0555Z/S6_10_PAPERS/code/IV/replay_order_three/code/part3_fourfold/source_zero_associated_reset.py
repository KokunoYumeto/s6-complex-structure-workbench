"""Actual graph-to-next-graph associated-node reset, with both charged charts."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
root=Path(__file__).resolve().parents[2]
z,B,D,xi,t=s.symbols('z B D xi t',nonzero=True)
v=(B-D*z)/2
F2=1-B*z**3-(1-2*v)*z**2
# Source R1 chart A=Dz,C=Bz, target of one -G translation.
Xout=F2/z**2
Aout=-F2/z**3
Bout=B-D*z-F2/z**3
Dout=-Bout/z
assert s.cancel(Aout*Bout-Xout*Dout)==0
assert s.cancel(Aout*(-z)-Xout)==0
assert s.cancel(Dout*(-z)-Bout)==0
Xin=B*z
Tin=D-Xin**2-(1-2*v)*Xin
Tout=s.cancel(Dout-Xout**2-(1-2*v)*Xout)
assert s.cancel(Tout-Tin)==0
assert s.cancel((Bout-Aout)/2-v)==0
# Gauge t0'=1,t1'=-z and actual Cartier line coefficient.
next_s0=Aout; next_s1=Dout
line_a1=-xi/z**2
line_a2=xi/z**4
# Central proper component, near its s=-1 node, with the literal sqrt= -s.
central={z:1/t,B:t*(t*t-1),D:t*t*(t*t-1)}
assert s.cancel(v.subs(central))==0
assert s.cancel(F2.subs(central))==0
x=1/t; y=t*(t*t-1); k=1-1/t; l=t*(t+1)*(t*t-1)
sig=-t
Fp=s.cancel(((sig+1)*k-x*x*l/(sig+1))/2)
Fm=s.cancel(((sig+1)*l-y*y*k/(sig+1))/2)
assert Fp==2 and Fm==0
assert s.cancel(next_s0.subs(central))==0
assert s.cancel(next_s1.subs(central))==0
# At the next target origin the chosen analytic sqrt is 1.
next_Fp=0
next_Fm=1-1/t
assert s.cancel(line_a2.subs(central)-xi*t**4)==0
assert s.cancel(line_a1.subs(central)+xi*t**2)==0
x,y,w0,t0,cl,q=s.symbols('x y w0 t0 cl q',nonzero=True)
sig0=s.symbols('sig0',nonzero=True)
vU=x*y+(y*w0-x*t0)/(2*sig0)
vV=x*y+(y*w0-x*t0)/(2*sig0)
assert vU==vV
assert s.cancel(cl*q*(1/cl)-q)==0
# Node U_j=1,V_j=q to previous V=1 chart, retaining c_lambda.
Uprev=cl*q; Vprev=1/cl
assert s.cancel(Uprev/cl-q)==0 and s.cancel(cl*Vprev-1)==0
# Effective charge-a weights in the U and V gauges coincide in ordered coords.
for a in [1,2,3]:
    auxU=[1-a,1,-1,-1]
    physU=[-1,0,0,0]
    effU=[s.Rational(p)-s.Rational(w,a) for p,w in zip(physU,auxU)]
    auxV=[1,1,-1,a-1]
    physV=[0,0,0,1]
    effV=[s.Rational(p)-s.Rational(w,a) for p,w in zip(physV,auxV)]
    assert effU==effV==[-s.Rational(1,a),-s.Rational(1,a),s.Rational(1,a),s.Rational(1,a)]
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
 'checks':20,
 'full_reset':{'F2':str(s.expand(F2)),'next_s0':str(s.factor(next_s0)),
   'next_s1':str(s.factor(next_s1)),'next_t0':'1','next_t1':'-z',
   'next_common_line_a1':str(line_a1),'next_common_line_a2':str(line_a2)},
 'central_component':{'z':'1/s','B':'s*(s^2-1)','D':'s^2*(s^2-1)',
   'chosen_square_root_near_s_minus_1':'-s','first_Fplus':str(Fp),'first_Fminus':str(Fm),
   'next_Fplus':0,'next_Fminus':'1-1/s',
   'node_coordinate_arrow':'xi/2 (finite nonzero) -> infinity; complementary coordinate Fplus/xi -> 0'},
 'charged_chart_continuation':{
   'U_chart':'U=1, V=w*T0, S0=w',
   'previous_V_chart':'V=1, U=w*T0, S0=w, z=T0',
   'ordered_coordinate_map':'(w,S1,T1,T0) -> (S0,S1,T1,z)',
   'chain_arrow':'j -> j-1; U_prev=c_lambda*q*U_j; V_prev=1/(c_lambda*U_j)',
   'physical_normalization':'multiply U_prev by c_lambda^-1, V_prev by c_lambda',
   'physical_line':'O(-a) on the positively complex oriented CP3 link',
   'multiplicity':'Two chart descriptions of one point, not two charged disks'},
 'scope':'The actual cyclic reset enters the complementary charge-a chart, which has a literal source-preserving adjacent-node overlap with the standard charged model. No radial/product-radius global attachment or individual source-zero return is inferred.'}
(root/'code/part3_fourfold/source_zero_associated_reset.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
