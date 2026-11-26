"""Admit only the wholly read LU comparison; never edit the manuscript."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import csv
import io
import re

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_corrected_initial_receiving'
P='S6_SERIES_PUBLISH_III_02LU_'
SID='maps:src:D.2.52'
REVIEW='agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02LU_root_admission_review.md'
csv.field_size_limit(100000000)

def read(path):
    with path.open(newline='') as f:
        reader=csv.DictReader(f,delimiter='\t')
        return reader.fieldnames,list(reader)

def write(path,fields,rows):
    buf=io.StringIO(newline='')
    w=csv.DictWriter(buf,fields,delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
    path.write_text(buf.getvalue(),newline='\n')

hashes={
 'receiving.tex':'b004d43a7ff659502f5d0a5d9434fe1b485be4c82fb0a070b79fed582dd0e90d',
 'comparison.md':'133f8a7c325bebaa70632638186bd92f90894d7ff28f03c7bbe00790fa6a2fdb',
 'source_checks.md':'8d4f6354190ed891da32e3715098fea148ede6fc0d781e1ee22a4f229487b9de',
 'replacements.tsv':'6fa249453256b9b4f6a69728e11b9e6393a1966b17339ea7985618c45f842d7c',
 'guards.tsv':'3f6188c87cb1a0f98c459fbe4e42dfd479296349bef254564a7652aafa49cb04',
 'defects.tsv':'6408e1e9e856e536987ee3792513c2cd5e1de086a36af7ecb64eb8e3093f9e6f',
 'CHECK_EVENTS.tsv':'38e78197590e2a044e7b20cc0adde1db87f6fccb76061277beaad116c3e7191b',
}
for name,digest in hashes.items():
    assert sha256((LANE/(P+name)).read_bytes()).hexdigest()==digest,name
assert (ROOT/REVIEW).is_file()
source=ROOT/'S6_SERIES_PUBLISH_III.tex';raw=source.read_bytes();text=raw.decode()
assert sha256(raw).hexdigest()=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
progress=ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv'
fields,rows=read(progress)
assert len(rows)==128 and sum(r['status']=='done' for r in rows)==125
row=next(r for r in rows if r['tag']=='02LU')
assert row['label']==SID and row['status']=='open'
assert row['proof_status']=='released_after_derivation' and row['root_release_authorization']
assert datetime.fromisoformat(row['derivation_completed_utc'].replace('Z','+00:00')) < datetime.fromisoformat(row['proof_released_utc'].replace('Z','+00:00'))
assert sha256((ROOT/row['derivation_path']).read_bytes()).hexdigest()==row['derivation_sha256']
_,replacements=read(LANE/(P+'replacements.tsv'))
_,guards=read(LANE/(P+'guards.tsv'))
assert len(replacements)==len(guards)==3
assert [(g['start_line'],g['end_line']) for g in guards]==[('21293','21348'),('21351','21442'),('21443','21457')]
for r,g in zip(replacements,guards):
    assert r['statement_id']==g['statement_id']==SID
    assert r['old_text'] and text.count(r['old_text'])==1
    assert sha256(r['old_text'].encode()).hexdigest()==g['old_sha256']
    assert sha256(r['new_text'].encode()).hexdigest()==g['new_sha256']
    for name in ('label','hypertarget','tag'):
        pattern=r'\\'+name+r'\{([^{}]+)\}'
        assert sorted(re.findall(pattern,r['old_text']))==sorted(re.findall(pattern,r['new_text']))
assert [bool(r['new_text']) for r in replacements]==[True,True,False]
receiver=(LANE/(P+'receiving.tex')).read_text()
assert receiver.rstrip('\n')=='\n\n'.join(r['new_text'].rstrip('\n') for r in replacements if r['new_text'])
assert re.findall(r'\\label\{([^{}]+)\}',receiver)==[SID,'maps:eq:D.CI1']
assert re.findall(r'\\hypertarget\{([^{}]+)\}',receiver)==['tag-02LU','tag-01YN']
assert re.findall(r'\\tag\{([^{}]+)\}',receiver)==['D.CI1']
defectfile=LANE/(P+'defects.tsv');dfields,defects=read(defectfile)
assert len(defects)==16 and all(d['statement_id']==SID for d in defects)
assert all(d['type'] not in ('D19','D25') for d in defects)
eventfile=ROOT/'CHECK_EVENTS.tsv';efields,events=read(eventfile)
pfields,proposals=read(LANE/(P+'CHECK_EVENTS.tsv'))
assert efields==pfields and len(proposals)==6
assert sorted(e['type'] for e in proposals)==sorted(['targeted proof check','computation or formal certificate','used and rechecked in this run','computation or formal certificate','computation or formal certificate','used and rechecked in this run'])
known={e['event_id'] for e in events};now=datetime.now(timezone.utc)
for e in proposals:
    assert e['statement_id']==SID and e['event_id'] not in known
    assert datetime.fromisoformat(e['date_utc'].replace('Z','+00:00'))<=now
    e['outcome']+=' Root admitted the completed comparison after the exact full reading recorded in '+REVIEW+'. Receiver SHA256 '+hashes['receiving.tex']+'. Canonical application and final unit/build/page gates remain open.'
    events.append(e);known.add(e['event_id'])
row.update(status='done',packet_status='required_check_complete',
           check_event_id=';'.join(e['event_id'] for e in proposals),
           proof_comparison_evidence=str((LANE/(P+'comparison.md')).relative_to(ROOT)),
           completion_evidence='; '.join((row['derivation_path'],str((LANE/(P+'comparison.md')).relative_to(ROOT)),str((LANE/(P+'receiving.tex')).relative_to(ROOT)),REVIEW)),
           source_ownership_status='verified_exact_individual_scope')
row['notes']+=' Seventh-continuation root admitted the exact LU comparison. Canonical application, unit restructuring and final page review remain separate open gates.'
for d in defects:
    d['review_status']='root comparison admitted; source application and final page review pending'
write(eventfile,efields,events)
write(progress,fields,rows)
write(defectfile,dfields,defects)
assert source.read_bytes()==raw
print('Admitted 02LU at',now.isoformat(),'; III required checks',str(sum(r['status']=='done' for r in rows))+'/'+str(len(rows))+'.')
print('Three exact guards;16 defects;6 narrowly typed events; canonical manuscript unchanged.')
