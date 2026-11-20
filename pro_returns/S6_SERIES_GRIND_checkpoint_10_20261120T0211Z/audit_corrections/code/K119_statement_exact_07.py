"""Fresh K119 derivation from the isolated statement and allowed K10 data.
No K119 receiving proof or its calculation has been opened.
"""
from pathlib import Path
from datetime import datetime, timezone
import sympy as s,json,hashlib,time
from sympy.matrices.normalforms import hermite_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

start=time.monotonic(); checks=[]
def ck(n,v):
    if not bool(v):raise AssertionError(n)
    checks.append({'name':n,'pass':True})
def mat(M):return [[str(x) for x in M.row(i)] for i in range(M.rows)]
def snf(M,n):
    D,U,V=[a.to_Matrix() for a in smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(s.ZZ))]
    ck(n+' equality',D==U*M*V)
    ck(n+' unimodularity',abs(U.det())==1 and abs(V.det())==1)
    return D,U,V
def rk(D):return sum(D[i,i]!=0 for i in range(min(D.shape)))
def solve(M,T,n):
    D,U,V=snf(M,n);r=rk(D);C=U*T;ck(n+' image',C[r:,:]==s.zeros(C.rows-r,T.cols));X=s.zeros(M.cols,T.cols)
    for i in range(r):
        for j in range(T.cols):
            q=s.Rational(C[i,j],D[i,i]);ck(n+' integral'+str((i,j)),q.q==1);X[i,j]=q
    X=V*X;ck(n+' solved',M*X==T);return X

t,a,u,z=s.symbols('t a u z');R=t*t+a;f=R*R+t;g=R**3+s.Rational(3,2)*t*R+s.Rational(3,8)
D=s.expand(64*(g*g-f**3));expected=48*a*(t*t+a)**2+8*t**3+72*a*t+9
ck('exact full discriminant polynomial',D==s.expand(expected))
ck('ordinary cap collision equation',D.subs(t,0)==3*(16*a**3+3))
ck('node branch derivative',s.cancel(-s.diff(D,a).subs(t,0)/s.diff(D,t).subs(t,0))==-2*a)
au=-u/s.Integer(3)-u**4/s.Integer(9);tc=1/(2*u)-u*u/3
collision=2187-16*u**3*(u**3+3)**3
ck('full collision pullback',s.expand((16*au**3+3)*729-collision)==0)
ck('collision factorization',s.expand(collision+(2*u**3-3)*(8*u**9+84*u**6+342*u**3+729))==0)
ck('all twelve u roots simple',s.gcd(collision,s.diff(collision,u))==1 and s.degree(collision,u)==12)
for name,excluded in [('u0',u),('a0',u**3+3),('ordered cusp',4*u**3+3),('unselected II',16*u**6+120*u**3+243)]:
    ck('disjoint boundary '+name,s.gcd(collision,excluded)==1)
ck('selected exactly six ordered points',s.cancel(tc-(3-2*u**3)/(6*u))==0)
ck('local a map has nonzero derivative at every collision',s.expand(s.diff(au,u)+(4*u**3+3)/9)==0 and s.gcd(collision,4*u**3+3)==1)
ck('ordinary collision has neither I9 nor II source',s.gcd(16*a**3+3,a*(256*a**3-3))==1)
xi,x,y,h,q=s.symbols('xi x y h q')
ck('full critical-root source factorization',s.expand(x**3-3*xi**2*x+2*xi**3-(x-xi)**2*(x+2*xi))==0)
ck('node at original collision',s.rem((x**3-3*a*a*x+2*(a**3+s.Rational(3,8)))-(x+a)**2*(x-2*a),16*a**3+3,a)==0)
ck('full h central unit',s.simplify(2*s.diff(g,t).subs(t,0)-3*(-a)*s.diff(f,t).subs(t,0))==6*a)
kap=-s.diff(D,t).subs(t,0)/(64*1728*a**6)
ck('actual inverse-j Tate leading coefficient',s.rem(s.together(kap-1/(288*a*a)).as_numer_denom()[0],16*a**3+3,a)==0)
P=-2+s.sqrt(3)
ck('marked normalization point and reciprocal',s.simplify((1-s.sqrt(3))/(1+s.sqrt(3))-P)==0 and s.simplify(1/P)==-2-s.sqrt(3))
ck('both point branches solve actual quadratic',s.simplify(P*P+4*P+1)==0)
m=-s.sqrt(3)*t;x2=s.expand(m*m-2*R)
ck('actual doubled point x coordinate',x2==t*t-2*a)
f2=(y-s.sqrt(3)/2+s.sqrt(3)*t*(x-R))/(x-x2)
c2=s.simplify(f2.subs({t:0,x:-a,y:0}))
ck('actual tangent quotient at node',c2==-s.sqrt(3)/(2*a))
ck('entire eighth multiplier central coefficient',s.rem(s.together(c2**8-9/a**2).as_numer_denom()[0],16*a**3+3,a)==0)
# The point-Cartier theta formula has no base-dependent f8 scalar left:
# f8=A8 f_P^8/f_(P^8), with the same A8 at p and p-G.
f2v,F,Ft,H,Ht,A8=s.symbols('f2 F Ft H Ht A8',nonzero=True)
B81=f2v**8*(A8*Ft**8/Ht)/(A8*F**8/H)
ck('full Miller/theta cancellation with unchanged base scalar',s.cancel(B81*Ht/H-(f2v*Ft/F)**8)==0)

