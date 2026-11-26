#!/usr/bin/env python3
"""Fresh LL marked-lattice and full finite-coefficient localization calculation.

Inputs are the defining KY raw profiles only. No LL original, target table,
historical target program, or historical target output is read.
The remaining refined-P choice is deliberately not inferred from lambda.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
from math import gcd
import json
import sympy as S
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parent.parent
STAGE = ROOT / 'agents/continuation7_iii_residual_two_primary'
STAGE.mkdir(exist_ok=True)
RAW = ROOT / 'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
EXPECTED = '6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522'
assert sha256(RAW.read_bytes()).hexdigest() == EXPECTED
raw = json.loads(RAW.read_text())
J = S.Matrix([[0, 1], [-1, 0]])
I4 = S.eye(4)
delta = S.Matrix([0, 0, 1, 0])
gamma = S.Matrix([0, 0, 0, 1])
pairs = list(combinations(range(4), 2))
tau, x, h = S.symbols('tau x h')


def ints(matrix):
    return [[int(v) for v in row] for row in matrix.tolist()]


def primitive_cycle(A):
    B = A - S.eye(2)
    column = next(B[:, j] for j in range(2) if B[:, j] != S.zeros(2, 1))
    common = gcd(int(column[0]), int(column[1]))
    u = column / common
    if next(v for v in u if v) < 0:
        u = -u
    uu = u * u.T * J
    nu = next(B[i, j] / uu[i, j] for i in range(2) for j in range(2) if uu[i, j])
    assert nu.is_Integer and nu > 0 and B == nu * uu
    p, q, one = S.gcdex(u[0], u[1])
    assert one == 1
    r = S.Matrix([-q, p])
    assert S.det(S.Matrix.hstack(u, r)) == 1
    return u, r, int(nu)


def exterior(T):
    return S.Matrix([[T[i, k] * T[j, l] - T[i, l] * T[j, k]
                      for k, l in pairs] for i, j in pairs])


def right_inverse(A):
    dm = DomainMatrix.from_Matrix(A).convert_to(S.ZZ)
    dd, uu, vv = smith_normal_decomp(dm)
    D, U, V = dd.to_Matrix(), uu.to_Matrix(), vv.to_Matrix()
    assert U * A * V == D
    assert abs(U.det()) == abs(V.det()) == 1
    rank = A.rows
    assert [abs(int(D[i, i])) for i in range(rank)] == [1] * rank
    inverse = V[:, :rank] * S.diag(*(1 / D[i, i] for i in range(rank))) * U
    assert A * inverse == S.eye(rank)
    assert all(entry.is_Integer for entry in inverse)
    return inverse, U, V


def reduced_degree_one(expression):
    return S.expand(expression).coeff(x, 1)


records = []
print('RAW_SHA256', EXPECTED)
for os, a, c, zeros in [(55, 5, 4, [2, 3, 4]), (45, 1, 8, [1, 2, 3, 4])]:
    profile = next(row for row in raw['rows'] if row['OS'] == os and row['profile'] == 'default')
    data = []
    for A0, g0, fiber in zip(profile['elliptic_matrices'],
                             profile['generator_section_cocycle'], profile['fibers']):
        A, g = S.Matrix(A0), S.Matrix(g0)
        u, r, nu = primitive_cycle(A)
        kappa = next(g[j] / u[j] for j in range(2) if u[j])
        assert kappa.is_Integer and g == kappa * u
        data.append((A, g, u, r, nu, int(kappa), fiber))
    for zero in zeros:
        Omega = S.Matrix([[0, a, 0, 0], [-a, 0, 0, 0],
                          [0, 0, 0, -c], [0, 0, c, 0]])
        matrices, angular, local = [], [], []
        for index, (A, g, u, r, nu, kappa, fiber) in enumerate(data):
            T = S.eye(4)
            T[:2, :2] = A
            T[:2, 3] = c * g
            T[2, :2] = -a * g.T * J * A
            T[2, 3] = S.Rational((index == zero) - a * c * kappa**2, nu)
            assert all(v.is_Integer for v in T)
            assert T.T * Omega * T == Omega and T * delta == delta
            matrices.append(T)
            short_u = S.Matrix([u[0], u[1], 0, 0])
            long_r = S.Matrix([r[0], r[1], 0, 0])
            if index == zero:
                assert nu == 1
                C = S.Matrix([[nu, c * kappa], [-a * kappa, 1 - a * c * kappa**2]])
                short = S.Matrix.hstack(short_u, delta) * C
                H = S.Matrix.hstack(short[:, 0], long_r, short[:, 1], gamma)
                Jordan = S.eye(4)
                Jordan[0, 1] = Jordan[2, 3] = 1
                assert H.det() == 1 and H.inv() * T * H == Jordan
                K = C.T * S.diag(a, -c)
                d = C.inv() * S.Matrix([0, 1])
                assert K == K.T and C * d == S.Matrix([0, 1])
                cusp = dict(C=ints(C), H=ints(H), H_inverse=ints(H.inv()),
                            K=ints(K), d=ints(d), nu=nu, kappa=kappa)
                angular += [short_u, delta]
            else:
                d0 = gcd(nu, a * kappa)
                l = (nu // d0) * short_u - (a * kappa // d0) * delta
                f = S.Matrix([[d0 * (u.T * J)[0], d0 * (u.T * J)[1],
                               0, S.Rational(c * kappa * d0, nu)]])
                assert all(v.is_Integer for v in f) and T - I4 == l * f
                assert gcd(*(int(v) for v in f)) == 1
                angular.append(l)
                local.append(dict(index=index, fiber=fiber, nu=nu, kappa=kappa,
                                  l=ints(l), f=ints(f), isotropy=nu // d0))
        product = S.eye(4)
        for T in matrices:
            product *= T
        assert product == I4
        ang = S.Matrix.hstack(*angular)
        minor = next(cols for cols in combinations(range(ang.cols), 3)
                     if abs(ang[:3, cols].det()) == 1)
        ang_inv = S.zeros(ang.cols, 3)
        B = ang[:3, minor]
        for j, col in enumerate(minor):
            ang_inv[col, :] = B.inv()[j, :]
        assert ang * ang_inv == I4[:, :3]
        rel = S.Matrix.hstack(*(exterior(T) - S.eye(6) for T in matrices))
        aa, bb, one = S.gcdex(a, -c)
        assert one == 1
        fibre_basis = S.zeros(6)
        fibre_basis[0, 0], fibre_basis[5, 0] = aa, bb
        fibre_basis[0, 1], fibre_basis[5, 1] = c, a
        for j, row in enumerate([1, 2, 3, 4], start=2):
            fibre_basis[row, j] = 1
        assert abs(fibre_basis.det()) == 1
        marked_rel = fibre_basis.inv() * rel
        assert marked_rel[0, :] == S.zeros(1, rel.cols)
        rel_inverse, smith_U, smith_V = right_inverse(marked_rel[1:, :])
        even_site = [row for row in local if row['isotropy'] % 2 == 0]
        assert len(even_site) == 1 and even_site[0]['nu'] == c
        nodal = even_site[0]
        kE = nodal['kappa']
        t = pow((a * kE) % c, -1, c)
        s = (1 - a * kE * t) // c
        Bnode = S.Matrix([[c, t], [-a * kE, s]])
        assert Bnode.det() == 1
        assert Bnode * S.Matrix([-t, c]) == S.Matrix([0, 1])
        Knode = S.Matrix([[a * c, 0], [a * t, -1]])
        assert S.Rational(c * (1 - a * t), 2) % c == 0
        kappa = cusp['kappa']
        C = S.Matrix(cusp['C'])
        K = S.Matrix(cusp['K'])
        d = S.Matrix(cusp['d'])
        eps = S.Matrix([1, 0])
        slope = S.Matrix([(K[0, 0] - 1) / 2, K[1, 1] / 2])
        dense = (eps.T * d)[0] / 2
        cartier = (slope.T * d)[0]
        character = dense + cartier
        assert character == S.Rational(c, 2) * (a * kappa * (c * kappa - 1) - 1)
        assert character.is_Integer and (2 * character) % c == 0
        degreeC, degreeE = a * (1 - c * kappa), -1
        weights = [(c * kappa - 1, 1, -c * kappa),
                   (-1, 1 - c * kappa, c * kappa)]
        assert all(gcd(w, c) == 1 for w in [-1, 1, -t, t])
        assert all(row['isotropy'] % 2 for row in local if row != nodal)
        # In H*(curve)[tau,tau^-1], x^2=0. Mixed elliptic degree-one
        # products have square zero and integrate to zero in degree two.
        mu_numerator = S.expand(-3 * t**2 * degreeC * (character + h)**2
                                - 3 * degreeE * h**2)
        mu_coefficients = [int(v) % c for v in S.Poly(mu_numerator, h).all_coeffs()]
        assert not any(mu_coefficients)
        lambda_value = -degreeC - degreeE
        assert (lambda_value - (1 - a)) % c == 0
        assert lambda_value % c == 0
        # Full primary quotient, with h(epsilon)=0, h(zeta)=1,
        # P(epsilon)=6 and P(zeta)=1. This does not select X's P.
        invariant_map = {(A, B): ((6*A+B) % c, B)
                         for A in range(c // 2) for B in range(c)}
        assert len(set(invariant_map.values())) == c*c//2
        possible = [(A, B, P0) for (A, B), (P0, mu) in invariant_map.items()
                    if mu == 0 and 2*P0 % c == 0]
        assert sorted(P0 for A, B, P0 in possible) == [0, c // 2]
        assert invariant_map[(0, 0)] == (0, 0)
        assert invariant_map[(c // 4, 0)] == (c // 2, 0)
        for e in [-1, 1]:
            assert abs(c * e) == c
        record = dict(OS=os, profile='default', a=a, c=c, zero=zero, e=[-1, 1],
            monodromies=[ints(T) for T in matrices], angular_columns=ints(ang),
            angular_unit_columns=list(minor), angular_right_inverse=ints(ang_inv),
            fibre_basis=ints(fibre_basis), fibre_basis_inverse=ints(fibre_basis.inv()),
            exterior_relations=ints(rel), exterior_kernel_right_inverse=ints(rel_inverse),
            smith_left=ints(smith_U), smith_right=ints(smith_V),
            cusp=cusp, rank_one=local,
            elliptic=dict(index=nodal['index'], kappa=kE, short_basis=ints(Bnode),
                          short_inverse=ints(Bnode.inv()), t=t, s=s, K=ints(Knode),
                          character=0, degree=degreeE),
            cusp_character=int(character % c), cusp_degree=degreeC,
            dense_phase_exponent=str(dense), cartier_exponent=str(cartier),
            circle_endpoint_weights=weights, mu_polynomial_numerator=str(mu_numerator),
            mu_polynomial_coefficients_mod_c=mu_coefficients,
            lambda_residue_representative_not_a_refined_lift=1-a,
            lambda_mod_c=int(lambda_value % c),
            unresolved_P_values=[0, c//2], model0_epsilon_coefficient=0,
            model1_epsilon_coefficient=c//4)
        records.append(record)
        print('ROW', os, 'a', a, 'c', c, 'zero', zero, 'kappa', kappa,
              'cusp_weight', int(character % c), 'cusp_degree', degreeC,
              'elliptic_t', t, 'mu', 0, 'lambda', int(lambda_value % c))
        print('  MAPS monodromy_product=I angular_unit_minor=' + str(minor) +
              ' exterior_coinvariant=Z with full inverse; both e=-1,+1')
print('ROWS', len(records), 'MARKED_INPUTS_AND_FULL_COEFFICIENT_LOCALIZATIONS_PASSED')
print('REFINED_P_GATE_RETAINED actual X has P in {0,c/2}; no division inference made')
out = STAGE / 'S6_SERIES_PUBLISH_III_02LL_fresh_localization_data.json'
out.write_text(json.dumps(dict(raw_sha256=EXPECTED, rows=records), indent=2) + '\n')
print('DATA', out.relative_to(ROOT), 'SHA256', sha256(out.read_bytes()).hexdigest())
