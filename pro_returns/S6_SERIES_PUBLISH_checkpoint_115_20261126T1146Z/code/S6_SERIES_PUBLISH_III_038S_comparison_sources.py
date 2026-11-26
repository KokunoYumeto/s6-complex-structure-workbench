#!/usr/bin/env python3
"""Open Milnor's public primary scan outside the returned checkpoint tree."""
from datetime import datetime, timezone
import hashlib
from pathlib import Path
from urllib.request import urlopen
import subprocess

EXTERNAL = Path('/workspace/scratch/9cfb6f861d2c/S6_SERIES_PUBLISH_external_tmp')
EXTERNAL.mkdir(exist_ok=True)
URL = 'https://www.maths.ed.ac.uk/~v1ranick/papers/milnortop.pdf'
path = EXTERNAL / 'S6_SERIES_PUBLISH_III_038S_Milnor_primary.pdf'
with urlopen(URL, timeout=45) as response:
    data = response.read()
    final_url = response.url
    status = response.status
assert data.startswith(b'%PDF')
path.write_bytes(data)
print('UTC', datetime.now(timezone.utc).isoformat())
print('URL', URL)
print('Final URL', final_url)
print('Status', status)
print('Bytes', len(data))
print('SHA256', hashlib.sha256(data).hexdigest())
print('External PDF', path)

text_path = path.with_suffix('.txt')
subprocess.run(['pdftotext', '-layout', str(path), str(text_path)], check=True)
metadata = subprocess.run(['pdfinfo', str(path)], check=True, text=True, capture_output=True)
print(metadata.stdout)
print('External extraction', text_path)
print('No primary publication bytes written into the checkpoint.')
