"""Preserve old bundle alias bytes before newer payloads overwrite their paths."""
from pathlib import Path
import json,zipfile,hashlib,shutil
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
STAGE=BASE/'checkpoint22_encoding';OUT=STAGE/'lossless_reencoding'
TARGET=BASE/'S6_06_BLIND_checkpoint_22.zip'
creation=json.loads((STAGE/'checkpoint22_creation.json').read_text())
with zipfile.ZipFile(BASE/'S6_06_BLIND_checkpoint_21.zip') as z:
 prior=json.loads(z.read('checkpoint21_transport_manifest.json'))
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
assert sha(TARGET)==creation['sha256']
candidate=OUT/'unverified_alias_candidate.zip';assert not candidate.exists()
TARGET.rename(candidate)
with zipfile.ZipFile(candidate) as z:
 manifest=json.loads(z.read('checkpoint22_transport_manifest.json'))
 restore=z.read('restore_checkpoint.py').decode()
for item in manifest['copies']:
 source=item['source'];info=manifest['files'][item['target']]
 item['source_generation']='old' if source in prior['packed_files'] and prior['files'][source]==info else 'new'
manifest['encoding_revision']['alias_preservation']='All reused old-bundle alias bytes are cached and verified before the new payload is extracted.'
needle=" for bundle in m['bundles']:\n  archive=base/bundle['file'];assert sha(archive)==bundle['sha256']"
replacement=""" for bundle_index,bundle in enumerate(m['bundles']):
  if bundle_index==len(m['bundles'])-1:
   for item in m['copies']:
    if item['source_generation']=='old':
     source=target(stage,item['source']);info=m['files'][item['target']]
     assert source.stat().st_size==info['bytes'] and sha(source)==info['sha256']
     cached=target(stage,'__transport__/base_cache/'+info['sha256'])
     cached.parent.mkdir(parents=True,exist_ok=True)
     if not cached.exists():shutil.copyfile(source,cached)
  archive=base/bundle['file'];assert sha(archive)==bundle['sha256']"""
assert needle in restore;restore=restore.replace(needle,replacement)
needle="  source=target(stage,item['source']);out=target(stage,item['target'])"
replacement="""  source_name=('__transport__/base_cache/'+m['files'][item['target']]['sha256']) if item['source_generation']=='old' else item['source']
  source=target(stage,source_name);out=target(stage,item['target'])"""
assert needle in restore;restore=restore.replace(needle,replacement)
compile(restore,'restore_checkpoint.py','exec')
(OUT/'restore_checkpoint.py').write_text(restore)
(OUT/'checkpoint22_transport_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
partial=OUT/'checkpoint22_alias_verified.partial';assert not partial.exists()
with zipfile.ZipFile(candidate) as source,zipfile.ZipFile(partial,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as sink:
 for item in source.infolist():
  if item.filename=='checkpoint22_transport_manifest.json':sink.writestr(item,json.dumps(manifest,indent=2)+'\n')
  elif item.filename=='restore_checkpoint.py':sink.writestr(item,restore)
  else:
   with source.open(item) as old,sink.open(item,'w') as new:shutil.copyfileobj(old,new,4*1024*1024)
 sink.write(Path(__file__),'finalize_checkpoint22_encoding.py')
assert partial.stat().st_size<=536870912
partial.rename(TARGET)
creation.update(bytes=TARGET.stat().st_size,sha256=sha(TARGET),encoding_revision=manifest['encoding_revision'],finalized_utc=datetime.now(timezone.utc).isoformat())
(STAGE/'checkpoint22_creation.json').write_text(json.dumps(creation,indent=2)+'\n')
(ROOT/'records/checkpoint22_lossless_reencoding.json').write_text(json.dumps(creation,indent=2)+'\n')
record={'status':'CORRECTED_BEFORE_DELIVERY','candidate_bytes':candidate.stat().st_size,'candidate_sha256':sha(candidate),'reason':'Four old-payload aliases used paths that the new payload replaces. Cache every reused old alias by SHA256 before extracting the new payload. No frozen research byte changed.','final_bytes':creation['bytes'],'final_sha256':creation['sha256']}
(ROOT/'records/attempts/checkpoint22_alias_preservation.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(creation,indent=2))
