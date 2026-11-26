#!/usr/bin/env python3
"""Guarded orbit-space name corrections after full affected-tail reading."""
from collections import Counter
import csv
from datetime import datetime, timezone
import json
import re
from zipfile import ZipFile

from S6_SERIES_PUBLISH_c9_scoped_notation_proposals import (
    ROOT, OWN, SOURCE, PROPOSALS, statement, between, names,
)


def prepare():
    sid = "maps:src:D.2.16"
    old = between(statement(sid), "Denote the closed quotient by $Q$", r"\end{proof}")
    names("02KQ-circle-quotient-name", sid, old, {"Q": r"\mathcal Q"},
        "The proof retains its elliptic section Q=G and earlier Q_0=-q_tor as the torsion translation in an original cap. The later orbit space becomes mathcal Q, with mathcal Q_0 for its tube complement and the corresponding prime, fixed-curve, tangent-bundle, collar-map, suspension and surgery names. The identity on scalar-circle orbits is the exact identification; all inverse Gysin maps, framed reconstruction maps and normal rotations are unchanged. The entire affected tail from the quotient declaration through the proof end, together with the earlier section and torsion-translation definitions, was read. The reverse name map recovers every formula and cited target.")

    sid = "maps:src:D.2.20"
    old = between(statement(sid), "Adjoin $C\\times D^3$ to the free quotient", r"\emph{The untwisted Engel member.}")
    names("02KV-circle-quotient-and-product", sid, old,
        {"Q": r"\mathcal Q", "P": r"\mathcal P"},
        "The theorem fixes sections P=G and Q=dG; the later Engel comparison again uses section P. The orbit space in this reconstruction becomes mathcal Q, and its punctured product with S^1 becomes mathcal P. These denote exactly the same quotient and product via identity on orbit classes and identity on the S^1 factor. Their complements, tangent bundles, homology maps, relative cohomology, degree-two products, framed suspensions and surgery maps therefore remain identical. The complete changed reconstruction/product/surgery block and the immediately following Engel identification were read, along with the initial section data. No section name is changed by the scope, and the exact reverse name map restores the block.")


def main():
    prepare()
    with ZipFile(ROOT.parents[1] / "upload/S6_SERIES_PUBLISH_continue_cp100.zip") as z:
        original = z.read("S6_SERIES_PUBLISH_checkpoint_100/S6_SERIES_PUBLISH_III.tex").decode("utf-8")
    now = datetime.now(timezone.utc).isoformat()
    df = next(csv.reader((ROOT / "S6_SERIES_PUBLISH_defects_III.tsv").open(), delimiter="\t"))
    ef = next(csv.reader((ROOT / "CHECK_EVENTS.tsv").open(), delimiter="\t"))
    candidate = SOURCE
    defects, events = [], []
    for i, p in enumerate(PROPOSALS, 1):
        assert candidate.count(p["old"]) == 1, (p["name"], "overlap")
        matches = list(re.finditer(r"\s+".join(re.escape(w) for w in p["old"].split()), original))
        assert len(matches) == 1, (p["name"], "cp100 comparison modulo whitespace", len(matches))
        candidate = candidate.replace(p["old"], p["new"], 1)
        p["change_id"] = f"CLAUDE-III-P15-QUOTIENT-{i:03d}"
        p["cp100_line"] = original.count("\n", 0, matches[0].start())+1
        defects.append(dict(change_id=p["change_id"], type="D20", statement_id=p["statement_id"],
            old_location=f"cp100 source line {p['cp100_line']}; tag {p['tag']}",
            old_page="current page concordance pending", new_location="same scoped proof tail; "+p["name"],
            new_page="pending current rendered-PDF review", old_text=p["old"], new_text=p["new"], reason=p["reason"],
            review_status="Full affected quotient/reconstruction blocks and initial section data read "+now+"; proposed for root admission; original cp100 comparison and exact reverse map pass; no independent-proof or PDF-page credit."))
        eid = f"publish:c9:III:quotient-notation:{i:03d}"
        row = {k: "" for k in ef}
        row.update(statement_id=p["statement_id"], date=now[:10], who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation nine global notation reviewer",
            type="used and rechecked in this run", outcome="Read the complete affected quotient/reconstruction block and active initial section data for "+p["name"]+". The new names identify the identical orbit space and product by identity on orbit classes and the circle factor. Original cp100 guard, exact reversal and preservation of all targets/citations pass. This records the scoped comparison and gives no independent whole-proof or PDF-page credit.",
            event_id=eid, phase="continuation9 Paper III quotient notation", source_file="code/S6_SERIES_PUBLISH_c9_quotient_notation_proposals.py",
            source_event_type="used and rechecked in this run", evidence_group=eid, date_utc=now,
            where="agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_quotient_notation_proposals.json")
        events.append(row)
        print(p["change_id"], p["statement_id"], p["name"])
    restored = candidate
    for p in reversed(PROPOSALS):
        assert restored.count(p["new"]) == 1
        restored = restored.replace(p["new"], p["old"], 1)
    assert restored == SOURCE
    targets = lambda s: Counter(re.findall(r"\\(?:label|hypertarget)\{[^{}]+\}", s))
    assert targets(SOURCE) == targets(candidate)
    (OWN / "S6_SERIES_PUBLISH_c9_quotient_notation_proposals.json").write_text(json.dumps(PROPOSALS, ensure_ascii=False, indent=2)+"\n", encoding="utf-8", newline="\n")
    for name, fields, rows in [("S6_SERIES_PUBLISH_c9_quotient_notation_defects.tsv", df, defects), ("S6_SERIES_PUBLISH_c9_quotient_notation_events.tsv", ef, events)]:
        with (OWN / name).open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader(); writer.writerows(rows)
    print(f"Prepared {len(PROPOSALS)} exact proposals and {len(events)} scoped events; cp100 guards, formal owners, permanent targets and exact reverse maps pass.")


if __name__ == "__main__":
    main()
