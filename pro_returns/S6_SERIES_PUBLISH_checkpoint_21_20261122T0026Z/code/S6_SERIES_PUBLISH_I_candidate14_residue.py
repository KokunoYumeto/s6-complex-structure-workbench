#!/usr/bin/env python3
"""Apply three reviewed prose deletions to the frozen candidate14 source.

This records a literal, reversible source edit and a complete-block comparison.
It does not record a new mathematical derivation or check event.
"""
from pathlib import Path
import collections
import csv
import datetime
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "agents/i_cont_edits"
EXPECTED_SOURCE = "1f2d0d376f71e7843265976aeeb72cf8e1ff77aea176ff5dbb4e67446c25b36f"
CANDIDATE14_PDF = "1abe0fc16350045cd2ce0aae57ce377dcfe2400de0b0bf58ba7e559d360bcb37"
sha = lambda data: hashlib.sha256(data).hexdigest()
csv.field_size_limit(100_000_000)


def full_block(text, label):
    pos = text.index(r"\label{" + label + "}")
    heads = list(re.finditer(r"\\begin\{(theorem|proposition|lemma|corollary)\}", text[:pos]))
    head = heads[-1]
    statement_end = text.index(r"\end{" + head[1] + "}", pos) + len(r"\end{" + head[1] + "}")
    assert re.match(r"\s*\\begin\{proof\}", text[statement_end:])
    end = text.index(r"\end{proof}", statement_end) + len(r"\end{proof}")
    return text[head.start():end], statement_end - head.start()


def math_segments(text):
    # Compare all inline/display delimiters and complete numbered math environments.
    text = re.sub(r"(?<!\\)%[^\n]*", "", text)
    parts = []
    for pattern in [
        r"(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$",
        r"(?<!\\)\$(?:\\.|[^$\\])*(?<!\\)\$",
        r"\\\[[\s\S]*?\\\]",
        r"\\\([\s\S]*?\\\)",
        r"\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?|eqnarray\*?)\}[\s\S]*?\\end\{(?:equation\*?|align\*?|gather\*?|multline\*?|eqnarray\*?)\}",
    ]:
        parts.append(re.findall(pattern, text))
    return parts


