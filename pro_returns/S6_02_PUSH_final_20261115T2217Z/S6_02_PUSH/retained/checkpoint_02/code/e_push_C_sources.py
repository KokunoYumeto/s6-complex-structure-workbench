"""Retain primary literature fetched during the independent C attempt."""
from pathlib import Path
import hashlib,json,subprocess,urllib.request
root=Path(__file__).resolve().parents[1]
outdir=root/'evidence/C_independent_primary'
outdir.mkdir(exist_ok=True)
sources={
 'AtiyahSinger1968III':'https://math.uchicago.edu/~shmuel/tom-readings/AS%20III.pdf',
 'Davis1982':'https://people.math.osu.edu/davis.12/old_papers/AJM-82.pdf',
 'HarveyKerinShankar2020':'https://cronfa.swan.ac.uk/Record/cronfa56479/Download/56479__19682__62bb12791aea4db3bed228393f6865d9.pdf',
 'CrowleySchick2013':'https://msp.org/gt/2013/17-3/gt-v17-n3-p11-s.pdf',
 'Takase2007':'https://arxiv.org/pdf/math/0506356',
 'Moriyama2011':'https://www.ms.u-tokyo.ac.jp/journal/pdf/jms180204.pdf'}
manifest=[]
for key,url in sources.items():
    p=outdir/(key+'.pdf')
    if not p.exists():
        with urllib.request.urlopen(url,timeout=45) as response:
            p.write_bytes(response.read())
    data=p.read_bytes()
    assert data.startswith(b'%PDF')
    subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
    manifest.append({'key':key,'url':url,'bytes':len(data),
                     'sha256':hashlib.sha256(data).hexdigest(),
                     'extracted_text_bytes':p.with_suffix('.txt').stat().st_size})
print(json.dumps(manifest,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(manifest,indent=2)+'\n')
