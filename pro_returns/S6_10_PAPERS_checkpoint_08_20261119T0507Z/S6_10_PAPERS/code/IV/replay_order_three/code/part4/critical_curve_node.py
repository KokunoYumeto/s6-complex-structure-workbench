"""Exact Hessian identities for the cusp-plus-line A1 exclusion."""
from pathlib import Path
import json
import sympy as sp
x,y,z,s,A,B,C,D,G=sp.symbols('x y z s A B C D G')
h=y*y-x**3-s*x*x
f=A*z*h+z*z*(B*x*x+C*x*y+D*y*y)+G*h*h
M=sp.hessian(f,(x,y)).subs({x:0,y:0})/2
F=sp.factor(M.det()/z**2)
expected=(-s*A+B*z)*(A+D*z)-C*C*z*z/4
assert sp.expand(F-expected)==0
assert sp.diff(F,z).subs({s:0,z:0})==A*B
assert sp.diff(F,s).subs({s:0,z:0})==-A*A
pinch=f.subs({A:1,B:1,C:0,D:0,G:0})
assert sp.factor(M.det().subs({A:1,B:1,C:0,D:0,G:0}))==z*z*(-s+z)
result={'working_proof':'notes/part4_local_node_working.md',
 'quadratic_matrix':[[str(v) for v in row] for row in M.tolist()],
 'determinant_divided_by_z_squared':str(F),
 'derivative_z_at_origin':'A*B','derivative_s_at_origin':'-A^2',
 'explicit_example':str(sp.expand(pinch)),
 'example_simple_hessian_zero':'z=s','all_checks_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('Cusp-plus-line critical-curve Hessian identities: PASS')
print('Hessian quadratic matrix:',M)
print('det/z^2 =',F)
print('Explicit model has a simple Hessian zero at z=s, away from the origin.')
