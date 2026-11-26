"""Admit the completed last Paper III check after root's whole comparison."""
from collections import Counter
import csv
from datetime import datetime, timezone
from hashlib import sha256
import io
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REL = Path("agents/continuation8_iii_lg_receiving")
LANE = ROOT / REL
PREFIX = "S6_SERIES_PUBLISH_III_02LG_"
NOW = datetime.now(timezone.utc).isoformat()
WHO = "GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed"
ALLOWED = {"targeted proof check", "independent re-proof",
           "computation or formal certificate", "used and rechecked in this run",
           "carried as background without fault found",
           "refuted, with the refined statement's id"}


def table(path):
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        return reader.fieldnames, list(reader)


def write_table(path, fields, rows):
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(buffer.getvalue(), encoding="utf-8", newline="\n")


receiver = (LANE / (PREFIX + "receiving.tex")).read_text(encoding="utf-8")
assert sha256(receiver.encode()).hexdigest() == "dcc39d05247e5a9e290c6ed46562393d87948cf42204d4b40f23c80b8e5ed69f"
assert len(receiver.splitlines()) == 109
assert receiver.count(r"\begin{problem}") == receiver.count(r"\end{problem}") == 1
assert r"\begin{proof}" not in receiver
assert r"\label{maps:src:D.2.4}" in receiver
assert r"\hypertarget{tag-02LG}" in receiver
original = (LANE / (PREFIX + "released_original.tex")).read_text(encoding="utf-8")
assert sha256(original.encode()).hexdigest() == "78bde0a45b4dd7f15b7d36ce092787c1c7144e231290f8018a0d5bd11e3dbbc0"
canonical = (ROOT / "S6_SERIES_PUBLISH_III.tex").read_text(encoding="utf-8")
assert sha256(canonical.encode()).hexdigest() == "9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0"
_, replacements = table(LANE / (PREFIX + "replacements.tsv"))
assert len(replacements) == 1
guard = replacements[0]
assert canonical.count(guard["old_text"]) == 1
assert guard["old_text"] == original and guard["new_text"] == receiver
applied = canonical.replace(original, receiver, 1)
assert applied.count(receiver) == 1 and applied.replace(receiver, original, 1) == canonical
for pattern in (r"\\label\{([^}]+)\}", r"\\hypertarget\{([^}]+)\}"):
    assert Counter(re.findall(pattern, original)) == Counter(re.findall(pattern, receiver))
