"""Record the complete exposed LH publication reading, without new blind credit."""
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
        ("02LH", "maps:src:D.2.40", "Read every line of the 1694-line repaired source, whole 567-line comparison, released 58-line statement and 219-line original proof, entire first-edited source and all 94 final changed source contexts. Preserved every original proof item: full Z plus Z/g fibre quotient, actual odd involution/cocycle splitting and inverse identification, all finite/root Thom columns, every-power freeness, actual cap covers/transfers and free targets, saturated kernels, all component-disc angular entries, complete Wang torsion and rim shears, both exceptional nonabelian rows, integral finite-first splitting, ranks, duality, both 495/459 sets and the exact even-lift example. Common proof owners and coprime comparison have explicit maps. Exposed use only; no mathematics program was executed."),
        ("Q138", "mapsIII:def:odd-weighted-data", "Read the full numbered input against the complete LH original, receiver and proof. It retains every natural positive section pair, d>0 with odd gcd(a,d), norm iterate and units, both ordered cap sets, every free finite/regular datum, all integer clutches, exact period injection, last unfilled-site order, fixed-domain peripheral insertion, and all L/beta component counts. OW1 keeps its identity; 495/459 catalogue counts remain theorem conclusions."),
        ("Q139", "mapsIII:rem:odd-weighted-calculations", "Read the complete final remark against the original trailing paragraphs, complete c7 comparison and whole calculation readout. Checked the g=1 quotient and Bezout inverse, all finite/fixed-normal column images and the self-inverse Chern-generator sign, using the bounded actual LD statement. The finite weights and all displayed computation totals retain their admitted scope; LI's input inclusion fixes the complete tuple. No historical/current computation execution or whole-LI reading is claimed by this event."),
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
                   evidence_group="III-C8-FOUNDATIONS-ODD-WEIGHTED-UNIT-REVIEW",
                   date_utc=when, where=note)
        rows.append(row)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print("Recorded one whole LH theorem/proof reading and two complete new formal items locally.")
    print("All three events are used and rechecked in this run; no central state changed.")


if __name__ == "__main__":
    main()
