"""Integrate the fully audited E6 selected-cusp return and preserve master72."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
qa=json.loads((R/'records/k95_standalone_visual_qa.json').read_text());assert qa['status']=='PASS'
for name,h in qa['hashes'].items():assert sha(R/name)==h,name
archive=R/'records/checkpoint23_prior_master72';archive.mkdir(exist_ok=False)
for name in ['notes/part3.tex','notes/part3_remaining_return_obligations.tex','code/update_report.py','code/part3/results_mapping.json','S6_06_BLIND_results.csv','S6_06_BLIND_report.md','S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.log','S6_06_BLIND_paper.aux','S6_06_BLIND_paper.toc']:
 p=R/name;q=archive/name;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
p=R/'notes/part3.tex';s=p.read_text();inc=r'\input{notes/part3_e6_selected_cusp.tex}';assert inc not in s;p.write_text(s+'\n'+inc+'\n')
p=R/'notes/part3_remaining_return_obligations.tex';s=p.read_text()
old=r'''attachment and return are still being calculated. The selected-cusp
boundary and other selected-node generators likewise retain their
working status until their complete comparison maps are audited. The working notes assign no return to an unfinished
attachment. Part 3.4 therefore remains incomplete.'''
new=r'''attachment and return are still being calculated.

P3K.95 completes the E6 selected-cusp generator on the ordered
\(w\)-cover for \(M_6\), suspension by \(-G\), and the quadratic
cap, with both primitive norm signs, all retained characters and
full reference annular maps, and every selected lattice-basis fan.
The exact source, Cartier, root, exterior, normal and Cox arrows
identify its full all-fan algorithm with P3K.71. On the vertical fan
\(T_j\) its physical pair and class are
\[
 (k_M,\ell_M)=(-6-18j(j-1),0),\qquad
 [\Sigma_j]=-1-3j(j-1)\pmod {28}.
\]
Its native free pair is \((0,-6-18j(j-1))\). The actual parameter
map satisfies \(r-1/3=-w^4/(3(w^2-3)^2)\), so the stated
ordered loop has degree four over the original source parameter.
Other selected-node generators and the remaining cap scopes still
require their full comparison maps. The working notes assign no
return to an unfinished attachment. Part 3.4 remains incomplete.'''
assert old in s;s=s.replace(old,new,1).replace('P3K.76--94 cited','P3K.76--95 cited').replace('P3K.92--94 are new complete proofs.','P3K.92--95 are new complete proofs.');p.write_text(s)
summary=('K95 completes the E6 ordered selected-cusp loop for M6,b1,m2, both signed primitive norms, every retained finite character and full annular reference, and every selected lattice fan. Its exact comparison to K71 gives vertical physical pair(-6-18j(j-1),0), class -1-3j(j-1) modulo28, and native pair(0,-6-18j(j-1)). The exact ordered parameter has degree4 over r-1/3. The remaining selected-node generators, other cap scopes and the complete three-step order-three collision return remain unfinished. ')
p=R/'code/update_report.py';s=p.read_text().replace('P3K.5–P3K.94','P3K.5–P3K.95');old='The selected-cusp and other source generators remain under full map audit. ';assert s.count(old)==2;s=s.replace(old,summary);s=s.replace('Checkpoint21 was independently restored in full and saved successfully, with 7,812 verified files.','Checkpoint21 was independently restored in full and saved successfully, with 7,812 verified files. Checkpoint22 was independently restored and saved with all8,125 frozen files and the779-page master72 manuscript; its byte-exact lossless reencoding and verification are recorded.');p.write_text(s)
p=R/'code/part3/results_mapping.json';m=json.loads(p.read_text());m['post_recovery_completed_return_results'].append({'id':'P3K.95','status':'Proved','item_of_prompt':'3.4','statement':summary,'proof':'notes/part3_e6_selected_cusp_working.md','latex_file':'notes/part3_e6_selected_cusp.tex','source_sha256':qa['hashes']['notes/part3_e6_selected_cusp_working.md'],'include_sha256':qa['hashes']['notes/part3_e6_selected_cusp.tex'],'certificate':'code/part3_fourfold/e6_selected_cusp.json','visual_qa':'records/k95_standalone_visual_qa.json','root_audit':'records/root_audit_e6_selected_cusp.json','provenance':'Full source/Cartier/root/cap/normal/Cox construction; root and independent peer read every proof section.'});p.write_text(json.dumps(m,indent=2)+'\n')
p=R/'records/root_audit_e6_selected_cusp.json';audit=json.loads(p.read_text());audit['pending']='Central master73 compilation and direct rendering review.';audit['promotion_crosscheck']='PASS: only the proved statement, source status and display/path layout changed after the fully audited proof.';audit['tex_sha256']=qa['hashes']['notes/part3_e6_selected_cusp.tex'];p.write_text(json.dumps(audit,indent=2)+'\n')
(R/'records/k95_master_integration.json').write_text(json.dumps({'status':'INTEGRATED_PENDING_MASTER73_QA','utc':datetime.now(timezone.utc).isoformat(),'retained_master72':str(archive.relative_to(R)),'audit':'records/root_audit_e6_selected_cusp.json'},indent=2)+'\n')
print('K95 integrated; master73 build and page review pending.')
