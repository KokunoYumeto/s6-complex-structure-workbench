"""Read-only independent inventory/evidence reconciliation at final delivery.

This does not substitute a label check for a mathematical proof review. It
records the actual full-proof, source-retention, program and visual evidence,
and distinguishes pending root packaging records from mathematical gaps.
Only its own audit JSON is written; canonical deliverables remain unchanged.
"""
from pathlib import Path
from collections import Counter, defaultdict
import csv
import datetime
import hashlib
import json
import re

D = Path(__file__).resolve().parents[2]
S = D.parent / "sources"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
load = lambda rel: json.loads((D / rel).read_text())
fields = "source_run source_id source_file paper printed_label kind statement_as_printed wording_vs_source recorded_checks your_check check_outcome found_in_AC26 found_in_E26 found_in_DGKX_v1 found_elsewhere credited_to notes".split()
with (D / "S6_09_PAPERS_inventory.csv").open(newline="") as stream:
    reader = csv.DictReader(stream)
    actual_fields = reader.fieldnames
    rows = list(reader)
identities = Counter((r["source_run"], r["source_id"]) for r in rows)
originals = []
required = set()
for path in sorted((S / "returns").glob("*/*_results.csv")):
    run = path.parent.name
    with path.open(newline="") as stream:
        source_rows = list(csv.DictReader(stream))
    selected = [r for r in source_rows if run != "S6_05_ARITHMETIC" or r["id"].startswith("C.")]
    required.update((run, r["id"]) for r in selected)
    originals.append({"source_file": str(path.relative_to(D.parent)), "sha256": sha(path), "all_rows": len(source_rows), "in_scope_rows": len(selected)})

empty = [{"source_run": r["source_run"], "source_id": r["source_id"], "fields": [f for f in fields if not r[f].strip()]} for r in rows if any(not r[f].strip() for f in fields)]
stale_pattern = re.compile(r"pending source comparison|not (?:yet )?examined|not (?:yet )?checked|global final-run comparison pending|proof comparison pending|source matches not yet complete", re.I)
current_fields = ["your_check", "check_outcome", "found_in_AC26", "found_in_E26", "found_in_DGKX_v1", "found_elsewhere", "credited_to"]
stale = [{"source_run": r["source_run"], "source_id": r["source_id"], "field": f} for r in rows for f in current_fields if stale_pattern.search(r[f])]

papers = {}
missing_destinations = []
missing_aux_destinations = []
shared_destinations = []
for paper in ["I", "II", "III"]:
    tex = D / f"S6_09_PAPERS_{paper}.tex"
    pdf = D / f"S6_09_PAPERS_{paper}.pdf"
    aux = D / f"S6_09_PAPERS_{paper}.aux"
    text = tex.read_text()
    label_counts = Counter(re.findall(r"\\label\{([^}]+)\}", text))
    aux_labels = set(re.findall(r"\\newlabel\{([^}]+)\}", aux.read_text()))
    refs = {s.strip() for match in re.finditer(r"\\(?:ref|eqref|cref|Cref|autoref)\*?\{([^}]+)\}", text) for s in match[1].split(",")}
    by_target = defaultdict(list)
    for row in [r for r in rows if r["paper"] == paper]:
        key = {"source_run": row["source_run"], "source_id": row["source_id"]}
        by_target[row["printed_label"]].append(key)
        if label_counts[row["printed_label"]] != 1:
            missing_destinations.append({**key, "paper": paper, "label": row["printed_label"], "occurrences": label_counts[row["printed_label"]]})
        if row["printed_label"] not in aux_labels:
            missing_aux_destinations.append({**key, "paper": paper, "label": row["printed_label"]})
    shared_destinations.extend({"paper": paper, "label": target, "rows": keys} for target, keys in by_target.items() if len(keys) > 1)
    validation_rel = f"records/{paper}_final_validation.json"
    validation_path = D / validation_rel
    validation = load(validation_rel) if validation_path.exists() else {}
    papers[paper] = {
        "rows": sum(r["paper"] == paper for r in rows),
        "unique_inventory_destinations": len(by_target),
        "tex_sha256": sha(tex), "pdf_sha256": sha(pdf), "aux_sha256": sha(aux),
        "actual_label_count": len(label_counts),
        "duplicate_actual_labels": {k: n for k, n in label_counts.items() if n != 1},
        "unresolved_static_internal_reference_targets": sorted(refs - label_counts.keys()),
        "validation_record": validation_rel,
        "validation_record_exists": validation_path.exists(),
        "validation_matches_current_files": validation.get("tex_sha256") == sha(tex) and validation.get("pdf_sha256") == sha(pdf),
        "validation_explicitly_passed": validation.get("gate_passed") is True,
        "validation_record_sha256": sha(validation_path) if validation_path.exists() else None,
        "scope": "Actual source and AUX identity checks; proof checking is established by the separately identified receiving reviews, not inferred from these labels."
    }

