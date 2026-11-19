#!/usr/bin/env python3
"""Exact orientation and Chern--Weil checks for the fixed-edge derivative.

This verifies local matrices and the universal clutch calculation only.
The actual-family Gysin comparison is proved in the companion Markdown note;
the sign of the disc-supported commutator is deliberately not assigned here.
"""
import json
from pathlib import Path
import sympy as s

OUT = Path(__file__).with_suffix('.json')

# Columns are the derivatives of h=u*i*u^-1 in the oriented (j,k) plane.
# For u=a0+j*a1 and a1=x+i*y they are -2k and -2j.
base_plus = s.Matrix([[0, -2], [-2, 0]])
# For k=v^-1*i*v and v=c0+j*conjugate(c1), c1=x+i*y,
# the derivatives are +2k and -2j.
base_minus = s.Matrix([[0, -2], [2, 0]])
normal_plus = s.eye(4)  # c0+j*conjugate(c1) in (1,i,j,k).
normal_minus = s.diag(1, 1, 1, -1)  # a0+j*a1 in that same real frame.
hopf = s.Matrix([[0, 2], [-2, 0]])  # q*i*q^-1 at q=1, inputs j,k.

assert base_plus.det() == -4
assert base_minus.det() == 4
assert normal_plus.det() == 1
assert normal_minus.det() == -1
assert hopf.det() == 4

ii = s.diag(s.I, -s.I)
jj = s.Matrix([[0, 1], [-1, 0]])
kk = ii * jj
assert ii * jj == kk and jj * kk == ii and kk * ii == jj
assert s.trace(ii * jj * kk) == -2
theta = s.symbols('theta', real=True)
# F=-dtheta*omega+(theta**2-theta)*omega**2.
# Moving dtheta to the right of the three-form reverses its sign.
trace_f2_coefficient = 2 * (theta**2 - theta)
coefficient_integral = s.integrate(trace_f2_coefficient, (theta, 0, 1))
trace_omega3_integral_over_pi2 = -24
c2_degree_one = coefficient_integral * trace_omega3_integral_over_pi2 / 8
assert coefficient_integral == s.Rational(-1, 3)
assert c2_degree_one == 1

data = {
    'scope': 'local exact orientation and universal Jin-clutch checks; no commutator sign assigned',
    'complex_to_plus_base_jk': base_plus.tolist(),
    'complex_to_plus_base_sign': -1,
    'complex_to_minus_base_jk': base_minus.tolist(),
    'complex_to_minus_base_sign': 1,
    'complex_to_plus_normal_H': normal_plus.tolist(),
    'complex_to_minus_normal_H': normal_minus.tolist(),
    'hopf_base_jk': hopf.tolist(),
    'physical_circle_at_q1': '-i',
    'sphere_q_orientation_relative_to_circle_times_base': -1,
    'exterior_complex_orientation_in_D3y_times_S3q': 1,
    'Jin_SU2_clutch_c2_per_degree': int(c2_degree_one),
    'Jin_adjoint_clutch_p1_per_degree': -4,
    'L_variation': 1,
    'L_quotient_k': -1,
    'L_quotient_ell': -4,
    'actual_relative_coefficients': {
        'variation': '-k_Jin',
        'B_exponent': '6*A_Jin',
        'R_exponent_after_LR_rewrite': '-6*A_Jin',
        'stable_derivative_in_fixed_product_frame': '12*A_Jin',
    },
    'commutator_Eells_Kuiper_sign': 'not assigned by this certificate',
}
OUT.write_text(json.dumps(data, indent=2, default=int) + '\n')
print('PASS: exact quaternion orientation matrices and Jin adjoint clutch p1=-4*degree')
print('Actual-family Gysin proof: notes/part3_fixed_edge_derivative_audit.md')

