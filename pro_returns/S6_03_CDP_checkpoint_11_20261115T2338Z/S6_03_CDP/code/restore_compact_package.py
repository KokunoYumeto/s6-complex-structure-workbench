"""Restore an immutable compact hourly ZIP from exact retained file bytes."""
from pathlib import Path
import base64
import hashlib
import json
import shutil
import sys
import tempfile
import zipfile

def reconstruct(root, recipe):
    output = tempfile.TemporaryFile()
    level = recipe['compression_level']
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED,
                         compresslevel=level) as archive:
        archive.comment = base64.b64decode(recipe['comment'])
        for entry in recipe['entries']:
            meta = entry['zip_metadata']
            info = zipfile.ZipInfo(meta['filename'], tuple(meta['date_time']))
            for key in ['compress_type', 'create_system', 'create_version',
                        'extract_version', 'reserved', 'flag_bits', 'volume',
                        'internal_attr', 'external_attr']:
                setattr(info, key, meta[key])
            info.extra = base64.b64decode(meta['extra'])
            info.comment = base64.b64decode(meta['comment'])
            info._compresslevel = level
            data = (root / entry['stored_path']).read_bytes()
            if len(data) != entry['size'] or hashlib.sha256(data).hexdigest() != entry['sha256']:
                raise ValueError('Historical content hash mismatch')
            archive.writestr(info, data)
    output.seek(0)
    h = hashlib.sha256()
    size = 0
    for block in iter(lambda: output.read(1024*1024), b''):
        h.update(block)
        size += len(block)
    if size != recipe['original_bytes'] or h.hexdigest() != recipe['original_sha256']:
        raise ValueError(f'Exact compact reconstruction failed: {size}, {h.hexdigest()}')
    output.seek(0)
    return output

if __name__ == '__main__':
    root = Path(__file__).resolve().parent.parent
    number = int(sys.argv[1])
    target = Path(sys.argv[2]).resolve()
    if target.exists():
        raise SystemExit('Refusing to overwrite an existing archive.')
    manifest = json.loads((root / 'history/compact_snapshots.json').read_text())
    rebuilt = reconstruct(root, manifest['snapshots'][str(number)])
    with target.open('xb') as stream:
        shutil.copyfileobj(rebuilt, stream, 1024*1024)
    rebuilt.close()
    print(f'Wrote byte-exact compact checkpoint: {target}')
