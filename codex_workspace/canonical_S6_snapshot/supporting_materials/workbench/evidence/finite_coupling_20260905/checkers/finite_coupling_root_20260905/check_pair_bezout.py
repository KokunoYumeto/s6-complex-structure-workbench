"""Bounded exact follow-up: common scalar-residual roots at the audit pair.

The supplied checker constructs the literal, unrestricted spatial pair and
all original residual polynomials. This script keeps those polynomials and
asks whether two complete Hermitian residual entries admit a Bezout identity.
No point is called a solution based on contracted equations or sample tests.
"""
import hashlib
import json
import os
from pathlib import Path
import runpy
import threading
import time

started = time.monotonic()
guard = threading.Timer(55.0, lambda: os._exit(124))
guard.daemon = True
guard.start()
source = Path(__file__).resolve().parents[1] / "finite_coupling_audit_20260905" / "check_independent.py"
data = runpy.run_path(str(source))
s, t = data["s"], data["t"]
left_expr = data["PH"][0, 0]
right_expr = data["PH"][1, 1]
left = s.Poly(left_expr, t, extension=s.sqrt(6))
right = s.Poly(right_expr, t, extension=s.sqrt(6))
coef_left, coef_right, common = s.gcdex(left, right)
assert coef_left * left + coef_right * right == common
certificate = {
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "source": source.name,
    "spatial_pair_in_exact_diagonal_coordinates": {
        "Z1": "mat(1,2,1+i,-1+2i,2-i)",
        "Z2": "mat(-2,1,2+3i,1-i,-1+2i)",
        "map_to_original_frame": "Z_j(original)=U Z_j(diagonal) U*; U is retained in the canonical scalar-coordinate section",
    },
    "field": "Q(sqrt(6))",
    "entries": ["P_H[1,1]", "P_H[2,2]"],
    "left_degree": int(left.degree()),
    "right_degree": int(right.degree()),
    "gcd_degree": int(common.degree()),
    "identity": "A(t)*P_H[1,1](t)+B(t)*P_H[2,2](t)=G(t)",
    "original_left_coefficients_descending": [str(c) for c in left.all_coeffs()],
    "original_right_coefficients_descending": [str(c) for c in right.all_coeffs()],
    "bezout_A_coefficients_descending": [str(c) for c in coef_left.all_coeffs()],
    "bezout_B_coefficients_descending": [str(c) for c in coef_right.all_coeffs()],
    "gcd_coefficients_descending": [str(c) for c in common.all_coeffs()],
    "identity_checked_exactly": True,
    "scope": "This single full spatial pair, not the entire spatial projection.",
    "elapsed_seconds": time.monotonic() - started,
}
target = Path(__file__).with_name("PAIR_BEZOUT_CERTIFICATE.json")
target.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")

# A compact, hand-replayable certificate: retain the exact input entries and
# reduce their coefficients through the explicit localized-ring map sqrt(6)
# -> 39 in F_101. Every denominator is checked before inversion.
prime, sqrt6_image = 101, 39
assert sqrt6_image**2 % prime == 6

def rational_mod(value):
    num, den = s.Rational(value).as_numer_denom()
    assert int(den) % prime != 0
    return int(num) * pow(int(den), -1, prime) % prime

def coefficient_mod(value):
    root = s.sqrt(6)
    conjugate = s.expand(value).xreplace({root: -root})
    rational = s.expand((value + conjugate) / 2)
    radical = s.simplify((value - conjugate) / (2 * root))
    assert rational.is_Rational and radical.is_Rational
    assert s.expand(value - rational - radical * root) == 0
    return (rational_mod(rational) + sqrt6_image * rational_mod(radical)) % prime

def reduction(poly):
    return s.Poly.from_list([coefficient_mod(c) for c in poly.all_coeffs()], t, modulus=prime)

reduced_left, reduced_right = reduction(left), reduction(right)
assert reduced_left.degree() == reduced_right.degree() == 12
red_A, red_B, red_G = s.gcdex(reduced_left, reduced_right)
assert red_G.as_expr() == 1
assert red_A * reduced_left + red_B * reduced_right == red_G

def residues(poly):
    return [int(c) % prime for c in poly.all_coeffs()]

modular = {
    "field": "F_101", "sqrt6_image": sqrt6_image,
    "all_original_coefficient_denominators_invertible": True,
    "original_entry_degrees_preserved": [12, 12],
    "coefficients_descending": {"P_H11": residues(reduced_left),
                                "P_H22": residues(reduced_right),
                                "A": residues(red_A), "B": residues(red_B)},
    "identity": "A*P_H11+B*P_H22=1 in F_101[t]",
    "identity_checked_exactly": True,
    "scope": "Nonzero Sylvester determinant at this one explicit full spatial pair; reduction is a certificate, not replacement of the real equations.",
}
modular_target = Path(__file__).with_name("PAIR_MODULAR_CERTIFICATE.json")
modular_target.write_text(json.dumps(modular, indent=2) + "\n", encoding="utf-8")
guard.cancel()
print(json.dumps({"gcd_degree": certificate["gcd_degree"], "identity_checked_exactly": True,
                  "certificate": str(target), "elapsed_seconds": certificate["elapsed_seconds"]}))
print(json.dumps(modular))
