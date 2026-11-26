from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
dest = root / 'records/S6_SERIES_PUBLISH_II_C4_C5_nonproof_setup_01.tex'
receipt = dest.with_suffix('.json')
if dest.exists() or receipt.exists():
    raise SystemExit('Refusing to overwrite an existing packet or receipt')

def sha(data):
    return hashlib.sha256(data).hexdigest()

specs = [
    ('S6_SERIES_PUBLISH_I.tex', 6183, 6222, r'\begin{definition}[Base and integral marking]'),
    ('S6_SERIES_PUBLISH_I.tex', 6224, 6246, r'\begin{definition}[The parameter and the finite translations]'),
    ('S6_SERIES_PUBLISH_II.tex', 26079, 26085, 'In this subsection $X=X_c$'),
]
parts = []
bindings = []
for name, first, last, initial in specs:
    raw = (root / name).read_bytes()
    lines = raw.decode().splitlines(keepends=True)
    text = ''.join(lines[first - 1:last])
    assert text.startswith(initial), (name, first)
    assert r'\begin{proof}' not in text and r'\end{proof}' not in text
    parts.append(f'% EXACT NONPROOF INPUT: {name}, source lines {first}--{last}\n' + text)
    bindings.append({'source': name, 'source_sha256': sha(raw),
                     'first_line': first, 'last_line': last,
                     'excerpt_sha256': sha(text.encode()), 'excerpt_bytes': len(text.encode())})
payload = '\n'.join(parts).encode()
dest.write_bytes(payload)
record = {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'packet': str(dest.relative_to(root)), 'sha256': sha(payload),
    'bindings': bindings,
    'scope': 'Current Paper I definitions and current Paper II nonproof subsection setup only. No seven-target proof, C.8, C.9, or C.13 supplied.',
    'reading': 'The root actually read every excerpt in full before extracting this packet; extraction itself adds no reading credit.',
}
receipt.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'packet': record['packet'], 'sha256': record['sha256'],
                  'receipt': str(receipt.relative_to(root)), 'receipt_sha256': sha(receipt.read_bytes())}))
