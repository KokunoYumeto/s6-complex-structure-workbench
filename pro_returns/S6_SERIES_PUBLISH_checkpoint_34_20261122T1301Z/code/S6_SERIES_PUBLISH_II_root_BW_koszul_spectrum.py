#!/usr/bin/env python3
"""Exact cubic-suspension table from the Koszul Hilbert series.

The calculation uses the degrees of the three partial derivatives, not a
chosen monomial basis for any ADE Jacobian algebra. Geometric input:
the partials of an isolated weighted homogeneous hypersurface form a
regular sequence; the shifted Hilbert degrees are its spectral weights.
The proof and primary-source record state the link and genus comparisons.
This program certifies the finite arithmetic only.
"""
from fractions import Fraction as Q
from math import gcd, lcm, prod
import itertools
import json


def series(weights):
    degree = lcm(*(w.denominator for w in weights))
    integral = [int(w * degree) for w in weights]
    socle = 3 * degree - 2 * sum(integral)
    bound = socle + 2 * degree
    # The free polynomial ring is obtained by three coin recurrences.
    h = [1] + [0] * bound
    for w in integral:
        for k in range(w, bound + 1):
            h[k] += h[k - w]
    # Koszul alternating sums for the regular sequence of partials.
    for w in integral:
        shift = degree - w
        h = [h[k] - (h[k - shift] if k >= shift else 0)
             for k in range(bound + 1)]
    assert all(v >= 0 for v in h[:socle + 1])
    assert not any(h[socle + 1:])
    h = h[:socle + 1]
    assert h == list(reversed(h))
    mu = prod((1 / w - 1) for w in weights)
    assert sum(h) == mu
    shifted = sum(integral)
    pg = sum(v for k, v in enumerate(h) if k + shifted <= degree)
    link_b1 = sum(v for k, v in enumerate(h)
                  if (k + shifted) % degree == 0)
    return dict(degree=degree, weights=integral,
                hilbert_coefficients=[[k, v] for k, v in enumerate(h) if v],
                milnor_number=int(mu), geometric_genus=pg,
                link_first_betti=link_b1)


def rows():
    result = []
    for n in range(1, 11):
        result.append((f'A{n}', [Q(1, 2), Q(1, n + 1)], n,
                       gcd(2, n + 1)))
    for n in range(4, 10):
        result.append((f'D{n}', [Q(n - 2, 2 * (n - 1)), Q(1, n - 1)],
                       n, 1 + gcd(2, n - 2)))
    result.extend([
        ('E6', [Q(1, 3), Q(1, 4)], 6, 1),
        ('E7', [Q(1, 3), Q(2, 9)], 7, 2),
        ('E8', [Q(1, 3), Q(1, 5)], 8, 1),
    ])
    output = []
    for name, w, mu, branches in result:
        assert (mu + branches - 1) % 2 == 0
        delta = (mu + branches - 1) // 2
        data = series(w + [Q(1, 3)])
        assert data['milnor_number'] == 2 * mu
        data.update(type=name, plane_delta=delta, plane_branches=branches,
                    within_BW_delta_range=delta <= 4)
        output.append(data)
    return output


def cost_bounds(table, budget):
    # Dynamic programming includes arbitrary finite multisets, not just one germ.
    states = {0: {(0, 0)}}
    for cost in range(budget + 1):
        for genera, links in tuple(states.get(cost, ())):
            for row in table:
                new_cost = cost + row['plane_delta']
                if new_cost <= budget:
                    states.setdefault(new_cost, set()).add(
                        (genera + row['geometric_genus'],
                         links + row['link_first_betti']))
    pairs = set().union(*states.values())
    result = dict(delta_budget=budget, maximal_total_geometric_genus=max(p[0] for p in pairs),
                  maximal_total_link_betti=max(p[1] for p in pairs),
                  attainable_pairs=sorted(pairs))
    assert result['maximal_total_geometric_genus'] == 1
    assert result['maximal_total_link_betti'] == 2
    return result


if __name__ == '__main__':
    table = rows()
    for r in table:
        expected_pg = 0 if r['type'] in ('A1', 'A2', 'A3', 'A4') else 1
        expected_link = 2 if r['type'] in ('A5', 'D4') else 0
        assert r['geometric_genus'] == expected_pg
        assert r['link_first_betti'] == expected_link
    print(json.dumps(dict(status='PASS', method='Koszul Hilbert series, exact integer degrees',
                          rows=table, multigerm_bounds=[cost_bounds(table, b) for b in (4, 5)],
                          scope='Finite arithmetic; no analytic classification or topological existence is inferred by code'),
                     indent=2))
