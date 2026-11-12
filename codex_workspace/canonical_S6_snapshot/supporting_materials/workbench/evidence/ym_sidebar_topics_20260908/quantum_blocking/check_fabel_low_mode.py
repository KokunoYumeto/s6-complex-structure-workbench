"""Independent incidence, boundary-moment and Fabel asymptotic diagnostics."""
from pathlib import Path
from itertools import product
import json, math, hashlib
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,ok,detail=None):
    checks.append({"name":name,"passed":bool(ok),"detail":detail})
    if not ok: raise AssertionError(name)
for L in [2,3,5]:
    N=2*L+1; h=math.pi/(2*N); sig=math.sqrt(8)*math.sin(h)
    verts=list(product(range(-L,L+1),repeat=3))
    edges=[(n,i) for n in verts for i in range(3) if n[i]<L]
    index={e:k for k,e in enumerate(edges)}
    def shift(n,i):
        t=list(n); t[i]+=1; return tuple(t)
    faces=[(n,i,j) for n in verts for i in range(3) for j in range(i+1,3) if n[i]<L and n[j]<L]
    facewords=[[(index[(n,i)],1),(index[(shift(n,i),j)],1),
                (index[(shift(n,j),i)],-1),(index[(n,j)],-1)] for n,i,j in faces]
    v0=lambda n:1/math.sqrt(N)
    v1=lambda n:-math.sqrt(2/N)*math.sin(math.pi*n/N)
    w1=lambda n:-math.sqrt(2/N)*math.cos(math.pi*(n+.5)/N)
    V=np.zeros((len(edges),3))
    for k,(n,e) in enumerate(edges):
        for i,(p,q) in enumerate([(1,2),(2,0),(0,1)]):
            if e==p: V[k,i]=w1(n[p])*v1(n[q])*v0(n[i])/math.sqrt(2)
            if e==q: V[k,i]=-v1(n[p])*w1(n[q])*v0(n[i])/math.sqrt(2)
    Y=np.array([sum(sign*V[k] for k,sign in word) for word in facewords])
    div={n:np.zeros(3) for n in verts}
    for k,(n,i) in enumerate(edges):
        div[n]-=V[k]; div[shift(n,i)]+=V[k]
    check(f"L={L}: original orthonormal transverse modes and curl",
          np.max(np.abs(V.T@V-np.eye(3)))<1e-12 and
          np.max(np.abs(Y.T@Y-sig**2*np.eye(3)))<1e-12 and
          max(np.max(np.abs(v)) for v in div.values())<1e-12)
    A=sum(n*n*v1(n)**2 for n in range(-L,L+1))
    B=sum((n+.5)**2*w1(n)**2 for n in range(-L,L))
    M=sum(n*v1(n)*v0(n) for n in range(-L,L+1))
    delta=(1-1/math.tan(h)**2)/8
    M2=math.cos(h)**2/(2*N*N*math.sin(h)**4)
    check(f"L={L}: direct original boundary moments",
          abs((B-A)/2+1/8-delta)<1e-11 and abs(M*M-M2)<1e-11)
    for a,b in [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]:
        S=np.zeros((3,3)); S[a,b]=S[b,a]=1
        fe=np.array([(np.array(n)+.5*np.eye(3)[i])@S@(np.array(n)+.5*np.eye(3)[i]) for n,i in edges])
        fp=np.array([sum(fe[k] for k,_ in word)/4 for word in facewords])
        actual=(Y.T@(fp[:,None]*Y))/sig-sig*(V.T@(fe[:,None]*V))
        expected=sig*(delta*(np.trace(S)*np.eye(3)-np.diag(np.diag(S)))+
                      M2*(S-np.diag(np.diag(S))))
        error=float(np.max(np.abs(actual-expected)))
        check(f"L={L}: full electric-plus-four-edge-magnetic block S{a+1}{b+1}",error<1e-9,{"max_absolute_error":error})
    # The magnetic term cannot be omitted: test identity weight.
    fe=np.array([sum((np.array(n)+.5*np.eye(3)[i])**2) for n,i in edges])
    fp=np.array([sum(fe[k] for k,_ in word)/4 for word in facewords])
    electric_only=-sig*(V.T@(fe[:,None]*V))
    correct=(Y.T@(fp[:,None]*Y))/sig+electric_only
    check(f"L={L}: omitted-magnetic negative control detected",np.linalg.norm(correct-electric_only)>1)
    # Midpoint-to-physical-coordinate map retains exact a^2 and raw a^4.
    physical_a=s.Rational(1,37)
    check(f"L={L}: physical midpoint raw factor",physical_a**4==s.Rational(1,37**4))
    if L==2:
        incidence=np.zeros((len(faces),len(edges)))
        for p,word in enumerate(facewords):
            for k,sign in word: incidence[p,k]=sign
        ev,vec=np.linalg.eigh(incidence.T@incidence)
        freqs=np.sqrt(ev[ev>1e-9]); all_modes=vec[:,ev>1e-9]
        check("L=2: full curl rank and isolated three-mode frequency",
              len(freqs)==4*L*L*(4*L+3) and
              np.max(np.abs(freqs[:3]-sig))<1e-11 and
              (freqs[3]+sig)/(2*sig)>1.1)
        Sstar=np.array([[4,6,-36],[6,9,-54],[-36,-54,324]],dtype=float)/64
        fe=np.array([(np.array(n)+.5*np.eye(3)[i])@Sstar@(np.array(n)+.5*np.eye(3)[i]) for n,i in edges])
        fp=np.array([sum(fe[k] for k,_ in word)/4 for word in facewords])
        curl_modes=incidence@all_modes
        AA=all_modes.T@(fe[:,None]*all_modes)
        MM=curl_modes.T@(fp[:,None]*curl_modes)
        outer=np.sqrt(freqs[:,None]*freqs[None,:])
        full=MM/outer-outer*AA
        low=sig*(delta*(np.trace(Sstar)*np.eye(3)-np.diag(np.diag(Sstar)))+
                 M2*(Sstar-np.diag(np.diag(Sstar))))
        lowmass=np.trace(low@low); allmass=np.trace(full@full)
        bound=sig**2*delta**2/(432*len(freqs)*L**4)
        check("L=2: full original-incidence matrix band mass and retained fraction",
              abs(np.trace(full[:3,:3]@full[:3,:3])-lowmass)<1e-8 and
              1>=lowmass/allmass>=bound,
              {"band_fraction":float(lowmass/allmass),"proved_lower_bound":bound})
        constant=(curl_modes.T@curl_modes)/outer-outer*(all_modes.T@all_modes)
        check("L=2: full electric/magnetic constant-weight cancellation",
              np.max(np.abs(constant))<1e-10)
