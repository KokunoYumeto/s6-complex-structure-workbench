"""Close the Paper II gate after the reviewed final unit-closure admission."""
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import io
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
units = list(csv.DictReader((ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv').open(), delimiter='\t'))
ii = [r for r in units if r['paper'] == 'II']
assert ii and all(r['status'] == 'done' for r in ii)
provenance = list(csv.DictReader((ROOT / 'S6_SERIES_PUBLISH_provenance_checks.tsv').open(), delimiter='\t'))
assert sum(r['paper'] == 'II' for r in provenance) == 51
assert all(r['resolution_status'].startswith('done: current Paper II provenance claim checked')
           for r in provenance if r['paper'] == 'II')
source = ROOT / 'S6_SERIES_PUBLISH_II.tex'
pdf = ROOT / 'build/II_c4_final_v3/S6_SERIES_PUBLISH_II.pdf'
source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
pdf_hash = hashlib.sha256(pdf.read_bytes()).hexdigest()
assert source_hash == '106fcde4a73b9d94f7bd328d05d517bb1c3813ca190bf253258ccf1bce5aa844'
assert pdf_hash == 'b31d78f93b0d96315575d1053cd55ff3b5ec0e6427756e62e9628733f0c7c058'
reading = (ROOT / 'S6_SERIES_PUBLISH_reading_II.md').read_text()
assert 'Final-candidate status: complete.' in reading.split('\n\n', 2)[1]
assert source_hash in reading and pdf_hash in reading
build = (ROOT / 'code/S6_SERIES_PUBLISH_c4_final_v3_build.out').read_text()
assert build.count('exit 0') == 3
for line in ('Overfull boxes: 1 ; exceeding 2pt: 0', 'undefined references/citations: 0',
             'missing glyphs: 0', 'missing fonts: 0', 'multiply defined labels: 0',
             'duplicate destinations: 0', 'rerun requests: 0',
             'rendered unresolved-reference fallback pages: 0'):
    assert line in build
finish = (ROOT / 'code/S6_SERIES_PUBLISH_c4_final_derive_II.out').read_text()
for line in ('Existing II provenance rows reconciled: 51',
             'Preserved Paper II required-check dispositions: 198',
             'Statement-associated event count: 3391', 'Exact program records: 159'):
    assert line in finish
archive = ROOT.parents[1] / 'upload/S6_SERIES_PUBLISH_continue_cp44.zip'
with zipfile.ZipFile(archive) as z:
    names = [n for n in z.namelist() if n.endswith('S6_SERIES_PUBLISH_checkpoint_44/S6_SERIES_PUBLISH_unit_progress.tsv')]
    assert len(names) == 1
    baseline = list(csv.DictReader(io.StringIO(z.read(names[0]).decode()), delimiter='\t'))
key = lambda r: (r['paper'], r['unit_id'], r['row_kind'], r['defect_type'])
current = {key(r): r for r in units}
closed = sum(r['paper'] == 'II' and r['status'] == 'open' and current[key(r)]['status'] == 'done'
             for r in baseline)
stamp = datetime.now(timezone.utc).isoformat()
title = '## Paper II gate closed — '
for name in ('S6_SERIES_PUBLISH_report.md', 'PROGRESS_LEDGER.md'):
    assert title not in (ROOT / name).read_text()
destination = ROOT / 'S6_SERIES_PUBLISH_II.pdf'
shutil.copyfile(pdf, destination)
assert hashlib.sha256(destination.read_bytes()).hexdigest() == pdf_hash
note = f'''
{title}{stamp}

INCOMPLETE for the five-paper task. Paper II is complete at its paper gate.
All {len(ii):,} II unit criteria are done, including the last 211 D23 rows and
five Methodology rows. Relative to checkpoint 44, {closed} existing open II
unit criteria have closed; newly introduced rows receive no baseline credit.
The canonical reading supplies actual image evidence for every physical page
1–787. The final build has one 0.89041pt overfull box and none above 2pt,
with no undefined reference/citation, missing font/glyph, duplicate label or
destination, or rerun request. All 50 final visual-repair statuses now point
to that completed reading. The final defect concordance has 11,694 explicit
dispositions and zero unresolved rows; historical old_page bytes are retained.

The single final derived pass preserves all 198 required-check dispositions,
including the historical false-as-stated 02UH claim and its exact retained
resolution owner. It records 482 current owners, 545 retained statement
identifiers, 3,391 event associations in 2,804 evidence groups, 159 program paths
(87 current code and 72 historical repository paths), and 51 reconciled II
provenance claims. Source and deposit agree. No independent proof or source
reading was inferred from final record reconciliation or page correspondence.

The admitted UN63 proof repair replaces its nonholomorphic logarithm assertion
with the explicit holomorphic exponential multiplier. The separate protected
statements push:src:E.5.2 and push:src:E.5.3 retain their original bytes under
the recorded exact admission guards. The earlier refined statements 02Y6 and
02XE remain the authoritative inputs for the coming III/IV application checks.

Final II source SHA-256: {source_hash}.
Final II PDF SHA-256: {pdf_hash}.
The validated PDF is now S6_SERIES_PUBLISH_II.pdf. Its mathematical comparisons,
source readings, defect rows and canonical page log retain their actual scopes.

Paper III now begins with its 128 required checks; Paper IV's 66 checks follow
only after III is complete. The final joint step still covers I–V references,
notation, series tables, final records/deposit fields and every first part.
I and V manuscripts have not been reopened for that step. The next progress
review remains due 13:47:46 UTC and the next timed checkpoint is 48 at the same
time. No extra checkpoint is created at this paper boundary.
'''
for name in ('S6_SERIES_PUBLISH_report.md', 'PROGRESS_LEDGER.md'):
    path = ROOT / name
    previous = path.read_text()
    if name.endswith('report.md'):
        assert previous.startswith('INCOMPLETE')
    path.write_text(previous + note, newline='\n')
print('Paper II gate closed at', stamp)
print('II unit criteria done:', len(ii), '; baseline open criteria closed:', closed)
print('Validated deliverable PDF:', destination)
print('Next active paper: III; 128 required checks. IV and the joint step remain.')
