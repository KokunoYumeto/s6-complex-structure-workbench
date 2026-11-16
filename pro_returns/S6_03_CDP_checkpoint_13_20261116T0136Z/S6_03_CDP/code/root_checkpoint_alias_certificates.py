"""Verify full-tree and alias recovery without creating an off-hour ZIP."""
from pathlib import Path
import hashlib
import json
import tempfile

from restore_current_tree import restore_current_tree

project = Path(__file__).resolve().parents[1]
prior = project.parent / 'checkpoint12_compact/contents'
with tempfile.TemporaryDirectory(prefix='cdp_current_restore_') as temporary:
    target = Path(temporary) / 'full_checkpoint12_tree'
    result = restore_current_tree(prior, target)
    manifest = json.loads((prior/'history/current_snapshot.json').read_text())
    for entry in manifest['files']:
        path = target / entry['path']
        assert path.stat().st_size == entry['size']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry['sha256']
    print('Complete checkpoint12 current tree restored and every output hash rechecked:', result, 'PASS')
    try:
        restore_current_tree(prior, target)
    except ValueError as error:
        assert 'Refusing to replace' in str(error)
    else:
        raise AssertionError('Existing current tree was not protected')
    print('Existing output tree refusal: PASS')

with tempfile.TemporaryDirectory(prefix='cdp_alias_fixture_') as temporary:
    fixture = Path(temporary) / 'fixture'
    (fixture/'history').mkdir(parents=True)
    payload = (project/'code/restore_current_tree.py').read_bytes()
    (fixture/'payload').write_bytes(payload)
    entries = [dict(path=name, stored_path='payload', size=len(payload),
                    sha256=hashlib.sha256(payload).hexdigest(), mode=0o100640,
                    mtime_ns=1234567890000000000)
               for name in ['S6_03_CDP/code/sample.py',
                            'S6_03_CDP/build/history/exact_copy.py']]
    (fixture/'history/current_snapshot.json').write_text(json.dumps({'files':entries}))
    target = Path(temporary) / 'restored'
    result = restore_current_tree(fixture, target)
    assert result['files'] == 2 and result['payloads_checked'] == 1
    for entry in entries:
        path = target / entry['path']
        assert path.read_bytes() == payload
        assert path.stat().st_mode & 0o777 == 0o640
        assert path.stat().st_mtime_ns == entry['mtime_ns']
    print('Distinct aliased paths, exact bytes, modes and timestamps:', result, 'PASS')
    entries[0]['sha256'] = '0'*64
    (fixture/'history/current_snapshot.json').write_text(json.dumps({'files':entries}))
    bad_target = Path(temporary) / 'bad_restored'
    try:
        restore_current_tree(fixture, bad_target)
    except ValueError as error:
        assert 'hash mismatch' in str(error)
        assert not bad_target.exists()
    else:
        raise AssertionError('Corrupt payload was accepted')
    print('Payload corruption rejected before creating output tree: PASS')

print('No ZIP or checkpoint created by these certificates.')
