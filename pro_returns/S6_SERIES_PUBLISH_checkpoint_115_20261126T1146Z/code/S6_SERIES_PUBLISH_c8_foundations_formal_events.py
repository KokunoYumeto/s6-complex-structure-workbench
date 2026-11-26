"""Record actual exposed readings of newly numbered formal items and KK/KL."""
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
        ("Q100", "mapsIII:def:marked-elliptic-cocycles", "Read the complete numbered definition and its source location in the OG unit. It fixes the ordered elliptic monodromies, integral section cocycles, period changes and saturation convention actually used in both finite covering constructions. The full old/repaired OG proof and admitted comparison were read. No new computation or independent check is claimed."),
        ("Q101", "mapsIII:rem:collision-configurations", "Read the complete numbered source-scope remark and its OG context. It retains the two positively stated collision configurations and exact Miranda/Fukae source locators established in the admitted OG comparison. This is exposed editorial/mathematical rereading; it does not claim a new primary-source or blind check."),
        ("Q102", "mapsIII:rem:positive-projective-periods", "Read the entire new common period remark and its actual OG-to-KM prerequisite. Verified the map z/omega_2 and inverse omega_2 w, the SL2 coordinate fractions and inverse period identities, the two finite matrices and their derivatives, and the exact cusp conjugacy A^-1 B=T and -(AB)^-1=STS^-1 with inverse conjugation. Reopened Herfurtner's primary printed p.2. The duplicate KM paragraph still awaits its owned pass; no independent credit is assigned."),
        ("Q103", "mapsIII:rem:collision-weierstrass-coordinate", "Read the complete alternate Weierstrass coordinate construction after relocation from the OG proof, including every forward/inverse rational coordinate and endpoint, with all existing equation labels retained. The complete OG unit and admitted source comparison were read. This is one exposed rereading of the existing construction."),
        ("Q104", "mapsIII:def:triangular-cusp", "Read the whole numbered lattice/unit fan definition moved before LK, including the full-index lattice, primitive quotient cells, holomorphic unit periods and height character q. Its entire cap proof was read against the admitted comparison, including every unit/lattice endpoint. No independent geometric check is inferred from this relocation."),
        ("Q105", "mapsIII:def:rank-one-wheel", "Read the complete numbered cyclic ruled-surface gluing definition and the full L5 Euler proof using it. The two disjoint sections and one-component self-gluing case remain explicit. This event records exposed use of the defined object, not a new proof-check method."),
        ("Q106", "mapsIII:def:finite-filling-inputs", "Read the full numbered finite-input definition after moving all 21 configurations, n values, G/P/Q choices, simple-zero markers and additive choices from KU. Read the complete repaired and rewritten KU proof and its admitted comparison. Its marked-model output scope remains exact; no geometric realization is inferred from the output records."),
        ("Q107", "mapsIII:def:two-finite-fibre-marking", "Read every entry of the relocated ordered lattice, three homological monodromy matrices and two distinguished vectors before LR. Read the complete LR proof and comparison, including the product/order/fixed-lattice equalities and both determinant cases. This is exposed use and rereading of the existing marking."),
        ("Q108", "mapsIII:def:conic-surgery", "Read the entire numbered conic embedding and oriented framed-surgery definition moved from LY. The full LY proof of normal triviality, framing uniqueness, surgery trace, cubic and oriented type was read against its admitted comparison. The definition introduces no additional classification claim or independent check."),
        ("Q109", "mapsIII:rem:initial-logarithmic-homology", "Read the complete numbered source-credit remark and the complete LR proof/comparison supporting its initial-case attribution and full positive-integer determinant range. No fresh source-wide or historical-executable reading is claimed."),
        ("Q111", "mapsIII:rem:iii-star-boundary-orientation", "Read the full LW conversion remark, its finite source/target bases and the complete surrounding proof. Direct multiplication gives diag(1,-1) B+ (-I2); the source negation and target t-negation are their own inverses. The conversion is relocated from the already admitted proof and receives exposed use credit only."),
        ("Q112", "mapsIII:rem:wang-boundary-orientation", "Read the full primitive-I2 boundary conversion remark and the complete LX proof/comparison. It preserves B+=(2n,6r alpha;0,1), the exact signed matrix identity and the two inverse involutions. No new independent arithmetic check is assigned."),
        ("Q113", "mapsIII:def:yang-finite-data", "Read the entire numbered Type B/C data table, positive integer R,k,l, ordered lattice, ell_1 and both deck/forward matrices after relocation. The whole KK proof and admitted comparison were read, preserving all R and both determinant cases. This is exposed prerequisite use."),
        ("Q114", "mapsIII:def:os49-component-zero", "Read the complete numbered explicit cubic, P, Q=3P, M and zero-component definition, and the whole KL proof before and after editing. Its old equation label/target survives. The exact comparison with later P3F.26--29 remains open and no geometric equality is inferred from coincident cubic coefficients alone."),
        ("02KK", "maps:src:D.2.10", "Read the complete repaired and edited theorem/proof and the whole c5 original/receiver comparison. Preserved every finite lattice, sweep coordinate, full augmented map, minor ideal, both relative kernels, actual normal-disc splitting, full integer ranges and broader free-affine surjection. Added explicit Type B original-group maps and inverses for both parities of R. Q113 supplies the common marking before use. No historical program executed."),
        ("02KL", "maps:src:D.2.11", "Read the complete original and edited KL theorem/proof and the exact historical full-proof/scope events; there is no c4--c8 KL receiver or required-progress row. Preserved gcd(n,3k)=1 and all n,r,k in that domain. Replaced the stale compendium pointer by the primary rank-one height/discriminant argument; opened Schuett--Shioda Corollary 6.13, sections 8.8/11.8/11.10 equation22. Added literal line-bundle, period, product and full-matrix quotient inverses. Read the entire newly written symbolic-map source and its successful output. The KL/P29 duplication/peripheral comparison and root's final structural decision remain open. No blind/independent credit or historical run is claimed."),
    ]
    for tag, statement, scope in scopes:
        event_id = f"ce:III:c8:foundations:{tag}:unit"
        if any(row["event_id"] == event_id for row in rows):
            raise ValueError("Event already exists: " + event_id)
        row = dict.fromkeys(fields, "")
        row.update(statement_id=statement, date=when[:10], who=WHO,
                   type="used and rechecked in this run", outcome=scope+
                   " Exact source edits and whole-unit findings are in the local defects table and review note; final canonical/progress/page gates remain root work.",
                   event_id=event_id, phase="current", source_file=note,
                   source_event_type="used and rechecked in this run",
                   evidence_group="III-C8-FOUNDATIONS-FORMAL-AND-FINITE-REVIEW",
                   date_utc=when, where=note)
        rows.append(row)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader(); writer.writerows(rows)
    print("Recorded fourteen actual new-formal-item readings and two complete theorem-unit rereads locally.")
    print("All event types: used and rechecked in this run.")
    print("No central event table, canonical manuscript or criterion state changed.")


if __name__ == "__main__":
    main()
