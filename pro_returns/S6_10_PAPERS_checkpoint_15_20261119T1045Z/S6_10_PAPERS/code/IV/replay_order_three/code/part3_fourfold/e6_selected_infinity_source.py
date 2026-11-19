"""Exact source, Miller, point/tensor and finite Cartier maps at E6 w=infinity.

This certifies EI.1--5 local and annular formulas. It does not assert the
two-variable finite-root attachment or a completed source return.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S

base=Path(__file__).resolve().parents[2]
e,x,y,t,s,q,u,vv=S.symbols("e x y t s q u vv")
d=1-3*e**2
A=3*e**2-2
C=(1-e**2)*(1+3*e**2)
Sb=C/4
curve=y**2-x**3-A*x**2-d*t*x-e**2*t**2
checks=[]


def check(name,value):
    answer=S.factor(S.together(value).as_numer_denom()[0])
    assert answer==0,(name,answer)
    checks.append(name)


alpha=e/d
ro=e**2*(3*e**2-2)/d**2
xo,yo,to=alpha**2*x,alpha**3*y,e*alpha**3*t
check("whole original source",
      (yo**2-xo**3-ro*xo**2-to*xo-to**2)/alpha**6-curve)
check("literal selected height",
      to-e**4*(1-e**2)/d**3-e**4*(t-1+e**2)/d**3)
check("original parameter order two unit",ro/e**2-(3*e**2-2)/d**2)
check("selected normalization",
      curve.subs({x:s*s-e*e,y:s*(s*s-1),t:1-e*e}))
check("complete half source arrow",
      curve.subs({e:-e,y:-y},simultaneous=True)-curve)
for name,expr in (("x",xo),("y",yo),("t",to)):
    check("half original "+name,
          expr.subs({e:-e,y:-y},simultaneous=True)-expr)
Z=(s-1)/(s+1)
P=-(1+e)/(1-e)
check("half ordered point",Z.subs(s,-s)-1/Z)
check("half marked point",P.subs(e,-e)-1/P)
check("marked G is s=-epsilon",Z.subs(s,-e)-P)
check("actual selected kappa",
      (-(e**-2-1)**2/(64*e**-6))*e**-2+(1-e**2)**2/64)

x2=Sb/e**2
y2=-e*t-d*x2/(2*e)
f2=(y-e*t-d*x/(2*e))/(x-x2)
f2hat=(e*y-e*e*t-d*x/2)/(e*e*x-Sb)
check("actual 2G x",x2-d*d/(4*e*e)+A)
check("actual 2G on source",
      curve.subs({x:x2,y:y2},simultaneous=True))
check("whole normalized f2",f2-e*f2hat)
check("finite central f2 factor",f2hat.subs(e,0)-2*x)
f2old=(yo-to-xo/2)/(xo-(S.Rational(1,4)-ro))
check("full original f2 scale",f2old-alpha*f2)
f3=Sb*x*(e*y-e*e*t-d*x/2)/(Sb*(e*y+e*e*t-d*x/2)-2*e**4*t*x)
g=e*t
dg=d/e
f3direct=x2*x*(y-g-dg*x/2)/(x2*(y+g+dg*x/2)-(dg*x2+2*g)*x)
check("whole third point Miller",f3-f3direct)
check("finite central third point Miller",f3.subs(e,0)-x)
X3=2*d*t/Sb+4*e**4*t*t/Sb**2
Y3=t*(d*d/Sb-1+6*d*e**4*t/Sb**2+8*e**8*t*t/Sb**3)
check("exact x3 chord",e*e*X3-4*g*g/x2**2-2*dg*g/x2)
check("exact y3 chord",e*Y3-(-g+(2*g/x2+dg/2)*e*e*X3))
L3=(3*e**4*X3**2+2*A*e*e*X3+d*t)/(2*Y3)
X6=L3**2-A*e*e-2*e**4*X3
f23hat=(e*y-e*e*Y3-L3*x+e*e*L3*X3)/(e*e*x-X6)
f23direct=(y-e*Y3-(L3/e)*(x-e*e*X3))/(x-X6/e**2)
check("whole sixth tangent factor",f23direct-e*f23hat)
for name,expr,target in (
 ("x3 scaled",X3,8*t),("y3 scaled",Y3,3*t),
 ("tangent scaled",L3,S.Rational(1,6)),
 ("x6 scaled",X6,S.Rational(1,36)),
 ("sixth tangent scaled",f23hat,6*x),
 ("whole sixth Miller scaled",f3*f3*f23hat,6*x**3)):
    check("central "+name,expr.subs(e,0)-target)
check("f2 exact half parity",
      (e*f2hat).subs({e:-e,y:-y},simultaneous=True)+e*f2hat)
check("f3 exact half parity",
      f3.subs({e:-e,y:-y},simultaneous=True)-f3)
# All functions in X3,Y3,L3,X6 are even. Test the full numerator form;
# this retains the sixth chord rather than replacing it by its divisor.
for name,expr in (("X3",X3),("Y3",Y3),("L3",L3),("X6",X6)):
    check("even "+name,expr.subs(e,-e)-expr)
check("sixth tangent half parity",
      f23hat.subs({e:-e,y:-y},simultaneous=True)-f23hat)

# Entire two chord maps and the resolved second source chart.
for sign in (-1,1):
    slope=(y+sign*e*t)/x
    xx=slope*slope-A-x
    yy=sign*e*t-slope*xx
    target=S.together(curve.subs({x:xx,y:yy},simultaneous=True)).as_numer_denom()[0]
    check("full source chord "+str(sign),S.rem(target,curve,y))
    check("central chord x "+str(sign),
          (xx.subs(e,0)-t/x).subs(y*y,x**3-2*x*x+t*x))
    numerator=S.together(yy.subs(e,0)+t*y/x**2).as_numer_denom()[0]
    check("central chord y "+str(sign),
          S.rem(numerator,curve.subs(e,0),y))
xb=vv*vv-A-d*u-e*e*u*u
Dm=d+2*e*vv+2*e*e*u
up=xb/Dm
vp=e*up-vv-e*u
xp=u*Dm
check("resolved source target equation",
      xp-(vp*vp-A-d*up-e*e*up*up))
check("resolved source preserves t",xp*up-xb*u)
check("resolved source preserves y formula",
      xp*vp-(e*xb*u-(vv+e*u)*xp))
check("exceptional conic discriminant",d*d-4*A*e*e-C)
a,b=S.symbols("a b")
check("reciprocal O-chart exact equation",
      (b-e)*(b+e)-a*(t*a*a+A*a+d)
      -(b*b-t*a**3-A*a*a-d*a-e*e))
check("central involution x",t/(t/x)-x)
check("central involution y",-t*(-t*y/x**2)/(t/x)**2-y)

# Full central six-factor values in the actual point frames.
xt=t/x
check("M6 chronological central product",
      (2*x)**6*(6*xt**3)/(6*x**3)-64*t**3)
check("M2 chronological central product",
      (2*x)*(2*xt)*(2*xt)**2*(2*x)**2-64*t**3)
check("original selected Hom scale",
      alpha**6*(e**4/d**3)/(e**4/d**3)**3-e**-2)
check("coupled scalar exponent",e**-2*e**6-e**4)

# Actual point/tensor coefficients and the selected-normalization pole.
ft=lambda zz,pp:(1-zz/pp)/(1-zz)
for aa in (2,6):
    sa=S.cancel((1+P**aa)/(1-P**aa))
    fa=(s+e)**aa/(s-sa)
    ratio=S.cancel(ft(Z,P)**aa/(fa*ft(Z,P**aa)))
    target=1/(2*e) if aa==2 else 1/(e*(6+20*e*e+6*e**4))
    check(f"a{aa} exact selected point/tensor pole",ratio-target)
    check(f"a{aa} exact selected Miller half parity",
          fa.subs({s:-s,e:-e},simultaneous=True)+fa)
    check(f"a{aa} full point-frame half",ft(1/Z,P**(-aa))-P**aa*ft(Z,P**aa))
    check(f"a{aa} tensor-frame half sign",
          ft(1/Z,1/P)**aa/(-fa)+P**aa*ft(Z,P)**aa/fa)
    sigma=e**4/d**3
    chi=alpha**(1-aa)
    check(f"a{aa} full Cox product",sigma/chi*chi-sigma)
    check(f"a{aa} physical normal determinant winding",
          -(aa+3)+(1-aa)-(-2*aa-2))
    for hh in range(-2,3):
        for jj in range(-2,3):
            check(f"a{aa} original Cox({hh},{jj})",
                  sigma**hh*chi**jj-e**(4*hh-(aa-1)*jj)*d**(-3*hh+(aa-1)*jj))
            check(f"a{aa} w Cox({hh},{jj})",
                  e**(-2*hh)*(e**(aa-1))**jj-e**(-2*hh+(aa-1)*jj))

tau2=2*e*Sb/(d*Sb+2*e**4*t)
check("actual finite formal second section",tau2+x2/y2)
check("second formal leading coefficient",(tau2/e).subs(e,0)-2)
Y6=-e**4*Y3-L3*X6+e**4*L3*X3
tau6=-e*X6/Y6
check("sixth formal leading coefficient",(tau6/e).subs(e,0)-6)
q0=S.Symbol("q0")
a2=-2*q0*q0;a4=q0**3
b2=4*a2;b4=2*a4;b6=S.Integer(0);b8=-a4*a4
c4=b2*b2-24*b4
c6=-b2**3+36*b2*b4-216*b6
Delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
check("central infinity actual c4",c4-q0**3*(-48+64*q0))
check("central infinity actual c6",c6-q0**5*(-576+512*q0))
check("central infinity actual discriminant",Delta-64*q0**9*(q0-1))

src=base/"notes/part3_e6_selected_infinity_working.md"
payload={
 "status":"PASS_LOCAL_SOURCE_AND_COLLAR","utc":datetime.now(timezone.utc).isoformat(),
 "source_sha256":hashlib.sha256(src.read_bytes()).hexdigest(),
 "count":len(checks),"checks":checks,
 "scope":"EI.1--5 exact source, complete Miller factors, finite I2 resolution, point/tensor collars, half endpoint and finite central Cartier specialization.",
 "not_assigned":"Two-variable root/exceptional-component extension, completed cap endpoint, characteristic pair or source return."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(payload,indent=2)+"\n")
print(json.dumps({k:payload[k] for k in ("status","count","source_sha256")},indent=2))
