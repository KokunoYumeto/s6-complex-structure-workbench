"""Sixth hourly review of continuation seven; no inventory refresh."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import io
import re

ROOT = Path(__file__).resolve().parents[1]
DUE = datetime(2026,11,25,1,34,24,tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= DUE
ledger = (ROOT/'PROGRESS_LEDGER.md').read_text()
assert '\n## Review 54 — ' not in ledger
baseline = re.search(r'Closed required identities at Review53: ([^\n]+)\.',ledger)
assert baseline
previous = set(baseline[1].split(', '))
assert len(previous) == 107

def table(name):
    with (ROOT/name).open(newline='') as stream:
        reader = csv.DictReader(stream,delimiter='\t')
        return reader.fieldnames,list(reader)

fields,rows = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events = {r['event_id']:r for r in table('CHECK_EVENTS.tsv')[1]}
updates = {
    '02L3': ('fresh_profile_synthesis_written_original_closed','/root',
             'Original closed. Exact target/dependencies and admitted L1 integral and smooth maps are read. The complete251-line fresh synthesis and new151-line raw-component program with all86 output lines recover all172 natural rows,59 sphere patterns on50 initial rows, the12/4/5 profile split and every affine-parameter and filling condition. Fresh completion is01:33:43 UTC; individual release remains pending.'),
    '02LB': ('whole_original_auxiliary_comparison_in_progress','/root/iii_graph',
             'Complete771-line fresh proof,339-line program, all380 output lines, bounded peer review and Andrus printed17,19--21,42 passed root review before individual release. The entire333-line original is now read by the comparator. Its polynomial gauges and prescribed-fan wall/circle data are being compared exactly. Receiving proof and refutation records remain open.'),
    '02LC': ('fresh_odd_cubic_global_comparison_in_progress','/root/iii_02ks',
             'Original closed. Exact target/dependencies and admitted K8/K9 full derivations are available. Actual finite-action fixed data, global equivariant class, full cubic and refined Pontryagin invariant remain in the fresh-proof lane.'),
    '02LD': ('fresh_weighted_catalogue_integral_maps_in_progress','/root/iii_02kr',
             'Original closed. New exterior program/output and saved raw data reconstruct all21 profiles and172 natural rows. The all-D cover, primitive exterior maps, component-orbit inverse and full finite projected lattices are being proved in the fresh lane; admitted LA is a bounded input.'),
}
for row in rows:
    if row['tag'] in updates and row['status'] == 'open':
        state,who,note = updates[row['tag']]
        row['packet_status'] = state
        row['assigned_checker'] = who
        row['notes'] += ' Review54: '+note
closed = [r for r in rows if r['status'] == 'done']
tags = {r['tag'] for r in closed}
new = sorted(tags-previous)
assert len(rows) == 128 and not previous-tags
for row in closed:
    for event_id in row['check_event_id'].split(';'):
        if event_id.strip():
            assert event_id.strip() in events
            assert events[event_id.strip()]['statement_id'] == row['label']
open_rows = [r for r in rows if r['status'] != 'done']
pending = [r['tag'] for r in open_rows if r['proof_status'] == 'released_after_derivation']
units = Counter(r['paper'] for r in table('S6_SERIES_PUBLISH_unit_progress.tsv')[1] if r['status'] == 'open')
assert units['III'] == 784 and units['IV'] == 756
source_sha = hashlib.sha256((ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert source_sha == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
old_counts = re.findall(r'Consecutive reviews without qualifying movement: (\d+)\.',ledger)
assert old_counts
no_movement = 0 if new else int(old_counts[-1])+1
open_table = '\n'.join('| '+' | '.join((r['tag'],r['label'],r['packet_status'],r['proof_status']))+' |'
                       for r in sorted(open_rows,key=lambda r:r['tag']))
note = f'''
## Review 54 — {now.isoformat()}

INCOMPLETE. Scheduled boundary: {DUE.isoformat()}.
Since Review53, {len(new)} required identities have closed:
{', '.join(new) or 'none'}. Paper III has {len(closed)}/128 complete
and {len(open_rows)} open. Every closure resolves to its exact events,
and no admitted identity has reopened. These required-row closures
are qualifying movement; the no-movement count is reset.

L9 is admitted after the whole fresh proof, original, every auxiliary,
receiving proof, programs and all output were read. Its full495-pattern
presentation covers1728 individual choices. The marked geometric
normal torus has the proved rim correction and exact integral shear;
the general Wang-section formula states every coordinate shift.
No theorem conclusion changed in that comparison.

LA is admitted with the all-weight cover, primitive graph/fibre maps,
the full cusp boundary torsion sequence and its relative section,
the unrestricted finite/original matrices, both attachment orders
and the exact finite meridian order. The weight-one endpoint is
identified by the actual identity covering and toric maps. Its D26
scope correction preserves every displayed formula. The final
receiver's complete syntax output and exact reversible guards were read.

L2 is admitted after every original auxiliary was compared. The
additional transitive rank-one root has full projected index m^3.
The corrected full auxiliary order includes these root factors;
the explicit simply connected order-three example has |H2|=18,
where the old formula gives2. The two-primary obstruction in both
minimal star caps is unchanged. The selected-cusp ray and cone
counts cover every root degree. The degree-one refinement has an
integral H2 right inverse and a surjective fundamental-group map,
proved by lifting to its image cover and factoring its degree.
The five narrowly typed events and eleven defect rows are admitted.

LB's complete fresh proof gives the prescribed-fan cubic1+kappa
and the two explicit order-two models. Its global equivariant-line
comparison, all raw pattern matrices and exact Andrus classification
scope passed root and peer readings. Its original is individually
released. The complete original/auxiliary comparison is in progress,
including the exact old-gauge pullback, actual wall degree and circle
weights. No completed comparison or required closure is claimed yet.

L3's new raw-component enumeration gives the21-profile59-pattern
summary; its complete251-line fresh synthesis is written, with the
entire151-line new program and all86 output lines read. Its original
remains closed pending individual release. LC's
global odd-cubic computation and LD's all-weight integral catalogue
remain in fresh-proof work. Their originals remain closed. These
drafts and computations earn no required-row closure.

### Every open III required identity

| Tag | Statement | Packet/check state | Original-proof state |
|---|---|---|---|
{open_table}

Released comparisons still open: {', '.join(pending) or 'none'}.
All {units['III']} III unit criteria, all66 IV required checks and
all {units['IV']} IV unit criteria retain their existing open rows.
The canonical III source remains unchanged at SHA256 {source_sha}.
The main gate is all III required checks before guarded source and
bibliography integration, the full unit pass, provenance, clean build
and rendered-page reading. IV follows III; I,II,V retain their closed
gates until the five-together step. The II E.5.2/E.5.3 inputs remain
unchanged.

Checkpoint77 saved the108/128 state at00:49:56 UTC. Checkpoint78
is due at this same01:34:24 UTC boundary and follows this review.

Closed required identities at Review54: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Next review: 2026-11-25T02:34:24+00:00.
Next checkpoint: 2026-11-25T02:19:24+00:00.
No inventory/census refresh or edit manifest, seal, receipt or rebinding
is made. Packaging earns no movement credit.
'''
buffer = io.StringIO(newline='')
writer = csv.DictWriter(buffer,fields,delimiter='\t',lineterminator='\n')
writer.writeheader()
writer.writerows(rows)
(ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv').write_text(buffer.getvalue(),newline='\n')
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    path=ROOT/name
    prior=path.read_text()
    assert '\n## Review 54 — ' not in prior
    path.write_text(prior+note,newline='\n')
print(f'Review54: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}')
print('Newly completed: '+', '.join(new))
print('Released comparisons open: '+', '.join(pending))
print('Recorded UTC: '+now.isoformat())
