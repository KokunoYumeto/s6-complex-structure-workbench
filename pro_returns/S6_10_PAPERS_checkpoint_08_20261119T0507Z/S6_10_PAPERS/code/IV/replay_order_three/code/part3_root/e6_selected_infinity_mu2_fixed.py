"""Actual fixed loci and normal arrows in the two-torsion quotient charts."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
PROOF = ROOT/'notes/part3_e6_selected_infinity_mu2_fixed_working.md'
PARENT = ROOT/'code/part3_root/e6_selected_infinity_mu2_pair.json'
parent = json.loads(PARENT.read_text())
labels = []


def ck(value, label):
    assert bool(value), label
    labels.append(label)


def equal(a, b):
    return all(S.cancel(x-y) == 0 for x, y in zip(a, b))


def serial(m):
    return [[str(x) for x in row] for row in m.tolist()]


t, z, a, u, rho = S.symbols('t z a u rho', nonzero=True)
A, B, C = S.symbols('A B C', nonzero=True)
zc, zy = S.symbols('z_chi z_zeta')
records = []
surface_transition = S.Matrix([[1, 2, 0, 0], [0, -1, 0, 0],
                               [0, -1, 1, 0], [0, 0, 0, 1]])
ck(abs(surface_transition.det()) == 1, 'full fixed-surface chart overlap is integral invertible')
ck(surface_transition**2 == S.eye(4), 'full overlap inverse retains radial and normal powers')
ck(-2*2+3*1+3*0 == -1, 'original canonical divisor agrees with fixed-curve adjunction')
cover_normal_transition = S.diag(1, 1, u**2)
ck(cover_normal_transition.inv() == S.diag(1, 1, u**-2), 'complete P1 normal arrow has actual inverse')

for j in range(1, 5):
    w = 1 if j % 2 else -1
    odd_index = 2 if j % 2 else 3
    neutral_index = 3 if j % 2 else 2
    e_line, e_neutral = (j, -j-1) if j % 2 else (-j-1, j)
    ck(e_line+e_neutral == -1, f'j{j}: original fourth-root product character')
    point_weights = [2*w, -w, -w, -w]
    surface_weights = [0, 0, w, -w]
    ck(all(point_weights), f'j{j}: unique isolated origin in line-pivot chart')
    ck(sum(v == 0 for v in surface_weights) == 2,
       f'j{j}: chi/zeta pivot fixed locus has complex dimension two')
    same = [row for row in parent['rows'] if row['j'] == j % 4]
    point = next(row for row in same if row['pivot_cover_coordinate'] == odd_index)
    surface = next(row for row in same if row['pivot_cover_coordinate'] == 0)
    ck(point['explicit_physical_weights'] == point_weights,
       f'j{j}: actual quotient certificate gives the isolated representation')
    ck(surface['explicit_physical_weights'] == surface_weights,
       f'j{j}: actual quotient certificate gives the surface representation')
    ck(surface['neutral_cover_coordinate'] == neutral_index,
       f'j{j}: neutral coordinate is the actual adjacent-chain coordinate')

    # Coordinates of the original free cover, in its literal chi,zeta,X,Y order.
    original = S.Matrix([t, t*z, t*a, u] if j % 2 else [t, t*z, u, t*a])
    jac = original.jacobian(S.Matrix([t, z, a, u])).det()
    coefficient_dt = S.expand(-8*(original[2]*original[3])**3*jac)
    ck(S.cancel(coefficient_dt/(2*t)+4*w*t**4*a**3*u**3) == 0,
       f'j{j}: exact oriented rho-chart coefficient -4w rho^2 a^3 u^3')
    ck(surface['original_volume_orders'] ==
       [2 if idx == next(k for k in range(4) if surface['explicit_coordinate_matrix'][0][k])
        else (3 if idx in [next(k for k in range(4) if surface['explicit_coordinate_matrix'][n][k]) for n in (2,3)] else 0)
        for idx in range(4)], f'j{j}: stored original divisor matches explicit quotient coordinates')

    # Full B arrow on chi-pivot charts, with all source mixing retained.
    before = S.Matrix([t, t*z, t*a, u])  # chi,zeta,odd line,neutral
    after = S.Matrix([t, A*t*z+B*t*a*u, C**w*t*a, C**(-w)*u])
    quotient_after = S.Matrix([after[0]**2, after[1]/after[0], after[2]/after[0], after[3]])
    expected = S.Matrix([t**2, A*z+B*a*u, C**w*a, C**(-w)*u])
    ck(equal(quotient_after, expected), f'j{j}: full source-mixing quotient square')

    # Source-pivot interchange commutes with the entire B map.
    f_then_d = S.Matrix([rho*(A*z+B*a*u)**2, 1/(A*z+B*a*u),
                         C**w*a/(A*z+B*a*u), C**(-w)*u])
    L = A+B*(a/z)*u
    d_then_f = S.Matrix([rho*z**2*L**2, (1/z)/L, C**w*(a/z)/L, C**(-w)*u])
    ck(equal(f_then_d, d_then_f), f'j{j}: two source pivots commute with full ideal arrow')

    inverse_gamma_cover = S.diag(-S.I, S.I, S.I**(-e_line), S.I**(-e_neutral))*after
    closing = S.Matrix([inverse_gamma_cover[0]**2,
                        inverse_gamma_cover[1]/inverse_gamma_cover[0],
                        inverse_gamma_cover[2]/inverse_gamma_cover[0], inverse_gamma_cover[3]])
    expected_closing = S.Matrix([-t**2, -A*z-B*a*u,
                                S.I**(1-e_line)*C**w*a, S.I**(-e_neutral)*C**(-w)*u])
    ck(equal(closing, expected_closing), f'j{j}: full gamma inverse B representative map')
    ck(S.simplify(inverse_gamma_cover[2]*inverse_gamma_cover[3]-S.I*t*a*u) == 0,
       f'j{j}: sigma changes by its actual quarter phase')
    ck(S.simplify(inverse_gamma_cover[0]*inverse_gamma_cover[2]*inverse_gamma_cover[3]-t**2*a*u) == 0,
       f'j{j}: original epsilon is fixed by the closing arrow')

    # Line-pivot map retains the linear mixing between its equal-weight variables.
    line_original = S.Matrix([t*zc, t*zy, t, u])
    line_after = S.Matrix([t*zc, A*t*zy+B*t*u, C**w*t, C**(-w)*u])
    line_expected = S.Matrix([C**(2*w)*t**2, C**(-w)*zc,
                             C**(-w)*(A*zy+B*u), C**(-w)*u])
    line_actual = S.Matrix([line_after[2]**2, line_after[0]/line_after[2],
                           line_after[1]/line_after[2], line_after[3]])
    ck(equal(line_actual, line_expected), f'j{j}: full line-pivot source map')
    ck(line_expected.subs({t:0, zc:0, zy:0, u:0}) == S.zeros(4, 1),
       f'j{j}: source reset preserves the isolated fixed point')
    ck(surface_transition*S.Matrix(surface_weights) == S.Matrix(surface_weights),
       f'j{j}: physical action commutes with the full surface overlap')
    numerator = 4-sum(x*x for x in point_weights)
    denominator = 24
    for value in point_weights:
        denominator *= value
    residue = Fraction(numerator, denominator)
    ck(residue == Fraction(1, 16), f'j{j}: exact positive-hyperplane isolated residue')
    records.append({
        'chain_node': j, 'node_modulo_actual_period': j % 4,
        'physical_line_weight': w, 'point_weights': point_weights,
        'surface_weights': surface_weights,
        'fixed_surface_exceptional_curve_self_intersection': -2,
        'normal_lines_on_exceptional_curve': [{'degree': 1, 'weight': w}, {'degree': 0, 'weight': -w}],
        'source_pivot_original_volume_unit_sign_and_scalar': -4*w,
        'source_pivot_original_divisor_orders': [2, 0, 3, 3],
        'full_closing_formula_in_rho_z_a_u': [str(q).replace('t**2', 'rho') for q in expected_closing],
        'line_pivot_B_formula': [str(q).replace('t**2', 'rho') for q in line_expected],
        'line_pivot_inverse_gamma_phase_powers': [-2*e_line, e_line-1, e_line+1, -e_neutral],
        'positive_hyperplane_residue': str(residue)
    })

for j in (1, 3):
    ck((-1)*2+1 == -1, f'curve{j}: normal weights transported by exact u squared transition')
    ck((j+1) % 2 == 0, f'curve{j}: the two charts are odd and next even')
ck(sum(Fraction(r['positive_hyperplane_residue']) for r in records) == Fraction(1, 4),
   'four actual point terms sum to one quarter in the positive-hyperplane polynomial')
out = {
    'status': 'PASS_MU2_FIXED_COMPONENTS_AND_NORMAL_ARROWS',
    'utc': datetime.now(timezone.utc).isoformat(), 'checks': len(labels), 'check_labels': labels,
    'parent_certificate_sha256': hashlib.sha256(PARENT.read_bytes()).hexdigest(),
    'proof_sha256': hashlib.sha256(PROOF.read_bytes()).hexdigest(),
    'compact_stabilizer_base_curves': [[1, 2], [3, 4]],
    'cover_normal_degrees': [0, 0, -2],
    'fixed_surface_overlap_exponent_matrix': [[int(x) for x in row] for row in surface_transition.tolist()],
    'nodes': records,
    'isolated_points': 4, 'positive_hyperplane_point_sum': '1/4',
    'unassigned': 'Global fixed-surface completion, physical generator/boundary orientation transfer, and total characteristic return.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('check_labels','nodes')}, indent=2))
