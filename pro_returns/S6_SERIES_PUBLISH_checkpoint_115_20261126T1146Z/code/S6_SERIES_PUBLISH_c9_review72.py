"""Scheduled hourly review72; record actual closures and the remaining gates."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
boundary = datetime.fromisoformat('2026-11-26T03:30:22+00:00')
now = datetime.now(timezone.utc)
assert now >= boundary, 'Review72 is not due.'


def table(name, delimiter='\t'):
    with (ROOT / name).open(newline='') as stream:
        return list(csv.DictReader(stream, delimiter=delimiter))


units = table('S6_SERIES_PUBLISH_unit_progress.tsv')
findings = table('S6_SERIES_PUBLISH_findings_III.tsv')
required = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
provenance = table('S6_SERIES_PUBLISH_provenance_checks.tsv')
builds = table('S6_SERIES_PUBLISH_build_progress.tsv')
assert len(required) == 128 and all(r['status'] == 'done' for r in required)
lp, = [r for r in units if r['paper'] == 'III' and r['unit_id'] == 'maps:src:D.2.48' and r['defect_type'] == 'D20']
assert lp['status'] == 'done'
t1, = [r for r in findings if r['id'] == 'T1']
assert t1['status'] == 'done'
reading = (ROOT / 'S6_SERIES_PUBLISH_reading_III.md').read_text()
assert '## Candidate02: complete attributed image reading' in reading
counts = {paper: Counter(r['status'] for r in units if r['paper'] == paper) for paper in ('III', 'IV')}
grouped = defaultdict(list)
for row in units:
    if row['paper'] in ('III', 'IV') and row['status'] != 'done':
        grouped[(row['paper'], row['unit_id'], row['status'])].append(row['defect_type'] or row['row_kind'])
iv_path = ROOT / 'S6_SERIES_PUBLISH_required_progress_IV.tsv'
iv = table(iv_path.name) if iv_path.exists() else [r for r in table('records/S6_SERIES_PUBLISH_required_check_candidates.csv', ',') if r['paper'] == 'IV']
lines = [f'\n\n## Review 72 — {now.isoformat()}\n',
    f'INCOMPLETE. Scheduled boundary: {boundary.isoformat()}.',
    'Qualifying movement since review71: T1 closed at its recorded complete two-kernel/alias scope; the reopened02LP D20 row closed after full original/proposed proof comparison and34 exact admissions; all696 candidate02 physical pages now have actual-image observations in four attributed174-page allocations. Those are completed gates at their exact source/PDF scopes. Packaging and additional exposed-use events themselves receive no movement credit.',
    'The subsequent source repairs retain exact old/new defect rows, complete forward/reverse substitutions, and precise exposed source-reading events. They reopen the current-source full-build gate. The old build remains the identified candidate02 image input and supplies no reading credit for changed final images. All128 required III checks remain complete; no additional independent mathematical proof credit is claimed.',
    'Final source reconciliation also rejected closure based solely on a paragraph boundary for nine concrete residual name assignments. Their nine containing D20 unit rows were explicitly reopened by c9_reopen_local_rebindings.py; exact bounded addenda and the final02L9 packet are being completed. The current statuses below retain those reopenings and any subsequent actual dispositions.',
    f"Paper III unit criteria: {counts['III']['done']} done, {sum(v for k,v in counts['III'].items() if k != 'done')} open. Paper IV unit criteria: {counts['IV']['done']} done, {sum(v for k,v in counts['IV'].items() if k != 'done')} open.",
    '\n### Every open unit row, grouped with its exact identity and criterion\n',
    '| Paper | Unit identifier | Status | Open criteria |', '|---|---|---|---|']
for (paper, unit, status), criteria in grouped.items():
    lines.append(f"| {paper} | {unit} | {status} | {', '.join(criteria)} |")
lines += ['\n### Supplied source findings still open\n', '| Finding | Status | Remaining gate |', '|---|---|---|']
for row in findings:
    if row['status'] != 'done':
        lines.append('| ' + ' | '.join(row[k].replace('|', '/') for k in ('id', 'status', 'remaining_gate')) + ' |')
lines += ['\nCompleted supplied finding IDs: ' + ', '.join(r['id'] for r in findings if r['status'] == 'done') + '.',
          '\n### Current build gates\n', '| Paper | Status | Actual scope and remaining gate |', '|---|---|---|']
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
lines += ['\nThe concrete remaining III gate is the current table state above: finish any still-open image-discovered source instances, admit the final ledger-count paragraph once, converge both repaired-source builds, actually read every changed full-page image, and settle the58 regrouped-unit D14 rows and all other final layout/reference/provenance gates. Final page-dependent records follow the verified PDF. Paper IV follows III; the joint I/II/V and five-paper reconciliation remains last.',
    'Each current-candidate page must be accounted for in its actual reading record. Full decoded-pixel equality at the same physical page can preserve only the original observation and attribution; all other current page images remain open until actually displayed and read. Render production and text/aux queries supply no reading credit.',
    'Consecutive hourly reviews without qualifying movement: 0.',
    'Next hourly review: 2026-11-26T04:30:22+00:00. Checkpoint104 is due at2026-11-26T03:30:22+00:00; the next scheduled checkpoint105 is2026-11-26T04:15:22+00:00.',
    'The two-consecutive-no-movement stop rule has not been reached.\n']
ledger = ROOT / 'PROGRESS_LEDGER.md'
before = ledger.read_text()
assert '\n## Review 72 ' not in before
ledger.write_text(before + '\n'.join(lines), newline='\n')
report = ROOT / 'S6_SERIES_PUBLISH_report.md'
report.write_text(report.read_text() + f'\n\n## Scheduled review72 — {now.isoformat()}\n\nINCOMPLETE. T1 and the reopened02LP D20 source row closed at their recorded scopes. All696 candidate02 pages have actual attributed image observations. Exact repairs followed; the current-source build and changed-image gates remain as explicitly recorded. III has{counts["III"]["done"]} done unit criteria and{sum(v for k,v in counts["III"].items() if k != "done")} open; all128 required checks remain complete. IV and the joint phase remain. The ledger lists every remaining unit/criterion, supplied finding, IV required check, build and provenance gate. Consecutive no-movement reviews:0.\n', newline='\n')
print('Review72 recorded:', now.isoformat())
print('Actual III/IV unit statuses:', counts)
print('All128 III required checks retained. T1 and02LP closures and actual696-page reading support qualifying movement; no packaging or independent-proof credit.')
