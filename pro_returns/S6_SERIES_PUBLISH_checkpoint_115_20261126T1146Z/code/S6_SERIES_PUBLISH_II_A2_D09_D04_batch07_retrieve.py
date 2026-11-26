"""Open historical program text outside deliverables; execute no producer."""
from pathlib import Path
import concurrent.futures
import datetime
import hashlib
import json
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch07_working'
TEMP = ROOT.parent.parent / 'S6_SERIES_PUBLISH_A_primary_temp/D09_batch07'
TEMP.mkdir(parents=True, exist_ok=True)
COMMIT = '83d76022bcd442278b760db9ff438afceed6c6ea'
PREFIX = f'https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/{COMMIT}/pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/'
stems = ['A_meridian_groups','D_monodromy_signatures','root_exceptional_leaves',
         'A_minimal_reduction','E_elliptic_roots','root_cusp_product']

def fetch(name):
    row = dict(name=name,url=PREFIX+name,repository_commit=COMMIT,
               attempted_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
               read_claim=False,executed=False)
    try:
        with urllib.request.urlopen(row['url'],timeout=40) as response:
            data=response.read()
            row.update(status=response.status,resolved_url=response.url,
                       bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        target=TEMP/name
        if target.exists():
            assert target.read_bytes()==data
        else:
            target.write_bytes(data)
        row['temporary_path']=str(target)
    except Exception as exc:
        row['error']=repr(exc)
    return row

names=[stem+suffix for stem in stems for suffix in ['.py','.out']]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    attempts=list(pool.map(fetch,names))
record=dict(completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            purpose='Historical source/output opening for bounded Paper II editorial comparison.',
            downloads_excluded_from_deliverables=True,attempts=attempts)
path=OUT/'S6_SERIES_PUBLISH_II_A2_batch07_retrieval_attempts_01.json'
assert not path.exists()
path.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
