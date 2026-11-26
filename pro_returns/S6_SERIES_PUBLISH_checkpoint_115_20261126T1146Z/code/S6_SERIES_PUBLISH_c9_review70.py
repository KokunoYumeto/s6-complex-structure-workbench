"""Scheduled review70: assess actual status movement since continuation start."""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone, timedelta
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
start = datetime.fromisoformat('2026-11-26T00:30:22+00:00')
boundary = start + timedelta(hours=1)
now = datetime.now(timezone.utc)
assert now >= boundary, 'Review is not due yet.'

def table(name):
    with (ROOT / name).open(newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))

units = table('S6_SERIES_PUBLISH_unit_progress.tsv')
findings = table('S6_SERIES_PUBLISH_findings_III.tsv')
required = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
provenance = table('S6_SERIES_PUBLISH_provenance_checks.tsv')
build = table('S6_SERIES_PUBLISH_build_progress.tsv')
closed_findings = [r['id'] for r in findings if r['status'] == 'done']
assert len(closed_findings) == 15
assert len(required) == 128 and all(r['status'] == 'done' for r in required)
counts = {paper: Counter(r['status'] for r in units if r['paper'] == paper) for paper in ['III', 'IV']}
grouped = defaultdict(list)
for row in units:
    if row['paper'] in ('III', 'IV') and row['status'] != 'done':
        grouped[(row['paper'], row['unit_id'], row['status'])].append(row['defect_type'] or row['row_kind'])

lines = [f'\n\n## Review 70 — {now.isoformat()}\n',
    f'INCOMPLETE. Scheduled boundary: {boundary.isoformat()}.',
    'Fifteen supplied Paper III reading-finding rows changed from open to done in this continuation: ' + ', '.join(closed_findings) + '.',
    'Those actual closures constitute qualifying movement. No new required identity is credited: all128 Paper III required checks were complete at continuation start and remain complete. The58-input matrix replay, source admissions, exposed reread events and checkpoint packaging receive no separate movement credit.',
    f"Paper III unit criteria: {counts['III']['done']} done, {sum(v for k,v in counts['III'].items() if k != 'done')} open. Paper IV: {counts['IV']['done']} done, {sum(v for k,v in counts['IV'].items() if k != 'done')} open; its66 required checks remain unbegun in their attached candidate records.",
    'The six observed D20 rows and methodology D15 row remain open until the full P15 source disposition and final count application. Several of their exact source corrections are already admitted, but this review does not infer whole-row closure from those partial admissions.',
    '\n### Every open unit row, grouped without losing its identity\n',
    '| Paper | Unit identifier | Status | Open criteria |', '|---|---|---|---|']
for (paper, unit, status), criteria in grouped.items():
    lines.append(f"| {paper} | {unit} | {status} | {', '.join(criteria)} |")
lines += ['\n### Other open rows and their actual gates\n',
    '| Finding | Status | Remaining gate |', '|---|---|---|']
for row in findings:
    if row['status'] != 'done':
        lines.append('| ' + ' | '.join(str(row[k]).replace('|', '/') for k in ['id','status','remaining_gate']) + ' |')
lines += ['\nPaper III provenance statuses are retained in the61 individually identified claims of `S6_SERIES_PUBLISH_provenance_checks.tsv`. Their source/deposit assessments and separate PDF/series gates are not collapsed into inferred final completion. Current status totals: ' + repr(dict(Counter(r['resolution_status'] for r in provenance if r['paper'] == 'III'))) + '.',
    'The Paper III clean-build row remains open. The current-source PDF has not yet been built, so every page of that future candidate remains unread. The80 actual pages read in the earlier pass08 receive no carryover credit for changed page images. Current and legacy full builds, complete logs and actual PDF alias checks remain required.',
    'Current main gate: finish the residual P15 source instances and the source count/provenance application, then establish both complete manuscript builds, finish the58 regrouped-unit D14 checks and other layout/reference criteria, and read every page of the converged Paper III PDF. Paper IV follows III; the final joint phase retains the authorized work on I, II and V. No reduction of the main gate is claimed beyond the fifteen actual supplied-finding closures.',
    'Consecutive reviews without qualifying movement: 0.',
    'Next hourly review: 2026-11-26T02:30:22+00:00. Next checkpoint102: 2026-11-26T02:00:22+00:00.',
    'The two-consecutive-no-movement stop rule has not been reached.\n']
ledger = ROOT / 'PROGRESS_LEDGER.md'
text = ledger.read_text()
assert '\n## Review 70 ' not in text
ledger.write_text(text + '\n'.join(lines), newline='\n')
report = ROOT / 'S6_SERIES_PUBLISH_report.md'
report.write_text(report.read_text() + f'\n\n## Scheduled review70 — {now.isoformat()}\n\nINCOMPLETE. Fifteen supplied Paper III reading findings closed since continuation start; all128 required checks remain complete. The live unit table records {counts["III"]["done"]} done and {sum(v for k,v in counts["III"].items() if k != "done")} open III criteria. Residual P15 source work, final count/provenance application, both full builds and every-page reading remain. The ledger groups every open III/IV unit row by its exact identifier and records all other current gates. This is qualifying status movement; consecutive no-movement reviews remain0. Packaging and added events are not counted as movement.\n', newline='\n')
print('Review70 recorded at', now.isoformat())
print('Qualifying closures:', ', '.join(closed_findings))
print('Unit statuses:', counts)
print('No build/page or independent proof credit added; no-movement counter0.')
