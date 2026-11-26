from pathlib import Path
import csv
import hashlib
import io

root = Path(__file__).resolve().parents[1]
start = '2026-11-24T11:15:57+00:00'
events_path = root / 'CHECK_EVENTS.tsv'
with events_path.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields = reader.fieldnames
    events = list(reader)
source = root.parent / 'CLAUDE_INTAKE_CHECK_EVENTS_20261124.tsv'
with source.open(newline='') as f:
    incoming = list(csv.DictReader(f, delimiter='\t'))
added = 0
for number, original in enumerate(incoming, 2):
    if any(all(row.get(k, '') == v for k, v in original.items()) for row in events):
        continue
    row = dict.fromkeys(fields, '')
    row.update(original)
    row['event_id'] = 'publish:c6:intake20261124:' + str(number)
    row['phase'] = 'sixth continuation intake'
    row['source_file'] = source.name
    row['source_row'] = str(number)
    row['source_event_type'] = original['type']
    row['evidence_group'] = row['event_id']
    row['publish_input_file'] = source.name
    row['publish_input_row'] = str(number)
    events.append(row)
    added += 1
stream = io.StringIO(newline='')
writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
writer.writeheader()
writer.writerows(events)
events_path.write_text(stream.getvalue(), newline='\n')

with (root / 'S6_SERIES_PUBLISH_required_progress_III.tsv').open(newline='') as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
closed = [r['tag'] for r in rows if r['status'] == 'done']
assert len(closed) == 68
source_hash = hashlib.sha256((root / 'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert source_hash == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
entry = f'''

## Sixth continuation started — {start}

INCOMPLETE. Restored the merged checkpoint 62 supplied in the continuation
archive. `python restore_cp62.py` verified all 14,149 base files with zero
size or SHA-256 mismatches. No earlier conversation or external workspace
was used. The current prompt supersedes earlier restoration and link rules.

Paper III starts at 68/128 required checks complete, 60 open, and 756 unit
criteria open. The 036Z and 037K fresh derivations and proof releases survive;
their comparisons remain open. Other prepared fourth/fifth-continuation work
is reused with its recorded exposure status. The manuscript has not changed;
its SHA-256 is {source_hash}.

Merged the two rows of `CLAUDE_INTAKE_CHECK_EVENTS_20261124.tsv` with their
five supplied fields unchanged. Their scope is exactly the named steps of
the 0374 and 036W refinements; they close no additional required row.

Work order: finish III's required checks, then its unit restructuring and
defect repairs, provenance, build and final-page reading; complete IV next;
then the joint five-paper work. II remains final. I and V remain at their
published records until the joint step. No prior gate is reopened by packing.

The qualifying-movement baseline is checkpoint 62's closed set:
{', '.join(closed)}.

Consecutive reviews without movement: 0. Review 43 is due
2026-11-24T12:15:57+00:00 and reviews follow hourly. Checkpoint 63 is due
2026-11-24T12:00:57+00:00 and checkpoints follow every 45 minutes of work.
All required-row states remain in `S6_SERIES_PUBLISH_required_progress_III.tsv`;
all unit-row states remain in `S6_SERIES_PUBLISH_unit_progress.tsv`.
'''
for name in ('S6_SERIES_PUBLISH_report.md', 'PROGRESS_LEDGER.md'):
    p = root / name
    text = p.read_text()
    if '## Sixth continuation started —' not in text:
        p.write_text(text + entry, newline='\n')
print(f'Continuation recorded at {start}; intake rows added: {added}; III required checks: {len(closed)}/128.')
