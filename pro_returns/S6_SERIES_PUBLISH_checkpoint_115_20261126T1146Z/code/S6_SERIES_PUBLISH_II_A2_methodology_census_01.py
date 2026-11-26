#!/usr/bin/env python3
"""Read-only, hash-bound Paper II event census; writes only its own new receipt.

Counts describe recorded rows and evidence identifiers, not independent proofs.
No source, ledger, inventory, tag, check status, or completion row is modified.
"""
from collections import Counter, defaultdict
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_methodology_census_01"
NAMES = ["CHECK_EVENTS.tsv", "S6_SERIES_PUBLISH_inventory.csv",
         "S6_SERIES_PUBLISH_tags.tsv", "S6_SERIES_PUBLISH_II.tex"]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_table(data, delimiter):
    return list(csv.DictReader(io.StringIO(data.decode("utf-8"), newline=""),
                               delimiter=delimiter))


def summarize(rows):
    types = sorted({r["type"] for r in rows})
    groups = defaultdict(list)
    for r in rows:
        groups[r["evidence_group"]].append(r)
    return {
        "event_rows": len(rows),
        "unique_nonempty_event_ids": len({r["event_id"] for r in rows if r["event_id"]}),
        "empty_event_ids": sum(not r["event_id"] for r in rows),
        "unique_statement_id_strings": len({r["statement_id"] for r in rows}),
        "unique_nonempty_evidence_groups": len({r["evidence_group"] for r in rows if r["evidence_group"]}),
        "empty_evidence_groups": sum(not r["evidence_group"] for r in rows),
        "by_type": {t: {"event_rows": sum(r["type"] == t for r in rows),
                       "unique_evidence_groups": len({r["evidence_group"] for r in rows if r["type"] == t})}
                    for t in types},
        "by_phase": dict(sorted(Counter(r["phase"] for r in rows).items())),
        "evidence_group_row_multiplicity": dict(sorted(Counter(len(v) for v in groups.values()).items())),
        "groups_containing_multiple_types": sum(len({r["type"] for r in v}) > 1 for v in groups.values()),
        "groups_containing_multiple_statement_ids": sum(len({r["statement_id"] for r in v}) > 1 for v in groups.values()),
    }


started = datetime.now(timezone.utc).isoformat()
snapshot = {name: (ROOT / name).read_bytes() for name in NAMES}
events = read_table(snapshot[NAMES[0]], "\t")
inventory = read_table(snapshot[NAMES[1]], ",")
tags = read_table(snapshot[NAMES[2]], "\t")
paper_map = defaultdict(set)
inventory_ii = set()
tag_ii = set()
for rows, fields, selected in [(inventory, ("label", "current_statement_owner"), inventory_ii),
                               (tags, ("label", "current_owner"), tag_ii)]:
    for r in rows:
        for field in fields:
            label = r[field]
            if label:
                paper_map[label].add(r["paper"])
                if r["paper"] == "II":
                    selected.add(label)
statement_rows = [r for r in events if r["statement_id"] in inventory_ii]
all_ii_rows = [r for r in events if r["statement_id"] in inventory_ii | tag_ii]
ids = Counter(r["event_id"] for r in events)
assert all(r["event_id"] for r in events)
assert max(ids.values()) == 1
assert not any(len(paper_map[r["statement_id"]]) > 1 for r in all_ii_rows)
ii_groups = {r["evidence_group"] for r in all_ii_rows}
outside_group_rows = [r["event_id"] for r in events
                      if r["statement_id"] not in inventory_ii | tag_ii
                      and r["evidence_group"] in ii_groups]
correction_rows = [r for r in all_ii_rows if r["phase"] == "publication correction and comparative proof review"]
correction_groups = defaultdict(list)
for n, r in enumerate(events, 1):
    if r in correction_rows:
        correction_groups[r["evidence_group"]].append({
            "ledger_data_record": n,
            **{k: r[k] for k in ["statement_id", "event_id", "type", "date_utc"]}
        })
