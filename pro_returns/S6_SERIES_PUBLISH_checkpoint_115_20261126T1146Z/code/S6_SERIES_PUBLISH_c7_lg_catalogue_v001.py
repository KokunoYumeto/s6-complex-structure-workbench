#!/usr/bin/env python3
"""Fresh LG enumeration from raw defining profiles and admitted local criteria.

No historical target program is imported.  Site indices are zero based.
Output is the full input digest, all raw sites, all natural rows, all 495
marked patterns, and every minimal pattern with its marked invariants.
"""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import gcd, lcm, prod
from pathlib import Path
import json
import re

W = Path(__file__).resolve().parents[1]
RAW = W / 'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
TARGET = W / 'agents/continuation7_iii_lg_statement/S6_SERIES_PUBLISH_III_02LG_statement_only.tex'
GOOD = {'II': (6, 1), 'III': (4, 2), 'IV': (3, 3),
        'III*': (4, 2), 'IV*': (3, 3)}
rho_nonzero = {'II': 1, 'III': 1, 'IV': 1, 'III*': 5,
               'IV*': 3, 'I1*': 2, 'I3*': 3}


def stamp():
    return datetime.now(timezone.utc).isoformat()


def multiplicative(f):
    m = re.fullmatch(r'I(\d+)', f)
    return int(m[1]) if m else None


