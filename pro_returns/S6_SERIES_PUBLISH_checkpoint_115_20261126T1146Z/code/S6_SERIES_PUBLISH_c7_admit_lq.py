"""Admit only LQ with its reviewed numbering maps and exact auxiliary deletion."""
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
TAG = '02LQ'
FOLDER = 'agents/continuation7_iii_star_logs_receiving'
RECEIVER_SHA = '8fb5f9436aad1b1cf09a27734076a598a34e8ac05bb005fc35d1cae72fb06a7e'
COMPARISON_SHA = '44e2cfed381b92ed95ddfa28de04bd2c6194d1bac9c490e80f32ea04434a2658'
GUARDS_SHA = '0a74c202a9c566cbc61c82d2157ede48722a306ee0e7d7690b74282059625c9d'
DEFECTS_SHA = '21cbe65331a320b097b4a97c69ff3f3261c28e23ce7064884f6bd1f786dc7aeb'
EVENTS_SHA = '01bcdea274efb6758c1ff9b03cb08983110aeb81b732f61bd2e3e13fa25e30fc'


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
assert row['status'] == 'open' and row['proof_status'] == 'released_after_derivation'
assert row['label'] == 'maps:src:D.2.49' and row['root_release_authorization']
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
assert len(guards) == 3 and len(defects) == 49
assert [bool(g['new_text']) for g in guards] == [True, True, False]
assert sha256(guards[-1]['old_text'].encode()).hexdigest() == 'b5b8c09831e7c346d72a294cea9045cf74bf837acbea9586431a7be4f57d68bf'
for guard in guards:
    assert guard['statement_id'] == row['label']
    old, new = guard['old_text'], guard['new_text']
    assert old and text.count(old) == 1
    for pattern in (r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}'):
        assert sorted(re.findall(pattern, old)) == sorted(re.findall(pattern, new))
assert receiver.read_text().rstrip('\n') == '\n\n'.join(g['new_text'].rstrip('\n') for g in guards if g['new_text'])

# The exact manual-number map is restricted to these reviewed bytes.
equation_tags = {1:'0247',2:'024I',3:'024O',4:'024P',5:'024Q',6:'024R',
                 7:'024S',8:'024T',9:'024U',10:'0248',11:'0249',12:'024A',
                 13:'024B',14:'024C',15:'024D',16:'024E',17:'024F',18:'024G',
                 19:'024H',20:'024J',21:'024K',22:'024L',23:'024M',24:'024N'}
old_all = '\n\n'.join(g['old_text'] for g in guards)
new_all = receiver.read_text()
assert set(re.findall(r'\\tag\{([^}]+)\}', old_all)) == {f'D.SL{n}' for n in range(1, 25)}
assert not re.findall(r'\\tag\{([^}]+)\}', new_all)
number_rows = [d for d in defects if d['type'] == 'D19']
assert len(number_rows) == 24
for n, target in equation_tags.items():
    tail = r'\hypertarget{tag-' + target + r'}{}\label{maps:eq:D.SL' + str(n) + '}'
    old_number = r'\tag{D.SL' + str(n) + '}' + tail
    new_number = r'\begin{equation}' + tail
    assert old_all.count(old_number) == 1 and new_all.count(new_number) == 1
    matches = [d for d in number_rows if d['old_text'] == old_number and d['new_text'] == new_number]
    assert len(matches) == 1 and matches[0]['statement_id'] == row['label']
    print(f'NUMBER_MAP D.SL{n} -> maps:eq:D.SL{n}, tag-{target} -> automatic equation; inverse by the same permanent identity')
refutations = [d for d in defects if d['type'] == 'D25']
assert len(refutations) == 1 and refutations[0]['change_id'] == 'III-c7-02LQ-38-complex-orientation-sign'
assert '20465--20467' in refutations[0]['old_location']
assert not any(d['type'] in ('D26', 'D27') for d in defects)

eventfile = ROOT / 'CHECK_EVENTS.tsv'
event_fields, events = read(eventfile)
proposal_fields, proposals = read(proposal)
assert event_fields == proposal_fields and len(proposals) == 3
assert [e['type'] for e in proposals] == ['targeted proof check', "refuted, with the refined statement's id", 'used and rechecked in this run']
assert proposals[1]['event_id'] == 'publish:c7:III:02LQ:complex-orientation-refinement'
assert 'Refuted only original proof item 8 at canonical 20465-20467' in proposals[1]['outcome']
assert 'Refined receiver id maps:src:D.2.49 preserves every theorem conclusion' in proposals[1]['outcome']
known = {e['event_id'] for e in events}
now = datetime.now(timezone.utc)
for event in proposals:
    assert event['statement_id'] == row['label'] and event['event_id'] not in known
    assert datetime.fromisoformat(event['date_utc'].replace('Z', '+00:00')) <= now
    event['outcome'] += (' Root admitted the completed comparison after the scope-specific full reading recorded in '
                         + args.root_review + '. Exact receiving SHA-256 ' + RECEIVER_SHA
                         + '. The24 D19 changes preserve each permanent identity by the explicitly verified bijection. Canonical application and final unit/build/page gates remain open.')
    events.append(event)
    known.add(event['event_id'])
row.update(status='done', packet_status='required_check_complete',
           check_event_id=';'.join(e['event_id'] for e in proposals),
           proof_comparison_evidence=str(comparison.relative_to(ROOT)),
           completion_evidence='; '.join((row['derivation_path'], str(comparison.relative_to(ROOT)), str(receiver.relative_to(ROOT)), args.root_review)),
           source_ownership_status='verified_exact_individual_scope')
row['notes'] += ' Seventh-continuation root admitted the exact completed LQ comparison, including every auxiliary, the narrow orientation refutation and24 bijective D19 maps. Canonical source application, unit restructuring and page review retain separate open rows.'
for defect in defects:
    defect['review_status'] = 'root comparison admitted; source application and final page review pending'

# All exact guards and records are checked before the sequential mutations.
write(eventfile, event_fields, events)
write(progress, fields, rows)
write(defectfile, defect_fields, defects)
assert source.read_bytes() == raw
print(f'Admitted {TAG} at {now.isoformat()}; III required checks {sum(r["status"] == "done" for r in rows)}/{len(rows)}.')
