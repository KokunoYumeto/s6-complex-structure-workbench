#!/usr/bin/env python3
"""Portable exact SymPy checks; no network, external files or numerical tolerance.

Run: python exact_hermitian_metric_spectrum_checker.py
The accompanying TeX proves the universal statements, spectral completeness,
and cusp inequalities. This checker verifies generic polynomial identities
and nontrivial exact rational/complex fixtures; it is not a proof assistant.
Every check() call counts as one assertion, including matrix identities.
"""

import sympy as sp

I = sp.I
Q = sp.Rational
checks = []


def clean(value):
    if isinstance(value, sp.MatrixBase):
        return value.applyfunc(lambda z: sp.cancel(sp.expand_complex(z)))
    return sp.cancel(sp.expand_complex(value))


def check(name, left, right):
    delta = clean(left - right)
    zero = sp.zeros(*delta.shape) if isinstance(delta, sp.MatrixBase) else 0
    assert delta == zero, (name, delta)
    checks.append(name)


def truth(name, value):
    assert value is True or value == sp.true, (name, value)
    checks.append(name)


def realify(mat):
    return sp.BlockMatrix([[sp.re(mat), -sp.im(mat)],
                           [sp.im(mat), sp.re(mat)]]).as_explicit()


def block(a, b, c, d):
    return a.row_join(b).col_join(c.row_join(d))


def sym3(prefix):
    a, b, c, d, e, f = sp.symbols(prefix + "0:6", real=True)
    return sp.Matrix([[a, b, c], [b, d, e], [c, e, f]])


def pos(name, mat):
    check(name + ": Hermitian", mat, mat.H)
    for j in range(1, mat.rows + 1):
        truth(name + ": leading minor " + str(j),
              sp.simplify(mat[:j, :j].det()) > 0)


Id = sp.eye(3)
Z = sp.zeros(3)
J = block(Z, -Id, Id, Z)
Jc = Id.row_join(I * Id)
E = sym3("e")
f1, f2, f3 = sp.symbols("f1 f2 f3", real=True)
F = sp.Matrix([[0, f1, f2], [-f1, 0, f3], [-f2, -f3, 0]])
Hgen = E + I * F
U, V = sym3("u"), sym3("v")
anti = block(U, V, V, -U)
Tgen = realify(Hgen) / 2 + anti
check("J square", J * J, -sp.eye(6))
check("J orthogonal", J.T * J, sp.eye(6))
check("generic H Hermitian", Hgen.H, Hgen)
check("realification transpose", realify(Hgen).T, realify(Hgen.H))
check("Hermitian realification commutes with J",
      J * realify(Hgen), realify(Hgen) * J)
check("kernel anticommutes with J", J * anti, -anti * J)
check("full generic observation", Jc * Tgen * Jc.H, Hgen)
check("kernel is unobserved", Jc * anti * Jc.H, sp.zeros(3))
check("J-invariant cometric average",
      (Tgen + J * Tgen * J.T) / 2, realify(Hgen) / 2)
check("commutator detects the entire kernel",
      J * Tgen - Tgen * J, 2 * J * anti)
parameters = sorted(anti.free_symbols, key=str)
truth("twelve kernel parameters", len(parameters) == 12)
truth("commutator has rank twelve in kernel coordinates",
      sp.Matrix(list(J * Tgen - Tgen * J)).jacobian(parameters).rank() == 12)
vectors = sp.symbols("r0:6", real=True)
rv = sp.Matrix(vectors)
cv = rv[:3, :] + I * rv[3:, :]
check("realification quadratic-form convention",
      (rv.T * realify(Hgen) * rv)[0], (cv.H * Hgen * cv)[0])
D = sp.Matrix(3, 3, sp.symbols("d0:9", real=True))
Fother = sp.Matrix(3, 3, sp.symbols("j0:9", real=True))
Dcomplex = D + I * Fother
check("generic realification multiplicative",
      realify(Hgen * Dcomplex), realify(Hgen) * realify(Dcomplex))

