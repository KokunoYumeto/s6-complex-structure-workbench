"""Post-exposure checks of the released KX auxiliary rank argument.

This is a new calculation from the defining marked A_i,g_i fixture.
It neither reads nor reruns a historical enumeration, and it does not
modify the frozen KX derivation, enumeration, output, or data.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import hashlib
import json
import re
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json"
data = json.loads(RAW.read_text())
J = s.Matrix([[0, 1], [-1, 0]])
print("POST-EXPOSURE KX AUXILIARY CHECK")
print("raw_sha256", hashlib.sha256(RAW.read_bytes()).hexdigest())

# A fixed nonzero three-column minor and its exact inverse prove rank
# three for the elliptic-plus-line block. Multiplication of the last
# row by any nonzero a preserves this rank. The fourth coordinate of
# every full monodromy difference is zero.
for profile in data["rows"]:
    blocks = []
    for A, g in zip(profile["elliptic_matrices"],
                    profile["generator_section_cocycle"]):
        A, g = s.Matrix(A), s.Matrix(g)
        assert A.det() == 1
        beta = -g.T * J * A
        blocks.append((A - s.eye(2)).col_join(beta))
    H = s.Matrix.hstack(*blocks)
    cols = next(c for c in combinations(range(H.cols), 3)
                if H[:, c].det() != 0)
    minor = H[:, cols]
    inverse = minor.inv()
    assert minor * inverse == s.eye(3) == inverse * minor
    kinds = profile["fibers"]
    additive = sum(not re.fullmatch(r"I\d+", k) for k in kinds)
    multiplicative = len(kinds) - additive
    root_rank = 0
    euler = 0
    for k in kinds:
        m = re.fullmatch(r"I(\d+)", k)
        star = re.fullmatch(r"I(\d+)\*", k)
        if m:
            n = int(m[1])
            root_rank += n - 1
            euler += n
        elif star:
            n = int(star[1])
            root_rank += n + 4
            euler += n + 6
        else:
            rr, ee = {"II": (0, 2), "III": (1, 3), "IV": (2, 4),
                      "IV*": (6, 8), "III*": (7, 9)}[k]
            root_rank += rr
            euler += ee
    assert H.rank() == 3
    assert root_rank == 7 and euler == 12
    assert 2 * additive + multiplicative == 5
    print(f'OS{profile["OS"]}/{profile["profile"]}: '
          f'columns={cols}, determinant={minor.det()}, '
          f'minor={minor.tolist()}, inverse={inverse.tolist()}, '
          f'Fa={additive}, Fm={multiplicative}, '
          f'root_rank={root_rank}, euler={euler}')

# Verify the literal displayed alternating form without choosing the
# unrestricted central entry c or specializing the section weights.
a, b, c, x, y, z, w, u, v = s.symbols("a b c x y z w u v")
B = s.Matrix([[x, y], [z, w]])
g = s.Matrix([u, v])
A = s.zeros(4)
A[:2, :2] = B
A[:2, 3] = b * g
A[2, :2] = -a * g.T * J * B
A[2, 2] = A[3, 3] = 1
A[2, 3] = c
Omega = s.diag(a * J, s.Matrix([[0, -b], [b, 0]]))
residual = (A.T * Omega * A - Omega).applyfunc(s.factor)
expected = s.zeros(4)
expected[0, 1] = a * (B.det() - 1)
expected[1, 0] = -expected[0, 1]
assert residual == expected
print("literal_T", A.tolist())
print("literal_Omega", Omega.tolist())
print("TtOmegaT_minus_Omega", residual.tolist())
print("Consequently the residual is zero on det(B)=1, for all a,b,c,g.")

# A complete symbolic finite-interval telescoping proof is printed in
# the note. These exact representatives additionally verify its signed
# theta-frame convention, including negative component translations.
cases = 0
for n in range(1, 13):
    for p in range(n):
        inc = -p
        F0 = [-min(0, i - p) for i in range(n)]
        def frame(i):
            q, r = divmod(i, n)
            return F0[r] + q * inc
        for shift in range(-2*n-1, 2*n+2):
            telescoped = sum(frame(i+shift)-frame(i) for i in range(n))
            assert telescoped == inc * shift
            for weight in (-1, 0, 1):
                zeros = [weight + frame(i) - frame(i+shift)
                         for i in range(n)]
                literal_period = s.Matrix([[n, shift], [-inc, -weight]])
                reflection = s.diag(1, -1)
                reflected = reflection * literal_period
                assert reflection**2 == s.eye(2)
                assert reflected == s.Matrix([[n, shift], [inc, weight]])
                assert sum(zeros) == n*weight - inc*shift
                assert reflected.det() == sum(zeros)
                assert literal_period.det() == -sum(zeros)
                cases += 1
print("theta_frame_exact_examples", cases)
print("No example count is used as a proof for unbounded parameters.")
print("PASS: 21 exact rank minors and inverses; all profile identities; "
      "literal alternating-form identity; signed period reflection.")
