"""Admit a complete, root-read comparison; leave manuscript application separate."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse
import csv
import io
import re

ROOT=Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
p=argparse.ArgumentParser()
p.add_argument('--tag',required=True)
p.add_argument('--folder',required=True)
p.add_argument('--comparison-sha',required=True)
p.add_argument('--receiver-sha',required=True)
a=p.parse_args()

def read(path):
    with path.open(newline='') as f:
        r=csv.DictReader(f,delimiter='\t');return r.fieldnames,list(r)

progress=ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv'
fields,rows=read(progress)
row=next(r for r in rows if r['tag']==a.tag)
assert row['status']=='open' and row['proof_status']=='released_after_derivation'
assert row['root_release_authorization']
assert datetime.fromisoformat(row['derivation_completed_utc'].replace('Z','+00:00'))<datetime.fromisoformat(row['proof_released_utc'].replace('Z','+00:00'))
assert sha256((ROOT/row['derivation_path']).read_bytes()).hexdigest()==row['derivation_sha256']
source=ROOT/'S6_SERIES_PUBLISH_III.tex'
raw=source.read_bytes();text=raw.decode()
assert sha256(raw).hexdigest()==row['released_source_sha256']
folder=ROOT/a.folder
comparison=folder/f'S6_SERIES_PUBLISH_III_{a.tag}_comparison.md'
receiver=folder/f'S6_SERIES_PUBLISH_III_{a.tag}_receiving.tex'
assert sha256(comparison.read_bytes()).hexdigest()==a.comparison_sha
assert sha256(receiver.read_bytes()).hexdigest()==a.receiver_sha
_,guards=read(folder/f'S6_SERIES_PUBLISH_III_{a.tag}_replacements.tsv')
assert guards
for g in guards:
    assert g['statement_id']==row['label']
    old,new=g['old_text'],g['new_text']
    assert old and text.count(old)==1
    for pattern in (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}'):
        assert sorted(re.findall(pattern,old))==sorted(re.findall(pattern,new))
assert receiver.read_text().rstrip('\n')=='\n\n'.join(g['new_text'].rstrip('\n') for g in guards)
eventfile=ROOT/'CHECK_EVENTS.tsv'
event_fields,events=read(eventfile)
proposal=folder/f'S6_SERIES_PUBLISH_III_{a.tag}_CHECK_EVENTS.tsv'
proposal_fields,proposals=read(proposal)
assert event_fields==proposal_fields and proposals
known={e['event_id'] for e in events}
now=datetime.now(timezone.utc)
for event in proposals:
    assert event['statement_id']==row['label'] and event['event_id'] not in known
    assert event['type'] in ('targeted proof check','computation or formal certificate','used and rechecked in this run') or event['type'].startswith('refuted')
    assert datetime.fromisoformat(event['date_utc'].replace('Z','+00:00'))<=now
    event['outcome']+=' Root read the complete fresh derivation, original scope, comparison, receiver and relevant arithmetic; exact receiver SHA256 '+a.receiver_sha+'. Manuscript application and final-page review remain open.'
    events.append(event);known.add(event['event_id'])
row.update(status='done',packet_status='required_check_complete',
           check_event_id=';'.join(e['event_id'] for e in proposals),
           proof_comparison_evidence=str(comparison.relative_to(ROOT)),
           completion_evidence=row['derivation_path']+'; '+str(comparison.relative_to(ROOT))+'; '+str(receiver.relative_to(ROOT)),
           source_ownership_status='verified_exact_individual_scope')
row['notes']+=' Sixth-continuation root admitted this exact comparison after full reading. Canonical source application, unit restructuring and page review retain separate open rows.'
for path,cols,data in ((eventfile,event_fields,events),(progress,fields,rows)):
    stream=io.StringIO(newline='');w=csv.DictWriter(stream,cols,delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(data);path.write_text(stream.getvalue(),newline='\n')
df,defects=read(folder/f'S6_SERIES_PUBLISH_III_{a.tag}_defects.tsv')
for defect in defects:
    defect['review_status']='root comparison admitted; source application and final page review pending'
stream=io.StringIO(newline='');w=csv.DictWriter(stream,df,delimiter='\t',lineterminator='\n')
w.writeheader();w.writerows(defects)
(folder/f'S6_SERIES_PUBLISH_III_{a.tag}_defects.tsv').write_text(stream.getvalue(),newline='\n')
assert source.read_bytes()==raw
message=f'Admitted {a.tag} at {now.isoformat()}; III required checks {sum(r["status"]=="done" for r in rows)}/{len(rows)}.\n'
(ROOT/'code'/f'S6_SERIES_PUBLISH_c6_admit_{a.tag}.out').write_text(message,newline='\n')
print(message,end='')
