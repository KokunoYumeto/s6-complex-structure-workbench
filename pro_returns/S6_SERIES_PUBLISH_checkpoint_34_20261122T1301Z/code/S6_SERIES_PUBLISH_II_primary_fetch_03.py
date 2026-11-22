from pathlib import Path
import concurrent.futures, datetime as dt, hashlib, json, urllib.request
R=Path(__file__).resolve().parents[1]
out=R.parent/'primary_continuation2_root_provenance'
jobs=[('DGKXv1_original.pdf','https://arxiv.org/pdf/2610.00250v1'),('Engel_v1_original.pdf','https://arxiv.org/pdf/2609.38442v1')]
def fetch(job):
    name,url=job; p=out/name
    result=dict(file=str(p),url=url,started_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(request,timeout=45) as response:
            b=response.read(); result['response_url']=response.url
        assert b.startswith(b'%PDF'), 'Response is not a PDF'
        assert not p.exists(), 'Refusing to replace an existing primary file'
        p.write_bytes(b)
        result.update(status='downloaded',bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
    except Exception as e:
        result.update(status='failed',error=repr(e))
    result['finished_utc']=dt.datetime.now(dt.timezone.utc).isoformat()
    return result
record=R/'records/S6_SERIES_PUBLISH_II_primary_fetch_03.json'; assert not record.exists()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool: results=list(pool.map(fetch,jobs))
data=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),results=results,reading_credit=0,events_added=0)
record.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
