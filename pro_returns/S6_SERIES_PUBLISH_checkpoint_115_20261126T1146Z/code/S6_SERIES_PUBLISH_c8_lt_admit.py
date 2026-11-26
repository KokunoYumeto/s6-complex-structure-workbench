"""Admit the wholly read LT comparison and prepare its exact source repairs."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import csv
import io
import re

ROOT = Path(__file__).resolve().parents[1]
OLD = ROOT / "agents/continuation7_iii_invariant_chern_receiving"
LANE = ROOT / "agents/continuation8_iii_lt"
LANE.mkdir(parents=True, exist_ok=True)
PREFIX = "S6_SERIES_PUBLISH_III_02LT_"
SID = "maps:src:D.2.51"
WHO = "GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed"
NOW = datetime.now(timezone.utc).isoformat()

def write(name, text):
    (LANE / name).write_text(text, encoding="utf-8", newline="\n")

def table(path, fields, rows):
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(out.getvalue(), encoding="utf-8", newline="\n")

receiver = (OLD / (PREFIX + "receiving.tex")).read_text()
assert sha256(receiver.encode()).hexdigest() == "36c6e6324085dcfa8aefdf47470aa4a260a378341490dd1a0104b131d819fff7"
old_initialization = r"""For any nonzero row $r=(r_1,\ldots,r_k)$, repeatedly combine its
current first entry $a$ and the next entry $b$. Choose integers
$s,t$ with $sa+tb=d=\gcd(a,b)>0$, and multiply those two columns
by"""
new_initialization = r"""For a nonzero row $r=(r_1,\ldots,r_k)$, first interchange the first
column and the least-indexed column with nonzero entry. The inverse is
the same transposition. Multiply the first column by the sign of its
entry; that diagonal sign map is also its own inverse. The first entry
is now positive. For $k=1$ these operations already give the required
matrix and its inverse. For $k\geq2$, successively combine the positive
first entry $a$ and each next entry $b$. Choose integers
$s,t$ with $sa+tb=d=\gcd(a,b)>0$, and multiply those two columns
by"""
assert receiver.count(old_initialization) == 1
receiver = receiver.replace(old_initialization, new_initialization)
old_completion = "A final sign change makes the first entry positive when required.\n"
assert receiver.count(old_completion) == 1
receiver = receiver.replace(old_completion, "The initial transposition and sign map are included in $V$ and $V^{-1}$.\n")
write(PREFIX + "receiving.tex", receiver)

def released_body(name):
    text = (OLD / (PREFIX + name)).read_text()
    return "\n".join(text.splitlines()[5:]) + "\n"

old_statement = released_body("released_statement.tex")
old_proof = released_body("released_proof.tex")
old_auxiliary = (OLD / (PREFIX + "released_following_auxiliary.tex")).read_text()
proof_start = receiver.index(r"\begin{proof}")
new_statement = receiver[:proof_start].rstrip() + "\n"
new_proof = receiver[proof_start:]
canonical = (ROOT / "S6_SERIES_PUBLISH_III.tex").read_text()
assert sha256(canonical.encode()).hexdigest() == "9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0"
for old in [old_statement, old_proof, old_auxiliary]:
    assert canonical.count(old) == 1, (len(old), canonical.count(old))
for pattern in [r"\\label\{([^}]+)\}", r"\\hypertarget\{([^}]+)\}"]:
    assert sorted(re.findall(pattern, old_statement + old_proof)) == sorted(re.findall(pattern, receiver)) or pattern.startswith(r"\\label"), pattern
old_labels = re.findall(r"\\label\{([^}]+)\}", old_statement + old_proof)
assert all(receiver.count(r"\label{" + label + "}") == 1 for label in old_labels)
assert receiver.count(r"\begin{theorem}") == 1
assert receiver.count(r"\begin{proof}") == 1
assert receiver.count(r"\end{proof}") == 1

replacements = [
    {"statement_id": SID, "old_text": old_statement, "new_text": new_statement,
     "reason": "Preserve all theorem conclusions and permanent identities; print the small tag, automatic equation numbers and positive marked-map scope."},
    {"statement_id": SID, "old_text": old_proof, "new_text": new_proof,
     "reason": "Replace the whole proof by the fully read exact cone, quotient, inverse, actual cap and boundary maps. Correct only the two D25 intermediate assertions and make the Euclidean initialization explicit."},
    {"statement_id": SID, "old_text": old_auxiliary, "new_text": "\n",
     "reason": "Move the complete historical computation provenance to the check record and the two printed program paths to the final programs table; retain every mathematical scope assertion in the theorem and proof."},
]
table(LANE / (PREFIX + "replacements.tsv"), ["statement_id", "old_text", "new_text", "reason"], replacements)

defect_fields = next(csv.reader((ROOT / "S6_SERIES_PUBLISH_defects_III.tsv").open(), delimiter="\t"))
defects = []
def defect(suffix, kind, location, old, new, reason):
    row = {k: "" for k in defect_fields}
    row.update(change_id="c8-III-02LT-" + suffix, type=kind, statement_id=SID,
               old_location=location, old_page="pending final page concordance",
               new_location="Theorem maps:src:D.2.51, sole receiving proof",
               new_page="pending final build", old_text=old, new_text=new,
               reason=reason, review_status="root whole proof comparison complete; canonical application and final page reading pending")
    defects.append(row)

defect("extension-splitting", "D25", "original proof item 4",
       "This proves the full nonsplit extension in $H_2$.",
       "The Gysin sequence has the section u -> [(su,0)]. The Wang sequence is 0 -> ker(d^t) + Z/(h/g) -> ker(d^t) + Z/h -> Z/g -> 0, with injection (u,a) -> (u,ga) and projection (u,b) -> b. Its explicit splitting exists exactly for gcd(g,h/g)=1.",
       "The original adjective fails at type III, Q=0, c=(2,-2), g=h=2. Exact quotient maps, inverses and an I1-star nonsplit example are proved. Every theorem group/image conclusion stands.")
defect("zero-chern-normal", "D25", "original proof item 10",
       "Its image in $H_2(U)$ is consequently torsion.",
       "The image lies in the scalar-long subgroup, Z/h for c nonzero and Zt for c=0. For type II, Q=0 and O(F), the canonical punctured line map I(p,w)=(p,u(p)w), inverse (p,W/u(p)), sends mu to mu_0+delta and the second normal to -t of infinite order.",
       "The exact meridian map and projection/point inclusion prove the zero-degree counterexample. Complete h=1 marked kernels and all theorem conclusions remain proved.")
defect("completion-initialization", "D22", "checkpoint91 staged receiver, integer completions paragraph",
       old_initialization,
       new_initialization,
       "An initial zero pair would leave the written gcd matrix undefined. The explicit first-nonzero transposition, sign map, singleton case and their inverses make every row length and zero-prefix case executable without changing the quotient theorem.")
defect("program-provenance", "D09", "original following auxiliary, source lines 21276-21291",
       old_auxiliary,
       "The complete scope, execution and exact coordinate comparison remain in the LT comparison/post-exposure note. The paper's final programs table will name code/III_invariant_chern_cone_fresh.py and code/outputs/III_invariant_chern_cone_fresh.json as plain paths.",
       "Program paths and check counts belong in the final programs table and records, while the mathematical cone derivation remains in the proof.")
defect("statement-header", "D10", "original theorem header",
       r"\StatementRecord{maps:src:D.2.51}{proved}{02LT}{\SeriesRef{maps:src:D.2.50}, \SeriesRef{maps:src:D.2.31}, \SeriesRef{maps:src:D.2.16}}",
       r"\textnormal{\small tag 02LT.}",
       "The permanent theorem label and hypertarget stay; the machine header is replaced by the prescribed small tag.")
defect("display-numbers", "D19", "original displays D.IC1-D.IC9",
       "Manual display numbers D.IC1-D.IC9.",
       "Automatic section equation numbering with every original equation label and hypertarget preserved.",
       "The old display labels stay available to all incoming references; the reader sees the paper's section numbering.")
table(LANE / (PREFIX + "defects.tsv"), defect_fields, defects)

review_path = "agents/continuation8_iii_lt/" + PREFIX + "root_admission_review.md"
review = f"""# 02LT — whole comparison and root admission

