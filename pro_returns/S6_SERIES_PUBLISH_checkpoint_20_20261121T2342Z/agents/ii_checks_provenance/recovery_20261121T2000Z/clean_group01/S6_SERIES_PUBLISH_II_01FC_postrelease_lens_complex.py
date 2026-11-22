"""Postrelease integral cellular check for the exact quotient Y_m.

The equivariant norm-one slice identifies Y_m with S^3 x L(m,1).
The nonminimal lens complex makes the two torsion entries explicit.
This supplements the printed transfer/UCT argument after proof release.
"""
import json
import sympy as s
m=s.symbols('m',integer=True,positive=True)
# S^3 has generators in dimensions 0 and 3. L(m,1) has one generator in
# dimensions 0,1,2,3, with sole nonzero boundary C2 -> C1 equal to m.
basis={n:[(i,j) for i in [0,3] for j in range(4) if i+j==n] for n in range(7)}
D={}
for n in range(1,7):
    matrix=s.zeros(len(basis[n-1]),len(basis[n]))
    for col,(i,j) in enumerate(basis[n]):
        if j==2:
            matrix[basis[n-1].index((i,1)),col]=(-1)**i*m
    D[n]=matrix
for n in range(2,7):
    assert D[n-1]*D[n]==s.zeros(len(basis[n-2]),len(basis[n]))
assert D[2]==s.Matrix([[m]]) and D[5]==s.Matrix([[-m]])
assert all(D[n].is_zero_matrix for n in [1,3,4,6])
ranks={n:(1 if n in [2,5] else 0) for n in range(1,7)}
betti=[len(basis[n])-ranks.get(n,0)-ranks.get(n+1,0) for n in range(7)]
assert betti==[1,0,0,2,0,0,1]
assert sum((-1)**n*b for n,b in enumerate(betti))==0
# In cohomological degree two, the outgoing differential is zero and the
# incoming one is [m], so H^2 is the actual quotient Z/mZ for every m>1.
assert D[3].T.is_zero_matrix and D[2].T==s.Matrix([[m]])
print(json.dumps({'timing':'after 01FC target proof release',
 'geometric_map':'unique norm-one slice is mu_m-equivariant, giving Y_m diffeomorphic to S3 times L(m,1)',
 'coefficient_scope':'all integers m>1; no inference from sampled m',
 'chain_dimensions':[len(basis[n]) for n in range(7)],
 'boundaries':{str(n):str(D[n]) for n in range(1,7)},
 'rational_betti_numbers':betti,'euler':0,
 'integral_H1':'Z/mZ','integral_H2':'0','integral_H2_cohomology':'Z/mZ',
 'cohomology_quotient_map':'Z --multiplication by m--> Z in cochain degrees 1 to 2',
 'new_independent_event_count':0,'all_assertions_passed':True},indent=2))
