#!/usr/bin/env python3
"""Record the checked core counterexample without closing either target."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib

ROOT=Path(__file__).resolve().parents[1]
OWN=ROOT/'agents/continuation6_iii_root'
PREFIX='S6_SERIES_PUBLISH_III_graph_line_core'
NOTE=OWN/(PREFIX+'_root_comparison.md')
now=datetime.now(timezone.utc).isoformat()
source=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert hashlib.sha256(source).hexdigest()=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'

def read(path):
    with path.open(newline='') as f:
        reader=csv.DictReader(f,delimiter='\t')
        return reader.fieldnames,list(reader)

def write(path,fields,rows):
    with path.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
        writer.writeheader();writer.writerows(rows)

fields,all_events=read(ROOT/'CHECK_EVENTS.tsv')
ids={r['event_id'] for r in all_events}
events=[];defects=[]
targets=[('02S8','night:P3F.31',
    r'At \(q=0\) the compression is the fixed sphere, and the constructed page is disjoint from it. Compactness therefore gives \(q_a>0\) such that their intersection has no point over \([0,q_a]\).'),
    ('02S9','night:P3F.32',
    r'The page misses the fixed sphere through its actual line subfan; therefore all remaining intersections are over a compact regular base interval.')]
for tag,label,old in targets:
    assert source.count(old.encode())==1
    loc=source.count(b'\n',0,source.index(old.encode()))+1
    eid='publish:c6:III:'+tag+':core-countercheck'
    assert eid not in ids
    event=dict.fromkeys(fields,'')
    event.update(statement_id=label,date=now[:10],
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; unexposed d2 checker and root full comparison',
        type='targeted proof check',event_id=eid,
        phase='independent narrow derivation followed by root original comparison',
        outcome='The unexposed333-line core-intersection addendum and new114-line real-Jacobian program/output were fixed at2026-11-24T15:34:37.723289+00:00 and fully read by root. Full-unit node maps put the two source nodes in complementary free core arcs. The complete positive-radius component sweeps have intersections(+1,-1); outer physical-dual degrees are(+1,-1), so graph-normal meridian degrees are(0,0). This refutes the intermediate whole-page equality j_+^*x=-c1(L_d) and its b|V consequence on actual closed I2 components, for all k>0 and integral d. Root read the entire original, staged receiver and comparison. The original compact regular-band separation omits the interior q=0 handle core. The earlier disjoint-core and exposed band repairs are withdrawn at that exact scope. This event checks and refutes an intermediate proof claim; it neither refutes nor establishes the final return integer, sphere class or product mapping torus. Complete corrected graph/cap/square calculation remains open. No full-target closure, source/unit/build/page credit or IV proof credit.',
        source_file='S6_SERIES_PUBLISH_III.tex',source_row=str(loc),
        source_event_type='targeted proof check',evidence_group=eid,
        publish_input_file=(OWN/(PREFIX+'_CHECK_EVENTS.tsv')).relative_to(ROOT).as_posix(),
        publish_input_row=str(len(events)+2),date_utc=now,
        where='; '.join([NOTE.relative_to(ROOT).as_posix(),
            'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_graph_line_core_addendum.md',
            'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_graph_line_core_intersection.py',
            'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_graph_line_core_intersection.out',
            'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_graph_line_withdrawal.md']))
    events.append(event)
    defects.append(dict(change_id='c6-III-'+tag+'-interior-core',type='D25',
        statement_id=label,old_location=f'S6_SERIES_PUBLISH_III.tex:{loc}',old_page='',
        new_location=NOTE.relative_to(ROOT).as_posix(),new_page='',old_text=old,
        new_text='The graph-normal meridian degrees on(C0,C1) are(0,0), whereas the physical-dual degrees are(+1,-1). The interior compression core supplies the signed difference. A complete receiving replacement remains pending.',
        reason='The displayed handle contains an interior q=0 core meeting every complete source shell. The original inference from disjointness from F to a compact regular intersection interval is false, and the full oriented sweep detects the resulting absolute line-class discrepancy.',
        review_status='confirmed D25 by fresh narrow derivation and full root comparison; repair pending; target remains open'))
progress_fields,progress=read(ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv')
for row in progress:
    if row['tag'] in {'02S8','02S9'}:
        assert row['status']=='open'
        row['notes']+=' Confirmed D25: interior q=0 compression core; graph component degrees(0,0) refute physical-dual identification. Narrow event publish:c6:III:'+row['tag']+':core-countercheck; full corrected graph/cap/square and final return remain open.'
        row['proof_comparison_evidence']+='; '+NOTE.relative_to(ROOT).as_posix()
write(OWN/(PREFIX+'_CHECK_EVENTS.tsv'),fields,events)
write(OWN/(PREFIX+'_defects.tsv'),list(defects[0]),defects)
write(ROOT/'CHECK_EVENTS.tsv',fields,all_events+events)
write(ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv',progress_fields,progress)
assert (ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()==source
print('Recorded two narrow core-countercheck events and two confirmed D25 defects at',now)
print('Both S8/S9 remain open; III done count:',sum(r['status']=='done' for r in progress))
