#!/usr/bin/env python3
"""Scheduled continuation-six Review48; no derived inventory refresh."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import csv,hashlib,re

root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
assert now>=datetime(2026,11,24,17,15,57,tzinfo=timezone.utc)
ledger=(root/'PROGRESS_LEDGER.md').read_text()
baseline=re.search(r'Closed required identities at Review47: ([^\n]+)\.',ledger)
assert baseline
previous=set(baseline[1].split(', '));assert len(previous)==91

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
## Review 48 — {now.isoformat()}

INCOMPLETE. The scheduled17:15:57 UTC review records {len(new)} newly
completed III required identities since Review47: {', '.join(new) or 'none'}.
III now has {len(closed)}/128 complete and {128-len(closed)} open.
No admitted required identity has been reopened. Every recorded closure
event resolves to its exact statement. The new closure is the complete
KQ comparison. Its fresh derivation, full original, all auxiliary
assertions, entire receiving proof, new computation, exact guards,
permanent pairs, defects and event have passed root review.

KR completed its944-line fresh derivation and full root review before
its individual original release at16:55:27 UTC. The whole original and
all auxiliary assertions have been read, together with the complete
receiving proof and new independent post-exposure computation. Its
written comparison, exact repair records and admission remain pending.
This release earns no closure credit. KS remains unexposed. Its checker
has frozen a proposed explicit divisor-cube counterexample to the
oriented assertion; root review has not yet accepted or rejected that
claim. Its other group assertions remain under fresh derivation.

The S8/S9 compression-core and incoming-boundary counterchecks remain
accepted at their exact recorded scopes. Both required rows stay open,
and the staged receivers remain UNREADY. The complete directed-period
marking now retains both integer shears, actual root characters, inverse
coordinate maps and cap changes. The local cap-normal proof and its
properness supplement have been fully read. Its independent ambient
orientation and cycle comparison remain under review. The new global
arc, rim and class derivations are saved but not yet accepted by root.
No complete global square, return index, sphere class or mapping torus
is admitted. Prior failed avoidance arguments remain disclosed.

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

Closed required identities at Review48: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Review49 is due2026-11-24T18:15:57+00:00. Checkpoint69 was packed
at16:31:05 UTC for the16:30:57 UTC boundary and delivered. Checkpoint70
is due17:15:57 UTC. This review creates no inventory, census, manifest,
seal or derived-file copy.
"""
for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
    path=root/name
    prior=path.read_text();assert '\n## Review 48 — ' not in prior
    path.write_text(prior+note,newline='\n')
print('Review48:',len(closed),'/128 done;',len(new),'new closures; no-movement count',no_movement)
print('Newly completed:',', '.join(new))
print('Released comparisons open:',', '.join(pending))
