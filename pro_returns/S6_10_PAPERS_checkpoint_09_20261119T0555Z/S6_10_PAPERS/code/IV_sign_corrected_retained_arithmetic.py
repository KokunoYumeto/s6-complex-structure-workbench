"""Current arithmetic of the corrected K50/54/56/57/58/59/60 consequences.

The physical-line and inverse-clutch morphisms are mathematical inputs
reviewed separately in K68. This program never treats the historical
positive central baseline as a current geometric conclusion.
"""
from pathlib import Path
from fractions import Fraction
import datetime
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
REPLAY = ROOT / 'analysis/IV_sign_third_replays/code/part3_fourfold'
checks = []


def exact(name, residual):
    assert s.simplify(residual) == 0, (name, residual)
    checks.append(name)


native = [(0, -6, -1), (0, -6, -1), (-6, 0, -1)]
flopped = [(-n, m + 2*n, z + n) for m, n, z in native]
assert [z % 28 for m, n, z in flopped] == [21, 21, 27]
checks.append('Corrected native Cox increments give 21,21,27')
for m, n, z in native:
    first = (m + 2*n, -n, z + n)
    back = (first[0] + 2*first[1], -first[1], first[2] + first[1])
    assert back == (m, n, z)
checks.append('Actual directed flop and its reverse cancel in free and central coordinates')

j, p, k = s.symbols('j p k', integer=True)
vertical = -1 - 3*j*(j-1)
exact('Corrected vertical positive recurrence', vertical.subs(j, j+1) - vertical + 6*j)
exact('Corrected vertical negative recurrence', vertical.subs(j, j-1) - vertical - (6*j-6))
exact('Vertical period28', vertical.subs(j, j+28) - vertical - 28*(-6*j-81))
exact('Vertical reflection', vertical.subs(j, 1-j) - vertical)
vertical_image = sorted({int(vertical.subs(j, n)) % 28 for n in range(28)})
assert vertical_image == [5, 7, 9, 13, 19, 21, 23, 27]
checks.append('All28 vertical residue positions give the corrected eight-value image')
staircase = -1 - 3*j*(j+1)
branch = -7 - 24*j*(j+1)
exact('Corrected staircase increment', staircase.subs(j, j+1)-staircase+6*(j+1))
exact('Corrected Q1 branch increment', staircase - 21*j*(j+1)-6 - branch)
exact('Second branch period7', branch.subs(j, j+7)-branch + 336*(j+4))
branch_image = sorted({int(branch.subs(j, n)) % 28 for n in range(7)})
assert branch_image == [1, 13, 17, 21]
assert int(branch.subs(j, 1)) % 28 == 1
checks.append('Seven corrected second-branch residues and actual j1 class')

data_inputs = []
infinity_rows = []
for a, b, N, expected_interior, expected_H in [
    (1, 2, 8, Fraction(9333, 16), Fraction(-9301, 16)),
    (2, 1, 6, Fraction(739), Fraction(-734)),
]:
    loaded = {}
    for kind in ['interior_residues', 'h_residues', 'e_cycles']:
        file = REPLAY / f'source_infinity_{kind}_{a}_{b}_{N}.json'
        loaded[kind] = json.loads(file.read_text())
        data_inputs.append({'file': str(file), 'sha256': hashlib.sha256(file.read_bytes()).hexdigest(),
                            'provenance': 'Fresh unchanged-program output from this third review batch'})
    interior = Fraction(loaded['interior_residues']['summary']['total_normal_link_residue']['rational'])
    H = Fraction(loaded['h_residues']['summary']['H_normal_link_residue']['rational'])
    assert (interior, H) == (expected_interior, expected_H)
    E = loaded['e_cycles']
    assert E['summary']['component_count'] == N
    for component in E['components']:
        assert component['intersection_matrix'] == [[-2, 2], [2, -2]]
        assert component['fibre_multiplicities'] == [1, 1]
        assert component['determinant_normal_divisor'] == [0, 0]
    intersection = s.Matrix([[-2, 2], [2, -2]])
    change = s.Matrix([[1, 0], [1, 1]])
    assert change.det() == 1 and change.T*intersection*change == s.diag(0, -2)
    ref = s.Matrix([0, -a])
    reference_square = (ref.T*s.diag(0, -2)*ref)[0]
    assert reference_square == -2*a*a
    # This is the actual closed-double lattice proved in IE.3, not the
    # annular E residue printed by the e_cycles program alone.
    closed_double_square = -reference_square
    per_double = Fraction(-3*int(closed_double_square), 24)
    total = interior + H + N*per_double
    dual_Jin_index = -total
    physical_index = -dual_Jin_index
    assert dual_Jin_index == (0 if a == 1 else 1)
    assert physical_index == (0 if a == 1 else -1)
    infinity_rows.append({'a': a, 'b': b, 'N': N,
        'interior': str(interior), 'H': str(H), 'E_closed_doubles': str(N*per_double),
        'normal_link_sum': str(total), 'dual_Jin_index': str(dual_Jin_index),
        'physical_index': str(physical_index)})
    checks.append(f'Fresh full infinity sums and actual I2 double lattice for {a},{b},{N}')

paired_rows = []
for a, physical_scalar, fixed_infinity in [(1, s.Integer(0), s.Integer(0)), (2, 3*p-1, s.Integer(-1))]:
    actual_infinity = fixed_infinity-2*k*physical_scalar
    pair_sum = a+2*k*physical_scalar
    exact(f'Corrected cut-surface sum a{a}', pair_sum-1+actual_infinity)
    for pv in range(1, 5):
        for kv in range(1, 5):
            value = int(physical_scalar.subs(p, pv))
            total = a+2*kv*value
            solutions = [(x, y) for x in range(28) for y in range(28)
                         if (x+y-total) % 28 == 0 and (y-x-a) % 28 == 0]
            asserted = [((kv*value+14*e) % 28, (a+kv*value+14*e) % 28) for e in (0, 1)]
            assert sorted(solutions) == sorted(asserted)
            paired_rows.append({'a': a, 'p': pv, 'k': kv, 'solutions': solutions})
checks.append('All32 bounded corrected paired congruences have precisely the two stated solutions')
assert [x for x in range(28) if 2*x % 28 == 0] == [0, 14]
checks.append('Kernel of doubling is exactly0,14; no unresolved geometric choice selected by code')

out = {'date': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'status': 'PASS',
       'checks': checks, 'check_count': len(checks), 'vertical_image': vertical_image,
       'second_branch_image': branch_image, 'infinity_rows': infinity_rows,
       'paired_rows': paired_rows, 'fresh_data_inputs': data_inputs,
       'scope': 'Exact corrected arithmetic after the separately proved physical-line, clutch, '
                'fan and E-double maps. Does not prove analytic properness, orientation maps, '
                'unbounded fan existence or the good-branch order-two choice.'}
dest = ROOT/'analysis/IV_sign_corrected_retained_arithmetic.json'
dest.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({key: value for key, value in out.items() if key not in ['paired_rows', 'fresh_data_inputs']}, indent=2))
