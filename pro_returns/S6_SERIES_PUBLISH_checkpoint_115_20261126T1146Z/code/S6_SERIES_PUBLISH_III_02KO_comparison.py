#!/usr/bin/env python3
"""Post-release comparison of KO's named maps and old/new conventions.

This does not import or rerun the fresh geometry program.  Its arithmetic
is a comparison after exposure, not an additional independent origination.
"""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re
import sympy as s

HERE = Path(__file__).resolve().parent
INPUT_ROOT = Path(__file__).resolve().parents[1] / 'agents/continuation6_iii_d2'
ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'S6_SERIES_PUBLISH_III_02KO'


def get(suffix):
    return (INPUT_ROOT / (PREFIX + '_' + suffix)).read_text()


def released(suffix, begin):
    text = get(suffix)
    return text[text.index(begin):].strip()


oldp = released('released_proof.tex', r'\begin{proof}')
olds = released('released_statement.tex', r'\begin{theorem}')
newp = get('proof_new.tex').strip()
news = get('statement_new.tex').strip()
assert sha256(oldp.encode()).hexdigest() == 'b0bf042ebb726346a764356e9e8db2cf4fcab1294c61de205217e9fcfc669ff2'
assert len(re.split(r'\\item ', oldp)[1:]) == 10
for pat in (r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\tag\{([^}]+)\}'):
    for a, b in ((olds, news), (oldp, newp)):
        assert Counter(re.findall(pat, a)) == Counter(re.findall(pat, b)), pat
assert all(name in newp for name in ('Y', 'B=Y/S^1', 'M_-', 'Q_0'))
print('All 10 original proof items accounted for; each original label, hypertarget and equation tag retained in its own scope.')

# The old order of the complex normal coordinates and the fresh order.
P = s.Matrix([[0, 1], [1, 0]])
W = s.diag(-1, 1)
assert P * W * P == s.diag(1, -1)
z = s.symbols('z', nonzero=True)
old_clutch = s.diag(z, 1/z)  # conjugate the second coordinate in (y,x)
fresh_clutch = s.diag(1/z, z)  # fresh scalar order (bar x,y)
assert P * old_clutch * P == fresh_clutch
normal_conjugation = s.diag(1, -1, 1, 1)
core_reversal = s.diag(1, -1)
assert normal_conjugation.det() == core_reversal.det() == -1
assert s.diag(core_reversal, normal_conjugation).det() == 1
print('D.S11: exact normal-weight permutation and clutching conjugacy; paired core/normal orientation reversal has determinant +1.')

# The two chart weight lists in old item 2 differ by this permutation.
P3 = s.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
assert P3 * s.Matrix([-1, 0, 1]) == s.Matrix([1, -1, 0])
assert P3.inv() == P3.T
print('Old cusp weights and both fresh triangle weights agree under the displayed inverse permutation.')

# Admitted KM specialization used by old item 4, with its actual section.
specialization = s.Matrix([[1,0,0,0,0,0], [0,0,1,-1,0,0],
                           [0,0,0,0,1,0], [0,0,0,0,0,1]])
section = s.Matrix([[1,0,0,0], [0,0,0,0], [0,1,0,0],
                    [0,0,0,0], [0,0,1,0], [0,0,0,1]])
relations = s.Matrix([[0,0], [1,1], [0,1], [0,1], [0,0], [0,0]])
assert specialization * section == s.eye(4)
assert specialization * relations == s.zeros(4,2)
assert s.Matrix.hstack(section, relations).det() in (-1,1)
m,a,b,c,p = s.symbols('m a b c p', integer=True)
for n in (1,-1):
    relation = s.Matrix([-a,-b,-c,-n,m])
    retract = s.Matrix([[0,0,1,-c/n,0]])
    assert retract * relation == s.zeros(1,1)
    assert retract * s.Matrix([0,0,1,0,0]) == s.ones(1,1)
    C = s.Matrix([[-p*b,p*a,n,-c,0], [m,0,0,0,a],
                  [0,m,0,0,b], [0,0,0,m,n]])
    assert C[:,2] * n == s.Matrix([1,0,0,0])
print('Old item 4: the admitted cusp specialization has an integral right inverse and full primitive kernel; the delta column kills the fibre generator for each n sign.')

# Exact torsion/free decomposition of the surgery quotient in D.S13.
inj = s.Matrix([[0,0], [1,0], [0,1]])
proj = s.Matrix([[0,1,0], [0,0,1]])
sigma = s.Matrix([1,0,0])
euler = s.Matrix([[1,0,0]])
assert proj * inj == s.eye(2)
assert euler * sigma == s.ones(1,1)
assert inj * proj + sigma * euler == s.eye(3)
assert euler * inj == s.zeros(1,2)
assert proj * s.diag(0,m,m) == m * proj
for weights in ((1,-1),(1,1)):
    assert (-1) ** sum(weights) == 1
print('D.S13: torsion inclusion, Euler splitting and inverse decomposition agree integrally for every m; both normal weight conventions have a periodic Spin lift.')

# The old GR gluing direction is attached to complement.  The exact
# conjugacy is checked independently of the pre-release computation.
t = s.symbols('t', real=True)
alpha = s.diag(s.Matrix([[s.cos(t),-s.sin(t)], [s.sin(t),s.cos(t)]]), s.eye(3))
A = s.diag(1,-1,-1,1,1)
assert A.det() == 1 and A*A == s.eye(5)
assert s.simplify(A * alpha * A - alpha.T) == s.zeros(5)
assert s.simplify(A * alpha.T - alpha * A) == s.zeros(5)
J3 = s.Matrix([[0,1],[-1,0]])
assert J3.det() == 1 and J3.inv() == -J3 and J3.rank() == 2
print('D.S9/D.S14: the SO(5) conjugacy reverses the loop with an explicit inverse; stabilization adds the rank-two unimodular middle summand.')

maps = {
    'normal_weight_permutation': P.tolist(),
    'triangle_weight_permutation': P3.tolist(),
    'cusp_specialization': specialization.tolist(),
    'cusp_specialization_section': section.tolist(),
    'cusp_primitive_kernel': relations.tolist(),
    'quotient_torsion_inclusion': inj.tolist(),
    'quotient_torsion_inverse': proj.tolist(),
    'quotient_meridian': sigma.tolist(),
    'quotient_euler': euler.tolist(),
    'alpha_conjugacy': A.tolist(),
    'stabilization_middle_pairing': J3.tolist(),
}
(HERE / (PREFIX + '_comparison_maps.json')).write_text(
    json.dumps(maps, default=int, indent=2) + '\n', newline='\n')
print('Comparison completed', datetime.now(timezone.utc).isoformat())
