"""Record the fourth hourly review of continuation five."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
assert now >= datetime(2026, 11, 23, 22, 26, 17, tzinfo=timezone.utc)
ledger = (ROOT / 'PROGRESS_LEDGER.md').read_text()
previous = re.search(r'^## Review 38 — ([^\n]+)', ledger, re.M)
assert previous
last = datetime.fromisoformat(previous[1])

def table(path):
    with path.open(newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

rows = table(ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv')
events = {e['event_id']: e for e in table(ROOT / 'CHECK_EVENTS.tsv')}
closed = [r for r in rows if r['status'] == 'done']
new = [r for r in closed if datetime.fromisoformat(
    events[r['check_event_id']]['date_utc'].replace('Z', '+00:00')) > last]
assert len(rows) == 128 and new
units = table(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
open_units = Counter(r['paper'] for r in units if r['status'] == 'open')
pending = [r['tag'] for r in rows if r['status'] == 'open'
           and r['proof_status'] == 'released_after_derivation']
source_sha = hashlib.sha256((ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert source_sha == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
note = f'''
## Review 39 — {now.isoformat()}

INCOMPLETE. The scheduled22:26:17 UTC review records qualifying movement
since Review38: {len(new)} further existing required III rows closed,
namely {', '.join(r['tag'] for r in new)}. Paper III has
{len(closed)}/128 required checks complete and {128-len(closed)} open.
Every credited closure has its full written fresh derivation and new
computation before individual proof release, complete old/new comparison,
and admitted check event. The separate02KD dependency retains no movement
credit in this table.

The admitted cover comparisons specify the parameter discs, maximal
triangle orbits, local-system obstruction and exact descent defect.
The canonical cyclic-action comparison includes the exact covering maps,
toric unit, quotient inverses and deck equivariance, including d=1.
The target-homotopy check realizes the two wedge decompositions by based
maps and inverse homotopies; exact loop words and null surjective quotient
maps prove the scope of its ordinary invariants. All corresponding
publication repairs remain in their guarded packets.

Individually released comparisons still open: {', '.join(pending) or 'none'}.
The metric-scope fresh derivation constructs a fixed compatible ambient
metric agreeing with any chosen finite slice, while proving uniform
ambient collapse and intrinsic expansion. Its comparison remains open
until its entire receiving text and event are admitted. The D2 lane has
raw defining matrices for KM with the target proof closed. The finite
checker owns fresh037N: root found an argument inside the old purported
statement-only definition packet and recorded that exposure; a separate
input packet withholds that argument. None of these pending states
receives completion credit.

Every required-row status is in S6_SERIES_PUBLISH_required_progress_III.tsv;
every unit-row status is in S6_SERIES_PUBLISH_unit_progress.tsv.
The open unit counts are {dict(open_units)}. All756 III unit criteria
remain open. The III manuscript SHA256 is {source_sha}.
Unit restructuring and defect removal, provenance, clean build,
typesetting and every final rendered-page reading remain open gates.
IV's66 checks and729 unit criteria await III. The main question remains
completion of all five publication-ready papers.

Current I and V remain closed until the joint step. Bounded cached-I
inputs carry no new I credit. II retains its final gate; E.5.2/E.5.3
remain unchanged. Every III/IV use of refined II02Y6/02XE still requires
its downstream scope check. Joint D26/later-type application, references,
notation, deposit fields, records tables and the final first-part readings
retain their own pending rows.

Consecutive reviews without qualifying movement:0. Review40 is due
2026-11-23T23:26:17+00:00. Checkpoint57 was saved on the22:11 boundary;
checkpoint58 is due2026-11-23T22:56:17+00:00. Packaging, source retrieval
and the unadmitted calculations count as no movement. No inventory,
census, manifest, seal or derived-file copy is produced by this review.
'''
for name in ['PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md']:
    path = ROOT / name
    text = path.read_text()
    assert '\n## Review 39 — ' not in text
    path.write_text(text + note, newline='\n')
print(f'Review39: {len(closed)}/128 done; {len(new)} new since38; no-movement count0.')
print('Newly completed:', ', '.join(r['tag'] for r in new))
