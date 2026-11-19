#!/usr/bin/env python3
import concurrent.futures,json,hashlib,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
URL='https://perso.limos.fr/~palafour/PAPERS/PDF/Garey-Johnson79.pdf'
SIZE=13756924
STEP=1000000
CACHE=ROOT/'retrieved_sources/gj_chunks';CACHE.mkdir(parents=True,exist_ok=True)
def get(a):
    b=min(a+STEP-1,SIZE-1)
    with urllib.request.urlopen(urllib.request.Request(URL,headers={'Range':f'bytes={a}-{b}'}),timeout=30) as r:
        status=r.status; cr=r.headers.get('Content-Range'); data=r.read()
    assert status==206 and cr==f'bytes {a}-{b}/{SIZE}' and len(data)==b-a+1,(status,cr,len(data))
    (CACHE/f'{a:08d}.part').write_bytes(data)
    return {'start':a,'end':b,'bytes':len(data),'status':status,'content_range':cr}
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    for row in pool.map(get,range(0,SIZE,STEP)):rows.append(row);print(row,flush=True)
data=b''.join((CACHE/f'{a:08d}.part').read_bytes() for a in range(0,SIZE,STEP))
assert len(data)==SIZE
(ROOT/'retrieved_sources/garey_johnson.pdf').write_bytes(data)
report={'url':URL,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'chunks':rows}
(ROOT/'Q03_DEPOSIT/code/C_gj_range_download_output.json').write_text(json.dumps(report,indent=2)+'\n')
print('SHA256',report['sha256'])
