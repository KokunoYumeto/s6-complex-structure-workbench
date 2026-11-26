#!/usr/bin/env python3
"""Retrieve primary reading inputs outside the deliverable and record only metadata."""
from pathlib import Path
from urllib.request import Request,urlopen
from concurrent.futures import ThreadPoolExecutor
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
TEMP=ROOT.parents[1]/'tmp/c9_sources'
TEMP.mkdir(parents=True,exist_ok=True)
HEADERS={'User-Agent':'S6 publication primary-source scope check'}
def fetch(url):
 with urlopen(Request(url,headers=HEADERS),timeout=40) as r:
  data=r.read();return data,r.headers.get('Last-Modified','')
def keep(url,name):
 data,modified=fetch(url)
 (TEMP/name).write_bytes(data)
 return dict(url=url,temporary_name=name,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),last_modified=modified)
repo='https://api.github.com/repos/philip-engel/philip-engel.github.io'
commit=json.loads(fetch(repo+'/commits/main')[0])['sha']
paths=['api/README.md','api/engine/integral_mv.py','api/engine/local_model_database.py','api/engine/local_filling_models.py','api/engine/derived_gluing.py','api/engine/threefold_pipeline.py','api/engine/threefold_topology.py','api/engine/explorer_api.py','api/engine/nonfree_boundary.py','api/engine/parameterized_models.py','api/engine/mumford_models.py','api/engine/group_resolutions.py','api/engine/os_monodromy.py','api/engine/local_model_database.tar.gz','docs/index.html']
base='https://raw.githubusercontent.com/philip-engel/philip-engel.github.io/'+commit+'/threefold-explorer/'
with ThreadPoolExecutor(max_workers=4) as pool:
 records=list(pool.map(lambda p:keep(base+p,'explorer_'+Path(p).name),paths))
result=dict(retrieval_date='2026-11-26',purpose='Read actual marked cochain interfaces and scope; no independent geometric derivation or numerical execution claimed by this retrieval.',repository_commit=commit,sources=records)
out=ROOT/'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_primary_source_metadata.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print('Pinned Threefold Explorer commit',commit)
for r in records:print(r['temporary_name'],r['bytes'],r['sha256'])
print('Temporary third-party material retained outside checkpoint; metadata only in deliverable.')
