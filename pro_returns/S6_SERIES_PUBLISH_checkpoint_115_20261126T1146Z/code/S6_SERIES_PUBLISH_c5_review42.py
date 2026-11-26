#!/usr/bin/env python3
"""Scheduled Review42, compared with the identities closed at Review41."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
assert now >= datetime(2026, 11, 24, 1, 26, 17, tzinfo=timezone.utc)
ledger = (ROOT / 'PROGRESS_LEDGER.md').read_text()
baseline = re.search(r'^Closed required identities at Review41: (.+)\.$', ledger, re.M)
assert baseline
previous = set(baseline[1].split(', '))
assert len(previous) == 62

def table(name):
    with (ROOT / name).open(newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

rows = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events = {r['event_id']: r for r in table('CHECK_EVENTS.tsv')}
closed = [r for r in rows if r['status'] == 'done']
tags = {r['tag'] for r in closed}
new = sorted(tags - previous)
reopened = sorted(previous - tags)
assert len(rows) == 128 and new and not reopened
for r in closed:
    assert r['check_event_id'] in events
    assert events[r['check_event_id']]['statement_id'] == r['label']
pending = sorted(r['tag'] for r in rows if r['status'] == 'open'
                 and r['proof_status'] == 'released_after_derivation')
units = Counter(r['paper'] for r in table('S6_SERIES_PUBLISH_unit_progress.tsv')
                if r['status'] == 'open')
sha = hashlib.sha256((ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert sha == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
note = f'''
## Review 42 — {now.isoformat()}

INCOMPLETE. The scheduled 01:26:17 UTC review records qualifying movement
since Review41: {len(new)} existing required III rows changed to done,
namely {', '.join(new)}. The live total is {len(closed)}/128 complete,
with {128-len(closed)} open. The comparison uses the actual closed-identity
set recorded at Review41. No identity reopened. Proposed events and
unadmitted comparisons provide no closure credit.

The completed comparisons include the quotient-carrier construction,
the explicit cusp polydisc and its torus fibre, and the open-cell
corollary. The cusp chart uses literal holomorphic inverse maps, a
single quantitatively injective deck-quotient neighborhood, and the
exact phase map onto its torus fibre. The open-cell argument supplies
the quotient-coordinate inverses, radial outside points, the full
closure and the entire intrinsic-ball isometries. Each admitted identity
has its complete pre-release derivation and new computation, complete
original-to-replacement comparison, exact guards, defects and event.
No rewrite has yet been applied to the III manuscript.

Individually released comparisons still open: {', '.join(pending) or 'none'}.
The seven-family elliptic argument now has certified maps from its
actual complex models to the marked peripheral systems, a section
class map, and an explicit divisor-line/circle isomorphism with local
component signs and the narrow-section integer framing. Its final
receiving-text comparison is still being read before admission.
The repeated-smash comparison is undergoing its final endpoint and
single-proof presentation corrections. The smooth logarithmic-filling
fresh check remains proof-closed and its actual semistable models are
still being completed. These pending steps receive no closure credit.

Every required-row status is in S6_SERIES_PUBLISH_required_progress_III.tsv,
and every unit-row status is in S6_SERIES_PUBLISH_unit_progress.tsv.
Open unit counts: {dict(units)}. All756 III unit criteria remain open.
The unchanged III source SHA256 is {sha}.
The main question remains all five publication-ready papers. Its gates
remain III's required checks, unit restructuring and defect removal,
provenance, clean build, typesetting and every final rendered-page reading;
then IV's66 required checks and729 unit criteria and publication gates;
then the joint series work.

I and V remain closed until the joint step. Bounded older-I construction
inputs receive no I credit. II remains final, with E.5.2/E.5.3 unchanged.
Every III/IV use of refined II02Y6/02XE still requires its downstream
scope check. Joint D26/later-type applications, cross-references, notation,
deposit fields, records tables and final first-part readings remain open.

Closed required identities at Review42: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement:0. Review43 is due
2026-11-24T02:26:17+00:00. Checkpoint61 was delivered on its scheduled
boundary; checkpoint62 is due2026-11-24T01:56:17+00:00.
Packaging is no movement. This review produces no inventory, census,
manifest, seal or derived-file copy.
'''
for name in ['PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md']:
    path = ROOT / name
    current = path.read_text()
    assert '\n## Review 42 — ' not in current
    path.write_text(current + note, newline='\n')
print(f'Review42: {len(closed)}/128 done; {len(new)} new closures since41; no-movement count0.')
print('Newly completed:', ', '.join(new))
print('Open released comparisons:', ', '.join(pending))
