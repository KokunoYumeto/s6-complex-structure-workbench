from pathlib import Path
from datetime import datetime, timezone
import csv, json, hashlib
ROOT=Path(__file__).resolve().parents[2]; A=ROOT/'analysis/continuation_V'
label='maps:src:F.2.37'
uses=r'\cref{maps:src:F.2.2}; \cref{maps:src:F.2.36}; \cref{maps:src:F.2.38}; \cref{maps:src:F.2.16}; the explicit affine lift and marked identity-slot maps displayed here'
changes=[]
for rel in ['papers/V/body.tex','papers/V/body_source.tex','S6_10_PAPERS_V.tex']:
 p=ROOT/rel; text=p.read_text(); start=text.index('\\StatementRecord{'+label+'}'); args=[]; j=start+len('\\StatementRecord')
 for _ in range(4):
  assert text[j]=='{'; depth=1; end=j+1
  while depth:
   if text[end]=='{':depth+=1
   elif text[end]=='}':depth-=1
   end+=1
  args.append((j+1,end-1,text[j+1:end-1])); j=end
 lo,hi,prior=args[3]; text=text[:lo]+uses+text[hi:]; p.write_text(text)
 changes.append({'path':rel,'old_uses':prior,'new_uses':uses})
proof='complete: exact six-item current proof is covered by the V before-read canonical-height/decision/witness/trace derivation and root before-read free-lift/identity-deletion derivation, with exact installed comparison in analysis/continuation_V/F2_37_current_union_comparison.md and both replacement receipts. Current proof SHA8950e1df488c54538d35d321afd3266e07bf2424252cb62e0abbbb0fff1752c1. F2.2 is a cited known input for the finite-order list; removed former routes are preserved and receive no retrospective prereading credit.'
compute='complete: root F2_37_auxiliary_fresh.py passes1348 exact pretarget checks; shared independent basic_algebra.py recomputes the finite-order list; VI F2_16_family_fresh.py independently verifies the actual word trace and consecutive difference among551 checks; involutions_and_period_lines.py recomputes all56 special normal forms. The finite candidate count is proved explicitly, with no runtime or arbitrary-input execution claim. Exact code locations and convention maps in F2_37_current_union_comparison.md.'
credit='complete: supporting-row exact source/dependency renewal in analysis/continuation_V/F2_37_current_union_comparison.md. Positive Bley–Hofmann–Johnston primary locators are retained through the actual F2.36 decision-and-witness input, with F2.2,F2.38,F2.16 supplying the stated lists and family. No repeated MAIN search applies, and dependency proof gates are not inferred.'
p=A/'completed_row_gates.json'; gates=json.loads(p.read_text()); assert label not in gates; gates[label]={'proof_rederivation_before_reading':proof,'new_independent_computations':compute,'renewed_main_result_credit_check':credit}; p.write_text(json.dumps(gates,indent=2)+'\n')
p=A/'printed_scope_overrides.json'; scopes=json.loads(p.read_text()); scopes[label]={'date':'2026-11-19','scope_tex':'Every step of the current proof has renewed prereading coverage: the canonical enumeration and actual conjugator argument by the Paper V reviewer, and the free affine lift and marked identity-slot maps by the root reviewer. The finite-order list is the already checked in-paper input. Newly authored exact programs verify the auxiliary computations and the actual word trace; the source and dependency scope was renewed. Former routes are preserved without retrospective prereading credit.','basis':'analysis/continuation_V/F2_37_current_union_comparison.md; F2_37_replacement_receipt.json; analysis/continuation_root/F2_37_auxiliary_installation_receipt.json'}; p.write_text(json.dumps(scopes,indent=2)+'\n')
p=ROOT/'records/continuation_V_events.tsv'
with p.open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation'
for typ,outcome in [('targeted proof check',proof),('computation or formal certificate',compute),('used and rechecked in this run',credit)]:rows.append({'statement_id':label,'date':'2026-11-19','who':who,'type':typ,'outcome':outcome})
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(rows)
with (A/'inventory_F2_37_updates.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['label','uses','credited_to','evidence'],delimiter='\t');w.writeheader();w.writerow({'label':label,'uses':uses,'credited_to':credit,'evidence':'analysis/continuation_V/F2_37_current_union_comparison.md'})
(A/'F2_37_registration_receipt.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'label':label,'events':len(rows),'uses_changes':changes,'gate_file_sha256':hashlib.sha256((A/'completed_row_gates.json').read_bytes()).hexdigest()},indent=2)+'\n')
print(json.dumps({'status':'complete','events':len(rows)}))
