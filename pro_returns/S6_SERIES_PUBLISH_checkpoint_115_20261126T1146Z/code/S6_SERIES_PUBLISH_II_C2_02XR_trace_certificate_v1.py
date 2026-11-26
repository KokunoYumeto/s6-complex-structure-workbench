"""Independent exact certificate for the prereading 02XR derivation.

No target proof or historical routine is imported.  Realize A_j monodromy
as minus the cyclic permutation on an augmentation lattice, factor its
characteristic polynomial, and test all transverse Milnor budgets <= 5.
"""
from itertools import combinations_with_replacement
import json
import sympy as s

x = s.Symbol('x')

def a_matrix(j):
    # Basis e_0-e_j,...,e_(j-1)-e_j of ker(sum:Z^(j+1)->Z).
    # The cyclic shift sends e_i to e_(i+1 mod j+1).
    n = j + 1
    cols = []
    for i in range(j):
        v = [0]*n
        v[(i+1)%n] -= 1
        v[0] += 1
        assert sum(v) == 0
        cols.append(s.Matrix(v[:j]))
    return s.Matrix.hstack(*cols)

def companion(p):
    p = s.Poly(p, x).monic()
    d = p.degree()
    c = s.zeros(d)
    for i in range(d-1):
        c[i+1,i] = 1
    for i in range(d):
        c[i,d-1] = -p.nth(i)
    return c

spectra = {}
for j in range(1,6):
    a = a_matrix(j)
    p = a.charpoly(x).as_expr()
    factors = []
    for d in range(1,13):
        q = s.cyclotomic_poly(d,x)
        while s.rem(p,q,x) == 0:
            factors.append(d)
            p = s.quo(p,q,x)
    assert p == 1
    spectra[j] = factors
    print('A_%d' % j, json.dumps({'matrix':[[int(a[i,k]) for k in range(j)] for i in range(j)],
        'cyclotomic_orders':factors,'traces_1_to_4':[int(s.trace(a**r)) for r in range(1,5)]}))

trace = {d:[int(s.trace(companion(s.cyclotomic_poly(d,x))**r)) for r in range(1,5)]
         for d in (1,3,4,6,10)}
print('cyclotomic_traces',json.dumps(trace,sort_keys=True))
supports = {}
partitions = [()]
for n in range(1,6):
    for count in range(1,n+1):
        partitions.extend(t for t in combinations_with_replacement(range(1,n+1),count) if sum(t)==n)
for t in partitions:
    support = tuple(sorted({1}|{d for j in t for d in spectra[j]}))
    supports.setdefault(support,[]).append(t)
    matrix = s.Matrix([[trace[d][r] for d in support] for r in range(3)])
    assert matrix.rank() == len(support), (t,support,matrix)
for support, cases in sorted(supports.items()):
    matrix = s.Matrix([[trace[d][r] for d in support] for r in range(3)])
    print('support',support,'trace_matrix',str(matrix.tolist()),'rank',matrix.rank(),'partitions',cases)
assert len(partitions) == 19
print('PASS: all 19 partitions of transverse Milnor budget 0..5 have full-column-rank first-three-trace systems.')
print('PASS: vanishing first three virtual traces forces every virtual cyclotomic multiplicity, and hence trace four, to vanish.')
