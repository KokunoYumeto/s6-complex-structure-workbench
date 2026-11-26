"""Record the third scheduled hourly review of the fourth continuation."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import io
import zipfile

ROOT = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc)
due = datetime(2026, 11, 23, 13, 47, 46, tzinfo=timezone.utc)
assert stamp >= due, 'The scheduled review is not due.'
csv.field_size_limit(100000000)
with zipfile.ZipFile(ROOT.parents[1] / 'upload/S6_SERIES_PUBLISH_continue_cp44.zip') as archive:
    names = [n for n in archive.namelist() if n.endswith('S6_SERIES_PUBLISH_checkpoint_44/S6_SERIES_PUBLISH_unit_progress.tsv')]
    assert len(names) == 1
    initial = list(csv.DictReader(io.StringIO(archive.read(names[0]).decode()), delimiter='\t'))
with (ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv').open() as stream:
    current = list(csv.DictReader(stream, delimiter='\t'))
key = lambda row: (row['paper'], row['unit_id'], row['row_kind'], row['defect_type'])
index = {key(row): row for row in current}
closed = [row for row in initial if row['paper'] == 'II' and row['status'] == 'open' and index[key(row)]['status'] == 'done']
assert len(closed) == 982
open_units = Counter(row['paper'] for row in current if row['status'] == 'open')
assert open_units['II'] == 0
with (ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv').open() as stream:
    required = list(csv.DictReader(stream, delimiter='\t'))
assert len(required) == 128
done = [row for row in required if row['status'] == 'done']
assert all(row['check_event_id'] and row['proof_comparison_evidence'] for row in done)
identities = ', '.join(row['tag'] for row in done)
new_ii = len(closed) - 729
assert new_ii > 0
note = f'''
## Review 32 — {stamp.isoformat()}

INCOMPLETE. The scheduled 13:47:46 UTC review records qualifying movement:
{len(closed)} existing checkpoint-44 open Paper II unit criteria are now done,
{new_ii} more than the 729 at review 31. All 5,876 II unit criteria are done.
Paper III additionally has {len(done)} admitted fresh required checks out of
128, at the exact identities {identities}. Their live rows bind written
pre-exposure derivations, separately authorized full-proof releases, full
comparisons and admitted targeted-check events. New receiving rows,
packaging, extraction, hashing and source acquisition receive no movement
credit. Open unit criteria by paper: {dict(open_units)}.

Paper II's gate closed at 13:13:05 UTC. The final source and 787-page PDF
retain the complete actual image-reading chain, all 198 required-check
dispositions, completed visual-repair reviews, and the reconciled final
statement, defect, provenance and program records. The build has one
0.89041pt overfull box, none above 2pt, and no missing font or glyph,
undefined reference or citation, duplicate label or destination, rerun
request or unresolved fallback. Its source and deposit bind 3,391 event
associations in 2,804 evidence groups at the II closure ledger. Later
cross-paper events remain for the scheduled joint reconciliation.

Paper III is active. Its one live 128-row required-check table preserves
all original identities and records exact current source ownership;
metadata owner hints and alias groups receive no automatic proof credit.
{128-len(done)} required checks remain open. The completed carrier-extension
and three-complex checks derive the exact maps before comparing the full
printed proofs. Further finite-cover, relative-realization and stable-framing
checks are individually assigned. Written derivations or released proofs
receive no completion credit before comparison and root admission.

The main question remains five publication-ready papers. The current gate
is III's required checks, mathematical and editorial revision, source and
reference verification, and final visual reading; IV's 66 required checks
and unit criteria then follow, before the joint I–V step. I and V manuscripts
remain unopened. Closed-I statement-only cached inputs used for III are
identified separately from fresh proof evidence. The protected II E.5.2
and E.5.3 statement bytes remain exact. Every III/IV use of refined II
02Y6 and 02XE retains its explicit downstream recheck requirement.

Consecutive reviews without qualifying movement: 0. Review 33 is due
2026-11-23T14:47:46+00:00. Checkpoint 48 is due now,
2026-11-23T13:47:46+00:00. No per-edit inventory refresh, manifest, seal,
rebinding or derived-file copy is produced for this review.
'''
for name in ('PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md'):
    path = ROOT / name
    old = path.read_text()
    assert '\n## Review 32 — ' not in old
    path.write_text(old + note, newline='\n')
print(f'Review 32 recorded: {len(closed)} baseline II closures, {new_ii} since review31; {len(done)} admitted III required checks; no-movement count 0.')
