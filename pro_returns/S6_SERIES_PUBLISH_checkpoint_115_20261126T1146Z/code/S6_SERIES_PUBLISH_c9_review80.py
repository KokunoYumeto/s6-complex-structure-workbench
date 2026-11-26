"""Record review80 only while the frozen current10 source gate is still open."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import argparse
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
p = argparse.ArgumentParser()
p.add_argument('--work-note', required=True)
a = p.parse_args()
now = datetime.now(timezone.utc)
start = datetime.fromisoformat('2026-11-26T10:30:22+00:00')
boundary = datetime.fromisoformat('2026-11-26T11:30:22+00:00')
assert now >= boundary, 'The scheduled hourly review has not arrived.'

def table(name, delimiter='\t'):
    with (ROOT / name).open(newline='') as f:
        return list(csv.DictReader(f, delimiter=delimiter))

def outside_interval(value):
    return not value or not (start <= datetime.fromisoformat(value) <= boundary)

ledger = ROOT / 'PROGRESS_LEDGER.md'
before = ledger.read_text()
assert '\n## Review 80 ' not in before
assert '\n## Review 79 ' in before
assert 'Consecutive hourly reviews without qualifying movement:0.' in before.split('\n## Review 79 ', 1)[1]
units = table('S6_SERIES_PUBLISH_unit_progress.tsv')
findings = table('S6_SERIES_PUBLISH_findings_III.tsv')
builds = table('S6_SERIES_PUBLISH_build_progress.tsv')
claims = table('S6_SERIES_PUBLISH_provenance_checks.tsv')
required = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
assert len(required) == 128 and all(r['status'] == 'done' for r in required)
p15, = [r for r in findings if r['id'] == 'P15']
assert p15['status'] == 'open'
build, = [r for r in builds if r['paper'] == 'III']
assert build['status'] == 'done' and build['date_utc'] == '2026-11-26T09:35:34.563481+00:00'
assert build['pdf_sha256'] == 'f284a0556c64684531f1d05b5370be02b111f8c9abee8c5ec7463bcf12ed2dc4'
source_sha = hashlib.sha256((ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert source_sha == '5a95d62059fcaf7859df33f5793d9cd97462024d50a1f7ee59f9fae0b2704187'
assert all(outside_interval(r['date_utc']) for r in units if r['paper'] == 'III' and r['status'] == 'done')
assert all(outside_interval(r['date_utc']) for r in findings if r['status'] == 'done')
reading = (ROOT / 'S6_SERIES_PUBLISH_reading_III.md').read_bytes()
assert hashlib.sha256(reading).hexdigest() == 'dc7c0f29a4cfcb1a23a46936c0d9f7f5819aba31e68c35eb8f74add179f185c4'
counts = {paper: Counter(r['status'] for r in units if r['paper'] == paper) for paper in ('III', 'IV')}
assert counts['III'] == Counter(done=3135, open=113)
grouped = defaultdict(list)
for row in units:
    if row['status'] != 'done':
        grouped[(row['paper'], row['unit_id'], row['status'])].append(row['defect_type'] or row['row_kind'])
criteria = Counter(r['defect_type'] or r['row_kind'] for r in units if r['paper'] == 'III' and r['status'] != 'done')
iv_path = ROOT / 'S6_SERIES_PUBLISH_required_progress_IV.tsv'
iv = table(iv_path.name) if iv_path.exists() else [r for r in table('records/S6_SERIES_PUBLISH_required_check_candidates.csv', ',') if r['paper'] == 'IV']
assert len(iv) == 66
iv_status = Counter(r['status'] if iv_path.exists() else 'unbegun' for r in iv)
count = json.loads((ROOT / 'records/S6_SERIES_PUBLISH_III_current_check_counts.json').read_text())
assert count['selected_event_associations'] == len(count['selected_event_ids']) == 1243
assert count['declared_evidence_groups'] == len(count['selected_evidence_groups']) == 956

lines = [f'\n\n## Review 80 — {now.isoformat()}\n',
    f'INCOMPLETE. Scheduled boundary: {boundary.isoformat()}. Exact interval: {start.isoformat()} through {boundary.isoformat()}.',
    'No qualifying movement occurred in this interval. The canonical source, accepted current10/legacy09 build and attributed current10 page coverage remain those accepted before the interval. P15 and its ten D20 units remain open. The completed source comparisons are staged and have not yet changed a current-source criterion, required check, build or final-image gate. They and checkpoint packaging receive no movement credit.',
    'The 02SA typography finding reopened one D23 row at2026-11-26T10:44:35.904701+00:00. Root also reopened D23 / series:III:main-theorems on two actual punctuation findings at2026-11-26T11:24:55.960385+00:00. Both reopenings are preserved; they are not qualifying movement. Existing completed required checks remain completed.',
    f'Live source SHA-256: {source_sha}.', a.work_note.strip(),
    f"Counts retained: {count['selected_event_associations']} associations in {count['declared_evidence_groups']} evidence groups; types {count['counts']}. No mathematical event or derived count is created by this review.",
    f"Actual unit state: III {counts['III']['done']} done and {sum(v for k, v in counts['III'].items() if k != 'done')} open; IV {counts['IV']['done']} done and {sum(v for k, v in counts['IV'].items() if k != 'done')} open. All128 III required checks remain done; IV has66 required rows, statuses {dict(iv_status)}.",
    f'Open III criteria: {dict(criteria)}. P15: {p15["status"]}.',
    '\n### Every remaining unit row by exact identity and criterion\n',
    '| Paper | Unit identifier | Status | Open criteria |', '|---|---|---|---|']
for (paper, key, status), types in grouped.items():
    lines.append(f"| {paper} | {key} | {status} | {', '.join(types)} |")
lines += ['\n### Supplied source findings\n', '| Finding | Status | Remaining gate |', '|---|---|---|']
for row in findings:
    if row['status'] != 'done':
        lines.append('| ' + ' | '.join(row[k].replace('|', '/') for k in ('id', 'status', 'remaining_gate')) + ' |')
lines += ['\n### Current build gates\n', '| Paper | Status | Scope and remaining gate |', '|---|---|---|']
for row in builds:
    if row['paper'] in ('III', 'IV'):
        lines.append('| ' + ' | '.join(row[k].replace('|', '/') for k in ('paper', 'status', 'detail')) + ' |')
lines += ['\n### Required checks remaining in Paper IV\n', '| Tag | Status |', '|---|---|']
for row in iv:
    status = row['status'] if iv_path.exists() else 'unbegun'
    if status != 'done':
        lines.append(f"| {row['tag']} | {status} |")
lines += ['\n### Paper III provenance and visual gates\n', '| Claim | Source status | Remaining gate |', '|---|---|---|']
for row in claims:
    if row['paper'] == 'III' and row['remaining_gate']:
        lines.append('| ' + ' | '.join(row[k].replace('|', '/') for k in ('claim_id', 'resolution_status', 'remaining_gate')) + ' |')
lines += ['\nNext: finish the full LE original/proposed/caller comparison and the integrated source/status/count review, then admit the supported source batch. Build current11/legacy10 and read every changed page. Complete supported non-joint III gates, then IV, then the joint five-paper work.',
    'P4, the series-table D18 row and four other-paper provenance claims remain joint. No top-level final III PDF or final extractor output has been admitted.',
    'Consecutive hourly reviews without qualifying movement:1. The two-review stop rule has not been reached.',
    'Next hourly review81:2026-11-26T12:30:22+00:00. Checkpoint114 was saved at11:01:00.935469 UTC; next checkpoint115:2026-11-26T11:45:22+00:00.\n']
report = ROOT / 'S6_SERIES_PUBLISH_report.md'
report_before = report.read_text()
summary = (f'\n\n## Scheduled review80 — {now.isoformat()}\n\nINCOMPLETE. '
    'No qualifying movement occurred in10:30:22–11:30:22 UTC. The current10 source/build/image state is unchanged; staged source comparisons and checkpoint packaging receive no movement credit. '
    f"III has {counts['III']['done']} done and {sum(v for k, v in counts['III'].items() if k != 'done')} open unit criteria; all128 required checks remain done. "
    + a.work_note.strip() + ' IV and the joint review remain. All exact open units and gates are recorded in review80. Consecutive no-movement reviews:1; continue the authorized work.\n')
assert ledger.read_text() == before and report.read_text() == report_before
ledger.write_text(before + '\n'.join(lines), newline='\n')
report.write_text(report_before + summary, newline='\n')
print('Review80 recorded', now.isoformat())
print('No qualifying movement in10:30:22–11:30:22UTC; consecutive no-movement reviews:1.')
print('Actual units', counts, 'Open III criteria', criteria)
print('Counts unchanged', count['selected_event_associations'], count['declared_evidence_groups'])
print('All open unit/finding/build/provenance gates recorded. Continue the authorized work.')
