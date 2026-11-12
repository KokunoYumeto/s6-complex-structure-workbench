"""Portable exact checker. Requires SymPy; no network, subprocesses or Lean.

The reported theorem is restricted to the cross--cross--block class.
This checker does not assert existence or exclusion for arbitrary su(3)^3.
"""
import sympy as s


def comm(A, B):
    return A*B-B*A


def tf(A):
    return A-s.trace(A)*s.eye(3)/3


def same(A, B):
    difference = A-B
    if isinstance(difference, s.MatrixBase):
        entries = list(difference)
    else:
        entries = [difference]
    assert all(s.simplify(s.expand(z)) == 0 for z in entries), difference


def X(v):
    return s.Matrix([[0, -s.conjugate(v[0]), -s.conjugate(v[1])],
                     [v[0], 0, 0], [v[1], 0, 0]])


def total(matrices):
    return sum(matrices, s.zeros(3))


def norm2(Z):
    return -s.trace(Z*Z)


def inner(Z, W):
    return -s.trace(Z*W)


r = s.sqrt(6)/4
H_original = s.Matrix([[0,0,0],[0,-s.Rational(1,2),1/(2*s.sqrt(2))],
                       [0,1/(2*s.sqrt(2)),s.Rational(1,2)]])
q = s.Matrix([1/(2*s.sqrt(2)),0,0])
A = s.sqrt(2)*s.Matrix([[0,-1,0],[1,0,0],[0,0,0]])
qq = q*q.T
F_original = -2*H_original+s.diag(-2,1,1)
same(comm(A,comm(A,H_original)),F_original)
same(6*tf(H_original.adjugate()-qq),s.diag(-2,1,1))
same(A*A*q,-2*q)
same(s.trace(H_original**2)+2*(q.T*q)[0],1)
xx=s.Rational(1,2)
dd=1/(2*s.sqrt(2))
S=s.Matrix([[dd,-(r+xx)],[r+xx,dd]])/s.sqrt(2*r*(r+xx))
U=s.diag(1,S)
H_diagonal=s.diag(0,r,-r)
H_off=s.Matrix([[0,0,0],[0,0,r],[0,r,0]])
same(S.T*S,s.eye(2))
same(S.det(),1)
same(U.T*H_original*U,H_diagonal)
same(U.T*q,q)
same(U*U.T,s.eye(3))
print('PASS: literal H,q,A, couplings and constant diagonalizing coordinate map')

ar,ai,br,bi,cr,ci,dr,di=s.symbols('ar ai br bi cr ci dr di',real=True)
v=s.Matrix([ar+s.I*ai,br+s.I*bi])
w=s.Matrix([cr+s.I*ci,dr+s.I*di])
C=X(v)
Z1=X(w)
Vj=[s.expand(z*s.conjugate(z)) for z in v]
Wj=[s.expand(z*s.conjugate(z)) for z in w]
V=sum(Vj)
W0=sum(Wj)
p=s.expand((s.conjugate(v).T*w)[0])
alpha=s.expand(s.re(p))
beta=s.expand(s.im(p))
betaj=[s.expand(s.im(s.conjugate(v[j])*w[j])) for j in range(2)]
Uv=v*s.conjugate(v).T-w*s.conjugate(w).T
eta,sx,sy,sz=s.symbols('eta sx sy sz',real=True)
B=-eta*s.eye(2)/2+s.Matrix([[sz,sx-s.I*sy],[sx+s.I*sy,-sz]])
D=s.diag(r,-r)
Z2_block=s.I*s.diag(eta,B)
same(comm(B,comm(B,D)),4*r*s.Matrix([
    [sx*sx+sy*sy,-sz*(sx-s.I*sy)],
    [-sz*(sx+s.I*sy),-sx*sx-sy*sy]]))
Rphi=comm(C,comm(C,H_diagonal))-comm(Z1,comm(Z1,H_diagonal))
Rphi-=comm(Z2_block,comm(Z2_block,H_diagonal))
Rphi-=(-2*H_diagonal+s.diag(-2,1,1))
same(Rphi[1:,1:],-Uv*D-D*Uv+comm(B,comm(B,D))-s.eye(2)+2*D)
Rb=(C*C-Z1*Z1-Z2_block*Z2_block)*q+2*q
same(Rb,s.Matrix([(2-V+W0+eta*eta)*q[0],0,0]))
print('PASS: complete scalar block classification without phase restrictions')

