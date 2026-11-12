"""Exact audit of the p=1201 selector rays inside Herm_3(H).

The certificate uses only the Python standard library.  It reconstructs the
complete selector census rather than trusting a copied table, retains channel,
residual, scale, orientation, and ordered denominators, and then checks the
linear/Jordan invariants of the canonical real 2-by-2 corner embedding.

It deliberately distinguishes three equivalence relations:

* fifteen marked oriented selector families;
* eleven unordered denominator triples;
* ten distinct hard-class prime progressions.

No claim that these fifteen rays form a basis of Herm_3(H) is encoded: the
certificate proves that their images span exactly a 3-dimensional corner.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from hashlib import sha256
import json
from math import factorial, gcd, isqrt, lcm


P0 = 1201
HARD_RESIDUE = 361
HARD_MODULUS = 840


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def divisors(n: int) -> list[int]:
    out: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def sqrt_interval(n: int, decimal_places: int = 100) -> tuple[Fraction, Fraction]:
    """A rigorous rational interval containing sqrt(n)."""
    scale = 10**decimal_places
    floor_scaled = isqrt(n * scale * scale)
    lo = Fraction(floor_scaled, scale)
    hi = Fraction(floor_scaled + 1, scale)
    require(lo * lo <= n < hi * hi, f"bad square-root enclosure for {n}")
    return lo, hi


SQRT2_LO, SQRT2_HI = sqrt_interval(2)
SQRT3_LO, SQRT3_HI = sqrt_interval(3)

# Rigorous interval enclosures for the three Koide chamber endpoints.
ALPHA_LO = (SQRT3_LO - SQRT2_HI) / (1 + SQRT2_HI)
ALPHA_HI = (SQRT3_HI - SQRT2_LO) / (1 + SQRT2_LO)
BETA_LO = (SQRT3_LO + SQRT2_LO) / (1 + SQRT2_HI)
BETA_HI = (SQRT3_HI + SQRT2_HI) / (1 + SQRT2_LO)
GAMMA_LO = 1 + SQRT2_LO
GAMMA_HI = 1 + SQRT2_HI


def compare_to_interval(x: Fraction, lo: Fraction, hi: Fraction) -> int:
    """Return -1 below, +1 above, and 0 only if the enclosure is inconclusive."""
    if x < lo:
        return -1
    if x > hi:
        return 1
    return 0


def positive_koide_ray(r: int, t: int) -> bool:
    theta = Fraction(r, t)
    c_alpha = compare_to_interval(theta, ALPHA_LO, ALPHA_HI)
    c_beta = compare_to_interval(theta, BETA_LO, BETA_HI)
    c_gamma = compare_to_interval(theta, GAMMA_LO, GAMMA_HI)
    require(0 not in (c_alpha, c_beta, c_gamma), "Koide boundary comparison unresolved")
    return c_alpha == -1 or (c_beta == 1 and c_gamma == -1)


@dataclass(frozen=True)
class State:
    tag: str
    channel: str
    epsilon: int
    j: int
    R: int
    a: int
    u: int
    v: int
    h: int
    r: int
    t: int
    T: int
    K: int
    kappa: int
    denominators: tuple[int, int, int]
    unordered_triple: tuple[int, int, int]
    native_prime_modulus: int
    hard_prime_modulus: int
    hard_scale_increment: int
    positive_koide: bool


TAG_BY_MARKING = {
    ("E", 23, 1, 18): "E23a",
    ("M", 23, 6, 17): "M23a",
    ("M", 23, 17, 6): "M23b",
    ("E", 23, 9, 1): "E23b",
    ("M", 31, 1, 154): "M31a",
    ("E", 31, 4, 1): "E31",
    ("M", 31, 154, 1): "M31b",
    ("M", 39, 1, 155): "M39a",
    ("E", 39, 5, 1): "E39",
    ("M", 39, 155, 1): "M39b",
    ("M", 47, 8, 39): "M47a",
    ("M", 47, 39, 8): "M47b",
    ("E", 71, 1, 6): "E71",
    ("E", 339, 35, 1): "E339",
    ("E", 1043, 33, 1): "E1043",
}


def reconstruct_census() -> list[State]:
    require(P0 % 12 == 1, "base prime is not 1 mod 12")
    states: list[State] = []
    for j in range((P0 - 1) // 4):
        R = 4 * j + 3
        a = (P0 + R) // 4
        require(4 * a == P0 + R, "shell equation failed")
        require(0 < R < P0, "residual outside shell range")
        for u in divisors(a * a):
            v = a * a // u
            for epsilon, channel in ((0, "E"), (1, "M")):
                selector_numerator = 4 * u + P0**epsilon
                if selector_numerator % R:
                    continue
                T = selector_numerator // R
                K_numerator = P0 ** (1 - epsilon) * T + 1
                require(K_numerator % 4 == 0, "K is not integral")
                K = K_numerator // 4

                g = gcd(a, u)
                require((g * g) % u == 0, "primitive scale is not integral")
                h = g * g // u
                r = u // g
                t = a // g
                require(gcd(r, t) == 1, "primitive ray is not primitive")
                require((u, a, v) == (h * r * r, h * r * t, h * t * t),
                        "rank-one factorization failed")

                if channel == "E":
                    require((P0 * r + t) % R == 0, "exterior incidence failed")
                    kappa = (P0 * r + t) // R
                    require(K == h * r * kappa, "exterior K factorization failed")
                    denominators = (
                        h * r * t,
                        h * t * kappa,
                        P0 * h * r * kappa,
                    )
                    native_modulus = 4 * r * t * R
                else:
                    require((r + t) % R == 0, "middle incidence failed")
                    kappa = (r + t) // R
                    require(K == h * r * kappa, "middle K factorization failed")
                    denominators = (
                        h * r * t,
                        P0 * h * r * kappa,
                        P0 * h * t * kappa,
                    )
                    native_modulus = 4 * r * t

                reciprocal_sum = sum(
                    (Fraction(1, d) for d in denominators), start=Fraction(0, 1)
                )
                require(reciprocal_sum == Fraction(4, P0), "unit-fraction identity failed")
                hard_modulus = lcm(native_modulus, HARD_MODULUS)
                hard_scale_increment = hard_modulus // (4 * r * t)
                require(hard_modulus % native_modulus == 0, "bad hard-class intersection")
                require(hard_modulus % HARD_MODULUS == 0, "hard class not preserved")
                require(gcd(P0, hard_modulus) == 1, "prime progression is not reduced")

                marking = (channel, R, r, t)
                require(marking in TAG_BY_MARKING, f"unexpected selector state {marking}")
                states.append(
                    State(
                        tag=TAG_BY_MARKING[marking],
                        channel=channel,
                        epsilon=epsilon,
                        j=j,
                        R=R,
                        a=a,
                        u=u,
                        v=v,
                        h=h,
                        r=r,
                        t=t,
                        T=T,
                        K=K,
                        kappa=kappa,
                        denominators=denominators,
                        unordered_triple=tuple(sorted(denominators)),
                        native_prime_modulus=native_modulus,
                        hard_prime_modulus=hard_modulus,
                        hard_scale_increment=hard_scale_increment,
                        positive_koide=positive_koide_ray(r, t),
                    )
                )

    states.sort(key=lambda q: list(TAG_BY_MARKING.values()).index(q.tag))
    require(len(states) == 15, "census does not have fifteen states")
    require({(q.channel, q.R, q.r, q.t) for q in states} == set(TAG_BY_MARKING),
            "reconstructed census differs from marked table")
    return states


STATES = reconstruct_census()
STATE_BY_TAG = {q.tag: q for q in STATES}
STATE_BY_CHANNEL_R_U = {(q.channel, q.R, q.u): q for q in STATES}


def verify_affine_family(q: State, hard_step_index: int) -> None:
    """Verify the exact hard-class subfamily for an arbitrary test index."""
    require(hard_step_index >= 0, "negative family parameter")
    p = P0 + q.hard_prime_modulus * hard_step_index
    h = q.h + q.hard_scale_increment * hard_step_index
    require(p == 4 * q.r * q.t * h - q.R, "affine shell equation failed")
    require(p % HARD_MODULUS == HARD_RESIDUE, "hard residue was not preserved")
    u = h * q.r * q.r
    if q.channel == "E":
        require((4 * u + 1) % q.R == 0, "propagated exterior gate failed")
        kappa = (p * q.r + q.t) // q.R
        require(p * q.r + q.t == q.R * kappa, "propagated exterior incidence failed")
        xyz = (
            h * q.r * q.t,
            h * q.t * kappa,
            p * h * q.r * kappa,
        )
    else:
        require((4 * u + p) % q.R == 0, "propagated middle gate failed")
        kappa = (q.r + q.t) // q.R
        require(q.r + q.t == q.R * kappa, "propagated middle incidence failed")
        xyz = (
            h * q.r * q.t,
            p * h * q.r * kappa,
            p * h * q.t * kappa,
        )
    require(
        sum((Fraction(1, d) for d in xyz), start=Fraction(0, 1)) == Fraction(4, p),
        "propagated unit-fraction identity failed",
    )


for state in STATES:
    for index in (0, 1, 2, 17):
        verify_affine_family(state, index)


def matrix_rank(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    matrix = [row[:] for row in rows]
    row_count = len(matrix)
    column_count = len(matrix[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next((i for i in range(pivot_row, row_count) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        pivot_value = matrix[pivot_row][column]
        matrix[pivot_row] = [x / pivot_value for x in matrix[pivot_row]]
        for i in range(row_count):
            if i == pivot_row or not matrix[i][column]:
                continue
            factor = matrix[i][column]
            matrix[i] = [x - factor * y for x, y in zip(matrix[i], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def determinant_3(rows: list[list[int]]) -> int:
    require(len(rows) == 3 and all(len(row) == 3 for row in rows), "not a 3-by-3 matrix")
    (a, b, c), (d, e, f), (g, h, i) = rows
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def ray_coordinates(q: State) -> tuple[int, int, int]:
    """Coordinates of Gamma/h in Sym_2(R): (r^2,rt,t^2)."""
    return q.r * q.r, q.r * q.t, q.t * q.t


def projector_coordinates(q: State) -> tuple[Fraction, Fraction, Fraction]:
    denominator = q.r * q.r + q.t * q.t
    return (
        Fraction(q.r * q.r, denominator),
        Fraction(q.r * q.t, denominator),
        Fraction(q.t * q.t, denominator),
    )


def jordan_product_sym2(
    x: tuple[Fraction, Fraction, Fraction],
    y: tuple[Fraction, Fraction, Fraction],
) -> tuple[Fraction, Fraction, Fraction]:
    """Jordan product in coordinates [[a,b],[b,c]]."""
    a, b, c = x
    d, e, f = y
    return (
        a * d + b * e,
        (e * (a + c) + b * (d + f)) / 2,
        b * e + c * f,
    )


PROJECTORS = {q.tag: projector_coordinates(q) for q in STATES}
for tag, projector in PROJECTORS.items():
    require(jordan_product_sym2(projector, projector) == projector,
            f"{tag} does not map to an idempotent")

for i, q in enumerate(STATES):
    for q2 in STATES[i + 1 :]:
        require(q.r * q2.t != q2.r * q.t,
                f"projective rays collide: {q.tag}, {q2.tag}")

RAY_MATRIX = [[Fraction(x) for x in ray_coordinates(q)] for q in STATES]
RAY_SPAN_RANK = matrix_rank(RAY_MATRIX)
require(RAY_SPAN_RANK == 3, "selector ray span is not the full 3-dimensional corner")

WITNESS_TAGS = ("E31", "E39", "E339")
WITNESS_ROWS = [list(ray_coordinates(STATE_BY_TAG[tag])) for tag in WITNESS_TAGS]
WITNESS_DETERMINANT = determinant_3(WITNESS_ROWS)
require(WITNESS_DETERMINANT == -930, "unexpected spanning witness determinant")

COLLINEAR_PROJECTIVE_TRIPLES: list[tuple[str, str, str]] = []
for i, q1 in enumerate(STATES):
    for j, q2 in enumerate(STATES[i + 1 :], start=i + 1):
        for q3 in STATES[j + 1 :]:
            rows = [list(ray_coordinates(q)) for q in (q1, q2, q3)]
            if determinant_3(rows) == 0:
                COLLINEAR_PROJECTIVE_TRIPLES.append((q1.tag, q2.tag, q3.tag))
require(not COLLINEAR_PROJECTIVE_TRIPLES,
        "three distinct selector points are collinear on the determinant conic")


def herm3h_vector(q: State) -> tuple[int, ...]:
    """Full 15 coordinates (d1,d2,d3,q1[4],q2[4],q3[4]).

    The canonical embedding is
      [[u,a],[a,v]] -> [[u,a,0],[a,v,0],[0,0,0]].
    In the Moore convention q3 is the (1,2) entry, and is real here.
    """
    return (q.u, q.v, 0, 0, 0, 0, 0, 0, 0, 0, 0, q.a, 0, 0, 0)


HERM_VECTORS = [list(map(Fraction, herm3h_vector(q))) for q in STATES]
require(all(len(row) == 15 for row in HERM_VECTORS), "bad Herm_3(H) coordinate length")
HERM_IMAGE_RANK = matrix_rank(HERM_VECTORS)
require(HERM_IMAGE_RANK == 3, "embedded selectors do not have rank three")


def orientation_reverse(q: State) -> State:
    """Normalized reversal: fixed on E, u<->v on M."""
    if q.channel == "E":
        return q
    return STATE_BY_CHANNEL_R_U[("M", q.R, q.v)]


require(all(orientation_reverse(orientation_reverse(q)) == q for q in STATES),
        "orientation reversal is not involutive")
REVERSAL_FIXED = sum(orientation_reverse(q) == q for q in STATES)
require(REVERSAL_FIXED == 7, "orientation reversal has wrong fixed count")

# The three E witness rays span the corner and are fixed by normalized
# reversal.  Therefore any linear map of the corner inducing reversal would
# be the identity, but every M pair consists of distinct rays.  These checked
# premises certify the linear/Jordan-symmetry obstruction stated in the report.
require(all(orientation_reverse(STATE_BY_TAG[tag]) == STATE_BY_TAG[tag] for tag in WITNESS_TAGS),
        "spanning exterior witnesses are not fixed")
require(any(orientation_reverse(q) != q for q in STATES if q.channel == "M"),
        "no nontrivial middle reversal pair found")


def transvection(v: int) -> int:
    """(x1,x2,x3,x4) -> (x1+x2,x2,x3,x4) over F_2."""
    require(0 <= v < 16, "vector outside F_2^4")
    x2 = (v >> 1) & 1
    return v ^ x2


NONZERO_F2_4 = tuple(range(1, 16))
require(all(transvection(transvection(v)) == v for v in range(16)),
        "transvection is not involutive")
F2_FIXED = sum(transvection(v) == v for v in NONZERO_F2_4)
require(F2_FIXED == 7, "F_2^4 transvection has wrong fixed count")

# One explicit but noncanonical C2-equivariant bijection.  Its arbitrariness is
# measured in the report; it is not promoted to an incidence correspondence.
C2_BIJECTION = {
    "E23a": 1,
    "E23b": 4,
    "E31": 5,
    "E39": 8,
    "E71": 9,
    "E339": 12,
    "E1043": 13,
    "M23a": 2,
    "M23b": 3,
    "M31a": 6,
    "M31b": 7,
    "M39a": 10,
    "M39b": 11,
    "M47a": 14,
    "M47b": 15,
}
require(set(C2_BIJECTION) == set(STATE_BY_TAG), "C2 map omits a selector state")
require(set(C2_BIJECTION.values()) == set(NONZERO_F2_4), "C2 map is not bijective")
require(all(
    C2_BIJECTION[orientation_reverse(q).tag] == transvection(C2_BIJECTION[q.tag])
    for q in STATES
), "displayed C2 bijection is not equivariant")

# Natural projective-line incidence on nonzero F_2^4 has triples x+y+z=0.
F2_PROJECTIVE_LINES = {
    tuple(sorted((x, y, x ^ y)))
    for x in NONZERO_F2_4
    for y in NONZERO_F2_4
    if x != y
}
require(len(F2_PROJECTIVE_LINES) == 35, "PG(3,2) line count is not 35")


UNORDERED_TRIPLES = {q.unordered_triple for q in STATES}
HARD_PROGRESSIONS: dict[int, list[str]] = {}
for q in STATES:
    HARD_PROGRESSIONS.setdefault(q.hard_prime_modulus, []).append(q.tag)

require(len(UNORDERED_TRIPLES) == 11, "unordered-triple quotient is not eleven")
require(len(HARD_PROGRESSIONS) == 10, "hard-progression quotient is not ten")
require(sum(q.channel == "E" for q in STATES) == 7, "wrong exterior count")
require(sum(q.channel == "M" for q in STATES) == 8, "wrong middle count")
require(sum(q.positive_koide for q in STATES) == 3, "wrong positive Koide count")
require({q.tag for q in STATES if q.positive_koide} == {"E23a", "M31a", "M39a"},
        "wrong positive Koide orientations")

# Exact cardinalities of comparison objects.  They are reported only as
# cardinality/cycle-type comparisons, not as intrinsic selector geometries.
A3_ROOTS = tuple((i, j) for i in range(4) for j in range(4) if i != j)
A3_UNORIENTED_ROOTS = tuple((i, j) for i in range(4) for j in range(i + 1, 4))
A3_MINUSCULE_WEIGHTS = tuple(
    [(1, i) for i in range(4)]
    + [(2, i, j) for i in range(4) for j in range(i + 1, 4)]
    + [(3, i) for i in range(4)]
)
require((len(A3_ROOTS), len(A3_UNORIENTED_ROOTS), len(A3_MINUSCULE_WEIGHTS)) == (12, 6, 14),
        "A3 comparison counts changed")


report = {
    "schema": "p1201-selector-herm3h-bridge-v2",
    "base_prime": P0,
    "hard_class": {"residue": HARD_RESIDUE, "modulus": HARD_MODULUS},
    "counts": {
        "marked_oriented_selector_families": len(STATES),
        "distinct_projective_primitive_rays": len({(q.r, q.t) for q in STATES}),
        "exterior_states": sum(q.channel == "E" for q in STATES),
        "middle_states": sum(q.channel == "M" for q in STATES),
        "unordered_denominator_triples": len(UNORDERED_TRIPLES),
        "distinct_hard_prime_progressions": len(HARD_PROGRESSIONS),
        "positive_koide_orientations": sum(q.positive_koide for q in STATES),
    },
    "states": [asdict(q) for q in STATES],
    "hard_progressions": {
        str(modulus): tags for modulus, tags in sorted(HARD_PROGRESSIONS.items())
    },
    "canonical_map": {
        "selector_to_rank_one": "Gamma=h[[r^2,rt],[rt,t^2]]=[[u,a],[a,v]]",
        "rank_one_to_Herm3H": "iota(Gamma)=[[u,a,0],[a,v,0],[0,0,0]]",
        "projector": "P=(r^2+ t^2)^(-1)[[r^2,rt,0],[rt,t^2,0],[0,0,0]]",
        "distinct_projective_images": 15,
        "linear_span_dimension_in_Herm3H": HERM_IMAGE_RANK,
        "jordan_closure_dimension": 3,
        "corner": (
            "C_R=iota(Sym_2(R))=e Herm_3(H) e intersect Herm_3(R), "
            "e=diag(1,1,0); C_R has dimension 3, while eJe=Herm_2(H) has dimension 6"
        ),
        "witness_tags": WITNESS_TAGS,
        "witness_coordinate_rows": WITNESS_ROWS,
        "witness_determinant": WITNESS_DETERMINANT,
        "collinear_triples_among_fifteen_conic_points": len(COLLINEAR_PROJECTIVE_TRIPLES),
    },
    "orientation_reversal": {
        "fixed_states": REVERSAL_FIXED,
        "two_cycles": 4,
        "linear_or_jordan_realization_on_canonical_corner": False,
        "obstruction": (
            "three fixed E images span the real symmetric corner C_R, hence a linear "
            "realization on C_R would be identity; "
            "four M pairs must be exchanged"
        ),
    },
    "finite_geometry_tests": {
        "F2_4_nonzero_points": 15,
        "transvection_fixed_nonzero_points": F2_FIXED,
        "transvection_two_cycles": 4,
        "C2_set_equivalence": True,
        "one_noncanonical_equivariant_bijection": C2_BIJECTION,
        "C2_set_automorphism_group_order": factorial(7) * (2**4) * factorial(4),
        "PG3_F2_lines": len(F2_PROJECTIVE_LINES),
        "selector_conic_collinear_triples": len(COLLINEAR_PROJECTIVE_TRIPLES),
        "projective_incidence_preserving_bijection": False,
        "A3_roots": len(A3_ROOTS),
        "A3_unoriented_roots": len(A3_UNORIENTED_ROOTS),
        "A3_minuscule_nonzero_weights": len(A3_MINUSCULE_WEIGHTS),
    },
    "conclusion": (
        "The exact selector-to-Jordan map gives fifteen distinct marked projective rank-one "
        "points, but they span and Jordan-generate only the 3-dimensional real symmetric "
        "corner C_R=iota(Sym_2(R)), properly contained in the 6-dimensional Peirce "
        "corner eJe=Herm_2(H). "
        "Thus the common number 15 is not a dimension/basis identification under the currently "
        "defined map."
    ),
}

encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
print(encoded, end="")
print("payload_sha256=" + sha256(encoded.encode("utf-8")).hexdigest())

