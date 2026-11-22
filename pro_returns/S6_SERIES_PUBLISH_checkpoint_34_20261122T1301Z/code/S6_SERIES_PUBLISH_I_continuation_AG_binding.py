"""Transport the existing A--G comparisons through exact editorial edits.

Every operation is a literal, reversible source map. This script creates no
mathematical checking event and assigns no fresh independence credit.
"""
import argparse
import csv
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT.parent / "S6_SERIES_PUBLISH_work/S6_SERIES_PUBLISH_checkpoint_10"
SHA = lambda value: hashlib.sha256(value).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--extra-edit-receipt", type=Path, action="append", default=[])
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    original_bytes = (BASELINE / "S6_SERIES_PUBLISH_I.tex").read_bytes()
    original = original_bytes.decode()
    current_bytes = (ROOT / "S6_SERIES_PUBLISH_I.tex").read_bytes()
    current = current_bytes.decode()
    receipts = [ROOT / "agents/i_cont_edits" / name for name in [
        "S6_SERIES_PUBLISH_I_continuation_edits_receipt.json",
        "S6_SERIES_PUBLISH_I_continuation_residue_receipt.json",
    ]]
    receipts.extend(path.resolve() for path in args.extra_edit_receipt)
    inputs = []
    changes = []
    mapped = original
    for path in receipts:
        receipt = json.loads(path.read_text())
        assert SHA(mapped.encode()) == receipt["before_source_sha256"]
        for change in receipt["changes"]:
            assert change["old"] and mapped.count(change["old"]) == 1, change["change_id"]
            mapped = mapped.replace(change["old"], change["new"], 1)
            changes.append(change)
        assert SHA(mapped.encode()) == receipt["after_source_sha256"]
        inputs.append(dict(path=str(path.relative_to(ROOT)), sha256=SHA(path.read_bytes())))
    assert mapped == current
    inverse = current
    for change in reversed(changes):
        # The edits receipt proves the full inverse; locate the replacement
        # using its original prefix to disambiguate short replacement strings.
        before = original
        for prior in changes[:changes.index(change)]:
            before = before.replace(prior["old"], prior["new"], 1)
        offset = before.index(change["old"])
        assert inverse[offset:offset + len(change["new"])] == change["new"]
        inverse = inverse[:offset] + change["old"] + inverse[offset + len(change["new"]):]
    assert inverse.encode() == original_bytes

    archive_path = ROOT / "agents/i_topology/S6_SERIES_PUBLISH_I_final_AG_current_binding.json"
    archive = json.loads(archive_path.read_text())
    assert archive["source_sha256"] == SHA(original_bytes)
    assert archive["ledger_sha256"] == SHA((ROOT / "CHECK_EVENTS.tsv").read_bytes())
    blocks = []
    for entry in archive["block_comparisons"]:
        old_block = entry["current_block"]
        assert original.count(old_block) == 1, (entry["label"], "baseline block")
        new_block = old_block
        applied = []
        for change in changes:
            if change["old"] in new_block:
                assert new_block.count(change["old"]) == 1
                new_block = new_block.replace(change["old"], change["new"], 1)
                applied.append(change["change_id"])
        assert current.count(new_block) == 1, (entry["label"], "current block")
        row = dict(scope=entry["scope"], label=entry["label"],
                   prior_block_sha256=SHA(old_block.encode()),
                   current_block_sha256=SHA(new_block.encode()),
                   byte_identical=old_block == new_block, literal_edit_ids=applied)
        if applied:
            row.update(prior_block=old_block, current_block=new_block)
        blocks.append(row)

    headlines = {}
    for letter, entry in archive["headlines"].items():
        assert current.count(entry["statement"]) == 1
        assert current.count(entry["outline"]) == 1
        headlines[letter] = dict(statement_sha256=SHA(entry["statement"].encode()),
                                 outline_sha256=SHA(entry["outline"].encode()),
                                 outline_items=entry["outline_items"],
                                 unchanged_from_candidate13=True)
    csv.field_size_limit(100_000_000)
    events = list(csv.DictReader((ROOT / "CHECK_EVENTS.tsv").open(), delimiter="\t"))
    by_event = {row["event_id"]: row for row in events}
    for event in archive["prior_evidence_event_rows"]:
        assert by_event[event["event_id"]] == event
    for pattern in [r"\\label\{([^}]+)\}", r"\\hypertarget\{tag-([^}]+)\}"]:
        assert re.findall(pattern, original) == re.findall(pattern, current)

    record = dict(
        created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
        paper="I", source_sha256=SHA(current_bytes),
        baseline_source_sha256=SHA(original_bytes),
        ledger_sha256=SHA((ROOT / "CHECK_EVENTS.tsv").read_bytes()), ledger_rows=len(events),
        inherited_global_binding=dict(path=str(archive_path.relative_to(ROOT)),
                                      sha256=SHA(archive_path.read_bytes())),
        edit_receipts=inputs, exact_edits=changes,
        source_exact_forward_and_inverse_maps_verified=True,
        headlines=headlines, blocks=blocks,
        inherited_event_ids=[event["event_id"] for event in archive["prior_evidence_event_rows"]],
        all_label_and_tag_sequences_preserved=True,
        current_headlines_and_40_outline_items_read_by_root=True,
        reading_scope=("Root read all seven complete candidate13 headlines and all forty outline items; "
                       "their current bytes are identical. Root read all literal edit differences and "
                       "the complete inherited global-binding scope. The editing agent's complete "
                       "affected-block comparisons supply the changed-proof editorial scope. "
                       "Unchanged full proofs retain their earlier scoped checking evidence."),
        mathematical_events_added=0, new_independent_credit=0, new_computation_credit=0,
    )
    if args.pdf:
        record["pdf_sha256"] = SHA(args.pdf.read_bytes())
        record["pdf"] = str(args.pdf.resolve().relative_to(ROOT))
    destination = args.out or ROOT / "records/S6_SERIES_PUBLISH_I_continuation_AG_binding.json"
    destination.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(dict(source_sha256=record["source_sha256"], headlines=len(headlines),
                          outline_items=sum(r["outline_items"] for r in headlines.values()),
                          block_associations=len(blocks),
                          byte_identical_blocks=sum(r["byte_identical"] for r in blocks),
                          edited_blocks=[r["label"] for r in blocks if not r["byte_identical"]],
                          exact_edits=len(changes), mathematical_events_added=0), indent=2))


if __name__ == "__main__":
    main()
