"""Exact branch-index complexes and universal Euler relations, before proof release."""
from itertools import combinations
import sympy as s
import json

complexes=[]
for r in (1,2,3):
    bases=[list(combinations(range(r),k)) for k in range(1,r+1)]
    maps=[]
    for k in range(len(bases)-1):
        M=s.zeros(len(bases[k+1]),len(bases[k]))
        for row,J in enumerate(bases[k+1]):
            for q in range(len(J)):
                I=J[:q]+J[q+1:]
                M[row,bases[k].index(I)]=(-1)**q
        maps.append(M)
    for k in range(len(maps)-1):
        assert maps[k+1]*maps[k]==s.zeros(maps[k+1].rows,maps[k].cols)
    ranks=[m.rank() for m in maps]
    dims=[len(b) for b in bases]
    cohom=[dims[k]-(ranks[k-1] if k else 0)-(ranks[k] if k<len(ranks) else 0) for k in range(len(dims))]
    assert cohom==[1]+[0]*(r-1)
    complexes.append({'local_branches':r,'dimensions':dims,'ranks':ranks,'cohomology_dimensions':cohom})

tau,C,T,D,S,chi=s.symbols('tau C T D S chi')
relations=[C-3*tau,D-2*C+3*tau,S-T+C-tau,chi-C/2+tau]
sol=s.solve(relations,[C,D,S,chi],dict=True)[0]
assert sol[C]==3*tau and sol[D]==3*tau and sol[S]==T-2*tau and sol[chi]==tau/2
uniform=s.simplify(sol[S].subs(T,sol[D]));assert uniform==tau
print(json.dumps({'timing':'before target-proof release','method':'alternating branch-incidence matrices and exact universal linear relations',
                  'local_complexes':complexes,'relations_solved':{str(k):str(v) for k,v in sol.items()},
                  'uniform_multiple_euler':str(uniform),'events_added':0},indent=2))
