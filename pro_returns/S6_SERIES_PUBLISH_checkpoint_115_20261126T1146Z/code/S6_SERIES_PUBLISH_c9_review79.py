"""Record review79 from the admitted build and completed attributed image reading."""
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
start = datetime.fromisoformat('2026-11-26T09:30:22+00:00')
boundary = datetime.fromisoformat('2026-11-26T10:30:22+00:00')
assert now >= boundary

def table(name, delimiter='\t'):
    with (ROOT/name).open(newline='') as f:
        return list(csv.DictReader(f, delimiter=delimiter))

ledger = ROOT/'PROGRESS_LEDGER.md'
before = ledger.read_text()
assert '\n## Review 79 ' not in before
builds = table('S6_SERIES_PUBLISH_build_progress.tsv')
build, = [r for r in builds if r['paper']=='III']
movement = datetime.fromisoformat('2026-11-26T09:35:34.563481+00:00')
assert start <= movement <= boundary
assert build['status']=='done' and build['date_utc']==movement.isoformat()
assert build['pdf_sha256']=='f284a0556c64684531f1d05b5370be02b111f8c9abee8c5ec7463bcf12ed2dc4'
admission = (ROOT/'code/S6_SERIES_PUBLISH_c9_admit_candidate10_builds_apply.out').read_text()
assert 'Admitted the Paper III build row and appended the observed T1/anchor recheck.' in admission
reading = (ROOT/'S6_SERIES_PUBLISH_reading_III.md').read_text()
assert '## Candidate10: completed attributed coverage' in reading
assert 'four actual89-page allocations' in (ROOT/'code/S6_SERIES_PUBLISH_c9_reconcile_candidate10_reading_apply.out').read_text()
root_reading = (ROOT/'agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate10_final_reading.md').read_text()
assert 'Completed at 2026-11-26T10:03:52.256718+00:00.' in root_reading
assert start <= datetime.fromisoformat('2026-11-26T10:03:52.256718+00:00') <= boundary
units = table('S6_SERIES_PUBLISH_unit_progress.tsv')
findings = table('S6_SERIES_PUBLISH_findings_III.tsv')
claims = table('S6_SERIES_PUBLISH_provenance_checks.tsv')
required = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
assert len(required)==128 and all(r['status']=='done' for r in required)
p15, = [r for r in findings if r['id']=='P15']
counts = {paper:Counter(r['status'] for r in units if r['paper']==paper) for paper in ('III','IV')}
grouped = defaultdict(list)
for row in units:
    if row['status']!='done':
        grouped[(row['paper'],row['unit_id'],row['status'])].append(row['defect_type'] or row['row_kind'])
