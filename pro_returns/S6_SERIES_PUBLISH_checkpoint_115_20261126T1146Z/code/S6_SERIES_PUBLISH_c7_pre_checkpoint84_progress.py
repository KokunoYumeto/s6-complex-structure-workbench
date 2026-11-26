#!/usr/bin/env python3
"""Record current incomplete fresh-reading states without closure credit."""
import csv
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv'
with path.open(newline='') as f:
    reader = csv.DictReader(f,delimiter='\t')
    fields,rows = reader.fieldnames,list(reader)
bytag = {r['tag']:r for r in rows}
lf = bytag['02LF']
assert lf['status'] == 'open' and lf['proof_status'] == 'embargoed'
fresh = 'agents/continuation7_iii_three_primary/S6_SERIES_PUBLISH_III_02LF_fresh_derivation.md'
digest = 'a882ffccd0d1daf7fa6c50f7e67924bec72e12bc1c60ec7acc9c9c9f246b5bb2'
assert sha256((ROOT/fresh).read_bytes()).hexdigest() == digest
lf.update(packet_status='fresh_frozen_awaiting_complete_root_review',
          derivation_path=fresh,derivation_sha256=digest,
          derivation_completed_utc='2026-11-25T06:01:00Z')
lf['notes'] += ' Checkpoint84 state: KS froze the complete1408-line proof at06:01 UTC with full C9 operation and all parameters. All lane source/output readings are complete; root complete review remains pending. Original stays closed to KS.'
for tag,status,note in [
 ('02LI','fresh_complete_draft_final_readback_pending',
  'Complete1112-line draft and successful4002-global-presentation ordered-word computation saved; final source/data/proof readback and freeze remain pending. Original stays closed.'),
 ('02LK','fresh_complete_draft_final_readback_pending',
  'Complete768-line general-lattice draft and139-lattice computation saved; final reread and freeze remain pending. Admitted bounded KB charts are disclosed. Root one-sentence dependency spill is recorded separately; independent checker remains unexposed.'),
]:
    r = bytag[tag]
    assert r['status'] == 'open' and r['proof_status'] == 'embargoed'
    r['packet_status'] = status
    r['notes'] += ' Checkpoint84 state: '+note
with path.open('w',newline='') as f:
    writer = csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n')
    writer.writeheader();writer.writerows(rows)
print('UPDATED LF,LI,LK incomplete fresh-reading states at',datetime.now(timezone.utc).isoformat())
print('REQUIRED_DONE',sum(r['status']=='done' for r in rows),'OF',len(rows))
print('NO required closure, original release or unit credit from this status record')
