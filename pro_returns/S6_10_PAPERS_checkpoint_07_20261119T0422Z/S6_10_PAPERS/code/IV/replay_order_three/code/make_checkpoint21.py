"""One complete immutable hourly snapshot, reusing verified lossless payloads.

All current files are represented byte for byte. The prior binary bundle is
reused solely as a compression dictionary/container; every final file is
verified by the new full manifest. No dependence on another downloaded ZIP
remains after this ZIP is delivered.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,zipfile,tarfile,io,lzma,re,shutil,time
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
TARGET=BASE/'S6_06_BLIND_checkpoint_21.zip'
STAGE=BASE/'checkpoint21_encoding';STAGE.mkdir(exist_ok=True)
assert not TARGET.exists()
prior=json.loads((BASE/'checkpoint19_transport_manifest.json').read_text())
with zipfile.ZipFile(BASE/'S6_06_BLIND_checkpoint_19.zip') as old:
    immediate=set(old.namelist())
basepacked=set(prior['files'])-immediate
basebundle=BASE/'checkpoint19_binary_artifacts.tar.xz'
assert basebundle.is_file()
def digest(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def packed(name):
    return Path(name).suffix.lower() in {'.png','.pdf','.log','.out','.err','.aux','.toc'} and name!=ROOT.name+'/S6_06_BLIND_paper.pdf'
def excluded(rel):
    source=any(rel.startswith(x) for x in ('records/primary_sources/','records/external_source_cache/','records/sources/','records/part5_comparison/'))
    return (source and Path(rel).suffix.lower() in ('.pdf','.txt','.png','.jpg','.jpeg','.tif','.tiff','.html')) or rel=='records/AC26_original_extracted.txt' or bool(re.fullmatch(r'records/web_\d+\.json',rel)) or rel=='code/part1/ocr_wall.out'
now=datetime.now(timezone.utc).isoformat()
rec={'checkpoint':TARGET.name,'created_utc':now,'due_utc':'2026-11-17T20:49:44+00:00','recovery_base':19,'checkpoint20':'Unconfirmed after execution outage; no uploaded checkpoint20 exists in this record.','blind_part5_sha256':{f:digest(ROOT/f) for f in ('notes/part5.tex','notes/part5_blind.md')}}
assert rec['blind_part5_sha256']['notes/part5.tex']=='f7b2188bbd5fc453780421599b65168141c8ed09480b1396794f02f41a680e0f'
assert rec['blind_part5_sha256']['notes/part5_blind.md']=='ffdac7780a3d5c35565e31e6bb1bebf459e0f7dc75355e19fc216b5ba4b9a1e4'
(ROOT/'records/checkpoint_21.json').write_text(json.dumps(rec,indent=2)+'\n')
with (ROOT/'S6_06_BLIND_literature_log.md').open('a') as f:f.write(f'\n| {now} | {TARGET.name} | Complete hourly checkpoint after restoration from checkpoint19 and conversation | Part5 immutable hashes reverified; missing checkpoint20 and reconstructed post19 files explicitly documented. |\n')
manifest={'snapshot':rec,'files':{},'base_bundle':'checkpoint19_binary_artifacts.tar.xz','delta_bundle':'checkpoint21_new_artifacts.tar.xz','scope':'Standalone full snapshot, all current artifact paths and bytes verified; supplied attachments and previously documented external source payloads excluded.'}
paths={};covered=[];delta=[];direct=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(ROOT).as_posix()
    if excluded(rel):continue
    name=p.relative_to(BASE).as_posix();info={'bytes':p.stat().st_size,'sha256':digest(p)}
    manifest['files'][name]=info;paths[name]=p
    if packed(name):
        if name in basepacked and prior['files'][name]==info:covered.append(name)
        else:delta.append(name)
    else:direct.append(name)
tarpath=STAGE/'checkpoint21_new_artifacts.tar.xz';assert not tarpath.exists()
seen={}
with lzma.open(tarpath,'xb',preset=6) as xz:
 with tarfile.open(fileobj=xz,mode='w|',format=tarfile.PAX_FORMAT) as tar:
  for name in delta:
    p=paths[name];data=p.read_bytes();h=hashlib.sha256(data).hexdigest();assert h==manifest['files'][name]['sha256']
    item=tarfile.TarInfo(name);item.mode=0o644;item.mtime=int(p.stat().st_mtime)
    if h in seen:item.type=tarfile.LNKTYPE;item.linkname=seen[h];tar.addfile(item)
    else:item.size=len(data);tar.addfile(item,io.BytesIO(data));seen[h]=name
manifest['packed_files']=covered+delta
manifest['bundles']=[{'file':basebundle.name,'sha256':digest(basebundle)},{'file':tarpath.name,'sha256':digest(tarpath)}]
restore=r'''"""Restore every current snapshot file and verify its size and SHA-256."""
from pathlib import Path
import hashlib,json,tarfile,tempfile,shutil
base=Path(__file__).resolve().parent
m=json.loads((base/'checkpoint21_transport_manifest.json').read_text())
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def target(root,name):
 p=(root/name).resolve()
 if not p.is_relative_to(root.resolve()):raise ValueError('Unsafe archive path')
 return p
with tempfile.TemporaryDirectory(prefix='.checkpoint21_restore_',dir=base) as tmp:
 stage=Path(tmp)
 for bundle in m['bundles']:
  archive=base/bundle['file']
  assert sha(archive)==bundle['sha256'],'Bundle checksum mismatch'
  with tarfile.open(archive,'r|xz') as tar:
   for member in tar:
    out=target(stage,member.name);out.parent.mkdir(parents=True,exist_ok=True)
    if member.islnk():
     old=target(stage,member.linkname)
     with old.open('rb') as source,out.open('wb') as sink:shutil.copyfileobj(source,sink)
    else:
     source=tar.extractfile(member)
     if source is None:raise ValueError('Missing packed bytes')
     with source,out.open('wb') as sink:shutil.copyfileobj(source,sink)
 for name in m['packed_files']:
  source=target(stage,name);info=m['files'][name]
  assert source.stat().st_size==info['bytes'] and sha(source)==info['sha256'],name
  out=target(base,name);out.parent.mkdir(parents=True,exist_ok=True)
  if out.exists():
   if out.stat().st_size!=info['bytes'] or sha(out)!=info['sha256']:raise ValueError('Refusing to overwrite changed file: '+name)
  else:shutil.copyfile(source,out)
for name,info in m['files'].items():
 p=target(base,name)
 assert p.stat().st_size==info['bytes'] and sha(p)==info['sha256'],name
print('PASS: restored and verified all '+str(len(m['files']))+' snapshot files.')
'''
manifestpath=STAGE/'checkpoint21_transport_manifest.json';manifestpath.write_text(json.dumps(manifest,indent=2)+'\n')
(STAGE/'restore_checkpoint.py').write_text(restore)
readme='''# Checkpoint 21: complete immutable snapshot

Extract this ZIP, then run `python3 restore_checkpoint.py`.
The current paper, TeX sources, report, code and proof notes are directly
available. Two included lossless binary bundles hold every archived PDF,
page render and build log. The restoration program materializes independent
files and verifies every size and SHA-256 against the full snapshot manifest.
This ZIP is standalone: no earlier checkpoint download is required.

Checkpoint19 was restored after an execution-environment loss. Later work
was reconstructed from the retained conversation; exact replay recoveries
and mathematical reconstructions are identified in records/recovery_20261117
and the other recovery records. Checkpoint20 was never confirmed or uploaded.
The immutable Part5 proof hashes are reverified. The report remains INCOMPLETE.
'''
partial=STAGE/'checkpoint21.partial';assert not partial.exists()
with zipfile.ZipFile(partial,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for name in direct:
  p=paths[name];assert digest(p)==manifest['files'][name]['sha256'],name
  z.write(p,name)
 z.write(basebundle,basebundle.name,compress_type=zipfile.ZIP_STORED)
 z.write(tarpath,tarpath.name,compress_type=zipfile.ZIP_STORED)
 z.write(manifestpath,manifestpath.name)
 z.write(STAGE/'restore_checkpoint.py','restore_checkpoint.py')
 z.writestr('READ_FIRST.md',readme)
for name,p in paths.items():assert p.stat().st_size==manifest['files'][name]['bytes'] and digest(p)==manifest['files'][name]['sha256'],name
assert partial.stat().st_size<=536870912,partial.stat().st_size
partial.rename(TARGET)
print(json.dumps({'status':'CREATED','path':str(TARGET),'bytes':TARGET.stat().st_size,'sha256':digest(TARGET),'snapshot_files':len(paths),'unchanged_packed_files':len(covered),'new_or_changed_packed_files':len(delta),'direct_files':len(direct),'record':rec},indent=2))
