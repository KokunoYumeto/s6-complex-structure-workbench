"""Create one scheduled lean checkpoint relative to the attached base.

The file list belongs to this checkpoint, never to an edit. Unchanged base
bytes, outside sources, derived-file diffs, caches and rendered pages stay out.
"""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv
from collections import Counter
import hashlib
import io
import re
import sys
import zipfile
from S6_SERIES_PUBLISH_c4_derive_II import current_data

ROOT = Path(__file__).resolve().parents[1]
number = int(sys.argv[1])
stamp = datetime.now(timezone.utc)
assert number>=45
due = datetime(2026,11,23,10,47,46,tzinfo=timezone.utc)+timedelta(minutes=45*(number-44))
if stamp < due:
    raise SystemExit(f'Checkpoint {number} is scheduled for {due.isoformat()}; continue manuscript work until then.')
stem = f'S6_SERIES_PUBLISH_checkpoint_{number:02d}'
destination = ROOT.parents[1] / (stem + '.zip')
if destination.exists():
    raise SystemExit('The checkpoint already exists; never overwrite a checkpoint.')
csv.field_size_limit(10000000)
with (ROOT.parent / 'BASE_FILELIST.tsv').open() as f:
    base_hashes = {r['sha256'] for r in csv.DictReader(f, delimiter='\t')}

# Compare existing ledger identities with the attached baseline in memory.
# This reads the original table without unpacking or copying the base again.
base_archive=ROOT.parents[1]/'upload/S6_SERIES_PUBLISH_continue_cp44.zip'
with zipfile.ZipFile(base_archive) as z:
    names=[n for n in z.namelist() if n.endswith('S6_SERIES_PUBLISH_checkpoint_44/S6_SERIES_PUBLISH_unit_progress.tsv')]
    assert len(names)==1,names
    initial=list(csv.DictReader(io.StringIO(z.read(names[0]).decode()),delimiter='\t'))
