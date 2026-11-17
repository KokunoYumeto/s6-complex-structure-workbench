"""Retrieve exact original source versions; retrieval is not a reading claim."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import gzip, hashlib, io, json, tarfile, urllib.request

ROOT=Path(__file__).resolve().parents[3]
DEST=ROOT/'sources/external/maps_audit'
OUT=ROOT/'deliverables/work/maps_audit'
SPECS=[
 ('goerss2008v1','0802.1006v1'),
 ('dugger_isaksen2009v1','0901.1632v1'),
 ('isaksen2014v2','1407.8418v2'),
 ('isaksen_wang_xu2020v1','2001.04247v1'),
 ('friedman2008v8','0809.4221v8'),
 ('luecke2021v2','2109.00048v2'),
]
def fetch(spec):
 stem,ident=spec;url=f'https://arxiv.org/src/{ident}';p=DEST/(stem+'.tar')
 try:
  if not p.exists():
   req=urllib.request.Request(url,headers={'User-Agent':'Research-source-verification/1.0'})
   with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
   p.write_bytes(data)
  data=p.read_bytes();folder=DEST/(stem+'_source');folder.mkdir(exist_ok=True)
  try:
   with tarfile.open(fileobj=io.BytesIO(data)) as tf: tf.extractall(folder,filter='data')
  except tarfile.ReadError:
   try: text=gzip.decompress(data)
   except OSError: text=data
   if b'\\document' not in text and b'\\input' not in text: raise ValueError('Response is not an identified TeX source archive')
   (folder/'author.tex').write_bytes(text)
  return dict(source=str(p.relative_to(ROOT)),url=url,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),status='Original version retrieved; mathematical reading pending',extracted_files=[str(q.relative_to(ROOT)) for q in sorted(folder.rglob('*')) if q.is_file()],date='2026-11-17')
 except Exception as e:return dict(url=url,status='Retrieval failed',error=str(e),date='2026-11-17')

with ThreadPoolExecutor(max_workers=6) as pool: records=list(pool.map(fetch,SPECS))
pin='2f1cd08cb4f7b7b643eec441eae78637bbb71973'
for name in ['cooperations.tex','mo.tex']:
 url=f'https://raw.githubusercontent.com/ecpeterson/FormalGeomNotes/{pin}/{name}'
 p=DEST/f'peterson_{pin[:12]}_{name}'
 try:
  if not p.exists():
   with urllib.request.urlopen(url,timeout=45) as r: p.write_bytes(r.read())
  data=p.read_bytes();records.append(dict(source=str(p.relative_to(ROOT)),url=url,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),status='Pinned author source retrieved; mathematical reading pending',date='2026-11-17'))
 except Exception as e: records.append(dict(url=url,status='Retrieval failed',error=str(e),date='2026-11-17'))
(OUT/'stable_primary_retrieval.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
for r in records: print(json.dumps({k:v for k,v in r.items() if k!='extracted_files'}))
