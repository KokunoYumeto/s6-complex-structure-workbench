"""Scheduled review71: assess actual status movement since continuation start."""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone, timedelta
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
start = datetime.fromisoformat('2026-11-26T00:30:22+00:00')
boundary = start + timedelta(hours=2)
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
assert len(closed_findings) == 14
assert len(required) == 128 and all(r['status'] == 'done' for r in required)
counts = {paper: Counter(r['status'] for r in units if r['paper'] == paper) for paper in ['III', 'IV']}
grouped = defaultdict(list)
for row in units:
    if row['paper'] in ('III', 'IV') and row['status'] != 'done':
        grouped[(row['paper'], row['unit_id'], row['status'])].append(row['defect_type'] or row['row_kind'])

lines = [f'\n\n## Review 71 — {now.isoformat()}\n',
    f'INCOMPLETE. Scheduled boundary: {boundary.isoformat()}.',
    'Qualifying movement since review70: the five previously open D20 rows other than the subsequently reopened02LP row, the organization D24 row and the methodology D15 row are closed at their recorded source scope. The full-build row is also done for the frozen source: both kernels converged with complete diagnostics and the current PDF is the actual reading input.',
    'The image reading found further exact P11/P15 instances and reopened those supplied finding rows;02LP’s D20 row is open again. Those reopenings are retained rather than hidden by the earlier source disposition. All128 required checks remain complete; no independent proof credit is added.',
    f"Paper III unit criteria: {counts['III']['done']} done, {sum(v for k,v in counts['III'].items() if k != 'done')} open. Paper IV: {counts['IV']['done']} done, {sum(v for k,v in counts['IV'].items() if k != 'done')} open; its66 required checks remain unbegun.",
    'The concrete main gate has advanced to full candidate image reading and the repairs it exposes. Current candidate02 and legacy candidate01 each contain696 pages, no unresolved reference/citation or font/anchor diagnostic, and no logged overflow above2pt. Actual images have nevertheless exposed two wide displays, so diagnostic success is not being substituted for visual reading.',
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
    'Actual reading completed and authored at this review: global pages1–174, root523–640, named-reader notes through at least330, and third-quarter notes through at least404. Further images already observed by the readers are not credited here until their written notes are confirmed. The old80-page pass08 record supplies no changed-image credit. Render generation alone supplies no reading credit.',
    'Current main gate: finish all696 candidate page images, settle every observed source/layout/reference issue with exact old/new defect rows and full affected-proof comparisons, update the selected event counts once after those admissions, rebuild both kernels, and read each changed final page. Then finish the58 D14 units and other actual layout/reference gates, the final derived records and program-visibility provenance. Paper IV follows III; I/II/V remain untouched until the joint phase.',
    'Consecutive reviews without qualifying movement: 0.',
    'Next hourly review: 2026-11-26T03:30:22+00:00. Next checkpoint103: 2026-11-26T02:45:22+00:00.',
    'The two-consecutive-no-movement stop rule has not been reached.\n']
ledger = ROOT / 'PROGRESS_LEDGER.md'
text = ledger.read_text()
assert '\n## Review 71 ' not in text
ledger.write_text(text + '\n'.join(lines), newline='\n')
report = ROOT / 'S6_SERIES_PUBLISH_report.md'
report.write_text(report.read_text() + f'\n\n## Scheduled review71 — {now.isoformat()}\n\nINCOMPLETE. Five retained D20 closures, one D24 closure, one methodology D15 closure, and both full manuscript builds provide qualifying movement since review70. Actual images reopened P11/P15 and02LP D20; those gates remain open. The live unit table records {counts["III"]["done"]} done and {sum(v for k,v in counts["III"].items() if k != "done")} open III criteria. Both kernels converge to696 pages. Every-page reading, observed source repairs, subsequent changed-page reading, final derived records and IV/joint work remain. The ledger preserves all open unit identities. Consecutive no-movement reviews remain0; packaging and exposed events receive no movement credit.\n', newline='\n')
print('Review71 recorded at', now.isoformat())
print('Source finding statuses retained; explicit new closures and reopens described in ledger.')
print('Unit statuses:', counts)
print('No build/page or independent proof credit added; no-movement counter0.')
