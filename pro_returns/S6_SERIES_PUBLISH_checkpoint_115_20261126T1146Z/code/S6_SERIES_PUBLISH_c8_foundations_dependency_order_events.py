"""Append the actual read-only construction-order findings and exposed-use events.

No manuscript, shared table, inventory, or criterion is written.
"""
from datetime import datetime, timezone
import csv
import io
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation8_iii_foundations"
REVIEW = LANE / "S6_SERIES_PUBLISH_c8_foundations_unit_reviews.md"
EVENTS = LANE / "S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv"
WHO = "GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed."
WHEN = datetime.now(timezone.utc).isoformat()
HEADING = "## Read-only construction-order follow-up"

NOTE = r"""

## Read-only construction-order follow-up

Attribution: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed.

The current Paper III body and all current editable body fragments were inspected for forward construction inputs using their actual labels and fragment ownership. Frontmatter, preamble and bibliography were excluded. The source pass covered `ref`, `eqref`, `cref`, `Cref`, `SeriesRef`, labelled `hyperref`, `hyperlink` and range references, then read the candidate clauses and their cited inputs. It also examined cross-subsection references inside an aggregate fragment and the source passages using “below”, “later” and related wording. The searches were temporary source queries; no dependency inventory was saved. One early text search was interrupted because it recomputed line bounds at every line; the corrected source query completed. That interrupted query supplies no finding or credit.

### Concrete late input, already accepted by root

The current edited `root/full_sphere_nullity.tex` directly requires `root/cusp_nullbordism.tex`. Definition Q256 (`wb:def:native-sphere-carriers`) takes the original cusp, quotient marking, skeleton collapse, native map and the exact inverse coordinate maps from Q258 (`wb:def:marked-cusp-nullbordism-data`). Proposition 038X (`wb:cusp-s12-one-copy-invariant`) uses the particular embedded three-torus and bounding derivative framing of 038S (`wb:cusp-null:thm`) to construct its two maps with coefficients zero and one. Its native coefficient-zero assertion also uses that theorem. Remark Q257 (`wb:remark:two-cusp-postcompositions`) uses the same actual frame and extended cap frame, through `wb:cusp-null:eq:actual-frame` and `wb:cusp-null:eq:extended-frame`.

Both complete current root fragments were read for this order. Q258 supplies beta and its inverse, the cube target map phi and its inverse, and d and its inverse before the nullbordism. The proof of 038S uses Q011 for the marked cusp, Q253 for ordered cube spheres, Q255 for relative smoothing, 03AE for the injective chart, and 02Q7 for the one-copy based null-homotopy. Those inputs are earlier than the late carrier group. Corollary 03A6 (`wb:cusp_s12_carrier_homotopy:L567`) defines its own map delta:[a]12 -> 2a nu9 and its inverse, proves their inverse identities, and applies delta inverse to the already zero suspension. It has no reverse dependency on the later coefficient proposition 038X.

The accepted order is therefore carriers, then `cusp_nullbordism`, then `full_sphere_nullity` and its comparison, then metrics. Root confirmed that this move was already planned. The current canonical text still had the opposite order when inspected; root owns the guarded move and its exact defect record. This follow-up adds no separate source application.

### Forward citations that supply comparisons

In Q021 (`mapsIII:def:retained-angle-cusp-data`), the displayed deck action changes A(t) inverse times log absolute x by the integral long-period vector. The preceding invertibility estimate and the real period decomposition prove the quotient formula locally. The later citation to 0370 (`wb:cusp-cone-native-descent`) is corroborative. The entire current 0370 statement and proof were read: its flat-marking quotient is [s,Pi(s)x] -> (t,[p x]), with the logarithm/exponentiation inverses, p M0 = p, the connected kernel and the radial marking inverse all printed. Its long-period coordinate is the same u in the earlier displayed decomposition. That citation does not require moving the later construction before the retained-angle proof.

Q137 (`mapsIII:rem:weighted-profile-calculations`) and Q139 (`mapsIII:rem:odd-weighted-calculations`) cite LI (`maps:src:D.2.41`) after their own proofs, describing the inclusion of their complete marked input sets into the later all-positive-weight algorithm. The clauses retain the same ordered initial row, weight, cap choices, affine powers and clutch, with the inverse on the image reading the same tuple. The current LI statement and complete proof were reread. Its actual geometric local inputs are the earlier LH cap maps, with their explicit roof-coordinate inverses and cover/transfer maps; its full bar-chain and five-column construction is then proved locally. These two closing citations do not create a prerequisite from LD or LH to LI.

The “core cofiber splitting constructed below” clause in J9 is supplied inside that same proof by kappa, its mapping-cone maps and the displayed inverse equivalences Phi and J. The “model defined below” clause in the all-multiplicative smooth recognition argument is supplied later in that same proof. The final open-problem references describe later open questions. They do not identify an additional cross-unit construction move.

### Disposition

No additional cross-unit forward construction dependency or shared-owner repair was identified beyond root's known late move, retained-angle-before-JA correction, local-Kummer-before-cyclic placement and early generic Q311/QC owners. The remaining labelled forward candidates are the comparisons just described. This is a source-reference-order finding with the actual read scopes above; it does not replace any remaining rendered-page, bibliography, primary-source or build review. No canonical or shared file was changed, and no criterion was closed.

The appended exposed-use events are limited to the actual source-input/coordinate readings used for this finding. Their type is “used and rechecked in this run”; there is no independent-check, new arithmetic execution or historical execution attribution.
"""

