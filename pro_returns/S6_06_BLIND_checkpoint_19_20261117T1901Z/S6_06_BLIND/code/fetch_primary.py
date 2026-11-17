"""Fetch only explicitly identified, permitted primary sources; no discovery."""
from pathlib import Path
from datetime import datetime,timezone
import urllib.request, json
root=Path(__file__).resolve().parents[1]
dest=root/'records'/'primary_sources';dest.mkdir(exist_ok=True)
sources=[
 ('OS91.pdf','https://rikkyo.repo.nii.ac.jp/record/10006/files/AA00610867_40-01_08.pdf'),
 ('Shi90.pdf','https://rikkyo.repo.nii.ac.jp/record/10027/files/AA00610867_39-02_05.pdf'),
 ('Jin26.pdf','https://arxiv.org/pdf/2608.26698'),
]
results=[]
for name,url in sources:
 row={'time':datetime.now(timezone.utc).isoformat(),'name':name,'url':url}
 try:
  with urllib.request.urlopen(url,timeout=20) as f:data=f.read()
  if not data.startswith(b'%PDF'): raise ValueError('response is not PDF')
  (dest/name).write_bytes(data)
  row.update(status='downloaded',bytes=len(data))
 except Exception as e:row.update(status='failed',error=str(e))
 results.append(row);print(json.dumps(row),flush=True)
(root/'records'/'primary_fetch.json').write_text(json.dumps(results,indent=2))
