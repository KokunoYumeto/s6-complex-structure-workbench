"""Individual original release after a complete frozen fresh proof and review."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse
import csv
import io
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SHA = '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
p = argparse.ArgumentParser()
p.add_argument('--tag', required=True)
p.add_argument('--folder', required=True)
p.add_argument('--derivation', required=True)
p.add_argument('--derivation-sha', required=True)
p.add_argument('--completed', required=True)
p.add_argument('--root-review', required=True)
a = p.parse_args()
fresh = ROOT / a.derivation
assert fresh.is_file() and sha256(fresh.read_bytes()).hexdigest() == a.derivation_sha
assert len(fresh.read_text().split()) > 100
review = ROOT / a.root_review
assert review.is_file() and len(review.read_text().split()) > 100
now = datetime.now(timezone.utc)
completed = datetime.fromisoformat(a.completed.replace('Z', '+00:00'))
assert completed < now
progress = ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv'
with progress.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
row = next(r for r in rows if r['tag'] == a.tag)
assert row['status'] == 'open' and row['proof_status'] == 'embargoed'
index = json.loads((ROOT / 'agents/continuation4_iii_infra/S6_SERIES_PUBLISH_III_packet_structure.json').read_text())
overrides = json.loads((ROOT / 'agents/continuation6_iii_infra/S6_SERIES_PUBLISH_III_carrier_resolved_scopes.json').read_text())
group = overrides.get(a.tag)
if group is None:
    group = next(g for g in index['metadata_groups'] if a.tag in g['candidate_tags'])
assert group['candidate_tags'] == [a.tag]
assert len(group['proof_spans']) == 1
span = group['proof_spans'][0]
first, last = span['start_line'], span['end_line']
raw = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert sha256(raw).hexdigest() == SOURCE_SHA
lines = raw.decode().splitlines()
proof = '\n'.join(lines[first-1:last])
assert proof.startswith('\\begin{proof}') and proof.endswith('\\end{proof}')
proof_sha = sha256(proof.encode()).hexdigest()
assert span['sha256'] in (proof_sha, sha256((proof+'\n').encode()).hexdigest())
sf, sl = group['statement_lines']
statement = '\n'.join(lines[sf-1:sl])
folder = ROOT / a.folder
folder.mkdir(parents=True, exist_ok=True)
out = folder / f'S6_SERIES_PUBLISH_III_{a.tag}_released_proof.tex'
assert not out.exists()
header = (f'% Individual original release: {now.isoformat()}\n'
          f'% Source SHA256 {SOURCE_SHA}; proof lines {first}--{last}.\n'
          f'% Proof SHA256 without terminal LF: {proof_sha}.\n'
          f'% Frozen fresh: {a.derivation}; completed {a.completed}.\n'
          f'% Fresh SHA256 {a.derivation_sha}; root review {a.root_review}.\n')
out.write_text(header + proof + '\n', newline='\n')
(folder / f'S6_SERIES_PUBLISH_III_{a.tag}_released_statement.tex').write_text(header + statement + '\n', newline='\n')
row.update(assigned_checker=a.folder, packet_status='fresh_written_original_comparison_pending',
           proof_status='released_after_derivation', unresolved_inputs='',
           derivation_path=a.derivation, derivation_sha256=a.derivation_sha,
           derivation_completed_utc=a.completed, root_release_authorization=a.root_review,
           proof_released_utc=now.isoformat(), released_source_sha256=SOURCE_SHA,
           released_proof_sha256=proof_sha, source_ownership_status='verified_exact_individual_scope')
row['notes'] += ' Individually released in continuation seven after full root fresh review; complete original comparison and receiver admission remain open. ' + a.root_review
buffer = io.StringIO(newline='')
writer = csv.DictWriter(buffer, fields, delimiter='\t', lineterminator='\n')
writer.writeheader()
writer.writerows(rows)
progress.write_text(buffer.getvalue(), newline='\n')
message = f'Released {a.tag} proof lines {first}--{last} at {now.isoformat()}; no required row closed.\n'
(ROOT / 'code' / f'S6_SERIES_PUBLISH_c7_release_{a.tag}.out').write_text(message, newline='\n')
print(message, end='')
