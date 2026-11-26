"""Record the due review and reopen the concrete candidate05 findings."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import csv
import hashlib

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
now = datetime.now(timezone.utc)
boundary = datetime.fromisoformat('2026-11-26T06:30:22+00:00')
assert now >= boundary
source = ROOT / 'S6_SERIES_PUBLISH_III.tex'
assert hashlib.sha256(source.read_bytes()).hexdigest() == '7769c410dbc30e0171a298400d54baf75481a4c358133564fac064b9da5598f4'

def table(name, delimiter='\t'):
    with (ROOT / name).open(newline='') as stream:
        return list(csv.DictReader(stream, delimiter=delimiter))

def write_table(name, rows):
    with (ROOT / name).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)

ledger_path = ROOT / 'PROGRESS_LEDGER.md'
ledger_before = ledger_path.read_text()
assert '\n## Review 75 ' not in ledger_before
units = table('S6_SERIES_PUBLISH_unit_progress.tsv')
findings = table('S6_SERIES_PUBLISH_findings_III.tsv')
builds = table('S6_SERIES_PUBLISH_build_progress.tsv')
provenance = table('S6_SERIES_PUBLISH_provenance_checks.tsv')
required = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
assert len(required) == 128 and all(row['status'] == 'done' for row in required)
build = next(row for row in builds if row['paper'] == 'III')
assert build['status'] == 'done'
assert datetime.fromisoformat(build['date_utc']) > datetime.fromisoformat('2026-11-26T05:30:32.689139+00:00')
assert build['pdf_sha256'] == '90d14a1f46004223a1b3ac7bd520024ddb05e8051cacc30f054a3d6e06d5c2e6'

proof_units = {
    'maps:src:D.2.25': '02L0 full-proof roles, including period, graph, Euler, Smith, CRT and framing objects',
    'maps:src:D.2.29': '02L4 Smith matrix/disc bundle, finite-power/free-rank, vector/Bezout, angular-parameter and projector/section roles',
    'maps:src:D.2.39': 'Containing section 17.1: 02LF and 02LJ complete-proof symbol bindings and explicit physical/rank-one/cusp period transports',
}
layout_units = {
    'maps:src:D.2.25': 'candidate05 pages 263–264: stranded simply-connected-reduction paragraph heading',
    'maps:src:D.2.44': 'candidate05 pages 502–503 and 513–514: stranded subsection/definition headings',
    'wb:cusp-cone-section': 'candidate05 pages 617–618: stranded section/subsection/definition headings',
    'wb:cusp-cone-target-slice-embeddings': 'candidate05 pages 626–627: stranded subsection/definition headings',
    'wb:sphere-metric-scaling-trichotomy': 'candidate05 pages 668–669: stranded subsection/theorem headings',
}
evidence = '; '.join([
    'agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_candidate05_first_range_images.md',
    'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_candidate05_pages300_433_review.md',
    'agents/continuation9_reading_thirdquarter/S6_SERIES_PUBLISH_c9_candidate05_pages434_567_review.md',
    'agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate05_final_reading.md',
    'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_candidate05_spacing_review.md',
])
reopened = []
for row in units:
    if row['paper'] != 'III':
        continue
    reason = (proof_units.get(row['unit_id']) if row['defect_type'] == 'D20'
              else layout_units.get(row['unit_id']) if row['defect_type'] == 'D23' else None)
    if reason:
        assert row['status'] == 'done'
        row['status'] = 'open'
        row['date_utc'] = now.isoformat()
        row['evidence'] += '; ' + evidence
        row['detail'] += ' Candidate05 actual-image and bounded-source finding reopens this criterion: ' + reason + '. Exact full-proof or layout repair, root admission and the resulting build/image checks remain. No paragraph-scope rebinding is accepted.'
        reopened.append((row['unit_id'], row['defect_type']))
assert len(reopened) == 8
for row in findings:
    if row['id'] in {'P11', 'P15'}:
        assert row['status'] == 'done'
        row['status'] = 'open'
        row['date_utc'] = now.isoformat()
        row['source_resolution'] += ' Candidate05 actual-image review and complete bounded source readings found residual proof-wide roles in 02L0, 02L4, 02LF and 02LJ. The explicit period-coordinate transports in LF/LJ are part of the same bounded repair. The prior final-source disposition is reopened for these concrete occurrences.'
        row['remaining_gate'] = 'Exact old/new full-proof comparisons for 02L0, 02L4, 02LF and 02LJ, including the real coordinate maps and their inverses; root admission; rebuilt pages and final gates.'
        row['evidence'] += '; ' + evidence
write_table('S6_SERIES_PUBLISH_unit_progress.tsv', units)
write_table('S6_SERIES_PUBLISH_findings_III.tsv', findings)

counts = {paper: Counter(row['status'] for row in units if row['paper'] == paper) for paper in ('III', 'IV')}
grouped = defaultdict(list)
for row in units:
    if row['status'] != 'done':
        grouped[(row['paper'], row['unit_id'], row['status'])].append(row['defect_type'] or row['row_kind'])
iv_file = ROOT / 'S6_SERIES_PUBLISH_required_progress_IV.tsv'
iv = table(iv_file.name) if iv_file.exists() else [row for row in table('records/S6_SERIES_PUBLISH_required_check_candidates.csv', ',') if row['paper'] == 'IV']
lines = [f'\n\n## Review 75 — {now.isoformat()}\n',
    f'INCOMPLETE. Scheduled boundary: {boundary.isoformat()}.',
    'Qualifying movement since review74: the open Paper III build row reached done on the actual current candidate05 and legacy candidate04 source, with final raw diagnostics, T1 records and all 249 statement-anchor comparisons reviewed. The four prior anchor exceptions were repaired with exact source rows, and the rebuilt pair has zero anchor exceptions. This is a completed build row under the prompt’s explicit main-question row definition. Packaging and pending source proposals earn no movement credit.',
    'The actual candidate05 page reading is now complete with original attributions: 164 pages transfer only by full decoded-pixel equality from the actually read candidate02 page, and all 535 changed pages have individual actual-image notes. Peer reports still require complete root reconciliation before canonical final-page closure. The candidate remains an intermediate artifact.',
    'The reading exposed eleven spacing sites, three literal Kodaira-fibre type formatting sites on pages 565–567, and four proof owners requiring complete notation/basis repair: 02L0, 02L4, 02LF and 02LJ. Three containing D20 rows and five additional D23 rows are explicitly reopened; P11 and P15 are open. Other containing layout rows were already open. The three fibre-name fixes are pending exact source rows; their page defects remain open in the final page gate. All workers are preparing proposals against the same frozen source. No new mathematical event, required-check completion or independent-proof credit is assigned by this review.',
    f"Paper III unit criteria: {counts['III']['done']} done and {sum(v for k,v in counts['III'].items() if k != 'done')} open. Paper IV: {counts['IV']['done']} done and {sum(v for k,v in counts['IV'].items() if k != 'done')} open. All 128 required III checks remain done; all 66 IV required checks remain unbegun.",
    '\n### Every open unit row, grouped by exact identity and criterion\n',
    '| Paper | Unit identifier | Status | Open criteria |', '|---|---|---|---|']
for (paper, unit, status), criteria in grouped.items():
    lines.append(f"| {paper} | {unit} | {status} | {', '.join(criteria)} |")
lines += ['\n### Supplied source findings\n', '| Finding | Status | Remaining gate |', '|---|---|---|']
for row in findings:
    if row['status'] != 'done':
        lines.append('| ' + ' | '.join(row[key].replace('|', '/') for key in ('id','status','remaining_gate')) + ' |')
lines += ['\n### Current build gates\n', '| Paper | Status | Actual scope and remaining gate |', '|---|---|---|']
for row in builds:
    if row['paper'] in ('III','IV'):
        lines.append('| ' + ' | '.join(row[key].replace('|','/') for key in ('paper','status','detail')) + ' |')
lines += ['\n### Required checks remaining in Paper IV\n', '| Tag | Status |', '|---|---|']
for row in iv:
    if row.get('status','open') != 'done':
        lines.append(f"| {row['tag']} | {row.get('status','open')} |")
lines += ['\n### Paper III provenance and final visual gates\n', '| Claim | Source status | Remaining gate |', '|---|---|---|']
for row in provenance:
    if row['paper'] == 'III' and row['remaining_gate']:
        lines.append('| ' + ' | '.join(row[key].replace('|','/') for key in ('claim_id','resolution_status','remaining_gate')) + ' |')
lines += [
    '\nNext operations: finish and review all four exact proof packets and fourteen local rendered fixes; admit them together; update any genuine new check counts once; build both TeX versions; read every changed page. Then close the non-joint III gates and derive the final records from that actual PDF. Paper IV follows, then joint I/II/V and the series comparison.',
    'P4, the four other-paper provenance claims and the series-table comparison remain joint. No top-level final Paper III PDF or final extractor output has been admitted.',
    'Consecutive hourly reviews without qualifying movement: 0.',
    'Next hourly review: 2026-11-26T07:30:22+00:00. Checkpoint108 is due at the same boundary as this review; checkpoint109 is due 2026-11-26T07:15:22+00:00.',
    'The two-consecutive-no-movement stop rule has not been reached.\n']
ledger_path.write_text(ledger_before + '\n'.join(lines), newline='\n')
report = ROOT / 'S6_SERIES_PUBLISH_report.md'
report.write_text(report.read_text() + f'\n\n## Scheduled review75 — {now.isoformat()}\n\nINCOMPLETE. The Paper III build row closed on the reviewed current candidate05 and legacy candidate04, with zero formal-anchor exceptions. All current pages now have attributed actual-image observations or exact decoded-pixel transfers; root reconciliation remains. New observed defects reopen eight unit criteria and P11/P15. III has {counts["III"]["done"]} done unit criteria and {sum(v for k,v in counts["III"].items() if k != "done")} open; all128 required checks remain done. Eleven layout repairs, three fibre-name formatting repairs and four bounded proof repairs are pending admission. The complete open-row and gate inventory is in review75 of the ledger. IV and the joint phase remain. Consecutive no-movement reviews:0.\n', newline='\n')
print('Review75 recorded:', now.isoformat())
print('Reopened unit criteria:', reopened)
print('Actual III/IV unit states:', counts)
print('Qualifying movement: one actual clean-build row closure. No packaging or pending-proposal credit.')
