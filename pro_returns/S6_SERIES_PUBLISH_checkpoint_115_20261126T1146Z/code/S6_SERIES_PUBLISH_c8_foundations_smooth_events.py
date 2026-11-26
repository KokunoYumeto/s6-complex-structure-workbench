"""Record exposed whole-unit readings for KN/KO and their definitions."""
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
        ("02KN", "maps:src:D.2.13", "Read the complete repaired KN statement/proof, full c6 original/receiving comparison and every edited line. Preserved all four surface deformations and exact markings, full positive-meridian/collar maps, central lattice and normal line, integral exterior and complete transfer, unrestricted prime-local ideals, both n=0 free splittings and middle cycles, torsion linking and full parameter/sphere endpoints. Q117 owns the unchanged input datum and refers directly to KM rows 1,2,4,6. Root agreed the actual KN-to-catalogue prerequisite placement. No historical/current mathematics program was executed and no new independent credit is claimed."),
        ("02KO", "maps:src:D.2.14", "Read the complete repaired KO statement/proof, full c6 original/fresh/receiving comparison and every edited proof line. Preserved every primitive angular/cusp map, fan chart and normal inverse, smooth Hopf quotient, integral Theta inverse, linking realization, alpha-direction conjugacy, equivariant bundle/collar reconstruction, original surgery objects and all spin/p1/parameter endpoints. Reopened Barden pp.367-368,372,376-377 and Galaz-Garcia--Reiser pp.9,10,17 in primary page images at the actual cited statements. One direct oriented classification proof remains, with distinct surgery consequences and the complete historical cancellation comparison kept in its admitted check file. Exposed use only."),
        ("Q117", "mapsIII:def:smooth-logarithmic-data", "Read the complete new numbered input and its original theorem/proof context. The four exact marked profiles, P=pG,Q=G, ordered zero, four primitive one-node/cusp fillings, period lattice, all m>0 and signed a,b,c,n, freeness gcd and t are unchanged. The actual surfaces are constructed from exact KM rows 1,2,4,6, with no reverse catalogue premise. This is an exposed prerequisite use and relocation reading."),
        ("Q118", "mapsIII:def:twisted-smale-suspension", "Read the complete numbered model definition, the old KO statement and the entire receiving proof. Positive m, the spin five-manifold, first-plane rotation and attached-to-complement convention are explicit. Opened Barden Theorems2.2-2.3 pp.376-377 and Galaz-Garcia--Reiser Definition5.1 p.17 in their primary page images. The exact inverse-alpha collar map and every original equation object remain. No independent origination is claimed."),
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
                   evidence_group="III-C8-FOUNDATIONS-SMOOTH-UNIT-REVIEW",
                   date_utc=when, where=note)
        rows.append(row)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print("Recorded two complete theorem readings and two new definition readings locally.")
    print("Every event is used and rechecked in this run; no central state changed.")


if __name__ == "__main__":
    main()
