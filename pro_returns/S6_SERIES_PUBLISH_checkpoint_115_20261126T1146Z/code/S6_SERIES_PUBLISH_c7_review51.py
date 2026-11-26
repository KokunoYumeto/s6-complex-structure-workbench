"""Record the third scheduled hourly review of continuation seven."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import re

ROOT=Path(__file__).resolve().parents[1]
DUE=datetime(2026,11,24,22,34,24,tzinfo=timezone.utc)
now=datetime.now(timezone.utc)
assert now>=DUE
ledger=(ROOT/'PROGRESS_LEDGER.md').read_text()
assert '\n## Review 51 — ' not in ledger
baseline=re.search(r'Closed required identities at Review50: ([^\n]+)\.',ledger)
assert baseline
previous=set(baseline[1].split(', '))
assert len(previous)==97


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
        if eid:assert eid in events and events[eid]['statement_id']==row['label']
open_rows=[r for r in rows if r['status']!='done']
pending=[r['tag'] for r in open_rows if r['proof_status']=='released_after_derivation']
units=Counter(r['paper'] for r in table('S6_SERIES_PUBLISH_unit_progress.tsv') if r['status']=='open')
assert units['III']==784 and units['IV']==756
source_sha=hashlib.sha256((ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert source_sha=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
old_counts=re.findall(r'Consecutive reviews without qualifying movement: (\d+)\.',ledger)
assert old_counts
no_movement=0 if new else int(old_counts[-1])+1
open_table='\n'.join('| '+r['tag']+' | '+r['label']+' | '+r['packet_status']+' | '+r['proof_status']+' |'
                     for r in sorted(open_rows,key=lambda r:r['tag']))
states={r['tag']:r['status']+'; '+r['packet_status'] for r in rows}
note=f'''
## Review 51 — {now.isoformat()}

INCOMPLETE. Scheduled boundary: {DUE.isoformat()}.
Since Review50, {len(new)} required identities have closed:
{', '.join(new) or 'none'}. Paper III has {len(closed)}/128 complete
and {len(open_rows)} open. Every closure resolves to its exact check
event; no admitted identity has reopened. The required-row closures
are the qualifying movement for this review.

KV and KW are admitted after complete fresh derivations, entire
original/receiver comparisons, all auxiliary assertions, independent
programs and every output row. Their marked cap and complement maps,
canonical divisor orders, smooth framed reconstruction and full ring
claims are settled at their recorded scopes. The cusp in these cases
is the identified-boundary hexagonal model; no KS embedded-divisor
cube calculation is transferred without its map. The older unverified
execution counts were removed from the proposed text.

KX current state: {states['02KX']}. Its frozen fresh proof establishes
the 172/226 finite data and exact line/vertical-divisor maps. Its
individual original was released only after that complete proof and
all new output had been read. The ensuing auxiliary derivation checks
the original theta-frame determinant, integral fan transport, local
specialization, original-cap Chern effects and global rank budget.
Its comparison receives credit only when its required row is closed.

L0 current state: {states['02L0']}; L1: {states['02L1']}.
Their distinct construction-only calculations derive the semistable
and nonstar catalogue constants, primitive graph maps and exact
fibre quotient. The specified KY cusp fan is retained. The additional
smooth argument uses actual toric flip charts and an exact relative
ball proof; it retains the degree-five complement class and the
outer boundary parameterization. Primary Barden, Kervaire--Milnor
and Milnor loci were reopened at the recorded scopes. These notes
and input computations do not themselves close required rows.

KZ current state: {states['02KZ']}. Its new I3-star exclusion derives
the primitive 3ell-component cover, every reflection offset and the
positive local quotient, with the two original-cap cases separately
treated. Its original comparison and admission have their own gates.

The root's L4/L6 local derivation includes every affine lift and proper
power, the torsion normal character, and the complete Thom kernel.
The exact all-parameter one-site minors retain the zero-Euler free
coordinate; a new direct-minor program checked 163200 presentations.
The finite-pattern inclusion is explicit: 164 primitive-gamma patterns
embed in the full 198 on 148 nonstar rows, with 34 additional patterns.
The local finite-position totals are 102=68+34 across the whole
catalogue and 94=62+32 on nonstar rows. The eight complementary
positions are listed, so the different scopes have exact inclusion
maps. Their global extension and original comparisons remain separate.

### Every open III required identity

| Tag | Statement | Packet/check state | Original-proof state |
|---|---|---|---|
{open_table}

The required-progress table retains each row's assigned checker,
unresolved inputs and evidence. Released comparisons still open:
{', '.join(pending) or 'none'}.

All 784 III unit criteria, all 66 IV required checks and all 756 IV
unit criteria remain open. Individual statuses remain in their
existing progress tables. Open unit counts: {dict(units)}.
Canonical III remains unchanged at SHA256 {source_sha}.
The main gate is completion of III's required checks before its
full unit pass, staged source/bibliography integration, provenance,
clean build and final page reading. IV follows III. I, II and V
retain their existing closed gates until the five-together step;
the specified II E.5.2/E.5.3 inputs remain unchanged.

Checkpoint73 contains its earlier 99/128 snapshot. The current
records, including this review, are due in checkpoint74 at the
same 22:34:24 boundary. No packaging or input preparation is counted
as progress.

Closed required identities at Review51: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Next review: 2026-11-24T23:34:24+00:00.
Next checkpoint after74: 2026-11-24T23:19:24+00:00.
This review refreshes no inventory or census and creates no edit
manifest, seal, receipt, rebinding or derived-file copy.
'''
for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
    p=ROOT/name
    prior=p.read_text()
    assert '\n## Review 51 — ' not in prior
    p.write_text(prior+note,newline='\n')
print(f'Review51: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}')
print('Newly completed: '+', '.join(new))
print('Released comparisons open: '+', '.join(pending))
print('Recorded UTC: '+now.isoformat())
