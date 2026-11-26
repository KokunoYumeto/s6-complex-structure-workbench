from pathlib import Path
import datetime as dt, hashlib, json, subprocess, sys, urllib.request

R=Path(__file__).resolve().parents[1]
inputs={
 'Demailly':dict(url='https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf', sha256='d7c7654a7417e8322e5dcf8fe8ec818b4c1a18cf280b41f2df5a871b776d89a1', pages=(79,80), locator='ChapterII section2.A, printed79-80, complete preparation proof and Theorem(2.1).'),
 'Hatcher':dict(url='https://pi.math.cornell.edu/~hatcher/AT/AT.pdf', sha256='bebb3032bf9021b956da3bd070eb6c67dc662cf849be9cdf6679f677560e5618', pages=(254,255), locator='Printed245-246, Theorem3.35 and compact-support/proper-map discussion. No claim to the complete multi-page proof or visual diagrams.')
}
key=sys.argv[1]; item=inputs[key]
with urllib.request.urlopen(item['url'],timeout=45) as response: data=response.read()
assert hashlib.sha256(data).hexdigest()==item['sha256']
p=subprocess.run(['pdftotext','-f',str(item['pages'][0]),'-l',str(item['pages'][1]),'-layout','-','-'],input=data,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
assert p.stdout and not p.stderr
record=dict(acquired_utc=dt.datetime.now(dt.timezone.utc).isoformat(),key=key,url=item['url'],pdf_sha256=item['sha256'],pdf_bytes=len(data),locator=item['locator'],pdf_pages=item['pages'],extracted_text_sha256=hashlib.sha256(p.stdout).hexdigest(),extracted_text_bytes=len(p.stdout),root_reading_pending=True,visual_credit=0,events_added=0,retained_download=False)
out=R/f'records/S6_SERIES_PUBLISH_II_YC_root_primary_{key}_01.json';assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
print(p.stdout.decode())
print(json.dumps(record))
