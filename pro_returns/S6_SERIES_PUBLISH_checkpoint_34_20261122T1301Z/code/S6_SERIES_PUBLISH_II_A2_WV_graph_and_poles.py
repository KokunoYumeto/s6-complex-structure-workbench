"""Exact bounded algebra for the pre-release WV derivation.

This verifies Euler/presentation counts and both blowup-chart pole identities.
It does not certify GSS classification, conductor duality, or van Kampen.
"""
import json
import sympy as S

c,s,b,r,t,q,N,g,R,n = S.symbols('c s b r t q N g R n', integer=True)
# A rational curve normalization has c spheres. There are t singular points
# and q inverse-image points. Its incidence graph has c+t vertices and q edges.
graph_rank = q-c-t+s
euler_by_gluing = 2*c-(q-t)
euler_by_graph = c+s-graph_rank
assert S.expand(euler_by_gluing-euler_by_graph)==0
pushout_graph_rank = r-s  # r edges and 1+s vertices, connected.
generators = 1+b+pushout_graph_rank
relators = r           # one actual relation from each cyclic D component.
deficiency = S.expand(generators-relators)
assert deficiency == 1+b-s
cover_generators = N*g-(N-1)
cover_relators = N*R
cover_deficiency = S.expand(cover_generators-cover_relators)
assert S.expand(cover_deficiency-(N*(g-R-1)+1))==0
cover_from_WV = S.expand((N*(g-R-1)+1).subs({g:generators,R:relators}))
assert cover_from_WV == N*b-N*s+1
free_abelian_bound = q-q*(q-1)/2
assert S.factor(1-free_abelian_bound)==(q-2)*(q-1)/2
tail = S.factor((1-free_abelian_bound).subs(q,n+2))
assert tail==n*(n+1)/2
rank_endpoints = {str(i):str(free_abelian_bound.subs(q,i)) for i in (0,1,2)}

# Incidence-rank changes when a leaf is appended or an edge is subdivided.
vertices,edges,components=S.symbols('vertices edges components',integer=True)
b1=edges-vertices+components
assert S.expand(b1.subs({vertices:vertices+1,edges:edges+1}, simultaneous=True)-b1)==0

# Exact Jacobian pullbacks of a meromorphic two-form. Smooth conductor y=0;
# nodal conductor xy=0. In both blowup charts, record exceptional poles.
u,v=S.symbols('u v')
charts=[('x=u,y=u*v',u,u*v,u),('x=u*v,y=v',u*v,v,v)]
chart_results=[]
for label,x,y,exceptional in charts:
    jac=S.Matrix([x,y]).jacobian([u,v]).det()
    smooth=S.cancel(jac/y)
    node=S.cancel(jac/(x*y))
    assert S.cancel(node-1/(u*v))==0
    expected_smooth=1/v if label=='x=u,y=u*v' else 1
    assert S.cancel(smooth-expected_smooth)==0
    chart_results.append({'chart':label,'jacobian':str(jac),
        'smooth_pole_form_coefficient':str(smooth),
        'node_pole_form_coefficient':str(node),
        'exceptional_equation':str(exceptional),
        'smooth_exceptional_pole_order':0,'node_exceptional_pole_order':1})

# Exact conductor ring for two branches: (f(x),g(y)) with f(0)=g(0).
# Truncation records a finite-degree diagnostic; the formal proof is in the
# derivation and does not infer the infinite ring statement from this sample.
degree=6
monomials=[S.Integer(1)]+[u**j for j in range(1,degree+1)]+[v**j for j in range(1,degree+1)]
image=[(S.expand(m.subs(v,0)),S.expand(m.subs(u,0))) for m in monomials]
assert image[0]==(1,1)
for j in range(1,degree+1):
    assert image[j]==(u**j,0)
    assert image[degree+j]==(0,v**j)

result={
 'scope':'Exact symbolic counting identities and local pole pullbacks; finite-degree ring diagnostic only. No complete geometric certificate.',
 'rational_image_curve':{'incidence_b1':str(graph_rank),'euler_by_normalization':str(euler_by_gluing),
     'euler_by_graph':str(euler_by_graph),'identity_residual':'0'},
 'conductor_pushout':{'central_vertex_group_generators':1,'image_vertex_generators':'b',
     'stable_letters':str(pushout_graph_rank),'generators':str(generators),
     'relators':str(relators),'deficiency':str(deficiency)},
 'finite_cover_presentation':{'generators':str(cover_generators),'relators':str(cover_relators),
     'deficiency':str(cover_deficiency),'WV_substitution':str(cover_from_WV)},
 'free_abelian_bound':{'rank_q_bound':str(free_abelian_bound),'one_minus_bound':str(S.factor(1-free_abelian_bound)),
     'ranks_0_1_2':rank_endpoints,'q_equals_n_plus_2_tail_nonnegative':str(tail),
     'deduction':'For N>0, N*(b-s)+1<=1 gives b<=s. Thus e(C)=c+s-b>=c>0.'},
 'cycle_operations':{'leaf_or_edge_subdivision_delta_b1':'0','smooth_coefficient_one_blowup_adds_no_conductor_component':True},
 'blowup_poles':chart_results,
 'node_ring_finite_diagnostic':{'degree':degree,'basis_dimension':len(monomials),
     'basis_maps':[[str(a),str(z)] for a,z in image],
     'scope_limit':'Only this finite truncation is computed; all convergent power-series tuples with a common constant are treated in the written proof.'}}
print(json.dumps(result,indent=2))
