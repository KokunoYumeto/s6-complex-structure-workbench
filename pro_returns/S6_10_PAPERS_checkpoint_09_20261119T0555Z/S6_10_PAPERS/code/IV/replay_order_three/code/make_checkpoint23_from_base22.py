"""Freeze and encode checkpoint23 with every research byte and verified PNGs."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,zipfile,tarfile,io,lzma,re,shutil,time
from checkpoint_copy_add import encode,decode
from checkpoint_png_codec import encode as encode_png,decode as decode_png

ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
TARGET=BASE/'S6_06_BLIND_checkpoint_23.zip';assert not TARGET.exists()
STAGE=BASE/'checkpoint23_encoding';STAGE.mkdir(exist_ok=False)
PREP=BASE/'checkpoint23_base22_final'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def excluded(rel):
 source=any(rel.startswith(x) for x in ('records/primary_sources/','records/external_source_cache/','records/sources/','records/part5_comparison/'))
 return (source and Path(rel).suffix.lower() in ('.pdf','.txt','.png','.jpg','.jpeg','.tif','.tiff','.html')) or rel=='records/AC26_original_extracted.txt' or bool(re.fullmatch(r'records/web_\d+\.json',rel)) or rel=='code/part1/ocr_wall.out'
record={'checkpoint':23,'due_utc':'2026-11-17T22:49:44+00:00','created_utc':datetime.now(timezone.utc).isoformat(),'verified_predecessor':22,'predecessor_sha256':'a8569992565dbc61be69488499c22dd871c0b2223ec6fd545fd8dfc570fe9e54','predecessor_library_id':'libfile_d7b619e483948191934e1e2a8d86dfd2','blind_part5_sha256':{name:sha(ROOT/name) for name in ('notes/part5.tex','notes/part5_blind.md')}}
assert record['blind_part5_sha256']['notes/part5.tex']=='f7b2188bbd5fc453780421599b65168141c8ed09480b1396794f02f41a680e0f'
assert record['blind_part5_sha256']['notes/part5_blind.md']=='ffdac7780a3d5c35565e31e6bb1bebf459e0f7dc75355e19fc216b5ba4b9a1e4'
(ROOT/'records/checkpoint_23.json').write_text(json.dumps(record,indent=2)+'\n')
with (ROOT/'S6_06_BLIND_literature_log.md').open('a') as f:f.write(f"\n| {record['created_utc']} | S6_06_BLIND_checkpoint_23.zip | Complete hourly snapshot after independently verified checkpoint22 | Full proof/code/log/attempt content, including exact original render bytes; Part5 immutable hashes reverified. |\n")
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
while not (PREP/'checkpoint23_base22_manifest.json').exists():time.sleep(5)
prior=json.loads((PREP/'checkpoint23_base22_manifest.json').read_text())
bundles=[]
for bundle in prior['bundles']:
 path=PREP/bundle['file'] if (PREP/bundle['file']).exists() else BASE/bundle['file']
 assert sha(path)==bundle['sha256'];bundles.append(path)
oldhash={info['sha256']:name for name,info in prior['files'].items()}
contents={};payload=[]
reference_name='S6_06_BLIND/S6_06_BLIND_paper.pdf'
reference=BASE/'checkpoint22_encoding/frozen'/reference_name
reference_sha=prior['files'][reference_name]['sha256'];assert sha(reference)==reference_sha
for h,(name,path,info) in unique.items():
 if h in oldhash:continue
 if name.endswith('.pdf') and info['bytes']>1000000:
  raw=path.read_bytes();patch,stats=encode(reference.read_bytes(),raw);assert decode(reference.read_bytes(),patch)==raw
  if len(patch)<len(raw)*.92:
   patchpath=STAGE/(h+'.copyadd');patchpath.write_bytes(patch)
   contents[h]={'bytes':len(raw),'storage':'copy_add','base_sha256':reference_sha,'patch_name':'patches/'+h,'patch_sha256':sha(patchpath),'stats':stats}
   payload.append(('patches/'+h,patchpath,'.pdfpatch',name));continue
 if name.endswith('.png'):
  raw=path.read_bytes();encoded=encode_png(raw)
  if encoded is not None:
   p=STAGE/(h+'.pngcodec');p.write_bytes(encoded)
   contents[h]={'bytes':len(raw),'storage':'png','encoded_name':'png/'+h,'encoded_sha256':sha(p)}
   payload.append(('png/'+h,p,'.png',name));continue
 contents[h]={'bytes':info['bytes'],'storage':'raw','name':'content/'+h}
 payload.append(('content/'+h,path,Path(name).suffix,name))
payload.sort(key=lambda row:(row[2],row[3]))
delta=STAGE/'checkpoint23_new_content.tar.xz'
with lzma.open(delta,'xb',filters=[{'id':lzma.FILTER_LZMA2,'preset':3,'dict_size':64*1024*1024}]) as stream:
 with tarfile.open(fileobj=stream,mode='w|',format=tarfile.PAX_FORMAT) as tar:
  for i,(name,path,suffix,source_name) in enumerate(payload):
   item=tarfile.TarInfo(name);item.mode=0o644;item.mtime=0;item.size=path.stat().st_size
   with path.open('rb') as source:tar.addfile(item,source)
   if i%100==0:print(json.dumps({'packed_new':i,'of':len(payload),'path':source_name}),flush=True)
direct=[f'S6_06_BLIND/{name}' for name in ('S6_06_BLIND_paper.tex','S6_06_BLIND_report.md','S6_06_BLIND_results.csv','S6_06_BLIND_literature_log.md')]
manifest={'snapshot':record,'files':files,'contents':contents,'base22_manifest':'checkpoint23_base22_manifest.json','delta':{'file':delta.name,'bytes':delta.stat().st_size,'sha256':sha(delta)},'direct_files':direct,'scope':'Complete standalone snapshot. All research files restore to their exact original size and SHA256; supplied/external payload exclusions retained.'}
manifestpath=STAGE/'checkpoint23_transport_manifest.json';manifestpath.write_text(json.dumps(manifest,indent=2)+'\n')
restore_base=(PREP/'restore_base22.py').read_text()
restore_base=restore_base.replace('import hashlib,json,tarfile,tempfile,shutil','import hashlib,json,tarfile,tempfile,shutil,sys')
restore_base=restore_base.replace('base=Path(__file__).resolve().parent',"archive_base=Path(__file__).resolve().parent\nbase=Path(sys.argv[1]).resolve()")
restore_base=restore_base.replace("m=json.loads((base/'checkpoint23_base22_manifest.json').read_text())","m=json.loads((archive_base/'checkpoint23_base22_manifest.json').read_text())\nfor name in m['direct_files']:\n out=base/name;out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(archive_base/'__base22_direct'/name,out)")
restore_base=restore_base.replace("archive=base/bundle['file']","archive=archive_base/bundle['file']")
compile(restore_base,'restore_base22.py','exec')
(STAGE/'restore_base22.py').write_text(restore_base)
restore=r'''"""Restore every frozen research file and independently verify exact byte hashes."""
from pathlib import Path
import hashlib,json,tarfile,tempfile,shutil,subprocess,sys
from checkpoint_copy_add import decode
from checkpoint_png_codec import decode as decode_png
base=Path(__file__).resolve().parent
m=json.loads((base/'checkpoint23_transport_manifest.json').read_text())
prior=json.loads((base/m['base22_manifest']).read_text())
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def target(root,name):
 p=(root/name).resolve()
 if not p.is_relative_to(root.resolve()):raise ValueError('Unsafe archive path')
 return p
with tempfile.TemporaryDirectory(prefix='.checkpoint23_restore_',dir=base) as tmp:
 stage=Path(tmp);old=stage/'base22';old.mkdir()
 subprocess.run([sys.executable,str(base/'restore_base22.py'),str(old)],check=True)
 oldhash={info['sha256']:name for name,info in prior['files'].items()}
 payload=stage/'new';payload.mkdir()
 bundle=m['delta'];archive=base/bundle['file']
 assert archive.stat().st_size==bundle['bytes'] and sha(archive)==bundle['sha256']
 with tarfile.open(archive,'r|xz') as tar:
  for member in tar:
   assert member.isfile();out=target(payload,member.name);out.parent.mkdir(parents=True,exist_ok=True)
   source=tar.extractfile(member)
   with source,out.open('wb') as sink:shutil.copyfileobj(source,sink)
 for h,info in m['contents'].items():
  if info['storage']=='raw':continue
  out=target(payload,'content/'+h);out.parent.mkdir(parents=True,exist_ok=True)
  if info['storage']=='png':
   p=target(payload,info['encoded_name']);assert sha(p)==info['encoded_sha256']
   out.write_bytes(decode_png(p.read_bytes()))
  elif info['storage']=='copy_add':
   reference=target(old,oldhash[info['base_sha256']]);assert sha(reference)==info['base_sha256']
   patch=target(payload,info['patch_name']);assert sha(patch)==info['patch_sha256']
   out.write_bytes(decode(reference.read_bytes(),patch.read_bytes()))
  else:raise ValueError('Unknown byte codec')
  assert out.stat().st_size==info['bytes'] and sha(out)==h
 verified=set()
 for name,info in m['files'].items():
  h=info['sha256'];source=target(old,oldhash[h]) if h in oldhash else target(payload,'content/'+h)
  if h not in verified:
   assert source.stat().st_size==info['bytes'] and sha(source)==h,name
   verified.add(h)
  out=target(base,name);out.parent.mkdir(parents=True,exist_ok=True)
  if out.exists():assert out.stat().st_size==info['bytes'] and sha(out)==h,'Refusing changed file: '+name
  else:shutil.copyfile(source,out)
for name,info in m['files'].items():
 p=target(base,name);assert p.stat().st_size==info['bytes'] and sha(p)==info['sha256'],name
print('PASS: restored and verified all '+str(len(m['files']))+' checkpoint23 files.')
'''
(STAGE/'restore_checkpoint.py').write_text(restore)
readme=f'''# Complete immutable checkpoint23\n\nExtract this ZIP and run `python3 restore_checkpoint.py`. The registers are directly readable; the paper is restored with the complete source tree. The restoration verifies all {len(files):,} research files by exact original size and SHA-256. This ZIP is standalone: all earlier base bytes, newer bytes, manifests and decoders are included. No earlier checkpoint download is needed.\n\nThe code uses Python's standard library. The PNG byte codec was encoded and independently verified with the zlib version named inside every encoded image. It preserves every PNG chunk and regenerates identical IDAT bytes; a runtime that produces different compressed bytes is rejected explicitly. No image pixels, page layout, PDF content, original file bytes, proofs, code, logs, or retained attempts are changed or omitted. Historical PDFs use verified exact copy/add patches.\n\nFrozen at {record['frozen_utc']}. The report remains INCOMPLETE. Supplied and external source payloads follow the documented exclusion rule.\n'''
partial=STAGE/'checkpoint23.partial'
with zipfile.ZipFile(partial,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for name in direct:z.write(paths[name],name)
 for path in bundles+[delta]:z.write(path,path.name,compress_type=zipfile.ZIP_STORED)
 z.write(PREP/'checkpoint23_base22_manifest.json','checkpoint23_base22_manifest.json')
 for name in prior['direct_files']:z.write(BASE/'checkpoint22_encoding/frozen'/name,'__base22_direct/'+name)
 for name in ('restore_base22.py','restore_checkpoint.py','checkpoint23_transport_manifest.json'):z.write(STAGE/name,name)
 for name in ('checkpoint_copy_add.py','checkpoint_png_codec.py'):z.write(ROOT/'code'/name,name)
 z.writestr('READ_FIRST.md',readme)
for name,path in paths.items():assert path.stat().st_size==files[name]['bytes'] and sha(path)==files[name]['sha256']
assert partial.stat().st_size<=536870912,partial.stat().st_size
partial.rename(TARGET)
result={'status':'CREATED','path':str(TARGET),'bytes':TARGET.stat().st_size,'sha256':sha(TARGET),'snapshot_files':len(files),'record':record,'new_unique_contents':len(payload)}
(STAGE/'checkpoint23_creation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
