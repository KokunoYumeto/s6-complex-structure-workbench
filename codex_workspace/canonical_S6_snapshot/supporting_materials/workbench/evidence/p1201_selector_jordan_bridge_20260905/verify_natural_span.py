"""Exact span test for the natural p=1201 selector-to-Jordan map.

The input is the independently checked complete selector census.  Each marked
state (h,r,s) determines the positive rank-one symmetric matrix

    Gamma = h * [[r^2, r*s], [r*s, s^2]].

We retain all fifteen quaternionic-Hermitian coordinates when embedding Gamma
as the upper-left real 2-by-2 corner of Herm_3(H).  The script proves by exact
integer row reduction that the fifteen projective selector rays are distinct,
but their linear span (and hence their Jordan-generated linear subalgebra) has
dimension three, not fifteen.
"""

from __future__ import annotations

from fractions import Fraction
from functools import reduce
from hashlib import sha256
import json
from math import gcd
from pathlib import Path


INPUT = Path(
    r"C:\Users\user\Documents\Erdos Strauss and related\Erdos-Straus-Foundation"
) / "certificates" / "p1201_affine_selector_families_results.json"
OUTPUT = Path(__file__).with_name("natural_span_results.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def integer_gcd(values: tuple[int, ...]) -> int:
    return reduce(gcd, (abs(v) for v in values), 0)


def divisors(n: int) -> list[int]:
    out: list[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    return sorted(out)


def trial_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def complete_selector_counts(p: int) -> dict[str, int]:
    """Enumerate the same complete oriented E/M selector at a fixed prime."""
    require(p % 4 == 1 and trial_prime(p), f"{p} is not a prime congruent to 1 mod 4")
    exterior = 0
    middle = 0
    unordered: set[tuple[int, int, int]] = set()
    for j in range((p - 1) // 4):
        R = 4 * j + 3
        a = (p + R) // 4
        require(4 * a == p + R, "shell integrality failed")
        for u in divisors(a * a):
            v = a * a // u
            for epsilon, channel in ((0, "E"), (1, "M")):
                numerator = 4 * u + p**epsilon
                if numerator % R:
                    continue
                T = numerator // R
                k_num = p ** (1 - epsilon) * T + 1
                require(k_num % 4 == 0, "K integrality failed")
                K = k_num // 4
                y = (p * a + (p * p // p**epsilon) * u) // R
                z = (p * a + p**epsilon * v) // R
                require(Fraction(4, p) == Fraction(1, a) + Fraction(1, y) + Fraction(1, z), "selector identity failed")
                unordered.add(tuple(sorted((a, y, z))))
                if channel == "E":
                    exterior += 1
                else:
                    middle += 1
    return {
        "exterior": exterior,
        "middle": middle,
        "oriented": exterior + middle,
        "unordered": len(unordered),
    }


def matrix_rank(rows: list[tuple[int, ...]]) -> int:
    """Rank over Q, with no floating-point arithmetic."""
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    nrows = len(a)
    ncols = len(a[0])
    require(all(len(row) == ncols for row in a), "ragged matrix")
    pivot_row = 0
    for col in range(ncols):
        pivot = next((i for i in range(pivot_row, nrows) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for i in range(nrows):
            if i == pivot_row or not a[i][col]:
                continue
            c = a[i][col]
            a[i] = [x - c * y for x, y in zip(a[i], a[pivot_row], strict=True)]
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def jordan_product_sym2(x: tuple[int, int, int], y: tuple[int, int, int]) -> tuple[Fraction, Fraction, Fraction]:
    """Coordinates (11,12,22) of (XY+YX)/2 for real symmetric 2x2 matrices."""
    u, a, v = map(Fraction, x)
    U, A, V = map(Fraction, y)
    return (
        u * U + a * A,
        (u * A + a * V + U * a + A * v) / 2,
        a * A + v * V,
    )


raw = json.loads(INPUT.read_text(encoding="utf-8"))
require(raw["status"] == "PASS", "input census is not marked PASS")
states = raw["states"]
require(len(states) == 15, "expected fifteen marked states")

records: list[dict[str, object]] = []
vectors3: list[tuple[int, int, int]] = []
vectors15: list[tuple[int, ...]] = []
projective: list[tuple[int, int, int]] = []

for state in states:
    h = int(state["h0"])
    r = int(state["r"])
    s = int(state["t"])
    u, a, v = h * r * r, h * r * s, h * s * s
    require(u * v == a * a, f"rank-one determinant failed for {state['tag']}")
    require(gcd(r, s) == 1, f"nonprimitive ray for {state['tag']}")
    primitive = (r * r, r * s, s * s)
    require(integer_gcd(primitive) == 1, f"projective vector not primitive for {state['tag']}")

    # Coordinate order for Herm_3(H): three real diagonal entries followed by
    # the four real components of q12, q13, q23.  The selector corner has only
    # d1=u, d2=v, and Re(q12)=a nonzero.
    embedded = (u, v, 0, a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    vectors3.append((u, a, v))
    vectors15.append(embedded)
    projective.append(primitive)
    records.append(
        {
            "tag": state["tag"],
            "channel": state["channel"],
            "R": state["R"],
            "h": h,
            "r": r,
            "s": s,
            "Gamma_coordinates_u_a_v": [u, a, v],
            "primitive_projective_ray": list(primitive),
            "Herm3H_coordinates": list(embedded),
        }
    )

require(len(set(projective)) == 15, "the fifteen projective rays are not distinct")
rank3 = matrix_rank(vectors3)
rank15 = matrix_rank(vectors15)
require(rank3 == 3, f"unexpected Sym_2 span rank {rank3}")
require(rank15 == 3, f"unexpected Herm_3(H) span rank {rank15}")

# The real upper-left Sym_2 corner is a Jordan subalgebra.  Exact products of
# every pair have no coordinate outside that corner.  Since the original
# vectors already span all of Sym_2(R), adjoining all Jordan products cannot
# enlarge the generated linear Jordan subalgebra.
products = [jordan_product_sym2(x, y) for x in vectors3 for y in vectors3]
product_rows = [tuple(int(z) if z.denominator == 1 else z for z in p) for p in products]
closure_rank = matrix_rank(vectors3 + product_rows)  # type: ignore[arg-type]
require(closure_rank == 3, f"unexpected Jordan closure rank {closure_rank}")

# Quotients already present in the source data change the count while leaving
# the 15-dimensional target algebra unchanged.
require(raw["canonical_unordered_base_triples"] == 11, "unexpected unordered count")
require(raw["distinct_hard_preserving_prime_progressions"] == 10, "unexpected progression count")

# The number fifteen is not stable even inside the same hard residue class
# p == 361 (mod 840).  These small exact enumerations provide direct
# counterexamples to treating it as an intrinsic dimension.
same_hard_class_counts = {
    str(p): complete_selector_counts(p) for p in (1201, 4561, 8761, 9601)
}
require(
    [same_hard_class_counts[str(p)]["oriented"] for p in (1201, 4561, 8761, 9601)]
    == [15, 54, 36, 29],
    "unexpected complete-selector count in the fixed hard class",
)

result = {
    "schema": "p1201-natural-selector-jordan-span-v1",
    "input": str(INPUT),
    "input_sha256": sha256(INPUT.read_bytes()).hexdigest(),
    "marked_oriented_states": 15,
    "distinct_projective_selector_rays": len(set(projective)),
    "canonical_unordered_triples": 11,
    "distinct_hard_preserving_prime_progressions": 10,
    "same_hard_residue_class_mod_840_counts": same_hard_class_counts,
    "natural_map": "(h,r,s) -> h[[r^2,rs],[rs,s^2]] -> upper-left real Sym_2 corner of Herm_3(H)",
    "rank_of_selector_images_in_Sym2R": rank3,
    "rank_of_selector_images_in_Herm3H": rank15,
    "rank_of_linear_Jordan_closure": closure_rank,
    "ambient_dimensions": {
        "Sym2R": 3,
        "Herm3H": 15,
        "projectivized_rank_one_Sym2R_conic": 1,
        "positive_rank_one_Sym2R_cone": 2,
    },
    "conclusion": (
        "The natural exact bridge produces fifteen distinct rational rays on one Veronese conic "
        "inside a three-dimensional Jordan corner.  It does not identify them with fifteen "
        "independent coordinate directions of Herm_3(H)."
    ),
    "states": records,
}

encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
OUTPUT.write_text(encoded, encoding="utf-8", newline="\n")
print("PASS")
print(f"input_sha256={result['input_sha256']}")
print(f"distinct_projective_rays={len(set(projective))}")
print(f"linear_span_rank={rank15}")
print(f"jordan_closure_rank={closure_rank}")
print(f"output_sha256={sha256(encoded.encode('utf-8')).hexdigest()}")

