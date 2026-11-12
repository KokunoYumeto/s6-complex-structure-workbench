"""Exact finite diagnostics for the original-angle native localization proof.

These checks test original noncommutative face words, finite open-box
combinatorics, generator/Haar constants, and algebraic coefficients.  They do
not certify the analytic moment, spectral, or simultaneous-limit theorems;
those arguments are written in the retained sources.
"""
from pathlib import Path
from itertools import combinations, product
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parent
checks = []


def eq(name, left, right=0):
    residual = s.simplify(left - right)
    if isinstance(residual, s.MatrixBase):
        assert residual == s.zeros(*residual.shape), (name, residual)
    else:
        assert residual == 0, (name, residual)
    checks.append({"name": name, "residual": str(residual)})


def exact_bool(name, condition, **data):
    assert condition, (name, data)
    checks.append({"name": name, "passed": True, **data})


def word(*terms):
    """Reduced free-group word: exact only by adjacent inverse cancellation."""
    out = []
    for term in terms:
        for letter in term:
            if out and out[-1] == (letter[0], -letter[1]):
                out.pop()
            else:
                out.append(letter)
    return tuple(out)


def inv(term):
    return tuple((name, -sign) for name, sign in reversed(term))


A, B, C, D, h = [((name, 1),) for name in ("A", "B", "C", "D", "h")]
original_face = word(A, B, inv(C), inv(D))
top_translated_face = word(A, B, inv(word(inv(h), C)), inv(D))
top_claim = word(original_face, D, h, inv(D))
bottom_translated_face = word(inv(h), A, B, inv(C), inv(D))
exact_bool(
    "N5 upper-edge translated original face word",
    top_translated_face == top_claim,
    reduced_word=top_translated_face,
)
exact_bool(
    "N6 lower-edge translated original face word",
    bottom_translated_face == word(inv(h), original_face),
    reduced_word=bottom_translated_face,
)

identity = s.eye(2)
pauli = [
    s.Matrix([[0, 1], [1, 0]]),
    s.Matrix([[0, -s.I], [s.I, 0]]),
    s.diag(1, -1),
]


def quaternion(q):
    return q[0] * identity + s.I * sum(
        (q[k + 1] * pauli[k] for k in range(3)), s.zeros(2)
    )


u0, u1, u2, u3, c, r1, r2, r3 = s.symbols(
    "u0 u1 u2 u3 c r1 r2 r3", real=True
)
u = [u0, u1, u2, u3]
r = [r1, r2, r3]
U = quaternion(u)
R = quaternion([c, *r])
eq("Pauli product fixes original generator metric", sum(
    ((-s.I * p / 2) ** 2 for p in pauli), s.zeros(2)
), -s.Rational(3, 4) * identity)
eq("unit-quaternion determinant", U.det(), sum(v**2 for v in u))
eq("unit-quaternion inverse numerator", U * U.conjugate().T,
   sum(v**2 for v in u) * identity)
eq("Pauli trace of translated pair", s.trace(U) + s.trace(U * R),
   2 * ((1 + c) * u0 - u1 * r1 - u2 * r2 - u3 * r3))
eq("sharp trace coefficient norm on unit sphere",
   (1 + c)**2 + (1 - c**2), 2 + 2*c)
alpha = s.symbols("alpha", real=True)
eq("half-angle sharp trace constant squared",
   2 + 2*s.cos(alpha), 4*s.cos(alpha / 2)**2)

# Lagrange's exact identity proves the Cauchy--Schwarz step without choosing
# an orientation or restricting any component of the original quaternion.
v = [1 + c, -r1, -r2, -r3]
eq("four-coordinate sharp Cauchy--Schwarz sum of squares",
   sum(x*x for x in u)*sum(x*x for x in v)
   - sum(u[k]*v[k] for k in range(4))**2,
   sum((u[i]*v[j] - u[j]*v[i])**2
       for i, j in combinations(range(4), 2)))
half = quaternion([c, *r])
unit_defect = 1 - c*c - sum(x*x for x in r)
eq("N7 exact square-root matrix identity modulo unit sphere",
   identity + half**2 - 2*c*half, unit_defect*identity)
