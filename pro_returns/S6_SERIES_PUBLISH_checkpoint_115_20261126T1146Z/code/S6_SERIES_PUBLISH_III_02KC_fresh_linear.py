#!/usr/bin/env python3
"""Fresh exact rational attachment calculation for 02KC, before proof exposure.

Inputs are the two defining monodromy matrices and marked affine vectors.
No manuscript, prior program, prior result file or target-proof text is read.
The geometric identification of these maps is proved in the fresh derivation.
"""

from datetime import datetime, timezone
from itertools import combinations
import argparse
import json
from pathlib import Path

import sympy as S


def exterior(A, degree):
    indices = list(combinations(range(A.rows), degree))
    return S.Matrix([
        [A.extract(rows, cols).det() for cols in indices]
        for rows in indices
    ])


def wedge(a, b):
    return S.Matrix([a[i] * b[j] - a[j] * b[i]
                     for i, j in combinations(range(4), 2)])


def strings(A):
    return [[str(S.factor(x)) for x in row] for row in A.tolist()]


def zero(A):
    return all(S.cancel(x) == 0 for x in A)


started = datetime.now(timezone.utc).isoformat()
T1 = S.Matrix([[1, 0, -6, 2], [0, -1, 1, 1],
               [0, -1, 0, 1], [0, 0, 0, 1]])
T2 = S.Matrix([[1, 6, 0, -3], [0, 0, -1, 1],
               [0, 1, 0, 0], [0, 0, 0, 1]])
A1, A2 = T1.inv().T, T2.inv().T
A0 = (A1 * A2).inv()
I4, I6 = S.eye(4), S.eye(6)
gamma, u, w, delta = [I4[:, i] for i in range(4)]
epsilon1 = S.Matrix([1, 2, -4, 0])
epsilon2 = S.Matrix([1, 3, -3, 0])
q = S.Matrix([[0, 0, 6, 1, 0, 0]])
assert A1 ** 3 == I4 and A2 ** 4 == I4
assert A1 * epsilon1 == epsilon1 and A2 * epsilon2 == epsilon2
assert A1 * delta == A2 * delta == A0 * delta == delta
assert A0 * w == w

D1 = (A1 - I4).row_join(A2 - I4)
D2 = (exterior(A1, 2) - I6).row_join(exterior(A2, 2) - I6)
assert D1.rank() == 3 and D2.rank() == 5
assert zero(q * D2)
assert (q * wedge(u, w))[0] == 1

Z4 = S.zeros(4, 1)
horizontal = S.Matrix.hstack(
    epsilon1.col_join(Z4), delta.col_join(Z4),
    Z4.col_join(epsilon2), Z4.col_join(delta),
    (-A1.inv() * w).col_join(-w),
)
assert zero(D1 * horizontal) and horizontal.rank() == 5
cusp_delta = (-A1.inv() * delta).col_join(-delta)
assert cusp_delta == -horizontal[:, 1] - horizontal[:, 3]
assert -A1.inv() * w == u - delta

fixed_dimensions = {}
for name, A in [('A1', A1), ('A2', A2), ('A0', A0)]:
    fixed_dimensions[name] = [
        S.binomial(4, k) - (exterior(A, k) - S.eye(S.binomial(4, k))).rank()
        for k in range(1, 5)
    ]
assert fixed_dimensions == {'A1': [2, 2, 2, 1],
                            'A2': [2, 2, 2, 1],
                            'A0': [2, 4, 2, 1]}

l0, l1, l2, k1, k2, a, b, c = S.symbols('l0 l1 l2 k1 k2 a b c')
p = 12*l0 - 4*l1 - 3*l2
v1, v2 = l1*epsilon1 + k1*delta, l2*epsilon2 + k2*delta
winding = l0*gamma + a*u + b*w + c*delta
vertical = [
    -(q*wedge(v1, epsilon1))[0]/3,
    -(q*wedge(v1, delta))[0]/3,
    -(q*wedge(v2, epsilon2))[0]/4,
    -(q*wedge(v2, delta))[0]/4,
    (q*wedge(winding, w))[0],
    (q*wedge(winding, delta))[0],
]
assert vertical == [2*k1, -2*l1, S.Rational(3,2)*k2,
                    -S.Rational(3,2)*l2, a, 6*l0]
M2 = S.zeros(6, 6)
M2[0, :] = S.Matrix([vertical])
for i in range(5):
    M2[i+1, i] = 1
M2[2, 5] = M2[4, 5] = -1
assert S.cancel(M2.det() + p/2) == 0
relation = M2[:, 5] + M2[:, 1] + M2[:, 3]
assert relation == S.Matrix([p/2, 0, 0, 0, 0, 0])

def inverse_degree_two(rhs):
    z, x1, x2, x3, x4, x5 = rhs
    t = 2*(z - 2*k1*x1 + 2*l1*x2 - S.Rational(3,2)*k2*x3
           + S.Rational(3,2)*l2*x4 - a*x5)/p
    return S.Matrix([x1, x2+t, x3, x4+t, x5, t])

inverse2 = S.Matrix.hstack(*[inverse_degree_two(S.eye(6)[:, i])
                              for i in range(6)])
assert zero(M2*inverse2-S.eye(6)) and zero(inverse2*M2-S.eye(6))

