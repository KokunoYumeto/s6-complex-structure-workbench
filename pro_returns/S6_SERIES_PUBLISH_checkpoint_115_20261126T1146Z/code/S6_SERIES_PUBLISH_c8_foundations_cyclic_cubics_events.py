"""Record the completed exposed finite-cubic and detector unit readings."""
import csv
from datetime import datetime, timezone
from S6_SERIES_PUBLISH_c8_foundations_marked_data import LANE, WHO

path = LANE / "S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv"
note = "agents/continuation8_iii_foundations/S6_SERIES_PUBLISH_c8_foundations_unit_reviews.md"
with path.open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields, rows = reader.fieldnames, list(reader)
when = datetime.now(timezone.utc).isoformat()
scopes = [
    ("02KI", "maps:src:D.1.9", "Read the whole repaired and original proofs, complete c5 comparison, full edited subsection and every final changed context. Preserved the full fixed-curve stabilizer, both exact delta-period chains, all full-unit sweeps and complex signs, downstairs component map (10,-2,12,0)h, Bezout UCT lift, all composite-ring basis inverses, normalized restriction and square -12, every cubic value and the full deck-module map. KF's identical normalization and relative injection now have one owner with their exact identity map. No program was executed and no independent credit is claimed."),
    ("02K8", "maps:src:D.1.10", "Read the whole repaired and original proofs, entire c5 comparison, whole edited subsection and final changed product-coordinate context. Preserved the exact path-fibration pullback, degree-eight calculation, complete integral prime-support induction and cyclic resolution, finite-coefficient generators, every Kunneth detector including repeated indices, arbitrary-u automorphism and inverse, canonical mu pushforward and all signed-d/rank-zero/trivial-factor endpoints. The application of KI now explicitly states d>1 and its separate already proved d=1 zero invariant. No mathematical execution or independent check is added."),
    ("Q143", "mapsIII:def:cyclic-coefficient-data", "Read the complete numbered coefficient-ring, divisor-reduction, cusp-edge and cyclic-matrix definition against KI's original and receiving proof. The full fixed-curve assertion and normalized v existence remain proved in KI; the definition keeps the exact complex fundamental-class pairing and every cyclic matrix entry."),
    ("Q144", "mapsIII:def:fundamental-class-invariant", "Read the complete signed-d/nonnegative-rank group and coordinate definition and the exact Zhubr classifying-map definition. Every allowed u is the cyclic projection plus its arbitrary free-coordinate values. The full canonical map induces identity on H2 and mu is its oriented fundamental-class pushforward; the local factor coordinates are related by actual projection pullbacks and inverse restrictions in K8."),
]
for tag, statement, scope in scopes:
    event_id = f"ce:III:c8:foundations:{tag}:unit"
    if any(row["event_id"] == event_id for row in rows):
        raise ValueError("Event already exists: " + event_id)
    row = dict.fromkeys(fields, "")
    row.update(statement_id=statement, date=when[:10], who=WHO,
               type="used and rechecked in this run", outcome=scope,
               event_id=event_id, phase="current", source_file=note,
               source_event_type="used and rechecked in this run",
               evidence_group="III-C8-CYCLIC-CUBICS-UNIT-REVIEW",
               date_utc=when, where=note)
    rows.append(row)
with path.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
print("Recorded four completed current source readings locally: KI, K8, Q143 and Q144.")
print("All are used and rechecked in this run; no central state changed.")
