"""Independent exact computation from F2.12 statement matrices only.
The target proof and its producing programs have not been read.
"""
from flint import fmpz_mat
from itertools import combinations
from pathlib import Path
import json,hashlib,math
checks=[]
def check(x,n):
 if not x:raise AssertionError(n)
 checks.append(n)
def eye(n):return fmpz_mat([[int(i==j)for j in range(n)]for i in range(n)])
def zero(m,n):return fmpz_mat(m,n)
def array(M):return [[int(M[i,j])for j in range(M.ncols())]for i in range(M.nrows())]
def cols(M,ix):return fmpz_mat([[M[i,j]for j in ix]for i in range(M.nrows())])
def sub(M,ri,cj):return fmpz_mat([[M[i,j]for j in cj]for i in ri])
def join(L):return fmpz_mat([[a for M in L for a in array(M)[i]]for i in range(L[0].nrows())])
def stack(L):return fmpz_mat([r for M in L for r in array(M)])
def integral_inverse(M):
 X=M.inv();check(all(x.denominator==1 for row in X.tolist() for x in row),'unimodular inverse integral');return fmpz_mat([[int(x)for x in row]for row in X.tolist()])
def kernel(M):
 H,U=M.transpose().hnf(transform=True);check(U*M.transpose()==H,'exact HNF transform');r=H.rank();V=U.transpose();K=cols(V,range(r,V.ncols()));check(M*K==zero(M.nrows(),K.ncols()),'exact kernel basis');return K,V,r
def wedge(M,k):
 ix=list(combinations(range(M.nrows()),k))
 return fmpz_mat([[int(sub(M,I,J).det()) if k else 1 for J in ix]for I in ix])
def smith(M):
 S=M.snf();return [abs(int(S[i,i]))for i in range(min(S.nrows(),S.ncols())) if S[i,i]]
A5=fmpz_mat([[1,0,1,0,0],[1,0,0,0,0],[-1,0,0,1,1],[1,-1,0,-1,0],[0,1,0,0,0]])
B5=fmpz_mat([[0,1,0,0,0],[0,0,0,0,1],[1,-2,0,0,0],[0,1,0,-1,-1],[0,0,1,1,2]])
A=eye(6);B=eye(6)
for i in range(5):
 for j in range(5):A[i+1,j+1]=A5[i,j];B[i+1,j+1]=B5[i,j]
B[0,4]=1
check(A**5==eye(6),'A order divides5');check(B**12==eye(6),'B order divides12')
for d in [1,2,3,4,6]:check(B**d!=eye(6),'B order excludes'+str(d))
N=A*B-eye(6);check(N*N==zero(6,6),'square-zero cusp');check(smith(N)==[1,1,1],'primitive rank-three cusp')
check(smith(A5*B5-eye(5))==[1,1],'primitive rank-two quotient cusp')
check(list(B5.charpoly())==[-1,1,1,-1,-1,1],'vertical characteristic (x-1)Phi12')
check(A!=eye(6),'A has exact order5')
# Explicit mod3 independent words in the full preserving-line matrix algebra.
rb={};mats=[];words=[]
def insert(M,w):
 v=[int(a)%3 for row in array(M)for a in row]
 for p in sorted(rb):
  t=v[p]
  if t:v=[(x-t*y)%3 for x,y in zip(v,rb[p])]
 if not any(v):return
 p=next(i for i,a in enumerate(v)if a);t=pow(v[p],-1,3);rb[p]=[x*t%3 for x in v];mats.append(M);words.append(w)
insert(eye(6),'1');i=0
while i<len(mats):
 M,w=mats[i],words[i];i+=1
 insert(M*A,w+'A');insert(M*B,w+'B')
