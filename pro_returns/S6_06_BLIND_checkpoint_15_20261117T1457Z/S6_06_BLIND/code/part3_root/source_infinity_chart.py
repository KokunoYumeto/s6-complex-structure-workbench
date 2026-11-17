"""Exact second boundary chart of the marked E7 source curve.

This computes actual coordinate and Hom-section maps only. No completed
suspension or sphere-return invariant is assigned here.
"""
from pathlib import Path
from datetime import datetime, timezone
import sympy as S
import json

z, x, y, t, s, q = S.symbols('z x y t s q', nonzero=True)
v=z**-2
X=z**-2*x
Y=z**-3*y
T=z**-4*t
old=Y**2-X**3-(1-2*v)*X**2-T*X-v**2
new=y**2-x**3-(z*z-2)*x*x-t*x-z*z
assert S.expand(z**6*old-new)==0
t0=1-2*z*z
assert S.expand(x**3+(z*z-2)*x*x+t0*x+z*z-(x-1)**2*(x+z*z))==0
fn=S.Matrix([s*s-z*z,s*(s*s-z*z-1),z])
assert S.expand(new.subs({x:fn[0],y:fn[1],t:t0}))==0
minor=fn.jacobian([s,z]).extract([0,2],[0,1]).det()
assert S.expand(minor-2*s)==0
# At s=0 the other first derivative is -(1+z^2), a unit near z=0.
assert S.simplify(S.diff(fn[1],s).subs(s,0)+1+z*z)==0

F21=(Y+v+T*X/(2*v))/X
F12=(Y-v-T*X/(2*v))/X
G21=(y+z+t*x/(2*z))/x
G12=(y-z-t*x/(2*z))/x
assert S.simplify(F21-z**-1*G21)==0
assert S.simplify(F12-z**-1*G12)==0
assert S.simplify(z**-4*q/(v*F21)-z**-1*q/G21)==0
node={x:1,y:0,t:t0}
assert S.simplify(G21.subs(node)-1/(2*z))==0
assert S.simplify(G12.subs(node)+1/(2*z))==0
assert S.simplify(z**-1/G21.subs(node)-2)==0
assert S.simplify(z**-1/G12.subs(node)+2)==0

poly=x**3+(z*z-2)*x*x+t*x+z*z
disc=S.factor(S.discriminant(poly,x))
assert S.expand(disc.subs(z,0)-4*t*t*(1-t))==0
c4=16*((z*z-2)**2-3*t)
# The leading coefficient of 1/j in the actual selected base q=t-t0.
tate_leading=S.factor(16*S.diff(disc,t).subs(t,t0)/c4.subs(t,t0)**3)
assert S.simplify(tate_leading+1/(64*(1+z*z)**3))==0

A=y-z; B=y+z; C=x; D=t+x*x+(z*z-2)*x
assert S.expand(A*B-C*D-new)==0
for a,b in [(1,2),(2,1)]:
    assert S.simplify((z**-2*x)**(-a)-z**(2*a)*x**(-a))==0
    assert 2*a*b-4==0
    assert S.simplify(z**-4*(z**(2*a))**b-1)==0
record={
 'utc':datetime.now(timezone.utc).isoformat(),
 'status':'PASS',
 'map':'v=zeta^(-2), X=zeta^(-2)X_inf, Y=zeta^(-3)Y_inf, T=zeta^(-4)T_inf',
 'equation':str(new),
 'marked_section':'G_inf=(0,zeta)',
 'selected_base':'T_inf=1-2*zeta^2',
 'normalization':[str(e) for e in fn],
 'central_cubic_discriminant':str(S.factor(disc.subs(z,0))),
 'selected_Hom_over_q':{'a2_b1':2,'a1_b2':-2},
 'selected_Tate_leading':str(tate_leading),
 'conifold':'(Y_inf-zeta)(Y_inf+zeta)=X_inf*(T_inf+X_inf^2+(zeta^2-2)*X_inf)',
 'suspension_comparison':'I U_a,old I^-1=zeta^(2a) U_a,inf; q_old=zeta^-4 q_inf; ab=2 gives unchanged scalar in B.',
 'finite_root_comparison_pending':'z_old^m=zeta^4 z_inf^m; its exact endpoint compensation remains required.',
 'scope':'Exact marked source and Cartier-Hom chart. The unselected I2 component suspension and resulting completed-family return remain under proof.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
