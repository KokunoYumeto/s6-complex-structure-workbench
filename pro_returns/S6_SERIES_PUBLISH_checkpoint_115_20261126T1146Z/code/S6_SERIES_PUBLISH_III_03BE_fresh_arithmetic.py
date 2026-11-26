#!/usr/bin/env python3
"""Exact quotient-diagram checks for 03BE's explicitly named examples.

No computation of pi_6(A) or of the native alpha order is asserted.
General group claims are proved in the pre-release derivation.
"""
from datetime import datetime, timezone

print('03BE new arithmetic started', datetime.now(timezone.utc).isoformat())
for modulus in (2, 4):
    group = tuple(range(modulus))
    epsilon = {x: x % 2 for x in group}
    kernel = frozenset(x for x in group if epsilon[x] == 0)
    coset = {x: frozenset((x + k) % modulus for k in kernel) for x in group}
    quotient = frozenset(coset.values())
    phi = {coset[x]: epsilon[x] for x in group}
    psi = {r: coset[r] for r in (0, 1)}
    assert len(quotient) == 2
    for x in group:
        assert psi[phi[coset[x]]] == coset[x]
        for y in group:
            assert epsilon[(x+y) % modulus] == (epsilon[x]+epsilon[y]) % 2
    for r in (0, 1):
        assert phi[psi[r]] == r
        for s in (0, 1):
            assert coset[(r+s) % modulus] == psi[(r+s) % 2]
    alpha_order = next(n for n in range(1, modulus+1) if n % modulus == 0)
    all_hom_images = [x for x in group if (2*x) % modulus == 0]
    section_images = [x for x in all_hom_images if epsilon[x] == 1]
    assert alpha_order == modulus
    assert section_images == ([1] if modulus == 2 else [])
    assert all(epsilon[n % modulus] == 1 for n in range(-101, 102, 2))
    print(f'E{modulus}: kernel={sorted(kernel)}, cosets={sorted(map(sorted, quotient))}; '
          f'Phi/Psi mutually inverse; order(alpha)={alpha_order}; '
          f'possible section images={section_images}')

# The universal integer computation is n=2q+r for r=0,1.
# Addition of representatives uses r+s=2carry+residue; q is arbitrary.
for r in (0, 1):
    for s in (0, 1):
        carry, residue = divmod(r+s, 2)
        assert r+s == 2*carry+residue
        assert residue in (0, 1)
        assert (r+s-residue) % 2 == 0
for n in range(-101, 102):
    q, r = divmod(n, 2)
    assert n == 2*q+r and r in (0, 1)
    assert (n-r) % 2 == 0
    assert bool(n % 2) == (r == 1)
print('Einfinity: both residue representatives and all four residue sums checked; '
      'n=2q+r checked on 203 signed integers; the derivation proves all integers')
print('Native result: epsilon(alpha)=1 is the admitted input; '
      'no native order or splitting is computed by these examples')
print('03BE new arithmetic complete', datetime.now(timezone.utc).isoformat())
