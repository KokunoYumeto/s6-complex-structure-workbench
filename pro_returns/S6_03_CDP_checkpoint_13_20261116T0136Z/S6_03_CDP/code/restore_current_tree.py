"""Reconstruct every current checkpoint path from its verified exact bytes.

Run the copy packaged as history/restore_current_tree.py with one new output
directory. Checkpoint12 and earlier manifests without stored_path are also
supported. No existing output directory or file is replaced.
"""
from pathlib import Path
import hashlib
import json
import os
import shutil
import stat
import sys


def safe_relative(value):
    path = Path(value)
    if path.is_absolute() or '..' in path.parts or not path.parts:
        raise ValueError('Unsafe checkpoint path')
    return path


def restore_current_tree(checkpoint_root, target):
    checkpoint_root = Path(checkpoint_root).resolve()
    target = Path(target).resolve()
    if target.exists():
        raise ValueError('Refusing to replace an existing current tree')
    entries = json.loads((checkpoint_root / 'history/current_snapshot.json').read_text())['files']
    paths = [str(safe_relative(entry['path'])) for entry in entries]
    if len(paths) != len(set(paths)):
        raise ValueError('Duplicate current path in manifest')
    # Verify every payload before writing any output files.
    checked = set()
    for entry in entries:
        source = checkpoint_root / safe_relative(entry.get('stored_path', entry['path']))
        check = (str(source), entry['sha256'], entry['size'])
        if check in checked:
            continue
        data = source.read_bytes()
        if len(data) != entry['size'] or hashlib.sha256(data).hexdigest() != entry['sha256']:
            raise ValueError('Current payload hash mismatch: ' + entry['path'])
        checked.add(check)
    target.mkdir(parents=True)
    total = 0
    for entry in entries:
        source = checkpoint_root / safe_relative(entry.get('stored_path', entry['path']))
        destination = target / safe_relative(entry['path'])
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        if 'mode' in entry:
            destination.chmod(stat.S_IMODE(entry['mode']))
        if 'mtime_ns' in entry:
            os.utime(destination, ns=(entry['mtime_ns'], entry['mtime_ns']))
        total += entry['size']
    return {'files': len(entries), 'payloads_checked': len(checked), 'bytes': total}


if __name__ == '__main__':
    root = Path(__file__).resolve().parent.parent
    print(json.dumps(restore_current_tree(root, sys.argv[1]), indent=2))
