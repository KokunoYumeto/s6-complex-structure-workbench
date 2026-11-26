"""Record scheduled review78 from completed observations and live canonical rows."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import argparse
import csv
import json
import hashlib

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'S6_SERIES_PUBLISH_unit_progress.tsv').is_file())
csv.field_size_limit(100000000)
parser = argparse.ArgumentParser()
parser.add_argument('--work-note', required=True)
args = parser.parse_args()
now = datetime.now(timezone.utc)
boundary = datetime.fromisoformat('2026-11-26T09:30:22+00:00')
assert now >= boundary

def table(name, delimiter='\t'):
    with (ROOT / name).open(newline='') as stream:
        return list(csv.DictReader(stream, delimiter=delimiter))

ledger = ROOT / 'PROGRESS_LEDGER.md'
before = ledger.read_text()
assert '\n## Review 78 ' not in before
closure = (ROOT / 'code/S6_SERIES_PUBLISH_c9_candidate07_source_close.out').read_text()
closure_utc = datetime.fromisoformat('2026-11-26T09:08:34.195099+00:00')
interval_start = datetime.fromisoformat('2026-11-26T08:30:22+00:00')
assert interval_start <= closure_utc <= boundary
assert 'UTC ' + closure_utc.isoformat() in closure
assert 'Four actual D20 owners and P15 source criterion: open -> done.' in closure
source_hash = hashlib.sha256((ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
units = table('S6_SERIES_PUBLISH_unit_progress.tsv')
findings = table('S6_SERIES_PUBLISH_findings_III.tsv')
builds = table('S6_SERIES_PUBLISH_build_progress.tsv')
claims = table('S6_SERIES_PUBLISH_provenance_checks.tsv')
required = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
assert len(required) == 128 and all(x['status'] == 'done' for x in required)
closed_owners = {'maps:src:D.2.24', 'maps:src:D.2.40', 'maps:src:D.2.41', 'wb:sphere-metric-scaling-trichotomy'}
for owner in closed_owners:
    row, = [x for x in units if (x['paper'], x['unit_id'], x['row_kind'], x['defect_type']) == ('III', owner, 'defect', 'D20')]
    assert 'S6_SERIES_PUBLISH_c9_candidate07_source_packet_review.md' in row['evidence']
p15, = [x for x in findings if x['id'] == 'P15']
assert 'All four whole-proof source comparisons completed' in p15['source_resolution']
count = json.loads((ROOT / 'records/S6_SERIES_PUBLISH_III_current_check_counts.json').read_text())
assert len(count['selected_event_ids']) == count['selected_event_associations']
assert len(count['selected_evidence_groups']) == count['declared_evidence_groups']
counts = {p: Counter(x['status'] for x in units if x['paper'] == p) for p in ('III', 'IV')}
grouped = defaultdict(list)
for row in units:
    if row['status'] != 'done':
        grouped[(row['paper'], row['unit_id'], row['status'])].append(row['defect_type'] or row['row_kind'])
iv_path = ROOT / 'S6_SERIES_PUBLISH_required_progress_IV.tsv'
iv = table(iv_path.name) if iv_path.exists() else [x for x in table('records/S6_SERIES_PUBLISH_required_check_candidates.csv', ',') if x['paper'] == 'IV']
assert len(iv) == 66
open_criteria = Counter(x['defect_type'] or x['row_kind'] for x in units if x['paper'] == 'III' and x['status'] != 'done')
iv_required_status = Counter(x['status'] if iv_path.exists() else 'unbegun' for x in iv)
lines = [f'\n\n## Review 78 — {now.isoformat()}\n',
    f'INCOMPLETE. Scheduled boundary: {boundary.isoformat()}.',
    f'Exact review interval: {interval_start.isoformat()} through {boundary.isoformat()}.',
    'Qualifying movement: four actual D20 unit criteria and the P15 source finding reached done at 2026-11-26T09:08:34.195099+00:00 after the complete coordinated source comparisons. The owners are maps:src:D.2.24, maps:src:D.2.40, maps:src:D.2.41 and wb:sphere-metric-scaling-trichotomy. Exact transition evidence is code/S6_SERIES_PUBLISH_c9_candidate07_source_close.py and code/S6_SERIES_PUBLISH_c9_candidate07_source_close.out; the canonical rows retain the completed source-packet review. These observed closures reset the consecutive no-movement count to zero.',
    'Count refresh, reading-history reconciliation, reopenings and diagnostic builds earn no qualifying movement credit. The latest fully reviewed diagnostic pair is current09/legacy08, on source 75000e4890bf8ff639d74dbfcfff77f06d1a48579c02667df04a4b1b7c29a254: both converged in two successful passes, 703 pages each, with no overflow above 2 pt. The separate formal-owner comparison found the 02LI destination on page 382 against aux/tag page 383 in both kernels. The exact layout reservation and successor current10/legacy09 verification remain distinct from build admission.',
    'Complete fresh compiler evidence: agents/continuation9_defect_records/S6_SERIES_PUBLISH_c9_current09_legacy08_build_logs_review.md. This review grants no new image or mathematical-check credit. Current statuses and the live source identity below are captured when this helper runs.',
    f'Live source SHA-256: {source_hash}.',
    args.work_note.strip(),
    f"Current count input: {count['selected_event_associations']} selected associations in {count['declared_evidence_groups']} evidence groups; six event types: {count['counts']}. This review does not refresh those derived counts or create a mathematical event.",
    f"Actual unit state: Paper III {counts['III']['done']} done and {sum(v for k,v in counts['III'].items() if k != 'done')} open; Paper IV {counts['IV']['done']} done and {sum(v for k,v in counts['IV'].items() if k != 'done')} open. All 128 III required checks remain done. Live IV required statuses: {dict(iv_required_status)} across 66 entries.",
    f'Live open III criteria: {dict(open_criteria)}. P15 live status: {p15["status"]}.',
    '\n### Every remaining unit row by exact identity and criterion\n',
    '| Paper | Unit identifier | Status | Open criteria |', '|---|---|---|---|']
for (paper, key, status), criteria in grouped.items():
    lines.append(f"| {paper} | {key} | {status} | {', '.join(criteria)} |")
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
    check_status = row['status'] if iv_path.exists() else 'unbegun'
    if check_status != 'done':
        lines.append(f"| {row['tag']} | {check_status} |")
lines += ['\n### Paper III provenance and visual gates\n', '| Claim | Source status | Remaining gate |', '|---|---|---|']
for row in claims:
    if row['paper'] == 'III' and row['remaining_gate']:
        lines.append('| ' + ' | '.join(row[k].replace('|', '/') for k in ('claim_id', 'resolution_status', 'remaining_gate')) + ' |')
lines += [
    '\nNext: complete the exact 02LI anchor reservation and successor current/legacy verification, then actual changed-page reading; admit only supported non-joint III criteria and final records. Paper IV then precedes the joint five-paper phase.',
    'P4, the series-table D18 row and four other-paper provenance claims remain joint. No top-level final Paper III PDF or final extractor output has been admitted. Packaging, proposals and routine guards earn no movement credit.',
    'Consecutive hourly reviews without qualifying movement: 0. The two-review stop rule has not been reached.',
    'Next hourly review 79: 2026-11-26T10:30:22+00:00. Checkpoint112 is due at this boundary, 2026-11-26T09:30:22+00:00; next checkpoint113: 2026-11-26T10:15:22+00:00.\n']
report = ROOT / 'S6_SERIES_PUBLISH_report.md'
report_before = report.read_text()
summary = (f'\n\n## Scheduled review78 — {now.isoformat()}\n\nINCOMPLETE. '
    'Qualifying movement is the four actual D20 closures and P15 source closure at 09:08:34.195099 UTC, evidenced by the source-close program/output and canonical rows. '
    'Current09/legacy08 remain diagnostic because the separate 02LI formal-owner page comparison has one mismatch; current build status is recorded from the live table. '
    'Count refresh, history reconciliation, reopenings and diagnostic runs receive no movement credit. '
    f"Paper III has {counts['III']['done']} done and {sum(v for k,v in counts['III'].items() if k != 'done')} open unit criteria. "
    'All 128 required checks remain done. ' + args.work_note.strip() +
    ' IV and joint review remain. Complete open rows and gates appear in ledger review78. Consecutive no-movement reviews: 0.\n')
assert ledger.read_text() == before and report.read_text() == report_before
ledger.write_text(before + '\n'.join(lines), newline='\n')
report.write_text(report_before + summary, newline='\n')
print('Review78 recorded', now.isoformat())
print('Qualifying movement: four actual D20 open->done transitions and P15 source closure at', closure_utc.isoformat())
print('Actual units', counts)
print('Counts unchanged:', count['selected_event_associations'], count['declared_evidence_groups'])
print('All current unit/finding/build/provenance gates recorded; consecutive no-movement reviews: 0.')