READINGS = [
    ("Q258", "wb:def:marked-cusp-nullbordism-data", "Read the whole current marked-cusp definition for the construction order. Its beta, skeleton quotient, phi, d, native g and each displayed inverse are supplied within this earlier owner; its cube-sphere input is Q253. This establishes the exact source data consumed by Q256, with no new independent or arithmetic credit."),
    ("038S", "wb:cusp-null:thm", "Read the whole current nullbordism statement and sole proof for its use in the later framing comparison. The required inputs are the earlier Q011 marked cusp, 03AE injective chart, Q255 based smoothing and 02Q7 null-homotopy. The specific torus, actual frame N J H inverse, frame homotopy, collared cap and extended frame are the inputs consumed by 038X and Q257. This is exposed source-order rereading."),
    ("03A6", "wb:cusp_s12_carrier_homotopy:L567", "Read the full current corollary and proof to check the apparent reverse dependency. The even-coordinate isomorphism delta and its inverse are defined and verified locally, and the based suspension homotopies carry the already zero class. Thus this proof uses 038S and Q258 without taking the later coefficient proposition 038X as an input. No independent-check credit."),
    ("Q256", "wb:def:native-sphere-carriers", "Read the complete current native-carrier definition. It expressly takes Q258's marked cusp, skeleton, map g and inverse d/phi coordinates, then defines the actual q2, p, P and Q with the same collapsed ends. This is the direct construction edge requiring Q258 before this definition; the current block is not yet applied by this agent."),
    ("038X", "wb:cusp-s12-one-copy-invariant", "Read the whole current coefficient/framed-fibre proposition and sole proof. Its coefficient-zero conclusion and F0/F1 construction consume 038S's particular embedded torus and bounding derivative frame; the target coordinate and tubular maps, J comparison, inverse unit degree and resulting framing change are explicit. This confirms an actual forward construction input in the former order, resolved by root's planned nullbordism-first placement; no independent or new computation credit."),
    ("Q257", "wb:remark:two-cusp-postcompositions", "Read the entire current numbered postcomposition comparison, including the literal p3 and p-hat-2 formulas, the inclusion M into N, both normal-frame inputs and the ordered Hopf-smash maps. It consumes the earlier retained-angle result and 038S's actual/extended three-frame. The accepted late order supplies both inputs before this remark; no new independent mathematical claim is assigned."),
    ("0370", "wb:cusp-cone-native-descent", "Read the entire current native-descent statement and proof to assess Q021's later citation. The exponentiation/logarithm maps identify the marked quotient, p M0 = p gives descent, and [s,Pi(s)x] maps to (t,[p x]); the radial isometry has the printed YT inverse. Q021 already derives its same long-period quotient from its own deck action and real period decomposition, so this use is corroborative and causes no required source move. No primary-source reopening or independent credit."),
    ("02LI", "maps:src:D.2.41", "Reread the current all-weight statement and complete bar-coordinate proof for the Q137/Q139 order question. Its earlier inputs are the LH local cap/roof maps, full saturated kernels and LD marked data; the proof supplies its own bar inverse, ordered suffix maps, five normal columns and complete integer gluing. The two earlier closing remarks only include their same marked input tuples into this later algorithm. No arithmetic program was run and no fresh independent event is inferred."),
]

review_bytes = REVIEW.read_bytes()
if HEADING.encode() in review_bytes:
    raise RuntimeError("The actual follow-up has already been recorded")
event_bytes = EVENTS.read_bytes()
reader = csv.DictReader(io.StringIO(event_bytes.decode()), delimiter="\t")
fields = reader.fieldnames
old_ids = {row["event_id"] for row in reader}
note_line = review_bytes.count(b"\n") + 3
buffer = io.StringIO(newline="")
writer = csv.DictWriter(buffer, fieldnames=fields, delimiter="\t", lineterminator="\n")
for tag, label, outcome in READINGS:
    identifier = f"ce:III:c8:dependency-order:{tag}:exposed-use"
    if identifier in old_ids:
        raise RuntimeError(f"Existing event: {identifier}")
    row = {key: "" for key in fields}
    row.update(statement_id=label, date=WHEN[:10], who=WHO,
               type="used and rechecked in this run", outcome=outcome,
               event_id=identifier, phase="current",
               source_file=str(REVIEW.relative_to(ROOT)), source_row=str(note_line),
               source_event_type="used and rechecked in this run",
               evidence_group="III-C8-CONSTRUCTION-ORDER-EXPOSED-READING",
               date_utc=WHEN, where=str(REVIEW.relative_to(ROOT)))
    writer.writerow(row)

def atomic(path, data):
    temporary = path.with_name(path.name + ".c8-order.tmp")
    temporary.write_bytes(data)
    temporary.replace(path)

assert event_bytes.endswith(b"\n")
atomic(REVIEW, review_bytes + NOTE.encode())
atomic(EVENTS, event_bytes + buffer.getvalue().encode())
print("Appended substantive source-order findings at review line", note_line)
print("Exposed-use events:", len(READINGS))
for tag, label, outcome in READINGS:
    print(tag, label)
    print(outcome)
print("Canonical/shared writes: 0. Criteria closed: 0. Independent events: 0.")
