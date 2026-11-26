"""Record scheduled review77 from completed observations and live canonical rows."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import argparse
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
parser = argparse.ArgumentParser()
parser.add_argument('--work-note', required=True)
args = parser.parse_args()
now = datetime.now(timezone.utc)
boundary = datetime.fromisoformat('2026-11-26T08:30:22+00:00')
assert now >= boundary

def table(name, delimiter='\t'):
    with (ROOT / name).open(newline='') as stream:
        return list(csv.DictReader(stream, delimiter=delimiter))

ledger = ROOT / 'PROGRESS_LEDGER.md'
before = ledger.read_text()
assert '\n## Review 77 ' not in before
apply = (ROOT / 'code/S6_SERIES_PUBLISH_c9_admit_candidate07_builds_apply.out').read_text()
assert 'Admitted the Paper III build row' in apply
assert 'de3ac6c29a2794176a70a4abf0c40c4702ad27a08d2c13ea223f6b509ca98bca' in apply
root_reading = (ROOT / 'agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate07_final_reading.md').read_text()
assert [int(x) for x in re.findall(r'^\| (\d+) \|', root_reading, re.M)] == list(range(631, 702))
assert 'Root range completion' in root_reading
global_reading = (ROOT / 'agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_candidate07_first_range_images.md').read_text()
assert 'All **71 assigned complete page images**' in global_reading
named_reading = (ROOT / 'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_candidate07_pages489_559_review.md').read_text()
assert 'every complete physical page from 489 through 559 inclusive: 71 pages' in named_reading
backend_reading = (ROOT / 'agents/continuation9_reading_thirdquarter/S6_SERIES_PUBLISH_c9_candidate07_pages560_630_review.md').read_text()
assert 'I actually viewed and read all 71 complete 150-dpi page images' in backend_reading
units = table('S6_SERIES_PUBLISH_unit_progress.tsv')
findings = table('S6_SERIES_PUBLISH_findings_III.tsv')
builds = table('S6_SERIES_PUBLISH_build_progress.tsv')
claims = table('S6_SERIES_PUBLISH_provenance_checks.tsv')
required = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
assert len(required) == 128 and all(x['status'] == 'done' for x in required)
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
lines = [f'\n\n## Review 77 — {now.isoformat()}\n',
    f'INCOMPLETE. Scheduled boundary: {boundary.isoformat()}.',
    'Qualifying movement: the actually open Paper III build row reached done at07:45:58.365073 UTC after root read the complete current07/legacy06 diagnostics and admission inspection. Both701-page builds have zero unresolved/rerun/font/destination errors, zero overflow above2pt and zero page exceptions among249 formal owners. Their two remaining overfull widths are0.83005pt and1.34203pt. The exact accepted output remains in code/S6_SERIES_PUBLISH_c9_admit_candidate07_builds_apply.out. A later source change reopens the build gate without erasing that actual completed transition.',
    'Qualifying page movement: all284 changed/new current07 pages were actually read by the four assigned readers,71 each. Root fully read all three complete other-reader reports and every own assigned image631–701. The417 full decoded same-page equalities transfer only the earlier actual observation and its original attribution. The701-page candidate is wholly accounted for, including all Programs and References pages, with explicit proof-boundary joins. A truncated667–671 tool response was given no credit; those pages were reopened in visible smaller calls and read.',
    'Current07 image/source reading found three new heading reservations, missing fibre/variable mathematical typography, and proof-wide selected-symbol cases in02KZ,02LH and03DC. Root read all216,1675 and601 original statement/proof lines respectively, the complete Q139 remark and all authored current image reports. The actual D20 owners and P15 were reopened; the651/652 actual D23 owner was also reopened. These reopenings and staged proposals earn no closure credit. Exact maps/inverses and actual downstream imports remain part of the source admission.',
    args.work_note.strip(),
    f"Current count input: {count['selected_event_associations']} selected associations in{count['declared_evidence_groups']} evidence groups. This review does not refresh those derived counts or create a mathematical event.",
    f"Actual unit state: Paper III {counts['III']['done']} done and{sum(v for k,v in counts['III'].items() if k != 'done')} open; Paper IV {counts['IV']['done']} done and{sum(v for k,v in counts['IV'].items() if k != 'done')} open. All128 III required checks remain done; all66 IV checks remain unbegun.",
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
    if row.get('status', 'open') != 'done':
        lines.append(f"| {row['tag']} | {row.get('status', 'open')} |")
lines += ['\n### Paper III provenance and visual gates\n', '| Claim | Source status | Remaining gate |', '|---|---|---|']
for row in claims:
    if row['paper'] == 'III' and row['remaining_gate']:
        lines.append('| ' + ' | '.join(row[k].replace('|', '/') for k in ('claim_id', 'resolution_status', 'remaining_gate')) + ' |')
lines += [
    '\nNext: finish the combined exact source correction, source comparisons and count reconciliation; obtain the accepted successor current/legacy pair and actual changed-page reading; admit supported non-joint III criteria and final records. Paper IV then precedes the joint five-paper phase.',
    'P4, the series-table D18 row and four other-paper provenance claims remain joint. No top-level final Paper III PDF or final extractor output has been admitted. Packaging, proposals and routine guards earn no movement credit.',
    'Consecutive hourly reviews without qualifying movement:0. The two-review stop rule has not been reached.',
    'Next hourly review:2026-11-26T09:30:22+00:00. Next checkpoint111:2026-11-26T08:45:22+00:00. Checkpoint110 was delivered with its cumulative snapshot.\n']
report = ROOT / 'S6_SERIES_PUBLISH_report.md'
report_before = report.read_text()
summary = (f'\n\n## Scheduled review77 — {now.isoformat()}\n\nINCOMPLETE. '
    'The actual Paper III build row closed after full current07/legacy06 diagnostic and target review. '
    'All284 changed/new pages were then actually read, with417 exact prior-image transfers retaining original attribution. '
    'The full candidate07 is accounted for, including Programs and References. New actual whole-proof naming and layout findings '
    'are explicitly reopened; staged proposals are not closures. '
    f"Paper III has{counts['III']['done']} done and{sum(v for k,v in counts['III'].items() if k != 'done')} open unit criteria. "
    'All128 required checks remain done. ' + args.work_note.strip() +
    ' IV and joint review remain. Complete open rows and gates appear in ledger review77. Consecutive no-movement reviews:0.\n')
assert ledger.read_text() == before and report.read_text() == report_before
ledger.write_text(before + '\n'.join(lines), newline='\n')
report.write_text(report_before + summary, newline='\n')
print('Review77 recorded', now.isoformat())
print('Qualifying movement: actual build open->done and284 actual changed-page observations.')
print('Actual units', counts)
print('Counts unchanged:', count['selected_event_associations'], count['declared_evidence_groups'])
print('All current unit/finding/build/provenance gates recorded; consecutive no-movement reviews:0.')
