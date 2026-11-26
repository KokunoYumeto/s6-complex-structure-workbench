"""Record the actual exposed KL/later-owner comparison reading."""
import csv
from datetime import datetime, timezone
from S6_SERIES_PUBLISH_c8_foundations_marked_data import LANE, WHO


def main():
    path = LANE / "S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv"
    note = "agents/continuation8_iii_foundations/S6_SERIES_PUBLISH_c8_foundations_unit_reviews.md"
    with path.open(newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        fields, rows = reader.fieldnames, list(reader)
    event_id = "ce:III:c8:foundations:02KL:os49-owner-comparison"
    if any(row["event_id"] == event_id for row in rows):
        raise ValueError("This comparison reading is already recorded")
    when = datetime.now(timezone.utc).isoformat()
    row = dict.fromkeys(fields, "")
    row.update(statement_id="maps:src:D.2.11", date=when[:10], who=WHO,
               type="used and rechecked in this run",
               outcome="Wholly read the final Q30N remark and P29 statement/proof in the frozen later OS49 construction, against the full bridge note and already wholly read KL proof. Checked the source and line scalar, actual directed theta periods, G0/G0 inverse, inverse Hurwitz/F0, parameter and group generator maps, full root/collar/positive-normal and toric fan maps. The complete coprime domains agree and KL remains the single common homology owner; P29 preserves its distinct full specialization lattices, all four +n Leray maps and proper r-family. No new mathematical disagreement found. Root controls canonical application and global D12/D14/D20/structure closure. The later Yang page locators remain a D18 follow-up. No historical or peer mathematics program executed and no independent credit claimed.",
               event_id=event_id, phase="current", source_file=note,
               source_event_type="used and rechecked in this run",
               evidence_group="III-C8-FOUNDATIONS-KL-OS49-COMPARISON",
               date_utc=when, where=note)
    rows.append(row)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print("Recorded the complete exposed KL/OS49 comparison reading locally.")
    print("Event type: used and rechecked in this run. No central state changed.")


if __name__ == "__main__":
    main()