# The original lattice maps, with no replacement of S by R.
P = sp.Matrix([[1, -1, 0], [0, 1, -1]])
B0 = sp.Matrix([[0, 1], [-1, 0]])
Ql = B0.inv() * P
S = sp.Matrix([[1, 1], [0, 1], [0, 0]])
u = sp.ones(3, 1)
C = P * P.T
R = P.T * C.inv()
X = R.row_join(u)
L = sp.diag(P, Ql)
Pr = sp.diag(P, P)
Lright = sp.diag(S, S * B0)
check("original C", C, sp.Matrix([[2, -1], [-1, 2]]))
check("original C determinant", C.det(), sp.Integer(3))
check("PS identity", P * S, sp.eye(2))
check("deck map identity", B0 * Ql, P)
check("Q S retains B0 inverse", Ql * S, B0.inv())
check("integral lattice right inverse", L * Lright, sp.eye(4))
truth("right inverse entries integral", all(z.is_Integer for z in Lright))
check("P kills original u", P * u, sp.zeros(2, 1))
check("Q kills original u", Ql * u, sp.zeros(2, 1))
truth("lattice kernel dimension two", 6 - L.rank() == 2)
check("u length retained", (u.T * u)[0], sp.Integer(3))
check("X inverse original factor 1/3",
      X.inv(), P.col_join(u.T / 3))

# A fully symbolic corrected period determinant.
y = sp.symbols("y", positive=True)
d11, d12, d21, d22 = sp.symbols("d11 d12 d21 d22", real=True)
D2 = sp.Matrix([[d11, d12], [d21, d22]])
Ysymbolic = y * Id + S * D2 * Ql
det_formula = y * (y**2 + y * sp.trace(D2 * B0.inv()) + D2.det())
check("all corrected volume coefficients retained",
      Ysymbolic.det(), det_formula)
check("exact volume leading coefficient",
      sp.limit(Ysymbolic.det() / y**3, y, sp.oo), sp.Integer(1))

# Nonzero real and imaginary correction in every entry: exact fixture only.
C2 = sp.Matrix([[Q(1, 5) + I / 7, -Q(2, 9) + I / 11],
                [Q(3, 10) - I / 13, Q(4, 15) + I / 17]])
C3 = S * C2 * Ql
x0, y0 = Q(2, 7), sp.Integer(5)
s0 = x0 + I * y0
Z3, Z2 = s0 * Id + C3, s0 * B0 + C2
A, Y = sp.re(Z3), sp.im(Z3)
N = block(Id, A, Z, Y)
Ni = block(Id, -A * Y.inv(), Z, Y.inv())
N2 = block(sp.eye(2), sp.re(Z2), sp.zeros(2), sp.im(Z2))
Om3, Om2 = Id.row_join(Z3), sp.eye(2).row_join(Z2)
check("corrected complex period map", P * Z3, Z2 * Ql)
check("original C3 annihilates u", C3 * u, sp.zeros(3, 1))
check("original C2 recovered from C3", P * C3 * S * B0, C2)
check("N inverse right", N * Ni, sp.eye(6))
check("N inverse left", Ni * N, sp.eye(6))
check("period factorization", Jc * N, Om3)
check("complex original lattice diagram", P * Om3, Om2 * L)
check("real original lattice diagram", Pr * N, N2 * L)
check("kernel elliptic periods", Z3 * u, s0 * u)
truth("fixture source period orientation positive", Y.det() > 0)
truth("fixture target real period nonsingular", N2.det() != 0)

# Nonreal positive H fixture with a direct positive-factor certificate.
Hfactor = sp.Matrix([[2, 0, 0], [1 + I, 3, 0], [2 - I, 1 + 2*I, 4]])
H = Hfactor * Hfactor.H
h = 2 * H.inv()
T = realify(H) / 2
g = realify(h)
W = Ni * T * Ni.T
gl = N.T * g * N
pos("H fixture", H)
pos("physical compatible cometric", T)
check("physical metric inverse", g * T, sp.eye(6))
check("Hermitian compatibility of physical metric", J.T * g * J, g)
check("metric-cometric lattice inverse", gl * W, sp.eye(6))
check("observation exact factors", Om3 * W * Om3.H, H)
check("Hermitian cometric factor one half", h.inv(), H / 2)
check("volume squared, physical vs lattice",
      gl.det(), Y.det()**2 * g.det())
