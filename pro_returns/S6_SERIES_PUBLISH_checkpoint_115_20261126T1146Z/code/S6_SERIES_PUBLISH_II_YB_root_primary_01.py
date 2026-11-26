from pathlib import Path
import datetime as dt,hashlib,json,subprocess,urllib.request
R=Path(__file__).resolve().parents[1]
url='https://content.algebraicgeometry.nl/2022-4/2022-4-014.pdf'
with urllib.request.urlopen(url,timeout=45) as response:
 data=response.read()
assert hashlib.sha256(data).hexdigest()=='b0898c9eeee06c4613b63bb9cfe4cc0da9ba3190c378b951586b5f5ef9a66bde'
p=subprocess.run(['pdftotext','-f','5','-l','6','-layout','-','-'],input=data,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
assert p.stdout and not p.stderr
record=dict(acquired_utc=dt.datetime.now(dt.timezone.utc).isoformat(),url=url,
 bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
 locator='Section1.1, equations(1.1.1)-(1.1.3), printed480, and full analytic-scope continuation printed481; PDF pages5-6.',
 extractor='pdftotext -f 5 -l 6 -layout - -',text_sha256=hashlib.sha256(p.stdout).hexdigest(),text_bytes=len(p.stdout),
 acquisition='Primary journal PDF read in memory and exact pages extracted; no downloaded PDF retained in current.',
 root_reading_pending=True,visual_reading_credit=0,check_events_added=0)
out=R/'records/S6_SERIES_PUBLISH_II_YB_root_primary_01.json';assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
print(p.stdout.decode())
print(json.dumps(record))
