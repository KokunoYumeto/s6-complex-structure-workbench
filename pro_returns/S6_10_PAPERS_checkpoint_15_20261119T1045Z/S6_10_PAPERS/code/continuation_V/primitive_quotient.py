#!/usr/bin/env python3
"""Fresh companion exterior-square, primitive/quotient and Hom computations."""
from pathlib import Path
import json,itertools
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.matrices.normalforms import smith_normal_form
x=s.symbols('x')
def companion(coeff):
 n=len(coeff)-1;M=s.zeros(n)
 for j in range(n-1):M[j+1,j]=1
 for i in range(n):M[i,n-1]=-coeff[n-i]
 return M
Cf=companion([1,1,1,1,1]);Cg=companion([1,0,0,0,1]);pairs=list(itertools.combinations(range(4),2))
def wedge(M):return s.Matrix([[M[a,c]*M[b,d]-M[a,d]*M[b,c] for c,d in pairs] for a,b in pairs])
WA=wedge(Cf.inv());WB=wedge(Cg);E=s.zeros(6)
for i,p in enumerate(pairs):
 for j,q in enumerate(pairs):
  a=p+q
  if len(set(a))==4:E[i,j]=(-1)**sum(a[h]>a[k] for h in range(4) for k in range(h+1,4))
assert abs(E.det())==1 and WA.T*E*WA==E and WB.T*E*WB==E
basis=(WA-s.eye(6)).col_join(WB-s.eye(6)).nullspace();assert len(basis)==1;q=basis[0];q*=s.ilcm(*[v.q for v in q]);q/=s.igcd(*map(int,q));assert abs((q.T*E*q)[0])==2
D,U,V=smith_normal_decomp(DomainMatrix.from_Matrix(q).convert_to(s.ZZ));D,U,V=[M.to_Matrix() for M in [D,U,V]];T=U.inv();assert abs(T.det())==1 and abs(D[0,0])==1
T[:,0]=q;assert abs(T.det())==1
QA=(T.inv()*WA*T)[1:,1:];QB=(T.inv()*WB*T)[1:,1:]
inp=json.loads(Path('/workspace/scratch/ae06852560d6/materials/S6_08_PAPERS_2_returns_code/returns/S6_04_MAPS_MANIFOLDS/records/fourfolds_marked_survivor_input.json').read_text());M1,M2=map(s.Matrix,inp['matrices']);A=M1.T[1:,1:];B=M2.T[1:,1:]
vars=s.symbols('z:25');Z=s.Matrix(5,5,vars);mat,_=s.linear_eq_to_matrix(list(QA*Z-Z*A)+list(QB*Z-Z*B),vars);h=mat.nullspace();assert len(h)==1;z=h[0];z*=s.ilcm(*[v.q for v in z]);z/=s.igcd(*map(int,z));K=s.Matrix(5,5,list(z));assert abs(K.det())==1
Q=q.row_join(T[:,1:]*K);assert abs(Q.det())==1
assert (Q.inv()*WA*Q)[1:,1:]==A and (Q.inv()*WB*Q)[1:,1:]==B
f=q.T*E;D,U,V=smith_normal_decomp(DomainMatrix.from_Matrix(f).convert_to(s.ZZ));D,U,V=[M.to_Matrix() for M in [D,U,V]];P=V[:,1:];assert f*P==s.zeros(1,5)
Pmap=(Q.inv()*P)[1:,:];smith=smith_normal_form(Pmap,domain=s.ZZ);diag=[abs(int(smith[i,i])) for i in range(5)];assert diag==[1,1,1,1,2]
PA=P.gauss_jordan_solve(WA*P)[0];PB=P.gauss_jordan_solve(WB*P)[0];eq,_=s.linear_eq_to_matrix(list(Z*PA-A*Z)+list(Z*PB-B*Z),vars);hom=eq.nullspace();assert len(hom)==1
assert Pmap*PA==A*Pmap and Pmap*PB==B*Pmap
# Finite global van Kampen abelian presentation after the group-theoretic
# coprime-action reduction, independently generated from the marked inputs.
ell=s.Matrix([[1,0,0,0,0,0]]);m1,m2=inp['orders'];v1,v2=map(s.Matrix,inp['numerators']);presentation=s.Matrix([[m1,0,-(ell*v1)[0]],[0,m2,-(ell*v2)[0]],[1,1,0]]);assert abs(presentation.det())==1
# Small exact certificate for the polynomial-centralizer argument printed
# after comparison: A is cyclic on e3; four commutator entries suffice.
e3=s.eye(5)[:,2];krylov=s.Matrix.hstack(*[A**k*e3 for k in range(5)]);assert krylov.det()==-1
commutators=[A**k*B-B*A**k for k in range(1,5)];places=[(0,1),(0,3),(1,3),(2,0)]
centralizer_minor=s.Matrix([[C[i,j] for C in commutators] for i,j in places]);assert centralizer_minor.det()==-1
expectedA=s.Matrix([[1,-1,0,1,0,0],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
expectedB=s.Matrix([[1,0,1,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
assert Q.inv()*WA*Q==expectedA and Q.inv()*WB*Q==expectedB
out={'status':'PASS','Cf':Cf.tolist(),'Cg':Cg.tolist(),'wedge_pairing':E.tolist(),'invariant_q':q.tolist(),'q_square':int((q.T*E*q)[0]),'constructed_integral_Q':Q.tolist(),'quotient_A':A.tolist(),'quotient_B':B.tolist(),'primitive_basis':P.tolist(),'natural_map':Pmap.tolist(),'natural_map_smith':diag,'rational_Hom_dimension':len(hom),'cyclic_krylov_determinant':int(krylov.det()),'centralizer_minor_positions_1based':[[i+1,j+1] for i,j in places],'centralizer_minor':centralizer_minor.tolist(),'centralizer_minor_determinant':int(centralizer_minor.det()),'global_pi1_abelian_presentation':presentation.tolist(),'global_pi1_determinant':int(presentation.det()),'scope':'Constructs actual integral quotient maps and proves the natural primitive map has index2. Non-isomorphism follows from the one-dimensional rational Hom space and2-adic valuation of2*c^5.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=int)+'\n');print(json.dumps(out,indent=2,default=int))
