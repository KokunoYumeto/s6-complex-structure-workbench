"""Exact centralizer, reflection candidates, and torsion translations."""
from pathlib import Path
import importlib.util,sympy as s,json,contextlib,io
from sympy.matrices.normalforms import hermite_normal_form
root=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('data',root/'background/data/fourfold_tuple.py');d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
X=s.Matrix(6,6,s.symbols('x0:36'));variables=list(X)
equations=s.Matrix(list(X*d.M1-d.M1*X)+list(X*d.M2-d.M2*X)).jacobian(variables)
ns=equations.nullspace();assert len(ns)==1
C=s.Matrix(6,6,ns[0]);assert C==s.eye(6)
tau=s.Matrix([0,1,1,1,1,1])/2
for M in [d.M1,d.M2,d.M0]:assert all(v.q==1 for v in (M-s.eye(6))*tau)
N=d.M0-s.eye(6)
R=s.Matrix([[1,0,0,0,0,0],[2,0,0,0,-1,0],[-1,0,-1,0,0,0],[-1,0,0,-1,0,0],[2,-1,0,0,0,0],[-1,1,1,1,1,1]])
assert R*R==s.eye(6) and R.det()==-1
assert all(R*M==M.inv()*R for M in [d.M1,d.M2])
out={'centralizer_dimension':len(ns),'centralizer_basis':[[str(v) for v in row] for row in C.tolist()],'tau':[str(v) for v in tau],'N_tau':[str(v) for v in N*tau],'reflection_homology':R.tolist(),'reflection_is_only_a_lattice_candidate':True}
for label,M,v,m in [('finite1',d.M1,d.v1,5),('finite2',d.M2,d.v2,4)]:
    norm=sum((M**k for k in range(m)),s.zeros(6));H=hermite_normal_form(norm);w=v-R*v
    coords=H.gauss_jordan_solve(w)[0];assert all(t.q==1 for t in coords)
    out[label]={'norm':norm.tolist(),'norm_image_basis':H.tolist(),'v_minus_Rv':list(w),'image_coordinates':list(coords)}
buffer=io.StringIO()
with contextlib.redirect_stdout(buffer):
    exec(Path(__file__).with_name('parabolic_cohomology.py').read_text())
out['parabolic_H1']={'free':h['free'],'torsion':[int(v) for v in h['torsion']],'D0':D0.tolist(),'D1':D1.tolist(),'local_bases':[K.tolist() for K in L]}
assert h['free']==0 and [int(v) for v in h['torsion']]==[2]
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print('centralizer Q*I; integral invertible elements ±I')
print('half-period',tau.T,'fixed modulo Lambda; N*tau=',(N*tau).T)
print('parabolic H1:',h['free'],h['torsion'])
print('D0',D0,'D1',D1)
print('reflection candidate',R,'det',R.det(),'square identity; geometric real structure still requires affine and cusp gluing')
