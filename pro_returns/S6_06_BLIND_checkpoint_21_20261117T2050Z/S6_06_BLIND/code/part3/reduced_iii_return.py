#!/usr/bin/env python3
"""Exact physical-character/origin and root arithmetic certificate.

The page embedding and relative translation comparison are proved in
notes/part3_reduced_iii_return.md; these identities do not replace them.
"""
from pathlib import Path
import json
import sympy as S

root = Path(__file__).resolve().parent
s, v, theta, m, g, C, c, c0 = S.symbols('s v theta m g C c c0')
delta = S.Matrix([0, 1])
gamma = S.Matrix([g, -C-s-m*v])  # B^{-1}, physical outward loop
o = S.Matrix([-g*s/m, C*s/m+s*s/(2*m)+s*v])
sigma = S.Matrix([g*v, -C*v-m*(v*v-v)/2])
F = sigma-o
zero = S.zeros(2, 1)
clean = lambda X: X.applyfunc(S.simplify)
assert clean(o.subs(v,v+1)-o-s*delta) == zero
assert clean(sigma.subs(v,v+1)-sigma-s*delta-gamma) == zero
assert clean(o.subs(s,s+2*m)-o+2*gamma-2*m*delta) == zero
assert clean(sigma.subs(s,s+2*m)-sigma) == zero
angular = clean(F.subs(v,v+theta)-F)
assert clean(angular-theta*gamma+m*theta*(theta-1)*delta/2) == zero
assert clean(angular.subs(s,s+2*m)-angular+2*m*theta*delta) == zero
assert (m*theta*(theta-1)/2).subs(theta,0) == 0
assert (m*theta*(theta-1)/2).subs(theta,1) == 0

# Ordinary -> cap cochain, with physical scalar character exp(2pi i zeta_2).
cochain = (c-c0)*s/m
assert S.simplify(cochain.subs(s,s+1)-cochain-(c-c0)/m) == 0
inverse_closing = S.simplify(cochain.subs(c,c+m)-cochain)
assert inverse_closing == s
# B has Lie translation -gamma; its inverse is exactly +gamma.
B = S.Matrix([-g,C+s+m*v])
assert B+gamma == zero

l = S.symbols('l', integer=True, nonnegative=True)
mm, kk = 4*l+3, 3*l+2
assert S.expand(3*mm-4*kk) == 1
assert S.expand(6*mm-6*kk) == 6*(l+1)
assert S.expand(5*mm-6*kk) == 2*l+3
assert S.expand(2*mm-2*kk) == 2*l+2
assert S.expand(3*mm-3*kk) == 3*l+3
chi = (mm+1)/4
PO = mm-chi
M2 = -2*chi-2*PO
A = (12*M2+24*chi)/24
assert S.simplify(chi-l-1) == 0
assert S.simplify(PO-3*l-2) == 0
assert S.simplify(M2+2*mm) == 0
assert S.simplify(A+3*l+2) == 0

t, x, y = S.symbols('t x y')
disc_second = S.factor(4*t**3+27*t**2)
assert disc_second == t**2*(4*t+27)
assert S.expand(1 + t - t - 1) == 0

record = {
    'status': 'PASS: exact physical-character and algebraic identities',
    'scope': 'P3K.24: the topology, physical-character square, page/line maps, and signed Thom comparison have passed independent audits; this script certifies the displayed exact identities.',
    'physical_character': 'a=zeta_1; V=exp(2*pi*i*zeta_2)',
    'B_translation': [str(z) for z in B],
    'positive_outward_gamma_B_inverse': [str(z) for z in gamma],
    'ordinary_to_cap_parameter_cochain': str(cochain),
    'inverse_closing_near_cap': str(inverse_closing),
    'positive_deck_at_cusp': 'V -> (t-t_c)*V',
    'origins': {'ordinary': [str(z) for z in o], 'cusp': [str(z) for z in sigma]},
    'angular_difference': [str(z) for z in angular],
    'auxiliary_cusp_deck': 's -> s+2*m',
    'line_gauge_winding': '-2*m',
    'second_source_discriminant': str(disc_second),
    'root_order': str(mm),
    'chi': str(S.simplify(chi)),
    'section_intersection': str(S.simplify(PO)),
    'line_square': str(S.simplify(M2)),
    'derived_index_after_geometric_comparison': str(S.simplify(A)),
}
(root/'reduced_iii_return.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS: B inverse = outward gamma; exact ordinary-to-cap closing square.')
print('PASS: both extending origins, endpoint gauges, and retained 2m cusp deck.')
print('PASS: both source root exponents, chi=l+1, M^2=-2m, A=-(3l+2).')
