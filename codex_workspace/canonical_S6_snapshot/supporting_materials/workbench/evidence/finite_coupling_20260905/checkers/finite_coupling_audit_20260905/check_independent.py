"""Independent exact finite-coupling audit: different pair and direct 8D solve.

No external input modules, numerical search, network, Lean, or subprocesses.
Exact symbolic identities, one process, single arithmetic worker, 55s watchdog.
"""
import os
for audit_worker_key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                         "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS"):
    os.environ[audit_worker_key] = "1"
import threading
import time
audit_started = time.monotonic()
audit_watchdog = threading.Timer(55.0, lambda: os._exit(124))
audit_watchdog.daemon = True
audit_watchdog.start()
import sympy as s

audit_checks = 0
def expand(x):
    return x.applyfunc(s.expand) if isinstance(x, s.MatrixBase) else s.expand(x)
def equal(x, y):
    global audit_checks
    d = expand(x-y)
    terms = list(d) if isinstance(d, s.MatrixBase) else [d]
    assert all(s.simplify(e) == 0 for e in terms), d
    audit_checks += 1
def bracket(x, y): return expand(x*y-y*x)
def ip(x, y): return expand(-s.trace(x*y))
def vn(v): return expand((s.conjugate(v).T*v)[0])
def tf(x): return expand(x-s.trace(x)*s.eye(3)/3)
def mat(a,h,v1,v2,z):
    b=(s.sympify(h)-a)/2
    return s.Matrix([[s.I*a,-s.conjugate(v1),-s.conjugate(v2)],
                     [v1,s.I*b,z],[v2,-s.conjugate(z),-s.I*(a+b)]])

r=s.sqrt(6)/4
H=s.diag(0,r,-r)
q=s.Matrix([1/(2*s.sqrt(2)),0,0])
F=s.diag(-2,1-2*r,1+2*r)
J=s.I*H
Iop=lambda x:tf(bracket(H,bracket(H,x))+q*q.T*x+x*q*q.T)
basis=[s.I*s.diag(2,-1,-1)]
for j,k in ((0,1),(0,2),(1,2)):
    e=s.zeros(3); e[j,k]=-1; e[k,j]=1; basis.append(e)
    e=s.zeros(3); e[j,k]=s.I; e[k,j]=s.I; basis.append(e)
full_basis=basis+[s.I*s.diag(0,1,-1)]
def coord(x, bb=basis): return s.Matrix([s.simplify(ip(b,x)/ip(b,b)) for b in bb])
def lift(c, bb=basis):
    y=s.zeros(3)
    for b,a in zip(bb,c): y+=a*b
    return expand(y)
def proj(x): return expand(x-ip(J,x)*J/ip(J,J))
I7=s.Matrix.hstack(*[coord(Iop(b)) for b in basis])
delta=I7.det()
equal(delta,s.Rational(3,128))
equal(ip(J,J),s.Rational(3,4))

# Distinct from the supplied checkpoint's pair, with all original real
# coordinate entries nonzero. The diagonal frame is an invertible conjugation.
Z1=mat(1,2,1+s.I,-1+2*s.I,2-s.I)
Z2=mat(-2,1,2+3*s.I,1-s.I,-1+2*s.I)
Z=(Z1,Z2)
B=bracket(Z1,Z2)
Kop=lambda x:-bracket(Z1,bracket(Z1,x))-bracket(Z2,bracket(Z2,x))
eta=ip(J,Kop(J)); beta=ip(J,B); w=proj(Kop(J))
assert eta>0 and ip(B,B)>0
Sop=lambda x:expand(proj(Kop(x))-w*ip(w,x)/eta)
S7=s.Matrix.hstack(*[coord(Sop(b)) for b in basis])
f=expand(proj(B)-beta*w/eta)
fc=coord(f)
alpha=s.Rational(1,4)+vn(Z1*q)+vn(Z2*q)
t=s.symbols('t',real=True)

# Polynomial determinant and vector adjugate via exact characteristic
# polynomial recursion, independently of a 7D adjugate or inverse routine.
C7=2*I7.inv()*S7
charpoly=C7.charpoly()
D=s.Poly(-delta*charpoly.as_expr().subs(charpoly.gen,-t),t).as_expr()
equal(s.Poly(D,t).LC(),delta)
assert s.degree(D,t)==7
bf=I7.inv()*fc
vcoeff={6:4*delta*bf}
for j in range(5,-1,-1):
    vcoeff[j]=expand(4*s.Poly(D,t).nth(j+1)*bf-C7*vcoeff[j+1])
Vc=sum((vcoeff[j]*t**j for j in range(7)),s.zeros(7,1))
equal((t*I7+2*S7)*Vc,4*D*fc)
V=lift(Vc)
N=expand(V+(2*beta*D-ip(w,V))*J/eta)
Q=vn(V*q)
assert s.degree(Q,t)<=12 and Q!=0
equal(t*Iop(N)+2*Kop(N),4*D*B)
equal(N*q,V*q)
print('PASS: polynomial 7D numerator and full 8D Gauss identity',flush=True)

