"""Retrieve original literature for inspection; retrieval is not verification."""
from pathlib import Path
import sys,json,urllib.request,concurrent.futures,hashlib,subprocess,re
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'deps/python'))
import bibtexparser
OUT=ROOT/'sources/external/root/retrieved';OUT.mkdir(parents=True,exist_ok=True)
lib=bibtexparser.parse_string((ROOT/'deliverables/S6_09_PAPERS_references.bib').read_text())
entries={x.key:{y.key:y.value for y in x.fields} for x in lib.entries}
contexts=json.loads((ROOT/'deliverables/work/root/citation_contexts.json').read_text())
skip={'VL26','Y26','DGKX26v1','VTwo26','E26','AC26','Schnell19','Cerf71','Smale61','EK62',
      'Shioda90','HS53','CDL24','Xiao91','IKN2005E','IKN2007ErratumE','Parusinski1990E',
      'BM95AB','EH2024E','KKN2008Root','HondaViaclovsky2025D','Meersseman2019E','AC26Root',
      'Lazzeri1973Root','CDP2020D','RR70push','BS76push','ViaLog26push','DGKXv1push',
      'RRV71push','Grauert60push','Grauert63push','DGKXv2push','ViaTwo26push','LRS2018D','BHPV2004E'}
def fetch(key):
    url=entries.get(key,{}).get('url','')
    if not url:return {'key':key,'state':'missing URL'}
    url=url.replace('arxiv.org/abs/','arxiv.org/pdf/').replace('arxiv.org/html/','arxiv.org/pdf/')
    if 'numdam.org/item/' in url and url.endswith('/'):
        url=url.rstrip('/')+'.pdf'
    row={'key':key,'url':url,'state':'retrieval only; unread'}
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        data=urllib.request.urlopen(req,timeout=35).read()
        if data[:5]!=b'%PDF-':
            p=OUT/(key+'.html');p.write_bytes(data)
            return {**row,'path':str(p.relative_to(ROOT)),'state':'HTML response, inspect or obtain PDF'}
        p=OUT/(key+'.pdf');p.write_bytes(data)
        z=subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],capture_output=True)
        return {**row,'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(data).hexdigest(),
                'bytes':len(data),'text_extraction_returncode':z.returncode}
    except Exception as e:return {**row,'state':'retrieval failed','error':str(e)}
keys=[k for k in contexts if k not in skip]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    rows=list(pool.map(fetch,keys))
target=ROOT/'deliverables/work/root/literature_retrieval.json'
target.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
for row in rows:print(row['key'],row['state'],row.get('bytes',''),row.get('error',''))
