"""Archive two positively identified primary analytic cohomology sources."""
from pathlib import Path
import datetime, hashlib, json, subprocess, urllib.request
R = Path(__file__).resolve().parents[1]
O = R / 'records/S6_SERIES_PUBLISH_II_analytic_primary_inputs_01'
assert not O.exists()
O.mkdir()
sources = [
    ('Douady1974', 'https://www.numdam.org/article/AST_1974__16__49_0.pdf',
     'Asterisque 16 (1974), 49–62; section 6 Theorem 2 p.59; sections 7–8 pp.61–62'),
    ('Grothendieck1961', 'https://www.numdam.org/item/SHC_1960-1961__13_2_A2_0.pdf',
     'Seminaire Henri Cartan 13 no.2 (1960–1961), expose 15, Theorem 1.3 p.2 and Corollary 1.4 pp.2–4'),
]
rows = []
for name, url, locator in sources:
    request = urllib.request.Request(url, headers={'User-Agent': 'S6-publication-primary-source-check'})
    with urllib.request.urlopen(request, timeout=45) as response:
        body = response.read()
        status = response.status
    assert status == 200 and body.startswith(b'%PDF')
    p = O / f'{name}.pdf'
    p.write_bytes(body)
    t = p.with_suffix('.txt')
    subprocess.run(['pdftotext', '-layout', str(p), str(t)], check=True)
    rows.append(dict(name=name, url=url, http_status=status, bytes=len(body),
                     pdf_path=str(p.relative_to(R)), pdf_sha256=hashlib.sha256(body).hexdigest(),
                     text_path=str(t.relative_to(R)), text_sha256=hashlib.sha256(t.read_bytes()).hexdigest(),
                     locator=locator))
receipt = dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), sources=rows,
               target_proofs_supplied=False, mathematical_check_events_added=0,
               scope='Primary sources for a statement-only checker input; PDF download itself is not a mathematical check.')
(O / 'download_receipt.json').write_text(json.dumps(receipt, indent=2, ensure_ascii=False)+'\n')
print(json.dumps(receipt, indent=2, ensure_ascii=False))
