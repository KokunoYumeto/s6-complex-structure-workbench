"""Record actual exposed KP/KQ unit and definition readings locally."""
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
        ("02KP", "maps:src:D.2.15", "Read the complete repaired KP statement/proof, full c6 comparison and every edited proof line, then every exact follow-up context. Retained the full marked surface, index-two cusp and inverse lattice map, all local and global integral attachments, canonical characters, free generator, cube and p1 computations, and full spin-bordism recognition. The English primary Zhubr text at Theorems3/5 pp.795-796 and section4.1 p.809 was read; only p.809 was additionally read in a page image. LO is an actual prerequisite notified to root. No historical/current mathematics program was run and no independent credit is claimed."),
        ("02KQ", "maps:src:D.2.16", "Read the complete repaired KQ statement/proof, all 216 lines of its c6 comparison, every edited proof line and every final changed context. Preserved both original star models, every ordered local/relative map, full exterior and transfer, all zero-n cycles and duality maps, free Euler-class proof and oriented reconstruction. The shared KN arithmetic is related by the exact coefficient-ring map and exhaustive unit hypotheses; the KO cusp uses the full H3 character map and inverse. Opened the used Ulmer-Urzua, Schutt-Shioda and Galaz-Garcia--Reiser primary statements and pages. Every positive m and signed translation endpoint remains. Exposed use only; no mathematics-program execution or independent credit."),
        ("Q119", "mapsIII:def:two-component-os56", "Read the complete new numbered definition against the old KP inputs and the full proof. The exact OS56 ordered profile, P=30G,Q=G, zero, four filling types, period marking, m=6k, every positive k, signed n/r and coprimality are unchanged. This is the relocation and exposed prerequisite reading actually performed."),
        ("Q120", "mapsIII:def:odd-star-logarithmic-data", "Read the complete new numbered definition against both original KQ configurations and every theorem/proof use. Both p/b rows, line M=O(P-O), period convention, original star/primitive node/cusp choices, every positive m and signed vector, freeness gcd and both named torsion groups are explicit. The missing local M name found in the first edited readback was restored before this final rereading. No independent check credit is assigned."),
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
                   evidence_group="III-C8-FOUNDATIONS-PRODUCT-STAR-UNIT-REVIEW",
                   date_utc=when, where=note)
        rows.append(row)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print("Recorded two theorem and two definition whole-unit readings locally.")
    print("Every event is used and rechecked in this run; no central state changed.")


if __name__ == "__main__":
    main()
