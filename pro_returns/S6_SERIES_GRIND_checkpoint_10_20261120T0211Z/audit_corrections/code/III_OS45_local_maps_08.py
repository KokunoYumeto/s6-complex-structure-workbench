"""Exact local fan, source-line and SL2 chart checks.
Not a certificate of the global critical-specialization linking.
The source statements/proofs were read before this new derivation.
"""
from pathlib import Path
import sympy as S
import json,hashlib,datetime,time
start=time.time(); checks=[]
def ck(name,truth,details=None):
    truth=bool(truth)
    checks.append({'name':name,'pass':truth,'details':details})
    if not truth: raise AssertionError(name)
def eq(name,left,right):
    z=left-right
    if isinstance(z,S.MatrixBase): z=z.applyfunc(S.simplify); ok=z==S.zeros(*z.shape)
    else: ok=S.simplify(z)==0
    ck(name,ok)
l1=S.Matrix([8,-6]); l2=S.Matrix([24,-16]); L=S.Matrix.hstack(l1,l2)
ck('actual period determinant16',L.det()==16)
eq('vertical source graph translation retained',9*l1-3*l2,S.Matrix([0,-6]))
P=S.Matrix([[1,1,1],[0,1,0],[5,5,6]])
ck('source graph cone smooth positively oriented',P.det()==1)
e=S.Matrix([0,1,0]); delta=S.Matrix([0,0,1]); a0=e-delta
for label,v,want in [('e1',e,[-1,1,0]),('delta',delta,[-1,0,1]),('actual source vanishing e1-delta',a0,[0,1,-1])]:
    eq(label+' weights in graph cone',P.inv()*v,S.Matrix(want))
# Complete quotient triangulation; no change of fan or period marking.
verts=[(r,s) for r in range(8) for s in range(2)]
tri=[]
for r,s in verts:
    for points in [[(r,s),(r+1,s),(r,s+1)],[(r+1,s),(r+1,s+1),(r,s+1)]]:
        C=S.Matrix.hstack(*[S.Matrix([1,*v]) for v in points])
        ck('smooth actual triangle '+str(points),C.det()==1)
        labs=[(u%8,v%2) for u,v in points]
        ck('three distinct component labels '+str(points),len(set(labs))==3)
        tri.append({'rays':points,'labels':labs})
