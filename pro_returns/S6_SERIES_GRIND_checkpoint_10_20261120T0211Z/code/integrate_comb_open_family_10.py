"""One-time guarded publication of the accepted actual twelve-tooth family."""
from pathlib import Path
from datetime import datetime, timezone
import copy, csv, hashlib, io, json, sys

R = Path(__file__).resolve().parents[1]
out = R/'analysis/comb_open_family_integration_10.json'
assert not out.exists()
sha = lambda b:hashlib.sha256(b).hexdigest()
packet = R/'audit_sign/comb_09'
assert sha((packet/'publication_guards.json').read_bytes()) == '509adef558d89eb555609736a03365be817e277de1d628070e487b6b70aa73ce'
assert sha((packet/'E25_proposition_and_proof.tex').read_bytes()) == '3cae248c5965ad3fd49de21cf59b2aeeb2847f9cfeeb339d82f0b88605c39491'
assert (R/'analysis/comb_open_family_acceptance_10.json').is_file()
q = json.loads((packet/'publication_guards.json').read_text())
before, pending, changes = {}, {}, []
def get(n):
    if n not in pending:
        before[n]=(R/n).read_text();pending[n]=before[n]
    return pending[n]
for a in q['guards']:
    names=[a['target']]
    if a['target']=='parts/II.body.tex':
        names.append('parts/II.body.linked.tex')
    for n in names:
        t=get(n)
        assert t.count(a['old_text'])==a['expected_count'], (n,a['reason'])
        pending[n]=t.replace(a['old_text'],a['new_text'])
        changes.append({'file':n,'reason':a['reason'],'old_sha256':sha(a['old_text'].encode()),'new_sha256':sha(a['new_text'].encode())})

# The frozen publication proposal remains unchanged. These exact receiving
# clarifications supply public numeric locators and the actual source map.
polish = [
    (r'Proposition labelled \texttt{comb}',r'Proposition~5.3'),
    ('The opened conic lemma gives the same local deformation space and',
     'Lemma~5.1 of \\cite{Viaclovsky2026Combs} gives the same local deformation space and'),
    ('Proposition \\texttt{comb}, equation \\texttt{originalnormal}\nand the subsequent twelve-tooth bound',r'Proposition~5.3 and \S9.2'),
    ('Lemma \\texttt{twistor}, Proposition \\texttt{comb}, and equation\n\\texttt{originalnormal}',r'Lemma~5.1, Proposition~5.3 and \S9.2'),
    ('The two-jet kernel in\n\\eqref{invII:eq:E12-jets} is unchanged by these reparameterizations.',
     'The actual source map is $y=r\\widetilde y/(1+t\\widetilde y)$.\nMultiplying its tautological columns by $1+t\\widetilde y$ gives\nexactly the displayed matrix action. The two-jet kernel in\n\\eqref{invII:eq:E12-jets} is unchanged by these reparameterizations.')
]
for n in ['parts/II.body.tex','parts/II.body.linked.tex']:
    for old,new in polish:
        assert pending[n].count(old)==1,(n,old)
        pending[n]=pending[n].replace(old,new)
        changes.append({'file':n,'old_text':old,'new_text':new,'reason':'Exact public source locator or underlying conic reparameterization; no result change.'})

for m in q['map_updates']:
    n=m['target'];d=json.loads(get(n))
    z=[x for x in d['main_theorems'] if x['letter']==m['letter']]
    assert len(z)==1
    z=z[0]
    assert z['title']==m['expected_old_title']
    assert [s['number'] for s in z['steps']]==m['expected_existing_step_numbers']
    z['title']=m['new_title']
    assert not set(m['append_body_labels'])&set(z['body_labels'])
    z['body_labels']+=m['append_body_labels'];z['steps'].append(m['append_step'])
    pending[n]=json.dumps(d,indent=2)+'\n'

n='audit_sign/row_assessments.json';d=json.loads(get(n));old_gate=copy.deepcopy(d['inv:E2.3'])
d['inv:E2.3'].update(
    confidence_state='Open general/special-member splitting problem with the actual open twelve-tooth family now proved',
    confidence_line='The complete root and independently frozen new two-jet derivations agree through the exact determinant/frame, analytic node-sufficiency, finite-character lift, admissible smoothing and collapse maps. E2.5 establishes K12=O(-8)+O(-9)^2 and Hodge49,48 on a nonempty open family. All earlier general bounds and source scopes are retained.',
    independent_routes=old_gate.get('independent_routes','')+' New complete independent derivation was frozen before the root target/code were received, with prior E15/E2.2 and route-cue exposure explicit. Receiving comparison and25 further exact checks follow that freeze; root53 fresh checks retain their own chronology.',
    remaining_risk='The splitting and section count for other tooth counts and for special members outside the established nonempty open twelve-tooth family remain. No numerical solution for a separately prescribed individual smoothing system is claimed.',
    format_check='Separate complete E2.5 proposition and seven-step proof inserted; old E2.3 label and all formula tags retained, with exact remaining scope. Current rebuild and page review pending.',
    layout_check='Pending current changed final-part pages after new E2.5 insertion.',
    completion_state='pending; general and special-member splitting question remains open')
