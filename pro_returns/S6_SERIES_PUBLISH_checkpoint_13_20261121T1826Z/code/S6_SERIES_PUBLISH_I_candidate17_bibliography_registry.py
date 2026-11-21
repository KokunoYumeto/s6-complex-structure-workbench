#!/usr/bin/env python3
"""Read-only primary registry retrieval for the frozen candidate17 bibliography.

Writes only the infrastructure agent's evidence directory. It neither changes
the bibliography nor awards mathematical or rendered-page reading credit.
"""
import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import re
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
AREA = ROOT / 'agents/continuation_infra/candidate17_bibliography_audit'
INVENTORY = ROOT / 'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate17_bibliography_inventory.json'

def retrieve(item):
    key, doi = item
    name = re.sub(r'[^A-Za-z0-9_.-]', '_', key)
    path = AREA / (name + '_crossref.json')
    url = 'https://api.crossref.org/works/' + urllib.parse.quote(doi, safe='')
    result = {'key':key,'doi':doi,'primary_registry_url':url}
    try:
        if not path.exists():
            req=urllib.request.Request(url,headers={'User-Agent':'Paper-I-bibliographic-metadata-audit/1.0','Accept':'application/json'})
            with urllib.request.urlopen(req, timeout=35) as response:
                raw=response.read()
            data=json.loads(raw)
            assert data.get('status')=='ok'
            path.write_bytes(raw)
        raw=path.read_bytes(); record=json.loads(raw)['message']
        result.update({'status':'retrieved','path':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(raw).hexdigest(),'title':record.get('title'), 'author':record.get('author'),'container-title':record.get('container-title'),'publisher':record.get('publisher'),'volume':record.get('volume'),'issue':record.get('issue'),'page':record.get('page'),'published':record.get('published'),'published-print':record.get('published-print'),'published-online':record.get('published-online'),'type':record.get('type'),'URL':record.get('URL')})
    except Exception as exc:
        result.update({'status':'unresolved','error':str(exc)})
    return result

def main():
    AREA.mkdir(exist_ok=True)
    inventory=json.loads(INVENTORY.read_text())
    source=ROOT/'S6_SERIES_PUBLISH_I.tex'
    assert hashlib.sha256(source.read_bytes()).hexdigest()==inventory['source_sha256']
    items=[]
    for entry in inventory['entries']:
        dois=entry['doi']
        if not dois:
            dois=re.findall(r'https://doi\.org/([^}]+)',entry['original_entry'])
        if dois: items.append((entry['key'],dois[0]))
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        rows=list(pool.map(retrieve,items))
    output={'source_sha256':inventory['source_sha256'],'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'Primary publisher-deposited Crossref DOI records; factual field comparison remains an explicit human/agent review, not an automated title equivalence assertion.','rows':rows,'mathematical_events_added':0}
    p=AREA/'existing_doi_registry_receipt.json'
    if p.exists(): raise FileExistsError(p)
    p.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    assert hashlib.sha256(source.read_bytes()).hexdigest()==inventory['source_sha256']
    print(json.dumps({'records':len(rows),'retrieved':sum(x['status']=='retrieved' for x in rows),'unresolved':[{k:v for k,v in x.items() if k in ['key','doi','error']} for x in rows if x['status']!='retrieved'],'receipt':str(p.relative_to(ROOT))}))

if __name__=='__main__':main()
