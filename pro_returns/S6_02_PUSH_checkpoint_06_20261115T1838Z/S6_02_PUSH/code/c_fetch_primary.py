"""Download opened primary sources for local inspection; retain URLs and digests.
Downloaded third-party PDFs are outside the deliverable directory.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlopen, Request
import hashlib,json
BASE=Path(__file__).resolve().parent
DEST=BASE.parents[1]/'external_sources'
DEST.mkdir(exist_ok=True)
SOURCES={
 'Cerf1970.pdf':'https://www.numdam.org/item/PMIHES_1970__39__5_0.pdf',
 'KervaireMilnor1963.pdf':'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/kervaire-milnor.pdf',
 'EellsKuiper1962.pdf':'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/eellskuiper.pdf',
 'DuranRigas2008.pdf':'https://www.ime.unicamp.br/~rigas/equivHtpyProofs.pdf',
}
def get(pair):
 name,url=pair
 try:
  with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as r:
   data=r.read()
  if not data.startswith(b'%PDF'):
   raise ValueError('not a PDF')
  (DEST/name).write_bytes(data)
  return {'name':name,'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'result':'downloaded'}
 except Exception as e:
  return {'name':name,'url':url,'result':'failed','error':str(e)}
if __name__=='__main__':
 with ThreadPoolExecutor(max_workers=4) as p:
  result=list(p.map(get,SOURCES.items()))
 (BASE/'c_fetch_primary.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
