#!/usr/bin/env python3
"""Fresh exact invariant-map checks for K9, before target-proof exposure."""
from collections import Counter
from itertools import product
from math import gcd, lcm
from pathlib import Path
import json
import sympy as s


rows = []
for d in (1, 5, 7, 11, 25, 35, 49):
    assert gcd(d,6) == 1
    data = (0,-d,d,0,0,0)
    l0,l1,l2,k1,k2,sigma = data
    actual_p = 12*l0-4*l1-3*l2
    assert actual_p == d
    assert l1 % 3 != 0 and l2 % 2 != 0

    # Hom(Z/d,Z/2) and Ext(Z/d,Z/2) use this exact same map.
    mod_two_images = {(d*x) % 2 for x in range(2)}
    mod_two_kernel = [x for x in range(2) if (d*x) % 2 == 0]
    assert mod_two_images == {0,1}
    assert mod_two_kernel == [0]
    quarter_kernel = [x for x in range(d) if (4*x) % d == 0]
    assert quarter_kernel == [0]
    inverse_four = 0 if d == 1 else pow(4,-1,d)
    assert (4*inverse_four-1) % d == 0

    if d == 1:
        rows.append({'d':d,'canonical_p':actual_p,'H2_rank':0,
                     'H3_rank':0,'H3_torsion_order':1,
                     'mod_two_kernel':mod_two_kernel,'mod_two_cokernel_order':1,
                     'quarter_kernel':quarter_kernel,'mu_order':1,
                     'finite_basis_and_cubic':'zero coefficient ring; no KI invocation'})
        continue

    rank = d-1
    cyclic = s.zeros(d)
    for i in range(d):
        cyclic[i,i] = -2
        cyclic[i,(i-1)%d] = 1
        cyclic[i,(i+1)%d] = 1
    reduced = cyclic[:rank,:rank]
    S = s.eye(rank).col_join(-s.ones(1,rank))
    assert S*reduced*S.T == cyclic
    square_values = S*(-12*s.ones(rank,1))
    assert all((int(value)+12) % d == 0 for value in square_values)
    assert cyclic*s.ones(d,1) == s.zeros(d,1)

    # Tensor enumeration is separate from expanding the closed formula.
    # Index 0 means u; indices 1,...,rank mean x_0,...,x_(rank-1).
    actual = Counter()
    for triple in product(range(rank+1),repeat=3):
        count_u = triple.count(0)
        if count_u == 1:
            free = [j-1 for j in triple if j]
            value = int(reduced[free[0],free[1]])
        elif count_u == 2:
            value = -12
        else:
            value = 0
        if value:
            actual[tuple(sorted(triple))] += value
    expected = Counter()
    for i in range(rank):
        expected[(0,0,i+1)] = -36
        expected[(0,i+1,i+1)] = -6
    for i in range(rank-1):
        expected[(0,i+1,i+2)] = 6
    assert actual == expected

    mu_coefficients = [int(reduced[i,j]) for i in range(rank)
                       for j in range(i,rank)] + [-12]*rank + [0]
    order = lcm(*(d//gcd(d,a) for a in mu_coefficients))
    assert order == d
    assert len(mu_coefficients) == rank*(rank+1)//2+rank+1
    rows.append({'d':d,'canonical_p':actual_p,'H2_rank':rank,
                 'H3_rank':0,'H3_torsion_order':d,
                 'mod_two_kernel':mod_two_kernel,'mod_two_cokernel_order':1,
                 'quarter_kernel':quarter_kernel,'inverse_four':inverse_four,
                 'full_pairing_reconstruction':'exact integer equality',
                 'square_value_reconstruction':'all entries -12 modulo d',
                 'ordered_triples_checked':(rank+1)**3,
                 'nonzero_integral_polynomial_terms':len(actual),
                 'full_mu_torsion_coordinates':len(mu_coefficients),
                 'mu_order':order})

out={'method':'Explicit cyclic homomorphisms, actual parameter substitution, '
              'integer relation matrix, and ordered-triple enumeration',
     'rows':rows,
     'scope':'Arithmetic validation only; external classification theorems are '
             'used at their stated maps, not computationally reproved.',
     'status':'all exact assertions passed'}
path=Path(__file__).with_suffix('.json')
with path.open('w',encoding='utf-8',newline='\n') as f:
    json.dump(out,f,ensure_ascii=False,indent=2)
    f.write('\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
