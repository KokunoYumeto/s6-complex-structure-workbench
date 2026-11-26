"""Extract only the exact clean LV theorem; expose no original proof."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
raw = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert sha256(raw).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
lines = raw.decode().splitlines()
first = 21458
assert lines[first-1].startswith(r'\begin{theorem}')
last = next(i+1 for i in range(first-1, len(lines)) if lines[i].strip() == r'\end{theorem}')
body = '\n'.join(lines[first-1:last])
assert r'\label{maps:src:D.2.53}' in body and r'\hypertarget{tag-02LV}' in body
assert r'\begin{proof}' not in body
clean = re.sub(r'^\\StatementRecord[^\n]*\n', '', body, flags=re.M) + '\n'
lane = ROOT / 'agents/continuation7_iii_lv_statement'
lane.mkdir(exist_ok=True)
destination = lane / 'S6_SERIES_PUBLISH_III_02LV_statement_only.tex'
assert not destination.exists()
destination.write_text(clean, newline='\n')
print('CLEAN_STATEMENT canonical lines', first, last, 'clean lines', len(clean.splitlines()))
print('FILE', destination.relative_to(ROOT), 'SHA256', sha256(destination.read_bytes()).hexdigest())
print('Original proof and historical target remain closed. UTC', datetime.now(timezone.utc).isoformat())
