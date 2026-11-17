"""Exact finite cyclic elliptic-fibre configurations for C.2.UN.33.

The geometric input is proved in the accompanying text.  This certificate
enumerates every character of every faithful cyclic elliptic-base action,
reduces the local reflection kernels, and checks all Euler and character sums.
"""
from math import gcd
from collections import Counter

euler = {'I0':0,'II':2,'III':3,'IV':4,'I0*':6,'IV*':8,'III*':9,'II*':10}
small = {2:'I0*',3:'IV',4:'III',6:'II'}
large = {2:'I0*',3:'IV*',4:'III*',6:'II*'}

def local_type(e, a):
    a %= e
    if a == 0:
        return 'I0'
    common = gcd(e,a)
    d, exponent = e//common, a//common
    assert d in (2,3,4,6)
    assert exponent in (1,d-1)
    return small[d] if exponent == 1 else large[d]

def canonical_config(types):
    return tuple(sorted(t for t in types if t != 'I0'))

seen = {1:set(),2:set()}
print('Source base P1: two branch values; primitive fibre orders 2,3,4,6.')
for d in (2,3,4,6):
    types = [local_type(d,1),local_type(d,-1)]
    total = sum(euler[t] for t in types)
    assert total == 12
    seen[1].add(canonical_config(types))
    print(f'  fibre order {d}: {types}; Euler={total}, chi=1')

branch = {2:[2,2,2,2],3:[3,3,3],4:[4,4,2],6:[6,3,2]}
print('Source base elliptic: all characters a modulo n, including zero.')
for n, indices in branch.items():
    # Riemann-Hurwitz: 0=n*(-2+sum(1-1/e)).
    from fractions import Fraction
    assert sum(Fraction(e-1,e) for e in indices) == 2
    for a in range(n):
        types = [local_type(e,a) for e in indices]
        total = sum(euler[t] for t in types)
        assert total % 12 == 0
        chi = total//12
        # On source H^1(O): base character is nontrivial; vertical survives
        # precisely for a=0.  H^0(K) has character zeta_n^(a+1).
        irregularity = int(a == 0)
        geometric_genus = int((a+1) % n == 0)
        assert chi == 1-irregularity+geometric_genus
        assert chi in (0,1,2)
        if chi:
            seen[chi].add(canonical_config(types))
        print(f'  n={n}, a={a}, indices={indices}: {types}; '
              f'Euler={total}, chi={chi}, q={irregularity}, pg={geometric_genus}')

assert len(seen[1]) == 7
assert len(seen[2]) == 4
print('Distinct positive-chi configurations:')
for chi in (1,2):
    for config in sorted(seen[chi]):
        assert sum(euler[t] for t in config) == 12*chi
        print(f'  chi={chi}: {dict(Counter(config))}')
print('Exactly seven chi=1 and four chi=2 configurations. All exact checks passed.')
