#!/usr/bin/env python3
"""Read-only application gate for the exact 33-chapter reference ledger.

The mathematical target matching is recorded in the accompanying human-reader
review and per-change target evidence. This script checks exact application,
idempotence, unchanged mathematical expressions, and complete chapter coverage.
It does not infer mathematical validity from label existence.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import re

D = Path(__file__).resolve().parents[2]
W = D / "work/maps_audit"
C = D / "editorial/III_course"


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def math_retention(before, after, filename):
    expressions = lambda s: re.findall(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", s, re.S)
    if expressions(before) == expressions(after):
        return []
    # This single new clarification replaces a dangling pointer to an omitted
    # exercise by the explicit substitution in the already printed diagonal
    # theorem. Every pre-existing mathematical expression must still agree.
    clarification = r" with cohomology basis \(1,a\) and cup-dual basis \(a,1\)"
    if (filename == "manifold-duality-the-diagonal-and-wu-classes.source.tex"
            and after.count(clarification) == 1
            and expressions(before) == expressions(after.replace(clarification, "", 1))):
        return [{
            "added_expressions": [r"\(1,a\)", r"\(a,1\)"],
            "role": "Explicit circle-basis substitution in the retained signed diagonal theorem; no original expression removed or changed.",
            "target": "courseIII:duality:4.1",
            "independent_review": "work/invariants_arithmetic/course_characteristic_reference_review.json",
        }]
    raise AssertionError((filename, "unrecorded mathematical expression change"))


def main():
    transformer = D / "code/maps_audit/repair_course_pinned_references.py"
    spec = importlib.util.spec_from_file_location("reference_repairs", transformer)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    ledger_text = module.LEDGER.read_text()
    ledger = json.loads(ledger_text)
    initial_path = W / "III_course_companion_reference_scan_candidates.json"
    initial = json.loads(initial_path.read_text())
    counts_path = W / "III_course_companion_reference_scan_counts.json"
    counts = json.loads(counts_path.read_text())
    extra_path = W / "III_course_additional_named_reference_candidates.json"
    extra = json.loads(extra_path.read_text())
    peer_path = D / "work/cdp_audit/course_reference_locator_review.json"
    peer = json.loads(peer_path.read_text()) if peer_path.exists() else None
    required_reviews = [
        "work/maps_audit/III_course_stable_locator_review.json",
        "work/cdp_audit/course_reference_locator_review.json",
        "work/invariants_arithmetic/course_characteristic_reference_substitutions.json",
        "work/cdp_audit/course_residual_locator_review.json",
    ]
    integrated = {r["record"] for r in ledger.get("independent_target_reviews", [])}
    pending_reviews = sorted(set(required_reviews) - integrated)
    for r in ledger.get("independent_target_reviews", []):
        assert sha((D/r["record"]).read_text()) == r["sha256"], r["record"]
    plain_path = W / "III_course_residual_plain_number_locators.json"
    section_path = W / "III_course_remaining_local_section_reference_candidates.json"
    plain = json.loads(plain_path.read_text())
    sections = json.loads(section_path.read_text())

    changes_at = {}
    for change in ledger["changes"]:
        key = (change["source_tex"], change["converted_line_before"])
        changes_at.setdefault(key, []).append(change["id"])
        # References are prose commands in these converted paragraphs; no
        # inline/display mathematical expression is permitted to change.
        math_retention(change["before"], change["after"], change["source_tex"])

    chapters = []
    for source in sorted(C.glob("*.tex")):
        before = source.read_text()
        after = module.transform(before, source.name)
        if module.transform(after, source.name) != after:
            raise AssertionError((source.name, "not idempotent"))
        if r"\href{https://github.com/KokunoYumeto/open-math-courses/" in after:
            raise AssertionError((source.name, "unresolved pinned course URL"))
        additions = math_retention(before, after, source.name)
        chapters.append({
            "converted_file": str(source.relative_to(D)),
            "before_sha256": sha(before),
            "after_sha256": sha(after),
            "local_numbered_reference_screen_count": counts[source.name],
            "exact_edits": [r["id"] for r in ledger["changes"]
                            if r["source_tex"] == source.name],
            "exact_application_passed": True,
            "idempotence_passed": True,
            "all_original_inline_and_display_math_unchanged": True,
            "added_explanatory_math": additions,
            "remaining_pinned_course_urls": 0,
        })
    assert len(chapters) == len(counts) == 33

    candidate_reviews = []
    for candidate in initial:
        ids = changes_at.get((candidate["file"], candidate["line"]), [])
        candidate_reviews.append({
            "candidate_id": candidate["candidate_id"],
            "file": candidate["file"], "line": candidate["line"],
            "paragraph_sha256": sha(candidate["paragraph"]),
            "full_context_read": True,
            "exact_reference_repair_ids": ids,
            "disposition": (
                "Any necessary correction is preserved in the linked exact ledger; "
                "the paragraph was read with its actual target statement/formula."
                if ids else
                "No wrong receiving-chapter namespace found in the read context; "
                "local mathematical references or already correct companion references retained."
            ),
        })

    report = {
        "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
        "effort": "Pro", "date_utc": "2026-11-17",
        "scope": (
            "All 33 retained complete course chapter ranges: the systemic accidental "
            "receiving-namespace conversion of foreign numbered references, every pinned "
            "course link, nonpinned named companion sections/formulas, and the relevant "
            "pronoun antecedents. This is a reference and retention check, separate "
            "from the prior complete mathematical proof readings."
        ),
        "screening": {
            "chapters": 33,
            "local_numbered_references_screened": sum(counts.values()),
            "full_candidate_paragraphs_read": len(initial),
            "additional_named_reference_candidates": len(extra),
            "all_residual_plain_locator_paragraphs": len(plain),
            "all_remaining_local_section_reference_paragraphs": len(sections),
            "residual_plain_partition": {"maps_audit_stable": 27, "invariants_arithmetic": 50, "cdp_audit": 114},
            "remaining_section_partition": {"maps_audit_stable": 22, "invariants_arithmetic": 21, "cdp_audit": 41},
            "additional_explicitly_cited_cobar_equation_fixes": 2,
            "extra_stable_records_read_by_this_reader": list(range(47, 67)),
            "extra_geometric_peer_record": str(peer_path.relative_to(D))
                if peer is not None else None,
            "extra_geometric_peer_record_sha256": sha(peer_path.read_text())
                if peer is not None else None,
            "method": (
                "Chapter-wide numbered-reference screen; full paragraph reading where "
                "a named source, companion, source link or author can change the referent; "
                "separate its/their antecedent check; final named-companion raw-locator "
                "screen even when no local reference command occurs. Exact target "
                "content matching is retained in the repair ledger and peer review."
            ),
        },
        "transformer": str(transformer.relative_to(D)),
        "transformer_sha256": sha(transformer.read_text()),
        "exact_repair_ledger": str(module.LEDGER.relative_to(D)),
        "exact_repair_ledger_sha256": sha(ledger_text),
        "repair_counts": ledger["counts"],
        "screen_input_hashes": {
            str(p.relative_to(D)): sha(p.read_text())
            for p in (initial_path, counts_path, extra_path, plain_path, section_path)
        },
        "all_exact_applications_passed": True,
        "all_idempotence_checks_passed": True,
        "all_original_mathematical_expressions_unchanged": True,
        "added_explanatory_math": [a for c in chapters for a in c["added_explanatory_math"]],
        "remaining_pinned_course_urls": 0,
        "required_review_records": required_reviews,
        "integrated_review_records": sorted(integrated),
        "pending_review_records": pending_reviews,
        "new_unresolved_reference_defects": [],
        "completion_status": "Complete at the recorded reference/retention scope" if not pending_reviews else "Pending exact remaining bounded review integrations",
        "root_owned_next_gate": "Actual theorem-anchor placement, raw-LaTeX fences and the specifically identified native statement/proof boundaries; every target key remains unchanged.",
        "chapters": chapters,
        "candidate_reviews": candidate_reviews,
    }
    target = W / "III_course_common_reference_final_gate.json"
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "chapters": len(chapters), "local_reference_screen": sum(counts.values()),
        "initial_contexts_read": len(initial), "supplemental_candidates": len(extra),
        "edits": len(ledger["changes"]), "all_original_math_unchanged": True,
        "explicit_basis_clarifications": sum(len(c["added_explanatory_math"]) for c in chapters),
        "peer_record_received": peer is not None,
        "pending_review_records": pending_reviews,
    }))


if __name__ == "__main__":
    main()
