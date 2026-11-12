import hashlib
import itertools
import json
import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
import sympy as sp
from matplotlib.patches import Rectangle
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


ROOT = pathlib.Path(__file__).resolve().parent
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)
CHECK_DIR = ROOT / "checks"
CHECK_DIR.mkdir(exist_ok=True)
CHECK_RECEIPT = CHECK_DIR / "MATHEMATICAL_CHECKS_V2.json"
DESIGN_RECEIPT = CHECK_DIR / "TOMOGRAPHY_DESIGN_MATRICES.json"

exact_checks = []
numerical_checks = []


def exact(name, condition, evidence):
    if not bool(condition):
        raise AssertionError(name)
    exact_checks.append({"name": name, "status": "passed", "evidence": evidence})


def numerical(name, condition, evidence):
    if not bool(condition):
        raise AssertionError(name)
    numerical_checks.append(
        {"name": name, "status": "passed", "evidence": evidence}
    )


def left_sp(q):
    a, b, c, d = map(sp.sympify, q)
    return sp.Matrix(
        [
            [a, -b, -c, -d],
            [b, a, -d, c],
            [c, d, a, -b],
            [d, -c, b, a],
        ]
    )


def left_np(q):
    a, b, c, d = q
    return np.array(
        [
            [a, -b, -c, -d],
            [b, a, -d, c],
            [c, d, a, -b],
            [d, -c, b, a],
        ],
        dtype=float,
    )


def qbar(q):
    return (q[0], -q[1], -q[2], -q[3])


def qmul(q, r):
    return tuple(left_sp(q) * sp.Matrix(r))


def qnorm2(q):
    return sum(sp.sympify(x) ** 2 for x in q)


def realify_sp(matrix):
    rows = []
    for block_row in matrix:
        converted = [left_sp(q) for q in block_row]
        for local_row in range(4):
            rows.append(
                [
                    converted[j][local_row, local_col]
                    for j in range(len(converted))
                    for local_col in range(4)
                ]
            )
    return sp.Matrix(rows)


def realify_np(matrix):
    return np.block([[left_np(q) for q in row] for row in matrix])


def moore_cubic(H):
    a = H[0][0][0]
    b = H[1][1][0]
    lam = H[2][2][0]
    v = H[0][1]
    q1 = H[0][2]
    q2 = H[1][2]
    cyclic = qmul(qmul(qbar(q1), v), q2)[0]
    return sp.expand(
        a * b * lam
        - lam * qnorm2(v)
        - b * qnorm2(q1)
        - a * qnorm2(q2)
        + 2 * cyclic
    )


# R1: one exact non-diagonal quaternionic matrix and the complete real block.
Hq = [
    [(sp.Integer(10), 0, 0, 0), (1, 1, 0, 0), (0, 1, 1, 0)],
    [(1, -1, 0, 0), (sp.Integer(11), 0, 0, 0), (1, 0, 1, 1)],
    [(0, -1, -1, 0), (1, 0, -1, -1), (sp.Integer(12), 0, 0, 0)],
]
LH = realify_sp(Hq)
NH = moore_cubic(Hq)
leading_minors = [LH[:k, :k].det() for k in range(1, 13)]
exact(
    "R1 exact positivity",
    all(value > 0 for value in leading_minors),
    "all twelve exact leading principal minors of the full real block are positive",
)
exact(
    "R1 Moore determinant identity",
    LH.det() == NH**4,
    f"det(realification) equals N(H)^4 with N(H)={NH}",
)
qa = (2, -1, 3, 1)
qb = (-1, 2, 0, 4)
exact(
    "R1 quaternion representation law",
    left_sp(qmul(qa, qb)) == left_sp(qa) * left_sp(qb)
    and left_sp(qbar(qa)) == left_sp(qa).T,
    "left multiplication and conjugate transpose checked in all four retained coordinates",
)


