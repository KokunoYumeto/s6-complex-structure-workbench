"""Record actual scoped audits. Never infer a proof check from a producer label."""
from pathlib import Path
import json,csv,re
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'deliverables'
p=OUT/'S6_09_PAPERS_inventory.csv'
with p.open(newline='') as f:r=csv.DictReader(f);fields=r.fieldnames;rows=list(r)
review=(ROOT/'sources/reviews/S6_02_REVIEW_FABLE/REVIEW.md').read_text()
family={m[1]:(m[2],m[3]) for m in re.finditer(r'^\| ([A-F]\.\d+\.\d+) \| [^|]+ \| ([^|]+) \| (.+) \|$',review,re.M)}
read_ids=[]
for prefix,n in [('A.1',2),('A.2',5),('A.3',3),('A.4',9),('B.1',2),('B.2',3),('B.3',8)]:
    read_ids += [f'{prefix}.{i}' for i in range(1,n+1)]
read_ids += [f'B.4.{i}' for i in range(1,34)]+['B.5.1']
read_ids += [f'E.2.{i}' for i in range(4,25)]
for prefix,n in [('D.1',3),('D.2',4),('D.3',2),('D.4',8),
                 ('E.1',3),('E.2',3),('E.3',3),('E.4',3)]:
    read_ids += [f'{prefix}.{i}' for i in range(1,n+1)]
root_audits=[]
for row in rows:
    sid=row['source_id'];run=row['source_run']
    if run=='S6_02_FAMILY' and sid in family:
        verdict,step=family[sid]
        row['recorded_checks']='reviews/S6_02_REVIEW_FABLE/REVIEW.md §3, row '+sid+': Claude Fable 5.2 (Anthropic), effort high, 12–13 November 2026. Verdict '+verdict.strip()+'. Checked step: '+step
        row['your_check']='GPT-6 Astra (OpenAI, ChatGPT Pro mode), 17 November 2026: recorded per-result check opened; complete source proof retained in candidate; label/heading changes recorded in work/root/I_assembly_changes.json; exact computation reruns in code/family and independent Arb rerun in code/push. Final notation and source-to-print comparison in progress.'
        row['check_outcome']='Recorded '+verdict.strip()+'; current editorial audit in progress.'
        if row['paper']=='I':row['printed_label']='fam:src:'+sid+' (candidate; final theorem number pending)'
        if sid=='B.3.1':row['notes']+=' | Recorded dictionary gap is addressed by PUSH E.1.1–E.1.3; preserve original arithmetic and full added dictionary.'
        if sid in ['C.3.3','E.1.5','E.2.3']:
            row['notes']+=' | Historical open formulation retained with its proved reductions and later answer; do not relabel the historical check as a failure to read.'
    if run=='S6_02_PUSH' and sid in read_ids:
        row['your_check']='GPT-6 Astra (OpenAI, ChatGPT Pro mode), 17 November 2026: complete argument read step by step and rederived; exact computations rerun where used. Detailed scopes: work/root/proof_audit.md and work/root/root_result_audit.json. Cited-statement verification and final source-to-print comparison are separately tracked and not inferred from the producer status.'
        row['check_outcome']='Mathematical argument passed current reading; exact literature dependencies and final editorial comparison in progress.'
        if row['paper']=='I':row['printed_label']='push:src:'+sid+' (candidate; final theorem number pending)'
        root_audits.append({'source_run':run,'source_id':sid,'state':row['check_outcome'],'check':row['your_check']})
with p.open('w',newline='') as f:w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
(OUT/'work/root/root_result_audit.json').write_text(json.dumps(root_audits,ensure_ascii=False,indent=2)+'\n')
print('Preserved FAMILY checks',len(family),'and current complete PUSH readings',len(root_audits),'in',len(rows),'inventory rows.')
