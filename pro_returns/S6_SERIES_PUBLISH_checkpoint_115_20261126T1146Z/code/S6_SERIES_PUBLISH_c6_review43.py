#!/usr/bin/env python3
"""First scheduled review of continuation six, against checkpoint62."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
assert now >= datetime(2026, 11, 24, 12, 15, 57, tzinfo=timezone.utc)
ledger = (ROOT / 'PROGRESS_LEDGER.md').read_text()
baseline = re.search(r'The qualifying-movement baseline is checkpoint 62\'s closed set:\n([^\n]+)\.', ledger)
assert baseline
previous = set(baseline[1].split(', '))
assert len(previous) == 68

def table(name):
    with (ROOT / name).open(newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

rows = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events = {r['event_id']: r for r in table('CHECK_EVENTS.tsv')}
closed = [r for r in rows if r['status'] == 'done']
tags = {r['tag'] for r in closed}
new = sorted(tags - previous)
reopened = sorted(previous - tags)
assert len(rows) == 128 and not reopened
for r in closed:
    assert r['check_event_id'] in events
    assert events[r['check_event_id']]['statement_id'] == r['label']
pending = sorted(r['tag'] for r in rows if r['status'] == 'open'
                 and r['proof_status'] == 'released_after_derivation')
units = Counter(r['paper'] for r in table('S6_SERIES_PUBLISH_unit_progress.tsv')
                if r['status'] == 'open')
sha = hashlib.sha256((ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert sha == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
no_movement = 0 if new else 1
note = f'''
## Review 43 — {now.isoformat()}

INCOMPLETE. The scheduled 12:15:57 UTC review records {len(new)} existing
required III rows changed to done since continuation six's checkpoint62
baseline: {', '.join(new) or 'none'}. The current total is {len(closed)}/128
complete, with {128-len(closed)} open. No identity reopened. The review uses
the 68 identities explicitly recorded at this continuation's start, so it
does not recount earlier work between Review42 and checkpoint62.

The admitted comparisons include the smooth logarithmic filling and its
integral homology, the full arbitrary-lattice toric cubic and characteristic
classes, the stable framing calculation, and the sphere-carrier smash maps.
The latter use the actual coordinate permutations, pinch maps and typed
suspensions. Each admitted identity has its saved pre-release derivation,
complete original-to-receiver comparison, exact guards, defects and event.
The KN comparison discloses a sign correction to its saved fresh negative
peripheral column; it does not refute the original theorem. Its final m>1
sentence now explicitly carries the preceding n=±1 scope. The OS49 initial
root-action extraction was corrected before its proof releases. Neither
correction is counted as an extra completed row.

Individually released comparisons still open: {', '.join(pending) or 'none'}.
The finite-cap derivation now includes the explicit modular period paths
and covering maps; the original-to-receiver comparison is in progress.
The D.2 oriented smooth classification and the framed nullbordism are being
derived from their actual actions, embeddings and ordered frames. Saved
partial derivations and released originals receive no closure credit.

Every required-row status is retained in
S6_SERIES_PUBLISH_required_progress_III.tsv and
S6_SERIES_PUBLISH_required_progress_IV.tsv. Every unit-row status is retained
in S6_SERIES_PUBLISH_unit_progress.tsv. Open unit counts: {dict(units)}.
All 756 III unit criteria remain open. No repair has been applied to the
III manuscript; its SHA256 remains {sha}.

The main question remains all five publication-ready papers. Its current
gate is completion of III's remaining required checks, followed by its unit
restructuring and all defects, provenance and links, clean pdfLaTeX build,
typesetting check and every rendered-page reading. Next come IV's 66
required checks, 729 unit criteria and all publication gates, followed by
the joint series work. Each outstanding provenance claim, build and final
page remains open; no new final candidate PDF has been certified.

I and V remain at their published closed gates until the joint step. II
remains final, with E.5.2/E.5.3 unchanged. Every III/IV use of refined
II02Y6/02XE still requires its downstream scope check. Joint D26 and later
defect applications, cross-references, notation, deposit fields, records
tables, page concordances and final first-part readings remain open.

Closed required identities at Review43: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Review44 is due 2026-11-24T13:15:57+00:00. Checkpoint63 was delivered at its
scheduled boundary; checkpoint64 is due 2026-11-24T12:45:57+00:00.
Packaging is no movement. This review creates no inventory, census,
manifest, seal or derived-file copy.
'''
for name in ['PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md']:
    path = ROOT / name
    current = path.read_text()
    assert '\n## Review 43 — ' not in current
    path.write_text(current + note, newline='\n')
print(f'Review43: {len(closed)}/128 done; {len(new)} new closures since checkpoint62; no-movement count {no_movement}.')
print('Newly completed:', ', '.join(new))
print('Open released comparisons:', ', '.join(pending))
