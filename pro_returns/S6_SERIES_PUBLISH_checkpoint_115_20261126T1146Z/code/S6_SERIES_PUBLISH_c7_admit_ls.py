"""Admit only the completed LS comparison; leave the manuscript unchanged."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import csv
import io
import re

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / 'agents/continuation7_iii_vertical_correction_receiving'
P = 'S6_SERIES_PUBLISH_III_02LS_'
SID = 'maps:src:D.2.50'
REVIEW = 'agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02LS_root_admission_review.md'
csv.field_size_limit(100000000)

def read(path):
    with path.open(newline='') as handle:
        reader = csv.DictReader(handle, delimiter='\t')
        return reader.fieldnames, list(reader)

def write(path, fields, rows):
    buffer = io.StringIO(newline='')
    writer = csv.DictWriter(buffer, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(buffer.getvalue(), newline='\n')

hashes = {
    'receiving.tex': 'da9c75e5b52f01faf8dad478f09eab997fb3c512d75a0cb6689264abac8c87a3',
    'comparison.md': '1f4a746e04e9ad949ba0d11059ae07b14232a34f99a86c2407b2bd49e235c0cf',
    'post_exposure_auxiliaries.md': '4936ba3d22e310d13e77b2ce03629e32c75bdb842dc3c19d7d846e4f5d14c3c9',
    'replacements.tsv': '6f32aca6ca2897bacc04c2c5de65cc70d8ca049006621325f8cfdf0b84e24229',
    'defects.tsv': '7cb78e273bd3fa7490df4644f3b51bd30eacd5ba27c32e853a4e5cd2b9930aad',
    'CHECK_EVENTS.tsv': '8a54e3e6075721ae08df3028776ba7c0d48131b9566565dc2a238e3f32f2c0eb',
}
for name, digest in hashes.items():
    assert sha256((LANE / (P + name)).read_bytes()).hexdigest() == digest, name
assert (ROOT / REVIEW).is_file()
source = ROOT / 'S6_SERIES_PUBLISH_III.tex'
raw = source.read_bytes()
text = raw.decode()
assert sha256(raw).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
progress = ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv'
fields, rows = read(progress)
assert len(rows) == 128 and sum(row['status'] == 'done' for row in rows) == 126
row = next(item for item in rows if item['tag'] == '02LS')
assert row['label'] == SID and row['status'] == 'open'
assert row['proof_status'] == 'released_after_derivation' and row['root_release_authorization']
assert datetime.fromisoformat(row['derivation_completed_utc'].replace('Z', '+00:00')) < datetime.fromisoformat(row['proof_released_utc'].replace('Z', '+00:00'))
assert sha256((ROOT / row['derivation_path']).read_bytes()).hexdigest() == row['derivation_sha256']
_, replacements = read(LANE / (P + 'replacements.tsv'))
assert len(replacements) == 2
expected_old = [
    '28e06fb3201b629a38501827be2c6f05963e9034c5c68c1d716d05b29894bcc3',
    '4c98c6661fe2ba1d417f25d06c78c9630c13723090854125fdc0d26d6ce614e4',
]
expected_new = [
    'aeabb5452f12cddd326995a83b02b3ddd48acb8183a4e6f97215efa242dc8d48',
    'f151fb99580375ed290b084c51ff95fbc374798bb4a83b23ce8da792b23f95aa',
]
for index, replacement in enumerate(replacements):
    assert replacement['statement_id'] == SID
    assert replacement['old_text'] and text.count(replacement['old_text']) == 1
    assert sha256(replacement['old_text'].encode()).hexdigest() == expected_old[index]
    assert sha256(replacement['new_text'].encode()).hexdigest() == expected_new[index]
    for name in ('label', 'hypertarget', 'tag'):
        pattern = r'\\' + name + r'\{([^{}]+)\}'
        assert sorted(re.findall(pattern, replacement['old_text'])) == sorted(re.findall(pattern, replacement['new_text']))
receiver = (LANE / (P + 'receiving.tex')).read_text()
assert receiver.rstrip('\n') == '\n\n'.join(item['new_text'].rstrip('\n') for item in replacements)
assert receiver.count(r'\begin{theorem}') == receiver.count(r'\end{theorem}') == 1
assert receiver.count(r'\begin{proof}') == receiver.count(r'\end{proof}') == 1
defectfile = LANE / (P + 'defects.tsv')
dfields, defects = read(defectfile)
assert len(defects) == 5 and all(item['statement_id'] == SID for item in defects)
assert sorted(item['type'] for item in defects) == ['D09', 'D09', 'D13', 'D20', 'D20']
for item in defects:
    assert text.count(item['old_text']) == 1 and receiver.count(item['new_text']) == 1
eventfile = ROOT / 'CHECK_EVENTS.tsv'
efields, events = read(eventfile)
pfields, proposals = read(LANE / (P + 'CHECK_EVENTS.tsv'))
assert efields == pfields and len(proposals) == 3
assert sorted(item['type'] for item in proposals) == ['computation or formal certificate', 'targeted proof check', 'used and rechecked in this run']
known = {item['event_id'] for item in events}
now = datetime.now(timezone.utc)
for event in proposals:
    assert event['statement_id'] == SID and event['event_id'] not in known
    assert event['evidence_group'] == 'publish:c7:III:02LS'
    assert datetime.fromisoformat(event['date_utc'].replace('Z', '+00:00')) <= now
    event['outcome'] += ' Root admitted the completed comparison after the exact full reading recorded in ' + REVIEW + '. Receiver SHA256 ' + hashes['receiving.tex'] + '. Canonical application and final unit/build/page gates remain open.'
    events.append(event)
    known.add(event['event_id'])
row.update(status='done', packet_status='required_check_complete',
           check_event_id=';'.join(item['event_id'] for item in proposals),
           proof_comparison_evidence=str((LANE / (P + 'comparison.md')).relative_to(ROOT)),
           completion_evidence='; '.join((row['derivation_path'], str((LANE / (P + 'comparison.md')).relative_to(ROOT)), str((LANE / (P + 'receiving.tex')).relative_to(ROOT)), REVIEW)),
           source_ownership_status='verified_exact_individual_scope')
row['notes'] += ' Seventh-continuation root admitted the exact LS comparison. Canonical application, unit restructuring and final page review remain separate open gates.'
for item in defects:
    item['review_status'] = 'root comparison admitted; source application and final page review pending'
write(eventfile, efields, events)
write(progress, fields, rows)
write(defectfile, dfields, defects)
assert source.read_bytes() == raw
print('Admitted 02LS at', now.isoformat(), '; III required checks', str(sum(item['status'] == 'done' for item in rows)) + '/' + str(len(rows)) + '.')
print('Two exact guards; five bounded repairs; three narrowly typed events; canonical manuscript unchanged.')