PH=expand(alpha*bracket(N,bracket(N,H))-Q*(bracket(Z1,bracket(Z1,H))+bracket(Z2,bracket(Z2,H))+F))
Pq=expand(alpha*N*N*q+Q*(2*s.eye(3)-Z1*Z1-Z2*Z2)*q)
P1=expand(alpha*(-D*D*Z1-2*D*bracket(N,Z2)+bracket(N,bracket(N,Z1)))+Q*(Kop(Z1)+t*Iop(Z1)/2))
P2=expand(alpha*(-D*D*Z2+2*D*bracket(N,Z1)+bracket(N,bracket(N,Z2)))+Q*(Kop(Z2)+t*Iop(Z2)/2))
for P,sign in ((PH,1),(P1,-1),(P2,-1)):
    equal(s.conjugate(P).T,sign*P)
    equal(s.trace(P),0)
p=expand(s.trace(PH*PH)+vn(Pq)-s.trace(P1*P1)-s.trace(P2*P2))
assert s.degree(p,t)==28
a=2*beta/eta
L1=expand(-Z1-2*a*bracket(J,Z2)+a*a*bracket(J,bracket(J,Z1)))
L2=expand(-Z2+2*a*bracket(J,Z1)+a*a*bracket(J,bracket(J,Z2)))
lead=expand(alpha**2*delta**4*(ip(L1,L1)+ip(L2,L2)))
assert lead>0
equal(s.Poly(p,t).LC(),lead)
equal(P1.applyfunc(lambda e:s.Poly(e,t).nth(14)),alpha*delta**2*L1)
equal(P2.applyfunc(lambda e:s.Poly(e,t).nth(14)),alpha*delta**2*L2)
print('PASS: exact degree 28, positive leading coefficient, all codomains',flush=True)

for tv in (s.Integer(2),s.Rational(5,3)):
    # Direct eight-dimensional inverse in a separate full basis.
    fullL=s.Matrix.hstack(*[coord(tv*Iop(b)+2*Kop(b),full_basis) for b in full_basis])
    direct=lift(fullL.inv()*4*coord(B,full_basis),full_basis)
    Dv=D.subs(t,tv); Qv=Q.subs(t,tv); Nv=N.subs(t,tv)
    assert Dv>0 and Qv>0
    equal(direct,Nv/Dv)
    tau=alpha*Dv**2/Qv
    for epsilon in (-1,1):
        omega=epsilon*s.sqrt(tau)
        temporal=epsilon*s.sqrt(alpha)*Nv/s.sqrt(Qv)
        equal(temporal,omega*direct)
        equal(tv*Iop(temporal)+2*Kop(temporal),4*omega*B)
        fullH=bracket(temporal,bracket(temporal,H))-bracket(Z1,bracket(Z1,H))-bracket(Z2,bracket(Z2,H))-F
        fullq=expand((temporal*temporal-Z1*Z1-Z2*Z2)*q+2*q)
        full1=expand(-omega**2*Z1-2*omega*bracket(temporal,Z2)+bracket(temporal,bracket(temporal,Z1))+Kop(Z1)+tv*Iop(Z1)/2)
        full2=expand(-omega**2*Z2+2*omega*bracket(temporal,Z1)+bracket(temporal,bracket(temporal,Z2))+Kop(Z2)+tv*Iop(Z2)/2)
        for actual,poly in ((fullH,PH),(fullq,Pq),(full1,P1),(full2,P2)):
            equal(actual,poly.subs(t,tv)/Qv)
        assert vn(fullq)>0  # These are tests of identities, never solutions.
    print(f'PASS: direct 8D inverse and all original equations on both branches at t={tv}',flush=True)

# Independent empty-domain case with f nonzero: the full lower su(2)
# carrier annihilates q and is closed under the two operators.
E1=full_basis[-1]+basis[-2]; E2=basis[-1]
EB=bracket(E1,E2)
EK=lambda x:-bracket(E1,bracket(E1,x))-bracket(E2,bracket(E2,x))
eeta=ip(J,EK(J)); ebeta=ip(J,EB); ew=proj(EK(J))
ef=expand(proj(EB)-ebeta*ew/eeta)
eS=lambda x:expand(proj(EK(x))-ew*ip(ew,x)/eeta)
assert ip(ef,ef)>0
for vv in (ef,eS(ef),eS(eS(ef))): equal(vv*q,s.zeros(3,1))
fullEL=s.Matrix.hstack(*[coord(Iop(b)+2*EK(b),full_basis) for b in full_basis])
eT=lift(fullEL.inv()*4*coord(EB,full_basis),full_basis)
equal(eT*q,s.zeros(3,1))
print('PASS: all three empty-domain tests with f nonzero and direct Gauss inverse',flush=True)
audit_watchdog.cancel()
print(f'ALL {audit_checks} INDEPENDENT EXACT CHECKS PASSED in {time.monotonic()-audit_started:.3f}s',flush=True)
