"""Bounded exact checker for unrestricted rotating-gauge constraint formulas.

One computational process; no network, subprocesses, numerical search or Lean.
All 24 real connection coordinates are symbolic in the scalar/stress checks.
A 55-second watchdog fails closed; the extra timer thread performs no algebra.
"""
import os
for thread_variable in (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS",
):
    os.environ[thread_variable] = "1"

import threading
import time

started = time.monotonic()
watchdog = threading.Timer(55.0, lambda: os._exit(124))
watchdog.daemon = True
watchdog.start()

import sympy as s


def comm(a, b):
    return a*b-b*a


def tf(a):
    return a-s.trace(a)*s.eye(3)/3


def inner(a, b):
    return -s.trace(a*b)


def sqnorm(a):
    return s.expand(s.conjugate(a)*a)


def same(a, b):
    difference = a-b
    entries = list(difference) if isinstance(difference, s.MatrixBase) else [difference]
    for entry in entries:
        assert s.expand(entry) == 0, s.expand(entry)


def coordinates(tag):
    a,b,u1,w1,u2,w2,x,y = s.symbols(
        f"{tag}a {tag}b {tag}u1 {tag}w1 {tag}u2 {tag}w2 {tag}x {tag}y",
        real=True,
    )
    v1=u1+s.I*w1
    v2=u2+s.I*w2
    z=x+s.I*y
    matrix=s.Matrix([
        [s.I*a,-s.conjugate(v1),-s.conjugate(v2)],
        [v1,s.I*b,z],
        [v2,-s.conjugate(z),-s.I*(a+b)],
    ])
    return dict(a=a,b=b,v1=v1,v2=v2,z=z,h=a+2*b,matrix=matrix)


cc,zz1,zz2=[coordinates(tag) for tag in ("c","x","y")]
data=[cc,zz1,zz2]
C,Z1,Z2=[item["matrix"] for item in data]
for matrix in (C,Z1,Z2):
    same(matrix+s.conjugate(matrix).T,s.zeros(3))
    same(s.trace(matrix),0)

r=s.sqrt(6)/4
q=s.Matrix([1/(2*s.sqrt(2)),0,0])
H=s.diag(0,r,-r)
F=s.diag(-2,1-2*r,1+2*r)


def signed(fn):
    return s.expand(fn(cc)-fn(zz1)-fn(zz2))


Da=signed(lambda t:t["a"]**2)
Dz=signed(lambda t:sqnorm(t["z"]))
D1=signed(lambda t:sqnorm(t["v1"]))
D2=signed(lambda t:sqnorm(t["v2"]))
m1=signed(lambda t:t["h"]*t["v1"])
m2=signed(lambda t:t["h"]*t["v2"])
mz=signed(lambda t:t["h"]*t["z"])
n1=signed(lambda t:t["z"]*t["v2"]+s.I*t["a"]*t["v1"]/2)
n2=signed(lambda t:s.conjugate(t["z"])*t["v1"]-s.I*t["a"]*t["v2"]/2)
QH=comm(C,comm(C,H))-comm(Z1,comm(Z1,H))-comm(Z2,comm(Z2,H))-F
Qq=(C*C-Z1*Z1-Z2*Z2)*q+2*q
expectedH=s.diag(
    2*r*(D1-D2)+2,
    -2*r*D1-4*r*Dz-(1-2*r),
    2*r*D2+4*r*Dz-(1+2*r),
)
expectedH[1,0]=r*(3*n1-s.I*m1/2)
expectedH[2,0]=r*(3*n2-s.I*m2/2)
expectedH[1,2]=-2*s.I*r*mz
expectedH[0,1]=s.conjugate(expectedH[1,0])
expectedH[0,2]=s.conjugate(expectedH[2,0])
expectedH[2,1]=s.conjugate(expectedH[1,2])
expectedq=q[0]*s.Matrix([2-Da-D1-D2,n1+s.I*m1/2,-n2-s.I*m2/2])
same(QH,expectedH)
same(Qq,expectedq)
print("PASS: complete scalar residual reconstruction on all 24 real color coordinates",flush=True)

