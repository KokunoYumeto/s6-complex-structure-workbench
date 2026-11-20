"""Integrate exact root-reviewed proof, source and presentation guards."""
from pathlib import Path
import datetime,hashlib,json,re

R=Path(__file__).resolve().parents[1]
packs=[
 ('II','audit_sign/II_followup_source_format_guards_06.json',8),
 ('IV','audit_sign/K111_retained_code_claim_guards_07.json',2),
 ('IV','audit_paper_i/closure_07/IV_workflow_residue_patches.json',7),
 ('V','audit_corrections/V_P112_P119_guarded_patches_07.json',16),
 ('V','audit_paper_i/closure_07/V_period_certificate_patches.json',3),
]
sources={p:(R/f'parts/{p}.body.linked.tex').read_text() for p in ['II','IV','V']}
updated=dict(sources);receipts=[]
for paper,filename,n in packs:
    f=R/filename;data=json.loads(f.read_text());guards=data['guards'] if isinstance(data,dict) else data
    assert len(guards)==n,(filename,len(guards))
    mapped=[]
    for g in guards:
        old=g.get('old',g.get('old_text'));new=g.get('new',g.get('new_text'))
        assert updated[paper].count(old)==1,(filename,g.get('label'),updated[paper].count(old))
        # The actual exported matrices and ODE solution are definitions here.
        new=new.replace('used to form $j_4$.  If $U_4j_4V_4$ is its exported Smith reduction,',
                        'used to form $j_4$.  Write $U_4j_4V_4$ for its exported Smith reduction;')
        new=new.replace("If $U_\\infty'=U_\\infty\\Gamma_\\infty$ and $U_\\infty(0)=I$, then",
                        "Let $U_\\infty$ solve $U_\\infty'=U_\\infty\\Gamma_\\infty$ with $U_\\infty(0)=I$.  The actual second evaluation is")
        updated[paper]=updated[paper].replace(old,new,1)
        mapped.append({'label':g.get('label'),'old':old,'new':new,'reason':g.get('reason',g.get('purpose',''))})
    receipts.append({'paper':paper,'guard_file':filename,'guard_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'guards':mapped})
for paper,s in updated.items():
    pattern=r'\\(?:tag|label)\{[^}]+\}'
    assert re.findall(pattern,sources[paper])==re.findall(pattern,s),(paper,'tag/label transport changed')
for paper,s in updated.items():(R/f'parts/{paper}.body.linked.tex').write_text(s)

out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'root_receiving_scope':'Root read the complete current P1.12/P1.19 proof, all 16 topology guards, all three fresh topology implementations and exact output basis maps; full receiving report and original Hatcher Theorem3.43 p254. Root read the complete replacement P1.16 proof, both current numerical implementations, complete path/error methodology and receipt. Root read all II, K111 and IV116/117/119 exact source/format guards; RFB/RFS replacements retain the displayed nonlinear geometric proofs and cite only actual current finite coverage.',
 'guards':sum(len(r['guards']) for r in receipts),'receipts':receipts,
 'papers':{p:{'before_sha256':hashlib.sha256(sources[p].encode()).hexdigest(),'after_sha256':hashlib.sha256(updated[p].encode()).hexdigest()} for p in updated},
 'pending':'Build26, actual changed-page inspection, current cross-paper page refresh, then exact row-specific completion assessment. No whole-before-proof or independent-model-family claim is added.'}
(R/'analysis/received_proof_integration_07.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'guards':out['guards'],'papers':list(updated)}))
