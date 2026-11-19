"""Re-encode the already frozen checkpoint22, preserving every original byte."""
from pathlib import Path
import hashlib, json, zipfile, tarfile, io, lzma, shutil
from datetime import datetime, timezone
from checkpoint_copy_add import encode, decode

ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT.parent
STAGE=BASE/'checkpoint22_encoding'; FROZEN=STAGE/'frozen'
OUT=STAGE/'lossless_reencoding'; OUT.mkdir(exist_ok=False)
TARGET=BASE/'S6_06_BLIND_checkpoint_22.zip'; assert not TARGET.exists()
original=json.loads((STAGE/'checkpoint22_transport_manifest.json').read_text())
with zipfile.ZipFile(BASE/'S6_06_BLIND_checkpoint_21.zip') as z:
    prior=json.loads(z.read('checkpoint21_transport_manifest.json'))
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
for bundle in prior['bundles']:
    assert sha(BASE/bundle['file'])==bundle['sha256']
oldhash={prior['files'][name]['sha256']:name for name in prior['packed_files']}
direct={f'S6_06_BLIND/{name}' for name in ['S6_06_BLIND_report.md','S6_06_BLIND_results.csv','S6_06_BLIND_literature_log.md','S6_06_BLIND_paper.tex']}
baseline='S6_06_BLIND/records/checkpoint19_prior_master66/S6_06_BLIND_paper.pdf'
assert baseline in prior['packed_files']
main='S6_06_BLIND/S6_06_BLIND_paper.pdf'
patch_bases={
    'S6_06_BLIND/records/checkpoint22_prior_master68/S6_06_BLIND_paper.pdf':baseline,
    main:baseline,
    'S6_06_BLIND/records/attempts/master71_before_k93/S6_06_BLIND_paper.pdf':main,
    'S6_06_BLIND/records/checkpoint22_prior_master71/S6_06_BLIND_paper.pdf':main,
}
manifest=dict(original)
manifest['encoding_revision']={'utc':datetime.now(timezone.utc).isoformat(),'reason':'Initial complete encoding exceeded the 512 MiB transfer limit; all 8125 frozen files retain their exact size and SHA-256.','initial_encoding_bytes':(STAGE/'checkpoint22.partial').stat().st_size,'initial_encoding_sha256':sha(STAGE/'checkpoint22.partial'),'codec':'stdlib LZMA plus fully documented byte-copy/add patches'}
manifest['bundles']=prior['bundles'].copy()
manifest['copies']=[];manifest['patches']=[]
manifest['direct_files']=sorted(direct)
manifest['packed_files']=[name for name in original['files'] if name not in direct]
payload=[];seen={}
for name,info in original['files'].items():
    p=FROZEN/name;assert p.stat().st_size==info['bytes'] and sha(p)==info['sha256'],name
    if name in direct or name in patch_bases:continue
    h=info['sha256']
    if h in oldhash:
        if name!=oldhash[h]:manifest['copies'].append({'target':name,'source':oldhash[h]})
    elif h in seen:
        manifest['copies'].append({'target':name,'source':seen[h]})
    else:
        seen[h]=name;payload.append((name,p))
for number,(name,reference) in enumerate(patch_bases.items()):
    base=(FROZEN/reference).read_bytes();data=(FROZEN/name).read_bytes()
    patch,stats=encode(base,data);assert decode(base,patch)==data
    path=OUT/f'patch_{number:02d}.copyadd';path.write_bytes(patch)
    archive_name=f'__transport__/patch_{number:02d}.copyadd'
    payload.append((archive_name,path))
    item={'target':name,'base':reference,'patch':archive_name,'patch_sha256':sha(path),'stats':stats}
    manifest['patches'].append(item);print(json.dumps({'patch':item}),flush=True)
tarpath=OUT/'checkpoint22_reencoded_artifacts.tar.xz'
payload.sort(key=lambda item:(Path(item[0]).suffix,item[0]))
with lzma.open(tarpath,'xb',filters=[{'id':lzma.FILTER_LZMA2,'preset':6,'dict_size':128*1024*1024}]) as xz:
    with tarfile.open(fileobj=xz,mode='w|',format=tarfile.PAX_FORMAT) as tar:
        for index,(name,p) in enumerate(payload):
            item=tarfile.TarInfo(name);item.mode=0o644;item.mtime=int(p.stat().st_mtime);item.size=p.stat().st_size
            with p.open('rb') as source:tar.addfile(item,source)
            if index%100==0:print(json.dumps({'packed':index,'of':len(payload),'path':name}),flush=True)
