"""Portable exact checks for period-map metric fibres.

Run: python exact_period_metric_checker.py
Dependency: SymPy. No files, canonical modules, floating-point arithmetic,
network calls, or Lean-family tools are used by this program.
Analytic smoothness and operator-norm inequalities are proved in the TeX
fragment; this checker verifies their exact algebraic ingredients.
"""

import sympy as sp


COUNT = 0


def reduce_exact(expr):
    return sp.cancel(sp.expand(expr))


def check(label, actual, expected=0):
    global COUNT
    residual = actual - expected
    if isinstance(residual, sp.MatrixBase):
        residual = residual.applyfunc(reduce_exact)
        assert residual == sp.zeros(*residual.shape), (label, residual)
    else:
        residual = sp.simplify(reduce_exact(residual))
        assert residual == 0, (label, residual)
    COUNT += 1
    print(f"PASS {COUNT:02d}: {label}")


def truth(label, value):
    global COUNT
    assert value is True or value == sp.true, (label, value)
    COUNT += 1
    print(f"PASS {COUNT:02d}: {label}")


def block(a, b, c, d):
    return a.row_join(b).col_join(c.row_join(d))


def hermitian3(prefix):
    diag = sp.symbols(f"{prefix}1:4", real=True)
    er = sp.symbols(f"{prefix}r1:4", real=True)
    fi = sp.symbols(f"{prefix}i1:4", real=True)
    E = sp.Matrix([[diag[0], er[0], er[1]],
                   [er[0], diag[1], er[2]],
                   [er[1], er[2], diag[2]]])
    F = sp.Matrix([[0, fi[0], fi[1]], [-fi[0], 0, fi[2]], [-fi[1], -fi[2], 0]])
    return E, F, E + sp.I*F


def symmetric3(prefix):
    symbols = sp.symbols(f"{prefix}0:6", real=True)
    return sp.Matrix([[symbols[0], symbols[1], symbols[2]],
                      [symbols[1], symbols[3], symbols[4]],
                      [symbols[2], symbols[4], symbols[5]]])


I3, O3 = sp.eye(3), sp.zeros(3)
P = sp.Matrix([[1, -1, 0], [0, 1, -1]])
u = sp.Matrix([1, 1, 1])
C = P * P.T
R = P.T * C.inv()
X = R.row_join(u)
B0 = sp.Matrix([[0, 1], [-1, 0]])
Qlatt = sp.Matrix([[0, -1, 1], [1, -1, 0]])
S = sp.Matrix([[1, 1], [0, 1], [0, 0]])
check("Q_latt is the original B0^-1 P", Qlatt, B0.inv()*P)
check("P S is I2", P*S, sp.eye(2))
check("Q_latt S is B0^-1", Qlatt*S, B0.inv())
check("retained C is [[2,-1],[-1,2]]", C, sp.Matrix([[2,-1],[-1,2]]))
check("retained determinant C is 3", C.det(), 3)
check("retained C eigenvalue minimum is 1", min(C.eigenvals()), 1)
check("retained C eigenvalue maximum is 3", max(C.eigenvals()), 3)
check("P R is I2", P*R, sp.eye(2))
check("P u is zero", P*u, sp.zeros(2,1))
check("det original marked X is 1", X.det(), 1)

x = sp.symbols("x", real=True)
y = sp.symbols("y", positive=True)
r11,r12,r21,r22,d11,d12,d21,d22 = sp.symbols(
    "r11 r12 r21 r22 d11 d12 d21 d22", real=True)
C2real = sp.Matrix([[r11,r12],[r21,r22]])
D2 = sp.Matrix([[d11,d12],[d21,d22]])
C2 = C2real + sp.I*D2
C3real = S*C2real*Qlatt
C3imag = S*D2*Qlatt
C3 = C3real + sp.I*C3imag
Z3 = (x+sp.I*y)*I3+C3
Z2 = (x+sp.I*y)*B0+C2
Omega3 = I3.row_join(Z3)
Omega2 = sp.eye(2).row_join(Z2)
Phi_latt = sp.diag(P,Qlatt)
check("all retained corrected periods intertwine", P*Z3, Z2*Qlatt)
check("full original period Gram intertwiner", P*Omega3, Omega2*Phi_latt)
check("C3 retains its exact original formula", C3, S*C2*Qlatt)
check("full correction C2 has the exact retained inverse", P*C3*S*B0, C2)
check("retained C3 annihilates original u", C3*u, sp.zeros(3,1))

Ar = x*I3+C3real
Y = y*I3+C3imag
K2 = y*sp.eye(2)+B0.inv()*D2
K2inv = K2.adjugate()/K2.det()
Yinv = (I3-S*D2*K2inv*Qlatt)/y
check("explicit retained-correction Y inverse on its nonsingular domain", Y*Yinv, I3)
check("both orders of Y inverse", Yinv*Y, I3)
detY_formula = y*(y**2+y*sp.trace(D2*B0.inv())+D2.det())
check("det Y retains the entire imaginary C2 correction", Y.det(), detY_formula)
check("expanded retained determinant coefficients", Y.det(),
      y*(y**2+y*(d12-d21)+d11*d22-d12*d21))
