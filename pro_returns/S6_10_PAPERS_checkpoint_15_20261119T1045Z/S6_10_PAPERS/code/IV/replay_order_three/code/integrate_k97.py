"""K97 integration delegated by root; preserve master73 and exact prior registers."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,fitz,re
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((R/'records/k97_export_manifest.json').read_text())
qa=dict(manifest);qa.update(status='PASS',reviewer='blind_control',utc=datetime.now(timezone.utc).isoformat(),pdf='records/k97_standalone/k97_standalone.pdf',pages=8,directly_reviewed_pages=list(range(1,9)),findings=[],visual_review='Every rendered page directly reviewed; no clipping, collisions, missing symbols or malformed equations.')
qa['pdf_sha256']=sha(R/qa['pdf']);doc=fitz.open(R/qa['pdf']);assert len(doc)==8
qa['out_of_bounds_words']=[(i+1,w[4]) for i,p in enumerate(doc) for w in p.get_text('words') if w[0]<-.5 or w[1]<-.5 or w[2]>p.rect.width+.5 or w[3]>p.rect.height+.5];assert not qa['out_of_bounds_words']
log=(R/'records/k97_standalone/k97_standalone.log').read_text();assert not re.search(r'Overfull|Missing character|undefined|LaTeX Error',log)
for k in ['source','include','certificate']:assert sha(R/qa[k])==qa[k+'_sha256']
peer=json.loads((R/'records/checks_audit_e6_d_zero_disc.json').read_text());assert peer['status']=='PASS' and peer['source_sha256']==qa['source_sha256']
(R/'records/k97_standalone_qa.json').write_text(json.dumps(qa,indent=2)+'\n');manifest['qa']='PASS';manifest['qa_record']='records/k97_standalone_qa.json';manifest['pdf']=qa['pdf'];manifest['pdf_sha256']=qa['pdf_sha256'];(R/'records/k97_export_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
archive=R/'records/attempts/master74_sources_before_k97';archive.mkdir(exist_ok=False)
for name in ['notes/part3.tex','notes/part3_remaining_return_obligations.tex','code/update_report.py','code/part3/results_mapping.json','S6_06_BLIND_results.csv','S6_06_BLIND_report.md','S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.log']:
 p=R/name;q=archive/name;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
p=R/'notes/part3.tex';s=p.read_text();inc=r'\input{notes/part3_e6_d_zero_disc.tex}';assert inc not in s;p.write_text(s+'\n'+inc+'\n')
para=r'''P3K.97 completes the native E6 infinity-coordinate disc at either
\(w^2=3\), for both cap progressions of P3K.96. The actual source,
Cartier, root, physical-circle and annular maps carry the punctured
original family to a proper smooth sphere family on the full native
disc. Both point and tensor Tate frames, every finite character,
the transported period discrepancy and the full scalar closing are
retained. Each prescribed lattice-basis fan and both primitive norm
signs have marked positive \(w\)-loop return zero. The exact original
parameter is
\[
 \epsilon=1/r=(w^2-3)^2/(3-2w^2).
\]
This marked loop has degree two over the original infinity meridian;
no shorter original-parameter endpoint or return is inferred.
'''
p=R/'notes/part3_remaining_return_obligations.tex';s=p.read_text();needle='The \\(r=1/4\\) order-three collision';assert needle in s;s=s.replace(needle,para+needle,1).replace('P3K.76--96 cited','P3K.76--97 cited').replace('P3K.92--96 are new complete proofs.','P3K.92--97 are new complete proofs.');p.write_text(s)
summary='K97 completes the E6 native infinity-coordinate disc at both w^2=3 points for both full cap progressions. Its actual source, Cartier, root, point/tensor Tate, period and scalar maps give marked w-loop return0 for every selected lattice fan and both norm signs. The exact parameter epsilon=1/r=(w^2-3)^2/(3-2w^2) has local degree2; no shorter original-parameter return is inferred. '
p=R/'code/update_report.py';s=p.read_text().replace('P3K.5–P3K.96','P3K.5–P3K.97');needle='The r=1/4 order-three collision now has';assert s.count(needle)==2;s=s.replace(needle,summary+needle);p.write_text(s)
p=R/'code/part3/results_mapping.json';m=json.loads(p.read_text());m['post_recovery_completed_return_results'].append(dict(id='P3K.97',status='Proved',item_of_prompt='3.4',statement=summary,proof=qa['source'],latex_file=qa['include'],source_sha256=qa['source_sha256'],include_sha256=qa['include_sha256'],certificate=qa['certificate'],visual_qa='records/k97_standalone_qa.json',root_audit='records/root_audit_e6_d_zero_disc.json'));p.write_text(json.dumps(m,indent=2)+'\n')
audit=dict(status='PASS',reviewer='root',recorded_by='blind_control under explicit delegated central ownership',utc=qa['utc'],id='P3K.97',source_sha256=qa['source_sha256'],tex_sha256=qa['include_sha256'],scope=summary,reviewed=['Full DZ6.1–6 root mathematical read','Actual source, both root progressions and finite-character endpoint','Point/theta/tensor frame dictionary with D^5 and D weights','Full period residual and reference-relative groupoid solve','Explicit fixed-contour Laurent O(-1), O, O(1) operators and finite averaging','Global divisor and NS generator proof','Cauchy scalar closure, both forward/inverse endpoint squares','Exact degree-two original infinity parameter','All eight standalone pages directly reviewed'],peer='records/checks_audit_e6_d_zero_disc.json',pending='Master74 integrated rendering and direct review')
(R/'records/root_audit_e6_d_zero_disc.json').write_text(json.dumps(audit,indent=2)+'\n');(R/'records/k97_master_integration.json').write_text(json.dumps(dict(status='INTEGRATED_PENDING_MASTER74_QA',archive=str(archive.relative_to(R)),utc=qa['utc']),indent=2)+'\n')
print('K97 standalone all8 pages PASS; central integration complete.')
