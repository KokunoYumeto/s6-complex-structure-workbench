"""Extract only LU's named additive-cap dependency statement for fresh work."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import re

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert sha256(source).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
lines = source.decode().splitlines()
hits = [i for i, line in enumerate(lines) if r'\hypertarget{tag-02LT}' in line]
assert len(hits) == 1
first = hits[0]
match = re.match(r'\\begin\{(theorem|proposition|lemma|corollary)\}', lines[first])
assert match, 'Expected exact statement start'
ending = r'\end{' + match[1] + '}'
last = next(i for i in range(first, len(lines)) if lines[i].strip() == ending)
body = '\n'.join(lines[first:last+1]) + '\n'
assert r'\begin{proof}' not in body
folder = ROOT / 'agents/continuation7_iii_lu_support_statement'
folder.mkdir(exist_ok=True)
target = folder / 'S6_SERIES_PUBLISH_III_02LT_statement_only.tex'
assert not target.exists()
header = '% Clean named dependency statement for LU fresh derivation.\n% LT and LU original proofs and historical targets remain closed.\n'
target.write_text(header + body, newline='\n')
print('EXTRACTED', datetime.now(timezone.utc).isoformat())
print('CANONICAL_LINES', first+1, last+1, 'LINES', last-first+1)
print('STATEMENT_SHA256', sha256(body.encode()).hexdigest())
print('INTAKE_SHA256', sha256(target.read_bytes()).hexdigest())
print('PATH', target.relative_to(ROOT))
print(header + body, end='')
