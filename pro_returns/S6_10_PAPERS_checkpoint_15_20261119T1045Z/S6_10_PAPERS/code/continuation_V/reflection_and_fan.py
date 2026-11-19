#!/usr/bin/env python3
"""Fresh rational reflection equations and explicit Kuhn edge obstruction."""
from pathlib import Path
import json,itertools,functools,math
import sympy as s
j=json.loads(Path('/workspace/scratch/ae06852560d6/materials/S6_08_PAPERS_2_returns_code/returns/S6_04_MAPS_MANIFOLDS/records/fourfolds_marked_survivor_input.json').read_text());M1,M2=map(s.Matrix,j['matrices']);S=s.Matrix(j['cusp_marking']);A=M1.T;B=M2.T
variables=s.symbols('r:36');Z=s.Matrix(6,6,variables);linear,_=s.linear_eq_to_matrix(list(Z*A-A.inv()*Z)+list(Z*B-B.inv()*Z),variables);basis=linear.nullspace();assert len(basis)==1
v=basis[0];v=v*s.ilcm(*[q.q for q in v]);v=v/s.igcd(*[int(x) for x in v]);R=s.Matrix(6,6,list(v));R=R/R[0,0];assert R*s.eye(6)[:,0]==s.eye(6)[:,0] and R*R==s.eye(6) and R.det()==-1
Rh=R.inv().T;M0=(M1*M2).inv();Rc=M1*Rh;alternate=M2.inv()*Rh
assert Rc*M0*Rc.inv()==M0.inv() and alternate*M0*alternate.inv()==M0.inv()
T=S.inv()*Rc*S;Ta=S.inv()*alternate*S;K=T[3:,3:];assert Ta[3:,3:]==K and T[:3,:3]==-K and T[3:,:3]==s.zeros(3)
edges={tuple(v) for v in itertools.product([0,1],repeat=3) if any(v)};edges|={tuple(-x for x in v) for v in list(edges)}
obstruction=tuple(K*s.Matrix([0,1,0]));assert obstruction not in edges and tuple(-x for x in obstruction) not in edges
out={'status':'PASS','rational_reflection_dimension':len(basis),'cohomology_R':R.tolist(),'homology_R':Rh.tolist(),'transported_cusp_T':T.tolist(),'valuation_K':K.tolist(),'K_e2':list(obstruction),'K_e2_is_Kuhn_edge':False,'minus_K_e2_is_Kuhn_edge':False,'scope':'Exact lattice and fan obstruction; its use for anti-biholomorphisms uses the intrinsic base and local valuation extension argument in prederivations_08.md.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=int)+'\n');print(json.dumps(out,indent=2,default=int))