eq("N7 sharp trace attained at inverse half rotation",
   s.trace(half.conjugate().T)
   + s.trace(half.conjugate().T * half**2) - 4*c,
   -2*c*unit_defect)
eq("one-face derivative normalization",
   sum(s.trace((-s.I*p/2)*U)**2 for p in pauli),
   u1*u1 + u2*u2 + u3*u3)
w = s.symbols("w", real=True)
eq("one-face gradient defect coefficient",
   (1-u0**2).subs(u0, 1-w/2), w-w*w/4)

# Independent rational matrices check the translated face products for
# several noncommuting link and conjugacy realizations.
rational_points = [
    (s.Rational(3, 5), s.Rational(4, 5), 0, 0),
    (s.Rational(1, 3), s.Rational(2, 3), s.Rational(2, 3), 0),
    (s.Rational(2, 3), 0, s.Rational(1, 3), s.Rational(2, 3)),
    (s.Rational(2, 3), s.Rational(1, 3), 0, -s.Rational(2, 3)),
    (s.Rational(1, 2), s.Rational(1, 2), s.Rational(1, 2), s.Rational(1, 2)),
]
mats = [quaternion(q) for q in rational_points]
for i in range(len(mats)):
    aa, bb, cc, dd, qq = [mats[(i+k) % len(mats)] for k in range(5)]
    hh = qq * mats[(i+2) % len(mats)] * qq.conjugate().T
    pp = aa * bb * cc.conjugate().T * dd.conjugate().T
    eq(f"rational noncommuting upper face realization {i+1}",
       aa*bb*(hh.conjugate().T*cc).conjugate().T*dd.conjugate().T,
       pp*dd*hh*dd.conjugate().T)
    eq(f"rational noncommuting lower face realization {i+1}",
       (hh.conjugate().T*aa)*bb*cc.conjugate().T*dd.conjugate().T,
       hh.conjugate().T*pp)


def shift(n, axis):
    return tuple(x + (k == axis) for k, x in enumerate(n))


for box_L in (1, 2, 3, 5):
    vertices = list(product(range(-box_L, box_L+1), repeat=3))
    edges = {(n, axis) for n in vertices for axis in range(3)
             if n[axis] < box_L}
    faces = [(n, i, j) for n in vertices for i, j in combinations(range(3), 2)
             if n[i] < box_L and n[j] < box_L]
    incidence = dict.fromkeys(edges, 0)
    for n, i, j in faces:
        face_edges = [(n, i), (shift(n, i), j),
                      (shift(n, j), i), (n, j)]
        assert len(set(face_edges)) == 4
        for edge in face_edges:
            incidence[edge] += 1
    native_edges = {edge for edge in edges
                    if edge[1] == 0 and edge[0][1] != 0}
    planes = {plane: sum(1 for n, i, j in faces
                        if (i, j) == (0, 1) and n[1] == plane)
              for plane in (-1, 0)}
    exact_bool(f"open-box full edge count L={box_L}",
               len(edges) == 3*(2*box_L)*(2*box_L+1)**2,
               edges=len(edges))
    exact_bool(f"open-box full face count L={box_L}",
               len(faces) == 12*box_L**2*(2*box_L+1),
               faces=len(faces))
    exact_bool(f"open-box native twirl count L={box_L}",
               len(native_edges) == 4*box_L**2*(2*box_L+1),
               native_edges=len(native_edges))
    exact_bool(f"open-box separated face planes L={box_L}",
               all(n == 2*box_L*(2*box_L+1) for n in planes.values()),
               plane_counts=planes)
    exact_bool(f"original face incidence for gradient bound L={box_L}",
               max(incidence.values()) == 4
               and sum(incidence.values()) == 4*len(faces),
               maximum_edge_incidence=max(incidence.values()),
               total_face_edge_incidences=sum(incidence.values()))
L = s.symbols("L", positive=True, integer=True)
eq("full nonlinear separation coefficient",
   2 * (2*L)*(2*L+1) * 4, 16*L*(2*L+1))
eq("full original potential gradient coefficient", 4*4, 16)

