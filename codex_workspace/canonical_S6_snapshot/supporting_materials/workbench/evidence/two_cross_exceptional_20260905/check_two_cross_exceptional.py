"""Exact replay of the explicitly restricted two-cross spatial theorem.

One small serial symbolic calculation. No numerical root search, no Lean,
no canonical edits, no file writes, and no asserted unrestricted emptiness.
All v,w components are independent real symbols combined into complex entries.
"""

from time import perf_counter
import sympy as s

started = perf_counter()
checks = 0
I = s.I
R = s.Rational


def bracket(a, b):
    return a * b - b * a


def trace_free(a):
    return a - s.trace(a) * s.eye(3) / 3


def check(label, value):
    global checks
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    for entry in entries:
        assert s.expand(entry) == 0, (label, s.expand(entry))
    checks += 1
    print("PASS:", label)


def cross(v):
    return s.Matrix([[0, -s.conjugate(v[0]), -s.conjugate(v[1])],
                     [v[0], 0, 0], [v[1], 0, 0]])


def inertia(a, h, q):
    p = q * q.conjugate().T
    return trace_free(bracket(h, bracket(h, a)) + p * a + a * p)


q = s.Matrix([1 / (2 * s.sqrt(2)), 0, 0])
r = s.sqrt(6) / 4
hlit = s.Matrix([[0, 0, 0], [0, -R(1, 2), 1 / (2 * s.sqrt(2))],
                [0, 1 / (2 * s.sqrt(2)), R(1, 2)]])
alit = s.sqrt(2) * s.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
check("literal force, retaining the original H and A",
      bracket(alit, bracket(alit, hlit)) + 2 * hlit - s.diag(-2, 1, 1))
check("literal H squared", hlit * hlit - s.diag(0, R(3, 8), R(3, 8)))
check("literal q norm", (q.conjugate().T * q)[0] - R(1, 8))

# Exact first frame: denominator retained, no physical scale divided out.
rr, xx, dd = s.symbols("rr xx dd", real=True)
raw = s.Matrix([[dd, -(rr + xx)], [rr + xx, dd]])
den = 2 * rr * (rr + xx)
hblock = s.Matrix([[-xx, dd], [dd, xx]])
for label, value in [
    ("U-frame column metric", raw.T * raw - den * s.eye(2)),
    ("U-frame ordered eigenvectors", hblock * raw - raw * s.diag(rr, -rr)),
    ("U-frame determinant", raw.det() - den),
]:
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    reduced = [s.rem(s.expand(z), rr**2 - xx**2 - dd**2, rr) for z in entries]
    check(label, s.Matrix(reduced))
check("retained r relation", r**2 - R(1, 2)**2 - (1 / (2 * s.sqrt(2)))**2)

v1r, v1i, v2r, v2i, w1r, w1i, w2r, w2i = s.symbols(
    "v1r v1i v2r v2i w1r w1i w2r w2i", real=True)
v = s.Matrix([v1r + I * v1i, v2r + I * v2i])
w = s.Matrix([w1r + I * w1i, w2r + I * w2i])
vstar, wstar = v.conjugate().T, w.conjugate().T
vnorm = (vstar * v)[0]
wnorm = (wstar * w)[0]
M = v * vstar + w * wstar
N = I * (v * wstar - w * vstar)
p = (vstar * w)[0]
alpha = s.expand((p + s.conjugate(p)) / 2)
b = s.expand((p - s.conjugate(p)) / (2 * I))
Z1, Z2 = cross(v), cross(w)
hd = s.diag(0, r, -r)
check("full cross inertia in the H-diagonal frame", inertia(Z1, hd, q) - Z1 / 2)

# Full scalar residuals before forcing temporal block parameters.
a, h, zr, zi = s.symbols("a h zr zi", real=True)
zz = zr + I * zi
Cgeneral = s.Matrix([[I*a, 0, 0], [0, I*(h-a)/2, zz],
                     [0, -s.conjugate(zz), -I*(a+h)/2]])
fd = -2 * hd + s.diag(-2, 1, 1)
scalar_h = bracket(Cgeneral, bracket(Cgeneral, hd))
scalar_h -= bracket(Z1, bracket(Z1, hd)) + bracket(Z2, bracket(Z2, hd)) + fd
zabs = zr**2 + zi**2
u, vv = M[0, 0], M[1, 1]
expected_h = s.Matrix([
    [2 - 2*r*(u-vv), 0, 0],
    [0, -4*r*zabs+2*r*u-1+2*r, -2*I*r*h*zz],
    [0, 2*I*r*h*s.conjugate(zz), 4*r*zabs-2*r*vv-1-2*r],
])
check("entire H-scalar residual before temporal classification", scalar_h - expected_h)
check("entire q-scalar residual before temporal classification",
      (Cgeneral**2-Z1**2-Z2**2)*q+2*q - (-a*a+vnorm+wnorm+2)*q)

# Exact second frame over the coordinate ring gamma*gammabar=1.
gamma, gammabar, ee = s.symbols("gamma gammabar ee")
W0 = s.Matrix([[gamma, gamma], [1, -1]]) / s.sqrt(2)
W0star = s.Matrix([[gammabar, 1], [gammabar, -1]]) / s.sqrt(2)
B0 = ee * s.Matrix([[-1, gamma], [gammabar, -1]]) / 2