initial_ledger_sha = "2b509a4485fa0851701e45b0ff856187187fa2a377ba2e0d2e9822f69d880d8c"
old_prefix = snapshot[NAMES[0]].splitlines(keepends=True)[:-1]
prefix_sha = sha(b"".join(old_prefix))
assert prefix_sha == initial_ledger_sha
assert events[-1]["event_id"] == "publish:editorial-dispositions01:01FH-title"

receipt = {
    "scope": "Read-only metadata census. No proof rereading, independent derivation, new check event, or canonical mutation.",
    "started_utc": started,
    "input_bindings": {name: {"sha256": sha(data), "bytes": len(data)} for name, data in snapshot.items()},
    "program": {"path": str(Path(__file__).relative_to(ROOT)), "sha256": sha(Path(__file__).read_bytes())},
    "mapping_rule": "Exact statement_id membership in the union of label and current_statement_owner for II inventory rows. The separately reported expanded scope also includes label/current_owner in II tag rows. No lexical prefix inference or proof-content inference.",
    "statement_linked_scope": summarize(statement_rows),
    "all_mapped_II_reference_entities_scope": summarize(all_ii_rows),
    "series_ledger_context": summarize(events),
    "scope_difference": [{k: r[k] for k in ["statement_id", "event_id", "type", "evidence_group"]}
                         for r in all_ii_rows if r["statement_id"] not in inventory_ii],
    "inventory_only_event_labels": sorted({r["statement_id"] for r in statement_rows if r["statement_id"] not in tag_ii}),
    "unmapped_ledger_identifiers": dict(sorted(Counter(r["statement_id"] for r in events if not paper_map[r["statement_id"]]).items())),
    "duplicate_event_ids": [],
    "ambiguous_II_paper_assignments": [],
    "II_group_rows_outside_II_mapping": outside_group_rows,
    "latest_correction_summary": summarize(correction_rows),
    "latest_correction_groups": dict(correction_groups),
    "historical_observation_before_FH_title_event": {
        "ledger_sha256": initial_ledger_sha, "ledger_rows": 8418,
        "statement_linked_rows": 2550, "statement_linked_groups": 2285,
        "all_mapped_II_rows": 2552, "all_mapped_II_groups": 2287,
        "verified_as_exact_current_ledger_byte_prefix": prefix_sha,
        "last_appended_event": {k: events[-1][k] for k in ["statement_id", "event_id", "type", "evidence_group", "date_utc"]},
    },
    "interpretation_limits": [
        "An event row is not an independent proof. A group identifier is a recorded grouping, not a certificate of independence.",
        "Type-specific unique-group counts overlap; they must not be added to obtain the total.",
        "Inventory-linked historical identifiers and merged/retired owners remain counted. Distinct statement_id strings are not the number of currently printed statements.",
        "The two equation-target rows are source-opening records, not whole-statement proof reviews; they are excluded from the primary statement-linked total.",
        "The latest compact construction, its R13/P4.40 refutations, P205 computation and exposed comparative reviews share one evidence group.",
        "A froze the whole-domain argument before its R13 target release, but used C's disclosed research after C had read the target. This is not independent rediscovery of C's global period construction.",
        "P206 and its four consumer reference reviews are exposed comparative/local computation work in a second evidence group.",
        "No event outcome, legacy independence claim, theorem proof, or cross-paper ownership history is re-audited by this census.",
    ],
}
for name in NAMES:
    assert (ROOT / name).read_bytes() == snapshot[name], f"Concurrent input mutation: {name}"
receipt["verified_unchanged_at_utc"] = datetime.now(timezone.utc).isoformat()
OUT.mkdir(exist_ok=False)
receipt_path = OUT / "S6_SERIES_PUBLISH_II_A2_methodology_census_01.json"
receipt_path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"receipt": str(receipt_path.relative_to(ROOT)), "sha256": sha(receipt_path.read_bytes()),
                  "statement_linked": receipt["statement_linked_scope"],
                  "all_II_entities": receipt["all_mapped_II_reference_entities_scope"],
                  "correction": receipt["latest_correction_summary"]}, indent=2))
