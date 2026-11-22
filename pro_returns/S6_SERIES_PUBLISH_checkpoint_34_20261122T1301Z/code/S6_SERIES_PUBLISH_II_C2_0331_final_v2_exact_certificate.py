"""Exact postrelease certificate for E.2.16.

New method: explicit integral generators of the difference-image lattice,
followed by a symbolic characteristic polynomial and exact permutations.
Historical comparison: the actually retrieved D_exact_checks.py lines 11--24
use simultaneous nullspaces and Smith normal form. The named
e_push_interior_cusp.py was not retrieved and is not run here.
"""
from pathlib import Path
from fractions import Fraction as F
from contextlib import redirect_stdout
import io, json, hashlib
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

I=s.eye(4)
A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
e=[I[:,j] for j in range(4)]
x=(A1-I)*e[1]
y=(A2-I)*e[1]
zv=(A1-I)*e[2]
assert e[1]==-2*y-zv
assert e[2]==-y-zv
assert e[3]==x-3*y-2*zv
assert (A1-I)[0,:]==s.zeros(1,4)==(A2-I)[0,:]
gamma=s.Matrix([[1,0,0,0]])
assert gamma*A1==gamma==gamma*A2
N=s.zeros(4);N[2,1]=1;N[3,0]=-1
assert N*e[1]==e[2] and N*e[0]==-e[3]
assert N*e[2]==s.zeros(4,1)==N*e[3]
assert N*N==s.zeros(4)
for cov in [s.Matrix([[1,0,0,0]]),s.Matrix([[0,1,0,0]])]:
    assert cov*N==s.zeros(1,4)

ca,sa,cb,sb,r,ct,lam,w=s.symbols("ca sa cb sb r ct lam w", nonzero=True)
R=s.Matrix([[ca,sa],[-sa,ca]])
Q=s.Matrix([[cb,r*sb],[-sb/r,cb]])
C=R*Q
trace=2*ca*cb-(r+1/r)*sa*sb
assert s.expand(s.trace(C)-trace)==0
assert s.expand(C.det()-(ca**2+sa**2)*(cb**2+sb**2))==0
assert s.expand((lam*s.eye(2)-C).det()-
                (lam**2-trace*lam+(ca**2+sa**2)*(cb**2+sb**2)))==0
H=(ct+ca*cb)/(sa*sb)
assert s.cancel(2*ca*cb-2*H*sa*sb+2*ct)==0
# On the unit-circle identities and cosh(ell)=H, this is the exact
# characteristic polynomial. Its roots are -w and -w^-1 for
# w=exp(pi*i/d), so their ratio is a primitive d-th root.
char=lam**2+2*ct*lam+1
assert s.cancel(char.subs({ct:(w+1/w)/2,lam:-w}))==0
assert s.cancel(char.subs({ct:(w+1/w)/2,lam:-1/w}))==0
assert F(1,3)+F(1,4)+F(1,3)==F(11,12)<1
assert max(F(1,6)+F(1,4)+F(1,2),F(1,3)+F(1,8)+F(1,2))==F(23,24)<1

def compose(a,b): return tuple(a[b[j]-1] for j in range(len(a)))
def order(a):
    v=tuple(range(1,len(a)+1));b=v
    for k in range(1,25):
        b=compose(a,b)
        if b==v:return k
    raise AssertionError("order not found")
a=(2,3,1,4)        # (123)
b=(3,4,2,1)        # (1324)
ab=compose(a,b)
assert order(a)==3 and order(b)==4 and ab==(1,4,3,2) and order(ab)==2
k,l=s.symbols("k l")
assert s.expand(13*k*l-3*k-4*l-
    (13*(k-1)*(l-1)+10*(k-1)+9*(l-1)+6))==0

root=next(p for p in Path(__file__).resolve().parents
          if (p/"records/S6_SERIES_PUBLISH_II_opened_programs_01/D_exact_checks.py").is_file())
old=root/"records/S6_SERIES_PUBLISH_II_opened_programs_01/D_exact_checks.py"
raw=old.read_text()
scope="\n".join(raw.splitlines()[10:24])+"\n"
capture=io.StringIO()
env={"s":s,"smith_normal_form":smith_normal_form,"ZZ":ZZ}
with redirect_stdout(capture):exec(compile(scope,str(old)+":11-24","exec"),env)
assert env["A1"]==A1 and env["A2"]==A2

out={
 "fresh_checks":{
   "difference_generators":{"x":list(map(int,x)),"y":list(map(int,y)),"z":list(map(int,zv))},
   "integral_basis_identities":["u=-2y-z","w=-y-z","delta=x-3y-2z"],
   "common_invariant_covectors":"Q*gamma, gamma=(1,0,0,0); explicit integral annihilator basis",
   "cusp_invariant_covectors":"span_Q(gamma,u_dual), dimension 2; im(N)=Z*w+Z*delta",
   "trace":"2 ca cb -(r+r^-1) sa sb = -2 ct after cosh(ell) substitution",
   "determinant":"(ca^2+sa^2)(cb^2+sb^2)=1",
   "characteristic_polynomial":"lambda^2+2 ct lambda+1; roots -w,-w^-1 for 2ct=w+w^-1",
   "projective_order_argument":"w=exp(pi*i/d) gives primitive eigenvalue ratio w^2; analytic angle inequality is proved in the comparison",
   "angle_sum_bounds":["11/12 for d>=3","23/24 for d=2 except (m,n)=(3,4)"],
   "exceptional_permutations":{"a":a,"b":b,"ab":ab,"orders":[order(a),order(b),order(ab)]},
   "canonical_integer_identity":True
 },
 "historical_comparison":{
   "path":str(old.relative_to(root)),
   "sha256":hashlib.sha256(old.read_bytes()).hexdigest(),
   "executed_lines":[11,24],
   "scope_sha256":hashlib.sha256(scope.encode()).hexdigest(),
   "stdout":capture.getvalue(),
   "method":"Retrieved historical slice solves simultaneous nullspaces and uses Smith normal form; fresh check uses explicit integral image generators and annihilator identities."
 },
 "missing_named_routine":{"name":"e_push_interior_cusp.py","retrieved":False,"read":False,"replayed":False},
 "all_assertions_passed":True,
 "independence":"Postrelease computational check in the target's single evidence group; no additional blind derivation credit."
}
print(json.dumps(out,indent=2))
