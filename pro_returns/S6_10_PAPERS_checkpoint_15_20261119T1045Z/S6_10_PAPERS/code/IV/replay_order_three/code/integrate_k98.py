"""Integrate the fully audited higher-cap E6 selected-cusp proof."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
qa=json.loads((R/'records/k98_standalone_visual_qa.json').read_text());assert qa['status']=='PASS'
source='notes/part3_e6_selected_cusp_all_caps_working.md';tex='notes/part3_e6_selected_cusp_all_caps.tex'
assert sha(R/source)==qa['source_sha256'] and sha(R/tex)==qa['tex_sha256']
assert sha(R/'code/part3_fourfold/k98_standalone.pdf')==qa['pdf_sha256']
peer=json.loads((R/'records/blind_audit_e6_selected_cusp_all_caps.json').read_text())
assert peer['status']=='PASS' and peer['source_sha256']==qa['source_sha256']
archive=R/'records/checkpoint24_prior_master74';archive.mkdir(exist_ok=False)
names=['S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.tex','S6_06_BLIND_paper.log','S6_06_BLIND_report.md','S6_06_BLIND_results.csv','notes/part3.tex','notes/part3_remaining_return_obligations.tex','code/update_report.py','code/part3/results_mapping.json','records/root_audit_e6_selected_cusp_all_caps.json']
for name in names:
 p=R/name;q=archive/name;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
p=R/'notes/part3.tex';s=p.read_text();inc=r'\input{notes/part3_e6_selected_cusp_all_caps.tex}';assert inc not in s;p.write_text(s+'\n'+inc+'\n')
p=R/'notes/part3_remaining_return_obligations.tex';s=p.read_text()
old=r'''Other selected-node generators and the remaining cap scopes still
require their full comparison maps.'''
new=r'''P3K.98 extends this full selected-cusp calculation to both complete
cap progressions of P3K.96, with the same fixed scalar, both norm signs,
every finite character and complete annular reference. Its actual
point-to-tensor line arrow, all higher root graphs, even-parameter
annular map and both normal caps identify the exact vertical free
pair above and every K71 fan step. The full smooth-fibre theta
reflection and its target period give the actual height-one arrow;
the relative \(p_1\) calculation carries the explicit regular-level
cobordism and its boundary transgression.
Other selected-node generators and the remaining singular-site and
endpoint scopes still require their full comparison maps.'''
assert old in s;s=s.replace(old,new,1).replace('P3K.76--97 cited','P3K.76--98 cited').replace('P3K.92--97 are new complete proofs.','P3K.92--98 are new complete proofs.');p.write_text(s)
summary=('K98 extends the ordered E6 selected-cusp calculation to both full cap progressions(6,1;3l+2),l>=0, and(2,3;3l),l>=1, with both primitive norm signs, every finite character/full reference, fixed scalar and every selected lattice fan. The actual source/Cartier/root/annular/normal/cap maps give the same vertical physical pair(-6-18j(j-1),0), native pair(0,-6-18j(j-1)), class-1-3j(j-1) modulo28 and full K71 fan algorithm. The exact theta reflection includes the target period, and the relative p1 pairing is proved by the literal regular-level cobordism with its full boundary transgression. ')
p=R/'code/update_report.py';s=p.read_text().replace('P3K.5–P3K.97','P3K.5–P3K.98')
needle='The remaining selected-node generators, other cap scopes and the complete three-step order-three collision return remain unfinished.'
replacement=summary+'The remaining selected-node generators, additional singular-site and endpoint scopes, and the complete three-step order-three collision return remain unfinished.'
assert s.count(needle)==2;s=s.replace(needle,replacement)
old='Checkpoint22 was independently restored and saved with all 8,125 frozen files and the 779-page master72 manuscript; its byte-exact lossless reencoding and verification are recorded.'
new=old+' Checkpoint23 was independently restored and saved with all8,464 frozen files and the805-page master74 manuscript; its exact original file sizes and hashes were all verified.'
assert old in s;s=s.replace(old,new);p.write_text(s)
p=R/'code/part3/results_mapping.json';m=json.loads(p.read_text());m['post_recovery_completed_return_results'].append({'id':'P3K.98','status':'Proved','item_of_prompt':'3.4','statement':summary,'proof':source,'latex_file':tex,'source_sha256':qa['source_sha256'],'include_sha256':qa['tex_sha256'],'certificate':qa['certificate'],'visual_qa':'records/k98_standalone_visual_qa.json','root_audit':'records/root_audit_e6_selected_cusp_all_caps.json','full_independent_peer':'records/blind_audit_e6_selected_cusp_all_caps.json'});p.write_text(json.dumps(m,indent=2)+'\n')
audit=json.loads((archive/'records/root_audit_e6_selected_cusp_all_caps.json').read_text())
audit.update(status='PASS',utc=datetime.now(timezone.utc).isoformat(),id='P3K.98',source_sha256=qa['source_sha256'],tex_sha256=qa['tex_sha256'],scope=summary,pending='Integrated master75 typesetting and direct visual review.',full_independent_peer='records/blind_audit_e6_selected_cusp_all_caps.json',standalone_qa='records/k98_standalone_visual_qa.json')
audit['reviewed']+=['Final EG41a relative regular-value cobordism, literal cutoff map and retained outer transgression','Exact final formal statement and all scope restrictions','Final standalone nine-page QA and source/include/certificate hash consistency']
(R/'records/root_audit_e6_selected_cusp_all_caps.json').write_text(json.dumps(audit,indent=2)+'\n')
(R/'records/k98_master_integration.json').write_text(json.dumps({'status':'INTEGRATED_PENDING_MASTER75_QA','utc':audit['utc'],'retained_master74':str(archive.relative_to(R)),'audit':'records/root_audit_e6_selected_cusp_all_caps.json'},indent=2)+'\n')
print('K98 integrated; master75 build and direct review pending.')