check(len(mats)==31,'full preserving-line algebra dimension31 mod3')
positions=[(0,j)for j in range(6)]+[(i,j)for i in range(1,6)for j in range(1,6)]
C=fmpz_mat([[M[i,j]for M in mats]for i,j in positions]);det=int(C.det());check(det%3!=0,'31-word determinant is a unit at3')
for M in mats:check(all(M[i,0]==0 for i in range(1,6)),'word preserves line')
# Full exact invariant-extension sheaf complexes.
sheaves=[]
for q in [1,2,3]:
 Aq=wedge(A,q);Bq=wedge(B,q);n=Aq.nrows();Id=eye(n)
 J1,_,_=kernel(Aq-Id);J2,_,_=kernel(Bq-Id);J0,_,_=kernel(Bq*Aq-Id)
 D=join([Aq-Id,Bq-Id]);K,V,rr=kernel(D)
 D0=stack([join([J1,zero(n,J2.ncols()),-J0]),join([zero(n,J1.ncols()),J2,-Aq*J0])])
 check(D*D0==zero(n,D0.ncols()),'degree'+str(q)+' sheaf d1d0 zero')
 W=integral_inverse(V)*D0;check(sub(W,range(rr),range(W.ncols()))==zero(rr,W.ncols()),'degree'+str(q)+' image in actual integral kernel')
 E=sub(W,range(rr,W.nrows()),range(W.ncols()));sf=smith(E);sd=smith(D)
 H0=D0.ncols()-D0.rank();H1free=K.ncols()-E.rank();H1three=[t for t in sf if t%3==0];H2three=[t for t in sd if t%3==0]
 if q==1:check(H0==1 and H1free==0 and not H1three and not H2three,'degree1 localized sheaf groups')
 if q==2:check(H0==0 and H1free==0 and not H1three and not H2three,'degree2 localized sheaf groups vanish')
 if q==3:check(H0==0,'degree3 global invariant zero')
 sheaves.append({'q':q,'finite_fixed_ranks':[J1.ncols(),J2.ncols()],'cusp_fixed_rank':J0.ncols(),'H0_rank':H0,'H1_free_rank':H1free,'H1_smith':sf,'H2_smith':sd,'Delta':array(D),'d0':array(D0),'kernel_basis':array(K),'image_coordinates':array(E),'invariant_bases':[array(J1),array(J2),array(J0)]})
# Low-degree finite cap Wang torsion and exact norm on its fixed line.
E=B5**4-B5**2+eye(5);Norm=sum((B5**i for i in range(12)),zero(5,5))
check(E*E==E and E.rank()==1,'integral fixed-line projector Phi12(B5)');check(Norm==12*E,'norm equals12 times primitive projector')
Ds=[]
for q in [1,2]:
 T=wedge(B5,q);sd=smith(T-eye(T.nrows()));check(all(t%3 for t in sd),'finite cap degree'+str(q)+' Wang quotient no3torsion');Ds.append({'q':q,'smith':sd})
# One explicit standard-lattice free simply connected filling.
v1=fmpz_mat([[3],[0],[0],[0],[0],[0]]);v2=fmpz_mat([[-7],[7],[-7],[7],[0],[7]])
check(A.transpose()*v1==v1 and B.transpose()*v2==v2,'actual homology fixed translation vectors')
check(math.gcd(3,5)==1 and math.gcd(-7,12)==1,'all nonidentity affine powers free by primitive character')
G=join([A.transpose()-eye(6),B.transpose()-eye(6)]);check(smith(G)==[1,1,1,1,1],'homology global coinvariants primitive rankone')
check(all(G[0,j]==0 for j in range(G.ncols())),'coinvariant character ell=x0')
R=fmpz_mat([[5,0,-3],[0,12,7],[1,1,0]]);check(abs(int(R.det()))==1,'actual remaining van Kampen relation determinant1')
result={'status':'PASS','checks':len(checks),'check_names':checks,'statement_input_matrices':{'A':array(A),'B':array(B)},'algebra_words':words,'algebra_coordinate_positions':positions,'algebra_certificate_matrix':array(C),'algebra_determinant':det,'cusp_smith':smith(N),'sheaf_complexes':sheaves,'finite_cap_low_degree_smith':Ds,'finite_fixed_projector':array(E),'finite_norm':array(Norm),'standard_filling':{'v1':array(v1),'v2':array(v2),'multiplicities':[5,12],'relation_matrix':array(R),'determinant':int(R.det())},'scope':'Exact computation from statement matrices before target proof reading. Universal invariant-lattice and arbitrary-multiplicity argument is written separately; this program does not infer those claims from a bounded parameter sample.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'PASS','checks':len(checks),'algebra_det':det,'sheaf_summary':[{k:z[k]for k in ['q','H0_rank','H1_free_rank','H1_smith','H2_smith']}for z in sheaves]}))