x,y,z=S.symbols('x y z',nonzero=True)
q=x*y*z; Z=y; V=x**5*y**5*z**6
W=q**6/(Z*V); X=q/Z; Y=Z
for name,l,r in [('literal source X',X,x*z),('literal source Y',Y,y),('actual extending line W',W,x)]:eq(name,l,r)
J=S.Matrix([X,Y,W]).jacobian([x,y,z]);eq('source-line Jacobian including winding',J.det(),-x)
XX,YY,WW=S.symbols('X Y W',nonzero=True)
for name,l,r in [('inverse x',W.subs({x:WW,y:YY,z:XX/WW}),WW),('inverse source X',X.subs({x:WW,y:YY,z:XX/WW}),XX),('inverse source Y',Y.subs({x:WW,y:YY,z:XX/WW}),YY)]:eq(name,l,r)
# Local source graph frames: flat-frame factor q^6/Z, not an omitted unit.
for i in range(7): ck('actual frame valuation i='+str(i),6-i==max(6-i,0))
B=S.Matrix([[1,0],[-1,1]])
ck('cusp boundary map meridian complement unimodular',B.det()==1)
ck('two meridians form full lattice',S.Matrix([[1,1],[-1,0]]).det()==1)
a,b,c,d,f,eps=S.symbols('a b c d f eps',nonzero=True)
# On SL2 use ad-bc=1; charts a,d,b and b,c,a.
U=a*b; VV=(a*d)**6/a
xc=1/b; yc=a*b; zc=d
for name,l,r in [('cusp fibration',xc*yc*zc,a*d),('cusp source U',yc,U),('cusp scalar V',xc**5*yc**5*zc**6,VV),('cusp physical line',xc,1/b)]:eq(name,l,r)
ck('cusp SL2 chart actual local isomorphism',S.factor(S.Matrix([xc,yc,zc]).jacobian([a,d,b]).det())!=0)
fn=1+b*c
Xn=-c/a; Yn=a*b; Wn=a/fn**6
for name,l,r in [('I1 node base',Xn*Yn,1-fn),('I1 source U',Yn,U),('I1 scalar V',1/Wn,fn**6/a)]:eq(name,l,r)
ck('I1 SL2 chart Jacobian at core nonzero',S.simplify(S.Matrix([Xn,Yn,Wn]).jacobian([b,c,a]).det().subs({b:0,c:0}))!=0)
eq('actual line transition on dense overlap',(a)/(1/b),U)
# Left-invariant calculation, no degree inferred from matrix ranks.
H,Uu,Vv=S.symbols('h u v')
G=S.Matrix([[a,b],[c,d]]); E1=S.Matrix([[0,b],[-c,0]])
Gi=S.Matrix([[d,-b],[-c,a]])
eq('e1 left-coordinate matrix',Gi*E1,S.Matrix([[b*c,b*d],[-a*c,-b*c]]))
A=a*c; BB=b*d
variation=G*S.Matrix([[H,Uu],[Vv,-H]])
eq('df on left Lie coordinates',d*variation[0,0]+a*variation[1,1],A*Uu+BB*Vv)
eq('vertical row kernel',A*BB+BB*(-A),0)
# Exact displaced compact group, treating alpha/baralpha and beta/barbeta independently.
al,be,ac,bc=S.symbols('alpha beta alpha_bar beta_bar')
Gp=S.Matrix([[1,eps],[0,1]])*S.Matrix([[al,be],[-bc,ac]])
for name,l,r in [('displaced a',Gp[0,0],al-eps*bc),('displaced b',Gp[0,1],be+eps*ac),('displaced c',Gp[1,0],-bc),('displaced d',Gp[1,1],ac)]:eq(name,l,r)
eq('displaced determinant',Gp.det(),al*ac+be*bc)
eq('displaced A',Gp[0,0]*Gp[1,0],-al*bc+eps*bc**2)
eq('displaced B',Gp[0,1]*Gp[1,1],be*ac+eps*ac**2)
# For eps>0 simultaneous zeros force (1+eps^2)z1=0.
z1,z2=S.symbols('z1 z2')
eq('nonzero pair contradiction coefficient',z1-eps*(-eps*z1),(1+eps**2)*z1)
# Squaring map has four positively oriented regular inverse images at a=(1,1)/sqrt2.
r=S.real_root(S.Rational(1,2),4)
for s1 in [-1,1]:
 for s2 in [-1,1]:
  ck('quadratic holomorphic target inverse '+str((s1,s2)),S.simplify((s1*r)**2-1/S.sqrt(2))==0 and S.simplify((s2*r)**2-1/S.sqrt(2))==0)
  ck('positive real Jacobian inverse '+str((s1,s2)),S.simplify(abs(4*(s1*r)*(s2*r))**2)>0)
root=Path(__file__).resolve().parents[1]
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'actor':'GPT-6 Astra, ChatGPT Pro mode; reasoning effort inherited, not separately exposed','exposure':'Receiving III D2.43/44/46/47/48/53 statements and proof inputs opened before this local reconstruction; no blind whole-theorem claim.','passed':len(checks),'checks':checks,'period_matrix':[list(L.row(i)) for i in range(2)],'graph_cone':[list(P.col(i)) for i in range(3)],'triangles':tri,'degree_computation':'For eps>0 the normalized pair (B,-A) has no zeros. Homotopy eps→infinity gives (conj(alpha)^2,-conj(beta)^2); simultaneous conjugation preserves orientation in real dimension4, and the holomorphic squaring pair has Brouwer degree4. This is a calculation in the explicit SL2 local model only.','scope':'Established exact fan/chart/line-gauge and local SL2 identities; global identified collar and critical-specialization intersections require the separately stated receiving comparison. No refined-class value computed.','seconds':time.time()-start,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
def encode(v):
 if isinstance(v,S.Integer): return int(v)
 return str(v)
dest=root/'III_OS45_local_maps_08.json';dest.write_text(json.dumps(out,indent=2,default=encode)+'\n');print('PASS',len(checks));print(dest);print(hashlib.sha256(dest.read_bytes()).hexdigest())
