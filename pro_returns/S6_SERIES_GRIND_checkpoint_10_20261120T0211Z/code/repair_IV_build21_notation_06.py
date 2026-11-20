"""Guarded transcription of the notation repair executed after build21 review.

This one-time edit has already been applied. Re-running against that edited
source deliberately fails its old-text guards. The receipt records the exact
before/after strings; there is no change to a mathematical assertion.
"""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'parts/IV.body.linked.tex'
source = path.read_text()
before = hashlib.sha256(source.encode()).hexdigest()
changes = [
    (r'rank-one (A\_7) cases', r'rank-one \(A_7\) cases'),
    ('belong to row45.', 'belong to row 45.'),
    (r'use (h(P)) from P3F.1', r'use \(h(P)\) from P3F.1'),
    (r'smaller than (4-h(P)).', r'smaller than \(4-h(P)\).'),
    (r'numerical pair ((-1,-4)):', r'numerical pair \((-1,-4)\):'),
    (r'projection to\(x,y\)', r'projection to \((x,y)\)'),
    (r'away from\(x,y\)=\(0,0\)', r'away from \((x,y)=(0,0)\)'),
    (r'over\(0,0\)', r'over \((0,0)\)'),
    (r'increasing by\(P3F.9.1\)', 'increasing by (P3F.9.1)'),
    (r'at the node is\((q,b)', r'at the node is \((q,b)'),
    (r'have coordinates \(0,1\) and\(1,8\)',
     r'have coordinates \((0,1)\) and \((1,8)\)'),
]
records = []
for old, new in changes:
    count = source.count(old)
    assert count > 0, old
    source = source.replace(old, new)
    records.append(dict(old=old, new=new, count=count,
                        transport='Identical coordinates and formula; mathematical delimiters and text spaces corrected.'))
path.write_text(source)
receipt = dict(
    utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    source='build21 actual image review',
    before_sha256=before,
    after_sha256=hashlib.sha256(source.encode()).hexdigest(),
    changes=records,
    mathematical_status_change=False,
)
(ROOT / 'analysis/IV_build21_visual_repairs_06.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({'guarded_changes': len(records), 'occurrences': sum(r['count'] for r in records)}))
