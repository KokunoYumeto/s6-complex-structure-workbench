#!/usr/bin/env python3
"""Scheduled third hourly review, compared with Review44's closed identities."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import csv,hashlib,re
ROOT=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
assert now>=datetime(2026,11,24,14,15,57,tzinfo=timezone.utc)
ledger=(ROOT/'PROGRESS_LEDGER.md').read_text()
baseline=re.search(r'Closed required identities at Review44: ([^\n]+)\.',ledger)
assert baseline
previous=set(baseline[1].split(', '));assert len(previous)==84

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
note=f'''
## Review 45 — {now.isoformat()}

INCOMPLETE. The scheduled14:15:57 UTC review records {len(new)} newly
completed III required identities since Review44: {', '.join(new) or 'none'}.
The current total is {len(closed)}/128 complete and {128-len(closed)} open.
No required identity reopened. Every admitted event identifier resolves to
that exact statement, including each identifier in multiple-event rows.

The new admitted comparisons cover the explicit fixed-embedding collapse
and its rescaled intrinsic geometry, and the additional framed-coefficient
carrier calculation. Their full fresh proofs, original comparisons,
receivers, exact guards and defect/event records support the closures.
No source-edit, unit-restructuring, build or page-reading credit follows
from those admissions.

The OS56/II fresh proof now includes its independently checked rational
model and section, exact marked-cover/peripheral maps and inverses,
integral attachments, canonical-line calculation, toric characteristic
classes and an application of the opened Zhubr primary classification.
It remains subject to full fresh review and individual original release.
The independent collision-realization fresh proof is also complete and
awaits root review. KY's full original/auxiliary comparison and KT's
whole-fibre derivation continue separately; the missing historical JSON
is not claimed bytewise compared.

The released S8/S9 original comparison exposed a global gap in the fresh
phase-avoidance step: its local phase lifts do not give a real lift around
the whole incoming torus. The frozen derivation is preserved. The global
graph-line comparison remains open, receives no pre-exposure credit from
that argument, and is being routed as a statement-only problem to an
unexposed checker while the receiver is repaired. Release earns no closure.
S3 remains in comparison after its earlier independent fresh derivation.

All still-open III identities: {', '.join(open_tags)}.
Proof-state counts: {dict(states)}. Individually released comparisons still
open: {', '.join(pending) or 'none'}.
The exact per-row statuses and unresolved inputs are retained in the
required-progress table. IV's66 required checks remain open; its downstream
use of refined II02Y6/02XE still needs the prescribed scope checks.

All unit statuses remain in S6_SERIES_PUBLISH_unit_progress.tsv, with open
counts {dict(units)}. III retains all756 open unit criteria and IV all729.
III's canonical source remains unchanged at SHA256 {sha}.
After the remaining III checks come its unit restructuring and all defect
applications, provenance/links, clean standalone pdfLaTeX build and every
rendered-page reading. IV follows in that order, then all five together.
No new final candidate PDF has been certified. I, II and V remain at their
closed gates until the joint step; II's E.5.2/E.5.3 remain unchanged.
The final cross-references, notation, deposit fields, joint defect passes,
records tables, concordances and final first-part readings remain open.

Closed required identities at Review45: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Review46 is due2026-11-24T15:15:57+00:00. Checkpoint66 is due now at its
scheduled14:15:57 UTC boundary; the next is15:00:57 UTC. Packaging earns
no movement. This review creates no inventory, census, manifest, seal or
derived-file copy.
'''
for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
    p=ROOT/name;s=p.read_text();assert '\n## Review 45 — ' not in s
    p.write_text(s+note,newline='\n')
print(f'Review45: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}.')
print('Newly completed:',', '.join(new))
print('Open released comparisons:',', '.join(pending))
