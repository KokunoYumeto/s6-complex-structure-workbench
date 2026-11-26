"""Record actual complete exposed readings of the weighted-profile unit."""
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
        ("02LD", "maps:src:D.2.37", "Read all 1777 repaired source lines, the complete c7 original/receiving comparison, every first-edited line and all 114 final changed source contexts. Preserved every general-a/d right inverse and wedge map, polynomial d=0 auxiliary, cusp boundary and relative sections, component-power inverse, all 436 rank-one maps, additive original kernels, arbitrary-j rim shear, full projected-lattice free criterion and 102 primitive examples, every Thom/root column, clutch/norm map, both exceptional nonabelian rows and complete torsion-sensitive extension. Both 495/459 sets and the exact 36-pattern map remain. Shared proof owners are used only with the printed input/chain maps. Exposed use only; no mathematics program was executed."),
        ("Q136", "mapsIII:def:weighted-natural-data", "Read the complete numbered definition against the original LD statement and whole proof. It preserves every natural row, positive coprime section pair, d>0 with gcd(a,d)=1, norm iterate/fan units, both cap sets, unrestricted free finite and regular inputs, all integer clutches, exact period and alternating-form definitions, and every L/beta component contribution. WP1-WP3 retain their identities; integrality, primitivity, cusp count and pattern counts remain theorem conclusions."),
        ("Q137", "mapsIII:rem:weighted-profile-calculations", "Read the full original trailing computation/scope paragraphs and complete numbered replacement. All 172 constant-specialization matrices, 1626 full graph presentations and 1131 weights above one remain. The actual constructive all-parameter proof is named. The forward LI pointer was checked against its bounded statement and identifies the exact identity inclusion on row, weight, ordered caps, all logarithmic data and clutch; it is not a premise of LD and gives no whole-LI or independent credit. Program paths remain in the single proposal table, with no execution claim."),
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
                   evidence_group="III-C8-FOUNDATIONS-WEIGHTED-PROFILES-UNIT-REVIEW",
                   date_utc=when, where=note)
        rows.append(row)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print("Recorded one complete theorem and two new formal-item readings locally.")
    print("Every event is used and rechecked in this run; no central state changed.")


if __name__ == "__main__":
    main()
