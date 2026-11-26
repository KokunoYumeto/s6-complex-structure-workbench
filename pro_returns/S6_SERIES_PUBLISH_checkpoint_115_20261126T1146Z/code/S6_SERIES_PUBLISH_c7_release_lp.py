"""Release both verified LP proof environments after the frozen full proof.

The general single-proof helper failed before mutation. This exact-target
variant retains every chronology, source-hash and ownership guard and
verifies each of LP's two proof hashes and their empty separator.
"""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import csv
import io
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SHA = '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
FOLDER = 'agents/continuation7_iii_weighted_cups_root'
FRESH = FOLDER + '/S6_SERIES_PUBLISH_III_02LP_fresh_derivation.md'
FRESH_SHA = '9554965e32768a0258adc3175bf9b2dc35522f20c60ca31fab0cd548ce91370d'
COMPLETED = '2026-11-25T04:06:19Z'
REVIEW = 'agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02LP_fresh_review.md'

assert sha256((ROOT / FRESH).read_bytes()).hexdigest() == FRESH_SHA
assert len((ROOT / REVIEW).read_text().split()) > 100
now = datetime.now(timezone.utc)
assert datetime.fromisoformat(COMPLETED.replace('Z', '+00:00')) < now
progress = ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv'
with progress.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
row = next(r for r in rows if r['tag'] == '02LP')
assert row['status'] == 'open' and row['proof_status'] == 'embargoed'
index = json.loads((ROOT / 'agents/continuation4_iii_infra/S6_SERIES_PUBLISH_III_packet_structure.json').read_text())
group = next(g for g in index['metadata_groups'] if g['candidate_tags'] == ['02LP'])
assert group['source_owners'] == ['maps:src:D.2.48']
assert group['source_ownership_verified'] is True
spans = group['proof_spans']
assert [(s['start_line'], s['end_line']) for s in spans] == [(19605, 19826), (19828, 20160)]
raw = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert sha256(raw).hexdigest() == SOURCE_SHA
lines = raw.decode().splitlines()
for span in spans:
    part = '\n'.join(lines[span['start_line']-1:span['end_line']])
    assert part.startswith('\\begin{proof}') and part.endswith('\\end{proof}')
    assert span['sha256'] in (sha256(part.encode()).hexdigest(),
                              sha256((part+'\n').encode()).hexdigest())
assert not lines[19826].strip()
assert lines[19827] == '\\begin{proof}[Proof of the complete invariant and classification]'
first, last = spans[0]['start_line'], spans[-1]['end_line']
proof = '\n'.join(lines[first-1:last])
assert '\\begin{theorem}' not in proof and '\\begin{proposition}' not in proof
proof_sha = sha256(proof.encode()).hexdigest()
sf, sl = group['statement_lines']
statement = '\n'.join(lines[sf-1:sl])
folder = ROOT / FOLDER
out = folder / 'S6_SERIES_PUBLISH_III_02LP_released_proof.tex'
assert not out.exists()
header = (f'% Individual original release: {now.isoformat()}\n'
          f'% Source SHA256 {SOURCE_SHA}; both proof spans {first}--{last}.\n'
          f'% Proof SHA256 without terminal LF: {proof_sha}.\n'
          f'% Frozen fresh: {FRESH}; completed {COMPLETED}.\n'
          f'% Fresh SHA256 {FRESH_SHA}; root review {REVIEW}.\n')
out.write_text(header+proof+'\n', newline='\n')
(folder / 'S6_SERIES_PUBLISH_III_02LP_released_statement.tex').write_text(header+statement+'\n', newline='\n')
row.update(assigned_checker=FOLDER, packet_status='fresh_written_original_comparison_pending',
           proof_status='released_after_derivation', unresolved_inputs='',
           derivation_path=FRESH, derivation_sha256=FRESH_SHA,
           derivation_completed_utc=COMPLETED, root_release_authorization=REVIEW,
           proof_released_utc=now.isoformat(), released_source_sha256=SOURCE_SHA,
           released_proof_sha256=proof_sha, source_ownership_status='verified_exact_individual_scope')
row['notes'] += (' LP has two same-owner proof environments, both individually hashed and released '
                 'after the complete root fresh proof; boundary/title inspection occurred after '
                 'the recorded fresh freeze and review. Full comparison and admission remain open. '+REVIEW)
buffer = io.StringIO(newline='')
writer = csv.DictWriter(buffer, fields, delimiter='\t', lineterminator='\n')
writer.writeheader()
writer.writerows(rows)
progress.write_text(buffer.getvalue(), newline='\n')
message = (f'Released 02LP both proof environments, lines {first}--{last}, '
           f'at {now.isoformat()}; source and both part hashes verified; no required row closed.\n')
(ROOT / 'code/S6_SERIES_PUBLISH_c7_release_02LP.out').write_text(message, newline='\n')
print(message, end='')
