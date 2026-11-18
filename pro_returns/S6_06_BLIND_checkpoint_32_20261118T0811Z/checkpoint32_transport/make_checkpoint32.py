"""Complete hourly checkpoint32 after the original32 freeze.

All predecessor raw, gzip, zlib, PNG-row, PNG and copy/add identities remain.
The unchanged prior decoder and every supporting module are delivered.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,lzma,os,re,shutil,subprocess,sys,tarfile,time,zipfile
from checkpoint_copy_add import encode,decode
from checkpoint_png_codec import encode as encode_png,decode as decode_png
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
STAGE=BASE/'checkpoint32_encoding';TARGET=BASE/'S6_06_BLIND_checkpoint_32.zip'
DUE=datetime.fromisoformat('2026-11-18T07:49:44+00:00')
PRIOR_MANIFEST=BASE/'checkpoint31_encoding/checkpoint31_transport_manifest.json'
def sha(path):
    with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def atomic_json(path,value):
    tmp=path.with_suffix(path.suffix+'.pending')
    tmp.write_text(json.dumps(value,indent=2)+'\n');tmp.replace(path)
def tar_stream_identity(path):
    digest=hashlib.sha256();amount=0
    with lzma.open(path,'rb') as f:
        while block:=f.read(1024*1024):digest.update(block);amount+=len(block)
    return amount,digest.hexdigest()
assert datetime.now(timezone.utc)>=DUE,'Hourly checkpoint is not yet due'
prior=json.loads(PRIOR_MANIFEST.read_text())
verification=json.loads((ROOT/'records/checkpoint31_verification.json').read_text())
creation=json.loads((BASE/'checkpoint31_encoding/checkpoint31_creation.json').read_text())
assert verification['status']=='PASS'
assert verification['restored_and_verified_files']==creation['snapshot_files']==12783
assert verification['sha256']==creation['sha256']
assert prior['transport_repairs']['status']=='PASS_BYTE_REVERSIBLE_GZIP_ZLIB_PNG_MEMBERS'
if TARGET.exists():
    done=json.loads((STAGE/'checkpoint32_creation.json').read_text())
    assert TARGET.stat().st_size==done['bytes'] and sha(TARGET)==done['sha256']
    print(json.dumps({'status':'ALREADY_COMPLETE',**done},indent=2),flush=True)
    raise SystemExit
STAGE.mkdir(exist_ok=True)
frozen=STAGE/'frozen';frozen_manifest=STAGE/'frozen_manifest.json'
assert frozen_manifest.exists(),'Run the separate hourly freeze first'
freeze=json.loads(frozen_manifest.read_text());files=freeze['files'];record=freeze['snapshot']
assert record['checkpoint']==32
assert record['prior_frozen_manifest_sha256']==sha(BASE/'checkpoint31_encoding/frozen_manifest.json')
folders=[BASE/f'checkpoint{k}_encoding' for k in range(32,23,-1)]
folders+=sorted(p for p in BASE.glob('checkpoint*_repack') if p.is_dir())
folders+=[BASE/'checkpoint31_png_rows_candidate/bundles',BASE/'checkpoint24_content_preparation/bundles']
bundle_paths=[]
for bundle in prior['bundles']:
    path=next(folder/bundle['file'] for folder in folders if (folder/bundle['file']).is_file())
    assert path.stat().st_size==bundle['bytes'] and sha(path)==bundle['sha256']
    bundle_paths.append(path)
extra_repack=None;extra_repack_selection=[]
prior_record=ROOT/'records/checkpoint32_predecessor_transport_manifest.json'
if not prior_record.exists():shutil.copyfile(PRIOR_MANIFEST,prior_record)
assert sha(prior_record)==sha(PRIOR_MANIFEST)
print(json.dumps({'status':'RESUMED_COMPLETE_FROZEN_TREE','files':len(files),'frozen_utc':record['frozen_utc']}),flush=True)
paths = {n: frozen/n for n in files}
unique = {}
for name, info in files.items():
    unique.setdefault(info['sha256'], (name, paths[name], info))
contents = dict(prior['contents'])
patch_order = list(prior['patch_order'])
payload = []
reference_name = 'S6_06_BLIND/S6_06_BLIND_paper.pdf'
reference = BASE/'checkpoint31_encoding/frozen'/reference_name
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
new_repack_path = BASE/'checkpoint32_new_repack/new_repack_p6_manifest.json'
new_repack = None
new_repack_selection = []
if new_repack_path.exists():
    new_repack = json.loads(new_repack_path.read_text())
    assert new_repack['status'] == 'PASS'
    assert new_repack['frozen_manifest_sha256'] == sha(frozen_manifest)
    assert new_repack['dictionary_bytes'] <= 64*1024*1024
for index, group in enumerate(groups):
    name = f'checkpoint32_new_content_{index:04d}.tar.xz'
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
        with lzma.open(temporary, 'xb', filters=[{'id': lzma.FILTER_LZMA2, 'preset': 6,
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
    if new_repack is not None:
        choice = new_repack['entries'].get(name)
        if choice is not None and choice['use_candidate']:
            assert choice['status'] == 'PASS_IDENTICAL_UNCOMPRESSED_TAR'
            assert choice['original'] == bundle
            assert choice['frozen_manifest_sha256'] == sha(frozen_manifest)
            candidate = new_repack_path.parent/choice['candidate_file']
            assert candidate.stat().st_size == choice['candidate_bytes']
            assert sha(candidate) == choice['candidate_sha256']
            expected_tar = (choice['tar_bytes'], choice['tar_sha256'])
            # Revalidate both complete uncompressed streams in the builder;
            # a smaller compressed representation never changes a TAR byte.
            assert tar_stream_identity(destination) == expected_tar
            assert tar_stream_identity(candidate) == expected_tar
            new_repack_selection.append(choice)
            bundle = choice['bundle']
            destination = candidate
    bundles.append(bundle)
    bundle_paths.append(destination)
    print(json.dumps({'status': 'CLOSED_NEW_SHARD', 'index': index, **bundle}), flush=True)

dictionary_repack_path=ROOT/'records/checkpoint32_png_dictionary_repack.json'
announced_dictionary=False
while not dictionary_repack_path.exists():
    if not announced_dictionary:
        print('All new32 shards are closed; waiting for the independently byte-equal smaller dictionary representation.',flush=True)
        announced_dictionary=True
    time.sleep(20)
dictionary_repack=json.loads(dictionary_repack_path.read_text())
assert dictionary_repack['status']=='PASS_IDENTICAL_UNCOMPRESSED_TAR'
old_dictionary=dictionary_repack['original'];new_dictionary=dictionary_repack['candidate']
dictionary_index=next(i for i,b in enumerate(bundles) if b['file']==old_dictionary['file'])
assert bundles[dictionary_index]['bytes']==old_dictionary['bytes']
assert bundles[dictionary_index]['sha256']==old_dictionary['sha256']
candidate_dictionary=Path(new_dictionary['local_path'])
assert candidate_dictionary.stat().st_size==new_dictionary['bytes']
assert sha(candidate_dictionary)==new_dictionary['sha256']
expected_dictionary_tar=(dictionary_repack['tar_bytes'],dictionary_repack['tar_sha256'])
assert tar_stream_identity(bundle_paths[dictionary_index])==expected_dictionary_tar
assert tar_stream_identity(candidate_dictionary)==expected_dictionary_tar
bundles[dictionary_index]={k:v for k,v in new_dictionary.items() if k!='local_path'}
bundle_paths[dictionary_index]=candidate_dictionary

direct = ['S6_06_BLIND/'+n for n in ('S6_06_BLIND_paper.pdf', 'S6_06_BLIND_paper.tex',
          'S6_06_BLIND_report.md', 'S6_06_BLIND_results.csv', 'S6_06_BLIND_literature_log.md')]
manifest = {'snapshot': record, 'files': files, 'contents': contents, 'patch_order': patch_order,
            'bundles': bundles, 'direct_files': direct, 'predecessor_files': prior['files'],
            'scope': 'Complete standalone snapshot with every verified predecessor content object and the complete predecessor manifest. Exact original bytes, full proofs/code/logs/attempts and documented supplied/external source-payload exclusions.'}
if new_repack is not None:
    manifest['new_stream_recompression'] = {
        'status': 'PASS_IDENTICAL_UNCOMPRESSED_TAR',
        'frozen_manifest_sha256': sha(frozen_manifest),
        'selection_manifest_sha256': sha(new_repack_path),
        'selected_shards': len(new_repack_selection),
        'saved_bytes': sum(item['saving'] for item in new_repack_selection),
        'scope': 'The same completed freeze and original closed TAR streams; both full uncompressed stream identities were independently revalidated while building this archive.'}
if extra_repack is not None:
    manifest['extra_predecessor_stream_recompression'] = {
        'status': 'PASS_IDENTICAL_UNCOMPRESSED_TAR',
        'frozen_manifest_sha256': sha(frozen_manifest),
        'selection_manifest_sha256': sha(extra_repack_path),
        'selected_shards': len(extra_repack_selection),
        'saved_bytes': sum(item['saving'] for item in extra_repack_selection),
        'scope': 'Further compression of retained predecessor closed TAR streams; original and candidate full uncompressed identities were revalidated in this builder.'}
# Carry the complete prior member layer before new raw/PNG/copy-add contents.
manifest['object_transforms']=prior.get('object_transforms',[])
manifest['transport_support_files']=prior.get('transport_support_files',[])
manifest['inherited_transport_repairs']=prior.get('transport_repairs',{})
manifest['dictionary_representation']={
    'status':'PASS_IDENTICAL_UNCOMPRESSED_TAR',
    'receipt_sha256':sha(dictionary_repack_path),
    'original':old_dictionary,'candidate':new_dictionary,
    'tar_bytes':dictionary_repack['tar_bytes'],'tar_sha256':dictionary_repack['tar_sha256'],
    'saved_bytes':dictionary_repack['saving'],
    'scope':'All original dictionary, row-index, TAR and research content bytes are unchanged.'}
for support in manifest['transport_support_files']:
    source=BASE/'checkpoint31_encoding'/support['file']
    assert source.stat().st_size==support['bytes'] and sha(source)==support['sha256']
    shutil.copyfile(source,STAGE/support['file'])
manifest_path = STAGE/'checkpoint32_transport_manifest.json'
atomic_json(manifest_path, manifest)
restore = (BASE/'checkpoint31_encoding/restore_checkpoint.py').read_text().replace('checkpoint31', 'checkpoint32')
compile(restore, 'restore_checkpoint.py', 'exec')
(STAGE/'restore_checkpoint.py').write_text(restore)
readme = f'''# Complete immutable checkpoint32

Extract this ZIP and run `python3 restore_checkpoint.py`. The current paper and registers are directly readable. The delivered standard-library restorer checks all {len(files):,} research files against their exact original sizes and SHA-256 hashes. Every compressed shard and decoder is included; no previous checkpoint download is needed.

All verified predecessor content is retained. Selected earlier tar streams may use a smaller compressed representation after exact uncompressed size and SHA-256 comparison; the full original project bytes are unchanged. Its complete file and content manifest is also preserved in the research records. Historical PDF copy/add records and lossless PNG reconstruction preserve the original bytes, not only appearances. Every prior member codec and its shared dictionary is retained; all decoder modules are included and hash-checked. The maximum LZMA dictionary is64MiB.

The new closed TAR streams may likewise use verified stronger compression. Their original receipts, full-stream size/SHA comparisons, repaired builder and recompression program are retained under checkpoint32_transport. The frozen project file list, original sizes, hashes and capture time are the same completed checkpoint32 freeze. Four JSON metadata entries use standard ZIP LZMA compression; Python's standard-library zipfile extractor supports this method. Their extracted bytes are unchanged, and the standalone restore verification checks the full snapshot after extraction.

Frozen at {record['frozen_utc']}. The report remains INCOMPLETE. The complete proofs, working notes, programs, certificates, logs, rendered pages and preserved attempts are included. The supplied and external source-payload exclusions are documented in the report. The resumable freeze and shard receipts are included under checkpoint32_transport.
'''
partial = STAGE/'checkpoint32.partial'
if partial.exists():
    partial.rename(STAGE/('checkpoint32.interrupted_'+str(time.time_ns())))
with zipfile.ZipFile(partial, 'x', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for name in direct:
        archive.write(paths[name], name)
    for path in bundle_paths:
        archive.write(path, path.name, compress_type=zipfile.ZIP_STORED)
    archive.write(manifest_path, manifest_path.name, compress_type=zipfile.ZIP_LZMA)
    archive.write(STAGE/'restore_checkpoint.py', 'restore_checkpoint.py')
    for support in manifest['transport_support_files']:
        archive.write(STAGE/support['file'],support['file'])
    for name in ('freeze_initial.json', 'freeze_journal.jsonl', 'frozen_manifest.json'):
        archive.write(STAGE/name, 'checkpoint32_transport/'+name, compress_type=zipfile.ZIP_LZMA)
    archive.write(ROOT/'code/make_checkpoint32.py', 'checkpoint32_transport/make_checkpoint32.py')
    archive.write(ROOT/'code/freeze_checkpoint32.py','checkpoint32_transport/freeze_checkpoint32.py')
    archive.write(ROOT/'code/prepare_checkpoint32_encoder.py','checkpoint32_transport/prepare_checkpoint32_encoder.py')
    archive.write(dictionary_repack_path,'checkpoint32_transport/'+dictionary_repack_path.name,compress_type=zipfile.ZIP_LZMA)
    archive.write(ROOT/'code/repack_checkpoint32_png_dictionary.py','checkpoint32_transport/repack_checkpoint32_png_dictionary.py')
    archive.write(ROOT/'code/part3_fourfold/assemble_checkpoint31_xz_blocks.py','checkpoint32_transport/assemble_checkpoint31_xz_blocks.py')
    for path in sorted(STAGE.glob('checkpoint32_new_content_*.tar.xz.json')):
        archive.write(path, 'checkpoint32_transport/'+path.name)
    if new_repack is not None:
        archive.write(new_repack_path,
                      'checkpoint32_transport/new_stream_recompression_manifest.json')
        archive.write(ROOT/'code/make_checkpoint32.py',
                      'checkpoint32_transport/make_checkpoint32_repaired.py')
        archive.write(ROOT/'code/part3_fourfold/repack_checkpoint32_new_streams.py',
                      'checkpoint32_transport/repack_checkpoint32_new_streams.py')
        archive.write(ROOT/'records/attempts/checkpoint32_size_gate_repair/preservation_manifest.json',
                      'checkpoint32_transport/failed_size_gate_preservation_manifest.json')
    if extra_repack is not None:
        archive.write(extra_repack_path,
                      'checkpoint32_transport/extra_predecessor_stream_recompression_manifest.json')
        archive.write(ROOT/'code/part3_fourfold/repack_checkpoint32_extra_streams.py',
                      'checkpoint32_transport/repack_checkpoint32_extra_streams.py')
    archive.writestr('READ_FIRST.md', readme)
for name, path in paths.items():
    assert path.stat().st_size == files[name]['bytes'] and sha(path) == files[name]['sha256']
assert partial.stat().st_size <= 536870912, partial.stat().st_size
result = {'status': 'CREATED', 'path': str(TARGET), 'bytes': partial.stat().st_size,
          'sha256': sha(partial), 'snapshot_files': len(files), 'record': record,
          'new_unique_contents': len(payload), 'closed_shards': len(bundles)}
atomic_json(STAGE/'checkpoint32_creation.json', result)
partial.rename(TARGET)
print(json.dumps(result, indent=2), flush=True)
