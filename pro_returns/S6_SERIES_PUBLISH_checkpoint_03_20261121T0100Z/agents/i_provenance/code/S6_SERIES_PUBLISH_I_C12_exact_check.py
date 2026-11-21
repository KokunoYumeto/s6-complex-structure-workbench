#!/usr/bin/env python3
"""New finite arithmetic supporting the preread C.1.2 derivation.

No earlier arithmetic program is imported. This verifies only the displayed
lattice kernels, their indices, and a rational Fourier-tail sign bound; the
analytic continuation is proved separately in the preread derivation.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

def multiply(a, b, square):
    # A quadratic generator theta has theta^2 = square[0]+square[1]*theta.
    return (a[0]*b[0]+a[1]*b[1]*square[0],
            a[0]*b[1]+a[1]*b[0]+a[1]*b[1]*square[1])

def plus(a, b):
    return (a[0]+b[0], a[1]+b[1])

def matrix_of(a, square):
    c1 = multiply(a, (1, 0), square)
    c2 = multiply(a, (0, 1), square)
    return ((c1[0], c2[0]), (c1[1], c2[1]))

def determinant(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]

i_square = (-1, 0)
rho_square = (-1, 1)
alpha_i, p_i = (1, -1), (F(1,2), F(-1,2))
alpha_rho, p_rho = (1, 1), (F(2,3), F(-1,3))
assert multiply(alpha_i, p_i, i_square) == (0, -1)
assert multiply(alpha_rho, p_rho, rho_square) == (1, 0)
assert plus(multiply((0,1),p_rho,rho_square),p_rho) == (1, 0)
assert plus(multiply((0,1),p_i,i_square),(-p_i[0],-p_i[1])) == (0, 1)
assert determinant(matrix_of(alpha_i, i_square)) == 2
assert determinant(matrix_of(alpha_rho, rho_square)) == 3

exp5_lower = sum((F(5)**k/F(factorial(k)) for k in range(7)), F(0))
r_upper = F(1,100)
halfperiod_lower = F(2,3)-16*r_upper/(1-r_upper)**2
assert exp5_lower > 100
assert halfperiod_lower > 0

result = {
    'scope': 'Exact finite arithmetic only; no numerical proof of logarithmic continuation is claimed.',
    'gaussian_endomorphism_matrix': matrix_of(alpha_i, i_square),
    'gaussian_kernel_index': 2,
    'gaussian_nonzero_kernel_point_image': [0, -1],
    'hexagonal_endomorphism_matrix': matrix_of(alpha_rho, rho_square),
    'hexagonal_kernel_index': 3,
    'hexagonal_nonzero_kernel_point_image': [1, 0],
    'rho_times_p_plus_p': [1,0],
    'exp5_taylor_lower_through_degree_6': str(exp5_lower),
    'exp5_taylor_lower_gt_100': True,
    'wp_halfperiod_over_pi_squared_lower_at_r_1_100': str(halfperiod_lower),
    'all_assertions_passed': True
}
out = Path(__file__).resolve().parents[1] / 'S6_SERIES_PUBLISH_I_C12_exact_check.json'
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
