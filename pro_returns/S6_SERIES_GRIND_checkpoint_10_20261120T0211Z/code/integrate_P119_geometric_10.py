"""One-time exact P1.19 geometric repair and comb-outline precision import."""
from pathlib import Path
from datetime import datetime, timezone
import copy, csv, hashlib, io, json

R=Path(__file__).resolve().parents[1]
out=R/'analysis/P119_geometric_integration_10.json'
assert not out.exists()
sha=lambda b:hashlib.sha256(b).hexdigest()
source=R/'audit_p119_fresh/comparison_09'
review=R/'audit_corrections/P119_geometric_09'
assert sha((review/'FULL_RECEIVING_REVIEW.md').read_bytes())=='7e3539b09d05e1109f1a15a93e695e7c757dc5a5a548e974a2a3e67b1948ebd2'
assert sha((source/'GEOMETRIC_COMPARISON_02.md').read_bytes())=='c5b7d4b21f94d941231013edf9eab19bc20d8569f91bd6049dcf81040c6b3f67'
pub=R/'audit_root/P119_geometric_10/root_reviewed_publication.tex'
assert sha(pub.read_bytes())=='bc82ad208b69e62b2cf719f1ce24fc2d564140dbfde71bfd8d29b0ca275d1899'
q=json.loads((source/'P119_SOURCE_GUARDS_02.json').read_text())
assert sha((source/'P119_PROPOSED_COMPLETE_02.tex').read_bytes())==q['complete_proposal_sha256']
before,pending,changes={},{},[]
def get(n):
    if n not in pending:
        before[n]=(R/n).read_text();pending[n]=before[n]
    return pending[n]
n=q['path'];t=get(n);assert sha(t.encode())==q['source_before_sha256']
original_proposal=(source/'P119_PROPOSED_COMPLETE_02.tex').read_text()
for g in q['guards']:
    assert t.count(g['old'])==g['expected_occurrences'],g['id']
    new=g['new']
    if g['id']=='p119_insert_complete_marked_proof':
        assert new.count(original_proposal)==1
        new=new.replace(original_proposal,pub.read_text())
    t=t.replace(g['old'],new)
    changes.append({'file':n,'guard':g['id'],'old_sha256':sha(g['old'].encode()),'new_sha256':sha(new.encode()),'reason':g['reason']})
assert t.count(r'\label{night:P1.19}')==1
for i in range(1,9):assert t.count(r'\tag{1.19.'+str(i)+'}')==1
pending[n]=t

# Apply the received central-node precision to the already integrated F step.
fq=json.loads((R/'audit_sign/comb_09/F_outline_precision_guard_10.json').read_text())
for g in fq['guards']:
    n=g['target'];t=get(n);assert t.count(g['old_text'])==g['expected_count']
    pending[n]=t.replace(g['old_text'],g['new_text'])
for g in fq['map_updates']:
    n=g['target'];d=json.loads(get(n))
    m=next(x for x in d['main_theorems'] if x['letter']==g['letter'])
    st=next(x for x in m['steps'] if x['number']==g['step'])
    assert st['claim_tex']==g['old_claim_tex'];st['claim_tex']=g['new_claim_tex']
    pending[n]=json.dumps(d,indent=2)+'\n'

