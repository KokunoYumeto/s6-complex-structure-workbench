"""Post-release algebra for the retained original six-item WV proof.

The local edge identity gives the cycle Laplacian kernel. Finite matrices
include the nodal one-component and two-component/two-intersection cases.
The Chern calculation is a symbolic truncated product, not a numerical test.
"""
import json
import sympy as S

x,e,h,n,k = S.symbols('x e h n k')
total = S.expand((1+x*h+e*h*h)*(1-x*h))
c1 = total.coeff(h,1)
c2 = total.coeff(h,2)
assert c1==0 and S.expand(c2-(e-x*x))==0
class_vii = S.expand(c2.subs({e:n+k,x*x:-(n+k)}))
assert class_vii==2*(n+k)

a,b=S.symbols('a b')
edge_vector=S.Matrix([1,-1])
edge_quadratic=(S.Matrix([a,b]).T*(edge_vector*edge_vector.T)*S.Matrix([a,b]))[0]
assert S.expand(edge_quadratic-(a-b)**2)==0
cases=[]
for size in (1,2,3,4,7,12):
    incidence=S.zeros(size,size)
    for j in range(size):
        incidence[j,j]+=1
        incidence[(j+1)%size,j]-=1
    cycle_intersection=-(incidence*incidence.T)
    kernel=cycle_intersection.nullspace()
    assert len(kernel)==1
    assert cycle_intersection*S.ones(size,1)==S.zeros(size,1)
    assert cycle_intersection.rank()==size-1
    variables=S.Matrix(S.symbols('z:'+str(size)))
    direct=(variables.T*cycle_intersection*variables)[0]
    edge_sum=-sum((variables[j]-variables[(j+1)%size])**2 for j in range(size))
    assert S.expand(direct-edge_sum)==0
    cases.append({'components':size,'rank':cycle_intersection.rank(),
        'kernel_dimension':len(kernel),'constant_kernel':True,
        'matrix':[list(cycle_intersection.row(i)) for i in range(size)] if size<=3 else 'finite matrix checked; omitted from output',
        'quadratic_identity_residual':'0'})

# The point-identification formula in the retained connected case is a
# specialization of the pre-freeze graph calculation, independently expanded.
c,branches,singulars=S.symbols('c branches singulars',integer=True)
b_graph=branches-c-singulars+1
e_by_normalization=2*c-(branches-singulars)
assert S.expand(e_by_normalization-(c+1-b_graph))==0

# The abelianization after one relator is Z^b modulo one exponent vector.
# The rank loss is either zero or one; these representative matrices check
# the zero and nonzero cases, without claiming a complete group certificate.
abelian_diagnostics=[]
for rank in (1,2,5):
    for vector in (S.zeros(1,rank),S.Matrix(1,rank,list(range(1,rank+1)))):
        loss=vector.rank()
        assert loss in (0,1)
        assert rank-loss>=rank-1
        abelian_diagnostics.append({'generators':rank,'exponent_vector':list(vector),
            'relation_matrix_rank':loss,'abelian_quotient_rank':rank-loss})

print(json.dumps({
    'scope':'Original proof algebra after release; no independent pre-proof derivation credit for this computation.',
    'normalization_immersion':{'chern_product':str(total),'c1':str(c1),'c2':str(c2),
        'consequence_when_ambient_classes_vanish':'e=x^2=K_T^2',
        'class_VII_c2_residual':str(class_vii),
        'positivity_hypotheses':'n>0, k>=0; residual cannot vanish'},
    'parabolic_cycle_kernel':{'one_edge_identity':str(edge_quadratic),
        'general_argument':'Summing -(z_i-z_j)^2 over the cycle edges makes the real kernel constant on each connected component. A connected cycle therefore has a one-dimensional constant kernel, including a self-loop or two parallel edges.',
        'finite_matrix_diagnostics':cases},
    'connected_conductor_image':{'graph_b1':str(b_graph),'normalization_euler':str(e_by_normalization),
        'formula':'e(C)=c+1-b','identity_residual':'0'},
    'one_relator_abelianization':{'general_bound':'rank(Z^b/<exponent-vector>)>=b-1',
        'finite_matrix_diagnostics':abelian_diagnostics,
        'scope_limit':'The free-product/amalgam normal-form arguments are proved in the comparison, not certified by these matrices.'}
},indent=2,default=lambda z:int(z) if z.is_Integer else str(z)))
