"""Exact retained Miller leading coefficients at generic I2."""
from pathlib import Path
import sympy as S,json
s,w,z,t=S.symbols("s w z t")
x=s+w*w-w
checks=[]
def ck(name,expr):
 assert S.factor(expr)==0,(name,S.factor(expr))
 checks.append(name)
lam=(1-3*s)/(2*(1-s));x6=s**3/(1-s)**2
ck("double_x_limit",lam**2-(S.Rational(1,4)-s)-x6)
num=(s-w*w)/x-(1-s)/s-lam*(2*w/x-2/s)
ck("tangent_numerator_first_order",num+2*(w-s)**2/((1-s)*x))
f23p=x*(w-S.Rational(1,2)-lam)/(x-x6)
ck("source_tangent_factor",f23p-x*(1-s)/((1-s)*w-s))
f23m=num/(-x6)
ck("target_tangent_factor_first_order",f23m-2*(1-s)*(w-s)**2/(s**3*x))
f3m=2*w**3/(x*(w-s))
B=(x/w)**6*(f3m/x)**2*f23m/f23p
ck("full_B6_order_three_coefficient",B-8*((1-s)*w-s)/s**3)
# Exact central translation and retained coefficient.
xc=z*w;tc=xc*(w-z-1)/2
zm=-w;wm=z-w+1;um=zm**2*wm;up=z*z*w
ck("central_U_ratio",um/up+2*tc/z**3)
ck("central_B6_limit",z**6*(um/up)**2-4*tc**2)
# Principal base divisor arithmetic, rows F0, F_selected, F_infty.
divB=S.Matrix([3,0,-2]);divfactor=S.Matrix([-3,1,2])
ck("selected_zero_divisor",sum(v*v for v in divB+divfactor-S.Matrix([0,1,0])))
out={"status":"PASS","count":len(checks),"checks":checks,
"generic_vertical_divisor":{"F0":3,"Finfinity":-2},
"selected_rigidification":"Bsel=(t-t_selected)*B6/t^3",
"central_limit":"4*(t-t_selected)/t",
"scope":"local coefficient identities and divisor accounting; global prescribed scalar/root/closing comparison remains explicit"}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out))