gamma,zeta=s.symbols('gamma zeta',nonzero=True)
ee=s.symbols('ee',real=True,nonzero=True)
W=zeta*s.Matrix([[gamma,gamma],[1,-1]])/s.sqrt(2)
Wdag=s.Matrix([[1/gamma,1],[1/gamma,-1]])/(zeta*s.sqrt(2))
Bphase=ee*s.Matrix([[-1,gamma],[1/gamma,-1]])/2
same(Wdag*W,s.eye(2))
same(W*Wdag,s.eye(2))
same(Wdag*Bphase*W,s.diag(0,-ee))
same(Wdag*D*W,r*s.Matrix([[0,1],[1,0]]))
same(s.expand(W.det()).subs(zeta*zeta,-1/gamma),1)
print('PASS: exact complex SU(2) map and inverse in the nonzero-phase branch')

G,omega,d1=s.symbols('G omega d1',real=True)
d2=-eta-d1
Z2=s.I*s.diag(eta,d1,d2)
n=[eta-d1,eta-d2]
Aj=[G/4+n[j]**2+W0 for j in range(2)]
Pj=[3*beta+2*omega*n[j] for j in range(2)]
Bj=[Aj[j]-(omega**2+V+W0) for j in range(2)]
same(-comm(Z1,comm(Z1,C)),X(W0*v+w*(s.conjugate(p)-2*p)))
same(comm(C,Z2),X(s.I*s.diag(*n)*v))


def inertia(H,Z):
    return tf(comm(H,comm(H,Z))+qq*Z+Z*qq)


def K(Z):
    return -comm(Z1,comm(Z1,Z))-comm(Z2,comm(Z2,Z))


for name,HH in [('diagonal',H_diagonal),('off-diagonal',H_off)]:
    same(inertia(HH,C),C/2)
    same(inertia(HH,Z1),Z1/2)
    gauss=G*inertia(HH,C)+2*K(C)-4*omega*comm(Z1,Z2)
    expected_g=s.Matrix([2*(Aj[j]*v[j]-(alpha+s.I*Pj[j])*w[j])
                         for j in range(2)])
    same(gauss,X(expected_g))
    sp1=-omega**2*Z1-2*omega*comm(C,Z2)+comm(C,comm(C,Z1))
    sp1+=K(Z1)+G*inertia(HH,Z1)/2
    expected_s=s.Matrix([Bj[j]*w[j]+(alpha-s.I*Pj[j])*v[j]
                         for j in range(2)])
    same(sp1,X(expected_s))
    sp2=-omega**2*Z2+2*omega*comm(C,Z1)+comm(C,comm(C,Z2))
    sp2+=K(Z2)+G*inertia(HH,Z2)/2
    ll=[s.simplify(inertia(HH,Z2)[j,j]/s.I) for j in range(3)]
    expected=s.zeros(3)
    expected[0,0]=s.I*(-omega**2*eta-2*sum(n[j]*(Vj[j]-Wj[j])
                       for j in range(2))-4*omega*beta+G*ll[0]/2)
    for j,ds in enumerate([d1,d2]):
        expected[j+1,j+1]=s.I*(-omega**2*ds+2*n[j]*(Vj[j]-Wj[j])
                               +4*omega*betaj[j]+G*ll[j+1]/2)
    expected[1,2]=s.I*(n[0]+n[1])*Uv[0,1]+2*omega*(
        -v[0]*s.conjugate(w[1])+w[0]*s.conjugate(v[1]))
    expected[2,1]=-s.conjugate(expected[1,2])
    same(sp2,expected)
    print('PASS: full Gauss and both spatial residuals in '+name+' matter frame')

sigma=s.symbols('sigma',real=True)
same(inertia(H_diagonal,s.I*s.diag(0,sigma,-sigma)),s.zeros(3))
same(inertia(H_off,s.I*s.diag(ee,0,-ee)),
     s.I*ee*s.diag(s.Rational(1,6),s.Rational(2,3),-s.Rational(5,6)))
