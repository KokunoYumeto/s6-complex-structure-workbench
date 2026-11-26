"""Record the complete exposed KT/KX/KY and new formal-item readings."""
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
        ("02KT", "maps:src:D.2.19",
         "Read the complete repaired KT statement/proof, its entire c6 original/receiving comparison, and every edited proof line. Preserved the generic chord/tangent function, all line-map inverses, full component criterion, integer degree, 104/88/348 counts and complete period-product/inverse argument. Q110 now precedes the criterion and replaces both the stale compendium and forward KY-table pointers. Repaired the signed intermediate sentence: the input g_i is the negative Abel--Jacobi cocycle; the exact self-inverse quotient map [x] to [-x] preserves component orders and zero, so every pair/count/conclusion remains. Q116 gives the exact vertical tensor conversion. No historical or continuation mathematics program was executed."),
        ("02KX", "maps:src:D.2.22",
         "Read all repaired KX theorem/proof lines, the entire c7 original/receiving comparison and all edited proof lines. Retained the complete signed Tate/fan maps, rational specialization and original-cap models, arbitrary-V rank budget, all 21 minors, effective norm, full component equation, all selected/unselected integer potentials, global line maps, zero translation/inverse and invariant-divisor freedom. The 172/226 counts and each peripheral marker remain. KX is the single owner of the natural classification formerly repeated in KY. The orphan external-question scope was sent to the final synthesis; the exact theorem scope is unchanged. Prior pre-/post-exposure chronology remains untouched."),
        ("02KY", "maps:src:D.2.23",
         "Read all repaired KY theorem/proof lines, the entire c6 original/receiving comparison and every edited proof line, including every normal-closure table row. Q110 owns the unchanged 82 ordered raw inputs and KX owns the duplicated natural classification. Preserved the distinct four-period marking, primitive cusp discs/inverse charts, 52 normal-closure rows, both odd-star exceptional maps, full local cyclic extension, canonical and arbitrary peripheral lifts, all endpoint groups and triangle representation. Added an explicit nonzero starting column, inverse swap, g>0 and zero-column skip for the Bezout reduction; all signed/zero powers and determinant endpoints remain. No new independent or historical-execution credit."),
        ("Q110", "mapsIII:def:elliptic-marked-data",
         "Read the entire relocated definition, every one of its 82 matrix/cocycle entries, all 21 fibre/peripheral lists, heights, periods and negative-increment convention. All numerical entries and their order are unchanged. The exact profile-label map replaces def/default by base for the same largest-fibre-count profile, with unadorned OS numbers identifying that same list. The complete KT/KX/KY proofs and comparisons were read. Root and lv_compare were notified of the actual label for their LN/LQ citations. This is exposed prerequisite use only."),
        ("Q116", "mapsIII:rem:vertical-section-lines",
         "Read the full new numbered conversion remark and its original KT paragraph, together with the full KT and KL proofs. It states J'=J tensor O(V-t_Q^*V), its inverse tensor change, and the exact OS49 degree vectors. Multiplication of meromorphic sections identifies the tensor product with the whole-fibre line, and tensoring by O(plus/minus C1) gives inverse functors; no unsupported isomorphism of the untensored line bundles is claimed. This is an exposed conversion reading only."),
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
                   evidence_group="III-C8-FOUNDATIONS-CATALOGUE-UNIT-REVIEW",
                   date_utc=when, where=note)
        rows.append(row)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print("Recorded three complete theorem-unit readings and two new formal-item readings locally.")
    print("Every event type is used and rechecked in this run; no central state changed.")


if __name__ == "__main__":
    main()
