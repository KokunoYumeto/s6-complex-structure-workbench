from pathlib import Path
from itertools import combinations,permutations
import sympy as s,json,time,hashlib
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from datetime import datetime,timezone
start=time.monotonic();checks=[]
def ck(n,v):
 if not bool(v):raise AssertionError(n)
 checks.append({'name':n,'pass':True})
def mat(M):return [[int(v) for v in M.row(i)] for i in range(M.rows)]
def snf(M):
 if M.rows==0 or M.cols==0:return s.zeros(*M.shape),s.eye(M.rows),s.eye(M.cols)
 D,U,V=smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(s.ZZ));D,U,V=[a.to_Matrix() for a in [D,U,V]]
 ck('Smith equality '+str(M.shape),D==U*M*V);ck('Smith unimodular '+str(M.shape),abs(U.det())==1 and abs(V.det())==1)
 return D,U,V
def wedge(M,k):
 rr=list(combinations(range(M.rows),k));cc=list(combinations(range(M.cols),k))
 return s.Matrix(len(rr),len(cc),lambda i,j:M[list(rr[i]),list(cc[j])].det())
def canon(vs):
 vs=sorted(tuple(v) for v in vs);a=vs[0];return tuple(tuple(v[i]-a[i] for i in range(3)) for v in vs)
cells=[set() for i in range(4)]
for perm in permutations(range(3)):
 vs=[(0,0,0)];v=[0,0,0]
 for i in perm:v=v.copy();v[i]+=1;vs.append(tuple(v))
 for k in range(4):
  for c in combinations(vs,k+1):cells[k].add(canon(c))
cells=[sorted(v) for v in cells];ck('26cells',sum(map(len,cells))==26)
inc=[]
for p in range(3):
 for ti,tau in enumerate(cells[p+1]):
  for j in range(p+2):inc.append((p,cells[p].index(canon(tau[:j]+tau[j+1:])),ti,(-1)**j))
ck('74incidences',len(inc)==74)
Qs={};Ss={}
for p in range(4):
 for i,c in enumerate(cells[p]):
  L=s.Matrix.hstack(*(s.Matrix(v) for v in c[1:])) if p else s.zeros(3,0)
  for ix in combinations(range(3),3-p):
   U=L.row_join(s.eye(3)[:,list(ix)])
   if abs(U.det())==1:break
  else:raise AssertionError('no completion')
  Q=U.inv()[p:,:];S=U[:,p:];Qs[p,i]=Q;Ss[p,i]=S
  ck('primitive quotient '+str((p,i)),Q*L==s.zeros(3-p,p) and Q*S==s.eye(3-p))
