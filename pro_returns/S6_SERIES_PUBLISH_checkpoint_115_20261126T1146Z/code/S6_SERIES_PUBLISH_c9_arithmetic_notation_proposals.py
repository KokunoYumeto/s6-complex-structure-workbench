#!/usr/bin/env python3
"""Guarded residual arithmetic-name corrections, with exact reverse maps."""
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
    sid = "maps:src:D.2.37"
    t = statement(sid)
    old = between(t, r"Choose integers \(A,B_0,C_0\)", "The fixed sweeps of")
    new = (old.replace("A,B_0,C_0", r"A_{\rm Bez},B_{\rm Bez},C_{\rm Bez}")
           .replace("qA+qdbz_2B_0-qdbz_1C_0", r"qA_{\rm Bez}+qdbz_2B_{\rm Bez}-qdbz_1C_{\rm Bez}")
           .replace("(A e_{12}+B_0e_{14}+C_0e_{24})", r"(A_{\rm Bez} e_{12}+B_{\rm Bez}e_{14}+C_{\rm Bez}e_{24})"))
    def undo(s):
        return s.replace(r"A_{\rm Bez}", "A").replace(r"B_{\rm Bez}", "B_0").replace(r"C_{\rm Bez}", "C_0")
    add("02LD-Bezout-section-coefficients", sid, old, new,
        "The same paragraph returns to monodromy A(d)H_d=H_dA(1) after using A as a scalar coefficient; C_0 also names the zero component in this proof. The section coefficients receive A_Bez,B_Bez,C_Bez. The identity on integer triples preserves the exact Bezout equation, its wedge-vector section, the image W and the two composites modulo the unchanged primitive relations. All monodromy matrices and component names remain fixed.", undo)

    old = between(t, r"Let \(A=A_i(d)\)", r"\emph{Regular logarithms and clutch.}")
    names("02LD-finite-projection-and-norm-maps", sid, old,
        {"P": r"\mathsf P_{\rm fix}", "Q": r"\mathsf Q_{\rm norm}", "F": r"F_{\rm fix}"},
        "The global sections P and Q remain fixed in the marked line construction, and F already denotes the whole-fibre multiplicity vector in the preceding nonzero-Chern cap. In the finite-cap arithmetic, the fixed-basis matrix becomes F_fix, the projector N_h/h becomes mathsf P_fix and the surjective norm-coordinate matrix H^{-1}F_fix^{-1}N_h becomes mathsf Q_norm. Every bare-matrix use through the freeness, torsion, normal-character and Thom-column arguments is updated, including products with R_pi. Indexed F_0 for the central quotient and F_1 for the explicitly chosen weight-one fixed basis are retained. The identity on matrix entries and their source/target lattices preserves kernels, projected lattices, exact sections, obstruction indices and torsion identifications. The full finite-cap block was read; all parameters and inverse translations are unchanged under exact reversal.", skip_subscript=True)

    old = between(t, "An explicit kernel algorithm retains", "For each such basis vector")
    names("02LD-relative-disc-matrices", sid, old,
        {"P": r"\mathsf P_{\rm log}", "M": r"\mathsf M_{\rm disc}"},
        "The later global relative calculation uses the same letters P and M as the elliptic section and its line bundle E(M). Its integer power-relation matrix and component-disc boundary matrix become mathsf P_log and mathsf M_disc. The equation M_disc z=P_log z-prime and its block kernel have identical integer entries. Identity on relation coefficients proves that projection, unique recovery of z-prime, Hermite basis and the following closed-cycle splitting are unchanged. These matrices are also separate from the finite-cap fixed-plane projector above.")

    sid = "maps:src:D.2.42"
    t = statement(sid)
    old = between(t, r"On \(C_f\), set \(A=a(\nu-k)\)", r"At \(E_3\)")
    names("02LJ-localization-edge-coefficient", sid, old, {"A": r"a_{\rm edge}"},
        "A is the marked elliptic monodromy and the linear deck map in this proof. The degree a(nu-k) of the restricted cohomology class is now a_edge. Its declaration, ordinary degree, restriction rho_3(a_edge z_C), cube and every localization term are renamed together. The coordinatewise identity on that integer leaves both cohomology classes and the exact mod-nine integral unchanged; all Euler factors, weights, labels and detector maps remain. The complete C_f localization block was read and compared with cp100.")

    sid = "maps:src:D.2.48"
    t = statement(sid)
    old = between(t, "Choose integers $B,C$ with", "The root-loop exponent")
    names("02LP-detector-character-and-kernel-coefficients", sid, old,
        {"B": r"b_{\chi}", "C": r"c_{\chi}", "A": r"a_{\rm ker}"},
        "B already denotes the complete normal relation matrix, C the critical cycle used by the subsequent linking calculation, and the adjacent paragraph uses A for the elliptic monodromy. The detector character values become b_chi,c_chi and the scalar in a_ker m_1+K n_1=1 becomes a_ker. The identity on the three integer choices preserves chi, its connected kernel fibre N, the loops h and q, their common generator t and all inverse base coordinates. K and its root-loop exponent are unchanged. The immediately following monodromy A and the later critical cycle C retain their meanings. The earlier independent Bezout choice A,B_0 is explicitly bound to its separate normal-column calculation and remains local.")


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
        p["change_id"] = f"CLAUDE-III-P15-ARITHMETIC-{i:03d}"
        p["cp100_line"] = original.count("\n", 0, matches[0].start())+1
        defects.append(dict(change_id=p["change_id"], type="D20", statement_id=p["statement_id"],
            old_location=f"cp100 source line {p['cp100_line']}; tag {p['tag']}",
            old_page="current page concordance pending", new_location="same scoped arithmetic block; "+p["name"],
            new_page="pending current rendered-PDF review", old_text=p["old"], new_text=p["new"], reason=p["reason"],
            review_status="Every affected arithmetic block, active defining context and dependent formula read "+now+"; proposed for root admission; cp100 comparison and exact reverse map pass; no independent whole-proof or PDF-page credit."))
        print(p["change_id"], p["statement_id"], p["name"])
    for j, sid in enumerate(dict.fromkeys(p["statement_id"] for p in PROPOSALS), 1):
        names_here = [p["name"] for p in PROPOSALS if p["statement_id"] == sid]
        eid = f"publish:c9:III:arithmetic-notation:{j:03d}"
        row = {k: "" for k in ef}
        row.update(statement_id=sid, date=now[:10], who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation nine global notation reviewer",
            type="used and rechecked in this run", outcome="Read the full affected arithmetic blocks, active definitions and each dependent expression for "+", ".join(names_here)+". Their identity coefficient/matrix maps and exact reverse names are documented in D20. Original cp100 comparison, current guards, targets/citations and exact reversal pass. This records scoped use and comparison, with no independent whole-proof or PDF-page claim.",
            event_id=eid, phase="continuation9 Paper III arithmetic notation", source_file="code/S6_SERIES_PUBLISH_c9_arithmetic_notation_proposals.py",
            source_event_type="used and rechecked in this run", evidence_group=eid, date_utc=now,
            where="agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_arithmetic_notation_proposals.json")
        events.append(row)
    restored = candidate
    for p in reversed(PROPOSALS):
        assert restored.count(p["new"]) == 1
        restored = restored.replace(p["new"], p["old"], 1)
    assert restored == SOURCE
    targets = lambda s: Counter(re.findall(r"\\(?:label|hypertarget)\{[^{}]+\}", s))
    assert targets(SOURCE) == targets(candidate)
    (OWN / "S6_SERIES_PUBLISH_c9_arithmetic_notation_proposals.json").write_text(json.dumps(PROPOSALS, ensure_ascii=False, indent=2)+"\n", encoding="utf-8", newline="\n")
    for name, fields, rows in [("S6_SERIES_PUBLISH_c9_arithmetic_notation_defects.tsv", df, defects), ("S6_SERIES_PUBLISH_c9_arithmetic_notation_events.tsv", ef, events)]:
        with (OWN / name).open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader(); writer.writerows(rows)
    print(f"Prepared {len(PROPOSALS)} exact proposals and {len(events)} scoped events; cp100 guards, formal owners, targets and exact reverse maps pass.")


if __name__ == "__main__":
    main()
