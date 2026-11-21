"""Reopen exact pinned program bytes lost in the execution-workspace reset."""
from pathlib import Path
import concurrent.futures, datetime, hashlib, json, urllib.request
R = Path(__file__).resolve().parents[1]
COMMIT = '83d76022bcd442278b760db9ff438afceed6c6ea'
TREE = R / 'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_pinned_program_tree.json'
paths = [
 'pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/' + name
 for name in ['C_euler.py', 'C_twists.py', 'E_checks.py', 'C_jets.py']
] + [
 'pro_returns/S6_06_BLIND_checkpoint_15_20261117T1457Z/S6_06_BLIND/code/part4/' + name
 for name in ['necessity_examples.py', 'example_mayer_vietoris.py', 'genus_one_conductor.py']
]
tree = json.loads(TREE.read_text())
assert tree['sha'] == COMMIT
entries = {x['path']: x for x in tree['tree']}
out = R / 'records/S6_SERIES_PUBLISH_II_opened_programs_recovery_01'
assert not out.exists()
out.mkdir()
def get(path):
 expected = entries[path]
 url = f'https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/{COMMIT}/{path}'
 req = urllib.request.Request(url, headers={'User-Agent': 'S6-publication-primary-source-check'})
 with urllib.request.urlopen(req, timeout=45) as response:
  body = response.read(); status = response.status
 assert status == 200 and len(body) == expected['size']
 blob = hashlib.sha1(b'blob ' + str(len(body)).encode() + b'\0' + body).hexdigest()
 assert blob == expected['sha']
 p = out / Path(path).name
 p.write_bytes(body)
 return dict(name=p.name, url=url, http_status=status, bytes=len(body), sha256=hashlib.sha256(body).hexdigest(), git_blob_sha1=blob, pinned_tree_exact_blob_match=True, local_path=str(p.relative_to(R)))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 rows = list(pool.map(get, paths))
record = dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), commit=COMMIT, tree_path=str(TREE.relative_to(R)), tree_sha256=hashlib.sha256(TREE.read_bytes()).hexdigest(), tree_truncated=tree['truncated'], scope='Only positively present exact tree entries are used. These source bytes are newly downloaded and verified after the reset. No old receipt is recreated and no absence claim is inferred from the truncated tree.', programs=rows, check_events_added=0)
(out / 'receipt.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
