"""Admit the completely compared horizontal/interface package.

Only the manuscript and the existing defect, reading-event and unit tables
change. No derived inventory, manifest or per-edit snapshot is refreshed.
"""
from S6_SERIES_PUBLISH_c4_edit import *
from S6_SERIES_PUBLISH_c4_admit import protected_statement
import csv

csv.field_size_limit(10000000)
prefix = ROOT / "agents/continuation4_horizontal/S6_SERIES_PUBLISH_horizontal"
_, guards = read_tsv(str(prefix) + "_guards.tsv")
_, defects = read_tsv(str(prefix) + "_defects.tsv")
_, events = read_tsv(str(prefix) + "_CHECK_EVENTS.tsv")
_, proposals = read_tsv(str(prefix) + "_unit_proposals.tsv")
assert len(guards) == 21 and len(defects) == 399 and len(events) == 32
before = SOURCE.read_text()
after = before
for guard in guards:
    assert after.count(guard["old_text"]) == 1, guard["change_id"]
    after = after.replace(guard["old_text"], guard["new_text"], 1)
for old, new in zip(identifiers(before), identifiers(after)):
    assert all(new[k] == v for k, v in old.items()), (old - new, new - old)
    assert all(new[k] == 1 for k in new.keys() - old.keys())
for label in ("push:src:E.5.2", "push:src:E.5.3"):
    assert protected_statement(before, label) == protected_statement(after, label)

fields, units = read_tsv(ROOT / "S6_SERIES_PUBLISH_unit_progress.tsv")
key = lambda r: (r["paper"], r["unit_id"], r["defect_type"] or r["row_kind"])
by_key = {key(r): r for r in units}
assert len(by_key) == len(units)
closures = []
for proposal in proposals:
    assert proposal["paper"] == "II" and proposal["unit_id"] == "sec:II:07"
    old = by_key[key(proposal)]
    assert old["status"] == proposal["prior_status"]
    done = proposal["proposed_status"] in ("done after guarded admission", "keep inherited done")
    status = "done" if done else "open"
    assert not (proposal["defect_type"] in ("D14", "D23", "D24") or proposal["row_kind"] == "structure") or status == "open"
    assert proposal["defect_type"] not in ("D10", "D16") or status == "done"
    assert old["status"] != "done" or status == "done"
    if old["status"] != "done" and status == "done":
        closures.append(key(proposal))
    old.update({k: proposal[k] for k in fields if k in proposal})
    old["status"] = status
    old["date_utc"] = now()
    old["detail"] += " Root read every changed full receiving proof, the old/new comparison and the exact earlier-owner alias changes; all 21 guards admitted with identifier multiplicities and protected statements unchanged. Final PDF reading remains open."
assert len(closures) == 20

for row in defects:
    row["review_status"] = "Complete original/receiving proof comparison by horizontal reader; root read the complete changed receiving proofs, comparison and earlier-owner alias diffs. Admitted after exact guards, identifier multiplicities and protected statement checks. Integrated rendering remains pending."
# Validate record-key conflicts before changing the shared manuscript.
for filename, rows, identity in (("S6_SERIES_PUBLISH_defects_II.tsv", defects, "change_id"), ("CHECK_EVENTS.tsv", events, "event_id")):
    _, current = read_tsv(ROOT / filename)
    existing = {r[identity]: r for r in current}
    assert len({r[identity] for r in rows}) == len(rows)
    assert not set(existing).intersection(r[identity] for r in rows)

SOURCE.write_text(after, newline="\n")
print("Exact substitutions:", len(guards))
print("Defect rows:", append_rows(ROOT / "S6_SERIES_PUBLISH_defects_II.tsv", defects, "change_id"))
print("Actual-reading events:", append_rows(ROOT / "CHECK_EVENTS.tsv", events, "event_id"))
write_tsv(ROOT / "S6_SERIES_PUBLISH_unit_progress.tsv", fields, units)
print("Existing open rows closed:", len(closures))
print("New unit rows: 0")
print("All inherited labels/tags and protected E.5.2/E.5.3 statements preserved exactly.")
