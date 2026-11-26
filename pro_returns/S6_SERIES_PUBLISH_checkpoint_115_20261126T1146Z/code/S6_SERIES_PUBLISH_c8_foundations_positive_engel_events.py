"""Record the actual exposed reading of the positive-weight Engel unit."""
import csv
from datetime import datetime, timezone
from S6_SERIES_PUBLISH_c8_foundations_marked_data import LANE, WHO


def main():
    path = LANE / "S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv"
    note = "agents/continuation8_iii_foundations/S6_SERIES_PUBLISH_c8_foundations_unit_reviews.md"
    with path.open(newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        fields, rows = reader.fieldnames, list(reader)
    when = datetime.now(timezone.utc).isoformat()
    scopes = [
        ("02LA", "maps:src:D.2.34", "Read all 725 repaired input lines, the full c7 original/receiving comparison, every edited line and all four final changed contexts. Retained the full positive-weight covering and conductor proof, primitive graph/wedge inverse maps, boundary Z/d and both attachment orders, all finite/original Thom and Gysin kernels, every free/noncoprime parameter, exact finite-meridian order and integral pair-sequence section, and all closed Smith forms at both rank endpoints. The positive-root model remains explicit and map-specific. Exposed use only; no mathematical program was executed."),
        ("Q133", "mapsIII:def:positive-engel-data", "Read the entire new definition against the original LA hypotheses and sole proof. It preserves the surface/line, translation and positive weight, exact toric period subgroup, ordered sites and periods, positive orders, signed affine parameters and effective original/logarithmic data. The column-cokernel matrix R is explicitly named with its old WE2 identity. The exact freeness criterion remains a proved theorem assertion."),
        ("Q134", "mapsIII:rem:positive-engel-specializations", "Read the full original post-proof specializations and entire replacement. WE14 and both-original groups remain. The simply connected criterion uses the exact determinant divisibilities. The KD comparison is an explicit abstract graded homology-coordinate map and inverse, checked against the bounded actual KD statement/lifted-source scope, with no geometric or whole-proof credit. The d=1 original Engel specialization uses the actual identity period/toric/original-cap maps to Q129."),
        ("Q135", "mapsIII:rem:positive-engel-calculations", "Read the entire original computational paragraph and numbered replacement. Integer inputs, exact free test, polynomial monodromy/exterior/graph identities, full area-kernel comparisons and all stated finite endpoint classes remain. Exact executable paths move to the single program table. No historical/current program execution or independent check is credited."),
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
                   evidence_group="III-C8-FOUNDATIONS-POSITIVE-ENGEL-UNIT-REVIEW",
                   date_utc=when, where=note)
        rows.append(row)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print("Recorded one complete theorem and three new formal-item readings locally.")
    print("Every event is used and rechecked in this run; no central state changed.")


if __name__ == "__main__":
    main()
