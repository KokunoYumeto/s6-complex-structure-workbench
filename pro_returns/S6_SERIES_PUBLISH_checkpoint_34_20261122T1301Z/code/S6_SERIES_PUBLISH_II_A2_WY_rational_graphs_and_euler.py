"""Exact bounded computations for the statement-first 02WY derivation.

The rational configurations are specified by their normalization components
and the complete inverse-image sets of singular points.  Graph Betti numbers
are computed from incidence matrices, independently of the symbolic count
used in the preceding WV check.  The geometric exhaustiveness is proved in
the derivation; this program does not infer classification from a sample.
"""
import json
import sympy as S

n, a, b, v = S.symbols('n a b v', integer=True)
M = S.Matrix([[n, 1], [1, 0]])
h, F = S.Matrix([1, 0]), S.Matrix([0, 1])
K = -2*h + (n-2)*F
D = -K
pair = lambda x, y: S.expand((x.T*M*y)[0])
H = D-v*F
pa = S.expand(1+pair(H,H+K)/2)
assert pair(D,F) == 2
assert pa == 1-v
H1,H2 = h+a*F,h+b*F
d = pair(H1,H2)
vertical = S.expand(2-n-a-b)
assert S.expand(d+vertical)==2
assert S.expand(pair(K+H1,H1)) == -2

def curve_graph(name, genera, singular_inverse_images, expected_graph_rank):
    # Every occurrence of a component index is a separate normalization
    # point; [0,0] is a self-node, while [0] is a unibranch singularity.
    c,t=len(genera),len(singular_inverse_images)
    edges=[(i,c+j) for j,branches in enumerate(singular_inverse_images)
           for i in branches]
    boundary=S.zeros(c+t,len(edges))
    for k,(i,j) in enumerate(edges):
        boundary[i,k]=-1
        boundary[j,k]=1
    rank=boundary.rank()
    connected_components=c+t-rank
    b1=len(edges)-rank
    assert connected_components==1
    assert b1==expected_graph_rank,(name,b1)
    euler=sum(2-2*g for g in genera)-sum(len(p)-1 for p in singular_inverse_images)
    assert euler==c+1-b1-2*sum(genera)
    return {'name':name,'normalization_genera':genera,
            'singular_point_branch_components':singular_inverse_images,
            'incidence_matrix_rank':rank,'graph_b1':b1,
            'connected_components':connected_components,'support_euler':euler}

cases=[
 ('smooth elliptic cubic or bisection',[1],[],0),
 ('nodal rational cubic or bisection',[0],[[0,0]],1),
 ('cuspidal rational cubic or bisection',[0],[[0]],0),
 ('line and conic, two transverse points',[0,0],[[0,1],[0,1]],1),
 ('line and conic, one tangent point',[0,0],[[0,1]],0),
 ('three lines in a triangle',[0,0,0],[[0,1],[1,2],[2,0]],1),
 ('three concurrent lines',[0,0,0],[[0,1,2]],0),
 ('double line plus another line',[0,0],[[0,1]],0),
 ('triple line',[0],[],0),
 ('two sections, intersection number two, distinct points',[0,0],[[0,1],[0,1]],1),
 ('two tangent sections',[0,0],[[0,1]],0),
 ('two sections meeting once and a fibre elsewhere',[0,0,0],[[0,1],[0,2],[1,2]],1),
 ('two sections and a fibre concurrent',[0,0,0],[[0,1,2]],0),
 ('disjoint sections and two distinct fibres',[0,0,0,0],[[0,2],[1,2],[0,3],[1,3]],1),
 ('disjoint sections and a doubled fibre',[0,0,0],[[0,2],[1,2]],0),
 ('smooth rational bisection and transverse fibre',[0,0],[[0,1],[0,1]],1),
 ('smooth rational bisection and tangent fibre',[0,0],[[0,1]],0),
]
graphs=[curve_graph(*case) for case in cases]
for leaf_count in (0,1,2,5):
    graphs.append(curve_graph('double section with %d fibre supports'%leaf_count,
                             [0]*(1+leaf_count),[[0,j+1] for j in range(leaf_count)],0))

# Universal Euler and characteristic-class identities.
z, c1, c2, normal = S.symbols('z c1 c2 normal')
chern = S.Poly((1+c1*z+c2*z**2)*(1+normal*z),z)
assert chern.coeff_monomial(z)==c1+normal
assert chern.coeff_monomial(z**2)==c2+c1*normal
b3,q,N,g,R=S.symbols('b3 q N g R',integer=True)
betti=[1,0,0,b3,0,0,1]
euler=sum((-1)**i*x for i,x in enumerate(betti))
assert euler==2-b3
qk=S.symbols('qk',integer=True,nonnegative=True)
parity=S.expand(euler.subs(b3,2*qk))
assert parity==2-2*qk

# Reidemeister-Schreier cell counts and the H_2 bound, by Euler numbers.
cover_chi=N*(1-g+R)
cover_def=S.expand(1-cover_chi)
assert cover_def==N*g-N*R-N+1
abelian_bound=S.expand(q-S.binomial(q,2).expand(func=True))
assert S.factor(1-abelian_bound)==(q-1)*(q-2)/2

result={
 'scope':'Exact symbolic ruled-surface intersection and Chern/Euler identities; complete incidence matrices for the listed rational configurations. Exhaustiveness and topology are proved in the derivation.',
 'hirzebruch_intersections':{'basis':['h','F'],'matrix':[[str(x) for x in row] for row in M.tolist()],
    'K_coordinates':[str(x) for x in K],'D_dot_F':str(pair(D,F)),
    'bisection_arithmetic_genus':str(pa),'two_section_intersection':str(d),
    'vertical_coefficient_sum':str(vertical),'intersection_plus_vertical_sum':'2'},
 'rational_configuration_graphs':graphs,
 'smooth_support_tangent_sequence':{'first_chern_equation':str(chern.coeff_monomial(z)),
    'second_chern_equation':str(chern.coeff_monomial(z**2)),
    'ambient_and_normal_rational_classes_zero_imply_c2_zero':True},
 'six_manifold_euler':{'betti_vector':[str(x) for x in betti],
    'euler':str(euler),'b3_even_substitution':str(parity),
    'nonnegative_values_with_b3_nonnegative_even':[2,0]},
 'virtually_abelian_bound':{'cover_cell_euler':str(cover_chi),
    'cover_deficiency':str(cover_def),'free_abelian_bound':str(abelian_bound),
    'one_minus_bound':str(S.factor(1-abelian_bound))},
 'no_whole_theorem_certificate':True}
print(json.dumps(result,indent=2))
