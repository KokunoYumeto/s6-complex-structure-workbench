"""Run only after the independent Part 5 proof is saved in checkpoint 01."""
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import urllib.request,json,subprocess
root=Path(__file__).resolve().parents[1]
assert (root/'records/checkpoint_01_saved.json').exists()
dest=root/'records/part5_comparison';dest.mkdir(exist_ok=True)
def get(version):
    rows=[]
    for base in ['https://arxiv.org/pdf/','https://export.arxiv.org/pdf/']:
        url=base+'2610.00250'+version
        row={'time':datetime.now(timezone.utc).isoformat(),'url':url,'version':version}
        try:
            data=urllib.request.urlopen(url,timeout=25).read()
            if not data.startswith(b'%PDF'):raise ValueError('Not a PDF')
            p=dest/f'2610.00250{version}.pdf';p.write_bytes(data)
            subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
            row.update(status='downloaded',bytes=len(data));rows.append(row);break
        except Exception as e:row.update(status='failed',error=str(e));rows.append(row)
    return rows
with ThreadPoolExecutor(max_workers=2) as pool:rows=sum(list(pool.map(get,['v1','v2'])),[])
(dest/'fetch_log.json').write_text(json.dumps(rows,indent=2)+'\n')
for row in rows:print(json.dumps(row))
with (root/'S6_06_BLIND_literature_log.md').open('a') as f:
    for r in sorted(rows,key=lambda x:x['time']):
        f.write('| '+r['time']+' | '+r['url']+' | Post-checkpoint Part5 comparison | '+r['status']+': '+str(r.get('bytes',r.get('error','')))+' |\n')
