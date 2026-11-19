from pathlib import Path
import importlib.util, itertools
import sympy as s
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy.polys.domains import ZZ
ROOT=Path(__file__).resolve().parents[3]
p=ROOT/'background/data/fourfold_tuple.py'
spec=importlib.util.spec_from_file_location('data',p);d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
A,B,M1,M2,M0,v1,v2,ell,Cf,Cg,Q=(getattr(d,k) for k in 'A B M1 M2 M0 v1 v2 ell Cf Cg Q'.split())
I=s.eye(6);N=M0-I

def out(name,obj): print(name+' = '+str(obj))
def exterior(M,k=2):
 inds=list(itertools.combinations(range(M.rows),k))
 return s.Matrix([[M.extract(i,j).det() for j in inds] for i in inds])
for name,M,m,v in [('M1',M1,5,v1),('M2',M2,4,v2)]:
 out(name,M);out(name+'_power',M**m);out(name+'_lower_powers',[M**j==I for j in range(1,m)]);out(name+'_charpoly',s.factor(M.charpoly().as_expr()));out(name+'_fixed', (M-I).nullspace());out(name+'_covectors',(M.T-I).nullspace());out(name+'_invariant_twist',M*v==v);out(name+'_affine_m_power',sum((M**j*v for j in range(m)),s.zeros(6,1))/m)
 out(name+'_power_translations',[sum((M**j*v for j in range(k)),s.zeros(6,1))/m for k in range(1,m)])
 out(name+'_ell_powers',[ell*M**j for j in range(m)])
 out(name+'_cokernel_smith',smith_normal_form(M-I,domain=ZZ))
out('M0',M0);out('N',N);out('N_squared',N*N);out('N_rank',N.rank());out('N_smith',smith_normal_form(N,domain=ZZ));out('N_image_HNF',hermite_normal_form(N));out('common_fixed_vectors',((M1-I).col_join(M2-I)).nullspace());out('common_fixed_covectors',((A-I).col_join(B-I)).nullspace());out('coinvariants_smith',smith_normal_form((M1-I).row_join(M2-I),domain=ZZ));out('coinvariants_image_HNF',hermite_normal_form((M1-I).row_join(M2-I)));out('cohom_coinvariants_smith',smith_normal_form((A-I).row_join(B-I),domain=ZZ));out('seifert_det',s.Matrix([[5,0,-1],[0,4,1],[1,1,0]]).det())
for name,C in [('Cf_inv',Cf.inv()),('Cg',Cg)]:
 E=exterior(C);out('wedge_'+name,E);out('Qinv_wedge_Q_'+name,Q.inv()*E*Q);out('Q_wedge_Qinv_'+name,Q*E*Q.inv())
for name,C,L in [('Cf_inv',Cf.inv(),A[1:,1:]),('Cg',Cg,B[1:,1:])]:
 E=Q.inv()*exterior(C)*Q;out('lower_identity_'+name,E[1:,1:]==L)
# Invariant bilinear forms in the 5-dimensional quotient
X=s.Matrix(5,5,s.symbols('x:25'))
LA,LB=A[1:,1:],B[1:,1:]
D=s.linear_eq_to_matrix(list(LA.T*X*LA-X)+list(LB.T*X*LB-X),list(X))[0]
out('quotient_invariant_bilinear_dimension',25-D.rank());out('quotient_invariant_forms',[s.Matrix(5,5,v) for v in D.nullspace()])
# Finite affine quotients' H1 via affine crystallographic presentation.
for name,M,m,v in [('M1',M1,5,v1),('M2',M2,4,v2)]:
 tr=sum((M**j*v for j in range(m)),s.zeros(6,1))/m
 R=s.zeros(7,7);R[:6,:6]=M-I;R[:6,6]=-tr;R[6,6]=m
 out(name+'_cap_H1_relations',R);out(name+'_cap_H1_smith',smith_normal_form(R,domain=ZZ))
# Companion pair common alternating form, and genus-two discriminant.
J=s.Matrix(4,4,s.symbols('j:16'))
D=s.linear_eq_to_matrix(list(Cf.T*J*Cf-J)+list(Cg.T*J*Cg-J)+list(J.T+J),list(J))[0]
out('companion_alternating_forms',[s.Matrix(4,4,v) for v in D.nullspace()])
x,l=s.symbols('x l');out('pencil_discriminant',s.factor(s.discriminant(x**5+l**3*x+l**4,x)))
