"""Freeze one full hourly checkpoint with exact lossless historical recipes.

Usage: python3 code/save_compact_checkpoint.py NN
The caller enforces the hourly schedule. No existing archive is changed.
All current deliverables are directly readable. Duplicate generated build
files share exact byte payloads, with every current path recorded and
restorable by the included current-tree restoration script. Every byte version held
by the preceding compact package is retained, and that exact ZIP can be
reconstructed and hash-verified. Legacy checkpoints1--9 remain restorable.
"""
from pathlib import Path
from datetime import datetime, timezone
import base64
import hashlib
import json
import shutil
import sys
import tempfile
import zipfile

project = Path(__file__).resolve().parents[1]
workspace = project.parent
number = int(sys.argv[1])
assert number >= 10
target = workspace / f'S6_03_CDP_checkpoint_{number:02d}.zip'
stage = workspace / f'checkpoint{number:02d}_compact' / 'contents'
if target.exists() or stage.exists():
    raise SystemExit('Refusing to replace an existing checkpoint or frozen tree.')
previous = (workspace / 'checkpoint09_compact' /
            'S6_03_CDP_checkpoint_09.zip') if number == 10 else (
            workspace / f'S6_03_CDP_checkpoint_{number-1:02d}.zip')
assert previous.is_file()
stamp = datetime.now(timezone.utc).isoformat()
with (project / 'records/checkpoints.md').open('a') as stream:
    stream.write(f'\n{number:02d}: {stamp}; full current project and research '
                 'support frozen. All historical byte versions retained with '
                 'exact archive reconstruction recipes; no preceding archive '
                 'changed. Supplied attachments excluded.\n')
stage.mkdir(parents=True)

