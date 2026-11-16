"""Read-only retrieval of current public primary-source Explorer files."""
from pathlib import Path
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import json
base='https://philip-engel.github.io/threefold-explorer/'
root=Path(__file__).resolve().parents[1]/'records'/'explorer'
root.mkdir(exist_ok=True)
paths=['index.html','assets/config.js','assets/app.js','assets/rational-sphere-presets.json',
       'docs/index.html','docs/MATHEMATICAL_SCOPE.md','docs/RUNTIME_DATABASE.md',
       'docs/COLLISION_PROFILES.md','COPYRIGHT.md','LICENSE-CODE.txt','LICENSE-DOCUMENTATION.md']
tree=json.load(urlopen('https://api.github.com/repos/philip-engel/philip-engel.github.io/git/trees/main?recursive=1',timeout=30))
root.joinpath('repository_tree.json').write_text(json.dumps(tree,indent=2))
paths += [x['path'].split('threefold-explorer/',1)[1] for x in tree['tree']
          if x['type']=='blob' and x['path'].startswith('threefold-explorer/api/')
          and 'local_model_database/' not in x['path']
          and not x['path'].endswith('local_model_database.tar.gz')]
base='https://raw.githubusercontent.com/philip-engel/philip-engel.github.io/main/threefold-explorer/'
def fetch(rel):
    dst=root/rel; dst.parent.mkdir(parents=True,exist_ok=True)
    try:
        data=urlopen(base+rel,timeout=30).read();dst.write_bytes(data)
        return {'url':base+rel,'path':str(dst.relative_to(root)),'bytes':len(data)}
    except Exception as e: return {'url':base+rel,'error':str(e)}
with ThreadPoolExecutor(max_workers=8) as pool:
    for item in pool.map(fetch,paths): print(json.dumps(item),flush=True)
