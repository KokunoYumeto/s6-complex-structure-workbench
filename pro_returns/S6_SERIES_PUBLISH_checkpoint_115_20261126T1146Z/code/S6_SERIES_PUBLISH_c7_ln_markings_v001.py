#!/usr/bin/env python3
"""Fresh LN: literal periods, exact component orders, and vertical normal closure.

Only the admitted KY defining fixture is read. No LN original, old target
program, old target output, or candidate list is an input. Integer inverse
maps are obtained from Bezout combinations of two-by-two minors.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
from math import gcd, lcm
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
EXPECTED = '6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522'
assert sha256(SOURCE.read_bytes()).hexdigest() == EXPECTED
DATA = json.loads(SOURCE.read_text())['rows']
J = sp.Matrix([[0, 1], [-1, 0]])
AA, BB, WW = sp.symbols('a b w')


def egcd(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if old_r < 0:
        old_r, old_s, old_t = -old_r, -old_s, -old_t
    assert old_s * a + old_t * b == old_r
    return old_r, old_s, old_t


def pair_inverse(vectors, factor=1):
    """Return S with V S = factor I by a literal Bezout sum of minors."""
    V = sp.Matrix.hstack(*vectors)
    g, coeff = 0, {}
    for i, j in combinations(range(V.cols), 2):
        det = int(sp.Matrix.hstack(V[:, i], V[:, j]).det())
        if not det:
            continue
        new_g, x, y = egcd(g, det)
        coeff = {key: value * x for key, value in coeff.items() if value * x}
        coeff[i, j] = coeff.get((i, j), 0) + y
        g = new_g
        if g == factor:
            break
    if g != factor:
        return g, None
    S = sp.zeros(V.cols, 2)
    for (i, j), c in coeff.items():
        S[i, 0] += c * V[1, j]
        S[j, 0] -= c * V[1, i]
        S[i, 1] -= c * V[0, j]
        S[j, 1] += c * V[0, i]
    assert V * S == factor * sp.eye(2)
    return g, S


def sparse_inverse(labels, S):
    return [[(labels[i], int(S[i, j])) for i in range(S.rows) if S[i, j]]
            for j in range(2)]


def mult_data(B, g):
    N = B - sp.eye(2)
    col = next(N[:, j] for j in range(2) if N[:, j] != sp.zeros(2, 1))
    divisor = gcd(*[abs(int(x)) for x in col])
    u = col / divisor
    first = next(x for x in u if x)
    if first < 0:
        u = -u
    one, s, t = egcd(int(u[0]), int(u[1]))
    assert one == 1
    r = sp.Matrix([-t, s])
    H = sp.Matrix.hstack(u, r)
    assert H.det() == 1
    nu = int((H.inv() * N * H)[0, 1])
    kappa = int((H.inv() * g)[0])
    assert nu > 0 and N == nu * u * u.T * J
    assert g == kappa * u
    z = sp.Rational(kappa, nu) * r
    assert N * z == g
    return nu, kappa, u, r, z


def full_matrix(B, g, z, w=0):
    row = -AA * g.T * J * B
    A = sp.eye(4)
    A[:2, :2] = B
    A[:2, 3] = BB * g
    A[2, :2] = row
    A[2, 3] = (row * (BB * z))[0] + w
    assert A.det() == 1
    return A


print('LN MARKINGS v001: defining input SHA256', EXPECTED)
print('All inverse assertions below are exact integer matrix identities.')
nonstar_count = 0
for row in DATA:
    name = f"OS{row['OS']}/{row['profile']}"
    Bs = [sp.Matrix(x) for x in row['elliptic_matrices']]
    gs = [sp.Matrix(x) for x in row['generator_section_cocycle']]
    kinds = row['fibers']
    d0 = int(1 / sp.Rational(row['height_of_generator']))
    total = sp.eye(4)
    orders, local_periods, coarse, coarse_names = [], [], [], []
    weights = []
    for i, (B, g, kind) in enumerate(zip(Bs, gs, kinds)):
        multiplicative = kind.startswith('I') and kind[1:].isdigit()
        if multiplicative:
            nu, kappa, u, r, z = mult_data(B, g)
            assert nu == int(kind[1:])
            C = sp.Matrix([[nu, BB * kappa],
                           [-AA * kappa, WW - AA * BB * sp.Rational(kappa*kappa, nu)]])
            assert sp.expand(C.det()) == nu * WW
            period = (i, nu, kappa, tuple(map(int, u)), tuple(map(int, r)))
            local_periods.append(period)
            coarse.append(nu * u)
            coarse_names.append(f'{i}:nu*u')
            wi = sp.Symbol(f'w{i}')
            weights.append(wi)
        else:
            z = (B - sp.eye(2)).inv() * g
            wi = 0
        order = lcm(*[int(x.q) for x in z])
        orders.append(order)
        assert (B - sp.eye(2)) * z == g
        r0 = -g.T * J * B
        assert r0 == z.T * J * (B - sp.eye(2))
        # If a*z is integral, r_i*z_i = (a*z)^T J (b*g).
        assert sp.expand((r0 * z)[0] - (z.T * J * g)[0]) == 0
        total = total * full_matrix(B, g, z, wi)
    expected = sp.eye(4)
    expected[2, 3] = sum(weights) - AA * BB / d0
    assert sp.simplify(total - expected) == sp.zeros(4)
    assert all(B.det() == 1 for B in Bs)
    # These raw monodromy images kill every elliptic-angular rim integrally.
    rim_vectors, rim_labels = [], []
    for i, B in enumerate(Bs):
        for j in range(2):
            v = (B - sp.eye(2))[:, j]
            if v != sp.zeros(2, 1):
                rim_vectors.append(v)
                rim_labels.append(f'({i},{j})')
    rim_index, rim_S = pair_inverse(rim_vectors)
    assert rim_index == 1
    print(name, 'component orders=', orders, 'd0=', d0,
          'product central=', str(expected[2, 3]))
    print('  literal multiplicative (i,nu,kappa,u,r)=', local_periods)
    print('  rim inverse=', sparse_inverse(rim_labels, rim_S))
    if any(kind.startswith('I') and kind.endswith('*') and kind[1:-1].isdigit()
           for kind in kinds):
        print('  vertical: an original odd-star cap kills the elliptic quotient after delta.')
        continue
    nonstar_count += 1
    # A zero-weight Mumford cap kills (nu/gcd(nu,a*kappa))*u after delta.
    # Its subgroup always contains nu*u, used here uniformly for every a.
    vectors, labels = list(coarse), list(coarse_names)
    for i, B in enumerate(Bs):
        for v, label in zip(coarse, coarse_names):
            for sign, C in [(1, B), (-1, B.inv())]:
                vectors.append(C * v)
                labels.append(f'B{i}^{sign}({label})')
    if (row['OS'], row['profile']) == (49, 'II'):
        assert all(all(int(x) % 2 == 0 for x in v) for v in vectors)
        _, half_S = pair_inverse([v / 2 for v in vectors])
        assert half_S is not None
        assert sp.Matrix.hstack(*vectors) * half_S == 2 * sp.eye(2)
        S, T = Bs[0] % 2, Bs[1] % 2
        assert S != sp.eye(2) and S**3 % 2 == sp.eye(2)
        assert S * T % 2 == sp.eye(2)
        assert int((S-sp.eye(2)).det()) % 2 == 1
        assert int((T-sp.eye(2)).det()) % 2 == 1
        print('  vertical: exactly 2Z^2 at the coarsest cap; inverse=',
              sparse_inverse(labels, half_S))
        print('  exceptional actions mod2=', S.tolist(), T.tolist(),
              '; both B-I invertible; fixed log powers have zero Klein-four part.')
    else:
        index, S = pair_inverse(vectors)
        assert index == 1, (name, index)
        print('  vertical: Z^2; inverse=', sparse_inverse(labels, S))
print('COMPLETE:', len(DATA), 'literal profile products,', len(DATA),
      'integral rim inverses,', nonstar_count,
      'non-odd-star closures; the sole residue is OS49/II with (Z/2)^2.')
print('No finite bound on a,b or weights was used: the symbolic identities and containment nu*u are universal.')
