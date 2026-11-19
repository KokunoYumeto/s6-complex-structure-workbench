"""Independent FLINT certificate for the actual finite-cover/sheaf maps.

The supplied target proof and its producing program remain unread.
Only the statement packet's construction matrices are imported.
"""
from pathlib import Path
from itertools import combinations,product
import json,re,sys,hashlib,datetime
BASE=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(BASE/'build/continuation_numeric/python'))
from flint import fmpz_mat,fmpq_mat
packet=BASE/'analysis/continuation_V/F2_6_integral_homology_statement_input_packet.md'
data=json.loads(re.search(r'```json\n(.*?)\n```',packet.read_text(),re.S).group(1))
def Z(x):return fmpz_mat(x)
def eye(n):return Z([[int(i==j) for j in range(n)] for i in range(n)])
def zero(n,m):return fmpz_mat(n,m)
def rows(A):return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def sub(A,rs,cs):
 rs,cs=list(rs),list(cs)
 return Z([[int(A[i,j]) for j in cs] for i in rs]) if rs and cs else zero(len(rs),len(cs))
def inv(A):
 B=A.inv();assert all(B[i,j]==int(B[i,j]) for i in range(B.nrows()) for j in range(B.ncols()))
 return Z(rows(B))
def hc(*aa):return Z([sum((rows(A)[i] for A in aa),[]) for i in range(aa[0].nrows())])
def vc(*aa):return Z(sum((rows(A) for A in aa),[]))
def ext(A,k):
 c=list(combinations(range(A.nrows()),k))
 return Z([[int(sub(A,I,J).det()) for J in c] for I in c]) if k else Z([[1]])
def snf(A):
 S=A.snf();r=A.rank()
 return {'rank':r,'free':A.nrows()-r,'torsion':[abs(int(S[i,i])) for i in range(r) if abs(S[i,i])>1],'diagonal':[int(S[i,i]) for i in range(min(S.nrows(),S.ncols()))]}
def kernel(A):
 H,T=A.transpose().hnf(transform=True);r=A.rank();assert H==T*A.transpose();assert abs(T.det())==1
 K=sub(T,range(r,T.nrows()),range(T.ncols())).transpose()
 L=sub(inv(T.transpose()),range(r,T.nrows()),range(T.ncols()))
 assert A*K==zero(A.nrows(),K.ncols());assert L*K==eye(K.ncols())
 return K,L
def image_basis(A):
 H=A.transpose().hnf();r=A.rank();return sub(H,range(r),range(H.ncols())).transpose()
def membership(A,w):
 B=image_basis(A);r=B.ncols();H,T=B.hnf(transform=True);tw=T*w
 if any(tw[i,0] for i in range(r,tw.nrows())):return False,None
 U=sub(H,range(r),range(r));x=fmpq_mat(U).inv()*fmpq_mat(sub(tw,range(r),[0]))
 ok=all(x[i,0]==int(x[i,0]) for i in range(r))
 if ok:
  xi=Z(rows(x));assert B*xi==w;return True,rows(xi)
 return False,None
def norm(A,m):
 N=zero(A.nrows(),A.ncols());P=eye(A.nrows())
 for _ in range(m):N+=P;P=P*A
 assert P==eye(A.nrows());return N
def embed_vertical(k):
 big=list(combinations(range(6),k));small=list(combinations(range(5),k))
 return Z([[int(I==tuple(j+1 for j in J)) for J in small] for I in big])
def embed_horizontal(k):
 big=list(combinations(range(6),k));small=list(combinations(range(5),k-1))
 return Z([[int(I==(0,)+tuple(j+1 for j in J)) for J in small] for I in big])

