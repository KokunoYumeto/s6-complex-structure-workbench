from pathlib import Path
import datetime, hashlib, json
import sympy as S

root=Path(__file__).resolve().parents[1]
r=S.symbols('r')
a=-3*r*(r**3-1)
b=2*(r**3-1)**2
y=S.sqrt(2)*(r**3-1)
assert S.expand(y*y-b)==0
ell2=a/(2*y)
x2=S.factor(ell2**2)
y2=S.factor(-ell2*x2-y)
ell3=S.factor((y2-y)/x2)
x3=S.factor(ell3**2-x2)
y3=S.factor(-ell3*x3-y)
assert S.factor(y2**2-x2**3-a*x2-b)==0
assert S.factor(y3**2-x3**3-a*x3-b)==0
u3=S.factor(-x3/y3)
leading=S.simplify(S.limit(u3/r**2,r,0))
assert leading==9*S.sqrt(2)/32
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'method':'Exact chord-and-tangent tripling in the smooth r^3=t Weierstrass model; formal parameter at the identity.',
 'a':str(a),'b':str(b),'P_y':str(y),'double_x':str(x2),'double_y':str(y2),
 'triple_slope':str(ell3),'triple_x':str(x3),'triple_y':str(y3),'formal_parameter':str(u3),
 'r2_coefficient':str(leading),'series':str(S.series(u3,r,0,7)),
 'curve_equations_verified':True,
 'scope':'Exact order-two contact. No numerical approximation and no target proof imported.'}
(root/'records/S6_SERIES_PUBLISH_I_A23_preread_computation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
