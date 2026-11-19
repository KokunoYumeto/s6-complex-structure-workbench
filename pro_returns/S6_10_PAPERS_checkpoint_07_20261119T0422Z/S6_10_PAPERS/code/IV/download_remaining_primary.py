"""Download explicitly identified primary sources for current local readings."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime, hashlib, json, subprocess, urllib.request

root = Path(__file__).resolve().parents[2]
dest = root / 'analysis/IV/references'
items = [
    ('Cerf1970', 'https://www.numdam.org/item/PMIHES_1970__39__5_0.pdf'),
    ('Smale1961', 'https://math.uchicago.edu/~shmuel/tom-readings/Smale,%20PC.pdf'),
    ('EellsKuiper1962', 'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/eellskuiper.pdf'),
    ('Takase2005v1', 'https://arxiv.org/pdf/math/0506356'),
]

def get(item):
    key, url = item
    rec = {'key': key, 'url': url, 'started_at': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=50) as response:
            data = response.read()
        if not data.startswith(b'%PDF'):
            raise ValueError('The response is not a PDF')
        path = dest / (key + '.pdf')
        path.write_bytes(data)
        subprocess.run(['pdftotext', '-layout', str(path), str(path.with_suffix('.txt'))], check=True)
        rec.update({'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest(), 'path':str(path.relative_to(root)), 'status':'downloaded; reading pending'})
    except Exception as exc:
        rec.update({'status':'failed', 'error':str(exc)})
    rec['ended_at'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    return rec

with ThreadPoolExecutor(max_workers=4) as pool:
    records = list(pool.map(get, items))
(dest / 'remaining_download_records.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
