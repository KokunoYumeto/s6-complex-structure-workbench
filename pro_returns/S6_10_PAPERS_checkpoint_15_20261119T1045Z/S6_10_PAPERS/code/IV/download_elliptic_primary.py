from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime,hashlib,json,subprocess,urllib.request
root=Path(__file__).resolve().parents[2]
dest=root/'analysis/IV/references'
items=[
 ('OguisoShioda1991','https://rikkyo.repo.nii.ac.jp/record/10006/files/AA00610867_40-01_08.pdf'),
 ('Shioda1990','https://rikkyo.repo.nii.ac.jp/record/10027/files/AA00610867_39-02_05.pdf'),
]
def get(item):
 key,url=item
 rec={'key':key,'url':url,'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as resp:data=resp.read()
  assert data.startswith(b'%PDF')
  p=dest/(key+'.pdf');p.write_bytes(data)
  subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
  rec.update(status='downloaded; reading pending',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),path=str(p.relative_to(root)))
 except Exception as exc:rec.update(status='failed',error=str(exc))
 rec['ended_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 return rec
with ThreadPoolExecutor(max_workers=2) as pool:records=list(pool.map(get,items))
(dest/'elliptic_download_records.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
