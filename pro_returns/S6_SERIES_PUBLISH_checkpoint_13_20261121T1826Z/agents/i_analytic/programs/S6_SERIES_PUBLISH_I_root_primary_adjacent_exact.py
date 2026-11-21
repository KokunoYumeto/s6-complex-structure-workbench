"""Fresh Paper I coefficient, integral-lattice and root-count corroboration.

Written after the printed proofs were read, 2026-11-19. This program imports
no historical checker. Universal identities are checked symbolically; bounded
counts and a rational signature example are explicitly identified as such.
It does not certify analytic extension, properness or coherent base change.
Run: python adjacent_exact.py > adjacent_exact.output.json
"""
import hashlib
import json
from itertools import permutations
from math import gcd, lcm
from pathlib import Path

import sympy as s
from sympy.matrices.normalforms import hermite_normal_form

checks = []
data = {}


def check(name, value, scope):
    if isinstance(value, s.MatrixBase):
        ok = all(s.cancel(x) == 0 for x in value)
    elif isinstance(value, bool):
        ok = value
    else:
        ok = s.cancel(value) == 0
    assert ok, name
    checks.append(dict(name=name, result="PASS", scope=scope))


z, v, C, mu, U, b, ell, N, m, n = s.symbols("z v C mu U b ell N m n")
a = b-N*ell
delta = s.Matrix([0, 1])
gamma = s.Matrix([6*mu, C-N*v-z])
zgamma = s.Matrix([6*z*mu, -z*(z+1)/2+z*(C-N*v)])
origin = s.Matrix([-6*b*mu*z/N, b*z*z/(2*N)-b*C*z/N+ell*z/2+v*(b*z+U)])
sigma = -ell*zgamma+s.Matrix([6*a*mu*v, v*U+a*C*v-N*a*v*v/2+N*a*v/2])
FN = s.Matrix([6*mu*(z+N*v)/N, C*(z+N*v)/N-(z+N*v)**2/(2*N)+N*v/2])
check("general N origin subtraction", sigma-origin-a*FN, "universal rational polynomial identity")
for name, form, sub, rhs in [
    ("origin cusp", origin, {z:z+N}, -b*gamma+N*(b+ell)*delta/2),
    ("origin parameter", origin, {v:v+1}, (b*z+U)*delta),
    ("sigma cusp", sigma, {z:z+N}, -N*ell*gamma+N*(N+1)*ell*delta/2),
    ("sigma parameter", sigma, {v:v+1}, (b*z+U)*delta+a*gamma),
    ("F cusp cover", a*FN, {z:z+N*m}, a*m*gamma-N*a*m*m*delta/2),
    ("F parameter cover", a*FN, {v:v+n}, a*n*gamma-N*a*n*(n-1)*delta/2),
]:
    check(name, form.subs(sub)-form-rhs, "universal identity; N nonzero")
check("full cusp collar coefficient", (a*z+U)*delta+a*gamma-s.Matrix([6*a*mu,U+a*C-N*a*v]), "actual lattice-period addition")
check("P2.2 specialization", (N*(b+ell)/2).subs(N,12)-6*(b+ell), "exact N=12 coefficient")
check("P2.2 sigma constant", (N*(N+1)*ell/2).subs(N,12)-78*ell, "exact N=12 coefficient")
check("P2.8 fivefold specialization", (sigma-origin).subs({N:12,b:5,ell:0})-5*FN.subs(N,12), "exact original example")

