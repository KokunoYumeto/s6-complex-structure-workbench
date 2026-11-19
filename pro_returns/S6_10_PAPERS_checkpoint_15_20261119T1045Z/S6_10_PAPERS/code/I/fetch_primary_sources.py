#!/usr/bin/env python3
"""Download already identified primary-source URLs; retrieval confers no reading credit."""
from pathlib import Path
import concurrent.futures, hashlib, json, re, sys, urllib.request
ROOT=Path(__file__).resolve().parents[2]
DEST=ROOT/'analysis/I_sources'
BIB=(ROOT/'S6_10_PAPERS_references.bib').read_text()
def fetch(key):
    block=re.search(r'@[^\n]+\{'+re.escape(key)+r',\n(.*?)(?=\n@|\Z)',BIB,re.S)
    if not block:return {'key':key,'error':'bibliography key missing'}
    m=re.search(r'url = \{([^}]+)\}',block.group(1))
    if not m:return {'key':key,'error':'URL missing'}
    url=m.group(1)
    if key=='Pinkham1974Root':url='https://www.numdam.org/item/AST_1974__20__1_0.pdf'
    if key=='Johansson2016':url='https://arxiv.org/pdf/1611.02831v1'
    path=DEST/(key+'.pdf')
    try:
        if path.exists(): data=path.read_bytes()
        else:
            with urllib.request.urlopen(url,timeout=45) as response:data=response.read()
            if not data.startswith(b'%PDF'):raise ValueError('Response is not PDF')
            path.write_bytes(data)
        return {'key':key,'url':url,'file':str(path.relative_to(ROOT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'status':'downloaded only; exact reading credit is separate'}
    except Exception as error:return {'key':key,'url':url,'error':str(error)}
if __name__=='__main__':
    keys=sys.argv[1:]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(fetch,keys))
    log=DEST/'primary_downloads.json'
    old=json.loads(log.read_text()) if log.exists() else []
    log.write_text(json.dumps(old+results,indent=2))
    print(json.dumps(results,indent=2))
