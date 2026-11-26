#!/usr/bin/env python3
"""Post-exposure LF comparison by exact changes of marked lattices.

This newly written program compares the released historical data with the
frozen fresh data. It does not import or execute either historical algorithm.
It records every period-basis inverse and the actual transported fan wall.
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as S

LANE = Path('agents/continuation7_iii_three_primary_receiving')
OLD = Path('/tmp/S6_SERIES_PUBLISH_c7_LF_historical')
paths = {
    'tate': OLD / 'S6_SERIES_PUBLISH_manifolds_c3_tate_markings.json',
    'ah': OLD / 'S6_SERIES_PUBLISH_fourfolds_D2_c3_AH.json',
    'fresh': Path('agents/continuation7_iii_three_primary/'
                  'S6_SERIES_PUBLISH_III_02LF_fresh_data_v003.json'),
}
data = {k: json.loads(p.read_text()) for k, p in paths.items()}
fresh = {}
for row in data['fresh']['patterns']:
    key = (row['OS'], row['profile'], row['a'], row['b'], row['zero'])
    fresh.setdefault(key, row)
ah = {tuple(row['key']): row for row in data['ah']['rows']}
x, y, j, t1, t2 = S.symbols('x y j t1 t2', integer=True)
e1, e2, zero = S.Matrix([1, 0]), S.Matrix([0, 1]), S.zeros(2, 1)
vertices = [e1, -e1 + e2, zero, e2]
signs = [1, 1, -1, -1]
records = []

def entries(matrix):
    return [[int(v) for v in row] for row in matrix.tolist()]

def eval_poly(poly, vector):
    return S.expand(poly.subs({x: vector[0], y: vector[1]}, simultaneous=True))

for oldrow in data['tate']:
    key = tuple(oldrow['key'])
    row = fresh[key]
    a, b = row['a'], row['b']
    freshlocals = {q['site']: q for q in row['locals']}
    ahlocals = {q['site']: q for q in ah[key]['local']}
    for oldlocal in oldrow['local']:
        site = oldlocal['site']
        loc = freshlocals[site]
        T = S.Matrix(loc['T'])
        basis = S.eye(4)
        basis[:2, :2] = S.Matrix.hstack(S.Matrix(loc['u']), S.Matrix(loc['v']))
        oldbasis = S.Matrix(oldlocal['basis'])
        change = basis.inv() * oldbasis
        inverse = change.inv()
        eps, shear = int(change[0, 0]), int(change[0, 1])
        expected = S.eye(4)
        expected[:2, :2] = S.Matrix([[eps, shear], [0, eps]])
        assert abs(eps) == 1 and change == expected
        assert change * inverse == inverse * change == S.eye(4)
        assert oldbasis.inv() * T * oldbasis == S.Matrix(oldlocal['adapted_monodromy'])
        n, h, rho = oldlocal['valuations']
        kap = loc['kappa']
        assert n == loc['nu'] and h == -eps * kap
        P = S.Matrix([[n, b * kap], [-a * kap, rho]])
        Pold = S.Matrix(oldlocal['period_matrix'])
        reflection = S.diag(eps, 1)
        assert Pold == reflection * P * reflection
        rec = {'key': key, 'site': site, 'basis_change_new_from_old': entries(change),
               'inverse_old_from_new': entries(inverse), 'epsilon': eps,
               'shear': shear, 'nu': n, 'kappa': kap,
               'old_H': h, 'old_R': rho}
        previous = ahlocals[site]
        if oldlocal['zero']:
            K = S.Matrix(loc['K'])
            assert P == S.Matrix(loc['C'])
            fan = Pold * reflection
            fan_inverse = reflection * Pold.inv()
            assert fan == reflection * P
            assert fan * fan_inverse == fan_inverse * fan == S.eye(2)
            psi = -a * rho * x*x - 2*a*b*h*x*y + b*n*y*y + a*x
            assert S.expand(psi - S.sympify(previous['support'],
                                          locals={'x': x, 'y': y})) == 0
            coords = fan * S.Matrix([t1, t2])
            pullback = eval_poly(psi, coords)
            target = -(S.Matrix([[t1, t2]]) * K * S.Matrix([t1, t2]))[0]
            target += a * eps * (n*t1 + b*kap*t2)
            assert S.expand(pullback - target) == 0
            old_wall = sum(sign * eval_poly(psi, v)
                           for sign, v in zip(signs, vertices))
            transported_wall = sum(sign * eval_poly(psi, fan*v)
                                   for sign, v in zip(signs, vertices))
            correct_degree = -int(transported_wall)
            assert old_wall == previous['doubled_curve_degree']
            assert correct_degree == 2*a*(n-b*kap) == 2*loc['alpha_C']
            k = b*kap
            A = a*(n-k)
            denominator = n*(k-n)
            residue = A**3*k**2*pow(denominator, -1, 9) % 9
            assert residue == 0 and k*k % 9 == 0
            rec.update({'fan_new_Jordan_to_old_physical': entries(fan),
                        'fan_inverse': entries(fan_inverse),
                        'old_untransported_degree': int(old_wall),
                        'transported_vector_wall': int(transported_wall),
                        'prescribed_line_degree': correct_degree,
                        'whole_circle_tangent_weights': [-k, k],
                        'Q3_restriction_coefficient_mod9': int(A**3*k*k % 9),
                        'Q3_localized_contribution_mod9': int(residue)})
            print('CUSP', key, 'site', site, 'epsilon', eps, 'shear', shear,
                  'FAN', entries(fan), 'INV', entries(fan_inverse),
                  'OLD_WALL', int(old_wall), 'DEGREE', correct_degree,
                  'TANGENT', [-k, k], 'Q3_MOD9', residue, flush=True)
        else:
            oldprimitive = S.Matrix(previous['primitive_period'])
            d0 = S.gcd(n, a*kap)
            n0 = n // int(d0)
            primitive = S.Matrix([n0, -a*kap//int(d0)])
            transported = reflection * oldprimitive
            tau = int(transported[0] / primitive[0])
            assert abs(tau) == 1 and transported == tau*primitive
            alpha, beta = previous['period_coefficients']
            assert alpha == eps*tau*d0 and beta == tau*b*kap//n0
            N = S.Rational(a*n, int(d0)**2)
            newpsi = -N*j*j + N*d0*j
            oldpsi = S.sympify(previous['integral_support'], locals={'j': j})
            assert S.expand(oldpsi - newpsi.subs(j, tau*j)
                            - a*tau*n0*(eps-1)*j) == 0
            rec.update({'primitive_sign': tau,
                        'primitive_new_from_old': entries(transported),
                        'primitive_new': entries(primitive),
                        'rank_one_coordinate_forward': tau,
                        'rank_one_coordinate_inverse': tau,
                        'integral_gauge_exponent': int(a*n0*(eps-1)),
                        'scalar_isotropy': n0})
            if n0 % 3 == 0:
                assert n0 == 3
                sigma = pow(a*kap, -1, 3)
                w = previous['normal_weight_mod_p']
                assert w == -eps*sigma % 3
                assert sorted([w, -w % 3]) == sorted([sigma, -sigma % 3])
                rec['old_normal_weight'] = w
                rec['specified_normal_pair_mod3'] = [sigma, -sigma % 3]
        records.append(rec)
        print('BASIS', key, site, entries(change), 'INVERSE', entries(inverse), flush=True)

assert len(records) == data['ah']['adapted_matrix_checks'] == 27
assert len(fresh) == len(data['tate']) == len(data['ah']['rows']) == 7
assert len(data['ah']['patterns']) == 8
assert data['ah']['full_four_row_hnf_checks'] == 14
assert len(data['ah']['finite_normal_checks']) == 3
assert len(data['ah']['original_choice_checks']) == 2
output = {'scope': 'Post-exposure comparison of all historical LF period markings '
                   'and fan supports; no historical algorithm executed.',
          'input_sha256': {k: sha256(p.read_bytes()).hexdigest()
                           for k, p in paths.items()},
          'records': records,
          'counts': {'initial_rows': 7, 'patterns': 8, 'adapted_maps': 27,
                     'archived_hnf_records': 14, 'finite_rows': 3,
                     'original_choices': 2}}
target = LANE / 'S6_SERIES_PUBLISH_III_02LF_auxiliary_maps_v001.json'
with target.open('x') as stream:
    json.dump(output, stream, indent=2)
    stream.write('\n')
print('ALL_27_MAPS_AND_7_PRESCRIBED_WALLS_PASS', flush=True)
print('SAVED', target, sha256(target.read_bytes()).hexdigest(), flush=True)
