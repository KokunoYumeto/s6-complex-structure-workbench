"""Portable exact audit of the specified quaternionic observation maps.

Run with Python and SymPy installed:
    python exact_observation_checker.py

No canonical verifier is imported. Quaternion multiplication is implemented
entry by entry using independently defined complex pairs a + b*j.
No floating-point arithmetic, files, network, PDF, or Lean tools are used.
"""

from dataclasses import dataclass

import sympy as sp


COUNT = 0


def exact(expr):
    return sp.simplify(sp.expand_complex(sp.expand(expr)))


def check(label, actual, expected=0):
    global COUNT
    difference = actual - expected
    if isinstance(difference, sp.MatrixBase):
        residual = difference.applyfunc(exact)
        assert residual == sp.zeros(*residual.shape), (label, residual)
    else:
        residual = exact(difference)
        assert residual == 0, (label, residual)
    COUNT += 1
    print(f"PASS {COUNT:02d}: {label}")


def check_true(label, statement):
    global COUNT
    assert statement is True or statement == sp.true, (label, statement)
    COUNT += 1
    print(f"PASS {COUNT:02d}: {label}")


def scalar_mul(left, right):
    """(a+b*j)(c+d*j), retaining ordered factors and conjugations."""
    a, b = left
    c, d = right
    return a * c - b * sp.conjugate(d), a * d + b * sp.conjugate(c)


