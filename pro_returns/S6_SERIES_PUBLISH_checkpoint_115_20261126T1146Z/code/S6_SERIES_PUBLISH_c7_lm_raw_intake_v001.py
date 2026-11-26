#!/usr/bin/env python3
"""LM statement-only intake of defining periods and literal critical degrees.

The LM original and historical target calculations remain closed. The
critical-cycle formulas are derived in the new root note from the admitted
fan and rank-one specialization maps. This intake determines the actual
seven marked rows before the full fresh proof is frozen.
"""
from hashlib import sha256
from pathlib import Path
from math import gcd
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
EXPECTED = '6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522'
assert sha256(RAW.read_bytes()).hexdigest() == EXPECTED
raw = json.loads(RAW.read_text())
J = S.Matrix([[0, 1], [-1, 0]])
rows = [(45, 'II', 1, 8, [2, 3]), (55, 'II', 5, 4, [3]),
        (55, 'default', 1, 20, [2, 3, 4]), (55, 'II', 1, 20, [3])]
print('RAW_SHA256', EXPECTED)
count = 0
for os, name, a, b, zeros in rows:
    profile = next(r for r in raw['rows'] if r['OS'] == os and r['profile'] == name)
    local = []
    for index, (kind, aa, gg) in enumerate(zip(profile['fibers'],
            profile['elliptic_matrices'], profile['generator_section_cocycle'])):
        A, G = S.Matrix(aa), S.Matrix(gg)
        if kind == 'II':
            assert (A-S.eye(2)).det() == 1 and A**6 == S.eye(2)
            z = (A-S.eye(2)).inv()*G
            assert all(x.is_Integer for x in z)
            local.append((kind, A, G, None, None, None, z))
            print('PROFILE', os, name, 'SITE', index, kind, 'A', aa, 'G', gg,
                  'fixed_lift', [-b*int(z[0]), -b*int(z[1]), 0, 1])
        else:
            D = A-S.eye(2)
            column = next(D[:, j] for j in range(2) if D[:, j] != S.zeros(2, 1))
            u = column/gcd(int(column[0]), int(column[1]))
            if next(x for x in u if x) < 0:
                u = -u
            B = u*u.T*J
            nu = next(D[i,j]/B[i,j] for i in range(2) for j in range(2) if B[i,j])
            kappa = next(G[i]/u[i] for i in range(2) if u[i])
            assert nu.is_Integer and kappa.is_Integer and nu > 0
            assert D == nu*B and G == kappa*u
            local.append((kind, A, G, u, int(nu), int(kappa), None))
            print('PROFILE', os, name, 'SITE', index, kind,
                  'u', [int(x) for x in u], 'kappa', int(kappa),
                  'isotropy', int(nu)//gcd(int(nu), a*int(kappa)))
    for zero in zeros:
        monodromies, degrees = [], []
        for index, (kind, A, G, u, nu, kappa, z) in enumerate(local):
            beta = -G.T*J*A
            T = S.eye(4)
            T[:2,:2], T[:2,3], T[2,:2] = A, b*G, a*beta
            if kind == 'II':
                T[2,3] = a*b*(beta*z)[0]
                degrees.append(0)
            else:
                T[2,3] = S.Rational(int(index == zero)-a*b*kappa*kappa, nu)
                if index == zero:
                    assert nu == 1
                    degrees.append(a-a*b*kappa-b+a*b*b*kappa*kappa)
                else:
                    degrees.append(-S.Rational(b*gcd(nu,a*kappa)**2,nu))
            assert all(x.is_Integer for x in T)
            monodromies.append(T)
        product = S.eye(4)
        for T in monodromies:
            product *= T
        assert product == S.eye(4)
        value = sum(degrees)
        assert value.is_Integer if isinstance(value, S.Basic) else isinstance(value, int)
        value = int(value)
        assert value % 2 == 0
        print('ROW', os, name, 'a', a, 'b', b, 'zero', zero,
              'critical_degrees_without_II', [int(x) for x in degrees],
              'Omega_total_without_II', value,
              'half_negative_mod_b', (-value//2) % b,
              'negative_mod_b', (-value) % b)
        if any(t[0] == 'II' for t in local):
            print('  original_II_adds', -2*b,
                  'half_negative_mod_b', (-(value-2*b)//2) % b)
            count += 2
        else:
            count += 1
print('PATTERNS', count)
assert count == 11
print('SCOPE defining periods and critical arithmetic only; full topology and refined framing remain in the fresh proof')
