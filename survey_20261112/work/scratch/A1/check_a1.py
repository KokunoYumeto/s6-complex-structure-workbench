# Sanity checks for reader A1 (not a verification of the workbench).
from sympy import Matrix, eye, zeros, symbols, gcd, sqrt, simplify, Rational, I, exp, pi, nsimplify
from sympy.matrices.normalforms import smith_normal_form
from sympy import ZZ
from itertools import combinations

T1 = Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]])
T2 = Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
T0 = (T1*T2).inv()
A1 = T1.inv().T; A2 = T2.inv().T; M0 = T0.inv().T
print("orders:", T1**3==eye(4), T2**4==eye(4), (T0-eye(4))**2==zeros(4,4))
print("A1 A2 M0 = I:", A1*A2*M0==eye(4))
v1 = Matrix([1,2,-4,0]); v2 = Matrix([-1,-3,3,0])
print("A1 v1=v1, A2 v2=v2:", A1*v1==v1, A2*v2==v2)
# finite-filling lattices
e1=Matrix([0,1,-2,0]); f1=Matrix([0,0,-3,1]); e2=Matrix([0,1,-1,0]); f2=Matrix([0,0,-2,1]); d=Matrix([0,0,0,1])
eps=Matrix([1,2,-4,0]); epsp=Matrix([1,3,-3,0])
print("det[eps,delta,e1,f1], det[eps',delta,e2,f2]:", Matrix.hstack(eps,d,e1,f1).det(), Matrix.hstack(epsp,d,e2,f2).det())
print("Smith(A1-I), Smith(A2-I):", smith_normal_form(A1-eye(4),domain=ZZ).diagonal(), smith_normal_form(A2-eye(4),domain=ZZ).diagonal())
# MV matrices
a1 = Matrix([[3,0,0,0],[0,2,1,3],[4,0,0,0],[0,-1,-1,-2]])
a2 = Matrix([[2,1,3,0,0,0],[-4,-2,0,1,0,0],[-2,-2,-4,0,0,0],[3,3,0,-1,0,0]])
print("Smith alpha1:", smith_normal_form(a1,domain=ZZ).diagonal(), " ker:", a1.nullspace())
print("Smith alpha2:", smith_normal_form(a2,domain=ZZ).diagonal(), " Phi*alpha2:", Matrix([[4,2,3,2]])*a2)
# one-shot Delta_1
l0=symbols('l0')
D1 = Matrix([
[1,0,l0,1,0,0,1,0,0],
[0,0,-1,0,0,1,0,0,0],
[0,0,-1,0,0,0,0,0,1],
[-1,0,0,0,0,0,0,0,0],
[0,-1,0,0,0,0,0,0,0],
[0,0,0,-3,0,-1,0,0,0],
[0,0,0,0,-1,0,0,0,0],
[0,0,0,0,0,0,4,0,-1],
[0,0,0,0,0,0,0,-1,0]])
print("det Delta_1:", D1.det().expand())
# collapse matrix kernel vs im(wedge^2 M0 - I)
def wedge2(M):
    idx=list(combinations(range(4),2))
    W=zeros(6,6)
    for a,(i,j) in enumerate(idx):
        for b,(k,l) in enumerate(idx):
            W[a,b]=M[i,k]*M[j,l]-M[i,l]*M[j,k]
    return W
W2=wedge2(M0)-eye(6)
c2=Matrix([[1,0,0,0,0,0],[0,0,-1,0,0,0],[0,-1,-1,1,1,0],[0,0,0,1,0,0]])
print("c2*(wedge2 M0 - I) = 0:", c2*W2==zeros(4,6), " rank im:", W2.rank(), " Smith c2:", smith_normal_form(c2,domain=ZZ).diagonal())
# invariant 2-form eta = u^w + 6 gamma^delta under wedge2(T_j) acting on wedge^2 V (basis gu,gw,gd,uw,ud,wd)
eta=Matrix([0,0,6,1,0,0])
print("eta invariant:", wedge2(T1)*eta==eta, wedge2(T2)*eta==eta)
# H_* = A2 A1
H=A2*A1; N=H-eye(4)
print("H*=A2A1:", H.tolist(), " N^2=0:", N**2==zeros(4,4))
# cusp edge multipliers
mu0,b0,h0=symbols('mu0 b0 h0')
C=Matrix([[6*mu0,h0],[b0-h0,mu0]]); B0=Matrix([[0,1],[-1,0]])
for a,v in [((0,1),(1,0)),((1,0),(0,1)),((1,1),(1,-1))]:
    print("edge",v,"a",a,":",(Matrix([a])*C*B0*Matrix(v))[0].expand())
# Kummer fibre lengths
for Nn in (2,3,4):
    tri=sum(1 for a in range(Nn) for b in range(Nn) for c in range(Nn) if min(a,b,c)==0)
    dbl=sum(1 for a in range(Nn) for b in range(Nn) if min(a,b)==0)
    print("N",Nn,"triple length",tri,"=",3*Nn**2-3*Nn+1,"double length",dbl,"=",2*Nn-1)
# product cover: kappa-free checks
rho=exp(I*pi/3)
print("mu1 first coord:", simplify(6*(2-rho)/3+2*rho-4), " mu2:", simplify(6*(1-I)/2+3*I-3))
# Engel section P=(0, sqrt2 t^2 (t-1)) on y^2=x^3-3t^3(t-1)x+2t^4(t-1)^2 ; nodal multiplier at t=infinity
t=symbols('t')
print("P on curve:", simplify((sqrt(2)*t**2*(t-1))**2-(0-0+2*t**4*(t-1)**2))==0)
u=(sqrt(2)-sqrt(3)*(0-1))/(sqrt(2)+sqrt(3)*(0-1))
print("node multiplier of P at infinity:", nsimplify(simplify(u)), float(u))
