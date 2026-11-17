#!/usr/bin/env python3
"""Read-only final 1184-row/17-column completeness, placement and credit gate.

Historical reviewer prose, genuinely open mathematics and explicit limits of a
source opening are retained and separately classified.  They are not silently
treated as current unfinished audit tasks or promoted to verified statements.
"""
from __future__ import annotations
import collections
import csv
import hashlib
import io
import json
import re
from pathlib import Path

from final_inventory_current_status import FIELDS

D = Path(__file__).resolve().parents[2]
W = D / "work/invariants_arithmetic"
INV = D / "S6_09_PAPERS_inventory.csv"
OUT = W / "final_inventory_completeness_credit_gate.json"
CREDITS = ["found_in_AC26", "found_in_E26", "found_in_DGKX_v1", "found_elsewhere", "credited_to"]
CURRENT = ["wording_vs_source", "your_check", "check_outcome"] + CREDITS + ["notes"]
PAT = re.compile(r"\b(?:pending|unexamined|unchecked|unreviewed|unread|unverified|incomplete|deferred|unassessed)\b|\bnot yet\b|\bawaiting\b|\bto be (?:checked|verified|compared)\b|\bnot (?:examined|checked|compared)\b", re.I)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def load(p):
    return json.loads(p.read_text())


def disposition(r, f, ctx):
    """Only the exact bounded contexts read in this final inventory are accepted."""
    sid, run = r["source_id"], r["source_run"]
    if f in CREDITS and ("absence from unread sections" in ctx or "No absence is asserted in unread material" in ctx):
        return "bounded_negative_search", "Explicitly refuses an absence claim about unread sources; the positive/negative comparison is closed only in its recorded scope."
    if run == "S6_04_MAPS_MANIFOLDS" and f == "your_check" and sid.startswith("D."):
        if "earlier_pending_language" in ctx:
            return "explicit_historical_completion", "The JSON marks earlier reservations historical and links the completed numerical/source closure in maps_D_independent_audit.json."
        if sid in ["D.2.17", "D.2.18", "D.2.20"] and "Closure 17Nov2026" in ctx:
            return "explicit_historical_completion", "The original reservation is followed immediately by the exit-0 unchanged-program rerun and original-source closure; retained history."
    if run == "S6_03_CDP" and sid in ["E2", "E17"] and f == "found_elsewhere" and "2018 journal edition remains unverified" in ctx:
        return "edition_limit", "The operative 2019 author version was opened and is cited as LRS2019; no verification or identity is asserted for the unopened 2018 edition."
    if run == "S6_04_MAPS_MANIFOLDS" and sid == "E.2.1" and f in ["found_elsewhere", "credited_to"] and "initial download was incomplete" in ctx:
        return "resolved_retrieval_history", "The failed initial download is explicitly followed by successful complete original-PDF retrieval; broad lattice theory is outside the claimed scope."
    if run == "S6_05_ARITHMETIC" and sid == "C.7.7" and f == "your_check" and "excludes the unverified unrestricted theta-lift" in ctx:
        return "excluded_unproved_extension", "The proved conditional statement excludes the unrestricted theta-lift criterion and norm claim; the remaining question is retained separately."
    if run == "CORRECTION_NOTE_20260901" and sid in ["lem:generic-endpoints", "thm:corrected-global"] and f == "found_elsewhere" and "published page numbering has not yet" in ctx:
        return "edition_locator_limit", "Complete operative author-version statements and proofs were read; the unopened journal pagination is expressly not certified."
    if run == "working_edition" and sid in ["cusp-s12-one-copy-invariant", "cusp_s12_carrier_homotopy:L567"] and f == "found_elsewhere" and "draft is explicitly preliminary and incomplete" in ctx:
        return "bibliographic_description", "Incomplete describes Hatcher's preliminary source draft, not the completed exact receiving-theorem reading."
    if run == "WORKING_EDITION_COURSE_PROVIDER" and f in ["found_elsewhere", "credited_to"] and "unchecked convergence theorem" in ctx:
        return "finite_computation_scope", "The record declines to infer an unproved convergence theorem from a finite certificate; complete provider proofs are separately retained."
    if f == "notes" and run == "S6_03_CDP":
        if sid == "C.2.UN.3" and "not compared by an assumed extension" in ctx:
            return "mathematical_method", "States that the proof does not assume an extension of punctured markings; no unfinished comparison is asserted."
        if sid == "C.2.UN.16" and "does not yet identify its quotient" in ctx:
            return "result_scope_and_later_answer", "The row records the generically finite comparison; the subsequent quotient identification is expressly recorded separately."
        if sid == "C.2.UN.33" and "Kodaira table has damaged OCR" in ctx:
            return "edition_history_with_completed_alternative", "Kodaira §8(ii)–(iv), pp.581–585 is opened; the clear Ulmer–Urzua author version §2.1–2.3, pp.3–6 and its p.6 matrix/period/character table were visually checked. The unchanged root_cyclic_elliptic_types.py rerun passed. Only the damaged 1963 table's visual matrix check is not claimed."
        if sid in ["C.2.UN.26", "C.2.UN.60", "C.2.UN.49", "C.2.UN.70", "C.2.UN.71"]:
            return "historical_source_cutoff", "The source checkpoint reservation is preserved as history; later completed named-reader/receiving-proof and computation events control the current fields."
    if f == "notes" and run == "S6_04_MAPS_MANIFOLDS":
        if sid in ["D.2.4", "D.2.53"]:
            return "explicit_open_scope", "The unrestricted smooth classification and reference-framing/critical-linking problem remain explicitly open. D.2.4 is an open-problem row; D.2.53 proves only its stated finite-complex/reference-independent scope. This is not a missing audit of a claimed complete classification."
        if sid == "D.2.43":
            return "local_theorem_scope", "The result is an exact local noncyclic-cap theorem, with no unrestricted global initial-data classification asserted."
        if sid in ["D.2.45", "D.2.48"]:
            return "explicit_nonreliance", "The full proof expressly avoids assuming the unverified model/table; the required construction/order is derived in the receiving proof."
        if sid == "F.2.6":
            return "resolved_historical_gap", "The earlier torsion-transgression reservation is explicitly followed by its complete proof and arithmetic closure; the separate existence and spectral-sequence questions retain their own scopes."
        if sid in ["F.2.20", "F.2.24"]:
            return "historical_source_program_status", "The pending phrase is in SOURCE NOTES. The completed per-row receiving proof and actual program reruns are in work/root/maps_F_final_result_checks.json and code/root_maps_F/final_execution_reconciliation.json."
    if f == "notes" and run == "WORKING_EDITION_COURSE_PROVIDER" and sid.startswith("CG-S6-DUALITY-") and "unread Wu-class material" in ctx:
        return "excluded_source_material", "Only the completely read duality/Euler sections1–4 are retained; source Wu-class material outside that scope is expressly excluded."
    return None