check("real Hermitian determinant square", g.det(), h.det()**2)
check("compatible complex volume factor eight", h.det(), 8 / H.det())
check("native physical metric", realify(sp.eye(3)), sp.eye(6))
We = Ni * Ni.T
check("native observation H=2I", Om3 * We * Om3.H, 2 * Id)
check("native observation G=2C", P * Om3 * We * Om3.H * P.T, 2 * C)
check("native lattice covariant/cometric inverse",
      N.T * N * We, sp.eye(6))

# Quotient metric, horizontal lift, and spectral intertwining.
G = P * H * P.T
h2 = 2 * G.inv()
T2 = realify(G) / 2
W2 = L * W * L.T
eta = H * P.T * G.inv()
pos("observed G", G)
check("target cometric pushforward", P * h.inv() * P.T, h2.inv())
check("real quotient cometric", Pr * T * Pr.T, T2)
check("original lattice quotient cometric",
      W2, N2.inv() * T2 * N2.inv().T)
check("target observation", Om2 * W2 * Om2.H, G)
check("target lattice metric/cometric inverse",
      (N2.T * realify(h2) * N2) * W2, sp.eye(4))
check("horizontal lift is right inverse", P * eta, sp.eye(2))
check("horizontal lift orthogonal to kernel", eta.H * h * u, sp.zeros(2, 1))
check("horizontal lift isometry", eta.H * h * eta, h2)
horizontal = eta * P
check("horizontal projection idempotent", horizontal * horizontal, horizontal)
check("horizontal projection self-adjoint for h", horizontal.H * h, h * horizontal)
check("vertical projection lands in kernel", P * (Id-horizontal), sp.zeros(2, 3))
check("native quotient metric C inverse", 2 * (2 * C).inv(), C.inv())
check("native horizontal lift original R", 2 * Id * P.T * (2*C).inv(), R)

k = sp.Matrix(sp.symbols("k0:6", real=True))
m, n = k[:3, :], k[3:, :]
pk = m.col_join(Y.inv().T * (n - A.T*m))
check("exact dual covector including correction", Ni.T * k, pk)
check("dual pairing integer-coordinate identity",
      (pk.T * N * rv)[0], (k.T * rv)[0])
check("physical and lattice spectral forms",
      (k.T * W * k)[0], (pk.T * T * pk)[0])
check("native exact spectral expression",
      (k.T * We * k)[0],
      (m.T*m)[0] + ((Y.inv().T*(n-A.T*m)).T *
                    (Y.inv().T*(n-A.T*m)))[0])
ell = sp.Matrix(sp.symbols("ell0:4", real=True))
check("spectral quotient equality including 4pi squared",
      4*sp.pi**2*(ell.T*W2*ell)[0],
      4*sp.pi**2*((L.T*ell).T*W*(L.T*ell))[0])
check("lattice pullback pairing", (ell.T*L*rv)[0], ((L.T*ell).T*rv)[0])
for a in range(6):
    ea = sp.eye(6)[:, a]
    check("marked spectrum recovers diagonal " + str(a),
          4*sp.pi**2*(ea.T*W*ea)[0]/(4*sp.pi**2), W[a, a])
for a in range(6):
    for b in range(a+1, 6):
        ea, eb = sp.eye(6)[:, a], sp.eye(6)[:, b]
        lam_sum = 4*sp.pi**2*((ea+eb).T*W*(ea+eb))[0]
        lam_a = 4*sp.pi**2*(ea.T*W*ea)[0]
        lam_b = 4*sp.pi**2*(eb.T*W*eb)[0]
        check("marked spectrum recovers off-diagonal " + str((a,b)),
              (lam_sum-lam_a-lam_b)/(8*sp.pi**2), W[a,b])

# Differential sign and all 2*pi factors, tested on a full nonconstant character.
xi = sp.Matrix(sp.symbols("xi0:6", real=True))
kfix = sp.Matrix([1, -2, 3, -1, 2, 4])
character = sp.exp(2*sp.pi*I*(kfix.T*xi)[0])
laplacian = -sum(W[a,b]*sp.diff(character, xi[a], xi[b])
                 for a in range(6) for b in range(6))
