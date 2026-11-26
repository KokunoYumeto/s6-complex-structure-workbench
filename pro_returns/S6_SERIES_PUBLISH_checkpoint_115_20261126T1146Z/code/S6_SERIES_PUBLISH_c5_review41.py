#!/usr/bin/env python3
"""Scheduled Review41, comparing the actual closed identities at Review40."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import re

ROOT=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
assert now>=datetime(2026,11,24,0,26,17,tzinfo=timezone.utc)
ledger=(ROOT/'PROGRESS_LEDGER.md').read_text()
baseline=re.search(r'^Closed required identities at Review40: (.+)\.$',ledger,re.M)
assert baseline
previous=set(baseline[1].split(', '));assert len(previous)==57
def table(name):
 with (ROOT/name).open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
rows=table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events={r['event_id']:r for r in table('CHECK_EVENTS.tsv')}
closed=[r for r in rows if r['status']=='done'];tags={r['tag'] for r in closed}
new=sorted(tags-previous);reopened=sorted(previous-tags)
assert len(rows)==128 and new and not reopened
for r in closed:
 assert r['check_event_id'] in events
 assert events[r['check_event_id']]['statement_id']==r['label']
pending=sorted(r['tag'] for r in rows if r['status']=='open' and r['proof_status']=='released_after_derivation')
units=Counter(r['paper'] for r in table('S6_SERIES_PUBLISH_unit_progress.tsv') if r['status']=='open')
sha=hashlib.sha256((ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert sha=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
note=f'''
## Review 41 — {now.isoformat()}

INCOMPLETE. The scheduled 00:26:17 UTC review records qualifying movement
since Review40: {len(new)} existing required III rows changed to done,
namely {', '.join(new)}. The live total is {len(closed)}/128 complete,
with {128-len(closed)} open. The baseline is the actual closed-identity
set printed at Review40. Proposed-event timestamps and unadmitted
computations provide no closure credit. No closed identity reopened.

The completed comparisons include all original statements and proofs,
the full fresh derivations and genuinely new computations read before
individual release, and the saved receiving texts, guards, defects and
individual events. The fixed-metric endpoint inequalities and tangent
inference have their recorded proof repairs. The degree-one base-cover
endpoint has its exact identity counterexample and separate M>1 refinement.
The quotient minima retain the actual primitive kernels and induced
metrics, finite-cover powers and integer saturation. The compact-carrier
comparison supplies explicit quotient/collar maps, cross/cap/boundary
homology maps, conic volume obstructions and compact blow-down maps.
No rewrite has yet been applied to the III manuscript.

Individually released comparisons still open: {', '.join(pending) or 'none'}.
The seven-family elliptic realization remains open until the actual
complex model is related to the prescribed marked peripheral matrices
and primitive section cocycle. Explicit primary models, collision-family
equations, integral braid/merger maps and ongoing dessin transports are
recorded as research toward that step; they do not close a required row.
The smooth logarithmic-filling calculation remains in its recorded fresh
state and shares the explicitly unresolved geometric input. Other fresh
checks retain their precise exposure and release states in the live table.

Every required-row status is in S6_SERIES_PUBLISH_required_progress_III.tsv,
and every unit-row status is in S6_SERIES_PUBLISH_unit_progress.tsv.
Open unit counts: {dict(units)}. All756 III unit criteria remain open.
The unchanged III source SHA256 is {sha}.
The main question remains all five publication-ready papers. Its gates
remain III's required checks, all unit restructuring/defect removal,
provenance, clean build, typesetting and every final rendered-page reading;
then IV's66 required checks and729 unit criteria with the corresponding
publication gates; then the joint series work.

I and V remain closed until the joint step. Bounded older-I construction
inputs receive no I credit. II remains final, with E.5.2/E.5.3 unchanged.
Every III/IV use of refined II02Y6/02XE still requires its downstream
scope check. Joint D26/later-type applications, cross-references, notation,
deposit fields, records tables and final first-part readings remain open.

Closed required identities at Review41: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement:0. Review42 is due
2026-11-24T01:26:17+00:00. Checkpoint60 is due on this00:26:17 boundary;
checkpoint61 is due2026-11-24T01:11:17+00:00. Packaging is no movement.
This review produces no inventory, census, manifest, seal or derived-file copy.
'''
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 p=ROOT/name;t=p.read_text();assert '\n## Review 41 — ' not in t
 p.write_text(t+note,newline='\n')
print(f'Review41: {len(closed)}/128 done; {len(new)} new closures since40; no-movement count0.')
print('Newly completed:',', '.join(new))
print('Open released comparisons:',', '.join(pending))