inputs=Path(__file__).parent.parent.parent/'audit_paper_i/iv_os45/K119_permitted_K10_matrix_inputs_07.json'
raw=json.loads(inputs.read_text());Ts=[s.Matrix(M) for M in raw['matrices_T']];Hs=[M.inv().T for M in Ts]
prod=s.eye(4)
for M in Hs:prod=prod*M
ck('actual ordered homology tuple product',prod==s.eye(4))
psi=s.Matrix([[1,0,0,0]]);delta=s.Matrix([0,0,0,1]);pref=s.eye(4);E=[];L=[];S=[];blocks=[];prefixes=[]
for i,M in enumerate(Hs):
    ck('actual homology integral '+str(i),all(x.q==1 for x in M))
    ck('actual invariant quotient '+str(i),psi*M==psi)
    ck('actual physical angular period '+str(i),M*delta==delta)
    N=M-s.eye(4);Q=hermite_normal_form(N)
    ck('actual local rank '+str(i),Q.cols==[1,1,1,1,2][i])
    Ei=solve(N,Q,'local actual-image lift '+str(i));Si=solve(Q,N,'local coboundary coordinates '+str(i))
    E.append(Q);L.append(Ei);S.append(Si);prefixes.append(pref.copy());blocks.append(pref*Q);pref=pref*M
Dn=s.Matrix.hstack(*blocks);D0=s.Matrix.vstack(*S)
ck('full integral period complex d2',Dn*D0==s.zeros(4,4))
DN,UN,VN=snf(Dn,'period top map');rn=rk(DN)
ck('H2 period group is the primitive Z psi',rn==3 and all(abs(DN[i,i])==1 for i in range(3)) and psi*Dn==s.zeros(1,Dn.cols))
coords=VN.inv()*D0;ck('period incoming lands in cycles',coords[:rn,:]==s.zeros(rn,4))
DH,UH,VH=snf(coords[rn:,:],'period H1 incoming')
ck('H1 full period sheaf zero integrally',rk(DH)==3 and all(abs(DH[i,i])==1 for i in range(3)))
ck('H0 period sheaf exact physical generator',D0.rank()==3 and D0*delta==s.zeros(D0.rows,1))
targets=s.eye(4)[:,1:]
pre=solve(Dn,targets,'three whole zero-norm target preimages')
local=[];off=0
for i,Q in enumerate(E):
    rr=pre[off:off+Q.cols,:];local.append(L[i]*rr);off+=Q.cols
ck('all three actual unsaturated monodromy preimages',sum((prefixes[i]*(Hs[i]-s.eye(4))*local[i] for i in range(5)),s.zeros(4,3))==targets)
out={'status':'PASS','actor':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed)',
     'utc':datetime.now(timezone.utc).isoformat(),'assertions':len(checks),'seconds':time.monotonic()-start,'checks':checks,
     'input_sha256':hashlib.sha256(inputs.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'D':str(D),'a_u':str(au),'selected_t':str(tc),'H':list(map(mat,Hs)),'prefixes':list(map(mat,prefixes)),
     'local_image_bases':list(map(mat,E)),'local_image_lifts':list(map(mat,L)),'period_D0':mat(D0),'period_D1':mat(Dn),
     'top_smith':mat(DN),'top_left':mat(UN),'top_right':mat(VN),'middle_smith':mat(DH),'middle_left':mat(UH),'middle_right':mat(VH),
     'image_coordinate_preimages':mat(pre),'actual_monodromy_preimages':list(map(mat,local)),
     'scope':'Fresh statement/input-only derivation of K119 collision/source/Tate/Miller constants and full integral extending-period complex. The K119 receiving proof and its numerical outputs have not been opened. Full holomorphic cap maps and endpoint argument are written separately before comparison; this finite program alone is not that geometric proof.'}
dest=Path(__file__).with_suffix('.json');tmp=dest.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2));tmp.replace(dest)
print(json.dumps({k:out[k] for k in ['status','assertions','seconds','source_sha256']}))
