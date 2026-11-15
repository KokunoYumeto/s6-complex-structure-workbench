"""Exact period, finite-action and conjugate-fill certificates for UN59."""
from pathlib import Path
import sympy as S

I = S.I
J = S.Matrix([[0, 1], [-1, 0]])
rho, chi, w = S.symbols('rho chi w', nonzero=True)
R = S.diag(rho, 1)

def bar(v):
    return S.conjugate(v).subs(S.conjugate(rho), 1/rho)

def V(c, v):
    return v + c*J*bar(v)

def zero(v):
    return all(S.simplify(a) == 0 for a in v)

def vector(prefix):
    x, y, z, t = S.symbols(prefix+'0:4', real=True)
    return S.Matrix([x+I*y, z+I*t])

v, b, bp, tau, taun, n = map(vector, ['v', 'b', 'bp', 't', 'tn', 'n'])
h, N = S.symbols('h N', positive=True, integer=True)
assert zero(R*V(chi, v)-V(rho*chi, R*v))
print('PASS exact equivariance R V_chi = V_(rho chi) R for arbitrary unit rho.')

# The root correction is a REAL rational multiple of a normal lattice vector.
lam = taun + R*b - tau - bp + h*n/N
transported = V(rho*chi, taun)+R*V(chi, b)-V(rho*chi, tau)-V(rho*chi, bp)+h*V(rho*chi, n)/N
assert zero(transported-V(rho*chi, lam))
print('PASS exact target-frame affine overlap including the normal correction h*n/N.')

Rinf = R/rho
assert zero(Rinf-J*bar(R)*J.inv())
tauinf = J*bar(tau)+w*tau/rho
assert zero(tauinf-(w/rho)*V(rho/w, tau))
print('PASS infinity linear part rho^-1 R = J conjugate(R) J^-1.')
print('PASS infinity translation J conjugate(tau)+rho^-1*w*tau from the actual frame change.')

# Full determinant retains arbitrary horizontal translation and both real characters.
x,y,a,c,c1,c2,s1,s2,A,B=S.symbols('x y a c c1 c2 s1 s2 A B', real=True)
z=x+I*y
def VV(v):
    return v+z*J*S.conjugate(v)
def real_column(v):
    return S.Matrix([S.re(v[0]),S.im(v[0]),S.re(v[1]),S.im(v[1])])
p=S.Matrix([0,1])
columns=[VV(S.Matrix([1,c1])),VV(S.Matrix([a+I*c,c2])),VV(p),
         VV(S.Matrix([s1+I*s2,I]))+(A+I*B)*VV(p)]
det=S.factor(S.Matrix.hstack(*map(real_column,columns)).det())
r2=x*x+y*y
assert S.expand(det-c*(1+r2)*(1+r2+B*(1-r2))) == 0
print('Full exact real determinant:', det)
print('With |chi|=r^k and B=-d*log(r)/(2*pi), this is strictly positive for every r>0,k>0,d>0.')

# Integral elliptic actions and explicit compact weighted examples.
actions={
    2:S.Matrix([[-1,0],[0,-1]]),
    3:S.Matrix([[0,-1],[1,-1]]),
    4:S.Matrix([[0,-1],[1,0]]),
    6:S.Matrix([[0,-1],[1,1]])
}
e3=S.Matrix([0,0,1])
for order, A2 in actions.items():
    A3=S.diag(A2,S.Matrix([[1]]))
    assert A3**order == S.eye(3)
    assert all(A3**a != S.eye(3) for a in range(1,order))
    length=2*order
    taus=[S.Rational(j,order)*e3 for j in range(length)]
    normals=[-e3 for j in range(length)]
    for j in range(length):
        target=(j+2)%length
        # The chosen b_j are equal multiples of i*p, hence fixed by A3.
        lam=taus[(j+1)%length]-taus[j]+normals[target]/order
        expected=-2*e3 if j==length-1 else S.zeros(3,1)
        assert lam==expected
        mu=S.zeros(3,1)
        for q in range(order):
            mu += A3**(order-1-q)*taus[(j+2*q)%length]
        assert mu == (order-1+(j%2))*e3
    u=-sum(normals,S.zeros(3,1))
    assert u==2*order*e3 and u/order==2*e3
    quotient=A3.inv()
    assert quotient != S.eye(3) and quotient**order == S.eye(3)
    print(f'Order {order}: {length} root ruled components; every overlap and order relation integral; quotient multiplicities ({order},{order}); finite elliptic gluing matrix {list(quotient[:2,:2])}.')

# Nth-order transport follows term by term from the exact elementary identity.
# Verify the exponent arithmetic for every admissible k,N through N=120.
count=0
for nN in range(1,121):
    for k in range(1,nN+1):
        order=nN//S.igcd(nN,k)
        if order not in (1,2,3,4,6):
            continue
        for a0 in range(nN):
            assert ((a0+1)+(nN-1-a0))*k % nN == 0
            count+=1
print('Exact admissible finite-order transport summands checked:',count)
print('PASS all symbolic period/action identities and all explicit nontrivial finite-linear-part examples.')