complexes={};hom={};projections={};collapse={};outcomp={}
for q in range(4):
 dims={d:len(cells[3-d])*len(list(combinations(range(d),q))) for d in range(4)}
 dif={0:s.zeros(0,dims[0]),4:s.zeros(dims[3],0)}
 for d in range(1,4):
  p=3-d;D=s.zeros(dims[d-1],dims[d]);ks=len(list(combinations(range(d),q)));kt=len(list(combinations(range(d-1),q)))
  if ks and kt:
   for pp,si,ti,sg in inc:
    if pp!=p:continue
    B=sg*wedge(Qs[p+1,ti]*Ss[p,si],q)
    D[ti*kt:(ti+1)*kt,si*ks:(si+1)*ks]+=B
  dif[d]=D
 for d in range(1,4):ck('d2 '+str((d,q)),dif[d-1]*dif[d]==s.zeros(dif[d-1].rows,dif[d].cols))
 for d in range(4):
  D,U,V=snf(dif[d]);r=sum(D[i,i]!=0 for i in range(min(D.shape)));Vin=V.inv();I=Vin*dif[d+1]
  ck('incoming cycles '+str((d,q)),I[:r,:]==s.zeros(r,I.cols));IB=I[r:,:]
  DI,UI,VI=snf(IB);ri=sum(DI[i,i]!=0 for i in range(min(DI.shape)))
  factors=[abs(int(DI[i,i])) for i in range(ri)];ck('free E2 '+str((d,q)),all(a==1 for a in factors))
  h=dims[d]-r-ri;hom[d,q]=h;proj=UI[ri:,:]*Vin[r:,:];projections[d,q]=proj
  # Integral PD/Alexander--Whitney map of the product torus.
  p=3-d;As=list(combinations(range(3),q));Bs=list(combinations(range(3),d));C=s.zeros(dims[d],len(Bs)*len(As));kcell=len(list(combinations(range(d),q)))
  for i,cell in enumerate(cells[p]):
   for jb,J in enumerate(Bs):
    Jc=tuple(j for j in range(3) if j not in J);word=J+Jc;sg=(-1)**sum(word[u]>word[v] for u in range(3) for v in range(u+1,3));coef=sg
    for r0 in range(p):coef*=cell[r0+1][Jc[r0]]-cell[r0][Jc[r0]]
    if kcell:C[i*kcell:(i+1)*kcell,jb*len(As):(jb+1)*len(As)]=coef*wedge(Qs[p,i],q)
  ck('collapse cycles '+str((d,q)),dif[d]*C==s.zeros(dif[d].rows,C.cols))
  HC=proj*C;DC,UC,VC=snf(HC);rc=sum(DC[i,i]!=0 for i in range(min(DC.shape)));ck('primitive graded collapse '+str((d,q)),all(abs(DC[i,i])==1 for i in range(rc)))
  collapse[d,q]=(HC,Bs,As);outcomp[str((d,q))]={'chain_rank':dims[d],'differential':mat(dif[d]),'cycle_basis':mat(V[:,r:]),'incoming_cycle_matrix':mat(IB),'incoming_smith':mat(DI),'Hprojection':mat(proj),'Hrank':h,'collapse_chain':mat(C),'collapse_H':mat(HC),'collapse_rank':int(rc),'cokernel_rank':int(h-rc)}
expected=[[1,3,3,1],[0,6,8,3],[0,0,7,3],[0,0,0,1]]
ck('all E2 ranks',[[hom[d,q] for d in range(4)] for q in range(4)]==expected)
M=s.eye(6)
for i in range(3):M[i,i+3]=1
ranks=[];cranks=[];collapses={}
for k in range(7):
 src=list(combinations(range(6),k));rows=[]
 for d in range(4):
  q=k-d
  if q not in range(4):continue
  HC,Bs,As=collapse[d,q];F=s.zeros(HC.rows,len(src))
  for jb,J in enumerate(Bs):
   for ia,I in enumerate(As):
    col=src.index(tuple(I)+tuple(j+3 for j in J));F[:,col]=(-1)**(d*q)*HC[:,jb*len(As)+ia]
  rows.append(F)
 F=s.Matrix.vstack(*rows);N=wedge(M,k)-s.eye(len(src));ck('actual marked monodromy annihilation '+str(k),F*N==s.zeros(F.rows,N.cols))
 D,U,V=snf(F);rr=sum(D[i,i]!=0 for i in range(min(D.shape)));ck('total collapse primitive '+str(k),all(abs(D[i,i])==1 for i in range(rr)))
 ranks.append(int(rr));cranks.append(F.rows);ck('coinvariant rank '+str(k),len(src)-N.rank()==rr);collapses[str(k)]={'matrix':mat(F),'source_basis':src,'smith':mat(D),'left':mat(U),'right':mat(V)}
ck('cusp homology ranks',cranks==[1,3,9,9,10,3,1]);ck('collapse image ranks',ranks==[1,3,9,9,9,3,1])
out={'actor':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed)','utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','assertions':len(checks),'elapsed_seconds':time.monotonic()-start,'checks':checks,'cells':cells,'incidences':inc,'quotients':{str(k):mat(v) for k,v in Qs.items()},'right_inverses':{str(k):mat(v) for k,v in Ss.items()},'complexes':outcomp,'collapse':collapses,'homology_ranks':cranks,'collapse_ranks':ranks,'scope':'Fresh reconstruction of all26periodic Kuhn simplex classes,74incidences, angular quotient maps, every E1 differential, integral E2 groups, PD/AW marked collapse and monodromy kernel/rank/primitive image. Geometry and higher-differential cancellation remain the explicit received P1.11 proof. This does not construct P1.19full global complex or its secondary attaching vectors.'}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2,default=str));print(json.dumps({'status':'PASS','assertions':len(checks),'seconds':out['elapsed_seconds'],'sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'output':str(p)}))
