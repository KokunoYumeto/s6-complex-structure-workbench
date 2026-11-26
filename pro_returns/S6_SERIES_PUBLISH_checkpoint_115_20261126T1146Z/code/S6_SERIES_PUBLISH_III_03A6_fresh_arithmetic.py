#!/usr/bin/env python3
"""Exact coefficient injection and all characters for the fresh03A6 check."""
from datetime import datetime, timezone
from fractions import Fraction

delta = tuple((2*a) % 24 for a in range(12))
assert len(set(delta)) == 12
assert tuple(a for a in range(12) if delta[a] == 0) == (0,)
inverse = {2*a: a for a in range(12)}
assert all(inverse[delta[a]] == a for a in range(12))
assert all(delta[inverse[b]] == b for b in delta)
for a in range(12):
    for b in range(12):
        assert delta[(a+b) % 12] == (delta[a]+delta[b]) % 24


def chi(b, k):
    return Fraction(b*k, 12) % 1


characters = [tuple(chi(b, k) for k in range(12)) for b in range(12)]
assert len(set(characters)) == 12
additivity_checks = 0
for b in range(12):
    assert chi(b+12, 1) == chi(b, 1)
    for k in range(12):
        assert chi(b, k+12) == chi(b, k)
        for ell in range(12):
            assert chi(b, (k+ell) % 12) == (chi(b, k)+chi(b, ell)) % 1
            additivity_checks += 1

# Nullity of E^6 g forces precisely this coefficient residue via delta.
forced_a, = [a for a in range(12) if delta[a] == 0]
# The one-copy class is independently zero by the based homotopy H_G.
# Its value is not inferred from injectivity of the suspension map.
one_copy_class = 0
theta = tuple((n*one_copy_class) % 12 for n in range(12))
assert theta == (0,)*12
composites = [[chi(b, theta[n]) for n in range(12)] for b in range(12)]
assert all(value == 0 for row in composites for value in row)

print('UTC:', datetime.now(timezone.utc).isoformat())
print('delta:Z/12 -> Z/24, a -> 2a:', delta)
print('Both inverse identities on the even image and all144 addition pairs verified')
print('Complete zero fibre of delta:', (forced_a,))
print('All12 characters k -> b*k/12 modZ constructed with exact Fraction values')
print('Character additivity equations verified:', additivity_checks)
print('Theta at the independently proved zero one-copy class:', theta)
print('Every one of144 character-composite values is0 inR/Z; exponential value is1')
print('The group and null-homotopy inputs are proved separately; no extra check event.')
