#!/usr/bin/env python3
"""Scheduled fourth hourly review, compared with Review45's closed identities."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import csv,hashlib,re
ROOT=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
assert now>=datetime(2026,11,24,15,15,57,tzinfo=timezone.utc)
ledger=(ROOT/'PROGRESS_LEDGER.md').read_text()
baseline=re.search(r'Closed required identities at Review45: ([^\n]+)\.',ledger)
assert baseline
previous=set(baseline[1].split(', '));assert len(previous)==86

def table(name):
    with (ROOT/name).open(newline='') as stream:
        return list(csv.DictReader(stream,delimiter='\t'))

rows=table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events={row['event_id']:row for row in table('CHECK_EVENTS.tsv')}
closed=[row for row in rows if row['status']=='done']
tags={row['tag'] for row in closed};new=sorted(tags-previous)
assert len(rows)==128 and not previous-tags
for row in closed:
    ids=[value.strip() for value in row['check_event_id'].split(';') if value.strip()]
    assert ids
    for eid in ids:assert eid in events and events[eid]['statement_id']==row['label']
open_tags=sorted(row['tag'] for row in rows if row['status']!='done')
pending=sorted(row['tag'] for row in rows if row['status']!='done' and row['proof_status']=='released_after_derivation')
states=Counter(row['proof_status'] for row in rows if row['status']!='done')
units=Counter(row['paper'] for row in table('S6_SERIES_PUBLISH_unit_progress.tsv') if row['status']=='open')
assert units['III']==756 and units['IV']==729
sha=hashlib.sha256((ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert sha=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
counts=re.findall(r'Consecutive reviews without qualifying movement: (\d+)\.',ledger)
assert counts
no_movement=0 if new else int(counts[-1])+1
note=f"""
## Review 46 — {now.isoformat()}

INCOMPLETE. The scheduled15:15:57 UTC review records {len(new)} newly
completed III required identities since Review45: {', '.join(new) or 'none'}.
The current total is {len(closed)}/128 complete and {128-len(closed)} open.
No required identity reopened. Every admitted event identifier resolves to
that exact statement, including each identifier in multiple-event rows.

The newly admitted comparisons cover the finite list of narrow multiples,
the actual whole-fibre line normalization, the section-twist return and
its collar signs, and both marked collision surfaces. Complete fresh
derivations precede their authorized original comparisons. Their receivers,
exact guards, defects and event rows have been fully reviewed. The marked
surface comparison also gives an author-only bibliography correction,
retained under its separate exact guard. These admissions confer no
source-edit, unit-restructuring, build or rendered-page credit.

The OS56/II computation is fully derived and its entire original proof
and every auxiliary assertion have been compared. Its receiving proof
and proposed admission records remain in preparation. The new odd-star
calculation is proceeding from statement, raw matrices, admitted inputs
and primary literature, with its target original closed.

The independent graph-line repair has now been fixed by an unexposed
checker and awaits full root review. Its scope is positive numerator
and every integral overlap exponent; negative transport remains separately
tracked. The earlier exposed global phase-avoidance gap remains disclosed
in the unchanged frozen S8/S9 derivation. The complete S8/S9 receivers
and comparisons are staged, with no fresh credit assigned to that withdrawn
inference or its dependent conclusion. Those targets remain open.

All still-open III identities: {', '.join(open_tags)}.
Proof-state counts: {dict(states)}. Individually released comparisons still
open: {', '.join(pending) or 'none'}.
The exact per-row statuses and unresolved inputs remain in the required
progress table. IV's66 required checks remain open, including the
prescribed scope checks for its uses of refined II02Y6/02XE.

All unit statuses remain in S6_SERIES_PUBLISH_unit_progress.tsv, with open
counts {dict(units)}. III retains all756 open unit criteria and IV all729.
III's canonical source remains unchanged at SHA256 {sha}.
The remaining III checks precede its unit restructuring, all defect
applications, provenance and links, clean standalone pdfLaTeX build, and
every rendered-page reading. IV follows, then all five together. I, II
and V retain their closed gates until that joint step; II E.5.2/E.5.3
remain unchanged. All final joint gates and deliverables remain open.

Closed required identities at Review46: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Review47 is due2026-11-24T16:15:57+00:00. Checkpoint67 was saved at
15:01:16 UTC for the15:00:57 UTC boundary; checkpoint68 is due15:45:57 UTC.
This review creates no inventory, census, manifest, seal or derived-file copy.
"""
for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
    p=ROOT/name;s=p.read_text();assert '\n## Review 46 — ' not in s
    p.write_text(s+note,newline='\n')
print(f'Review46: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}.')
print('Newly completed:',', '.join(new))
print('Open released comparisons:',', '.join(pending))
