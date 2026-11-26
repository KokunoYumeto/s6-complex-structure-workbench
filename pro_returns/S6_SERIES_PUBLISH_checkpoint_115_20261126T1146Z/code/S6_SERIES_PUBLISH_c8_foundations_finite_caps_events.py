"""Record the complete exposed finite-cap unit readings and new formal items."""
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
        ("02L4", "maps:src:D.2.29", "Read the entire repaired theorem, sole proof and orphan examples/computation paragraphs; read the full c7 original/receiving comparison, all 761 edited fragment lines and final changed contexts. Preserved the 68/62 scope and six-position complement, whole-disc affine conjugacy, all-power freeness, exact core/normal character, full integral Thom kernel, global cap elimination and free-chain bridge, both rational ranks and every integer clutch. The general period-lift correction remains v+N_m lambda. Exposed use only; no historical/current mathematics program was executed."),
        ("02L6", "maps:src:D.2.30", "Read the complete repaired statement/proof, full c7 comparison and every edited line. Preserved all 102 positions and 68/34 split, literal fixed/coinvariant/norm inverse maps, all three Thom columns, full 198-pattern enumeration and 164-pattern inclusion, exact one-site lift/clutch map with inverse, both Smith endpoints and all-site Seifert obstruction. Coordinated the clause-level L3-before-L4/L6 order with lg_fresh and root. No independent check or execution credit is assigned."),
        ("Q121", "mapsIII:def:primitive-fixed-finite-data", "Read the complete new input definition against the original L4 statement and full proof. The common section/period/area data, primitive fixed vector, all m=d k with k>0, signed n/r, t, nonstar global caps, arbitrary regular sites and integer clutch retain their exact scope. This is a numbered relocation and exposed use."),
        ("Q122", "mapsIII:rem:finite-torsion-examples", "Read both original examples and the complete rewritten remark. The actual clutch is now stated as e=0 in both; the first full Thom quotient is shown by the residue map from s,L-prime to (Z/3)^2 and its inverse. The second zero-Euler groups follow from the displayed rank-one relation. No new parameter range or independent event is inferred."),
        ("Q123", "mapsIII:rem:primitive-finite-calculations", "Read the entire original finite computation paragraph and the numbered replacement, preserving all 68 inputs, k=1..6, all residue pairs and 150059/305/99/55 results. The executable path moved to the one program proposal table. The historical program was neither read nor executed in this pass; this event records only the actual exposed statement reading."),
        ("Q124", "mapsIII:def:general-finite-additive-data", "Read the entire new definition against the original AF1 and parameter clauses and the whole general-lattice proof. The positive generator g, q_v, positive k, signed r/n, power and t retain their domains; AF1's old label/anchor remains. The counts and g-value range remain theorem conclusions. Exposed use only."),
        ("Q125", "mapsIII:rem:general-finite-calculations", "Read the original trailing finite calculation and complete numbered replacement. All 34 additional bases, k/residue bounds, 38675/175/35/725 values and five-clutch scope remain. Historical JSON availability and execution chronology stay in the full c7 comparison and program proposal note; no new historical or independent credit is assigned."),
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
                   evidence_group="III-C8-FOUNDATIONS-FINITE-CAPS-UNIT-REVIEW",
                   date_utc=when, where=note)
        rows.append(row)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print("Recorded two complete theorem and five new formal-item readings locally.")
    print("Every event is used and rechecked in this run; no central state changed.")


if __name__ == "__main__":
    main()
