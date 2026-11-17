from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
urls=[('openalex','https://api.openalex.org/works/https://doi.org/10.1017/S0017089524000272'),('semantic','https://api.semanticscholar.org/graph/v1/paper/DOI:10.1017/S0017089524000272?fields=title,openAccessPdf,externalIds,url'),('crossref','https://api.crossref.org/works/10.1017/S0017089524000272')]
def get(row):
 name,url=row
 try:
  d=urlopen(url,timeout=25).read();(root/f'records/C_Pham2025_{name}.json').write_bytes(d);j=json.loads(d)
  if name=='openalex':return name,{'locations':j.get('locations'),'open_access':j.get('open_access')}
  if name=='crossref':return name,{k:j['message'].get(k) for k in ['link','resource','relation']}
  return name,j
 except Exception as e:return name,{'error':str(e)}
for name,result in ThreadPoolExecutor(3).map(get,urls):print(name,json.dumps(result,ensure_ascii=False))