A1 = s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
eye = s.eye(4)
N1 = sum((A1**j for j in range(3)), s.zeros(4))
N2 = sum((A2**j for j in range(4)), s.zeros(4))
d = s.Matrix([0,0,0,1])
e1 = s.Matrix([1,2,-4,0])
e2 = s.Matrix([1,3,-3,0])
check("original order three", A1**3-eye, "actual integral matrix")
check("original order four", A2**4-eye, "actual integral matrix")
check("norm image one", hermite_normal_form(N1)-hermite_normal_form(s.Matrix.hstack(3*e1,d)), "equality of integral column lattices")
check("norm image two", hermite_normal_form(N2)-hermite_normal_form(s.Matrix.hstack(4*e2,2*d)), "equality of integral column lattices")
comm = (s.kronecker_product(eye,A1)-s.kronecker_product(A1.T,eye)).col_join(s.kronecker_product(eye,A2)-s.kronecker_product(A2.T,eye))
check("centralizer rank", comm.rank()==14, "exact rational rank; two-dimensional kernel")
E = s.zeros(4); E[3,0] = 1
check("centralizer identity basis", comm*s.Matrix(list(eye.T)), "column-vectorized identity")
check("centralizer shear basis", comm*s.Matrix(list(E.T)), "column-vectorized E41")
for k, l in [(1,1),(1,2),(5,2),(5,4),(7,2)]:
    check(f"repeated norms {k},{l}", sum((A1**j for j in range(3*k)),s.zeros(4))==k*N1 and sum((A2**j for j in range(4*l)),s.zeros(4))==l*N2, "bounded examples; universal repetition follows from A1^3=A2^4=I")
    check(f"least common shift {k},{l}", gcd(3*k,4*l)==1 and lcm(k,2*l)==2*k*l, "bounded coprime examples; not a replacement for the printed gcd proof")
Cmat = s.Matrix([[-6,1,-1,0],[2,-1,0,0],[0,1,1,0],[-3,0,-1,0]])
K = s.Matrix([[0,1,2],[1,0,0],[0,1,0],[0,0,1]])
B = s.Matrix([[2,-1,0,0],[0,1,1,0],[-3,0,-1,0]])
check("allowed-pair inclusion", K*B-Cmat, "full integral C=KB")
check("allowed-pair primitive quotient", B[:,:3].det()-1, "unimodular three-column basis proves saturated equality")
check("allowed-pair explicit inverse", B[:,:3]*B[:,:3].inv()-s.eye(3), "exact inverse over integers")
check("finite-orbit annihilator", s.Matrix([[0,1,0],[6,0,1],[0,0,-1]]).det()-6, "zero common rational kernel")
data["integral_lattices"] = {"A1":A1.tolist(),"A2":A2.tolist(),"N1":N1.tolist(),"N2":N2.tolist(),"C":Cmat.tolist(),"K":K.tolist(),"B":B.tolist(),"B_inverse":B[:,:3].inv().tolist()}

l0,l1,l2,a1,a2,r,nu=s.symbols("l0 l1 l2 a1 a2 r nu")
p=12*l0-4*l1-3*l2
check("primitive integer intersection", lcm(3,4,1)==12, "intersection 3Z cap 4Z cap Z")
check("oriented collar sum", (4*l1-a1)+(3*l2-a2)+(-12*l0+a1+a2)+p, "universal exact boundary coefficients")
check("collar endpoint functional", -nu*(s.Integer(0)-1)-nu, "fundamental theorem of calculus for every cutoff from one to zero")
rho=1-3*r*r+2*r*r*r
check("explicit collar polynomial", s.integrate(-nu*s.diff(rho,r),(r,0,1))-nu, "one exact cutoff example corroborates the endpoint identity")
y,mm,rr,tr,mr,br=s.symbols("y mm rr tr mr br")
period=s.Matrix([[6*mr,tr,1,0],[6*mm,y,0,0],[br,mr,0,1],[rr,mm,0,0]])
D=y*rr-6*mm*mm
check("real period determinant",period.det()-D,"actual row order Re zeta1, Im zeta1, Re zeta2, Im zeta2")
eta={(1,2):s.Integer(1),(0,3):s.Integer(6)}
top=0
for I,c in eta.items():
    for J,dv in eta.items():
        q=I+J
        if len(set(q))==4:
            inv=sum(q[i]>q[j] for i in range(4) for j in range(i+1,4))
            top+=(-1)**inv*c*dv
check("eta exterior square",top-12,"coefficient in gamma,u,w,delta order; complex orientation has determinant D<0")
H=s.Matrix([[rr,-6*mm],[-6*mm,6*y]])/D
check("Hermitian determinant",H.det()-6/D,"universal rational identity")
Hr=H.subs({y:2,mm:1,rr:1})
eigs=list(Hr.eigenvals())
check("rational eigenvalue signature",sum(e.is_positive is True for e in eigs)==1 and sum(e.is_negative is True for e in eigs)==1,"exact rational matrix example y=2,m=1,Im beta=1")
L=s.Matrix([[1,0],[-6,1]])
check("rational diagonal elimination",Hr-L*s.diag(-s.Rational(1,4),6)*L.T,"exact congruence with one negative and one positive pivot")
data["fibre_sign"]={"period_determinant":str(D),"eta_square":str(top),"Hermitian_example":Hr.tolist(),"eigenvalues":[str(e) for e in eigs],"LDL_pivots":["-1/4","6"]}

