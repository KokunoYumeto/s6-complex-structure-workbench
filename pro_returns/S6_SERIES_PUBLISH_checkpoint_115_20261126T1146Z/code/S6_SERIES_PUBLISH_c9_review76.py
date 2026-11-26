"""Record scheduled review76 from the actual canonical rows and completed work."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import csv
import json

ROOT=Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
now=datetime.now(timezone.utc)
boundary=datetime.fromisoformat('2026-11-26T07:30:22+00:00')
previous=datetime.fromisoformat('2026-11-26T06:36:29.220714+00:00')
assert now>=boundary

def table(name, delimiter='\t'):
    with (ROOT/name).open(newline='') as f:
        return list(csv.DictReader(f,delimiter=delimiter))

ledger=ROOT/'PROGRESS_LEDGER.md'
before=ledger.read_text()
assert '\n## Review 76 ' not in before
units=table('S6_SERIES_PUBLISH_unit_progress.tsv')
findings=table('S6_SERIES_PUBLISH_findings_III.tsv')
builds=table('S6_SERIES_PUBLISH_build_progress.tsv')
claims=table('S6_SERIES_PUBLISH_provenance_checks.tsv')
required=table('S6_SERIES_PUBLISH_required_progress_III.tsv')
assert len(required)==128 and all(r['status']=='done' for r in required)
closed=[]
for key in ('maps:src:D.2.25','maps:src:D.2.29','maps:src:D.2.39'):
    row,=[r for r in units if r['paper']=='III' and r['unit_id']==key and r['defect_type']=='D20']
    assert row['status']=='done' and datetime.fromisoformat(row['date_utc'])>previous
    assert 'candidate05_combined_source_review.md' in row['evidence']
    closed.append(row)
assert 'open\', \'done' in (ROOT/'code/S6_SERIES_PUBLISH_c9_candidate05_source_disposition.out').read_text()
count=json.loads((ROOT/'records/S6_SERIES_PUBLISH_III_current_check_counts.json').read_text())
assert count['selected_event_associations']==1239 and count['declared_evidence_groups']==953
assert len(count['selected_event_ids'])==1239 and len(count['selected_evidence_groups'])==953
counts={p:Counter(r['status'] for r in units if r['paper']==p) for p in ('III','IV')}
grouped=defaultdict(list)
for row in units:
    if row['status']!='done':
        grouped[(row['paper'],row['unit_id'],row['status'])].append(row['defect_type'] or row['row_kind'])
iv_path=ROOT/'S6_SERIES_PUBLISH_required_progress_IV.tsv'
iv=table(iv_path.name) if iv_path.exists() else [r for r in table('records/S6_SERIES_PUBLISH_required_check_candidates.csv',',') if r['paper']=='IV']
assert len(iv)==66
lines=[f'\n\n## Review 76 — {now.isoformat()}\n',
    f'INCOMPLETE. Scheduled boundary: {boundary.isoformat()}.',
    'Qualifying movement: the three actually reopened D20 rows for D.2.25, D.2.29 and D.2.39 reached done at 07:26:32 UTC after root completed the original/proposed full-proof comparisons and admitted all four proof packets. The containing D.2.39 row covers both LF and LJ with separate formal event owners. P11/P15 also returned to done at source scope. The actual source-disposition output, exact defect/event append and root-authored map/inverse review establish these closures. Packaging, staged proposals and successful guard checks alone earn no movement credit.',
    'The combined source batch admitted159 exact replacements and four used-and-rechecked events. It includes all eleven observed spacing repairs and three fibre-type formatting repairs. The 02S4 containing D23 row was explicitly reopened for its changed-page observation. The final count paragraph and both deposit forms now agree on1239 associations in953 groups, with category totals422/2/58/637/90/30. No independent-proof or additional computation event was added.',
    'The first count inspection stopped before any write because the prior aggregate summary had no selected_event_ids field. The corrected bounded adapter removes exactly the four newly appended events and verifies every preceding category, group total, exact prior prose and249 owners. Its successful inspection and application are retained. The new count JSON explicitly includes selected IDs and groups. A read-only peer check has identified the corresponding final-derivation group-key adapter; its exact correction is being prepared, and no derivation has run.',
    'Current candidate06 and legacy candidate05 each completed three successful TeX passes and converged to701 pages. Their final logs have zero unresolved/rerun, font or duplicate/missing-destination diagnostics, but three overfull displays measure21.24054pt,14.52957pt and51.98416pt. The build row remains open. Backend is reading the full actual logs and preparing exact reflows; global is checking T1 and all formal anchors on this completed intermediate pair before the next shared repair/build batch. No new page-reading credit has been awarded.',
    f"Actual unit state: Paper III {counts['III']['done']} done, {sum(v for k,v in counts['III'].items() if k!='done')} open; Paper IV {counts['IV']['done']} done, {sum(v for k,v in counts['IV'].items() if k!='done')} open. All128 III required checks remain done; all66 IV checks remain unbegun.",
    '\n### Every remaining unit row by exact identity and criterion\n',
    '| Paper | Unit identifier | Status | Open criteria |','|---|---|---|---|']
for (paper,key,status),criteria in grouped.items():
    lines.append(f"| {paper} | {key} | {status} | {', '.join(criteria)} |")
lines+=['\n### Supplied source findings\n','| Finding | Status | Remaining gate |','|---|---|---|']
for row in findings:
    if row['status']!='done':
        lines.append('| '+' | '.join(row[k].replace('|','/') for k in ('id','status','remaining_gate'))+' |')
lines+=['\n### Current build gates\n','| Paper | Status | Scope and remaining gate |','|---|---|---|']
for row in builds:
    if row['paper'] in ('III','IV'):
        lines.append('| '+' | '.join(row[k].replace('|','/') for k in ('paper','status','detail'))+' |')
lines+=['\n### Required checks remaining in Paper IV\n','| Tag | Status |','|---|---|']
for row in iv:
    if row.get('status','open')!='done':
        lines.append(f"| {row['tag']} | {row.get('status','open')} |")
lines+=['\n### Paper III provenance and visual gates\n','| Claim | Source status | Remaining gate |','|---|---|---|']
for row in claims:
    if row['paper']=='III' and row['remaining_gate']:
        lines.append('| '+' | '.join(row[k].replace('|','/') for k in ('claim_id','resolution_status','remaining_gate'))+' |')
lines += [
    '\nNext: admit the exact current diagnostic repairs with any formal-anchor findings, obtain the accepted current/legacy pair, render and actually read every changed page. Reconcile the final record adapter, close the supported non-joint III criteria, and derive the records once from the accepted final artifact. Paper IV follows, then the joint five-paper phase.',
    'P4, the series-table D18 row and the four other-paper provenance claims remain joint. The top-level final Paper III PDF and final extractor output have not been admitted.',
    'Consecutive hourly reviews without qualifying movement:0. The two-review stop rule has not been reached.',
    'Next hourly review:2026-11-26T08:30:22+00:00. Next checkpoint110:2026-11-26T08:00:22+00:00. Checkpoint109 was delivered with its cumulative snapshot.\n']
ledger.write_text(before+'\n'.join(lines),newline='\n')
report=ROOT/'S6_SERIES_PUBLISH_report.md'
report.write_text(report.read_text()+f'\n\n## Scheduled review76 — {now.isoformat()}\n\nINCOMPLETE. Three reopened source D20 rows closed after complete root review and159 exact admitted repairs; P11/P15 are done at source scope. One additional D23 row is open for the observed02S4 formatting. Paper III has{counts["III"]["done"]} done and{sum(v for k,v in counts["III"].items() if k!="done")} open unit criteria. All128 required checks remain done. Counts are1239 associations/953 groups with four new used events. Both701-page builds converged but have three overflows above2pt, so the build and image gates remain open. The exact reflow batch and final-record schema reconciliation are in progress. IV and joint review remain. Complete open rows and remaining gates are in review76 of the ledger. Consecutive no-movement reviews:0.\n',newline='\n')
print('Review76 recorded',now.isoformat())
print('Qualifying completed source criteria',[(r['unit_id'],r['defect_type'],r['date_utc']) for r in closed])
print('Actual units',counts)
print('Build not accepted:3overflows; image/record/IV/joint gates remain. Consecutive no-movement reviews:0.')
