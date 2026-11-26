"""Prepare exact local KX receiver guards and proposed check records.

Reads only individually released KX blocks and this lane's evidence.
Does not read or write the canonical source or any global record.
Run before admission only.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_initial"
STEM = "S6_SERIES_PUBLISH_III_02KX_"
SID = "maps:src:D.2.22"

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

frozen = {
    LANE/(STEM+"fresh_derivation.md"):
        "69d4882771ff170cd96de4525cb85b96cb5235c1b23f865308d2425052fb399b",
    LANE/(STEM+"fresh_necessity_aux.md"):
        "cdbf00f9d3794cd34bd86f8103e32b379081b6d9529db92263ab40a1b922a34c",
    LANE/(STEM+"primary_reading.md"):
        "271a103d740fae64facd34f65258082e8a220f5cd8e698730e88dded930a7cf0",
    LANE/(STEM+"fresh_vertical_data.json"):
        "12c391234cf864decec6457019180e20c510ff76e5ffd2f6ea79a42dcce71b8c",
    ROOT/"code/S6_SERIES_PUBLISH_c7_kx_vertical.py":
        "8910104e8118887fa392b7c2c8eebc89fbdc278a6a0412861686933a3ed3056f",
    ROOT/"code/S6_SERIES_PUBLISH_c7_kx_vertical.out":
        "97d1adf685350f445686dd53e8f15dde99354386bca9ee093832ef3eb93f6331",
}
for path, expected in frozen.items():
    assert sha(path) == expected, path

def block(text, env):
    begin = r"\begin{" + env + "}"
    end = r"\end{" + env + "}"
    assert text.count(begin) == text.count(end) == 1
    start = text.index(begin)
    return text[start:text.index(end, start)+len(end)]

old_statement = block((LANE/(STEM+"released_statement.tex")).read_text(), "theorem")
old_proof = block((LANE/(STEM+"released_proof.tex")).read_text(), "proof")
assert hashlib.sha256(old_proof.encode()).hexdigest() == (
    "5814bb9426e7a0e0fca647dea01be7f0f5271d3416bfc506194447d7746555df")
receiver = (LANE/(STEM+"receiving.tex")).read_text()
new_statement = block(receiver, "theorem")
new_proof = block(receiver, "proof")
old_combined = old_statement + "\n\n" + old_proof
new_combined = new_statement + "\n\n" + new_proof
assert receiver.rstrip("\n") == new_combined

for kind in ("label", "hypertarget", "tag"):
    pattern = re.compile(r"\\"+kind+r"\{([^{}]+)\}")
    old_ids = Counter(pattern.findall(old_combined))
    new_ids = Counter(pattern.findall(new_combined))
    assert old_ids == new_ids, (kind, old_ids, new_ids)
    print(kind, dict(new_ids))
assert len(re.findall(r"\\label\{", receiver)) == 6
assert len(re.findall(r"\\hypertarget\{", receiver)) == 6
assert len(re.findall(r"\\tag\{", receiver)) == 5
assert r"\textnormal{\small tag02KX.}" in new_statement
for forbidden in (r"\StatementRecord", r"\SeriesRef", "records/",
                  ".json", "code/", "SHA256", "the program"):
    assert forbidden not in receiver, forbidden

# Structural checks are not a TeX compilation or rendered-page review.
stack = []
for match in re.finditer(r"\\(begin|end)\{([^{}]+)\}", receiver):
    action, env = match.groups()
    if action == "begin":
        stack.append(env)
    else:
        assert stack and stack.pop() == env, match.group()
assert not stack
depth = 0
for char in re.sub(r"\\[{}]", "", receiver):
    if char == "{":
        depth += 1
    elif char == "}":
        depth -= 1
        assert depth >= 0
assert depth == 0
for left, right in ((r"\(", r"\)"), (r"\[", r"\]")):
    assert receiver.count(left) == receiver.count(right)

def write_tsv(name, fields, rows):
    path = LANE/(STEM+name+".tsv")
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t",
                                lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return path

reason = (
    "Complete fresh derivation accepted before individual original release; "
    "all theorem clauses and thirteen proof items compared. Preserve all "
    "permanent identities; give full component/line/translation maps, "
    "cap specialization and rank argument, complete finite tables, "
    "integral solutions and invariant freedom; remove historical "
    "execution and machine-header claims.")
guards = [
    dict(statement_id=SID, old_text=old_statement, new_text=new_statement,
         reason=reason),
    dict(statement_id=SID, old_text=old_proof, new_text=new_proof,
         reason=reason),
]
guard_path = write_tsv("replacements",
    ["statement_id", "old_text", "new_text", "reason"], guards)
replay = old_combined
for row in guards:
    assert replay.count(row["old_text"]) == 1
    replay = replay.replace(row["old_text"], row["new_text"], 1)
assert replay == new_combined
with guard_path.open(newline="") as handle:
    reread = list(csv.DictReader(handle, delimiter="\t"))
assert reread == guards
print("exact_guards", "two separate complete blocks; local replay PASS")

def excerpt(text, start, finish):
    i = text.index(start)
    j = text.index(finish, i)+len(finish)
    return text[i:j]

def defect(suffix, kind, location, old, new, explanation, identity=SID):
    return dict(
        change_id="c7-III-02KX-"+suffix, type=kind,
        statement_id=identity, old_location=location, old_page="",
        new_location=str((LANE/(STEM+"receiving.tex")).relative_to(ROOT)),
        new_page="", old_text=old, new_text=new, reason=explanation,
        review_status="whole comparison submitted to root; admission pending")

defects = [
    defect("machine-header", "D10", "S6_SERIES_PUBLISH_III.tex; "+SID,
        next(line for line in old_statement.splitlines()
             if line.startswith(r"\StatementRecord")),
        r"\textnormal{\small tag02KX.}",
        "Remove the production header and retain all labels, targets and the small printed theorem tag."),
    defect("complete-mathematical-catalogue", "D09",
        "S6_SERIES_PUBLISH_III.tex; "+SID,
        r"\texttt{records/manifolds\_sphere\_natural.json}.",
        excerpt(new_proof, r"\item \emph{The complete marked counts.}",
                "This proves both counts and the stated marking conventions."),
        "Replace the external historical file pointer by complete natural ordered-pair and marked-position tables, the positive factor-divisor rule, and explicit integral solutions."),
    defect("historical-computation", "D09",
        "S6_SERIES_PUBLISH_III.tex:12107--12241",
        excerpt(old_proof, "The exact twenty-one canonical blocks saved",
                "change the conclusion."),
        excerpt(new_proof, "For the twenty-one marked tuples",
                "their common degree-one coinvariant has dimension one."),
        "Historical code/output remain unopened. New raw-fixture rank minors and inverses, literal symbolic Omega identity, profile Euler/root sums and the separately frozen 226-row potential computation verify the mathematical assertions. The receiver states the formulas and finite data, not historical execution."),
    defect("procedural-contrast", "D02",
        "S6_SERIES_PUBLISH_III.tex:12029--12030",
        excerpt(old_proof, "This proves the local equality directly",
                "the line."),
        "",
        "The extending frame, inverse arrow, reciprocal unit and transported fan are stated as the mathematical proof; remove the procedural comparison."),
    defect("scope-prose", "D11",
        "S6_SERIES_PUBLISH_III.tex; "+SID,
        excerpt(old_statement, "This is a finite list of possible initial data",
                "its filling choices are spheres."),
        "Subsequent filling choices\nretain their logarithmic and gluing parameters.",
        "Express the initial-data scope once positively, preserving every filling parameter."),
    defect("signed-period-fan-map", "D22",
        "S6_SERIES_PUBLISH_III.tex:12018--12022",
        excerpt(old_proof, "The actual valuation", "is therefore $|nw-AB|$."),
        excerpt(new_proof, "The elliptic deck map",
                "Thus the period index is \\(|nw-AB|\\)."),
        "Supply the coordinate inversion and inverse, reciprocal vertical units and reflected fan. The original determinant and Euler conclusions stand.",
        "maps:eq:D.FI2"),
    defect("minimal-cap-specialization", "D22",
        "S6_SERIES_PUBLISH_III.tex:12070--12072",
        excerpt(old_proof, "Pull back the four independent specialization classes",
                "space, of dimension four; hence it again gives surjectivity."),
        excerpt(new_proof, "For the minimal quotient",
                "Dualizing gives the four specialization classes."),
        "The admitted KB conductor homology does not explicitly provide this restriction map. Add normal-disc PL and the two angular sweep maps, their complementary Wang projection and the inverse obtained by subtracting sweeps; then apply the genuine period cover."),
    defect("original-cap-and-vertical-rank", "D22",
        "S6_SERIES_PUBLISH_III.tex:12078--12096",
        excerpt(old_proof, "There is a separate check for an original cap;",
                "by averaging, which is legitimate over $\\mathbb Q$."),
        excerpt(new_proof, r"\item \emph{The original caps and their component degrees.}",
                "is onto in every one-orbit case."),
        "Supply the same-germ contraction and roof inverse, normalized-component flat line, Gysin and PL maps, and the component-preserving norm proving f=2/3 also for arbitrary integral V. No original mathematical conclusion is refuted."),
    defect("integral-solutions-and-translation", "D22",
        "S6_SERIES_PUBLISH_III.tex:12208--12241",
        excerpt(old_proof, "The broader count normalizes",
                "the different marking convention in the two counts."),
        excerpt(new_proof, r"\item \emph{Translation of the zero and complete solution freedom.}",
                "included in this description."),
        "Give the exact simultaneous translation, F_R line map and reciprocal, induced vertical and base factors, transported multiplier/fan/collar and full invariant-lattice inverse. Integral potentials display every nonzero local solution, with actual global line existence."),
    defect("primary-locators", "D18",
        "S6_SERIES_PUBLISH_III.tex:12167",
        r"\cite[Theorem 6.3 and Corollary 6.13]{manSS10}",
        r"\cite[Theorem 6.3, p.~23; Corollary 6.13,"+"\n"+
        r"pp.~29--30; Section 8.3, p.~39]{manSS10}",
        "Give exact locators in the read arXiv:0907.0298v3 source. The post-exposure record distinguishes text from visual reads and excludes the unused anticanonical-ampleness sentence; the application uses rational chi(O)=1 and e=12."),
]
defect_path = write_tsv("defects",
    ["change_id", "type", "statement_id", "old_location", "old_page",
     "new_location", "new_page", "old_text", "new_text", "reason",
     "review_status"], defects)

timestamp = datetime.now(timezone.utc).isoformat()
who = ("GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately "
       "exposed; seventh publication continuation")
outcome = (
    "The theorem and every mathematical auxiliary conclusion stand. "
    "Complete fresh derivation frozen 21:50:07 UTC, SHA "
    "69d4882771ff170cd96de4525cb85b96cb5235c1b23f865308d2425052fb399b, "
    "root-reviewed before individual release 21:52:43.731624 UTC. "
    "The admitted KY natural criterion/count exposure was disclosed; "
    "necessity, 172 natural and 226 enlarged marked data, every integral V, "
    "global line existence and exact Q-invariant freedom were rederived "
    "from raw marked A_i,g_i and new potential/orbit arithmetic. All 226 rows, "
    "potentials and ten nonzero local cases were read. The entire released "
    "statement and all thirteen original proof items were then compared. "
    "Post-exposure work supplies theta/unit/inverse-arrow/reflected-fan maps, "
    "all local cap restriction maps, the two normal sweeps proving the four "
    "minimal specialization classes, same-germ original-cap flat-line/Gysin/PL "
    "maps, arbitrary-V unit-norm central-entry check, global graph/MV rank "
    "budget D.FI4, and exact zero-component translation including all line "
    "and base factors. The new auxiliary program and full output verify "
    "all 21 rank minors/inverses, literal unrestricted Omega identity, "
    "all profile Euler/root counts and 8502 signed examples; universal "
    "claims have proofs and are not extrapolated from examples. "
    "The complete receiver was read and all six label/target pairs and "
    "five equation tags are preserved by two separate exact guards. "
    "SS primary scopes and KB/L1 dependency scopes are recorded; p.25 was "
    "visually read before exposure, additional SS pages were text-read. "
    "SS's Section 8.3 anticanonical-ampleness sentence is unused; rational "
    "chi(O)=1 and the Euler formula give 12. Frozen fresh hashes unchanged. "
    "Historical programs/results and root's held candidate program remain "
    "unopened and uncredited. No D25/D26/D27 is alleged. This is one targeted "
    "event, with no extra blind or independent-family credit for "
    "post-exposure work or coordination. No canonical/global edit, "
    "isolated/canonical build, whole-PDF reading, page review, unit closure "
    "or paper-gate credit is claimed; root admission pending.")
evidence = [
    *[str(p.relative_to(ROOT)) for p in frozen],
    str((LANE/(STEM+"released_statement.tex")).relative_to(ROOT)),
    str((LANE/(STEM+"released_proof.tex")).relative_to(ROOT)),
    str((LANE/(STEM+"post_exposure_derivation.md")).relative_to(ROOT)),
    str((LANE/(STEM+"comparison.md")).relative_to(ROOT)),
    str((LANE/(STEM+"receiving.tex")).relative_to(ROOT)),
    str(guard_path.relative_to(ROOT)),
    str(defect_path.relative_to(ROOT)),
    "code/S6_SERIES_PUBLISH_c7_kx_auxiliary.py",
    "code/S6_SERIES_PUBLISH_c7_kx_auxiliary.out",
    "code/S6_SERIES_PUBLISH_c7_kx_records.py",
    "code/S6_SERIES_PUBLISH_c7_kx_records.out",
]
event_id = "publish:c7:III:02KX:targeted"
event = dict(
    statement_id=SID, date=timestamp[:10], who=who,
    type="targeted proof check", outcome=outcome, event_id=event_id,
    phase="complete blind derivation, individual release, full original and receiving comparison",
    source_file="S6_SERIES_PUBLISH_III.tex", source_row="11974",
    source_event_type="targeted proof check", evidence_group=event_id,
    publish_input_file=str((LANE/(STEM+"CHECK_EVENTS.tsv")).relative_to(ROOT)),
    publish_input_row="2", date_utc=timestamp, where="; ".join(evidence))
event_path = write_tsv("CHECK_EVENTS",
    ["statement_id", "date", "who", "type", "outcome", "event_id", "phase",
     "source_file", "source_row", "source_event_type", "evidence_group",
     "publish_input_file", "publish_input_row", "date_utc", "where"], [event])

for path, count in ((defect_path, 10), (event_path, 1)):
    with path.open(newline="") as handle:
        assert len(list(csv.DictReader(handle, delimiter="\t"))) == count
print("record_timestamp_utc", timestamp)
print("defect_rows", len(defects), "targeted_events", 1)
print("receiver_lines", len(receiver.splitlines()))
for path in [LANE/(STEM+"receiving.tex"),
             LANE/(STEM+"post_exposure_derivation.md"),
             LANE/(STEM+"comparison.md"), guard_path, defect_path, event_path,
             ROOT/"code/S6_SERIES_PUBLISH_c7_kx_auxiliary.py",
             ROOT/"code/S6_SERIES_PUBLISH_c7_kx_auxiliary.out",
             Path(__file__)]:
    print("sha256", sha(path), str(path.relative_to(ROOT)))
print("PASS: frozen fresh bytes; exact original proof; complete identities; "
      "two separate guards; local replay; receiver structure; ten defect "
      "proposals; one targeted event. No canonical/global files touched.")
