from pathlib import Path
from urllib.request import urlopen
import hashlib
root=Path(__file__).resolve().parents[2]/"research_downloads"
root.mkdir(exist_ok=True)
urls={"Silverman_MSRI2006.pdf":"https://slmath-production-assets.sfo3.digitaloceanspaces.com/attachments/workshops/301/HtSurveyMSRIJan06.pdf", "CallSilverman1993.pdf":"https://www.numdam.org/item/CM_1993__89_2_163_0.pdf"}
for name,url in urls.items():
 try:
  with urlopen(url, timeout=30) as r:
   data=r.read(); final=r.url
  assert data.startswith(b"%PDF"),(name,data[:20])
  (root/name).write_bytes(data)
  print(name,len(data),hashlib.sha256(data).hexdigest(),final)
 except Exception as e:print(name,type(e).__name__,str(e))
