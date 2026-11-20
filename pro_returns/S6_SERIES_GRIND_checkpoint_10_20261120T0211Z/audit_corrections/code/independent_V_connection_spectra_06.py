from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from itertools import combinations
from datetime import datetime,timezone
import json,time,hashlib
start=time.monotonic(); checks=[]
def ck(name,cond,data=None):
 if not bool(cond): raise AssertionError(name)
 checks.append({'name':name,'pass':True,'data':data})
l,x,t=s.symbols('l x t'); f=x**5+l**3*x+l**4
cols=[]; exacts=[]
for k in range(4):
 cs=s.symbols('c0:4'); rs=s.symbols('r0:5'); R=sum(rs[j]*x**j for j in range(5))
 poly=s.Poly(-x**k*s.diff(f,l)/2-f*sum(cs[j]*x**j for j in range(4))-f*s.diff(R,x)+s.diff(f,x)*R/2,x)
 sol=s.solve(poly.all_coeffs(),[*cs,*rs],dict=True)
 ck('unique polynomial reduction '+str(k),len(sol)==1)
 v=sol[0]; cols.append(s.Matrix([s.factor(v[c]) for c in cs])); exacts.append(s.factor(R.subs(v)))
 ck('exact differential identity '+str(k),s.factor(poly.as_expr().subs(v))==0)
G4=s.Matrix.hstack(*cols); pairs=list(combinations(range(4),2)); W=s.zeros(6)
for c,(i,j) in enumerate(pairs):
 for k in range(4):
  if k!=j:
   a,b=sorted((k,j));W[pairs.index((a,b)),c]+=(1 if k<j else -1)*G4[k,i]
  if k!=i:
   a,b=sorted((i,k));W[pairs.index((a,b)),c]+=(1 if i<k else -1)*G4[k,j]
Q=s.zeros(5,6)
for i,j in enumerate([0,1,2,4,5]): Q[i,j]=1
Q[2,3]=-3
incl=s.zeros(6,5)
for j,i in enumerate([0,1,2,4,5]): incl[i,j]=1
GW=Q*W*incl
printed=s.Matrix([
[-8*(625*l+48)/l,-8,10*l,s.Rational(75,2)*l**2,0],
[-s.Rational(125,2)/l,-4*(625*l+48)/l,8,0,s.Rational(75,2)*l**2],
[300/l**2,-375/l,0,-48,60*l],
[120/l**3,0,s.Rational(125,2)/l,4*(625*l+48)/l,-8],
[0,120/l**3,50/l**2,-s.Rational(125,2)/l,8*(625*l+48)/l]])/(3125*l+256)
for i in range(5):
 for j in range(5): ck('quotient Gauss-Manin '+str((i,j)),s.factor(GW[i,j]-printed[i,j])==0)
rel=s.Matrix([0,0,3,1,0,0]);ck('symplectic quotient relation horizontal',all(s.factor(v)==0 for v in W*rel))
A=s.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=s.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
I=s.eye(6);M1=A.T;M2=B.T;M0=(M1*M2).inv();N=M0-I
for M,m,name in [(M1,5,'M1'),(M2,4,'M2')]:
 ck(name+' power',M**m==I)
 for j in range(1,m): ck(name+' minimal '+str(j),M**j!=I)
ck('charpoly M1',s.expand(M1.charpoly(t).as_expr()-(t-1)**2*s.cyclotomic_poly(5,t))==0)
ck('charpoly M2',s.expand(M2.charpoly(t).as_expr()-(t-1)**2*(t+1)**2*(t*t+1))==0)
ck('nilpotent square',N*N==s.zeros(6));ck('nilpotent rank',N.rank()==3)
def sd(M):
 D=smith_normal_form(M,domain=s.ZZ);return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
ck('nilpotent primitive image',sd(N)==[1,1,1])
for M,K,inv,coin,name in [(M1,M2,0,[1,1,1,1,1],'homology'),(A,B,1,[1,1,1,1,1,2],'cohomology')]:
 ck(name+' fixed rank',6-s.Matrix.vstack(M-I,K-I).rank()==inv)
 ck(name+' coinvariant smith',sd(s.Matrix.hstack(M-I,K-I))==coin)
e0=s.eye(6)[:,0];ck('homology common functional',e0.T*M1==e0.T and e0.T*M2==e0.T)
v1=s.Matrix([1,3,-2,-1,2,0]);v2=-e0
for M,v,m in [(M1,v1,5),(M2,v2,4)]:
 ck('affine invariant numerator '+str(m),M*v==v)
 for j in range(1,m): ck('affine no fixed point '+str((m,j)),s.Rational(j*(e0.T*v)[0],m).q!=1)
ns=[n for n in range(1,19) if s.totient(n)<=6]; products=[]
def visit(i,left,rec):
 if i==len(ns):
  if left==0 and rec.get(1,0)>0:
   order=s.ilcm(*[n for n,k in rec.items() if k]) if len(rec)>1 else next(iter(rec))
   products.append({'multiplicities':dict(rec),'order':int(order),'complex':rec.get(1,0)%2==0 and rec.get(2,0)%2==0})
  return
 n=ns[i];d=int(s.totient(n))
 for k in range(left//d+1):
  if k:rec[n]=k
  else:rec.pop(n,None)
  visit(i+1,left-k*d,rec)
 rec.pop(n,None)
visit(0,6,{})
ck('spectral total',len(products)==38,len(products));ck('complex total',sum(p['complex'] for p in products)==19)
ck('spectral orders',sorted(set(p['order'] for p in products))==[1,2,3,4,5,6,8,10,12])
# Characteristic-number and Hodge consistency, not a cohomology derivation.
c2=s.symbols('c2');td=(3*c2-6)/720;sig=(3*c2+84)/45
ck('Todd-signature identity',s.simplify(sig-16*td-2)==0)
ck('Todd integer bound',[(i,16*i+2) for i in range(-10,11) if abs(16*i+2)<=4]==[(0,2)])
H=s.Matrix([[1,1,0,0,0],[0,2,1,0,0],[0,1,6,1,0],[0,0,1,2,0],[0,0,0,1,1]])
ck('Hodge Serre symmetry',all(H[p,q]==H[4-p,4-q] for p in range(5) for q in range(5)))
ck('Hodge total Euler',sum((-1)**(p+q)*H[p,q] for p in range(5) for q in range(5))==6)
ck('Hodge chi0',sum((-1)**q*H[0,q] for q in range(5))==0)
out={'actor':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed)','utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','assertions':len(checks),'elapsed_seconds':time.monotonic()-start,'checks':checks,'Gamma4':str(G4),'exact_primitives':[str(r) for r in exacts],'spectral_products':products,'scope':'Independent rational Gauss-Manin reduction and exterior quotient, exact integral monodromy and affine-power tests, complete finite spectral enumeration. Hodge/characteristic checks are consistency only, not cohomology proofs. Upper extension b, monodromy intertwiner existence and scalar alpha are not established here.'}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2));print(json.dumps({'status':'PASS','assertions':len(checks),'seconds':out['elapsed_seconds'],'output':str(path),'sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}))
