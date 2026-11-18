"""Prepare the next exact encoder, carrying every31 member transform."""
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parents[1]
original=ROOT/'records/attempts/checkpoint31_size_gate_repair/make_checkpoint31.py'
old=original.read_text()
tail=old[old.index('paths = {n: frozen/n for n in files}'):]
tail=tail.replace('checkpoint31','checkpoint32').replace('checkpoint30','checkpoint31')
tail=tail.replace('checkpoint_31','checkpoint_32')

header='''"""Complete hourly checkpoint32 after the original32 freeze.

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
    tmp.write_text(json.dumps(value,indent=2)+'\\n');tmp.replace(path)
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
'''

needle="manifest_path = STAGE/'checkpoint32_transport_manifest.json'"
insert="""# Carry the complete prior member layer before new raw/PNG/copy-add contents.
manifest['object_transforms']=prior.get('object_transforms',[])
manifest['transport_support_files']=prior.get('transport_support_files',[])
manifest['inherited_transport_repairs']=prior.get('transport_repairs',{})
for support in manifest['transport_support_files']:
    source=BASE/'checkpoint31_encoding'/support['file']
    assert source.stat().st_size==support['bytes'] and sha(source)==support['sha256']
    shutil.copyfile(source,STAGE/support['file'])
"""
assert needle in tail;tail=tail.replace(needle,insert+needle)
needle2="""    for name in ('checkpoint_copy_add.py', 'checkpoint_png_codec.py'):
        archive.write(frozen/'S6_06_BLIND/code'/name, name)"""
replace2="""    for support in manifest['transport_support_files']:
        archive.write(STAGE/support['file'],support['file'])"""
assert needle2 in tail;tail=tail.replace(needle2,replace2)
tail=tail.replace('The maximum LZMA dictionary is64MiB.',
 'Every prior member codec and its shared dictionary is retained; all decoder modules are included and hash-checked. The maximum LZMA dictionary is64MiB.')
tail=tail.replace("        archive.write(frozen/'S6_06_BLIND/code/make_checkpoint32.py', 'checkpoint32_transport/make_checkpoint32.py')",
 "        archive.write(ROOT/'code/make_checkpoint32.py', 'checkpoint32_transport/make_checkpoint32.py')")
# The existing line has four spaces in the preserved builder.
tail=tail.replace("    archive.write(frozen/'S6_06_BLIND/code/make_checkpoint32.py', 'checkpoint32_transport/make_checkpoint32.py')",
 "    archive.write(ROOT/'code/make_checkpoint32.py', 'checkpoint32_transport/make_checkpoint32.py')\n    archive.write(ROOT/'code/freeze_checkpoint32.py','checkpoint32_transport/freeze_checkpoint32.py')\n    archive.write(ROOT/'code/prepare_checkpoint32_encoder.py','checkpoint32_transport/prepare_checkpoint32_encoder.py')")
source=header+tail
compile(source,'make_checkpoint32.py','exec')
dest=ROOT/'code/make_checkpoint32.py';assert not dest.exists();dest.write_text(source)
verifier=(ROOT/'code/verify_checkpoint31.py').read_text().replace('checkpoint31','checkpoint32').replace('checkpoint_31','checkpoint_32')
compile(verifier,'verify_checkpoint32.py','exec')
(ROOT/'code/verify_checkpoint32.py').write_text(verifier)
rec={'status':'PREPARED_EXACT_TRANSFORM_INHERITING_ENCODER',
 'source_builder_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),
 'new_builder_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
 'new_verifier_sha256':hashlib.sha256(verifier.encode()).hexdigest(),
 'scope':'Separate immutable32 freeze; all31 content/member transforms, shared dictionaries, decoder modules, predecessor files and patch order preserved. Encoding waits for complete31 standalone verification.'}
(ROOT/'records/checkpoint32_encoder_preparation.json').write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps(rec,indent=2))
