#!/usr/bin/env python3
"""Publish the current all-paper notation record, preserving its old public copy."""
import hashlib
import json
from pathlib import Path

D = Path(__file__).resolve().parents[2]
current = D / "work/invariants_arithmetic/notation_concordance.json"
public = D / "records/notation_concordance.json"
raw = current.read_bytes()
obj = json.loads(raw)
assert obj["inventory_rows"] == 1184 and obj["all_actual_label_count"] == 7223
assert obj["explicit_alias_count"] == 268 and obj["numbers_in_markdown"]
assert not obj["unplaced_results"] and not obj["missing_aux_numbers"]
sha = lambda b: hashlib.sha256(b).hexdigest()
old = public.read_bytes()
record = D / "records/notation_concordance_final_refresh.json"
if old == raw:
    assert record.exists(), "Matching public record needs its explicit provenance"
    print(json.dumps({"already_current": True, "public_sha256": sha(raw)}))
else:
    oldobj = json.loads(old)
    archive = D / ("records/notation_concordance_historical_" + sha(old)[:16] + ".json")
    if archive.exists():
        assert archive.read_bytes() == old
    else:
        archive.write_bytes(old)
    tmp = public.with_suffix(".refresh-tmp")
    tmp.write_bytes(raw)
    assert public.read_bytes() == old and current.read_bytes() == raw
    tmp.replace(public)
    result = {
        "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)", "effort": "Pro",
        "date_utc": "2026-11-17", "passed": True,
        "old_public_sha256": sha(old), "old_inventory_rows": oldobj.get("inventory_rows"),
        "old_unplaced_result_count": len(oldobj.get("unplaced_results", [])),
        "historical_archive": str(archive.relative_to(D)),
        "current_source_record": str(current.relative_to(D)),
        "current_public_record": str(public.relative_to(D)),
        "public_sha256": sha(raw), "byte_identical_to_current_work_record": True,
        "inventory_rows": obj["inventory_rows"], "all_actual_labels": obj["all_actual_label_count"],
        "explicit_aliases": obj["explicit_alias_count"], "unplaced_results": 0,
        "missing_aux_numbers": 0,
        "scope": "Archive the obsolete 938-row public record and publish the final numbered 1184-row record; no paper, inventory, notation body or proof changed."
    }
    record.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"published": True, "rows": obj["inventory_rows"], "public_sha256": sha(raw), "record": str(record.relative_to(D))}))
