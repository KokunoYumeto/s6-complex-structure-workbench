#!/usr/bin/env python3
"""Cache opened primary texts outside the deliverable; retain only metadata inside."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT.parent/'external_sources'/'E_hopf_primary'
DEST.mkdir(parents=True,exist_ok=True)
SOURCES = [
 ('CDP2020.pdf','https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CDF2D04CFB35CEE105E10B188D97D68A/S0010437X19007802a.pdf/the-algebraic-dimension-of-compact-complex-threefolds-with-vanishing-second-betti-number.pdf','Publisher original; Theorem2.1 and Sections4,6,7 opened. Theorem2.2 not imported.'),
 ('KerrLazaSaito2022.pdf','https://content.algebraicgeometry.nl/2022-4/2022-4-014.pdf','Publisher original; Proposition1 and Remark2.4 opened.'),
 ('Dloussky2005_v3.pdf','https://arxiv.org/pdf/math/0406387','Author arXiv v3; Section1.3 opened, trace and determinant discussion.'),
 ('Fujino2021_author.pdf','https://www.math.kyoto-u.ac.jp/~fujino/kahlersurface6.pdf','Author version; original publisher full text Definition3.1 and Lemma3.3/Corollary3.4 separately opened.'),
 ('BHPV2004_VI_preview.pdf','https://page-one.springer.com/pdf/preview/10.1007/978-3-642-57739-0_7','Official publisher two-page preview, pp243-244; Theorem1.1 and Table10 opened. No other book pages claimed opened.'),
 ('Fujimoto1988.pdf','https://scispace.com/pdf/logarithmic-transformations-on-elliptic-fiber-spaces-1uinrvp8jj.pdf','Mirror of original journal article; printed pp98-99 and Example3.4 opened. Primary text, mirror host.')
]

def fetch(source):
    name,url,scope=source
    path=DEST/name
    record={'filename':name,'url':url,'scope':scope,'local_external_path':str(path)}
    try:
        if path.exists() and path.read_bytes().startswith(b'%PDF'):
            data=path.read_bytes()
            record['download']='cached'
        else:
            req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (mathematics source verification)'})
            with urllib.request.urlopen(req,timeout=40) as response:
                data=response.read()
            if not data.startswith(b'%PDF'):
                raise ValueError('response is not a PDF')
            path.write_bytes(data)
            record['download']='saved'
        record.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    except Exception as exc:
        record.update(download='failed',error=f'{type(exc).__name__}: {exc}')
    return record

with ThreadPoolExecutor(max_workers=4) as pool:
    records=list(pool.map(fetch,SOURCES))
result={'accessed_utc':datetime.now(timezone.utc).isoformat(),'full_texts_outside_package':True,'sources':records}
payload=json.dumps(result,indent=2)+'\n'
(ROOT/'evidence'/'E_hopf_sources.json').write_text(payload)
(ROOT/'code'/'e_push_hopf_sources.out').write_text(payload)
print(payload,end='')
