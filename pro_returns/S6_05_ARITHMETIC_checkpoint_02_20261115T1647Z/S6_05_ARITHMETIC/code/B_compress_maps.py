"""Lossless compression of dense orbit certificates; preserve exact bytes."""
from pathlib import Path
import gzip,hashlib,shutil,json
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'records';CACHE=ROOT.parent/'B_cache';CACHE.mkdir(exist_ok=True)
out=[]
for p in sorted(REC.glob('B_A[12]_stratum_*.bin')):
 target=p.with_suffix('.bin.gz')
 with p.open('rb') as a,gzip.open(target,'wb',compresslevel=9) as b:shutil.copyfileobj(a,b)
 h=hashlib.sha256(p.read_bytes()).hexdigest()
 with gzip.open(target,'rb') as f:assert hashlib.sha256(f.read()).hexdigest()==h
 out.append({'file':target.name,'uncompressed_bytes':p.stat().st_size,'sha256_uncompressed':h,'compressed_bytes':target.stat().st_size})
 p.replace(CACHE/p.name)
 print(target.name,out[-1],flush=True)
(REC/'B_orbit_map_manifest.json').write_text(json.dumps(out))
