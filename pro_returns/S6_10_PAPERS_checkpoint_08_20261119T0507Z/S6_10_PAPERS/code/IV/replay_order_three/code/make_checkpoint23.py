"""Create one complete immutable checkpoint with content-addressed lossless bytes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,zipfile,tarfile,io,lzma,re,shutil
from checkpoint_copy_add import encode,decode
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
TARGET=BASE/'S6_06_BLIND_checkpoint_23.zip';assert not TARGET.exists()
STAGE=BASE/'checkpoint23_encoding';STAGE.mkdir(exist_ok=False)
prior=json.loads((BASE/'checkpoint23_base_content_manifest.json').read_text());assert prior['status']=='COMPLETE'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
basebundle=BASE/prior['bundle']['file'];assert sha(basebundle)==prior['bundle']['sha256']
def excluded(rel):
 source=any(rel.startswith(x) for x in ('records/primary_sources/','records/external_source_cache/','records/sources/','records/part5_comparison/'))
 return (source and Path(rel).suffix.lower() in ('.pdf','.txt','.png','.jpg','.jpeg','.tif','.tiff','.html')) or rel=='records/AC26_original_extracted.txt' or bool(re.fullmatch(r'records/web_\d+\.json',rel)) or rel=='code/part1/ocr_wall.out'
record={'checkpoint':23,'due_utc':'2026-11-17T22:49:44+00:00','created_utc':datetime.now(timezone.utc).isoformat(),'verified_predecessor':22,'predecessor_sha256':'a8569992565dbc61be69488499c22dd871c0b2223ec6fd545fd8dfc570fe9e54','predecessor_library_id':'libfile_d7b619e483948191934e1e2a8d86dfd2','blind_part5_sha256':{name:sha(ROOT/name) for name in ('notes/part5.tex','notes/part5_blind.md')}}
assert record['blind_part5_sha256']['notes/part5.tex']=='f7b2188bbd5fc453780421599b65168141c8ed09480b1396794f02f41a680e0f'
assert record['blind_part5_sha256']['notes/part5_blind.md']=='ffdac7780a3d5c35565e31e6bb1bebf459e0f7dc75355e19fc216b5ba4b9a1e4'
(ROOT/'records/checkpoint_23.json').write_text(json.dumps(record,indent=2)+'\n')
with (ROOT/'S6_06_BLIND_literature_log.md').open('a') as f:f.write(f"\n| {record['created_utc']} | S6_06_BLIND_checkpoint_23.zip | Complete hourly snapshot after independently verified checkpoint22 | Full frozen proof/code/log/attempt content; Part5 immutable hashes reverified. |\n")
frozen=STAGE/'frozen';files={};paths={};unique={}
for p in sorted(ROOT.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(ROOT).as_posix()
 if excluded(rel):continue
 name=p.relative_to(BASE).as_posix();info={'bytes':p.stat().st_size,'sha256':sha(p)}
 copy=frozen/name;copy.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,copy)
 assert copy.stat().st_size==info['bytes'] and sha(copy)==info['sha256'],name
 files[name]=info;paths[name]=copy;unique.setdefault(info['sha256'],(name,copy,info))
record['frozen_utc']=datetime.now(timezone.utc).isoformat()
print(json.dumps({'status':'FROZEN','utc':record['frozen_utc'],'files':len(files)}),flush=True)
contents=prior['contents'].copy();patch_order=prior['patch_order'].copy();payload=[]
reference_name='S6_06_BLIND/S6_06_BLIND_paper.pdf'
reference=BASE/'checkpoint22_encoding/frozen'/reference_name
reference_sha=prior['files'][reference_name]['sha256'];assert sha(reference)==reference_sha
for h,(name,path,info) in unique.items():
 if h in contents:assert contents[h]['bytes']==info['bytes'];continue
 if name.endswith('.pdf') and info['bytes']>1000000:
  raw=path.read_bytes();patch,stats=encode(reference.read_bytes(),raw);assert decode(reference.read_bytes(),patch)==raw
  if len(patch)<len(raw)*.92:
   patchpath=STAGE/(h+'.copyadd');patchpath.write_bytes(patch)
   contents[h]={'bytes':len(raw),'storage':'copy_add','base_sha256':reference_sha,'patch_name':'patches/'+h,'patch_sha256':sha(patchpath),'stats':stats}
   patch_order.append(h);payload.append(('patches/'+h,patchpath,'.pdfpatch',name));continue
 contents[h]={'bytes':info['bytes'],'storage':'raw','name':'content/'+h}
 payload.append(('content/'+h,path,Path(name).suffix,name))
payload.sort(key=lambda row:(row[2],row[3]))
delta=STAGE/'checkpoint23_new_content.tar.xz'
with lzma.open(delta,'xb',filters=[{'id':lzma.FILTER_LZMA2,'preset':6,'dict_size':64*1024*1024}]) as stream:
 with tarfile.open(fileobj=stream,mode='w|',format=tarfile.PAX_FORMAT) as tar:
  for name,path,suffix,source_name in payload:
   item=tarfile.TarInfo(name);item.mode=0o644;item.mtime=0;item.size=path.stat().st_size
   with path.open('rb') as source:tar.addfile(item,source)
direct=[f'S6_06_BLIND/{name}' for name in ('S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.tex','S6_06_BLIND_report.md','S6_06_BLIND_results.csv','S6_06_BLIND_literature_log.md')]
manifest={'snapshot':record,'files':files,'contents':contents,'patch_order':patch_order,'bundles':[prior['bundle'],{'file':delta.name,'bytes':delta.stat().st_size,'sha256':sha(delta)}],'direct_files':direct,'scope':'Full standalone snapshot. All research files restored byte exactly; supplied/external source payloads excluded by the documented rule.'}
manifestpath=STAGE/'checkpoint23_transport_manifest.json';manifestpath.write_text(json.dumps(manifest,indent=2)+'\n')
restore=r'''"""Restore every frozen research file and verify all sizes/SHA256 (stdlib only)."""
from pathlib import Path
import hashlib,json,tarfile,tempfile,shutil
from checkpoint_copy_add import decode
base=Path(__file__).resolve().parent
m=json.loads((base/'checkpoint23_transport_manifest.json').read_text())
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def target(root,name):
 p=(root/name).resolve()
 if not p.is_relative_to(root.resolve()):raise ValueError('Unsafe archive path')
 return p
with tempfile.TemporaryDirectory(prefix='.checkpoint23_restore_',dir=base) as tmp:
 stage=Path(tmp)
 for bundle in m['bundles']:
  archive=base/bundle['file'];assert archive.stat().st_size==bundle['bytes'] and sha(archive)==bundle['sha256']
  with tarfile.open(archive,'r|xz') as tar:
   for member in tar:
    if not member.isfile():raise ValueError('Unexpected non-file payload')
    out=target(stage,member.name);out.parent.mkdir(parents=True,exist_ok=True)
    source=tar.extractfile(member)
    if source is None:raise ValueError('Missing packed bytes')
    with source,out.open('wb') as sink:shutil.copyfileobj(source,sink)
 for h in m['patch_order']:
  info=m['contents'][h];assert info['storage']=='copy_add'
  reference=target(stage,'content/'+info['base_sha256'])
  assert sha(reference)==info['base_sha256']
  patch=target(stage,info['patch_name']);assert sha(patch)==info['patch_sha256']
  out=target(stage,'content/'+h);out.write_bytes(decode(reference.read_bytes(),patch.read_bytes()))
  assert out.stat().st_size==info['bytes'] and sha(out)==h
 verified=set()
 for name,info in m['files'].items():
  h=info['sha256'];source=target(stage,'content/'+h)
  if h not in verified:
   assert source.stat().st_size==info['bytes'] and sha(source)==h,name
   verified.add(h)
  out=target(base,name);out.parent.mkdir(parents=True,exist_ok=True)
  if out.exists():assert out.stat().st_size==info['bytes'] and sha(out)==h,'Refusing changed file: '+name
  else:shutil.copyfile(source,out)
for name,info in m['files'].items():
 p=target(base,name);assert p.stat().st_size==info['bytes'] and sha(p)==info['sha256'],name
print('PASS: restored and verified all '+str(len(m['files']))+' snapshot files.')
'''
(STAGE/'restore_checkpoint.py').write_text(restore)
readme=f'''# Complete immutable checkpoint23\n\nExtract this ZIP and run `python3 restore_checkpoint.py` using Python3.12 or later. The current paper and registers are directly readable. Restoration uses only the Python standard library, restores every one of the {len(files):,} frozen research files and verifies its exact size and SHA-256. The maximum LZMA dictionary is256MiB.\n\nThis ZIP is standalone. Its two lossless bundles, content manifest and byte-copy/add decoder are included; no previous download is required. Historical PDFs use exact copy/add instructions whose inputs and reconstructed bytes are independently verified. No image or PDF is resampled or regenerated.\n\nFrozen at {record['frozen_utc']}. The report remains INCOMPLETE. Full proofs, code, certificates, logs, renders and preserved mathematical attempts are included. The documented supplied/external source-payload exclusions remain in force.\n'''
partial=STAGE/'checkpoint23.partial'
with zipfile.ZipFile(partial,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for name in direct:z.write(paths[name],name)
 for path in (basebundle,delta):z.write(path,path.name,compress_type=zipfile.ZIP_STORED)
 z.write(manifestpath,manifestpath.name);z.write(STAGE/'restore_checkpoint.py','restore_checkpoint.py')
 z.write(ROOT/'code/checkpoint_copy_add.py','checkpoint_copy_add.py');z.writestr('READ_FIRST.md',readme)
for name,path in paths.items():assert path.stat().st_size==files[name]['bytes'] and sha(path)==files[name]['sha256']
assert partial.stat().st_size<=536870912,partial.stat().st_size
partial.rename(TARGET)
result={'status':'CREATED','path':str(TARGET),'bytes':TARGET.stat().st_size,'sha256':sha(TARGET),'snapshot_files':len(files),'record':record,'new_unique_contents':len(payload)}
(STAGE/'checkpoint23_creation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
