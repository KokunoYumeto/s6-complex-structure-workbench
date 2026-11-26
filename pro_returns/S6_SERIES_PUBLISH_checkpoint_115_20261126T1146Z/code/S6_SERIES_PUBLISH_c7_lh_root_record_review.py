#!/usr/bin/env python3
"""Read serialized LH proposals and compare them to the fully read bodies."""
import csv
from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/'agents/continuation7_iii_odd_weighted'
PREFIX = 'S6_SERIES_PUBLISH_III_02LH_'
csv.field_size_limit(100000000)

def rows(suffix):
    path = LANE/(PREFIX+suffix+'.tsv')
    with path.open(newline='') as f:
        result = list(csv.DictReader(f,delimiter='\t'))
    assert b'\r' not in path.read_bytes()
    return result

replacements = rows('replacements')
assert len(replacements) == 2
old_bodies = [r['old_text'] for r in replacements]
new_bodies = [r['new_text'] for r in replacements]
receiver = (LANE/(PREFIX+'receiving.tex')).read_text()
assert receiver.rstrip('\n') == '\n\n'.join(x.rstrip('\n') for x in new_bodies)
canonical = (ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert sha256(canonical).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
lines = canonical.decode().splitlines()
for r,(lo,hi) in zip(replacements,[(16765,16822),(16825,17043)]):
    assert '\n'.join(lines[lo-1:hi]) == r['old_text']
    print('REPLACEMENT',lo,hi,r['reason'])

defects = rows('defects')
assert len(defects) == 34
for r in defects:
    assert any(r['old_text'] in body for body in old_bodies)
    assert any(r['new_text'] in body for body in new_bodies)
    for loc,body,key,offset in (
        (r['old_location'],lines,'old_text',1),
        (r['new_location'],receiver.splitlines(),'new_text',1),
    ):
        lo,hi = map(int,re.search(r'lines (\d+)--(\d+)',loc).groups())
        assert r[key] in '\n'.join(body[lo-offset:hi-offset+1])
    print('DEFECT',r['change_id'],r['type'])
    for k in ('old_location','new_location','reason','old_page','new_page','review_status'):
        print(' ',k+':',r[k])
    print('  BODY_MEMBERSHIP exact old and new strings and their bounded locations verified')

events = rows('CHECK_EVENTS')
assert len(events) == 2 and len({r['evidence_group'] for r in events}) == 1
for r in events:
    print('EVENT')
    for k,v in r.items():
        print(' ',k+':',v)
assert sha256((ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest() == sha256(canonical).hexdigest()
print('PASS all serialized fields checked; old/new text membership in the wholly read bodies is exact')
print('SCOPE record check only; no new mathematical or independent-proof credit')
