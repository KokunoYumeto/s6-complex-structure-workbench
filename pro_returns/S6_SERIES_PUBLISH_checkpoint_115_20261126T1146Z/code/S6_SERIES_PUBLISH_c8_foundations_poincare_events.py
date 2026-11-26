"""Record the completed exposed KM and Q115 readings; fix their final sentence join."""
import csv
from datetime import datetime, timezone
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor, LANE, WHO


def main():
    e = Editor("elliptic_poincare", "c8-III-foundations-KM-join-")
    e.replace(r"""The identities for $\vartheta$ above give
$\vartheta(z-P)/\vartheta(z)$ divisor $P-O$ and
$\tau$-multiplier $e^{2\pi iP}$.""", r"""By the identities for $\vartheta$ above, the quotient
$\vartheta(z-P)/\vartheta(z)$ has divisor $P-O$ and
$\tau$-multiplier $e^{2\pi iP}$.""", "D23", "maps:src:D.2.12",
              "State the theta-quotient divisor with an explicit subject and verb; no formula or mathematical conclusion changes.")
    e.finish()
    path = LANE / "S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv"
    note = "agents/continuation8_iii_foundations/S6_SERIES_PUBLISH_c8_foundations_unit_reviews.md"
    with path.open(newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        fields, rows = reader.fieldnames, list(reader)
    when = datetime.now(timezone.utc).isoformat()
    scopes = [
        ("02KM", "maps:src:D.2.12",
         "Read all 1285 lines of the repaired KM unit, the entire c5 original/receiving comparison, then every edited proof line consecutively and all final changes in context. Preserved the seven geometric models, rational whole-segment root bounds, inverse peripheral words and period maps, complete theta/Poincare rigidification and full integer height, all component signs, all reduced/finite attachment maps and the unrestricted affine-period endpoint. Moved the seven-profile data to Q115 and replaced the duplicate shared projective-period paragraph by Q102; the OG/KM shared-period relocation is now complete. The r-to-R0 affine map and inverse, all positive multiplicities, signed coprime data and both sphere signs remain. No historical mathematics program was executed; no fresh or independent check credit is claimed."),
        ("Q115", "mapsIII:def:seven-log-profiles",
         "Read the complete new numbered definition after relocation from the KM statement, including every one of the seven ordered configurations, P/G and Q/G, selected zero, additive order and fixed vector in the unchanged period basis. The complete repaired and edited KM proof and admitted comparison were read and show existence and topology for these data. This is an exposed prerequisite reading, not an independent theorem check."),
    ]
    for tag, statement, scope in scopes:
        event_id = "ce:III:c8:foundations:" + tag + ":unit"
        if any(row["event_id"] == event_id for row in rows):
            raise ValueError("Event already exists: " + event_id)
        row = dict.fromkeys(fields, "")
        row.update(statement_id=statement, date=when[:10], who=WHO,
                   type="used and rechecked in this run", outcome=scope,
                   event_id=event_id, phase="current", source_file=note,
                   source_event_type="used and rechecked in this run",
                   evidence_group="III-C8-FOUNDATIONS-KM-UNIT-REVIEW",
                   date_utc=when, where=note)
        rows.append(row)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print("Recorded two local used-and-rechecked events with their exact scopes.")


if __name__ == "__main__":
    main()
