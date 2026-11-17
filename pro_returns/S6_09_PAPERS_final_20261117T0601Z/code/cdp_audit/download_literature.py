"""Retrieve primary references outside deliverables; preserve only metadata there."""
from pathlib import Path
from urllib.request import Request,urlopen
from concurrent.futures import ThreadPoolExecutor
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'reference_downloads/cdp_audit';OUT.mkdir(parents=True,exist_ok=True)
URLS={
'GS2014':'https://arxiv.org/pdf/1109.2612',
'CDP2020':'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CDF2D04CFB35CEE105E10B188D97D68A/S0010437X19007802a.pdf/the-algebraic-dimension-of-compact-complex-threefolds-with-vanishing-second-betti-number.pdf',
'CDP1998_preprint':'https://arxiv.org/pdf/math/9607215',
'HKP2000_preprint':'https://arxiv.org/pdf/math/9812076',
'SchnellLecture3':'https://www.math.stonybrook.edu/~cschnell/mat615/lectures/lecture3.pdf',
'ACampo1975':'https://www.e-periodica.ch/cntmng?bot=1&pid=com-001%3A1975%3A50%3A%3A27',
'Kulikov1981':'https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1953&what=fullteng',
'Kulikov1977':'https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1877&what=fullteng',
'Cartan1957':'https://www.numdam.org/article/BSMF_1957__85__77_0.pdf',
'Bingener1980':'https://www.numdam.org/article/ASENS_1980_4_13_3_317_0.pdf',
'RamisRuget1970':'https://www.numdam.org/article/PMIHES_1970__38__77_0.pdf',
}
def run(kv):
 k,u=kv;p=OUT/(k+'.pdf');r={'key':k,'url':u}
 try:
  if p.exists(): d=p.read_bytes()
  else:d=urlopen(Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=18).read()
  if not d.startswith(b'%PDF'): raise ValueError('response is not PDF')
  p.write_bytes(d);r.update(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(d).hexdigest(),bytes=len(d),status='downloaded')
 except Exception as e:r.update(status='download failed',error=str(e))
 return r
with ThreadPoolExecutor(max_workers=4) as pool: rows=list(pool.map(run,URLS.items()))
(OUT/'downloads.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