# Mayer--Vietoris degree-one map, with signs (exterior, -fillings).
# Columns: finite1(epsilon1,delta,t1), finite2(epsilon2,delta,t2),
# cusp(gamma,u,t0). Rows: exterior(gamma,t1,t2), finite1(epsilon1,delta),
# finite2(epsilon2,delta), cusp(gamma,u).
M1 = S.zeros(9, 9)
M1[0, 0] = M1[0, 3] = M1[0, 6] = 1
M1[1, 2] = M1[2, 5] = 1
M1[1, 8] = M1[2, 8] = -1
M1[3, 0] = M1[4, 1] = -1
M1[3, 2], M1[4, 2] = -l1/3, -k1/3
M1[5, 3] = M1[6, 4] = -1
M1[5, 5], M1[6, 5] = -l2/4, -k2/4
M1[7, 6] = M1[8, 7] = -1
M1[7, 8], M1[8, 8] = l0, a

def inverse_degree_one(rhs):
    eg, et1, et2, n1e, n1d, n2e, n2d, n0g, n0u = rhs
    z0 = 12*(eg+n1e+n2e+n0g+l1*et1/3+l2*et2/4)/p
    z1, z2 = et1+z0, et2+z0
    return S.Matrix([-n1e-l1*z1/3, -n1d-k1*z1/3, z1,
                     -n2e-l2*z2/4, -n2d-k2*z2/4, z2,
                     l0*z0-n0g, a*z0-n0u, z0])

inverse1 = S.Matrix.hstack(*[inverse_degree_one(S.eye(9)[:, i])
                              for i in range(9)])
assert zero(M1*inverse1-S.eye(9)) and zero(inverse1*M1-S.eye(9))
assert S.factor(M1.det()/p) in [S.Rational(1,12), S.Rational(-1,12)]

# The actual cusp degree-two incidence matrix on a deck-character t.
# Component basis H,E_A,E_B,E_C; edge directions e1,e2,e1-e2.
t = S.symbols('t', nonzero=True)
ca = S.Matrix([1,-1,0,-1])
cb = S.Matrix([0,1,0,0])
cc = S.Matrix([1,-1,-1,0])
cd = S.Matrix([0,0,1,0])
ce = S.Matrix([1,0,-1,-1])
cf = S.Matrix([0,0,0,1])
cusp_D = S.Matrix.hstack(ca-cd, cb-t*ce, cf-cc/t)
column_change = S.Matrix([[1,t,1/t],[0,1,0],[0,0,1]])
cusp_reduced = S.Matrix.hstack(ca-cd, (1-t)*cb, (1-1/t)*cf)
assert zero(cusp_D*column_change - cusp_reduced)
assert column_change.det() == 1
minor = S.factor(cusp_reduced.extract([0,1,3],[0,1,2]).det())
assert S.factor(minor - (1-t)*(1-1/t)) == 0
cusp_kernel_at_one = S.Matrix([[1,1],[1,0],[0,1]])
assert cusp_D.subs(t,1).rank() == 1
assert zero(cusp_D.subs(t,1)*cusp_kernel_at_one)
assert cusp_kernel_at_one.rank() == 2

report = {
    'scope': 'Fresh exact rational attachment and character algebra for 02KC; no target-proof/program/result file read.',
    'started_utc': started,
    'finished_utc': datetime.now(timezone.utc).isoformat(),
    'sympy_version': S.__version__,
    'A1': strings(A1), 'A2': strings(A2), 'A0': strings(A0),
    'fixed_dimensions_exterior_degrees_1_to_4': {
        name: [int(x) for x in dims] for name,dims in fixed_dimensions.items()},
    'exterior_D1_rank': int(D1.rank()),
    'exterior_degree2_relation_rank': int(D2.rank()),
    'q_pairing_row': strings(q),
    'horizontal_basis': strings(horizontal),
    'horizontal_basis_rank': int(horizontal.rank()),
    'horizontal_boundary_zero': True,
    'cusp_delta_horizontal_relation': 'cusp_delta = -finite1_delta - finite2_delta',
    'degree1_MV_map': strings(M1),
    'degree1_determinant': str(S.factor(M1.det())),
    'degree1_explicit_inverse_both_compositions_identity': True,
    'degree2_filling_kernel_map': strings(M2),
    'degree2_determinant': str(S.factor(M2.det())),
    'degree2_delta_relation': strings(relation),
    'degree2_explicit_inverse_both_compositions_identity': True,
    'cusp_character_D': strings(cusp_D),
    'cusp_column_change': strings(column_change),
    'cusp_reduced_D': strings(cusp_reduced),
    'cusp_nontrivial_character_minor': str(minor),
    'cusp_kernel_at_character_one': strings(cusp_kernel_at_one),
    'universal_conclusions': [
        'For every admissible datum p is nonzero; the displayed degree1 and degree2 inverse maps are defined.',
        'The degree2 relation coefficient is exactly p/2, with all k1,k2 and non-gamma cusp winding terms accounted for.',
        'For every t not equal to 1 the displayed cusp minor is nonzero; at t=1 the rank is one.',
        'These are symbolic identities, not an inference from a finite list of parameter samples.',
    ],
}
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path,
                    help='Optional output path; the default only prints and preserves existing output.')
args = parser.parse_args()
if args.output is not None:
    args.output.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
