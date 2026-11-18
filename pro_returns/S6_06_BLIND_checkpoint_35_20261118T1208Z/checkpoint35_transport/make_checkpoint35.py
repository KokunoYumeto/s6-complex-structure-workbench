"""Complete hourly checkpoint35 from its own immutable freeze.

All predecessor raw, gzip, zlib, PNG-row, PNG and copy/add identities remain.
The verified predecessor streaming decoder and every supporting module are delivered.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,lzma,os,re,shutil,subprocess,sys,tarfile,time,zipfile
from checkpoint_copy_add import encode,decode
from checkpoint_png_codec import encode as encode_png,decode as decode_png
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
STAGE=BASE/'checkpoint35_encoding';TARGET=BASE/'S6_06_BLIND_checkpoint_35.zip'
DUE=datetime.fromisoformat('2026-11-18T10:49:44+00:00')
PRIOR_MANIFEST=BASE/'checkpoint34_encoding/checkpoint34_transport_manifest.json'
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
verification=json.loads((ROOT/'records/checkpoint34_verification.json').read_text())
creation=json.loads((BASE/'checkpoint34_encoding/checkpoint34_creation.json').read_text())
assert verification['status']=='PASS'
assert verification['restored_and_verified_files']==creation['snapshot_files']==15229
assert verification['sha256']==creation['sha256']
assert prior['inherited_transport_repairs']['status']=='PASS_BYTE_REVERSIBLE_GZIP_ZLIB_PNG_MEMBERS'
if TARGET.exists():
    done=json.loads((STAGE/'checkpoint35_creation.json').read_text())
    assert TARGET.stat().st_size==done['bytes'] and sha(TARGET)==done['sha256']
    print(json.dumps({'status':'ALREADY_COMPLETE',**done},indent=2),flush=True)
    raise SystemExit
STAGE.mkdir(exist_ok=True)
frozen=STAGE/'frozen';frozen_manifest=STAGE/'frozen_manifest.json'
assert frozen_manifest.exists(),'Run the separate hourly freeze first'
freeze=json.loads(frozen_manifest.read_text());files=freeze['files'];record=freeze['snapshot']
assert record['checkpoint']==35
assert record['prior_frozen_manifest_sha256']==sha(BASE/'checkpoint34_encoding/frozen_manifest.json')
folders=[BASE/f'checkpoint{k}_encoding' for k in range(35,23,-1)]
folders+=sorted(p for p in BASE.glob('checkpoint*_repack') if p.is_dir())
folders+=[BASE/'checkpoint33_final_encoding',BASE/'checkpoint33_member_repair',BASE/'checkpoint33_dictionary_rgb_complete',BASE/'checkpoint33_png_rows_candidate',BASE/'checkpoint33_zlib_complete_candidate',BASE/'checkpoint32_png_repack/bundles',BASE/'checkpoint34_png_repack/bundles',BASE/'checkpoint31_png_rows_candidate/bundles',BASE/'checkpoint24_content_preparation/bundles']
bundle_paths=[]
for bundle in prior['bundles']:
    path=next(folder/bundle['file'] for folder in folders if (folder/bundle['file']).is_file())
    assert path.stat().st_size==bundle['bytes'] and sha(path)==bundle['sha256']
    bundle_paths.append(path)
extra_repack=None;extra_repack_selection=[]
prior_record=ROOT/'records/checkpoint35_predecessor_transport_manifest.json'
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
reference = BASE/'checkpoint34_encoding/frozen'/reference_name
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
new_repack_path = BASE/'checkpoint35_new_repack/new_repack_manifest.json'
new_repack = None
new_repack_selection = []
if new_repack_path.exists():
    new_repack = json.loads(new_repack_path.read_text())
    assert new_repack['status'] == 'PASS'
    assert new_repack['frozen_manifest_sha256'] == sha(frozen_manifest)
    assert new_repack['dictionary_bytes'] <= 64*1024*1024
for index, group in enumerate(groups):
    name = f'checkpoint35_new_content_{index:04d}.tar.xz'
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

# The already-verified32 dictionary representation is inherited byte-for-byte.
# The verified original dictionary bytes and outer row-plane representation are inherited without reinterpretation.
extra_repack_path=BASE/'checkpoint35_extra_repack/extra_repack_manifest.json'
if extra_repack_path.exists():
    extra_repack=json.loads(extra_repack_path.read_text())
    assert extra_repack['status']=='PASS'
    assert extra_repack['prior_manifest_sha256']==sha(PRIOR_MANIFEST)
    forbidden=prior['dictionary_representation']['candidate']['file']
    protected_dictionaries={forbidden}
    outer=prior.get('checkpoint33_dictionary_outer_representation',{})
    if outer:protected_dictionaries.add(outer['selected_bundle']['file'])
    for index,original in enumerate(list(bundles)):
        choice=extra_repack['entries'].get(original['file'])
        if choice is None or not choice['use_candidate']:continue
        assert original['file'] not in protected_dictionaries,'Inherited dictionary representations must remain unchanged'
        assert choice['status']=='PASS_IDENTICAL_UNCOMPRESSED_TAR'
        assert choice['original']==original
        candidate=extra_repack_path.parent/choice['candidate_file']
        assert candidate.stat().st_size==choice['candidate_bytes'] and sha(candidate)==choice['candidate_sha256']
        identity=(choice['tar_bytes'],choice['tar_sha256'])
        assert tar_stream_identity(bundle_paths[index])==identity
        assert tar_stream_identity(candidate)==identity
        bundles[index]=choice['bundle'];bundle_paths[index]=candidate
        extra_repack_selection.append(choice)

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
manifest['inherited_transport_repairs']=prior['inherited_transport_repairs']
manifest['dictionary_representation']=prior['dictionary_representation']
for field in ('checkpoint33_exact_member_repair','checkpoint33_dictionary_outer_representation'):
    if field in prior:manifest[field]=prior[field]
# Preserve the tested streaming dictionary-first extraction order.
renamed={row['original']['file']:row['bundle']['file'] for row in extra_repack_selection}
old_order=[renamed.get(name,name) for name in prior.get('restore_bundle_order',[])]
all_names=[b['file'] for b in bundles]
assert all(name in all_names for name in old_order)
manifest['restore_bundle_order']=old_order+[name for name in all_names if name not in old_order]
assert manifest['object_transforms']==prior['object_transforms']
assert manifest['transport_support_files']==prior['transport_support_files']
assert manifest['dictionary_representation']==prior['dictionary_representation']
for support in manifest['transport_support_files']:
    source=BASE/'checkpoint34_encoding'/support['file']
    assert source.stat().st_size==support['bytes'] and sha(source)==support['sha256']
    shutil.copyfile(source,STAGE/support['file'])
manifest_path = STAGE/'checkpoint35_transport_manifest.json'
atomic_json(manifest_path, manifest)
restore = (BASE/'checkpoint34_encoding/restore_checkpoint.py').read_text().replace('checkpoint34', 'checkpoint35')
compile(restore, 'restore_checkpoint.py', 'exec')
(STAGE/'restore_checkpoint.py').write_text(restore)
readme = f'''# Complete immutable checkpoint35

Extract this ZIP and run `python3 restore_checkpoint.py`. The current paper and registers are directly readable. The delivered standard-library restorer checks all {len(files):,} research files against their exact original sizes and SHA-256 hashes. Every compressed shard and decoder is included; no previous checkpoint download is needed.

All verified predecessor content is retained. Selected earlier tar streams may use a smaller compressed representation after exact uncompressed size and SHA-256 comparison; the full original project bytes are unchanged. Its complete file and content manifest is also preserved in the research records. Historical PDF copy/add records and lossless PNG reconstruction preserve the original bytes, not only appearances. Every prior member codec and its shared dictionary is retained; all decoder modules are included and hash-checked. The maximum LZMA dictionary is64MiB.

The new closed TAR streams may likewise use verified stronger compression. Their original receipts, full-stream size/SHA comparisons, repaired builder and recompression program are retained under checkpoint35_transport. The frozen project file list, original sizes, hashes and capture time are the same completed checkpoint35 freeze. Four JSON metadata entries use standard ZIP LZMA compression; Python's standard-library zipfile extractor supports this method. Their extracted bytes are unchanged, and the standalone restore verification checks the full snapshot after extraction.

Frozen at {record['frozen_utc']}. The report remains INCOMPLETE. The complete proofs, working notes, programs, certificates, logs, rendered pages and preserved attempts are included. The supplied and external source-payload exclusions are documented in the report. The resumable freeze and shard receipts are included under checkpoint35_transport.
'''
partial = STAGE/'checkpoint35.partial'
if partial.exists():
    partial.rename(STAGE/('checkpoint35.interrupted_'+str(time.time_ns())))
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
        archive.write(STAGE/name, 'checkpoint35_transport/'+name, compress_type=zipfile.ZIP_LZMA)
    archive.write(ROOT/'code/make_checkpoint35.py', 'checkpoint35_transport/make_checkpoint35.py')
    archive.write(ROOT/'code/freeze_checkpoint35.py','checkpoint35_transport/freeze_checkpoint35.py')
    for path in sorted(STAGE.glob('checkpoint35_new_content_*.tar.xz.json')):
        archive.write(path, 'checkpoint35_transport/'+path.name)
    archive.write(ROOT/'code/repack_checkpoint35_closed_streams.py','checkpoint35_transport/repack_checkpoint35_closed_streams.py')
    if new_repack is not None:
        archive.write(new_repack_path,'checkpoint35_transport/new_stream_recompression_manifest.json')
    if extra_repack is not None:
        archive.write(extra_repack_path,'checkpoint35_transport/extra_predecessor_stream_recompression_manifest.json')
    archive.writestr('READ_FIRST.md', readme)
for name, path in paths.items():
    assert path.stat().st_size == files[name]['bytes'] and sha(path) == files[name]['sha256']
measurement={'status':'MEASURED_COMPLETE_ENCODED_ARCHIVE','frozen_manifest_sha256':sha(frozen_manifest),
 'prior_archive_bytes':creation['bytes'],'prior_archive_sha256':creation['sha256'],
 'candidate_archive_bytes':partial.stat().st_size,'size_limit':536870912,
 'over_limit_bytes':max(0,partial.stat().st_size-536870912),
 'new_unique_contents':len(payload),'new_closed_shards':len(groups),
 'new_bundle_bytes':sum(p.stat().st_size for p in bundle_paths[len(prior['bundles']):]),
 'all_bundle_bytes':sum(p.stat().st_size for p in bundle_paths),
 'new_stream_recompression_saving':sum(x['saving'] for x in new_repack_selection),
 'predecessor_stream_recompression_saving':sum(x['saving'] for x in extra_repack_selection),
 'dictionary_representation_unchanged':manifest['dictionary_representation']==prior['dictionary_representation'],
 'new_payloads':[{'packed_name':x[0],'bytes':x[1].stat().st_size,'suffix':x[2]} for x in payload]}
atomic_json(STAGE/'checkpoint35_size_measurement.json',measurement)
if measurement['over_limit_bytes']:
    saved=STAGE/('checkpoint35.oversize_'+str(time.time_ns()))
    partial.rename(saved)
    measurement['preserved_oversize_candidate']=str(saved)
    atomic_json(STAGE/'checkpoint35_size_measurement.json',measurement)
    print(json.dumps({'status':'MEASURED_SIZE_REPAIR_REQUIRED','bytes':measurement['candidate_archive_bytes'],
       'over_limit_bytes':measurement['over_limit_bytes'],'preserved':str(saved)}),flush=True)
    raise SystemExit(42)

result = {'status': 'CREATED', 'path': str(TARGET), 'bytes': partial.stat().st_size,
          'sha256': sha(partial), 'snapshot_files': len(files), 'record': record,
          'new_unique_contents': len(payload), 'closed_shards': len(bundles)}
atomic_json(STAGE/'checkpoint35_creation.json', result)
partial.rename(TARGET)
print(json.dumps(result, indent=2), flush=True)
