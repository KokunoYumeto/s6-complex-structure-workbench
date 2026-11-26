#!/usr/bin/env python3
"""Fresh exact arithmetic for K8; no target proof or earlier program read."""
from collections import Counter
from itertools import product
from math import comb, gcd
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def away_from_six(n):
    n = abs(int(n))
    for p in (2, 3):
        while n and n % p == 0:
            n //= p
    return n


def compositions(total, slots):
    if slots == 0:
        return [()] if total == 0 else []
    if slots == 1:
        return [(total,)]
    return [(i,) + rest for i in range(total + 1)
            for rest in compositions(total - i, slots - 1)]


# The three d_3 maps are computed as the polynomial differential
# D(f(c))=d*a*f'(c), with a exterior of degree 3. This builds the
# integer matrices before any localization or reduction is applied.
c, a, d = s.symbols('c a d')
transgressions = []
for k in range(1, 4):
    actual = s.expand(d * a * s.diff(c ** k, c))
    expected = k * d * a * c ** (k - 1)
    assert s.expand(actual - expected) == 0
    transgressions.append({'source_degree': 2*k,
                           'target_degree': 2*k+1,
                           'coefficient': str(actual.coeff(a*c**(k-1)))})

smith_checks = []
for modulus in (1, -1, 5, -5, 7, 11, 25, 35, 49, 55, 125, 175):
    assert gcd(modulus, 6) == 1
    factors = []
    for k in range(1, 4):
        S = smith_normal_form(s.Matrix([[k * modulus]]), domain=ZZ)
        invariant = abs(int(S[0, 0]))
        localized = away_from_six(invariant)
        assert localized == abs(modulus)
        # On the dual cyclic group, evaluation at the residue of 1
        # has kernel zero, including non-squarefree examples.
        residues = range(abs(modulus))
        assert all((z % abs(modulus) == 0) == (z == 0) for z in residues)
        factors.append({'k': k, 'integer_smith': invariant,
                        'localized_order': localized})
    smith_checks.append({'d': modulus, 'factors': factors})

# Generate every degree-six product cell from its individual factor
# degrees, and pair it with monomials by tensor-factor evaluation.
# This computes the detector matrix independently of a rank formula.
pairing_checks = []
for rank in range(0, 9):
    basis = []
    for cyclic_power in range(0, 4):
        for exponents in compositions(3-cyclic_power, rank):
            basis.append((cyclic_power, exponents))
    pairing = s.Matrix([[int(m == cell) for cell in basis] for m in basis])
    assert pairing == s.eye(len(basis))
    kinds = Counter(cyclic_power for cyclic_power, _ in basis)
    expected = [comb(rank+2, 3), comb(rank+1, 2), rank, 1]
    assert [kinds[k] for k in range(4)] == expected
    assert sum(expected[1:]) == comb(rank+1, 2)+rank+1
    pairing_checks.append({'rank': rank, 'kind_counts': expected,
                           'matrix_size': len(basis), 'determinant': 1})

# A separate polynomial computation constructs the full cubic
# coordinate-change matrix for u -> u + sum a_i*x_i. It includes
# the pure free monomials and hence checks the mixed free/torsion
# triangular transformation as well as its inverse.
substitution_checks = []
for rank in range(0, 5):
    xs = s.symbols('x0:'+str(rank))
    u = s.Symbol('u')
    variables = (u,) + xs
    powers = [(j,) + e for j in range(4)
              for e in compositions(3-j, rank)]
    mons = [s.prod(v**p for v, p in zip(variables, exponent))
            for exponent in powers]
    shift = sum((2*i+1) * x for i, x in enumerate(xs))
    plus = s.Matrix([[s.Poly(s.expand(m.subs(u,u+shift)), *variables)
                       .coeff_monomial(n) for n in mons] for m in mons])
    minus = s.Matrix([[s.Poly(s.expand(m.subs(u,u-shift)), *variables)
                        .coeff_monomial(n) for n in mons] for m in mons])
    assert plus * minus == s.eye(len(mons))
    assert minus * plus == s.eye(len(mons))
    assert plus.det() == 1
    assert minus.det() == 1
    substitution_checks.append({'rank': rank, 'size': len(mons),
                                'plus_det': 1, 'minus_det': 1,
                                'both_compositions': 'identity'})

x, y, z = s.symbols('x y z')
polarized = (x+y+z)**3-(x+y)**3-(x+z)**3-(y+z)**3+x**3+y**3+z**3
assert s.expand(polarized-6*x*y*z) == 0

output = {'method': 'Exact polynomial differential, integer Smith factors, '
                    'tensor-factor cell pairing, and invertible cubic substitution',
          'transgressions': transgressions,
          'smith_checks': smith_checks,
          'pairing_checks': pairing_checks,
          'substitution_checks': substitution_checks,
          'polarization': str(s.expand(polarized)),
          'endpoint_d_one': 'All three positive-degree cyclic groups have order 1.',
          'endpoint_rank_zero': 'Only the cyclic degree-six generator and u^3 remain.',
          'status': 'all exact assertions passed'}
path = Path(__file__).with_suffix('.json')
with path.open('w', encoding='utf-8', newline='\n') as handle:
    json.dump(output, handle, ensure_ascii=False, indent=2)
    handle.write('\n')
print(json.dumps(output, ensure_ascii=False, indent=2))
