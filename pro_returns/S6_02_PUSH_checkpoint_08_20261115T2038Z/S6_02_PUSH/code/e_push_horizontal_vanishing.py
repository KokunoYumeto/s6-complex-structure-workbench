#!/usr/bin/env python3
"""Exact HRR coefficient audit for E.2.9; analytic vanishing is proved in TeX."""
from pathlib import Path
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
t, c1, c2, c3 = sp.symbols('t c1 c2 c3')
ch_tangent = 3 + c1*t + (c1*c1-2*c2)*t*t/2 + (c1**3-3*c1*c2+3*c3)*t**3/6
todd = 1 + c1*t/2 + (c1*c1+c2)*t*t/12 + c1*c2*t**3/24
coefficient = sp.expand(ch_tangent*todd).coeff(t, 3)
expected = c1**3/2-sp.Rational(19,24)*c1*c2+c3/2
assert sp.expand(coefficient-expected) == 0
sphere_value = coefficient.subs({c1:0,c2:0,c3:2})
assert sphere_value == 1
result = {
    'statement':'E.2.9',
    'scope':'Only the exact Hirzebruch-Riemann-Roch polynomial is checked computationally. No analytic vanishing, duality, or compactness assertion is inferred from this program.',
    'ch_T_degree_at_most_3':str(ch_tangent),
    'Todd_degree_at_most_3':str(todd),
    'degree_3_coefficient':str(coefficient),
    'specialization_c1_c2_zero_c3_two':str(sphere_value),
    'status':'PASS'
}
text = json.dumps(result,indent=2)+'\n'
(HERE/'e_push_horizontal_vanishing.json').write_text(text)
(HERE/'e_push_horizontal_vanishing.out').write_text(text)
print(text,end='')
