#!/usr/bin/env python3
import concurrent.futures,hashlib,json,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BASE='https://kokunoyumeto.github.io/open-math-courses-public/courses/three-machine-unit-job-scheduling/'
CACHE=ROOT/'retrieved_sources/course'; CACHE.mkdir(parents=True,exist_ok=True)
def fetch(p):
    with urllib.request.urlopen(BASE+p,timeout=25) as r:b=r.read()
    q=CACHE/p; q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(b);return b
meta=json.loads(fetch('course.json'))
rows=[]
def job(u):
    b=fetch(u['source']);a=ROOT/'background/sources/lessons/three-machine-unit-job-scheduling'/Path(u['source']).name
    return {'id':u['id'],'url':BASE+u['source'],'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'metadata_sha256':u['source_sha256'],'matches_metadata':hashlib.sha256(b).hexdigest()==u['source_sha256'],'attached_identical': a.read_bytes()==b if a.exists() else None}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    for r in pool.map(job,meta['units']): rows.append(r);print(r,flush=True)
for p in ['providers.json','provenance.json']:
    try:b=fetch(p);print(p,len(b),flush=True)
    except Exception as e: print(p,str(e),flush=True)
(ROOT/'Q03_DEPOSIT/code/C_course_compare_output.json').write_text(json.dumps(rows,indent=2)+'\n')
