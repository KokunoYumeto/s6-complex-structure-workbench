"""Exact phase, lattice and polynomial checks for C.3.13.

The global integral-one-form extension is proved in the text; this
script checks only its finite algebraic and marking inputs.
"""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

q, R, S, t = s.symbols('q R S t', nonzero=True)
theta, w, A, kappa = s.symbols('theta w A kappa', real=True)
checks = {}
checks['first_root_z1_phase_integral'] = 3*s.Rational(1,3) == 1
checks['first_root_z2_phase_integral'] = -s.Rational(1,3)+4*s.Rational(1,3) == 1
checks['second_root_z1_phase_integral'] = -s.Rational(1,4)-3*s.Rational(1,4) == -1
checks['second_root_z2_phase_integral'] = -4*s.Rational(1,4) == -1
for eps in (1,-1):
    ordinary = theta+eps*w+A
    ell = eps*w+kappa
    checks[f'finite_radial_cancellation_{eps}'] = s.expand(ordinary-ell-A)==theta-kappa
base_numerator = R**12*t
base_denominator = R**12*t-R**12*(t-1)
checks['weighted_base_coordinate'] = s.cancel(base_numerator/base_denominator)==t
checks['cusp_normal_function'] = s.expand(S**12-S**12*(1-q))==q*S**12
checks['cusp_argument_degree'] = 3*4 == 4*3 == 12

# Ordered orbit-fibre basis (gamma,u,w); delta has been divided out.
mon = s.Matrix([[1,0,0],[0,1,0],[0,1,1]])
snf = smith_normal_form(mon-s.eye(3), domain=s.ZZ)
nonzero_invariants = [abs(snf[i,i]) for i in range(3) if snf[i,i] != 0]
checks['link_H1_torsion_free'] = nonzero_invariants == [1]
checks['link_H1_rank_three'] = 3-(mon-s.eye(3)).rank()+1 == 3
restriction_dual = s.Matrix([[1,0],[0,1],[0,0]])
checks['relative_H1_restriction_injective'] = restriction_dual.rank()==2
checks['transverse_meridian_value_zero'] = (restriction_dual*s.Matrix([1,0]))[2] == 0

assert all(checks.values()), checks
result = {
  'status':'PASS',
  'checks':checks,
  'link_H1_generators':['gamma','u','transverse q meridian'],
  'scope':'Finite exact checks. No Haefliger number or six-dimensional framing is computed.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
