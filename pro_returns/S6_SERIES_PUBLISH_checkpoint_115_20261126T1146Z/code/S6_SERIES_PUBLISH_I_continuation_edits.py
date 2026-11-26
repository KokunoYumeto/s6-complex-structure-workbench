#!/usr/bin/env python3
"""Apply the bounded, archived candidate-13 corrections for the continuation.

The complete affected current proof blocks and every replacement difference
were read by GPT-6 Astra (OpenAI), ChatGPT Pro mode, on 21 November 2026.
No independent derivation, numerical computation, or new check event is claimed.
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
EXPECTED = "26a6f5f8b1e911de363bed7346e970bc8fb77b21cf04fe9a2ce4d1f90d95b49e"
PDF_SHA = "519355e39d7d821a10d728d5c8dbf69a50826ee215ab98619803d44e1cae2a2b"
RECORDS_URL = "https://github.com/KokunoYumeto/s6-complex-structure-workbench/tree/1fb9194767aef92abcc06071e3820c2f226b9512/pro_returns/S6_SERIES_PUBLISH_checkpoint_10_20261121T0612Z/"
sha = lambda b: hashlib.sha256(b).hexdigest()
csv.field_size_limit(100_000_000)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    path = ROOT / "S6_SERIES_PUBLISH_I.tex"
    before_bytes = path.read_bytes()
    assert sha(before_bytes) == EXPECTED, "Source is no longer candidate 13"
    before = before_bytes.decode("utf-8")
    assert "\r" not in before
    text = before
    edits = []
    inherited_guards = []
    archives = []
    synctex = json.loads((ROOT / f"records/S6_SERIES_PUBLISH_synctex_cache_{PDF_SHA}.json").read_text())

    def apply(old, new, kind, reason, statement, page=None, origin="continuation"):
        nonlocal text
        assert text.count(old) == 1, (statement, kind, text.count(old))
        start = text.index(old)
        assert before.count(old) == 1, (statement, "not unique in candidate13")
        old_line = before[:before.index(old)].count("\n") + 1
        line_count = old.count("\n") + 1
        mapped_pages = sorted({p for line in range(old_line, old_line + line_count)
                               for p in synctex.get(str(line), [])})
        if page is not None:
            assert page in mapped_pages or not mapped_pages, (page, mapped_pages)
        text = text[:start] + new + text[start + len(old):]
        edits.append({"old": old, "new": new, "type": kind,
                      "statement_id": statement, "reason": reason,
                      "old_source_line": old_line, "old_candidate_pages": mapped_pages,
                      "origin": origin, "applied_offset": start})

    guard_files = [
        ("records/S6_SERIES_PUBLISH_I_candidate13_root_residue_guards.json", None, None),
        ("agents/i_analytic/S6_SERIES_PUBLISH_I_candidate13_Buchdahl_guarded.json", None, None),
        ("agents/i_topology/S6_SERIES_PUBLISH_I_candidate13_page207_D02_guard.json", "D02", "push:src:B.4.10"),
        ("agents/i_provenance/S6_SERIES_PUBLISH_I_candidate13_visual_guards.json", None, None),
    ]
    for filename, default_kind, default_statement in guard_files:
        p = ROOT / filename
        record = json.loads(p.read_text())
        assert record["source_sha256"] == EXPECTED
        inherited_guards.append({"path": filename, "sha256": sha(p.read_bytes())})
        for g in record["guards"]:
            kind = g.get("defect_type", g.get("defect", default_kind))
            if kind is None:
                kind = "D18" if g["id"] == "IA-C13-BUCHDAHL-LOCATOR" else "D02"
            statement = g.get("statement_id", default_statement)
            reason = g["reason"] + " Complete current affected block read; exact archived replacement compared; all remaining bytes of that block preserved."
            apply(g["old"], g["new"], kind, reason, statement,
                  g.get("page", record.get("page")), filename)
    assert len(edits) == 11
    assert collections.Counter(g["type"] for g in edits) == {"D02": 6, "D23": 4, "D18": 1}

    current_files = list(ROOT.glob("records/S6_SERIES_PUBLISH_I_candidate13_root_residue/*current_full_block.tex"))
    current_files += list(ROOT.glob("agents/i_*/S6_SERIES_PUBLISH_I_candidate13*current*tex"))
    for current in sorted(current_files):
        replacement = Path(str(current).replace("_current_", "_replacement_"))
        if not replacement.exists():
            continue
        a = current.read_text()
        b = replacement.read_text()
        assert before.count(a) == 1
        assert text.count(b) == 1
        computed = a
        used = []
        for g in edits:
            if g["old"] in computed:
                assert computed.count(g["old"]) == 1
                computed = computed.replace(g["old"], g["new"], 1)
                used.append(g["statement_id"])
        assert computed == b, current
        proof_marker = "\\begin{proof}"
        statement_unchanged = (a[:a.index(proof_marker)] == b[:b.index(proof_marker)]) if proof_marker in a else None
        if statement_unchanged is not None:
            assert statement_unchanged
        archives.append({"current_path": str(current.relative_to(ROOT)),
                         "current_sha256": sha(current.read_bytes()),
                         "replacement_path": str(replacement.relative_to(ROOT)),
                         "replacement_sha256": sha(replacement.read_bytes()),
                         "complete_statement_bytes_unchanged": statement_unchanged,
                         "archive_equals_exact_guard_replacements": True,
                         "statement_ids": sorted(set(used))})
    assert len(archives) == 9

    accent_edits = [
        ("whose Poincare\ndual is", "whose Poincar\\'e\ndual is", "fam:src:E.1.4"),
        ("Poincare--Lefschetz duality", "Poincar\\'e--Lefschetz duality", "inv:B3.3"),
        ("Poincare duality then gives", "Poincar\\'e duality then gives", "inv:B3.3"),
    ]
    for old, new, statement in accent_edits:
        apply(old, new, "D23", "Restore the acute accent in Poincare's name; all mathematical tokens, maps, groups and conclusions remain unchanged.", statement)
    assert "Poincare" not in text

    old = r"\newcommand{\SsixRepositoryCommit}{83d76022bcd442278b760db9ff438afceed6c6ea}"
    new = old + "\n" + r"\newcommand{\SsixPublishRecords}{" + RECORDS_URL + "}"
    apply(old, new, "D18", "Define the publication-records address once beside the historical program-commit macro, as required by continuation section 0.2. The address is the explicitly requested checkpoint-10 folder; its deposit-time replacement remains a stated delivery step.", "preamble")

    old = """and the writing of 16--20 November 2026. The publication revision