def digest_path(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()

def metadata(info):
    out = {key: getattr(info, key) for key in [
        'filename', 'date_time', 'compress_type', 'create_system',
        'create_version', 'extract_version', 'reserved', 'flag_bits',
        'volume', 'internal_attr', 'external_attr']}
    out['extra'] = base64.b64encode(info.extra).decode()
    out['comment'] = base64.b64encode(info.comment).decode()
    return out

files = [(path, Path('S6_03_CDP') / path.relative_to(project))
         for path in sorted(project.rglob('*')) if path.is_file()]
for name in ['library_helpers_current', 'research_tmp', 'scratch_references']:
    directory = workspace / name
    if directory.exists():
        files.extend((path, Path('research_support') / name /
                      path.relative_to(directory))
                     for path in sorted(directory.rglob('*')) if path.is_file())
files.sort(key=lambda pair: (
    str(pair[1]).startswith('S6_03_CDP/build/'), str(pair[1])))
seen = {}
current = []
aliases = 0
for source, relative in files:
    destination = stage / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    digest = digest_path(destination)
    stored_path = seen.get(digest)
    is_build = str(relative).startswith('S6_03_CDP/build/')
    if is_build and stored_path is not None:
        destination.unlink()
        aliases += 1
    else:
        stored_path = str(relative)
        seen.setdefault(digest, stored_path)
    current.append({'path': str(relative), 'sha256': digest,
                    'size': source.stat().st_size,
                    'stored_path': stored_path,
                    'mode': source.stat().st_mode,
                    'mtime_ns': source.stat().st_mtime_ns})
print(f'Frozen current tree: {len(current)} files at {stamp}; '
      f'{aliases} duplicate build paths share verified payloads', flush=True)

prior_recipe = {'original_name': previous.name,
                'original_bytes': previous.stat().st_size,
                'original_sha256': digest_path(previous),
                'compression_level': 9, 'entries': []}
with zipfile.ZipFile(previous) as archive:
    legacy = json.loads(archive.read('history/snapshots.json'))
    if 'history/compact_snapshots.json' in archive.namelist():
        compacts = json.loads(archive.read('history/compact_snapshots.json'))
    else:
        compacts = {'format': 1, 'snapshots': {}}
    prior_recipe['comment'] = base64.b64encode(archive.comment).decode()
    for info in archive.infolist():
        path = Path(info.filename)
        if path.is_absolute() or '..' in path.parts or info.is_dir():
            raise ValueError('Unexpected or unsafe checkpoint member')
        data = archive.read(info)
        digest = hashlib.sha256(data).hexdigest()
        if digest not in seen:
            relative = Path('history/file_versions') / digest / path.name
            destination = stage / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            seen[digest] = str(relative)
        prior_recipe['entries'].append({
            'zip_metadata': metadata(info), 'sha256': digest,
            'size': len(data), 'stored_path': seen[digest]})

# Every old recipe is relocated by its checked content hash, never by a
# filename guess. The exact prior manifest bytes are themselves preserved.
for snapshot in legacy['snapshots'].values():
    for entry in snapshot['entries']:
        if 'sha256' in entry:
            entry['stored_path'] = seen[entry['sha256']]
for snapshot in compacts['snapshots'].values():
    for entry in snapshot['entries']:
        entry['stored_path'] = seen[entry['sha256']]
compacts['snapshots'][str(number-1)] = prior_recipe
history = stage / 'history'
history.mkdir(exist_ok=True)
(history / 'snapshots.json').write_text(json.dumps(legacy, indent=2)+'\n')
(history / 'compact_snapshots.json').write_text(
    json.dumps(compacts, indent=2)+'\n')
(history / 'current_snapshot.json').write_text(json.dumps({
    'number': number, 'created_utc': stamp, 'files': current}, indent=2)+'\n')
shutil.copy2(project / 'code/restore_compact_checkpoint.py',
             history / 'restore_snapshot.py')
shutil.copy2(project / 'code/restore_compact_package.py',
             history / 'restore_compact_package.py')
shutil.copy2(project / 'code/restore_current_tree.py',
             history / 'restore_current_tree.py')
(stage / 'CHECKPOINT.md').write_text(f'''# Complete hourly checkpoint {number:02d}

Frozen at {stamp}. The current paper, PDF, report, CSV, bibliography,
source, code, records and current research support are directly readable
under S6_03_CDP/ and research_support/. Exactly {aliases} duplicate
generated build paths share their byte-identical payload with another
retained path. All paths, bytes, sizes, hashes and file modes of the full
current tree are recorded in history/current_snapshot.json. Reconstruct
that exact full current tree into a new directory with:

    python3 history/restore_current_tree.py /absolute/path/new_current_tree

Every distinct historical file version from the preceding compact package
is retained under its exact content hash. No authored file, proof passage,
code, output, note, log, or earlier packaging record has been omitted.
Unchanged bytes are shared only within the archive representation.

history/current_snapshot.json records the frozen current tree. The legacy
history/snapshots.json and history/restore_snapshot.py reconstruct any
original checkpoint1 through9 byte for byte. The exact compact checkpoint
packages9 through{number-1} are described in history/compact_snapshots.json:

    python3 history/restore_compact_package.py {number-1} /absolute/path/prior.zip

The restore programs refuse to replace files and verify the exact original
ZIP byte hash. The immediately preceding compact package was reconstructed
in an anonymous temporary file and its byte hash verified during this save.
All older recipes retain their previously verified bytes and ZIP metadata.
No earlier checkpoint was overwritten, renamed or deleted.
''')

sys.path.insert(0, str(project / 'code'))
from restore_compact_package import reconstruct
rebuilt = reconstruct(stage, prior_recipe)
rebuilt.close()
print(f'Byte-exact compact checkpoint {number-1:02d} reconstruction: PASS',
      flush=True)

with zipfile.ZipFile(target, 'x', compression=zipfile.ZIP_DEFLATED,
                     compresslevel=9) as archive:
    for path in sorted(stage.rglob('*')):
        if path.is_file():
            archive.write(path, str(path.relative_to(stage)))
result = {'path': str(target), 'created_utc': stamp,
            'members': sum(path.is_file() for path in stage.rglob('*')),
          'current_authored_files': len(current),
          'duplicate_build_path_aliases': aliases,
          'unique_retained_content_versions': len(seen),
          'bytes': target.stat().st_size, 'sha256': digest_path(target),
          'previous_compact_archive_verified': number-1,
          'legacy_exact_archives_retained': list(range(1, 10))}
assert result['bytes'] <= 512*1024*1024, 'Upload limit exceeded'
(project / 'records' / f'checkpoint_{number:02d}_manifest.json').write_text(
    json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2), flush=True)

