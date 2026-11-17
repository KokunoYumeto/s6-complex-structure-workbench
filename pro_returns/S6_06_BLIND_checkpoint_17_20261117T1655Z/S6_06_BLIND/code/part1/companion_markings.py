from pathlib import Path
import importlib.util
import sympy as s
root=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('tupledata',root/'background/data/fourfold_tuple.py');d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
X=s.Matrix(4,4,s.symbols('x:16'))
for name,eq in [('inverse_both',list(X*d.Cf.inv()-d.Cf*X)+list(X*d.Cg-d.Cg.inv()*X)),('swap_inverse_orientation',list(X*d.Cf-d.Cf.inv()*X)+list(X*d.Cg.inv()-d.Cg*X))]:
 D=s.linear_eq_to_matrix(eq,list(X))[0]
 print(name,'dimension',len(D.nullspace()))
 for v in D.nullspace():
  T=s.Matrix(4,4,v);print(T,'det',T.det())
print('Cf_inv_Cg',d.Cf.inv()*d.Cg)
print('Cg_Cf_inv',d.Cg*d.Cf.inv())
delta=s.Matrix([1,1,1,0])
J=s.Matrix([[0,-1,1,-1],[1,0,-1,1],[-1,1,0,-1],[1,-1,1,0]])
K=s.Matrix.hstack(*[d.Cf**i*delta for i in range(4)])
print('model_vanishing_delta',delta)
print('symplectic_form',J,'det',J.det())
print('transvection',d.Cf.inv()*d.Cg==s.eye(4)-delta*(delta.T*J))
print('orbit_basis',K,'det',K.det())
print('orbit_pairing',K.T*J*K,'det',(K.T*J*K).det())
