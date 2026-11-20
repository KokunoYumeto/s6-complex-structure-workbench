"""Preserved functions for the two imports already executed inline on 20 Nov.

Do not rerun on the current canonical files. The exact before/after receipts
are analysis/P1A6_final_completion_08.json and
analysis/UN24_UN39_final_completion_08.json. Saving these functions records the
inline program; it adds no execution or mathematical check event.
"""
from pathlib import Path
import csv, datetime, hashlib, json

R=Path(__file__).resolve().parents[1]

def import_p1a6():
    p=R/'audit_corrections/row_assessments.json'; d=json.loads(p.read_text())
    label='night:P1A.6'; before=d[label].copy()
    assert not before.get('completion_state','').startswith('done')
    guards=json.loads((R/'audit_corrections/V_exact_source_locators_guard_08.json').read_text())
    s=(R/'parts/V.body.linked.tex').read_text(); assert s.count(guards[0]['new_text'])==1
    qa=R/'audit_root/build30_V_visual_QA.json'; q=json.loads(qa.read_text())
    assert q['result']=='PASS' and 142 in q['pages']
    d[label].update(
      remaining_risk='No row-specific mathematical, before-reading, source-credit, source-format or layout gate remains at the stated proper-submersion scope. The imported P1A.3/P1A.4 results retain their own separately recorded evidence.',
      format_check='PASS: exact Cartan1952 Expose19 Section5 pp19-14--19-15 citation, explicit Stein hull argument using z and 1/z, and coherent-structure-sheaf specialization are integrated. The three numbered steps and stated proper-submersion scope are intact.',
      layout_check='PASS: root actually viewed the complete current statement and all three proof steps on build30 page142, PDFSHA'+q['pdf_sha256']+'. Full page image SHA'+next(x['sha256'] for x in q['images'] if x['page']==142)+'. Source citations, Cayley map and torsor argument are legible; exact receipt audit_root/build30_V_visual_QA.json.',
      completion_state='done')
    p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
    rec={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'label':label,'before':before,'after':d[label],
         'qa_sha256':hashlib.sha256(qa.read_bytes()).hexdigest(),'integration_receipt':'analysis/primary_and_P119_integration_08.json',
         'scope':'This one row closes after its previously pending citation/actual-page gates. No other pending row or imported theorem is promoted.'}
    (R/'analysis/P1A6_final_completion_08.json').write_text(json.dumps(rec,indent=2)+'\n')

def import_un24_un39():
    p=R/'audit_sign/UN24_UN39_final_completion_proposals_08.json'; data=json.loads(p.read_text())
    ip=R/'S6_SERIES_GRIND_inventory.csv'
    with ip.open() as f:
        reader=csv.DictReader(f); cols=list(reader.fieldnames); rows=list(reader)
    ap=R/'audit_sign/row_assessments.json'; ass=json.loads(ap.read_text()); receipts=[]
    for record in data['records']:
        label=record['label']; selected=[x for x in rows if x['label']==label]; assert len(selected)==1
        for change in record['guarded_source_updates']:
            field=change['field']; assert selected[0].get(field,'')==change['old_value'],(label,field)
            if field not in cols: cols.append(field)
            selected[0][field]=change['new_value']
        receipts.append({'label':label,'assessment_before':ass[label],
                         'assessment_after':record['assessment_proposal'],
                         'source_updates':record['guarded_source_updates'],
                         'publication_gate_receipt':record['publication_gate_receipt']})
        ass[label]=record['assessment_proposal']
    with ip.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)
    ap.write_text(json.dumps(ass,indent=2,ensure_ascii=False)+'\n')
    receipt={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
             'proposal_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'rows':receipts,
             'scope':'Two whole rows accepted at their exact retained reading-order and current proof/source/computation/visual scopes. The607 assertions are shared once across both rows.'}
    (R/'analysis/UN24_UN39_final_completion_08.json').write_text(json.dumps(receipt,indent=2)+'\n')

if __name__=='__main__':
    raise SystemExit('These imports already ran inline; consult the exact receipts. No replay was performed.')