# R2 and R5: both markings, Schur blocks, and the complete covariance split.
P = sp.Matrix([[1, -1, 0], [0, 1, -1]])
u = sp.ones(3, 1)
C = P * P.T
R = P.T * C.inv()
X = R.row_join(u)
D = X.T * X
I4 = sp.eye(4)
Xr = sp.kronecker_product(X, I4)
Dr = sp.kronecker_product(D, I4)
Rr = sp.kronecker_product(R, I4)
ur = sp.kronecker_product(u, I4)
Breal = Xr.T * LH * Xr
Psireal = Xr.inv() * LH * Xr.T.inv()
exact(
    "R2 marking matrices and Jacobians",
    X.det() == 1
    and X.inv() == P.col_join(u.T / 3)
    and D == sp.diag(C.inv(), 3)
    and D.det() == 1
    and Breal == Dr * Psireal * Dr,
    "exact rational matrices verify X inverse, both determinants, and B=D Psi D",
)
c_scalar = Breal[8, 8]
exact(
    "R2 scalar conditional block",
    Breal[8:12, 8:12] == c_scalar * I4,
    "the last quaternionic diagonal block is exactly c times the four-dimensional identity",
)
ell_real = Breal[8:12, 0:8] / c_scalar
Sreal = (
    Breal[0:8, 0:8]
    - Breal[0:8, 8:12] * Breal[8:12, 0:8] / c_scalar
)
conditional_map = Rr - ur * ell_real
covariance_split = (
    conditional_map * Sreal.inv() * conditional_map.T
    + ur * ur.T / c_scalar
)
exact(
    "R5 full Schur covariance factorization",
    LH.inv() == covariance_split,
    "the observed and conditional terms sum to the entire inverse realification",
)
r_symbol = sp.symbols("r", positive=True)
Hr = P.T * C.inv() * P + (r_symbol / 3) * u * u.T
exact(
    "R2 and R7 witness coordinates",
    X.T * Hr * X == sp.diag(C.inv(), 3 * r_symbol)
    and sp.factor(Hr.det()) == r_symbol,
    "the witness has fixed S=C^{-1}, c=3r, ell=0, and original cubic r",
)


# R3 and R8: exact moments and boundary orders.
m, beta = sp.symbols("m beta", positive=True)
J1 = (m**2 - beta**2) ** sp.Rational(-1, 2)
integer_moment_expressions = {}
for p in range(1, 7):
    value = sp.simplify(
        (-1) ** (p - 1) * sp.diff(J1, m, p - 1) / sp.factorial(p - 1)
    )
    integer_moment_expressions[p] = value
exact(
    "R3 exact mass moment",
    sp.simplify(
        integer_moment_expressions[2]
        - m / (m**2 - beta**2) ** sp.Rational(3, 2)
    )
    == 0,
    "the p=2 derivative is m/(m^2-beta^2)^(3/2)",
)
coefficient_identities = []
p_symbol = sp.symbols("p")
for k in range(6):
    left_coefficient = sp.rf(p_symbol, 2 * k) / (
        4**k * sp.factorial(k) ** 2
    )
    right_coefficient = (
        sp.rf(p_symbol / 2, k)
        * sp.rf((p_symbol + 1) / 2, k)
        / sp.factorial(k) ** 2
    )
    coefficient_identities.append(sp.simplify(left_coefficient - right_coefficient))
exact(
    "R8 hypergeometric coefficients",
    all(value == 0 for value in coefficient_identities),
    "the first six symbolic coefficients satisfy the exact duplication identity used in the proof",
)
exact(
    "R8 zero orders",
    sp.simplify(beta**2 * (1 - (m / beta) ** 2) - (beta**2 - m**2))
    == 0
    and sp.limit(beta * (1 - sp.cos(sp.Symbol("t"))) / sp.Symbol("t") ** 2, sp.Symbol("t"), 0)
    == beta / 2,
    "simple-zero derivative square is beta^2-m^2 and the tangency coefficient is beta/2",
)
example_mass = sp.simplify(
    sp.Integer(6) / (sp.Integer(36) - 20) ** sp.Rational(3, 2)
)
exact(
    "R3 retained numerical example",
    example_mass == sp.Rational(3, 32)
    and sp.Rational(3, 32) / sp.Rational(1, 36) == sp.Rational(27, 8),
    "the full mass factor and mean-substitution ratio are 3/32 and 27/8 before the retained pi^6",
)


