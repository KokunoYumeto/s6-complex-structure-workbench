"""Exact arithmetic of the Jin quotient classification used in B.6.18.

The geometric primary theorem is not proved by this script. It checks
the change of basis and the specialization to the actual ell=-4.
"""
from pathlib import Path
import json
import sympy as s

A,B,k,ell=s.symbols('A B k ell',integer=True)
characteristic=s.Matrix([[1,8],[4,8]])
assert characteristic.det()==-24
sol=s.solve([A+8*B-k,4*A+8*B-ell],[A,B])
assert sol[B]==(4*k-ell)/24
assert s.simplify(sol[A]-(ell-k)/3)==0
actual={str(v):str(s.simplify(expr.subs(ell,-4))) for v,expr in sol.items()}
assert s.simplify(sol[A].subs({ell:-4,k:-1+6*B})+1+2*B)==0
assert s.simplify(sol[B].subs({ell:-4,k:-1+6*B})-B)==0
out={'generator_columns_k_ell':characteristic.tolist(),
     'inverse_coefficients':{str(v):str(expr) for v,expr in sol.items()},
     'actual_ell_minus_four':actual,
     'actual_class':'a^(-1-2B) b^B; k=-1+6B',
     'integer_B_evaluated':False}
text=json.dumps(out,indent=2,default=str)+'\n'
print(text,end='')
Path(__file__).with_suffix('.out.json').write_text(text)
