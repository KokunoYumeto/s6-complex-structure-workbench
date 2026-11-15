"""Repackage one frozen hourly snapshot without nested duplicate file versions.

Earlier immutable ZIPs are read only. All original ZIP bytes are reproducible
from the complete file versions and exact ZIP metadata, and are verified here.
"""
from pathlib import Path
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
stage = workspace / f'checkpoint{number:02d}_compact'
tree = stage / 'contents'
target = stage / f'S6_03_CDP_checkpoint_{number:02d}.zip'
if target.exists() or tree.exists():
    raise SystemExit('Refusing to replace an existing repackaged snapshot.')
tree.mkdir(parents=True)

def digest_path(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()

def metadata(info):
    result = {key: getattr(info, key) for key in [
        'filename', 'date_time', 'compress_type', 'create_system',
        'create_version', 'extract_version', 'reserved', 'flag_bits',
        'volume', 'internal_attr', 'external_attr']}
    result['extra'] = base64.b64encode(info.extra).decode()
    result['comment'] = base64.b64encode(info.comment).decode()
    return result

manifest = {'format': 1, 'latest': number, 'snapshots': {}}
seen = {}
for n in range(number, 0, -1):
    original = workspace / f'S6_03_CDP_checkpoint_{n:02d}.zip'
    snapshot = {'original_name': original.name,
                'original_bytes': original.stat().st_size,
                'original_sha256': digest_path(original),
                'entries': []}
    with zipfile.ZipFile(original) as archive:
        snapshot['comment'] = base64.b64encode(archive.comment).decode()
        for info in archive.infolist():
            entry = {'zip_metadata': metadata(info)}
            path = Path(info.filename)
            if path.is_absolute() or '..' in path.parts:
                raise ValueError('Unsafe stored path')
            if info.filename == f'archives/S6_03_CDP_checkpoint_{n-1:02d}.zip':
                entry['archive_snapshot'] = n - 1
            else:
                data = archive.read(info)
                digest = hashlib.sha256(data).hexdigest()
                if n == number:
                    relative = path
                    destination = tree / relative
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_bytes(data)
                    seen.setdefault(digest, str(relative))
                elif digest not in seen:
                    relative = Path('history/file_versions') / digest / path.name
                    destination = tree / relative
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_bytes(data)
                    seen[digest] = str(relative)
                entry.update({'sha256': digest, 'size': len(data),
                              'stored_path': seen[digest]})
            snapshot['entries'].append(entry)
    manifest['snapshots'][str(n)] = snapshot
    print(f'Indexed snapshot {n:02d}: {len(snapshot["entries"])} original members',
          flush=True)

history = tree / 'history'
history.mkdir(exist_ok=True)
(history / 'snapshots.json').write_text(json.dumps(manifest, indent=2) + '\n')
restore_source = project / 'code/restore_compact_checkpoint.py'
shutil.copy2(restore_source, history / 'restore_snapshot.py')
readme = '''# Exact packaging of the 21:36 UTC checkpoint

This is the same hourly snapshot as the original checkpoint09. The complete
current deliverable tree is directly under S6_03_CDP/, with all current
research support under research_support/. No later research changes have
been added to that tree. The original recursively nested ZIP exceeded the
512MiB upload limit. No earlier checkpoint or original archive was changed.

Every distinct historical authored file version is retained. Unchanged
copies share their stored bytes; history/snapshots.json records every
original path, file hash, complete ZIP metadata and original archive hash.
The old ZIP wrappers are represented by this exact lossless recipe instead
of recursively storing their already duplicated bytes. No authored file,
proof passage, code, output, note or log has been omitted.

To reconstruct any original checkpoint ZIP byte for byte, run:

    python3 history/restore_snapshot.py 9 /absolute/path/original_checkpoint09.zip

Use 1 through9 to reconstruct any earlier original. The script checks its
exact original SHA256 before writing the chosen output. Every original
checkpoint1 through9 was reconstructed and its byte hash verified during
this repackaging. The current files can be used directly without restoration.
'''
(tree / 'REPACKING.md').write_text(readme)

# Use the same self-contained restore routine supplied in the package.
sys.path.insert(0, str(project / 'code'))
from restore_compact_checkpoint import rebuild_all
rebuilt = rebuild_all(tree, manifest, number, verbose=True)
rebuilt.close()

with zipfile.ZipFile(target, 'x', compression=zipfile.ZIP_DEFLATED,
                     compresslevel=9) as archive:
    for path in sorted(tree.rglob('*')):
        if path.is_file():
            archive.write(path, str(path.relative_to(tree)))
result = {'source_snapshot': number,
          'original_path': str(workspace / f'S6_03_CDP_checkpoint_{number:02d}.zip'),
          'path': str(target), 'bytes': target.stat().st_size,
          'sha256': digest_path(target), 'unique_file_versions': len(seen),
          'exact_original_archives_verified': list(range(1, number+1))}
assert result['bytes'] <= 512*1024*1024
(project / 'records/checkpoint_09_repack.json').write_text(
    json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2), flush=True)
