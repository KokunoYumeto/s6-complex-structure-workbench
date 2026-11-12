"""Exact, independent check of the moving-sector orbit and its parameter family.

Run: python exact_checker.py
Requires SymPy. Uses no floating-point numbers, external data, or Lean tools.
The original coordinates and constants are retained throughout. CAS reductions
evaluate exact identity residuals; they do not rescale or replace the fields.
"""

import sympy as sp


CHECKS = 0


def reduced(value):
    return sp.simplify(sp.trigsimp(sp.expand(value)))


def check(label, actual, expected=0):
    global CHECKS
    difference = actual - expected
    if isinstance(difference, sp.MatrixBase):
        residual = difference.applyfunc(reduced)
        assert residual == sp.zeros(*residual.shape), (label, residual)
    else:
        residual = reduced(difference)
        assert residual == 0, (label, residual)
    CHECKS += 1
    print(f"PASS {CHECKS:02d}: {label}")


def comm(left, right):
    return left * right - right * left


def tf(matrix):
    return matrix - sp.trace(matrix) * sp.eye(3) / 3


r = sp.Rational
I = sp.eye(3)
u = sp.Matrix([1, 1, 1])
b0 = sp.Matrix([1, -1, 0]) / 4
Phi0 = sp.Matrix([[1, 1, 1], [1, 1, 1], [1, 1, -2]]) / 4
J = sp.Matrix([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
Pi = u * u.T / 3
Q = I - Pi
Omega = sp.sqrt(r(2, 3)) * J
t = sp.symbols("t", real=True)
O = Pi + sp.cos(sp.sqrt(2) * t) * Q + sp.sin(sp.sqrt(2) * t) * J / sp.sqrt(3)

check("u has original squared length 3", (u.T * u)[0], 3)
check("J is skew-symmetric", J.T, -J)
check("J fixes the u-axis infinitesimally", J * u, sp.zeros(3, 1))
check("J squared is exactly -3Q", J * J, -3 * Q)
check("Pi is idempotent", Pi * Pi, Pi)
check("Q is idempotent", Q * Q, Q)
check("Pi Q vanishes", Pi * Q, sp.zeros(3))
check("Pi J vanishes", Pi * J, sp.zeros(3))
check("J Pi vanishes", J * Pi, sp.zeros(3))
check("Q J equals J", Q * J, J)
check("O(0) is the identity", O.subs(t, 0), I)
check("O is orthogonal for every real t", O.T * O, I)
check("O fixes the original u", O * u, u)
check("O prime equals Omega O", O.diff(t), Omega * O)
check("O commutes with Omega", O * Omega, Omega * O)
check("O has the stated period", O.subs(t, t + sp.sqrt(2) * sp.pi), O)

check("Phi0 is real symmetric", Phi0.T, Phi0)
check("Phi0 is trace-free", sp.trace(Phi0))
check("b0 lies in u-perp", (u.T * b0)[0])
check("b0 squared length", (b0.T * b0)[0], r(1, 8))
check("trace Phi0 squared", sp.trace(Phi0 * Phi0), r(3, 4))
s0 = sp.trace(Phi0 * Phi0) + 2 * (b0.T * b0)[0]
check("s0 equals exactly 1", s0, 1)
check("Phi0 b0 vanishes", Phi0 * b0, sp.zeros(3, 1))
check("adjugate at the original Phi0", Phi0.adjugate(),
      sp.Matrix([[-3, 3, 0], [3, -3, 0], [0, 0, 0]]) / 16)
C0 = tf(Phi0.adjugate() - b0 * b0.T)
check("trace-free nonlinear force at t=0", C0,
      sp.Matrix([[-1, 3, 0], [3, -1, 0], [0, 0, 2]]) / 12)
bdot0 = Omega * b0
Phidot0 = comm(Omega, Phi0)
check("original initial b velocity", bdot0,
      sp.sqrt(6) * sp.Matrix([1, 1, -2]) / 12)
check("original initial Phi velocity", Phidot0,
      sp.sqrt(6) * sp.Matrix([[0, 0, -1], [0, 0, 1], [-1, 1, 0]]) / 4)
check("original initial b equation", Omega * Omega * b0,
      -(1 + s0) * b0 - 6 * Phi0 * b0)
check("original initial Phi double commutator", comm(Omega, Phidot0),
      sp.Matrix([[-2, 2, -1], [2, -2, -1], [-1, -1, 4]]) / 2)
check("original initial Phi equation", comm(Omega, Phidot0),
      -(1 + s0) * Phi0 + 6 * C0)

bt = (O * b0).applyfunc(reduced)
Phit = (O * Phi0 * O.T).applyfunc(reduced)
st = sp.trace(Phit * Phit) + 2 * (bt.T * bt)[0]
check("s(t) equals 1 for every real t", st, 1)
check("rho(t) vanishes for every real t", (u.T * bt)[0])
check("Phi(t)b(t) vanishes for every real t", Phit * bt, sp.zeros(3, 1))
check("full time-dependent b equation", bt.diff(t, 2), -2 * bt - 6 * Phit * bt)
check("adjugate covariance for this singular orbit", Phit.adjugate(),
      O * Phi0.adjugate() * O.T)
check("full time-dependent Phi equation", Phit.diff(t, 2),
      -2 * Phit + 6 * tf(Phit.adjugate() - bt * bt.T))
quarter_period = sp.pi / (2 * sp.sqrt(2))
v = J * b0
check("second trajectory direction is Jb0/sqrt(3)", bt.subs(t, quarter_period),
      v / sp.sqrt(3))
check("independent second plane direction", v, sp.Matrix([1, 1, -2]) / 4)
check("plane directions are orthogonal", (b0.T * v)[0])
check("second plane direction has nonzero norm", (v.T * v)[0], r(3, 8))
check("exact fixed-sector obstruction vector", Phi0 * v, sp.Matrix([0, 0, r(3, 8)]))
check("exact nonzero u-component obstruction", (u.T * Phi0 * v)[0], r(3, 8))

e1 = sp.Matrix([1, -1, 0]) / sp.sqrt(2)
e2 = sp.Matrix([1, 1, -2]) / sp.sqrt(6)
e3 = u / sp.sqrt(3)
F = sp.Matrix.hstack(e1, e2, e3)
L = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
check("computational frame is orthonormal", F.T * F, I)
check("computational frame preserves orientation", F.det(), 1)
check("original u is sqrt(3) times the third frame vector", F.T * u,
      sp.Matrix([0, 0, sp.sqrt(3)]))
check("J in the explicit computational frame", F.T * J * F, sp.sqrt(3) * L)
check("concrete b in the explicit frame", F.T * b0,
      sp.Matrix([sp.sqrt(2) / 4, 0, 0]))
check("concrete Phi in the explicit frame", F.T * Phi0 * F,
      sp.Matrix([[0, 0, 0], [0, -r(1, 2), sp.sqrt(2) / 4],
                 [0, sp.sqrt(2) / 4, r(1, 2)]]))

x, d, B, omega, a, Gamma, mass_squared = sp.symbols(
    "x d B omega a Gamma mass_squared", real=True)
kappa = sp.symbols("kappa", real=True, nonzero=True)
S = x**2 + d**2 + B**2
A = sp.Matrix([[0, 0, 0], [0, -x, d], [0, d, x]])
beta = sp.Matrix([B, 0, 0])
K = omega * L
R = sp.Matrix([[sp.cos(omega * t), -sp.sin(omega * t), 0],
               [sp.sin(omega * t), sp.cos(omega * t), 0], [0, 0, 1]])
check("general rotating frame is orthogonal", R.T * R, I)
check("general rotating frame derivative", R.diff(t), K * R)
check("general seed scalar is exactly 2S", sp.trace(A * A) + 2 * (beta.T * beta)[0], 2 * S)
check("general seed annihilates beta", A * beta, sp.zeros(3, 1))
check("general adjugate", A.adjugate(), sp.diag(-x**2 - d**2, 0, 0))
check("general trace-free nonlinear force", tf(A.adjugate() - beta * beta.T),
      S * sp.diag(-2, 1, 1) / 3)
check("general first commutator", comm(K, A),
      sp.Matrix([[0, omega * x, -omega * d], [omega * x, 0, 0], [-omega * d, 0, 0]]))
check("general double commutator", comm(K, comm(K, A)),
      sp.Matrix([[-2 * omega**2 * x, 0, 0],
                 [0, 2 * omega**2 * x, -omega**2 * d], [0, -omega**2 * d, 0]]))
effective_a = mass_squared + 2 * Gamma * S
Phi_residual = comm(K, comm(K, A)) + effective_a * A - kappa * tf(A.adjugate() - beta * beta.T)
b_residual = K * K * beta + effective_a * beta + kappa * A * beta
check("complete general Phi residual before imposing equalities", Phi_residual,
      sp.Matrix([[2 * (kappa * S / 3 - omega**2 * x), 0, 0],
                 [0, 2 * omega**2 * x - effective_a * x - kappa * S / 3,
                  d * (effective_a - omega**2)],
                 [0, d * (effective_a - omega**2), effective_a * x - kappa * S / 3]]))
check("complete general b residual before imposing equalities", b_residual,
      sp.Matrix([B * (effective_a - omega**2), 0, 0]))

constraints = {
    B**2: 3 * a * x / kappa - x**2 - d**2,
    omega**2: a,
    mass_squared: a * (1 - 6 * Gamma * x / kappa),
}


def impose(matrix):
    # The complete residual is polynomial; no division by B, d, or x is used.
    return matrix.applyfunc(lambda entry: sp.expand(entry).subs(constraints, simultaneous=True))


check("general Phi residual under all exact parameter equalities", impose(Phi_residual), sp.zeros(3))
# Dividing this known polynomial by its explicit factor B is exact and is checked.
check("general b residual factorization", b_residual[0], B * (effective_a - omega**2))
check("general b residual coefficient under equalities",
      sp.expand(effective_a - omega**2).subs(constraints, simultaneous=True))
check("general s under the parameter equalities",
      (2 * S).subs(B**2, constraints[B**2]), 6 * a * x / kappa)
check("general original-coordinate seed", F * A * F.T,
      x * sp.Matrix([[1, 1, 4], [1, 1, 4], [4, 4, -2]]) / 6
      + d * sp.Matrix([[2, 2, -1], [2, 2, -1], [-1, -1, -4]]) / (3 * sp.sqrt(2)))
check("general moving-line obstruction in the original u scale", (u.T * F * A * sp.Matrix([0, 1, 0]))[0], sp.sqrt(3) * d)

mu0 = comm(Phi0, Phidot0) + b0 * bdot0.T - bdot0 * b0.T
check("concrete moment is exactly -Omega/2", mu0, -Omega / 2)
check("concrete moment is traceless", sp.trace(mu0))
check("concrete moment squared norm is strictly nonzero", -sp.trace(mu0 * mu0), 1)
Adot = comm(K, A)
betadot = K * beta
mu_family = comm(A, Adot) + beta * betadot.T - betadot * beta.T
check("general moment is exactly -S K", mu_family, -S * K)
check("general moment norm", -sp.trace(mu_family * mu_family), 2 * omega**2 * S**2)
K0 = sp.trace(Phidot0 * Phidot0) / 2 + (bdot0.T * bdot0)[0]
V0 = s0 / 2 + s0**2 / 4 - 6 * (Phi0.det() - (b0.T * Phi0 * b0)[0])
check("concrete scalar kinetic energy", K0, 1)
check("concrete cubic invariant vanishes", Phi0.det() - (b0.T * Phi0 * b0)[0])
check("concrete scalar potential", V0, r(3, 4))
check("concrete scalar energy", K0 + V0, r(7, 4))
K_family = sp.trace(Adot * Adot) / 2 + (betadot.T * betadot)[0]
check("general scalar kinetic energy", K_family, omega**2 * S)
check("general cubic invariant vanishes", A.det() - (beta.T * A * beta)[0])

# Gauge convention: D_t b = dot b + A0 b, D_t Phi = dot Phi + [A0,Phi].
U = O.T
A0_prime = -U.diff(t) * U.T
check("rotating gauge makes b static", U * bt, b0)
check("rotating gauge makes Phi static", U * Phit * U.T, Phi0)
check("rotating gauge connection is +Omega", A0_prime, Omega)
check("rotating gauge retains the same nonzero moment", U * mu0 * U.T, mu0)
check("static-gauge covariant b velocity retains motion", A0_prime * b0, bdot0)
check("static-gauge covariant Phi velocity retains motion", comm(A0_prime, Phi0), Phidot0)

print(f"ALL {CHECKS} EXACT CHECKS PASSED")
print(f"SymPy version: {sp.__version__}")
print("Concrete s=1, mu=-Omega/2, kinetic=1, potential=3/4, energy=7/4.")
print("No floating-point arithmetic, external data, or Lean-family process used.")
