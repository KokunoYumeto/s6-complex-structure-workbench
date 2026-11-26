"""Recompute complete small Kummer orbits using determinant lines modulo N.

This post-release comparison uses exterior squares and unit-normalized
Pluecker columns. The referenced old program uses integral column Hermite
normal form. The exact bijection between these representations is proved
in the written comparison. This program never imports or runs the old one.
"""
from collections import deque
from datetime import datetime, timezone
from itertools import combinations
from math import gcd
from pathlib import Path
import hashlib
import json

from S6_SERIES_PUBLISH_III_02K5_fresh_orbit import calculate, mul, power


def exterior_square(matrix):
    pairs = list(combinations(range(4), 2))
    return [[matrix[i][k] * matrix[j][l] - matrix[i][l] * matrix[j][k]
             for k, l in pairs] for i, j in pairs]


def orbit(n, generators):
    units = [u for u in range(n) if gcd(u, n) == 1]

    def canonical(column):
        return min(tuple(u*x % n for x in column) for u in units)

    initial = canonical((1, 0, 0, 0, 0, 0))
    seen, queue = {initial}, deque([initial])
    transitions = 0
    while queue:
        column = queue.popleft()
        for matrix in generators:
            target = canonical([sum(a*b for a, b in zip(row, column))
                                for row in matrix])
            transitions += 1
            assert gcd(n, *target) == 1
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return {'N': n, 'orbit_size': len(seen), 'generator_transitions': transitions,
            'complete_reachable_set_sha256': hashlib.sha256(
                json.dumps(sorted(seen), separators=(',', ':')).encode()).hexdigest()}


def main():
    fresh = calculate()
    a1, a2, u, v = (fresh[k] for k in ('A1', 'A2', 'U', 'V'))
    # The original printed family is exactly D^a U^b, with D=U V^{-1}.
    d = mul(mul(mul(power(a2, 2), a1), power(a2, 2)), power(a1, 2))
    assert d == [[1, 0, 0, 0], [0, 1, 0, 0], [6, 0, 1, 0], [-6, 1, 0, 1]]
    assert mul(d, v) == u
    actions = [exterior_square(a1), exterior_square(a2)]
    results = [orbit(n, actions) for n in range(2, 9)]
    counts = [r['orbit_size'] for r in results]
    assert counts == [12, 36, 96, 150, 432, 392, 768]
    result = {
        'target': '02K5 / maps:src:C.1.4',
        'completed_utc': datetime.now(timezone.utc).isoformat(),
        'exposure': 'Post-release recomputation of the full small-orbit counts; the complete all-N written derivation was fixed before release.',
        'method': 'Breadth-first orbit of primitive determinant-line columns in exterior^2 (Z/NZ)^4, modulo multiplication by units, using exact 2x2 minors.',
        'old_method': 'The referenced original code uses integral column Hermite normal form. It was read after proof release; it was not imported or executed.',
        'D': d, 'exact_family_change': 'D^a U^b = U^(a+b) V^(-a); inverse parameter map a=-s, b=r+s.',
        'wedge_basis': [list(p) for p in combinations(range(4), 2)],
        'exterior_generator_matrices': actions,
        'complete_orbits': results,
        'scope': 'The seven finite cardinalities are exhaustive for their stated moduli. The all-N orbit lower bound remains the separate pre-exposure integer graph proof.',
        'attribution': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical reasoning effort not separately exposed; fourth continuation, root full-orbit recomputation',
    }
    out = Path(__file__).resolve().parents[1] / 'agents/continuation4_iii_root/S6_SERIES_PUBLISH_III_02K5_exterior_orbit.json'
    out.write_text(json.dumps(result, indent=2) + '\n', newline='\n')
    print('Complete exterior-square orbit cardinalities:', counts)
    print('Printed and fresh integer families agree by (r,s)=(a+b,-a).')
    print(out)


if __name__ == '__main__':
    main()
