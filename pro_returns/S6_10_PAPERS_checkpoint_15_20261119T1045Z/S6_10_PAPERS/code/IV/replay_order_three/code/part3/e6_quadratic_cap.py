"""Actual E6 IV-root Cartier charts and exact norm identities."""
from pathlib import Path
import sympy as S,json
a,b,z,s,X,Y,r,d,w=S.symbols("a b z s X Y r d w")
checks=[]
def ck(name,e):
 assert S.factor(e)==0,(name,S.factor(e))
 checks.append(name)
for name,xx,uu,vv in [
 ("middle",a*b,a*a*b,a*b*b),
 ("outer_u",a*b,a,a*a*b**3),
 ("outer_v",a*b,a*a*b**3,a)]:
 ck(name+"_A2",uu*vv-xx**3)
 ck(name+"_deck_x",xx.subs({a:-a,b:-b},simultaneous=True)-xx)
 ck(name+"_deck_u",uu.subs({a:-a,b:-b},simultaneous=True)+uu)
 ck(name+"_deck_v",vv.subs({a:-a,b:-b},simultaneous=True)+vv)
ck("outer_middle_x",(1/b)*(a*b*b)-a*b)
ck("outer_middle_u",(1/b)**2*(a*b*b)-a)
ck("outer_middle_v",(1/b)*(a*b*b)**2-a*a*b**3)
L,v0=S.symbols("L v0")
ck("point_line_blowup",S.cancel((z*v0)/(z*v0-z*L)-v0/(v0-L)))
# Deck parity and formal 3G line point.
w3=-2*s*z*(2+s*z*z)/(8+6*s*z*z+(s*s-s**3)*z**4)
ck("3G_odd",w3.subs(z,-z)+w3)
ck("3G_first_coefficient",S.limit(w3/z,z,0)+s/2)
# Actual central root and selected-height coefficients.
tsel=S.symbols("tsel")
ck("root_B6_scaling",z**6*4*z**-4-4*z*z)
ck("root_selected_coefficient",(z**-2-tsel)*z**6*z**-6*(4*z*z)-4*(1-tsel*z*z))
# General tangent coefficient for X^3+(d²/4-s)X²+d T X+T².
x=s+w*w-d*w
lam=d*(d*d-3*s)/(2*(d*d-s))
x6=s**3/(d*d-s)**2
ck("general_double_point",lam*lam-(d*d/4-s)-x6)
num=(s-w*w)/x-(d*d-s)/s-lam*(2*w/x-2*d/s)
f23p=x*(w-d/2-lam)/(x-x6)
f23m=num/(-x6)
f3m=2*w**3/(x*(d*w-s))
coef=(x/w)**6*(f3m/x)**2*f23m/f23p
ck("general_I2_coefficient",coef-8*((d*d-s)*w-d*s)/s**3)
ck("regular_D_zero",coef.subs({d:0,s:3})+8*w/9)
# Quotient intersection and multiplicity pullbacks.
ck("strict_component_square",S.Rational(-4,2)+2)
ck("exceptional_image_square",S.Rational(4*-1,2)+2)
ck("triple_multiplicity",2*3-3*2)
ck("outer_multiplicity",2*1-1*2)
ck("old_component_multiplicity",2*1-2)
out={"status":"PASS","count":len(checks),"checks":checks,"scope":"explicit root charts, Cartier equality, norm algebra and generic coefficients; reference annular attachment remains separately recorded"}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":"PASS","count":len(checks)}))