criteria = Counter(r['defect_type'] or r['row_kind'] for r in units if r['paper']=='III' and r['status']!='done')
iv_path = ROOT/'S6_SERIES_PUBLISH_required_progress_IV.tsv'
iv = table(iv_path.name) if iv_path.exists() else [r for r in table('records/S6_SERIES_PUBLISH_required_check_candidates.csv',',') if r['paper']=='IV']
assert len(iv)==66
iv_status = Counter(r['status'] if iv_path.exists() else 'unbegun' for r in iv)
count = json.loads((ROOT/'records/S6_SERIES_PUBLISH_III_current_check_counts.json').read_text())
assert len(count['selected_event_ids'])==count['selected_event_associations']
assert len(count['selected_evidence_groups'])==count['declared_evidence_groups']
source_sha = hashlib.sha256((ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
lines = [f'\n\n## Review 79 — {now.isoformat()}\n',
    f'INCOMPLETE. Scheduled boundary: {boundary.isoformat()}. Exact interval: {start.isoformat()} through {boundary.isoformat()}.',
    'Qualifying movement: the Paper III build gate reached done at 2026-11-26T09:35:34.563481+00:00 after actual current10/legacy09 convergence, complete raw-log review and exact alias/link/formal-owner inspections. The observed transition is retained in code/S6_SERIES_PUBLISH_c9_admit_candidate10_builds.py, its apply.out and the canonical build row. Both PDFs have703 pages; all249 formal owners have zero exceptions and every named internal link resolves. This actual gate transition resets consecutive no-movement reviews to zero.',
    'Substantive actual reading also completed within this interval: all356 changed current10 pages were viewed and read, four allocations of89, including all three adjoining joins and every Programs/References page. The other347 pages preserve original observations through exact full decoded same-page equality. Root completed its actual615–703 range at10:03:52.256718 UTC and fully read all four authored reports. The canonical reading history and exact reconciliation output retain the original reader/PDF lineage. The reconciliation itself adds no reading credit.',
    'The page pass exposed source-role and layout findings. Their exact D20 rows and P15 are open; these reopenings do not revoke the unchanged required mathematical checks or earn movement credit. Staged proposals, guards, counts and checkpoint packaging earn no qualifying movement. No final publication-PDF closure or new independent check is asserted.',
    f'Live source SHA-256: {source_sha}.', a.work_note.strip(),
    f"Counts retained: {count['selected_event_associations']} associations in {count['declared_evidence_groups']} evidence groups; types {count['counts']}. No mathematical event or derived count is created by this review.",
    f"Actual unit state: III {counts['III']['done']} done and {sum(v for k,v in counts['III'].items() if k!='done')} open; IV {counts['IV']['done']} done and {sum(v for k,v in counts['IV'].items() if k!='done')} open. All128 III required checks remain done; IV has66 required rows, statuses {dict(iv_status)}.",
    f'Open III criteria: {dict(criteria)}. P15: {p15["status"]}.',
    '\n### Every remaining unit row by exact identity and criterion\n',
    '| Paper | Unit identifier | Status | Open criteria |','|---|---|---|---|']
for (paper,key,status),types in grouped.items():
    lines.append(f"| {paper} | {key} | {status} | {', '.join(types)} |")
lines += ['\n### Supplied source findings\n','| Finding | Status | Remaining gate |','|---|---|---|']
for row in findings:
    if row['status']!='done':
        lines.append('| '+' | '.join(row[k].replace('|','/') for k in ('id','status','remaining_gate'))+' |')
lines += ['\n### Current build gates\n','| Paper | Status | Scope and remaining gate |','|---|---|---|']
for row in builds:
    if row['paper'] in ('III','IV'):
        lines.append('| '+' | '.join(row[k].replace('|','/') for k in ('paper','status','detail'))+' |')
lines += ['\n### Required checks remaining in Paper IV\n','| Tag | Status |','|---|---|']
for row in iv:
    status = row['status'] if iv_path.exists() else 'unbegun'
    if status!='done':
        lines.append(f"| {row['tag']} | {status} |")
lines += ['\n### Paper III provenance and visual gates\n','| Claim | Source status | Remaining gate |','|---|---|---|']
for row in claims:
    if row['paper']=='III' and row['remaining_gate']:
        lines.append('| '+' | '.join(row[k].replace('|','/') for k in ('claim_id','resolution_status','remaining_gate'))+' |')
lines += ['\nNext: finish the complete original/proposed/caller comparisons, admit only exact supported source rows and exposed associations, then build current11/legacy10 and read every changed page. Final non-joint III records follow supported closure; IV then precedes the joint five-paper phase.',
    'P4, the series-table D18 row and four other-paper provenance claims remain joint. No top-level final III PDF or final extractor output has been admitted.',
    'Consecutive hourly reviews without qualifying movement:0. The two-review stop rule has not been reached.',
    'Next hourly review80:2026-11-26T11:30:22+00:00. Checkpoint113 was saved at10:16:02.008981 UTC; next checkpoint114:2026-11-26T11:00:22+00:00.\n']
report = ROOT/'S6_SERIES_PUBLISH_report.md'
report_before = report.read_text()
summary = (f'\n\n## Scheduled review79 — {now.isoformat()}\n\nINCOMPLETE. '
    'Qualifying movement is the actual Paper III build gate open→done at09:35:34.563481 UTC. Complete current10 image coverage also finished:347 attributed exact transfers plus356 actual changed-page readings, including all Programs and References. '
    f"III has {counts['III']['done']} done and {sum(v for k,v in counts['III'].items() if k!='done')} open unit criteria; all128 required checks remain done. "
    +a.work_note.strip()+' Reopenings, staged proposals, reconciliation and packaging earn no movement credit. IV and the joint review remain. All exact open units and gates are recorded in review79. Consecutive no-movement reviews:0.\n')
assert ledger.read_text()==before and report.read_text()==report_before
ledger.write_text(before+'\n'.join(lines),newline='\n')
report.write_text(report_before+summary,newline='\n')
print('Review79 recorded',now.isoformat())
print('Qualifying movement: actual III build open→done',movement.isoformat())
print('Completed image coverage:347 exact transfers +356 actual fresh pages; original attribution retained.')
print('Actual units',counts,'Open III criteria',criteria)
print('Counts unchanged',count['selected_event_associations'],count['declared_evidence_groups'])
print('All open unit/finding/build/provenance gates recorded; consecutive no-movement reviews:0.')
