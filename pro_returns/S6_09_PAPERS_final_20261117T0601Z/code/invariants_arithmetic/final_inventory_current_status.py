#!/usr/bin/env python3
"""Prepare/apply a strictly bounded, fully archived final inventory metadata repair.

This is not an assembler or a historical finalizer.  It never edits a paper or
changes a statement, mathematical outcome, source-credit cell, or proof check.
The apply operation validates the exact entire input snapshot and every old cell.
"""
from __future__ import annotations
import argparse
import collections
import csv
import hashlib
import io
import json
from pathlib import Path

D = Path(__file__).resolve().parents[2]
ROOT = D.parent
W = D / "work/invariants_arithmetic"
INV = D / "S6_09_PAPERS_inventory.csv"
OVERLAY = W / "final_inventory_current_status_overlay.json"
APPLIED = W / "final_inventory_current_status_applied.json"
FIELDS = ["source_run", "source_id", "source_file", "paper", "printed_label",
          "kind", "statement_as_printed", "wording_vs_source", "recorded_checks",
          "your_check", "check_outcome", "found_in_AC26", "found_in_E26",
          "found_in_DGKX_v1", "found_elsewhere", "credited_to", "notes"]


def digest(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def load(p: Path):
    return json.loads(p.read_text())


def save(p: Path, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def prepare():
    raw = INV.read_bytes()
    rd = csv.DictReader(io.StringIO(raw.decode()))
    assert rd.fieldnames == FIELDS
    rows = list(rd)
    assert len(rows) == 1184
    papers = {p: (D / f"S6_09_PAPERS_{p}.tex").read_text() for p in ["I", "II", "III"]}
    changes = []
    evidence = {}

    def cite(path: str):
        p = ROOT / path
        assert p.is_file(), path
        evidence[path] = digest(p.read_bytes())
        return path

    def change(r, field, new, reason, locators):
        old = r[field]
        assert old != new and new.strip()
        changes.append({"source_run": r["source_run"], "source_id": r["source_id"],
                        "paper": r["paper"], "printed_label": r["printed_label"],
                        "field": field, "before": old, "after": new,
                        "reason": reason, "evidence": locators})

    # The root has refreshed the literal statements.  Check the actual current
    # paper at each label before removing either obsolete production prefix.
    prefixes = ["Not yet printed; source statement retained in notes.",
                "Source statement recorded; final wording comparison pending."]
    for r in rows:
        for prefix in prefixes:
            if r["wording_vs_source"].startswith(prefix):
                text = papers[r["paper"]]
                anchor = "\\label{" + r["printed_label"] + "}"
                assert text.count(anchor) == 1, (r["source_id"], "label")
                assert anchor in r["statement_as_printed"], r["source_id"]
                assert r["statement_as_printed"] in text, (r["source_id"], "literal statement")
                after = r["wording_vs_source"][len(prefix):].lstrip(" |")
                assert after.startswith("Exact final statement extracted from the printed label.")
                change(r, "wording_vs_source", after,
                       "Remove the obsolete production prefix after verifying the complete literal printed field at its unique actual label; retain all later extraction/transform descriptions.",
                       [{"paper": r["paper"], "printed_label": r["printed_label"],
                         "statement_sha256": digest(r["statement_as_printed"].encode()),
                         "paper_sha256": digest(text.encode())}])

    cn_source = cite("sources/correction_note/N_singular_fibre_vanishing_step.tex")
    cn_audit = cite("deliverables/work/cdp_audit/working_edition_inventory.json")
    cn_credit = cite("deliverables/work/maps_audit/correction_note15_credit_overlay.json")
    cn_rows = {(x["source_run"], x["source_id"]): x for x in load(ROOT / cn_audit)}
    dual_source = cite("sources/codex_workspace/courses/CG-S6/sources/manifold-duality-the-diagonal-and-wu-classes.source.txt")
    dual_inv = cite("deliverables/work/maps_audit/course_duality_euler_provider_inventory.json")
    dual_full = cite("deliverables/work/maps_audit/course_duality_euler_full_check.json")
    dual_rows = {x["source_id"]: x for x in load(ROOT / dual_inv)}
    for r in rows:
        if r["recorded_checks"].strip():
            continue
        if r["source_run"] == "CORRECTION_NOTE_20260901":
            src = cn_rows[(r["source_run"], r["source_id"])]
            assert not src["recorded_checks"].strip()
            value = ("No earlier named per-result independent proof-reading event was located in the inspected correction-note source or its attached audit inventory. "
                     "Source disclosure: OpenAI Codex gpt-5.6-sol, effort Ultra, drafting and audit assistance; document date 1 September 2026. "
                     "The disclosure at sources/correction_note/N_singular_fibre_vanishing_step.tex lines 935–943 does not identify an independent prior reader, exact per-result time, or full-proof scope. "
                     "The current complete independent reading remains separately recorded in your_check and work/cdp_audit/working_edition_inventory.json for this source_id.")
            change(r, "recorded_checks", value,
                   "Make the bounded absence of an attached prior reader explicit, while preserving the actual producer disclosure without promoting it to independent verification.",
                   [cn_source + ":40,935–943", cn_audit + "#" + r["source_id"], cn_credit + "#" + r["source_id"]])
        elif r["source_run"] == "WORKING_EDITION_COURSE_PROVIDER" and r["source_id"] in dual_rows:
            q = dual_rows[r["source_id"]]
            value = ("Producer self-check, not a separate independent reading: GPT-6.1 Sol (OpenAI), effort Ultra, October 2026; no day recorded. "
                     "The source header at sources/codex_workspace/courses/CG-S6/sources/manifold-duality-the-diagonal-and-wu-classes.source.txt line 3 states: "
                     + q["raw_producer_header"] + " "
                     "No attached earlier independent prior-reader record was located in the provider inventory. "
                     f"This result occupies source lines {q['start_line']}–{q['end_line']}; "
                     "the current complete independent reading is event new-course-provider-duality-euler-scoped-20261117, recorded in your_check and work/maps_audit/course_duality_euler_full_check.json.")
            change(r, "recorded_checks", value,
                   "Restore the exact genuine producer self-check and delimit the absence of a separate prior independent reader; do not infer a check date or scope not present in the source.",
                   [dual_source + ":3", dual_inv + "#" + r["source_id"], dual_full])
        else:
            raise ValueError("Unreviewed empty prior-check cell: " + str((r["source_run"], r["source_id"])))

    # These eight notes were blank; the current full proof checks already exist.
    # Add only source and retention provenance, with no new check claim.
    proof_record = cite("deliverables/work/root/proof_audit.md")
    note_scopes = {
        "algebraic_dimension.tex": "Working-edition analytic proofs compared in full, algebraic_dimension.tex entry",
        "analytic_canonical_ring.tex": "Working-edition analytic proofs compared in full, analytic_canonical_ring.tex entry",
        "period_parameter_deformation.tex": "Working-edition analytic proofs compared in full, period_parameter_deformation.tex entry",
        "period_shift_classification.tex": "Period-shift and Hodge-line full original proofs, full period_shift_classification.tex reading",
    }
    for r in rows:
        if r["notes"].strip():
            continue
        assert r["source_run"] == "WORKING_EDITION"
        source, line = r["source_file"].rsplit(":", 1)
        source = cite("sources/" + source)
        scope = note_scopes[Path(source).name]
        value = (f"Original source {source}, statement beginning at line {line}; source SHA256 {evidence[source]}. "
                 f"Actual statement destination: Paper {r['paper']}, {r['printed_label']}. "
                 f"Existing complete proof-reading evidence: work/root/proof_audit.md, '{scope}'. ")
        if r["source_id"] == "pshift:thm:classification":
            assert "\\label{wb:pshift:sec:classification}" in papers["I"]
            value += ("The statement is shared with fam:src:A.5.1; the complete distinct period-shift argument is retained at wb:pshift:sec:classification. ")
        else:
            value += "The source method is retained in the corresponding complete working-edition section of Paper I. "
        value += "This entry supplies source/retention provenance for the existing check."
        change(r, "notes", value, "Fill an empty provenance note using the actual source, printed label and existing complete proof-reading record.", [source, proof_record + "#" + scope])

    # The exact stale metadata below predates the completed, per-row closures.
    # Archive each old full field; preserve every unrelated source note.
    maps_path = cite("deliverables/work/maps_audit/III_maps60_final_closure.json")
    maps_rows = {x["source_id"]: x for x in load(ROOT / maps_path)}
    wb_path = cite("deliverables/work/maps_audit/III_working30_final_closure.json")
    wb_rows = {x["source_id"]: x for x in load(ROOT / wb_path)}
    top_path = cite("deliverables/work/maps_audit/paperI_topology_manifest.json")
    top_rows = load(ROOT / top_path)
    for r in rows:
        old = r["notes"]
        stale = "audit_notes: Internal arguments checked; source matches not yet complete."
        if stale in old:
            q = maps_rows[r["source_id"]]
            assert q["full_receiving_proof_read"] and q["source_dependency_status"].startswith("Closed")
            current = ("audit_notes: Exact receiving-proof and operative-source closure completed; "
                       + q["source_dependency_status"] + " Record: work/maps_audit/III_maps60_final_closure.json#"
                       + r["source_id"] + "; result-specific credit: " + q["credit_record"] + ".")
            change(r, "notes", old.replace(stale, current),
                   "Replace only obsolete current audit metadata with its completed row-specific source/credit closure; retain the full old field in this overlay.",
                   [maps_path + "#" + r["source_id"], q["credit_record"]])
        stale = "overlap_status=partial or same conclusion; proof comparison pending"
        if stale in old:
            sid = r["source_id"]
            if sid in wb_rows:
                q = wb_rows[sid]
                assert q["full_receiving_proof_read"] and q["source_dependency_status"].startswith("Closed")
                ref = wb_path + "#" + sid
                evidence_scope = {k: q[k] for k in ["source_statement_range", "source_full_proof_range", "current_check_event_ids", "source_dependency_status", "exact_dependency_closure", "repair_files", "credit_record"]}
            else:
                candidates = [q for q in top_rows if r["printed_label"] in q["labels"]]
                assert len(candidates) == 1, (sid, "no exact final proof mapping")
                q = candidates[0]
                ref = top_path + "#" + q["source"]
                evidence_scope = {k: q[k] for k in ["proof_preservation", "mathematical_changes", "new_check", "dependency_audit_completion"]}
            current = ("overlap_status=partial or shared conclusion; completed receiving-proof/dependency comparison: " + ref
                       + f"; final statement destination Paper {r['paper']}, {r['printed_label']}; distinct complete source methods retained")
            change(r, "notes", old.replace(stale, current),
                   "Replace the obsolete proof-comparison status with the exact completed source-method/dependency record; shared conclusions are not counted as new statements.",
                   [{"record": ref, "actual_completed_scope": evidence_scope}])

    keys = [(r["source_run"], r["source_id"], r["field"]) for r in changes]
    assert len(keys) == len(set(keys)), "Two edits to the same cell need explicit composition"
    assert collections.Counter(x["field"] for x in changes) == {"wording_vs_source": 277, "recorded_checks": 23, "notes": 44}
    assert INV.read_bytes() == raw, "Inventory changed during preparation"
    snapshot = W / ("final_inventory_before_current_status_" + digest(raw)[:16] + ".csv")
    if snapshot.exists():
        assert snapshot.read_bytes() == raw
    else:
        snapshot.write_bytes(raw)
    result = {"reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)", "effort": "Pro", "date_utc": "2026-11-17",
              "scope": "Only obsolete production metadata, exact completed comparison statuses, empty prior-reader provenance and empty source notes; no mathematical proof/outcome/credit edits.",
              "inventory_sha256_before": digest(raw), "rows": len(rows), "columns": FIELDS,
              "full_inventory_before_archive": str(snapshot.relative_to(D)),
              "unchanged_fields": [x for x in FIELDS if x not in ["wording_vs_source", "recorded_checks", "notes"]],
              "paper_sha256": {p: digest(s.encode()) for p, s in papers.items()},
              "evidence_sha256": evidence, "changes": changes,
              "changed_cells_by_field": dict(collections.Counter(x["field"] for x in changes))}
    save(OVERLAY, result)
    print(json.dumps({"prepared": True, "changes": len(changes), "by_field": result["changed_cells_by_field"], "before_sha256": digest(raw)}))


def apply():
    obj = load(OVERLAY)
    raw = INV.read_bytes()
    assert digest(raw) == obj["inventory_sha256_before"], "Inventory snapshot mismatch; do not silently rebase"
    rd = csv.DictReader(io.StringIO(raw.decode()))
    assert rd.fieldnames == FIELDS
    rows = list(rd)
    indexed = {(r["source_run"], r["source_id"]): r for r in rows}
    assert len(indexed) == len(rows) == 1184
    for event in obj["changes"]:
        r = indexed[(event["source_run"], event["source_id"])]
        assert r[event["field"]] == event["before"], "Old cell mismatch"
        assert r["paper"] == event["paper"] and r["printed_label"] == event["printed_label"]
        r[event["field"]] = event["after"]
    for r in rows:
        assert all(r[f].strip() for f in FIELDS), (r["source_run"], r["source_id"], "empty field")
    stream = io.StringIO(newline="")
    wr = csv.DictWriter(stream, fieldnames=FIELDS)
    wr.writeheader(); wr.writerows(rows)
    after = stream.getvalue().encode()
    assert INV.read_bytes() == raw, "Inventory changed before atomic update"
    for p, h in obj["paper_sha256"].items():
        assert digest((D / f"S6_09_PAPERS_{p}.tex").read_bytes()) == h, "Paper changed"
    tmp = INV.with_suffix(".metadata-tmp")
    tmp.write_bytes(after); tmp.replace(INV)
    archive = W / ("final_inventory_after_current_status_" + digest(after)[:16] + ".csv")
    archive.write_bytes(after)
    save(APPLIED, {"reader": obj["reader"], "effort": obj["effort"], "date_utc": obj["date_utc"],
                   "inventory_sha256_before": digest(raw), "inventory_sha256_after": digest(after),
                   "rows": len(rows), "columns": FIELDS, "changes": len(obj["changes"]),
                   "changed_cells_by_field": obj["changed_cells_by_field"],
                   "complete_before_after_overlay": str(OVERLAY.relative_to(D)),
                   "full_before_archive": obj["full_inventory_before_archive"],
                   "full_after_archive": str(archive.relative_to(D)),
                   "all_other_fields_byte_identical": True, "papers_unchanged": obj["paper_sha256"]})
    print(json.dumps({"applied": True, "rows": len(rows), "changed_cells": len(obj["changes"]), "after_sha256": digest(after)}))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--prepare", action="store_true")
    g.add_argument("--apply", action="store_true")
    a = p.parse_args()
    prepare() if a.prepare else apply()
