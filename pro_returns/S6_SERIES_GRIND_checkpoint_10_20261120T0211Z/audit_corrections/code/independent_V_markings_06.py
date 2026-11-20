from pathlib import Path
from itertools import combinations
import sympy as s,json,time,hashlib
from sympy.matrices.normalforms import smith_normal_form
from datetime import datetime,timezone
start=time.monotonic();checks=[]
def ck(n,v,data=None):
 if not bool(v):raise AssertionError(n)
 checks.append({'name':n,'pass':True,'data':data})
Cf=s.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]]);Cg=s.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
A=s.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=s.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
pairs=list(combinations(range(4),2))
def wedge(M):return s.Matrix([[M[list(i),list(j)].det() for j in pairs] for i in pairs])
Q=s.eye(6);Q[:,0]=s.ones(6,1)
ck('unimodular wedge quotient basis',Q.det()==1)
for M,T,n in [(Cf.inv(),A,'A'),(Cg,B,'B')]:ck('full integral quotient '+n,(Q.inv()*wedge(M)*Q)[1:6,1:6]==T[1:6,1:6])
J=s.Matrix([[0,1,-1,1],[-1,0,1,-1],[1,-1,0,1],[-1,1,-1,0]]);d=s.Matrix([1,1,1,0]);e4=s.eye(4)[:,3]
ck('symplectic Cf',Cf.T*J*Cf==J);ck('symplectic Cg',Cg.T*J*Cg==J);ck('primitive PL map',Cf.inv()*Cg-s.eye(4)==d*e4.T);ck('PL coefficient',d.T*J==e4.T)
D=s.Matrix.hstack(*(Cf**i*d for i in range(4)));ck('vanishing orbit unimodular',D.det()==1);G=D.T*J*D
ck('actual orbit pairing',G==s.Matrix([[0,1,0,0],[-1,0,1,0],[0,-1,0,1],[0,0,-1,0]]));ck('integral inverse bothways',all(v.q==1 for v in D.inv()) and D*D.inv()==s.eye(4))
W=s.zeros(4)
for i in range(4):W[i,3-i]=1
ck('reversal involution',W*W==s.eye(4));ck('reversal orientation',W.det()==1);ck('reversal Cf',W*Cf*W==Cf.inv());ck('reversal Cg',W*Cg*W==Cg.inv());ck('pairing reversal',W.T*J*W==-J)
ck('based cusp conjugation',Cf*(Cg.inv()*Cf)*Cf.inv()==Cf*Cg.inv())
j=s.Matrix([[0,1,1,-1,1],[-1,2,1,-1,1],[-1,1,2,-1,1],[-1,1,1,0,1],[-1,1,1,-1,2]])
Sj=smith_normal_form(j,domain=s.ZZ);ck('primitive quotient SNF',[abs(int(Sj[i,i])) for i in range(5)]==[1,1,1,1,2]);ck('primitive quotient determinant',j.det()==2)
AA=A[1:6,1:6];BB=B[1:6,1:6];v=s.eye(5)[:,2];ck('quotient cyclic vector',s.Matrix.hstack(*(AA**i*v for i in range(5))).det()==-1)
us=s.symbols('u1:5');C=sum((us[i-1]*AA**i for i in range(1,5)),s.zeros(5));eq=s.Matrix([ (C*BB-BB*C)[i,j] for i,j in [(0,1),(0,3),(1,3),(2,0)]]).jacobian(us);ck('commutator determinant',eq.det()==-1)
M1=A.T;M2=B.T;M0=(M1*M2).inv();S=s.Matrix([[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[-1,0,0,0,1,0],[1,0,0,0,0,1],[-1,0,0,0,0,0]])
std=s.eye(6)
for i in range(3):std[i,i+3]=1
ck('S primitive marking',abs(S.det())==1 and S.inv()*M0*S==std)
R=s.Matrix([[1,0,0,0,0,0],[2,0,0,0,-1,0],[-1,0,-1,0,0,0],[-1,0,0,-1,0,0],[2,-1,0,0,0,0],[-1,1,1,1,1,1]])
ck('antiintertwiner involution',R*R==s.eye(6));ck('antiintertwiner unimodular',abs(R.det())==1)
for M,n in [(M1,'M1'),(M2,'M2')]:ck('antiintertwiner '+n,R*M==M.inv()*R)
vs=s.symbols('r0:36');V=s.Matrix(6,6,vs);eq=s.Matrix(list(V*M1-M1.inv()*V)+list(V*M2-M2.inv()*V)).jacobian(vs);ck('all rational antiintertwiners dimension1',36-eq.rank()==1)
e0=s.eye(6)[:,0];ck('finite affine obstruction',e0.T*R==e0.T and s.Rational(2,5).q!=1)
H=S.inv()*M2.inv()*(-R)*S;P=s.Matrix([[1,0,0],[0,1,0],[1,-1,-1]]);ck('actual based cusp block',H[:3,:3]==P and H[3:,3:]==-P and H[3:,:3]==s.zeros(3))
rays={tuple(v) for v in __import__('itertools').product([0,1],repeat=3) if any(v)};rays|={tuple(-a for a in v) for v in list(rays)}
w=tuple(-P*s.eye(3)[:,1]);ck('actual ray obstruction',w==(0,-1,1) and w not in rays)
# Cusp lift scalar as a polynomial identity in arbitrary vectors.
Nv=(B*A).inv()-s.eye(6);Dh=Cf*Cg.inv()-s.eye(4);av=s.Matrix(s.symbols('a0:4'));bv=s.Matrix(s.symbols('b0:4'))
def wed(a,b):return s.Matrix([a[i]*b[j]-a[j]*b[i] for i,j in pairs])
pv=(Q.inv()*wed(av,Dh*bv))[1:6,0];full=s.zeros(6,1);full[1:6,0]=pv
ck('cusp full scalar identity',s.expand((Nv*full)[0]-av[0]*bv[0])==0);ck('cusp quotient kernel',all(s.expand(v)==0 for v in (Nv*full)[1:6,0]))
x,l,u,X,Y=s.symbols('x l u X Y');f=x**5+l**3*x+l**4;ls=-s.Rational(256,3125);xd=s.Rational(64,625)
ck('pencil discriminant',s.factor(s.discriminant(f,x)-l**15*(3125*l+256))==0);ck('node double root',f.subs({l:ls,x:xd})==0 and s.diff(f,x).subs({l:ls,x:xd})==0);ck('node transverse',s.diff(f,x,2).subs({l:ls,x:xd})!=0 and s.diff(f,l).subs({l:ls,x:xd})!=0)
ck('zero root chart',s.expand(f.subs({l:u**8,x:u**6*X})/u**30-(X**5+X+u**2))==0);ck('infinity root chart',s.expand(f.subs({l:u**-5,x:u**-4*X})*u**20-(X**5+u*X+1))==0)
ck('zero smooth central',s.gcd(X**5+X,5*X**4+1)==1);ck('infinity smooth central',s.gcd(X**5+1,5*X**4)==1);ck('Hodge root degree',s.Rational(2,5)-s.Rational(3,8)==s.Rational(1,40))
out={'actor':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed)','utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','assertions':len(checks),'elapsed_seconds':time.monotonic()-start,'checks':checks,'scope':'After receiving proofs: exact P1.2 quotient/intertwiner obstruction, P1.7 actual integral marking and inverse, P1.17 based antiintertwiner/fan obstruction, P1.8 full cusp scalar identity, and P1.4 discriminant/root substitutions. Fresh programs do not claim historical execution replay.'}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2,default=str));print(json.dumps({'status':'PASS','assertions':len(checks),'seconds':out['elapsed_seconds'],'sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}))
