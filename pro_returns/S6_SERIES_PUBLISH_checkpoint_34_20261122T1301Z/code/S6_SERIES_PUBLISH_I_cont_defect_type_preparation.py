#!/usr/bin/env python3
"""Prepare Paper I's 25 individual type dispositions without changing status files.

The inherited proof/comparison evidence is retained with its original scope.
Actual image reading, contextual review and reversible source transport have
separate records. This script creates no mathematical-check event.
"""
from pathlib import Path
import collections
import csv
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "agents/i_cont_edits"
EXPECTED_SOURCE = "45bf46fc14a50f7a148cdd34bf2be68b04cd89e1cb7d620191c6e8518f7249f8"
EXPECTED_PDF = "b72c6da6acddfd797c82837fbd086e222eeef8e4526ed736328affde474df780"
BASE_SOURCE = "26a6f5f8b1e911de363bed7346e970bc8fb77b21cf04fe9a2ce4d1f90d95b49e"
C14_SOURCE = "1f2d0d376f71e7843265976aeeb72cf8e1ff77aea176ff5dbb4e67446c25b36f"
C14_PDF = "1abe0fc16350045cd2ce0aae57ce377dcfe2400de0b0bf58ba7e559d360bcb37"
CORE_FIELDS = ["change_id", "type", "statement_id", "old_text", "new_text", "reason"]
sha = lambda data: hashlib.sha256(data).hexdigest()
csv.field_size_limit(100_000_000)


def read_json(path):
    return json.loads((ROOT / path).read_text())


def relocated(path):
    prefix = "/workspace/scratch/653608133b22/work/"
    if path.startswith(prefix):
        return path[len(prefix):]
    p = Path(path)
    return str(p.relative_to(ROOT)) if p.is_absolute() else path


def evidence(path, scope, expected=None, kind="continuation"):
    path = relocated(path)
    actual = sha((ROOT / path).read_bytes())
    if expected is not None:
        assert actual == expected, (path, actual, expected)
    return {"path": path, "sha256": actual, "scope": scope, "kind": kind}


def content_hash(rows):
    projection = {"fields": CORE_FIELDS, "rows": [[row[k] for k in CORE_FIELDS] for row in rows]}
    return sha((json.dumps(projection, ensure_ascii=False, separators=(",", ":")) + "\n").encode())


