#!/usr/bin/env python3
"""Bind proof-free completed-I inputs and reconcile required-row metadata."""
from pathlib import Path
import csv
import datetime as dt
import hashlib
import json
import re

R = Path(__file__).resolve().parents[1]
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, value):
    assert not p.exists(), p
    p.write_text(json.dumps(value, indent=2) + '\n')

ip = R / 'S6_SERIES_PUBLISH_I.tex'
s = ip.read_text()
assert sha(ip) == '179fcc4e85fb7902aaf978bcd809cf9928ebc0a46cda5628d5096e6fa0011d74'
labels = ['I:def:finite-coordinates', 'inv:A2.3', 'inv:A2.1', 'inv:A2.2', 'inv:C3.2']
blocks = []
items = []
for label in labels:
    needle = '\\label{' + label + '}'
    assert s.count(needle) == 1
    at = s.index(needle)
    starts = list(re.finditer(r'\\begin\{(definition|proposition)\}', s[:at]))
    start = starts[-1].start()
    env = starts[-1].group(1)
    end = s.index('\\end{' + env + '}', at) + len('\\end{' + env + '}')
    block = s[start:end]
    assert '\\begin{proof}' not in block
    blocks.append('% Completed I statement: ' + label + '\n' + block)
    items.append({'label': label, 'start_character': start, 'end_character': end,
                  'first_line': s.count('\n', 0, start) + 1,
                  'last_line': s.count('\n', 0, end) + 1,
                  'sha256': hashlib.sha256(block.encode()).hexdigest()})
op = R / 'records/S6_SERIES_PUBLISH_II_FT_completed_I_statement_inputs_01.tex'
assert not op.exists()
op.write_text('% Completed-I input statements only; no FT/C.13 proof.\n\n' + '\n\n'.join(blocks) + '\n')
save(op.with_suffix('.json'), {'created_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
    'source': str(ip.relative_to(R)), 'source_sha256': sha(ip),
    'packet': str(op.relative_to(R)), 'packet_sha256': sha(op), 'statements': items,
    'scope': 'Exact nonproof statement extraction. Root read these complete statements before extraction. Extraction and hashes confer no page-reading or new mathematical-check credit.',
    'mathematical_events_added': 0})

cp = R / 'records/S6_SERIES_PUBLISH_required_check_candidates.csv'
mp = R / 'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json'
with cp.open() as f:
    rows = [r for r in csv.DictReader(f) if r['paper'] == 'II']
c = {r['label']: r for r in rows}
assert len(c) == len(rows)
m = {k:v for k,v in json.loads(mp.read_text())['rows'].items() if v.get('paper') == 'II'}
intersection = set(c) & set(m)
assert intersection == {'inv:wb:uniform-nontorsion-provenance'}
assert m[next(iter(intersection))]['completion_kind'] == 'retired nonmathematical production remark'
assert len(set(c) | set(m)) == 197
rp = R / 'records/S6_SERIES_PUBLISH_II_required_count_reconciliation_01.json'
save(rp, {'created_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
    'candidate_csv_sha256': sha(cp), 'completion_manifest_sha256': sha(mp),
    'candidate_rows': len(c), 'resolved_rows': len(m),
    'intersection_labels': sorted(intersection), 'distinct_union_rows': len(set(c) | set(m)),
    'uncompleted_candidate_rows': len(set(c)-set(m)),
    'explanation': 'The candidate generator still lists the documented retired production remark, which the completion manifest resolves without independent-proof credit. Removing this exact intersection reconciles the counts; no source or completion row is changed.',
    'mathematical_events_added': 0})
print(json.dumps({'packet': str(op.relative_to(R)), 'packet_sha256': sha(op),
    'packet_receipt_sha256': sha(op.with_suffix('.json')), 'reconciliation': str(rp.relative_to(R)),
    'reconciliation_sha256': sha(rp), 'resolved':len(m), 'uncompleted':len(set(c)-set(m))}, indent=2))
