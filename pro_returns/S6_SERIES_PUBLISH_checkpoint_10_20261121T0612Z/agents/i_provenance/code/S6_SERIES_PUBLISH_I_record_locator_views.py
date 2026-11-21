import hashlib,json,sys,time
from pathlib import Path
ROOT=Path('/workspace/scratch/653608133b22/work/agents/i_provenance/literature')
OUT=ROOT/'S6_SERIES_PUBLISH_I_final_primary_locator_receipt.json'
data=json.loads(OUT.read_text())
retrieval={r['key']:r for r in json.loads((ROOT/'S6_SERIES_PUBLISH_I_final_locator_retrieval.json').read_text())}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
for record in json.loads(sys.stdin.read()):
    key=record.pop('download_key'); r=retrieval[key]
    pages=record.pop('pages')
    views=[]
    for pair in pages:
        pdfpage,printed=pair
        p=ROOT/f'S6_SERIES_PUBLISH_I_{key}_pdf{pdfpage:03}.png'
        assert p.exists(),p
        views.append({'printed_page':printed,'pdf_page':pdfpage,'image':str(p),'image_sha256':sha(p)})
    record.update(pdf=r['path'],pdf_sha256=r['sha256'],url=r['url'],actual_page_views=views,viewed_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),verification_kind='actual rendered primary page reading; zero mathematical events')
    data['sources']=[s for s in data['sources'] if s['key']!=record['key']]+[record]
OUT.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
print('recorded',len(data['sources']),'sources',OUT)
