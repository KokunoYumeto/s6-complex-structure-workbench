"""Retrieve the two exact primary editions; downloads confer no reading credit."""
from pathlib import Path
import concurrent.futures,hashlib,json,urllib.request
P=Path(__file__).resolve().parents[2]
DEST=P/'analysis/I_sources'
def get(v):
    url=f'https://arxiv.org/pdf/2610.00250v{v}'
    row={'version':v,'url':url}
    try:
        with urllib.request.urlopen(url,timeout=40) as response:
            data=response.read();row['final_url']=response.url
        if not data.startswith(b'%PDF'):raise ValueError('Response is not a PDF')
        path=DEST/f'DGKXv{v}.pdf';path.write_bytes(data)
        row.update(path=str(path.relative_to(P)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    except Exception as error:row['failure']=str(error)
    return row
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    rows=list(pool.map(get,[1,2]))
(DEST/'DGKX_download_receipt.json').write_text(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=2))