pending[n]=json.dumps(d,indent=2)+'\n'
n='audit_root/row_assessments.json';d=json.loads(get(n));assert 'inv:E2.5' not in d
d['inv:E2.5']={
    'confidence_state':'Complete mathematical proof accepted for the constructed nonempty open twelve-tooth family',
    'confidence_line':'Full root derivation, complete independent freeze, complete receiving comparison and all publication proof steps have been read. The actual root/node/conic/frame/collapse maps and both cohomology vanishings prove the splitting. Root53 fresh assertions and receiving25 assertions have their exact independent/exposed scopes retained.',
    'independent_routes':['Root complete derivation and53-assertion new implementation, followed by explicit root-family supplement.','Independent25KB derivation frozen before root target and code reading, with prior inputs and route cues disclosed.','Complete receiving comparison and25-assertion post-receiving determinant/node/character/Hermite check.'],
    'remaining_risk':'No mathematical gate remains for this exact open-family statement. Current publication/source-credit and rendered-page gate still pending; broad E2.3 remains open.',
    'format_check':'Complete seven-step proof, statement, main F and seventh outline step, exact source locators and preserved final-part scope integrated; rebuild pending.',
    'layout_check':'Pending actual new-proof and changed front/final page inspection.',
    'completion_state':'pending current proof/source/format/layout consolidation'}
pending[n]=json.dumps(d,indent=2)+'\n'

n='S6_SERIES_GRIND_inventory.csv';s=get(n);reader=csv.DictReader(io.StringIO(s));fields=reader.fieldnames;rows=list(reader)
assert not any(v['label']=='inv:E2.5' for v in rows)
v={k:'' for k in fields}
v.update(paper='II',label='inv:E2.5',source_run='S6_SERIES_GRIND',source_id='E2.5',kind='new result',status='proved',main_or_supporting='supporting',uses='inv:E2.2; cdp:st:E15; invII:eq:E.6; Viaclovsky2026Combs',source_inventory_row='S6_SERIES_GRIND:comb:E2.5',source_paper='II',credited_to='Viaclovsky2026Combs Lemma5.1, Proposition5.3, section9.2 and section10(2); actual E15/E2.2 inputs. The new flat-kernel/two-jet/collapse proof is supplied here.',check_record=json.dumps({'root_acceptance':'analysis/comb_open_family_acceptance_10.json','source_comparison':'audit_sign/comb_09/source_comparison.json'}),notes='Nonempty open family of actual admissible twelve-tooth embedded smoothings; K12=O(-8)+O(-9)^2, e12=0, Hodge49,48. No general/special-member classification or numerical uniquely prescribed smoothing is inferred.',placement_state='printed in II',writing_state='complete seven-step proof and linked main F expansion',confidence_state='accepted proof; final publication consolidation pending',completion_state='pending current proof/source/format/layout consolidation',source_credit_verdict='Exact opened construction/source maps and separate new full proof; no worldwide priority claim',literature_disposition='Complete new actual kernel calculation retained at its exact open-family scope.')
rows.append(v)
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields);w.writeheader();w.writerows(rows);pending[n]=buf.getvalue()

n='analysis/source_bibliography_entries.json';d=json.loads(get(n))
note='\\newblock Freshly opened in this continuation on20November2026: original source Lemma5.1 and complete proof, Proposition5.3 and complete fixed-marking comb-smoothing proof, section9.2 original normal splitting and twelve-tooth bound, and section10(2) remaining Hodge question. Root and sign receiving scopes are separately recorded in audit_sign/comb_09/source_comparison.json and the root acceptance receipt. The new two-jet/collapse computation is supplied in E2.5.\n'
for e in d['Viaclovsky2026Combs']:
    assert note not in e['text'];e['text']+='\n'+note
pending[n]=json.dumps(d,indent=2,ensure_ascii=False)+'\n'

for n,t in pending.items():(R/n).write_text(t)
receipt={'utc':datetime.now(timezone.utc).isoformat(),'decision':'Accepted open-family result integrated; E2.3 remains open; no whole-row completion yet.','source_guards':q,'receiving_polish':polish,'old_E23_assessment':old_gate,'changes':changes,'files':{n:{'before_sha256':sha(before[n].encode()),'after_sha256':sha(t.encode())} for n,t in pending.items()},'root_reading':'Full independent and receiving derivations, full25-check code/output and complete E25 publication proof read. Explicit source locators rechecked from the original source.','pipeline_note':'Applied body guards to both raw and active linked II bodies. resolve_references.py was not rerun; unrelated later linked-source edits remain intact.'}
out.write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'files':len(pending),'inventory_rows':len(rows),'receipt':str(out.relative_to(R))}))
