#!/usr/bin/env python3
"""Exact coefficient transports for fresh LG catalogue, no target history."""
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
from math import gcd, prod
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FRESH = ROOT / 'code/S6_SERIES_PUBLISH_c7_lg_catalogue_v001.out'
PATTERN = re.compile(
    r'^MINIMAL162 (\d+) (\S+) F (.*?) c (\d+) '
    r'nu_kappa (-?\d+) (-?\d+) P (-?\d+) lambda (-?\d+) '
    r'mu (-?\d+) D3 (\d+) model (\S+)$'
)


def d3(c):
    return c * gcd(c, 3)


def units(c):
    return [u for u in range(1, c) if gcd(u, c) == 1] if c > 1 else [1]


def pair_image(c, P, mu, u):
    return (u * P % c, u ** 3 * mu % d3(c))


def check_crt(factors):
    c = prod(factors)
    assert all(gcd(x, y) == 1 for j, x in enumerate(factors)
               for y in factors[:j])
    mult = [c // n for n in factors]
    ds = [d3(n) for n in factors]
    assert prod(ds) == d3(c)
    inv1 = [pow(a, -1, n) for a, n in zip(mult, factors)]
    inv3 = [pow(a ** 3, -1, D) for a, D in zip(mult, ds)]
    for x in product(*(range(n) for n in factors)):
        z = sum(a * t for a, t in zip(mult, x)) % c
        back = tuple(v * z % n for v, n in zip(inv1, factors))
        assert back == x
    for z in range(c):
        x = [v * z % n for v, n in zip(inv1, factors)]
        assert sum(a * t for a, t in zip(mult, x)) % c == z
    for y in product(*(range(D) for D in ds)):
        z = sum(a ** 3 * t for a, t in zip(mult, y)) % d3(c)
        back = tuple(v * z % D for v, D in zip(inv3, ds))
        assert back == y
    for z in range(d3(c)):
        y = [v * z % D for v, D in zip(inv3, ds)]
        assert sum(a ** 3 * t for a, t in zip(mult, y)) % d3(c) == z
    print('CRT', factors, 'H2_multipliers', mult, 'H2_inverse', inv1,
          'H6_multipliers', [a ** 3 % d3(c) for a in mult],
          'H6_inverse', inv3, 'ALL_COMPOSITIONS_IDENTITY')


def main():
    print('SOURCE', Path(__file__).name, sha256(Path(__file__).read_bytes()).hexdigest())
    print('FRESH_INPUT', FRESH.name, sha256(FRESH.read_bytes()).hexdigest())
    rows = []
    for line in FRESH.read_text().splitlines():
        m = PATTERN.fullmatch(line)
        if m:
            j, key, finite, c, nu, kap, P, lam, mu, D, model = m.groups()
            rows.append((int(j), key, finite, int(c), int(nu), int(kap),
                         int(P), int(lam), int(mu), int(D), model))
    assert len(rows) == 162
    assert [r[0] for r in rows] == list(range(1, 163))
    classes = Counter()
    model_to_class = defaultdict(set)
    class_to_model = defaultdict(set)
    row_transports = []
    for j, key, finite, c, nu, kap, P, lam, mu, D, model in rows:
        assert D == d3(c) and lam == (2 * P) % c
        images = {pair_image(c, P, mu, u) for u in units(c)}
        rep = min(images)
        u = next(u for u in units(c) if pair_image(c, P, mu, u) == rep)
        v = pow(u, -1, c) if c > 1 else 1
        assert pair_image(c, *rep, v) == (P, mu)
        assert (u * v - 1) % c == 0
        identity = (c, *rep)
        classes[identity] += 1
        model_to_class[model].add(identity)
        class_to_model[identity].add(model)
        row_transports.append((j, key, finite, c, (P, mu), rep, u, v, model))
    assert all(len(s) == 1 for s in model_to_class.values())
    assert all(len(s) == 1 for s in class_to_model.values())
    for row in row_transports:
        j, key, finite, c, pair, rep, u, v, model = row
        print('TRANSPORT', j, key, 'F', finite, 'c', c, 'pair', pair,
              'representative', rep, 'u', u, 'inverse', v, 'model', model)
    for identity, count in sorted(classes.items()):
        print('ORBIT', identity, 'patterns', count,
              'model', next(iter(class_to_model[identity])))
    assert len(classes) == 24
    for factors in [(2, 3), (2, 5), (2, 7), (3, 5), (4, 5), (2, 3, 5)]:
        check_crt(factors)
    print('SUMMARY', 'rows', len(rows), 'complete_invariant_orbits', len(classes),
          'model_bijection', len(model_to_class), 'ALL_ASSERTIONS_PASSED')


if __name__ == '__main__':
    main()
