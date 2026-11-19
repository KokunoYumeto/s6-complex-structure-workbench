#!/usr/bin/env python3
"""Exact boundary-frame identities for the real return trace, P3K.9."""
from pathlib import Path
import json
import sympy as sp

out = Path(__file__).resolve().parent
alpha, theta, beta, phi, d, g = sp.symbols(
    'alpha theta beta phi d g', real=True)
rho=sp.symbols('rho',positive=True)

def rz(a):
    return sp.Matrix([[sp.cos(a), -sp.sin(a), 0],
                      [sp.sin(a), sp.cos(a), 0], [0, 0, 1]])

def frame(a, t):
    return sp.Matrix([
        [-sp.sin(a), sp.cos(t)*sp.cos(a), sp.sin(t)*sp.cos(a)],
        [ sp.cos(a), sp.cos(t)*sp.sin(a), sp.sin(t)*sp.sin(a)],
        [0, sp.sin(t), -sp.cos(t)]])

def exact_zero(matrix):
    return matrix.applyfunc(lambda entry: sp.trigsimp(sp.expand_trig(entry))) == sp.zeros(*matrix.shape)

G = frame(alpha, theta)
assert exact_zero(G.T*G - sp.eye(3))
assert sp.trigsimp(G.det()) == 1
assert exact_zero(G-rz(alpha)*frame(0, theta))
assert exact_zero(rz(alpha+beta)-rz(alpha)*rz(beta))
full = frame(phi-d*(theta+g), theta)
factored = rz(-d*g)*rz(phi-d*theta)*frame(0, theta)
assert exact_zero(full-factored)

# Explicit quotient by the oriented outward-page/inward-compression
# collar tangent u=(cos(alpha),sin(alpha),rho,0).
projection=sp.Matrix([[1,0,-sp.cos(alpha)/rho,0],
                      [0,1,-sp.sin(alpha)/rho,0],
                      [0,0,0,1]])
collar=sp.Matrix([sp.cos(alpha),sp.sin(alpha),rho,0])
assert projection*collar==sp.zeros(3,1)
normal=sp.Matrix([-sp.sin(alpha),sp.cos(alpha),0,0])
param_x=sp.Matrix([0,0,sp.cos(theta),-sp.sin(theta)])
param_y=sp.Matrix([0,0,sp.sin(theta),sp.cos(theta)])
projected=sp.diag(rho,rho,1)*projection*sp.Matrix.hstack(normal,-param_x,-param_y)*sp.diag(1/rho,1,1)
assert exact_zero(projected-G)

b_square = sp.Integer(-8)
p1_base = sp.Integer(-24)
p1_normal = sp.Integer(0)
k_gamma = (p1_normal+3*b_square)/4
ell_gamma = p1_base+p1_normal
index_gamma = (4*k_gamma-ell_gamma)/24
degree = 6
assert (k_gamma, ell_gamma, index_gamma) == (-6, -24, 0)
assert (k_gamma/degree, ell_gamma/degree) == (-1, -4)

data = {
    'proof': 'notes/part3_fourfold.md P3K.9',
    'method': 'Exact frame transition, cubic Pontryagin transgression, then integral framing descent.',
    'coordinates': 'All angles in this computation are radians.',
    'collar_phase': 'phi is the outward page phase, equal to the Milnor-page phase plus pi.',
    'collar_vector': ['cos(alpha)','sin(alpha)','rho>0','0'],
    'normal_quotient': [[str(entry) for entry in row] for row in projection.tolist()],
    'quotient_kills_collar': True,
    'quotient_recovers_G_after_oriented_contractible_frame_changes': True,
    'G': [[str(entry) for entry in row] for row in G.tolist()],
    'G_transpose_G': 'I_3',
    'det_G': 1,
    'rotation_factorization': 'G(alpha,theta)=R_z(alpha) G(0,theta)',
    'actual_boundary_relation': 'gamma=theta+g_epsilon(p)',
    'transition': 'h(p)^(-1) G(phi-d*(theta+g_epsilon(p)),theta)',
    'factor_T2': 'h(p)^(-1) R_z(-d*g_epsilon(p))',
    'factor_S1': 'R_z(phi-d*theta) G(0,theta)',
    'pontryagin_transgression': 'The product cubic differs from the sum of the factor cubics by an exact form. Both factor cubics vanish by dimension.',
    'p1_normal': int(p1_normal),
    'b_square': int(b_square),
    'p1_base': int(p1_base),
    'one_gamma_turn': {'k_Jin': int(k_gamma), 'ell_Jin': int(ell_gamma), 'index': int(index_gamma)},
    'physical_mapping_torus': 'Jin M_(f^(-1))',
    'bordism_boundary': '-physical_mapping_torus disjoint_union -normal_sphere_bundle',
    'orientation_consequence': 'Jin(f) has the same characteristic numbers as the positively oriented normal sphere bundle.',
    'framing_gauge_pi1': 'Z/2 direct_sum Z',
    'sixfold_pullback': '(epsilon,n) -> (0,6*n)',
    'constant_axis_Z2_correction': 'Extends over D3; zero cubic transgression and no change in k or ell.',
    'original_descended_rotating_framing': {'k_Jin': int(k_gamma/degree), 'ell_Jin': int(ell_gamma/degree), 'index': 0},
    'other_framing_changes': '(k,ell) -> (k+n,ell+4*n); index unchanged'
}
(out/'normal_clutch.json').write_text(json.dumps(data, indent=2)+'\n')
print(json.dumps(data, indent=2))
