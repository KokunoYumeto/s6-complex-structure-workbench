"""Exact intersection-ring calculation for the statement-first BW derivation.

This is a new calculation before opening the target proof. It verifies the
displayed numerical identities; the geometric and topological arguments are
proved in the separately frozen derivation.
"""
import json
import sympy as s

def pair(x, y):
    return s.expand(2*x[0]*y[0] + x[0]*y[1] + x[1]*y[0])

K=(-2,0)
def chi(x):
    return s.simplify(1+pair(x,(x[0]-K[0],x[1]-K[1]))/2)
def pa(x):
    return s.simplify(1+pair(x,(x[0]+K[0],x[1]+K[1]))/2)

k,ell,c,g,d,b,L,n,q=s.symbols('k ell c g d b L n q',integer=True)
character_chi=[chi((0,0)),chi((-1,0)),chi((-2,0))]
assert character_chi==[1,0,1]
assert pa((3,-k))==4-2*k
assert pa((2,2+ell-k))==3+ell-k
assert pair((1,-2-ell),(2,2+ell-k))==2-ell-k
assert pair((1,0),(1,0))*3==6

# e(D)=2c-2g-b, and delta=3+c-g for p_a(D)=4.
eD=2*c-2*g-b
eX=3*4-2*eD
eResolution=eX+n-L
b2Resolution=eResolution-2+4*q
rankLower=s.expand((b2Resolution-n-c).subs(g,3+c-d))
assert rankLower==22-4*d+2*b-L-c+4*q

worst=[]
for components in (1,2):
    for delta in range(5):
        bound=int(rankLower.subs({c:components,d:delta,b:0,L:2,q:0}))
        assert bound>0
        worst.append(dict(branch_components=components,total_delta=delta,
                          certified_lower_bound=bound))

print(json.dumps(dict(
    intersection_ring='xi^2=2, xi.F=1, F^2=0, K=-2xi',
    cyclic_character_Euler_characteristics=[int(x) for x in character_chi],
    cubic_horizontal_arithmetic_genus=str(pa((3,-k))),
    double_horizontal_arithmetic_genus=str(pa((2,2+ell-k))),
    section_double_intersection=str(pair((1,-2-ell),(2,2+ell-k))),
    square_of_pulled_back_xi=6,
    nondegenerate_core_rank_lower_bound=str(rankLower),
    reduced_cubic_cases=worst,
    first_Betti_bound='2q+c-1 <= c+1 <= 3 for c<=2',
    scope='Exact numerical identities only; no target proof read or geometric assertion inferred from code.'
),indent=2))
