"""Exact characteristic substitutions for the actual source-zero boundary.

The relative cohomology, spin structure, and boundary identification are
proved in notes/part3_source_zero_spin_c_boundary_working.md. This file
checks the polynomial identities and the explicit generator normalization.
It does not compute the still-required global pairings or signature.
"""
from datetime import datetime, timezone
from pathlib import Path
import json
import sympy as s

z, p, c1, c2, sig = s.symbols('z p c1 c2 sig')
phat = (p + z*z) / 2
cn = (phat*phat - sig)/8 - s.Rational(5,12)*z*z*phat + z**4/4
pontryagin = (3*p*p - 14*z*z*p + 7*z**4 - 12*sig)/96
chern = (-c1**4 + 4*c1*c1*c2 + 3*c2*c2 - 3*sig)/24
jiang = 28*((p*p-4*sig)/896 - z*z*p/192 + z**4/384)
checks = []

def check(name, expression):
    assert s.expand(expression) == 0, name
    checks.append(name)

check('CN2.1_to_Pontryagin', cn - pontryagin)
check('almost_complex_hat_p', phat.subs({p:c1*c1-2*c2, z:c1})-(c1*c1-c2))
check('Pontryagin_to_Chern', pontryagin.subs({p:c1*c1-2*c2, z:c1})-chern)
check('Jiang_to_CN_same_normalization', jiang-cn)
check('spin_specialization', cn.subs(z,0)-(p*p-4*sig)/32)
check('Milnor_e1_p1_6_generator', cn.subs({z:0,p:6,sig:1})-1)
check('product_S1_D7_zero', cn.subs({z:0,p:0,sig:0}))
check('closed_spin_c_index_polynomial', cn/28-((p*p-4*sig)/896-z*z*p/192+z**4/384))

result = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'status': 'PASS',
    'check_count': len(checks),
    'checks': checks,
    'integer_normalization': 'mu in Z/28 equals 28 times the classical Eells-Kuiper invariant',
    'Pontryagin_expression': str(s.expand(pontryagin)),
    'Chern_expression': str(s.expand(chern)),
    'source': 'Crowley-Nordstrom, Exotic G2-manifolds, Math. Ann. 381 (2021), 29-74, Lemma 2.1(i), equation (2.1)',
    'remaining_numeric_inputs': ['relative c1^4', 'relative c1^2*c2', 'relative c2^2', 'signature(W)'],
    'return_class_assigned': False
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
