"""Bounded exact checks for the full coupling-fibre elimination.

No numerical search, no subprocesses, no network, no Lean.  One algebra
process, one BLAS worker, 55-second watchdog. The finite-root theorem,
positive domains and global degree bounds are proved in the TeX.
"""
import os
for task_thread_variable in (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS",
):
    os.environ[task_thread_variable] = "1"
import threading
import time
started = time.monotonic()
watchdog = threading.Timer(55.0, lambda: os._exit(124))
watchdog.daemon = True
watchdog.start()
import sympy as s

checks = 0
def same(a,b):
    global checks
    delta=a-b
    entries=list(delta) if isinstance(delta,s.MatrixBase) else [delta]
    for e in entries:
        assert s.simplify(e)==0, e
    checks += 1

def comm(x,y): return (x*y-y*x).applyfunc(s.expand)
def inner(x,y): return s.expand(-s.trace(x*y))
def tf(x): return (x-s.trace(x)*s.eye(3)/3).applyfunc(s.expand)
def vector_norm(x): return s.expand((x.conjugate().T*x)[0])

r=s.sqrt(6)/4
H=s.diag(0,r,-r)
q=s.Matrix([1/(2*s.sqrt(2)),0,0])
F=s.diag(-2,1-2*r,1+2*r)
J=s.I*H
Q=q*q.T
Iop=lambda x: tf(comm(H,comm(H,x))+Q*x+x*Q)
same(inner(J,J),s.Rational(3,4))
same(Iop(J),s.zeros(3))
same(J*q,s.zeros(3,1))

# Full diagonal-frame coordinates; this is an exact invertible frame change.
x=s.Rational(1,2); d0=1/(2*s.sqrt(2))
S=s.Matrix([[d0,-(r+x)],[r+x,d0]])/s.sqrt(2*r*(r+x))
U=s.diag(1,S)
Ho=s.Matrix([[0,0,0],[0,-x,d0],[0,d0,x]])
same(U.T*U,s.eye(3))
same(U.T*Ho*U,H)
same(U.T*q,q)

def matrix(a,h,v1,v2,z):
    b=(h-a)/2
    return s.Matrix([[s.I*a,-s.conjugate(v1),-s.conjugate(v2)],
                     [v1,s.I*b,z],
                     [v2,-s.conjugate(z),-s.I*(a+b)]])

a,h,v1r,v1i,v2r,v2i,zr,zi=s.symbols('a h v1r v1i v2r v2i zr zi',real=True)
X=matrix(a,h,v1r+s.I*v1i,v2r+s.I*v2i,zr+s.I*zi)
same(inner(X,X),s.Rational(3,2)*a*a+h*h/2+
     2*(v1r*v1r+v1i*v1i+v2r*v2r+v2i*v2i+zr*zr+zi*zi))
Da,Dz,D1,D2,Dh=s.symbols('Da Dz D1 D2 Dh',real=True)
norm_difference=s.Rational(3,2)*Da+Dh/2+2*(D1+D2+Dz)
same(norm_difference.subs({Da:4*Dz,D2:2-4*Dz-D1}),4+Dh/2)
print('PASS: original H/q frame and full symbolic signed norm law')

W=[s.I*s.diag(2,-1,-1)]
for j,k in ((0,1),(0,2),(1,2)):
    b=s.zeros(3); b[j,k]=-1; b[k,j]=1; W.append(b)
    b=s.zeros(3); b[j,k]=s.I; b[k,j]=s.I; W.append(b)
norms=[inner(b,b) for b in W]
def coords(y): return s.Matrix([s.simplify(inner(b,y)/n) for b,n in zip(W,norms)])
def lift(v):
    out=s.zeros(3)
    for b,c in zip(W,v): out+=b*c
    return out
def projection(y): return (y-inner(J,y)*J/inner(J,J)).applyfunc(s.expand)
I7=s.Matrix.hstack(*[coords(Iop(b)) for b in W])
same(I7,s.diag(s.Rational(1,6),s.Rational(1,2),s.Rational(1,2),
                    s.Rational(1,2),s.Rational(1,2),s.Rational(3,2),s.Rational(3,2)))
same(I7.det(),s.Rational(3,128))
for basis_vector in W[-2:]:
    same(basis_vector*q,s.zeros(3,1))
    same(Iop(basis_vector),s.Rational(3,2)*basis_vector)

