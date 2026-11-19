"""Verify the new content-addressed base and every historical PDF patch."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,tarfile,shutil
from checkpoint_copy_add import decode
R=Path(__file__).resolve().parents[1];B=R.parent
m=json.loads((B/'checkpoint23_base_content_manifest.json').read_text())
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
p=B/m['bundle']['file'];assert p.stat().st_size==m['bundle']['bytes'] and sha(p)==m['bundle']['sha256']
dest=B/'checkpoint23_base_verify';dest.mkdir(exist_ok=False)
with tarfile.open(p,'r|xz') as tar:
 for item in tar:
  name=Path(item.name);assert not name.is_absolute() and '..' not in name.parts and item.isfile()
  out=dest/name;out.parent.mkdir(parents=True,exist_ok=True)
  with tar.extractfile(item) as source,out.open('wb') as sink:shutil.copyfileobj(source,sink)
for h in m['patch_order']:
 info=m['contents'][h];reference=dest/'content'/info['base_sha256'];patch=dest/info['patch_name']
 assert sha(reference)==info['base_sha256'] and sha(patch)==info['patch_sha256']
 (dest/'content'/h).write_bytes(decode(reference.read_bytes(),patch.read_bytes()))
for h,info in m['contents'].items():
 p=dest/'content'/h;assert p.stat().st_size==info['bytes'] and sha(p)==h,h
for name,info in m['files'].items():assert m['contents'][info['sha256']]['bytes']==info['bytes'],name
rec={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'bundle':m['bundle'],'verified_unique_contents':len(m['contents']),'represented_research_files':len(m['files']),'decoded_pdf_patches':len(m['patch_order']),'checks':'Independent tar extraction, all raw and reconstructed content hashes/sizes, and every frozen research file reference.'}
(R/'records/checkpoint23_content_base_verification.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec,indent=2))
