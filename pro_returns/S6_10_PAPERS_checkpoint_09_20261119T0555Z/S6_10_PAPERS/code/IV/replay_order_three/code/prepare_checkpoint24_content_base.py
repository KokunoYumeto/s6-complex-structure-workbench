"""Resumable lossless storage preparation from the verified checkpoint23 tree.

This creates no research checkpoint. Every source byte is already frozen and
verified. Independently closed shards and per-content caches make interruption
recoverable without restarting a long compression stream.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,io,lzma,tarfile,time,os
from checkpoint_copy_add import encode as encode_patch,decode as decode_patch
from checkpoint_png_codec import encode as encode_png,decode as decode_png

ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
SOURCE=BASE/'checkpoint23_encoding';FROZEN=SOURCE/'frozen'
OUT=BASE/'checkpoint24_content_preparation';OUT.mkdir(exist_ok=True)
CACHE=OUT/'cache';CACHE.mkdir(exist_ok=True)
BUNDLES=OUT/'bundles';BUNDLES.mkdir(exist_ok=True)
source=json.loads((SOURCE/'checkpoint23_transport_manifest.json').read_text())
verification=json.loads((ROOT/'records/checkpoint23_verification.json').read_text())
assert verification['status']=='PASS' and verification['restored_and_verified_files']==len(source['files'])
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def save(path,value):
 temp=path.with_suffix(path.suffix+'.writing');temp.write_text(json.dumps(value,indent=2)+'\n');temp.replace(path)
unique={}
for name,info in source['files'].items():
 path=FROZEN/name;assert path.stat().st_size==info['bytes'] and sha(path)==info['sha256'],name
 unique.setdefault(info['sha256'],{'name':name,'path':path,'bytes':info['bytes']})
contents={};payload=[];patch_order=[];available=[];started=time.monotonic()
large=sorted([(h,v) for h,v in unique.items() if v['name'].endswith('.pdf') and v['bytes']>1000000],key=lambda x:(x[1]['bytes'],x[0]))
for h,item in large:
 cache=CACHE/(h+'.json')
 if cache.exists():
  entry=json.loads(cache.read_text())
 else:
  data=item['path'].read_bytes();best=None
  for bh,bi in available[-2:]:
   reference=bi['path'].read_bytes();patch,stats=encode_patch(reference,data)
   assert decode_patch(reference,patch)==data
   if best is None or len(patch)<len(best[1]):best=(bh,patch,stats)
  if best is not None and len(best[1])<len(data)*.92:
   bh,patch,stats=best;p=CACHE/(h+'.copyadd');p.write_bytes(patch)
   entry={'storage':'copy_add','bytes':len(data),'base_sha256':bh,'patch_name':'patches/'+h,'patch_sha256':sha(p),'stats':stats}
  else:entry={'storage':'raw','bytes':len(data),'name':'content/'+h}
  save(cache,entry)
 contents[h]=entry
 if entry['storage']=='copy_add':
  p=CACHE/(h+'.copyadd');assert sha(p)==entry['patch_sha256'];patch_order.append(h)
  payload.append((entry['patch_name'],p,'.pdfpatch',item['name'],entry['patch_sha256']))
 available.append((h,item))
for count,(h,item) in enumerate(sorted(unique.items(),key=lambda pair:pair[1]['name'])):
 if h in contents and contents[h]['storage']=='copy_add':continue
 p=item['path'];suffix=Path(item['name']).suffix
 if suffix=='.png':
  cache=CACHE/(h+'.json')
  if cache.exists():entry=json.loads(cache.read_text())
  else:
   raw=p.read_bytes();encoded=encode_png(raw)
   if encoded is None:entry={'storage':'raw','bytes':len(raw),'name':'content/'+h}
   else:
    out=CACHE/(h+'.pngcodec');out.write_bytes(encoded)
    entry={'storage':'png','bytes':len(raw),'encoded_name':'png/'+h,'encoded_sha256':sha(out)}
   save(cache,entry)
  contents[h]=entry
  if entry['storage']=='png':
   out=CACHE/(h+'.pngcodec');assert sha(out)==entry['encoded_sha256']
   payload.append((entry['encoded_name'],out,suffix,item['name'],entry['encoded_sha256']))
  else:payload.append((entry['name'],p,suffix,item['name'],h))
 else:
  contents[h]={'storage':'raw','bytes':item['bytes'],'name':'content/'+h}
  payload.append(('content/'+h,p,suffix,item['name'],h))
 if count%200==0:print(json.dumps({'stage':'content','processed':count,'unique':len(unique),'seconds':round(time.monotonic()-started,1)}),flush=True)
payload.sort(key=lambda row:(row[2],row[3]))
groups=[];current=[];current_bytes=0
for row in payload:
 size=row[1].stat().st_size
 if current and current_bytes+size>96*1024*1024:
  groups.append(current);current=[];current_bytes=0
 current.append(row);current_bytes+=size
if current:groups.append(current)
bundles=[]
for index,group in enumerate(groups):
 name=f'checkpoint24_base_{index:04d}.tar.xz';path=BUNDLES/name;record=path.with_suffix(path.suffix+'.json')
 fingerprint=hashlib.sha256(json.dumps([(n,p.stat().st_size,h) for n,p,s,o,h in group],separators=(',',':')).encode()).hexdigest()
 if record.exists():
  result=json.loads(record.read_text());assert result['fingerprint']==fingerprint
  assert path.stat().st_size==result['bytes'] and sha(path)==result['sha256']
 else:
  partial=path.with_suffix(path.suffix+'.partial')
  if partial.exists():partial.rename(partial.with_name(partial.name+'.interrupted_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')))
  with lzma.open(partial,'xb',filters=[{'id':lzma.FILTER_LZMA2,'preset':3,'dict_size':64*1024*1024}]) as stream:
   with tarfile.open(fileobj=stream,mode='w|',format=tarfile.PAX_FORMAT) as tar:
    for n,p,s,o,h in group:
     assert sha(p)==h
     item=tarfile.TarInfo(n);item.size=p.stat().st_size;item.mtime=0;item.mode=0o644
     with p.open('rb') as reader:tar.addfile(item,reader)
  partial.rename(path)
  result={'file':name,'local_path':str(path),'bytes':path.stat().st_size,'sha256':sha(path),'members':len(group),'fingerprint':fingerprint}
  save(record,result)
 bundles.append(result)
 print(json.dumps({'stage':'bundle','done':index+1,'total':len(groups),'bundle_bytes':result['bytes'],'total_bytes':sum(x['bytes'] for x in bundles),'seconds':round(time.monotonic()-started,1)}),flush=True)
result={'status':'COMPLETE','created_utc':datetime.now(timezone.utc).isoformat(),'basis':'All verified checkpoint23 frozen research bytes, content-addressed with independently closed resumable shards.','files':source['files'],'contents':contents,'patch_order':patch_order,'bundles':bundles,'unique_files':len(unique),'source_files':len(source['files']),'elapsed_seconds':round(time.monotonic()-started,1),'bundle_bytes':sum(x['bytes'] for x in bundles),'codec':'Exact copy/add PDF bytes; exact original PNG chunks and verified zlib bytes; raw remaining files.'}
save(BASE/'checkpoint24_base_content_manifest.json',result)
record={k:v for k,v in result.items() if k not in ('files','contents','patch_order','bundles')};record['bundles']=len(bundles)
save(ROOT/'records/checkpoint24_content_base_preparation.json',record)
print(json.dumps(record,indent=2),flush=True)
