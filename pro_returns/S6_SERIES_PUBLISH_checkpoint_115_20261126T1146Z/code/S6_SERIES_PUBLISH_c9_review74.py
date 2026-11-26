"""Scheduled review74: actual source closures and every remaining gate."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
boundary = datetime.fromisoformat('2026-11-26T05:30:22+00:00')
previous_review = datetime.fromisoformat('2026-11-26T04:30:35.137506+00:00')
now = datetime.now(timezone.utc)
assert now >= boundary, 'Review74 is not due.'

def table(name, delimiter='\t'):
    with (ROOT / name).open(newline='') as stream:
        return list(csv.DictReader(stream, delimiter=delimiter))

units = table('S6_SERIES_PUBLISH_unit_progress.tsv')
findings = table('S6_SERIES_PUBLISH_findings_III.tsv')
required = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
provenance = table('S6_SERIES_PUBLISH_provenance_checks.tsv')
builds = table('S6_SERIES_PUBLISH_build_progress.tsv')
assert len(required) == 128 and all(row['status'] == 'done' for row in required)
candidate_ids = {
    'maps:src:D.2.32', 'maps:src:D.2.35', 'maps:src:D.2.49',
    'maps:src:D.2.26', 'maps:src:D.2.31',
    'mapsD:repair:collision-realization', 'maps:src:D.2.27',
}
closed = [row for row in units
          if row['paper'] == 'III' and row['defect_type'] == 'D20'
          and row['unit_id'] in candidate_ids and row['status'] == 'done'
          and datetime.fromisoformat(row['date_utc']) > previous_review]
assert len(closed) >= 6
counts = {paper: Counter(row['status'] for row in units if row['paper'] == paper)
          for paper in ('III', 'IV')}
grouped = defaultdict(list)
for row in units:
    if row['status'] != 'done':
        grouped[(row['paper'], row['unit_id'], row['status'])].append(row['defect_type'] or row['row_kind'])
iv_path = ROOT / 'S6_SERIES_PUBLISH_required_progress_IV.tsv'
iv = table(iv_path.name) if iv_path.exists() else [row for row in table('records/S6_SERIES_PUBLISH_required_check_candidates.csv', ',') if row['paper'] == 'IV']
lines = [f'\n\n## Review 74 — {now.isoformat()}\n',
    f'INCOMPLETE. Scheduled boundary: {boundary.isoformat()}.',
    f'Qualifying movement since review73: {len(closed)} actual D20 source units, each explicitly open during this interval, have their exact admitted dispositions and are currently done. The list excludes any currently reopened case. It includes the L8 branch, LE period/scalar, LQ complete retained roles, L1 complete proof roles, L7 marked-complement imports and OG selected-generator branch; the L2 unit is included only when its recorded closure has actually occurred. Packaging, prepared code, extra exposed-use events and repeated descriptions are not counted as movement.',
    'The exact maps remain the basis of each disposition: primitive shears and their inverses, marked period identities, lattice and group quotient maps, cap sections, CRT inverses, and the shifted/direct cocycle assembly outputs. No paragraph-boundary exception or new independent-proof credit is used.',
    'Currently closed source units from this interval: ' + ', '.join(row['unit_id'] for row in closed) + '.',
    f"Paper III unit criteria: {counts['III']['done']} done, {sum(value for key,value in counts['III'].items() if key != 'done')} open. Paper IV: {counts['IV']['done']} done, {sum(value for key,value in counts['IV'].items() if key != 'done')} open. All 128 required III checks remain done.",
    '\n### Every open unit row, grouped by exact identity and criterion\n',
    '| Paper | Unit identifier | Status | Open criteria |', '|---|---|---|---|']
for (paper, unit, status), criteria in grouped.items():
    lines.append(f"| {paper} | {unit} | {status} | {', '.join(criteria)} |")
lines += ['\n### Supplied source findings\n', '| Finding | Status | Remaining gate |', '|---|---|---|']
for row in findings:
    if row['status'] != 'done':
        lines.append('| ' + ' | '.join(row[key].replace('|', '/') for key in ('id', 'status', 'remaining_gate')) + ' |')
lines.append('\nCompleted supplied finding IDs: ' + ', '.join(row['id'] for row in findings if row['status'] == 'done') + '.')
lines += ['\n### Current build gates\n', '| Paper | Status | Actual scope and remaining gate |', '|---|---|---|']
for row in builds:
    if row['paper'] in ('III', 'IV'):
        lines.append('| ' + ' | '.join(row[key].replace('|', '/') for key in ('paper', 'status', 'detail')) + ' |')
lines += ['\n### Required checks remaining in Paper IV\n', '| Tag | Status |', '|---|---|']
for row in iv:
    if row.get('status', 'open') != 'done':
        lines.append(f"| {row['tag']} | {row.get('status', 'open')} |")
lines += ['\n### Paper III provenance and final visual gates\n', '| Claim | Source status | Remaining gate |', '|---|---|---|']
for row in provenance:
    if row['paper'] == 'III' and row['remaining_gate']:
        lines.append('| ' + ' | '.join(row[key].replace('|', '/') for key in ('claim_id', 'resolution_status', 'remaining_gate')) + ' |')
lines += [
    '\nThe final authored-retention reconciliation has exact peer and root reports. Root read the entire current L2 original, all 876 original difference lines and the final boundary-count binding delta, the complete review, event and successful comparison output. Its 23 exact fragments and one exposed-use event are now admitted in code/S6_SERIES_PUBLISH_c9_admit_02L2_retention.out, and code/S6_SERIES_PUBLISH_c9_close_L2_retention.out closes that source unit. P11/P15 finding status remains exactly the actual table above; the final authored dispositions supply their reviewed closure evidence.',
    'The bounded programs review found exactly one missing record for the already printed 58-input replay. All 181 previous records and historical execution limits are retained. The reviewed one-row reconciliation remains subject to its actual inspect/apply outputs; preparation alone closes no provenance or image criterion.',
    'The next operations are the final ledger paragraph and one replay record, both same-source builds with complete diagnostics and actual anchor checks, and every changed page of the new PDF. The 58 D14 groupings and all old candidate02 page observations retain their exact earlier-PDF attribution. Only actual complete decoded-pixel equality at the same physical page transfers an earlier image observation; every other current page is open until read.',
    'Paper IV follows the completed non-joint III gates. P4, the four other-paper provenance claims and the series-table joint comparison remain for the five-paper phase. I, II and V retain their earlier individual gates until then.',
    'Consecutive hourly reviews without qualifying movement: 0.',
    'Next hourly review: 2026-11-26T06:30:22+00:00. Checkpoint106 was saved at its recorded snapshot; checkpoint107 is due 2026-11-26T05:45:22+00:00.',
    'The two-consecutive-no-movement stop rule has not been reached.\n',
]
ledger = ROOT / 'PROGRESS_LEDGER.md'
before = ledger.read_text()
assert '\n## Review 74 ' not in before
ledger.write_text(before + '\n'.join(lines), newline='\n')
report = ROOT / 'S6_SERIES_PUBLISH_report.md'
report.write_text(report.read_text() + f'\n\n## Scheduled review74 — {now.isoformat()}\n\nINCOMPLETE. {len(closed)} actual D20 source units closed through admitted exact comparisons during this interval and remain done. All 128 required III checks remain complete. III has {counts["III"]["done"]} done unit criteria and {sum(value for key,value in counts["III"].items() if key != "done")} open. The ledger records every remaining unit/criterion and the actual source-finding, build, IV-check and provenance states. Final source admission, counts and program-record reconciliation, fresh builds, changed-page reading and derivation remain governed by those actual states. IV and the joint phase follow. Consecutive no-movement reviews: 0.\n', newline='\n')
print('Review74 recorded:', now.isoformat())
print('Actual III/IV unit statuses:', counts)
print(len(closed), 'actual source-unit closures support qualifying movement. No packaging or independent-proof credit.')