@dataclass(frozen=True)
class QM:
    a: sp.Matrix
    b: sp.Matrix

    def __post_init__(self):
        assert self.a.shape == self.b.shape

    def __add__(self, other):
        return QM(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return QM(self.a - other.a, self.b - other.b)

    def scale(self, scalar):
        """Only real scalars are used in this checker."""
        return QM(scalar * self.a, scalar * self.b)

    def star(self):
        return QM(self.a.conjugate().T, -self.b.T)

    def __matmul__(self, other):
        rows, inner = self.a.shape
        other_inner, cols = other.a.shape
        assert inner == other_inner
        result_a = sp.zeros(rows, cols)
        result_b = sp.zeros(rows, cols)
        for row in range(rows):
            for col in range(cols):
                for index in range(inner):
                    part_a, part_b = scalar_mul(
                        (self.a[row, index], self.b[row, index]),
                        (other.a[index, col], other.b[index, col]),
                    )
                    result_a[row, col] += part_a
                    result_b[row, col] += part_b
        return QM(result_a, result_b)


def complex_matrix(matrix):
    matrix = sp.Matrix(matrix)
    return QM(matrix, sp.zeros(*matrix.shape))


def scalar_quaternion(a, b=0):
    return QM(sp.Matrix([[a]]), sp.Matrix([[b]]))


def qcheck(label, actual, expected):
    check(label + " [complex part]", actual.a, expected.a)
    check(label + " [j part]", actual.b, expected.b)


def rho_skew(vector):
    c1, c2, c3 = [sp.conjugate(entry) for entry in vector]
    return sp.Matrix([[0, c3, -c2], [-c3, 0, c1], [c2, -c1, 0]])


def theta(matrix, vector):
    return QM(sp.Matrix(matrix), rho_skew(vector))


def project_complex(matrix):
    assert matrix.a.rows == matrix.a.cols
    imaginary_identity = complex_matrix(sp.I * sp.eye(matrix.a.rows))
    return (matrix - imaginary_identity @ matrix @ imaginary_identity).scale(sp.Rational(1, 2))


def representation(matrix):
    """Used only as an additional check, not to implement multiplication."""
    return matrix.a.row_join(matrix.b).col_join(
        (-matrix.b.conjugate()).row_join(matrix.a.conjugate())
    )


one = scalar_quaternion(1)
qi = scalar_quaternion(sp.I)
qj = scalar_quaternion(0, 1)
qk = scalar_quaternion(0, sp.I)
qcheck("i squared equals -1", qi @ qi, one.scale(-1))
qcheck("j squared equals -1", qj @ qj, one.scale(-1))
qcheck("k squared equals -1", qk @ qk, one.scale(-1))
qcheck("i j equals k", qi @ qj, qk)
qcheck("j i equals -k", qj @ qi, qk.scale(-1))
qa, qb, qc, qd, qe, qf = sp.symbols("qa qb qc qd qe qf", complex=True)
q = scalar_quaternion(qa, qb)
r = scalar_quaternion(qc, qd)
s = scalar_quaternion(qe, qf)
qcheck("generic scalar associativity", (q @ r) @ s, q @ (r @ s))
qcheck("generic conjugation reverses order", (q @ r).star(), r.star() @ q.star())
check("faithful representation respects the independently computed product",
      representation(q @ r), representation(q) * representation(r))
qcheck("generic scalar complex projection", project_complex(q), scalar_quaternion(qa))
qcheck("complex projection is idempotent", project_complex(project_complex(q)),
       project_complex(q))

P = sp.Matrix([[1, -1, 0], [0, 1, -1]])
u = sp.Matrix([1, 1, 1])
C = sp.Matrix([[2, -1], [-1, 2]])
Cinv = sp.Matrix([[2, 1], [1, 2]]) / 3
R = sp.Matrix([[2, 1], [-1, 1], [-1, -2]]) / 3
X = R.row_join(u)
Xinv = P.col_join(u.T / 3)
epsilon_skew = sp.Matrix([[0, 1], [-1, 0]])
check("original marking C=PP*", P * P.T, C)
check("retained inverse metric", C * Cinv, sp.eye(2))
check("original right inverse R=P*C^-1", P.T * Cinv, R)
check("P R is I2", P * R, sp.eye(2))
check("P annihilates original u", P * u, sp.zeros(2, 1))
check("u* R vanishes", u.T * R, sp.zeros(1, 2))
check("R P retains the exact nonunitary complement", R * P, sp.eye(3) - u * u.T / 3)
check("X X^-1 is I3", X * Xinv, sp.eye(3))
check("X^-1 X is I3", Xinv * X, sp.eye(3))
check("det X is exactly 1", X.det(), 1)
check("R*R is C^-1", R.T * R, Cinv)
check("X*X retains the block metric", X.T * X, sp.diag(Cinv, sp.Integer(3)))
check("u* u remains 3", (u.T * u)[0], 3)

a11, a22, a33, a12r, a12i, a13r, a13i, a23r, a23i = sp.symbols(
    "a11 a22 a33 a12r a12i a13r a13i a23r a23i", real=True
)
b1r, b1i, b2r, b2i, b3r, b3i = sp.symbols(
    "b1r b1i b2r b2i b3r b3i", real=True
)
A = sp.Matrix([
    [a11, a12r + sp.I * a12i, a13r + sp.I * a13i],
    [a12r - sp.I * a12i, a22, a23r + sp.I * a23i],
    [a13r - sp.I * a13i, a23r - sp.I * a23i, a33],
])
b = sp.Matrix([b1r + sp.I*b1i, b2r + sp.I*b2i, b3r + sp.I*b3i])
H = theta(A, b)
qcheck("generic 15-real-coordinate Theta is Hermitian", H.star(), H)
rho = (u.T * b)[0]
G_compressed = P * A * P.T
compressed = complex_matrix(P) @ H @ complex_matrix(P.T)
qcheck("generic PHP*=G+conjugate(rho) epsilon j", compressed,
       QM(G_compressed, sp.conjugate(rho) * epsilon_skew))
qcheck("generic matrix complex projection extracts G", project_complex(compressed),
       complex_matrix(G_compressed))
i2 = complex_matrix(sp.I * sp.eye(2))
qcheck("i I2 is quaternionically unitary", i2.star() @ i2, complex_matrix(sp.eye(2)))
qcheck("projection is precisely average of the two congruences",
       project_complex(compressed),
       (compressed + i2.star() @ compressed @ i2).scale(sp.Rational(1, 2)))
check("second retained skew identity", Xinv * rho_skew(b) * Xinv.T,
      rho_skew(X.T * b))

parameters = [
    a11, a22, a33, a12r, a12i, a13r, a13i, a23r, a23i,
    b1r, b1i, b2r, b2i, b3r, b3i,
]
observed_components = sp.Matrix([
    G_compressed[0, 0], G_compressed[1, 1],
    sp.re(G_compressed[0, 1]), sp.im(G_compressed[0, 1]),
])
observation_matrix = observed_components.jacobian(parameters)
check("real observation rank is 4", observation_matrix.rank(), 4)
check("full real kernel dimension is 11", len(parameters) - observation_matrix.rank(), 11)

g11, g22, gr, gi, rr, ri, lam = sp.symbols("g11 g22 gr gi rr ri lam", real=True)
G = sp.Matrix([[g11, gr + sp.I*gi], [gr - sp.I*gi, g22]])
rho_given = rr + sp.I*ri
observed_block = QM(G, sp.conjugate(rho_given) * epsilon_skew)
qcheck("prescribed observed block is Hermitian", observed_block.star(), observed_block)
upper = scalar_quaternion(G[0, 1], sp.conjugate(rho_given))
upper_norm = upper @ upper.star()
norm_expected = gr**2 + gi**2 + rr**2 + ri**2
qcheck("quaternionic off-diagonal norm retains both hidden coordinates",
       upper_norm, scalar_quaternion(norm_expected))
det_G = G.det()
moore2 = g11 * g22 - upper_norm.a[0]
check("Moore determinant gives the exact hidden-coordinate bound",
      moore2, det_G - (rr**2 + ri**2))
check("faithful complex determinant is the square of the computed Moore determinant",
      representation(observed_block).det(), moore2**2)

positive_a = sp.symbols("positive_a", positive=True)
block_positive_a = QM(G.subs(g11, positive_a), observed_block.b)
lower = QM(
    sp.Matrix([[1, 0], [sp.conjugate(G[0, 1])/positive_a, 1]]),
    sp.Matrix([[0, 0], [-sp.conjugate(rho_given)/positive_a, 0]]),
)
schur_diagonal = complex_matrix(sp.diag(positive_a, g22 - norm_expected/positive_a))
qcheck("exact Schur congruence for a>0", lower @ schur_diagonal @ lower.star(),
       block_positive_a)
check("Schur complement numerator is precisely the Moore determinant",
      positive_a * (g22 - norm_expected/positive_a),
      moore2.subs(g11, positive_a))
tau = sp.symbols("tau", real=True)
zero_a_block = QM(G.subs(g11, 0), observed_block.b)
zero_a_test_vector = QM(
    sp.Matrix([-tau * G[0, 1], 1]),
    sp.Matrix([-tau * sp.conjugate(rho_given), 0]),
)
zero_a_form = zero_a_test_vector.star() @ zero_a_block @ zero_a_test_vector
qcheck("a=0 exact nonzero-q witness form",
       zero_a_form, scalar_quaternion(g22 - 2*tau*norm_expected))
qcheck("a=0 nonzero-q witness is -1 at tau=(d+1)/(2|q|^2)",
       QM(zero_a_form.a.subs(tau, (g22+1)/(2*norm_expected)),
          zero_a_form.b.subs(tau, (g22+1)/(2*norm_expected))),
       scalar_quaternion(-1))

positive_section = R * G * R.T
qcheck("complex right section is observed exactly",
       project_complex(complex_matrix(P) @ complex_matrix(positive_section) @ complex_matrix(P.T)),
       complex_matrix(G))
t11, t12, t21, t22 = sp.symbols("t11 t12 t21 t22", complex=True)
T = sp.Matrix([[t11, t12], [t21, t22]])
check("positive section preserves the full symbolic Gram factor",
      R * (T * T.conjugate().T) * R.T,
      (R * T) * (R * T).conjugate().T)

A_lift = R * G * R.T + lam * u * u.T
b_lift = rho_given * u / 3
H_lift = theta(A_lift, b_lift)
lift_compressed = complex_matrix(Xinv) @ H_lift @ complex_matrix(Xinv.T)
expected_lift_a = sp.diag(G, lam)
expected_lift_b = sp.zeros(3)
expected_lift_b[:2, :2] = sp.conjugate(rho_given) * epsilon_skew
qcheck("prescribed lift has precisely the asserted marked block",
       lift_compressed, QM(expected_lift_a, expected_lift_b))
check("prescribed lift has chi=R*b=0", R.T * b_lift, sp.zeros(2, 1))
check("prescribed lift retains prescribed rho", (u.T * b_lift)[0], rho_given)
qcheck("prescribed lift retains prescribed observation",
       project_complex(complex_matrix(P) @ H_lift @ complex_matrix(P.T)),
       complex_matrix(G))
qcheck("marked block returns the unchanged original lift",
       complex_matrix(X) @ lift_compressed @ complex_matrix(X.T), H_lift)

trace_correction = sp.trace(Cinv * G)
tracefree_section = R * G * R.T - trace_correction * u * u.T / 3
check("trace coefficient is tr(C^-1 G)", sp.trace(R * G * R.T), trace_correction)
check("trace-free section is actually trace-free", sp.trace(tracefree_section))
check("trace-free section is Hermitian", tracefree_section.conjugate().T, tracefree_section)
check("trace-free section retains its exact u-axis eigenvalue",
      tracefree_section * u, -trace_correction * u)
qcheck("trace-free section retains G exactly",
       project_complex(complex_matrix(P) @ complex_matrix(tracefree_section) @ complex_matrix(P.T)),
       complex_matrix(G))

eps = sp.symbols("eps", positive=True)
G_eps = eps * sp.eye(2)
rho_eps = eps / 2
A_eps = R * G_eps * R.T + eps * u * u.T
b_eps = rho_eps * u / 3
H_eps = theta(A_eps, b_eps)
L_eps = QM(sp.eye(3), sp.Matrix([[0, 0, 0], [-sp.Rational(1, 2), 0, 0], [0, 0, 0]]))
D_eps = complex_matrix(sp.diag(eps, 3*eps/4, eps))
qcheck("epsilon lift has explicit positive diagonal congruence factorization",
       complex_matrix(X) @ L_eps @ D_eps @ L_eps.star() @ complex_matrix(X.T),
       H_eps)
check_true("every epsilon diagonal pivot is positive",
           all(pivot.is_positive for pivot in D_eps.a.diagonal()))
check("epsilon lower factor has invertible faithful representation",
      representation(L_eps).det(), 1)
check_true("epsilon hidden coordinate is nonzero", rho_eps.is_positive)
check("epsilon observed determinant is eps squared", G_eps.det(), eps**2)
check("epsilon hidden-coordinate bound has strict positive excess",
      G_eps.det() - rho_eps**2, 3*eps**2/4)
check("epsilon observed determinant tends to zero",
      sp.limit(G_eps.det(), eps, 0, dir="+"), 0)
qcheck("epsilon observation remains prescribed",
       project_complex(complex_matrix(P) @ H_eps @ complex_matrix(P.T)),
       complex_matrix(G_eps))

shift = sp.symbols("shift", real=True)
qcheck("general scalar shift retains the nonunitary C exactly",
       project_complex(complex_matrix(P) @ (H - complex_matrix(shift*sp.eye(3))) @ complex_matrix(P.T)),
       complex_matrix(P * A * P.T - shift*C))
Phi_example = sp.diag(-2, -1, 3)
Q_example = theta(Phi_example, sp.zeros(3, 1))
minimum = min(Phi_example.eigenvals().keys())
check("diagonal spectral-floor input is trace-free", sp.trace(Phi_example))
check("diagonal least eigenvalue is exactly -2", minimum, -2)
check("faithful representation has the same least spectral value",
      min(representation(Q_example).eigenvals().keys()), minimum)
H_floor = Q_example - complex_matrix(minimum*sp.eye(3))
qcheck("exact spectral-floor matrix", H_floor, complex_matrix(sp.diag(0, 1, 5)))
check_true("spectral-floor matrix is positive semidefinite",
           all(value >= 0 for value in H_floor.a.diagonal()))
check("spectral-floor matrix is on the positive boundary", H_floor.a.det())
G_floor = project_complex(complex_matrix(P) @ H_floor @ complex_matrix(P.T))
qcheck("spectral-floor observation has the retained C correction",
       G_floor, complex_matrix(P * Phi_example * P.T - minimum*C))
qcheck("spectral-floor observed matrix in original marking",
       G_floor, complex_matrix(sp.Matrix([[1, -1], [-1, 6]])))
check("spectral-floor observed determinant is exactly 5", G_floor.a.det(), 5)

print(f"ALL {COUNT} EXACT CHECKS PASSED")
print(f"SymPy version: {sp.__version__}")
print("Scope: symbolic marking, complex-pair quaternion maps, Schur identity,")
print("prescribed lift, trace-free section, exact positive epsilon family,")
print("general real scalar shift, and one diagonal trace-free spectral-floor example.")
print("Not a numerical sampler, global eigenvalue algorithm, or dynamics/physics audit.")
