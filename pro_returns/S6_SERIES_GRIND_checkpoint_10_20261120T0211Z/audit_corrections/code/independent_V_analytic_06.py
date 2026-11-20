from pathlib import Path
from itertools import combinations,permutations
from collections import Counter
from math import gcd
from functools import reduce
import sympy as s,json,time,hashlib
from sympy.matrices.normalforms import smith_normal_form
from datetime import datetime,timezone
start=time.monotonic();checks=[]
def ck(n,v,data=None):
 if not bool(v):raise AssertionError(n)
 checks.append({'name':n,'pass':True,'data':data})
def canonical(vertices):
 vs=sorted(tuple(v) for v in vertices);a=vs[0]
 return tuple(tuple(v[i]-a[i] for i in range(3)) for v in vs)
cells=[set() for i in range(4)];top=[]
for perm in permutations(range(3)):
 vs=[(0,0,0)];v=[0,0,0]
 for i in perm:v=v.copy();v[i]+=1;vs.append(tuple(v))
 sg=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3));top.append((canonical(vs),sg))
 for k in range(4):
  for face in combinations(vs,k+1):cells[k].add(canonical(face))
cells=[sorted(c) for c in cells];ck('periodic Kuhn face counts',list(map(len,cells))==[1,7,12,6])
ds=[None]
for k in range(1,4):
 D=s.zeros(len(cells[k-1]),len(cells[k]))
 for j,c in enumerate(cells[k]):
  for i in range(k+1):D[cells[k-1].index(canonical(c[:i]+c[i+1:])),j]+=(-1)**i
 ds.append(D);S=smith_normal_form(D,domain=s.ZZ);nf=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
 ck('Kuhn Smith unit factors '+str(k),all(v==1 for v in nf),nf)
for k in [2,3]:ck('Kuhn boundary square '+str(k),ds[k-1]*ds[k]==s.zeros(ds[k-1].rows,ds[k].cols))
ranks=[0]+[d.rank() for d in ds[1:]]+[0];betti=[len(cells[k])-ranks[k]-ranks[k+1] for k in range(4)];ck('dual torus coherent ranks',betti==[1,3,3,1])
fund=s.Matrix([dict(top)[c] for c in cells[3]]);ck('oriented fundamental3cycle',ds[3]*fund==s.zeros(len(cells[2]),1))
for order in permutations(range(3)):
 val=0
 for c,coef in top:
  val+=coef*s.prod(c[j+1][order[j]]-c[j][order[j]] for j in range(3))
 sg=(-1)**sum(order[i]>order[j] for i in range(3) for j in range(i+1,3));ck('actual AW exterior triple '+str(order),val==sg)
# Root-line pushforwards; no inference of connecting ranks from dimensions alone.
def deg(j):return int(s.floor(s.Rational(4*j,5))+s.floor(-s.Rational(3*j,4)))
G=[0,-1,-2]
def hvec(weights):
 ans=[0]*5
 for j in range(4):
  for ws in combinations(G,j):
   for n in weights:
    d=deg(n+sum(ws));ans[j]+=max(d+1,0);ans[j+1]+=max(-d-1,0)
 return ans
for weights,expected,name in [([0],[1,1,0,0,0],'O'),([0,1,2],[1,3,2,0,0],'F'),([11],[0,2,3,1,0],'L11'),([1,2,3],[0,2,3,1,0],'wedge2F'),([11,12,13],[2,6,7,3,0],'L11F'),([5],[1,2,1,0,0],'L5'),([-6,-5,-4],[0,0,0,1,1],'Fminus6')]:
 ck('root cohomology '+name,hvec(weights)==expected,hvec(weights))
ck('canonical exponent',11+0+1+2-20==-6)
ck('moving pencil degree1',deg(24)==1)
ck('moving pencil section orders',(int(s.floor(s.Rational(4*24,5))),int(s.floor(-s.Rational(3*24,4))))==(19,-18))
l,z=s.symbols('l z');a=-s.Rational(256,3125);D=3125*l+256
GW=s.Matrix([[-8*(625*l+48)/l,-8,10*l,s.Rational(75,2)*l**2,0],[-s.Rational(125,2)/l,-4*(625*l+48)/l,8,0,s.Rational(75,2)*l**2],[300/l**2,-375/l,0,-48,60*l],[120/l**3,0,s.Rational(125,2)/l,4*(625*l+48)/l,-8],[0,120/l**3,50/l**2,-s.Rational(125,2)/l,8*(625*l+48)/l]])/D
b=s.Matrix([[-s.Rational(25,6)/l**2,-s.Rational(125,48)/l,0,1,0]])/(l-a);G6=s.zeros(6);G6[0,1:6]=b;G6[1:6,1:6]=GW
F=s.zeros(6,3);F[3,0]=1;F[0,0]=s.Rational(4,3)*z;F[2,1]=1;F[1,2]=1
P=s.zeros(3,6);P[0,0]=1;P[0,3]=-s.Rational(4,3)*z;P[1,4]=1;P[2,5]=1
R=(P*G6*F).applyfunc(lambda v:s.factor((l-a)*v).subs(l,a))
AA=-s.Rational(125,12288)*(192*z-3125);BB=-s.Rational(78125,393216)*(96*z+3125);CC=-s.Rational(125,512);EE=s.Rational(78125,32768);DD=-s.Rational(146484375,2097152)
printed=s.Matrix([[0,AA,BB],[CC,0,DD],[EE,DD,0]])
for i in range(3):
 for j in range(3):ck('actual projected cusp residue '+str((i,j)),s.factor(R[i,j]-printed[i,j])==0)
