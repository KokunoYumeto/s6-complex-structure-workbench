"""Exact arithmetic and normalized-cover maps for the prereading BX proof."""
import json
import sympy as s

ell, k, delta, b, q, link = s.symbols('ell k delta b q link', integer=True)
def intersect(x, y):
    return s.expand(2*x[0]*y[0]+x[0]*y[1]+x[1]*y[0])
canonical = (-2, 0)
def genus(d):
    return s.simplify(1+intersect(d,(d[0]+canonical[0],d[1]+canonical[1]))/2)
def chi(d):
    return s.simplify(1+intersect(d,(d[0]-canonical[0],d[1]-canonical[1]))/2)
section = (1, -2-ell)
double = (2, 2+ell-k)
assert genus(double) == 3+ell-k
assert intersect(section,double) == 2-ell-k
allowed = [(kk,ll) for kk in range(8) for ll in range(-12,13)
           if 3+ll-kk>=1 and 2-ll-kk>=0]
assert allowed == [(0,-2),(0,-1),(0,0),(0,1),(0,2),(1,-1),(1,0),(1,1),(2,0)]

reduced = []
for scalar_degree, components, max_delta, min_b, max_link, max_q, rank_base in [
    (0,2,4,0,2,1,1),
    (1,3,5,2,2,1,2),
    (2,4,6,4,0,0,2),
]:
    minimum_rank = 22-4*max_delta+2*min_b-max_link-components
    maximal_b1 = 2*max_q+components-rank_base
    assert minimum_rank>0 and maximal_b1<=3
    reduced.append(dict(scalar_degree=scalar_degree, components=components,
                        minimal_pairing_rank=minimum_rank, maximal_first_betti=maximal_b1))

# Double scalar zero: the normalized character algebra is O + O(-xi)
# + O(-2xi+F), hence Euler characteristic one.
character_chi = [chi((0,0)),chi((-1,0)),chi((-2,1))]
assert character_chi == [1,0,0]
a, c = s.symbols('a c')
z, t, w, v = a**3, c**3, a**2*c, a*c**2
assert s.expand(w**2-z*v) == 0
assert s.expand(w*v-z*t) == 0
assert s.expand(v**2-w*t) == 0
assert s.expand(w**3-z**2*t) == 0
# In the second equation the algebra generator r is t; the relation is
# w*v=z*t, exactly the invariant a^3*c^3.
invariant_generators = [(3,0),(2,1),(1,2),(0,3)]
assert all((i+j)%3==0 for i,j in invariant_generators)
u, h = s.symbols('u h')
assert s.expand((u*h)**2*((u*h)-u**2) - u**3*h**2*(h-u)) == 0

# Resolution of the tangency normalization: one (-3) central curve and
# three (-2) leaves; it is a connected rational tree.
matrix=s.Matrix([[-3,1,1,1],[1,-2,0,0],[1,0,-2,0],[1,0,0,-2]])
principal=[int(matrix[:i,:i].det()) for i in range(1,5)]
assert all((-1)**i*principal[i-1]>0 for i in range(1,5))
Z=s.ones(4,1)
K=s.Matrix([1,0,0,0])
assert 1+(Z.dot(matrix*Z)+Z.dot(K))/2 == 0
double_zero_cases=[]
for branch_surplus, exceptional_components in [(3,3),(2,5)]:
    eU=3*branch_surplus
    b1_boundary=branch_surplus
    minimum_rank=eU-1-b1_boundary
    assert minimum_rank in (5,3)
    double_zero_cases.append(dict(branch_surplus=branch_surplus,
                                 exceptional_components=exceptional_components,
                                 eU=eU,b1_boundary=b1_boundary,
                                 minimum_pairing_rank=minimum_rank,maximal_first_betti=1))
print(json.dumps(dict(status='PASS',allowed_scalar_and_section_degrees=allowed,
                      double_arithmetic_genus=str(genus(double)),
                      section_double_intersection=str(intersect(section,double)),
                      reduced_cases=reduced,normalized_character_chi=[int(x) for x in character_chi],
                      node_normalization=dict(z='a^3',r='c^3',w='a^2*c',v='a*c^2',group='diagonal mu3'),
                      tangency_blowup_identity='z=u*h, w=u*W gives W^3=h^2*(h-u)',
                      tangency_exceptional_matrix=[list(matrix.row(i)) for i in range(4)],
                      negative_definiteness_principal_minors=principal,
                      double_zero_cases=double_zero_cases,
                      scope='Exact algebra and numerical bounds; analytic maps, cohomology and boundary topology are proved in the prereading derivation.'),
                     indent=2,default=int))