check("Laplacian character sign and 4pi squared",
      sp.simplify(laplacian/character),
      4*sp.pi**2*(kfix.T*W*kfix)[0])

M3 = block(Id, Id, Z, Id)
M2 = block(sp.eye(2), B0, sp.zeros(2), sp.eye(2))
Nprime = block(Id, A+Id, Z, Y)
Wprime = Nprime.inv()*T*Nprime.inv().T
check("real period monodromy", Nprime, N*M3)
check("original quotient monodromy", L*M3, M2*L)
check("lattice cometric monodromy", Wprime, M3.inv()*W*M3.inv().T)
check("physical dual covector marking equivariance",
      Nprime.inv().T*M3.T*k, Ni.T*k)
check("eigenvalue marking equivariance",
      ((M3.T*k).T*Wprime*(M3.T*k))[0], (k.T*W*k)[0])

# Prescribed G fibre, exact five-parameter Schur form at a nonreal fixture.
z = sp.Matrix([1 + 2*I, Q(1,3)-I])
tau = Q(7,5)
schur = block(G, z, z.H, sp.Matrix([[(z.H*G.inv()*z)[0]+tau]]))
Hlift = X*schur*X.H
check("five-parameter prescribed quotient", P*Hlift*P.T, G)
check("five-parameter exact Schur complement",
      schur[2,2]-(z.H*G.inv()*z)[0], tau)
pos("positive prescribed Hermitian lift", Hlift)
check("prescribed lift quotient metric unchanged",
      P*(2*Hlift.inv()).inv()*P.T, G/2)

# Native corrected cusp limits and original root-lattice constants.
Ycusp = y*Id + sp.im(C3)
check("native corrected source volume polynomial",
      Ycusp.det(),
      y*(y**2+y*sp.trace(sp.im(C2)*B0.inv())+sp.im(C2).det()))
for j in range(3):
    nj = Id[:,j]
    form = (nj.T*Ycusp.inv()*Ycusp.inv().T*nj)[0]
    check("native source pure-dual leading constant " + str(j),
          sp.limit(y**2*4*sp.pi**2*form, y, sp.oo), 4*sp.pi**2)
root = sp.Matrix([1,-1,0])
check("short root zero sum", (u.T*root)[0], sp.Integer(0))
check("short root squared norm two", (root.T*root)[0], sp.Integer(2))
root_form = (root.T*Ycusp.inv()*Ycusp.inv().T*root)[0]
check("native target root leading constant",
      sp.limit(y**2*4*sp.pi**2*root_form, y, sp.oo), 8*sp.pi**2)
a,b = sp.symbols("a b", integer=True)
ab = sp.Matrix([a,b])
check("original root-lattice norm polynomial",
      (ab.T*C*ab)[0], 2*(a*a-a*b+b*b))
m1,m3 = sp.symbols("m1 m3", integer=True)
check("integral zero-sum triple inverse image",
      P.T*sp.Matrix([m1,-m3]), sp.Matrix([m1,-m1-m3,m3]))
eps = sp.symbols("epsilon", real=True)
Teps = sp.diag(1+eps,1,1,1-eps,1,1)
check("non-Hermitian family has fixed observation", Jc*Teps*Jc.H, 2*Id)
check("non-Hermitian family commutator coefficient",
      J*Teps-Teps*J,
      2*eps*J*sp.diag(1,0,0,-1,0,0))
check("non-Hermitian family determinant", Teps.det(), 1-eps**2)

print("PASS:", len(checks), "exact assertions")
print("Generic identities: realification, full anti-J fibre, rank-12 detection,")
print("corrected determinant, metric/cometric maps, marked spectrum polarization.")
print("Exact fixtures: all original periods nonzero; Hermitian positivity,")
print("horizontal lift, lattice quotient, monodromy, characters, cusp constants.")
print("Analytic completeness, uniform inequalities and minima are proved in TeX;")
print("this checker does not claim to mechanically certify those analytic proofs.")