N = block(I3,Ar,O3,Y)
Ninv = block(I3,-Ar*Yinv,O3,Yinv)
Jcomplex = I3.row_join(sp.I*I3)
check("real period factorization Omega3=Jcomplex N", Omega3, Jcomplex*N)
check("full real period inverse", N*Ninv, sp.eye(6))
check("opposite order of real period inverse", Ninv*N, sp.eye(6))
check("Omega3 N^-1 retains complex target coordinates", Omega3*Ninv, Jcomplex)

M = block(I3,I3,O3,I3)
Mminus = block(I3,-I3,O3,I3)
check("real period map has exact monodromy", N.subs(x,x+1), N*M)
check("complex period map has exact monodromy", Omega3.subs(x,x+1), Omega3*M)
check("inverse real period monodromy", Ninv.subs(x,x+1), Mminus*Ninv)

E,F,H = hermitian3("h")
Vhalf = block(E,-F,F,E)/2
U,V = symmetric3("u"),symmetric3("v")
kernel = block(U,V,V,-U)
covariance = Vhalf+kernel
check("Hermitian target is unchanged by adjoint", H.conjugate().T, H)
check("canonical real covariance is symmetric", Vhalf.T, Vhalf)
check("canonical real covariance maps to the full H", Jcomplex*Vhalf*Jcomplex.conjugate().T, H)
check("twelve-parameter real symmetric kernel maps exactly to zero",
      Jcomplex*kernel*Jcomplex.conjugate().T, sp.zeros(3))
check("entire affine fibre maps to the same original H",
      Jcomplex*covariance*Jcomplex.conjugate().T, H)
rr = sp.Matrix(sp.symbols("rr0:3",real=True))
ii = sp.Matrix(sp.symbols("ii0:3",real=True))
vcomplex = rr+sp.I*ii
vreal = rr.col_join(ii)
check("realification quadratic form retains complex positivity",
      (vreal.T*(2*Vhalf)*vreal)[0],
      (vcomplex.conjugate().T*H*vcomplex)[0])
change = block(I3,sp.I*I3,I3,-sp.I*I3)
check("realification is conjugate to H and conjugate H",
      change*(2*Vhalf), sp.diag(H,H.conjugate())*change)
check("realification change is invertible", change.det(), 8*sp.I)

wij = sp.symbols("w0:21",real=True)
Wgeneric = sp.zeros(6)
index = 0
for row in range(6):
    for col in range(row,6):
        Wgeneric[row,col] = Wgeneric[col,row] = wij[index]
        index += 1
Hgeneric = sp.expand(Jcomplex*Wgeneric*Jcomplex.conjugate().T)
hcomponents = sp.Matrix([
    Hgeneric[0,0],Hgeneric[1,1],Hgeneric[2,2],
    sp.re(Hgeneric[0,1]),sp.re(Hgeneric[0,2]),sp.re(Hgeneric[1,2]),
    sp.im(Hgeneric[0,1]),sp.im(Hgeneric[0,2]),sp.im(Hgeneric[1,2]),
])
check("real metric-to-H map rank is 9", hcomponents.jacobian(wij).rank(),9)
check("full metric fibre dimension is 12",21-hcomponents.jacobian(wij).rank(),12)
Ggeneric = P*Hgeneric*P.T
gcomponents = sp.Matrix([
    Ggeneric[0,0],Ggeneric[1,1],
    sp.re(Ggeneric[0,1]),sp.im(Ggeneric[0,1]),
])
check("real metric-to-observation map rank is 4",gcomponents.jacobian(wij).rank(),4)
check("observed metric fibre dimension is 17",21-gcomponents.jacobian(wij).rank(),17)

g11,g22,gr,gi,z1r,z1i,z2r,z2i = sp.symbols(
    "g11 g22 gr gi z1r z1i z2r z2i",real=True)
tau = sp.symbols("tau",positive=True)
G = sp.Matrix([[g11,gr+sp.I*gi],[gr-sp.I*gi,g22]])
z = sp.Matrix([z1r+sp.I*z1i,z2r+sp.I*z2i])
Ginv = G.adjugate()/G.det()
excess = (z.conjugate().T*Ginv*z)[0]+tau
Hmarked = block(G,z,z.conjugate().T,sp.Matrix([[excess]]))
Hlift = X*Hmarked*X.T
L = block(sp.eye(2),sp.zeros(2,1),z.conjugate().T*Ginv,sp.ones(1))
check("complete positive observed H fibre has exact Schur factorization",
      L*sp.diag(G,tau)*L.conjugate().T,Hmarked)
check("complete H lift retains observed G",P*Hlift*P.T,G)

