"""Download exact primary inputs for the old-source proof review.

Downloads and text extraction confer no proof or source-reading credit.
"""
from pathlib import Path
import concurrent.futures,hashlib,json,urllib.request
import fitz
P=Path(__file__).resolve().parents[2];D=P/'analysis/IV/references'
targets={
 'ChernSimons1974E':'https://math.mit.edu/juvitop/pastseminars/notes_2019_Fall/Chern-Simons.pdf',
 'CrowleyNordstrom2020':'https://arxiv.org/pdf/1411.0656v4',
 'FintushelPao1983D':'https://msp.org/pjm/1983/109-2/pjm-v109-n2-p09-p.pdf',
 'Wall1966VE':'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/wclass5.pdf',
 'Wall1967CorrE':'https://link.springer.com/content/pdf/10.1007/BF01425407.pdf',
 'Olbermann2010D':'https://msp.org/agt/2010/10-4/agt-v10-n4-p03-p.pdf',
}
def fetch(item):
 key,url=item;r={'key':key,'url':url}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=40) as response:raw=response.read();r['final_url']=response.url
  assert raw.startswith(b'%PDF'), 'Response is not a PDF'
  f=D/(key+'.pdf');f.write_bytes(raw);d=fitz.open(f)
  (D/(key+'.txt')).write_text('\n'.join(f'=== PDF PAGE {i+1} ===\n'+x.get_text() for i,x in enumerate(d)))
  r.update(path=str(f.relative_to(P)),bytes=len(raw),pages=len(d),sha256=hashlib.sha256(raw).hexdigest())
 except Exception as error:r['error']=str(error)
 return r
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(fetch,targets.items()))
(D/'root_primary_downloads.json').write_text(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=2))
