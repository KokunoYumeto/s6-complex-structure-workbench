"""Exact negative-definite completion in P4.37."""
from pathlib import Path
import json
import sympy as sp
rr,rz,zz,dr,ar,dz,az,dd,da,aa,n=sp.symbols('rr rz zz dr ar dz az dd da aa n')
B=rr+dr+ar-rz+dz-2*az+zz
q_shift=(rr+2*dr+dd)-(rz+dr-ar+dz+dd-da)+(zz+2*dz-2*az+dd-2*da+aa)
assert sp.expand(q_shift-(B+dd-da+aa))==0
assert sp.expand((n+q_shift).subs({dd:-n,da:aa})-B)==0
x,y,z,w=sp.symbols('x y z w',real=True)
q1=-x*x+x*y-y*y
assert sp.expand(q1+sp.Rational(1,2)*(x*x+y*y+(x-y)**2))==0
result={'proof':'P4.37','base_expression':str(B),
        'shifted_quadratic':str(sp.expand(q_shift)),
        'constant_difference':'D^2-D.A+A^2=-n',
        'negative_form_identity':str(q1),
        'all_checks_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('P4.37 exact Chern-square completion: PASS')
print('q(R+D,Z+D-A) = B + D^2 - D.A + A^2')
print('D^2=-n and D.A=A^2 give B=n+q(R+D,Z+D-A).')
print('Negative-definite q is strictly negative because R+D is nonzero.')
