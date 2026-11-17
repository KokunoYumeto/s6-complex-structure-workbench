"""Merge explicit per-result source comparisons without widening their scope."""
from pathlib import Path
import csv,json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'deliverables'
p=OUT/'S6_09_PAPERS_inventory.csv'
with p.open(newline='') as f:
    reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
index={(r['source_run'],r['source_id']):r for r in rows}
names={'AC2026':'Claude and Alpöge, AC26','AC26':'Claude and Alpöge, AC26',
       'Engel2026':'Engel','DuEtAl2026v1':'Du, Guo, Kusakabe and Xie, version 1'}
cols=['found_in_AC26','found_in_E26','found_in_DGKX_v1','found_elsewhere']
merged=[]
def target(x):
    r=index.get((x.get('source_run'),x['source_id']))
    if r is not None:return r
    found=[r for r in rows if r['source_id']==x['source_id'] and not r['source_run'].startswith('S6_')]
    if len(found)!=1:raise ValueError(('ambiguous row',x.get('source_run'),x['source_id']))
    return found[0]
for rel in ['work/invariants_arithmetic/credit_comparison.json',
            'work/maps_audit/credit_comparison_I.json',
            'work/cdp_audit/paperI_transfer_credit_audit.json',
            'work/root/cdp_reserved_credit_comparison.json',
            'work/cdp_audit/credit_comparison_239.json',
            'work/root/II_push_E5_credit_comparison.json']:
    path=OUT/rel
    if not path.exists():continue
    data=json.loads(path.read_text())
    if isinstance(data,dict):data=data.get('rows',data.get('results',data.get('comparisons',[])))
    for x in data:
        r=target(x);credits=[]
        if 'credit_outcomes' in x:
            mapping={'AC26':'found_in_AC26','E26':'found_in_E26',
                     'DGKX2026v1':'found_in_DGKX_v1','elsewhere':'found_elsewhere'}
            for src,col in mapping.items():
                r[col]=json.dumps({'outcome':x['credit_outcomes'][src],
                                   'search':x.get('searches',{}).get(src),
                                   'reader':x.get('reader'),
                                   'record':rel},ensure_ascii=False)
            if x['source_id']=='E9':credits=['Du, Guo, Kusakabe and Xie, version 1, Theorem6.12 and Proposition6.16; re-derived after reading that version.']
            elif 'semidirect' in x['source_id']:
                credits=['Claude and Alpöge, AC26, section10.5, Lemma10.7, p.90; full quotient proof re-derived in independent wording.']
                r['kind']='Cited/re-derived'
            else:credits=['AC26 supplies the monodromy matrices; the index-twelve kernel computation is shared with FAM F1.1. No exhaustive absence claim is made.']
        else:
            for col in cols:
                d=x.get(col)
                if d is None:raise ValueError((rel,x['source_id'],'missing',col))
                r[col]=d if isinstance(d,str) else json.dumps(d,ensure_ascii=False)
                if not isinstance(d,dict) or d.get('status') not in {'found','found_in_checked_scope'}:continue
                matches=d.get('matches',[d])
                for m in matches:
                    key=m.get('citation_key','');loc=m.get('locator','')
                    role='Known conclusion' if m.get('full_statement_found') else 'Antecedent/input'
                    if m.get('kind')=='correction_of_source_claim':role='Statement corrected'
                    credits.append(role+': '+names.get(key,key)+', '+loc+'. '+m.get('relation',''))
            if x.get('credited_to'):credits=[x['credited_to']]
        if credits:r['credited_to']=' | '.join(dict.fromkeys(credits))
        else:r['credited_to']='No full matching conclusion found in the explicitly checked scopes. All known construction inputs and operative external theorems are cited at their points of use; no exhaustive novelty claim.'
        note='Explicit source comparison: '+rel
        if note not in r['notes']:r['notes']+=' | '+note
        merged.append({'source_run':r['source_run'],'source_id':r['source_id'],'record':rel})

# Course aliases are checked against the full independent proof blocks.
course=OUT/'work/maps_audit/paperI_course_homology_concordance.json'
if course.exists():
    x=json.loads(course.read_text());r=target(x)
    r['paper']='I';r['printed_label']=x['printed_label'];r['kind']='Theorem (shared integral homology statement)'
    r['your_check']='GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, 17 November 2026: '+x['your_check']
    r['check_outcome']=x['check_outcome']
    r['notes']+=' | Exact source-to-print steps in work/maps_audit/paperI_course_homology_concordance.json'
r=index.get(('course_CG-S6','CG-S6-07-HOMOTOPY'))
if r and (OUT/'work/maps_audit/paperI_course_homotopy.tex').exists():
    r['paper']='I';r['printed_label']='mapsI:course:CG-S6-07-HOMOTOPY';r['kind']='Theorem with a distinct retained proof'
    r['your_check']='GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, 17 November 2026: complete original degree-one/path-fibration proof read and rederived, including chain, CW/Hurewicz, path-fibration and integral Serre prerequisites. Both inverse homotopies are retained. Full selected proof ranges and hashes are in paperI_course_foundations_manifest.json. Independent checker reruns passed 34/34 and 38/38.'
    r['check_outcome']='Passed full proof and source-hypothesis checks; complete four-block proof printed.'
for r in rows:
    if r['source_run']=='course_CG-S6' and r['paper']=='I' and not r['recorded_checks']:
        r['recorded_checks']='The course records author self-checks by GPT-6 Astra (OpenAI), Codex reasoning effort ultra, October2026. They are provenance, not an independent check; the complete independent current reading is recorded separately.'
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
(OUT/'records/credit_matrix_merge.json').write_text(json.dumps(merged,indent=2)+'\n')
print('Explicit credit rows merged:',len(merged))
