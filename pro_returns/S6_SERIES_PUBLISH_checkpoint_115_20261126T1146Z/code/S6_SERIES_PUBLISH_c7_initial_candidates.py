"""Fresh finite section-pair enumeration from construction data only.

The 02KX original and all former enumeration algorithms are unopened.
This program checks the finite arithmetic/component-degree conditions;
it gives no credit for the still-needed global necessity and integral
vertical-divisor existence proofs.
"""
from collections import Counter
from fractions import Fraction
from math import gcd, lcm
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
raw = json.loads((ROOT/'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json').read_text())

def component(moduli, rows, a):
    return tuple((a*r[0]) % m for m,r in zip(moduli,rows))

def degree_difference(c, a, b):
    moduli, rows = c['moduli'], c['rows']
    answer = Counter()
    for coefficient, value in ((1,a),(-1,0),(-1,a-b),(1,-b)):
        answer[component(moduli,rows,value)] += coefficient
    return {key:value for key,value in answer.items() if value}

def node_column(n, k):
    answer = Counter()
    answer[((k-1)%n,)] += 1
    answer[(k,)] -= 2
    answer[((k+1)%n,)] += 1
    return {key:value for key,value in answer.items() if value}

def divisors(t):
    return [a for a in range(1,t+1) if t%a == 0]

natural, enlarged = [], []
for row in raw['rows']:
    h = Fraction(row['height_of_generator'])
    assert h.numerator == 1
    d = h.denominator
    fibres, components = row['fibers'], row['component_coordinates']
    assert len(fibres) == len(components)
    for i, kind in enumerate(fibres):
        match = re.fullmatch(r'I([1-9][0-9]*)',kind)
        if not match:
            continue
        n = int(match[1])
        if d%n:
            continue
        t = d//n
        for a in divisors(t):
            b = t//a
            c = components[i]
            if n == 1:
                q, p = 0,0
                assert not c['moduli']
            else:
                assert c['moduli'] == [n] and len(c['rows']) == 1
                p = component(c['moduli'],c['rows'],a)[0]
                q = component(c['moduli'],c['rows'],b)[0]
            if gcd(q,n) != 1:
                continue
            item = dict(OS=row['OS'],profile=row['profile'],zero_index=i+1,
                        zero_fibre=kind,d=d,a=a,b=b,P_component=p,Q_component=q)
            enlarged.append(item)
            residuals = [degree_difference(cj,a,b) for cj in components]
            outside_zero = all(not v for j,v in enumerate(residuals) if j != i)
            if n == 1:
                positions = [0] if not residuals[i] else []
            else:
                positions = [k for k in range(n) if residuals[i] == node_column(n,k)]
            if outside_zero:
                for k in positions:
                    natural.append(dict(item,zero_component=k))
            # The two finite congruences used by the prospective constructive
            # vertical proof are checked explicitly, not used as its substitute.
            if n > 1:
                assert (p*q-1)%n == 0,(item,p,q)
            for j,cj in enumerate(components):
                if j == i:
                    continue
                orders = [m//gcd(b*r[0],m) for m,r in zip(cj['moduli'],cj['rows'])]
                order = lcm(*orders) if orders else 1
                assert a%order == 0,(item,j,cj,order)

print('Fresh arithmetic enumeration; KX original and prior algorithms unopened.')
print('Natural literal component-degree solutions:',len(natural))
print('Enlarged height/transitive candidates:',len(enlarged))
print('OS/profile | natural | enlarged')
for row in raw['rows']:
    key = (row['OS'],row['profile'])
    nn = sum((r['OS'],r['profile']) == key for r in natural)
    ne = sum((r['OS'],r['profile']) == key for r in enlarged)
    print(*key,nn,ne,sep=' | ')
print('All enlarged candidates satisfy p*q=1 modulo the zero-fibre index;')
print('at every other component group the order of bG divides a.')
print('These congruences and counts do not yet certify global necessity or integral V existence.')
out = ROOT/'agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02KX_fresh_candidate_data.json'
out.write_text(json.dumps({'natural':natural,'enlarged':enlarged},indent=2)+'\n',newline='\n')
