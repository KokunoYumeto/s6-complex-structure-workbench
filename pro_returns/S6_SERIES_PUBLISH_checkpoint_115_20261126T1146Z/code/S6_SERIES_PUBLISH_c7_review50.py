"""Record continuation seven's second scheduled hourly review."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import re

ROOT=Path(__file__).resolve().parents[1]
DUE=datetime(2026,11,24,21,34,24,tzinfo=timezone.utc)
now=datetime.now(timezone.utc)
assert now>=DUE
ledger=(ROOT/'PROGRESS_LEDGER.md').read_text()
assert '\n## Review 50 — ' not in ledger
baseline=re.search(r'Closed required identities at Review49: ([^\n]+)\.',ledger)
assert baseline
previous=set(baseline[1].split(', '))
assert len(previous)==93

def table(name):
    with (ROOT/name).open(newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))

rows=table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events={r['event_id']:r for r in table('CHECK_EVENTS.tsv')}
closed=[r for r in rows if r['status']=='done']
tags={r['tag'] for r in closed}
new=sorted(tags-previous)
assert len(rows)==128 and not previous-tags
for row in closed:
    for eid in row['check_event_id'].split(';'):
        eid=eid.strip()
        if eid:
            assert eid in events and events[eid]['statement_id']==row['label']
open_rows=[r for r in rows if r['status']!='done']
pending=[r['tag'] for r in open_rows if r['proof_status']=='released_after_derivation']
units=Counter(r['paper'] for r in table('S6_SERIES_PUBLISH_unit_progress.tsv') if r['status']=='open')
assert units['III']==784 and units['IV']==756
source_sha=hashlib.sha256((ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert source_sha=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
old_counts=re.findall(r'Consecutive reviews without qualifying movement: (\d+)\.',ledger)
assert old_counts
no_movement=0 if new else int(old_counts[-1])+1
open_table='\n'.join('| '+r['tag']+' | '+r['label']+' | '+r['packet_status']+' | '+r['proof_status']+' |' for r in sorted(open_rows,key=lambda r:r['tag']))
note=f'''
## Review 50 — {now.isoformat()}

INCOMPLETE. Scheduled boundary: {DUE.isoformat()}.
Since Review49, {len(new)} required identities have closed:
{', '.join(new) or 'none'}. Paper III has {len(closed)}/128 complete
and {len(open_rows)} open. Every closure resolves to its exact check
event; no admitted required identity has reopened. These completed
required checks supply qualifying movement.

S8 and S9 now have complete corrected proofs and whole-original
comparisons: the capped square gives return integer zero, oriented
sphere class zero and product mapping torus. Their failed original
substitutions remain recorded. KS is fully settled: D.V1/V2 stand,
D.V3 is refuted by the integral divisor cube six, and the corrected
flag-manifold connected-sum classification is proved with the complex
orientation and exact framing. Its full auxiliary comparison includes
the true fixed-class/surgery maps and the post-exposure correction of
the working G/−G component label. The corrected label leaves the
actual periods, line, caps and all proven groups/cubics unchanged.

KU's complete bounded archive check is admitted. It gives exact
coverage of the fifty inputs and eight clutch records, with all
reported integral groups and recognition flags checked. Its local
catalogue table is self-contained. No new remote execution or
unpublished-local-model proof is credited. KV and KW have completed
fresh proofs and authorized individual releases; their exact current
comparison states appear below. Historical program counts remain
unverified wherever their old programs were not opened.

KX has its construction-only inputs and a fresh checker, with a
separate fresh necessity subtask. Root's new finite component-degree
enumeration is held from that checker until its distinct derivation
and program are complete; this arithmetic alone closes no row. L0
has a prepared fresh input scope and awaits/reactivates its checker
at the available concurrency slot. L1's complete target statement
has been manually separated as claims; its original proof remains
embargoed and its KX/L0 dependencies remain open. Input preparation,
release and packaging earn no closure credit.

### Every open III required identity

| Tag | Statement | Packet/check state | Original-proof state |
|---|---|---|---|
{open_table}

The required-progress table retains each row's exact unresolved
inputs, assigned checker and evidence paths. Released comparisons
still open: {', '.join(pending) or 'none'}.

All 784 III unit criteria, all 66 IV required checks and all 756 IV
unit criteria remain open. Their individual rows retain status in
the unit and IV required-progress tables. Current open unit counts:
{dict(units)}. D27's 55 added III/IV criteria and the later joint
applications remain open. Canonical III is unchanged at SHA256
{source_sha}.

The main gate remains completion of III's required checks before
the full unit pass, staged text/bibliography application, provenance,
clean build and every final rendered page. IV follows III; I, II
and V retain their existing closed gates until the five-together
step. The specified II E.5.2/E.5.3 inputs are unchanged. No final
paper has been reopened or rebuilt here. Checkpoint72 records its
earlier95/128 snapshot; later admissions are in the current records.

Closed required identities at Review50: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Next review: 2026-11-24T22:34:24+00:00.
Next checkpoint: 2026-11-24T21:49:24+00:00.
This review refreshes no inventory or census and creates no edit
manifest, seal, receipt, rebinding or derived-file copy.
'''
for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
    p=ROOT/name
    prior=p.read_text()
    assert '\n## Review 50 — ' not in prior
    p.write_text(prior+note,newline='\n')
print(f'Review50: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}')
print('Newly completed: '+', '.join(new))
print('Released comparisons open: '+', '.join(pending))
print('Recorded UTC: '+now.isoformat())
