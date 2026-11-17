"""Restore and independently verify every frozen research file, using stdlib only."""
from pathlib import Path
import hashlib,json,tarfile,tempfile,shutil,sys
from checkpoint_copy_add import decode
from checkpoint_png_codec import decode as decode_png
archive_base=Path(__file__).resolve().parent
base=Path(sys.argv[1]).resolve()
m=json.loads((archive_base/'checkpoint23_base22_manifest.json').read_text())
for name in m['direct_files']:
 out=base/name;out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(archive_base/'__base22_direct'/name,out)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def target(root,name):
 p=(root/name).resolve()
 if not p.is_relative_to(root.resolve()):raise ValueError('Unsafe archive path')
 return p
with tempfile.TemporaryDirectory(prefix='.checkpoint22_restore_',dir=base) as tmp:
 stage=Path(tmp)
 for bundle_index,bundle in enumerate(m['bundles']):
  if bundle_index==len(m['bundles'])-1:
   for item in m['copies']:
    if item['source_generation']=='old':
     source=target(stage,item['source']);info=m['files'][item['target']]
     assert source.stat().st_size==info['bytes'] and sha(source)==info['sha256']
     cached=target(stage,'__transport__/base_cache/'+info['sha256'])
     cached.parent.mkdir(parents=True,exist_ok=True)
     if not cached.exists():shutil.copyfile(source,cached)
  archive=archive_base/bundle['file'];assert sha(archive)==bundle['sha256']
  with tarfile.open(archive,'r|xz') as tar:
   for member in tar:
    out=target(stage,member.name);out.parent.mkdir(parents=True,exist_ok=True)
    if member.islnk():
     with target(stage,member.linkname).open('rb') as source,out.open('wb') as sink:shutil.copyfileobj(source,sink)
    else:
     source=tar.extractfile(member)
     if source is None:raise ValueError('Missing packed bytes')
     with source,out.open('wb') as sink:shutil.copyfileobj(source,sink)
 for item in m.get('pngs',[]):
  source=target(stage,item['encoded']);out=target(stage,item['target'])
  out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(decode_png(source.read_bytes()))
  assert out.stat().st_size==item['bytes'] and sha(out)==item['sha256']
 for item in m['copies']:
  source_name=('__transport__/base_cache/'+m['files'][item['target']]['sha256']) if item['source_generation']=='old' else item['source']
  source=target(stage,source_name);out=target(stage,item['target'])
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
