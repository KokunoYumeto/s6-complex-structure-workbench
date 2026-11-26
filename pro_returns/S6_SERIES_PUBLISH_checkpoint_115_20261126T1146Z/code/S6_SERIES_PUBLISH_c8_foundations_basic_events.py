"""Record the five actual exposed unit rereads in the local CHECK_EVENTS table."""
import csv
from datetime import datetime, timezone
from S6_SERIES_PUBLISH_c8_foundations_marked_data import ROOT, LANE, WHO


def main():
    path = LANE / "S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv"
    note = "agents/continuation8_iii_foundations/S6_SERIES_PUBLISH_c8_foundations_unit_reviews.md"
    with path.open(newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        fields, rows = reader.fieldnames, list(reader)
    when = datetime.now(timezone.utc).isoformat()
    common = (
        "Read the complete repaired unit and all five sole proofs, each complete admitted original/receiving comparison, "
        "and the entire edited fragment; reread every final changed context. Exact edits are in the local defects table. "
        "This is exposed use and rereading, with no historical program execution, new arithmetic run, or blind/independent credit. "
    )
    scopes = [
        ("02LR", "maps:src:D.2.5", "F5: Preserved all two-finite-fibre matrices, free quotient and clutching maps, van Kampen inverse, complete degree-one kernel, exterior preimages, cusp quotient and finite transfer B. Preserved both P cases, all inverse integral operations, the explicit P=0 cycle and splitting, all homology and the exact gcd sphere criterion. Q107 supplies the complete marking before use; Q109 numbers the known-case attribution. Positive-integer degrees are explicit."),
        ("02LW", "maps:src:D.2.6", "F6: Preserved g versus x*=g^-1, the exact overlap conjugacy and inverse, all eight reduced sweeps, full graph quotient inverse, positive B+, its cyclic map and inverse, all 4k parameters and sphere signs. Q111 holds the complete alternative source/target involutions. The exact two Paper II references remain for root's current-edition expansion."),
        ("02LX", "maps:src:D.2.7", "F7: Preserved the primitive I2 period map and inverse, all four monodromies, vanishing quotient sections, full X_D maps, finite J and section/kernel identities, positive B+, cyclic quotient and all 3k parameters. Q112 gives the exact alternative signed-coordinate involutions. Removed only the orphan API contrast; no unproved model identification or nonrelationship is asserted."),
        ("02LY", "maps:src:D.2.8", "F8: Preserved the all-k/all-r/n=±1 fixed set, exact line factors and connection, corrected positive Cartier values and integral-period character, quotient semicharacter/pullback inverse, Borel extension and localization inverse, cubic one, surgery trace and p1, and the explicit oriented augmented-ring isomorphism/inverse. Q108 supplies the conic construction before use. All historical correction/exposure chronology remains in its original records."),
        ("02LZ", "maps:src:D.2.9", "F9: Preserved the corrected affine relation, q=r-3k and inverse, complete radial/unit collar isotopy and inverse, type-II/cusp integral maps, graph inverse, full relative matrices and all signed n and integer r at every positive k. Removed the orphan transcription '3k family'; actual multiplicity 4k and the valid affine shift remain. All source credits remain at their proof inputs."),
    ]
    for tag, statement, scope in scopes:
        event_id = f"ce:III:c8:foundations:{tag}:unit"
        if any(row["event_id"] == event_id for row in rows):
            raise ValueError("Event already recorded: " + event_id)
        row = dict.fromkeys(fields, "")
        row.update(statement_id=statement, date=when[:10], who=WHO,
                   type="used and rechecked in this run", outcome=common+scope+
                   " Canonical admission, shared progress, final references, pages and rendering remain root work.",
                   event_id=event_id, phase="current", source_file=note,
                   source_event_type="used and rechecked in this run",
                   evidence_group="III-C8-FOUNDATIONS-BASIC-UNIT-REVIEW",
                   date_utc=when, where=note)
        rows.append(row)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print("Recorded five actual exposed unit-rereading events in the local CHECK_EVENTS table.")
    print("Attribution:", WHO)
    print("No central table, criterion state, canonical source or independence count changed.")


if __name__ == "__main__":
    main()
