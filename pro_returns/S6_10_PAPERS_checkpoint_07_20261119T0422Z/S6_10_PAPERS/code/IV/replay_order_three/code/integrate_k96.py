"""Integrate both fully audited E6 unselected-III cap progressions."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
qa=json.loads((R/'records/k96_standalone_qa.json').read_text());assert qa['status']=='PASS'
for name,key in [('source','source_sha256'),('include','include_sha256'),('pdf','pdf_sha256'),('certificate','certificate_sha256')]:assert sha(R/qa[name])==qa[key]
peer=json.loads((R/'records/checks_audit_e6_unselected_iii_extension.json').read_text());assert peer['status']=='PASS' and peer['source_sha256']==qa['source_sha256']
archive=R/'records/attempts/master73_sources_before_k96';archive.mkdir(exist_ok=False)
for name in ['notes/part3.tex','notes/part3_remaining_return_obligations.tex','code/update_report.py','code/part3/results_mapping.json','S6_06_BLIND_results.csv','S6_06_BLIND_report.md']:
 p=R/name;q=archive/name;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
p=R/'notes/part3.tex';s=p.read_text();inc=r'\input{notes/part3_e6_unselected_iii_extension.tex}';assert inc not in s;p.write_text(s+'\n'+inc+'\n')
p=R/'notes/part3_remaining_return_obligations.tex';s=p.read_text()
old=r'''The other cap orders and line branches at that collision remain
outside this completed scope. The \(r=1/4\) order-three collision'''
new=r'''P3K.96 extends this disc construction to both full progressions
\[
 (a,b;m)=(6,1;3l+2),\quad l\ge0,
 \qquad (a,b;m)=(2,3;3l),\quad l\ge1.
\]
The root fibres are respectively reduced type \(IV\) and smooth
elliptic. The proof gives the actual higher A2 translation, every
regular graph ray \((j,1)\), both section coefficient maps, the
good-root exceptional correction, the literal chord lift with central
coefficient one, its full norm unit of value four, every finite
character, and the complete reference-relative annular cochain.
For both primitive norm signs and every selected lattice-basis fan,
the proper source-disc family has identity closing and return zero.
The \(r=1/4\) order-three collision'''
assert old in s;s=s.replace(old,new,1).replace('P3K.76--95 cited','P3K.76--96 cited').replace('P3K.92--95 are new complete proofs.','P3K.92--96 are new complete proofs.');p.write_text(s)
summary=('K96 proves the full unselected-III disc extension for both (a,b;m)=(6,1;3l+2),l>=0, and (2,3;3l),l>=1. It retains the exact higher source/root graph, both Cartier section coefficients, the good-root exceptional correction, the central-one chord lift, full norm unit4, every finite character and complete annular reference. Both norm signs and every selected lattice fan have actual identity closing and return0. ')
p=R/'code/update_report.py';s=p.read_text().replace('P3K.5–P3K.95','P3K.5–P3K.96');old='Other line branches and cap orders remain open there. ';assert s.count(old)==2;s=s.replace(old,summary).replace('with all8,125 frozen files and the779-page','with all 8,125 frozen files and the 779-page');p.write_text(s)
p=R/'code/part3/results_mapping.json';m=json.loads(p.read_text());m['post_recovery_completed_return_results'].append({'id':'P3K.96','status':'Proved','item_of_prompt':'3.4','statement':summary,'proof':qa['source'],'latex_file':qa['include'],'source_sha256':qa['source_sha256'],'include_sha256':qa['include_sha256'],'certificate':qa['certificate'],'visual_qa':'records/k96_standalone_qa.json','root_audit':'records/root_audit_e6_unselected_iii_extension.json','provenance':'Full EX1–6 root read, checks full independent audit, and fourfold higher-root/line audit; exact graph-ray source omission corrected and all earlier bytes retained.'});p.write_text(json.dumps(m,indent=2)+'\n')
audit={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'reviewer':'root','id':'P3K.96','source_sha256':qa['source_sha256'],'tex_sha256':qa['include_sha256'],'scope':summary,'reviewed':['Entire EX1–6','Full M2 point/tensor multiplier and all finite/infinity vertical orders','Every good/reduced root equation and exact Miller weights','Actual higher A2 charts, implicit z function, translation field and full finite deck','Exact regular graph rays(j,1), adjacent determinant1, both coefficients j and distinct equality-ray directions','Quotient descent and unique minimal regular source, both inverse product maps of the common normalized graph','Good-root exceptional support functions and every correction ideal','Typed chord lift, both central-one formal-coordinate factors, exact deck cancellation','Full norm root, finite character, complete sector/log/reference Cauchy square','Uniform primitive-generator quotient, all-fan sphere transfer and identity disc closing','Numbered statement and all-page standalone QA/export hash consistency'],'peer_full':'records/checks_audit_e6_unselected_iii_extension.json','peer_root_line':'records/fourfold_audit_e6_higher_root_line.json','source_correction_history':'records/attempts/e6_unselected_iii_extension/graph_ray_source_patch_miss/','pending':'Integrated master73 typesetting and direct page review.'}
(R/'records/root_audit_e6_unselected_iii_extension.json').write_text(json.dumps(audit,indent=2)+'\n')
(R/'records/k96_master_integration.json').write_text(json.dumps({'status':'INTEGRATED_PENDING_MASTER73_QA','utc':audit['utc'],'retained_previous_sources':str(archive.relative_to(R)),'audit':'records/root_audit_e6_unselected_iii_extension.json'},indent=2)+'\n')
print('K96 integrated; master73 compilation and page review pending.')
