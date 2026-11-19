"""Integrate the independently audited good attachment and reduced-II topology."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil
root=Path(__file__).resolve().parents[1]
def read(name):return json.loads((root/name).read_text())
def sha(name):return hashlib.sha256((root/name).read_bytes()).hexdigest()
stems={83:'part3_source_zero_good_attachment',84:'part3_os49_reduced_ii_caps'}
# Mathematical promotion and master typesetting run while the independent
# all-page standalone visual reviews finish. The checkpoint-ready script
# requires both final PASS records before any deliverable is frozen.
q83=read('records/k83_standalone_checks.json')
assert not q83['bounds_issues'] and not q83['warnings']
# Final inline delimiter fixes are saved; standalone final QA checks the final hash.
assert (root/'notes/part3_source_zero_good_attachment.tex').is_file()
q84=read('records/k84_export_manifest.json')
assert q84['draft_sha256']==sha('notes/part3_os49_reduced_ii_caps.tex')
assert read('records/root_audit_source_zero_good_global_attachment.json')['status']=='PASS_GC1_TO_GC10_FULL_GLOBAL_ATTACHMENT'
assert read('records/fourfold_audit_source_zero_good_attachment.json')['status']=='PASS'
assert read('records/root_audit_os49_reduced_ii_caps_working.json')['status']=='PASS_RI1_TO_RI5'
assert read('records/fourfold_audit_os49_reduced_ii_caps.json')['status']=='PASS'
archive=root/'records/checkpoint19_prior_master66';archive.mkdir(exist_ok=False)
for name in ('S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.log',
 'notes/part3.tex','notes/part3_remaining_return_obligations.tex',
 'code/update_report.py','code/part3/results_mapping.json'):
 dest=archive/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(root/name,dest)
p=root/'notes/part3.tex';s=p.read_text()
for n,stem in stems.items():
 line='\\input{notes/'+stem+'.tex}';assert line not in s;s+='\n'+line+'\n'
p.write_text(s)
p=root/'notes/part3_remaining_return_obligations.tex';s=p.read_text()
old=r'''The good branch retains the two possibilities
\((Z_0,Z_1)=(0,1)\) or \((14,15)\) until its separate
two-primitive global proof is promoted. Its full finite cut,
two intermediate cap characters and upper source-moment trace
are recorded in the good-cut working proof. Source-zero returns
on nonvertical fans require their own completed comparison.'''
new=r'''K83 completes the separate good-branch two-primitive global
attachment. Its initial physical integer is zero and its
reflected class is one, with the coupled pair \((0,1)\).
Combining its actual initial return with K82 gives every good
vertical class
\[
 Z_j=4\binom{j+1}{3}+\binom{j+1}{2}
                       -4pk\binom j2\pmod {28}.
\]
Both intermediate cap characters, both chronological charged
faces and the upper source-moment trace are retained in K83.
Source-zero returns on nonvertical fans require their own
completed comparison with the full initial relative integers.'''
assert old in s;s=s.replace(old,new)
old=r'''The reduced-II roots of order \(6l+1\) retain their separate
source and Cartier calculation under audit. Remaining parts of
item 3.4 include those singular-site sectors, source-zero
nonvertical fans, the remaining marked source-moduli loops and
endpoint sectors outside the completed fixed-source scope.
No value is assigned here to those remaining sectors.'''
new=r'''K84 constructs the reduced-II roots of order \(h=6l+1\)
with their actual source and Cartier arrows. Together with the
IV-star cap \(m=3k\), their sphere sector is exactly
\[
                 h n_A+m n_B=\pm1.
\]
All four integral specialization and prism maps, the full
fundamental group and every retained line character are proved.
The smallest such datum is \((m,h,n_A,n_B)=(3,7,1,-2)\).
Its return, further singular-site scopes, source-zero nonvertical
fans, the remaining marked source-moduli loops and endpoint
sectors outside the completed fixed-source scope remain to be
computed through their actual maps. No value is assigned here
to those remaining returns.'''
assert old in s;s=s.replace(old,new)
old=r'''The good branch has a separate two-primitive finite strip and
the exact upper free source trace in
\path{notes/part3_source_zero_good_cut_working.md}; its final
actual-return comparison remains under independent review at
this stage of the record.'''
new=r'''K83 supplies the good branch's separate two-primitive finite
strip, its exact upper free source trace and final actual-return
comparison. Its complete oriented physical quotient boundary is
\[
              -N-P_0-P_1-B_F-B_4+Q_{\rm up}.
\]
Both charged physical lines are \(\mathcal O(-1)\); the upper
line has its explicit global nonzero coefficient frame. The whole
fixed and four-sphere normal clutches remain in the calculation.
Every auxiliary characteristic index is zero. The same selected
Hopf tube and K68 inverse-clutch map identify the resulting
\(A(N)=0\) with the actual good parameter return.'''
assert old in s;s=s.replace(old,new)
p.write_text(s)
p=root/'code/update_report.py';s=p.read_text()
s=s.replace('P3K.5–P3K.82; exact corrected scopes below','P3K.5–P3K.84; exact corrected scopes below')
old='The good branch still retains(0,1) or(14,15) while its separate full two-primitive attachment and actual-return comparison receive final review.'
new='K83 proves the separate good two-primitive global attachment: the initial physical integer is0 and the reflected class1, with coupled pair(0,1). Its two chronological charged faces and one upper source-trace face have their actual physical lines; the whole fixed trace and normal clutches occur once. Combining K83 with K82 gives every good vertical class Z_j=4*binom(j+1,3)+binom(j+1,2)-4*p*k*binom(j,2) modulo28.'
assert s.count(old)==2;s=s.replace(old,new)
old='The reduced-II order6l+1 source/Cartier topology is recorded separately under audit. K75 retains the good source-zero attachment, source-zero nonvertical fans, further singular-site scopes, marked source-moduli loops and endpoint sectors outside the completed fixed-source OS49 scope.'
new='K84 constructs the full reduced-II root of orderh=6l+1 and proves the joint IVstar m=3k sphere criterion h*n_A+m*n_B=+/-1, with every actual source/Cartier arrow, full integral specialization matrix, D-valued prism, fundamental relation and finite character. The smallest datum is(m,h,n_A,n_B)=(3,7,1,-2). Its return remains under construction. K75 retains source-zero nonvertical fans, the reduced-II returns and further singular-site scopes, marked source-moduli loops and endpoint sectors outside the completed fixed-source OS49 scope.'
assert s.count(old)==2;s=s.replace(old,new)
p.write_text(s)
p=root/'code/part3/results_mapping.json';m=json.loads(p.read_text())
rows=m.setdefault('additional_source_loop_results',[])
for n,stem in stems.items():
 if not any(x.get('id')==f'P3K.{n}' for x in rows):
  rows.append({'id':f'P3K.{n}','status':'Proved','item_of_prompt':'3.4',
   'statement':('Complete good source-zero attachment: initial integer0, reflected class1 and coupled pair(0,1).' if n==83 else 'Actual reduced-II OS49 caps and full joint integral sphere topology h*n_A+m*n_B=+/-1.'),
   'latex_file':f'notes/{stem}.tex','visual_qa':f'records/k{n}_standalone_visual_qa.json'})
p.write_text(json.dumps(m,indent=2)+'\n')
(root/'records/k83_k84_promotion.json').write_text(json.dumps({
 'utc':datetime.now(timezone.utc).isoformat(),'status':'PROMOTED_AFTER_TWO_FULL_PROOF_AUDITS_FINAL_CHECKPOINT_REQUIRES_ALL_PAGE_QA',
 'statements':['P3K.83','P3K.84'],'archive':str(archive.relative_to(root)),
 'include_hashes':{str(n):sha(f'notes/{stem}.tex') for n,stem in stems.items()},
 'next_master_build':67,'remaining':'Nonvertical source-zero relative data, reduced-II returns and other source/endpoint sectors.'
},indent=2)+'\n')
print('K83--84 integrated; prior complete master66 and scope preserved.')
