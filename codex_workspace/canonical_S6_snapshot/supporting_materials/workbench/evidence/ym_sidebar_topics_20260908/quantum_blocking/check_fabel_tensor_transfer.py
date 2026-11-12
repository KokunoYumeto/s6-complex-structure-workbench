"""Independent polynomial, open-box, symmetry and transport checks.

No spectrum or interacting vacuum is numerically substituted. Finite checks
diagnose the coefficient calculations; the companion proves the measure maps.
"""
from pathlib import Path
from itertools import product, combinations, permutations
from fractions import Fraction as Q
import json, hashlib
import sympy as s

ROOT = Path(__file__).resolve().parent
checks = []
def exact(name, expr):
    entries = list(expr) if isinstance(expr, s.MatrixBase) else [expr]
    ok = all(s.cancel(v) == 0 for v in entries)
    checks.append({"name": name, "passed": ok})
    if not ok: raise AssertionError(name)

L = s.symbols("L", positive=True, integer=True)
v = s.symbols("s11 s22 s33 s12 s13 s23", real=True)
S = s.Matrix([[v[0],v[3],v[4]],[v[3],v[1],v[5]],[v[4],v[5],v[2]]])
Ni, I2 = 2*L, L*(4*L**2-1)/6
N, N2, En = 4*L, 2*L*(2*L**2+1)/3, -2*L
cop = sum(Ni*(2*L-1)*(2*L+1)*(S[i,i]+3*S[j,j])**2/16
          for i in range(3) for j in range(3) if i != j)
hinge = 0
for i in range(3):
    j,k = [r for r in range(3) if r != i]
    c = (2*S[i,i]+3*S[j,j]+3*S[k,k])/8
    hinge += (I2*N**2*(S[i,j]**2+S[i,k]**2)
       +Ni*N*N2*(S[j,j]**2+S[k,k]**2+2*S[j,k]**2)
       +2*Ni*En**2*(S[j,j]*S[k,k]+S[j,k]**2)
       +2*c*Ni*N*En*(S[j,j]+S[k,k])+c**2*Ni*N**2)
D = s.expand(cop+hinge)
def at(vec):
    return s.factor(D.subs(dict(zip(v,vec))))
D0, DE, DT = at([1,1,1,0,0,0]), at([1,-1,0,0,0,0]), at([0,0,0,1,0,0])
trace = s.trace(S)
w0 = trace**2/9
wE = sum((S[i,i]-trace/3)**2 for i in range(3))/2
wT = sum(S[i,j]**2 for i in range(3) for j in range(i+1,3))
exact("analytic cubic decomposition of full adjacent-face coefficient",
      D - w0*D0-wE*DE-wT*DT)

def graph(ell):
    nodes = list(product(range(-ell,ell+1), repeat=3))
    edges = [(n,i) for n in nodes for i in range(3) if n[i]<ell]
    edge_index = {e:k for k,e in enumerate(edges)}
    faces=[]
    for n in nodes:
        for i,j in combinations(range(3),2):
            if n[i]==ell or n[j]==ell: continue
            ni=list(n); ni[i]+=1
            nj=list(n); nj[j]+=1
            faces.append(((n,i),(tuple(ni),j),(tuple(nj),i),(n,j)))
    incidence={e:[] for e in edges}
    for p in faces:
        for e in p: incidence[e].append(p)
    return nodes,edges,faces,incidence,edge_index

def basis4(e):
    n,i=e
    X=[2*n[r]+int(r==i) for r in range(3)]
    return [X[0]**2,X[1]**2,X[2]**2,2*X[0]*X[1],2*X[0]*X[2],2*X[1]*X[2]]

for ell in (1,2,3,4):
    nodes,edges,faces,inc,index=graph(ell)
    exact(f"L={ell} edges",len(edges)-3*(2*ell)*(2*ell+1)**2)
    exact(f"L={ell} faces",len(faces)-3*(2*ell)**2*(2*ell+1))
    rows={e:basis4(e) for e in edges}
    fp16={p:[sum(rows[e][k] for e in p) for k in range(6)] for p in faces}
    G=[[0]*6 for _ in range(6)]
    affine_G=[[Q(0)]*3 for _ in range(3)]
    for e in edges:
        for p,q in combinations(inc[e],2):
            d16=[fp16[p][k]+fp16[q][k]-8*rows[e][k] for k in range(6)]
            for i in range(6):
                for j in range(6): G[i][j]+=d16[i]*d16[j]
            ae=[]
            for r in range(3):
                fm=lambda link: Q(2*link[0][r]+int(link[1]==r),2)
                ae.append(sum(fm(l) for l in p)/4+sum(fm(l) for l in q)/4-2*fm(e))
            for i in range(3):
                for j in range(3): affine_G[i][j]+=ae[i]*ae[j]
    G=s.Matrix(G)/256
    analytic=s.hessian(D,v)/2
    exact(f"L={ell} all 36 quadratic coefficient entries",G-analytic.subs(L,ell))
    exact(f"L={ell} all 9 affine coefficient entries",s.Matrix(affine_G)-16*ell**3*s.eye(3))
    # Exact finite sums used in the all-L derivation, including endpoints.
    exact(f"L={ell} midpoint second moment",sum(Q(2*n+1,2)**2 for n in range(-ell,ell))-I2.subs(L,ell))
    oriented=[(n,ep) for n in range(-ell,ell+1) for ep in (-1,1) if -ell<=n+ep<=ell]
    exact(f"L={ell} oriented transverse second moment",sum(n*n for n,ep in oriented)-N2.subs(L,ell))
    exact(f"L={ell} signed endpoint moment",sum(n*ep for n,ep in oriented)-En.subs(L,ell))

