from pathlib import Path
from itertools import combinations
import importlib.util
import sympy as s
root=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('tupledata',root/'background/data/fourfold_tuple.py');d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
def wedge(m):
 inds=list(combinations(range(4),2));return s.Matrix([[m.extract(i,j).det() for j in inds] for i in inds])
B=s.zeros(6)
for i,j,a in [(0,5,1),(1,4,-1),(2,3,1)]:B[i,j]=B[j,i]=a
om=s.ones(6,1);c=(om.T*B)
P=s.Matrix.vstack(-c[:,1:],s.eye(5));G=P.T*B*P
K=(d.Q.inv()*P)[1:,:]
L=d.A[1:,1:];R=d.B[1:,1:]
Gl=2*((d.Q.T*B*d.Q)[1:,1:]-(d.Q.T*B*d.Q)[1:,:1]*(d.Q.T*B*d.Q)[:1,1:]/2)
print('wedge_pairing',B,'det',B.det());print('omega',om,'omega_square',(om.T*B*om)[0]);print('contraction',c)
print('primitive_basis',P);print('primitive_form',G,'det',G.det());print('quotient_form',Gl,'det',Gl.det());print('primitive_to_quotient',K,'det',K.det());print('pullback_form',K.T*Gl*K,'equals_2G',K.T*Gl*K==2*G)
for name,E in [('Cf_inv',wedge(d.Cf.inv())),('Cg',wedge(d.Cg))]:
 Rp=(E*P)[1:,:]
 print('primitive_action',name,Rp)
 print('intertwining',name,(L if name=='Cf_inv' else R)*K==K*Rp)
print('primitive_form_content',s.igcd(*list(G)));print('quotient_form_content',s.igcd(*list(Gl)))
# All bilinear forms, exact dimension, no symmetry assumption.
for name,X,Y in [('primitive',(wedge(d.Cf.inv())*P)[1:,:],(wedge(d.Cg)*P)[1:,:]),('quotient',L,R)]:
 H=s.Matrix(5,5,s.symbols('h:25'))
 D=s.linear_eq_to_matrix(list(X.T*H*X-H)+list(Y.T*H*Y-H),list(H))[0]
 print(name,'invariant_bilinear_space_dimension',25-D.rank())
