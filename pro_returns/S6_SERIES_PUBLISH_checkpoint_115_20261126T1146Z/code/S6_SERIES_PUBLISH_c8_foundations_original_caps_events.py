"""Record actual complete exposed readings of the original-cap publication units."""
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
        ("02L7", "maps:src:D.2.31", "Read the whole repaired statement/sole proof and post-proof calculation paragraph, full c7 comparison, every first-edited line and final changed contexts. Preserved all original line/isotopy/component maps, all-172 exterior inverses, full finite/regular norm columns, integral bridge at both Euler values, complete b=1 CRT maps, actual s=0 before fan changes, OS47 mu2 counterexample and disjoint relative-ball repair, free-Euler argument and oriented refined reconstruction including even R. The shared KQ reconstruction now has its exact role map and inverses. Exposed use only; no mathematics program was executed."),
        ("02L8", "maps:src:D.2.32", "Read the complete repaired statement/proof, full c7 comparison and every edited line. Preserved all primitive Chern/Gysin maps, full raw-to-Wang kernel, signed b/q pairing, complete normal maps, 46 occurrences, 282/228/54 enumeration, unrestricted finite/regular columns, full Seifert group and integral L+r bridge including zero Euler. The KV/KW specialization maps were checked against the bounded actual statement/proof scopes and are printed with inverses; those bounded readings receive no whole-proof or independent credit."),
        ("02L9", "maps:src:D.2.33", "Read the complete repaired theorem and sole proof, full c7 comparison and every edited line. Retained the cycle line and gauge construction, all period/component inverses, Gysin rim/component section, raw/Wang kernels and preimages, arbitrary-j rim shear and commuting exterior map, zero-Chern target isomorphisms, complete finite/regular parameter maps and L+r bridge, and all 495/1728 catalogue entries/subtotals. The current Q110/KX component involution is identified exactly; common proof ownership is through printed identity maps. No independent or historical execution credit is assigned."),
        ("Q126", "mapsIII:def:zero-chern-original-data", "Read the complete new definition against the full original L7 hypotheses and proof. All marked natural rows, positive coprime sections, period/area form, original and logarithmic choices, arbitrary regular sites/clutch, ordered filling patterns and component defect retain their exact scope. KY explicitly owns the marked multiplicative and zero models. Numbered relocation and exposed use only."),
        ("Q127", "mapsIII:rem:zero-chern-original-calculations", "Read the complete original computational paragraph and the new numbered remark. It preserves all 396 unselected local occurrences, 228 patterns and 144 full-matrix comparisons, including the exact one-orbit coordinate comparison to both KQ and KR. Only executable bookkeeping moves to the one program table. No historical or current program execution is claimed."),
        ("Q128", "mapsIII:def:all-original-additive-data", "Read the complete new input definition against L8's original hypotheses and its entire proof. The full additive/original/finite choices, positive/free/clutch scope, component counts, L and beta retain their meanings; the OC2 equation identity moves unchanged with its single definition. Exposed use only."),
        ("Q129", "mapsIII:rem:original-additive-specializations", "Read the entire new specialization remark, its L8 derivation and bounded actual KV/KW source scopes. The Engel identity uses the exact ordinary-disc map at (m,v)=(1,0); the five mixed rows use the explicit positive-order and signed-parameter map and inverse, with the same marked fixed vector, line and full cap/exterior diagrams. The existing SeriesRef remains for root expansion. No fresh independent comparison is claimed."),
        ("Q130", "mapsIII:rem:all-original-additive-calculations", "Read the whole original calculation paragraph and complete numbered replacement. All 46 primitive Chern vectors, logarithm vectors, full area kernels and images, 282 patterns and 74/9/54 finite comparison scope remain. Program paths move to the single proposal table. No mathematical program was read or executed by this event."),
        ("Q131", "mapsIII:def:original-multiplicative-data", "Read the complete new definition against the original L9 statement and full proof. Every original/primitive multiplicative choice, additive option, positive order, free affine lift and integer clutch remains. L and all three beta contributions keep their exact component domains. Exposed numbered relocation only."),
        ("Q132", "mapsIII:rem:original-multiplicative-calculations", "Read the original trailing calculation and complete numbered replacement. It keeps all 120 local normal forms, full primitive/monodromy kernels, signed area and Chern/component data, all six type subtotals and 213/18/172 comparison scope. The unbounded theorem continues to rest on the full proof. No historical/current run or independent credit is inferred."),
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
                   evidence_group="III-C8-FOUNDATIONS-ORIGINAL-CAPS-UNIT-REVIEW",
                   date_utc=when, where=note)
        rows.append(row)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print("Recorded three complete theorem and seven new formal-item readings locally.")
    print("Every event is used and rechecked in this run; no central state changed.")


if __name__ == "__main__":
    main()
