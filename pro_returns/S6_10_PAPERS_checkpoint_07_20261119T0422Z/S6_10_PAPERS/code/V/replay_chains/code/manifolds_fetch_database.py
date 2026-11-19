"""Retrieve the public research database into a sibling, non-deliverable cache.

The tabulated data are expressly excluded from the Explorer source-code licence.
This script records their public URL and checks the exact research snapshot hash;
it does not redistribute the data as part of this project's deliverable.
"""
from pathlib import Path
from urllib.request import urlopen
import hashlib,json,tarfile

root=Path(__file__).resolve().parents[1]
cache=root.parent/'external_cache'/'threefold_explorer'
cache.mkdir(parents=True,exist_ok=True)
manifest=json.loads((root/'records/manifolds_database_manifest.json').read_text())
for entry in manifest['files']:
    target=cache/entry['name']
    data=target.read_bytes() if target.exists() else urlopen(entry['url'],timeout=60).read()
    digest=hashlib.sha256(data).hexdigest()
    if digest!=entry['sha256']:
        raise RuntimeError('Public database snapshot changed; refusing unrecorded data: '+digest)
    target.write_bytes(data)
    with tarfile.open(target,'r:gz') as archive:
        archive.extractall(cache,filter='data')
    print(entry['name'],len(data),digest)
