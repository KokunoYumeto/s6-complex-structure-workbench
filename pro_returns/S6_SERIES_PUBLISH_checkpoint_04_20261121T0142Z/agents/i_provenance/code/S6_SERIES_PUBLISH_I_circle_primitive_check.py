from sympy import Matrix,eye,zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
import pathlib,json
A1=Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
M0=Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
v1=Matrix([1,2,-4,0]);v2=Matrix([-1,-3,3,0]);e=eye(4)
def ser(m):return [[str(x) for x in list(m.row(i))] for i in range(m.rows)]
k=Matrix.vstack(A1-e,A2-e);kt=Matrix.vstack((A1-e).T,(A2-e).T)
van=(M0-e).columnspace();basis=Matrix.hstack(*van)
closure=Matrix.hstack(basis,A1*basis,A2*basis)
L=e[:,1:4]
assert all(x[0]==0 for x in closure.columnspace())
assert closure.rank()==3
out={'A1_power3_identity':A1**3==e,'A2_power4_identity':A2**4==e,'common_invariant_vector_basis':[ser(x) for x in k.nullspace()],'common_invariant_covector_basis':[ser(x) for x in kt.nullspace()],'cusp_vanishing_image_basis':[ser(x) for x in van],'invariant_closure_generators':ser(closure),'closure_smith':ser(smith_normal_form(closure,domain=ZZ)),'closure_rank':closure.rank(),'primitive_L_basis':ser(L),'gamma_L_zero':all(x==0 for x in L.row(0)),'finite_norms':[]}
for A,v,m in [(A1,v1,3),(A2,v2,4)]:
 N=sum((A**i for i in range(m)),zeros(4));assert all((x/m).q==1 for x in N*v)
 out['finite_norms'].append({'m':m,'gamma_v':str(v[0]),'N_v_over_m':ser(N*v/m),'intermediate_gamma_translations':[str(v[0]*i/m) for i in range(1,m)]})
p=pathlib.Path('/workspace/scratch/653608133b22/work/agents/i_provenance/S6_SERIES_PUBLISH_I_circle_primitive_check.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