def component_order(c):
    orders = [m // gcd(m, row[0]) for m, row in zip(c['moduli'], c['rows'])]
    return lcm(*orders) if orders else 1


def narrow(site, a):
    return a % site['h'] == 0


def log_vector(B, g):
    a, b = B[0][0] - 1, B[0][1]
    c, d = B[1][0], B[1][1] - 1
    det = a*d-b*c
    assert det
    return (F(d*g[0]-b*g[1], det), F(-c*g[0]+a*g[1], det))


def primitive_data(B, g, n):
    M = [[B[i][j]-(i == j) for j in range(2)] for i in range(2)]
    col = next([M[0][j], M[1][j]] for j in range(2) if any(M[i][j] for i in range(2)))
    div = gcd(*col)
    u = [x//div for x in col]
    if next(x for x in u if x) < 0:
        u = [-x for x in u]
    uj = [-u[1], u[0]]
    assert M == [[n*u[i]*uj[j] for j in range(2)] for i in range(2)]
    j = next(j for j in range(2) if u[j])
    kap = F(g[j], u[j])
    assert kap.denominator == 1 and g == [int(kap)*x for x in u]
    return u, int(kap)


def group_ring(a, b, kap, n):
    c = [0]*n
    for j, e in [(a*kap, 1), (0, -1), ((a-b)*kap, -1), (-b*kap, 1)]:
        c[j % n] += e
    ans = []
    for h in range(n):
        d = [0]*n
        for j, e in [(h, -2), (h-1, 1), (h+1, 1)]:
            d[j % n] += e
        if c == d:
            ans.append(h)
    return ans


def rowkey(r):
    return (r['OS'], r['profile'], r['a'], r['b'], r['zero'])


def textkey(r):
    return '/'.join(map(str, rowkey(r)))


def choices(sites):
    return [tuple(s for s, bit in zip(sites, bits) if bit)
            for bits in product((0, 1), repeat=len(sites))]


def original_minimal(s, a, b):
    return s['f'] == 'II' or (s['f'] in ('III', 'IV') and narrow(s, a) and not narrow(s, b))


def crt(a, m, b, n):
    assert gcd(m, n) == 1
    x = (a*n*pow(n, -1, m)+b*m*pow(m, -1, n)) % (m*n)
    assert x % m == a % m and x % n == b % n
    return x


def residual(r, c):
    os, pr, a, b, z = rowkey(r)
    if c == 4:
        assert (os, a, b) == (55, 5, 4)
        P = 2 if pr == 'default' and z == 3 else 0
        return P, f'Z4,{int(P != 0)}'
    if c == 8:
        assert (os, a, b) == (45, 1, 8)
        P = 4 if (pr == 'default' and z in (2, 3)) or (pr == 'II' and z == 2) else 0
        return P, f'Z8,{int(P != 0)}'
    assert c == 20 and (os, a, b) == (55, 1, 20)
    P = 14 if pr == 'default' and z == 3 else 4
    return P, f'Z4,{int(P == 14)}#Z5,1'


def invariants(r, c):
    a, b, nu, kap = r['a'], r['b'], r['nu'], r['kap']
    t = (1+kap) % 2
    D3 = c*gcd(c, 3)
    if c == 1:
        return 0, 0, 1, 'S6'
    if c == 2:
        return t, t, D3, f'M2,{t}'
    if c == 3:
        return 0, 0, D3, 'M3,0'
    if c in (4, 8, 20):
        P, model = residual(r, c)
        return P, 0, D3, model
    if c in (5, 7):
        P = ((b//c-a*nu)*pow(2, -1, c)) % c
        return P, 0, D3, f'Z{c},{int(P != 0)}'
    if c in (10, 14):
        p = c//2
        Pp = ((b//p-a*nu)*pow(2, -1, p)) % p
        return crt(t, 2, Pp, p), p*t, D3, f'M2,{t}#Z{p},{int(Pp != 0)}'
    if c == 6:
        return 3*t, 9*t, D3, f'M2,{t}#M3,0'
    if c == 15:
        P5 = ((b//5-a*nu)*3) % 5
        assert P5 in (0, 3)
        eps = int(P5 != 0)
        return 3*eps, 0, D3, f'M3,0#Z5,{eps}'
    assert c == 30
    assert ((b//5-a*nu)*3) % 5 == 0
    return 15*t, 45*t, D3, f'M2,{t}#M3,0#Z5,0'


def main():
    print('START', stamp())
    print('SOURCE', Path(__file__).name, sha256(Path(__file__).read_bytes()).hexdigest())
    for name, path in [('RAW', RAW), ('CLEAN_TARGET', TARGET)]:
        print(name, len(path.read_bytes()), sha256(path.read_bytes()).hexdigest())
    data = json.loads(RAW.read_text())
    rows = []
    profile_counts = Counter()
    for prof in data['rows']:
        d0 = F(prof['height_of_generator']).denominator
        ss = []
        for i, (f, B, g, comp) in enumerate(zip(prof['fibers'], prof['elliptic_matrices'],
                                               prof['generator_section_cocycle'], prof['component_coordinates'])):
            n = multiplicative(f)
            s = dict(i=i, f=f, h=component_order(comp), B=B, g=g, n=n)
            if n:
                s['u'], s['kap'] = primitive_data(B, g, n)
            else:
                s['zG'] = log_vector(B, g)
            ss.append(s)
            print('RAW_SITE', prof['OS'], prof['profile'], i, f, 'B', B, 'g', g,
                  'component', comp, 'h', s['h'], 'u_kappa' if n else 'zG',
                  (s['u'], s['kap']) if n else [str(x) for x in s['zG']])
        for s in ss:
            nu = s['n']
            if not nu or d0 % nu:
                continue
            ab = d0//nu
            for a in range(1, ab+1):
                if ab % a:
                    continue
                b = ab//a
                if gcd(b*s['kap'], nu) != 1:
                    continue
                if any(not (narrow(t, a) or narrow(t, b)) for t in ss if t is not s):
                    continue
                hs = group_ring(a, b, s['kap'], nu)
                if not hs:
                    continue
                assert hs == [0] and gcd(a, b) == 1
                r = dict(OS=prof['OS'], profile=prof['profile'], a=a, b=b,
                         zero=s['i'], nu=nu, kap=s['kap'], d0=d0, sites=ss)
                rows.append(r)
                profile_counts[(prof['OS'], prof['profile'])] += 1
    rows.sort(key=rowkey)
    assert len(rows) == 172 and len({rowkey(r) for r in rows}) == 172
    allpat = []
    mins = []
    compatible = []
    excluded = []
    zero_patterns = []
    positive_zero = []
    additive_patterns = []
    nonzero_original = []
    nonzero_mult_positions = set()
    for r in rows:
        ss = r['sites']; a, b, z = r['a'], r['b'], r['zero']
        good = [s['i'] for s in ss if s['f'] in GOOD]
        mult = [s['i'] for s in ss if s['n'] and s['i'] != z and not narrow(s, a)]
        nonzero_mult_positions.update((rowkey(r), i) for i in mult)
        print('NATURAL', textkey(r), 'nu_kappa', r['nu'], r['kap'], 'd0', r['d0'],
              'finite_sites', good, 'nonzero_mult_sites', mult)
        for finite in choices(good):
            orig = [s for s in ss if not s['n'] and s['i'] not in finite]
            pk = (rowkey(r), finite)
            additive_patterns.append(pk)
            if any(not narrow(s, a) for s in orig):
                nonzero_original.append(pk)
            else:
                zero_patterns.append(pk)
                beta = sum(rho_nonzero[s['f']]-1 for s in orig)
                if beta:
                    positive_zero.append((pk, beta))
            for orig_mult in choices(mult):
                allpat.append((r, finite, orig_mult))
            if not all(original_minimal(s, a, b) for s in orig):
                continue
            if not all(all((b*x).denominator == 1 for x in ss[i]['zG']) for i in finite):
                continue
            compatible.append(pk)
            orders = [GOOD[ss[i]['f']][0] for i in finite]
            if any(gcd(orders[i], orders[j]) != 1 for i in range(len(orders)) for j in range(i)):
                excluded.append(pk)
                continue
            qf = prod(GOOD[ss[i]['f']][1] for i in finite)
            assert b % qf == 0
            c = b//qf
            P, mu, D3, model = invariants(r, c)
            mins.append((r, finite, c, P, mu, D3, model))
    for j, (r, finite, orig_mult) in enumerate(allpat, 1):
        print('PATTERN495', j, textkey(r), 'F', finite, 'O_mult', orig_mult)
    for j, (r, finite, c, P, mu, D3, model) in enumerate(mins, 1):
        print('MINIMAL162', j, textkey(r), 'F', finite, 'c', c,
              'nu_kappa', r['nu'], r['kap'], 'P', P, 'lambda', 2*P % c,
              'mu', mu, 'D3', D3, 'model', model)
    residual_counts = Counter(x[2] for x in mins)
    model_counts = Counter(x[6] for x in mins)
    sphere_rows = {rowkey(x[0]) for x in mins if x[2] == 1}
    sphere_profiles = Counter((x[0]['OS'], x[0]['profile']) for x in mins if x[2] == 1)
    stars459 = [p for p in allpat if not any(p[0]['sites'][i]['f'].endswith('*') for i in p[1])]
    print('PROFILE_NATURAL_COUNTS', sorted(profile_counts.items()))
    print('PROFILE_SPHERE_COUNTS', sorted(sphere_profiles.items()))
    print('RESIDUAL_COUNTS', sorted(residual_counts.items()))
    print('MODEL_COUNTS', sorted(model_counts.items()))
    print('EXCLUDED_NONCOPRIME', excluded)
    print('SUMMARY', 'natural', len(rows), 'additive', len(additive_patterns),
          'nonzero_original', len(nonzero_original), 'zero_original', len(zero_patterns),
          'zero_rows', len({x[0] for x in zero_patterns}), 'positive_zero', len(positive_zero),
          'nonzero_mult_positions', len(nonzero_mult_positions), 'patterns', len(allpat),
          'star_original_patterns', len(stars459), 'compatible_minimal', len(compatible),
          'minimal', len(mins), 'sphere_rows', len(sphere_rows), 'oriented_types', len(model_counts))
    assert (len(additive_patterns), len(nonzero_original), len(zero_patterns),
            len({x[0] for x in zero_patterns}), len(positive_zero)) == (282, 54, 228, 160, 30)
    assert (len(nonzero_mult_positions), len(allpat), len(stars459)) == (120, 495, 459)
    assert (len(compatible), len(excluded), len(mins), len(sphere_rows), len(model_counts)) == (164, 2, 162, 50, 24)
    assert residual_counts == Counter({1:59, 2:15, 3:8, 4:5, 5:24, 6:5, 7:12,
                                      8:8, 10:7, 14:5, 15:7, 20:5, 30:2})
    print('END', stamp(), 'ALL_EXACT_ASSERTIONS_PASSED')


if __name__ == '__main__':
    main()
