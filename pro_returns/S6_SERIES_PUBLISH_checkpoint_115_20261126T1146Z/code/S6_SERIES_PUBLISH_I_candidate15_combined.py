#!/usr/bin/env python3
"""Prepare or apply the three reviewed candidate15 guard batches.

Default operation creates a reviewable proposal and comparison archives only.
Canonical mutation requires --apply and the explicitly reviewed provenance hash.
Completed reading records and canonical status/check files are never written.
"""
from pathlib import Path
import argparse
import collections
import csv
import datetime
import difflib
import hashlib
import io
import json
import re
from S6_SERIES_PUBLISH_synctex_batch import Scanner

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "agents/i_cont_edits"
SOURCE_SHA = "45bf46fc14a50f7a148cdd34bf2be68b04cd89e1cb7d620191c6e8518f7249f8"
PDF_SHA = "b72c6da6acddfd797c82837fbd086e222eeef8e4526ed736328affde474df780"
GUARD_FILES = [
    ("agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate15_root_guards.json", "edcf9a1bd12cca6c7f0f90d84716e657113dbc0b541ae28ebe769ab687c776ac", 14),
    ("agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate15_edits_guards.json", "4d8c3dccad928ae08dc67a48235ed3efaef5535c825178ce4b6854b042d17ae0", 22),
    ("agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate15_provenance_guards.json", "eb55df7eba02abcb71d2e15e252b92fdd060bce5b9f202d62aa64711c4727160", 26),
]
IMMUTABLE_READINGS = {
    "agents/i_cont_edits/S6_SERIES_PUBLISH_I_final_candidate15_reading_edits.json": "e3c53f4c427d5668a2e09a7947d0b068deb0521e7515baa76ac40bd641162cad",
    "agents/i_cont_provenance/S6_SERIES_PUBLISH_I_final_candidate15_reading_provenance.json": "7f8ab4fe229a633d5c122413df54edc73af990e1cab875b14d8a033a363d1d55",
}
sha = lambda data: hashlib.sha256(data).hexdigest()
csv.field_size_limit(100_000_000)


def inline(text):
    return re.findall(r"(?<!\\)\$(?:\\.|[^$\\])*(?<!\\)\$", text)


def displays(text):
    return [re.findall(pattern, text) for pattern in [
        r"\\\[[\s\S]*?\\\]", r"(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$",
        r"\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}[\s\S]*?\\end\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}",
    ]]


