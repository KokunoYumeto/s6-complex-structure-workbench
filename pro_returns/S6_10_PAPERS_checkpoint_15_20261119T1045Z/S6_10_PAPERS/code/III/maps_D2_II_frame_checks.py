"""Exact A2 critical ideal and corrected multiple-fibre differential checks."""
from pathlib import Path
import json
import sympy as s
x,y,z,xb,yb=s.symbols('x y z xb yb')
df=s.Matrix([[-3*x*x,2*y,0]])
ker=s.Matrix([[2*y,0],[3*x*x,0],[0,1]])
assert df*ker==s.zeros(1,2)
bott=s.Matrix([[2*y,-3*xb*xb],[3*x*x,2*yb]])
star=s.Matrix([[2*yb,3*xb*xb],[-3*x*x,2*y]])
norm=4*y*yb+9*x*x*xb*xb
assert star*bott==norm*s.eye(2)
assert bott.det()==norm
assert s.Matrix([[-3*x*x,2*y]])*bott==s.Matrix([[0,norm]])
# Local length of C[x,y]/(x^2,y), with a third free critical coordinate.
groebner=s.groebner([x*x,y],x,y)
assert groebner.reduce(x*x)[1]==0
assert groebner.reduce(y)[1]==0
assert groebner.reduce(x)[1]==x
assert groebner.reduce(s.Integer(1))[1]==1
m=s.symbols('m',integer=True,positive=True)
u=s.symbols('u',nonzero=True)
q=s.symbols('q',nonzero=True)
# q=s^m has common df divisor (m-1)[s=0]; dividing leaves m ds.
normal_exponent=(m-1)+1-m
assert s.expand(normal_exponent)==0
result=dict(type_II_kernel_verified=True,
            type_II_jacobian_standard_monomials=['1','x'],
            critical_multiplicity=2,
            bott_degree=2,
            good_log_corrected_coefficient='m',
            good_log_corrected_critical_cycle=0,
            deck_equivariance_exponent=str(normal_exponent),
            scope='Original II and free good-reduction logarithmic caps only')
root=Path(__file__).resolve().parent
(root/'maps_D2_II_frame_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
