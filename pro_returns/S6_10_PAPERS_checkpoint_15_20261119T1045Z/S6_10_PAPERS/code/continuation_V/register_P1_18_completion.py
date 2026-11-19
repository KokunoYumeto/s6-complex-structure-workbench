from pathlib import Path
from datetime import datetime, timezone
import csv,json,hashlib
ROOT=Path(__file__).resolve().parents[2]; A=ROOT/'analysis/continuation_V'
label='night:P1.18'; sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
required=[
 'analysis/continuation_root/P1_18_installed_geometric_comparison.json',
 'analysis/continuation_VI/P1_18_installed_analytic_comparison_receipt.json',
 'analysis/continuation_V_ledger/P1_18_polynomial_majorant_comparison_receipt.json',
 'analysis/continuation_V_ledger/P1_18_anchor_gauge_comparison_receipt.json',
]
for rel in required: assert (ROOT/rel).exists(),rel
proof='complete: every current retained proof step is covered by root geometric/global/splitting prereading derivation (09:34:01), VI complete analytic-certificate prereading derivation (09:57:19), and ledger isolated pretarget polynomial-majorant and right-ODE anchor/gauge derivations. Every installed scope was compared in the exact receipts listed in analysis/continuation_V/P1_18_current_union_comparison.md. Current proof SHA83f64e2a793a92aa2ca9d6c664c3ac311803d401611eb56dca3d4e923f318be1; full old proof is preserved. This is a complete union of scoped prereading checks, not a single-reviewer whole-proof claim.'
compute='complete: newly authored owner period/root/Hessian/cusp/collar programs cover the full110-digit computation with1203+592+10780+336=12911 leaves, no holes,18 actual central inverse checks, and the normalized constant/splitting. The persisted precise-endpoint replay verifies all12911 strict predicates, four exact rational lower bounds and both printed infinity bounds; its earlier coarse-string failure remains preserved. VI independent713-check256-bit program verifies all recurrences/actual matrix maps on recorded representative domains; root14 exact checks verify marked symmetry/cusp maps. A separately authored second period method agrees beyond89digits. Exact current hashes and domains are retained in the aggregate receipt; no original producing program is used as the new-code witness.'
credit='complete: renewed MAIN comparison at the exact normalized Frobenius minimum, parameter boundary and full complex splitting scope is retained in renewed_credit_searches.json and renewed_credit_comparison.md. Current supplemental source comparison in P1_18_current_union_comparison.md credits the opened primary Teschl Lemma2.7pp42–43 and DLMF§1.9(iii)(1.9.30–31), with root exact source receipt. Bounded nonlocation is not a priority claim; positive construction/known-input credits and actual maps are retained.'
p=A/'completed_row_gates.json'; gates=json.loads(p.read_text()); prior=gates[label].copy(); gates[label]={'proof_rederivation_before_reading':proof,'new_independent_computations':compute,'renewed_main_result_credit_check':credit};p.write_text(json.dumps(gates,indent=2)+'\n')
p=A/'printed_scope_overrides.json'; scopes=json.loads(p.read_text());scopes[label]={'date':'2026-11-19','scope_tex':'Every step of the current seven-step proof has renewed prereading coverage through the root geometric derivation, the Paper VI analytic derivation, and two isolated ledger derivations for the actual polynomial-bound and anchor maps. Each installed scope was compared after its derivation was frozen. Independently authored programs verify the complete 12911-leaf domain certificate, central inverse and Hessian, exact symmetry and cusp maps; a separate period method verifies the normalized constants. The renewed main-result and primary-input credit comparison is recorded. The full former proof is preserved without retrospective prereading credit.','basis':'analysis/continuation_V/P1_18_current_union_comparison.md; P1_18_replacement_receipt.json; P1_18_registration_receipt.json'};p.write_text(json.dumps(scopes,indent=2)+'\n')
uses=r'\cref{night:P1.15}; the rational connection and root-gauge definitions displayed in \cref{night:P1.16}; \cref{night:P1.8}; \cite[Lemma~2.7, pp.~42--43]{TeschlODE2012}; \cite[\S1.9(iii), (1.9.30)--(1.9.31)]{DLMFCauchy2026}'
use_changes=[]
for rel in ['papers/V/body.tex','papers/V/body_source.tex','S6_10_PAPERS_V.tex']:
 p=ROOT/rel;text=p.read_text();j=text.index('\\StatementRecord{'+label+'}')+len('\\StatementRecord');args=[]
 for _ in range(4):
  assert text[j]=='{';depth=1;e=j+1
  while depth:
   if text[e]=='{':depth+=1
   elif text[e]=='}':depth-=1
   e+=1
  args.append((j+1,e-1,text[j+1:e-1]));j=e
 lo,hi,old=args[3];p.write_text(text[:lo]+uses+text[hi:]);use_changes.append({'path':rel,'old_uses':old,'new_uses':uses})
p=ROOT/'records/continuation_V_events.tsv'
with p.open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation'
for typ,outcome in [('targeted proof check',proof),('computation or formal certificate',compute),('used and rechecked in this run',credit)]:rows.append({'statement_id':label,'date':'2026-11-19','who':who,'type':typ,'outcome':outcome})
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(rows)
with (A/'inventory_P1_18_updates.tsv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=['label','uses','credited_to','evidence'],delimiter='\t');w.writeheader();w.writerow({'label':label,'uses':uses,'credited_to':credit,'evidence':'analysis/continuation_V/P1_18_current_union_comparison.md'})
# Root explicitly requested these exact owner overrides in the root mapping.
rp=ROOT/'analysis/continuation_root/printed_scope_overrides.json'; before=rp.read_bytes();mapping=json.loads(before); preserved=A/'root_scope_before_P1_18_F2_13_F2_37_merge.json';assert not preserved.exists();preserved.write_bytes(before)
oldroot={}
for lab in ['maps:src:F.2.13','maps:src:F.2.37',label]:oldroot[lab]=mapping.get(lab);mapping[lab]=scopes[lab]
rp.write_text(json.dumps(mapping,indent=2)+'\n')
evidence=required+[
 'analysis/continuation_V/P1_18_replacement_receipt.json',
 'analysis/continuation_root/P1_18_before_read.md',
 'analysis/continuation_VI/P1_18_analytic_certificates_before_read.md',
 'analysis/continuation_V_ledger/P1_18_anchor_gauge_before_read.md',
 'analysis/continuation_V_ledger/P1_18_polynomial_majorant_before_read.md',
 'code/continuation_V/minimum_precise_endpoint_summary.py',
 'code/continuation_V/minimum_precise_endpoint_summary.json',
 'code/continuation_V/minimum_certificate_renewal.json',
 'code/continuation_V/central_real_system_fresh.output.json',
 'code/continuation_VI/P1_18_analytic_certificates_fresh.output.json',
 'analysis/continuation_root/P1_18_exact_symmetry_fresh.output.json',
 'analysis/continuation_root/P1_18_analytic_primary_sources.json',
]
receipt={'utc':datetime.now(timezone.utc).isoformat(),'status':'complete current proof/computation/source union','label':label,'events':len(rows),'prior_owner_fields':prior,'uses_changes':use_changes,'evidence_sha256':{r:sha(ROOT/r) for r in evidence},'root_scope_merge':{'prior_sha256':hashlib.sha256(before).hexdigest(),'preserved_path':str(preserved.relative_to(ROOT)),'prior_values':oldroot,'current_sha256':sha(rp)}}
(A/'P1_18_registration_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':receipt['status'],'events':len(rows),'root_scopes_added':list(oldroot)}))
