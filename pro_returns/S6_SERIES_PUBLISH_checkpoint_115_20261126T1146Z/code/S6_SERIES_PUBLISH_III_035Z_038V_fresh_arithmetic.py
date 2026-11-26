#!/usr/bin/env python3
"""Exact cyclic-group arithmetic supporting the fresh external-smash proof.

The primary readings, rather than this program, supply the homotopy groups.
The cube/pinch proof, rather than this program, supplies the homomorphisms.
This exhausts the finite possibilities for the two homomorphisms once their
source and target groups have been proved. No target proof is opened.
"""
from datetime import datetime, timezone


def hom(a, m, n):
    """Homomorphism Z/m -> Z/n taking 1 to a, as a full value table."""
    assert (m * a) % n == 0
    values = tuple((a * k) % n for k in range(m))
    for j in range(m):
        for k in range(m):
            assert values[(j+k) % m] == (values[j]+values[k]) % n
    return values


print('UTC:', datetime.now(timezone.utc).isoformat())
kernel12 = tuple(a for a in range(24) if (12*a) % 24 == 0)
even24 = tuple(2*a for a in range(12))
assert kernel12 == even24
print('ker([12]:Z/24 -> Z/24) =', kernel12)

delta = hom(2, 12, 24)
assert delta == even24
inverse = {2*a: a for a in range(12)}
assert all(inverse[delta[a]] == a for a in range(12))
assert all(delta[inverse[b]] == b for b in even24)
print('delta:Z/12 -> ker[12], a -> 2a, and delta^-1 verified exactly')

first = [hom(a, 12, 24) for a in kernel12]
second = [hom(a, 24, 2) for a in range(2) if (24*a) % 2 == 0]
composite_pairs = 0
composite_values = 0
for r in first:
    for d in second:
        composite_pairs += 1
        for a in range(12):
            assert d[r[a]] == 0
            composite_values += 1
print('Hom(Z/12,Z/24):', len(first), 'full homomorphism tables')
print('Hom(Z/24,Z/2):', len(second), 'full homomorphism tables')
print('All composite pairs:', composite_pairs, '; all source values:', composite_values)
print('Every composite Z/12 -> Z/24 -> Z/2 is zero')
print('This is exact finite arithmetic; it supplies no separate topological proof credit.')
