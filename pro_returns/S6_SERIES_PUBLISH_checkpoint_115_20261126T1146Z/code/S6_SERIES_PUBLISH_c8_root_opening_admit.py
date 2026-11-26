"""Record actual whole-source opening-unit reviews and their remaining gates."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import csv
import itertools

import S6_SERIES_PUBLISH_c8_root_units as r
import S6_SERIES_PUBLISH_c8_integrate_units as u

ROOT = u.ROOT
now = datetime.now(timezone.utc).isoformat()
evidence = "agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_opening_units_review.md"
fragment = u.WORK / "root/radial_coordinates.tex"
old_unit = fragment.read_text(encoding="utf-8")
old = "All these quantities are real. Write\n"
new = r"""The components $\alpha_T,m_T,\eta_T,H_T,\xi_T,B_T$ and
the combinations $c_T,L_T,q_T,D_T$ are real. Write
"""
assert old_unit.count(old) == 1
new_unit = old_unit.replace(old, new, 1)
source_path = u.repairs.SOURCE
source = source_path.read_text(encoding="utf-8")
assert source.count(old_unit) == 1
candidate = source.replace(old_unit, new_unit, 1)
regular_path = u.WORK / "root/regular_quotients.tex"
old_regular = regular_path.read_text(encoding="utf-8")
heading = "\\section{Global torus quotients and their extension obstructions}\n"
new_heading = heading + "\\subsection{Invariant characters and compactification}\n\\hypertarget{tag-Q006}{}\\label{mapsIII:sec:regular-quotients}\n"
assert old_regular.count(heading) == 1
new_regular = old_regular.replace(heading, new_heading, 1)
assert candidate.count(old_regular) == 1
candidate = candidate.replace(old_regular, new_regular, 1)
u.check_permanent_identifiers(source, candidate,
    ["mapsIII:sec:regular-quotients"], ["tag-Q006"])

fields, defects = r.table(r.DEFECTS)
for suffix, kind, statement, old_text, new_text, reason in (
    ("REAL-COMPONENT-SCOPE", "D26", "mapsIII:def:radial-cusp-data", old, new,
     "Resolve the inherited ambiguous all-these referent: the decomposed real components and their combinations are real; the three original mu,h,b functions retain their explicitly complex decompositions."),
    ("GLOBAL-SUBSECTION", "D14", "mapsIII:sec:regular-quotients", heading, new_heading,
     "Give the separated global theorem a real subsection unit before the later carrier subsections. All its publication criteria remain open."),
):
    ident = "III-C8-OPENING-" + suffix
    assert not any(x["change_id"] == ident for x in defects)
    defects.append(dict(change_id=ident,type=kind,statement_id=statement,
        old_location="opening/global source unit before final readback",
        old_page="pending page concordance",new_location=statement,
        new_page="pending final PDF",old_text=old_text,new_text=new_text,
        reason=reason,review_status="whole source readback complete; final page reading open"))

P = [[0,-2,-1,-2],[2,-1,0,-1],[0,2,1,3],[-1,0,0,0]]
Q = [[0,0,0,-1],[-1,-1,-1,-2],[-1,2,0,4],[1,0,1,0]]
def product(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
I = [[int(i==j) for j in range(4)] for i in range(4)]
assert product(P,Q) == I == product(Q,P)
det = 0
for perm in itertools.permutations(range(4)):
    sign = (-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
    term = sign
    for i in range(4): term *= P[i][perm[i]]
    det += term
assert det == -1
print("MARKING_DETERMINANT", det)
print("MARKING_BOTH_COMPOSITES", product(P,Q), product(Q,P))

event_path = ROOT / "CHECK_EVENTS.tsv"
event_fields, events = r.table(event_path)
who = "GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight, root"
outcomes = {
 "mapsIII:def:marked-family": "Whole rewritten definition compared with the complete former convention block and admissibility residues in02K7; original multiplicities, orientations and parameter restrictions preserved. No new independent check of the family construction.",
 "mapsIII:rem:dual-transport": "Whole numbered remark read against the prior cohomology-transport convention. Evaluation pairing, inverse transpose, inverse map and induced pullback are explicit and verified algebraically.",
 "mapsIII:def:period-parameters": "Whole definition compared with the prior period convention; period matrix, normalization, maximum, c range and positive parameter-loop lift preserved. Live fam:src:C.2.3 input matched through the attached statement inventory; stale printed SRef remains an open reference gate.",
 "mapsIII:def:engel-marking": "Whole definition compared with the previous marking formulas. Integral inverse and both products checked exactly; determinant-1, fourth-row character and inverse twist map verified. This records a publication comparison, not a pre-exposure re-proof.",
 "mapsIII:def:radial-cusp-data": "Whole numbered input and its well-definedness proof compared with the former input paragraphs; exact t_c,s,h,b substitutions, opened AC26 Proposition3.21 p22, holomorphic difference-quotient estimate and T0 range checked. Real-component referent clarified.",
 "mapsIII:carrier-real-periods": "Whole repaired proof before presentation and whole current proof read. Realification and inverse, determinant-D_T, two-by-two elimination and both dual-lattice maps retained unchanged; new numbered input precedes the proposition.",
 "wb:cusp-spec-native-quotient": "Whole repaired and publication proofs read. The period-basis paragraph moved into its proof; exact kernel inclusion/inverse operation, quotient distance, Frobenius bound, product systole and surjectivity onto the exact Euclidean balls preserved in their full T,R scopes.",
}
for label, outcome in outcomes.items():
    ident = "publish:c8:III:opening:" + label
    assert not any(x["event_id"] == ident for x in events)
    row = {k:"" for k in event_fields}
    row.update(statement_id=label,date="2026-11-25",who=who,
        type="used and rechecked in this run",outcome=outcome,event_id=ident,
        phase="continuation8 publication unit comparison",source_file=evidence,
        source_event_type="used and rechecked in this run",
        evidence_group="publish:c8:III:opening-units",date_utc=now,where=evidence)
    events.append(row)

progress_path = ROOT / "S6_SERIES_PUBLISH_unit_progress.tsv"
progress_fields, progress = r.table(progress_path)
closed = 0
for row in progress:
    if row["paper"] != "III": continue
    if row["unit_id"] == "sec:III:conventions":
        row["unit_id"] = "mapsIII:sec:marked-conventions"
        row["unit_title"] = "Markings and period parameters"
        done = row["defect_type"] not in {"D04","D06"}
    elif row["unit_id"] == "mapsIII:carrier-radial-prerequisites":
        done = True
    else:
        continue
    assert row["status"] == "open"
    row.update(status="done" if done else "open",date_utc=now,evidence=evidence,
        detail="Whole current canonical source unit and all-register evidence read; final PDF/build gates remain separate." if done
        else "Correct live maximum input selected; inherited SRef printed number and PDF path remain stale until final reference regeneration.")
    closed += int(done)
assert closed == 54
assert not any(x["paper"]=="III" and x["unit_id"]=="mapsIII:sec:regular-quotients" for x in progress)
for criterion in [f"D{i:02d}" for i in range(1,28)] + ["structure"]:
    row = {k:"" for k in progress_fields}
    row.update(paper="III",unit_id="mapsIII:sec:regular-quotients",
        unit_title="Invariant characters and compactification",
        row_kind="structure" if criterion=="structure" else "defect",
        defect_type="" if criterion=="structure" else criterion,status="open",date_utc=now,
        evidence=evidence,detail="Separated from the original radial parent to resolve cell-calculation dependencies; no completion credit transfers. Whole publication pass pending.")
    progress.append(row)

fragment.write_text(new_unit,encoding="utf-8",newline="\n")
regular_path.write_text(new_regular,encoding="utf-8",newline="\n")
source_path.write_text(candidate,encoding="utf-8",newline="\n")
r.write_table(r.DEFECTS,fields,defects)
r.write_table(event_path,event_fields,events)
r.write_table(progress_path,progress_fields,progress)
print("SOURCE_LOCAL_CRITERIA_CLOSED",closed)
print("CONVENTION_REFERENCE_CRITERIA_OPEN",2)
print("SEPARATED_GLOBAL_CRITERIA_OPEN",28)
print("USED_AND_RECHECKED_EVENTS",len(outcomes))
print("UTC",now)
print("III_TEXT_COMPLETE false; clean build, provenance and page gates remain open")