n='audit_corrections/row_assessments.json';d=json.loads(get(n));old=copy.deepcopy(d['night:P1.19']);v=d['night:P1.19']
v.update(
 confidence_state='Proved: complete actual integral geometric diagram comparison received and integrated',
 confidence_line='The full new all-degree triangle/product and floor-chain maps realize the literal signed finite-cap norm maps and based affine meridians. The coefficient-two cap homotopy, complement cone map, inverse-word cusp homotopy and explicit integral seven-chain fix the simultaneous marking. Root and corrections received every proof step, both154/113-check programs and the50-check receiving implementation. The retained local-duality/F_k reduction and full integral arrays then give the stated actual global homology.',
 independent_routes=old['independent_routes']+' The new geometric repair is post-reading work: complete new25KB derivation,154 exact diagram checks and113 top-adapter checks, then full root/corrections receiving comparison and50 independent signed-sweep/filler/shear checks at their stated exposed scopes. The cusp sign reconstruction was committed before its new proof section was opened, after the target formula was supplied. No full-before-reading credit is manufactured for the additional all-degree geometric block.',
 remaining_risk='The mathematical common-fibre/finite-cap/cusp-marking gate is closed by the complete explicit maps. Current rebuilt-page/source-reference checks remain. The full before-reading confidence scope of the added geometric steps still requires reconciliation or a fresh derivation; the old failed cellular-approximation claim and its withdrawn closure remain preserved.',
 format_check='Permanent label and all eight old formula tags preserved; complete theorem restored before the genus-two section. The exact geometric comparison and local-duality normal form are fully printed. An ambiguous rank-nine antecedent is replaced by the explicit H4 boundary map. Current build pending.',
 layout_check='Pending actual current complete new proof, diagnostic and moved-section page inspection; old build31/32 receipts retain their exact scopes.',
 completion_state='pending current full-proof layout/reference and added-step before-reading confidence reconciliation')
pending[n]=json.dumps(d,indent=2)+'\n'

n='S6_SERIES_GRIND_inventory.csv';reader=csv.DictReader(io.StringIO(get(n)));fields=reader.fieldnames;rows=list(reader)
matches=[r for r in rows if r['label']=='night:P1.19'];assert len(matches)==1
r=matches[0];assert r['status']=='open';r['status']='proved'
r['source_credit_verdict']='The actual geometric-diagram gate is now closed by the full explicit all-degree maps and received proof. The prior fresh frozen algebraic derivation and all exact source openings retain their chronology; new geometric steps are post-reading and are assessed separately for whole-row completion.'
r['notes']+=' Current20November2026 repair: full integral geometric common-fibre/finite-cap/cusp comparison accepted and integrated, including actual based meridians, coefficient-two cap homotopy and seven-chain cusp identification. See analysis/P119_geometric_integration_10.json. Prior withdrawn closure and gap placement are retained as chronological history.'
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields);w.writeheader();w.writerows(rows);pending[n]=buf.getvalue()

for n,t in pending.items():(R/n).write_text(t)
now=datetime.now(timezone.utc).isoformat()
receipt={'utc':now,'decision':'Mathematical geometric comparison accepted and integrated; P1.19 restored to proved. Whole-row completion remains pending its exact confidence and current-page gates.','root_reading':'Complete new geometric proof, full154/113 programs, full publication TeX (reread alone after initial truncated combined call), full corrections receiving report/exposure/sign reconstruction and all50-check code/output actually read.','old_assessment':old,'new_assessment':v,'guards':q,'publication_clarification':json.loads((pub.parent/'publication_precision_10.json').read_text()),'comb_outline_precision':fq,'changes':changes,'files':{n:{'before_sha256':sha(before[n].encode()),'after_sha256':sha(t.encode())} for n,t in pending.items()},'receiving_sha256':{str(p.relative_to(R)):sha(p.read_bytes()) for p in [source/'GEOMETRIC_COMPARISON_02.md',source/'geometric_diagram_check_02.py',source/'geometric_diagram_check_02.json',source/'top_chain_adapter.py',source/'top_chain_adapter.json',review/'FULL_RECEIVING_REVIEW.md',review/'FULL_RECEIVING_RECEIPT.json',review/'receiving_sign_reconstruction.md',review/'exact_receiving_checks.py',review/'exact_receiving_checks.json',pub]}}
out.write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
e=R/'audit_root/P119_geometric_10/CHECK_EVENTS.tsv';assert not e.exists()
with e.open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome','event_id'])
    w.writerow(['night:P1.19',now,'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; root','targeted proof check','Full new all-degree geometric proof, complete receiving report, exact code and publication proof accepted. All actual q_i, common-fibre, cone, inverse-word and invariant-subtorus maps are supplied. Mathematical status restored to proved; whole-row confidence/QA gates retain their precise remaining scope. Receipt analysis/P119_geometric_integration_10.json.','ce:grind-root:P119-geometric-acceptance-10'])
print(json.dumps({'files':len(pending),'P119_status':'proved','whole_row_completion_awarded':False,'receipt':str(out.relative_to(R))}))
