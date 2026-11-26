"""Render the exact SS10 primary pages for the LS fresh derivation.

The source PDF and page images remain outside the returned work tree.
Only metadata and actual command streams are recorded here.
"""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import subprocess

PDF = Path('/workspace/scratch/bd22a44d51b1/primary_c7_ks/schuett_shioda_0907.0298.pdf')
TEMP = Path('/tmp/S6_SERIES_PUBLISH_c7_LS_SS10')
TEMP.mkdir(exist_ok=True)
assert sha256(PDF.read_bytes()).hexdigest() == 'eeac47d53b52e96a1d2457a131dcce474332dd6b226e4dcd944575e995aa44b1'
print('SOURCE https://arxiv.org/pdf/0907.0298v3; arXiv v3, 9 July 2010', flush=True)
print('PDF_SHA256', sha256(PDF.read_bytes()).hexdigest(), flush=True)
for number in (25, 32, 33, 34, 50, 51, 52):
    prefix = TEMP / ('S6_SERIES_PUBLISH_SS10_page_' + str(number))
    result = subprocess.run(['pdftoppm', '-f', str(number), '-l', str(number),
                             '-singlefile', '-png', '-scale-to', '1800',
                             str(PDF), str(prefix)], text=True, capture_output=True)
    print('PAGE', number, 'EXIT', result.returncode,
          'STDOUT', repr(result.stdout), 'STDERR', repr(result.stderr), flush=True)
    assert result.returncode == 0
    target = prefix.with_suffix('.png')
    assert target.is_file()
    print('IMAGE', target, 'BYTES', target.stat().st_size, flush=True)
print('Rendering only; visual reading credit begins when the images are opened.', flush=True)
print('COMPLETED_UTC', datetime.now(timezone.utc).isoformat(), flush=True)
