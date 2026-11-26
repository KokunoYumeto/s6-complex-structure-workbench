"""Scheduled lean checkpoints; no edit-level inventory or manifest refresh."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import argparse
import csv
import hashlib
import io
import os
import zipfile

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
DEST=BASE.parent
START=datetime(2026,11,22,16,56,58,tzinfo=timezone.utc)
parser=argparse.ArgumentParser()
parser.add_argument('number',type=int)
parser.add_argument('notes_file',type=Path)
args=parser.parse_args()
assert args.number>=36
due=START+timedelta(minutes=45*(args.number-35))
stamp=datetime.now(timezone.utc)
assert stamp>=due, f'Checkpoint is not due until {due.isoformat()}'
stem=f'S6_SERIES_PUBLISH_checkpoint_{args.number:02}'
destination=DEST/(stem+'.zip')
assert not destination.exists(), 'Never overwrite an earlier checkpoint.'
heading=f'## Checkpoint {args.number:02} — {stamp.isoformat()}'
notes=args.notes_file.read_text().strip()
section='\n\n'+heading+'\n\n'+notes+'\n'
for filename in ['S6_SERIES_PUBLISH_report.md','PROGRESS_LEDGER.md']:
    path=ROOT/filename
    assert f'## Checkpoint {args.number:02} — ' not in path.read_text()
    with path.open('a',newline='\n') as handle:
        handle.write(section)

with (BASE/'BASE_FILELIST.tsv').open(newline='') as handle:
    baseline={row['path']:row for row in csv.DictReader(handle,delimiter='\t')}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def stable_bytes(path):
    for _ in range(3):
        first=path.stat()
        data=path.read_bytes()
        last=path.stat()
        if (first.st_size,first.st_mtime_ns)==(last.st_size,last.st_mtime_ns):
            return data
    raise RuntimeError(f'File changed during checkpoint read: {path}')

candidates=[]
for path in ROOT.iterdir():
    if path.is_file() and (
        path.name.startswith('S6_SERIES_PUBLISH') or
        path.name in ['CHECK_EVENTS.tsv','PROGRESS_LEDGER.md','S6_DEFECT_REGISTER.csv']):
        candidates.append(path)
for folder in [ROOT/'code']+sorted((ROOT/'agents').glob('continuation3*')):
    candidates.extend(path for path in folder.rglob('*') if path.is_file())

staged={}
excluded_suffixes={'.zip','.pdf','.png','.jpg','.jpeg','.webp','.gif','.pyc','.aux','.toc','.log','.nav','.snm'}
for path in sorted(set(candidates)):
    relative=path.relative_to(ROOT).as_posix()
    if '__pycache__' in path.parts or path.suffix.lower() in excluded_suffixes:
        continue
    # Finished comparison snapshots are reproducible from the base, manuscript
    # and mandatory defect rows; the active construction comparison stays.
    if '_P244_' in path.name and (path.name.endswith('_input.tex') or path.name.endswith('_receiving.tex')):
        continue
    data=stable_bytes(path)
    old=baseline.get(ROOT.name+'/'+relative)
    if old and int(old['size'])==len(data) and old['sha256']==digest(data):
        continue
    staged[relative]=data

readme=f"""# {stem}

INCOMPLETE — continuing Paper II.

Scheduled time: {due.isoformat()}.
Snapshot time: {stamp.isoformat()}.

Restore the supplied base archive once and verify it with restore_cp35.py.
Overlay this folder's files, preserving their relative paths, onto the merged
S6_SERIES_PUBLISH_checkpoint_35 working directory. Do not replace the base
directory wholesale: unchanged base files are intentionally omitted here.
The base plus this newest checkpoint restore the recorded working state.

Read the last report and ledger sections, then continue Paper II. Papers III
and IV follow in that order; the completed I/V gates stay closed until the
five-together step. The newest central TeX and tables are authoritative.
Agent fragments are preparation or comparison material; their admission
state is described by the report and corresponding code outputs.

The file list gives the size and SHA-256 of every payload except itself.
This checkpoint contains no earlier ZIP, unchanged base copy, downloaded
published work, extracted published text, rendered page image or provisional
PDF. The working-build log summary and bounded page-reading record remain.
Final PDF delivery and complete rendered-page reading are still pending.

Next checkpoint: {(due+timedelta(minutes=45)).isoformat()}.
Next hourly review remains on the hourly schedule from {START.isoformat()}.
"""
staged[stem+'_README.md']=readme.encode()
output_path=ROOT/'code'/f'S6_SERIES_PUBLISH_c3_checkpoint_{args.number:02}.out'
output=f'Scheduled checkpoint {args.number:02}\nDue: {due.isoformat()}\nSnapshot: {stamp.isoformat()}\nPayload files before this output and filelist: {len(staged)}\nUnchanged base files, published-source copies and page images excluded.\n'
output_path.write_text(output,newline='\n')
staged[output_path.relative_to(ROOT).as_posix()]=output.encode()
table=io.StringIO(newline='')
writer=csv.writer(table,delimiter='\t',lineterminator='\n')
writer.writerow(['path','size','sha256'])
for relative,data in sorted(staged.items()):
    writer.writerow([relative,len(data),digest(data)])
staged[stem+'_filelist.tsv']=table.getvalue().encode()
temporary=DEST/(stem+'.building')
assert not temporary.exists()
with zipfile.ZipFile(temporary,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
    for relative,data in sorted(staged.items()):
        archive.writestr(stem+'/'+relative,data)
assert temporary.stat().st_size<500_000_000
with zipfile.ZipFile(temporary) as archive:
    assert archive.testzip() is None
    for relative,data in staged.items():
        assert digest(archive.read(stem+'/'+relative))==digest(data),relative
os.link(temporary,destination)
temporary.unlink()
print(f'Verified scheduled checkpoint: {destination}')
print(f'Payload entries: {len(staged)}; ZIP bytes: {destination.stat().st_size}')
print('No edit-level derived-file refresh, independent check or progress-row closure is created by packaging.')
