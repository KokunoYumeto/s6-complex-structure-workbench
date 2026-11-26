"""Post-exposure LU: derive every additional residue pair from raw periods.

The input is only the admitted twenty-one-profile fixture. Component orders
are calculated from actual rational period logarithms, and a separate CRT
count is compared with direct residue enumeration. No historical program
or historical correction list is imported or executed.
"""
from datetime import datetime, timezone
from hashlib import sha256
from itertools import product
from math import gcd, lcm, prod
from pathlib import Path
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
assert sha256(RAW.read_bytes()).hexdigest() == '6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522'
rows = json.loads(RAW.read_bytes())['rows']
assert len(rows) == 21


def bezout_pair(a, b):
    r, rr, x, xx, y, yy = a, b, 1, 0, 0, 1
    while rr:
        q = r // rr
        r, rr, x, xx, y, yy = rr, r-q*rr, xx, x-q*xx, yy, y-q*yy
    sign = 1 if r >= 0 else -1
    return sign*r, sign*x, sign*y


def period(B, g, kind):
    A = B-S.eye(2)
    if A.det():
        z = A.inv()*g
        data = {'z_G': list(map(str, z))}
    else:
        assert kind.startswith('I') and kind[1:].isdigit() and A.rank() == 1
        col = next(A[:, j] for j in range(2) if A[:, j] != S.zeros(2, 1))
        common = gcd(*map(abs, map(int, col)))
        u = col/common
        if next(x for x in u if x) < 0:
            u = -u
        one, x, y = bezout_pair(int(u[0]), int(u[1]))
        assert one == 1
        v = S.Matrix([-y, x])
        read = S.Matrix([[x, y]])
        nu = int((read*A*v)[0])
        kappa = int((read*g)[0])
        assert nu == int(kind[1:]) and A*v == nu*u and g == kappa*u
        assert S.Matrix.hstack(u, v).det() == 1
        z = S.Rational(kappa, nu)*v
        data = {'u': list(map(int, u)), 'v': list(map(int, v)),
                'period_inverse': S.Matrix.hstack(u, v).inv().tolist(),
                'nu': nu, 'kappa': kappa, 'z_G': list(map(str, z))}
    assert A*z == g
    h = lcm(*(int(x.q) for x in z))
    data.update(order=h, order_multiple=list(map(int, h*z)))
    if 'nu' in data:
        assert gcd(data['nu'], data['kappa']) == 1
        assert h == data['nu']
    return data


def cyclic_inverse(hvec):
    n = len(hvec)
    assert sum(hvec) == 0 and sum(i*x for i, x in enumerate(hvec)) % n == 0
    r0 = -sum((n-1-i)*x for i, x in enumerate(hvec)) // n
    rr = [r0 + sum(hvec[:i]) for i in range(n)]
    assert sum(rr) == 0
    divisor = [0] + [sum(rr[1:i+1]) for i in range(1, n)]
    C = -2*S.eye(n)
    for i in range(n):
        C[i, (i-1) % n] += 1
        C[i, (i+1) % n] += 1
    assert C*S.Matrix(divisor) == S.Matrix(hvec)
    return divisor


print('START', datetime.now(timezone.utc).isoformat(), flush=True)
profile_data, additional = [], []
for row in rows:
    height = S.Rational(row['height_of_generator'])
    d0 = int(1/height)
    assert height*d0 == 1
    local = [period(S.Matrix(B), S.Matrix(g), kind)
             for B, g, kind in zip(row['elliptic_matrices'],
                                  row['generator_section_cocycle'], row['fibers'])]
    orders = [d['order'] for d in local if d['order'] > 1]
    assert prod(orders) == d0
    assert all(gcd(x, y) == 1 for i, x in enumerate(orders) for y in orders[i+1:])
    coefficients = [(d0//h)*pow(d0//h, -1, h) for h in orders]
    for a in range(d0):
        assert sum(c*(a % h) for c, h in zip(coefficients, orders)) % d0 == a
    all_height, old = [], []
    for a, b in product(range(d0), repeat=2):
        if a*b % d0:
            continue
        all_height.append((a, b))
        new_sites = [j for j, data in enumerate(local)
                     if a % data['order'] and b % data['order']]
        if not new_sites:
            old.append((a, b))
            continue
        assert a > 0 and b > 0
        details = []
        for j in new_sites:
            kind, data = row['fibers'][j], local[j]
            assert a*b % data['order'] == 0
            item = dict(site=j, type=kind, order=data['order'],
                        generator_residues=[a % data['order'], b % data['order']])
            if 'nu' in data:
                n, kappa = data['nu'], data['kappa']
                p, q = -a*kappa % n, -b*kappa % n
                g = gcd(n, q)
                ell = n//g
                assert p % ell == 0 and g > 1
                degree = [(p//ell)*(int(i % g == 1)-int(i % g == 0)) for i in range(n)]
                hvec = [degree[i]-int(i == p)+int(i == 0) for i in range(n)]
                divisor = cyclic_inverse(hvec)
                assert all(degree[(i+q) % n] == degree[i] for i in range(n))
                item.update(physical_residues=[p, q], divisor=divisor, degrees=degree)
            else:
                assert kind in ('I1*', 'I3*') and data['order'] == 4
                assert a % 4 == b % 4 == 2
                size = 6 if kind == 'I1*' else 8
                item.update(divisor=[-1]+[0]*(size-1),
                            degrees=[1, 1, 0, 0, -1]+[0]*(size-5),
                            canonical_orbits=[[0, 1], [2, 3]]+[[i] for i in range(4, size)],
                            h=1)
            details.append(item)
        entry = dict(OS=row['OS'], profile=row['profile'], d0=d0, a=a, b=b,
                     height=a*b//d0, newly_nonnarrow=details)
        additional.append(entry)
    height_count = prod(sum(gcd(h, x) for x in range(h)) for h in orders)
    old_count = prod(2*h-1 for h in orders)
    assert len(all_height) == height_count and len(old) == old_count
    selected = [r for r in additional if (r['OS'], r['profile']) == (row['OS'], row['profile'])]
    assert len(selected) == height_count-old_count
    profile_data.append(dict(OS=row['OS'], profile=row['profile'], d0=d0,
                             local_periods=local, CRT_coefficients=coefficients,
                             height_count=height_count, narrow_OR_count=old_count,
                             additional_pairs=[[r['a'], r['b']] for r in selected]))
    print('PROFILE', row['OS'], row['profile'], 'd0', d0, 'orders', orders,
          'height', height_count, 'narrow_OR', old_count, 'additional', len(selected), flush=True)
assert len(additional) == 45
for i, row in enumerate(additional, 1):
    print('ADDITIONAL', i, json.dumps(row, sort_keys=True, separators=(',', ':')), flush=True)
destination = ROOT / 'agents/continuation7_iii_corrected_initial_receiving/S6_SERIES_PUBLISH_III_02LU_additional_residue_pairs_v001.json'
assert not destination.exists()
destination.write_text(json.dumps({'scope': __doc__, 'profiles': profile_data,
                                   'additional_pairs': additional}, indent=2, default=int)+'\n')
print('COMPLETE 21 raw period tables; exact CRT inverses; all45 additional residue pairs and literal local corrections.', flush=True)
print('DATA', destination.relative_to(ROOT), 'SHA256', sha256(destination.read_bytes()).hexdigest(), flush=True)
print('END', datetime.now(timezone.utc).isoformat(), flush=True)
