from pathlib import Path
import sympy as s,json,time,hashlib
from datetime import datetime,timezone
start=time.monotonic(); checks=[]
def ck(n,v,data=None):
 if not bool(v):raise AssertionError(n)
 checks.append({'name':n,'pass':True,'data':data})
l=s.symbols('l');ls=-s.Rational(256,3125)
GW=s.Matrix([
[-8*(625*l+48)/l,-8,10*l,s.Rational(75,2)*l**2,0],
[-s.Rational(125,2)/l,-4*(625*l+48)/l,8,0,s.Rational(75,2)*l**2],
[300/l**2,-375/l,0,-48,60*l],
[120/l**3,0,s.Rational(125,2)/l,4*(625*l+48)/l,-8],
[0,120/l**3,50/l**2,-s.Rational(125,2)/l,8*(625*l+48)/l]])/(3125*l+256)
R=GW.applyfunc(lambda z:s.factor(z*(l-ls)).subs(l,ls));ck('quotient nilpotent residue',R*R==s.zeros(5));ck('quotient residue rank2',R.rank()==2)
for j,expected in zip([2,1,0,-1,-2],[[-2],[-1],[],[0],[1]]):
 ps=[p for p in range(-10,11) if 3*j+3+4*p>=0 and -4*j-1-5*p>=0]
 ck('root regular monomials '+str(j),ps==expected,ps)
for j in range(-2,3):
 deg=s.floor(s.Rational(4*j,5))+s.floor(-s.Rational(3*j,4));ck('coarse degree '+str(j),deg==(0 if j==0 else -1),int(deg))
a,b,c,d=s.symbols('a b c d');brow=s.Matrix([[a/l**2,b/l,0,c,d*l]])/(l-ls);br=s.Matrix([[a/ls**2,b/ls,0,c,d*ls]])
U=(br*R).jacobian([a,b,c,d]);ck('upper nilpotent constraints rank2',U.rank()==2)
b1=s.Matrix([-s.Rational(25,6),-s.Rational(125,48),1,0]);b2=s.Matrix([s.Rational(5,3),-s.Rational(25,3),0,1]);ck('two solution directions',U*b1==s.zeros(5,1) and U*b2==s.zeros(5,1));ck('directions independent',s.Matrix.hstack(b1,b2).rank()==2)
cob=(-48*b1+60*b2)/3125;cb=brow.subs(dict(zip([a,b,c,d],cob)))
ck('full connection coboundary',all(s.factor(cb[0,i]-GW[2,i])==0 for i in range(5)))
ck('first direction not coboundary',s.Matrix.hstack(b1,cob).rank()==2)
r1=br.subs(dict(zip([a,b,c,d],b1)));R6=s.zeros(6);R6[0,1:6]=r1;R6[1:6,1:6]=R
ck('full residue rank3',R6.rank()==3);ck('full square zero',R6*R6==s.zeros(6))
v=s.Matrix([-s.Rational(4096,1171875),s.Rational(64,1875),1,0,0]);ck('displayed kernel vector',R*v==s.zeros(5,1));ck('kernel contraction', (r1*v)[0]==s.Rational(625,192));ck('normalization scalar',s.Rational(625,192)/s.Rational(4,3)*2==s.Rational(625,128))
A=s.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=s.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
xs=s.symbols('x0:36');X=s.Matrix(6,6,xs);eq=s.Matrix(list(X*A-A*X)+list(X*B-B*X)).jacobian(xs)
ck('simultaneous centralizer dimension1',36-eq.rank()==1);ck('scalar spans centralizer',eq*s.Matrix(list(s.eye(6)))==s.zeros(72,1))
# Actual finite-cap group abelianization from printed affine numerator, independent Smith.
from sympy.matrices.normalforms import smith_normal_form
for M,v,m,factors in [(A.T,s.Matrix([1,3,-2,-1,2,0]),5,[1,1,1,1,1]),(B.T,s.Matrix([-1,0,0,0,0,0]),4,[1,1,1,1,2])]:
 mat=(M-s.eye(6)).col_join(s.zeros(1,6));mat=mat.row_join((-v).col_join(s.Matrix([m])))
 D=smith_normal_form(mat,domain=s.ZZ);got=[abs(int(D[i,i])) for i in range(7) if D[i,i]]
 ck('finite cap H1 '+str(m),got==factors,got)
out={'actor':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed)','utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','assertions':len(checks),'elapsed_seconds':time.monotonic()-start,'checks':checks,'residue':str(R),'scope':'After full receiving P1.15 proof: exact root regularity, coarse H1 degrees, full upper-extension nilpotent quotient, nontrivial class, scalar normalization, simultaneous centralizer; also complete finite-cap H1 relation matrices P1.3. Does not replay historical code.'}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2));print(json.dumps({'status':'PASS','assertions':len(checks),'seconds':out['elapsed_seconds'],'sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}))
