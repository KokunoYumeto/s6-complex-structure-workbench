from pathlib import Path
from itertools import product
import importlib.util
import sympy as s
root=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('tupledata',root/'background/data/fourfold_tuple.py');t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
X=s.Matrix(6,6,s.symbols('x:36'))
D=s.linear_eq_to_matrix(list(X*t.M1-t.M1*X)+list(X*t.M2-t.M2*X),list(X))[0]
print('centralizer_dimension',36-D.rank())
for v in D.nullspace():print('centralizer_basis',s.Matrix(6,6,v))
print('complete_search_mod2_bound',2**6)
for vec in product(range(2),repeat=6):
 v=s.Matrix(vec)
 if all(int(z)%2==0 for z in (t.M1-s.eye(6))*v) and all(int(z)%2==0 for z in (t.M2-s.eye(6))*v):
  print('common_fixed_mod2',v.T,'cuspNv',((t.M0-s.eye(6))*v).T)
D=s.linear_eq_to_matrix(list(X*t.M1-t.M1.inv()*X)+list(X*t.M2-t.M2.inv()*X),list(X))[0]
print('simultaneous_inverse_intertwiners',36-D.rank())
for v in D.nullspace():
 R=s.Matrix(6,6,v);den=s.ilcm(*[x.q for x in R]);R=R*den
 print('inverse_intertwiner',R,'det',R.det(),'square',R*R,'ell_row',R[0,:])
for i,M,v in [(1,t.M1,t.v1),(2,t.M2,t.v2)]:
 diff=-R*v+v
 print('real_twist_difference',i,diff.T)
 try: print('rational_image_solution',(M-s.eye(6)).gauss_jordan_solve(diff)[0])
 except ValueError: print('rational_image_solution: none')
 m={1:5,2:4}[i]
 print('difference_divided_by_m',(diff/m).T)
from sympy.matrices.normalforms import hermite_normal_form
for i,M,v,m in [(1,t.M1,t.v1,5),(2,t.M2,t.v2,4)]:
 norm=sum((M**j for j in range(m)),s.zeros(6));H=hermite_normal_form(norm);diff=-R*v+v
 sol=H.gauss_jordan_solve(diff)[0]
 print('real_norm_membership',i,'HNF',H,'coords',sol,'integral',all(x.q==1 for x in sol))
N=t.M0-s.eye(6);S=s.Matrix.hstack(N[:,0],N[:,3],N[:,4],s.eye(6)[:,0],s.eye(6)[:,3],s.eye(6)[:,4])
print('inverse_intertwiner_cusp_marking',S.inv()*R*S)
Rc=t.M2.inv()*R
print('based_cusp_real_intertwiner',S.inv()*Rc*S,'antiN',Rc*N==-N*Rc)
