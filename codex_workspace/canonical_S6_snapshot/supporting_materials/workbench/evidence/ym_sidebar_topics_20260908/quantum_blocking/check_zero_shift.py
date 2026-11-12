"""Exact diagnostics for zero-shift forms and exhaustive affine cases.

These rational finite matrices check identities and inequalities, never
replace the interacting vacuum or the manuscript's analytic proofs.
"""
from pathlib import Path
from itertools import combinations
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parent
count = 0
def check(statement, name):
    global count
    if not bool(statement):
        raise AssertionError(name)
    count += 1

def zero(value, name):
    check(s.factor(value) == 0, name)

def psd(matrix, name):
    for size in range(1, matrix.rows + 1):
        for indices in combinations(range(matrix.rows), size):
            check(matrix.extract(indices, indices).det() >= 0, name)

z = s.symbols("z", real=True)
C = s.Matrix([[5, 1], [1, 7]])
b = s.Matrix([1, 2])
d = s.Rational(3, 2)
a = s.Rational(8)
K = s.Matrix([[a, *b], [b[0], C[0, 0], C[0, 1]],
              [b[1], C[1, 0], C[1, 1]]])
gram = s.diag(d, 1, 1)
res = (C + z*s.eye(2)).inv()
M1 = (b.T*res*b)[0]
M2 = (b.T*res**2*b)[0]
M3 = (b.T*res**3*b)[0]
w = res*b
v = s.Matrix([1, -w[0], -w[1]])
norm = d+M2
energy = a-M1-z*M2
quotient = energy/norm
zero((v.T*gram*v)[0]-norm, "physical norm")
zero((v.T*K*v)[0]-energy, "full energy")
zero(s.diff(quotient, z)-2*M3*(z+quotient)/norm, "quotient derivative")
zero(s.diff(energy, z)-2*z*M3, "energy derivative")
zero(s.diff(a+z*d-M1, z)-norm, "norm derivative")
check(s.diff(quotient, z).subs(z, 0) > 0, "zero shift is not quotient minimum")
check(quotient.subs(z, -s.Rational(1, 10)) < quotient.subs(z, 0),
      "negative shift strict quotient improvement")
check(energy.subs(z, -s.Rational(1, 10)) > energy.subs(z, 0),
      "negative shift increases numerator")

# Every branch of the affine theorem, including its threshold and zero coupling.
cases = [
    ("interior_root", s.Rational(19, 6), s.Matrix([1, 2]), 2, 1),
    ("threshold_attained", s.Rational(7), s.Matrix([0, 2]), 2, 3),
    ("threshold_unattained", s.Rational(8), s.Matrix([0, 2]), 2, 3),
    ("uncoupled_interior", s.Rational(4), s.zeros(2, 1), 2, 2),
    ("uncoupled_threshold", s.Rational(6), s.zeros(2, 1), 2, 3),
    ("uncoupled_unattained", s.Rational(8), s.zeros(2, 1), 2, 3),
]
E, x, y = s.symbols("E x y", real=True)
C = s.diag(3, 7)
for name, a, b, d, infimum in cases:
    K = s.Matrix([[a, *b], [b[0], 3, 0], [b[1], 0, 7]])
    gram = s.diag(d, 1, 1)
    psd(K, name+" positive full form")
    F = a-E*d-(b.T*(C-E*s.eye(2)).inv()*b)[0]
    check(F.subs(E, 0) > 0, name+" positive zero Schur")
    h = s.Matrix([x, y])
    u = s.Matrix([1, x, y])
    w = (C-E*s.eye(2)).inv()*b
    zero((u.T*(K-E*gram)*u)[0]-F-((h+w).T*(C-E*s.eye(2))*(h+w))[0],
         name+" shifted completion")
    psd(K-infimum*gram, name+" exact infimum lower bound")
    if infimum < 3:
        zero(F.subs(E, infimum), name+" actual interior root")
        h0 = -(C-infimum*s.eye(2)).inv()*b
        u0 = s.Matrix([1, *h0])
        zero((u0.T*(K-infimum*gram)*u0)[0], name+" actual attainment")
        zero((u0.T*gram*u0)[0]+s.diff(F, E).subs(E, infimum),
             name+" root derivative norm")
    else:
        boundary = s.limit(F, E, 3, dir="-")
        check(boundary >= 0, name+" correct boundary branch")
        h0 = s.Matrix([x, -b[1]/4])
        u0 = s.Matrix([1, *h0])
        zero((u0.T*(K-3*gram)*u0)[0]-boundary,
             name+" boundary completed square with arbitrary kernel component")
        check((boundary == 0) == ("unattained" not in name),
              name+" exhaustive attainment criterion")
        escape = s.Matrix([1, x, 0])
        zero(s.limit((escape.T*K*escape)[0]/(escape.T*gram*escape)[0], x, s.oo)-3,
             name+" actual complementary escape limit")

# Exact all-state comparison for 81 interacting rational block examples.
# C has a known exact bottom; S0 is positive by construction.
examples = 0
for b0 in (s.Rational(-2), s.Rational(1, 2), s.Rational(3)):
    for b1 in (s.Rational(-1), s.Rational(1), s.Rational(5, 2)):
        for d in (s.Rational(1, 2), s.Rational(1), s.Rational(3)):
            for schur in (s.Rational(1, 7), s.Rational(2), s.Rational(11)):
                b = s.Matrix([b0, b1])
                c = s.Rational(3)
                a = schur+(b.T*C.inv()*b)[0]
                K = s.Matrix([[a, b0, b1], [b0, 3, 0], [b1, 0, 7]])
                gram = s.diag(d, 1, 1)
                w = C.inv()*b
                Rnorm = d+(w.T*w)[0]
                lamR = schur/Rnorm
                harmonic = lamR*c/(lamR+c)
                psd(K-harmonic*gram, "all-state harmonic lower bound")
                check(harmonic >= min(lamR, c)/2, "uniform factor two")
                u = s.Matrix([1, x, y])
                v = s.Matrix([1, -w[0], -w[1]])
                k = u-v
                zero((v.T*K*k)[0], "exact energy orthogonality")
                zero((u.T*K*u)[0]-(v.T*K*v)[0]-(k.T*K*k)[0],
                     "full energy split")
                zero((u.T*gram*u)[0]-(v.T*gram*v)[0]-(k.T*gram*k)[0]
                     -2*(v.T*gram*k)[0], "retained norm cross term")
                examples += 1

alpha, kappa, g, spacing, ell, m, N = s.symbols(
    "alpha kappa g spacing ell m N", positive=True)
Delta = 3*kappa*alpha**N/4
zero((kappa*ell/Delta).subs(ell, 4*m)-16*m/(3*alpha**N),
     "zero-loop norm in original physical block length")
zero(Delta.subs(kappa, 2*g**2/spacing)-3*g**2*alpha**N/(2*spacing),
     "finite-box gap in original physical coefficients")
receipt = {
    "status": "passed",
    "exact_assertions": count,
    "affine_cases": [case[0] for case in cases],
    "rational_block_examples": examples,
    "scope": "Exact rational diagnostics of physical norms, Rayleigh derivatives, "
             "all affine threshold cases, energy-orthogonal decomposition and "
             "the block-independent factor-two comparison. Analytic gauge, "
             "domain and all-volume proofs are in the manuscript; no vacuum replacement.",
    "sha256": {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
               for name in ("check_zero_shift.py", "extensive_quantum_blocking.tex")}
}
(ROOT/"ZERO_SHIFT_CHECKS.json").write_text(json.dumps(receipt, indent=2)+"\n",
                                        encoding="utf-8")
print(json.dumps(receipt, indent=2))
