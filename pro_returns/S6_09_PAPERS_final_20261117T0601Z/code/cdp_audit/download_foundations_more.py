from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,urllib.request
OUT=Path(__file__).resolve().parents[3]/'reference_downloads/cdp_audit'
urls={
'BS76':('https://djvu.online/file/2hQiOnz8WuoQk','.html'),
'Nakano1970':('https://ems.press/content/serial-article-files/41677','.pdf'),
'FujikiNakano1971':('https://www.jstage.jst.go.jp/article/kyotoms1969/7/3/7_3_637/_pdf/-char/ja','.pdf'),
'GrossSiebert2006I':('https://arxiv.org/pdf/math/0309070','.pdf'),
'Grauert1960':('https://www.numdam.org/article/PMIHES_1960__5__5_0.pdf','.pdf'),
'Grauert1963':('https://www.numdam.org/item/PMIHES_1963__16__35_0.pdf','.pdf'),
}
def get(item):
 key,(url,ext)=item
 try:
  with urllib.request.urlopen(url,timeout=20) as r: data=r.read()
  if ext=='.pdf' and not data.startswith(b'%PDF'): raise ValueError('not PDF')
  if ext=='.html' and b'challenge_id' in data: raise ValueError('anti-bot challenge; original source text available only through web retrieval')
  path=OUT/(key+ext);path.write_bytes(data)
  return dict(key=key,url=url,path=str(path.relative_to(OUT.parents[1])),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),status='downloaded')
 except Exception as e:return dict(key=key,url=url,status='download failed',error=str(e))
with ThreadPoolExecutor(max_workers=3) as pool: result=list(pool.map(get,urls.items()))
(OUT/'downloads_foundations_more.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
