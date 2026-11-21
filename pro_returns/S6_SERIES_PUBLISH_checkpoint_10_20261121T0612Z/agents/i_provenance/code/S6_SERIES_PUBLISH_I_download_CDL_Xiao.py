from pathlib import Path
from datetime import datetime,timezone
import urllib.request,concurrent.futures,hashlib,json,subprocess
P=Path('/workspace/scratch/653608133b22/work/agents/i_provenance/literature')
items=[('CDL2024','https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/EnriquesOne.pdf'),('Xiao1991','https://archive.mpim-bonn.mpg.de/id/eprint/2953/1/preprint_1991_30.pdf')]
def get(x):
 name,url=x; req=urllib.request.Request(url,headers={'User-Agent':'S6-series-publication-source-audit'})
 with urllib.request.urlopen(req,timeout=45) as r:b=r.read();status=r.status
 assert b.startswith(b'%PDF'),name
 p=P/('S6_SERIES_PUBLISH_I_'+name+'.pdf');p.write_bytes(b)
 text=p.with_suffix('.txt');subprocess.run(['pdftotext','-layout',str(p),str(text)],check=True)
 return {'name':name,'url':url,'http_status':status,'pdf':str(p),'text':str(text),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'retrieved_utc':datetime.now(timezone.utc).isoformat(),'scope':'Retrieval and text indexing only; exact pages to be actually viewed/read separately.'}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:rows=list(pool.map(get,items))
(P/'S6_SERIES_PUBLISH_I_CDL_Xiao_retrieval_receipt.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
