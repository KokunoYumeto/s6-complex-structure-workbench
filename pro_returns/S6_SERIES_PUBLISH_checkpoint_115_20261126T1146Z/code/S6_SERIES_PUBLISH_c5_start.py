"""Record continuation five and merge the ten attached intake rows verbatim."""
from pathlib import Path
import csv
import datetime as dt

ROOT = Path(__file__).resolve().parents[1]
START = "2026-11-23T18:26:17Z"
MARK = "## Fifth continuation from checkpoint 52"

def write_tsv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

events_path = ROOT / "CHECK_EVENTS.tsv"
with events_path.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f, delimiter="\t")
    fields = reader.fieldnames
    rows = list(reader)
with (ROOT.parent / "CLAUDE_INTAKE_CHECK_EVENTS_20261123.tsv").open(encoding="utf-8", newline="") as f:
    intake = list(csv.DictReader(f, delimiter="\t"))
added = 0
for i, row in enumerate(intake, 1):
    if any(all(old.get(k) == v for k, v in row.items()) for old in rows):
        continue
    new = {k: "" for k in fields}
    new.update(row)
    new.update(event_id=f"publish:c5:claude-intake-20261123:{i:02d}",
               phase="intake of checkpoints 47–52; merged continuation five",
               source_file="CLAUDE_INTAKE_CHECK_EVENTS_20261123.tsv",
               source_row=str(i+1), source_event_type=row["type"],
               evidence_group=f"claude-intake-20261123:{i:02d}",
               publish_input_file="CLAUDE_INTAKE_CHECK_EVENTS_20261123.tsv",
               publish_input_row=str(i+1))
    rows.append(new)
    added += 1
withdrawn = [r for r in rows if r.get("event_id") == "III-C4-02L5-FRESH-TARGETED-ASTRA"]
for row in withdrawn:
    if "withdrawn" not in row["outcome"].lower():
        row["outcome"] += (
            " WITHDRAWN on 2026-11-23 at 14:49 UTC: the pre-proof derivation used the "
            "opposite gluing direction; the written old n=1 gluing is X(-sigma_1) "
            "with p=-13, rather than the asserted p=11. It receives no live "
            "completion or substantive-count credit. The replacement fresh-Euler "
            "event retains its separately established scope."
        )
write_tsv(events_path, fields, rows)

note = f"""\n\n{MARK} — {START}

INCOMPLETE. GPT-6 Astra (OpenAI), ChatGPT Pro mode, continues from the
attached merged checkpoint 52. The numerical effort setting is not separately
exposed. The first recorded session clock is {START}. Every one of the 13,358
base files was verified by restore_cp52.py with zero mismatches before edits.
The supplied continuation prompt supersedes earlier restoration and link rules.
No earlier conversation, Library search, Space or unattached prior file was used.

Paper III is active: 19/128 required identities done, 109 open, and 756 unit
criteria open. The recorded pre-proof derivations and authorized releases for
02JA and 02KC are continued through full comparisons. The separate 02KD
transitive-dependency comparison supplies no new required identity. The 02KF
derivation continues before exposure to its printed proof. Three delegated
comparisons use the preserved chronology; rereading contributes no new
independent method. Source applications wait for the unit-by-unit revision.

The ten attached Claude intake rows were merged preserving their five original
fields exactly and their expressly bounded outcomes. The withdrawn 02L5 event
retains its historical row with explicit exclusion from live credit.
No intake merge, source verification or packaging is counted as row movement.
Paper II's closed manuscript and the Paper I/V texts of record remain reserved
for the joint step. Paper IV follows the complete Paper III gate; its 66 required
checks and 729 unit criteria remain open. D26 applications retain their own rows.

The inherited no-movement count is zero. Review 36 is due 2026-11-23T19:26:17Z,
then reviews hourly. Checkpoint 53 is due 2026-11-23T19:11:17Z, then checkpoints
every 45 minutes. The five-paper publication gate remains open. No per-edit
manifest, seal, inventory refresh or derived-file copy is created.
"""
for name in ("S6_SERIES_PUBLISH_report.md", "PROGRESS_LEDGER.md"):
    path = ROOT / name
    current = path.read_text(encoding="utf-8")
    if MARK not in current:
        path.write_text(current.rstrip() + note + "\n", encoding="utf-8", newline="\n")
print(f"Continuation recorded at {START}; intake events added: {added}; total intake rows: {len(intake)}")
print(f"Withdrawn event rows retained: {len(withdrawn)}")
