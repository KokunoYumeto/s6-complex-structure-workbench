#!/usr/bin/env python3
"""Reproduce opened-source byte comparisons for the Q03 audit.
Downloads are research inputs, stored outside the deliverable tree.
"""
import concurrent.futures, hashlib, json, urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'Q03_DEPOSIT'/'code'
CACHE=ROOT/'retrieved_sources'
CACHE.mkdir(exist_ok=True)
def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Q03-DEPOSIT-source-audit'}),timeout=40) as f:
        return f.read()
def sha(b): return hashlib.sha256(b).hexdigest()
report={'date':'2026-11-15','comparison':[],'retrievals':[]}
commit=json.loads(fetch('https://api.github.com/repos/openai/math/commits/main'))['sha']
report['openai_math_commit']=commit
base='preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/'
attached=ROOT/'background/sources/papers/openai-scheduling'
def compare(p):
    rel=p.relative_to(attached).as_posix(); u=f'https://raw.githubusercontent.com/openai/math/{commit}/{base}{rel}'
    b=fetch(u); dst=CACHE/'openai'/rel; dst.parent.mkdir(parents=True,exist_ok=True); dst.write_bytes(b)
    a=p.read_bytes()
    return {'file':rel,'url':u,'attached_bytes':len(a),'published_bytes':len(b),'attached_sha256':sha(a),'published_sha256':sha(b),'equal':a==b}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    for result in pool.map(compare,sorted(p for p in attached.rglob('*') if p.is_file())):
        report['comparison'].append(result)
        print(result['file'], 'IDENTICAL' if result['equal'] else 'DIFFERENT',result['published_bytes'],flush=True)
other={
 'scope_124.md':f'https://raw.githubusercontent.com/openai/math/{commit}/lean/docs/124.md',
 'jansen.pdf':'https://arxiv.org/pdf/2611.09392',
 'nederlof.pdf':'https://arxiv.org/pdf/2312.03495',
 'das_wiese.pdf':'https://arxiv.org/pdf/2501.09091',
 'coffman_graham.pdf':'https://fanchung.ucsd.edu/ron/papers/72_04_two_processors.pdf',
 'ullman.pdf':'https://www.cs.montana.edu/bhz/classes/fall-2021/csci460/paper4.pdf',
 'garey_johnson.pdf':'https://perso.limos.fr/~palafour/PAPERS/PDF/Garey-Johnson79.pdf',
 'drbh_bbd3013.zip':'https://codeload.github.com/drbh/scheduling-proof-exploration/zip/bbd30137258b15d8c5caedd035d72e8e8a875dbd',
}
def get_item(x):
    name,u=x
    try:
        b=fetch(u); (CACHE/name).write_bytes(b)
        return {'file':name,'url':u,'bytes':len(b),'sha256':sha(b),'status':'opened'}
    except Exception as e: return {'file':name,'url':u,'status':'failed','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    for result in pool.map(get_item,other.items()):
        report['retrievals'].append(result); print(result,flush=True)
(OUT/'C_retrieve_compare_output.json').write_text(json.dumps(report,indent=2)+'\n')
