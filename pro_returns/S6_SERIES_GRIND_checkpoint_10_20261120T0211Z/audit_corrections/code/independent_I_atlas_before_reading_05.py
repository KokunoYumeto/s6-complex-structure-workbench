"""Fresh symbolic checks, written before exposure to receiving C3.8 proof.

Only the isolated target and the explicitly permitted earlier inputs were read.
The complete mathematical derivation is in I_atlas_before_reading_05.md.
This program verifies finite identities, not analytic compactness/properness.
"""
import hashlib
import json
import time
from pathlib import Path
import sympy as s

started = time.perf_counter()
checks = []

def check(name, expression):
    entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
    residuals = [s.factor(s.cancel(x)) for x in entries]
    ok = all(x == 0 for x in residuals)
    checks.append({"name": name, "passed": ok,
                   "residuals": [str(x) for x in residuals]})
    if not ok:
        raise AssertionError((name, residuals))

T, M, B, Td, Md, Bd = s.symbols("tau mu beta tau_t mu_t beta_t")
J = s.Matrix([[0, 1], [6, 0]])
Z = s.Matrix([[6*M, T], [B, M]])
Zd = s.Matrix([[6*Md, Td], [Bd, Md]])
K = 6*Md**2 - Td*Bd
S = J * Zd.inv()
check("S explicit symmetric expression", S-s.Matrix([[-Bd,6*Md],[6*Md,-6*Td]])/K)
check("S symmetric", S-S.T)
check("S Z_t equals J", S*Zd-J)

def deriv(expr):
    return s.diff(expr,T)*Td+s.diff(expr,M)*Md+s.diff(expr,B)*Bd

period_maps = [
    ((T-1)/T, (1-M)/T, B+2-6*(1-M)**2/T,
     s.Matrix([[-1/T,0],[(1-M)/T,1]])),
    (-1/T, 1+M/T, B-3-6*M**2/T,
     s.Matrix([[1/T,0],[-M/T,1]])),
]
for n,(t,m,b,R) in enumerate(period_maps,1):
    Zp = s.Matrix([[6*m,t],[b,m]])
    Sp = J * Zp.applyfunc(deriv).inv()
    check(f"generator {n} exact quadratic tensor covariance", R.T*Sp*R-S)
    check(f"generator {n} vertical field covariance", R*s.Matrix([0,1])-s.Matrix([0,1]))

A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
v1=s.Matrix([1,2,-4,0]); v2=s.Matrix([-1,-3,3,0])
for n,A,v,m in [(1,A1,v1,3),(2,A2,v2,4)]:
    check(f"finite {n} order {m}", A**m-s.eye(4))
    check(f"finite {n} original vector fixed", A*v-v)
    total=s.zeros(4,1)
    for k in range(m): total += A**k*v/s.Integer(m)
    check(f"finite {n} m-th affine power is original lattice vector", total-v)

# Primitive A and the complete lattice one-form, with base derivative terms.
u,g,w,d,t=s.symbols("u gamma w delta t")
nu,ng,nw,nd=s.symbols("n_u n_gamma n_w n_delta")
coords=[g,u,w,d,t]
dz1=s.Matrix([6*M,T,1,0,6*g*Md+u*Td])
dz2=s.Matrix([B,M,0,1,g*Bd+u*Md])
dt=s.Matrix([0,0,0,0,1])
A=u*dz1+6*g*dz2-(u*u*Td+12*u*g*Md+6*g*g*Bd)*dt/2

def total_deriv(expr,index):
    if index == 4:
        return deriv(expr)
    return s.diff(expr,coords[index])

for i in range(5):
    for j in range(i+1,5):
        target=6 if (i,j)==(0,3) else 1 if (i,j)==(1,2) else 0
        check(f"dA fibre-flat exterior coefficient {i},{j}",
              total_deriv(A[j],i)-total_deriv(A[i],j)-target)

