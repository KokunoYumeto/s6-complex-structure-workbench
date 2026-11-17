#!/usr/bin/env python3
"""Per-result, explicitly scoped comparison with the original baseline sources.

Search hits are an index to the actually read source statements, not an
independent novelty argument. A negative field means no exact statement was
found in this declared comparison; it does not claim absence everywhere.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import unicodedata

ROOT=Path(__file__).resolve().parents[3]
WORK=ROOT/'deliverables/work/invariants_arithmetic'
rows=json.loads((WORK/'maps_D_independent_audit.json').read_text())
credit={r['citation_key']:r for r in json.loads((WORK/'source_credit_map.json').read_text())}
refs={r['citation_key']:r for r in json.loads((WORK/'maps_D_references_verified.json').read_text())}
meta={'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17 UTC'}

specs={}
for short,key in [('AC26','AC2026'),('E26','Engel2026'),('DGKX_v1','DuEtAl2026v1'),('DGKX_v2','DuEtAl2026v2')]:
    r=credit[key]
    specs[short]={k:r[k] for k in ['local_source','source_sha256','opened_locator']}
    specs[short]['citation_key']=key
    specs[short]['index_source']='sources/audit_cache/inv_ari/AC26_text.txt' if short=='AC26' else r['local_source']
specs['AC26']['opened_locator']+=' MAPS-specific opening: original Theorems7.17 and7.22, printed pp57 and60; the normalized cusp and marked local constructions in §§4–7. The PDF wins over transcription.'
specs['E26']['opened_locator']+=' MAPS-specific opening: Lemma2.1/Corollary2.2 lines335–403; Remark8.1 lines1645–1681 and Remark8.5 lines1738–1759, including the stated broader construction and explicitly open manifold range.'
specs['DGKX_v1']['opened_locator']+=' MAPS-specific opening: conic-band small-resolution charts and contraction lines3060–3125; Proposition local-conifold-curve and full proof lines8483–8510. These are local geometry, not the global smoothing/smooth-type result.'
for key in ['manViaclovskyLogs26','manViaclovskyTwo26','manWang26','manLR26','manYang26']:
    r=refs[key]
    specs[key]={k:r[k] for k in ['local_source','source_sha256','opened_locator']}
    specs[key].update(citation_key=key,index_source=r['local_source'])

vocab={
 'cover':['universal cover','cyclic cover','Euler','Betti','connected sum','deck','torsion','homology'],
 'ring':['cup','cubic','Chern','Pontryagin','torsion','component','cover'],
 'smooth':['Zhubr','spin','bordism','surgery','diffeomorph','classification','refined','fundamental class'],
 'catalogue':['Mordell','narrow','profile','configuration','clutch','sphere','filling','height'],
 'log':['logarithmic','multiplicit','finite','twist','Mayer','homology','Seifert','cusp'],
 'original':['original','additive','star','component','Chern','mapping torus','boundary','narrow'],
 'weighted':['weight','iterate','linearization','correction','bar','normal','homology','height'],
 'cusp':['normalization','cusp','triangular','period lattice','component','intersection','torsion'],
 'conifold':['conifold','smoothing','small resolution','flat','proper','S^3','canonical','algebraic dimension'],
}
topic={
 **{f'D.1.{n}':('cover' if n<=4 or n==7 or n==12 else 'ring' if n in [5,6,8,9] else 'smooth') for n in range(1,13)},
 **{f'D.2.{n}':'catalogue' for n in [1,2,3,4,19,22,23,24,25,26,27,28]},
 **{f'D.2.{n}':'log' for n in [5,6,7,9,10,11,12,13,15,21,29,30]},
 **{f'D.2.{n}':'smooth' for n in [8,14,35,36,38,39,42,44,45,48]},
 **{f'D.2.{n}':'original' for n in [16,17,18,20,31,32,33,49,51]},
 **{f'D.2.{n}':'weighted' for n in [34,37,40,41,46,50,52]},
 **{f'D.2.{n}':'cusp' for n in [43,47,53]},
 **{f'D.3.{n}':'conifold' for n in range(1,5)},
}
assert set(topic)=={r['source_id'] for r in rows}

def fold(s):
    s=unicodedata.normalize('NFKD',s).casefold()
    s=''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[\\{}"\'`~-]','',s)
indices={k:(ROOT/v['index_source']).read_text(errors='replace').splitlines() for k,v in specs.items()}
folded={k:list(map(fold,lines)) for k,lines in indices.items()}
logs=[]
def search(sid,key):
    terms=vocab[topic[sid]]
    termrows=[]
    for term in terms:
        found=[i+1 for i,line in enumerate(folded[key]) if fold(term) in line]
        termrows.append({'term':term,'count':len(found),'line_numbers':found})
    rec={'source_id':sid,'source':key,'index_source':specs[key]['index_source'],'terms':termrows}
    logs.append(rec)
    return {'search_log':'work/invariants_arithmetic/maps_D_credit_search_log.json',
            'record_key':sid+'|'+key,'terms_searched':terms,
            'hit_counts':{x['term']:x['count'] for x in termrows}}

matches={}
def put(ids,baseline,locator,relation,kind='construction_input_only',full=False):
    for sid in ids:
        matches[(sid,baseline)]={'locator':locator,'relation':relation,'kind':kind,'full_statement_found':full}

put([f'D.1.{n}' for n in range(1,13)],'AC26',
    'Original Theorems7.17 and7.22, pp57 and60; normalized cusp and marked local maps §§4–7.',
    'The admissible quotient family, cyclic fundamental group and integral quotient homology are prior input. The universal-cover ring, full Zhubr data and canonical free-action classification are not the statements of these theorems.')
put(['D.1.5','D.1.8'],'AC26','Proposition9.11 pp70–71 and Theorem9.1 pp64–65.',
    'The original canonical formula and original sphere Chern data are known. Integral vanishing after the nontrivial universal cover is an additional marked pullback calculation.')
put(['D.2.1','D.2.2','D.2.5','D.2.34','D.2.48'],'AC26','Theorems7.17,7.22 and8.1; original IV*,III,I1 family.',
    'The weight-one order-(3,4) family is a known original case. The wider catalogue, all positive weights, arbitrary orders and full smooth invariants are additional.',kind='original_case_only')
put(['D.2.3'],'AC26','Theorem7.22 and §8 Euler computation.',
    'Euler2 for the original one-vertex cusp is known. The general triangular V-vertex formula and the recorded clutch comparisons are a separate extension.',kind='original_case_only')
put(['D.2.20'],'AC26','§7 untwisted and twisted marked topology.',
    'The original configuration is a comparison case. The six original-filled profile families and their smooth classification are not the original theorem.',kind='original_case_only')
put(['D.2.43','D.2.47'],'AC26','§4 and §7.2, normalized dP6 cusp and its incidence maps.',
    'The one-vertex normalized toric cusp is earlier geometric input. The nonsaturated arbitrary-period kernel and every component cubic are not given there.',kind='original_case_only')
put(['D.3.3'],'AC26','Proposition9.11 and Proposition9.13, pp70–76.',
    'The canonical and structure-direct-image formulas on the original family are known. Their continuation through the moving-zero/conifold family is rederived here.',kind='original_case_only')

put([f'D.2.{n}' for n in range(1,54)],'E26','Remark8.5, S6.tex lines1738–1759; §§1–3 and §7 for the original construction.',
    'Engel explicitly gives the broader section-line/translation construction and asks which six-manifolds occur. This is construction credit and an earlier open programme; it is not an earlier proof of this row’s exact all-parameter topology or classification.',kind='earlier_programme_and_construction')
put(['D.2.34','D.2.48'],'E26','Lemma2.1/Corollary2.2 lines335–403; main theorem882–910; homology1617–1643; Remark8.5.',
    'The IV*,III,I1 section-line geometry and weight-one sphere are known. All-weight integral homology and complete oriented smooth classification are additional.',kind='original_case_only')
put(['D.1.1','D.1.3','D.1.4','D.1.11','D.1.12'],'E26','Main theorem882–910; integral homology1617–1643.',
    'The original sphere and quotient construction are known inputs. The nontrivial degree-d universal covers and their complete invariants are not supplied.',kind='original_case_only')
put(['D.3.1'],'E26','Remark8.1, lines1645–1681.',
    'The linearization-scale degeneration is posed as a conjecture. It is a different degeneration from the moving-zero conifold family; no proof of D3.1 is credited to this conjecture.',kind='related_distinct_question')

put(['D.3.1'],'DGKX_v1','Conic-band small-resolution charts lines3060–3125; local-conifold-curve proposition8483–8510.',
    'The standard two-chart small resolution and its local contraction are already explicit. The global moving-zero proper flat family and its smoothing are not these local statements.',kind='local_antecedent_only')
put(['D.3.3'],'DGKX_v1','§6 structure-direct-images and canonical-root formulas; §7 intrinsic fibration.',
    'Original-family logarithmic canonical/direct-image input is known. The smoothing formulas and algebraic-dimension assertion require the additional global family argument.',kind='original_case_only')
put(['D.1.7'],'DGKX_v1','Theorem1.4 lines335–344 and exact-period/classification section.',
    'The original-family exact period equivalence is prior input. The degree-d smooth quotient/cover classification and this discrete-twist comparison are additional.',kind='partial_antecedent')

elsewhere={
 'D.2.1':['manFukae02','manMiranda90','manExplorer26'],
 'D.2.2':['manExplorer26'], 'D.2.3':['manExplorer26'],
 'D.2.5':['manViaclovskyLogs26'], 'D.2.6':['manViaclovskyTwo26'],
 'D.2.7':['manWang26'], 'D.2.8':['manWang26','manZhubr75'],
 'D.2.9':['manLR26'], 'D.2.10':['manYang26'],
 'D.2.11':['manYang26','manLR26'], 'D.2.12':['manExplorer26'],
 'D.2.13':['manViaclovskyLogs26'],
 'D.2.14':['manGR25','manBarden65','manReiser24','manZhubr75'],
 'D.2.15':['manGR25'], 'D.2.16':['manGR25','manSS10','manUU21'],
 'D.2.19':['manSS10'], 'D.2.20':['manGR25'],
 'D.2.22':['manSS10'], 'D.2.25':['manGR25'],
 'D.2.26':['manUU21'], 'D.2.27':['manSS10'],
 'D.2.31':['manBarden65','manGR25','manUU21'],
 'D.2.35':['manWang26','manZhubr75'],
 'D.2.36':['manZhubr75'], 'D.2.38':['manZhubr75'],
 'D.2.39':['manZhubr75','ffThomas56'],
 'D.2.41':['manBrown82'], 'D.2.42':['manZhubr75','ffThomas56'],
 'D.2.44':['manZhubr75','ffZhubr13','ffBrown72','mapsKaplan79'],
 'D.2.45':['manZhubr75','ffZhubr13','mapsKaplan79'],
 'D.2.46':['manSS10'],
 'D.2.48':['manZhubr75','ffThomas56','mapsKaplan79','mapsWhitehead50'],
 'D.2.53':['ffThomas56'],
 'D.1.10':['manZhubr75'], 'D.1.11':['manZhubr75','manReiser24'],
 'D.3.2':['manKM63','BHS19'], 'D.3.4':['manCDP98'],
}
relations={
 'D.2.1':'Miranda supplies the allowable configurations and Fukae the default marked rational-surface lattices. The collision applet supplies tabulated marked data but no published geometric realization certificate. The new writing-stage provider proves the exact50/II and56/II marked realizations; this distinction is retained.',
 'D.2.2':'The finite table is the applet’s archived output. Its exact payloads and returned invariants are independently checked; the table is not credited as an independent proof of the unpublished local geometric comparisons.',
 'D.2.3':'The four finite clutch comparisons are existing archived applet results. The Euler calculation is derived in full in this proof.',
 'D.2.5':'Viaclovsky’s logarithmic construction and determinant-one sphere case are antecedents; the receiving arbitrary-determinant groups and degenerate case are a full new derivation.',
 'D.2.6':'The order-four III-star construction and its marked rank-one caps are already in Viaclovsky. The all4k topology is additional.',
 'D.2.7':'Wang already constructs the order-three member with H2=H3=Z/2. The all3k twists use the actual primitive(2,1) I2 cap and are independently computed here.',
 'D.2.8':'Wang Theorem7.1/AppendixB already identifies his original member by the mod2 cube and conic surgery. The receiving all-simply-connected-twist extension is additional; full classification is justified by the independently opened Zhubr source.',
 'D.2.9':'The original Liu–Rollenske monodromy, product-II cap and sphere case are known. The unrestricted finite order/twist computation is additional.',
 'D.2.10':'Yang Theorem7.13 contains exactly the two k=l=1 homology families. The arbitrary higher orders, invariant translation vectors and P=0 case are additional and proved integrally.',
 'D.2.11':'Yang’s Type-C modular and affine-period functions and LR’s product-II mechanism are known. The explicit3P realization and resulting cap/gluing computation are new receiving arguments.',
 'D.3.4':'CDP1998 Example2.3 p83 gives the earlier a=1 structures on S3xS3. The general-fibre topology comparison distinguishes the present displayed family and is proved here.',
}
output=[]
for row in rows:
    sid=row['source_id']; rec={'source_run':row['source_run'],'source_id':sid,
        'printed_label':row['printed_label'],'statement':row['source_title'],**meta}
    searches={key:search(sid,key) for key in specs}
    for baseline,field in [('AC26','found_in_AC26'),('E26','found_in_E26'),('DGKX_v1','found_in_DGKX_v1')]:
        spec=specs[baseline]; found=matches.get((sid,baseline))
        rec[field]={**spec,'search_scope':searches[baseline],
            'status':'found_antecedent' if found else 'not_found_in_scoped_comparison',
            'full_statement_found':False,
            'relation':'No exact statement of this row was found in the whole-source term search and the declared original-source readings. This is a scoped comparison, not a claim of global novelty.'}
        if found:rec[field].update(found)
    keys=elsewhere.get(sid,[])
    rec['found_elsewhere']={'status':'found_antecedent' if keys else 'not_found_in_scoped_comparison',
        'full_statement_found':False,'sources_checked':[
            {'citation_key':k,'opened_locator':refs[k]['opened_locator'],
             'local_source':refs[k].get('local_source'),'source_sha256':refs[k].get('source_sha256'),
             'scope':refs[k]['actual_use']} for k in keys],
        'additional_search_scope':[searches[k] for k in specs if k not in ['AC26','E26','DGKX_v1']],
        'relation':relations.get(sid,
             'The listed primary sources supply exact construction/classification/operation prerequisites at the stated locators. No earlier source was found containing this full marked all-parameter statement.' if keys else
             'No exact statement found in the six explicitly searched further sources; this does not claim a search of all literature. Earlier internal producing-run records are preserved separately as provenance, not external credit.')}
    if sid=='D.2.4':
        rec['credit_note']='This is the explicitly retained open-scope ledger, not a theorem or novelty claim.'
    if sid in ['D.2.51','D.2.52','D.2.53']:
        rec['credit_note']='Only the stated proved scope is compared; the expressly retained torsion-marking/refined-invariant questions are not promoted to theorems.'
    output.append(rec)

(WORK/'maps_D_credit_search_log.json').write_text(json.dumps(logs,indent=2,ensure_ascii=False)+'\n')
(WORK/'maps_D_credit_comparison.json').write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n')
with (WORK/'maps_D_credit_comparison.csv').open('w',newline='') as f:
    fields=['source_run','source_id','printed_label','statement','found_in_AC26','found_in_E26','found_in_DGKX_v1','found_elsewhere','checker','effort','date']
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for r in output:w.writerow({k:json.dumps(r[k],ensure_ascii=False) if isinstance(r[k],dict) else r[k] for k in fields})
print(json.dumps({'rows':len(output),'actual_source_searches':len(logs),'baseline_fields':4,'scope':'No worldwide novelty inference.'},indent=2))