u11,u22,ur,ui=s.symbols('u11 u22 ur ui',real=True)
uu=s.Matrix([[u11,ur+s.I*ui],[ur-s.I*ui,u22]])
same(-uu*(r*s.Matrix([[0,1],[1,0]]))-(r*s.Matrix([[0,1],[1,0]]))*uu,
     -r*s.Matrix([[2*ur,u11+u22],[u11+u22,2*ur]]))
same(1/(4*r*r),s.Rational(2,3))
rho1,rho2=s.symbols('rho1 rho2',real=True)
wratio=-s.I*s.diag(rho1,rho2)*v
off=s.I*3*ee*(v[0]*s.conjugate(v[1])-wratio[0]*s.conjugate(wratio[1]))
off+=2*omega*(-v[0]*s.conjugate(wratio[1])+wratio[0]*s.conjugate(v[1]))
same(off,s.I*v[0]*s.conjugate(v[1])*(3*ee*(1-rho1*rho2)
                                   -2*omega*(rho1+rho2)))
print('PASS: both scalar branches, exact inertia factors and contradiction ratio')

# Exact noncommuting full-su(3) test, independent of the block restriction.
CC=s.Matrix([[s.I,1+2*s.I,3],[-1+2*s.I,-3*s.I,2-s.I],[-3,-2-s.I,2*s.I]])
ZZ=[s.Matrix([[2*s.I,s.I,1+s.I],[s.I,-s.I,2],[-1+s.I,-2,-s.I]]),
    s.Matrix([[0,2,s.I],[-2,s.I,1-3*s.I],[s.I,-1-3*s.I,-s.I]])]
for M in [CC]+ZZ:
    same(M.conjugate().T+M,s.zeros(3))
    same(s.trace(M),0)
II=lambda M: inertia(H_original,M)
KK=lambda M: -total(comm(Z,comm(Z,M)) for Z in ZZ)
c=inner(CC,II(CC)); z=sum(inner(Z,II(Z)) for Z in ZZ)
k=sum(norm2(comm(CC,Z)) for Z in ZZ)
dd=norm2(comm(ZZ[0],ZZ[1])); z0=sum(norm2(Z) for Z in ZZ)
bb=inner(CC,comm(ZZ[0],ZZ[1]))
RP=comm(CC,comm(CC,H_original))-total(comm(Z,comm(Z,H_original)) for Z in ZZ)-F_original
RV=(CC*CC-total(Z*Z for Z in ZZ))*q+2*q
same(s.trace(H_original*RP)+2*s.re((q.T*RV)[0]),-c+z+2)
RG=G*II(CC)+2*KK(CC)-4*omega*comm(ZZ[0],ZZ[1])
same(inner(CC,RG),G*c+2*k-4*omega*bb)
RS1=-omega**2*ZZ[0]-2*omega*comm(CC,ZZ[1])+comm(CC,comm(CC,ZZ[0]))+KK(ZZ[0])+G*II(ZZ[0])/2
RS2=-omega**2*ZZ[1]+2*omega*comm(CC,ZZ[0])+comm(CC,comm(CC,ZZ[1]))+KK(ZZ[1])+G*II(ZZ[1])/2
same(inner(ZZ[0],RS1)+inner(ZZ[1],RS2),-omega**2*z0+4*omega*bb-k+2*dd+G*z/2)
print('PASS: general pairing identities on one exact full-algebra test triple')
print('ALL EXACT CHECKS PASSED. The unrestricted finite su(3)^3 system remains OPEN.')



# Additional original-coordinate and Gauss-inverse tests; analytic proofs stay in TeX.
uv=s.Matrix([1,1,1]); vv=s.Matrix([1,-1,0]); ww=s.Matrix([1,1,-2])
K_original=s.Matrix.hstack(vv/s.sqrt(2),ww/s.sqrt(6),uv/s.sqrt(3))
Omega_original=s.sqrt(s.Rational(2,3))*s.Matrix([[0,-1,1],[1,0,-1],[-1,1,0]])
Phi_original=s.Matrix([[1,1,1],[1,1,1],[1,1,-2]])/4
b_original=vv/4
same(K_original.T*K_original,s.eye(3)); same(K_original.det(),1)
same(K_original.T*Phi_original*K_original,H_original)
same(K_original.T*b_original,q)
same(K_original.T*Omega_original*K_original,A)
same(K_original*A*K_original.T,Omega_original)
print('PASS: exact original K, Phi0, b0, Omega coordinate maps and inverse')

