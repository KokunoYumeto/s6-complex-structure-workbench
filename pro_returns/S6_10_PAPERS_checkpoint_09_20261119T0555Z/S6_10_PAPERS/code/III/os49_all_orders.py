"""Exact arbitrary-order OS49 finite-cap lattice identities (P3F.29)."""
from itertools import combinations
from pathlib import Path
from math import gcd
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form


def wedge(a, q):
    ix = list(combinations(range(4), q))
    return s.Matrix([[a.extract(i, j).det() for j in ix] for i in ix])


def contract(ell, q):
    src = list(combinations(range(4), q))
    dst = list(combinations(range(4), q - 1))
    out = s.zeros(len(dst), len(src))
    for j, ix in enumerate(src):
        for h, b in enumerate(ix):
            out[dst.index(ix[:h] + ix[h+1:]), j] += (-1)**h * ell[b]
    return out


def smith(a):
    b = smith_normal_form(a, domain=s.ZZ)
    return [abs(int(b[j, j])) for j in range(min(b.shape)) if b[j, j]]


T = s.Matrix([[1,-3,-3,-1],[0,-2,-3,-1],[0,1,1,0],[0,0,0,1]])
A = T.inv().T
n,d,k = s.symbols('n d k', integer=True)
ell = s.Matrix([n,-n,0,d])
assert A*ell == ell and A**3 == s.eye(4)
assert smith(A-s.eye(4)) == [1,1]
P = s.Matrix([[1,0,0,0],[0,0,-1,3]])
assert P*(A-s.eye(4)) == s.zeros(2,4)
assert smith(P) == [1,1]
assert P*ell == s.Matrix([n,3*d])
u2 = s.Matrix([0,-1,3,0,0,0])
v2 = s.Matrix([0,1,0,1,0,0])
phi = s.Matrix([1,0,0,0])
chi = s.Matrix([0,0,1,1])
assert wedge(T,2)*u2 == u2 and wedge(T,2)*v2 == v2
assert wedge(T,3)*phi == phi and wedge(T,3)*chi == chi
assert contract(ell,2)*u2 == s.Matrix([-3*d,0,-n,3*n])
assert contract(ell,2)*v2 == s.zeros(4,1)
inv = {1:s.Matrix([1,0,0,0]),2:u2+v2,3:phi,4:s.Matrix([1])}
coinv = {0:s.Matrix([[1]]),1:s.Matrix([[0,0,0,1]]),
         2:s.Matrix([[0,0,1,3,0,0]]),3:s.Matrix([[0,0,0,1]])}
indices = {1:3*k,2:k,3:k,4:3*k}
contractions = {}
for q in range(1,5):
    num = (coinv[q-1]*contract(ell,q)*inv[q])[0]
    assert s.expand(num - ([n,3*n,3*n,n][q-1])) == 0
    assert s.cancel(indices[q]*num/(3*k)) == n
    contractions[q] = str(num)

samples = []
for kval in range(1,9):
    m = 3*kval
    for nval in range(-m+1,m):
        if gcd(nval,m) != 1:
            continue
        for dval in range(-2,3):
            ev = ell.subs({n:nval,d:dval})
            finite = s.zeros(5,5)
            finite[:4,:4] = A-s.eye(4)
            finite[:4,4] = -ev
            finite[4,4] = m
            assert smith(finite) == [1,1,1]
            invn = pow(nval,-1,m)
            # The displayed first and third lattices satisfy their exact
            # congruences and have the stated indices.
            L1 = s.Matrix([[m,-3*dval*invn],[0,1]])
            assert abs(L1.det()) == m
            assert all(v % m == 0 for v in (s.Matrix([[nval,3*dval]])*L1))
            L3 = s.Matrix([[kval,-dval*invn],[0,1]])
            assert abs(L3.det()) == kval
            assert all(v % kval == 0 for v in (s.Matrix([[1,dval*invn]])*L3))
            samples.append([kval,nval,dval])

out = {'claim':'P3F.29','hypotheses':'k>0, m=3k, gcd(n,m)=1, d arbitrary',
       'log_vector':['n','-n',0,'d'],
       'cap_H1_presentation':['n','3*d','-m'],
       'specialization_indices':['m','k','k','m'],
       'coinvariant_contractions':contractions,
       'four_d2':['n']*4,
       'pi1':'Z/abs(n)',
       'integral_homology':['Z','Z/abs(n)','Z/abs(n)','Z/abs(n)','Z/abs(n)',0,'Z'],
       'finite_sample_count':len(samples),
       'return_index':'Unassigned; the actual mixed-circle comparison remains required.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact symbolic contractions:',contractions)
print('All four d2 are multiplication by n for arbitrary k,n,d in the stated sector.')
print('Finite cap presentation and lattice samples checked:',len(samples))
print('n=+/-1 gives the standard smooth S6 for every k and d.')
print(out['return_index'])
