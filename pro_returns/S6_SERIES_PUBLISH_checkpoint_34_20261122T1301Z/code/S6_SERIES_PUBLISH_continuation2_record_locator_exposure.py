from pathlib import Path
import datetime as dt, hashlib, json, re

R = Path(__file__).resolve().parents[1]
source = R / 'S6_SERIES_PUBLISH_II.tex'
b = source.read_bytes()
assert hashlib.sha256(b).hexdigest() == 'f36a31dacdc81b2545513acba04e6c5889749bf08ad80927cc02084263215066'
lines = b.decode().splitlines()
observed = [34,35,36,37,253,326,489,4725,5527,5542,5555,5963,6012,6829,7066,7227,7622,7996,7997,8808,9126,9138,9282,9316,9392,9561,9744,9791,9850,10009,10018,10048,10053,13586,14139,14299,14331,14333,14630,14692,14705,14733,20782,21280,21359,21607,21867,21898,21922,22839,23776,24548,25392,25529,25934,26100,26497,26517,26777,27759,28803,29115,29332,29435,29449]
headers = []
for i, line in enumerate(lines, 1):
    m = re.search(r'\\hypertarget\{tag-([^}]+)\}\{\}\\label\{([^}]+)\}', line)
    if m:
        headers.append((i, m.group(1), m.group(2)))
rows = []
for n in observed:
    earlier = [h for h in headers if h[0] <= n]
    nearest = earlier[-1] if earlier else None
    rows.append(dict(line=n, text=lines[n-1], nearest_preceding_tag=nearest[1] if nearest else None, nearest_preceding_owner=nearest[2] if nearest else None, locator_scope='Nearest preceding statement header only; this does not certify proof ownership across intervening sections.'))
now = dt.datetime.now(dt.timezone.utc).isoformat()
out = R / 'records/S6_SERIES_PUBLISH_II_root_locator_exposure_01.json'
assert not out.exists()
record = dict(recorded_utc=now, checker='root', source_sha256=hashlib.sha256(b).hexdigest(), actual_command="rg -n 'corollary|global sections|vector fields|HKP|main:F|main:G|scalar' ../S6_PUBLISH_literature_arxiv/math_9812076/math_9812076.tex S6_SERIES_PUBLISH_II.tex | head -n 75", purpose='Locate frontmatter primary-source credits and the HKP corollary.', exposure=rows, chronology='The returned one-line hits were displayed before the complete XU frozen-derivation reading. No whole pending target proof was displayed by this search. The root reviews are comparative reviews and receive no independent targeted-check credit; all checker-agent freezes keep their own recorded chronology. This search output was not sent to the independent checkers.', events_added=0, page_reading_credit=0)
out.write_text(json.dumps(record, indent=2) + '\n')
receipt = R / 'records/S6_SERIES_PUBLISH_checkpoint_27_delivery.json'
rb = receipt.read_bytes()
rr = json.loads(rb)
mtime = dt.datetime.fromtimestamp(receipt.stat().st_mtime, dt.timezone.utc).isoformat()
assert rr['created_utc'] == '2026-11-22T07:49:27Z'
assert mtime.startswith('2026-11-22T07:49:20.')
clar = R / 'records/S6_SERIES_PUBLISH_checkpoint_27_delivery_timestamp_clarification.json'
assert not clar.exists()
clar.write_text(json.dumps(dict(recorded_utc=now, receipt_path=str(receipt.relative_to(R)), receipt_sha256=hashlib.sha256(rb).hexdigest(), original_created_utc=rr['created_utc'], observed_receipt_file_write_time_utc=mtime, clarification='The original created_utc was manually entered about seven seconds after the observed file write time. Use the observed write time for receipt-creation chronology. The original delivery receipt, ZIP, successful upload identity, payload verification and schedule are unchanged. No new upload is claimed.'), indent=2) + '\n')
pending = {'night:P4.55','night:P4.56','night:P4.57','night:P4.37','night:P4R.13','night:P4R.18','night:P4R.19','night:P4R.20','cdp:st:C.2.RAT.2','cdp:st:C.2.RAT.4','cdp:st:C.2.RAT.5','cdp:st:C.2.RAT.7','cdp:st:C.2.RAT.8','cdp:st:C.2.RAT.9'}
print(json.dumps(dict(record=str(out.relative_to(R)), sha256=hashlib.sha256(out.read_bytes()).hexdigest(), pending_nearest_headers=[dict(line=x['line'], owner=x['nearest_preceding_owner']) for x in rows if x['nearest_preceding_owner'] in pending], timestamp_clarification=str(clar.relative_to(R))), indent=2))