# The scalar form identity retains both real and imaginary components of u.
f, df, re, im, dre, dim = s.symbols("f df re im dre dim", real=True)
eq("complex-valued IMS form product identity",
   (df*re+f*dre)**2 + (df*im+f*dim)**2
   - (dre*(2*f*df*re+f*f*dre) + dim*(2*f*df*im+f*f*dim)),
   df**2*(re**2+im**2))
a, g, E, Bn, Bprev = s.symbols("a g E Bn Bprev", positive=True)
n = s.symbols("n", positive=True, integer=True)
eq("potential moment recurrence powers and original coefficients",
   2*a*E*g*g*Bn*g**(2*n)
   + 16*n*n*g**4*Bprev*g**(2*n-2),
   (2*a*E*Bn + 16*n*n*Bprev)*g**(2*n+2))
x = s.symbols("x", positive=True)
moments = [s.Integer(1), x]
for degree in range(1, 4):
    moments.append(s.expand(x*moments[degree]
                            + 16*degree**2*moments[degree-1]))
expected_moments = [1, x, x*x+16, x**3+80*x,
                    x**4+224*x*x+2304]
for degree, expected in enumerate(expected_moments):
    eq(f"potential moment B{degree}", moments[degree], expected)
z = s.symbols("z", positive=True)
eq("strict one-half translation-distance margin",
   s.Rational(1, 2) - z/(2*(1+z)), 1/(2*(1+z)))
eq("positive overlap from unit-vector squared distance",
   1-s.Rational(1, 2)**2/2, s.Rational(7, 8))
eq("raw centered squared-norm lower-bound factor",
   1-s.Rational(1, 2)**2, s.Rational(3, 4))

radius, cutoff = s.symbols("radius cutoff", positive=True)
eq("original T-coordinate Haar radial density",
   4*s.pi*radius**2/(16*s.pi**2)
   * (s.sin(radius/2)/(radius/2))**2,
   s.sin(radius/2)**2/s.pi)
eq("complete exponential-ball Haar normalization",
   s.integrate(s.sin(radius/2)**2/s.pi, (radius, 0, 2*s.pi)), 1)
eq("small-ball Haar lower-bound coefficient",
   s.integrate(radius**2/s.pi**3, (radius, 0, cutoff)),
   cutoff**3/(3*s.pi**3))
phi = s.symbols("phi", positive=True)
eq("class-angle defect Jacobian",
   (2/s.pi)*s.sin(phi)**2/s.diff(2-2*s.cos(phi), phi),
   s.sin(phi)/s.pi)
eq("squared class-angle defect density",
   (1-s.cos(phi)**2).subs(s.cos(phi), 1-w/2), w-w*w/4)
cosine = s.symbols("cosine", real=True)
eq("defect-density probability normalization",
   s.integrate(2*s.sqrt(1-cosine**2)/s.pi, (cosine, -1, 1)), 1)
eq("all-positive-cutoff Haar cap coefficient",
   s.integrate(s.sqrt(radius)/s.pi, (radius, 0, cutoff)),
   2*cutoff**s.Rational(3, 2)/(3*s.pi))

dimcut = s.symbols("D", positive=True, integer=True)
d = s.symbols("d", positive=True, integer=True)
projection_rank = dimcut*(dimcut+1)*(2*dimcut+1)/6
eq("exact Peter-Weyl projection diagonal",
   s.summation(d*d, (d, 1, dimcut)), projection_rank)
eq("dimension-cube projection rank bound factorization",
   dimcut**3-projection_rank, dimcut*(dimcut-1)*(4*dimcut+1)/6)
optimized_cutoff = g**2*(dimcut*g)**(-s.Rational(6, 11))
eq("optimized cap contribution exponent",
   dimcut**3*optimized_cutoff**s.Rational(3, 2),
   (dimcut*g)**s.Rational(24, 11))
eq("optimized fourth-moment contribution exponent",
   g**8*optimized_cutoff**-4, (dimcut*g)**s.Rational(24, 11))

