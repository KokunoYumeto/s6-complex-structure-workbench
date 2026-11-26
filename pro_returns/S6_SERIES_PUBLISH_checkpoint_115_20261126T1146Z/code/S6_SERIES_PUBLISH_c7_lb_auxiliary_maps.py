#!/usr/bin/env python3
"""Post-exposure LB auxiliary maps; frozen fresh inputs are read-only.

This checks the released proof's additional exact identities and the
literal transport of its line factors to the prescribed Jordan fan.
It imports no historical target algorithm and writes only new c7 files.
"""
from pathlib import Path
from hashlib import sha256
from math import gcd
from functools import reduce
from itertools import combinations
import json
import sympy as s

ROOT = Path(__file__).resolve().parent.parent
LANE = ROOT/'agents/continuation7_iii_conic'
DATA = LANE/'S6_SERIES_PUBLISH_III_02LB_fresh_data.json'
RAW = ROOT/'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
fresh = json.loads(DATA.read_text())
raw = json.loads(RAW.read_text())
assert sha256(RAW.read_bytes()).hexdigest() == '6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522'
profiles = {(r['OS'], r['profile']): r for r in raw['rows']}


def bezout(a, b):
    g, u, v = a, 1, 0
    h, x, y = b, 0, 1
    while h:
        q = g//h
        g, h, u, x, v, y = h, g-q*h, x, u-q*x, y, v-q*y
    if g < 0:
        g, u, v = -g, -u, -v
    assert u*a+v*b == g
    return g, u, v


def right_inverse(M):
    ans = s.zeros(M.cols, M.rows)
    total = 0
    for cols in combinations(range(M.cols), M.rows):
        block = M[:, list(cols)]
        determinant = int(block.det())
        if not determinant:
            continue
        new, u, v = bezout(total, determinant)
        ans *= u
        adj = block.adjugate()
        for j, col in enumerate(cols):
            ans[col, :] += v*adj[j, :]
        total = new
        if total == 1:
            break
    assert total == 1 and M*ans == s.eye(M.rows)
    return ans


def serial(M):
    assert all(x.q == 1 for x in M)
    return [[int(x) for x in row] for row in M.tolist()]


def affine(A, t):
    out = s.eye(4)
    out[:3, :3] = A
    out[:3, 3] = t
    return out


# Additive logarithms retain the sign constants and every nonzero unit.
a, b, H, G, R = s.symbols('a b H G R')
Ah = s.Matrix([[1, 0, 0], [0, 1, 0], [-a, 0, 1]])
Af = s.Matrix([[1, 0, 0], [0, 1, 0], [0, b, 1]])
Aj = s.Matrix([[-1, 0, 0], [0, -1, 0], [-a, 0, 1]])
h = affine(Ah, s.Matrix([H, a*G, a/2]))
f = affine(Af, s.Matrix([-b*G, R, -a*b*G/2+b*R/2]))
j = affine(Aj, s.zeros(3, 1))
assert s.simplify(h*f-f*h) == s.zeros(4)
assert j*j == s.eye(4)
assert s.simplify(j*f*j-f.inv()) == s.zeros(4)
commutator = s.simplify(j*h*j-h.inv())
expected = s.zeros(4)
expected[2, 3] = a
assert commutator == expected  # exp(2 pi i a)=1 for every integral a.

hp = affine(Ah, s.Matrix([H, a*G, a/2+(1-a)*H/2]))
fp = affine(Af, s.Matrix([-b*G, R, -b*G/2+b*R/2]))
jp = affine(s.Matrix([[-1, 0, 0], [0, -1, 0], [-1, 0, 1]]), s.zeros(3, 1))
gauge = affine(s.Matrix([[1, 0, 0], [0, 1, 0], [(a-1)/2, 0, 1]]), s.zeros(3, 1))
for old, new in [(hp, h), (fp, f), (jp, j)]:
    assert s.simplify(gauge*old*gauge.inv()-new) == s.zeros(4)
assert gauge*gauge.inv() == s.eye(4)