# R4: common-space affinity and its second-order Fisher coefficient.
eps = sp.symbols("eps")
h_diag = [sp.Integer(2), sp.Integer(3), sp.Integer(5)]
k_diag = [sp.Integer(1), sp.Integer(-2), sp.Integer(3)]
N_h = sp.prod(h_diag)
N_he = sp.prod(h + eps * k for h, k in zip(h_diag, k_diag))
N_mid = sp.prod(h + eps * k / 2 for h, k in zip(h_diag, k_diag))
affinity_eps = sp.factor(N_h * N_he / N_mid**2)
fisher_value = 2 * sum((k / h) ** 2 for h, k in zip(h_diag, k_diag))
second_coefficient = sp.expand(sp.series(affinity_eps, eps, 0, 3).removeO()).coeff(
    eps, 2
)
exact(
    "R4 local affinity coefficient",
    sp.simplify(second_coefficient + fisher_value / 8) == 0,
    "the exact diagonal specialization has coefficient -I/8 with every factor retained",
)
g_diag = [sp.Integer(7), sp.Integer(11), sp.Integer(13)]
direct_affinity = sp.prod(
    4 * h * g / (h + g) ** 2 for h, g in zip(h_diag, g_diag)
)
moore_affinity = (
    sp.prod(h_diag)
    * sp.prod(g_diag)
    / sp.prod((h + g) / 2 for h, g in zip(h_diag, g_diag)) ** 2
)
exact(
    "R4 evaluated affinity",
    sp.simplify(direct_affinity - moore_affinity) == 0,
    "the product of the three four-real-dimensional Gaussian overlaps equals the Moore-cubic formula",
)


# R6: static divisibility and the separately clocked convolution law.
tau, s, distance, tau_c = sp.symbols(
    "tau s distance tau_c", positive=True
)
exact(
    "R6 static clocks",
    sp.expand((tau + s) ** 2 - tau**2 - s**2) == 2 * tau * s
    and sp.simplify(tau**2 - s**2 - (tau - s) * (tau + s)) == 0,
    "the semigroup defect and CP propagator clock are exact polynomial identities",
)
exact(
    "R6 Brownian clock",
    sp.expand(tau_c * (tau + s) - tau_c * tau - tau_c * s) == 0,
    "linear covariance time gives the exact convolution and channel semigroup exponent",
)


def measurement_row(vector, quaternion_dimension):
    blocks = [sp.Matrix(vector[4 * i : 4 * i + 4]) for i in range(quaternion_dimension)]
    row = [int((block.T * block)[0]) for block in blocks]
    units = [
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
    ]
    for i in range(quaternion_dimension):
        for j in range(i + 1, quaternion_dimension):
            for unit in units:
                row.append(int(2 * (blocks[i].T * left_sp(unit) * blocks[j])[0]))
    return row


def difference(a, b):
    return tuple(x - y for x, y in zip(a, b))


v_points = [
    (0,) * 12,
    (1, 0, 0, 0) + (0,) * 8,
    (0,) * 4 + (1, 0, 0, 0) + (0,) * 4,
    (0,) * 8 + (1, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0),
    (1, 0, 1, 0, 0, -1, 0, 0, 0, 0, 1, 0),
]
v_pairs = list(itertools.combinations(range(6), 2))
M3 = sp.Matrix(
    [
        measurement_row(difference(v_points[a], v_points[b]), 3)
        for a, b in v_pairs
    ]
)
w_points = [
    (0,) * 8,
    (1, 0, 0, 0) + (0,) * 4,
    (0,) * 4 + (1, 0, 0, 0),
    (0, -1, 0, 0, 0, 0, -1, 0),
]
w_pairs = list(itertools.combinations(range(4), 2))
M2 = sp.Matrix(
    [
        measurement_row(difference(w_points[a], w_points[b]), 2)
        for a, b in w_pairs
    ]
)
smith3 = smith_normal_form(M3, domain=ZZ)
smith2 = smith_normal_form(M2, domain=ZZ)
smith3_diag = [int(smith3[i, i]) for i in range(15)]
smith2_diag = [int(smith2[i, i]) for i in range(6)]
exact(
    "R7 full minimal design",
    M3.det() == -4096
    and M3.rank() == 15
    and sorted(abs(x) for x in smith3_diag) == [1, 1, 1] + [2] * 12,
    "the exact 15 by 15 matrix has determinant -2^12 and Smith factors 1,1,1 followed by twelve factors 2",
)
exact(
    "R7 observed minimal design",
    M2.det() == -16
    and M2.rank() == 6
    and sorted(abs(x) for x in smith2_diag) == [1, 1] + [2] * 4,
    "the exact 6 by 6 matrix has determinant -2^4 and the required six-dimensional rank",
)
theta3 = sp.Matrix(
    [
        Hq[0][0][0],
        Hq[1][1][0],
        Hq[2][2][0],
        *Hq[0][1],
        *Hq[0][2],
        *Hq[1][2],
    ]
)
full_data = M3 * theta3 / 2
exact(
    "R7 non-diagonal exact reconstruction",
    2 * M3.inv() * full_data == theta3,
    "all fifteen parameters of a positive non-diagonal quaternionic Hermitian matrix are recovered",
)
theta2 = sp.Matrix([7, 9, 1, -2, 3, 1])
observed_data = M2 * theta2 / 2
exact(
    "R7 observed exact reconstruction",
    2 * M2.inv() * observed_data == theta2,
    "both diagonal and all four quaternionic off-diagonal components are recovered",
)
exact(
    "R7 dimension lower bounds",
    3 + 4 * 3 == 15
    and 2 + 4 == 6
    and sp.binomial(5, 2) < 15 <= sp.binomial(6, 2)
    and sp.binomial(3, 2) < 6 <= sp.binomial(4, 2),
    "Herm_3(H) and Herm_2(H) have dimensions 15 and 6, forcing six and four levels for pair data",
)