Admitted {NOW}. This is the supporting unit theorem maps:src:D.2.51;
it creates no required row among the 128 Paper III checks.

## Reading actually completed in continuation eight

Root read the entire checkpoint91 973-line receiver in consecutive
ranges 1-280, 281-560, 561-805 and 806-973; the entire 313-line
comparison; all 491 lines of the post-exposure note; and the full
released 112-line statement, 156-line proof and 16-line following
auxiliary. The five-line release headers were read with the statement
and proof. The receiver and original were compared clause by clause.
Root then wrote and read the explicit Euclidean initialization below.
No whole fresh-source rereading or new historical replay is claimed
for this continuation. Checkpoint91's completed fresh-proof and actual
source/output readings retain their recorded authorship and scopes.

The inherited pre-exposure proof froze at 2026-11-25T10:20:03+00:00,
SHA256 53b54211c8562b23795caf8e434dee89d6f8553bd31a2f7f200e9d1f5b303068,
and was root-read before the 10:29:02.864443 release. Its 1911 finite
cones supplement its all-integer quotient and inverse maps; their
scope is not enlarged here. The post-exposure replay and exact
historical-to-fresh maps were already completed and read at checkpoint91.

## Mathematical review

The roof reparametrization, lifted central retraction and two mapping-
torus homotopies retain the given line arrow. The clutch construction
gives exactly d2(x,t)=(c^t x,0), d3(u,y)=(A0 y,c^t y), d4(z)=(-A0 z,0).
The explicit orbit section s and partial-sum inverse K prove A0 K=I
on ker R. Phi[(x,t)]=(Rx,[t-c^t K(x-sRx)]_h) and
Psi(u,b)=[(su,b)] are inverse, with the stated integral boundary
preimage. At c=0 the second coordinate is an integer. The H1, H3,
H4 and fundamental-group maps are fully explicit.

