#!/usr/bin/env python3
"""Fresh L3 profile synthesis from raw component equations only."""
from pathlib import Path
from fractions import Fraction
from math import gcd, lcm
from functools import reduce
from itertools import product, combinations
from collections import Counter
import csv
import hashlib
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / 'agents/continuation7_iii_profile_synthesis'
RAW = ROOT / 'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
raw_bytes = RAW.read_bytes()
assert hashlib.sha256(raw_bytes).hexdigest() == '6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522'
raw = json.loads(raw_bytes)
J = sp.Matrix([[0, 1], [-1, 0]])
I = sp.eye(2)
order = {'II': 6, 'III': 4, 'IV': 3, 'III*': 4, 'IV*': 3}
index = {'II': 1, 'III': 2, 'IV': 3, 'III*': 2, 'IV*': 3}

def integral(values):
    return all(sp.denom(x) == 1 for x in values)

def multiplicative(kind):
    return kind[0] == 'I' and kind[1:].isdigit()

def narrow(row, place, multiple):
    datum = row['component_coordinates'][place]
    return all((multiple * v[0]) % modulus == 0
               for v, modulus in zip(datum['rows'], datum['moduli']))

def component_order(row, place, multiple):
    datum = row['component_coordinates'][place]
    return lcm(*(modulus//gcd(modulus,multiple*v[0])
                 for v,modulus in zip(datum['rows'],datum['moduli'])))

def cyclic_delta(nu, terms):
    coefficients = [0] * nu
    for power, coefficient in terms:
        coefficients[power % nu] += coefficient
    return coefficients

def local_data(A, g, nu):
    kernel = (A-I).nullspace()
    assert len(kernel) == 1
    v = kernel[0]
    v *= lcm(*(int(sp.denom(x)) for x in v))
    v /= reduce(gcd, (abs(int(x)) for x in v))
    first = next(x for x in v if x)
    if first < 0:
        v = -v
    assert A-I == nu*v*(v.T*J)
    ix = next(i for i, x in enumerate(v) if x)
    kappa = g[ix]/v[ix]
    assert sp.denom(kappa) == 1 and g == kappa*v
    return v, int(kappa)

natural = []
patterns = []
summaries = []
for profile_number, row in enumerate(raw['rows']):
    height = Fraction(row['height_of_generator'])
    assert height.numerator == 1
    denominator = height.denominator
    matrices = [sp.Matrix(a) for a in row['elliptic_matrices']]
    cocycles = [sp.Matrix(g) for g in row['generator_section_cocycle']]
    local_rows = []
    for zero, kind in enumerate(row['fibers']):
        if not multiplicative(kind):
            continue
        nu = int(kind[1:])
        u, kappa = local_data(matrices[zero], cocycles[zero], nu)
        if denominator % nu:
            continue
        product_ab = denominator//nu
        for a in sp.divisors(product_ab):
            a = int(a)
            b = product_ab//a
            if gcd(b*kappa, nu) != 1:
                continue
            degrees = cyclic_delta(nu, [(a*kappa, 1), (0, -1),
                                        ((a-b)*kappa, -1), (-b*kappa, 1)])
            zero_components = [h for h in range(nu)
                               if degrees == cyclic_delta(nu, [(h, -2), (h-1, 1), (h+1, 1)])]
            if not zero_components:
                continue
            if any(not (narrow(row, i, a) or narrow(row, i, b))
                   for i in range(len(matrices)) if i != zero):
                continue
            assert gcd(a,b) == 1 and zero_components == [0]
            item = dict(profile_number=profile_number, OS=row['OS'], profile=row['profile'],
                        a=a, b=b, zero=zero, zero_type=kind, kappa=kappa)
            natural.append(item)
            local_rows.append(item)
    excluded_star = any(kind.startswith('I') and kind.endswith('*')
                        and kind[1:-1].isdigit() for kind in row['fibers'])
    count_before = len(patterns)
    for item in local_rows:
        if excluded_star:
            continue
        alternatives = []
        for i, kind in enumerate(row['fibers']):
            if multiplicative(kind):
                continue
            possible = []
            if kind in ('II','III','IV') and narrow(row, i, item['a']) and component_order(row,i,item['b']) == index[kind]:
                possible.append(dict(position=i, type=kind, choice='original', q=1, d=1))
            fixed_long = (matrices[i]-I).inv()*cocycles[i]*item['b']
            if integral(fixed_long):
                possible.append(dict(position=i, type=kind, choice='finite', q=index[kind], d=order[kind]))
            alternatives.append(possible)
        for choices in product(*alternatives):
            finite = [x for x in choices if x['choice'] == 'finite']
            q_product = reduce(lambda x,y:x*y,(x['q'] for x in finite),1)
            if item['b'] != q_product:
                continue
            if len(finite) > 2 or any(gcd(x['d'],y['d']) != 1 for x,y in combinations(finite,2)):
                continue
            patterns.append(dict(**item, choices=choices, finite_count=len(finite)))
    own = patterns[count_before:]
    category = 'unbounded' if any(x['finite_count'] for x in own) else ('orders_one' if own else 'none')
    summaries.append(dict(OS=row['OS'], profile=row['profile'], fibers=row['fibers'],
                          natural=len(local_rows), patterns=len(own), multiplicities=category))

distinct = {(x['OS'],x['profile'],x['a'],x['b'],x['zero']) for x in patterns}
LANE.mkdir(parents=True,exist_ok=True)
result = dict(raw_sha256=hashlib.sha256(raw_bytes).hexdigest(),natural_count=len(natural),
              pattern_count=len(patterns),distinct_initial_rows=len(distinct),
              summary=summaries,patterns=patterns)
(LANE/'S6_SERIES_PUBLISH_III_02L3_fresh_data.json').write_text(json.dumps(result,indent=2)+'\n',newline='\n')
with (LANE/'S6_SERIES_PUBLISH_III_02L3_fresh_patterns.tsv').open('w',newline='') as stream:
    writer=csv.writer(stream,delimiter='\t',lineterminator='\n')
    writer.writerow(['number','OS','profile','a','b','zero','zero_type','additive_choices'])
    for n,x in enumerate(patterns,1):
        choices=';'.join(f"{c['position']}:{c['type']}:{c['choice']}" for c in x['choices']) or 'none'
        writer.writerow([n,x['OS'],x['profile'],x['a'],x['b'],x['zero'],x['zero_type'],choices])
print('RAW_SHA256',result['raw_sha256'])
print('NATURAL',len(natural),'SPHERE_PATTERNS',len(patterns),'DISTINCT_ROWS',len(distinct))
print('PROFILE_CATEGORIES',dict(Counter(x['multiplicities'] for x in summaries)))
for x in summaries:
    print('PROFILE',x['OS'],x['profile'],','.join(x['fibers']),'natural',x['natural'],'sphere_patterns',x['patterns'],x['multiplicities'])
for n,x in enumerate(patterns,1):
    choices=';'.join(f"{c['position']}:{c['type']}:{c['choice']}" for c in x['choices']) or 'none'
    print('PATTERN',n,x['OS'],x['profile'],'a,b',x['a'],x['b'],'zero',x['zero'],'choices',choices)
print('TWO_FINITE_PATTERNS',[(x['OS'],x['profile'],x['a'],x['b'],x['zero'],[(c['type'],c['d']) for c in x['choices']]) for x in patterns if x['finite_count']==2])
print('PASS: complete raw divisor enumeration, all cyclic component positions, all additive choices and finite-order coprimality tests; zero positions are numbered from zero.')
print('No L3 original, original target program, historical sphere table or derived L1 catalogue was read.')
