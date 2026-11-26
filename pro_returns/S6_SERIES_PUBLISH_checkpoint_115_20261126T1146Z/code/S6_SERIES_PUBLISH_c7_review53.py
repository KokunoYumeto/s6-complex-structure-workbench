"""Fifth hourly review of continuation seven; no inventory refresh."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv, hashlib, io, re
ROOT=Path(__file__).resolve().parents[1]
DUE=datetime(2026,11,25,0,34,24,tzinfo=timezone.utc)
now=datetime.now(timezone.utc)
assert now>=DUE
ledger=(ROOT/'PROGRESS_LEDGER.md').read_text()
assert '\n## Review 53 — ' not in ledger
baseline=re.search(r'Closed required identities at Review52: ([^\n]+)\.',ledger)
assert baseline
previous=set(baseline[1].split(', '));assert len(previous)==103

def table(name):
 with (ROOT/name).open(newline='') as f:
  r=csv.DictReader(f,delimiter='\t');return r.fieldnames,list(r)

fields,rows=table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events={r['event_id']:r for r in table('CHECK_EVENTS.tsv')[1]}
updates={
 '02L2':('full_original_comparison_auxiliary_order_refinement','/root/iii_graph','The complete fresh integral star-cap proof and program/output passed root review before individual release. All original items have been read. The auxiliary exact-order formula must include extra transitive odd rank-one root quotients: the actual order-three example has kappa=27 and total H2 order18, whereas its old formula gives2. Full geometric maps, revised order and receiver comparison are in progress; the target two-primary exclusion stands.'),
 '02L9':('whole_original_comparison_and_receiver_in_progress','/root/iii_02kr','Complete851-line fresh proof, new317-line program, all28 output lines and syntax output passed root review before release. The full original is now read. The alternate Wang sweep needs its exact rim-section shear; its exterior image is zero, so the complete495-pattern conclusion is unchanged. Receiver, auxiliary comparison and records remain open.'),
 '02LA':('whole_original_auxiliary_comparison_receiver_in_progress','/root','The complete all-weight fresh proof, actual D-cover, full cusp relative sequence and unrestricted finite/original matrices were reviewed before release, including two bounded peer reviews. All original proof items are now read. New post-exposure symbolic checks verify every auxiliary minor, area kernel and the finite-meridian order. Receiving proof and endpoint-scope clarification remain in progress.'),
 '02LB':('fresh_conic_classification_in_progress','/root/iii_02ks','Original closed. The exact15-pattern target is read and admitted inputs resolved. Fresh work retains the prescribed fan and is checking the global equivariant-line comparison for the finite cubic; no original conclusion or refutation is yet claimed.'),
 '02LC':('fresh_statement_and_classification_inputs_read','/root','Original closed. Root read only the exact target and dependency statements, plus the admitted complete K9 classification derivation/comparison. The local invariant computation has not yet been proved.'),
}
for row in rows:
 if row['tag'] in updates:
  state,who,note=updates[row['tag']]
  assert row['status']=='open'
  row['packet_status']=state;row['assigned_checker']=who
  row['notes']+=' Review53: '+note
closed=[r for r in rows if r['status']=='done'];tags={r['tag'] for r in closed}
new=sorted(tags-previous)
assert len(rows)==128 and not previous-tags
for row in closed:
 for eid in row['check_event_id'].split(';'):
  if eid.strip():assert eid.strip() in events and events[eid.strip()]['statement_id']==row['label']
open_rows=[r for r in rows if r['status']!='done']
pending=[r['tag'] for r in open_rows if r['proof_status']=='released_after_derivation']
units=Counter(r['paper'] for r in table('S6_SERIES_PUBLISH_unit_progress.tsv')[1] if r['status']=='open')
assert units['III']==784 and units['IV']==756
source_sha=hashlib.sha256((ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert source_sha=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
old_counts=re.findall(r'Consecutive reviews without qualifying movement: (\d+)\.',ledger)
assert old_counts
no_movement=0 if new else int(old_counts[-1])+1
open_table='\n'.join('| '+r['tag']+' | '+r['label']+' | '+r['packet_status']+' | '+r['proof_status']+' |' for r in sorted(open_rows,key=lambda r:r['tag']))
note=f"""
## Review 53 — {now.isoformat()}

INCOMPLETE. Scheduled boundary: {DUE.isoformat()}.
Since Review52, {len(new)} required identities have closed:
{', '.join(new) or 'none'}. Paper III has {len(closed)}/128 complete
and {len(open_rows)} open. Every closure resolves to its exact events,
and no admitted identity has reopened. These required-row closures
are qualifying movement; the no-movement count is reset.

L0 and L1 are admitted after complete fresh, original, auxiliary and
receiving readings. Their precise physical-fan counterexamples have
global geometric repairs. L0 also corrects the original-I2 local-rank
explanation by its primitive global bridge class. Their full smooth
conclusions retain the exact global-map scope, with no extra pointwise
claim on other caps. The general cancellation attribution is replaced
by explicit unstabilized reconstruction.

L7 and L8 are now admitted. Their complete original and receiving
proofs, every auxiliary, the new programs and all output were read.
L7 gives all228 zero-Chern patterns, the primitive mixed-torus maps,
the full integral homology and the b=1 smooth classification. Its
intermediate physical-circle assertion has the explicit order-two
stabilizer counterexample and the component-section-preserving
oriented global fan repair. L8 gives all282 additive patterns and
54 nonzero-Chern patterns, the exact original fibre kernel and the
full L+r bridge at zero as well as nonzero Euler number. All theorem
conclusions stand. Their targeted and post-exposure events retain
separate scope and shared evidence groups.

L2, L9 and LA are individually released after complete fresh proofs
and root reviews. Their original/receiving comparisons remain open.
L2's main star-cap obstruction is proved, while a further original
auxiliary exact-order formula is being corrected for allowed odd
rank-one root quotients. The explicit order-three construction has
normal index27 and total H2 order18. Its two-primary conclusion is
unchanged. L9 has the complete495-pattern local/global proof; its
original's rim-section correction is being related by an exact
unipotent map whose exterior area is zero. LA has the actual all-D
cover, primitive cusp relative image and integral section retaining
boundary torsion. Its original auxiliary minors and alternate
attachment-order meridian have now been verified; its final receiver
and weight-one scope wording remain in progress.

LB's fresh prescribed-fan equivariant computation and LC's initial
classification-input reading earn no closure. Their originals remain
closed. L3's fresh synthesis remains in progress with its original
closed. No draft, release, computation alone or packaging is counted
as a completed required row.

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

Checkpoint76 saved the105/128 state at00:07:18 UTC. This review and
subsequent work are due in checkpoint77 at00:49:24 UTC.

Closed required identities at Review53: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Next review: 2026-11-25T01:34:24+00:00.
Next checkpoint: 2026-11-25T00:49:24+00:00.
No inventory/census refresh or edit manifest, seal, receipt or rebinding
is made. Packaging earns no movement credit.
"""
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
(ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv').write_text(buf.getvalue(),newline='\n')
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 p=ROOT/name;prior=p.read_text();assert '\n## Review 53 — ' not in prior;p.write_text(prior+note,newline='\n')
print(f'Review53: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}')
print('Newly completed: '+', '.join(new))
print('Released comparisons open: '+', '.join(pending))
print('Recorded UTC: '+now.isoformat())
