#!/usr/bin/env python3
"""Exact equivariant characteristic polynomials for the common flop link."""
from pathlib import Path
import sympy as s
import json
r,t,u = s.symbols('r s u', integer=True)
p_old = ((r+t)**2+r*r+t*t)*u*u
p_new = ((r-t)**2+r*r+t*t)*u*u
e_q = r*t*u*u
assert s.expand(p_new-p_old) == -4*e_q
assert s.expand(p_old-2*(r*r+r*t+t*t)*u*u) == 0
assert s.expand(p_new-2*(r*r-r*t+t*t)*u*u) == 0
data = {
 'old_base_rotation_weight': str(-r-t),
 'new_base_rotation_weight': str(t-r),
 'q_complex_weights_in_H_orientation': [str(-t),str(-r)],
 'q_equivariant_Euler_class': str(e_q),
 'old_equivariant_p1': str(s.expand(p_old)),
 'new_equivariant_p1': str(s.expand(p_new)),
 'difference': str(s.expand(p_new-p_old)),
 'relative_Thom_coefficient': -4,
 'relative_bundle_convention': 'new-minus-old, boundary identification old->new is Ad(q^-1), hence new->old clutch on the doubled q-disc is Ad(q)',
 'scope': 'universal relative equivariant tangent clutch; no global doubled-four-cycle pullback or cross-edge return value is inferred',
}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS: p1_new-p1_old=-4*e_eq(D4_q), with the exact new-minus-old Thom convention.')