# Numerical evidence is grouped separately and is never used as a proof substitute.
rng = np.random.default_rng(20260930)
max_cubic_relative_error = 0.0
for _ in range(10):
    sample = np.zeros((3, 3, 4), dtype=float)
    for i in range(3):
        sample[i, i, 0] = 10 + i
        for j in range(i + 1, 3):
            sample[i, j] = rng.normal(size=4) / 4
            sample[j, i] = np.array(qbar(tuple(sample[i, j])), dtype=float)
    real_sample = realify_np(sample)
    cubic_sample = float(
        sample[0, 0, 0] * sample[1, 1, 0] * sample[2, 2, 0]
        - sample[2, 2, 0] * np.dot(sample[0, 1], sample[0, 1])
        - sample[1, 1, 0] * np.dot(sample[0, 2], sample[0, 2])
        - sample[0, 0, 0] * np.dot(sample[1, 2], sample[1, 2])
        + 2
        * (
            left_np(qbar(tuple(sample[0, 2])))
            @ left_np(tuple(sample[0, 1]))
            @ sample[1, 2]
        )[0]
    )
    max_cubic_relative_error = max(
        max_cubic_relative_error,
        abs(np.linalg.det(real_sample) ** 0.25 / cubic_sample - 1),
    )
numerical(
    "R1 realification stress sample",
    max_cubic_relative_error < 2e-12,
    f"ten deterministic non-diagonal samples; maximum relative error {max_cubic_relative_error:.3e}",
)

angles = np.linspace(0, 2 * np.pi, 262144, endpoint=False)
mass_quadrature = np.mean(np.pi**6 / (6 - 2 * np.sqrt(5) * np.cos(angles)) ** 2)
numerical(
    "R3 independent circle quadrature",
    abs(mass_quadrature / (3 * np.pi**6 / 32) - 1) < 2e-13,
    "262,144-point periodic quadrature includes the complete pi^6 factor",
)
mp.mp.dps = 50
p_value = mp.mpf("0.75")
m_value = mp.mpf("2.0")
beta_value = mp.mpf("1.0")
quadrature_p = mp.quad(
    lambda t: (m_value - beta_value * mp.cos(t)) ** (-p_value),
    [0, 2 * mp.pi],
) / (2 * mp.pi)
hypergeom_p = m_value ** (-p_value) * mp.hyp2f1(
    p_value / 2,
    (p_value + 1) / 2,
    1,
    (beta_value / m_value) ** 2,
)
numerical(
    "R8 noninteger moment quadrature",
    abs(quadrature_p - hypergeom_p) < mp.mpf("1e-45"),
    "50-digit quadrature agrees with the retained hypergeometric expression for p=3/4, m=2, beta=1",
)

