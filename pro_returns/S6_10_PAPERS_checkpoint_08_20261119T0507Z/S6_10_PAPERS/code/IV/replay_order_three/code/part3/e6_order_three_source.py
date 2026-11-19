"""Exact source and Miller identities; no completed quotient or return asserted."""
from pathlib import Path
import sympy as S,json
x,y,t,s,z,w=S.symbols("x y t s z w")
F=y*y-x**3-(S.Rational(1,4)-s)*x*x-t*x-t*t
U=y-t-x/2;V=y+t+x/2
checks=[]
def red(f):
 n,d=S.fraction(S.cancel(f))
 return S.cancel(S.rem(S.Poly(n,y),S.Poly(F,y)).as_expr()/d)
def ck(name,f):
 assert S.factor(f)==0,(name,S.factor(f))
 checks.append(name)
ck("cA2",red(U*V-x*x*(x-s)))
lam=-2*t/s-S.Rational(1,2);xp=2*t*(2*t+s)/s**2
Lp=y-t-lam*x;Lm=y+t+lam*x
ck("chord_product",red(Lp*Lm-x*(x-s)*(x-xp)))
ck("f3_arrow",red(U*Lp/((x-s)*(x-xp))-x*U/Lm))
ck("f3_retained_base",S.cancel(x*U/Lm-s*x*U/(s*V-(s+2*t)*x)))
xx=s+z*w;yy=xx*(z+w)/2;tt=xx*(w-z-1)/2
ck("full_chart",S.expand(F.subs({x:xx,y:yy,t:tt},simultaneous=True)))
zp=s/z+w-z-1;wp=-z
ck("translation_x",S.cancel(s+zp*wp-(s-xx+z*(z+1))))
zi=-wp;wi=s/wp+zp-wp+1
ck("inverse_z",zi-z);ck("inverse_w",S.cancel(wi-w))
X,Y,Z,rr=S.symbols("X Y Z rr")
ck("quadratic_root",S.expand((Z**3*Y)**2-(Z**2*X)**3-rr*(Z**2)**2*(Z**2*X)**2-(Z**2)**3*(Z**2*X)-(Z**2)**4-Z**6*(Y**2-X**3-Z**2*(rr*X**2+X+1))))
out={"status":"PASS","count":len(checks),"checks":checks,"scope":"explicit source and rational Cartier identities only; full M6/root line attachment remains working"}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out))
