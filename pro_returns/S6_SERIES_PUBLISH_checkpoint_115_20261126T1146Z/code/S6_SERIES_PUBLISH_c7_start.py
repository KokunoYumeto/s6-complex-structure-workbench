"""Record continuation seven and merge the supplied cp63--70 intake verbatim."""
from pathlib import Path
import csv
import hashlib

ROOT = Path(__file__).resolve().parents[1]
START = '2026-11-24T19:34:24+00:00'
source = ROOT.parent / 'CLAUDE_INTAKE_CHECK_EVENTS_cp63_70.tsv'
target = ROOT / 'CHECK_EVENTS.tsv'
with target.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
original_fields = ['statement_id', 'date', 'who', 'type', 'outcome']
keys = {tuple(row[k] for k in original_fields) for row in rows}
added = 0
with source.open(newline='') as f:
    for i, row in enumerate(csv.DictReader(f, delimiter='\t'), 2):
        key = tuple(row[k] for k in original_fields)
        if key in keys:
            continue
        event = {k: '' for k in fields}
        event.update(row)
        event_id = 'publish:c7:intake63-70:' + hashlib.sha256('\0'.join(key).encode()).hexdigest()[:16]
        event.update(event_id=event_id, phase='current', source_file=source.name,
                     source_row=str(i), source_event_type=row['type'],
                     evidence_group=event_id, publish_input_file=source.name,
                     publish_input_row=str(i), date_utc=START,
                     where='Supplied cp63--70 intake; scope and exclusions retained verbatim.')
        rows.append(event)
        keys.add(key)
        added += 1
if added:
    with target.open('w', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)

note = f'''

## Continuation seven started — {START}

INCOMPLETE. Restored the attached merged checkpoint 70 once. The supplied
restore_cp70.py verified all 14,751 base files with zero size or SHA-256
mismatches. No unreceived work after checkpoint 70 is assumed. This
continuation starts with Paper III at 92/128 required checks complete,
36 open, and all 756 unit criteria open. Paper IV retains 66 required
checks and 729 unit criteria. Paper II is final; I and V retain their
closed gates until the five-together step. Review 48 is the latest
received review; the consecutive reviews without movement counter is zero.

Merged the six attached CLAUDE_INTAKE_CHECK_EVENTS_cp63_70.tsv events with
their five source fields preserved verbatim, including every scope
restriction. These events close no required check. The checkpoint-70
paragraph repeats a stale KR embargo sentence: Review 48 and the required
table establish its individual original release at 16:55:27 UTC. Its
comparison and admission remain pending. KS remains embargoed.

Work resumes on the complete corrected global class, cap square, return
index, oriented sphere and mapping torus for 02S8/02S9, the proposed
02KS cubic obstruction and complete refinement, and the pending 02KR
comparison. New derivations are kept in continuation7 checker folders.
No manuscript or closed paper gate has been changed at this start.

The next 45-minute checkpoint is 71, due 2026-11-24T20:19:24+00:00.
The next hourly review is 49, due 2026-11-24T20:34:24+00:00.
Checkpoint packing and restoration earn no movement credit.
'''
for name in ['S6_SERIES_PUBLISH_report.md', 'PROGRESS_LEDGER.md']:
    path = ROOT / name
    text = path.read_text()
    if '## Continuation seven started' not in text:
        path.write_text(text + note, newline='\n')
print(f'Continuation start {START}; intake events added {added}; no row closed.')