LH_np = np.array(LH, dtype=float)
Sigma_np = 0.5 * np.linalg.inv(LH_np)
couplings = rng.integers(-2, 3, size=(6, 12)).astype(float)
coupling_differences = couplings[:, None, :] - couplings[None, :, :]
quadratic_distances = np.einsum(
    "abi,ij,abj->ab", coupling_differences, np.linalg.inv(LH_np), coupling_differences
)
static_kernel = np.exp(-(0.7**2) * quadratic_distances / 4)
numerical(
    "R5 complete-positive coherence kernel",
    np.linalg.eigvalsh(static_kernel)[0] > -2e-12,
    "a deterministic non-diagonal six-level Gram kernel is positive semidefinite",
)
tau_num = 0.7
s_num = 0.4
static_later = np.exp(-(tau_num**2) * quadratic_distances / 4)
static_earlier = np.exp(-(s_num**2) * quadratic_distances / 4)
static_propagator = np.exp(
    -((tau_num**2 - s_num**2) * quadratic_distances / 4)
)
brownian_composed = np.exp(-3 * tau_num * quadratic_distances / 4) * np.exp(
    -3 * s_num * quadratic_distances / 4
)
brownian_total = np.exp(-3 * (tau_num + s_num) * quadratic_distances / 4)
numerical(
    "R6 finite channel clocks",
    np.allclose(static_propagator * static_earlier, static_later)
    and np.allclose(brownian_composed, brownian_total),
    "static CP propagation and Brownian homogeneous composition agree entry by entry",
)


def save_all(fig, stem):
    paths = []
    for extension in ["png", "svg", "pdf"]:
        path = FIG / f"{stem}.{extension}"
        fig.savefig(path, dpi=200, bbox_inches="tight")
        paths.append(path)
    return paths


plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
    }
)
generated_figures = []

fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
m_grid = np.linspace(2 * np.sqrt(5) + 0.05, 12, 700)
axes[0].plot(
    m_grid,
    np.pi**6 * m_grid / (m_grid * m_grid - 20) ** 1.5,
    label=r"Exact average $\pi^6m/(m^2-20)^{3/2}$",
    lw=2.4,
)
axes[0].plot(
    m_grid,
    np.pi**6 / m_grid**2,
    label=r"Mean substitution $\pi^6/m^2$",
    lw=2,
    ls="--",
)
axes[0].axvspan(0, 2 * np.sqrt(5), color="#f0c3bd", alpha=0.45)
axes[0].axvline(2 * np.sqrt(5), color="#98443a", lw=1.4)
axes[0].set_yscale("log")
axes[0].set_xlim(0, 12)
axes[0].set_ylim(6, 5000)
axes[0].set_xlabel(r"Original $m=\lambda(59/4)-20$")
axes[0].set_ylabel(r"Gaussian mass with the full $\pi^6$ factor")
axes[0].set_title("R3: positive fibres and finite mass")
axes[0].text(0.3, 800, "Positive part exists;\n$p=2$ average diverges", fontsize=10)
axes[0].scatter([6], [3 * np.pi**6 / 32], c="#174d70", zorder=4)
axes[0].annotate(
    r"$m=6:\ 3\pi^6/32$",
    (6, 3 * np.pi**6 / 32),
    (7, 180),
    arrowprops={"arrowstyle": "->"},
    fontsize=10,
)
axes[0].legend(loc="lower left", fontsize=8)
t_grid = np.linspace(0, 8, 500)
axes[1].plot(t_grid, np.exp(-(t_grid**2) / 8), label=r"Static $\tau x$: $e^{-\tau^2/8}$", lw=2.4)
axes[1].plot(
    t_grid,
    np.exp(-3 * t_grid / 8),
    label=r"Integrated $Y_\tau$, $\tau_c=3$: $e^{-3\tau/8}$",
    lw=2,
    ls="--",
)
axes[1].set_xlabel(r"Time $\tau$")
axes[1].set_ylabel("Coherence magnitude")
axes[1].set_title(r"R5–R6: $H=\operatorname{diag}(2,3,5)$")
axes[1].text(3.0, 0.83, r"$b_0=0,\ b_1=e_1,\ E_0=E_1$", fontsize=10)
axes[1].legend(fontsize=9)
fig.tight_layout()
generated_figures.extend(save_all(fig, "mass_and_time_laws"))
plt.close(fig)

