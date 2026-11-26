"""Record the scheduled third hourly review of continuation five."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import csv,re

ROOT=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
due=datetime(2026,11,23,21,26,17,tzinfo=timezone.utc)
assert now>=due,'Review38 is not yet due.'
ledger=ROOT/'PROGRESS_LEDGER.md'
previous=re.search(r'^## Review 37 — ([^\n]+)',ledger.read_text(),re.M)
assert previous
last=datetime.fromisoformat(previous[1])
def table(path):
    with path.open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
rows=table(ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv')
events={e['event_id']:e for e in table(ROOT/'CHECK_EVENTS.tsv')}
closed=[r for r in rows if r['status']=='done']
assert len(rows)==128
new=[r for r in closed if datetime.fromisoformat(events[r['check_event_id']]['date_utc'].replace('Z','+00:00'))>last]
assert new
assert all(r['check_event_id'] and r['proof_comparison_evidence'] and r['derivation_completed_utc'] for r in closed)
units=table(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
open_units=Counter(r['paper'] for r in units if r['status']=='open')
pending=[r['tag'] for r in rows if r['status']=='open' and r['proof_status']=='released_after_derivation']
note=f'''
## Review 38 — {now.isoformat()}

INCOMPLETE. The scheduled21:26:17 UTC review records qualifying movement
since Review37: {len(new)} further existing Paper III required rows closed,
namely {', '.join(r['tag'] for r in new)}. Paper III is at
{len(closed)}/128 required checks, with {128-len(closed)} open. Each closed
row has a complete written fresh derivation and new computation before
individual proof release, full printed/receiving comparison, and its
admitted event. The separate 02KD dependency check receives no movement
credit in this table.

The additional work establishes the torus/smoothing and finite-family
comparisons in the admitted packets. The Yang all-order check uses exact
inverse maps between its two-generator and three-generator presentations,
the complete relative kernels for both P cases, and constructive checks
of every historical computational input. The circle-quotient comparison
includes the natural exact sequence of integral local systems. All
publication repairs are queued in exact guards; no III source is edited.

The three separate cover arguments 037X,037Y,0382 were released only after
all three fresh derivations and new programs/outputs were read. Their
actual theorem/paragraph scopes are bound individually; the historical
metadata group gives no alias credit. Released comparisons still open:
{', '.join(pending) or 'none'}. LY remains proof-closed pending root review
of the frozen derivation and the explicit pre-exposure local divisor-sign
correction. LZ remains in fresh derivation. These unfinished states are
not credited as completed required checks.

Every required-row status remains in
S6_SERIES_PUBLISH_required_progress_III.tsv; every unit-row status remains
in S6_SERIES_PUBLISH_unit_progress.tsv. Open unit counts are
{dict(open_units)}. All756 III unit criteria remain open. Its manuscript
SHA256 is still9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0.
The unit restructuring/defect-removal, provenance, clean-build, typesetting
and full final-page readings retain their open gates. Paper IV's66 checks
and729 unit criteria await III. The main question remains completion of
all five publication-ready papers.

Current I and V remain closed until the joint step; bounded cached-I
inputs receive no fresh-I credit. II retains its final gate; E.5.2 and
E.5.3 remain unchanged. Every III/IV use of refined II02Y6/02XE still
requires the recorded downstream scope check. Joint D26/later-defect
application, series references, notation, deposit fields, records tables
and the first-part readings retain their own pending states. Root's
incidental target exposures are recorded, including the KA proof opened
only to separate its construction data, and the few036A locator lines;
their unexposed checkers own the fresh derivations.

Consecutive reviews without qualifying movement:0. Review39 is due
2026-11-23T22:26:17+00:00. Checkpoint56 is due at this review boundary;
checkpoint57 is due2026-11-23T22:11:17+00:00. Packaging and source retrieval
count as no movement. No inventory, census, manifest or derived-file copy
is produced by this review.
'''
for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
    path=ROOT/name;old=path.read_text();assert '\n## Review 38 — ' not in old
    path.write_text(old+note,newline='\n')
print(f'Review38: {len(closed)}/128 required rows done; {len(new)} new since Review37; no-movement count0.')
print('Newly completed:',', '.join(r['tag'] for r in new))
