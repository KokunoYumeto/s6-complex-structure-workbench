from pathlib import Path
import urllib.request, hashlib, json, subprocess

out = Path(__file__).resolve().parents[1] / 'primary_sources'
url = 'https://arxiv.org/pdf/1406.2226v3'
pdf = out / 'CrowleyNordstrom2019_v3_fresh.pdf'
req = urllib.request.Request(url, headers={'User-Agent': 'S6 mathematical source verification'})
with urllib.request.urlopen(req, timeout=45) as response:
    data = response.read()
pdf.write_bytes(data)
assert data[:4] == b'%PDF'
txt = pdf.with_suffix('.txt')
proc = subprocess.run(['pdftotext', '-layout', str(pdf), str(txt)], capture_output=True, text=True)
record = {'url': url, 'file': str(pdf), 'size': len(data),
          'sha256': hashlib.sha256(data).hexdigest(),
          'pdftotext_returncode': proc.returncode,
          'pdftotext_stderr': proc.stderr}
(out / 'CrowleyNordstrom2019_v3_fresh_metadata.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
assert proc.returncode == 0