def unit_reduce(expr):
    out = 0
    for (k, ell), coeff in s.Poly(s.expand(expr), gamma, gammabar).terms():
        m = min(k, ell)
        out += coeff * gamma**(k-m) * gammabar**(ell-m)
    return s.expand(out)


for label, value in [
    ("second-frame unitarity on the full unit-circle coordinate ring", W0star*W0-s.eye(2)),
    ("second-frame C spectrum without changing ee", W0star*B0*W0-s.diag(0, -ee)),
    ("second-frame retained H", W0star*s.diag(r, -r)*W0-r*s.Matrix([[0, 1], [1, 0]])),
]:
    check(label, value.applyfunc(unit_reduce))
check("determinant correction zeta squared equals minus gammabar",
      unit_reduce((-gammabar)*W0.det()-1))

# Every literal residual in the classified frame, all v,w coordinates retained.
e, t, omega = s.symbols("e t omega", real=True, nonzero=True)
C = I * e * s.diag(1, 0, -1)
H = s.Matrix([[0, 0, 0], [0, 0, r], [0, r, 0]])
F = -2 * H + s.diag(-2, 1, 1)
Q = s.diag(1, 2)
E = s.diag(R(2, 3), -R(5, 6))


def K(x):
    return -bracket(Z1, bracket(Z1, x)) - bracket(Z2, bracket(Z2, x))


check("full cross inertia after the exact second frame", inertia(Z1, H, q)-Z1/2)
check("full temporal inertia including every coefficient",
      inertia(C, H, q)-I*e*s.diag(R(1, 6), R(2, 3), -R(5, 6)))
ReM12 = s.expand((M[0, 1]+s.conjugate(M[0, 1]))/2)
Sh = bracket(C, bracket(C, H))-bracket(Z1, bracket(Z1, H))-bracket(Z2, bracket(Z2, H))-F
gap = vnorm+wnorm-e*e+2
target_h = s.Matrix([[2-4*r*ReM12, 0, 0],
                     [0, 2*r*ReM12-1, r*gap],
                     [0, r*gap, 2*r*ReM12-1]])
check("entire H-scalar residual after classification", Sh-target_h)
check("entire q-scalar residual after classification", (C**2-Z1**2-Z2**2)*q+2*q-gap*q)

target_bracket = s.zeros(3)
target_bracket[0, 0] = -2*I*b
target_bracket[1:3, 1:3] = I*N
check("entire spatial bracket", bracket(Z1, Z2)-target_bracket)
target_KC = s.zeros(3)
target_KC[0, 0] = 2*I*e*s.trace(Q*M)
target_KC[1:3, 1:3] = -I*e*(Q*M+M*Q)
check("entire K(C)", K(C)-target_KC)
gauss = t*inertia(C, H, q)+2*K(C)-4*omega*bracket(Z1, Z2)
target_gauss = s.zeros(3)
target_gauss[0, 0] = I*(e*t/6+4*e*s.trace(Q*M)+8*omega*b)
target_gauss[1:3, 1:3] = I*(e*t*E-2*e*(Q*M+M*Q)-4*omega*N)
check("entire Gauss residual, not only a contraction", gauss-target_gauss)

D = (t/4-omega**2)*s.eye(2)-e**2*Q**2
s1 = (D+wnorm*s.eye(2))*v+(-alpha*s.eye(2)+I*(2*omega*e*Q-3*b*s.eye(2)))*w
s2 = (D+vnorm*s.eye(2))*w+(-alpha*s.eye(2)-I*(2*omega*e*Q-3*b*s.eye(2)))*v
sp1 = -omega**2*Z1-2*omega*bracket(C, Z2)+bracket(C, bracket(C, Z1))+K(Z1)+t*inertia(Z1, H, q)/2
sp2 = -omega**2*Z2+2*omega*bracket(C, Z1)+bracket(C, bracket(C, Z2))+K(Z2)+t*inertia(Z2, H, q)/2
check("entire first spatial residual", sp1-cross(s1))
check("entire second spatial residual", sp2-cross(s2))
detM = s.expand(M.det())
area = v[0]*w[1]-v[1]*w[0]
check("nonnegative Gram determinant identity", detM-area*s.conjugate(area))
check("full spatial outer-product identity",
      s1*vstar+s2*wstar-(D*M+detM*s.eye(2)+(4*b*s.eye(2)-2*omega*e*Q)*N))

mu1, mu2, det_symbol = s.symbols("mu1 mu2 det_symbol", real=True)
b_gauss = -e*(mu1+2*mu2+t/24)/(2*omega)
N22_gauss = -e*(2*mu2+5*t/24)/omega
chi = 3*e/(2*omega)
B2 = 4*b_gauss-4*omega*e
positive = det_symbol+(e**2/omega**2)*(mu1+2*mu2+t/24+2*omega**2)*(mu2+5*t/12)
check("final exact positivity identity after the off-diagonal equation",
      B2*(chi*mu2+N22_gauss)+det_symbol-positive)

elapsed = perf_counter()-started
assert elapsed < 60, elapsed
print(f"ALL {checks} EXACT CHECK GROUPS PASSED; elapsed={elapsed:.3f}s")
