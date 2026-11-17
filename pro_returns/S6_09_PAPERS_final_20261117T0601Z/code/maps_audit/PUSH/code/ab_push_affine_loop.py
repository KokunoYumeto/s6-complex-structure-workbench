"""Independent exact referee checks for B.4.32.

These identities verify lattice transport, root normalization, and the
actual affine-overlap formulas.  They do not replace the geometric
section-independence argument in B.4.30--B.4.32.
"""
from pathlib import Path
import json
import sympy as S

A1 = S.Matrix([[1, 0, 0, 0], [6, 0, 1, 0],
               [-6, -1, -1, 0], [-2, 1, 0, 1]])
A2 = S.Matrix([[1, 0, 0, 0], [0, 0, -1, 0],
               [-6, 1, 0, 0], [3, 0, 1, 1]])
delta = S.Matrix([0, 0, 0, 1])
gamma = S.Matrix([[1, 0, 0, 0]])
E = delta * gamma
Id = S.eye(4)
assert E * E == S.zeros(4)
for A in (A1, A2):
    assert A * delta == delta
    assert gamma * A == gamma
    assert A * E == E * A
assert A1 ** 3 == Id and A2 ** 4 == Id

B1, B2 = A1[:3, :3], A2[:3, :3]
fixed1 = S.Matrix([1, 2, -4])
fixed2 = S.Matrix([1, 3, -3])
assert B1 * fixed1 == fixed1
assert B2 * fixed2 == fixed2
assert (B1 - S.eye(3)).rank() == 2
assert (B2 - S.eye(3)).rank() == 2
stack = (B1 - S.eye(3)).col_join(B2 - S.eye(3))
minor = stack.extract([1, 2, 4], [0, 1, 2]).det()
assert minor == 6
M1, M2 = B1[1:, 1:], B2[1:, 1:]
U = M1 * M2
V = M2 * U * M2.inv()
assert U == S.Matrix([[1, 0], [-1, 1]])
assert V == S.Matrix([[1, 1], [0, 1]])

m, e = S.symbols('m e', integer=True, positive=True)
T = Id - m * E
power = Id - e * m * E
assert (power * T - (Id - (e + 1) * m * E)).applyfunc(S.expand) == S.zeros(4)
norm = e * Id - m * e * (e - 1) / 2 * E
norm_next = (e + 1) * Id - m * (e + 1) * e / 2 * E
assert (norm + power - norm_next).applyfunc(S.expand) == S.zeros(4)
assert norm.subs(e, 1) == Id
assert (norm - e * Id)[:3, :] == S.zeros(3, 4)

tau, mu, beta, c = S.symbols('tau mu beta c')
P = S.Matrix([[6 * mu, tau, 1, 0], [beta + c, mu, 0, 1]])
ed = S.Matrix([0, 1])
frames = [
    (A1, (tau - 1) / tau, (1 - mu) / tau,
     beta + 2 - 6 * (1 - mu) ** 2 / tau,
     S.Matrix([[-1 / tau, 0], [(1 - mu) / tau, 1]])),
    (A2, -1 / tau, 1 + mu / tau,
     beta - 3 - 6 * mu ** 2 / tau,
     S.Matrix([[1 / tau, 0], [-mu / tau, 1]])),
]
for A, tp, mp, bp, R in frames:
    target_P = S.Matrix([[6 * mp, tp, 1, 0], [bp + c, mp, 0, 1]])
    assert R * ed == ed
    assert R.diff(c) == S.zeros(2)
    assert (R * P - target_P * A).applyfunc(S.factor) == S.zeros(2, 4)

v, w = S.symbols('v w')
Ppart = P.subs(c, 0)
for vector in (S.Matrix([1, 2, -4, 0]), S.Matrix([-1, -3, 3, 0])):
    epsilon = (gamma * vector)[0]
    difference = w * P.subs(c, -12 * v) * vector + 12 * epsilon * w * v * ed
    assert (difference - w * Ppart * vector).applyfunc(S.expand) == S.zeros(2, 1)
    assert difference.diff(v) == S.zeros(2, 1)

s, C, kappa = S.symbols('s C kappa')
sigma = S.Matrix([6 * mu * v, -6 * v ** 2 + v * (C - 12 * kappa)])
L = s + 12 * v
F = S.Matrix([mu * L / 2, C * L / 12 - L ** 2 / 24 + 6 * v])
G = S.Matrix([mu * s / 2, C * s / 12 - s ** 2 / 24])
k = -s + 12 * kappa
assert (F - sigma - k * v * ed - G - 6 * v * ed).applyfunc(S.expand) == S.zeros(2, 1)
assert ((G + 6 * v * ed).subs(v, v + 1) - (G + 6 * v * ed)) == 6 * ed
n, D = S.symbols('n D', integer=True, positive=True)
gamma_period = S.Matrix([6 * mu, C - s - 12 * v])
clutching_jump = F.subs(v, v + n) - F
assert (clutching_jump - n * gamma_period + 6 * n * (n - 1) * ed).applyfunc(S.expand) == S.zeros(2, 1)
period_label = S.Matrix([n, 0, 0, -6 * n * (n - 1)])
assert (gamma * period_label)[0] == n
assert S.ask(S.Q.positive(D * (gamma * period_label)[0])) is True

record = {
    'status': 'PASS',
    'quotient_fixed_lines': [list(fixed1), list(fixed2)],
    'common_fixed_space_rank': int(stack.rank()),
    'nonzero_exact_minor': int(minor),
    'root_normalization': 'Symbolic induction for all positive integers e; not a finite sample.',
    'root_norm': 'e I - m e(e-1)/2 E; quotient is e I',
    'period_covariance': 'Both source-to-target R_j P = P_prime A_j checked exactly.',
    'finite_connector': 'Both full vector connectors are independent of v after c=-12v.',
    'cusp_extra_radial_label': '6 delta',
    'all_cover_clutching_label': 'n gamma - 6n(n-1) delta; gamma evaluation of D times this is Dn > 0',
    'scope': 'Exact algebra only; independent geometric referee is ab_push_global_loop_referee.md.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record, indent=2, default=str) + '\n')
print('PASS: full three-dimensional quotient has zero common fixed space (minor = 6).')
print('PASS: root-transfer formula holds by symbolic induction for every positive degree.')
print('PASS: both actual Lie-frame covariance identities hold and their frames fix delta.')
print('PASS: both finite-place connectors cancel every r logarithm exactly.')
print('PASS: corrected cusp comparison adds only the period 6 delta.')
print('PASS: every positive cover and trace multiplier retains clutching gamma value Dn > 0.')
print('ALL EXACT REFEREE CHECKS PASSED')
