"""Fresh exact F2.5 certificates; reads only the clean statement/input packet.

SymPy rational elimination and exact real radicals are used. No original
F2.5/F2.6 producing program is opened, imported, or reused.
"""
from pathlib import Path
from itertools import combinations
from datetime import datetime, timezone
import hashlib
import json
import re
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / 'analysis/continuation_V/F2_5_candidate_statement_input_packet.md'
data = json.loads(re.search(r'```json\s*(.*?)\s*```', PACKET.read_text(), re.S).group(1))
M1, M2 = s.Matrix(data['M1']), s.Matrix(data['M2'])
I = s.eye(6)
checks = []


def zero(name, a):
    entries = list(a) if isinstance(a, s.MatrixBase) else [a]
    assert all(s.simplify(s.expand(x)) == 0 for x in entries), name
    checks.append(name)


def serial(a):
    return [[str(x) for x in row] for row in a.tolist()]


def exterior(a, q):
    choices = list(combinations(range(a.rows), q))
    return s.Matrix([[a.extract(r, c).det() for c in choices] for r in choices])


def columns(v, n):
    return s.Matrix.hstack(*v) if v else s.zeros(n, 0)


def rank_witness(a):
    cs = list(a.rref()[1])
    basis = a[:, cs]
    rs = list(basis.T.rref()[1])
    square = basis[rs, :]
    coefficients = square.inv() * a[rs, :]
    zero('rank reconstruction ' + str(a.shape), basis * coefficients - a)
    return {'rank': len(cs), 'rows': rs, 'columns': cs,
            'minor': str(square.det()), 'coefficients': serial(coefficients)}


rational = []
expected = [(2, 2, 3, 6, 6), (3, 3, 9, 15, 15),
            (4, 4, 9, 17, 20), (3, 3, 9, 15, 15)]
for q in range(1, 5):
    A, B = exterior(M1.T, q), exterior(M2.T, q)
    n = A.rows
    C = (B * A).inv()
    j1 = columns((A - s.eye(n)).nullspace(), n)
    j2 = columns((B - s.eye(n)).nullspace(), n)
    j0 = columns((C - s.eye(n)).nullspace(), n)
    d0 = s.Matrix.vstack(s.Matrix.hstack(j1, s.zeros(n, j2.cols), -j0),
                        s.Matrix.hstack(s.zeros(n, j1.cols), j2, -A * j0))
    delta = s.Matrix.hstack(A - s.eye(n), B - s.eye(n))
    zero(f'actual cellular d squared q{q}', delta * d0)
    rd, rr = rank_witness(d0), rank_witness(delta)
    observed = (j1.cols, j2.cols, j0.cols, rd['rank'], rr['rank'])
    assert observed == expected[q - 1], (q, observed)
    checks.append(f'all rational dimensions q{q}')
    rational.append({'q': q, 'dimension': n, 'stalk_dimensions': list(observed[:3]),
                     'H_dimensions': [d0.cols - rd['rank'],
                                      2 * n - rr['rank'] - rd['rank'], n - rr['rank']],
                     'J1': serial(j1), 'J2': serial(j2), 'J0': serial(j0),
                     'd0': serial(d0), 'delta': serial(delta),
                     'd0_rank_certificate': rd, 'delta_rank_certificate': rr})

J2 = s.Matrix([[0, -1], [1, 0]])
finite = []
for index, (M, order) in enumerate([(M1, 5), (M2, 4)], 1):
    zero(f'finite order site{index}', M ** order - I)
    v = s.Matrix(data[f'v{index}'])
    zero(f'affine fixed numerator site{index}', M * v - v)
    plus = sum((M ** k for k in range(order)), s.zeros(6)) / order
    if order == 5:
        X = columns(plus.columnspace() + (I - plus).columnspace(), 6)
        D = (X.inv() * M * X)[2:6, 2:6]
        s72 = s.sqrt(10 + 2 * s.sqrt(5)) / 4
        s144 = s.sqrt(10 - 2 * s.sqrt(5)) / 4
        aa = s.Rational(2, 5) * (s72 + s144)
        bb = s.Rational(2, 5) * (s144 - s72)
        K = aa * (D - D.inv()) + bb * (D ** 2 - D ** -2)
        J = X * s.diag(J2, K) * X.inv()
    else:
        minus = sum(((-1) ** k * M ** k for k in range(order)), s.zeros(6)) / order
        rotating = I - plus - minus
        X = columns(plus.columnspace() + minus.columnspace() + rotating.columnspace(), 6)
        J = X * s.diag(J2, J2, s.zeros(2)) * X.inv() + M * rotating
    zero(f'actual finite complex square site{index}', J * J + I)
    zero(f'actual finite complex commutator site{index}', M * J - J * M)
    flip = X * s.diag(1, -1, 1, 1, 1, 1) * X.inv()
    opposite = flip * J * flip.inv()
    zero(f'orientation flip determinant site{index}', flip.det() + 1)
    zero(f'orientation flip remains equivariant site{index}', M * opposite - opposite * M)
    zero(f'orientation flip complex square site{index}', opposite * opposite + I)
    finite.append({'site': index, 'basis': serial(X), 'J': serial(J),
                   'opposite_orientation_J': serial(opposite),
                   'orientation_switch': serial(flip), 'switch_determinant': str(flip.det())})

# The prereading van Kampen proof first puts the remaining generator in Lambda,
# making the group abelian. This is its exact integral relation matrix.
relations = s.Matrix([[-1, 5, 0], [1, 0, 4], [0, 1, 1]])
zero('fundamental-group relation determinant', relations.det() + 1)
assert all(x.q == 1 for x in relations.inv())
checks.append('integral inverse of actual abelian relations')

t = s.symbols('t', integer=True)
c2sq = (720 * t + 6) / 3
sigma = s.expand((3 * c2sq + 84) / 45)
zero('Todd/signature substitution', sigma - (16 * t + 2))
lower, upper = s.ceiling(s.Rational(-6, 16)), s.floor(s.Rational(2, 16))
assert lower == upper == 0
checks.append('exact integer signature bound')

out = {'status': 'PASS', 'finished_at_utc': datetime.now(timezone.utc).isoformat(),
       'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'packet_sha256': hashlib.sha256(PACKET.read_bytes()).hexdigest(),
       'method': 'new SymPy rational nullspaces/minors and exact real radicals',
       'checks': len(checks), 'check_names': checks, 'rational_complexes': rational,
       'actual_finite_complex_structures': finite,
       'fundamental_group_relations': serial(relations),
       'relations_inverse': serial(relations.inv()), 'signature_formula': str(sigma),
       'Todd_integer_interval': [int(lower), int(upper)], 'signature': 2,
       'scope': 'Direct independent matrix, finite-complex-structure and index certificates. No conclusion of F2.6/P1.12/P1.13 imported; no original producing program read or reused.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({k: v for k, v in out.items() if k not in
                  ('rational_complexes', 'actual_finite_complex_structures')}, indent=2))
