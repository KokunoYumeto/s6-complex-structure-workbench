"""Losslessly encode the SAME frozen checkpoint below the transfer limit.

The original hourly ZIP is immutable. Every original member remains represented
byte for byte. Repeated PNG byte streams use standard tar hardlink records in
one nested image bundle; restore_checkpoint.py materializes independent copies
and verifies the entire original snapshot. No later research is added.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib, io, json, shutil, subprocess, tarfile, zipfile

ROOT=Path(__file__).resolve().parents[1]
ORIGINAL=ROOT.parent/'S6_06_BLIND_checkpoint_17.zip'
STAGE=ROOT.parent/'checkpoint17_transfer'
STAGE.mkdir(exist_ok=True)
TARGET=STAGE/ORIGINAL.name
if TARGET.exists():
    raise SystemExit('Refusing to overwrite a transfer archive')
TAR=STAGE/'checkpoint17_qa_images.tar'
COMPRESSED=STAGE/'checkpoint17_qa_images.tar.xz'
if COMPRESSED.exists():
    raise SystemExit('Refusing to overwrite compressed images')
if TAR.exists():
    raise SystemExit('Refusing to overwrite an image bundle')

restore=r'''"""Restore and verify every byte of the original hourly snapshot."""
from pathlib import Path
import hashlib,json,shutil,tarfile
base=Path(__file__).resolve().parent
manifest=json.loads((base/'checkpoint17_transport_manifest.json').read_text())
bundle=base/'checkpoint17_qa_images.tar.xz'
def destination(name):
    p=(base/name).resolve()
    if not p.is_relative_to(base.resolve()):
        raise ValueError('Unsafe archive path')
    return p
with tarfile.open(bundle,'r:xz') as archive:
    for member in archive.getmembers():
        target=destination(member.name)
        target.parent.mkdir(parents=True,exist_ok=True)
        expected=manifest['files'][member.name]['sha256']
        if target.exists():
            if hashlib.sha256(target.read_bytes()).hexdigest()!=expected:
                raise ValueError('Refusing to overwrite changed file: '+member.name)
            continue
        stream=archive.extractfile(member)
        if stream is None:
            raise ValueError('Missing image data: '+member.name)
        with stream, target.open('xb') as out:
            shutil.copyfileobj(stream,out)
for name,info in manifest['files'].items():
    p=destination(name)
    if p.stat().st_size!=info['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=info['sha256']:
        raise ValueError('Snapshot verification failed: '+name)
print('PASS: restored and verified all '+str(len(manifest['files']))+' original files.')
'''

manifest={'original_archive':ORIGINAL.name,
 'original_archive_sha256':hashlib.sha256(ORIGINAL.read_bytes()).hexdigest(),
 'original_archive_bytes':ORIGINAL.stat().st_size,
 'snapshot_started_utc':json.loads((ROOT.parent/'checkpoint17_create.out').read_text())['record']['created_utc'],
 'encoding_utc':datetime.now(timezone.utc).isoformat(),
 'purpose':'Transfer encoding of the same immutable checkpoint17; no later work included.',
 'files':{}}
seen={}; images=links=0
with zipfile.ZipFile(ORIGINAL) as source, tarfile.open(TAR,'x',format=tarfile.PAX_FORMAT) as packed:
    for member in source.infolist():
        data=source.read(member)
        digest=hashlib.sha256(data).hexdigest()
        manifest['files'][member.filename]={'bytes':len(data),'sha256':digest}
        if not member.filename.endswith('.png'):
            continue
        item=tarfile.TarInfo(member.filename)
        item.mode=0o644
        item.mtime=int(datetime(*member.date_time,tzinfo=timezone.utc).timestamp())
        if digest in seen:
            item.type=tarfile.LNKTYPE
            item.linkname=seen[digest]
            packed.addfile(item)
            links+=1
        else:
            item.size=len(data)
            packed.addfile(item,io.BytesIO(data))
            seen[digest]=member.filename
        images+=1

with COMPRESSED.open('xb') as output:
    subprocess.run(['xz','-T2','-6','-c',str(TAR)],stdout=output,check=True)

readme='''# Checkpoint 17: complete frozen snapshot

This package contains the exact snapshot taken at 16:49:44 UTC on 17 November
2026. The original immutable ZIP exceeded the file-transfer limit. To preserve
every file, repeated QA images are represented by standard tar hardlink entries
inside the losslessly XZ-compressed checkpoint17_qa_images.tar.xz. All other original files retain their paths
and bytes. No later research has been included in this package.

After extracting this ZIP, run:

    python3 restore_checkpoint.py

The script creates independent image files at their original paths and checks
the size and SHA-256 of EVERY original file against the frozen manifest. It
refuses to overwrite any changed file. Python's standard library is sufficient.
The paper, report, TeX sources, proof notes, scripts and data are immediately
available before this image-restoration step.

The original archive's SHA-256 is recorded in checkpoint17_transport_manifest.json.
The original archive remains unchanged. This is a transfer encoding of that
same checkpoint, not a second checkpoint or a later research snapshot.
'''
with zipfile.ZipFile(ORIGINAL) as source, zipfile.ZipFile(TARGET,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as dest:
    for member in source.infolist():
        if not member.filename.endswith('.png'):
            dest.writestr(member,source.read(member))
    dest.write(COMPRESSED,'checkpoint17_qa_images.tar.xz',compress_type=zipfile.ZIP_STORED)
    dest.writestr('restore_checkpoint.py',restore)
    dest.writestr('checkpoint17_transport_manifest.json',json.dumps(manifest,indent=2)+'\n')
    dest.writestr('READ_FIRST.md',readme)

assert TARGET.stat().st_size<=536870912,TARGET.stat().st_size
result={'status':'ENCODED','original_archive':str(ORIGINAL),
 'original_sha256':manifest['original_archive_sha256'],
 'original_bytes':manifest['original_archive_bytes'],
 'transfer_archive':str(TARGET),'transfer_bytes':TARGET.stat().st_size,
 'transfer_sha256':hashlib.sha256(TARGET.read_bytes()).hexdigest(),
 'original_files':len(manifest['files']),'images':images,'exact_duplicate_images':links,
 'image_bundle_codec':'XZ/LZMA2 preset6 two threads, stored in outerZIP',
 'compressed_image_bytes':COMPRESSED.stat().st_size,
 'verification':'pending full extraction and byte verification'}
(ROOT/'records/checkpoint17_transfer_encoding.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