evidence_paths = [
    "work/maps_audit/III_MAPS190_source_to_print_check.json",
    "work/maps_audit/III_course249_final_source_to_print_check.json",
    "work/invariants_arithmetic/maps_D_source_to_print_check.json",
    "work/cdp_audit/push_C_retention/current_final_retention.json",
    "records/II_final_exact_retention_chain.json",
    "records/II_final_label_identity_check.json",
    "records/III_program_index_validation.json",
    "records/notation_concordance.json",
    "records/notation_concordance_final_refresh.json",
    "records/checkpoint_retention.json",
    "validation/III_3da988a3aeb1/maps_changed_review/final_visual_review_build24.json",
]
evidence = [{"file": p, "exists": (D / p).is_file(), "sha256": sha(D / p) if (D / p).is_file() else None} for p in evidence_paths]
maps = load(evidence_paths[0])
course = load(evidence_paths[1])
d69 = load(evidence_paths[2])
push = load(evidence_paths[3])
ii = load(evidence_paths[4])
program = load("records/III_program_index_validation.json")
notation = load("records/notation_concordance.json")
checkpoints = load("records/checkpoint_retention.json")
visual = load("validation/III_3da988a3aeb1/maps_changed_review/final_visual_review_build24.json")
retention = {
    "MAPS": {"complete_blocks": maps["rows"], "passed": maps["passed"], "complete_proofs": maps["complete_proofs"], "failed_ids": maps["failed_ids"], "matches_current_source": maps["paper_III_sha256"] == papers["III"]["tex_sha256"]},
    "course": {"chapters": course["chapters"], "units": course["units"], "passed_chapters": course["passed_chapters"], "passed_units": course["passed_units"], "failed_chapters": course["failed_chapters"], "failed_units": course["failed_units"], "matches_current_source": course["paper_III_sha256"] == papers["III"]["tex_sha256"]},
    "independent_D69": {"passed": d69["passed"], "matches_current_source": d69["paper_III_sha256"] == papers["III"]["tex_sha256"]},
    "PUSH_C": {"all_34_complete_III_blocks_retained": push["all_34_complete_III_blocks_retained"], "all_16_documented_replacements_remain_present": push["all_16_documented_replacements_remain_present"], "matches_current_source": push["III_tex_sha256"] == papers["III"]["tex_sha256"]},
    "II_exact_final_chain": {"passed": ii["passed"], "canonical_blocks": ii["canonical_CDP_blocks_retained"], "complete_E1_1_proof_retained_byte_identically_once": ii["complete_E1_1_proof_retained_byte_identically_once"], "matches_current_source": ii["final_tex_sha256"] == papers["II"]["tex_sha256"]},
}
packaging_items = []
for paper, p in papers.items():
    if not p["validation_matches_current_files"] or not p["validation_explicitly_passed"]:
        packaging_items.append({"owner": "root", "item": f"Refresh {paper} final validation with current frozen files and existing final visual evidence.", "kind": "record finalization", "not_a_mathematical_gap": True})
report = D / "S6_09_PAPERS_report.md"
if report.read_text().splitlines()[0].startswith("INCOMPLETE"):
    packaging_items.append({"owner": "root", "item": "Finalize report status only after all final gates and packaging checks pass.", "kind": "record finalization", "not_a_mathematical_gap": True})