Mofx = block(I3,x*I3,O3,I3)
Nrelative = block(I3,C3real,O3,Y)
check("relative real period map retains all C3",N,Nrelative*Mofx)
tildeOmega = I3.row_join(sp.I*y*I3+C3)
check("relative complex period formula",Omega3*Mofx.inv(),tildeOmega)
check("unweighted retained Gram expansion",
      tildeOmega*tildeOmega.conjugate().T,
      I3+y**2*I3+sp.I*y*(C3.conjugate().T-C3)+C3*C3.conjugate().T)
a,bound_b,K = sp.symbols("a bound_b K",positive=True)
ratio_bound = a*(1+(y-K)**2)/(3*bound_b*(1+(y+K)**2))
check("uniform relative-metric ratio lower-bound limit",
      sp.limit(ratio_bound,y,sp.oo),a/(3*bound_b))
dpositive = sp.symbols("dpositive",positive=True)
truth("ratio bound is positive throughout y>K",
      ratio_bound.subs(y,K+dpositive).is_positive)

alpha_obs,beta_obs,lam,p,delta,qchar = sp.symbols(
    "alpha_obs beta_obs lam p delta qchar",positive=True)
Gdelta = sp.diag(alpha_obs,delta)
Hdelta = R*Gdelta*R.T+lam*u*u.T
check("rank-loss lift keeps original observed matrix",P*Hdelta*P.T,Gdelta)
check("rank-loss H determinant retains lambda and alpha",Hdelta.det(),lam*alpha_obs*delta)
check("rank-loss lift original-axis eigenvalue",Hdelta*u,3*lam*u)
check("rank-loss H complete characteristic polynomial",
      (qchar*I3-Hdelta).det(),
      (qchar-3*lam)*(qchar**2-sp.Rational(2,3)*(alpha_obs+delta)*qchar+alpha_obs*delta/3))
hminus = (alpha_obs+delta-sp.sqrt(alpha_obs**2-alpha_obs*delta+delta**2))/3
hplus = (alpha_obs+delta+sp.sqrt(alpha_obs**2-alpha_obs*delta+delta**2))/3
check("small H eigenvalue has exact leading coefficient",
      sp.limit(hminus/delta,delta,0,dir="+"),sp.Rational(1,2))
check("large plane eigenvalue retains alpha_obs",
      sp.limit(hplus,delta,0,dir="+"),2*alpha_obs/3)
check("rank-loss observed determinant is exact",
      Gdelta.det().subs(delta,beta_obs*y**(-p)),alpha_obs*beta_obs*y**(-p))
check("det Y has exact leading coefficient despite retained C2",
      sp.limit(detY_formula/y**3,y,sp.oo),1)
detWscaled = alpha_obs**2*lam**2*beta_obs**2/(64*(detY_formula/y**3)**2)
check("rank-loss metric determinant leading coefficient",
      sp.limit(detWscaled,y,sp.oo),alpha_obs**2*lam**2*beta_obs**2/64)

# An additional full original-coordinate, nonreal, rational exact example.
sample = {
    r11:1,r12:3,r21:-2,r22:4,
    d11:2,d12:-1,d21:sp.Rational(1,2),d22:-3,
    x:sp.Rational(2,5),y:7,
}
Omega_sample = Omega3.subs(sample)
N_sample = N.subs(sample)
Ninv_sample = Ninv.subs(sample)
Tsample = sp.Matrix([[2,0,0],[1+sp.I,3,0],[-sp.I,sp.Rational(1,2),1]])
Hsample = Tsample*Tsample.conjugate().T
Esample,Fsample = sp.re(Hsample),sp.im(Hsample)
Vsample = block(Esample,-Fsample,Fsample,Esample)/2
Wsample = Ninv_sample*Vsample*Ninv_sample.T
check("full nonreal sample reproduces H with original periods",
      Omega_sample*Wsample*Omega_sample.conjugate().T,Hsample)
check("full sample lattice metric is real",sp.im(Wsample),sp.zeros(6))
check("full sample lattice metric is symmetric",Wsample.T,Wsample)
truth("all full sample leading principal minors are strictly positive",
      all(Wsample[:j,:j].det()>0 for j in range(1,7)))
Nnext = N.subs(x,x+1).subs(sample)
Wnext = Nnext.inv()*Vsample*Nnext.inv().T
check("full sample W obeys inverse-congruence monodromy",
      Wnext,Mminus*Wsample*Mminus.T)
check("full sample observed G is unchanged",
      P*Omega_sample*Wsample*Omega_sample.conjugate().T*P.T,P*Hsample*P.T)
check("full sample metric determinant formula",
      Wsample.det(),Hsample.det()**2/(64*Y.subs(sample).det()**2))

print(f"ALL {COUNT} EXACT CHECKS PASSED")
print(f"SymPy version: {sp.__version__}")
print("Scope: retained periods, inverse real period map, full affine fibres,")
print("monodromy, observed H lifts, exact rank-loss algebra and constants,")
print("and a full nonreal rational SPD example. Analytic bounds are proved")
print("in the companion TeX; no physical-selection or global-filling claim.")