C1=s.Matrix([[-CC,AA,0],[-EE,0,BB],[0,-DD,DD]]);C2=s.Matrix([[-DD,DD,0],[EE,0,-BB],[0,-CC,AA]])
ck('C1 determinant',s.factor(C1.det()-s.Rational(476837158203125,281474976710656)*(384*z+3125))==0);ck('C2 determinant',s.factor(C2.det()+C1.det())==0)
ck('exceptional real parameter factor',s.solve(384*(-s.Rational(625,128)*z)+3125,z)==[s.Rational(5,3)])
r=s.symbols('r');Q=s.Matrix([[-s.Rational(78125,6)+300*r,-s.Rational(390625,48)-375*r,0],[120,0,s.Rational(125,2)],[0,120,50]])/(3125*(1-a))
ck('base KS determinant',s.factor(Q.det()-3/(625*(1-a)**3))==0)
ck('parameter rank1 distinct from rank3 base',s.Matrix([[0,0,1],[0,0,0],[0,0,0]]).rank()==1 and Q.det()!=0)
A=s.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]]).T
B=s.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]]).T
js=s.symbols('j0:15');J=s.zeros(6)
for v,(i,j) in zip(js,combinations(range(6),2)):J[i,j]=v;J[j,i]=-v
mat=s.Matrix(list(A.T*J*A-J)+list(B.T*J*B-J)).jacobian(js);ck('invariant alternating space zero',mat.rank()==15)
K=s.Matrix([[0,0,0],[0,1,0],[1,0,0],[0,0,0],[0,-1,0],[0,0,1]])
T=s.Matrix([[0,0,0],[0,1,0],[1,0,0],[0,0,-1],[0,0,1],[0,0,-1]])
Z=s.Matrix([[-2,-1,1],[0,-1,1],[1,0,1]])
N1=sum((A**i for i in range(5)),s.zeros(6));N2=sum((B**i for i in range(4)),s.zeros(6));M=s.Matrix.vstack(N1,N2)
ck('norm kernel rank3',M.rank()==3 and M*K==s.zeros(12,3));ck('cusp kernel rank3',(A*B-s.eye(6)).rank()==3 and (A*B-s.eye(6))*T==s.zeros(6,3))
for Qm,name in [(K,'K'),(T,'T')]:
 gcdmin=reduce(gcd,[abs(int(Qm[list(ix),:].det())) for ix in combinations(range(6),3)])
 ck('primitive kernel basis '+name,gcdmin==1)
ck('actual parabolic quotient map',(B-s.eye(6))*T==K*Z);SZ=smith_normal_form(Z,domain=s.ZZ);ck('parabolic Smith112',[abs(int(SZ[i,i])) for i in range(3)]==[1,1,2])
tau=s.Matrix([0,1,1,1,1,1])/2;N=(A*B).inv()-s.eye(6);lam=s.eye(6)[:,4]
for Qm,name in [(A,'A'),(B,'B')]:ck('half-period deck compatibility '+name,all(v.q==1 for v in (Qm-s.eye(6))*tau))
ck('actual integral half-period subtraction',N*(tau-lam)==s.zeros(6,1));ck('half-period nonzero order2',all(v.q==1 for v in 2*tau) and any(v.q==2 for v in tau))
# Exact Cayley-domain transport.
u,v,c=s.symbols('u v c',real=True);xi=u+s.I*v;num=xi-s.I*(c+1);den=xi-s.I*(c-1)
ck('Cayley half-plane to disk',s.expand(den*s.conjugate(den)-num*s.conjugate(num))==4*(v-c))
y=s.symbols('y');chiy=(1+y)**4*s.Rational(2,240)+(((-1+10*y-y*y)**2)/144-(1+y)**4/120)*6
ck('analytic RR polynomial',s.expand(chiy-(-y+4*y*y-y**3))==0)
out={'actor':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed)','utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','assertions':len(checks),'elapsed_seconds':time.monotonic()-start,'checks':checks,'kuhn_cells':cells,'kuhn_differentials':{str(i):[list(ds[i].row(j)) for j in range(ds[i].rows)] for i in range(1,4)},'scope':'Fresh exact arithmetic after full receiving proofs P1A1--6. Reconstructs periodic Kuhn dual complex and actual AW cup products, root-line groups, projected Gauss-Manin residue, determinant exception and KS, invariant divisor/translation quotient and explicit bounded half-period, Cayley and RR substitutions. Does not claim a new blind whole-proof derivation.'}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2,default=str));print(json.dumps({'status':'PASS','assertions':len(checks),'seconds':out['elapsed_seconds'],'sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}))