# Exact arbitrary finite masses exercise the floor in the layer-cake identity.
for support in (1, 2, 5, 9):
    masses = s.symbols(f"p1:{support+1}", nonnegative=True)
    cumulative = [sum(masses[:k]) for k in range(1, support+1)]
    layer = sum(cumulative[k-1] * (s.Rational(1, k*k)
                                  - s.Rational(1, (k+1)**2))
                for k in range(1, support))
    layer += cumulative[-1]*s.Rational(1, support**2)
    eq(f"exact layer-cake with arbitrary masses on {support} dimensions",
       layer, sum(masses[k-1]/k**2 for k in range(1, support+1)))
t, A4, B4 = s.symbols("t A4 B4", positive=True)
eq("layer-cake low interval integral",
   2*A4*g**s.Rational(24, 11)
   * s.integrate(t**(-s.Rational(9, 11)), (t, 1, 1/g)),
   11*A4*(g*g-g**s.Rational(24, 11)))
eq("layer-cake tail integral",
   s.integrate(2*t**-3, (t, 1/g, s.oo)), g*g)
eq("epsilon-free raw mass constant",
   (1+11*A4).subs(A4, 4/(3*s.pi)+2*B4),
   1+44/(3*s.pi)+22*B4)

# N35: retain the exact determinant factor as a symbol until the final limit.
j, Dexact, Ilat, Drelative = s.symbols(
    "j Dexact Ilat Drelative", positive=True
)
theta_exact = 2*s.pi/(10**4*j**2*Dexact)
Nj = 2*j*j+1
amplitude = (s.Rational(2, 3)*theta_exact**2
             * s.sqrt(3*Ilat/s.Integer(2560))*Nj**s.Rational(7, 2)/g**2)
normalized_amplitude = amplitude/(g**-2*j**-5)
eq("N35 exact original angle and box prefactor before limit",
   normalized_amplitude.subs(Dexact, Drelative*j**4),
   8*s.pi**2/(3*10**8)*s.sqrt(3*Ilat/s.Integer(2560))
   * (2+j**-2)**s.Rational(7, 2)/Drelative**2)
eq("N35 original raw covariance norm coefficient",
   s.sqrt(3*Ilat/s.Integer(2560))*2**s.Rational(7, 2),
   s.sqrt(3*Ilat/20))
eq("N35 original amplitude final coefficient",
   s.limit(normalized_amplitude.subs(Dexact, j**4), j, s.oo),
   8*s.pi**2/(3*10**8)*s.sqrt(3*Ilat/20))
eq("N35 retained coupling lower-growth power",
   (j**-5)**-2*j**-5, j**5)
k = s.symbols("k", positive=True, integer=True)
substitutions = {a: 1/(100*j), g: 2**-k}
eq("N30 exact electric coefficient", (2*g*g/a).subs(substitutions),
   200*j*2**(-2*k))
eq("N30 exact magnetic coefficient", (1/(2*g*g*a)).subs(substitutions),
   50*j*2**(2*k))
eq("N30 exact magnetic/electric ratio", (1/(4*g**4)).subs(substitutions),
   2**(4*k-2))
M = s.symbols("M", positive=True, integer=True)
eq("N30 exact original scalar potential term",
   (M/(g*g*a)).subs(substitutions), 100*j*2**(2*k)*M)

source_paths = [
    "sources/native_original_angle_weak_localization.md",
    "check_native_localization.py",
]
report = {
    "scope": (
        "Exact finite noncommutative words, rational SU(2) matrices, "
        "open-box enumeration, generator/Haar constants and scalar identities "
        "only. The written proofs, not these diagnostics, establish analytic "
        "moments, spectral localization and simultaneous limits."
    ),
    "exact_checks": len(checks),
    "all_passed": True,
    "exact_results": checks,
    "numerical_checks": 0,
    "sources": {
        p: {"sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
        for p in source_paths
    },
}
(ROOT/"NATIVE_LOCALIZATION_CHECKS.json").write_text(
    json.dumps(report, indent=2)+"\n", encoding="utf-8"
)
print(json.dumps({
    "exact_checks": len(checks), "numerical_checks": 0, "all_passed": True
}))