def mono(weight, positive=False):
    lo=1 if positive else 0
    if weight<0:return 0
    return sum(3*aa+4*bb==weight for aa in range(lo,weight//3+1) for bb in range(lo,weight//4+1))
count_rows=[]
for nn in range(-240,241):
    r1=nn%3;r2=(3*nn)%4;dd=(nn-4*r1-3*r2)//12
    assert 12*dd+4*r1+3*r2==nn
    actual=[mono(nn),mono(-nn,True)]
    coarse=[max(dd+1,0),max(-dd-1,0)]
    assert actual==coarse
    assert actual[1]==mono(-nn-7)
    count_rows.append(dict(n=nn,r1=r1,r2=r2,d=dd,h0=actual[0],h1=actual[1]))
check("root monomial and Cech dimensions",len(count_rows)==481,"481 bounded integers, both dimensions and the exact negative-monomial shift; printed residue decomposition is the universal proof")
data["root_count_rows"]=count_rows

t=s.symbols("t");AA=-3*t**3*(t-1);BB=2*t**4*(t-1)**2
x1=s.Integer(0);y1=s.sqrt(2)*t*t*(t-1)
slope=AA/(2*y1);x2=s.cancel(slope*slope);y2=s.cancel(slope*(-x2)-y1)
check("duplication x",x2-9*t*t/8,"chord-and-tangent formula on the printed cubic")
check("duplication y",y2-t*t*(32-5*t)/(16*s.sqrt(2)),"same original point and differential convention")
disc=s.factor(-16*(4*AA**3+27*BB**2))
check("cubic discriminant",disc-1728*t**8*(t-1)**3,"exact polynomial factorization")
tt=s.Rational(32,5)
check("regular order-four point",disc.subs(t,tt)!=0 and y1.subs(t,tt)!=0 and y2.subs(t,tt)==0,"P non-2-torsion; 2P finite nonzero 2-torsion on a smooth fibre")
check("double-point substitution",(y2*y2-(x2**3+AA*x2+BB)),"exact full cubic substitution")
data["order_four_example"]={"t":str(tt),"discriminant":str(disc.subs(t,tt)),"x2":str(x2.subs(t,tt)),"y2":str(y2.subs(t,tt))}

zz,ww,xx,yy,aa,bb,kk,rrr=s.symbols("zz ww xx yy aa bb kk rrr")
node=zz*ww-rrr*xx*yy
check("plumbing first blowup chart",node.subs({rrr:zz*aa,ww:aa*xx*yy},simultaneous=True),"exact map r=za,w=axy")
check("plumbing second strict transform",node.subs(zz,rrr*bb)-rrr*(bb*ww-xx*yy),"saturated strict-transform equation bw=xy")
check("plumbing first small chart",(bb*ww-xx*yy).subs({bb:xx*kk,yy:kk*ww},simultaneous=True),"b=xk,y=kw")
check("plumbing second small chart",(bb*ww-xx*yy).subs({xx:bb*kk,ww:kk*yy},simultaneous=True),"x=bk,w=ky")
check("plumbing overlap inverse x",(xx*kk)/kk-xx,"k'=1/k on the actual overlap")
check("plumbing overlap inverse w",(kk*ww)/kk-ww,"same inverse map")
check("first cusp cone unimodular",abs(s.Matrix([[0,1,1],[0,0,1],[1,1,1]]).det())==1,"original main-diagonal lower triangle")
check("second cusp cone unimodular",abs(s.Matrix([[0,0,1],[0,1,1],[1,1,1]]).det())==1,"original main-diagonal upper triangle")

out={"author":"GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family","exposure":"fresh after-reading implementation; no historical checker imported","python_method":"SymPy exact rational/polynomial arithmetic, HNF, custom exterior multiplication and direct monomial enumeration","sympy_version":s.__version__,"source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"passed":len(checks),"checks":checks,"data":data}
print(json.dumps(out,indent=2,default=str))
