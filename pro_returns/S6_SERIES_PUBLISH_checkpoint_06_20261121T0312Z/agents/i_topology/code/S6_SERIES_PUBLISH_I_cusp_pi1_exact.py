"""Exact integral presentation check for IP07; no numeric tolerance."""
import json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
out=Path(__file__).resolve().parents[1]/'output'/'S6_SERIES_PUBLISH_I_cusp_pi1_exact.json'
# Ordered marked torus basis (g,u,w,d); the last generator below is base b.
M=s.Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
P=s.Matrix([[1,0,0,0],[0,1,0,0]])
B0=s.Matrix([[0,1],[-1,0]])
# Ray columns in (w,d,b), with their explicit integral inverse.
R=s.Matrix([[0,1,0],[0,0,1],[1,1,1]])
assert R.det()==1 and R.inv()*R==s.eye(3)
# Full five-generator abelianized presentation: monodromy relations, then toric meridians.
mon=(M-s.eye(4)).col_join(s.zeros(1,4))
rays=s.zeros(2,3).col_join(R)
relations=mon.row_join(rays)
D=smith_normal_form(relations,domain=ZZ)
diag=[int(abs(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
projection=P.row_join(s.zeros(2,1))
assert diag==[1,1,1] and relations.rank()==3
assert projection*relations==s.zeros(2,relations.cols)
assert P*M==P and B0.det()==1
# Integral splitting: g,u survive; w,d,b lie in the ray span with explicit inverse columns.
assert rays[2:,:].inv()==R.inv()
assert projection[:,0:2]==s.eye(2)
result={'basis':['g','u','w','d','b'],'monodromy':M.tolist(),'fan_index_matrix':B0.tolist(),
'primitive_rays_in_w_d_b':R.tolist(),'ray_determinant':int(R.det()),'ray_inverse':R.inv().tolist(),
'full_relation_matrix':relations.tolist(),'smith_nonzero_diagonal':diag,'relation_rank':int(relations.rank()),
'free_quotient_rank':5-relations.rank(),'quotient_projection':projection.tolist(),
'quotient_monodromy_identity':True,'literal_gamma_degree_on_g':1,
'geometric_scope':'The nonabelian presentation has commuting lattice generators; killing b,w,d leaves freely commuting g,u. The simply connected toric-cover proof supplies the absence of further relations.'}
out.write_text(json.dumps(result,indent=2,default=int))
print(json.dumps(result,indent=2,default=int))