# Pull back A at translated coordinates, including differential translation.
dz1p=dz1+(6*ng*Md+nu*Td)*dt
dz2p=dz2+(ng*Bd+nu*Md)*dt
Ap=(u+nu)*dz1p+6*(g+ng)*dz2p-((u+nu)**2*Td+
    12*(u+nu)*(g+ng)*Md+6*(g+ng)**2*Bd)*dt/2
alambda=nu*dz1+6*ng*dz2+(nu**2*Td+12*nu*ng*Md+6*ng**2*Bd)*dt/2
check("complete lattice primitive difference",Ap-A-alambda)
lam=s.Matrix([ng,nu])
check("quadratic-lift lattice cross coefficient", (Zd*lam).T*S-lam.T*J.T)
check("quadratic-lift lattice base coefficient",
      ((Zd*lam).T*S*(Zd*lam))[0]-(nu**2*Td+12*nu*ng*Md+6*ng**2*Bd))

# Cusp residue identities; full C(q) enters the analytic formula in the report.
B0=s.Matrix([[0,1],[-1,0]])
H=s.diag(1,-6)
check("cusp limiting matrix J B0 inverse",J*B0.inv()-H)
check("cusp exact H B0 equals J",H*B0-J)
vx,vy,l1,l2=s.symbols("v_x v_y lambda_1 lambda_2")
v=s.Matrix([vx,vy]); lam=s.Matrix([l1,l2]); shift=B0*lam
res=(lam.T*J.T*v)[0]+(lam.T*B0.T*J*lam)[0]/2+((v.T*H*v)[0]-((v+shift).T*H*(v+shift))[0])/2
check("all-ray exact logarithmic cusp residue cancellation",res)

z0,z1,z2=s.symbols("z0 z1 z2",nonzero=True)
e0,e1,e2=s.symbols("dz0 dz1 dz2")
b00,b01,b02,b11,b12,b22=s.symbols("B00 B01 B02 B11 B12 B22")
bmat=s.Matrix([[b00,b01,b02],[b01,b11,b12],[b02,b12,b22]])
logs=s.Matrix([e0/z0,e1/z1,e2/z2]); q=z0*z1*z2
dq=z1*z2*e0+z0*z2*e1+z0*z1*e2
raw=q*(logs.T*bmat*logs)[0]/2
sub=dq*(b00*e0/z0+b11*e1/z1+b22*e2/z2)/2
regular=(b01-(b00+b11)/2)*z2*e0*e1+(b02-(b00+b22)/2)*z1*e0*e2+(b12-(b11+b22)/2)*z0*e1*e2
check("toric quadratic lift regular at every double and triple point",raw-sub-regular)

for name,vertices in [
    ("lower",[(vx,vy),(vx+1,vy),(vx,vy+1)]),
    ("upper",[(vx+1,vy),(vx,vy+1),(vx+1,vy+1)])]:
    V=s.Matrix([[p[0] for p in vertices],[p[1] for p in vertices],[1,1,1]])
    Vp=V.copy()
    for j in range(3):
        Vp[0,j]+=shift[0]; Vp[1,j]+=shift[1]
    U=s.Matrix([[1,0,shift[0]],[0,1,shift[1]],[0,0,1]])
    check(f"{name} exact fan translation matrix",Vp-U*V)
    check(f"{name} integral unimodular absolute determinant",V.det()**2-1)
    check(f"{name} full unit multiplier spatial exponents",Vp.inv()[:,:2]-V.inv()[:,:2])
    check(f"{name} product of cusp coordinate unit multipliers is one",s.ones(1,3)*V.inv()[:,:2])

check("standard exponential sign p is minus one",12*0-4*1-3*(-1)+1)
output={"status":"PASS","checks":checks,"count":len(checks),
        "seconds":round(time.perf_counter()-started,6),
        "exposure":"Before receiving C3.8 proof; isolated target plus permitted earlier inputs and DGKX v1 period/scalar tables only.",
        "scope":"Exact finite algebra. Analytic extension and locally finite partition are proved in the accompanying prereading derivation.",
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
dest=Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:v for k,v in output.items() if k!='checks'},indent=2))
