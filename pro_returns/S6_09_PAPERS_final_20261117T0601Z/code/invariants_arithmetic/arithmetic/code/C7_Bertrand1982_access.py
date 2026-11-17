"""Check the public volume URL cited in a later mathematical bibliography.

No account, proxy, authorization header, or access-control workaround is used.
Full third-party source content remains outside the deliverable tree.
"""
from pathlib import Path
from urllib.request import urlopen
import hashlib
import subprocess

root = Path(__file__).resolve().parents[1]
url = ('https://plouffe.fr/simon/math/Seminaire%20de%20Theorie%20des%20'
       'Nombres,%20Paris,%201980-1981.pdf')
print('Public source URL:', url, flush=True)
try:
    with urlopen(url, timeout=35) as response:
        data = response.read(75_000_001)
        print('Final URL:', response.url, 'status:', response.status, flush=True)
    assert len(data) <= 75_000_000, 'Source exceeds research retrieval size limit'
    assert data.startswith(b'%PDF-'), 'Response is not a PDF'
    archive = root.parent / 'research_downloads/C7_division'
    archive.mkdir(parents=True, exist_ok=True)
    path = archive / 'C_Paris1980_81_volume.pdf'
    path.write_bytes(data)
    print('PATH:', path, 'BYTES:', len(data),
          'SHA256:', hashlib.sha256(data).hexdigest(), flush=True)
    subprocess.run(['pdfinfo', str(path)], check=True)
    subprocess.run(['pdftotext', '-f', '1', '-l', '25', '-layout',
                    str(path), str(archive/'C_Bertrand1982_first25.txt')],
                   check=True)
    out = archive / 'C_Bertrand1982_render'
    out.mkdir(exist_ok=True)
    subprocess.run(['pdftoppm', '-f', '5', '-l', '15', '-png', '-r', '130',
                    str(path), str(out/'page')], check=True)
except Exception as exc:
    print(type(exc).__name__ + ':', exc, flush=True)
