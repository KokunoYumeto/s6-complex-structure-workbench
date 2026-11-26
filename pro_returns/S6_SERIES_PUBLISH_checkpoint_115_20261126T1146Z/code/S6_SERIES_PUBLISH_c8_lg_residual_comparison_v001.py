#!/usr/bin/env python3
"""Post-exposure comparison of LG's uniform residual claims.

Geometry comes from the admitted LL/LM proofs recorded in the frozen
fresh catalogue. This program compares the released claim with all
marked rows and every cyclic unit map; it does not rederive geometry.
"""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from math import gcd
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = ROOT / 'agents/continuation8_iii_lg_receiving/S6_SERIES_PUBLISH_III_02LG_released_original.tex'
FRESH = ROOT / 'code/S6_SERIES_PUBLISH_c7_lg_catalogue_v001.out'
pattern = re.compile(
    r'^MINIMAL162 (\d+) (\S+) F (.*?) c (\d+) '
    r'nu_kappa (-?\d+) (-?\d+) P (-?\d+) lambda (-?\d+) '
    r'mu (-?\d+) D3 (\d+) model (\S+)$')

old = ORIGINAL.read_bytes()
assert sha256(old).hexdigest() == '78bde0a45b4dd7f15b7d36ce092787c1c7144e231290f8018a0d5bd11e3dbbc0'
assert r'Residual orders $4,8,20$ give respectively' in old.decode()
assert r'Their full refined classes are $2,0,14$' in old.decode()
old_P = {4: 2, 8: 0, 20: 14}
old_model = {4: 'Z4,1', 8: 'Z8,0', 20: 'Z4,1#Z5,1'}
rows = []
for line in FRESH.read_text().splitlines():
    m = pattern.fullmatch(line)
    if m:
        j, key, finite, c, nu, kap, P, lam, mu, D, model = m.groups()
        rows.append((int(j), key, finite, int(c), int(P), int(lam), int(mu), int(D), model))
assert len(rows) == 162
residual = [r for r in rows if r[3] in old_P]
assert len(residual) == 18

print('UTC', datetime.now(timezone.utc).isoformat())
print('SOURCE_SHA256', sha256(Path(__file__).read_bytes()).hexdigest())
print('ORIGINAL_SHA256', sha256(old).hexdigest())
print('FRESH_SHA256', sha256(FRESH.read_bytes()).hexdigest())
changed, retained = Counter(), Counter()
for j, key, finite, c, P, lam, mu, D, model in residual:
    assert D == c * gcd(c, 3) and lam == 2 * P % c and mu == 0
    maps = []
    for u in range(1, c):
        if gcd(u, c) != 1:
            continue
        v = pow(u, -1, c)
        assert u * v % c == 1
        assert all(v * (u * x % c) % c == x for x in range(c))
        assert all(u * (v * x % c) % c == x for x in range(c))
        if u * old_P[c] % c == P:
            assert u * (2 * old_P[c] % c) % c == lam
            assert u**3 * 0 % D == mu
            maps.append((u, v))
    same = bool(maps)
    (retained if same else changed)[c] += 1
    old_order = c // gcd(c, old_P[c])
    new_order = c // gcd(c, P)
    assert same == (old_order == new_order)
    print('ROW', j, key, 'F', finite, 'c', c,
          'old_P_model', (old_P[c], old_model[c]),
          'new_P_model', (P, model), 'orders', (old_order, new_order),
          'unit_maps_and_inverses', maps,
          'UNCHANGED' if same else 'D27')

assert dict(changed) == {4: 4, 8: 4, 20: 4}
assert dict(retained) == {4: 1, 8: 4, 20: 1}
for x in range(4):
    for y in range(5):
        z = (5 * x + 4 * y) % 20
        assert (z % 4, 4 * z % 5) == (x, y)
for z in range(20):
    assert (5 * (z % 4) + 4 * (4 * z % 5)) % 20 == z
for eps in (0, 1):
    assert (5 * (2 * eps) + 4) % 20 == 4 + 10 * eps
print('CRT20', 'forward=5x+4y', 'inverse=(z%4,4z%5)', 'ALL_COMPOSITES_IDENTITY')
print('CHANGED', sorted(changed.items()), 'RETAINED', sorted(retained.items()))
print('SUMMARY', 'patterns', 18, 'changed', sum(changed.values()),
      'retained', sum(retained.values()), 'ALL_ASSERTIONS_PASSED')