manifest['bundles'].append({'file':tarpath.name,'sha256':sha(tarpath)})
manifest.pop('base_bundles',None);manifest.pop('delta_bundle',None)
manifestpath=OUT/'checkpoint22_transport_manifest.json';manifestpath.write_text(json.dumps(manifest,indent=2)+'\n')
restore=r'''"""Restore and independently verify every frozen research file, using stdlib only."""
from pathlib import Path
import hashlib,json,tarfile,tempfile,shutil
from checkpoint_copy_add import decode
base=Path(__file__).resolve().parent
m=json.loads((base/'checkpoint22_transport_manifest.json').read_text())
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def target(root,name):
 p=(root/name).resolve()
 if not p.is_relative_to(root.resolve()):raise ValueError('Unsafe archive path')
 return p
with tempfile.TemporaryDirectory(prefix='.checkpoint22_restore_',dir=base) as tmp:
 stage=Path(tmp)
 for bundle in m['bundles']:
  archive=base/bundle['file'];assert sha(archive)==bundle['sha256']
  with tarfile.open(archive,'r|xz') as tar:
   for member in tar:
    out=target(stage,member.name);out.parent.mkdir(parents=True,exist_ok=True)
    if member.islnk():
     with target(stage,member.linkname).open('rb') as source,out.open('wb') as sink:shutil.copyfileobj(source,sink)
    else:
     source=tar.extractfile(member)
     if source is None:raise ValueError('Missing packed bytes')
     with source,out.open('wb') as sink:shutil.copyfileobj(source,sink)
 for item in m['copies']:
  source=target(stage,item['source']);out=target(stage,item['target'])
  out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,out)
 for item in m['patches']:
  reference=target(stage,item['base']);patch=target(stage,item['patch'])
  assert sha(patch)==item['patch_sha256']
  out=target(stage,item['target']);out.parent.mkdir(parents=True,exist_ok=True)
  out.write_bytes(decode(reference.read_bytes(),patch.read_bytes()))
 for name in m['packed_files']:
  source=target(stage,name);info=m['files'][name]
  assert source.stat().st_size==info['bytes'] and sha(source)==info['sha256'],name
  out=target(base,name);out.parent.mkdir(parents=True,exist_ok=True)
  if out.exists():
   assert out.stat().st_size==info['bytes'] and sha(out)==info['sha256'],'Refusing changed file: '+name
  else:shutil.copyfile(source,out)
for name,info in m['files'].items():
 p=target(base,name);assert p.stat().st_size==info['bytes'] and sha(p)==info['sha256'],name
print('PASS: restored and verified all '+str(len(m['files']))+' snapshot files.')
'''
(OUT/'restore_checkpoint.py').write_text(restore)
readme='''# Complete immutable checkpoint 22\n\nExtract this ZIP, then run `python3 restore_checkpoint.py`. Python 3.12 or later is recommended. The restoration uses only the Python standard library. It restores the complete paper, sources, proofs, code, certificates, logs, renders, and preserved attempts, and verifies the exact size and SHA-256 of all 8,125 frozen research files.\n\nThis ZIP is standalone. All three lossless bundles and the documented copy/add decoder are included; no earlier download is required. Four successive master PDFs use exact byte-copy/add patches with explicit baseline hashes. The report and registers are directly readable before restoration. The maximum LZMA dictionary is 128 MiB.\n\nThe research snapshot was frozen at 2026-11-17T21:50:10.905330+00:00. Only its lossless storage encoding changed after the first encoding exceeded the file-size limit. Every frozen file is preserved byte for byte. The report remains INCOMPLETE. The verified checkpoint21 predecessor and the unconfirmed checkpoint20 are recorded in the research files.\n'''
partial=OUT/'checkpoint22.partial'
with zipfile.ZipFile(partial,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for name in sorted(direct):z.write(FROZEN/name,name)
    for bundle in manifest['bundles']:
        p=tarpath if bundle['file']==tarpath.name else BASE/bundle['file']
        z.write(p,p.name,compress_type=zipfile.ZIP_STORED)
    z.write(manifestpath,manifestpath.name)
    z.write(OUT/'restore_checkpoint.py','restore_checkpoint.py')
    z.write(ROOT/'code/checkpoint_copy_add.py','checkpoint_copy_add.py')
    z.write(Path(__file__),'reencode_checkpoint22.py')
    z.writestr('READ_FIRST.md',readme)
result={'status':'CREATED','path':str(TARGET),'bytes':partial.stat().st_size,'sha256':sha(partial),'snapshot_files':len(manifest['files']),'record':manifest['snapshot'],'encoding_revision':manifest['encoding_revision'],'payload_bytes':tarpath.stat().st_size}
print(json.dumps(result,indent=2),flush=True)
assert partial.stat().st_size<=536870912,partial.stat().st_size
partial.rename(TARGET)
(STAGE/'checkpoint22_creation.json').write_text(json.dumps(result,indent=2)+'\n')
(ROOT/'records/checkpoint22_lossless_reencoding.json').write_text(json.dumps(result,indent=2)+'\n')