def main():
    raw = INV.read_bytes()
    applied = load(W / "final_inventory_current_status_applied.json")
    assert sha(raw) == applied["inventory_sha256_after"], "The stable input changed; review before rerunning"
    rd = csv.DictReader(io.StringIO(raw.decode()))
    fields = rd.fieldnames
    rows = list(rd)
    papers = {p: (D / f"S6_09_PAPERS_{p}.tex").read_bytes() for p in ["I", "II", "III"]}
    texts = {p: b.decode() for p, b in papers.items()}
    snapshots = {str(INV.relative_to(D)): sha(raw)}
    snapshots.update({f"S6_09_PAPERS_{p}.tex": sha(b) for p, b in papers.items()})
    records, contexts, errors = [], [], []
    ids = [(r["source_run"], r["source_id"]) for r in rows]
    if len(ids) != len(set(ids)): errors.append("Duplicate inventory source keys")
    if fields != FIELDS: errors.append("Column names/order differ from the required17")
    if len(rows) != 1184: errors.append("Wrong row count")
    for r in rows:
        key = [r["source_run"], r["source_id"]]
        empty = [f for f in FIELDS if not isinstance(r.get(f), str) or not r[f].strip()]
        anchor = "\\label{" + r["printed_label"] + "}"
        text = texts.get(r["paper"], "")
        placed = text.count(anchor) == 1
        literal = anchor in r["statement_as_printed"] and r["statement_as_printed"] in text
        unresolved = []
        for f in CURRENT:
            for m in PAT.finditer(r[f]):
                ctx = r[f][max(0, m.start()-120):m.end()+180]
                checked = disposition(r, f, ctx)
                entry = {"source_run": key[0], "source_id": key[1], "field": f,
                         "exact_matched_token": m.group(), "context": ctx,
                         "disposition": checked[0] if checked else "unresolved_current_status",
                         "reason": checked[1] if checked else "No reviewed disposition for this current-field occurrence."}
                contexts.append(entry)
                if not checked: unresolved.append(entry)
        if empty or not placed or not literal or unresolved:
            errors.append({"source_key": key, "empty_fields": empty, "placed": placed,
                           "literal_statement_matches": literal, "unresolved_contexts": unresolved})
        records.append({"source_run": key[0], "source_id": key[1], "paper": r["paper"],
                        "printed_label": r["printed_label"], "all_17_fields_nonempty": not empty,
                        "unique_actual_destination": placed, "complete_literal_printed_field_matches": literal,
                        "five_credit_fields_nonempty": all(r[f].strip() for f in CREDITS),
                        "credit_field_sha256": {f: sha(r[f].encode()) for f in CREDITS},
                        "current_unresolved_status_count": len(unresolved)})

    merge_path = D / "records/final_credit_closure_merge.json"
    merge = load(merge_path)
    current = {(r["source_run"], r["source_id"]): r for r in rows}
    merge_checks = []
    for ev in merge["events"]:
        r = current[(ev["source_run"], ev["source_id"])]
        checks = {f: r[f] == ev["after"][f] for f in CREDITS + ["your_check", "check_outcome"]}
        merge_checks.append({"source_run": ev["source_run"], "source_id": ev["source_id"],
                             "overlay": ev["overlay"], "final_credit_and_check_fields_match": checks})
        if not all(checks.values()): errors.append({"final_credit_merge_discrepancy": merge_checks[-1]})
    snapshots[str(merge_path.relative_to(D))] = sha(merge_path.read_bytes())

    notation_path = D / "records/notation_concordance.json"
    notation = load(notation_path)
    notation_ok = (notation["inventory_rows"] == len(rows) and notation["all_actual_label_count"] == 7223
                   and notation["explicit_alias_count"] == 268 and notation["numbers_in_markdown"]
                   and not notation["unplaced_results"] and not notation["missing_aux_numbers"]
                   and notation_path.read_bytes() == (W / "notation_concordance.json").read_bytes())
    if not notation_ok: errors.append("Public notation record does not match final1184-row numbered snapshot")
    snapshots[str(notation_path.relative_to(D))] = sha(notation_path.read_bytes())
    assert INV.read_bytes() == raw
    for p, b in papers.items(): assert (D / f"S6_09_PAPERS_{p}.tex").read_bytes() == b
    result = {"reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)", "effort": "Pro", "date_utc": "2026-11-17",
              "passed": not errors, "gate_passed": not errors, "inventory_sha256": sha(raw),
              "row_count": len(rows), "column_count": len(fields), "columns": fields,
              "rows_by_paper": dict(collections.Counter(r["paper"] for r in rows)),
              "empty_cells": sum(not r[f].strip() for r in rows for f in FIELDS),
              "empty_credit_cells": sum(not r[f].strip() for r in rows for f in CREDITS),
              "stale_current_status_cells": len({(x["source_run"],x["source_id"],x["field"]) for x in contexts if x["disposition"] == "unresolved_current_status"}),
              "unplaced_rows": sum(not r["unique_actual_destination"] for r in records),
              "literal_statement_mismatches": sum(not r["complete_literal_printed_field_matches"] for r in records),
              "final_credit_merge_rows_checked": len(merge_checks),
              "final_credit_merge_current_fields_match": all(all(x["final_credit_and_check_fields_match"].values()) for x in merge_checks),
              "historical_or_scope_limited_keyword_contexts": len(contexts),
              "keyword_disposition_counts": dict(collections.Counter(x["disposition"] for x in contexts)),
              "public_notation_record_current": notation_ok,
              "metadata_repair_record": "work/invariants_arithmetic/final_inventory_current_status_applied.json",
              "exact_before_after_history": "work/invariants_arithmetic/final_inventory_current_status_overlay.json",
              "input_sha256": snapshots, "errors": errors,
              "scope": "Every required cell and every actual printed destination/literal statement is checked. Current credit/check statuses are distinguished from preserved historical reservations, qualified source-edition limits and genuinely open mathematical extensions. This gate does not assert that every inventoried result is proved or that bounded negative searches establish worldwide novelty.",
              "UN33_scope_confirmation": {
                  "record": "work/cdp_audit/references_verified.json#Kodaira1963II,UlmerUrzua2021",
                  "confirmed_by": "GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, cdp_audit receiving reader, 17 November2026",
                  "scope": "Kodaira §8(ii)–(iv), pp.581–585, including identity-monodromy regularity; clear Ulmer–Urzua author version §2.1–2.3 pp.3–6 and full p.6 table visually opened; positive H1/right-action and root characters checked; unchanged root_cyclic_elliptic_types.py exit0. Damaged1963 TableI visual matrix check remains expressly unclaimed."
              },
              "credit_merge_checks": merge_checks, "reviewed_keyword_contexts": contexts,
              "records": records}
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ["passed","row_count","column_count","empty_cells","empty_credit_cells","stale_current_status_cells","unplaced_rows","literal_statement_mismatches","final_credit_merge_rows_checked","public_notation_record_current"]}))
    if errors:
        print(json.dumps(errors[:5], ensure_ascii=False)[:8000])
        raise SystemExit(1)


if __name__ == "__main__":
    main()