defect = bool(actual_fields != fields or len(rows) != 1184 or len(required) != 745 or any(identities[x] != 1 for x in required) or any(n != 1 for n in identities.values()) or empty or stale or missing_destinations or missing_aux_destinations or any(p["duplicate_actual_labels"] or p["unresolved_static_internal_reference_targets"] for p in papers.values()))
result = {
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)", "effort": "Pro", "date_utc": "2026-11-17", "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "scope": "Read-only final inventory, source-to-print evidence and packaging-record reconciliation. No canonical paper or inventory is changed; no mathematical result is promoted from metadata alone.",
    "inventory_sha256": sha(D / "S6_09_PAPERS_inventory.csv"), "columns": actual_fields, "required_columns_exact": actual_fields == fields,
    "inventory_rows": len(rows), "original_run_rows": len(required), "additional_rows": len(rows) - len(required), "original_result_tables": originals,
    "original_rows_not_retained_exactly_once": [list(x) for x in sorted(required) if identities[x] != 1],
    "duplicate_inventory_keys": [list(x) for x, n in identities.items() if n != 1], "empty_current_fields": empty, "stale_current_fields": stale,
    "missing_or_duplicated_printed_destinations": missing_destinations, "missing_aux_destinations": missing_aux_destinations,
    "shared_inventory_destinations": shared_destinations,
    "shared_destination_scope": "Several distinct source identities intentionally alias one statement with its retained proof(s); these are not duplicate TeX labels. The exact per-row concordance and full-proof reading records govern their disposition.",
    "papers": papers, "evidence_snapshots": evidence, "source_retention": retention,
    "notation": {"inventory_rows": notation["inventory_rows"], "unplaced_results": notation["unplaced_results"], "missing_aux_numbers": notation["missing_aux_numbers"], "output_matches": notation["output_sha256"] == sha(D / "S6_09_PAPERS_notation_sheet.md")},
    "checkpoint_retention": {"archives": len(checkpoints["archives"]), "member_occurrences": len(checkpoints["members"]), "omitted_checkpoint_members": checkpoints["omitted_checkpoint_members"], "scope": "The final root packager must revalidate the member hashes after any metadata updates; this audit does not replace that archive-membership check."},
    "program_catalogue": {"counts": program["counts"], "verified_distinct_archive_files": program["verified_distinct_archive_files"], "receiving_references_present": program["receiving_references_present"], "missing_paths_or_hash_mismatches": program["missing_paths_or_hash_mismatches"], "missing_receiving_labels": program["missing_receiving_labels"], "scope": "Retains five narrative successes without recorded numeric exit, four imported implementations and one historical failed auxiliary. The tex_sha256 in this record identifies its standalone index, not the canonical paper."},
    "III_final_visual": {"pdf_sha256": visual["pdf_sha256"], "matches_current_pdf": visual["pdf_sha256"] == papers["III"]["pdf_sha256"], "selected_pages_covered": visual["current_selected_pages"], "new_pages_actually_viewed": len(visual["actually_viewed_pages"]), "pixel_identical_prior_pages": visual["unchanged_pages_with_prior_actual_visual_review"], "all_eleven_restoration_events_covered": len(visual["eleven_restored_push_events"]) == 11, "outcome": visual["layout_outcome"]},
    "root_final_gate_script_review": {"file": "code/editorial/final_package_gate.py", "sha256": sha(D / "code/editorial/final_package_gate.py"), "finding": "Read in full. It requires all original identities, all literal printed statements, exact open-boundary placements, verified citation provenance, final canonical hashes, clean build logs, visual records, source-retention records, final notation and exact checkpoint member retention. It explicitly separates this consistency gate from mathematical proof verification. No additional blocking manuscript condition was found in this review."},
    "remaining_record_finalization_at_snapshot": packaging_items,
    "new_manuscript_or_inventory_defect_found": defect,
    "scope_limits": ["Not an independent new reading of all 1184 mathematical proofs; earlier exact receiving/proof/source/program records supply those checks.", "Not a claim that every page of each PDF was visually opened; the recorded sampled and former-overflow page scopes apply.", "Bounded literature searches do not establish worldwide absence or priority.", "Final report, II/III validation refreshes and final ZIP CRC/payload-hash gate remain root-owned."],
}
out = D / "work/maps_audit/final_package_independent_gate.json"
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"written": str(out.relative_to(D)), "new_defect": defect, "rows": len(rows), "original_rows": len(required), "remaining_record_finalizations": packaging_items}, ensure_ascii=False))
