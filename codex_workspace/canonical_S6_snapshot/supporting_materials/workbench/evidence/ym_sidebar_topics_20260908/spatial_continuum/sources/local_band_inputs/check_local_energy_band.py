"""Local-energy compression diagnostics; not an interacting continuum certification."""
from pathlib import Path
from itertools import product
import math,json
import numpy as np
import sympy as s
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,ok,details=None):
    checks.append({"name":name,"passed":bool(ok),"details":details})
    if not ok: raise AssertionError(name)
# Exact seven-coordinate inner product and limiting self-adjoint matrix.
basis=[]
for i in range(3):
    B=s.zeros(3);B[i,i]=1;basis.append(B)
for i,j in [(0,1),(0,2),(1,2)]:
    B=s.zeros(3);B[i,j]=B[j,i]=1;basis.append(B)
gram=s.diag(1,6,6,6,12,12,12)
Z=s.zeros(7)
for i in range(3):
    Z[0,i+1]=6;Z[i+1,0]=1
for i in range(1,7):Z[i,i]=4
check("Exact raw Gram adjoint identity",gram*Z==Z.T*gram)
check("Exact trace/traceless spectral polynomial",
      s.factor(Z.charpoly().as_expr())==(s.Symbol("lambda")-4)**5*(s.Symbol("lambda")**2-4*s.Symbol("lambda")-18))
vac=s.eye(7)[:,0]
check("Exact vacuum-to-band squared norm", (Z*vac).dot(gram*(Z*vac))==18)
eta=s.Matrix([s.Rational(1,4),s.Rational(3,8),-s.Rational(9,4)])
S=eta*eta.T
Bstar=s.zeros(3)
for i in range(3):
    Bstar[i,i]=-25*s.sqrt(2)/s.pi*(s.trace(S)-S[i,i])
    for j in range(i+1,3):
        Bstar[i,j]=Bstar[j,i]=400*s.sqrt(2)/s.pi**3*S[i,j]
Cstar=s.Rational(204976875,512)/s.pi**2+3982500/s.pi**6
check("Raw Fabel frame coefficient norm",s.simplify(6*s.trace(Bstar*Bstar)-Cstar)==0)
check("Raw Fabel local mixed sign and coefficient",
      s.simplify(6*s.sqrt(2)*s.pi*s.trace(Bstar))==-s.Rational(25275,8))
# Polynomial creation basis: exact factorial norms, no interacting vacuum substitution.
zz=s.symbols("z0:6")
RR=s.Matrix([[2,-1],[-1,3]])
BB=s.Matrix([[s.Rational(1,3),2],[2,-1]])
QQ=s.Matrix([[1,2],[2,4]])
def pair(mat):
    return s.expand(sum(mat[i,k]*zz[3*i+c]*zz[3*k+c]
                        for i in range(2) for k in range(2) for c in range(3)))
def inner(poly,qoly):
    pp=s.Poly(poly,*zz).as_dict();qq=s.Poly(qoly,*zz).as_dict()
    return s.expand(sum(v*qq.get(k,0)*math.prod(math.factorial(n) for n in k) for k,v in pp.items()))
number=s.expand(sum(QQ[i,k]*zz[3*i+c]*s.diff(pair(BB),zz[3*k+c])
                    for i in range(2) for k in range(2) for c in range(3)))
check("Direct six-coordinate number-preserving matrix action",
      s.expand(number-pair(QQ*BB+BB*QQ))==0)
ann=s.expand(sum(RR[i,k]*s.diff(pair(BB),zz[3*i+c],zz[3*k+c])
                 for i in range(2) for k in range(2) for c in range(3)))
check("Direct pair annihilation coefficient",ann==6*s.trace(RR*BB))
check("Direct pair raw inner product",inner(pair(RR),pair(BB))==6*s.trace(RR*BB))
four=s.expand(pair(RR)*pair(BB))
check("Two and four creation sectors orthogonal with nonzero leakage",
      inner(four,pair(BB))==0 and inner(four,four)>0)
