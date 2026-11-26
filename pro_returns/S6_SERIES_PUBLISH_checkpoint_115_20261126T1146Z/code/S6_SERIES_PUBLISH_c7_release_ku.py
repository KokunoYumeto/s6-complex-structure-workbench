"""Release the whole argument-bearing KU environment after fresh review."""
import csv
import hashlib
import io
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SHA = '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
FRESH_SHA = '9760a76042b595bbda8033782598bff9ffe747d72126541046fa8520e1e0a9e7'
folder = ROOT/'agents/continuation7_iii_ku'
fresh = folder/'S6_SERIES_PUBLISH_III_02KU_fresh_derivation.md'
review = ROOT/'agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02KU_fresh_root_review.md'
sha = lambda b: hashlib.sha256(b).hexdigest()
assert sha(fresh.read_bytes()) == FRESH_SHA
assert len(review.read_text().split()) > 100
now = datetime.now(timezone.utc)
completed = datetime.fromtimestamp(fresh.stat().st_mtime, timezone.utc)
assert completed < now
progress = ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv'
with progress.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
row = next(r for r in rows if r['tag'] == '02KU')
assert row['status'] == 'open' and row['proof_status'] == 'embargoed'
raw = (ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert sha(raw) == SOURCE_SHA
text = raw.decode()
first_token = r'\begin{computed}[as a bounded exact computation]\hypertarget{tag-02KU}{}\label{maps:src:D.2.2}'
assert text.count(first_token) == 1
start = text.index(first_token)
end = text.index(r'\end{computed}',start)+len(r'\end{computed}')
original = text[start:end]
assert original.count(r'\begin{computed}') == original.count(r'\end{computed}') == 1
assert original.count(r'\label{maps:src:D.2.2}') == 1
assert r'\begin{proof}' not in original
first = text[:start].count('\n')+1
last = text[:end].count('\n')+1
original_sha = sha(original.encode())
header = (f'% Whole argument-bearing computed environment released: {now.isoformat()}\n'
          f'% Source SHA256 {SOURCE_SHA}; source lines {first}--{last}.\n'
          f'% Complete environment SHA256 without terminal LF: {original_sha}.\n'
          f'% Fresh completed (final file write, before checker freeze message): {completed.isoformat()}.\n'
          f'% Fresh SHA256 {FRESH_SHA}; review {review.relative_to(ROOT)}.\n')
released = folder/'S6_SERIES_PUBLISH_III_02KU_released_original.tex'
assert not released.exists()
released.write_text(header+original+'\n',newline='\n')
row.update(assigned_checker=str(folder.relative_to(ROOT)),
           packet_status='fresh_written_original_comparison_pending',
           proof_status='released_after_derivation',unresolved_inputs='',
           derivation_path=str(fresh.relative_to(ROOT)),derivation_sha256=FRESH_SHA,
           derivation_completed_utc=completed.isoformat(),
           root_release_authorization=str(review.relative_to(ROOT)),
           proof_released_utc=now.isoformat(),released_source_sha256=SOURCE_SHA,
           released_proof_sha256=original_sha,
           source_ownership_status='verified_exact_individual_argument_bearing_scope')
row['notes'] += (' Whole argument-bearing computed environment released in continuation seven after complete root fresh/program/output review; no separate proof environment exists. Original comparison and admission remain open. '+str(review.relative_to(ROOT)))
buffer = io.StringIO(newline='')
writer = csv.DictWriter(buffer, fields, delimiter='\t',lineterminator='\n')
writer.writeheader();writer.writerows(rows)
progress.write_text(buffer.getvalue(),newline='\n')
message = f'Released complete 02KU environment lines {first}--{last} at {now.isoformat()}; fresh final write {completed.isoformat()}; no row closed.\n'
(ROOT/'code/S6_SERIES_PUBLISH_c7_release_02KU.out').write_text(message,newline='\n')
assert (ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes() == raw
print(message,end='')