def source_block(text, position):
    bib_start = text.index(r"\begin{thebibliography}")
    if position > bib_start:
        starts = list(re.finditer(r"\\bibitem(?:\[[\s\S]*?\])?\{([^}]+)\}", text))
        head = [m for m in starts if m.start() <= position][-1]
        later = [m.start() for m in starts if m.start() > head.start()]
        end = min(later) if later else text.index(r"\end{thebibliography}", head.end())
        return "bib:" + head[1], head.start(), end, "bibliography entry"
    starts = list(re.finditer(r"\\begin\{(theorem|proposition|lemma|corollary|remark|definition|cited|maintheorem|computed)\}", text))
    head = [m for m in starts if m.start() <= position][-1]
    end = text.index(r"\end{" + head[1] + "}", head.end()) + len(r"\end{" + head[1] + "}")
    if re.match(r"\s*\\begin\{proof\}", text[end:]):
        end = text.index(r"\end{proof}", end) + len(r"\end{proof}")
    assert head.start() <= position < end, (position, head.start(), end)
    label = re.search(r"\\label\{([^}]+)\}", text[head.start():end])[1]
    return label, head.start(), end, "complete statement and attached proof"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--approved-provenance-sha")
    args = parser.parse_args()
    if args.apply:
        assert args.approved_provenance_sha == GUARD_FILES[2][1], "The reviewed provenance guard hash must be supplied explicitly."

    source_path = ROOT / "S6_SERIES_PUBLISH_I.tex"
    log_path = ROOT / "S6_SERIES_PUBLISH_defects_I.tsv"
    before_bytes = source_path.read_bytes()
    assert sha(before_bytes) == SOURCE_SHA
    before = before_bytes.decode()
    assert "\r" not in before
    log_before = log_path.read_bytes()
    with log_path.open() as f:
        reader = csv.DictReader(f, delimiter="\t")
        fields, rows = reader.fieldnames, list(reader)
    assert len(rows) == 1977
    protected_before = {path: sha((ROOT / path).read_bytes()) for path in IMMUTABLE_READINGS}
    assert protected_before == IMMUTABLE_READINGS
    ledger_path = ROOT / "CHECK_EVENTS.tsv"
    ledger_before = sha(ledger_path.read_bytes())
    pdf_path = ROOT / "build/I_candidate15/S6_SERIES_PUBLISH_I.pdf"
    assert sha(pdf_path.read_bytes()) == PDF_SHA

    changes, guard_receipts, provided_blocks = [], [], {}
    for path, digest, expected_count in GUARD_FILES:
        raw = (ROOT / path).read_bytes()
        assert sha(raw) == digest
        document = json.loads(raw)
        guards = document if isinstance(document, list) else document["guards"]
        assert len(guards) == expected_count
        guard_receipts.append({"path": path, "sha256": digest, "guards": len(guards)})
        for guard in guards:
            assert guard["source_sha256"] == SOURCE_SHA
            old, new = guard.get("old", guard.get("before")), guard.get("new", guard.get("after"))
            assert isinstance(old, str) and isinstance(new, str) and before.count(old) == 1, guard["id"]
            position = before.index(old)
            label, start, end, kind = source_block(before, position)
            assert position + len(old) <= end, guard["id"]
            old_inline, new_inline = collections.Counter(inline(old)), collections.Counter(inline(new))
            removed = list((old_inline - new_inline).elements())
            inserted = list((new_inline - old_inline).elements())
            assert not inserted, (guard["id"], inserted)
            change = {"guard_id": guard["id"], "type": guard["type"],
                "statement_id": guard.get("statement_id", label), "owning_block_id": label,
                "old": old, "new": new, "reason": guard["reason"],
                "old_source_line": before[:position].count("\n") + 1,
                "candidate15_read_page": guard.get("page"), "guard_file": path,
                "guard_file_sha256": digest, "original_offset": position,
                "block_start": start, "block_end": end, "block_kind": kind,
                "removed_inline_mentions_in_prose": removed,
                "new_inline_math_segments": [],
                "retained_exact_occurrences_of_removed_mentions_in_block": {token: before[start:end].count(token) - old.count(token) + new.count(token) for token in removed}}
            changes.append(change)
            if "full_block_archive" in guard:
                a = guard["full_block_archive"]
                provided_blocks[(a["original"], a["proposed"])] = (a["original_sha256"], a["proposed_sha256"])
            if "original_full_block" in guard:
                provided_blocks[(guard["original_full_block"], guard["proposed_full_block"])] = (guard["original_full_block_sha256"], guard["proposed_full_block_sha256"])
    assert len(changes) == 62
    assert sum(len(g["removed_inline_mentions_in_prose"]) for g in changes) == 12
    after = before
    for change in changes:
        assert after.count(change["old"]) == 1
        position = after.index(change["old"])
        change["applied_offset"] = position
        after = after[:position] + change["new"] + after[position + len(change["old"]):]
    reverse = after
    for change in reversed(changes):
        position = change["applied_offset"]
        assert reverse[position:position + len(change["new"])] == change["new"]
        reverse = reverse[:position] + change["old"] + reverse[position + len(change["new"]):]
    assert reverse == before
    assert displays(before) == displays(after)
    sequence_counts = {}
    for name, pattern in [
        ("labels", r"\\label\{([^}]+)\}"), ("tag_targets", r"\\hypertarget\{(tag-[^}]+)\}"),
        ("all_targets", r"\\hypertarget\{([^}]+)\}"),
        ("citation_reference_commands", r"\\(?:eqref|ref|cref|Cref|cite|citet|citep)(?:\[[^\]]*\])?\{[^}]+\}"),
        ("bibliography_keys", r"\\bibitem(?:\[[\s\S]*?\])?\{([^}]+)\}"),
    ]:
        a, b = re.findall(pattern, before), re.findall(pattern, after)
        assert a == b, name
        sequence_counts[name] = len(a)

    supplied_archives = []
    for (pa, pb), (ha, hb) in provided_blocks.items():
        a, b = (ROOT / pa).read_text(), (ROOT / pb).read_text()
        assert sha(a.encode()) == ha and sha(b.encode()) == hb
        assert before.count(a) == 1
        transformed = a
        for change in changes:
            if change["old"] in transformed:
                assert transformed.count(change["old"]) == 1
                transformed = transformed.replace(change["old"], change["new"], 1)
        assert transformed == b, pa
        assert after.count(b) == 1
        supplied_archives.append({"original": pa, "original_sha256": ha, "proposed": pb, "proposed_sha256": hb,
                                  "exact_supplied_complete_replacement_verified": True})

    groups = collections.OrderedDict()
    for change in changes:
        groups.setdefault((change["block_start"], change["block_end"]), []).append(change)
    archives = []
    masked_before, masked_after = before, after
    for number, ((start, end), group) in enumerate(groups.items(), 1):
        a = before[start:end]
        b = a
        for change in group:
            assert b.count(change["old"]) == 1
            b = b.replace(change["old"], change["new"], 1)
        assert after.count(b) == 1
        assert displays(a) == displays(b)
        stem = OUT / f"S6_SERIES_PUBLISH_I_candidate15_combined_block_{number:02d}"
        pa, pb, pd = Path(str(stem) + "_original.tex"), Path(str(stem) + "_proposed.tex"), Path(str(stem) + ".diff")
        pa.write_text(a); pb.write_text(b)
        pd.write_text("".join(difflib.unified_diff(a.splitlines(True), b.splitlines(True), fromfile=group[0]["owning_block_id"] + "/candidate15", tofile=group[0]["owning_block_id"] + "/combined-proposal")))
        archives.append({"statement_id": group[0]["owning_block_id"], "kind": group[0]["block_kind"],
            "guard_ids": [g["guard_id"] for g in group], "original": str(pa.relative_to(ROOT)), "original_sha256": sha(pa.read_bytes()),
            "proposed": str(pb.relative_to(ROOT)), "proposed_sha256": sha(pb.read_bytes()), "diff": str(pd.relative_to(ROOT)),
            "diff_sha256": sha(pd.read_bytes()), "every_other_block_byte_unchanged": True, "all_display_math_identical": True})
        marker = "EXACTLY_COMPARED_BLOCK:" + str(number)
        assert masked_before.count(a) == masked_after.count(b) == 1
        masked_before = masked_before.replace(a, marker, 1)
        masked_after = masked_after.replace(b, marker, 1)
    assert masked_before == masked_after

    with Scanner(pdf_path) as scanner:
        for change in changes:
            line = change["old_source_line"]
            pages = sorted({p for ln in range(line, line + change["old"].count("\n") + 1) for p in scanner.pages(source_path, ln)})
            hint = change["candidate15_read_page"]
            if hint is not None:
                assert not pages or hint in pages, (change["guard_id"], hint, pages)
            change["candidate15_synctex_pages"] = pages
            change["candidate15_pages"] = pages or ([hint] if hint is not None else [])
            assert change["candidate15_pages"], change["guard_id"]

    question_start = before.index("The exact analytic leading quotients in\n")
    question_end = before.index(r"\subsection{The unresolved relative-period bound}", question_start)
    question = before[question_start:question_end]
    assert after.count(question) == 1
    assert r"\#\operatorname{Sha}(E_{11}/\mathbb Q)" in question
    question_receipt = {"source_sha256": SOURCE_SHA, "candidate15_page": 330,
        "section_labels": ["ari:open:norm", "ari:C.7.5"], "source_line": before[:question_start].count("\n") + 1,
        "exact_text": question, "text_sha256": sha(question.encode()), "unchanged_in_proposal": True,
        "scope": "Verified the already-existing final-part group-order question supporting the reason for I15-edits-01. No new open question is added."}

    proposal_path = OUT / "S6_SERIES_PUBLISH_I_candidate16_proposed_source.tex"
    proposal_path.write_text(after)
    all_diff = OUT / "S6_SERIES_PUBLISH_I_candidate15_combined.diff"
    all_diff.write_text("".join(difflib.unified_diff(before.splitlines(True), after.splitlines(True), fromfile="candidate15", tofile="candidate16/proposed")))
    receipt = {"created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "paper": "I",
        "checker": "GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation 21 November 2026",
        "mode": "applied" if args.apply else "prepared only",
        "before_source_sha256": SOURCE_SHA, "candidate15_pdf_sha256": PDF_SHA,
        "proposed_source_sha256": sha(after.encode()), "proposal": str(proposal_path.relative_to(ROOT)),
        "before_defect_log_sha256": sha(log_before), "existing_defect_rows": len(rows),
        "guard_files": guard_receipts, "changes": changes, "archives": archives,
        "supplied_complete_block_replacements_verified": supplied_archives,
        "exact_forward_and_inverse_source_maps_verified": True,
        "all_source_outside_compared_blocks_byte_identical": True,
        "all_display_math_sequences_identical": True,
        "label_target_citation_reference_and_bibliography_key_sequences_preserved": True,
        "sequence_counts": sequence_counts,
        "removed_inline_symbol_mentions": {"edits_agent": 9, "provenance_agent": 3, "total": 12,
            "scope": "The individual changes list each repeated/generic inline mention removed only with a quoted scope or production clause. No new inline formula is inserted. No claim of literal equality of all inline-math sequences is made; all operative formulas, hypotheses, maps, values and conclusions retain the full-block comparisons and the reviewed reasons."},
        "unchanged_final_part_question": question_receipt,
        "immutable_reading_records": IMMUTABLE_READINGS,
        "check_ledger_sha256": ledger_before,
        "new_defect_rows": len(changes) if args.apply else 0,
        "proposed_defect_rows": len(changes), "projected_total_defect_rows": len(rows) + len(changes),
        "mathematical_events_added": 0, "canonical_status_files_modified": False,
        "review_scope": "Root reviewed the root batch and editing-agent batch; the complete proof/statement reading and exact guard comparisons remain in their immutable reader receipts. Provenance approval is represented by the explicitly supplied hash at canonical application. The combined implementation verifies exact replacements in every supplied complete block and every newly archived complete block. No independent mathematical derivation is claimed.",
        "pending": ["Root approval of the final provenance batch" if not args.apply else "candidate16 clean build", "every changed final whole-page image actually read", "current source/PDF/provenance/defect-page binding", "remaining individual type statuses"]}

    assert source_path.read_bytes() == before_bytes and log_path.read_bytes() == log_before
    if args.apply:
        original_rows = [dict(row) for row in rows]
        for change in changes:
            pages = ",".join(map(str, change["candidate15_pages"]))
            row = {field: "" for field in fields}
            row.update({"change_id": f"I-{len(rows) + 1:05d}", "type": change["type"], "statement_id": change["statement_id"],
                "old_location": f"candidate15 source line {change['old_source_line']}; {change['statement_id']}", "old_page": pages,
                "new_location": change["statement_id"], "new_page": "pending candidate16 build",
                "old_text": change["old"], "new_text": change["new"], "reason": change["reason"],
                "review_status": "applied; consolidated reviewed guards and complete-block comparisons verified; candidate16 changed-page reading pending",
                "mapped_old_location": f"candidate15 {change['statement_id']}; pages {pages}",
                "mapped_new_location": "pending candidate16 build and changed-page reading",
                "page_mapping_method": f"candidate15 source-bound libsynctex and actual reading guard; source SHA {SOURCE_SHA}; PDF SHA {PDF_SHA}"})
            rows.append(row)
            change["change_id"] = row["change_id"]
        assert rows[:1977] == original_rows
        buffer = io.StringIO(newline="")
        writer = csv.DictWriter(buffer, fieldnames=fields, delimiter="\t")
        writer.writeheader(); writer.writerows(rows)
        source_path.write_text(after)
        log_path.write_bytes(buffer.getvalue().encode())
        receipt.update({"after_source_sha256": sha(source_path.read_bytes()), "after_defect_log_sha256": sha(log_path.read_bytes()),
                        "total_defect_rows": len(rows), "approved_provenance_guard_sha256": args.approved_provenance_sha,
                        "existing_log_rows_preserved": 1977})
    for path, digest in IMMUTABLE_READINGS.items():
        assert sha((ROOT / path).read_bytes()) == digest
    assert sha(ledger_path.read_bytes()) == ledger_before
    name = "S6_SERIES_PUBLISH_I_candidate15_combined_apply_receipt.json" if args.apply else "S6_SERIES_PUBLISH_I_candidate15_combined_preparation.json"
    result_path = OUT / name
    result_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"mode": receipt["mode"], "receipt": str(result_path.relative_to(ROOT)), "receipt_sha256": sha(result_path.read_bytes()),
        "before_source_sha256": SOURCE_SHA, "proposed_source_sha256": receipt["proposed_source_sha256"],
        "after_source_sha256": receipt.get("after_source_sha256"), "after_defect_log_sha256": receipt.get("after_defect_log_sha256"),
        "guards": len(changes), "complete_blocks": len(archives), "proposed_total_rows": 1977 + len(changes),
        "types": dict(collections.Counter(g["type"] for g in changes)), "sequence_counts": sequence_counts,
        "mathematical_events_added": 0}, indent=2))


if __name__ == "__main__":
    main()
