#!/usr/bin/env python3
"""Reversible administrative roles/credit update; no proof status promotion."""
from pathlib import Path
import csv,json,hashlib,datetime
csv.field_size_limit(16*1024*1024)
ROOT=Path(__file__).resolve().parents[2];A=ROOT/'analysis/continuation_IV'
inventory=ROOT/'S6_10_PAPERS_inventory.csv'
with inventory.open() as f:r=csv.DictReader(f);fields=r.fieldnames;rows=list(r)
targets={f'night:P3K.{i}' for i in range(109,120)}
receipt=A/'new_main_credit_patch.json'
if not receipt.exists():
 receipt.write_text(json.dumps({'applied_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'reason':'The eleven new substantial endpoint/classification/return statements are main rows; preserve the receiving proof and computation gates explicitly.',
 'before_inventory_sha256':hashlib.sha256(inventory.read_bytes()).hexdigest(),
 'prior_fields':[{k:r[k] for k in ['label','main_or_supporting','credited_to','notes']} for r in rows if r['label'] in targets]},ensure_ascii=False,indent=2)+'\n')
common='S6_06_BLIND source; renewed19November2026 bounded credit comparison: original AC26 PDF pp25--26,82--83; Engel Initial construction/Lemma2.1 and Additional remarks; DGKXv1 exact-period/intrinsic-fibration/full-automorphism loci; DGKXv2 relative construction. Positive antecedents and each row exact searched claim are in analysis/continuation_IV/renewed_credit_comparison.md, with49-source hash/query log renewed_credit_searches.json. The exact new statement was not located in those declared searches; no global novelty or priority claim.'
for row in rows:
 if row['label'] not in targets:continue
 row['main_or_supporting']='main';row['credited_to']=common
 notes=json.loads(row['notes']);notes['continuation_credit_receipt']='analysis/continuation_IV/renewed_credit_comparison.md';notes['continuation_main_role_receipt']='analysis/continuation_IV/new_main_credit_patch.json'
 row['notes']=json.dumps(notes,ensure_ascii=False)
with inventory.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
gate_path=A/'completed_row_gates.json'
gates=json.loads(gate_path.read_text()) if gate_path.exists() else {}
for lab in sorted(targets):
 gates.setdefault(lab,{})['renewed_main_result_credit_check']='complete at the declared bounded-search scope: fresh original AC26 PDF/E26/DGKXv1/v2 and all attached TeX source queries; positive source antecedents and exact row-specific comparison in analysis/continuation_IV/renewed_credit_comparison.md, full hashes/hits renewed_credit_searches.json. No proof promotion or unqualified novelty claim.'
gate_path.write_text(json.dumps(gates,indent=2)+'\n')
events=ROOT/'records/continuation_IV_events.tsv'
with events.open() as f:r=csv.DictReader(f,delimiter='\t');ef=r.fieldnames;ers=list(r)
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation'
new=[]
for lab in sorted(targets):
 new.append(dict(statement_id=lab,date='2026-11-19',who=who,type='used and rechecked in this run',outcome='Administrative inventory role reconciliation: substantive new cp36 endpoint/classification/return statement designated main; previous supporting intake default retained in analysis/continuation_IV/new_main_credit_patch.json. Receiving mathematical status remains open, with separate proof/computation gates. This is metadata reconciliation only; no new mathematical check.'))
 new.append(dict(statement_id=lab,date='2026-11-19',who=who,type='used and rechecked in this run',outcome='Renewed row-specific credit comparison: searched49 supplied primary source texts with exact row/query mapping, including original AC26 PDF, Engel, DGKXv1 andv2 and other attached TeX papers. Opened positive source construction, scalar-action, height, intrinsic-fibration and endpoint antecedents; did not locate the exact new row statement in the declared searches. Full comparison and exact III generic-source morphism: analysis/continuation_IV/renewed_credit_comparison.md; fresh hashes and1813 source-term searches: renewed_credit_searches.json. Bounded search conclusion only; no global priority claim and no proof gate promotion.'))
new.append(dict(statement_id='night:P3K.115',date='2026-11-19',who=who,type='computation or formal certificate',outcome='Fresh independent complete-prism solver code/continuation_IV/scalar_fan_new_solver.py, without reading producing code, solves10 equations in9 variables by exact rational Gaussian elimination. ForM6/M2 profiles, seeds-3 through4 and every word starting0 of lengths1--6:1008 family-path records,15408 target solves,154080 equations pass; l=1,2,3 verifies affine coefficients and M2 homogeneity; exact vertical unit witnesses cover every M6 l mod7. Complete paths and outputs under analysis/continuation_IV/scalar_fan_new_solver*. No finite enumeration claim for unexamined geometric families or whole-row gate.'))
new.append(dict(statement_id='night:P3K.114',date='2026-11-19',who=who,type='computation or formal certificate',outcome='Fresh7-check exact program code/continuation_IV/Engel_III_source_map.py verifies the invertible base/source morphism s=4/(27t+4), X=(3s/sqrt2)^2*x, Y=(3s/sqrt2)^3*y between the generic III equation and Engel original Initial construction model, including marked G image and j=1728s. All residuals zero, output analysis/continuation_IV/Engel_III_source_map.output.json. Generic-source comparison only; completed cap/endpoint maps require their separate proof.'))
keys={tuple(e[k] for k in ef) for e in ers}
for e in new:
 if tuple(e[k] for k in ef) not in keys:ers.append(e)
with events.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=ef,delimiter='\t');w.writeheader();w.writerows(ers)
print(json.dumps({'main_rows':len(targets),'credit_gates':len(gates),'IV_events':len(ers)}))
