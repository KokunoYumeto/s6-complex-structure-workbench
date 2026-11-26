"""Record only the completed exposed characteristic-class source readings."""
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
    ("02KE", "maps:src:D.1.5", "Read the full repaired source, entire 223-line c4 comparison and all 20 original proof lines, the full edited unit and every changed context. Preserved the complex covering/deck derivatives, integral UCT/Ext maps, mod-two Chern identity, every character restriction, isotropic component kernel and d=1 endpoint. The duplicate cusp/graph derivation now uses KC's wholly read identical subspaces, coefficient-lift inverse, finite transfer and equivariant retraction. No original assertion is refuted, no arithmetic program was run and no independent-check credit is claimed."),
    ("02KF", "maps:src:D.1.6", "Read the whole repaired theorem/proof, complete 137-line comparison and all 57 original proof lines, followed by the whole edited source. Preserved the full Thom augmentation and branch maps, all cyclic Cartan products, relative normal-disc and period-sweep chain, r=-T(u,w)=-2h with its inverse modulo d, exact torsion generator, all positive-degree products and the d=1 graded-ring isomorphism."),
    ("02KH", "maps:src:D.1.8", "Read the whole repaired theorem/proof, complete 291-line comparison and all 28 original proof lines, followed by the whole edited source. Preserved the primitive downstairs fibre functional, T=2h, every degree-one lifted torus and its translation homotopy, the full simplex-sum transfer, oriented cap/transfer identity, zero integral degree-four pullback and complex derivative giving c2=p1=0, including d=1."),
    ("Q142", "mapsIII:def:cyclic-cohomology-data", "Read the final complete numbered cover/divisor/ruling definition against the actual KB exceptional rays and normalization map. The correct coefficient map is (a,b1,b2,b3) to (a,b3,b1,b2), with inverse (a,cA,cB,cC) to (a,cB,cC,cA). A false initial local permutation was corrected in an exact D25 row before canonical application and carries no separate check credit. The final normalized-domain, image-cycle, orientation and ruling definitions agree with every retained ring proof."),
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
               evidence_group="III-C8-CYCLIC-CLASSES-UNIT-REVIEW",
               date_utc=when, where=note)
    rows.append(row)
with path.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
print("Recorded four completed current source readings locally: KE, KF, KH and final Q142.")
print("Every event is used and rechecked in this run; no failed-candidate or independent credit.")
