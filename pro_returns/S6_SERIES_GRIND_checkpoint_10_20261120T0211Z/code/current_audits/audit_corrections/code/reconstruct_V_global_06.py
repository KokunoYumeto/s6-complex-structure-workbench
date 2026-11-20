from pathlib import Path
from itertools import combinations
import sympy as s,json,time,hashlib
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from datetime import datetime,timezone
start=time.monotonic();checks=[]
def ck(n,v):
 if not bool(v):raise AssertionError(n)
 checks.append({'name':n,'pass':True})
def mat(M):return [[int(v) for v in M.row(i)] for i in range(M.rows)]
def wedge(M,k):
 rr=list(combinations(range(M.rows),k)) if 0<=k<=M.rows else [];cc=list(combinations(range(M.cols),k)) if 0<=k<=M.cols else []
 return s.Matrix(len(rr),len(cc),lambda i,j:M[list(rr[i]),list(cc[j])].det())
def rank(D):return sum(D[i,i]!=0 for i in range(min(D.shape)))
def snf(M):
 if M.rows==0 or M.cols==0:return s.zeros(*M.shape),s.eye(M.rows),s.eye(M.cols)
 D,U,V=[a.to_Matrix() for a in smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(s.ZZ))];ck('Smith matrix equality '+str(M.shape),D==U*M*V);ck('Smith unimodular '+str(M.shape),abs(U.det())==1 and abs(V.det())==1);return D,U,V

def homology(ds,dims,name):
 ret={}
 for k,n in enumerate(dims):
  Do=ds[k];Di=ds[k+1] if k+1<len(ds) else s.zeros(n,0);ck(name+' d2 '+str(k),Do*Di==s.zeros(Do.rows,Di.cols));D,U,V=snf(Do);r=rank(D);Vi=V.inv();incoming=Vi*Di;ck(name+' incomingcycle '+str(k),incoming[:r,:]==s.zeros(r,Di.cols));B=incoming[r:,:];DB,UB,VB=snf(B);rb=rank(DB);C=V[:,r:];free=C*UB.inv()[:,rb:];proj=UB[rb:,:]*Vi[r:,:];tors=[abs(int(DB[i,i])) for i in range(rb) if abs(DB[i,i])>1]
  ret[k]={'free':free,'proj':proj,'torsion':tors,'rank':n-r-rb,'cycles':C,'incoming':B,'incoming_smith':DB,'incoming_left':UB,'incoming_right':VB,'outgoing_right':V,'outgoing_right_inverse':Vi,'outgoing_rank':r,'incoming_rank':rb}
 return ret

def solve_int(M,T,name):
 D,U,V=snf(M);r=rank(D);Z=U*T;ck(name+' imagezero',Z[r:,:]==s.zeros(Z.rows-r,Z.cols));X=s.zeros(M.cols,T.cols)
 for i in range(r):
  for j in range(T.cols):
   v=s.Rational(Z[i,j],D[i,i]);ck(name+' integral '+str((i,j)),v.q==1);X[i,j]=v
 X=V*X;ck(name+' solved',M*X==T);return X
A=s.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]]).T
B=s.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]]).T
M0=(A*B).inv();Ms=[M0,A,B];mult=[None,5,4];vs=[None,s.Matrix([1,3,-2,-1,2,0]),s.Matrix([-1,0,0,0,0,0])]
cs=[len(list(combinations(range(6),k))) if 0<=k<=6 else 0 for k in range(9)];c=lambda k:cs[k] if 0<=k<len(cs) else 0
Ws={(i,k):wedge(M,k) for i,M in enumerate(Ms) for k in range(8)}
bdims=[c(k)+c(k-1) for k in range(9)];gdim=[c(k)+2*c(k-1) for k in range(9)];bd={};gd={};main={}
for i in range(3):
 bd[i]=[];main[i]=[]
 for k in range(9):
  D=s.zeros(bdims[k-1] if k else 0,bdims[k])
  if k and c(k-1):D[:c(k-1),c(k):]=Ws[i,k-1]-s.eye(c(k-1))
  bd[i].append(D);J=s.zeros(gdim[k],bdims[k]);J[:c(k),:c(k)]=s.eye(c(k))
  if c(k-1):
   if i==1:J[c(k):c(k)+c(k-1),c(k):]=s.eye(c(k-1))
   elif i==2:J[c(k)+c(k-1):,c(k):]=s.eye(c(k-1))
   else:J[c(k):c(k)+c(k-1),c(k):]=-Ws[2,k-1]*Ws[0,k-1];J[c(k)+c(k-1):,c(k):]=-Ws[0,k-1]
  main[i].append(J)
