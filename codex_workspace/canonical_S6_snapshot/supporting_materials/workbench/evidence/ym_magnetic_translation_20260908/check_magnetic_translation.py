"""Exact finite Haar-twirl, box-sum, and coefficient checks.

Only integers and fractions are used.  The four quaternion conjugations
twirl every 2-by-2 matrix exactly; they are not a numerical Haar sample.
Analytic-vacuum and operator-domain proofs are in the companion Markdown.
"""

from fractions import Fraction as F
from itertools import product


def qmul(a, b):
    """SU(2) quaternion convention q0 I - i sum(qk sigma_k)."""
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (
        a0*b0-a1*b1-a2*b2-a3*b3,
        a0*b1+a1*b0+a2*b3-a3*b2,
        a0*b2+a2*b0+a3*b1-a1*b3,
        a0*b3+a3*b0+a1*b2-a2*b1,
    )


def qinv(a):
    return (a[0], -a[1], -a[2], -a[3])


def qproduct(*factors):
    out = (F(1), F(0), F(0), F(0))
    for factor in factors:
        out = qmul(out, factor)
    return out


def unit(a):
    return sum(x*x for x in a) == 1


identity = (F(1), F(0), F(0), F(0))
twirl = tuple(tuple(F(int(i == j)) for i in range(4)) for j in range(4))
links = (
    (F(3, 5), F(4, 5), F(0), F(0)),
    (F(5, 13), F(0), F(12, 13), F(0)),
    (F(8, 17), F(0), F(0), F(15, 17)),
    (F(1, 2), F(1, 2), F(1, 2), F(1, 2)),
)
generic_h = (
    (F(7, 25), F(24, 25), F(0), F(0)),
    (F(20, 29), F(0), F(21, 29), F(0)),
    (F(12, 37), F(0), F(0), F(35, 37)),
    (F(1, 2), -F(1, 2), F(1, 2), -F(1, 2)),
)
for quaternion in links + generic_h + twirl:
    assert unit(quaternion)

# Four conjugations annihilate all imaginary coordinates and fix the scalar.
for test in generic_h + ((F(2), F(3), F(5), F(7)),):
    avg = tuple(
        sum(qproduct(qinv(g), test, g)[i] for g in twirl)/4
        for i in range(4)
    )
    assert avg == (test[0], F(0), F(0), F(0))


def alpha(h):
    bottom, right, top, left = h
    return qproduct(left, qinv(bottom))[0] * qinv(right)[0] * top[0]


def actual_vertex_twirl(h):
    """Translate the four independently gauge-transformed physical links."""
    total = F(0)
    for g00, g10, g11, g01 in product(twirl, repeat=4):
        gauge_links = (
            qproduct(g00, links[0], qinv(g10)),
            qproduct(g10, links[1], qinv(g11)),
            qproduct(g01, links[2], qinv(g11)),
            qproduct(g00, links[3], qinv(g01)),
        )
        translated = tuple(qproduct(qinv(k), u) for k, u in zip(h, gauge_links))
        word = qproduct(
            translated[0], translated[1],
            qinv(translated[2]), qinv(translated[3]),
        )
        total += 2*word[0]
    return total/F(4**4)


wilson = 2*qproduct(links[0], links[1], qinv(links[2]), qinv(links[3]))[0]
assert wilson != 0
shared = generic_h[0]
cases = (
    (identity,)*4,
    generic_h,
    (shared, identity, identity, shared),
    (twirl[3],)*4,
)
for h in cases:
    assert actual_vertex_twirl(h) == alpha(h)*wilson
    assert alpha(tuple(qinv(matrix) for matrix in h)) == alpha(h)
assert alpha(cases[2]) == 1  # shared source factors cancel BEFORE twirling
assert alpha(cases[3]) == 0
flat_background_word = qproduct(cases[3][0], cases[3][1],
                               qinv(cases[3][2]), qinv(cases[3][3]))
assert flat_background_word[0] == 1  # naive background-holonomy coefficient

# Exact cosine cycles for theta = 0, pi/2, pi, pi/3.
cycles = {
    "0": (F(1),),
    "pi/2": (F(1), F(0), -F(1), F(0)),
    "pi": (F(1), -F(1)),
    "pi/3": (F(1), F(1, 2), -F(1, 2), -F(1), -F(1, 2), F(1, 2)),
}


