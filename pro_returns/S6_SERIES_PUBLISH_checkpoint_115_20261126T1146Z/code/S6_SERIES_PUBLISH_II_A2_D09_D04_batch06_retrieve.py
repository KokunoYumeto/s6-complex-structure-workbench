"""Open pinned historical program sources/outputs; retain downloads outside current.

Reading and execution claims are deliberately separate from successful retrieval.
"""
from pathlib import Path
import concurrent.futures
import datetime
import hashlib
import json
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
TEMP = ROOT.parents[1] / 'S6_SERIES_PUBLISH_A_primary_temp/D09_batch06'
TEMP.mkdir(parents=True, exist_ok=True)
OUT = ROOT / 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch06_working'
COMMIT = '83d76022bcd442278b760db9ff438afceed6c6ea'
BASE = 'https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/' + COMMIT + '/'
CDP = 'pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/'
BLIND = 'pro_returns/S6_06_BLIND_checkpoint_15_20261117T1457Z/S6_06_BLIND/code/part4/'
GRIND = 'pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z/'
jobs = []
for stem in ['E_triple_images', 'A_low_delta_cusp', 'E_binary_products', 'E_cubic_double',
             'D_trivial_monodromy', 'A_return_germs', 'root_cyclic_elliptic_types']:
    for ext in ['.py', '.out']:
        jobs.append((stem + ext, CDP + stem + ext))
for name in ['example_mayer_vietoris.py', 'example_mayer_vietoris.out', 'example_matrices.json']:
    jobs.append((name, BLIND + name))
for stem in ['independent_sign_checks', 'UN24_UN39_exact_certificate_08']:
    jobs.append((stem + '.py', GRIND + 'code/current_audits/audit_sign/code/' + stem + '.py'))
    jobs.append((stem + '.json', GRIND + 'code/current_audits/audit_sign/' + stem + '.json'))
    jobs.append((stem + '.stdout.txt', GRIND + 'code/current_audits/audit_sign/' + stem + '.stdout.txt'))

def retrieve(job):
    name, relative = job
    url = BASE + relative
    row = dict(name=name, url=url, repository_commit=COMMIT,
               attempted_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
               read_claim=False, executed=False)
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read()
            row.update(status=response.status, resolved_url=response.url)
        path = TEMP / name
        if path.exists():
            assert path.read_bytes() == data
        else:
            path.write_bytes(data)
        row.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), temporary_path=str(path))
    except Exception as error:
        row.update(error=repr(error))
    return row

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    rows = list(executor.map(retrieve, jobs))
record = dict(completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              purpose='Exact historical source/output opening for a post-reading editorial comparison',
              downloads_excluded_from_deliverables=True, attempts=rows)
path = OUT / 'S6_SERIES_PUBLISH_II_A2_batch06_retrieval_attempts_01.json'
assert not path.exists(), path
path.write_text(json.dumps(record, indent=2) + '\n')
for row in rows:
    print(json.dumps({k: row[k] for k in ['name', 'status', 'bytes', 'sha256', 'error'] if k in row}))