delta=1/(2*r)
daz,dz0=s.symbols("daz dz0",real=True)
same(2*r*((1-delta-2*dz0)-(1+delta-2*dz0))+2,0)
same(-2*r*(1-delta-2*dz0)-4*r*dz0-(1-2*r),0)
same(2*r*(1+delta-2*dz0)+4*r*dz0-(1+2*r),0)
same(2-4*dz0-(1-delta-2*dz0)-(1+delta-2*dz0),0)
same(3*(n1+s.I*m1/2)-(3*n1-s.I*m1/2),2*s.I*m1)
same(-3*(-n2-s.I*m2/2)-(3*n2-s.I*m2/2),2*s.I*m2)
same(inner(s.I*H,C),r*cc["h"])
print("PASS: exact inverse scalar-entry relations and original stabilizer coefficient",flush=True)


def inertia(matrix):
    return tf(comm(H,comm(H,matrix))+q*q.T*matrix+matrix*q*q.T)


inertiaExpected=s.Matrix([
    [s.I*cc["a"]/6,-s.conjugate(cc["v1"])/2,-s.conjugate(cc["v2"])/2],
    [cc["v1"]/2,-s.I*cc["a"]/12,3*cc["z"]/2],
    [cc["v2"]/2,-3*s.conjugate(cc["z"])/2,-s.I*cc["a"]/12],
])
same(inertia(C),inertiaExpected)
same(inner(C,inertia(C)),cc["a"]**2/4+sqnorm(cc["v1"])+sqnorm(cc["v2"])+3*sqnorm(cc["z"]))
print("PASS: entire su(3) inertia, including all kinetic coefficients",flush=True)

G,omega=s.symbols("G omega",real=True)
Z=[Z1,Z2]


def K(matrix):
    return -comm(Z1,comm(Z1,matrix))-comm(Z2,comm(Z2,matrix))


spatial=[
    -omega**2*Z1-2*omega*comm(C,Z2)+comm(C,comm(C,Z1))+K(Z1)+G*inertia(Z1)/2,
    -omega**2*Z2+2*omega*comm(C,Z1)+comm(C,comm(C,Z2))+K(Z2)+G*inertia(Z2)/2,
]
gram=s.Matrix(2,2,lambda j,k:inner(Z[j],Z[k]))
cgram=s.Matrix(2,2,lambda j,k:inner(comm(C,Z[j]),comm(C,Z[k])))
mass=s.Matrix(2,2,lambda j,k:inner(Z[j],inertia(Z[k])))
bracket=comm(Z1,Z2)
d=inner(bracket,bracket)
beta=inner(C,bracket)
pairing=s.Matrix(2,2,lambda j,k:inner(Z[j],spatial[k]))
same(pairing,-omega**2*gram-cgram+G*mass/2+(d+2*omega*beta)*s.eye(2))
print("PASS: full 2x2 spatial pairing matrix with unrestricted complex entries",flush=True)

n,b,c,A11,A12,A22=s.symbols("n b c A11 A12 A22",real=True)
h=n*c-b*b
discriminant=(A11*c+A22*n-2*A12*b)**2-4*(A11*A22-A12*A12)*h
squares=(A11*(n*c-2*b*b)+2*b*n*A12-n*n*A22)**2+4*h*(n*A12-b*A11)**2
same(n*n*discriminant,squares)
same((A11*(n*c-2*b*b)+2*b*n*A12-n*n*A22).subs(A12,b*A11/n),n*(c*A11-n*A22))
print("PASS: exact nonnegative stress discriminant identity and equality equations",flush=True)

Ho=s.Matrix([[0,0,0],[0,-s.Rational(1,2),1/(2*s.sqrt(2))],[0,1/(2*s.sqrt(2)),s.Rational(1,2)]])
Ao=s.sqrt(2)*s.Matrix([[0,-1,0],[1,0,0],[0,0,0]])
Cs=s.Rational(5,3)*Ao+s.Rational(4,3)*s.I*Ho
Zs=s.Rational(4,3)*Ao+s.Rational(5,3)*s.I*Ho
same(comm(Cs,comm(Cs,Ho))-comm(Zs,comm(Zs,Ho)),comm(Ao,comm(Ao,Ho)))
same((Cs*Cs-Zs*Zs)*q,-2*q)
same(inner(s.I*Ho,Cs),8*r*r/3)
same(inner(s.I*Ho,Zs),10*r*r/3)
cp=s.symbols("cp",real=True)
same((8*r/3)**2*(s.Rational(16,9)*cp+cp),(10*r/3)**2*s.Rational(16,9)*cp)
print("PASS: exact scalar-compatible saturation witness; not a gauge solution",flush=True)

watchdog.cancel()
print(f"ALL NEW EXACT CHECKS PASSED in {time.monotonic()-started:.3f} seconds.",flush=True)
print("The unrestricted residual zero set remains unresolved; no numeric zero was sought.",flush=True)
