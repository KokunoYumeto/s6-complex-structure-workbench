"""Record the root's full E108--109 review and exact relative ledger.

The geometric statements in `reviewed` record a completed human-readable
proof review. The arithmetic below is a separate exact reproducible check;
it does not stand in for the source, line, cap, or boundary morphisms.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "notes/part3_e6_order_three_source_working.md"
EXPECTED = "d7180ab4503249c18237299d164817abdd70174c58bae394959c95850e99ec33"
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
assert sha(SOURCE) == EXPECTED
text = SOURCE.read_text()
sections = {}
for start, end in [("## E87", "## E88"), ("## E102", "## E103"),
                   ("## E104", "## E108"), ("## E108", None)]:
    chunk = text[text.index(start):text.index(end) if end else len(text)]
    sections[start] = hashlib.sha256(chunk.encode()).hexdigest()

I = ((-2, 1, 1), (1, -2, 1), (1, 1, -2))
D, fibre = (3, 2, 4), (1, 1, 1)
def pair(a, b):
    return sum(a[i] * I[i][j] * b[j] for i in range(3) for j in range(3))
assert pair(D, D) == -6
assert pair(D, fibre) == pair(fibre, fibre) == 0
compact_rows = [(-F(1895, 18), -F(50, 3)),
                (F(1121, 18), F(596, 3)), (-1, -31), (-1, -31)]
compact = tuple(sum(row[j] for row in compact_rows) for j in range(2))
assert compact == (-45, 120)
normal_squares = (6, -6, 6)
tangent = 3 * 3 * (-3)
lower = (normal_squares[0] + normal_squares[2] - normal_squares[1],
         tangent + normal_squares[0] + 2 * normal_squares[1] + normal_squares[2])
assert lower == (18, -27)
inner = tuple(compact[j] + 4 * lower[j] for j in range(2))
assert inner == (27, 12)
# E109.4--5: the outer boundary sign and Stokes give this same
# pair in the positive-parameter convention. E109.5a is the actual
# line-preserving orientation-reversing diffeomorphism to Jin's convention.
jin = tuple(-v for v in inner)
index = (4 * jin[0] - jin[1]) / 24
assert jin == (-27, -12) and index == -4
dependencies = [
    "notes/part3_e6_order_three_lower_surfaces_working.md",
    "notes/part3_e6_order_three_lower_relative_working.md",
    "notes/part3_e6_order_three_fixed_surfaces_working.md",
    "notes/part3_e6_order_three_surface_aux_audit.md",
    "notes/part3_physical_line_corrigendum.tex",
    "records/blind_audit_e6_order_three_relative_double.json",
    "records/blind_audit_e6_order_three_outer_transfer.json",
    "code/part3/e6_order_three_relative_double.json",
]
record = {
    "reviewer": "root",
    "utc": datetime.now(timezone.utc).isoformat(),
    "status": "PASS_COMPLETE_INITIAL_FAN_OUTER_TRANSFER",
    "source": str(SOURCE.relative_to(ROOT)),
    "source_sha256": EXPECTED,
    "full_sections_read": sections,
    "dependencies": {p: sha(ROOT / p) for p in dependencies},
    "reviewed": [
        "E108 identifies the reference normal lines as the actual point line M6 and its inverse by the entire H=P^-6 U6^-1 Z^3 map, not by its uncorrected VC coefficient.",
        "The B^-j representative, complete c multiplier, h point-theta period P6, lambda qK P^-3 suspension, their inverses, and Fpt composed with H agree with LS.1--4 and E104--106.",
        "Actual I3 source H1, T3 boundary presentation, section-disc killing of alpha, and the literal eR=(t/eta)eL clutch give the primitive connecting class F. Full unit gauges are retained as integral multiples of F, annihilated in all required pairings by the displayed intersection matrix.",
        "The source flow is complex diagonal on the two nonzero-weight normal lines. Its invariant partition has no linear normal term, and s=UV has zero differential there. This fixes the normal-line gluing without an unstated U2 clutch.",
        "All four lower surfaces have the executed nine interior source blowups, identity boundary blowdown and unchanged normal rows. The integral exceptional basis and Jacobian divisor give tangent p1=-27 on each double.",
        "The compact subtotal includes all276 curves,117 surfaces and both separate ten-point blocks; root's independent117-surface auxiliary localization is retained.",
        "E109 retains all three native fundamental domains and determinants, full lower source contractions, finite support checks and bounded full units. Its proper total-line cut uses marked boundary source maps with their stated scope.",
        "The exterior source flow is prescribed on disjoint source, selected and root collars. The actual root/annular reference cochain, finite character, q2/h2 forward maps and inverse closings are carried pointwise.",
        "Both selected endpoint comparisons retain the same lambda^-2 factor. Their remaining full ratios extend through the source disc. The exact Cox maps, physical Hopf phase and positive-Hermitian ball map carry the same physical line and K68 inverse-clutch.",
        "The complex/circle-first outer boundary is -Y wedge dtheta. Finite-chart Stokes gives positive-parameter pair(27,12). The literal [y,t] to[y,1-t] and corresponding physical-line map respect both full endpoint relations and give Jin pair(-27,-12).",
        "E87's actual two-parameter family and all four edge maps extend over the interval-concatenation pair of pants. This subtracts the scalar reference exactly once, as an integral characteristic pair, and identifies the result with the fixed-scalar source loop.",
        "K68 PL.6 supplies the exact physical sphere gluing and index-to-Theta7 map. No integer has been chosen from a residue or from the earlier isolated charge-three chart."
    ],
    "arithmetic": {
        "compact_pair": [int(v) for v in compact],
        "lower_double_pair": list(lower),
        "inner_pair": [int(v) for v in inner],
        "Jin_pair": [int(v) for v in jin],
        "physical_index": int(index),
        "Theta7_residue": int(index) % 28
    },
    "scope": "The exact E87 fixed-scalar order-three source loop on its retained initial selected fan and quadratic cap. The formal statement must retain its complete source, norm, finite character and reference data.",
    "pending": "Standalone full proof export and typesetting; other-fan and higher-cap extensions are separate ongoing work."
}
out = ROOT / "records/root_audit_e6_order_three_outer_transfer.json"
out.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": record["status"], "audit": str(out.relative_to(ROOT)),
                  "Jin_pair": record["arithmetic"]["Jin_pair"],
                  "index": int(index), "residue": int(index) % 28}))
