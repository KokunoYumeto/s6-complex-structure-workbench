"""Independent exact check of the displayed Weyl/root octonion coordinates."""
from pathlib import Path
import runpy
import json
import sympy as s

data=runpy.run_path(str(Path(__file__).with_name('check_niemeier_triality.py')))
L=data['L']
rho=s.Matrix([s.Rational(t,2) for t in (5,3,1,-1,-3,-5)]*4+[3,2,1,0])
alpha=s.Matrix([1,-1]+[0]*26)
U=s.ones(8,1)
V=s.Matrix([1/s.sqrt(2)]*4+[s.sqrt(3),2/s.sqrt(3),1/s.sqrt(3),0])
varrho=s.Matrix.vstack(V+2*U,V,V-2*U)
d0=s.Matrix([(2+s.sqrt(2))/3,-s.Rational(2,3)]+[0]*6)
d1=s.Matrix([(s.sqrt(2)-1)/3,s.Rational(1,3)]+[0]*6)
delta=s.Matrix.vstack(d0,d1,d1)
assert all(s.simplify(x)==0 for x in L*rho-varrho)
assert all(s.simplify(x)==0 for x in L*alpha-delta)
assert s.simplify(varrho.dot(varrho))==84
assert s.simplify(delta.dot(delta))==2
assert s.simplify(varrho.dot(delta))==1
shift=varrho/6-delta
assert s.simplify(shift.dot(shift))==4
print(json.dumps({'marked_weyl_and_simple_root':'PASS','rho_norm_squared':84,
                  'alpha_norm_squared':2,'pairing':1,'neighbor_shift_norm_squared':4}))
