"""Prepare a fully lossless content-addressed base from the verified frozen22 tree.

This is compression preparation, not a new research checkpoint. Each future
snapshot selects exact content hashes; no source path is reused by assumption.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,io,lzma,tarfile,time
from checkpoint_copy_add import encode,decode
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
OLD=BASE/'checkpoint22_encoding';FROZEN=OLD/'frozen'
PREP=BASE/'checkpoint23_preparation';PREP.mkdir(exist_ok=False)
manifest=json.loads((OLD/'checkpoint22_transport_manifest.json').read_text())
verified=json.loads((ROOT/'records/checkpoint22_verification.json').read_text());assert verified['status']=='PASS'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
unique={}
for name,info in manifest['files'].items():
 p=FROZEN/name;assert p.stat().st_size==info['bytes'] and sha(p)==info['sha256'],name
 unique.setdefault(info['sha256'],{'name':name,'path':p,'bytes':info['bytes']})
large_pdfs=sorted([(h,v) for h,v in unique.items() if v['name'].endswith('.pdf') and v['bytes']>1000000],key=lambda x:x[1]['bytes'])
contents={};patch_items=[];available=[]
for h,item in large_pdfs:
 target=item['path'].read_bytes();best=None
 for base_h,base_item in available[-2:]:
  reference=base_item['path'].read_bytes();patch,stats=encode(reference,target)
  assert decode(reference,patch)==target
  if best is None or len(patch)<len(best[2]):best=(base_h,base_item,patch,stats)
 if best is not None and len(best[2])<len(target)*.92:
  base_h,base_item,patch,stats=best
  p=PREP/(h+'.copyadd');p.write_bytes(patch)
  contents[h]={'bytes':len(target),'storage':'copy_add','base_sha256':base_h,'patch_name':'patches/'+h,'patch_sha256':sha(p),'stats':stats}
  patch_items.append(('patches/'+h,p,'.pdfpatch',item['name']))
  print(json.dumps({'pdf':item['name'],'base':base_item['name'],'stats':stats}),flush=True)
 else:
  contents[h]={'bytes':len(target),'storage':'raw','name':'content/'+h}
 available.append((h,item))
payload=[]
for h,item in unique.items():
 if h in contents and contents[h]['storage']=='copy_add':continue
 contents[h]={'bytes':item['bytes'],'storage':'raw','name':'content/'+h}
 suffix=Path(item['name']).suffix
 payload.append(('content/'+h,item['path'],suffix,item['name']))
payload+=patch_items
payload.sort(key=lambda row:(row[2],row[3]))
target=BASE/'checkpoint23_base_content.tar.xz';assert not target.exists()
partial=PREP/'checkpoint23_base_content.partial';started=time.monotonic()
with lzma.open(partial,'xb',filters=[{'id':lzma.FILTER_LZMA2,'preset':6,'dict_size':256*1024*1024}]) as stream:
 with tarfile.open(fileobj=stream,mode='w|',format=tarfile.PAX_FORMAT) as tar:
  for index,(name,path,suffix,original_name) in enumerate(payload):
   item=tarfile.TarInfo(name);item.mode=0o644;item.mtime=0;item.size=path.stat().st_size
   with path.open('rb') as source:tar.addfile(item,source)
   if index%200==0:print(json.dumps({'packed':index,'total':len(payload),'path':original_name,'seconds':round(time.monotonic()-started,1)}),flush=True)
partial.rename(target)
result={'status':'COMPLETE','created_utc':datetime.now(timezone.utc).isoformat(),'basis':'Verified frozen checkpoint22 files, all exact byte hashes retained','files':manifest['files'],'contents':contents,'patch_order':[h for h,item in large_pdfs if contents[h]['storage']=='copy_add'],'bundle':{'file':target.name,'bytes':target.stat().st_size,'sha256':sha(target)},'unique_files':len(unique),'source_files':len(manifest['files']),'elapsed_seconds':round(time.monotonic()-started,1)}
(BASE/'checkpoint23_base_content_manifest.json').write_text(json.dumps(result,indent=2)+'\n')
record={k:v for k,v in result.items() if k not in ('files','contents','patch_order')}
(ROOT/'records/checkpoint23_content_base_preparation.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
