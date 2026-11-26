#!/usr/bin/env python3
"""Post-release exact Poincare coordinate checks; no historical imports."""
from datetime import datetime, timezone
import sympy as s

a,b,c,d=s.symbols('a b c d')
tau,taubar=s.symbols('tau taubar')
x1,x2,y1,y2=s.symbols('x1 x2 y1 y2')
m,n,p,q=s.symbols('m n p q')
r1,r2,s1,s2,kappa=s.symbols('r1 r2 s1 s2 kappa')
scalars=(tau,taubar,x1,x2,y1,y2,m,n,p,q,r1,r2,s1,s2,kappa)
G=s.groebner([a*d-b*c-1],a,b,c,d,
             domain=s.QQ.frac_field(*scalars))
checks=0

def zero(expr):
    global checks
    numerator=s.cancel(expr).as_numer_denom()[0]
    assert G.reduce(s.expand(numerator))[1]==0, s.factor(numerator)
    checks+=1

def matrix_zero(M):
    for entry in M:
        zero(entry)

A=s.Matrix([[a,b],[c,d]])
Ai=s.Matrix([[d,-b],[-c,a]])
J=s.Matrix([[0,1],[-1,0]])
x=s.Matrix([x1,x2])
y=s.Matrix([y1,y2])
z=x1+tau*x2
w=y1+tau*y2
D=d-c*tau
tp=(a*tau-b)/D
xp=A*x
yp=A*y
zp=z/D
wp=w/D

# Literal theta-line gauge under simultaneous lattice translations.
lattice=-(z+m+n*tau)*(y2+q)+(n*w+q*z+n*q*tau)+z*y2
zero(lattice-(n*y1-m*y2-m*q))
print('Lattice gauge: exponent = n*y1-m*y2-m*q; integer -m*q disappears.')

# No division by a, c or d: every identity is reduced modulo det(A)=1.
matrix_zero(Ai*A-s.eye(2))
matrix_zero(A.T*J*A-J)
zero(xp[0]+tp*xp[1]-zp)
zero(yp[0]+tp*yp[1]-wp)
zero(zp*yp[1]-z*y2-c*z*w/D)
tpbar=(a*taubar-b)/(d-c*taubar)
zero(tp-tpbar-(tau-taubar)/(D*(d-c*taubar)))
print('Modular map: tau prime, both Abel coordinates, holomorphic line factor and positive imaginary part.')

Di=a+c*tp
zero(Di-1/D)
zero((d*tp+b)/Di-tau)
zero(zp/Di-z)
zero(wp/Di-w)
zero(c*z*w/D-c*zp*wp/Di)
print('Modular inverse A^-1: tau,z,w restored; exponential factors multiply to one.')

def affine(M,r,t,k):
    F=s.eye(6)
    F[:2,:2]=M
    F[2:4,2:4]=M
    F[:2,5]=r
    F[2:4,5]=t
    F[4,2:4]=r.T*J*M
    F[4,5]=k
    return F

r=s.Matrix([r1,r2])
t=s.Matrix([s1,s2])
ri=-Ai*r
ti=-Ai*t
ki=(r.T*J*t)[0]-kappa
F=affine(A,r,t,kappa)
Fi=affine(Ai,ri,ti,ki)
matrix_zero(Fi*F-s.eye(6))
matrix_zero(F*Fi-s.eye(6))
print('Affine circle inverse: (A^-1,-A^-1 r,-A^-1 s,r^t J s-kappa), both compositions identity.')

theta_shift=(r.T*J*yp)[0]+kappa
raw_exponent=(zp+r1+tp*r2)*(yp[1]+s2)-z*y2-theta_shift
holomorphic=c*z*w/D+r2*wp+s2*zp+r2*s2*tp-kappa
zero(raw_exponent-holomorphic-r1*s2)
print('Full affine holomorphic factor: c*z*w/D+r2*w_A+s2*z_A+r2*s2*tau_prime-kappa.')
print('Its difference from the exact circle gauge is the integer r1*s2.')

# Inverse holomorphic factor, with the corresponding inverse affine data.
znew=zp+r1+tp*r2
wnew=wp+s1+tp*s2
zback_linear=znew/Di
wback_linear=wnew/Di
inverse_holomorphic=(-c*znew*wnew/Di+ri[1]*wback_linear+
                     ti[1]*zback_linear+ri[1]*ti[1]*tau-ki)
zero(holomorphic+inverse_holomorphic+r1*s2+ri[0]*ti[1])
print('Full affine inverse holomorphic factors differ from one only by the displayed integral exponential.')

# Simultaneous elliptic inversion is a literal map of the rigidified line.
zero((-z)*(-y2)-z*y2)
matrix_zero((-s.eye(2)).T*J*(-s.eye(2))-J)
print('Simultaneous elliptic inversion preserves the gauge, symplectic form and zero-axis rigidifications.')
print('Exact scalar identities checked:',checks)
print('Completed',datetime.now(timezone.utc).isoformat())
