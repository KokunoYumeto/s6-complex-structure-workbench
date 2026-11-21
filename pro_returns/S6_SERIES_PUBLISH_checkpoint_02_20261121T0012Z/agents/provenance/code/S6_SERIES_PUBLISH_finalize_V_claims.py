#!/usr/bin/env python3
"""Close the original 35 three-way provenance rows against current V metadata.

Additional rows cover primary inputs added or verified during the revision.
This audit adds no mathematical-check events.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parents[2]
PATH = ROOT / "S6_SERIES_PUBLISH_provenance_checks_V.tsv"
csv.field_size_limit(10**9)


def main():
    rows = list(csv.DictReader(PATH.open(), delimiter="\t"))
    tex_path = BASE / "work/S6_SERIES_PUBLISH_V.tex"
    tex = tex_path.read_text()
    meta_path = ROOT / "S6_SERIES_PUBLISH_deposit_fields_V.json"
    metadata = json.loads(meta_path.read_text())
    snapshot = json.loads((ROOT / "S6_SERIES_PUBLISH_deposit_fields_V_receipt.json").read_text())
    old_metadata = json.loads((BASE / "source/HEXAGON_METADATA_V.json").read_text())
    method_start = tex.index(r"\subsection{Methodology}")
    method_stop = tex.index(r"\subsection{", method_start + 1)
    method = " ".join(tex[method_start:method_stop].split())
    count_ok = all(phrase in method for phrase in [
        "334 examinations of proof steps", "45 independent re-derivations", "166 computations or formal certificates", "301 readings"])
    # These are statement labels, retained through reordering. Printed theorem
    # letters are deliberately not inferred from the old deposit's A--F order.
    locations = {
        "V-P01":"title block; Methodology first and final paragraphs",
        "V-P02":"Methodology paragraph 1",
        "V-P03":"Methodology paragraph 1",
        "V-P04":"Methodology paragraph 2",
        "V-P05":"Methodology count paragraph",
        "V-P06":"Methodology count and scope paragraphs",
        "V-P07":"Methodology count and scope paragraphs",
        "V-P08":"night:P1.12; integral transgression proposition; Methodology count/scope paragraph",
        "V-P09":"Methodology collaboration paragraph and linked scoped records",
        "V-P10":"Methodology collaboration paragraph and linked scoped records",
        "V-P11":"night:P1.18; Methodology numerical-check scope paragraph",
        "V-P12":"SsixRepositoryCommit macro; Methodology historical-record link; Programs table",
        "V-P13":"Methodology dedication paragraph",
        "V-P14":"The series and this paper; Known and new, series:V:A and series:V:B rows; AC26 bibliography entry",
        "V-P15":"resolved-fourfold datum; Known and new, series:V:A row; E26 bibliography entry",
        "V-P16":"known characteristic-number input; Known and new, series:V:A row; ffEsoleKang entry",
        "V-P17":"maps:src:E.1.6 and series:V:A; Known and new, series:V:A row",
        "V-P18":"series:V:D; Known and new, series:V:D row; ffMandal entry",
        "V-P19":"series:V:E; Known and new, series:V:E row; DGKX2026v1 entry",
        "V-P20":"classical primitive exterior-square input; pubLieGroups2016 entry",
        "V-P21":"maps:src:F.2.5, maps:src:F.3.6--7; Known and new, series:V:B/C rows; Yang2026 entry",
        "V-P22":"maps:src:F.3.8--11; Known and new, series:V:F row; IVVOkaOneV5 entry",
        "V-P23":"maps:src:F.3.4; ffDeligne entry",
        "V-P24":"maps:src:F.3.9--11; ffForstnericPrezelj02 entry",
        "V-P25":"series:V:D; night:P1.13; maps:src:F.4.1; IVVWallForm entry",
        "V-P26":"series:V:D; maps:src:F.4.1; IVVKramerStolz entry",
        "V-P27":"night:P1.13; maps:src:F.4.1; ffPetersSterk entry",
        "V-P28":"maps:src:F.2.36--39; Known and new, series:V:F row; rootBHJ22 entry",
        "V-P29":"maps:src:F.4.1; Known and new, series:V:D row; ffMandal entry",
    }
    claims = {
        "V-P01":"The text is AI-authored and no human has checked the mathematics.",
        "V-P02":"GPT-5.6 Sol (OpenAI), Codex, reasoning effort ultra, wrote the working edition on 24 August--9 September 2026.",
        "V-P03":"GPT-6 Astra (OpenAI), ChatGPT Pro mode, performed the stated research, derivation and writing phases and this 20 November revision; current reasoning effort was inherited and no separate numerical setting was exposed.",
        "V-P04":"Claude Fable 5.2 (Anthropic), at high and max, and Claude Opus 5.5 (Anthropic), at max, undertook the recorded readings and computations on 12--20 November 2026.",
        "V-P05":"Current V statement scopes have 334 proof-step examinations, 45 independent re-derivations, 166 computations/certificates, 301 readings and 86 background-use associations; outlines separately have 8 examinations and 3 re-derivations.",
        "V-P06":"Checks are reported by kind and exact outcome scope; no claim that every statement received all methods or that every historical check independently re-derived every step is retained.",
        "V-P07":"Totals count statement--check associations, with each original association counted once; unsupported distributions of independent runs and a median are omitted.",
        "V-P08":"Current exact integer calculations and scoped proof rereadings cover the torsion-transgression chain; the old single-run exception is not repeated.",
        "V-P09":"The Opus review's inspected passages and computations, including its explicit integral-topology limitation, are preserved in the records and accurately described in the deposit.",
        "V-P10":"The Fable review is described as comparison of introductory statements/outlines with cited body statements, with its recorded scope preserved.",
        "V-P11":"The interval certificate, separately implemented numerical comparison and exact coverage/sign checks have their respective recorded scopes; these current computations were under GPT-6 Astra.",
        "V-P12":"The full immutable commit identifies historical files; new publication-revision records are described as accompanying the current source distribution.",
        "V-P13":"The work is dedicated under CC0 1.0 Universal at the canonical Creative Commons URL.",
        "V-P14":"The initial complex six-spheres and their relevant topology/specialization inputs are credited to Claude and L. Alpöge's original manuscript.",
        "V-P15":"Engel supplies the specified elliptic surface and Weierstrass equation, cited at arXiv v1 section 2 p.3.",
        "V-P16":"Esole--Kang supplies the universal characteristic polynomials at equations (1.2)--(1.4), printed pp.3--4.",
        "V-P17":"Jia--Meng Theorem 1.1 and Remark 1.2 p.2 supply the Kaehler modification used in the class-C exclusion.",
        "V-P18":"Mandal Corollary 1.4 p.4 supplies the almost-complex existence criterion; the compact integrable realization is the contribution of V.",
        "V-P19":"DGKX v1 is credited for the weighted-base and direct-image method, with its rank-two source scope explicit.",
    }
    primary_updates = {
        "V-P15":"Official https://arxiv.org/pdf/2609.38442v1 opened: section 2, printed/PDF p.3, contains j=1728t, fibre types IV*, III, I1 and the Weierstrass equation. Lemma 7.6 p.21 also opened. Receipt: literature/S6_SERIES_PUBLISH_Engel_DGKX_receipt.json.",
        "V-P16":"Official https://arxiv.org/pdf/1807.08755v1 opened: equation (1.2) printed p.3/PDF p.4; (1.3)--(1.4) printed p.4/PDF p.5. PDF SHA256 69bb3819230a1ed2c7f44d1289c5cd86b5661ce90066be2430e939ed63f0aa42.",
        "V-P17":"Official https://arxiv.org/pdf/2201.06748v1 opened: Theorem 1.1 and Remark 1.2 printed/PDF p.2. PDF SHA256 919fefb36a82745d62717c03b8efd5d9d5dfdf6a36851b539d77481c88a1f6fd.",
        "V-P18":"Official https://arxiv.org/pdf/2609.27929v1 opened: Corollary 1.4 p.4. PDF SHA256 062e16c766eb19182417093f8d1088981d3444c4f1b01f5794199a94d26b42cb.",
        "V-P19":"Official https://arxiv.org/pdf/2610.00250v1 opened: Lemma 6.1 p.74, Lemma 6.2 pp.74--75, Proposition 6.5 p.76, Proposition 6.6 p.77 and Proposition 6.10 pp.79--80. The last proposition concerns a two-dimensional torus family. PDF SHA256 7facc6e55c7a578315a981224c45f184d3033b6159773304968508aca2710ab3.",
        "V-P22":"Official arXiv v5 PDF: Definition 7.11, Remark 7.12 and the observation before Proposition 7.13 p.23; Proposition 7.13(a,b) p.23, (c,d) p.24, with the bundle assertion in (d). Official Springer metadata opened: Math. Z.311, article33 (2025), DOI10.1007/s00209-025-03833-4. Exact v5 pages remain the cited locators.",
        "V-P25":"Authors' primary v3 PDF opened at section 3.3 pp.11--12, Definition 3.6 p.12 and Theorem 3.7(1) pp.13--14. Official Cambridge publication metadata independently opened: J. Aust. Math. Soc.115(2),172--203(2023), DOI10.1017/S1446788722000167. Version-specific locators remain explicit.",
        "V-P29":"Official https://arxiv.org/pdf/2609.27929v1 opened: Lemma 2.1 p.5 and Theorem 2.4 p.7 give p1(HP2)=2alpha, p2=7alpha^2 and the connected-sum formulas. The official PDF pages now independently confirm the previously checked TeX labels.",
    }
    current_by_id = {}
    for row in rows:
        if row["claim_id"] not in {f"V-P{x:02d}" for x in range(1,30)} | {"V-N"+x for x in "ABCDEF"}:
            continue
        identity = row["claim_id"]
        row.setdefault("prior_claim", row["claim"])
        row.setdefault("prior_records_assessment", row["against_records"])
        row.setdefault("prior_recomputation_assessment", row["by_recomputation"])
        row.setdefault("prior_primary_assessment", row["against_primary_source"])
        row["claim"] = claims.get(identity, row["claim"])
        row["current_paper_location"] = locations.get(identity, "")
        row["current_deposit_location"] = "Provenance: How it was checked" if identity in {f"V-P{x:02d}" for x in range(5,12)} else "Provenance; Comments where applicable"
        row["resolution_status"] = "resolved at the recorded current-source snapshot"
        row["required_action"] = "Resolved in the listed current source and deposit locations; final publication snapshot must retain this exact scope."
        row["remaining_gate"] = ""
        row["old_HEXAGON_disposition"] = "Retained with exact present scope; the attached original metadata remains unchanged."
        row["current_resolution"] = "Current manuscript and proposed deposit agree with the specified source and recorded scope."
        if identity in primary_updates:
            row["against_primary_source"] = primary_updates[identity]
        if identity in {"V-P01","V-P02","V-P03","V-P04"}:
            row["against_records"] = "Matched to PROMPT section 4.1, the attached design/intake/review bylines and the current event who/date fields. Current effort disclosure states only the inherited setting actually exposed in this session."
            row["by_recomputation"] = "No numerical claim for this row; date/model strings were compared with the supplied records and current metadata."
        if identity == "V-P05":
            row["against_records"] = "The 7413-row merged ledger preserves the 7258 supplied baseline/post-cp10 rows and the 155 current scoped agent associations; zero exact duplicates were removed."
            row["by_recomputation"] = "Recomputed from the latest nine agent TSVs: 121 current environments,126 retained statement identifiers,932 associations,885 declared evidence groups; targeted334,re-proof45,computation166,used301,background86. Outlines separately8 targeted+3 re-proof. See deposit receipt and records_current_V."
            row["old_HEXAGON_disposition"] = "Replaced the unverifiable run-frequency distribution by typed association counts; the supplied old metadata is preserved as evidence."
            if not count_ok:
                row["resolution_status"] = "awaiting root methodology count synchronization"
                row["remaining_gate"] = "Set current methodology to334/45/166/301 and preserve separate outline8+3 before final build."
        if identity in {"V-P06","V-P07"}:
            row["old_HEXAGON_disposition"] = "The universal/median/separate-run wording is removed from the proposed deposit; positive kind/count/scope wording replaces it."
            row["current_resolution"] = "The methodology explicitly counts links and records examined scope; the deposit uses the same convention."
        if identity == "V-P08":
            row["old_HEXAGON_disposition"] = "The old one-run exception is replaced by the exact current integer-computation and proof-reading scopes."
        if identity in {"V-P09","V-P10"}:
            row["old_HEXAGON_disposition"] = "The older 'found no fault' descriptions are replaced by the passages and calculations actually examined, without asserting a whole-proof check."
        if identity == "V-P11":
            row["old_HEXAGON_disposition"] = "The GPT-6 provenance of the interval remains explicit; new numerical and finite-certificate checks are added with their own scope."
        if identity == "V-P12":
            row["by_recomputation"] = "Full commit resolution and raw file hashes checked; all53 program paths opened or covered by a matching primary raw-source receipt. Current publication artifacts are not assigned to the historical commit."
            row["old_HEXAGON_disposition"] = "The short hash is expanded; historical availability and the current accompanying source distribution are stated explicitly."
        if identity == "V-P13":
            row["current_deposit_location"] = "Provenance final paragraph; Licence field"
        if identity == "V-P19":
            row["current_resolution"] = "The opening table now says 'Weighted-base and direct-image method'; V proves its own rank-three calculation."
        if identity.startswith("V-N"):
            stable = identity[-1]
            row["current_paper_location"] = f"Abstract; series:V:{stable} literature-status line; Known and new row for series:V:{stable}"
            row["current_deposit_location"] = "Abstract; Comments"
            row["resolution_status"] = "resolved as a scoped contribution claim after bounded literature review"
            row["current_resolution"] = "The contribution is stated at the manuscript's exact scope and known inputs are credited at their locators. The search log supplies bounded evidence; no claim of an exhaustive proof of priority is made."
            row["required_action"] = "Retain the exact contribution scope and known-input credits; do not strengthen the wording to an unverified priority claim."
            row["by_recomputation"] = "No check-count or bibliometric assertion. The current contribution was compared with the cited source statements; mathematical calculations are the separately logged analytic/topology checks."
            if stable == "A":
                row["claim"] = "New compact smooth fourfold obtained by a small crepant resolution of its Weierstrass model, bimeromorphic to the indicated elliptic fibre product, with the stated invariants."
                row["old_HEXAGON_disposition"] = "The old abstract's phrase 'small crepant resolution of the transverse elliptic fibre product' is replaced by the exact Weierstrass-resolution morphism and its bimeromorphic relation to the product."
        if identity == "V-P22" and "10.1007/s00209-025-03833-4" not in tex:
            row["remaining_gate"] = "Apply the verified published Oka metadata to the standalone bibliography while retaining the v5 locator note. Shared-bibliography guarded patch supplied."
        if identity == "V-P29":
            row["required_action"] = "Resolved: exact official v1 pages5 and7 now independently confirmed; retain these pages."
        row["evidence"] += "; current source:work/S6_SERIES_PUBLISH_V.tex; current deposit:agents/provenance/S6_SERIES_PUBLISH_deposit_fields_V.json"
        current_by_id[identity] = row

    assert len(current_by_id) == 35
    additions = [
        ("V-P30", "Almost-complex Todd integrality applies to the characteristic-number argument.",
         "Known characteristic-number input; HirzebruchTopologicalMethods entry",
         "The topology agent independently reconstructed the characteristic-number argument, then opened the cited source at its almost-complex scope.",
         "The independent exact arithmetic yields c2^2=2,p1^2=8,p2=14,signature2 from Euler6 and the rank-four signature bound; see topology check outputs. This row awards no additional mathematical check.",
         "Official archive https://hirzebruch.mpim-bonn.mpg.de/id/eprint/114/1/M2_Topological%20methods.pdf: printed pp.183--184/PDF pp.194--195, Theorems24.5.3--24.5.4 and the Todd-genus integrality corollary. Both pages visually opened by topology agent; receipt agents/v_topology/S6_SERIES_PUBLISH_V_Hirzebruch_source_check.json."),
        ("V-P31", "The program table's historical files are present at the exact immutable pin, and current independent checks are kept in the source-distribution records.",
         "Programs table; SsixRepositoryCommit macro; Methodology availability paragraph",
         "All49 historical names removed or retained in the editorial chunks were preserved, plus4 operative interval modules. Nine diagnostic/reconstruction/old-loop files stay in the check records;44 programs appear in19 table rows.",
         "53 unique historical files:13 match supplied cp10 manifest size/SHA and40 match immutable cp15 Git blob IDs; every opened raw URL returned200. No mathematical check events were added by this verification.",
         "Pinned commit83d76022bcd442278b760db9ff438afceed6c6ea opened directly; immutable cp15 III/V trees and raw sources checked. Receipts: S6_SERIES_PUBLISH_V_program_path_receipt.json; analytic pinned-program receipt; merged programs_all.tsv."),
        ("V-P32", "AC26 section7.7 is cited at its verified printed span pp.60--63.",
         "Known and new, series:V:B row",
         "Original attached108-page PDF used as the controlling source, with fresh extraction of the section and heading boundaries.",
         "The extracted printed-page span was compared with the source PDF: section begins60; Lemma7.25/Proposition7.26 at61; Proposition7.27 at62--63; Corollary7.29 at63 before section8.",
         "Original AC26 PDF and exact locator receipt S6_SERIES_PUBLISH_AC26_section_7_7_receipt.json; the previous estimated pp.60--64 was corrected before final use."),
        ("V-P33", "Catanese Theorem2.1 p.264 supplies the persistence of complex tori under deformation.",
         "Known and new, series:V:E row; Catanese2004 entry",
         "Matches the torus-deformation input used in the current period-family argument; current source statement read at its cited page.",
         "No numerical claim; the theorem and immediately preceding marked-torus parameterization were compared with the cited use.",
         "Author-hosted published PDF https://www.mathe8.uni-bayreuth.de/de/team/prof-fabrizio-catanese-old/pdf/085.pdf, printed p.264/PDF p.4, Theorem2.1. Receipt literature/S6_SERIES_PUBLISH_Catanese_receipt.json."),
        ("V-P34", "The Gronwall and Cauchy formulas used by the interval continuation have exact primary locators.",
         "night:P1.18; TeschlODE2012 and DLMFCauchy2026 entries",
         "Analytic agent opened both primary formulas and retained their roles in the rational-connection continuation bound.",
         "Bibliographic verification only, with zero additional mathematical events.",
         "Teschl author PDF, Lemma2.7 and equation(2.36), printed pp.42--43/PDF pp.53--54; DLMF https://dlmf.nist.gov/1.9 section1.9(iii), equations1.9.30--1.9.31. Exact analytic-agent locator receipts under agents/v_analytic/literature/."),
    ]
    for identity, claim, location, records, computation, primary in additions:
        current_by_id[identity] = {
            "claim_id":identity,"paper":"V","locations":location,"claim":claim,
            "against_records":records,"by_recomputation":computation,"against_primary_source":primary,
            "required_action":"Resolved at the listed source scope; retain the exact locator and availability wording.",
            "evidence":primary,"prior_claim":"supplemental current-revision claim",
            "current_paper_location":location,"current_deposit_location":"Comments or Provenance where applicable",
            "resolution_status":"resolved at the recorded current-source snapshot","remaining_gate":"",
            "old_HEXAGON_disposition":"The old metadata makes no more specific claim; the current source and records now supply this precision.",
            "current_resolution":"Primary statement/page or immutable file identity checked as stated; no new mathematical event claimed."}
    final = [current_by_id[row["claim_id"]] for row in rows if row["claim_id"] in current_by_id and row["claim_id"] not in {x[0] for x in additions}]
    final.extend(current_by_id[x[0]] for x in additions)
    assert len(final) == 40
    fields = list(dict.fromkeys(field for row in final for field in row))
    with PATH.open("w", newline="") as handle:
        writer = csv.DictWriter(handle,fieldnames=fields,delimiter="\t")
        writer.writeheader();writer.writerows(final)
    receipt = {
        "created_utc":datetime.now(timezone.utc).isoformat(),"original_rows_closed":35,"supplemental_rows":5,
        "rows":len(final),"paper_source_sha256":hashlib.sha256(tex_path.read_bytes()).hexdigest(),
        "deposit_fields_sha256":hashlib.sha256(meta_path.read_bytes()).hexdigest(),
        "old_HEXAGON_sha256":hashlib.sha256((BASE / "source/HEXAGON_METADATA_V.json").read_bytes()).hexdigest(),
        "ledger_snapshot":snapshot,"methodology_counts_match_snapshot":count_ok,
        "remaining_claim_actions":[{"claim_id":row["claim_id"],"gate":row["remaining_gate"]} for row in final if row["remaining_gate"]],
        "separate_final_gate":"The rendered final PDFs have not been certified by this metadata/provenance audit; root owns their final page readings.",
        "mathematical_events_added":0,
        "novelty_scope":"Bounded source/search review supports scoped contribution wording; no exhaustive priority claim is certified."}
    (ROOT / "S6_SERIES_PUBLISH_V_provenance_disposition_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n")
    report = ["# Paper V provenance dispositions", "", f"All 35 original claim rows were compared with the current manuscript, the proposed deposit fields and the preserved original deposit. Five supplemental rows cover the almost-complex index input, program paths, AC26 section pagination, Catanese, and the analytic error-bound citations.", "",
              "The current count snapshot has 7,413 merged ledger rows. Paper V has 121 statement environments and 126 retained subject identifiers, with 932 associations: 334 targeted examinations, 45 independent re-derivations, 166 computations/certificates, 301 readings and 86 background uses. The outlines add eight targeted examinations and three re-derivations separately. No metadata operation was counted as a mathematical check.", "",
              "The proposed deposit uses the current abstract verbatim apart from whitespace. It preserves the exact Weierstrass-resolution morphism and the bimeromorphic relation to the fibre product. It removes the old unsupported run-frequency/median assertions and states the recorded scopes of the Opus and Fable reviews. The inherited current reasoning effort is disclosed without inventing a numeric setting.", "",
              "All historical program links use the full verified commit. Current-revision additions are described as accompanying the source distribution. Published Conway and Oka metadata are paired with the exact author-version/preprint locators actually checked.", "",
              "## Remaining gates", ""]
    gates = receipt["remaining_claim_actions"]
    report.extend([f'- {x["claim_id"]}: {x["gate"]}' for x in gates] or ["- No open source-level provenance correction at this recorded snapshot."])
    report.extend(["- Regenerate the counts and metadata after any later ledger or statement-scope change.", "- Final rendered-page reading and the full five-paper completion gates remain with root; this audit does not certify them.", ""])
    (ROOT / "S6_SERIES_PUBLISH_V_provenance_dispositions.md").write_text("\n".join(report))
    print(json.dumps({key:receipt[key] for key in ["original_rows_closed","supplemental_rows","rows","methodology_counts_match_snapshot","remaining_claim_actions","mathematical_events_added"]},indent=2))


if __name__ == "__main__": main()
