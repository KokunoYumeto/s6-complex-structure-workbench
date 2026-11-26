"""Individual LV original release after the completed written fresh proof."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import csv

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SHA = '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
fresh_rel = 'agents/continuation7_iii_weighted_os45_fresh/S6_SERIES_PUBLISH_III_02LV_fresh_derivation.md'
fresh_sha = 'f5c325d1bd275d0cb8dac6a97b5d2ac5516cffbb4b8110e79a1f90c6dbe5a448'
review_rel = 'agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02LV_root_fresh_review.md'
assert sha256((ROOT / fresh_rel).read_bytes()).hexdigest() == fresh_sha
assert len((ROOT / review_rel).read_text().split()) > 500
now = datetime.now(timezone.utc)
assert now > datetime(2026, 11, 25, 11, 16, 4, 388868, tzinfo=timezone.utc)
required = ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv'
required_bytes = required.read_bytes()
with required.open(newline='') as stream:
    rows = list(csv.DictReader(stream, delimiter='\t'))
assert len(rows) == 128 and all(row['tag'] != '02LV' for row in rows)
units = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
unit_bytes = units.read_bytes()
raw = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert sha256(raw).hexdigest() == SOURCE_SHA
lines = raw.decode().splitlines()
sf, sl = 21458, 21513
statement = '\n'.join(lines[sf-1:sl])
assert '\\label{maps:src:D.2.53}' in statement
assert '\\begin{proof}' not in statement
first = next(i for i in range(sl, len(lines)) if lines[i].startswith('\\begin{proof}'))
assert first - sl < 6
last = next(i for i in range(first, len(lines)) if lines[i] == '\\end{proof}')
assert last - first < 4000
proof = '\n'.join(lines[first:last+1])
assert proof.count('\\begin{proof}') == proof.count('\\end{proof}') == 1
proof_sha = sha256(proof.encode()).hexdigest()
folder = ROOT / 'agents/continuation7_iii_weighted_os45_receiving'
folder.mkdir(exist_ok=True)
header = (f'% Individual unit-only original release: {now.isoformat()}\n'
          f'% Source SHA256 {SOURCE_SHA}; proof lines {first+1}--{last+1}.\n'
          f'% Proof SHA256 without terminal LF: {proof_sha}.\n'
          f'% Frozen fresh: {fresh_rel}; completed 2026-11-25T11:16:04.388868+00:00.\n'
          f'% Fresh SHA256 {fresh_sha}; root review {review_rel}.\n')
for kind, body in [('statement', statement), ('proof', proof)]:
    target = folder / f'S6_SERIES_PUBLISH_III_02LV_released_{kind}.tex'
    assert not target.exists()
    target.write_text(header + body + '\n', newline='\n')
assert required.read_bytes() == required_bytes and units.read_bytes() == unit_bytes
assert (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes() == raw
print(f'Released unit-only 02LV proof lines {first+1}--{last+1} at {now.isoformat()}; no required row or unit closed.')
print(f'Proof SHA256 without terminal LF: {proof_sha}.')
