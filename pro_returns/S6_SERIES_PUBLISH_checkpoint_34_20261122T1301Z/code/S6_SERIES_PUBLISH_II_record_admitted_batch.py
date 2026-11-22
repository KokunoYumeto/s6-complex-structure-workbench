"""Append an admitted batch's exact current state to both continuation journals."""
from pathlib import Path
from collections import Counter
import csv, datetime, hashlib, json, sys
R = Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)
sha = lambda b: hashlib.sha256(b).hexdigest()
c = json.loads((R/sys.argv[1]).read_text())
o = R/c['record_directory']
v = json.loads((o/'append_verification.json').read_text())
m = json.loads((R/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json').read_text())
rows = [x for x in m['rows'].values() if x['paper']=='II']
retired = sum(x.get('completion_kind')=='retired nonmathematical production remark' for x in rows)
source = sha((R/'S6_SERIES_PUBLISH_II.tex').read_bytes())
assert source == c['source_sha256']
assert sha((R/'CHECK_EVENTS.tsv').read_bytes()) == v['after_ledger_sha256']
with (R/'S6_SERIES_PUBLISH_defects_II.tsv').open(newline='') as f:
    edits = len(list(csv.DictReader(f,delimiter='\t')))
with (R/c['event_bundle']).open(newline='') as f:
    counts = Counter(x['type'] for x in csv.DictReader(f,delimiter='\t'))
assert sum(counts.values()) == c['events'] == v['added_rows']
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
number = c['batch_id'].removeprefix('CLEAN')
heading = f'## Paper II fresh checks batch {number} '
notes = (R/sys.argv[2]).read_text().strip() if len(sys.argv)>2 else ''
manifest_path = str((o/'manifest.json').relative_to(R))
body = f'''

{heading}— {now}

{c['scope']}

{notes}

Paper II has {len(rows)} of 197 required rows resolved: {len(rows)-retired} independent checks and {retired} documented production-only retirement. Exact admission evidence is `{manifest_path}`, SHA-256 `{sha((o/'manifest.json').read_bytes())}`. Current source SHA-256 is `{source}`, with {edits} logged edits.

CHECK_EVENTS.tsv has {v['after_rows']:,} rows, SHA-256 `{v['after_ledger_sha256']}`. New events: {', '.join(f'{n} {typ}' for typ,n in counts.items())}. The entire old ledger byte prefix, every old row, exact new tail and unique event identifiers were verified. This batch assigns no page-image reading credit. Paper I remains complete and untouched; the whole project remains incomplete.
'''
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    p = R/name
    old = p.read_bytes()
    assert heading.encode() not in old
    p.write_bytes(old+body.encode())
    assert p.read_bytes().startswith(old)
receipt = dict(created_utc=now,batch=c['batch_id'],required_rows_resolved=len(rows),
    independent_checks=len(rows)-retired,retired_rows=retired,source_sha256=source,
    defect_rows=edits,ledger_rows=v['after_rows'],body_sha256=sha(body.encode()),
    config=dict(path=sys.argv[1],sha256=sha((R/sys.argv[1]).read_bytes())))
p = o/'journal_record.json'
assert not p.exists()
p.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
