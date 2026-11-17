"""Retain six independently checked writing repairs as new inventory units.

These are writing-stage proofs, not retroactively attributed to a course.
The retained original proofs and historical open states are not removed.
"""
from pathlib import Path
import csv,json,re,hashlib
D=Path(__file__).resolve().parents[2]
p=D/'S6_09_PAPERS_inventory.csv'
with p.open(newline='') as f:
    rd=csv.DictReader(f);fields=rd.fieldnames;rows=list(rd)
index={(r['source_run'],r['source_id']):r for r in rows}
reviews=json.loads((D/'work/maps_audit/independent_repair_reviews.json').read_text())
for event in reviews:
    local=D.parent/event['source']
    assert hashlib.sha256(local.read_bytes()).hexdigest()==event['source_sha256']
recommend=json.loads((D/'work/maps_audit/reviewed_repair_label_recommendations.json').read_text())['rows']
added=[]
for x in recommend:
    key=('WRITING_REPAIR',x['source_id'])
    if key in index:continue
    file=D/'work/maps_audit'/x['proof_file'];s=file.read_text()
    event=next(e for e in reviews if e['source'].endswith(x['proof_file']))
    pos=s.index('\\label{'+x['printed_label']+'}')
    begins=list(re.finditer(r'\\begin\{(lemma|proposition)\}(?:\[([^\]]*)\])?',s[:pos]))
    m=begins[-1];end=s.index('\\end{'+m[1]+'}',pos)+len('\\end{'+m[1]+'}')
    row={k:'' for k in fields}
    row.update(source_run='WRITING_REPAIR',source_id=x['source_id'],source_file=str(file.relative_to(D)),
        paper='III',kind='Classical prerequisite re-derivation' if 'PT-' in x['source_id'] else 'Lemma' if m[1]=='lemma' else 'Question settled',
        statement_as_printed='COMPLETE CHECKED STATEMENT PENDING PLACEMENT: '+s[m.start():end],
        wording_vs_source='New writing-stage proof. '+event['required_correction'],
        recorded_checks='Independent current check, not an inherited historical check; see '+event['event_id']+'.',
        your_check='GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026, separate agent /root: '+event['precise_scope'],
        check_outcome=event['outcome']+' Final source-to-print comparison pending Paper III assembly.',
        found_in_AC26='Scoped comparison pending; no novelty claim.',
        found_in_E26='Scoped comparison pending; no novelty claim.',
        found_in_DGKX_v1='Scoped comparison pending; no novelty claim.',
        found_elsewhere='Classical Pontryagin–Thom prerequisite; no novelty claimed.' if 'PT-' in x['source_id'] else 'Constructed from the proved local fundamental-group inclusion; full literature comparison pending.',
        credited_to='Classical Pontryagin–Thom constructions; exact sources and hypotheses at their points of use.' if 'PT-' in x['source_id'] else 'Underlying complex construction and local toric model credited to AC26; this extension homotopy is an additional writing-stage proof.',
        notes=x['relationship']+' Reserved label '+x['printed_label']+'. Producer GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026; independent reader same model/effort/date in separate agent. Complete source SHA256 '+event['source_sha256']+'.')
    rows.append(row);index[key]=row;added.append(x['source_id'])
assert len(fields)==17 and len(index)==len(rows)
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
(D/'records/writing_repair_inventory_additions.json').write_text(json.dumps({'added':added,'total':len(rows),'hash_verified_reviews':reviews},indent=2)+'\n')
print('Writing repairs added:',len(added),'inventory:',len(rows))
