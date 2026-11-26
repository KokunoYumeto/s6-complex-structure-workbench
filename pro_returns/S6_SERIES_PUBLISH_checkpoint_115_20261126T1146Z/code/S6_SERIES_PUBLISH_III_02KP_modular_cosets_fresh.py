#!/usr/bin/env python3
"""New exact modular coset and generator witnesses for OS56/II.

The subgroup inputs are the four bare 2x2 matrices, not filled topology.
The positive loops around j=0,1,infinity act projectively as r,s,T,
where r=(S T)^-1, s=S and r s T=1.
"""
from datetime import datetime, timezone
from itertools import product
import json
from pathlib import Path
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup, coset_enumeration_r

ROOT = Path(__file__).resolve().parents[1]


def mul(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def inv(a):
    assert a[0]*a[3]-a[1]*a[2] == 1
    return (a[3], -a[1], -a[2], a[0])


def power(a, n):
    if n < 0:
        return power(inv(a), -n)
    out = (1,0,0,1)
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n >>= 1
    return out


def project(a):
    return tuple(-x for x in a) if next(x for x in a if x) < 0 else a


S = (0,-1,1,0)
T = (1,1,0,1)
R = inv(mul(S,T))
identity = (1,0,0,1)
As = [(5,8,-2,-3),(27,37,-19,-26),(61,80,-45,-59),(4,3,-3,-2)]
assert mul(mul(mul(As[0],As[1]),As[2]),As[3]) == identity
assert power(As[1],3) == (-1,0,0,-1)
F,s,r = free_group('s,r')
t = s*r**-1
modular = FpGroup(F,[s**2,r**3])


def as_word(a):
    current = a
    word = F.identity
    factors = []
    while current[2]:
        q = current[0]//current[2]
        factors.append(('T',q))
        factors.append(('S',-1))
        word *= t**q*s
        current = mul(S,mul(power(T,-q),current))
    assert abs(current[0]) == abs(current[3]) == 1
    q = current[1]*current[0]
    word *= t**q
    factors.append(('T',q))
    check = identity
    for name,n in factors:
        check = mul(check,power(T if name == 'T' else S,n))
    assert project(check) == project(a)
    return word,factors


subwords = [as_word(a)[0] for a in As]
cosets = coset_enumeration_r(modular,subwords,max_cosets=10000)
cosets.compress()
cosets.standardize()
table = cosets.table
assert len(table) == 10 and all(x is not None for row in table for x in row)
alphabet = list(cosets.A)
generator_mats = {s:S,s**-1:inv(S),r:R,r**-1:inv(R)}
assert len(alphabet) == 4
column = {x:i for i,x in enumerate(alphabet)}
reps = {0:(identity,[])}
queue = [0]
while queue:
    i = queue.pop(0)
    matrix,word = reps[i]
    for g in (s,r):
        j = table[i][column[g]]
        if j not in reps:
            reps[j] = (mul(matrix,generator_mats[g]),word+[str(g)])
            queue.append(j)
assert len(reps) == 10

# A right coset edge from H u to H v gives u g v^-1 in H.
schreier = []
for i in range(10):
    for g in (s,r):
        j = table[i][column[g]]
        h = project(mul(mul(reps[i][0],generator_mats[g]),inv(reps[j][0])))
        schreier.append((i,str(g),j,h))

# Independent exact membership witnesses, by meet in the middle in A1..A4.
gens = [(a,[i+1]) for i,a in enumerate(As)]
gens += [(inv(a),[-(i+1)]) for i,a in enumerate(As)]
words = {identity:[]}
frontier = [identity]
for depth in range(1,6):
    nxt = []
    for a in frontier:
        old = words[a]
        for g,w in gens:
            if old and old[-1] == -w[0]:
                continue
            b = project(mul(a,g))
            if b not in words:
                words[b] = old+w
                nxt.append(b)
    frontier = nxt
    unresolved = []
    witnesses = []
    for i,g,j,h in schreier:
        if h in words:
            answer = words[h]
        else:
            answer = None
            for a,w in words.items():
                b = project(mul(inv(a),h))
                if b in words:
                    answer = w+words[b]
                    break
        if answer is None:
            unresolved.append(h)
            continue
        check = identity
        for letter in answer:
            check = mul(check,power(As[abs(letter)-1],1 if letter>0 else -1))
        assert project(check) == h
        witnesses.append(dict(source=i,generator=g,target=j,matrix=h,
                              word_in_A=answer))
    if not unresolved:
        break
assert not unresolved, unresolved


def cycle_list(perm):
    todo = set(range(len(perm)))
    out = []
    while todo:
        x = min(todo)
        cycle = []
        while x in todo:
            todo.remove(x)
            cycle.append(x)
            x = perm[x]
        out.append(cycle)
    return out


ps = [row[column[s]] for row in table]
pr = [row[column[r]] for row in table]
pt = [table[table[i][column[s]]][column[r**-1]] for i in range(10)]
assert sorted(map(len,cycle_list(pr))) == [1,3,3,3]
assert sorted(map(len,cycle_list(ps))) == [2,2,2,2,2]
assert sorted(map(len,cycle_list(pt))) == [2,3,5]
data = dict(conventions='right cosets H u; right generator action; matrices act on columns',
            matrices=As,subgroup_words=[str(w) for w in subwords],
            alphabet=[str(x) for x in alphabet],table=table,
            representatives=[dict(coset=i,matrix=reps[i][0],word=reps[i][1])
                             for i in range(10)],
            schreier_membership_witnesses=witnesses,
            r_cycles=cycle_list(pr),s_cycles=cycle_list(ps),T_cycles=cycle_list(pt))
outpath=ROOT/'agents/continuation6_iii_infra/S6_SERIES_PUBLISH_III_02KP_modular_maps.json'
outpath.write_text(json.dumps(data,indent=2)+'\n',newline='\n')
print('Raw product is I; A_II^3=-I.')
print('Projective subgroup index:',len(table))
print('All twenty Schreier edge matrices expressed in A1..A4; maximum word length:',
      max(len(w['word_in_A']) for w in witnesses))
print('Positive j=0 cycles:',data['r_cycles'])
print('Positive j=1 cycles:',data['s_cycles'])
print('Positive j=infinity cycles:',data['T_cycles'])
print('Exact maps:',outpath.relative_to(ROOT))
print('Completed:',datetime.now(timezone.utc).isoformat())