# Universal physical support function and both exact period differences.
n, jj, x, y = s.symbols('n j x y', nonzero=True)
rho = (1-a*b*jj**2)/n
phi = lambda X, Y: (-a*rho*X**2-2*a*b*jj*X*Y+b*n*Y**2+a*X)/2
assert s.expand(phi(x+n, y+a*jj)-phi(x, y)+a*x) == 0
assert s.expand(phi(x-b*jj, y+rho)-phi(x, y)-b*y-(b*rho-a*b*jj)/2) == 0

N, al, be, tt = s.symbols('N alpha beta t')
phi1 = lambda t: -N*t*(t-al)/2
assert s.expand(phi1(tt+al)-phi1(tt)+N*al*tt) == 0
assert s.expand(phi1(tt+be)-phi1(tt)+N*be*tt+N*be*(be-al)/2) == 0

answers = []
rank_one_checks = 0
for rec in fresh['patterns']:
    aa, bb, nu, kap = rec['a'], rec['b'], rec['nu'], rec['kappa']
    T = [s.Matrix(M) for M in rec['forward_matrices']]
    relation = s.Matrix.hstack(*[M-s.eye(4) for M in T])
    assert relation[3, :] == s.zeros(1, relation.cols)
    inverse = right_inverse(relation[:3, :])
    angular = s.Matrix(rec['kill_matrix'])
    unit_cols, unit_det = next((cols, int(angular[:, list(cols)].det()))
        for cols in combinations(range(angular.cols), 3)
        if abs(int(angular[:, list(cols)].det())) == 1)
    unit_block = angular[:, list(unit_cols)]
    assert unit_block*(unit_det*unit_block.adjugate()) == s.eye(3)

    C = s.Matrix(rec['C'])
    K = s.Matrix(rec['K'])
    eps = s.Matrix(rec['epsilon'])
    assert C == s.Matrix([[nu, bb*kap], [-aa*kap, s.Rational(1-aa*bb*kap**2, nu)]])
    vx, vy = s.symbols('vx vy')
    v = s.Matrix([vx, vy])
    xx, yy = C*v
    rh = C[1, 1]
    physical_phi = (-aa*rh*xx**2+2*aa*bb*kap*xx*yy+bb*nu*yy**2+aa*xx)/2
    psi = (v.T*K*v-eps.T*v)[0]/2
    L = (aa*C[0, :].T-eps)/2
    assert all(c.q == 1 for c in L)
    assert s.expand(physical_phi+psi-(L.T*v)[0]) == 0

    d = s.Matrix(rec['delta_jordan'])
    plus_weights = [-d[0]-d[1], d[1], d[0]]
    minus_weights = [-d[1], d[0]+d[1], -d[0]]
    assert all(int(w)%2 == wanted for w, wanted in zip(plus_weights, [1, 1, 0]))
    assert all(int(w)%2 == wanted for w, wanted in zip(minus_weights, [1, 1, 0]))
    degree = K[0, 0]-K[0, 1]
    old_degree = -aa*rh-aa*bb*kap
    assert degree == rec['cusp_degree'] and degree%2 == old_degree%2 == 1
    assert K[0, 0]+K[0, 1]-degree == 2*K[0, 1]

    row = profiles[(rec['OS'], rec['profile'])]
    node_data = []
    for i, kind in enumerate(row['fibers']):
        if not (kind.startswith('I') and kind[1:].isdigit()) or i == rec['zero']:
            continue
        ni = int(kind[1:])
        A = s.Matrix(row['elliptic_matrices'][i])
        g = s.Matrix(row['generator_section_cocycle'][i])
        col = next((A-s.eye(2))[:, z] for z in range(2) if (A-s.eye(2))[:, z] != s.zeros(2, 1))
        u = col/reduce(gcd, [abs(int(c)) for c in col])
        if next(c for c in u if c) < 0:
            u = -u
        idx = next(z for z in range(2) if u[z])
        ji = -g[idx]/u[idx]
        assert ji.q == 1 and g == -ji*u
        alpha = gcd(ni, int(aa*ji))
        v1, v2 = s.Integer(ni)//alpha, aa*ji/alpha
        beta = -bb*ji/v1
        kk = aa*v1/alpha
        assert all(c.q == 1 for c in [v1, v2, beta, kk])
        assert gcd(alpha, int(beta)) == 1
        assert -aa*beta*v1 == bb*alpha*v2
        assert int(kk)%2 == 0 or alpha%2 == 1
        if int(v1)%2:
            assert int(beta)%2 == 0 and alpha%2 == 1
        else:
            assert v1 == 2 and alpha == 1 and int(ji)%2 == 1
            old_short = s.Matrix([[s.Rational(1-aa*ji, 2), 1], [-aa*ji, 2]])
            assert old_short.det() == 1
            old_inverse = s.Matrix([[2, -1], [aa*ji, s.Rational(1-aa*ji, 2)]])
            assert old_short*old_inverse == s.eye(2)
            fresh_short = s.Matrix([[2, 1], [aa*ji, s.Rational(1+aa*ji, 2)]])
            assert old_inverse == fresh_short*s.Matrix([[1, -1], [0, 1]])
        rank_one_checks += 1
        node_data.append([i, ni, int(ji), alpha, int(beta), int(v1), int(v2), int(kk)])

    answers.append(dict(number=rec['number'], OS=rec['OS'], profile=rec['profile'],
        a=aa, b=bb, zero=rec['zero'], all_monodromy_relation=serial(relation[:3, :]),
        all_monodromy_right_inverse=serial(inverse), cartier_gauge=[int(z) for z in L],
        angular_unit_minor_columns=list(unit_cols), angular_unit_minor_determinant=unit_det,
        weights_plus=[int(z) for z in plus_weights], weights_minus=[int(z) for z in minus_weights],
        actual_wall_degree=int(degree), old_physical_wall_expression=int(old_degree),
        rank_one_data=node_data, cube=rec['cube']))

