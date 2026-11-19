"""Archive primary sources opened during the second hour of this blind run."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import urllib.request, subprocess, json
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'records/primary_sources'
SOURCES={
'Lojasiewicz64':'https://www.numdam.org/item/ASNSP_1964_3_18_4_449_0.pdf',
'BobadillaKollar12':'https://www.journalofsing.org/volume5/bobadilla-kollar.pdf'}
def fetch(item):
    name,url=item
    row={'name':name,'url':url,'time':datetime.now(timezone.utc).isoformat()}
    try:
        data=urllib.request.urlopen(url,timeout=25).read()
        assert data.startswith(b'%PDF')
        pdf=DEST/(name+'.pdf');pdf.write_bytes(data)
        subprocess.run(['pdftotext','-layout',str(pdf),str(pdf.with_suffix('.txt'))],check=True)
        row.update(status='downloaded',bytes=len(data))
    except Exception as e:
        row.update(status='failed',error=str(e))
    return row
with ThreadPoolExecutor(max_workers=2) as pool:
    rows=list(pool.map(fetch,SOURCES.items()))
(DEST/'root_second_hour_fetch.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
with (ROOT/'S6_06_BLIND_literature_log.md').open('a') as f:
    now=datetime.now(timezone.utc).isoformat()
    f.write('| '+now+' | Primary searches on torus degeneration fundamental groups and compatible analytic triangulations; Lojasiewicz1964 Theorems1–2 pp463–464; Bobadilla–Kollar2012 Definition1 and following retraction statement p85 | Verify the local specialization group argument for arbitrary irreducible supports | Opened by root through the web tool before archival download. The compatible-triangulation theorem supplies an independent neighbourhood-retraction construction. No assertion of homotopy triviality of the family is used. |\n')
    for r in rows:
        f.write('| '+r['time']+' | '+r['url']+' | Archive the opened primary source | '+r['status']+' |\n')
