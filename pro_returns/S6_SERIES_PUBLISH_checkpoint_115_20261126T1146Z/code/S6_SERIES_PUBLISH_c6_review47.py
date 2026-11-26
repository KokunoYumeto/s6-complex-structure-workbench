#!/usr/bin/env python3
"""Scheduled continuation-six Review47; no derived inventory refresh."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import csv,hashlib,re

root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
assert now>=datetime(2026,11,24,16,15,57,tzinfo=timezone.utc)
ledger=(root/'PROGRESS_LEDGER.md').read_text()
baseline=re.search(r'Closed required identities at Review46: ([^\n]+)\.',ledger)
assert baseline
previous=set(baseline[1].split(', '));assert len(previous)==90

def table(name):
    with (root/name).open(newline='') as stream:
        return list(csv.DictReader(stream,delimiter='\t'))

rows=table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events={r['event_id']:r for r in table('CHECK_EVENTS.tsv')}
closed=[r for r in rows if r['status']=='done']
tags={r['tag'] for r in closed};new=sorted(tags-previous)
assert len(rows)==128 and not previous-tags
for row in closed:
    for eid in [x.strip() for x in row['check_event_id'].split(';') if x.strip()]:
        assert eid in events and events[eid]['statement_id']==row['label']
open_tags=sorted(r['tag'] for r in rows if r['status']!='done')
pending=sorted(r['tag'] for r in rows if r['status']!='done' and r['proof_status']=='released_after_derivation')
states=Counter(r['proof_status'] for r in rows if r['status']!='done')
units=Counter(r['paper'] for r in table('S6_SERIES_PUBLISH_unit_progress.tsv') if r['status']=='open')
assert units['III']==756 and units['IV']==729
source_sha=hashlib.sha256((root/'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert source_sha=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
counts=re.findall(r'Consecutive reviews without qualifying movement: (\d+)\.',ledger)
assert counts
no_movement=0 if new else int(counts[-1])+1
note=f"""
## Review 47 — {now.isoformat()}

INCOMPLETE. The scheduled16:15:57 UTC review records {len(new)} newly
completed III required identities since Review46: {', '.join(new) or 'none'}.
III now has {len(closed)}/128 complete and {128-len(closed)} open.
No admitted required identity has been reopened. Every recorded closure
event resolves to its exact statement. The new closure is the complete
OS56/II comparison: its fresh derivation, whole original and all auxiliary
assertions, complete receiving proof, independent post-exposure computation,
exact guards, permanent pairs, defects and event were fully reviewed.

The graph-line gate has changed substantively. Root accepted the unexposed
core countercheck, which gives graph-meridian degrees(0,0) on the actual
closed I2 components, and separately accepted the new incoming-torus
calculation. For positive numerator the latter gives graph degree m and
compression-cap b degree2m. Both exact calculations retain full unit maps,
inverses, corner collars and oriented intersections. Four narrow targeted
events and four confirmed D25 rows record the two failures of the original
physical-dual and zero-cap substitutions. Neither target is closed. Their
staged receiving proofs are UNREADY. The complete integral global class,
capped square, final return index, sphere class and mapping torus remain
open. The prior attempted avoidance proofs remain disclosed and withdrawn
at their failed geometric scope.

A dependency extraction also found a directed cusp-period issue. The new
local sign conjugacy and full period arrows have been read, but the actual
based integral shifts and root characters are still being carried through
the cap identification. No zero-shift global identification is accepted
from monodromy alone, and no admitted source bytes have been changed.
The independent graph checker is continuing the integral handle calculation
without any unsupported closed ambient-cap premise.

The full1049-line KQ fresh derivation,385-line new program,91-line output,
all saved inverse matrices and primary scopes were reviewed by root before
its individual original release at16:04:46.930387 UTC. Its entire original
and every auxiliary assertion are now under comparison, including the
additional relative groups, canonical-form and surgery assertions.
Its complete receiver and admission remain pending. The KR original stays
closed. Root's new KR work derives the explicit two surface models, marked
cycle and section maps, original finite additive fillings and global
integral maps; the full regular-log and oriented reconstruction write-up
is still in preparation. These activities alone receive no closure credit.

All open III identities: {', '.join(open_tags)}.
Proof-state counts: {dict(states)}. Released comparisons still open:
{', '.join(pending) or 'none'}. The required progress table retains every
row's exact status, unresolved inputs and evidence locators.

IV's66 required checks remain open. All unit statuses remain in the unit
progress table, with open counts {dict(units)}; III retains756 and IV729.
III's canonical SHA256 remains {source_sha}. Required checks precede each
paper's unit restructuring, all defect applications, provenance and links,
clean standalone pdfLaTeX build and every rendered-page reading. IV follows
III, then all five together. I, II and V remain closed until that joint
step, with II E.5.2/E.5.3 unchanged. All joint final gates remain open.

Closed required identities at Review47: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Review48 is due2026-11-24T17:15:57+00:00. Checkpoint68 was packed at
15:46:08 UTC for the15:45:57 UTC boundary and delivered. Checkpoint69
is due16:30:57 UTC. This review creates no inventory, census, manifest,
seal or derived-file copy.
"""
for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
    path=root/name
    prior=path.read_text();assert '\n## Review 47 — ' not in prior
    path.write_text(prior+note,newline='\n')
print('Review47:',len(closed),'/128 done;',len(new),'new closures; no-movement count',no_movement)
print('Newly completed:',', '.join(new))
print('Released comparisons open:',', '.join(pending))
