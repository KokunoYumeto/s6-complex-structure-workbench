"""Record the complete exposed LI publication pass and new formal items."""
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
        ("02LI", "maps:src:D.2.41", "Read the whole 502-line repaired source, complete 246-line comparison, whole released original statement, all 199 original proof lines and both original following paragraphs, the entire first-edited source and all final changed source contexts. Preserved all fifteen signed bar/word/normal identities, the full integral inverse section, every core relation and even-torsion shear, all-positive local cap maps, saturated kernels, complete component-disc indices, Seifert inverse paths, both rank cases and integral duality. Added the exact norm polar telescoping/additivity proof for the asserted source relation map as D22, with no refuted conclusion. No arithmetic source was executed and no fresh-check credit is claimed."),
        ("Q140", "mapsIII:def:all-weight-integral-data", "Read the complete numbered definition against every original and receiving input. It retains all natural positive pairs, every d>0, norm line and units, both cap sets, every free finite/regular datum and clutch, actual weighted counts, the four ordered periods, last-site ordering, K and fixed-domain J_i maps, full norm, all signed quadratic coefficients and the exact final-word suffix. The oriented torus class is defined by its actual induced T2 map. Symmetry and the primitive identity remain theorem conclusions."),
        ("Q141", "mapsIII:rem:all-weight-integral-calculation", "Read the original executable/scope paragraphs and the complete numbered replacement. It retains the full coefficient-vector method, ordered last word, all relations and normal columns, finite-period sum and integer-kernel/Smith/Hermite operations, with the complete homology output at every stated parameter. The odd comparison is the proved full coordinate change using mathfrak-h and its inverse, including norm columns. Historical and current finite computation attribution stays in its original records; no new run or smooth classification is claimed."),
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
                   evidence_group="III-C8-FOUNDATIONS-INTEGRAL-WEIGHTS-UNIT-REVIEW",
                   date_utc=when, where=note)
        rows.append(row)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print("Recorded one whole LI theorem/proof and two complete new formal-item readings locally.")
    print("Every event is used and rechecked in this run; no central state changed.")


if __name__ == "__main__":
    main()
