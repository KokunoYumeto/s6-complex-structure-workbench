"""Admit an individually completed comparison after root review.

This records checks only; it never applies a receiver to the manuscript.
"""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse
import csv
import io
import re

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
parser = argparse.ArgumentParser()
parser.add_argument('--tag', required=True)
parser.add_argument('--folder', required=True)
parser.add_argument('--comparison-sha', required=True)
parser.add_argument('--receiver-sha', required=True)
parser.add_argument('--root-review', required=True)
args = parser.parse_args()

def read(path):
    with path.open(newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames, list(reader)

def write(path, fields, rows):
    buf = io.StringIO(newline='')
    writer = csv.DictWriter(buf, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(buf.getvalue(), newline='\n')

progress = ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv'
fields, rows = read(progress)
row = next(r for r in rows if r['tag'] == args.tag)
assert row['status'] == 'open'
assert row['proof_status'] == 'released_after_derivation'
assert row['root_release_authorization']
assert datetime.fromisoformat(row['derivation_completed_utc'].replace('Z','+00:00')) < datetime.fromisoformat(row['proof_released_utc'].replace('Z','+00:00'))
assert sha256((ROOT/row['derivation_path']).read_bytes()).hexdigest() == row['derivation_sha256']
source = ROOT/'S6_SERIES_PUBLISH_III.tex'
raw = source.read_bytes()
text = raw.decode()
assert sha256(raw).hexdigest() == row['released_source_sha256']
folder = ROOT/args.folder
comparison = folder/f'S6_SERIES_PUBLISH_III_{args.tag}_comparison.md'
receiver = folder/f'S6_SERIES_PUBLISH_III_{args.tag}_receiving.tex'
review = ROOT/args.root_review
assert review.is_file() and review.stat().st_size > 0
assert sha256(comparison.read_bytes()).hexdigest() == args.comparison_sha
assert sha256(receiver.read_bytes()).hexdigest() == args.receiver_sha
_, guards = read(folder/f'S6_SERIES_PUBLISH_III_{args.tag}_replacements.tsv')
assert guards
for guard in guards:
    assert guard['statement_id'] == row['label']
    old, new = guard['old_text'], guard['new_text']
    assert old and text.count(old) == 1
    for pattern in (r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\tag\{([^}]+)\}'):
        assert sorted(re.findall(pattern, old)) == sorted(re.findall(pattern, new))
assert receiver.read_text().rstrip('\n') == '\n\n'.join(g['new_text'].rstrip('\n') for g in guards)

eventfile = ROOT/'CHECK_EVENTS.tsv'
event_fields, events = read(eventfile)
proposal = folder/f'S6_SERIES_PUBLISH_III_{args.tag}_CHECK_EVENTS.tsv'
proposal_fields, proposals = read(proposal)
assert event_fields == proposal_fields and proposals
known = {e['event_id'] for e in events}
now = datetime.now(timezone.utc)
for event in proposals:
    assert event['statement_id'] == row['label'] and event['event_id'] not in known
    assert event['type'] in ('targeted proof check','computation or formal certificate','used and rechecked in this run') or event['type'].startswith('refuted')
    assert datetime.fromisoformat(event['date_utc'].replace('Z','+00:00')) <= now
    event['outcome'] += (' Root admitted the completed comparison after the scope-specific full reading recorded in '
                         + args.root_review + '. Exact receiving SHA-256 ' + args.receiver_sha
                         + '. Canonical application and final unit/build/page gates remain open.')
    events.append(event)
    known.add(event['event_id'])

row.update(status='done', packet_status='required_check_complete',
           check_event_id=';'.join(e['event_id'] for e in proposals),
           proof_comparison_evidence=str(comparison.relative_to(ROOT)),
           completion_evidence='; '.join((row['derivation_path'], str(comparison.relative_to(ROOT)), str(receiver.relative_to(ROOT)), args.root_review)),
           source_ownership_status='verified_exact_individual_scope')
row['notes'] += ' Seventh-continuation root admitted the exact completed comparison. Canonical source application, unit restructuring and page review retain separate open rows.'

# All guards and records are checked before these sequential mutations.
write(eventfile, event_fields, events)
write(progress, fields, rows)
defectfile = folder/f'S6_SERIES_PUBLISH_III_{args.tag}_defects.tsv'
defect_fields, defects = read(defectfile)
for defect in defects:
    defect['review_status'] = 'root comparison admitted; source application and final page review pending'
write(defectfile, defect_fields, defects)
assert source.read_bytes() == raw
print(f'Admitted {args.tag} at {now.isoformat()}; III required checks {sum(r["status"]=="done" for r in rows)}/{len(rows)}.')
