"""Scheduled review73: actual source closures and every remaining gate."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
boundary = datetime.fromisoformat('2026-11-26T04:30:22+00:00')
now = datetime.now(timezone.utc)
assert now >= boundary, 'Review73 is not due.'

def table(name, delimiter='\t'):
    with (ROOT / name).open(newline='') as f:
        return list(csv.DictReader(f, delimiter=delimiter))

units = table('S6_SERIES_PUBLISH_unit_progress.tsv')
findings = table('S6_SERIES_PUBLISH_findings_III.tsv')
required = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
provenance = table('S6_SERIES_PUBLISH_provenance_checks.tsv')
builds = table('S6_SERIES_PUBLISH_build_progress.tsv')
assert len(required) == 128 and all(r['status'] == 'done' for r in required)
reviewed_candidates = [
    'maps:src:D.2.18', 'maps:src:D.2.32', 'maps:src:D.2.33',
    'maps:src:D.2.34', 'night:P3F.31', 'night:P3F.32',
    'maps:src:D.2.9', 'maps:src:D.2.10', 'maps:src:D.2.13',
    'maps:src:D.2.37', 'maps:src:D.2.49', 'night:P3F.26',
    'maps:src:D.2.35', 'maps:src:D.2.39', 'maps:src:D.2.50',
    'maps:src:D.2.51', 'maps:src:D.2.53', 'night:P3F.34',
    'maps:src:D.1.1', 'maps:src:D.2.44', 'maps:src:D.2.26',
]
closed_since_review72 = []
for subject in reviewed_candidates:
    row, = [r for r in units if r['paper'] == 'III' and r['unit_id'] == subject and r['defect_type'] == 'D20']
    if row['status'] == 'done':
        closed_since_review72.append(subject)
assert len(closed_since_review72) >= 17
counts = {p: Counter(r['status'] for r in units if r['paper'] == p) for p in ('III', 'IV')}
grouped = defaultdict(list)
for row in units:
    if row['status'] != 'done':
        grouped[(row['paper'], row['unit_id'], row['status'])].append(row['defect_type'] or row['row_kind'])
iv_path = ROOT / 'S6_SERIES_PUBLISH_required_progress_IV.tsv'
iv = table(iv_path.name) if iv_path.exists() else [r for r in table('records/S6_SERIES_PUBLISH_required_check_candidates.csv', ',') if r['paper'] == 'IV']
lines = [f'\n\n## Review 73 — {now.isoformat()}\n',
    f'INCOMPLETE. Scheduled boundary: {boundary.isoformat()}.',
    f'Qualifying movement since review72: {len(closed_since_review72)} explicitly reopened or subsequently confirmed D20 source units are closed through exact admitted repairs and full affected-scope comparisons. Any subsequently reopened retained-role case is excluded from that closed list and appears in the current open rows below. The record does not count preparation, packaging, extra exposed-use events or a repeated description of a gate as movement.',
    'The source reconciliation withdrew paragraph-only exceptions. Each concrete named-object repair follows its actual formulas, coefficient maps and inverse constructions, including downstream imports. The additional radial-period comparison preserves the native T-indexed entries of the pointwise matrices and binds the limiting value directly. No additional independent mathematical proof credit is claimed.',
    'The current admitted source-unit closures in this interval: ' + ', '.join(closed_since_review72) + '.',
    f"Paper III unit criteria: {counts['III']['done']} done, {sum(v for k,v in counts['III'].items() if k != 'done')} open. Paper IV: {counts['IV']['done']} done, {sum(v for k,v in counts['IV'].items() if k != 'done')} open. All128 required III checks remain done.",
    '\n### Every open unit row, grouped by exact identity and criterion\n',
    '| Paper | Unit identifier | Status | Open criteria |', '|---|---|---|---|']
for (paper, unit, status), criteria in grouped.items():
    lines.append(f"| {paper} | {unit} | {status} | {', '.join(criteria)} |")
lines += ['\n### Supplied source findings\n', '| Finding | Status | Remaining gate |', '|---|---|---|']
for row in findings:
    if row['status'] != 'done':
        lines.append('| ' + ' | '.join(row[k].replace('|', '/') for k in ('id', 'status', 'remaining_gate')) + ' |')
lines.append('\nCompleted supplied finding IDs: ' + ', '.join(r['id'] for r in findings if r['status'] == 'done') + '.')
lines += ['\n### Current build gates\n', '| Paper | Status | Actual scope and remaining gate |', '|---|---|---|']
for row in builds:
    if row['paper'] in ('III', 'IV'):
        lines.append('| ' + ' | '.join(row[k].replace('|', '/') for k in ('paper', 'status', 'detail')) + ' |')
lines += ['\n### Required checks remaining in Paper IV\n', '| Tag | Status |', '|---|---|']
for row in iv:
    if row.get('status', 'open') != 'done':
        lines.append(f"| {row['tag']} | {row.get('status', 'open')} |")
lines += ['\n### Paper III provenance and final visual gates\n', '| Claim | Source status | Remaining gate |', '|---|---|---|']
for row in provenance:
    if row['paper'] == 'III' and row['remaining_gate']:
        lines.append('| ' + ' | '.join(row[k].replace('|', '/') for k in ('claim_id', 'resolution_status', 'remaining_gate')) + ' |')
lines += [
    '\nThe main gate is the exact current table state above: finish any still-open source disposition, derive the final ledger paragraph once, converge both same-source builds, inspect the complete diagnostics and actual anchor results, then read every changed final page. The58 authored D14 groupings have actual candidate02 image evidence and substantive source dispositions; final changed-image verification remains. Page-dependent records follow the final verified PDF. IV follows III, and the joint I/II/V and five-paper reconciliation remains last.',
    'All696 old candidate02 page observations retain their original attribution and identified input. They confer no reading credit on a changed current page. Exact full decoded-pixel equality at the same physical page preserves only the existing observation; every other new page must be actually displayed and read.',
    'Consecutive hourly reviews without qualifying movement: 0.',
    'Next hourly review: 2026-11-26T05:30:22+00:00. Checkpoint105 was saved at its recorded scheduled snapshot; checkpoint106 is due2026-11-26T05:00:22+00:00.',
    'The two-consecutive-no-movement stop rule has not been reached.\n',
]
ledger = ROOT / 'PROGRESS_LEDGER.md'
before = ledger.read_text()
assert '\n## Review 73 ' not in before
ledger.write_text(before + '\n'.join(lines), newline='\n')
report = ROOT / 'S6_SERIES_PUBLISH_report.md'
report.write_text(report.read_text() + f'\n\n## Scheduled review73 — {now.isoformat()}\n\nINCOMPLETE. {len(closed_since_review72)} actual D20 source units are closed through admitted exact comparisons during this review interval, excluding the explicitly reopened current cases; all128 required III checks remain complete. III has{counts["III"]["done"]} done unit criteria and{sum(v for k,v in counts["III"].items() if k != "done")} open. The ledger records the actual supplied-finding/build states, every remaining unit/criterion, IV required checks and provenance gates. Current-source builds, changed-image reading and final derivation remain governed by those exact states; IV and joint I/II/V follow. Consecutive no-movement reviews:0.\n', newline='\n')
print('Review73 recorded:', now.isoformat())
print('Actual III/IV unit statuses:', counts)
print(len(closed_since_review72), 'exact source-unit closures support qualifying movement. No packaging or independent-proof credit.')