def main():
    source = ROOT / "S6_SERIES_PUBLISH_I.tex"
    defect_log = ROOT / "S6_SERIES_PUBLISH_defects_I.tsv"
    before_bytes = source.read_bytes()
    assert sha(before_bytes) == EXPECTED_SOURCE
    before = before_bytes.decode("utf-8")
    assert "\r" not in before
    guards_path = ROOT / "agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate14_infra_guards.json"
    infra_guards = json.loads(guards_path.read_text())
    assert len(infra_guards) == 2
    changes = []
    labels = ["push:src:B.4.22", "push:src:B.4.23"]
    for g, label in zip(infra_guards, labels):
        assert g["source_sha256"] == EXPECTED_SOURCE
        for field in ["original_full_proof", "proposed_full_proof"]:
            assert sha((ROOT / g[field]).read_bytes()) == g[field + "_sha256"]
        a = (ROOT / g["original_full_proof"]).read_text()
        b = (ROOT / g["proposed_full_proof"]).read_text()
        assert before.count(a) == 1
        assert a.count(g["before"]) == 1
        assert a.replace(g["before"], g["after"], 1) == b
        changes.append({"guard_id": g["id"], "type": g["type"],
                        "old": g["before"], "new": g["after"],
                        "statement_id": label, "old_candidate14_page": g["page"],
                        "reason": g["reason"] + " Complete current statement and proof read; exact replacement compared. All mathematical segments, source locators, labels and targets are preserved.",
                        "origin": str(guards_path.relative_to(ROOT))})
    changes.append({
        "guard_id": "I14-root-03", "type": "D11", "statement_id": "fam:src:A.5.2",
        "old": "=H^1(Q(6))=0$; its splitting is not asserted canonical.",
        "new": "=H^1(Q(6))=0$.", "old_candidate14_page": 325,
        "reason": "The statement asserts the displayed direct images, and the proof establishes the existence of the extension splitting through Ext^1(O(-6),Q)=H^1(Q(6))=0 with Q=O(-1)|_{2p_1}. Remove the repeated negative scope sentence about canonicity. The complete theorem and appended connecting-map, cokernel and extension argument are unchanged apart from this deletion; every mathematical segment, label and target is preserved.",
        "origin": "root-reviewed exact guard, continuation 21 November 2026"})

    after = before
    for g in changes:
        assert before.count(g["old"]) == 1
        assert after.count(g["old"]) == 1
        g["old_source_line"] = before[:before.index(g["old"])].count("\n") + 1
        g["applied_offset"] = after.index(g["old"])
        after = after.replace(g["old"], g["new"], 1)

    reconstructed = after
    for g in reversed(changes):
        start = g["applied_offset"]
        assert reconstructed[start:start + len(g["new"])] == g["new"]
        reconstructed = reconstructed[:start] + g["old"] + reconstructed[start + len(g["new"]):]
    assert reconstructed == before
    anchor_counts = {}
    for name, pattern in [
        ("labels", r"\\label\{([^}]+)\}"),
        ("tag_targets", r"\\hypertarget\{(tag-[^}]+)\}"),
        ("all_targets", r"\\hypertarget\{([^}]+)\}"),
    ]:
        a, b = re.findall(pattern, before), re.findall(pattern, after)
        assert a == b
        anchor_counts[name] = len(a)
    archives = []
    unaffected_before, unaffected_after = before, after
    for number, g in enumerate(changes, 1):
        a, a_end = full_block(before, g["statement_id"])
        b, b_end = full_block(after, g["statement_id"])
        assert a[:a_end] == b[:b_end]
        assert a.count(g["old"]) == 1
        assert a.replace(g["old"], g["new"], 1) == b
        assert math_segments(a) == math_segments(b)
        marker = "COMPARED_COMPLETE_BLOCK:" + g["statement_id"]
        assert unaffected_before.count(a) == unaffected_after.count(b) == 1
        unaffected_before = unaffected_before.replace(a, marker, 1)
        unaffected_after = unaffected_after.replace(b, marker, 1)
        stem = OUT / f"S6_SERIES_PUBLISH_I_candidate14_residue_{number:02d}"
        pa = Path(str(stem) + "_current_full_block.tex")
        pb = Path(str(stem) + "_replacement_full_block.tex")
        pa.write_text(a)
        pb.write_text(b)
        archives.append({"statement_id": g["statement_id"],
                         "before": str(pa.relative_to(ROOT)), "before_sha256": sha(pa.read_bytes()),
                         "after": str(pb.relative_to(ROOT)), "after_sha256": sha(pb.read_bytes()),
                         "complete_statement_bytes_unchanged": True,
                         "all_other_proof_bytes_unchanged": True,
                         "mathematical_segments_identical": True})
    assert unaffected_before == unaffected_after

    log_before_bytes = defect_log.read_bytes()
    with defect_log.open() as f:
        reader = csv.DictReader(f, delimiter="\t")
        fieldnames = reader.fieldnames
        rows = list(reader)
    assert len(rows) == 1974
    old_rows = [dict(row) for row in rows]
    for g in changes:
        line, page = g["old_source_line"], g["old_candidate14_page"]
        row = {key: "" for key in fieldnames}
        row.update({"change_id": f"I-{len(rows) + 1:05d}", "type": g["type"],
                    "statement_id": g["statement_id"],
                    "old_location": f"candidate14 source line {line}; {g['statement_id']}",
                    "old_page": str(page), "new_location": g["statement_id"],
                    "new_page": "pending candidate15 build", "old_text": g["old"],
                    "new_text": g["new"], "reason": g["reason"],
                    "review_status": "applied; complete affected proof read and exact comparison complete; candidate15 changed-page reading pending",
                    "mapped_old_location": f"candidate14 {g['statement_id']}; page {page}",
                    "mapped_new_location": "pending candidate15 build and changed-page reading",
                    "page_mapping_method": f"actually read candidate14 whole page and literal source guard; source SHA {EXPECTED_SOURCE}; PDF SHA {CANDIDATE14_PDF}"})
        rows.append(row)
        g["change_id"] = row["change_id"]
    assert rows[:1974] == old_rows
    assert sha(source.read_bytes()) == EXPECTED_SOURCE
    assert defect_log.read_bytes() == log_before_bytes
    source.write_text(after)
    with defect_log.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    receipt = {
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "checker": "GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation 21 November 2026",
        "before_source_sha256": EXPECTED_SOURCE,
        "after_source_sha256": sha(source.read_bytes()),
        "candidate14_pdf_sha256": CANDIDATE14_PDF,
        "before_defect_log_sha256": sha(log_before_bytes),
        "after_defect_log_sha256": sha(defect_log.read_bytes()),
        "guard_file": str(guards_path.relative_to(ROOT)),
        "guard_file_sha256": sha(guards_path.read_bytes()),
        "changes": changes, "archives": archives,
        "full_current_statements_and_proofs_read": True,
        "replacement_differences_read_and_compared": True,
        "exact_reverse_reconstruction_verified": True,
        "all_math_segments_and_label_and_target_sequences_preserved": True,
        "anchor_counts": anchor_counts,
        "existing_log_rows_preserved": 1974,
        "new_defect_rows": 3, "total_defect_rows": len(rows),
        "mathematical_statement_changes": 0, "mathematical_events_added": 0,
        "pending": ["candidate15 build", "every changed whole page actually read", "candidate15 source/PDF/ledger/provenance binding", "final defect-page mapping"]}
    receipt_path = OUT / "S6_SERIES_PUBLISH_I_candidate14_residue_receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    (OUT / "S6_SERIES_PUBLISH_I_candidate14_residue.diff").write_text("".join(difflib.unified_diff(before.splitlines(True), after.splitlines(True), fromfile="candidate14", tofile="candidate15/source")))
    print(json.dumps({key: receipt[key] for key in ["created_utc", "after_source_sha256", "after_defect_log_sha256", "new_defect_rows", "total_defect_rows", "mathematical_statement_changes", "mathematical_events_added", "anchor_counts"]}, indent=2))


if __name__ == "__main__":
    main()
