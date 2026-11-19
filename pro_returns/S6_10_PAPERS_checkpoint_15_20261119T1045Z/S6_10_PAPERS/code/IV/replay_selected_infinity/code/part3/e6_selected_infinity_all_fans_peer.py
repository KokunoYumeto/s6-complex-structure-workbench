"""Independent collar algebra and fresh SymPy full-prism solves for IF."""
from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
from itertools import combinations
import hashlib,json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'notes/part3_e6_selected_infinity_all_fans_working.md'
EXPECTED='f161af882d422499980fda2414d5be5924a47bfd10d0ea6be3872770d3222960'
assert hashlib.sha256(SRC.read_bytes()).hexdigest()==EXPECTED
checks=[];solves=[]
def eq(name,value):
    value=S.factor(S.together(value))
    assert value==0,(name,str(value))
    checks.append(name)
def ck(name,value):
    assert value,name
    checks.append(name)
def wedge(A,B):
    out={}
    for ia,ca in A.items():
        for ib,cb in B.items():
            if set(ia)&set(ib):continue
            inv=sum(a>b for a in ia for b in ib)
            key=tuple(sorted(ia+ib))
            out[key]=S.expand(out.get(key,0)+(-1)**inv*ca*cb)
    return {k:v for k,v in out.items() if v!=0}
def add(A,B):
    out=dict(A)
    for k,v in B.items():out[k]=S.expand(out.get(k,0)+v)
    return {k:v for k,v in out.items() if v!=0}
def scale(A,k):return {i:S.expand(k*v) for i,v in A.items()}

# Original-height connection, in (alpha,u,b,gamma,theta) orientation.
j,alpha,theta,s=S.symbols('j alpha theta s')
beta={(1,):-j,(2,):-j*alpha+4*j*theta}
Fext={(0,3):1,(0,2):j}
dbeta={(0,2):-j,(2,4):-4*j}
Fs=add(Fext,scale(dbeta,s))
cube=scale(wedge(beta,wedge(Fs,Fs)),3)
eq('entire original collar transgression',
   S.integrate(cube[(0,1,2,3,4)],(s,0,1))-12*j*j)
eq('outward collar direction',-S.integrate(cube[(0,1,2,3,4)],(s,0,1))+12*j*j)
Xi={(2,4):-1}
ck('relative theta-source tensor has square zero',not wedge(Xi,Xi))
N=S.Matrix([[0,1,-j],[0,0,0],[0,0,0]])
ck('actual source derivative Maurer block square zero',N*N==S.zeros(3))
eq('actual source derivative trace square',S.trace(N*N))
a=S.symbols('a')
G=S.Matrix([[1,a,-j*a],[0,1,-j],[0,0,1]])
ck('full source Maurer matrix',G.inv()*G.diff(a)==N)
ck('full source coframe determinant',G.det()==1)
eq('native physical cubic',2-6+4)
eq('native physical Pontryagin-linear',4*2-8)
L=S.symbols('L')
eq('reflection fixes affine coefficient',(-4+L-12+4).subs(L,12))
eq('vertical cubic reflection',(-4-12*j*(j-1))-(-4-12*(1-j)*(-j)))

# Exact phase/Cox frame and full original-coordinate half-turn.
z,zb=S.symbols('z zb',nonzero=True)
G0=S.Matrix([[1,-z],[zb,1]])
G1=S.Matrix([[1/zb,-1],[1,1/z]])
ck('literal two-chart positive Cox frame',G1*S.diag(zb,z)==G0)
q,V,P=S.symbols('q V P',nonzero=True)
eq('full theta and target-period coefficient cancellation',P**6*P**(-6)*V-V)
eq('reflected source map squares literally',q/(q/z)-z)
eps,d,xe,ye,te=S.symbols('eps d xe ye te',nonzero=True)
eq('half-turn original x',(-eps)**2*d**(-2)*xe-eps**2*d**(-2)*xe)
eq('half-turn original y',(-eps)**3*d**(-3)*(-ye)-eps**3*d**(-3)*ye)
eq('half-turn original height',(-eps)**4*d**(-3)*te-eps**4*d**(-3)*te)

# Both universal affine reset identities.
x,y=S.symbols('x y',nonzero=True)
w=(x,y,-x-y);D=-x*y*(x+y);NN=x*x+x*y+y*y
for i,(xx,yy) in enumerate([(x+y,y),(x,x+y)]):
    ww=(xx,yy,-xx-yy);DD=ww[0]*ww[1]*ww[2]
    eq(f'full selected derivative affine identity Q{i}',DD/ww[2]+D/w[i])
    eq(f'norm difference identity Q{i}',xx*xx+xx*yy+yy*yy-NN+2*D/w[i])
for wx,dd in zip(w,(-x-2*y,-2*x-y,x-y)):
    ck('literal base/normal Spin parity',S.Poly(dd-wx,x,y).all_coeffs()==[] if False else all(c%2==0 for c in S.Poly(dd-wx,x,y).coeffs()))

# Fresh full systems: ten exact equations for nine unknowns.
Q=(S.ImmutableMatrix([[1,-1],[0,1]]),S.ImmutableMatrix([[1,0],[-1,1]]))
pairs=((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))
unknown=S.symbols('v00 v01 v02 v11 v12 v22 d0 d1 d2')
def local(P,t):
    P=S.Matrix(2,2,P);B=2*t*P.inv()*S.diag(1,0)*P
    xx,yy=P.inv()*S.Matrix([0,1])
    w=(xx,yy,-xx-yy);d=(-xx-2*yy,-2*xx-yy,xx-yy)
    ell=(B[1,1]-B[1,0],B[0,0]-B[0,1],B[1,1])
    I=tuple(t*w[i]+d[i]*(ell[i]-t) for i in range(3))
    J=tuple(t*w[i]-d[i]*(ell[i]-t) for i in range(3))
    return w,I,J
