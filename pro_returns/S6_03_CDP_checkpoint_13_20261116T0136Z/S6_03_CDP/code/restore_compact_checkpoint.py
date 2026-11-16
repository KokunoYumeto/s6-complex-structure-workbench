"""Reconstruct original immutable checkpoint ZIPs from lossless file versions."""
from pathlib import Path
import base64
import hashlib
import json
import shutil
import sys
import tempfile
import zipfile

def rebuild_all(root, manifest, number, verbose=False):
    previous = None
    for n in range(1, number+1):
        snapshot = manifest['snapshots'][str(n)]
        output = tempfile.TemporaryFile()
        with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED,
                             compresslevel=6) as archive:
            archive.comment = base64.b64decode(snapshot['comment'])
            for entry in snapshot['entries']:
                meta = entry['zip_metadata']
                info = zipfile.ZipInfo(meta['filename'], tuple(meta['date_time']))
                for key in ['compress_type', 'create_system', 'create_version',
                            'extract_version', 'reserved', 'flag_bits', 'volume',
                            'internal_attr', 'external_attr']:
                    setattr(info, key, meta[key])
                info.extra = base64.b64decode(meta['extra'])
                info.comment = base64.b64decode(meta['comment'])
                info._compresslevel = 6
                if 'archive_snapshot' in entry:
                    assert entry['archive_snapshot'] == n-1 and previous is not None
                    previous.seek(0)
                    info.file_size = manifest['snapshots'][str(n-1)]['original_bytes']
                    with archive.open(info, 'w') as dest:
                        shutil.copyfileobj(previous, dest, 1024*1024)
                else:
                    data = (root / entry['stored_path']).read_bytes()
                    if hashlib.sha256(data).hexdigest() != entry['sha256']:
                        raise ValueError('Historical file hash mismatch')
                    archive.writestr(info, data)
        output.seek(0)
        digest = hashlib.sha256()
        size = 0
        for block in iter(lambda: output.read(1024*1024), b''):
            digest.update(block)
            size += len(block)
        if size != snapshot['original_bytes'] or digest.hexdigest() != snapshot['original_sha256']:
            raise ValueError(f'Archive {n:02d} byte reconstruction mismatch: '
                             f'{size}, {digest.hexdigest()}')
        if previous is not None:
            previous.close()
        previous = output
        if verbose:
            print(f'Byte-exact original checkpoint {n:02d}: PASS ({size} bytes)',
                  flush=True)
    previous.seek(0)
    return previous

if __name__ == '__main__':
    root = Path(__file__).resolve().parent.parent
    manifest = json.loads((root / 'history/snapshots.json').read_text())
    number = int(sys.argv[1])
    target = Path(sys.argv[2]).resolve()
    if target.exists():
        raise SystemExit('Refusing to overwrite an existing archive.')
    rebuilt = rebuild_all(root, manifest, number, verbose=True)
    with target.open('xb') as out:
        shutil.copyfileobj(rebuilt, out, 1024*1024)
    rebuilt.close()
    print(f'Wrote byte-exact original checkpoint: {target}')