M1,M2=Z(data['M1']),Z(data['M2']);A1,A2=M1.transpose(),M2.transpose()
M0=inv(M1*M2);S=Z(data['cusp_marking_S'])
assert inv(S)*M0*S==Z([[int(i==j or (i<3 and j==i+3)) for j in range(6)] for i in range(6)])
C1=Z([[-1,-1,0,-1,0],[0,1,0,1,1],[0,1,0,0,0],[0,-1,-1,0,-1],[0,0,1,0,0]])
C2=Z([[-1,0,-1,0,-1],[0,1,0,0,0],[0,0,0,1,0],[0,-1,0,-1,1],[0,0,1,0,0]])
finite=[]
for i,M,C,m in [(1,M1,C1,5),(2,M2,C2,4)]:
 v=Z([[x] for x in data[f'v{i}']]);assert M*v==v
 P=hc(v,vc(zero(1,5),C));assert abs(P.det())==1
 new=inv(P)*M*P;D=sub(new,range(1,6),range(1,6))
 assert new==vc(hc(Z([[1]]),zero(1,5)),hc(zero(5,1),D))
 assert all(sum(abs(int(D[a,b])) for b in range(5))==1 for a in range(5))
 assert all(sum(abs(int(D[a,b])) for a in range(5))==1 for b in range(5))
 assert D**m==eye(5)
 finite.append({'i':i,'m':m,'P':P,'D':D,'Q':inv(P).transpose()})
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'packet_sha256':hashlib.sha256(packet.read_bytes()).hexdigest(),'method':'FLINT exact exterior minors, integral Hermite transformations, signed-permutation cellular models, explicit restriction/coinvariant maps; no source-producing code read.','finite_conjugacies':[{'i':f['i'],'m':f['m'],'P':rows(f['P']),'P_inverse':rows(inv(f['P'])),'D':rows(f['D'])} for f in finite],'degrees':{},'transgression':{}}
for q in range(1,5):
 A,B=ext(A1,q),ext(A2,q);C=ext(M0.transpose(),q);n=A.nrows();I=eye(n)
 assert C==inv(B*A)
 J=[];local=[]
 for f in finite:
  Tq=ext(f['D'].transpose(),q);Tprev=ext(f['D'].transpose(),q-1)
  Kq,_=kernel(Tq-eye(Tq.nrows()));N=norm(Tprev,f['m'])
  raw=hc(embed_vertical(q)*Kq,embed_horizontal(q)*N)
  Ji=image_basis(ext(f['Q'],q)*raw)
  assert (A if f['i']==1 else B)*Ji==Ji
  J.append(Ji);local.append({'i':f['i'],'image_basis':rows(Ji),'torsion_of_stalk':snf(Tprev-eye(Tprev.nrows()))['torsion']})
 J0,_=kernel(C-I)
 d0=vc(hc(J[0],zero(n,J[1].ncols()),-J0),hc(zero(n,J[0].ncols()),J[1],-A*J0))
 d1=hc(A-I,B-I);assert d1*d0==zero(n,d0.ncols())
 K,L=kernel(d1);R=L*d0;assert K*R==d0
 coho1=snf(R);h0=d0.ncols()-d0.rank();coho2=snf(d1)
 out['degrees'][str(q)]={'local':local,'cusp_image_basis':rows(J0),'d0':rows(d0),'d1':rows(d1),'kernel_basis':rows(K),'kernel_left_inverse':rows(L),'relations_in_kernel':rows(R),'H0_rank':h0,'H1':coho1,'H2':coho2}

f=finite[1]
for k in range(1,4):
 T=ext(f['D'].transpose(),k);E=T-eye(T.nrows());N=norm(T,4)
 A,B=ext(A1,k),ext(A2,k);G=hc(A-eye(A.nrows()),B-eye(B.nrows()))
 inclusion=ext(f['Q'],k)*embed_vertical(k)
 found=None
 for j in range(T.nrows()):
  w=Z([[int(i==j)] for i in range(T.nrows())]);yes,_=membership(E,w);twice,witness=membership(E,2*w)
  if twice and not yes:
   assert N*w==zero(T.nrows(),1)
   z=inclusion*w;glob,_=membership(G,z);twog,gwi=membership(G,2*z)
   if not glob and twog:
    found={'cell_index':list(combinations(range(5),k))[j],'w_signed_basis':rows(w),'w_original_basis':rows(z),'local_twice_w_image_basis_coordinates':witness,'global_twice_w_image_basis_coordinates':gwi,'local_cokernel':snf(E),'global_cokernel':snf(G),'norm_w_zero':True,'image_is_nonzero_order_two':True};break
 assert found is not None
 # Fox/cellular substitution for old generators g,h and new v=g^4 h^-1,t=g.
 assert Z([[4,1],[-1,0]]).det()==1
 assert N*w==zero(T.nrows(),1)
 assert T**4==eye(T.nrows())
 found['base_change_columns_v_t']=[[4,1],[-1,0]];found['cochain_on_v']=rows(N*w);found['cochain_on_t']=rows(w)
 out['transgression'][str(k+1)]=found
expected={1:(1,0,[]),2:(0,0,[]),3:(0,3,[]),4:(0,0,[])}
for q,(h0,h1,tors) in expected.items():
 d=out['degrees'][str(q)];assert d['H0_rank']==h0;assert d['H1']['free']==h1;assert d['H1']['torsion']==tors
 assert d['H2']['free']==0 and d['H2']['torsion']==[2]
out['status']='passed'
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'finite_conjugacies':'exact integral signed permutations','sheaf_summary':{q:{'H0':d['H0_rank'],'H1_free':d['H1']['free'],'H1_torsion':d['H1']['torsion'],'H2_torsion':d['H2']['torsion']} for q,d in out['degrees'].items()},'transgression_degrees':list(out['transgression'])},indent=2))
