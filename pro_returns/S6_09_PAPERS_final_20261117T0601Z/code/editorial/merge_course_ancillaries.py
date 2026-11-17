"""Add ten independently read course prerequisites without replacing run rows."""
from pathlib import Path
import csv,json,re

OUT=Path(__file__).resolve().parents[2]
path=OUT/'S6_09_PAPERS_inventory.csv'
with path.open() as f:
    rd=csv.DictReader(f); fields=rd.fieldnames; rows=list(rd)
index={(r['source_run'],r['source_id']):r for r in rows}
source=OUT/'work/maps_audit/paperI_course_ancillary_inventory.json'
items=json.loads(source.read_text())
paper=(OUT/'S6_09_PAPERS_I.tex').read_text()
manifest=[]
for item in items:
    key=(item['source_run'],item['source_id'])
    row=index.get(key,{k:'' for k in fields})
    for k in fields:
        if k in item: row[k]=item[k]
    label=item['printed_label']; pos=paper.index('\\label{'+label+'}')
    starts=list(re.finditer(r'\\begin\{(theorem|lemma|corollary|proposition|example|remark|exercise)\}',paper[:pos]))
    if starts:
        m=starts[-1]; end=paper.find('\\end{'+m[1]+'}',pos)
        if end>=0 and '\\end{'+m[1]+'}' not in paper[m.end():pos]:
            row['statement_as_printed']=paper[m.start():end+len('\\end{'+m[1]+'}')]
    if not row['statement_as_printed']:
        tail=paper[pos:]; stop=re.search(r'\\begin\{proof\}|\n\\(?:sub)*section|\n\\paragraph',tail)
        row['statement_as_printed']=tail[:stop.start() if stop else 2500]
    row['wording_vs_source']='Complete classical provider argument retained; TeX conversion and label normalization only. Exact receiving-source ranges and provenance are in paperI_course_foundations_manifest.json. No new mathematical result is claimed.'
    row['recorded_checks']=item['recorded_checks']+' Exact producer dates and the undated original homotopy-fibres header remain distinct in the foundations manifest.'
    row['your_check']='GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026: '+item['your_check']+' Full proof scope: '+str(item['full_proof_source_lines'])+' in '+item['source_file']+'.'
    for k in ['found_in_AC26','found_in_E26','found_in_DGKX_v1']:
        row[k]='Classical prerequisite or worked teaching example, not claimed new and not attributed to this construction paper. Its complete receiving proof is printed and independently read; no result-specific negative literature-absence assertion is made.'
    if 'CW-THEOREM' in item['source_id']:
        row['found_elsewhere']='Known: Hatcher, Algebraic Topology (2002), Theorem 4.32, pp.366–367, original statement and proof opened; connected CW type and first nonzero integral degree matched. The complete receiving-source rederivation is printed.'
    elif 'PF-THEOREM' in item['source_id']:
        row['found_elsewhere']='Known: Hatcher, Algebraic Topology (2002), Corollary 4.33, pp.367–368, original statement and proof opened; simply connected CW type and integral homology equivalence matched. The complete actual-map path-fibre proof is printed.'
    else:
        row['found_elsewhere']='Classical singular-chain argument or its worked consequence, fully proved here; no novelty assertion. Hatcher Theorem 4.32 and Corollary 4.33 are used only for the homotopy principles they state, not as locators for this separate chain calculation.'
    row['notes']='Added prerequisite row; preserves all initial 928 inventory rows. Source SHA256 '+item['source_sha256']+'; audit work/maps_audit/paperI_course_foundations_manifest.json; portable finite checkers supplement, and do not replace, the full proofs.'
    if key not in index:
        rows.append(row);index[key]=row
    manifest.append({'source_id':key[1],'printed_label':label,'source_sha256':item['source_sha256']})
assert len(fields)==17 and len(rows)>=938 and len(index)==len(rows)
with path.open('w',newline='') as f:
    wr=csv.DictWriter(f,fields);wr.writeheader();wr.writerows(rows)
(OUT/'records/course_inventory_additions.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Preserved 928 original rows; added 10 course prerequisites; total',len(rows))