for k in range(9):
 D=s.zeros(gdim[k-1] if k else 0,gdim[k])
 if k and c(k-1):D[:c(k-1),c(k):c(k)+c(k-1)]=Ws[1,k-1]-s.eye(c(k-1));D[:c(k-1),c(k)+c(k-1):]=Ws[2,k-1]-s.eye(c(k-1))
 gd[k]=D
edim=[len(list(combinations(range(5),k)))+len(list(combinations(range(5),k-1))) if k>=1 else 1 for k in range(9)]
# combinations rejects negative only; k>5 is empty.
eds={};caps={}
for i,M in [(1,A),(2,B)]:
 eps=int(vs[i][0]);P=s.Matrix.hstack(eps*vs[i],s.eye(6)[:,1:]);ck('finite primitive split '+str(i),abs(P.det())==1);RM=P.inv()*M*P;R=RM[1:,1:];ck('finite block split '+str(i),RM==s.diag(s.ones(1),R));eds[i]=[];caps[i]=[]
 for k in range(9):
  aa=list(combinations(range(5),k));bb=list(combinations(range(5),k-1)) if k else [];D=s.zeros(edim[k-1] if k else 0,edim[k]);W=wedge(R,k-1) if k else s.zeros(0)
  if k and bb:D[:len(bb),len(aa):]=W-s.eye(len(bb))
  eds[i].append(D);split=s.zeros(edim[k],bdims[k]);fk=list(combinations(range(6),k));sk=list(combinations(range(6),k-1)) if k else [];norm=sum((W**j for j in range(mult[i])),s.zeros(*W.shape)) if bb else s.zeros(0)
  for j,I in enumerate(fk):
   if 0 not in I:split[aa.index(tuple(t-1 for t in I)),j]=1
   else:split[len(aa):,j]=eps*norm[:,bb.index(tuple(t-1 for t in I[1:]))]
  for j,I in enumerate(sk):
   if 0 not in I:split[len(aa)+bb.index(tuple(t-1 for t in I)),len(fk)+j]=1
  change=s.diag(wedge(P.inv(),k),wedge(P.inv(),k-1)) if k else wedge(P.inv(),0)
  caps[i].append(split*change)
  if k:ck('finite chainmap '+str((i,k)),eds[i][k]*caps[i][k]==caps[i][k-1]*bd[i][k])
ydim=[gdim[k]+2*edim[k]+2*(bdims[k-1] if k else 0) for k in range(9)];yd=[];jy=[]
for k in range(9):
 tar=gdim[k]+2*edim[k];tprev=gdim[k-1]+2*edim[k-1] if k else 0;D=s.zeros(ydim[k-1] if k else 0,ydim[k])
 if k:
  D[:tprev,:tar]=s.diag(gd[k],eds[1][k],eds[2][k]);F=s.zeros(tprev,2*bdims[k-1]);F[:gdim[k-1],:bdims[k-1]]=main[1][k-1];F[:gdim[k-1],bdims[k-1]:]=main[2][k-1];F[gdim[k-1]:gdim[k-1]+edim[k-1],:bdims[k-1]]=-caps[1][k-1];F[gdim[k-1]+edim[k-1]:,bdims[k-1]:]=-caps[2][k-1];D[:tprev,tar:]=F;D[tprev:,tar:]=s.diag(-bd[1][k-1],-bd[2][k-1])
 yd.append(D);J=s.zeros(ydim[k],bdims[k]);J[:gdim[k],:]=main[0][k];jy.append(J)
 if k:ck('cusp to complement chainmap '+str(k),yd[k]*jy[k]==jy[k-1]*bd[0][k])
