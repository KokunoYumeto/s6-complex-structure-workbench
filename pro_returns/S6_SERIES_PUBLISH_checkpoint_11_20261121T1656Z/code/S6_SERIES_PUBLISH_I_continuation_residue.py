#!/usr/bin/env python3
"""Remove three repeated scope clauses after complete affected-block comparison."""
from pathlib import Path
import csv
import datetime
import difflib
import hashlib
import json
import re
import S6_SERIES_PUBLISH_editing as editing

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent / "S6_SERIES_PUBLISH_work"
OUT = ROOT / "agents/i_cont_edits"
EXPECTED = "118cbc5fc62e7b9cc59a2bb5fdb0bbec691c92bdd9bab8046a6a567164175888"
ORIGINAL = "26a6f5f8b1e911de363bed7346e970bc8fb77b21cf04fe9a2ce4d1f90d95b49e"
PDF_SHA = "519355e39d7d821a10d728d5c8dbf69a50826ee215ab98619803d44e1cae2a2b"
sha = lambda b: hashlib.sha256(b).hexdigest()
editing.SOURCE = BASE
csv.field_size_limit(100_000_000)


def main():
    ed = editing.Editor("I")
    assert sha(ed.before.encode()) == EXPECTED
    original = (BASE / "S6_SERIES_PUBLISH_checkpoint_10/S6_SERIES_PUBLISH_I.tex").read_text()
    assert sha(original.encode()) == ORIGINAL
    synctex = json.loads((ROOT / f"records/S6_SERIES_PUBLISH_synctex_cache_{PDF_SHA}.json").read_text())
    changes = [
        {"statement_id": "push:src:D.4.3", "type": "D11",
         "old": "closure. This does not identify it with that closure.",
         "new": "closure.",
         "reason": "The proposition already states the exact containment of the fixed closed period group in every Chabauty limit. The preceding proof sentence establishes that containment. Remove the repeated scope disclaimer, preserving the complete statement, the explicit period map A, both group formulas, the closedness argument and every other proof byte."},
        {"statement_id": "push:src:D.4.3", "type": "D02",
         "old": "rank is exactly three. This confirms the linear algebra of \\cref{fam:src:C.3.1}, \\cref{fam:src:C.3.2}\nwithout a positivity assumption.",
         "new": "rank is exactly three. This confirms the linear algebra of \\cref{fam:src:C.3.1}, \\cref{fam:src:C.3.2}.",
         "reason": "The exact column-independence calculation states its hypotheses positively and proves rank three. Remove the adjacent defensive clause about a positivity assumption; retain the computation, rank, cited inputs and all mathematical content."},
        {"statement_id": "ari:C.6.R2", "type": "D02",
         "old": "$\\sum|a_n|(R/n_0)^k$ controls accumulated rounding without\nassuming cancellation.",
         "new": "$\\sum|a_n|(R/n_0)^k$ controls accumulated rounding.",
         "reason": "The displayed sum of absolute coefficient values supplies the bound for every normalized moment. Preserve that exact formula, all recurrence inputs and every numerical error allowance; remove the defensive qualification about cancellation."},
    ]
    original_blocks = {label: editing.block(ed.before, label) for label in {g["statement_id"] for g in changes}}
    for g in changes:
        assert ed.text.count(g["old"]) == 1
        g["applied_offset"] = ed.text.index(g["old"])
        ed.replace(g["old"], g["new"], g["type"], g["reason"], g["statement_id"])
        line = original[:original.index(g["old"])].count("\n") + 1
        pages = sorted({p for n in range(line, line + g["old"].count("\n") + 1) for p in synctex.get(str(n), [])})
        g["old_candidate13_source_line"] = line
        g["old_candidate13_pages"] = pages
        page_string = ",".join(map(str, pages))
        ed.rows[-1].update({"old_location": f"candidate13 source line {line}; {g['statement_id']}",
                            "old_page": page_string,
                            "new_page": "pending integrated build",
                            "review_status": "applied; complete affected proof read and exact comparison complete; changed-page reading pending",
                            "mapped_old_location": f"candidate13 {g['statement_id']}; pages {page_string}",
                            "mapped_new_location": "pending integrated build and changed-page reading",
                            "page_mapping_method": f"candidate13 source-bound SyncTeX cache; source SHA {ORIGINAL}; PDF SHA {PDF_SHA}"})
    archives = []
    for n, (label, a) in enumerate(sorted(original_blocks.items()), 1):
        b = editing.block(ed.text, label)
        assert a[:a.index(r"\begin{proof}")] == b[:b.index(r"\begin{proof}")]
        proposed = a
        for g in changes:
            if g["statement_id"] == label:
                assert proposed.count(g["old"]) == 1
                proposed = proposed.replace(g["old"], g["new"], 1)
        assert proposed == b
        prefix = OUT / f"S6_SERIES_PUBLISH_I_continuation_residue_{n:02d}"
        pa, pb = Path(str(prefix) + "_current_full_block.tex"), Path(str(prefix) + "_replacement_full_block.tex")
        pa.write_text(a)
        pb.write_text(b)
        archives.append({"statement_id": label, "before": str(pa.relative_to(ROOT)), "before_sha256": sha(pa.read_bytes()),
                         "after": str(pb.relative_to(ROOT)), "after_sha256": sha(pb.read_bytes()),
                         "complete_statement_bytes_unchanged": True, "all_other_proof_bytes_unchanged": True})
    reconstructed = ed.text
    for g in reversed(changes):
        start = g["applied_offset"]
        assert reconstructed[start:start + len(g["new"])] == g["new"]
        reconstructed = reconstructed[:start] + g["old"] + reconstructed[start + len(g["new"]):]
    assert reconstructed == ed.before
    for pattern in (r"\\label\{([^}]+)\}", r"\\hypertarget\{(tag-[^}]+)\}"):
        assert re.findall(pattern, ed.before) == re.findall(pattern, ed.text)
    log_path = ROOT / "S6_SERIES_PUBLISH_defects_I.tsv"
    with log_path.open() as f:
        old_rows = list(csv.DictReader(f, delimiter="\t"))
    ed.save()
    for i, g in enumerate(changes, len(old_rows) + 1):
        g["change_id"] = f"I-{i:05d}"
    receipt = {"created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "checker": "GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation 21 November 2026",
               "before_source_sha256": EXPECTED, "after_source_sha256": sha(ed.text.encode()),
               "changes": changes, "archives": archives,
               "full_current_blocks_read": True, "replacement_differences_read_and_compared": True,
               "exact_reverse_reconstruction_verified": True, "label_and_tag_sequence_preserved": True,
               "mathematical_statement_changes": 0, "check_events_added": 0,
               "new_defect_rows": len(changes), "total_defect_rows": len(old_rows) + len(changes),
               "pending": ["integrated build", "every changed page image actually read", "final source/PDF/ledger bindings"]}
    (OUT / "S6_SERIES_PUBLISH_I_continuation_residue_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    (OUT / "S6_SERIES_PUBLISH_I_continuation_residue.diff").write_text("".join(difflib.unified_diff(ed.before.splitlines(True), ed.text.splitlines(True), fromfile="continuation/first-edits", tofile="continuation/scope-residue")))
    print(json.dumps({k: receipt[k] for k in ["created_utc", "after_source_sha256", "new_defect_rows", "total_defect_rows", "mathematical_statement_changes", "check_events_added"]}, indent=2))


if __name__ == "__main__":
    main()