with (ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv').open() as f:
    current=list(csv.DictReader(f,delimiter='\t'))
key=lambda r:(r['paper'],r['unit_id'],r['row_kind'],r['defect_type'])
index={key(r):r for r in current}
initial_keys={key(r) for r in initial}
stable_closed=sum(r['paper']=='II' and r['status']=='open' and key(r) in index and index[key(r)]['status']=='done' for r in initial)
new_unit_rows=sum(key(r) not in initial_keys for r in current)
open_units=Counter(r['paper'] for r in current if r['status']=='open')
active=next((p for p in ('II','III','IV') if open_units[p]),'joint I–V step')
phase=f'Paper {active} is active.' if active!='joint I–V step' else 'The final joint I–V step is active.'
remaining=('The final 787-page image reading is complete. The remaining II criteria '
           'are exactly the open rows of the unit table and their stated final-record gates.'
           if open_units['II'] else
           'Paper II has no open unit criteria; its final image reading, derived records and '
           'provenance reconciliation are complete. The current III/IV required-check and unit '
           'rows retain their exact individual states.')
if (ROOT/'S6_SERIES_PUBLISH_new_defect_applications.tsv').exists():
    remaining += (' The dated II closure concerns the original 25-type register. '
                  'New D26 statement-scope applications remain explicit open gates '
                  'for all five papers; the II, I and V applications await the joint step. '
                  'No historical closure is treated as a completed D26 application.')
reviews=re.findall(r'(?m)^## Review (\d+) — (.+)$',(ROOT/'PROGRESS_LEDGER.md').read_text())
last_review,last_review_time=reviews[-1]
next_review=datetime(2026,11,23,10,47,46,tzinfo=timezone.utc)+timedelta(hours=int(last_review)-28)
latest_build=max((ROOT/'code').glob('S6_SERIES_PUBLISH_c4_final*_build.out'),key=lambda p:p.stat().st_mtime,default=None)
build=latest_build.read_text() if latest_build else 'Final build pending.'
count_data=current_data()
count_note=(f"The methodology and deposit currently agree at {len(count_data['selected']):,} exact event associations in {len(count_data['groups']):,} evidence groups."
            if open_units['II'] else
            'The closed Paper II source and deposit record 3,391 event associations in 2,804 evidence groups at their final II ledger binding. Later cross-paper events will be reconciled at the scheduled joint step.')
page_status=(ROOT/'S6_SERIES_PUBLISH_reading_II.md').read_text().split('\n\n',2)[1]
required_notes=[]
for paper in ('III','IV'):
    path=ROOT/f'S6_SERIES_PUBLISH_required_progress_{paper}.tsv'
    if path.exists():
        with path.open() as stream:
            required_rows=list(csv.DictReader(stream,delimiter='\t'))
        states=Counter(r['status'] for r in required_rows)
        completed=[r['tag'] for r in required_rows if r['status']=='done']
        named=', '.join(completed) if len(completed)<=12 else f'{len(completed)} exact tag rows in {path.name}'
        required_notes.append(f'{paper}: {states["done"]} required checks done, {states["open"]} open; completed identities: {named or "none"}.')
required_note=' '.join(required_notes) or 'Required III/IV checks remain at their preceding recorded states.'

note = f'''\n## Checkpoint {number:02d} — {stamp.isoformat()}

INCOMPLETE. {phase} Paper II conductor stages 18–21, the full
horizontal/interface and reduction packages, main C, all A–G outline comparisons,
seven-part placement, the reader routes and the bibliography source/locus review
are admitted. Relative to the actual checkpoint-44 ledger, {stable_closed} existing
open II unit criteria are now done. The {new_unit_rows} subsequently introduced
rows receive no baseline movement credit. Exact row evidence remains in the unit
table. The protected E.5.2/E.5.3 statements retain their exact bytes.

The found nonholomorphic-logarithm assertion in UN63 is repaired by its explicit
holomorphic exponential multiplier. The final counts use actual current owners
and verified retained statement aliases, preserving all 198 completed required
checks and their exposure scopes. {count_note} No new independent derivation
was inferred from a source, label or page check. Six obsolete printed
bibliography entries were removed with individual reasons; their histories remain.

The build exposed and corrected recursive/multiple equation-label calls, three
late split-display alias installations and one 12.1012pt-wide display, retaining
every mathematical expression and target. The latest build output is
{str(latest_build.relative_to(ROOT)) if latest_build else 'pending'}. Current page status: {page_status}

{remaining} Open unit criteria by paper: {dict(open_units)}.
{required_note}
I and V retain their gates and wait for the final joint step. The latest dated
progress review is {last_review}, recorded {last_review_time}; its exact movement
and no-movement count are in the ledger. The next review is due {next_review.isoformat()}.
No per-edit
inventory refresh, manifest, seal or rebinding was made.
'''
for name in ('S6_SERIES_PUBLISH_report.md', 'PROGRESS_LEDGER.md'):
    p = ROOT / name
    text = p.read_text()
    if name.endswith('report.md') and not text.startswith('INCOMPLETE'):
        raise ValueError('The report must begin INCOMPLETE.')
    p.write_text(text + note, newline='\n')
readme = ROOT / (stem + '_README.md')
readme.write_text(f'''# {stem}

Status: INCOMPLETE. Created {stamp.isoformat()}.

Restore the attached base with its restore_cp44.py, then overlay this ZIP's
relative paths in S6_SERIES_PUBLISH_checkpoint_44/. This ZIP contains all needed
new or changed work since checkpoint 44; identical base bytes are omitted.
The current report, ledger, manuscript and defect/event/unit tables are the
records of admitted work. Prepared agent files are not admitted merely by
being present: consult those records and each admission program's output.

No published-source copies, extracted source text, prior archives, derived-file
diffs or rendered pages are included. Literature records contain locators,
hashes and original summaries. The file list gives byte size and SHA-256 for
every payload file; it excludes its own recursive hash. PDFs are withheld until
the final current build has passed the required rendering and page reading.

Current phase: {phase} Continue in the order II, III, IV, then the five together. The next
checkpoint is {number+1}, due {(due+timedelta(minutes=45)).isoformat()}. Do not reopen
I or V before the joint step. Existing statements push:src:E.5.2 and
push:src:E.5.3 remain protected; all III/IV uses of night:P4R.13 and night:P4.40
must be checked against their refined statements when those papers begin.
''', newline='\n')
output = ROOT / 'code' / f'S6_SERIES_PUBLISH_c4_checkpoint_{number:02d}.out'
output.write_text(f'Scheduled checkpoint {number:02d}: {stamp.isoformat()}\nRelative overlay against attached base; unchanged base hashes excluded.\nPayload SHA-256 and byte sizes are in {stem}_filelist.tsv.\n', newline='\n')

payload = []
for p in sorted(ROOT.rglob('*')):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT)
    if any(part in ('__pycache__', '.git', 'build', 'tex-runtime') for part in rel.parts):
        continue
    if p.suffix.lower()=='.pdf':
        if not (p.parent==ROOT and p.name in ('S6_SERIES_PUBLISH_II.pdf','S6_SERIES_PUBLISH_III.pdf','S6_SERIES_PUBLISH_IV.pdf')):
            continue
        paper=p.stem.rsplit('_',1)[-1]
        reading=(ROOT/f'S6_SERIES_PUBLISH_reading_{paper}.md').read_text()
        if 'Final-candidate status: complete' not in reading or hashlib.sha256(p.read_bytes()).hexdigest() not in reading:
            continue
    if p.suffix.lower() in ('.zip', '.png', '.jpg', '.jpeg', '.webp', '.pyc', '.aux', '.log', '.toc', '.orig', '.rej'):
        continue
    if '_filelist' in p.name or '_diff' in p.name or p.name.endswith('.diff'):
        continue
    if p.name == 'S6_SERIES_PUBLISH_c4_defect_concordance_plan.json':
        # This full derived preview is reproducible from the retained helper.
        continue
    if p.name.startswith('S6_SERIES_PUBLISH_checkpoint_') and p != readme:
        continue
    data = p.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest in base_hashes:
        continue
    if not (rel.parts[0] in ('code', 'agents', 'records') or len(rel.parts) == 1):
        raise ValueError(('Unreviewed payload location', str(rel)))
    payload.append((str(rel), len(data), digest, data))

listing = io.StringIO(newline='')
writer = csv.writer(listing, delimiter='\t', lineterminator='\n')
writer.writerow(('path', 'size', 'sha256'))
writer.writerows((p, n, h) for p, n, h, data in payload)
list_bytes = listing.getvalue().encode()
with zipfile.ZipFile(destination, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for name, size, digest, data in payload:
        z.writestr(name, data)
    z.writestr(stem + '_filelist.tsv', list_bytes)
if destination.stat().st_size >= 500_000_000:
    raise ValueError('Checkpoint requires parts before delivery.')
with zipfile.ZipFile(destination) as z:
    assert z.testzip() is None
    for name, size, digest, data in payload:
        actual = z.read(name)
        assert len(actual) == size and hashlib.sha256(actual).hexdigest() == digest
print(destination)
print('Payload files:', len(payload), 'plus checkpoint file list')
print('Payload bytes:', sum(n for p, n, h, data in payload))
print('Archive bytes:', destination.stat().st_size)
print('Archive SHA-256:', hashlib.sha256(destination.read_bytes()).hexdigest())
print('All payload sizes and hashes verified; no unchanged base file packed.')