The complex multiplicity cycle stays (mu,0); its scalar correction in
the split coordinates is computed explicitly. The seven weighted
diagrams and the marked component cocycle prove q_Q=gcd(l_j mu_j),
and k z integral is equivalent through B-I to k q in its image. The
actual narrow long cover proves the primitive free fibre row and
retains the scalar-long coordinate. The normal-disc construction,
integral clutch equation alpha=rz and scalar subtraction prove the
full boundary image and Wang-kernel surjectivity. For h=1 the explicit
chain Kx+(t-c^t Kx)eta bounds both literal normal images. The two star
degree vectors have the given component permutations and eta=-e4.

Original item 4's universally nonsplit adjective is refuted by
type III with Q=0 and c=(2,-2). The Gysin extension has its displayed
section, while the Wang extension splits exactly for gcd(g,h/g)=1.
The receiver supplies the precise two sequences, inverse maps and
both split and nonsplit geometric examples.

Original item 10's unqualified torsion inference fails at c=0.
For type II, Q=0 and O(F), I(p,w)=(p,u w) and I^-1(p,W)=(p,W/u)
send mu to mu_0+delta, so the second normal maps to -t. Projection
and point inclusion prove infinite order. All theorem conclusions,
including the c=0 image and h=1 marked kernels, remain proved.

The only new clarification is the Euclidean completion's first-
nonzero transposition and sign map, both with their inverses, and
the one-coordinate case. Every subsequent pair has positive first
entry, so its d is nonzero. The product V includes those initial
maps; the displayed L and L^-1 formulas remain valid. This resolves
a literal zero-prefix omission in the staged receiver without a
change to a mathematical conclusion.

## Records and publication scope

The final receiving file has {len(receiver.splitlines())} lines and
SHA256 {sha256(receiver.encode()).hexdigest()}.
Its three replacement rows retain the exact statement, proof and
following-auxiliary source guards. All permanent labels/hypertargets
are retained. Six local defect rows record both D25 repairs, the
completion clarification and the three presentation changes.
The three scoped events share one evidence group; no independent-
before-exposure credit is given to this continuation's readback.

