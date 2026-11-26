#!/usr/bin/env python3
"""Fresh direct-minor check of the one-finite-cap presentation.

Reads only the root's newly derived literal finite lattices. No L4/L6
original or historical program is read. The all-parameter proof is in
the adjacent fresh derivation; this bounded check uses determinants of
the full presentation, without importing a Smith reduction routine.
"""
from pathlib import Path
from itertools import combinations, permutations
from math import gcd
from functools import reduce
from collections import Counter
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'agents/continuation7_iii_finite_general/S6_SERIES_PUBLISH_III_finite_fresh_lattices.json'
rows = json.loads(SRC.read_text())['positions']


def det(matrix):
    size = len(matrix)
    ans = 0
    for p in permutations(range(size)):
        parity = sum(p[i] > p[j] for i in range(size) for j in range(i+1, size))
        term = (-1)**parity
        for i in range(size):
            term *= matrix[i][p[i]]
        ans += term
    return ans


def divisors(matrix):
    result = []
    for size in range(1, min(len(matrix), len(matrix[0]))+1):
        values = []
        for rr in combinations(range(len(matrix)), size):
            for cc in combinations(range(len(matrix[0])), size):
                values.append(det([[matrix[i][j] for j in cc] for i in rr]))
        value = reduce(gcd, values, 0)
        if not value:
            break
        result.append(abs(value))
    return result


print('FRESH_LITERAL_LATTICES_SHA256', hashlib.sha256(SRC.read_bytes()).hexdigest())
totals = Counter()
for index, row in enumerate(rows, 1):
    b, g, q, qv, d = (row[key] for key in ('b', 'g', 'q', 'qv', 'order'))
    count = Counter()
    assert qv*g == q and b % qv == 0
    for k in (1, 2, 3, 4):
        m = d*k
        assert m % g == m % qv == 0
        for n in range(m):
            for r in range(m):
                t = gcd(m, qv*r, g*n)
                if gcd(m, n, r) != 1 or (m//t) % d:
                    continue
                for e in (-2, 0, 1, 3):
                    # Columns are the three full Thom images and the
                    # marked global relation D+b e s=0.
                    original = [[b*g*n//qv, -b*r, 0, b*e],
                                [m//qv, 0, r, 1],
                                [0, m//g, n, 0]]
                    nprime = n-(m//g)*e
                    K = m//g
                    reduced = [[b*g*nprime//qv, -b*r, 0],
                               [0, K, nprime]]
                    actual = divisors(original)
                    actual_reduced = divisors(reduced)
                    assert actual == [1]+actual_reduced
                    if nprime:
                        h = gcd(b, K, nprime)
                        delta2 = b*g*abs(nprime)*t//q
                        assert b*g*abs(nprime)*t % q == 0
                        assert delta2 % (h*h) == 0
                        assert actual == [1, h, delta2]
                        count['nonzero_euler'] += 1
                    else:
                        assert actual == [1, gcd(b, K)]
                        count['zero_euler'] += 1
                    count['torsion_core'] += int(t > 1)
    totals.update(count)
    print('POSITION', index, row['OS'], row['profile'],
          'a/b', row['a'], b, 'zero', row['zero_index'],
          'finite', row['finite_index'], row['kind'],
          'g/qv', g, qv, dict(sorted(count.items())), 'PASS')
print('TOTALS', dict(sorted(totals.items())))
print('PASS direct determinantal divisors of every tested full presentation,')
print('PASS including nonzero/zero rational Euler values and nontrivial core torsion.')