SOURCE_REVIEWS = {
    "D01": "The inherited 50 edit associations and exact prior comparison records are preserved. Root read all 145 D01 contexts in the restored residue inventory: geometric original data, original editions, published corrections and the expressly required methodology account have stated referents. The continuation replaces only the specified methodology dates/model wording and transports every other passage through the exact 24-edit map.",
    "D02": "The inherited 184 associations are joined by ten continuation edits. All changed complete statements/proofs were read and the replacement differences compared. They retain the specified integer, gluing domain, developing-map domain, component definitions, period calculation, rank calculation, absolute error bound, blow-up charts and deformation hypotheses. The candidate14 page233/page236 guards are applied as I-01975/I-01976, with every mathematical segment and all other affected proof bytes identical. Root's contextual dispositions and the complete candidate14 reading supply positive review beyond a pattern count.",
    "D03": "I-01949 is present as the concrete pair (0,0),(0,-3i), with the exact line-plus-period comparison. Candidate13 page140 explicitly records the repaired statement and complete proof. Candidate14's complete coverage carries or rereads that whole image. The continuation source map preserves this statement and proof byte for byte.",
    "D04": "The inherited 27 associations retain their numbered local statements/equations and opened primary-source locators. The current 24-edit map introduces no detached document key: its reference changes are the recorded Buchdahl locator, citation typography and publication-records macro. The candidate15 build has zero unresolved references/citations, and the inherited locator/reference audits retain their full scope.",
    "D05": "Root read all three D05 contexts in the residue inventory and identified the stated mathematical requirements. The inherited 27 associations and complete family/Hodge comparisons give the positive mathematical definitions and inputs. No continuation change introduces a request as a reference or theorem subject.",
    "D06": "The duplicate supplying aliases were repaired by I-01945/I-01946 and were actually read on candidate13 page14. The coherent-descent alias and its proposition both resolve to7.5; the classification appendix alias and its theorem both resolve to7.8 in candidate14's auxiliary file. Candidate13 pages44/51 record the complete receiving material. All aliases and every target are preserved by the continuation map.",
    "D07": "The zero coded-edit count is accompanied by positive occurrence review. Current model names in printed prose occur in the required methodology. Claude--Alpoge references identify the cited AC2026 authors and their stated mathematical contributions. The single CurrentChecker occurrence is its unused preamble definition; the permanent-tag macro prints only its tag argument. All corresponding source contexts were inspected, and the candidate14 full-page record covers the actual printed text.",
    "D08": "The inherited 432 edit associations retain their mathematical method/input/result replacements. The provenance agent read all192 contextual candidates for candidate14, then established an order-preserving source/PDF occurrence correspondence for candidate15. Across D08/D09,243 contexts are unchanged and all7 changed extracted contexts were read. The current audit reports no residual defect or guard; these context reviews have no page-reading or mathematical-event credit.",
    "D09": "The inherited190 associations and authenticated78-link end-table receipt retain their scope. All58 filename-pattern contexts were read and occur in the allowed program table. Candidate15's exact sequence correspondence and the actual reading of its changed contexts preserve that disposition; the numerical58-hit inventory and78-link table describe different recorded counts. The body computation descriptions remain those of the full inherited comparison records.",
    "D10": "The current StatementRecord definition prints the permanent small tag only. The inherited119 apparatus edits retain their exact comparison scope. The24-edit forward/inverse map preserves the ordered925 labels,598 tag targets and668 total targets. The shared metadata fields remain available in source/records without being printed by this macro.",
    "D11": "The inherited13 associations are joined by I-01972 and I-01977. The Chabauty proof retains its exact containment statement and period map; the appended tangent proof retains Q=O(-1)|_{2p_1}, the Ext^1/H^1 vanishing and existence of the splitting. Complete before/after blocks prove the deletions change only the repeated negative scope clauses. Root's two original D11 contexts plus the extra page325 replay hit are individually recorded.",
    "D12": "The inherited93 associations include the complete common-family, canonical-ring, tangent and automorphism consolidation comparisons and alias maps. All24 continuation edits are bounded prose/citation/typography changes within their archived locations; the exact source reconstruction shows no duplicated statement/proof has been introduced. The80 transported global source-block associations retain the earlier scoped checking evidence.",
    "D13": "The inherited42 associations and complete common-definition/maps comparisons place each recorded input in its owning numbered environment or proof. The current continuation does not relocate an input or add an orphan paragraph. All changed proof blocks preserve their owning statement and every other proof byte, apart from the explicitly compared edits.",
    "D14": "The inherited45 associations retain the recorded construction-before-use order, coherent-family/classification relocation and early cusp/residue inputs. The current source is the exact24-edit continuation of that ordering. Seven headlines,40 outline items and80 mapped source-block associations are bound in the current A--G receipt, while the complete candidate14 page reading records the actual layout and section order.",
    "D15": "The inherited44 associations are joined by the three precise section1.5 edits I-01969--I-01971. The exposed model/provider/ChatGPT Pro mode and21 November continuation date are stated without a new numerical effort attribution. The source now uses the single required records link and names the CC0 objects directly. Seven main statements/outlines and their status structure remain unchanged. The42-claim provenance record retains its own final rendered/source binding gate.",
    "D16": "The inherited112 associations retain the short mathematical statement titles with their complete comparison records. None of the24 continuation edits changes a title or adds a statement. Candidate14's complete actual-page coverage supports the title presentation; candidate15's reflow is a separate final page gate.",
    "D17": "The four inherited associations retain the opened exact source locators and the receiving matrix, characteristic-zero, parameter, measure and convergence identifications documented by their original receipts. The specifically required credited re-derived appendices remain. The24-edit reconstruction preserves these statements, proofs and citations without a new reproof claim.",
    "D18": "The inherited187 associations are joined by I-01956 (the already opened Buchdahl Theorem11,p297 locator) and I-01968 (one required publication-records macro beside the historical commit macro). The117-entry bibliography is byte-identical to candidate13's bibliography. Candidate13 pages335--346 were actually read; candidate14 complete coverage preserves their image evidence. The retained checkpoint pin was opened in the provenance receipt, with deposit-time final-pin replacement still a stated delivery step.",
    "D19": "The331 inherited equation associations retain their original/current anchor map and reference audit. The current source contains the same section-numbering declaration and the continuation preserves all labels and targets. None of the24 edits changes an equation environment or numbering declaration; the repaired cdots spelling is separately classified D23. The clean candidate15 build supplies the current reference-resolution check.",
    "D20": "The eight inherited associations retain the exact differential/lattice, invariant-pushforward, frame-transport and trace-sign comparisons. The continuation introduces no normalization or conversion claim. The current global source map transports the original scoped mathematical evidence, and every changed complete proof retains its stated inputs and maps.",
    "D21": "The one inherited association retains the exact squarefree division-polynomial/degree torsion-count corollary and the complete replacement comparison. No continuation edit promotes a numerical agreement to a result. Reading and typography operations are explicitly assigned zero mathematical-event credit.",
    "D22": "The three inherited associations retain the recorded toric fixed/character-extension loci,2pi-i chain map and twelve-term scalar-period calculation. No value, parameter choice or conversion formula is changed by the24 continuation edits; exact source transport binds these already recorded reasons to the current source.",
    "D23": "The inherited47 associations are joined by seven typography repairs: cdots, citation separation/spaces and three Poincare accents. Candidate13 page17 records the repaired diagram routes; its page315/page316 records the stage heading and final QED placement. The candidate13 addendum resolves the previously orphaned late headings. Candidate14's full346-page coverage, including all57 changed whole images, records the applied typography and reflow. The three later prose deletions require candidate15 reflow reading, which remains a separate final gate.",
    "D24": "The17 inherited associations retain the supplying/receiving theorem, outline and known/new comparisons. The current A--G receipt reconstructs all24 edits, preserves all seven headline and40 outline-item byte sequences, and transports80 archived source-block associations. Thus the current introduction/body comparison uses the same stated mechanisms and hypotheses as those scoped records.",
    "D25": "The17 inherited tagged associations retain the exact error/completion scopes and complete replacement/re-use comparisons for the lattice boundary point, logarithm clause, radial ratio, selected cusp diagonal, component resolution and Gross auxiliary-field hypotheses. The log preserves the one historical refuted clause and its refined identifier. None of the24 continuation edits is classified as a new theorem error or adds a mathematical event. The current source reconstruction and full changed-block comparisons transport that evidence; the dossier makes no new independent mathematical certification.",
}


