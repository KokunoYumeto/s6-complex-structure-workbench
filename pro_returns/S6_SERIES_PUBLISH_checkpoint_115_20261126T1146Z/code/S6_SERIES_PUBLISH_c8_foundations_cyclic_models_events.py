"""Record the completed exposed family, recognition and action unit readings."""
import csv
from datetime import datetime, timezone
import io
from S6_SERIES_PUBLISH_c8_foundations_marked_data import LANE, WHO

path = LANE / "S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv"
note = "agents/continuation8_iii_foundations/S6_SERIES_PUBLISH_c8_foundations_unit_reviews.md"
with path.open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields, rows = reader.fieldnames, list(reader)
when = datetime.now(timezone.utc).isoformat()
scopes = [
    ("02KG", "maps:src:D.1.7", "Read the complete repaired and original proofs, entire 250-line c5 comparison, full edited subsection and every final changed context. Preserved the all-data biholomorphism, every compact-parameter torus/root/cusp bound, finite fan representatives, proper holomorphic gluing, horizontal inverse flow, based inverse lifts, complete coherent even shifts, local additive-sheaf scaling, all overlaps/inverses and group law, exact punctured-disc family and every fixed-u root/endpoint. The source now names the exact admitted Teschl preliminary version. No current other-paper manuscript, new mathematical execution or independent check is credited."),
    ("02K9", "maps:src:D.1.11", "Read the entire repaired/current c7 proof and original proof, whole 265-line c5 comparison and corrected 89-line c7 source comparison, the full edited subsection and changed contexts. Preserved full integral H3 and b3 scope, exact spin and quarter-Pontryagin maps, full marked mu, the complete detector and marking inverse, both directions of the oriented classification map, canonical realization and explicit stable tangent inverse proving M1 is the standard oriented S6. The exact pp.793-794 printed H2 conditions and the actual Section 4.1 p.809 zero-free-H3 scope remain. No fresh source refutation, independent classification proof or new computation is claimed."),
    ("02KA", "maps:src:D.1.12", "Read the whole repaired and original proofs, entire 100-line c5 comparison, the complete edited source and final model-conjugacy context. Preserved S_d and both covered root actions, all affine powers and commutators, every finite and toric stabilizer argument, full holomorphic units, all three quotient maps and orbit inverses, actual canonical-model identity, conjugacy/inverse to any other oriented representative, based lift equation and cyclic automorphism, full family-only fixed-u count and d=1 trivial action. No other-paper tangent/Kodaira result, old executable or independent arithmetic event is credited."),
    ("Q145", "mapsIII:def:canonical-cyclic-model", "Read the full numbered canonical tuple, parameter domain, member, cover and underlying smooth-model definition against KG/K9/KA's complete source inputs. Md is the actual canonical cover with complex charts read as real charts by the identity and inverse; its uniqueness is subsequently proved in K9. The w-to-W multiplication by (-1)^k2, its inverse, and u=w²=W² keep every discrete twist and the exact existing parameter normalization."),
    ("Q146", "mapsIII:def:cyclic-classifying-data", "Read the entire numbered marked invariant against KI/K8/K9 and the corrected primary-source comparison. It retains A_d, every principal Cartan coefficient, all -12 terms, zero free/z3 coordinates, the explicit indexing correspondence and inverse, full refined-class meaning p(N), marking H2 to A_d, and the d=1 zero datum. K9 derives each coefficient through the full detector and realizes the datum by the canonical cover; no uniqueness is assumed in this definition."),
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
               evidence_group="III-C8-CYCLIC-MODELS-UNIT-REVIEW",
               date_utc=when, where=note)
    rows.append(row)
buffer = io.StringIO(newline="")
writer = csv.DictWriter(buffer, fieldnames=fields, delimiter="\t", lineterminator="\n")
writer.writeheader()
writer.writerows(rows)
temporary = path.with_suffix(".tmp")
temporary.write_text(buffer.getvalue())
temporary.replace(path)
print("Recorded five completed exposed readings locally: KG, corrected K9, KA, Q145 and Q146.")
print("All are used and rechecked in this run; event table replaced atomically; no shared state changed.")