ck('complement chain ranks',ydim==[3,22,71,132,155,118,57,16,2]);HY=homology(yd,ydim,'Y');ck('Y free ranks',[HY[k]['rank'] for k in range(9)]==[1,1,3,9,12,9,3,0,0] and all(not v['torsion'] for v in HY.values()))
HB=homology(bd[0],bdims,'B0');ck('boundary torsion only H3',[HB[k]['torsion'] for k in range(9)]==[[],[],[],[2],[],[],[],[],[]])
source=Path(__file__).with_name('reconstruct_V_cusp_06.json');dat=json.loads(source.read_text());S=s.Matrix([[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[-1,0,0,0,1,0],[1,0,0,0,0,1],[-1,0,0,0,0,0]])
cdim=dat['homology_ranks']+[0,0];kap=[];f0=[]
for k in range(9):
 F=s.Matrix(dat['collapse'][str(k)]['matrix'])*wedge(S.inv(),k) if k<=6 else s.zeros(0,c(k));kap.append(F);f0.append(F.row_join(s.zeros(cdim[k],c(k-1))))
DK,UK,VK=snf(kap[4]);ck('cusp degree4 quotient rank1',rank(DK)==9);psi=UK[-1,:];e=UK.inv()[:,-1];K=UK.inv()[:,:9];ck('psi and K',psi*kap[4]==s.zeros(1,c(4)) and (psi*e)[0]==1 and psi*K==s.zeros(1,9))
h3=HB[3];ind=next(i for i in range(h3['incoming_rank']) if abs(h3['incoming_smith'][i,i])==2);t=h3['incoming_left'][ind,:]*h3['outgoing_right_inverse'][h3['outgoing_rank']:,:];r=t*bd[0][4]/2;ck('integral Ext cocycle',all(v.q==1 for v in r));ck('full Ext relations',r*bd[0][5]==s.zeros(1,bdims[5]) and 2*r==t*bd[0][4])
# Actual degree4 homology gluing, then construct all missing secondary-class lifts.
H4=HB[4]['free'];j4=s.Matrix.vstack(HY[4]['proj']*jy[4]*H4,f0[4]*H4);DJ,UJ,VJ=snf(j4);ck('j4 primitive rank18',rank(DJ)==18 and all(abs(DJ[i,i])==1 for i in range(18)))
WC=solve_int(j4,s.zeros(HY[4]['rank'],9).col_join(K),'j4 K lift');X=H4*WC;T=solve_int(yd[5],jy[4]*X,'complement nullchain');ck('full secondary lifts',bd[0][4]*X==s.zeros(bdims[3],9) and f0[4]*X==K and yd[5]*T==jy[4]*X and r*X==s.zeros(1,9))
fc=[v.copy() for v in f0];fc[4]+=e*r
for k in range(1,9):ck('corrected cusp chainmap '+str(k),fc[k-1]*bd[0][k]==s.zeros(cdim[k-1],bdims[k]))
globdim=[ydim[k]+cdim[k]+(bdims[k-1] if k else 0) for k in range(9)];glob=[]
for k in range(9):
 D=s.zeros(globdim[k-1] if k else 0,globdim[k]);tar=ydim[k]+cdim[k];tp=ydim[k-1]+cdim[k-1] if k else 0
 if k:D[:ydim[k-1],:ydim[k]]=yd[k];D[:tp,tar:]=s.Matrix.vstack(jy[k-1],fc[k-1]);D[tp:,tar:]=-bd[0][k-1]
 glob.append(D)
ck('global chain ranks',globdim==[4,26,87,162,200,156,79,23,3]);HG=homology(glob,globdim,'M');ck('global free homology',[HG[k]['rank'] for k in range(9)]==[1,0,0,0,4,0,0,0,1] and all(not v['torsion'] for v in HG.values()));ck('global differential ranks',[HG[k]['outgoing_rank'] for k in range(1,9)]==[3,23,64,98,98,58,21,2])
out={'actor':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed)','utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','assertions':len(checks),'elapsed_seconds':time.monotonic()-start,'checks':checks,'cusp_input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'Y_differentials':{str(i):mat(v) for i,v in enumerate(yd)},'boundary_differentials':{str(i):mat(v) for i,v in enumerate(bd[0])},'jY':{str(i):mat(v) for i,v in enumerate(jy)},'kappa':{str(i):mat(v) for i,v in enumerate(kap)},'psi':mat(psi),'e':mat(e),'K':mat(K),'j4':mat(j4),'W':mat(WC),'X':mat(X),'T':mat(T),'r':mat(r),'t':mat(t),'global_differentials':{str(i):mat(v) for i,v in enumerate(glob)},'global_certificates':{str(k):{n:mat(v) if isinstance(v,s.MatrixBase) else v for n,v in h.items()} for k,h in HG.items()},'scope':'Fresh actual complement/finite-cap and cusp boundary chain models from printed P1.12, own freshly reconstructed marked cusp data, full missing secondary lifts/Ext relations, and every global differential/incoming Smith certificate. No global Poincare duality used in computation. Local geometric PL condition odd class is an explicit receiving-proof input. Same model-family implementation; no historical code imported.'}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2,default=str));print(json.dumps({'status':'PASS','assertions':len(checks),'seconds':out['elapsed_seconds'],'sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'output':str(p)}))
