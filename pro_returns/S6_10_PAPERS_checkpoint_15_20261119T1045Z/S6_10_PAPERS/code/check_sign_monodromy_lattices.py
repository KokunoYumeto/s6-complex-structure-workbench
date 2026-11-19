"""Independent exact replays of UN.11 and UN.36 finite calculations.

This checks the displayed matrices, not the analytic comparison maps.
"""
from pathlib import Path
from itertools import combinations
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
x, t = s.symbols('x t')

def companion(poly):
    p = s.Poly(poly, x)
    n = p.degree()
    a = s.zeros(n)
    for j in range(n-1):
        a[j+1,j] = 1
    for j in range(n):
        a[j,n-1] = -p.nth(j)
    return a

def exterior(a, q):
    ix = list(combinations(range(a.rows), q))
    return s.Matrix([[a.extract(i,j).det() for j in ix] for i in ix])

expected = [
    ([1,1,1,1], {}), ([1,1,2,2], {}), ([1,1,3], {}),
    ([1,1,4], {}), ([1,1,6], {}),
    ([2,2,2,2], {1:16,2:-8}), ([3,3], {1:9,3:-3}),
    ([2,2,4], {1:8,2:-4}), ([4,4], {1:4,2:6,4:-4}),
    ([5], {1:5,5:-1}), ([2,2,3], {1:12,2:-6,3:-4,6:2}),
    ([2,2,6], {1:4,2:-2,3:4,6:-2}),
    ([3,6], {1:3,2:3,3:-1,6:-1}),
    ([6,6], {1:1,2:4,3:5,6:-4}),
    ([8], {1:2,2:1,4:3,8:-2}),
    ([10], {1:1,2:2,5:3,10:-2}),
    ([3,4], {1:6,2:3,3:-2,4:-3,6:-1,12:1}),
    ([4,6], {1:2,2:5,3:2,4:-3,6:-3,12:1}),
    ([12], {1:1,3:1,4:2,6:2,12:-2}),
]
rows = []
for factors, want in expected:
    blocks = [companion(s.cyclotomic_poly(d,x)) for d in factors]
    a = s.diag(*blocks)
    assert a.shape == (4,4) and a.det() == 1
    order = int(s.ilcm(*factors)) if len(factors)>1 else factors[0]
    assert a**order == s.eye(4)
    p = a.charpoly(x).as_expr()
    traces = {k:int(s.resultant(p,1-x**k,x)) for k in range(1,2*order+3)}
    actual = {}
    for n in range(1,2*order+3):
        value = sum(s.mobius(n//d)*traces[d] for d in s.divisors(n))/n
        assert value.is_integer
        if value:
            actual[n] = int(value)
    assert actual == want, (factors, actual, want)
    zeta = s.Integer(1)
    for q in range(5):
        aq = exterior(a,q)
        zeta *= (s.eye(aq.rows)-t*aq).det()**((-1)**(q+1))
    stratum = s.prod((1-t**n)**(-v) for n,v in actual.items())
    assert s.cancel(zeta-stratum) == 0
    average = s.Rational(sum(traces[k] for k in range(1,order+1)),order)
    want_average = (0 if 1 in factors else 8 if factors==[2,2,2,2]
                    else 6 if factors in ([3,3],[4,4],[6,6]) else 4)
    assert average == want_average
    assert average == sum(actual.values())
    rows.append({'cyclotomic_factors':factors,'order':order,
                 'matrix':a.tolist(),'signature':actual,
                 'determinant_values':traces,'exterior_zeta':str(s.factor(zeta)),
                 'UN39_average':int(average),'UN39_zero_index':int(average/2)})

pairs = list(combinations(range(4),2))
def wedge_sign(i,j):
    v = list(i+j)
    if len(set(v)) < 4:
        return 0
    return (-1)**sum(v[a]>v[b] for a in range(4) for b in range(a+1,4))
q = s.Matrix([[wedge_sign(i,j) for j in pairs] for i in pairs])
assert q.det() == -1

def v(pair):
    z = s.zeros(6,1)
    z[pairs.index(pair),0] = 1
    return z

lattices = []
for rank, eps in [(0,0),(1,0),(2,1),(2,-1)]:
    n = s.zeros(4)
    if rank:
        n[0,1] = 1
    if rank==2:
        n[2,3] = eps
    u = s.eye(4)+n
    a2 = exterior(u,2)
    if rank==0:
        b = s.eye(6)
    elif rank==1:
        b = s.Matrix.hstack(v((0,1)),v((0,2)),v((0,3)),v((2,3)))
    else:
        b = s.Matrix.hstack(v((0,1)),v((2,3)),v((0,2)),v((0,3))-eps*v((1,2)))
    assert (a2-s.eye(6))*b == s.zeros(6,b.cols)
    assert b.rank() == 6-(a2-s.eye(6)).rank()
    gram = b.T*q*b
    eig = gram.eigenvals()
    inertia = [sum(mult for value,mult in eig.items() if value>0),
               sum(mult for value,mult in eig.items() if value<0),
               sum(mult for value,mult in eig.items() if value==0)]
    want = {(0,0):[3,3,0],(1,0):[1,1,2],(2,1):[1,2,1],(2,-1):[2,1,1]}[rank,eps]
    assert inertia == want
    lattices.append({'rank':rank,'epsilon':eps,'monodromy':u.tolist(),
                     'invariant_basis':b.tolist(),'gram':gram.tolist(),'inertia':inertia})

ns = s.Matrix([[0,1,1,1],[1,0,1,1],[1,1,0,3],[1,1,3,0]])
assert ns.det() == -3
out = {'date':'2026-11-18','method':'Fresh exact SymPy computation; no source checker was executed.',
       'UN11':rows,'UN36':lattices,'UN8_NS_determinant':int(ns.det()),
       'limitations':'Analytic transport, nearby-cycle comparisons and geometric occurrence are mathematical proof inputs, not certified by this script.'}
(ROOT/'analysis/sign_monodromy_lattice_replay.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps({'signature_rows':len(rows),'lattice_cases':len(lattices),'NS_determinant':int(ns.det()),'result':'PASS'}))
