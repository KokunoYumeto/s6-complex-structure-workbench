"""Start continuation eight, merge the supplied intake, and correct event types."""
from pathlib import Path
import csv
import hashlib
import io
import subprocess
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
START = "2026-11-25T15:23:14+00:00"
WHO = "GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; eighth continuation"

verification = subprocess.run(
    ["python", str(BASE / "restore_cp91.py")], cwd=BASE,
    capture_output=True, text=True, check=True,
)
print(verification.stdout, end="")
assert not verification.stderr

events_path = ROOT / "CHECK_EVENTS.tsv"
with events_path.open(encoding="utf-8", newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields = reader.fieldnames
    rows = list(reader)
source_path = BASE / "CLAUDE_INTAKE_CHECK_EVENTS_cp71_91.tsv"
with source_path.open(encoding="utf-8", newline="") as stream:
    incoming = list(csv.DictReader(stream, delimiter="\t"))
source_fields = ["statement_id", "date", "who", "type", "outcome"]
existing = {tuple(row[k] for k in source_fields) for row in rows}
merged = []
for line, supplied in enumerate(incoming, 2):
    signature = tuple(supplied[k] for k in source_fields)
    if signature in existing:
        continue
    row = {k: "" for k in fields}
    row.update(supplied)
    row["event_id"] = "publish:c8:claude-intake-cp71-91:" + str(line - 1).zfill(2)
    row["phase"] = "continuation8-intake"
    row["source_file"] = source_path.name
    row["source_row"] = str(line)
    row["source_event_type"] = supplied["type"]
    row["evidence_group"] = row["event_id"]
    row["publish_input_file"] = source_path.name
    row["publish_input_row"] = str(line)
    rows.append(row)
    existing.add(signature)
    merged.append(row["event_id"])
corrections = {
    "publish:c7:III:02LF:three-false-intermediate-occurrences": "maps:src:D.2.39",
    "publish:c7:III:02LI:scope-refined": "maps:src:D.2.41",
    "publish:c7:III:02LN:period-index-reason": "maps:src:D.2.46",
}
fixed = []
canonical_type = "refuted, with the refined statement's id"
for row in rows:
    refined_id = corrections.get(row["event_id"])
    if refined_id is None:
        continue
    previous_type = row["type"]
    if previous_type != canonical_type:
        if not row["source_event_type"]:
            row["source_event_type"] = previous_type
        row["type"] = canonical_type
        row["outcome"] = "Refined statement id: " + refined_id + ". " + row["outcome"]
        fixed.append((row["event_id"], previous_type, refined_id))
buffer = io.StringIO(newline="")
writer = csv.DictWriter(buffer, fieldnames=fields, delimiter="\t", lineterminator="\n")
writer.writeheader()
writer.writerows(rows)
events_path.write_text(buffer.getvalue(), encoding="utf-8", newline="\n")
for supplied in incoming:
    assert any(all(row[k] == supplied[k] for k in source_fields) for row in rows)

timestamp = datetime.now(timezone.utc).isoformat()
section = f"""

## Eighth continuation — start {START}

Resumed from the attached merged checkpoint 91. The base verification
completed with 16,237 files verified and zero mismatches. The supplied
prompt supersedes the earlier restore instructions. Work begins with
Paper III: whole reading and admission of 02LT, complete comparison of
02LV, then the fresh synthesis and original comparison of 02LG.
The original and historical target inputs of 02LG remain closed.
The canonical Paper III source is unchanged at
9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0.

Merged all 11 supplied intake events from
CLAUDE_INTAKE_CHECK_EVENTS_cp71_91.tsv with their five supplied fields
verbatim. The three noncanonical refutation types for 02LF, 02LI and
02LN now use the prescribed event type; the receiving statement id is
explicit in each outcome. This changes no mathematical scope or count
of substantive checks and closes no required or publication-unit row.

Current gate: 127/128 Paper III required checks complete, 784 Paper III
unit criteria open; Paper IV has 66 required checks and 756 unit
criteria open. I, II and V keep their individual gates until the
five-paper step. The last received review records movement, so the
consecutive no-movement count starts at zero. First checkpoint due
2026-11-25T16:08:14+00:00 (number 92); first hourly review due
2026-11-25T16:23:14+00:00 (review 64). Further boundaries run from this
continuation's start. The report remains INCOMPLETE.

Startup record written {timestamp}; code/S6_SERIES_PUBLISH_c8_start.py
records the exact intake merge and event-type repairs.
"""
for name in ["S6_SERIES_PUBLISH_report.md", "PROGRESS_LEDGER.md"]:
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    marker = "## Eighth continuation — start " + START
    assert marker not in text, "The start record already exists."
    path.write_text(text.rstrip() + section + "\n", encoding="utf-8", newline="\n")
print("Merged", len(merged), "supplied intake events, preserving all five fields.")
for event_id, previous, refined_id in fixed:
    print("Corrected event type:", event_id, repr(previous), "->", canonical_type,
          "; refined statement", refined_id)
print("Continuation start:", START)
print("Next checkpoint: 92 at 2026-11-25T16:08:14+00:00")
print("Next review: 64 at 2026-11-25T16:23:14+00:00")
