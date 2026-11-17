#!/usr/bin/env python3
"""Exact P4R.20 spectral, ring, and incidence certificates."""
from pathlib import Path
import itertools
import json
import sympy as S

t, b = S.symbols('t b', integer=True)
def intersection(D,E):
    a,c = D
    aa,cc = E
    return S.expand(2*a*aa+a*cc+aa*c)
DH,DR,K = (2,t-b),(1,-t),(-2,0)
pa = S.simplify(1+(intersection(DH,DH)+intersection(DH,K))/2)
n = intersection(DH,DR)
assert pa == 1+t-b
assert n == 4-t-b
assert S.simplify(pa+n-(5-2*b)) == 0

u,v,z,w,a,r1,r2 = S.symbols('u v z w a r1 r2')
fH = v*v+u*u*(z+a*u)
normalization_remainder = S.expand(fH.subs({v:u*w,z:-w*w-a*u}))
assert normalization_remainder == 0
gb = S.groebner([u,v*v,z],u,v,z)
assert [str(p.as_expr()) for p in gb.polys] == ['u','v**2','z']
ribbon_basis = ['1','v']
eps = S.symbols('eps')
alpha,beta,gamma,delta = S.symbols('alpha beta gamma delta')
f = u*fH*(z+alpha*u+beta*v)*(z+gamma*u+delta*v)
cubic = S.expand(f.subs({u:eps*u,v:eps*v})).coeff(eps,3)
assert S.expand(cubic-z*z*u*(v*v+u*u*z)) == 0

degree_lists=[]
for c in range(2,4):
    for ds in itertools.product(range(1,4),repeat=c):
        if sum(ds)==3 and ds[0]==ds[-1]==1:
            degree_lists.append(list(ds))
assert degree_lists == [[1,1,1]]

pp,pm = S.symbols('p_plus p_minus')
cplus = [4,2+pp,2+pp]
cminus = [1+pm,1+pm,2]
equalities = [S.expand(x-y) for x,y in zip(cplus,cminus)]
solutions = S.solve(equalities,[pp,pm],dict=True)
assert solutions == []

result = {
 'statement':'P4R.20',
 'scope':'One three-branch image point; generic B has at least three normalization branches',
 'spectral_genus':str(pa),
 'spectral_intersection':str(n),
 'genus_plus_intersection':str(S.expand(pa+n)),
 'ribbon_groebner_basis':[str(p.as_expr()) for p in gb.polys],
 'ribbon_standard_monomials':ribbon_basis,
 'actual_normalization_equation_remainder':str(normalization_remainder),
 'normal_cubic_example_identity':str(S.factor(cubic)),
 'endpoint_degree_lists_with_total_three':degree_lists,
 'factor_marking_at_B_plus':['H=W1','f1=W2','f2=W3'],
 'factor_marking_at_B_minus':['f1=W1','f2=W2','R=W3'],
 'conductor_vector_B_plus':[str(x) for x in cplus],
 'conductor_vector_B_minus':[str(x) for x in cminus],
 'conductor_equality_equations':[str(x) for x in equalities],
 'solutions':solutions,
 'proof_note':'The graph bounds, local factorization, divisor orders, and global conductor constancy are proved in notes/part4_degree_two_triple_point.md and .tex; this certificate verifies their exact algebra and finite incidence conclusion.',
}
dest=Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(result,indent=2)+'\n')
print('PASS: spectral genus/intersection, length-two ribbon, normalization map, cubic scalar, endpoint degrees, and conductor mismatch.')
print(dest)
