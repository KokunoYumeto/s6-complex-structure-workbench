#!/usr/bin/env python3
"""Fetch exact Yang v1 source/PDF into /tmp; report byte identities only."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,tarfile,urllib.request

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
TEMP=Path('/tmp/S6_SERIES_PUBLISH_c5_02KK_primary')
TEMP.mkdir(exist_ok=True)
attached=BASE/'S6_GRIND_6_literature/papers/arXiv_2609.29666_Yang_src/Compact_Complex_Threefolds_REPAIRED_v4_5.tex'
out=[]
for kind,extension in [('src','tar'),('pdf','pdf')]:
    url='https://arxiv.org/'+kind+'/2609.29666v1'
    path=TEMP/('Yang_v1.'+extension)
    if not path.exists():
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=45) as response:
            data=response.read()
        path.write_bytes(data)
    data=path.read_bytes()
    row={'version':'v1','kind':kind,'url':url,'bytes':len(data),
         'sha256':hashlib.sha256(data).hexdigest()}
    if kind=='src':
        with tarfile.open(path) as archive:
            names=[n for n in archive.getnames() if n.endswith('.tex')]
            name=next(n for n in names if 'Compact_Complex_Threefolds' in n)
            tex=archive.extractfile(name).read()
        row.update(main_tex=name,main_tex_sha256=hashlib.sha256(tex).hexdigest(),
                   attached_equal=tex==attached.read_bytes())
        (TEMP/'Yang_v1.tex').write_bytes(tex)
    else:
        assert data.startswith(b'%PDF-')
    out.append(row)
print(json.dumps({'retrieved_utc':datetime.now(timezone.utc).isoformat(),
                  'sources':out,'source_content_in_deliverables':False},indent=2))
