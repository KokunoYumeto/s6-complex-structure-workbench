"""Independently restore every unique byte content in the prepared base24."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,tarfile,shutil,time
from checkpoint_copy_add import decode as decode_patch
from checkpoint_png_codec import decode as decode_png
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
manifest=BASE/'checkpoint24_base_content_manifest.json'
while not manifest.exists():time.sleep(5)
m=json.loads(manifest.read_text());assert m['status']=='COMPLETE'
OUT=BASE/'checkpoint24_base_verify';OUT.mkdir(exist_ok=True)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def target(name):
 p=(OUT/name).resolve();assert p.is_relative_to(OUT.resolve());return p
for i,bundle in enumerate(m['bundles']):
 p=Path(bundle['local_path']);assert p.stat().st_size==bundle['bytes'] and sha(p)==bundle['sha256']
 with tarfile.open(p,'r|xz') as t:
  for member in t:
   assert member.isfile();out=target(member.name);out.parent.mkdir(parents=True,exist_ok=True)
   reader=t.extractfile(member)
   with reader,out.open('wb') as sink:shutil.copyfileobj(reader,sink)
 print(json.dumps({'extracted_bundle':i+1,'of':len(m['bundles'])}),flush=True)
for h in m['patch_order']:
 item=m['contents'][h];reference=target('content/'+item['base_sha256']);patch=target(item['patch_name'])
 assert sha(reference)==item['base_sha256'] and sha(patch)==item['patch_sha256']
 out=target('content/'+h);out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(decode_patch(reference.read_bytes(),patch.read_bytes()))
 assert sha(out)==h and out.stat().st_size==item['bytes']
pngs=0
for i,(h,item) in enumerate(m['contents'].items()):
 out=target('content/'+h)
 if item['storage']=='png':
  p=target(item['encoded_name']);assert sha(p)==item['encoded_sha256']
  if not out.exists() or sha(out)!=h:
   out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(decode_png(p.read_bytes()))
  pngs+=1
 assert out.stat().st_size==item['bytes'] and sha(out)==h,h
 if i%200==0:print(json.dumps({'verified_contents':i,'of':len(m['contents']),'pngs':pngs}),flush=True)
for name,info in m['files'].items():
 item=m['contents'][info['sha256']];assert item['bytes']==info['bytes']
record={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'source_files':len(m['files']),'unique_contents':len(m['contents']),'exact_pngs':pngs,'bundles':len(m['bundles']),'bundle_bytes':sum(b['bytes'] for b in m['bundles']),'manifest_sha256':sha(manifest),'verification':'Every shard independently extracted; every historical PDF patch and PNG byte codec decoded; every unique original byte size/SHA256 verified; every frozen file reference verified against that content.'}
(ROOT/'records/checkpoint24_content_base_verification.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
