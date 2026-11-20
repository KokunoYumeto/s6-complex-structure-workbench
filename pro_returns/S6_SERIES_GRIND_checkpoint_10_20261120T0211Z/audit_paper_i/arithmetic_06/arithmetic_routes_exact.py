#!/usr/bin/env python3
"""Exact corroboration of two bounded arithmetic routes; no transcendence claim.

Written after the frozen prereading_new_routes.md derivation and after checking
the corresponding Huber--Wuestholz source statements/proofs. This is a fresh
symbolic implementation, not a recovered historical program.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import sympy as S


ROOT = Path(__file__).resolve().parent
checks = []


def check(name, lhs, rhs=0):
    if isinstance(lhs, S.MatrixBase):
        rhs = S.zeros(*lhs.shape) if rhs == 0 else rhs
        ok = all(S.simplify(x) == 0 for x in lhs-rhs)
    else:
        ok = S.simplify(lhs-rhs) == 0
    checks.append({"name": name, "passed": bool(ok)})
    if not ok:
        raise AssertionError(name)


def serial(matrix):
    return [[str(x) for x in row] for row in matrix.tolist()]


def compound(matrix):
    pairs = list(itertools.combinations(range(matrix.rows), 2))
    return S.Matrix([[matrix.extract(rows, cols).det()
                      for cols in pairs] for rows in pairs])


t, w1, w2, e1, e2, u, z, v, s = S.symbols(
    't w1 w2 e1 e2 u z v s', nonzero=True)
k1, k2 = S.symbols('k1 k2')
P = S.Matrix([[t, k1, k2, v], [0, w1, w2, u],
              [0, e1, e2, z], [0, 0, 0, 1]])
C = compound(P)
pairs = list(itertools.combinations(range(4), 2))
weights = [-2, -1, -1, 0]
wedge_weights = [weights[i]+weights[j] for i, j in pairs]
check('actual_compact_minor', C[0, 4], k1*u-w1*v)
check('central_change_of_actual_minor',
      C[0, 4].subs(v, v+t*s)-C[0, 4], -t*s*w1)
check('exterior_weights', S.Matrix(wedge_weights),
      S.Matrix([-3, -3, -2, -2, -1, -1]))
check('twisted_exterior_weights', S.Matrix(wedge_weights)+2*S.ones(6, 1),
      S.Matrix([-1, -1, 0, 0, 1, 1]))

sub_indices = [0, 1, 2, 3]
quot_indices = [2, 3, 4, 5]
sub = C.extract(sub_indices, sub_indices)
quot = C.extract(quot_indices, quot_indices)
check('W_minus_2_is_preserved', C.extract([4, 5], sub_indices))
check('W_minus_3_is_preserved', C.extract(quot_indices, [0, 1]))
check('central_variable_absent_from_W_minus_2', sub.diff(v))
check('central_variable_absent_from_quotient_by_W_minus_3', quot.diff(v))
input_vector = S.eye(6)[:, 4]
check('actual_Betti_input_in_Gr_minus_1', input_vector.extract([4, 5], [0]),
      S.Matrix([1, 0]))
check('actual_deRham_row_nonzero_on_W_minus_3',
      S.eye(6)[0, :].extract([0], [0, 1]), S.Matrix([[1, 0]]))

# Literal convention eta_1 omega_2 - eta_2 omega_1 = t.
legendre_e2 = (e1*w2-t)/w1
substitution = {k1: z*w1-e1*u, k2: z*w2-e2*u}
Pdiag = P.subs(substitution).subs(e2, legendre_e2)
Cdiag = compound(Pdiag)
check('diagonal_legendre_subblock',
      S.simplify(Cdiag.extract(sub_indices, sub_indices)/t),
      S.Matrix([[w1, w2, u, -u],
                [e1, legendre_e2, z, -z],
                [0, 0, 1, 0], [0, 0, 0, -1]]))
check('Legendre_recovery_u',
      ((k1*w2-k2*w1)/(-t)).subs(substitution).subs(e2, legendre_e2), u)
check('Legendre_recovery_zeta',
      ((k1*e2-k2*e1)/(-t)).subs(substitution).subs(e2, legendre_e2), z)

# Exact constant basis changes identify the two central-free blocks.
sub_left = S.diag(1, 1, 1, 1)
sub_left[2, 3] = 1
sub_right = S.diag(1, 1, 1, -1)
sub_right[2, 3] = -1
P_point = S.Matrix([[w1, w2, u], [e1, legendre_e2, z], [0, 0, 1]])
sub_expected = S.diag(P_point, S.ones(1, 1))
check('subblock_is_point_motive_plus_lattice',
      sub_left*Cdiag.extract(sub_indices,sub_indices)*sub_right/t,
      sub_expected)
quot_left = S.eye(4)
quot_left[0, 1] = -1
quot_right = S.eye(4)
quot_right[0, 1], quot_right[1, 1] = 1, -1
P_group = Pdiag[:3, :3]
check('quotient_is_group_motive_plus_Tate',
      quot_left*Cdiag.extract(quot_indices,quot_indices)*quot_right,
      S.diag(S.Matrix([[t]]), P_group))
for name, change in [('sub_left',sub_left),('sub_right',sub_right),
                     ('quot_left',quot_left),('quot_right',quot_right)]:
    check(name+'_unimodular', change.det()**2, 1)

# Cartier duality is t*P_group^(-transpose), not an isogeny with [0->G].
dual_left = S.Matrix([[0,0,1],[0,-1,0],[1,0,0]])
dual_right = S.Matrix([[0,0,1],[0,1,0],[-1,0,0]])
check('exact_Cartier_dual_period_transport',
      dual_left*(t*P_group.inv().T)*dual_right, P_point)
check('Cartier_dual_left_unimodular', dual_left.det()**2, 1)
check('Cartier_dual_right_unimodular', dual_right.det()**2, 1)

# The diagonal self-duality leaves the central coordinate v entirely free.
JB = S.Matrix([[0, 0, 0, 1], [0, 0, 1, 0],
               [0, -1, 0, 0], [-1, 0, 0, 0]])
JD = S.Matrix([[0, 0, 0, 1], [0, 0, -1, 0],
               [0, 1, 0, 0], [-1, 0, 0, 0]])
check('diagonal_symplectic_comparison_for_arbitrary_v', Pdiag.T*JD*Pdiag, t*JB)
check('diagonal_symplectic_comparison_survives_central_change',
      Pdiag.subs(v, v+t*s).T*JD*Pdiag.subs(v, v+t*s), t*JB)

# Primitive exterior bases: 01,02,03-12,13,23 on Betti;
# 01,02,03+12,13,23 on de Rham. Both primitive kernels have dimension 5.
BB = S.zeros(6, 5)
BD = S.zeros(6, 5)
for index, row in enumerate([0, 1, 4, 5]):
    column = [0, 1, 3, 4][index]
    BB[row, column] = BD[row, column] = 1
BB[2, 2], BB[3, 2] = 1, -1
BD[2, 2], BD[3, 2] = 1, 1
pairB = S.Matrix([[JB[i, j] for i, j in pairs]])
pairD = S.Matrix([[JD[i, j] for i, j in pairs]])
check('primitive_Betti_kernel', pairB*BB)
check('primitive_deRham_kernel', pairD*BD)
check('primitive_Betti_rank', BB.rank(), 5)
check('primitive_deRham_rank', BD.rank(), 5)
primitive = (Cdiag*BB).extract([0, 1, 2, 4, 5], range(5))
check('exact_primitive_comparison', BD*primitive, Cdiag*BB)
check('actual_minor_in_primitive_comparison', primitive[0, 3],
      u*(z*w1-e1*u)-w1*v)
check('primitive_central_derivative_rank', primitive.diff(v).rank(), 2)

# Five actual CM classes in the full order Z[(1+beta)/2].
# A lists coefficients in (1,beta). U is a literal unimodular character change.
A = S.Matrix([[1, 0], [0, 1], [S.Rational(1, 2), S.Rational(1, 2)],
              [2, -1], [S.Rational(3, 2), S.Rational(1, 2)]])
U = S.Matrix([[1, 0, 0, 0, 0], [0, 0, 1, 0, 0],
              [1, 1, -2, 0, 0], [-3, 0, 2, 1, 0],
              [-1, 0, -1, 0, 1]])
normal = S.Matrix([[1, 0], [S.Rational(1, 2), S.Rational(1, 2)],
                   [0, 0], [0, 0], [0, 0]])
check('unimodular_CM_change_det', U.det(), -1)
check('integral_inverse_CM_change', U*U.inv(), S.eye(5))
check('CM_extension_exact_normal_form', U*A, normal)
check('all_three_split_character_rows', U[2:, :]*A)
check('split_character_rank', U[2:, :].rank(), 3)
check('two_nonsplit_CM_classes_rank', normal[:2, :].rank(), 2)
for i, entry in enumerate(U.inv()):
    check(f'unimodular_inverse_integral_{i}', S.denom(entry), 1)

# Explicit comparison maps between bases (1,beta) and (1,(1+beta)/2).
# F covers [2] on E, with torus (t1,t2)->(t1^2,t1*t2).
# G covers id on E, with torus (s1,s2)->(s1,s1^-1*s2^2).
F = S.Matrix([[2, 0], [1, 1]])
G = S.Matrix([[1, 0], [-1, 2]])
L = normal[:2, :]
check('F_extension_compatibility_base_two', F, 2*L)
check('G_extension_compatibility_base_identity', G*L, S.eye(2))
check('G_composed_F_torus_is_multiplication_two', G*F, 2*S.eye(2))
check('F_composed_G_torus_is_multiplication_two', F*G, 2*S.eye(2))
check('F_torus_degree', abs(F.det()), 2)
check('G_torus_degree', abs(G.det()), 2)
check('composite_total_degree', (4*abs(F.det()))*abs(G.det()), 2**4)

# The Ribet projection condition in this CM order has positive norm n^2+19m^2.
n, m, beta = S.symbols('n m beta')
check('Ribet_projection_norm',
      S.rem(S.expand((n-m*beta)*(n+m*beta)), beta**2+19, beta), n*n+19*m*m)

result = {
    'author': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same family',
    'phase': 'S6_SERIES_GRIND',
    'scope': ('Exact algebraic corroboration of the exterior-square/truncation route '
              'and finite CM extension-character reduction. No evaluation or '
              'transcendence conclusion for N(Q).'),
    'sympy_version': S.__version__,
    'checks_passed': len(checks),
    'checks': checks,
    'ordered_wedge_pairs': pairs,
    'wedge_weights': wedge_weights,
    'period_matrix': serial(P),
    'compound_matrix': serial(C),
    'W_minus_2_block': serial(sub),
    'quotient_by_W_minus_3_block': serial(quot),
    'diagonal_primitive_compound': serial(primitive),
    'subblock_left_basis_change': serial(sub_left),
    'subblock_right_basis_change': serial(sub_right),
    'quotient_left_basis_change': serial(quot_left),
    'quotient_right_basis_change': serial(quot_right),
    'Cartier_dual_left_basis_change': serial(dual_left),
    'Cartier_dual_right_basis_change': serial(dual_right),
    'CM_coefficient_matrix': serial(A),
    'unimodular_character_change': serial(U),
    'unimodular_character_change_inverse': serial(U.inv()),
    'CM_reduced_coefficients': serial(normal),
    'F_base_multiplication': 2,
    'F_torus_matrix': serial(F),
    'F_degree': 8,
    'G_base_multiplication': 1,
    'G_torus_matrix': serial(G),
    'G_degree': 2,
    'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
output = ROOT/'arithmetic_routes_exact.output.json'
output.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'checks_passed': len(checks), 'output': str(output),
                  'program_sha256': result['program_sha256']}, indent=2))