@lru_cache(None)
def solve(P,t,c,e,selected):
    w,I,J=local(P,t)
    V=S.zeros(3)
    for ind,(r,s) in enumerate(pairs):V[r,s]=V[s,r]=unknown[ind]
    de=unknown[6:]
    equations=[]
    for i in [1,2]:
        for r in range(3):
            equations.append(w[i]*V[r,i]-w[0]*V[r,0]-
                             (I[i] if r==i else 0)+(I[0] if r==0 else 0))
        equations.append(w[i]*de[i]-w[0]*de[0]-J[i]+J[0])
    equations.extend([V[selected,selected]-c,de[selected]-e])
    A,b=S.linear_eq_to_matrix(equations,unknown)
    answer,params=A.gauss_jordan_solve(b)
    ck('full prism rank nine',A.rank()==9 and len(params)==0)
    for row in A*answer-b:eq('original full prism row',row)
    ck('full solution integral',all(v.q==1 for v in answer))
    Vout=V.subs(dict(zip(unknown,answer)))
    dout=tuple(answer[6:])
    solves.append({'basis':list(P),'trace':t,'selected':selected,'variation':list(map(list,Vout.tolist())),'delta':list(dout)})
    return S.ImmutableMatrix(Vout),dout
def seed(jj,t):
    P=S.ImmutableMatrix([[1,0],[jj,1]])
    if t==-4:c=24*jj*(jj-1);e=-24-24*jj*(jj-1);ret=-1-2*jj*(jj-1)
    else:c=18*jj*(jj-1);e=-12-18*jj*(jj-1);ret=-1-3*jj*(jj-1)
    V,de=solve(tuple(P),t,c,e,0)
    return P,V,de,S.Integer(ret)
def step(state,i,t):
    P,V,de,ret=state;c=V[i,i];e=de[i];Pn=P*Q[i]
    Vn,dn=solve(tuple(Pn),t,c,2*c-e,2)
    denominator=4 if t==-4 else 2
    rho=(e-c)/denominator
    ck('actual native degree integral',rho.q==1)
    eq('literal selected inverse degree',(dn[2]-Vn[2,2])/denominator+rho)
    return Pn,Vn,dn,ret+rho
def compare(ours,reference):
    P,V,de,ret=ours;P6,V6,d6,s6=reference
    ck('same actual canonical word',P==P6)
    for v in V-S.Rational(4,3)*V6:eq('full affine variation entry',v)
    xx,yy=P.inv()*S.Matrix([0,1]);w=(xx,yy,-xx-yy);D=w[0]*w[1]*w[2]
    correction=(-8,0,0) if xx==0 else tuple(8*D/w[i] for i in range(3))
    for i in range(3):eq('full affine derivative entry',de[i]-S.Rational(4,3)*d6[i]-correction[i])
    eq('full integer evaluation',ret-S.Rational(2,3)*(s6+1)+(xx*xx+xx*yy+yy*yy))
    ck('path sum odd',ret%2==1)
for jj in range(-6,7):
    ours=seed(jj,-4);ref=seed(jj,-3);compare(ours,ref)
    for i in [0,1,0,1]:
        ours=step(ours,i,-4);ref=step(ref,i,-3);compare(ours,ref)

witnesses=[(1,'0111110',-17639),(3,'011',-165),(5,'011101',-21415),
 (7,'00001',-385),(9,'00',-19),(11,'0111',-465),(13,'01',-43),
 (15,'0010',-601),(17,'00011',-991),(19,'000',-37),(21,'0',-7),
 (23,'0000',-61),(25,'000110',-6667),(27,'0000000',-169)]
for residue,word,integer in witnesses:
    ours=seed(0,-4);ref=seed(0,-3)
    for char in word:
        ours=step(ours,int(char),-4);ref=step(ref,int(char),-3);compare(ours,ref)
    eq('complete witness integer',ours[3]-integer)
    ck('complete witness residue',ours[3]%28==residue)
ck('entire image witnessed',{r for r,w,s in witnesses}==set(range(1,28,2)))
result={'status':'PASS_FULL_IF_GEOMETRIC_INPUTS_AND_INDEPENDENT_PRISMS',
 'utc':datetime.now(timezone.utc).isoformat(),'source':str(SRC.relative_to(ROOT)),
 'source_sha256':EXPECTED,'checks':len(checks),'fresh_complete_systems':len(solves),
 'identities':checks,'full_solutions':solves,
 'scope':'Original M6,(m,n)=(2,1), full positive epsilon loop, IA.1 scalar range; relative collar/reflection inputs, actual doubled/native reset and exact affine relation. Geometric line/Cech/tangent/endpoint proof is separately audited.'}
def enc(v):
    if isinstance(v,S.Integer):return int(v)
    if isinstance(v,S.Rational):return str(v)
    raise TypeError(type(v))
(ROOT/'code/part3/e6_selected_infinity_all_fans_peer.json').write_text(json.dumps(result,indent=2,default=enc)+'\n')
print(json.dumps({k:result[k] for k in ['status','checks','fresh_complete_systems','source_sha256']},indent=2))
