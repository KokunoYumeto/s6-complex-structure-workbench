#!/usr/bin/env python3
"""Fresh exact checks after E18 prederivation; no producer program was read.

This checks the scalar identity and explicit lattice/cohomology linear maps.
It is not a numerical substitute for the analytic theta or torus arguments.
"""
import json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

checks = []
def check(name, expression):
    residual = s.simplify(expression)
    assert residual == 0, (name, residual)
    checks.append({"name": name, "residual": str(residual), "passed": True})

p, h, e, w = s.symbols('p h E2 wp')
Bprime = s.I/s.pi*h*p + (-w-s.pi**2*e/3+h*h)/(4*s.pi**2) + e/12
check('E2 cancellation', Bprime - (s.I*h*p/s.pi+(h*h-w)/(4*s.pi**2)))
check('determinant square correction', Bprime-p*p + (p-s.I*h/(2*s.pi))**2+w/(4*s.pi**2))
check('constant half-period determinant', (Bprime-p*p).subs({p:0,h:0})+w/(4*s.pi**2))

# Original lattice basis is (e1,e2,(tau,1/2),(3,6v)).
# Symmetric lattice basis is (e1,e2,(tau,1/2),(1/2,v)).
inclusion = s.diag(1,1,1,6)
snf = smith_normal_form(inclusion, domain=ZZ)
assert list(snf.diagonal()) == [1,1,1,6]
checks.append({"name":"exact lattice inclusion and cokernel", "inclusion":str(inclusion), "smith_diagonal":[1,1,1,6], "index":6, "passed":True})
x,y,a,b=s.symbols('x y a b', real=True)
original_periods=s.Matrix([[1,0,x,3],[0,0,y,0],[0,1,s.Rational(1,2),6*a],[0,0,0,6*b]])
check('original real determinant', original_periods.det()+6*y*b)

# Boundary on H^1(O) is cup/wedge with kappa. Its columns are
# -the second kappa column and the first kappa column.
A,B,C,D=s.symbols('A B C D')
kappa=s.Matrix([[A,B],[C,D]])
boundary=s.Matrix([[-B,A],[-D,C]])
check('boundary determinant equals KS determinant', boundary.det()-kappa.det())
actual_kappa=s.diag(1,-w/(4*s.pi**2))
actual_boundary=s.Matrix.hstack(-actual_kappa[:,1],actual_kappa[:,0])
check('half-period boundary determinant', actual_boundary.det()+w/(4*s.pi**2))

# Exact multiplicative factor from the theta quasiperiodicity for P=1/2.
check('line multiplier', s.exp(2*s.pi*s.I*s.Rational(1,2))+1)
check('sixfold elliptic translation', -6*s.Rational(1,2)+3)

result={"scope":"Fresh symbolic identity, lattice inclusion, and cohomology boundary maps; analytic assertions are proved in the written receipt.",
        "check_count":len(checks),"all_passed":all(c['passed'] for c in checks),"checks":checks}
out=Path(__file__).resolve().parents[2]/'analysis/continuation_II_ledger/E18_exact_algebra.output.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({"all_passed":result['all_passed'],"check_count":len(checks),"output":str(out)}))
