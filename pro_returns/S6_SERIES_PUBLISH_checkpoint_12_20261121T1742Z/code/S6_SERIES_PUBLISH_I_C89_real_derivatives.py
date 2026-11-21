"""Fresh real-coordinate Jacobian/Hessian check before target-proof comparison."""
from pathlib import Path
import sympy as s
import json, hashlib, datetime

r=Path(__file__).resolve().parents[1]
x,y,U,V,S,T,p,q,a,b=s.symbols('x y U V S T p q a b',real=True)
mr=U+p*x-q*y; mi=V+q*x+p*y
tr=S+a*x-b*y; ti=T+b*x+a*y
betaa=mi/ti; betab=mr-betaa*tr
origin={x:0,y:0}
jac=(s.diff(betab,x)*s.diff(betaa,y)-s.diff(betab,y)*s.diff(betaa,x)).subs(origin)
den=((p-V*a/T)**2+(q-V*b/T)**2)/T
lap=(s.diff(mi**2/ti,x,2)+s.diff(mi**2/ti,y,2)).subs(origin)/2
assert s.factor(jac-den)==0
assert s.factor(lap-den)==0
P,Pi,T0,E=s.symbols('P Pi T0 E',positive=True)
A=3*P/(16*Pi**2); C=P**2/Pi**3
c0=s.simplify(4*A**2/(9*T0*C**s.Rational(4,3)))
assert s.simplify(c0-1/(64*T0*P**s.Rational(2,3)))==0
B=9*Pi**4*E/4
c1=s.simplify(1/(16*s.sqrt(B)))
assert s.simplify(c1-1/(24*Pi**2*s.sqrt(E)))==0
record={
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'method':'Real affine holomorphic jets; determinant of the Betti Jacobian and real Laplacian computed independently, then exact Puiseux pullback constants.',
 'jacobian':str(s.factor(jac)), 'gaussian_laplacian_half':str(s.factor(lap)),
 'density0_constant':str(c0),'density1_constant':str(c1),
 'assertions':4,'outcome':'PASS',
 'scope':'Factors/sign and finite-point constants only; not a fresh global equidistribution computation.'
}
out=r/'records/S6_SERIES_PUBLISH_I_C89_real_derivatives.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
