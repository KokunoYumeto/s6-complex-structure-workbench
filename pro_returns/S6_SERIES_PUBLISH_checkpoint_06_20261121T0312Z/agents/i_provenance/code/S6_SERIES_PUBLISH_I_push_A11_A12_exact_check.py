from pathlib import Path
import hashlib, json, datetime
import sympy as S
from itertools import combinations
from functools import reduce
from math import gcd

B=Path('/workspace/scratch/653608133b22/work/agents/i_provenance')
M=S.Matrix.hstack(*[S.Matrix(v) for v in [(0,1,0,0),(0,-1,1,1),(1,0,0,0),(-1,0,1,0),(0,0,0,1)]])
minor_gcd=reduce(gcd,(abs(int(M[:,c].det())) for c in combinations(range(5),4)),0)
kernel=M.nullspace()[0]
kernel=[int(v*2) if v.q==2 else int(v) for v in kernel]
assert minor_gcd==1 and M*S.Matrix([1,1,-1,-1,-1])==S.zeros(4,1)
x,y,z,v,u,q,a,b,Y=S.symbols('x y z v u q a b Y')
G=S.groebner([x*y-u*q,z*v-q],x,y,z,v,u,q,order='lex')
H=S.hessian(x*y-u*z*v,(x,y,z,v))
assert S.factor(H.det())==u**2
new_a={x:a*v,y:u*Y,z:a*Y}
new_b={v:b*x,y:u*b*z}
assert S.expand((x*y-u*z*v).subs(new_a,simultaneous=True))==0
assert S.expand((x*y-u*z*v).subs(new_b,simultaneous=True))==0
upper=S.Matrix([[-1,0,1],[0,-1,1],[1,1,-1]])
lower=S.Matrix([[0,1,0],[1,0,0],[-1,-1,1]])
old1=S.Matrix([[1,0,0],[0,-1,1],[-1,1,0]])
old2=S.Matrix([[0,1,0],[-1,0,1],[1,-1,0]])
def rays(A):
 assert abs(A.det())==1
 return sorted([list(map(int,A.inv()[:,i])) for i in range(3)])
U,L,O1,O2=map(rays,[upper,lower,old1,old2])
new_edge=sorted(set(map(tuple,U))&set(map(tuple,L)))
old_edge=sorted(set(map(tuple,O1))&set(map(tuple,O2)))
assert new_edge==[(0,1,1),(1,0,1)]
assert old_edge==[(0,0,1),(1,1,1)]
payload={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'fresh integer-lattice minors, saturated hypersurface certificate inputs, exact Jacobian Hessian, unimodular inverse cone-ray extraction, and incidence substitutions; no attached program rerun','generator_matrix':[[int(t) for t in row] for row in M.tolist()],'maximal_minor_gcd':minor_gcd,'primitive_kernel':[1,1,-1,-1,-1],'base_equation_groebner_basis':[str(p.as_expr()) for p in G.polys],'fixed_u_node_hessian_determinant':str(S.factor(H.det())),'corrected_upper_chart_rays':U,'corrected_lower_chart_rays':L,'corrected_common_edge':new_edge,'old_chart_1_rays':O1,'old_chart_2_rays':O2,'old_common_edge':old_edge,'corrected_transition':'b=1/a; (x,z)=a*(v,Y); y=uY','incidence_polynomial_substitutions_pass':True,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(B/'S6_SERIES_PUBLISH_I_push_A11_A12_exact_check.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps(payload,indent=2))
