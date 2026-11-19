from pathlib import Path
import json,hashlib,datetime,shutil,sys,re
R=Path(__file__).resolve().parents[2];A=R/'analysis/continuation_II_ledger'
rels=['papers/II/revisions/cdp_st_A.3.4.tex','papers/II/body_source.tex','papers/II/body.tex','S6_10_PAPERS_II.tex'];B=A/'A3_4_Step5_installation_before';rec=A/'A3_4_Step5_installation_receipt.json'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
if '--revert' in sys.argv:
 x=json.loads(rec.read_text());assert all(h(R/p)==x['after_sha256'][p] for p in rels),'A file changed after installation; review before reverting.'
 for i,p in enumerate(rels):shutil.copyfile(B/f'{i:02d}_{Path(p).name}',R/p)
 print('Restored exact four prior files.');sys.exit()
assert not rec.exists();B.mkdir(exist_ok=False)
old=(A/'A3_4_target_after_freeze.tex').read_text().rstrip('\n');marker=r'\noindent\textbf{Step 5.}';prefix=old[:old.index(marker)];oldstep=old[old.index(marker):old.index(r'\end{proof}')]
newstep=(A/'A3_4_Step5_finite_kernel_replacement.tex').read_text();new=prefix+newstep+r'\end{proof}'
(A/'A3_4_current_replacement_proof.tex').write_text(new+'\n');(A/'A3_4_old_Step5_preserved.tex').write_text(oldstep)
before={};current_proof_hashes={}
for i,rel in enumerate(rels):
 p=R/rel;before[rel]=h(p);shutil.copyfile(p,B/f'{i:02d}_{p.name}');s=p.read_text();k=s.index(r'\label{cdp:st:A.3.4}');a=s.index(r'\begin{proof}',k);b=s.index(r'\end{proof}',a)+len(r'\end{proof}');original=s[a:b]
 if i==0:
  strip=lambda z:re.sub(r'\\noindent\\textbf\{Step \d+\.\} ','',z).strip()
  assert strip(original)==strip(old),'Revision has unexpected mathematics.'
 else:assert original==old,'Active proof differs from frozen target.'
 (A/f'A3_4_{p.name}_proof_before_Step5.tex').write_text(original+'\n')
 s=s[:a]+new+s[b:];p.write_text(s)
 # Full active proof prefix is byte-identical to old Steps1–4.
 assert new.startswith(prefix)
 current_proof_hashes[rel]=hashlib.sha256(new.encode()).hexdigest()
x={'installed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'label':'cdp:st:A.3.4','authorization':'Root explicitly authorized Step5-only replacement after the clean finite-kernel derivation, with all old text preserved; Steps1–4 remain pending fresh residual review.','before_sha256':before,'after_sha256':{p:h(R/p) for p in rels},'old_full_proof_sha256':hashlib.sha256(old.encode()).hexdigest(),'current_proof_sha256_without_trailing_newline':hashlib.sha256(new.encode()).hexdigest(),'current_proof_hashes':current_proof_hashes,'steps1_through4_byte_identical_in_active_proofs':True,'final_singular_scope_sentence_retained':newstep.endswith('For a singular support the identical root cover retains its singularities and the kernel $N^*\\otimes\\mathcal J^{-1}$; the present proof does not erase that term in Remark~7.4.\n'),'revision_numbered_to_preserve_generator_output':True,'mathematical_statement_changed':False,'status_changed':False,'full_current_proof_gate_closed':False,'frozen_derivation':'analysis/continuation_II_ledger/A3_4_before_read_receipt.json','replacement_scope':'Finite smooth-cover graded-factor parameter family, actual Green-operator kernel map and minors; the previous unsupported inference from upper semicontinuity alone is expanded. The full root-cover route is not retroactively credited.','revert':'python code/continuation_II_ledger/install_A3_4_Step5.py --revert with exact after-hash guards.'}
rec.write_text(json.dumps(x,indent=2)+'\n');print(json.dumps({'installed_at':x['installed_at'],'current_proof_sha256':x['current_proof_sha256_without_trailing_newline'],'steps1_through4_preserved':True,'full_gate_closed':False,'receipt_sha256':h(rec)}))