_, defects = table(LANE / (PREFIX + "defects.tsv"))
assert any("D27" in r["type"] for r in defects)
assert any("D26" in r["type"] for r in defects)
fields, events = table(ROOT / "CHECK_EVENTS.tsv")
incoming_fields, incoming = table(LANE / (PREFIX + "CHECK_EVENTS.tsv"))
assert incoming and set(incoming_fields) <= set(fields)
assert all(r["type"] in ALLOWED and r["statement_id"] == "maps:src:D.2.4" for r in incoming)
assert all("Astra Pro" in r["who"] and "not separately exposed" in r["who"] for r in incoming)
existing_ids = {r["event_id"] for r in events}
assert not any(r["event_id"] in existing_ids for r in incoming)
progress_fields, progress = table(ROOT / "S6_SERIES_PUBLISH_required_progress_III.tsv")
assert len(progress) == 128
target = next(r for r in progress if r["tag"] == "02LG")
assert target["status"] == "open" and sum(r["status"] == "done" for r in progress) == 127
assert target["derivation_sha256"] == "2ec88ef8479dc870b20515290225c1e45eb26ac31ddecb7eda6aa68cb7912059"
assert target["proof_status"] == "released_after_derivation"
comparison = (REL / (PREFIX + "comparison.md")).as_posix()
review_path = REL / (PREFIX + "root_admission_review.md")
review = f"""# 02LG: whole comparison and root admission

Admitted {NOW} by {WHO}.
This closes the last required checking row, bringing Paper III to128/128.
The mathematical Problem retains its open status and its permanent identity.
The canonical manuscript remains unchanged until the separate guarded
application; no publication-unit criterion closes at this admission.

## Whole readings and actual scope

Root wholly read the784-line frozen fresh synthesis after the LT/LV
support admissions, before the individual original release. The complete
85-line original was then read; it has no separate proof environment.
Root now wholly read the109-line receiver, the complete280-line comparison,
the305-line historical count note, and the complete bounded LT/LU/LV
support note. The179-line count-comparison source and all71 actual stdout
lines, the82-line residual-comparison source and all25 actual stdout lines,
and both empty stderr streams were read. The local packet source, actual
streams, exact replacement, defects and event proposals were read before
this admission. The pre-exposure coefficient and catalogue sources and
actual streams were already wholly read at the fresh-review gate.

The helper's complete six historical-source readings and exhaustive
enumeration-field comparisons on five saved JSON bodies retain their
stated scope. Root does not claim manual whole reading of those source
bodies or of their geometric matrix arrays, nor execution of historical
mains. The main checker's full old dependency-packet, check-entry and
LL/LM comparison readings remain attributed to that checker. No new
primary-literature proof reading or independent checker family is inferred.

## Mathematical admission

The172-row natural catalogue,495 broad presentation patterns,162 minimal
patterns and59 sphere patterns on50 rows stand. Historical and fresh
records are identified by the five marked row coordinates and the finite
additive/original multiplicative site sets, with explicit inverse choice
lists. The original-star subset has459 elements. Removing finite III*/IV*
choices is its retraction; adding the unique such site gives the inverse
on the36 complementary choices. The495 count has no new count refutation.

The uniform residual-order smooth assignments fail in12 of18 cases.
The exact obstruction is naturality of the refined invariant under every
cyclic isomorphism x -> ux, with the Bezout inverse: it preserves zero
and element order. At residual orders4,8,20 the corrected values are
2 epsilon,4 epsilon,4+10 epsilon, respectively. For20 the map
(x,y) ->5x+4y and inverse(z mod4,4z mod5) identifies both components;
the cubed coefficients give the degree-six map. All18 complete
fundamental-class invariants remain zero. The single D27 refutation
records the affected synthesis clause and the same refined statement id.

The marked-column scope is nonzero corrected multidegree with h=1,
together with unchanged zero-degree caps in their extending frames.
At c=0 the scalar-long coordinate is free. The explicit O(F) tensor
map(p,w)->(p,u w), inverse(p,W)->(p,W/u), sends the meridian to
mu0+delta and the transported second normal to minus that free class.
This proves the D26 scope clarification; the original LG text does not
assert an extra zero column at that endpoint, so no such refutation is
invented. The original weighted OS45 odd framing-degree sentence is
true. Its exact Bott/Lie-frame comparison agrees with reference parity1
and complete critical linking minus1. The receiver cites the sole LV
proof and retains all weighted OS45 conclusions.

The receiver keeps one titled Problem, its visible tag02LG and label,
and its four precise remaining sectors. Proved reductions cite their
body results. No second derivation or proof is printed there.

## Records and next gate

Receiver SHA256:
dcc39d05247e5a9e290c6ed46562393d87948cf42204d4b40f23c80b8e5ed69f.
The packet has{len(replacements)} guard,{len(defects)} defect rows and
{len(incoming)} scoped events. Those events are merged without adding
credit for assembly or root readback. The next work is application of
all admitted repairs, followed by final mathematical unit order and the
complete register pass, provenance, clean build and every-page reading.
IV follows III; I,II,V remain closed until the joint stage.
"""
target.update({"status": "done", "packet_status": "required_check_complete",
               "assigned_checker": "/root/lg_fresh; root whole admission",
               "check_event_id": ";".join(r["event_id"] for r in incoming),
               "proof_comparison_evidence": comparison,
               "completion_evidence": review_path.as_posix() + "; " + comparison,
               "unresolved_inputs": ""})
target["notes"] += (" Admitted " + NOW + ": complete fresh/original/history/receiving comparison; "
                    "D27 residual assignments refined, D26 exact marked-column scope; counts and OS45 framing stand. "
                    "Required check complete; Problem remains mathematically open; final unit/provenance/build/pages open.")
# All guards, event fields and row identities have been validated before writes.
(ROOT / review_path).write_text(review, encoding="utf-8", newline="\n")
write_table(ROOT / "CHECK_EVENTS.tsv", fields, events + [{k: r.get(k, "") for k in fields} for r in incoming])
write_table(ROOT / "S6_SERIES_PUBLISH_required_progress_III.tsv", progress_fields, progress)
note = f"""\n### Last Paper III required check 02LG admitted — {NOW}

Paper III now has128/128 required checks complete. The full comparison
preserves the495-presentation scope and proves the459-subset maps.
It corrects12 residual smooth assignments through preserved integral
invariants and makes the additive marked-column endpoint scope explicit.
The original weighted OS45 framing claim stands. The mathematical
Problem remains open in its precise four sectors. See {review_path.as_posix()}.
All784 publication-unit criteria remain open. The canonical source is
unchanged pending guarded application of the admitted repairs. This
required-row closure is qualifying movement after Review64; source
application and packaging will receive no separate movement credit.
"""
for name in ("PROGRESS_LEDGER.md", "S6_SERIES_PUBLISH_report.md"):
    path = ROOT / name
    path.write_text(path.read_text(encoding="utf-8") + note, encoding="utf-8", newline="\n")
print("ADMITTED maps:src:D.2.4 at", NOW)
print("Paper III required checks:128/128; mathematical Problem remains open")
print("RECEIVER", len(receiver.splitlines()), sha256(receiver.encode()).hexdigest())
print("GUARDS", len(replacements), "DEFECTS", len(defects), "EVENTS", len(incoming))
print("Canonical source unchanged; unit criteria remain open")