The canonical manuscript is unchanged. Applying its repairs, the
publication units, apparatus, build and final page readings remain
open. LT is now an admitted support for the fresh LG synthesis.
"""
write(PREFIX + "root_admission_review.md", review)

with (ROOT / "CHECK_EVENTS.tsv").open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    event_fields, all_events = reader.fieldnames, list(reader)
events = []
def event(suffix, typ, outcome, who=WHO):
    row = {k: "" for k in event_fields}
    row.update(statement_id=SID, date="2026-11-25", who=who, type=typ,
               outcome=outcome, event_id="publish:c8:III:02LT:" + suffix,
               phase="continuation8-support-admission", source_file="S6_SERIES_PUBLISH_III.tex",
               source_row="21006", source_event_type=typ,
               evidence_group="publish:c7-c8:III:02LT",
               publish_input_file="agents/continuation8_iii_lt/" + PREFIX + "CHECK_EVENTS.tsv",
               publish_input_row=str(len(events) + 2), date_utc=NOW, where=review_path)
    events.append(row)

event("inherited-fresh-targeted", "targeted proof check",
      "Admit the prior continuation's completed pre-exposure derivation, frozen 2026-11-25T10:20:03+00:00 before the 10:29:02.864443 original release. Its recorded whole fresh proof, 1911 finite cone calculation and exact inverse maps prove the actual integral cone, all groups, literal scalar-long/area images, primitive fibre and full boundary image, and h=1 marked kernels. Checkpoint91's root fresh review supplies the actual pre-exposure reading chronology. The complete original comparison has now been root-read and settled. This event imports that completed work; it does not claim a new blind derivation in continuation eight. The h>1 individual marked torsion columns retain their stated cellular-representative scope.",
      "GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation seven fresh derivation, admitted in continuation eight")
event("two-intermediate-refutations", "refuted, with the refined statement's id",
      "Refined statement id: maps:src:D.2.51. Refute only original proof item4's universal nonsplit assertion and item10's zero-projection-implies-torsion assertion at c=0. The exact Wang extension has injection (u,a)->(u,ga), projection (u,b)->b mod g, and splits exactly when gcd(g,h/g)=1; typeIII,Q=0,c=(2,-2) gives a split counterexample. For typeII,Q=0,O(F), the punctured tensor map (p,w)->(p,u w), inverse division by u, sends mu to mu0+delta and the second normal to the primitive infinite class -t. All theorem conclusions remain proved, with the complete quotient/inverse and cap maps in the receiving proof. These are two bounded D25 intermediate repairs, with no D26/D27 statement refutation.")
event("whole-comparison", "used and rechecked in this run",
      "Root wholly read the checkpoint91 receiver, complete released statement/proof/following auxiliary, 313-line comparison and 491-line post-exposure note. Exact original and receiving clauses, both narrow D25 repairs and the zero-prefix/singleton initialization were checked. The actual historical replay and whole code/output readings remain those documented at checkpoint91; they were not rerun here. All labels and hypertargets are preserved in one theorem/one proof. Canonical source application, publication units, final build and page readings remain open; 02LT is supporting unit work outside the128 required identities.")
table(LANE / (PREFIX + "CHECK_EVENTS.tsv"), event_fields, events)
existing_ids = {r["event_id"] for r in all_events}
assert not any(r["event_id"] in existing_ids for r in events)
table(ROOT / "CHECK_EVENTS.tsv", event_fields, all_events + events)

ledger = ROOT / "PROGRESS_LEDGER.md"
with ledger.open("a", encoding="utf-8", newline="\n") as stream:
    stream.write(f"\n### Supporting comparison 02LT admitted — {NOW}\n\n")
    stream.write("Root whole reading is complete; the cone/group/image conclusions stand, with the two bounded intermediate repairs and explicit completion initialization in " + review_path + ". No required identity or publication-unit row is closed. The remaining LG support comparison is 02LV; the LG original remains closed.\n")
print("ADMITTED supporting theorem", SID, "at", NOW)
print("RECEIVER", len(receiver.splitlines()), "lines", sha256(receiver.encode()).hexdigest())
print("REPLACEMENTS", len(replacements), "DEFECTS", len(defects), "EVENTS", len(events))
print("All three original spans occur exactly once; original identities retained.")
print("Canonical source unchanged; no required or unit rows closed.")
