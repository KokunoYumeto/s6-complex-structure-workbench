import concurrent.futures, hashlib, json, sys, time, urllib.request
from pathlib import Path

ROOT=Path('/workspace/scratch/653608133b22/work/agents/i_provenance/literature')
targets=json.loads((ROOT/'S6_SERIES_PUBLISH_I_final_locator_targets.json').read_text())
if len(sys.argv)>1:
    wanted=set(sys.argv[1:]); targets=[t for t in targets if t['key'] in wanted]
outpath=ROOT/'S6_SERIES_PUBLISH_I_final_locator_retrieval.json'
prior=json.loads(outpath.read_text()) if outpath.exists() else []

def fetch(t):
    r=dict(t); path=ROOT/f"S6_SERIES_PUBLISH_I_{t['key']}.pdf"
    try:
        req=urllib.request.Request(t['url'],headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=45) as f:
            data=f.read(); r.update(http_status=f.status,final_url=f.url,content_type=f.headers.get('Content-Type'))
        r.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),retrieved_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
        if not data.startswith(b'%PDF'):
            raise ValueError('response is not a PDF')
        path.write_bytes(data); r['path']=str(path); r['status']='downloaded only; no page-view claim'
    except Exception as e:
        r['status']='retrieval failed';r['error']=str(e)
    return r

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
    for r in ex.map(fetch,targets):
        prior=[p for p in prior if p['key']!=r['key']]+[r]
        outpath.write_text(json.dumps(prior,indent=2,ensure_ascii=False)+'\n')
        print(r['key'],r['status'],r.get('bytes'),r.get('error',''),flush=True)
