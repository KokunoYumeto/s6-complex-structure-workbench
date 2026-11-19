"""Freeze the complete hourly checkpoint24 and preserve every original byte."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, zipfile, tarfile, lzma, re, shutil, time
from checkpoint_copy_add import encode, decode
from checkpoint_png_codec import encode as encode_png, decode as decode_png

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
TARGET = BASE / 'S6_06_BLIND_checkpoint_24.zip'
assert not TARGET.exists()
STAGE = BASE / 'checkpoint24_encoding'
assert STAGE.is_dir()
prior = json.loads((BASE / 'checkpoint24_base_content_manifest.json').read_text())
verification = json.loads((ROOT / 'records/checkpoint24_content_base_verification.json').read_text())
assert prior['status'] == 'COMPLETE' and verification['status'] == 'PASS'

def sha(path):
    with path.open('rb') as source:
        return hashlib.file_digest(source, 'sha256').hexdigest()

def excluded(rel):
    source = any(rel.startswith(prefix) for prefix in (
        'records/primary_sources/', 'records/external_source_cache/',
        'records/sources/', 'records/part5_comparison/'))
    return ((source and Path(rel).suffix.lower() in
             ('.pdf', '.txt', '.png', '.jpg', '.jpeg', '.tif', '.tiff', '.html'))
            or rel == 'records/AC26_original_extracted.txt'
            or bool(re.fullmatch(r'records/web_\d+\.json', rel))
            or rel == 'code/part1/ocr_wall.out')

frozen = STAGE / 'frozen'
record = json.loads((frozen / 'S6_06_BLIND/records/checkpoint_24.json').read_text())
progress = [json.loads(line) for line in (BASE/'checkpoint24_waiter.out').read_text().splitlines() if line.startswith('{')]
freeze = next(row for row in progress if row.get('status') == 'FROZEN')
record['frozen_utc'] = freeze['utc']
files, paths, unique = {}, {}, {}
for path in sorted(frozen.rglob('*')):
    if not path.is_file():continue
    name = path.relative_to(frozen).as_posix()
    info = {'bytes':path.stat().st_size,'sha256':sha(path)}
    files[name], paths[name] = info, path
    unique.setdefault(info['sha256'], (name,path,info))
assert len(files) == freeze['files'] == 8748
print(json.dumps({'status':'RESUMED_FROZEN_TREE','files':len(files),'frozen_utc':record['frozen_utc']}),flush=True)

bundle_paths, bundles = [], []
for bundle in prior['bundles']:
    path = Path(bundle['local_path'])
    assert path.stat().st_size == bundle['bytes'] and sha(path) == bundle['sha256']
    bundle_paths.append(path)
    bundles.append({key: value for key, value in bundle.items() if key != 'local_path'})
contents = dict(prior['contents'])
patch_order = list(prior['patch_order'])
payload = []
reference_name = 'S6_06_BLIND/S6_06_BLIND_paper.pdf'
reference = BASE / 'checkpoint23_encoding/frozen' / reference_name
reference_sha = prior['files'][reference_name]['sha256']
assert sha(reference) == reference_sha
reference_bytes = reference.read_bytes()
for h, (name, path, info) in unique.items():
    if h in contents:
        assert contents[h]['bytes'] == info['bytes']
        continue
    raw = None
    if name.endswith('.pdf') and info['bytes'] > 1000000:
        raw = path.read_bytes()
        patch, stats = encode(reference_bytes, raw)
        assert decode(reference_bytes, patch) == raw
        if len(patch) < len(raw) * .92:
            encoded = STAGE / (h + '.copyadd')
            encoded.write_bytes(patch)
            contents[h] = {'bytes': len(raw), 'storage': 'copy_add',
                           'base_sha256': reference_sha, 'patch_name': 'patches/' + h,
                           'patch_sha256': sha(encoded), 'stats': stats}
            patch_order.append(h)
            payload.append(('patches/' + h, encoded, '.pdfpatch', name))
            continue
    if name.endswith('.png'):
        raw = path.read_bytes()
        packed = encode_png(raw)
        if packed is not None:
            assert decode_png(packed) == raw
            encoded = STAGE / (h + '.pngcodec')
            encoded.write_bytes(packed)
            contents[h] = {'bytes': len(raw), 'storage': 'png',
                           'encoded_name': 'png/' + h, 'encoded_sha256': sha(encoded)}
            payload.append(('png/' + h, encoded, '.png', name))
            continue
    contents[h] = {'bytes': info['bytes'], 'storage': 'raw', 'name': 'content/' + h}
    payload.append(('content/' + h, path, Path(name).suffix, name))

payload.sort(key=lambda row: (row[2], row[3]))
delta = STAGE / 'checkpoint24_new_content.tar.xz'
with lzma.open(delta, 'xb', filters=[{'id': lzma.FILTER_LZMA2, 'preset': 3,
                                    'dict_size': 64 * 1024 * 1024}]) as stream:
    with tarfile.open(fileobj=stream, mode='w|', format=tarfile.PAX_FORMAT) as tar:
        for index, (name, path, suffix, source_name) in enumerate(payload):
            item = tarfile.TarInfo(name)
            item.mode, item.mtime, item.size = 0o644, 0, path.stat().st_size
            with path.open('rb') as source:
                tar.addfile(item, source)
            if index % 100 == 0:
                print(json.dumps({'packed_new': index, 'of': len(payload), 'path': source_name}), flush=True)
bundles.append({'file': delta.name, 'bytes': delta.stat().st_size, 'sha256': sha(delta)})
bundle_paths.append(delta)
direct = ['S6_06_BLIND/' + name for name in (
    'S6_06_BLIND_paper.pdf', 'S6_06_BLIND_paper.tex', 'S6_06_BLIND_report.md',
    'S6_06_BLIND_results.csv', 'S6_06_BLIND_literature_log.md')]
manifest = {
    'snapshot': record, 'files': files, 'contents': contents,
    'patch_order': patch_order, 'bundles': bundles, 'direct_files': direct,
    'predecessor_files': prior['files'],
    'scope': 'Complete standalone snapshot, including the complete verified predecessor content. Every research file restores to its exact original size and SHA256. Supplied and external source payload exclusions are retained.',
}
manifest_path = STAGE / 'checkpoint24_transport_manifest.json'
manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
restore = r'''"""Restore all frozen research bytes and independently verify every SHA256."""
from pathlib import Path
import hashlib,json,tarfile,tempfile,shutil
from checkpoint_copy_add import decode
from checkpoint_png_codec import decode as decode_png
base=Path(__file__).resolve().parent
m=json.loads((base/'checkpoint24_transport_manifest.json').read_text())
def sha(path):
 with path.open('rb') as source:return hashlib.file_digest(source,'sha256').hexdigest()
def target(root,name):
 path=(root/name).resolve()
 if not path.is_relative_to(root.resolve()):raise ValueError('Unsafe archive path')
 return path
with tempfile.TemporaryDirectory(prefix='.checkpoint24_restore_',dir=base) as temporary:
 stage=Path(temporary)
 for index,bundle in enumerate(m['bundles']):
  archive=base/bundle['file']
  assert archive.stat().st_size==bundle['bytes'] and sha(archive)==bundle['sha256']
  with tarfile.open(archive,'r|xz') as tar:
   for member in tar:
    if not member.isfile():raise ValueError('Unexpected non-file payload')
    out=target(stage,member.name);out.parent.mkdir(parents=True,exist_ok=True)
    source=tar.extractfile(member)
    if source is None:raise ValueError('Missing packed bytes')
    with source,out.open('wb') as sink:shutil.copyfileobj(source,sink)
  if index%10==0:print('Extracted bundle '+str(index+1)+'/'+str(len(m['bundles'])),flush=True)
 for h,info in m['contents'].items():
  if info['storage']!='png':continue
  packed=target(stage,info['encoded_name']);assert sha(packed)==info['encoded_sha256']
  out=target(stage,'content/'+h);out.parent.mkdir(parents=True,exist_ok=True)
  out.write_bytes(decode_png(packed.read_bytes()))
  assert out.stat().st_size==info['bytes'] and sha(out)==h
 for h in m['patch_order']:
  info=m['contents'][h];assert info['storage']=='copy_add'
  reference=target(stage,'content/'+info['base_sha256']);assert sha(reference)==info['base_sha256']
  patch=target(stage,info['patch_name']);assert sha(patch)==info['patch_sha256']
  out=target(stage,'content/'+h);out.write_bytes(decode(reference.read_bytes(),patch.read_bytes()))
  assert out.stat().st_size==info['bytes'] and sha(out)==h
 for h,info in m['contents'].items():
  out=target(stage,'content/'+h)
  assert out.stat().st_size==info['bytes'] and sha(out)==h
 for name,info in m['predecessor_files'].items():
  source=target(stage,'content/'+info['sha256'])
  assert source.stat().st_size==info['bytes'] and sha(source)==info['sha256'],name
 for name,info in m['files'].items():
  source=target(stage,'content/'+info['sha256'])
  assert source.stat().st_size==info['bytes'] and sha(source)==info['sha256'],name
  out=target(base,name);out.parent.mkdir(parents=True,exist_ok=True)
  if out.exists():assert out.stat().st_size==info['bytes'] and sha(out)==info['sha256'],'Refusing changed file: '+name
  else:shutil.copyfile(source,out)
for name,info in m['files'].items():
 path=target(base,name);assert path.stat().st_size==info['bytes'] and sha(path)==info['sha256'],name
print('PASS: restored and verified all '+str(len(m['files']))+' checkpoint24 files; complete predecessor bytes also verified.',flush=True)
'''
compile(restore, 'restore_checkpoint.py', 'exec')
(STAGE / 'restore_checkpoint.py').write_text(restore)
readme = f'''# Complete immutable checkpoint24

Extract this ZIP and run `python3 restore_checkpoint.py`. The current paper and registers are directly readable. Restoration uses Python's standard library and verifies every one of the {len(files):,} research files by exact original size and SHA-256. All bundles and decoders are included; no earlier checkpoint download is needed.

The manifest retains the full predecessor file map and every predecessor content object. The delivered restorer verifies those bytes as well as the current snapshot. Historical PDFs use exact copy/add instructions. The PNG codec preserves all original chunks and requires identical reconstructed compressed bytes, with the encoding zlib version recorded inside each payload. No image pixels, layout, PDF content or original research bytes are changed. The maximum LZMA dictionary is64MiB.

Frozen at {record['frozen_utc']}. The report remains INCOMPLETE. All proofs, code, certificates, logs, renders and preserved attempts are included. The documented supplied/external source-payload exclusions remain in force.
'''
partial = STAGE / 'checkpoint24.partial'
with zipfile.ZipFile(partial, 'x', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for name in direct:
        archive.write(paths[name], name)
    for path in bundle_paths:
        archive.write(path, path.name, compress_type=zipfile.ZIP_STORED)
    archive.write(manifest_path, manifest_path.name)
    archive.write(STAGE / 'restore_checkpoint.py', 'restore_checkpoint.py')
    for name in ('checkpoint_copy_add.py', 'checkpoint_png_codec.py'):
        archive.write(ROOT / 'code' / name, name)
    archive.write(ROOT/'code/resume_checkpoint24.py','checkpoint24_transport/resume_checkpoint24.py')
    archive.write(ROOT/'records/checkpoint24_encoding_interruption.json','checkpoint24_transport/interruption.json')
    archive.writestr('READ_FIRST.md', readme)
for name, path in paths.items():
    assert path.stat().st_size == files[name]['bytes'] and sha(path) == files[name]['sha256']
assert partial.stat().st_size <= 536870912, partial.stat().st_size
partial.rename(TARGET)
result = {'status': 'CREATED', 'path': str(TARGET), 'bytes': TARGET.stat().st_size,
          'sha256': sha(TARGET), 'snapshot_files': len(files), 'record': record,
          'new_unique_contents': len(payload)}
(STAGE / 'checkpoint24_creation.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2), flush=True)