basis=[]
for j,k in [(0,1),(0,2),(1,2)]:
    E=s.zeros(3); E[j,k]=1; E[k,j]=-1; basis.append(E)
    E=s.zeros(3); E[j,k]=s.I; E[k,j]=s.I; basis.append(E)
basis += [s.I*s.diag(1,-1,0),s.I*s.diag(1,1,-2)]
weights=[inner(E,E) for E in basis]
assert weights==[2,2,2,2,2,2,2,6]
Zp,Zr=ZZ
Gfixed=s.Rational(7,5)
Itest=lambda Z: inertia(H_diagonal,Z)
Ktest=lambda Z: -comm(Zp,comm(Zp,Z))-comm(Zr,comm(Zr,Z))
Ltest=lambda Z: Gfixed*Itest(Z)+2*Ktest(Z)
Lmatrix=s.Matrix([[s.simplify(inner(E,Ltest(F))/weights[j])
                   for F in basis] for j,E in enumerate(basis)])
weighted=s.diag(*weights)*Lmatrix
same(weighted,weighted.T)
assert all(weighted[:j,:j].det()>0 for j in range(1,9))
Bracket=comm(Zp,Zr)
Bcoordinates=s.Matrix([inner(E,Bracket)/weights[j] for j,E in enumerate(basis)])
Tcoords=4*Lmatrix.inv()*Bcoordinates
TT=total(Tcoords[j]*basis[j] for j in range(8))
same(Ltest(TT),4*Bracket)
same(TT.conjugate().T+TT,s.zeros(3)); same(s.trace(TT),0)
vectornorm=lambda v: s.simplify((v.conjugate().T*v)[0])
den=vectornorm(TT*q)
assert den>0
tau=s.simplify((s.Rational(1,4)+vectornorm(Zp*q)+vectornorm(Zr*q))/den)
assert tau>0
Fdiag=-2*H_diagonal+s.diag(-2,1,1)
redH=tau*comm(TT,comm(TT,H_diagonal))-comm(Zp,comm(Zp,H_diagonal))-comm(Zr,comm(Zr,H_diagonal))-Fdiag
redq=(tau*TT*TT-Zp*Zp-Zr*Zr)*q+2*q
red1=tau*(-Zp-2*comm(TT,Zr)+comm(TT,comm(TT,Zp)))+Ktest(Zp)+Gfixed*Itest(Zp)/2
red2=tau*(-Zr+2*comm(TT,Zp)+comm(TT,comm(TT,Zr)))+Ktest(Zr)+Gfixed*Itest(Zr)/2
for sign in [-1,1]:
    om=sign*s.sqrt(tau); CT=om*TT
    same(Ltest(CT),4*om*Bracket)
    same(comm(CT,comm(CT,H_diagonal))-comm(Zp,comm(Zp,H_diagonal))-comm(Zr,comm(Zr,H_diagonal))-Fdiag,redH)
    same((CT*CT-Zp*Zp-Zr*Zr)*q+2*q,redq)
    same(-om**2*Zp-2*om*comm(CT,Zr)+comm(CT,comm(CT,Zp))+Ktest(Zp)+Gfixed*Itest(Zp)/2,red1)
    same(-om**2*Zr+2*om*comm(CT,Zp)+comm(CT,comm(CT,Zr))+Ktest(Zr)+Gfixed*Itest(Zr)/2,red2)
same((q.conjugate().T*redq)[0],0)
assert any(s.simplify(e)!=0 for e in redq)
print('PASS: positive Gauss inverse, original Gram weights, all four residual identities and both frequency signs on exact test data')
print('PASS: scalar contraction vanishes but full vector residual does not; no false solution claimed')
