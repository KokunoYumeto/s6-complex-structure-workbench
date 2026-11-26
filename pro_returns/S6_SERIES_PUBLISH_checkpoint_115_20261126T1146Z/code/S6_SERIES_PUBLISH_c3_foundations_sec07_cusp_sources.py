from pathlib import Path
import hashlib
import subprocess
import urllib.request

out=Path('/workspace/scratch/9fcd229a9ed4/base/S6_PUBLISH_c3_foundations_sources')
url='https://arxiv.org/pdf/1512.02840v1'
path=out/'S6_SERIES_PUBLISH_SiersmaTibar2017_v1.pdf'
with urllib.request.urlopen(url,timeout=40) as response:
    payload=response.read()
assert payload.startswith(b'%PDF'),payload[:80]
path.write_bytes(payload)
subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True)
print(url)
print(len(payload),hashlib.sha256(payload).hexdigest())
subprocess.run(['pdftotext','-f','1','-l','4','-layout',str(path),'-'],check=True)