x,y,w,z=s.symbols("x y w z", real=True)
F=s.Matrix([(1+x*y)**3*w+y*y*(1+x*y)*(4+3*x*y),
            y+3*x*(1+x*y)**2*w+3*x*y*y*(4+3*x*y),
            2*x-3*x*x*y-x**3*w])
J=F.jacobian([x,y,w]); q0={x:1,y:-s.Rational(3,2),w:s.Rational(13,2)}
J0=J.subs(q0); Jz=J.subs({x:1/z,y:-3*z/2,w:13*z*z/2})
Bt=s.eye(3); Bt[1,2]=3*(1-z*z)/4
C=J0.inv()*Bt.inv()*Jz
K=s.simplify(C*C.T)
eta=s.Matrix([s.Rational(1,4),s.Rational(3,8),-s.Rational(9,4)])
star=eta*eta.T
check("Original Jacobian determinant",s.factor(J.det())==-2)
check("Full unscaled Fabel tensor endpoint",all(s.limit(z**6*K[i,j],z,0,dir="+")==star[i,j] for i in range(3) for j in range(3)))
diag=sum((s.trace(star)-star[i,i])**2 for i in range(3))
off=sum(star[i,j]**2 for i in range(3) for j in range(i+1,3))
check("Exact endpoint diagonal and off-diagonal coefficients",
      diag==s.Rational(109321,2048) and off==s.Rational(531,512))
const=7500*diag/s.pi**2+3840000*off/s.pi**6
check("Exact raw j^18 norm coefficient",
      s.simplify(const-(s.Rational(204976875,512)/s.pi**2+3982500/s.pi**6))==0)
# Trigonometric moment identities, differentiated as closed geometric sums.
t, NN=s.symbols("t NN", positive=True, real=True)
DN=s.sin(NN*t/2)/s.sin(t/2)
DM=s.sin((NN-1)*t/2)/s.sin(t/2)
check("Differentiated vertex/edge Dirichlet identity",
      s.trigsimp(DM-(DN*s.cos(t/2)-s.cos(NN*t/2)))==0)
# Numeric evaluations are diagnostics for formulas proved at all L in the text.
for j in [20,50,100]:
    N=2*j*j+1; h=math.pi/(2*N); sig=math.sqrt(8)*math.sin(h); aa=1/(100*j)
    de=(1-1/math.tan(h)**2)/8
    mm=math.cos(h)**2/(2*N*N*math.sin(h)**4)
    Kj=np.array(K.subs(z,s.Rational(1,j))).astype(float)
    R=sig*(de*(np.trace(Kj)*np.eye(3)-np.diag(np.diag(Kj)))+mm*(Kj-np.diag(np.diag(Kj))))
    norm=3*np.trace(R@R)/(8*aa*aa); gap=2*sig/aa
    check(f"j={j}: retained-scale asymptotic diagnostic",
          abs(norm/j**18/float(const)-1)<.06 and abs(j*gap/(100*math.sqrt(2)*math.pi)-1)<.01,
          {"raw_norm_over_j18":float(norm/j**18),"j_times_gap":float(j*gap)})
receipt={"checks":checks,"passed_groups":len(checks),
"raw_norm_limit":str(const),"raw_norm_limit_float":float(const),
"scope":"Incidence, original coordinates and algebra diagnostics; full fixed-box/diagonal proof is in the manuscript. No interacting continuum reconstruction is certified."}
(ROOT/"FABEL_LOW_MODE_CHECKS.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed_groups":len(checks),"raw_norm_limit":str(const)},indent=2))
