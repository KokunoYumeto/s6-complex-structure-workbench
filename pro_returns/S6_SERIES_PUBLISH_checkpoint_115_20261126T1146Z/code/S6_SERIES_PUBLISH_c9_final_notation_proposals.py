#!/usr/bin/env python3
"""Final context-read P15 guards; leaves shared source and tables to root."""
from collections import Counter
import csv
from datetime import datetime, timezone
import json
import re
from zipfile import ZipFile

from S6_SERIES_PUBLISH_c9_scoped_notation_proposals import (
    ROOT, OWN, SOURCE, PROPOSALS, statement, between, add, names,
)


def prepare():
    sid = "maps:src:D.2.26"
    t = statement(sid)
    old = between(t, "Choose integers $A,B,C$ with", "Also $\\operatorname{im}(A-I)")
    new = (old.replace("$A,B,C$", r"$A_{\rm Bez},B_{\rm Bez},C_{\rm Bez}$")
           .replace("qA+qz_{Q,2}B-qz_{Q,1}C", r"qA_{\rm Bez}+qz_{Q,2}B_{\rm Bez}-qz_{Q,1}C_{\rm Bez}")
           .replace("(Ae_{12}+Be_{14}+Ce_{24})", r"(A_{\rm Bez}e_{12}+B_{\rm Bez}e_{14}+C_{\rm Bez}e_{24})"))
    add("02L1-Bezout-coefficients", sid, old, new,
        "The coefficient A is followed immediately by the active monodromy A in im(A-I), and coefficient C appears beside the component class [C]. The three coefficient names become A_Bez,B_Bez,C_Bez. Their values and equation are unchanged; the coefficientwise identity from the original triple to the renamed triple carries the displayed section vector to itself. Both section composites and all matrix and component symbols therefore stay fixed. The suffix avoids the existing affine-translation b_0 later in this proof.",
        lambda s: s.replace(r"A_{\rm Bez}", "A").replace(r"B_{\rm Bez}", "B").replace(r"C_{\rm Bez}", "C"))

    sid = "maps:src:D.2.42"
    t = statement(sid)
    old = "\\(qA+qz_{Q,2}B-qz_{Q,1}C=1\\), followed by \\(\\wedge^2S_P^{-1}\\),"
    new = r"\(qA_{\rm Bez}+qz_{Q,2}B_{\rm Bez}-qz_{Q,1}C_{\rm Bez}=1\), followed by \(\wedge^2S_P^{-1}\),"
    add("02LJ-Bezout-coefficients", sid, old, new,
        "The preceding original-cap construction uses monodromy A and the component class [C]. The Bezout coefficients in its section equation receive A_Bez,B_Bez,C_Bez. The identity on integer triples preserves the equation and its section under wedge^2 S_P^{-1}; [C] and every matrix are unchanged. The suffix also avoids c_0, the actual central-surface group generator in the following finite-cap construction.",
        lambda s: s.replace(r"A_{\rm Bez}", "A").replace(r"B_{\rm Bez}", "B").replace(r"C_{\rm Bez}", "C"))

    sid = "maps:src:D.2.40"
    t = statement(sid)
    old = between(t, "In a free presentation of the exterior degree-one group", r"\emph{The full fundamental group for all weights and orders.}")
    names("02LH-relative-disc-matrices", sid, old,
        {"P": r"\mathsf P_{\rm log}", "M": r"\mathsf M_{\rm disc}"},
        "P is the fixed elliptic section and M the section line, whose circle bundle E(M) was used in the cap calculation. The log-relation matrix and component-disc boundary matrix receive mathsf P_log and mathsf M_disc. Every matrix use in the integral kernel equation, injectivity argument and relative splitting is renamed together, including the retained g delta relation. The identity on rows and columns proves that the kernel, its projection to z, the unique z-prime inverse, its Hermite basis, and the resulting closed cycles are unchanged. The source matrix identity (MN-I)x earlier in the proof has explicitly bound arbitrary matrices and is untouched.")

    sid = "maps:src:D.2.17"
    t = statement(sid)
    old = between(t, "Let $D_0$ be the first three rows", "For the regular log,")
    new = old.replace("D_0", r"\mathsf D_0")
    add("02KR-graph-row-matrix", sid, old, new,
        "D_0 denotes the first three graph rows here, but later D_0 denotes a normal disc in D_0+m(D_1+D_2+D_3). The graph matrix becomes mathsf D_0 at its declaration and every subsequent matrix formula. Its entries, right inverse C, graph splitting K,L and integral vanishing relations are identical. The normal discs retain D_i. The complete 478-line statement/proof was read for this naming decision; the exact reverse matrix-name map recovers all changed formulas.",
        lambda s: s.replace(r"\mathsf D_0", "D_0"))
    old = between(t, "Let $Q$ be the smooth oriented quotient", r"\end{proof}")
    names("02KR-circle-quotient-name", sid, old, {"Q": r"\mathcal Q"},
        "The statement fixes elliptic section Q=G, and the original-cap calculation uses Q_0=-q_tor. The later smooth circle quotient and its tube complement become mathcal Q and mathcal Q_0, with all dependent quotient primes, fixed-curve subscripts, tangent/Stiefel-Whitney terms, suspension and surgery references updated throughout the remainder of the proof. This denotes precisely the same orbit space, open subset and maps; the identity on orbit classes induces the unchanged homology, Gysin and reconstruction maps. The complete statement/proof was read, and the reverse name map fixes every gluing, inverse, orientation and cited statement.")


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
        p["change_id"] = f"CLAUDE-III-P15-FINAL-{i:03d}"
        p["cp100_line"] = original.count("\n", 0, matches[0].start())+1
        defects.append(dict(change_id=p["change_id"], type="D20", statement_id=p["statement_id"],
            old_location=f"cp100 source line {p['cp100_line']}; tag {p['tag']}",
            old_page="current page concordance pending", new_location="same scoped proof block; "+p["name"],
            new_page="pending current rendered-PDF review", old_text=p["old"], new_text=p["new"], reason=p["reason"],
            review_status="Exact old/new blocks and their active defining contexts read "+now+"; proposed for root admission; original cp100 comparison and exact reverse map pass; no independent-proof or PDF-page credit."))
        print(p["change_id"], p["statement_id"], p["name"])
    for j, sid in enumerate(dict.fromkeys(p["statement_id"] for p in PROPOSALS), 1):
        names_here = [p["name"] for p in PROPOSALS if p["statement_id"] == sid]
        eid = f"publish:c9:III:final-notation:{j:03d}"
        row = {k: "" for k in ef}
        row.update(statement_id=sid, date=now[:10], who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation nine global notation reviewer",
            type="used and rechecked in this run", outcome="Read the original cp100 and current blocks, the active defining contexts and all changed expressions for "+", ".join(names_here)+". The D20 rows give identity maps on the named coefficients, matrix coordinates or orbit classes and their exact reverse names. All targets/citations are fixed. This records scoped use and comparison; complete reading of 02KR is separately documented in its reasons, and no independent proof or PDF-page review is claimed.",
            event_id=eid, phase="continuation9 Paper III final notation", source_file="code/S6_SERIES_PUBLISH_c9_final_notation_proposals.py",
            source_event_type="used and rechecked in this run", evidence_group=eid, date_utc=now,
            where="agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_final_notation_proposals.json")
        events.append(row)
    restored = candidate
    for p in reversed(PROPOSALS):
        assert restored.count(p["new"]) == 1
        restored = restored.replace(p["new"], p["old"], 1)
    assert restored == SOURCE
    targets = lambda s: Counter(re.findall(r"\\(?:label|hypertarget)\{[^{}]+\}", s))
    assert targets(SOURCE) == targets(candidate)
    (OWN / "S6_SERIES_PUBLISH_c9_final_notation_proposals.json").write_text(json.dumps(PROPOSALS, ensure_ascii=False, indent=2)+"\n", encoding="utf-8", newline="\n")
    for name, fields, rows in [("S6_SERIES_PUBLISH_c9_final_notation_defects.tsv", df, defects), ("S6_SERIES_PUBLISH_c9_final_notation_events.tsv", ef, events)]:
        with (OWN / name).open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader(); writer.writerows(rows)
    print(f"Prepared {len(PROPOSALS)} exact proposals and {len(events)} scoped events; cp100 guards, formal owners, permanent targets and exact reverse maps pass.")


if __name__ == "__main__":
    main()
