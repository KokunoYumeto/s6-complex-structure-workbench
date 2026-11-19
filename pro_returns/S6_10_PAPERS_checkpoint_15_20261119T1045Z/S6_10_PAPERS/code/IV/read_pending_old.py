"""Extract exact pending IV source extents for manual proof review.

Extraction confers no proof-check credit. The nine blocks assigned separately
to the inventory reviewer are excluded from the root's reading batches.
"""
from pathlib import Path
import argparse, hashlib, json
P=Path(__file__).resolve().parents[2]
R=P.parents[1]
reserved={'maps:src:B.6.2'}|{f'maps:src:B.6.{n}' for n in range(5,13)}
rows=json.loads((P/'analysis/IV/pending_old_source_blocks.json').read_text())
rows=[r for r in rows if r['label'] not in reserved]
ap=argparse.ArgumentParser();ap.add_argument('start',type=int);ap.add_argument('count',type=int);a=ap.parse_args()
for n,r in enumerate(rows[a.start:a.start+a.count],a.start):
    src=R/r['file'];data=src.read_bytes()
    assert hashlib.sha256(data).hexdigest()==r['source_file_sha256']
    text=data.decode();block=text[int(r['start']):int(r['end'])]
    print(f"\n===== {n}: {r['label']} =====\n{block}\n")
