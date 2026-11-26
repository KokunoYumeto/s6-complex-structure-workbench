"""Release an individually reviewed proof after its saved fresh derivation."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse
import csv
import io
import json

ROOT=Path(__file__).resolve().parents[1]
SOURCE_SHA='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
p=argparse.ArgumentParser()
p.add_argument('--tag',required=True)
p.add_argument('--folder',required=True)
p.add_argument('--derivation',required=True)
p.add_argument('--completed',required=True)
p.add_argument('--review-note',required=True)
a=p.parse_args()
fresh=ROOT/a.derivation
assert fresh.is_file() and len(fresh.read_text().split())>100
now=datetime.now(timezone.utc)
completed=datetime.fromisoformat(a.completed.replace('Z','+00:00'))
assert completed<now
index=json.loads((ROOT/'agents/continuation4_iii_infra/S6_SERIES_PUBLISH_III_packet_structure.json').read_text())
resolved=ROOT/'agents/continuation6_iii_infra/S6_SERIES_PUBLISH_III_carrier_resolved_scopes.json'
overrides=json.loads(resolved.read_text()) if resolved.exists() else {}
group=overrides.get(a.tag)
if group is None:
    group=next(g for g in index['metadata_groups'] if a.tag in g['candidate_tags'])
assert group['candidate_tags']==[a.tag]
spans=group['proof_spans']
if a.tag=='03BC':
    # The later separate proof is the section's retained-angle conclusion.
    # This release is exactly the proposition's own immediately following proof.
    spans=[spans[0]]
assert len(spans)==1
first,last=spans[0]['start_line'],spans[0]['end_line']
source=ROOT/'S6_SERIES_PUBLISH_III.tex'
raw=source.read_bytes()
assert sha256(raw).hexdigest()==SOURCE_SHA
lines=raw.decode().splitlines()
proof='\n'.join(lines[first-1:last])
paragraph=group.get('proof_kind')=='argument_paragraph'
if paragraph:
    assert proof.startswith('\\paragraph{')
else:
    assert proof.startswith('\\begin{proof}') and proof.endswith('\\end{proof}')
proof_sha=sha256(proof.encode()).hexdigest()
assert spans[0]['sha256'] in (proof_sha,sha256((proof+'\n').encode()).hexdigest())
statement=None
if group['statement_lines'] is not None:
    sf,sl=group['statement_lines']
    statement='\n'.join(lines[sf-1:sl])
folder=ROOT/a.folder
folder.mkdir(parents=True,exist_ok=True)
out=folder/f'S6_SERIES_PUBLISH_III_{a.tag}_released_proof.tex'
assert not out.exists()
header=(f'% Individual release after complete fresh review: {now.isoformat()}\n'
        f'% Source SHA256 {SOURCE_SHA}; source proof lines {first}--{last}.\n'
        f'% Proof SHA256 (without terminal LF): {proof_sha}.\n'
        f'% Fresh derivation: {a.derivation}; completed {a.completed}.\n')
out.write_text(header+proof+'\n',newline='\n')
if statement is not None:
    (folder/f'S6_SERIES_PUBLISH_III_{a.tag}_released_statement.tex').write_text(header+statement+'\n',newline='\n')
progress=ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv'
with progress.open(newline='') as f:
    r=csv.DictReader(f,delimiter='\t'); fields=r.fieldnames; rows=list(r)
row=next(r for r in rows if r['tag']==a.tag)
assert row['status']=='open' and row['proof_status']=='embargoed'
row.update(assigned_checker=a.folder,packet_status='fresh_written_original_comparison_pending',
           proof_status='released_after_derivation',unresolved_inputs='',
           derivation_path=a.derivation,derivation_sha256=sha256(fresh.read_bytes()).hexdigest(),
           derivation_completed_utc=a.completed,root_release_authorization=a.review_note,
           proof_released_utc=now.isoformat(),released_source_sha256=SOURCE_SHA,
           released_proof_sha256=proof_sha,source_ownership_status='verified_exact_individual_scope')
row['notes']+=' Individually released in continuation six after root full fresh review; comparison remains open. '+a.review_note
stream=io.StringIO(newline='')
w=csv.DictWriter(stream,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
progress.write_text(stream.getvalue(),newline='\n')
message=f'Released {a.tag} proof lines {first}--{last} at {now.isoformat()}; no required row closed.\n'
(ROOT/'code'/f'S6_SERIES_PUBLISH_c6_release_{a.tag}.out').write_text(message,newline='\n')
print(message,end='')
