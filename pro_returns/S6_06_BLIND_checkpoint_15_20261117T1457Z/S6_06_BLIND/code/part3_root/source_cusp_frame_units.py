"""Independent exact physical-q normal coefficients and source-period units."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as S

u,rho,s,X,Y,x,t=S.symbols('u rho s X Y x t')
q=(Y**2-X**2*(X+rho**2))/(X+u)
xp=s-rho; yp=s+rho; Xn=xp*yp; Yn=s*Xn
n=S.Matrix([3*s*s-rho*rho,-2*s,2*rho*Xn])
dq=S.Matrix([S.diff(q,z).subs({X:Xn,Y:Yn}) for z in [X,Y,rho]])
for z in dq+Xn/(Xn+u)*n:
    assert S.factor(z)==0
Z=xp/yp
assert S.factor((-Xn/(Xn+u))/Z+yp**2/(Xn+u))==0
assert S.factor((-Xn/(Xn+u))*Z+xp**2/(Xn+u))==0
assert S.factor(yp**2*S.diff(Z,s)-2*rho)==0

rs=(1-2*u**3)/(3*u**2); t0=u**2-2/u
poly=x**3+3*rs*x*x+t*x+1
assert S.factor(poly.subs({x:u,t:t0}))==0
f21=(Y+1+t*x/2)/x
f12=(Y-1-t*x/2)/x
assert S.factor(f21.subs({x:u,Y:0,t:t0})-u*u/2)==0
assert S.factor(f12.subs({x:u,Y:0,t:t0})+u*u/2)==0
sG=-1/u
PG=S.factor((sG-rho)/(sG+rho))
assert S.factor(PG-(1+u*rho)/(1-u*rho))==0
assert S.factor((sG*sG-(u+u**-2))+u)==0
disc=S.discriminant(poly,x)
c4=16*((3*rs)**2-3*t)
tate=S.factor(16*S.diff(disc,t).subs(t,t0)/c4.subs(t,t0)**3)
assert S.factor(tate+u/(64*(u+u**-2)**3))==0

record={
 'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
 'normal_covector':[str(z) for z in n],
 'physical_q_gradient_factor':'-(s-rho)*(s+rho)/(s^2-rho^2+u)',
 'first_Cox_normal_factor':'-(s+rho)^2/(s^2-rho^2+u)',
 'second_Cox_normal_factor':'-(s-rho)^2/(s^2-rho^2+u)',
 'retained_Cartier_canonical_determinant':'(s+rho)^2*dZ/ds=2rho',
 'marked_source_section_coordinate':str(PG),
 'actual_selected_Hom_over_q':{'a2_b1':'2/u^2','a1_b2':'-2/u^2'},
 'Tate_leading':str(tate),
 'winding_proof':'Near u_star^3=-1, u is a nonzero holomorphic function of rho^2. The factors 1±u*rho and ±2/u^2 are units on the full disc. With rho^2=u+u^-2, the Tate coefficient is -u/(64rho^6), of winding -6. The physical-q normal comparison has the extending unit -1/(s^2-rho^2+u).',
 'scope':'Exact local frame and period inputs only; no other-edge variation or all-fan return is assigned.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
