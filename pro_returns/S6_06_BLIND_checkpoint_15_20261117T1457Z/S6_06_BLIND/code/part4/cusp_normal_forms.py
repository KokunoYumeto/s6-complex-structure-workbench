"""Exact local algebra in P4.28 and its D4 warning example."""
from pathlib import Path
import json
import sympy as sp

x,y,Y,z,h,b,A,B,C,eps=sp.symbols("x y Y z h b A B C eps")
quadratic=h*x*x+2*h*b*x*y+h*b*b*y*y
assert sp.expand(quadratic-h*(x+b*y)**2)==0

a=x*A
bb=x*x*B
c=x*x*C
P=y**3+a*y*y+bb*y+c
depressed=sp.expand(P.subs(y,Y-a/3))
H=sp.cancel((depressed-Y**3)/(x*x))
assert sp.expand(depressed-(Y**3+x*x*H))==0
assert sp.Poly(H,x,Y,A,B,C).domain == sp.QQ
expected=(B-A*A/3)*Y+C-x*A*B/3+2*x*A**3/27
assert sp.expand(H-expected)==0

X,Z=sp.symbols("X Z")
g=X*X+y**3*(z*z+y*y+eps)
assert sp.expand(g-(X*X+y**3*(z*z+y*y+eps)))==0
gradient=[sp.diff(g,t) for t in (X,y,z)]
Hessian=sp.hessian(g,(X,y,z))
critical_det=sp.factor(Hessian.det().subs({X:0,z:0,eps:-sp.Rational(5,3)*y*y}))
assert critical_det==40*y**6
critical_value=sp.expand(g.subs({X:0,z:0,eps:-sp.Rational(5,3)*y*y}))
assert critical_value==-sp.Rational(2,3)*y**5

result={
 "proof":"P4.28",
 "rank_one_hessian_factorization":str(sp.factor(quadratic)),
 "depressed_cubic":str(depressed),
 "factor_H":str(H),
 "D4_deformation_gradient":[str(t) for t in gradient],
 "D4_nonzero_critical_hessian":str(critical_det),
 "D4_nonzero_critical_value":str(critical_value),
 "all_checks_passed":True}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print("P4.28 local normal-form identities: PASS")
print("Rank-one Hessian:",sp.factor(quadratic))
print("Depressed cubic equals Y^3+x^2 H with H =",H)
print("D4 deformation also has Morse points off its zero divisor:")
print(" Hessian determinant =",critical_det)
print(" critical value =",critical_value)