fig, ax = plt.subplots(figsize=(12, 6))
ax.axis("off")
boxes = [
    (0.01, 0.68, 0.27, 0.22, r"Original parameter $H>0$" + "\n" + r"$N(H),\ Z(H)=\pi^6/N(H)^2$"),
    (0.39, 0.68, 0.27, 0.22, r"Jordan marking $\Psi$" + "\n" + r"$\Psi=X^{-1}HX^{-*}$"),
    (0.75, 0.68, 0.24, 0.22, r"Sample precision $B$" + "\n" + r"$B=X^*HX=D\Psi D$"),
    (0.01, 0.28, 0.27, 0.22, r"Original sample $q\in\mathbb{H}^3$" + "\n" + r"$d^{12}q;\ \xi=X^*q$"),
    (0.39, 0.28, 0.27, 0.22, r"Observation $y=Pq\in\mathbb{H}^2$" + "\n" + r"Affine sample fibre: real dimension 4"),
    (0.75, 0.28, 0.24, 0.22, r"Parameters $(S,c,\ell)$" + "\n" + r"$H\mapsto S$: real dimension 9 fibres"),
]
for x0, y0, width, height, label in boxes:
    ax.add_patch(
        Rectangle(
            (x0, y0),
            width,
            height,
            fc="#edf3f7",
            ec="#274b67",
            lw=1.4,
            transform=ax.transAxes,
        )
    )
    ax.text(
        x0 + width / 2,
        y0 + height / 2,
        label,
        ha="center",
        va="center",
        fontsize=11,
        transform=ax.transAxes,
    )
for start, end in [
    ((0.28, 0.79), (0.39, 0.79)),
    ((0.66, 0.79), (0.75, 0.79)),
    ((0.28, 0.39), (0.39, 0.39)),
    ((0.87, 0.68), (0.87, 0.50)),
]:
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        xycoords="axes fraction",
        arrowprops={"arrowstyle": "->", "lw": 1.7},
    )
ax.text(0.33, 0.84, "R2", ha="center", transform=ax.transAxes)
ax.text(0.705, 0.84, r"$D=X^*X$", ha="center", fontsize=10, transform=ax.transAxes)
ax.text(
    0.50,
    0.12,
    "Fixed $c$ and $\\ell$, varying $S$: six-dimensional relative-entropy data-processing equality family.\n"
    "Fixed $S$, varying $c$ and $\\ell$: nine-dimensional parameter fibre.\n"
    "The residual metric-map fibre is a separate four-circle object (R3).",
    ha="center",
    fontsize=12,
    transform=ax.transAxes,
)
fig.tight_layout()
generated_figures.extend(save_all(fig, "exact_maps"))
plt.close(fig)

fig, ax = plt.subplots(figsize=(11.5, 6.2))
ax.set_xlim(-1.5, 2.0)
ax.set_ylim(0, 2.0)
ax.add_patch(Rectangle((-1.5, 0), 0.5, 2, color="#d9dde2"))
ax.add_patch(Rectangle((-1, 0), 2, 1, color="#c8e6c9"))
ax.add_patch(Rectangle((-1, 1), 2, 1, color="#f4b7b2"))
ax.add_patch(Rectangle((1, 0), 1, 2, color="#c8e6c9"))
ax.axvline(-1, color="#39424e", lw=1.4)
ax.axvline(1, color="#7b2d26", lw=2.2)
ax.axhline(1, xmin=0.143, xmax=0.714, color="#7b2d26", ls="--", lw=1.3)
ax.plot([1, 1], [0, 0.5], color="#1f6b3a", lw=7, solid_capstyle="butt")
ax.plot([1, 1], [0.5, 2], color="#9b322a", lw=7, solid_capstyle="butt")
ax.axhline(0.5, color="#7b2d26", ls=":", lw=1.1)
ax.text(-1.25, 1.05, "No strictly\npositive point", ha="center", va="center")
ax.text(0, 0.48, r"Finite: $0<p<1$", ha="center", va="center", fontsize=12)
ax.text(0, 1.48, r"Divergent: $p\geq1$", ha="center", va="center", fontsize=12)
ax.text(1.5, 1.02, "Finite for every\n$p>0$", ha="center", va="center", fontsize=12)
ax.annotate(
    r"Tangency $m=\beta$: finite iff $p<1/2$",
    xy=(1, 0.46),
    xytext=(0.12, 0.17),
    arrowprops={"arrowstyle": "->"},
    fontsize=10,
)
ax.set_xlabel(r"Exact ratio $m/\beta$")
ax.set_ylabel(r"Exponent $p$ in $N^{-p}$")
ax.set_title("R8: sharp residual-fibre integrability thresholds")
ax.set_xticks([-1, 0, 1, 2])
ax.set_yticks([0, 0.5, 1, 1.5, 2])
fig.tight_layout()
generated_figures.extend(save_all(fig, "residual_integrability_map"))
plt.close(fig)

fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))
for ax, count, prefix, title, subtitle in [
    (
        axes[0],
        6,
        "v",
        "Full quaternionic precision",
        r"$K_6$: 15 edges = 15 parameters, $\det M_3=-2^{12}$",
    ),
    (
        axes[1],
        4,
        "w",
        "Observation-only precision",
        r"$K_4$: 6 edges = 6 parameters, $\det M_2=-2^4$",
    ),
]:
    theta_grid = np.linspace(np.pi / 2, np.pi / 2 + 2 * np.pi, count, endpoint=False)
    positions = np.column_stack([np.cos(theta_grid), np.sin(theta_grid)])
    for i, j in itertools.combinations(range(count), 2):
        ax.plot(
            [positions[i, 0], positions[j, 0]],
            [positions[i, 1], positions[j, 1]],
            color="#8aa1b2",
            lw=1.1,
            zorder=1,
        )
    ax.scatter(positions[:, 0], positions[:, 1], s=520, c="#e8f0f5", edgecolors="#274b67", lw=1.5, zorder=2)
    for i, (x0, y0) in enumerate(positions):
        ax.text(x0, y0, rf"${prefix}_{i}$", ha="center", va="center", fontsize=12, zorder=3)
    ax.text(0, -1.45, subtitle, ha="center", fontsize=10)
    ax.set_title(title, fontsize=13)
    ax.set_aspect("equal")
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.62, 1.28)
    ax.axis("off")
fig.suptitle("R7: every edge supplies one pair-coherence magnitude", fontsize=14)
fig.tight_layout()
generated_figures.extend(save_all(fig, "tomography_designs"))
plt.close(fig)

design_receipt = {
    "coordinate_order": [
        "diagonal entries",
        "off-diagonal quaternion components in 1,i,j,k order",
    ],
    "full_design": {
        "points": [list(point) for point in v_points],
        "pair_order": [list(pair) for pair in v_pairs],
        "matrix": [[int(value) for value in row] for row in M3.tolist()],
        "determinant": int(M3.det()),
        "smith_diagonal": smith3_diag,
    },
    "observed_design": {
        "points": [list(point) for point in w_points],
        "pair_order": [list(pair) for pair in w_pairs],
        "matrix": [[int(value) for value in row] for row in M2.tolist()],
        "determinant": int(M2.det()),
        "smith_diagonal": smith2_diag,
    },
}
DESIGN_RECEIPT.write_text(
    json.dumps(design_receipt, indent=2) + "\n", encoding="utf-8"
)

figure_records = [
    {
        "file": str(path.relative_to(ROOT)),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }
    for path in sorted(generated_figures)
]
receipt = {
    "edition": "V2 independent quality audit",
    "proof_scope": "checks are reproducibility evidence; complete arguments remain in MATHEMATICAL_NOTE.md and TOMOGRAPHY_DESIGN.md",
    "exact_checks": exact_checks,
    "numerical_checks": numerical_checks,
    "exact_check_groups_passed": len(exact_checks),
    "numerical_evidence_groups_passed": len(numerical_checks),
    "maximum_relative_cubic_stress_error": max_cubic_relative_error,
    "integer_residual_moments_p_1_through_6": {
        str(p): str(value) for p, value in integer_moment_expressions.items()
    },
    "tomography_design_receipt": DESIGN_RECEIPT.name,
    "figures": figure_records,
    "supersedes": "MATHEMATICAL_CHECKS.json",
}
CHECK_RECEIPT.write_text(
    json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(
    json.dumps(
        {
            "exact_groups": len(exact_checks),
            "numerical_groups": len(numerical_checks),
            "figures": len(figure_records),
            "M3_determinant": int(M3.det()),
            "M2_determinant": int(M2.det()),
            "maximum_relative_cubic_stress_error": max_cubic_relative_error,
        }
    )
)