and further checks of this paper were undertaken by GPT-6 Astra
on 20--21 November 2026. The reasoning-effort setting of this
publication session was inherited; the interface exposed no separate
numerical setting."""
    new = """and the writing of 16--20 November 2026. GPT-6 Astra (OpenAI),
in ChatGPT Pro mode, also undertook the publication revision and
further checks of this paper on 20--21 November 2026, including
the continuation on 21 November."""
    apply(old, new, "D15", "Name the model, provider, exposed ChatGPT Pro mode and continuation date explicitly. Preserve the research, re-derivation and writing dates; no separate numerical effort setting is inferred.", "section 1.5")

    old = r"""The historical sources, programs and check records are available in the
\href{https://github.com/KokunoYumeto/s6-complex-structure-workbench/tree/\SsixRepositoryCommit/pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z/}{project repository}.
The additional records and programs of this publication revision
accompany its source distribution."""
    new = r"""The check records and programs are linked from the
\href{\SsixPublishRecords}{project repository}."""
    apply(old, new, "D15", "Replace the false statement that records accompany the deposited TeX by the single mandated link to the publication records, through the preamble macro. Hexagon accepts the TeX source alone, as recorded in continuation section 0.2.", "section 1.5")

    old = "The text and accompanying work are dedicated to the public domain under"
    new = "The text, programs and check records are dedicated to the public domain under"
    apply(old, new, "D15", "Preserve the CC0 dedication while naming its objects directly, without suggesting that separate programs or records accompany the deposited source.", "section 1.5")

    for pattern in (r"\\label\{([^}]+)\}", r"\\hypertarget\{(tag-[^}]+)\}"):
        assert re.findall(pattern, before) == re.findall(pattern, text)
    reconstructed = text
    for g in reversed(edits):
        p = g["applied_offset"]
        assert reconstructed[p:p + len(g["new"])] == g["new"]
        reconstructed = reconstructed[:p] + g["old"] + reconstructed[p + len(g["new"]):]
    assert reconstructed == before
    assert text.count(r"\newcommand{\SsixPublishRecords}") == 1
    assert text.count(r"\href{\SsixPublishRecords}") == 1

    defect_path = ROOT / "S6_SERIES_PUBLISH_defects_I.tsv"
    with defect_path.open() as f:
        reader = csv.DictReader(f, delimiter="\t")
        fieldnames = reader.fieldnames
        rows = list(reader)
    original_defect_sha = sha(defect_path.read_bytes())
    old_count = len(rows)
    for g in edits:
        old_location = f"candidate 13 source line {g['old_source_line']}; {g['statement_id']}"
        pages = ",".join(map(str, g["old_candidate_pages"])) or "nonprinting preamble"
        row = {k: "" for k in fieldnames}
        row.update({"change_id": f"I-{len(rows) + 1:05d}", "type": g["type"],
                    "statement_id": g["statement_id"], "old_location": old_location,
                    "old_page": pages, "new_location": g["statement_id"],
                    "new_page": "pending integrated build", "old_text": g["old"],
                    "new_text": g["new"], "reason": g["reason"],
                    "review_status": "applied; exact source comparison complete; final page review pending",
                    "mapped_old_location": f"candidate13 {g['statement_id']}; pages {pages}",
                    "mapped_new_location": "pending integrated build and changed-page reading",
                    "page_mapping_method": "candidate13 source-bound SyncTeX cache; source SHA 26a6f5f8b1e911de363bed7346e970bc8fb77b21cf04fe9a2ce4d1f90d95b49e; PDF SHA " + PDF_SHA})
        rows.append(row)
        g["change_id"] = row["change_id"]
    path.write_text(text)
    with defect_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    receipt = {"created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "checker": "GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation 21 November 2026",
               "before_source_sha256": EXPECTED, "after_source_sha256": sha(path.read_bytes()),
               "before_defect_log_sha256": original_defect_sha,
               "after_defect_log_sha256": sha(defect_path.read_bytes()),
               "existing_defect_rows": old_count, "new_defect_rows": len(edits),
               "total_defect_rows": len(rows), "changes": edits,
               "guard_files": inherited_guards, "affected_archives": archives,
               "source_labels_and_tag_sequence_preserved": True,
               "exact_reverse_reconstruction_verified": True,
               "check_events_added": 0,
               "proof_scope": "Complete candidate13 affected blocks read and compared against every replacement difference. Nine archived replacements are exactly the eleven guards applied to their complete current blocks; all theorem/lemma/proposition statements are byte-identical. Three later changes restore accents only. No new mathematical derivation, strengthened statement, proof step, numerical value, hypothesis or construction map is introduced.",
               "pending": ["integrated build", "every changed whole-page image read", "final source/PDF/ledger/provenance bindings", "final defect-page mapping"]}
    (OUT / "S6_SERIES_PUBLISH_I_continuation_edits_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    diff = "".join(difflib.unified_diff(before.splitlines(True), text.splitlines(True), fromfile="checkpoint10/candidate13", tofile="continuation/integrated-source"))
    (OUT / "S6_SERIES_PUBLISH_I_continuation_edits.diff").write_text(diff)
    print(json.dumps({k: receipt[k] for k in ["created_utc", "before_source_sha256", "after_source_sha256", "existing_defect_rows", "new_defect_rows", "total_defect_rows", "check_events_added"]}, indent=2))


if __name__ == "__main__":
    main()