# One fixed full-algebra pair; all eight real coordinates of each are nonzero.
Z1=matrix(s.Integer(1),s.Integer(3),1+s.I,2-s.I,1+2*s.I)
Z2=matrix(s.Integer(2),s.Integer(-2),-1+2*s.I,3+s.I,2-3*s.I)
B=comm(Z1,Z2)
assert s.simplify(inner(B,B))>0
Kop=lambda y:-comm(Z1,comm(Z1,y))-comm(Z2,comm(Z2,y))
eta=s.simplify(inner(J,Kop(J)))
assert eta>0
w=s.simplify(projection(Kop(J)))
beta=s.simplify(inner(J,B))
Sop=lambda y:projection(Kop(y))-w*inner(w,y)/eta
S7=s.simplify(s.Matrix.hstack(*[coords(Sop(b)) for b in W]))
f=s.simplify(projection(B)-beta*w/eta)
f7=coords(f)
alpha=s.Rational(1,4)+vector_norm(Z1*q)+vector_norm(Z2*q)

for t in (s.Integer(1),s.Integer(3)):
    M=t*I7+2*S7
    D=s.factor(M.det())
    assert D>0
    vc=4*M.inv()*f7*D
    V=s.simplify(lift(vc))
    N=s.simplify(V+(2*beta*D-inner(w,V))*J/eta)
    T=(N/D).applyfunc(s.expand)
    same(t*Iop(T)+2*Kop(T),4*B)
    same(T*q,V*q/D)
    q7=s.simplify(vector_norm(V*q))
    assert q7>0
    tau=alpha*D*D/q7

    RH=tau*comm(T,comm(T,H))-comm(Z1,comm(Z1,H))-comm(Z2,comm(Z2,H))-F
    Rq=(tau*T*T-Z1*Z1-Z2*Z2)*q+2*q
    R1=tau*(-Z1-2*comm(T,Z2)+comm(T,comm(T,Z1)))+Kop(Z1)+t*Iop(Z1)/2
    R2=tau*(-Z2+2*comm(T,Z1)+comm(T,comm(T,Z2)))+Kop(Z2)+t*Iop(Z2)/2
    PH=alpha*comm(N,comm(N,H))-q7*(comm(Z1,comm(Z1,H))+comm(Z2,comm(Z2,H))+F)
    Pq=alpha*N*N*q+q7*(2*s.eye(3)-Z1*Z1-Z2*Z2)*q
    P1=alpha*(-D*D*Z1-2*D*comm(N,Z2)+comm(N,comm(N,Z1)))+q7*(Kop(Z1)+t*Iop(Z1)/2)
    P2=alpha*(-D*D*Z2+2*D*comm(N,Z1)+comm(N,comm(N,Z2)))+q7*(Kop(Z2)+t*Iop(Z2)/2)
    for actual,poly in ((RH,PH),(Rq,Pq),(R1,P1),(R2,P2)):
        same(actual,poly/q7)

    # Verify the pre-existing full spatial stress signs on the same pair.
    G=s.Matrix(2,2,lambda j,k:inner((Z1,Z2)[j],(Z1,Z2)[k]))
    DT=s.Matrix(2,2,lambda j,k:inner(comm(T,(Z1,Z2)[j]),comm(T,(Z1,Z2)[k])))
    IM=s.Matrix(2,2,lambda j,k:inner((Z1,Z2)[j],Iop((Z1,Z2)[k])))
    d=inner(B,B); bt=inner(T,B)
    pairings=s.Matrix(2,2,lambda j,k:inner((Z1,Z2)[j],(R1,R2)[k]))
    same(pairings,-tau*(G+DT-2*bt*s.eye(2))+d*s.eye(2)+t*IM/2)
    # The polynomial zero is never confused with these nonzero test residuals.
    assert s.simplify(vector_norm(Pq))>0
    print(f'PASS: full Schur inverse, every residual numerator and stress at g²={t}')

# A direct empty-domain test; no test point is substituted for the full class.
E1,E2=W[-2:]
EB=comm(E1,E2)
EK=lambda y:-comm(E1,comm(E1,y))-comm(E2,comm(E2,y))
eeta=inner(J,EK(J)); ew=projection(EK(J)); ebeta=inner(J,EB)
assert eeta>0
ef=projection(EB)-ebeta*ew/eeta
same(ef,s.zeros(3))
eT=2*ebeta*J/eeta
same(Iop(eT)+2*EK(eT),4*EB)
same(eT*q,s.zeros(3,1))
print('PASS: two-dimensional matter-annihilating space and exact empty-domain witness')

watchdog.cancel()
print(f'ALL {checks} EXACT IDENTITY CHECKS PASSED in {time.monotonic()-started:.3f} seconds.')