def main():
    old_path = "agents/i_provenance/S6_SERIES_PUBLISH_I_defect_type_closure_evidence.json"
    old = read_json(old_path)
    add_path = "agents/i_provenance/S6_SERIES_PUBLISH_I_defect_type_candidate13_addendum.json"
    addendum = read_json(add_path)
    source_bytes = (ROOT / "S6_SERIES_PUBLISH_I.tex").read_bytes()
    source = source_bytes.decode()
    assert sha(source_bytes) == EXPECTED_SOURCE
    log_path = ROOT / "S6_SERIES_PUBLISH_defects_I.tsv"
    log_bytes = log_path.read_bytes()
    with log_path.open() as f:
        log = list(csv.DictReader(f, delimiter="\t"))
    with (ROOT / relocated(old["defect_log"]["snapshot"])).open() as f:
        inherited_log = list(csv.DictReader(f, delimiter="\t"))
    assert len(inherited_log) == 1953 and len(log) == 1977
    assert [[x[k] for k in CORE_FIELDS] for x in log[:1953]] == [[x[k] for k in CORE_FIELDS] for x in inherited_log]

    receipt_paths = [
        "agents/i_cont_edits/S6_SERIES_PUBLISH_I_continuation_edits_receipt.json",
        "agents/i_cont_edits/S6_SERIES_PUBLISH_I_continuation_residue_receipt.json",
        "agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate14_residue_receipt.json",
    ]
    baseline_path = ROOT.parent / "S6_SERIES_PUBLISH_work/S6_SERIES_PUBLISH_checkpoint_10/S6_SERIES_PUBLISH_I.tex"
    baseline = baseline_path.read_text()
    assert sha(baseline.encode()) == BASE_SOURCE
    transported = baseline
    all_changes, edit_receipts = [], []
    for path in receipt_paths:
        receipt = read_json(path)
        assert sha(transported.encode()) == receipt["before_source_sha256"]
        for change in receipt["changes"]:
            start = change["applied_offset"]
            assert transported[start:start + len(change["old"])] == change["old"]
            transported = transported[:start] + change["new"] + transported[start + len(change["old"]):]
            row = log[int(change["change_id"].split("-")[1]) - 1]
            assert (row["type"], row["statement_id"], row["old_text"], row["new_text"], row["reason"]) == (change["type"], change["statement_id"], change["old"], change["new"], change["reason"])
            all_changes.append({**change, "receipt": path})
        assert sha(transported.encode()) == receipt["after_source_sha256"]
        edit_receipts.append(evidence(path, "Exact forward/inverse source changes and complete affected-block comparisons."))
    assert transported == source and len(all_changes) == 24
    reverse = source
    for change in reversed(all_changes):
        start = change["applied_offset"]
        assert reverse[start:start + len(change["new"])] == change["new"]
        reverse = reverse[:start] + change["old"] + reverse[start + len(change["new"]):]
    assert reverse == baseline

    cov14_path = "agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate14_complete_coverage_snapshot.json"
    cov14 = read_json(cov14_path)
    assert (cov14["source_sha256"], cov14["pdf_sha256"], cov14["covered_pages"], cov14["page_count"]) == (C14_SOURCE, C14_PDF, 346, 346)
    assert cov14["all_pages_read"] and not cov14["missing_pages"]
    reading_sources = {}
    for page in cov14["pages"]:
        p = ROOT / f"render/I_candidate14/page_{page['page']:03d}.png"
        assert sha(p.read_bytes()) == page["image_sha256"]
        reading_sources[page["reading_record"]] = page["reading_record_sha256"]
    for path, expected in reading_sources.items():
        assert sha((ROOT / path).read_bytes()) == expected
    assert sha((ROOT / "build/I_candidate14/S6_SERIES_PUBLISH_I.pdf").read_bytes()) == C14_PDF
    assert sha((ROOT / "render/I_candidate14/manifest.json").read_bytes()) == cov14["render_manifest_sha256"]

    build_path = "build/I_candidate15/build_summary.json"
    build = read_json(build_path)
    assert (build["source_sha256"], build["pdf_sha256"]) == (EXPECTED_SOURCE, EXPECTED_PDF)
    assert sha((ROOT / "build/I_candidate15/S6_SERIES_PUBLISH_I.pdf").read_bytes()) == EXPECTED_PDF
    for key in ["overfull_total", "overfull_above_2pt", "undefined_references", "undefined_citations", "missing_characters", "missing_fonts", "multiply_defined", "duplicate_destinations"]:
        assert build[key] == 0
    assert build["shell_escape"] is False

    root_path = "records/S6_SERIES_PUBLISH_I_continuation_root_residue_dispositions.json"
    root_review = read_json(root_path)
    assert len(root_review["rows_read"]) == 155 and root_review["additional_replay_hit"]["type"] == "D11"
    contextual_path = "agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate15_D08_D09_dispositions.json"
    contextual = read_json(contextual_path)
    assert (contextual["source_sha256"], contextual["pdf_sha256"]) == (EXPECTED_SOURCE, EXPECTED_PDF)
    assert contextual["counts"] == {"D08": 192, "D09": 58}
    assert not contextual["confirmed_new_defects"] and not contextual["proposed_guards"]
    ag_path = "records/S6_SERIES_PUBLISH_I_continuation_AG_binding.json"
    ag = read_json(ag_path)
    assert ag["source_sha256"] == EXPECTED_SOURCE and len(ag["exact_edits"]) == 24
    assert len(ag["headlines"]) == 7 and sum(x["outline_items"] for x in ag["headlines"].values()) == 40
    assert ag["source_exact_forward_and_inverse_maps_verified"]

    aux14 = (ROOT / "build/I_candidate14/S6_SERIES_PUBLISH_I.aux").read_text()
    for label, number in [("I:coherent-descent-proof", "7.5"), ("app:rederive:fam-src-A.5.1", "7.8")]:
        assert r"\newlabel{" + label + "}{{" + number + "}" in aux14
    assert r"\newcommand{\StatementRecord}[4]{{\upshape\footnotesize[tag~\texttt{#3}]}\enspace\ignorespaces}" in source
    assert source.count(r"\CurrentChecker") == 1
    assert source.count(r"\newcommand{\SsixPublishRecords}") == source.count(r"\href{\SsixPublishRecords}") == 1
    assert r"\numberwithin{equation}{section}" in source
    bib = lambda s: s[s.index(r"\begin{thebibliography}"):s.index(r"\end{thebibliography}")]
    assert bib(source) == bib(baseline)
    assert len(re.findall(r"\\bibitem", bib(source))) == 117
    for pattern in [r"\\label\{([^}]+)\}", r"\\hypertarget\{([^}]+)\}"]:
        assert re.findall(pattern, source) == re.findall(pattern, baseline)

    common_current = [
        evidence(old_path, "Original individual D01--D25 inspected scopes, exact edit associations and inherited proof/source receipts.", kind="inherited dossier"),
        evidence(add_path, "Actual candidate13 late-page reading and individually resolved/pending findings.", kind="inherited addendum"),
        evidence("records/S6_SERIES_PUBLISH_I_candidate13_complete_coverage_snapshot.json", "Complete candidate13 actual-reading coverage; inheritance requires whole-image equality.", kind="actual page coverage"),
        evidence(cov14_path, "All346 candidate14 whole-page images covered; all image and referenced reading-record hashes verified here.", kind="actual page coverage"),
        evidence(build_path, "Candidate15 exact source/PDF and all-zero recorded typesetting checks.", kind="build"),
    ] + edit_receipts
    verified_inherited = {}
    type_rows = []
    associations = []
    old_edits = {row["change_id"]: row for row in inherited_log}
    for old_type in old["types"]:
        typ = old_type["type_id"]
        selected = [row for row in log if typ in re.findall(r"D\d\d", row["type"])]
        inherited_ids = [row["change_id"] for row in selected if row["change_id"] in old_edits]
        assert inherited_ids == old_type["edit_ids"]
        new_changes = [change for change in all_changes if typ in re.findall(r"D\d\d", change["type"])]
        ev = []
        for old_evidence in old_type["evidence"]:
            e = evidence(old_evidence["path"], old_evidence.get("scope", "Inherited scoped evidence."), old_evidence["sha256"], "inherited scoped comparison/review")
            verified_inherited[e["path"]] = e["sha256"]
            ev.append(e)
        ev += common_current
        if typ in ["D01", "D02", "D05", "D11", "D23"]:
            ev.append(evidence(root_path, "155 original contexts actually read and one additional approved D11 replay hit; no automatic absence or mathematical-check inference.", kind="contextual reading"))
        if typ in ["D08", "D09"]:
            ev.append(evidence(contextual_path, "Candidate15 bound contextual review:192 D08 and58 D09; all7 changed extracted contexts read.", kind="contextual reading"))
        if typ in ["D12", "D14", "D15", "D24", "D25"]:
            ev.append(evidence(ag_path, "Current exact24-edit transport, seven headlines,40 outline items and80 archived source-block associations.", kind="global source binding"))
        if typ in ["D07", "D15", "D18"]:
            ev.append(evidence("agents/i_cont_provenance/S6_SERIES_PUBLISH_I_cont_provenance_binding.json", "Continuation42-claim/count/model/date/deposit binding; its own final candidate/PDF gate is retained.", kind="provenance preparation"))
        if typ == "D06":
            ev.append(evidence("build/I_candidate14/S6_SERIES_PUBLISH_I.aux", "Actual alias pairs resolve to7.5 and7.8; current source preserves all labels.", kind="reference resolution"))
        for row in selected:
            associations.append({"type_id": typ, "change_id": row["change_id"], "statement_id": row["statement_id"], "origin": "inherited candidate13" if row["change_id"] in old_edits else "continuation"})
        type_rows.append({
            "type_id": typ, "class": old_type["class"], "defect": old_type["defect"], "required_fix": old_type["required_fix"],
            "status": "source_clear_pending_final_binding",
            "proposed_disposition": "The recorded source issues are resolved. Final individual type closure awaits the named current-candidate bindings.",
            "source_clear_in_recorded_review_scope": True,
            "source_review": SOURCE_REVIEWS[typ],
            "inherited_status": old_type["status"], "inherited_inspected_scope": old_type["inspected_scope"],
            "inherited_remaining_as_recorded": old_type["remaining"],
            "inherited_gate_disposition": "The inherited candidate13 page-reading dependencies have actual candidate13/candidate14 coverage and the individually recorded repairs. Final certification is now bound to candidate15; the original pending status is retained above as historical evidence.",
            "inherited_edit_associations": len(inherited_ids), "continuation_edit_associations": len(new_changes), "current_edit_associations": len(selected),
            "edit_ids": [row["change_id"] for row in selected], "continuation_edit_ids": [change["change_id"] for change in new_changes],
            "edit_content_sha256": content_hash(selected),
            "remaining_content_issues": [],
            "remaining_dependencies": [
                "Complete candidate15 actual whole-page coverage, with source/PDF binding and exact image equality for inherited pages.",
                "Final current-source/PDF/check-ledger/provenance binding, including the42 source/report/deposit claims where applicable.",
                "Final defect-page mapping and rebinding of the full defect-log hash; the edit-content and type-association hashes are recorded separately."],
            "evidence": ev,
            "new_mathematical_events": 0,
        })
    # New findings from the actual candidate15 reading supersede the earlier
    # source-clear dispositions. No pending proposal is counted as an applied edit.
    pending_files = []
    pending_by_type = collections.defaultdict(list)
    for guard_path in [
        "agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate15_root_guards.json",
        "agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate15_edits_guards.json",
        "agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate15_provenance_guards.json",
    ]:
        if not (ROOT / guard_path).exists():
            continue
        datum = read_json(guard_path)
        guards = datum if isinstance(datum, list) else datum["guards"]
        guard_ev = evidence(guard_path, "Exact candidate15 guard proposals; no source mutation or applied-edit credit.", kind="pending source guard")
        pending_files.append({**guard_ev, "guards": len(guards)})
        for guard in guards:
            for typ in re.findall(r"D\d\d", guard.get("type", guard.get("defect_type", ""))):
                pending_by_type[typ].append({"guard_id": guard["id"], "page": guard.get("page"),
                    "statement_id": guard.get("statement_id"), "guard_file": guard_path,
                    "guard_file_sha256": guard_ev["sha256"], "status": "pending consolidated approved source application"})
    # Root explicitly read the25 rows and reopened the title-wording disposition
    # along with D01/D18 from the provenance reader's actual pages.
    for typ, pages, scope in [
        ("D01", [316, 321], "Own-history/re-derived wording in the credited appendices; preserve mathematical credit and exact source/version comparison."),
        ("D16", [316], "Process/history wording in the Appendix A remark title; root explicitly reopened this title disposition."),
        ("D18", [335, 336, 337, 340, 341, 342, 343, 344], "Provenance reader's exact publisher-link and bibliography-field/duplicate-year findings; full guard batch remains pending application."),
    ]:
        pending_by_type[typ].append({"candidate": "I_candidate15", "pages": pages,
            "reported_by": "provenance actual reading and root review", "scope": scope,
            "reading_record": "agents/i_cont_provenance/S6_SERIES_PUBLISH_I_final_candidate15_reading_provenance.json"})
    pending_reading = evidence("agents/i_cont_provenance/S6_SERIES_PUBLISH_I_final_candidate15_reading_provenance.json", "Actual full pages308--345 and their named pending findings.", kind="actual page reading")
    for row in type_rows:
        typ = row["type_id"]
        if typ not in pending_by_type:
            continue
        row.update({"status": "open_candidate15_source_guards_pending",
            "proposed_disposition": "Keep this type open for the recorded candidate15 guard batch. Apply only the consolidated approved changes and bind complete-block comparisons before revisiting closure.",
            "source_clear_in_recorded_review_scope": False,
            "remaining_content_issues": pending_by_type[typ]})
        row["source_review"] += " The subsequent candidate15 actual-page findings listed below supersede this earlier source-clear scope; their exact guard proposals remain unapplied."
        row["remaining_dependencies"].insert(0, "Complete the consolidated candidate15 guard review/application for this type and retain its full before/after block evidence.")
        for ev in pending_files:
            if any(issue.get("guard_file") == ev["path"] for issue in pending_by_type[typ]):
                row["evidence"].append(ev)
        row["evidence"].append(pending_reading)
    open_types = [row["type_id"] for row in type_rows if not row["source_clear_in_recorded_review_scope"]]
    assert len(type_rows) == 25 and sum(row["current_edit_associations"] for row in type_rows) == 2070
    assert len(verified_inherited) == 57
    association_path = OUT / "S6_SERIES_PUBLISH_I_cont_defect_type_associations.tsv"
    with association_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["type_id", "change_id", "statement_id", "origin"], delimiter="\t")
        writer.writeheader(); writer.writerows(associations)

    prepared = {
        "schema": 1, "paper": "I", "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "candidate": "I_candidate15", "source_sha256": EXPECTED_SOURCE, "pdf_sha256": EXPECTED_PDF,
        "defect_log_sha256": sha(log_bytes), "defect_log_content_sha256": content_hash(log),
        "defect_log_content_hash_specification": {"fields": CORE_FIELDS, "serialization": "UTF-8 JSON object with keys fields then rows; rows are ordered lists of these fields in log order; ensure_ascii=False, separators comma/colon, one final newline. Page/location/status fields are excluded."},
        "defect_type_associations": {"path": str(association_path.relative_to(ROOT)), "sha256": sha(association_path.read_bytes()), "count": len(associations)},
        "source_path": "S6_SERIES_PUBLISH_I.tex", "pdf_path": "build/I_candidate15/S6_SERIES_PUBLISH_I.pdf", "defect_log_path": "S6_SERIES_PUBLISH_defects_I.tsv",
        "unique_edit_rows": len(log), "inherited_unique_edit_rows": 1953, "continuation_unique_edit_rows": 24,
        "inherited_edit_type_associations": 2046, "edit_type_associations": 2070,
        "count_semantics": old["count_semantics"],
        "register_snapshot": evidence(old["register"]["snapshot"], "The25 original type definitions, with historical status preserved.", old["register"]["sha256"], "register snapshot"),
        "all_types_source_clear": all(row["source_clear_in_recorded_review_scope"] for row in type_rows),
        "source_clear_scope": ", ".join(open_types) + " remain open for the individually recorded candidate15 findings. Other type rows retain their bounded individual evidence dispositions. The source remains frozen; no new mathematical certification is made.",
        "final_certified": False, "canonical_status_modified": False, "mathematical_events_added": 0,
        "source_transport": {"baseline_source_sha256": BASE_SOURCE, "current_source_sha256": EXPECTED_SOURCE, "exact_forward_and_reverse_reconstruction": True, "edits": all_changes, "receipt_files": edit_receipts},
        "prior_candidate14": {"source_sha256": C14_SOURCE, "pdf_sha256": C14_PDF, "complete_page_count": 346, "coverage": evidence(cov14_path, "Immutable complete candidate14 actual-reading snapshot."), "individual_image_hashes_verified": 346, "referenced_reading_record_hashes_verified": len(reading_sources), "newly_read_pages": 57},
        "inherited_evidence_files_verified": [{"path": p, "sha256": h} for p,h in sorted(verified_inherited.items())],
        "root_contextual_counts": dict(collections.Counter(row["type"] for row in root_review["rows_read"])),
        "root_additional_replay_hit": root_review["additional_replay_hit"],
        "candidate15_D08_D09_counts": contextual["counts"],
        "candidate15_build": evidence(build_path, "Exact current source/PDF and clean pdfLaTeX build."),
        "pending_candidate15_guard_files": pending_files,
        "pending_candidate15_types": open_types,
        "rows": type_rows,
        "remaining_dependencies": ["Consolidated candidate15 guard review and approved source repair for " + ", ".join(open_types), "Current-candidate actual rendered-page coverage after edits", "Final current-candidate provenance binding", "Final mapped defect-log hash"],
        "limitations": ["Original mathematical check scopes and counts are carried without creating a new check event.", "Pattern occurrence equality supports transport only; the positive contextual review and inherited comparison receipts supply the disposition.", "The final status fields and canonical register/check ledger are owned by root and are unchanged by this preparation."]}
    out = OUT / "S6_SERIES_PUBLISH_I_cont_defect_type_closure_preparation.json"
    out.write_text(json.dumps(prepared, ensure_ascii=False, indent=2) + "\n")
    lines = ["# Paper I — individual defect-type closure preparation", "", "This is a preparation dossier. " + ", ".join(open_types) + " remain open for the individually recorded candidate15 findings. Exact guard proposals are pending consolidated application. The all-types source-clear flag is false. Final current-candidate whole-page coverage, provenance and mapped-log bindings also remain pending. Canonical status files and the mathematical-check ledger are unchanged.", "", f"- Source SHA-256: `{EXPECTED_SOURCE}`", f"- Candidate15 PDF SHA-256: `{EXPECTED_PDF}`", f"- Defect log SHA-256 at preparation: `{prepared['defect_log_sha256']}`", f"- Stable edit-content SHA-256: `{prepared['defect_log_content_sha256']}`", f"- Type-association TSV SHA-256: `{prepared['defect_type_associations']['sha256']}`", "- 1,977 unique edit rows; 2,070 type associations; 24 continuation edits. Composite codes contribute to each listed type. These counts describe repair records, not unique mathematical errors or independent checks.", "- All57 distinct inherited evidence-file hashes,346 candidate14 image hashes and every referenced reading-record hash were verified. Candidate14 coverage is preserved in a separate immutable snapshot.", "- Seven main statements and40 outline items are unchanged; the current global receipt transports80 source-block associations. No mathematical event is added.", "", "## Per-type source dispositions", "", "| Type | Inherited associations | Continuation associations | Current associations | Proposed status |", "|---|---:|---:|---:|---|"]
    for row in type_rows:
        disposition = "Open: candidate15 content guards pending" if not row["source_clear_in_recorded_review_scope"] else "Source clear in recorded scope; final bindings pending"
        lines.append(f"| {row['type_id']} | {row['inherited_edit_associations']} | {row['continuation_edit_associations']} | {row['current_edit_associations']} | {disposition} |")
    for row in type_rows:
        lines += ["", f"## {row['type_id']} — {row['defect']}", "", row["source_review"], "", "Continuation edit IDs: " + (", ".join(row["continuation_edit_ids"]) or "none") + ".", "", "The full JSON row retains every inherited edit ID, individual evidence path/hash, original inspected scope and original pending wording. Remaining dependencies: candidate15 actual page coverage; final current-candidate provenance; final defect-page mapping/full-log hash."]
    lines += ["", "## Source/edit transport", "", "The three complete edit receipts reconstruct candidate13 source26a6… through18 initial edits,3 scope residues and3 candidate14 residues to current source45bf…. Reversing the24 exact offset maps recovers the original source byte for byte. The first1,953 log rows retain all six edit-content fields exactly; later page mapping may change only fields excluded by the separately specified content hash.", "", "## Final gates", "", "1. Complete the113 changed candidate15 whole-image readings; inherit earlier reading only through complete-image hash equality.", "2. Bind the final source, PDF, check ledger and42 provenance claims to the same candidate.", "3. Map all1,977 defect rows to the final PDF and update the full-log hash. Recheck the stable content and type-association hashes.", "", "Root retains responsibility for the final25 individual status dispositions. No source edit or status mutation is performed by this dossier script.", ""]
    out.with_suffix(".md").write_text("\n".join(lines))
    print(json.dumps({"output": str(out.relative_to(ROOT)), "output_sha256": sha(out.read_bytes()), "source_sha256": EXPECTED_SOURCE, "pdf_sha256": EXPECTED_PDF, "defect_log_sha256": prepared["defect_log_sha256"], "defect_log_content_sha256": prepared["defect_log_content_sha256"], "type_rows": len(type_rows), "unique_edit_rows": len(log), "edit_type_associations": 2070, "all_types_source_clear": prepared["all_types_source_clear"], "final_certified": False, "mathematical_events_added": 0}, indent=2))


if __name__ == "__main__":
    main()