# Every signed permutation maps the original open edges and faces, including
# orientation reversals, bijectively. This tests the actual finite geometry.
for ell in (1,2):
    nodes,edges,faces,inc,index=graph(ell)
    face_sets={frozenset(p) for p in faces}
    for perm in permutations(range(3)):
        for signs in product((-1,1),repeat=3):
            emap={}
            for e in edges:
                n,i=e
                rn=[0]*3
                for r in range(3): rn[perm[r]]=signs[r]*n[r]
                j=perm[i]
                if signs[i]<0: rn[j]-=1
                im=(tuple(rn),j)
                assert im in index
                emap[e]=im
                # Midpoint relation without rescaling original coordinates.
                for r in range(3):
                    assert 2*rn[perm[r]]+int(j==perm[r]) == signs[r]*(2*n[r]+int(i==r))
            assert len(set(emap.values()))==len(edges)
            assert {frozenset(emap[e] for e in p) for p in faces}==face_sets
    checks.append({"name":f"L={ell} all 48 signed-permutation edge/face/midpoint maps","passed":True})

# Reconstruct Fabel's full inverse material map from the original polynomials.
x,y,w,z=s.symbols("x y w z")
F=s.Matrix([(1+x*y)**3*w+y*y*(1+x*y)*(4+3*x*y),
             y+3*x*(1+x*y)**2*w+3*x*y*y*(4+3*x*y),
             2*x-3*x*x*y-x*x*x*w])
J=F.jacobian([x,y,w])
exact("original Fabel determinant",J.det()+2)
gam={x:1/z,y:-3*z/2,w:13*z*z/2}
Jg=J.subs(gam); J0=J.subs({x:1,y:-s.Rational(3,2),w:s.Rational(13,2)})
B=s.eye(3); B[1,2]=3*(1-z*z)/4
C=J0.inv()*B.inv()*Jg
A=Jg.inv()*B*J0
exact("full two-sided material inverse",A*C-s.eye(3))
exact("material inverse reverse composition",C*A-s.eye(3))
K=C*C.T
eta=s.Matrix([s.Rational(1,4),s.Rational(3,8),-s.Rational(9,4)])
Klim=K.applyfunc(lambda t:s.limit(z**6*t,z,0,dir="+"))
exact("full tensor leading matrix",Klim-eta*eta.T)
coeffs=[w0,wE,wT]
sv=[Klim[0,0],Klim[1,1],Klim[2,2],Klim[0,1],Klim[0,2],Klim[1,2]]
weights=[s.factor(c.subs(dict(zip(v,sv)))) for c in coeffs]
exact("three limiting spectral weights",
      s.Matrix(weights)-s.Matrix([s.Rational(113569,36864),s.Rational(100825,12288),s.Rational(531,512)]))
exact("non-affine boundary coefficient for tensor limit",
      at(sv)-sum(w*d for w,d in zip(weights,[D0,DE,DT])))

# Noncommuting link covariance: conventional transport has the reverse
# endpoint law; the inverse link is required by the retained convention.
I=s.I
sigmas=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
hs=s.Rational(3,5)*s.eye(2)+I*s.Rational(4,5)*sigmas[0]
ht=s.Rational(5,13)*s.eye(2)+I*s.Rational(12,13)*sigmas[1]
P=s.Rational(8,17)*s.eye(2)+I*s.Rational(15,17)*sigmas[2]
Ph=ht.inv()*P*hs
exact("inverse transport endpoint covariance",Ph.inv()-hs.inv()*P.inv()*ht)
assert any(s.cancel(q)!=0 for q in Ph-hs.inv()*P*ht), "Negative control failed"
checks.append({"name":"wrong endpoint assignment rejected on noncommuting sample","passed":True})
Ta,Tb=-I*sigmas[0]/2,-I*sigmas[1]/2
eps=s.symbols("eps")
def exp2(M,sgn=1): return s.eye(2)+sgn*eps*M+eps**2*M*M/2
plaquette=exp2(Ta)*exp2(Tb)*exp2(Ta,-1)*exp2(Tb,-1)
second=plaquette.applyfunc(lambda e:s.expand(e).coeff(eps,2))
exact("inverse-link positive curvature commutator sign",second-(Ta*Tb-Tb*Ta))

# Source-faithful local energy identity and first surviving two-channel moments.
c0,kap,Vtot,Hfree=s.symbols("c0 kappa Vtot Hfree", real=True)
Dconstant=kap*c0*Hfree+c0*Vtot
exact("constant local energy is c0 times full H",Dconstant-c0*(kap*Hfree+Vtot))
assert s.expand(kap*c0*Hfree-c0*(kap*Hfree+Vtot)) != 0
checks.append({"name":"electric-only constant operator rejected","passed":True})
exact("two-channel state norm coefficient",s.Rational(1,4*9**2)+s.Rational(3,4*39**2)-s.Rational(49,13689))
exact("two-channel energy coefficient",s.Rational(9,2)*s.Rational(1,4*9**2)+s.Rational(13,2)*s.Rational(3,4*39**2)-s.Rational(2,117))
exact("first surviving ratio",s.Rational(2,117)/s.Rational(49,13689)-s.Rational(234,49))

report={"passed":len(checks),"checks":checks,
 "all_L_coefficients":{"D_identity":str(D0),"D_diagonal_difference":str(DE),"D_off_diagonal":str(DT),
                     "D_rank_one_limit":str(at(sv))},
 "tensor_limit_weights":[str(w) for w in weights],
 "scope":"Algebra, independent full-box enumeration, boundary moments and noncommuting transport. No vacuum spectrum substituted.",
 "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/"FABEL_TENSOR_TRANSFER_CHECKS.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in report.items() if k!="checks"},indent=2))
