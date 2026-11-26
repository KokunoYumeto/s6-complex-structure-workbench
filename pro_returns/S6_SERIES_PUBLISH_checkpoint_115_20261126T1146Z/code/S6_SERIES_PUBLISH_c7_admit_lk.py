"""Admit only LK, including its fourteen reviewed equation-number changes.

This records the completed check. It does not apply a canonical edit.
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
parser.add_argument('--root-review', required=True)
args = parser.parse_args()
TAG = '02LK'
FOLDER = 'agents/continuation7_iii_general_cusp_receiving'
RECEIVER_SHA = '05449b31014711d8305e0e5e0ea4706698ab2a191e40ad2078e13aaa1bf996db'
COMPARISON_SHA = '875092bba7507707198d3463f192415f6f733d8db386e0d5dca5255af6226a2e'
GUARDS_SHA = 'a29a3eb0f94267223df86f4d658e1c33e602a061cff551bb602dfb3965719a12'
DEFECTS_SHA = '237c96b149d6d8d85f7cd393084c8516925cf83acfb23ed2b1257ad719d80767'
EVENTS_SHA = '176656ba15df71d9aac52f083a47005996415d79a58d0a5bf177d25245e4a195'


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
row = next(r for r in rows if r['tag'] == TAG)
assert row['status'] == 'open'
assert row['proof_status'] == 'released_after_derivation'
assert row['label'] == 'maps:src:D.2.43'
assert row['root_release_authorization']
assert datetime.fromisoformat(row['derivation_completed_utc'].replace('Z', '+00:00')) < datetime.fromisoformat(row['proof_released_utc'].replace('Z', '+00:00'))
assert sha256((ROOT / row['derivation_path']).read_bytes()).hexdigest() == row['derivation_sha256']
source = ROOT / 'S6_SERIES_PUBLISH_III.tex'
raw = source.read_bytes()
text = raw.decode()
assert sha256(raw).hexdigest() == row['released_source_sha256'] == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
folder = ROOT / FOLDER
comparison = folder / f'S6_SERIES_PUBLISH_III_{TAG}_comparison.md'
receiver = folder / f'S6_SERIES_PUBLISH_III_{TAG}_receiving.tex'
guardfile = folder / f'S6_SERIES_PUBLISH_III_{TAG}_replacements.tsv'
defectfile = folder / f'S6_SERIES_PUBLISH_III_{TAG}_defects.tsv'
proposal = folder / f'S6_SERIES_PUBLISH_III_{TAG}_CHECK_EVENTS.tsv'
review = ROOT / args.root_review
assert review.is_file() and review.stat().st_size > 1000
for path, digest in ((comparison, COMPARISON_SHA), (receiver, RECEIVER_SHA),
                     (guardfile, GUARDS_SHA), (defectfile, DEFECTS_SHA),
                     (proposal, EVENTS_SHA)):
    assert sha256(path.read_bytes()).hexdigest() == digest, path
_, guards = read(guardfile)
defect_fields, defects = read(defectfile)
assert len(guards) == 3 and len(defects) == 29
assert [bool(g['new_text']) for g in guards] == [True, True, False]
for guard in guards:
    assert guard['statement_id'] == row['label']
    old, new = guard['old_text'], guard['new_text']
    assert old and text.count(old) == 1
    for pattern in (r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}'):
        assert sorted(re.findall(pattern, old)) == sorted(re.findall(pattern, new))
assert receiver.read_text().rstrip('\n') == '\n\n'.join(g['new_text'].rstrip('\n') for g in guards if g['new_text'])

# Prove the exact old printed tag -> permanent identity -> new equation map.
# This is restricted to the reviewed LK source and receiver bytes above.
equation_tags = {1: '01YY', 2: '01Z4', 3: '01Z5', 4: '01Z6', 5: '01Z7',
                 6: '01Z8', 7: '01Z9', 8: '01ZA', 9: '01ZB', 10: '01YZ',
                 11: '01Z0', 12: '01Z1', 13: '01Z2', 14: '01Z3'}
old_all = '\n\n'.join(g['old_text'] for g in guards)
new_all = receiver.read_text()
assert re.findall(r'\\tag\{([^}]+)\}', old_all) == [f'D.GC{n}' for n in range(1, 15)]
assert not re.findall(r'\\tag\{([^}]+)\}', new_all)
number_rows = [d for d in defects if d['type'] == 'D19']
assert len(number_rows) == 14
for n, target in equation_tags.items():
    tail = r'\hypertarget{tag-' + target + r'}{}\label{maps:eq:D.GC' + str(n) + '}'
    old_number = r'\tag{D.GC' + str(n) + '}' + tail
    new_number = r'\begin{equation}' + tail
    assert old_all.count(old_number) == 1
    assert new_all.count(new_number) == 1
    matches = [d for d in number_rows if d['old_text'] == old_number and d['new_text'] == new_number]
    assert len(matches) == 1 and matches[0]['statement_id'] == row['label']
    print(f'NUMBER_MAP D.GC{n} -> maps:eq:D.GC{n}, tag-{target} -> automatic equation; inverse by the same permanent identity')
assert not any(d['type'] in ('D25', 'D26', 'D27') for d in defects)

eventfile = ROOT / 'CHECK_EVENTS.tsv'
event_fields, events = read(eventfile)
proposal_fields, proposals = read(proposal)
assert event_fields == proposal_fields and len(proposals) == 2
known = {e['event_id'] for e in events}
now = datetime.now(timezone.utc)
for event in proposals:
    assert event['statement_id'] == row['label'] and event['event_id'] not in known
    assert event['type'] in ('targeted proof check', 'used and rechecked in this run')
    assert datetime.fromisoformat(event['date_utc'].replace('Z', '+00:00')) <= now
    event['outcome'] += (' Root admitted the completed comparison after the scope-specific full reading recorded in '
                         + args.root_review + '. Exact receiving SHA-256 ' + RECEIVER_SHA
                         + '. The fourteen D19 changes preserve each permanent identity by the explicitly verified bijection. Canonical application and final unit/build/page gates remain open.')
    events.append(event)
    known.add(event['event_id'])

row.update(status='done', packet_status='required_check_complete',
           check_event_id=';'.join(e['event_id'] for e in proposals),
           proof_comparison_evidence=str(comparison.relative_to(ROOT)),
           completion_evidence='; '.join((row['derivation_path'], str(comparison.relative_to(ROOT)), str(receiver.relative_to(ROOT)), args.root_review)),
           source_ownership_status='verified_exact_individual_scope')
row['notes'] += ' Seventh-continuation root admitted the exact completed comparison, including the following auxiliary and fourteen explicitly mapped D19 equation-number changes. Canonical source application, unit restructuring and page review retain separate open rows.'
for defect in defects:
    defect['review_status'] = 'root comparison admitted; source application and final page review pending'

# All exact guards, schemas, records and identity maps precede mutations.
write(eventfile, event_fields, events)
write(progress, fields, rows)
write(defectfile, defect_fields, defects)
assert source.read_bytes() == raw
print(f'Admitted {TAG} at {now.isoformat()}; III required checks {sum(r["status"] == "done" for r in rows)}/{len(rows)}.')
