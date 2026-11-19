from pathlib import Path
import importlib.util,contextlib,io
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form
with contextlib.redirect_stdout(io.StringIO()):
 exec(Path(__file__).with_name('cusp_complex.py').read_text().replace("Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2,default=int))",''))
root=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('tupledata',root/'background/data/fourfold_tuple.py');t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
for label,M1,M2,M0 in [('homology',t.M1,t.M2,t.M0),('cohomology_reverse',t.B,t.A,(t.B*t.A).inv())]:
 I=s.eye(6);L=[hermite_normal_form(M-I) for M in [M1,M2,M0]]
 D1=L[0].row_join(M1*L[1]).row_join(M1*M2*L[2])
 blocks=[]
 for M,K in zip([M1,M2,M0],L):
  C=K.gauss_jordan_solve(M-I)[0];assert all(x.q==1 for x in C);blocks.append(C)
 D0=s.Matrix.vstack(*blocks);assert D1*D0==s.zeros(6,6)
 h=homology(D1,D0)
 print(label,'image_bases',L,'D1',D1,'D0',D0,'H1',h['free'],h['torsion'])
 print('H2_smith',snf(D1)[0])
M1,M2,M0=t.M1,t.M2,t.M0;I=s.eye(6)
L=[]
for M,m in [(M1,5),(M2,4)]:
 norm=sum((M**j for j in range(m)),s.zeros(6));dd,uu,vv=snf(norm);L.append(vv[:,norm.rank():])
L.append(hermite_normal_form(M0-I))
D1=L[0].row_join(M1*L[1]).row_join(M1*M2*L[2])
D0=s.Matrix.vstack(*[K.gauss_jordan_solve(M-I)[0] for M,K in zip([M1,M2,M0],L)])
h=homology(D1,D0)
print('orbifold_finite_parabolic_cusp','L',L,'D1',D1,'D0',D0,'H1',h['free'],h['torsion'])
