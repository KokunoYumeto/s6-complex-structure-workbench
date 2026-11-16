"""Fetch the pinned Julia runtime used for the integral-conjugacy calculation.

The runtime is a disposable sibling cache, never part of a deliverable ZIP.
The SHA256 is published on Julia's official old-releases page for1.10.10.
Hecke is installed separately in the same task-owned cache.
"""
from pathlib import Path
from urllib.request import urlopen
import hashlib, json, tarfile

root=Path(__file__).resolve().parents[1]
cache=root.parent/'external_cache'/'integral_conjugacy_runtime'
cache.mkdir(parents=True,exist_ok=True)
url='https://julialang-s3.julialang.org/bin/linux/x64/1.10/julia-1.10.10-linux-x86_64.tar.gz'
expected='6a78a03a71c7ab792e8673dc5cedb918e037f081ceb58b50971dfb7c64c5bf81'
archive=cache/'julia-1.10.10-linux-x86_64.tar.gz'
if not archive.exists():
    with urlopen(url,timeout=45) as response, archive.open('wb') as out:
        while True:
            block=response.read(1024*1024)
            if not block:break
            out.write(block)
actual=hashlib.sha256(archive.read_bytes()).hexdigest()
if actual!=expected:raise RuntimeError('Julia archive checksum mismatch: '+actual)
runtime=cache/'julia-1.10.10'
if not runtime.exists():
    with tarfile.open(archive,'r:gz') as package:package.extractall(cache,filter='data')
record={'runtime_version':'1.10.10','url':url,'sha256':actual,'bytes':archive.stat().st_size,'binary':str(runtime/'bin/julia')}
(root/'records/integral_conjugacy_runtime.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