def norm_coefficient(L, cosine):
    a = 2*L*(2*L+1)
    b = 4*L*L
    s12 = sum((1-cosine(m)*cosine(m+1))**2 for m in range(-L, L))
    s13 = sum((1-cosine(m)**2)**2 for m in range(-L, L+1))
    return a*s12+b*s13


for L in range(2, 8):
    a = 2*L*(2*L+1)
    b = 4*L*L
    moment12 = sum((F(m*m+m)+F(1, 2))**2 for m in range(-L, L))
    moment13 = sum(F(m)**4 for m in range(-L, L+1))
    assert moment12 == F(L*(4*L**4+1), 10)
    assert moment13 == F(L*(L+1)*(2*L+1)*(3*L*L+3*L-1), 15)
    polynomial = F(L*L*(2*L+1)*(24*L**4+24*L**3+8*L*L-4*L+3), 15)
    assert a*moment12+b*moment13 == polynomial
    overlap_moment = (
        a*sum(F(m*m+m)+F(1, 2) for m in range(-L, L))
        + b*sum(F(m*m) for m in range(-L, L+1))
    )
    assert overlap_moment == F(2*L*L*(2*L+1)*(4*L*L+2*L+1), 3)
    moment_cube = sum((F(m*m+m)+F(1, 2))**3 for m in range(-L, L))
    moment_six = sum(F(m)**6 for m in range(-L, L+1))
    assert moment_cube == F(2*L**7, 7)-F(L**5, 5)+F(L**3, 6)-F(L, 420)
    assert moment_six == F(L*(L+1)*(2*L+1)*(3*L**4+6*L**3-3*L+1), 21)
    error_coefficient = F(2, 3)*(a*moment_cube+b*moment_six)
    error_polynomial = F(
        L*L*(2*L+1)*(240*L**6+360*L**5+156*L**4-120*L**3-10*L*L+40*L-1),
        315,
    )
    assert error_coefficient == error_polynomial
    assert 0 < error_coefficient <= 16*L**9
    face_count_diagonal = 12*L**4*(2*L*L+1)
    assert F(3, 16*face_count_diagonal) == F(1, 64*L**4*(2*L*L+1))

    for angle, cycle in cycles.items():
        cosine = lambda m, seq=cycle: seq[m % len(seq)]
        direct = norm_coefficient(L, cosine)
        odd1 = sum(cosine(2*m+1) for m in range(-L, L))
        odd2 = sum(cosine(2*(2*m+1)) for m in range(-L, L))
        even2 = sum(cosine(2*m) for m in range(-L, L+1))
        even4 = sum(cosine(4*m) for m in range(-L, L+1))
        a_theta = 1-cosine(1)/2
        fourier12 = 2*L*(a_theta*a_theta+F(1, 8))-a_theta*odd1+odd2/8
        fourier13 = F(3*(2*L+1), 8)-even2/2+even4/8
        assert direct == a*fourier12+b*fourier13
        if angle == "0":
            assert direct == 0
        elif angle == "pi":
            assert direct == 16*L*L*(2*L+1)
        elif angle == "pi/2":
            assert direct == 4*L*L*(3*L+1+(L % 2))
        else:
            assert direct > 0

    # The exact central cochain flips EVERY face, including planes 13 and 23.
    vertices = product(range(-L, L+1), repeat=3)
    for n in vertices:
        for i, j in ((0, 1), (0, 2), (1, 2)):
            if n[i] == L or n[j] == L:
                continue
            ni, nj = list(n), list(n)
            ni[i] += 1
            nj[j] += 1
            sign = lambda x, k: -1 if sum(x[:k]) % 2 else 1
            assert sign(n, i)*sign(ni, j)*sign(nj, i)*sign(n, j) == -1

print("PASS: four exact 256-term vertex twirls, including noncommuting h,")
print("shared-source cancellation, and the failure of the naive holonomy rule.")
print("PASS: exact whole-box angular/Fourier sums, exceptional angles,")
print("both small-angle L-polynomials, and all-plane coupling-parity cochain")
print("for L=2,...,7. No floating point or sampled Haar integration used.")
print("PASS: exact sixth-order error polynomial, the bound 16 L^9,")
print("and the original diagonal's full-face spectral radius.")