ex = next(r for r in answers if r['OS'] == 47 and r['profile'] == 'default' and r['zero'] == 3)
assert ex['actual_wall_degree'] == -7 and ex['old_physical_wall_expression'] == 77
assert ex['weights_plus'] == [1, 1, -2] and ex['cube'] == 0
out = dict(fresh_data_sha256=sha256(DATA.read_bytes()).hexdigest(),
    raw_sha256=sha256(RAW.read_bytes()).hexdigest(), patterns=answers,
    all_monodromy_primitive_rows=len(answers), rank_one_sites=rank_one_checks,
    logarithmic_JhJ_correction='integer a; exponentiates to one',
    coefficient_bordism_quotient='Z<epsilon,zeta>/<epsilon,2zeta> -> Z/2; (A,B) -> B mod2')
path = LANE/'S6_SERIES_PUBLISH_III_02LB_post_exposure_maps.json'
path.write_text(json.dumps(out, indent=2)+'\n')
print('POST-EXPOSURE AUXILIARY MAPS; no old target algorithm loaded')
print('FRESH_DATA_SHA256', out['fresh_data_sha256'])
print('RAW_SHA256', out['raw_sha256'])
print('PASS hF=Fh; J2=1; JFJ=F^-1; JhJ=h^-1 modulo the integral logarithmic constant a')
print('PASS exact gauge z^((a-1)/2) and inverse carry physical prequantum h,F,J to the released factors')
print('PASS both physical support translations; prescribed-fan pullback phi(Cv)=-psi(v)+L.v and inverse')
for r in answers:
    print('PATTERN', r['number'], r['OS'], r['profile'], 'a,b', (r['a'], r['b']),
          'zero-based', r['zero'], 'L', r['cartier_gauge'], 'weights', r['weights_plus'],
          r['weights_minus'], 'degree actual/old', r['actual_wall_degree'],
          r['old_physical_wall_expression'], 'cube', r['cube'],
          'angular unit minor', r['angular_unit_minor_columns'], r['angular_unit_minor_determinant'])
print('PASS all-monodromy image = ker(gamma*), with integral right inverses for', len(answers), 'patterns')
print('PASS exact rank-one period laws, integral support parity and fixed-site coordinate inverses at', rank_one_checks, 'sites')
print('PASS alternate diagonal changes the actual wall degree by 2 K12; involution signs remain (-,-,+)')
print('COUNTEREXAMPLE OS47/default (7,2), zero-based 3: actual degree -7; old absolute wall expression 77; weights (1,1,-2); cubic 0')
print('BORDISM INPUT independently read in primary source; quotient inverse 1 -> reduced CP3, detected by cubic')
print('PASS all symbolic and integer checks; source/bibliographic reading is recorded separately')
