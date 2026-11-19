"""Complete hourly checkpoint25, resumable from the first frozen byte.

All closed predecessor shards are reused byte for byte. A persistent file
list, per-file journal and frozen manifest precede encoding. New payload
shards are independently closed and recorded before the final immutable
ZIP is published. Re-entry never changes a completed frozen file.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import lzma
import os
import re
import shutil
import sys
import tarfile
import time
import zipfile
from checkpoint_copy_add import encode, decode
from checkpoint_png_codec import encode as encode_png, decode as decode_png

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
STAGE = BASE/'checkpoint25_encoding'
TARGET = BASE/'S6_06_BLIND_checkpoint_25.zip'
DUE = datetime.fromisoformat('2026-11-18T00:49:44+00:00')
PRIOR_MANIFEST = BASE/'checkpoint24_encoding/checkpoint24_transport_manifest.json'


def sha(path):
    with path.open('rb') as source:
        return hashlib.file_digest(source, 'sha256').hexdigest()


def atomic_json(path, value):
    temporary = path.with_suffix(path.suffix+'.pending')
    temporary.write_text(json.dumps(value, indent=2)+'\n')
    temporary.replace(path)


def excluded(rel):
    source = any(rel.startswith(prefix) for prefix in (
        'records/primary_sources/', 'records/external_source_cache/',
        'records/sources/', 'records/part5_comparison/'))
    return ((source and Path(rel).suffix.lower() in
             ('.pdf', '.txt', '.png', '.jpg', '.jpeg', '.tif', '.tiff', '.html'))
            or rel == 'records/AC26_original_extracted.txt'
            or bool(re.fullmatch(r'records/web_\d+\.json', rel))
            or rel == 'code/part1/ocr_wall.out')


prior = json.loads(PRIOR_MANIFEST.read_text())
verification = json.loads((ROOT/'records/checkpoint24_verification.json').read_text())
assert verification['status'] == 'PASS' and verification['restored_and_verified_files'] == 8748
assert verification['sha256'] == 'cdaa86333532bbd2b3cf1c0ca43cd51bc92b40b4f275d6a720448904ca6a062e'
bundle_paths = []
for bundle in prior['bundles']:
    candidates = [BASE/'checkpoint24_content_preparation/bundles'/bundle['file'],
                  BASE/'checkpoint24_encoding'/bundle['file']]
    path = next(p for p in candidates if p.is_file())
    assert path.stat().st_size == bundle['bytes'] and sha(path) == bundle['sha256'], path
    bundle_paths.append(path)

if '--preflight' in sys.argv:
    record = {'status': 'PASS', 'utc': datetime.now(timezone.utc).isoformat(),
              'predecessor_manifest_sha256': sha(PRIOR_MANIFEST),
              'verified_closed_shards': len(bundle_paths),
              'closed_shard_bytes': sum(p.stat().st_size for p in bundle_paths),
              'predecessor_archive_sha256': verification['sha256'],
              'strategy': 'Reuse all verified closed shards; freeze journal precedes new-content encoding; each new shard and the final ZIP publish atomically.'}
    atomic_json(ROOT/'records/checkpoint25_preflight.json', record)
    archive_record = ROOT/'records/checkpoint25_predecessor_transport_manifest.json'
    if not archive_record.exists():
        shutil.copy2(PRIOR_MANIFEST, archive_record)
    assert sha(archive_record) == sha(PRIOR_MANIFEST)
    print(json.dumps(record, indent=2), flush=True)
    raise SystemExit

assert datetime.now(timezone.utc) >= DUE, 'Hourly checkpoint is not yet due'
if TARGET.exists():
    result = json.loads((STAGE/'checkpoint25_creation.json').read_text())
    assert TARGET.stat().st_size == result['bytes'] and sha(TARGET) == result['sha256']
    print(json.dumps({'status': 'ALREADY_COMPLETE', **result}, indent=2), flush=True)
    raise SystemExit
STAGE.mkdir(exist_ok=True)
frozen = STAGE/'frozen'
initial = STAGE/'freeze_initial.json'
if not initial.exists():
    record = {
        'checkpoint': 25, 'due_utc': DUE.isoformat(),
        'created_utc': datetime.now(timezone.utc).isoformat(),
        'verified_predecessor': 24,
        'predecessor_sha256': verification['sha256'],
        'predecessor_library_id': 'libfile_20e73511ddc88191b3d9010deec456b6',
        'blind_part5_sha256': {n: sha(ROOT/n) for n in ('notes/part5.tex', 'notes/part5_blind.md')}
    }
    assert record['blind_part5_sha256']['notes/part5.tex'] == 'f7b2188bbd5fc453780421599b65168141c8ed09480b1396794f02f41a680e0f'
    assert record['blind_part5_sha256']['notes/part5_blind.md'] == 'ffdac7780a3d5c35565e31e6bb1bebf459e0f7dc75355e19fc216b5ba4b9a1e4'
    atomic_json(ROOT/'records/checkpoint_25.json', record)
    marker = '| S6_06_BLIND_checkpoint_25.zip |'
    log_path = ROOT/'S6_06_BLIND_literature_log.md'
    if marker not in log_path.read_text():
        with log_path.open('a') as log:
            log.write(f"\n| {record['created_utc']} {marker} Complete hourly snapshot after independently verified checkpoint24 | All proof/code/log/attempt contents, exact original rendered bytes and immutable blind Part5 retained. |\n")
    names = [p.relative_to(ROOT).as_posix() for p in sorted(ROOT.rglob('*'))
             if p.is_file() and not excluded(p.relative_to(ROOT).as_posix())]
    atomic_json(initial, {'record': record, 'root_relative_file_list': names})
initial_data = json.loads(initial.read_text())
record = initial_data['record']
frozen_manifest = STAGE/'frozen_manifest.json'
if frozen_manifest.exists():
    freeze = json.loads(frozen_manifest.read_text())
    files = freeze['files']
    record = freeze['snapshot']
    print(json.dumps({'status': 'RESUMED_COMPLETE_FROZEN_TREE', 'files': len(files),
                      'frozen_utc': record['frozen_utc']}), flush=True)
else:
    journal = STAGE/'freeze_journal.jsonl'
    files = {}
    if journal.exists():
        for line in journal.read_text().splitlines():
            entry = json.loads(line)
            files[entry['name']] = entry['info']
    with journal.open('a') as log:
        for number, rel in enumerate(initial_data['root_relative_file_list']):
            name = 'S6_06_BLIND/'+rel
            path = ROOT/rel
            copy = frozen/name
            if name in files:
                assert copy.stat().st_size == files[name]['bytes'] and sha(copy) == files[name]['sha256']
                continue
            copy.parent.mkdir(parents=True, exist_ok=True)
            # The copy owns its bytes, and a source rewrite during copying is
            # retried before this file can enter the immutable freeze journal.
            for retry in range(8):
                before = {'bytes': path.stat().st_size, 'sha256': sha(path)}
                temporary = copy.with_name(copy.name+'.freezing')
                shutil.copy2(path, temporary)
                after = {'bytes': temporary.stat().st_size, 'sha256': sha(temporary)}
                if before == after and path.stat().st_size == before['bytes'] and sha(path) == before['sha256']:
                    temporary.replace(copy)
                    break
                temporary.rename(STAGE/f'changed_during_freeze_{number}_{retry}')
            else:
                raise RuntimeError('Source continuously changed during freeze: '+rel)
            files[name] = before
            log.write(json.dumps({'name': name, 'info': before})+'\n')
            log.flush()
            os.fsync(log.fileno())
            if number % 1500 == 0:
                print(json.dumps({'status': 'FREEZING', 'files': number+1}), flush=True)
    record['frozen_utc'] = datetime.now(timezone.utc).isoformat()
    atomic_json(frozen_manifest, {'snapshot': record, 'files': files})
    print(json.dumps({'status': 'FROZEN', 'files': len(files), 'utc': record['frozen_utc']}), flush=True)

paths = {n: frozen/n for n in files}
unique = {}
for name, info in files.items():
    unique.setdefault(info['sha256'], (name, paths[name], info))
contents = dict(prior['contents'])
patch_order = list(prior['patch_order'])
payload = []
reference_name = 'S6_06_BLIND/S6_06_BLIND_paper.pdf'
reference = BASE/'checkpoint24_encoding/frozen'/reference_name
reference_sha = prior['files'][reference_name]['sha256']
assert sha(reference) == reference_sha
reference_bytes = reference.read_bytes()
cache = STAGE/'encoded_objects'
cache.mkdir(exist_ok=True)
for h, (name, path, info) in unique.items():
    if h in contents:
        assert contents[h]['bytes'] == info['bytes']
        continue
    meta = cache/(h+'.json')
    if meta.exists():
        saved = json.loads(meta.read_text())
        encoded = Path(saved['local_path'])
        assert encoded.stat().st_size == saved['encoded_bytes'] and sha(encoded) == saved['encoded_sha256']
        contents[h] = saved['content']
        payload.append((saved['packed_name'], encoded, Path(name).suffix, name))
        if contents[h]['storage'] == 'copy_add':
            patch_order.append(h)
        continue
    entry = None
    if name.endswith('.pdf') and info['bytes'] > 1000000:
        raw = path.read_bytes()
        packed, stats = encode(reference_bytes, raw)
        assert decode(reference_bytes, packed) == raw
        if len(packed) < len(raw)*.92:
            encoded = cache/(h+'.copyadd')
            encoded.write_bytes(packed)
            packed_name = 'patches/'+h
            entry = {'bytes': len(raw), 'storage': 'copy_add', 'base_sha256': reference_sha,
                     'patch_name': packed_name, 'patch_sha256': sha(encoded), 'stats': stats}
            patch_order.append(h)
    if entry is None and name.endswith('.png'):
        raw = path.read_bytes()
        packed = encode_png(raw)
        if packed is not None:
            assert decode_png(packed) == raw
            encoded = cache/(h+'.pngcodec')
            encoded.write_bytes(packed)
            packed_name = 'png/'+h
            entry = {'bytes': len(raw), 'storage': 'png', 'encoded_name': packed_name,
                     'encoded_sha256': sha(encoded)}
    if entry is None:
        encoded, packed_name = path, 'content/'+h
        entry = {'bytes': info['bytes'], 'storage': 'raw', 'name': packed_name}
    contents[h] = entry
    payload.append((packed_name, encoded, Path(name).suffix, name))
    atomic_json(meta, {'content': entry, 'packed_name': packed_name, 'local_path': str(encoded),
                      'encoded_bytes': encoded.stat().st_size, 'encoded_sha256': sha(encoded)})

payload.sort(key=lambda row: (row[2], row[3]))
groups, group, size = [], [], 0
for row in payload:
    amount = row[1].stat().st_size
    if group and size+amount > 64*1024*1024:
        groups.append(group)
        group, size = [], 0
    group.append(row)
    size += amount
if group:
    groups.append(group)
bundles = list(prior['bundles'])
for index, group in enumerate(groups):
    name = f'checkpoint25_new_content_{index:04d}.tar.xz'
    destination = STAGE/name
    receipt = STAGE/(name+'.json')
    fingerprint = hashlib.sha256('\n'.join(r[0]+':'+sha(r[1]) for r in group).encode()).hexdigest()
    if receipt.exists():
        bundle = json.loads(receipt.read_text())
        assert bundle['fingerprint'] == fingerprint
        assert destination.stat().st_size == bundle['bytes'] and sha(destination) == bundle['sha256']
    else:
        temporary = destination.with_suffix(destination.suffix+'.partial')
        if temporary.exists():
            temporary.rename(STAGE/(name+'.interrupted_'+str(time.time_ns())))
        with lzma.open(temporary, 'xb', filters=[{'id': lzma.FILTER_LZMA2, 'preset': 3,
                                                'dict_size': 64*1024*1024}]) as stream:
            with tarfile.open(fileobj=stream, mode='w|', format=tarfile.PAX_FORMAT) as tar:
                for packed_name, path, suffix, original_name in group:
                    item = tarfile.TarInfo(packed_name)
                    item.mode, item.mtime, item.size = 0o644, 0, path.stat().st_size
                    with path.open('rb') as source:
                        tar.addfile(item, source)
        temporary.replace(destination)
        bundle = {'file': name, 'bytes': destination.stat().st_size, 'sha256': sha(destination),
                  'members': len(group), 'fingerprint': fingerprint}
        atomic_json(receipt, bundle)
    bundles.append(bundle)
    bundle_paths.append(destination)
    print(json.dumps({'status': 'CLOSED_NEW_SHARD', 'index': index, **bundle}), flush=True)

direct = ['S6_06_BLIND/'+n for n in ('S6_06_BLIND_paper.pdf', 'S6_06_BLIND_paper.tex',
          'S6_06_BLIND_report.md', 'S6_06_BLIND_results.csv', 'S6_06_BLIND_literature_log.md')]
manifest = {'snapshot': record, 'files': files, 'contents': contents, 'patch_order': patch_order,
            'bundles': bundles, 'direct_files': direct, 'predecessor_files': prior['files'],
            'scope': 'Complete standalone snapshot with every verified predecessor content object and the complete predecessor manifest. Exact original bytes, full proofs/code/logs/attempts and documented supplied/external source-payload exclusions.'}
manifest_path = STAGE/'checkpoint25_transport_manifest.json'
atomic_json(manifest_path, manifest)
restore = (BASE/'checkpoint24_encoding/restore_checkpoint.py').read_text().replace('checkpoint24', 'checkpoint25')
compile(restore, 'restore_checkpoint.py', 'exec')
(STAGE/'restore_checkpoint.py').write_text(restore)
readme = f'''# Complete immutable checkpoint25

Extract this ZIP and run `python3 restore_checkpoint.py`. The current paper and registers are directly readable. The delivered standard-library restorer checks all {len(files):,} research files against their exact original sizes and SHA-256 hashes. Every compressed shard and decoder is included; no previous checkpoint download is needed.

All verified predecessor content is retained. Its complete file and content manifest is also preserved in the research records. Historical PDF copy/add records and lossless PNG reconstruction preserve the original bytes, not only appearances. The maximum LZMA dictionary is64MiB.

Frozen at {record['frozen_utc']}. The report remains INCOMPLETE. The complete proofs, working notes, programs, certificates, logs, rendered pages and preserved attempts are included. The supplied and external source-payload exclusions are documented in the report. The resumable freeze and shard receipts are included under checkpoint25_transport.
'''
partial = STAGE/'checkpoint25.partial'
if partial.exists():
    partial.rename(STAGE/('checkpoint25.interrupted_'+str(time.time_ns())))
with zipfile.ZipFile(partial, 'x', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for name in direct:
        archive.write(paths[name], name)
    for path in bundle_paths:
        archive.write(path, path.name, compress_type=zipfile.ZIP_STORED)
    archive.write(manifest_path, manifest_path.name)
    archive.write(STAGE/'restore_checkpoint.py', 'restore_checkpoint.py')
    for name in ('checkpoint_copy_add.py', 'checkpoint_png_codec.py'):
        archive.write(frozen/'S6_06_BLIND/code'/name, name)
    for name in ('freeze_initial.json', 'freeze_journal.jsonl', 'frozen_manifest.json'):
        archive.write(STAGE/name, 'checkpoint25_transport/'+name)
    archive.write(frozen/'S6_06_BLIND/code/make_checkpoint25.py', 'checkpoint25_transport/make_checkpoint25.py')
    for path in sorted(STAGE.glob('checkpoint25_new_content_*.tar.xz.json')):
        archive.write(path, 'checkpoint25_transport/'+path.name)
    archive.writestr('READ_FIRST.md', readme)
for name, path in paths.items():
    assert path.stat().st_size == files[name]['bytes'] and sha(path) == files[name]['sha256']
assert partial.stat().st_size <= 536870912, partial.stat().st_size
result = {'status': 'CREATED', 'path': str(TARGET), 'bytes': partial.stat().st_size,
          'sha256': sha(partial), 'snapshot_files': len(files), 'record': record,
          'new_unique_contents': len(payload), 'closed_shards': len(bundles)}
atomic_json(STAGE/'checkpoint25_creation.json', result)
partial.rename(TARGET)
print(json.dumps(result, indent=2), flush=True)