radial=sum(zz[c]**2 for c in range(3))
check("One-spatial-mode retained four-creation norm",inner(radial**2,radial**2)==120)
# Direct finite incidence check for local weights, independent of tensor formulas.
for L in [2,3]:
    N=2*L+1; h=math.pi/(2*N); sig=math.sqrt(8)*math.sin(h); a=.13
    ns=list(product(range(-L,L+1),repeat=3))
    edges=[(n,k) for n in ns for k in range(3) if n[k]<L]; idx={e:i for i,e in enumerate(edges)}
    def shift(n,k):
        r=list(n);r[k]+=1;return tuple(r)
    faces=[(n,p,q) for n in ns for p in range(3) for q in range(p+1,3) if n[p]<L and n[q]<L]
    words=[[(idx[(n,p)],1),(idx[(shift(n,p),q)],1),(idx[(shift(n,q),p)],-1),(idx[(n,q)],-1)] for n,p,q in faces]
    v0=lambda n:N**-.5
    v1=lambda n:-(2/N)**.5*math.sin(math.pi*n/N)
    w=lambda n:-(2/N)**.5*math.cos(math.pi*(n+.5)/N)
    V=np.zeros((len(edges),3))
    for k,(n,d) in enumerate(edges):
        for i,(p,q) in enumerate([(1,2),(2,0),(0,1)]):
            if d==p:V[k,i]=v0(n[i])*w(n[p])*v1(n[q])/math.sqrt(2)
            if d==q:V[k,i]=-v0(n[i])*v1(n[p])*w(n[q])/math.sqrt(2)
    curls=np.array([sum(sign*V[k] for k,sign in ww) for ww in words])
    def weight(x):return math.exp(-sum(t*t for t in x)/.04)*(1+.2*x[0]-.3*x[1]+.1*x[2])
    fe=np.array([weight(a*(np.array(n)+.5*np.eye(3)[d])) for n,d in edges])
    fp=np.array([sum(fe[k] for k,_ in ww)/4 for ww in words])
    A=V.T@(fe[:,None]*V);F=(curls.T@(fp[:,None]*curls))/sig**2
    R=sig*(F-A);Q=sig*(F+A)
    check(f"L={L}: full curl-weight matrix has no cross-plane entries",np.max(np.abs(F-np.diag(np.diag(F))))<1e-14)
    check(f"L={L}: local electric+magnetic reconstruction",np.max(np.abs((Q+R)/2-sig*F))<1e-13 and np.max(np.abs((Q-R)/2-sig*A))<1e-13)
    # Vacuum creation norm by a direct 9-variable polynomial Gaussian moment.
    check(f"L={L}: nonzero local band mass",3*np.trace(R@R)/(8*a*a)>0)
# Separable compact C-infinity profile with nonzero cross moments.
radius=.01; tilt=[.3,-.2,.4]
def bump(t):
    return math.exp(-1/(1-t*t)) if abs(t)<1 else 0.
I0=radius*quad(bump,-1,1,epsabs=1e-13)[0]
I1=[radius**2*b*quad(lambda t:t*t*bump(t),-1,1,epsabs=1e-13)[0] for b in tilt]
H=I0**3
for j in [12,24,48,96]:
    L=j*j;N=2*L+1;a=1/(100*j);ell=a*N;h=math.pi/(2*N);sig=math.sqrt(8)*math.sin(h)
    # All other sampled weights vanish exactly, so omitted entries contribute zero.
    ns=np.arange(-j-2,j+3,dtype=float)
    v0=np.full(ns.shape,1/math.sqrt(N))
    v1=-math.sqrt(2/N)*np.sin(math.pi*ns/N)
    ww=-math.sqrt(2/N)*np.cos(math.pi*(ns+.5)/N)
    vals=[]
    for b in tilt:
        fun=lambda x:np.array([bump(float(t/radius))*(1+b*float(t/radius)) for t in x])
        hv=fun(a*ns);he=fun(a*(ns+.5));hp=fun(a*(ns+1))
        vals.append((sum(hv*v0*v0),sum(hv*v1*v1),sum(hv*v0*v1),
                     sum(he*ww*ww),sum((hv+hp)*ww*ww)))
    A=np.zeros((3,3));F=np.zeros((3,3))
    for i,(p,q) in enumerate([(1,2),(2,0),(0,1)]):
        A[i,i]=.5*vals[i][0]*(vals[p][3]*vals[q][1]+vals[p][1]*vals[q][3])
        F[i,i]=.25*vals[i][0]*(vals[p][3]*vals[q][4]+vals[p][4]*vals[q][3])
    for i,k in [(0,1),(0,2),(1,2)]:
        d=3-i-k;A[i,k]=A[k,i]=-.5*vals[d][3]*vals[i][2]*vals[k][2]
    R=sig*(F-A);Q=sig*(F+A)
    target=4*math.sqrt(2)*math.pi*H
    error=max(np.max(np.abs(ell**4*R/a-target*np.eye(3))),
              np.max(np.abs(ell**4*Q/a-target*np.eye(3))))/target
    check(f"j={j}: compact-profile raw fourth-power matrix",error<.015,{"relative_error":float(error)})
    mass=3*np.trace(R@R)/(8*a*a)
    check(f"j={j}: raw eighth-power band norm",abs(ell**8*mass/(36*math.pi**2*H*H)-1)<.03)
    for i,k in [(0,1),(0,2),(1,2)]:
        target2=2*math.sqrt(2)*math.pi**3*I1[i]*I1[k]*I0
        check(f"j={j}: retained off-diagonal quadrupole {i}{k}",
              abs(ell**6*R[i,k]/a/target2-1)<.02)
    check(f"j={j}: physical and box-time frequency",abs(ell*2*sig/a/(2*math.sqrt(2)*math.pi)-1)<.001)
receipt={"passed_groups":len(checks),"checks":checks,"scope":"Exact finite-dimensional identities and numerical incidence/Riemann-sum diagnostics. No nonlinear continuum theorem is tested."}
(ROOT/"LOCAL_ENERGY_BAND_CHECKS.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed_groups":len(checks),"last":checks[-1]},indent=2))
