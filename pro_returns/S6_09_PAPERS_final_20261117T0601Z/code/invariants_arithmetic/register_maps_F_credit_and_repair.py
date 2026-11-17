#!/usr/bin/env python3
"""Persist bounded source comparisons and the independently reviewed provider row.

This reads the originals named in each search record.  A scoped negative result
does not assert absence from literature that was not searched.
"""
from pathlib import Path
import copy
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
D = ROOT / 'deliverables'
W = D / 'work/invariants_arithmetic'
META = dict(checker='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro', date='2026-11-17 UTC')

def read(name):
    return json.loads((W/name).read_text())

def save(name, obj):
    (W/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

paths = {r['source']:r['index_source'] for r in read('maps_D_credit_search_log.json')}
base = {r['citation_key']:r for r in read('source_credit_map.json')}
modern = {r['citation_key']:r for r in read('maps_D_references_verified.json')}
baseline_keys = {'AC26':'AC2026','E26':'Engel2026','DGKX_v1':'DuEtAl2026v1','DGKX_v2':'DuEtAl2026v2'}
queries = {
 'F.2.33':['finite affine','cap complex','bar complex','Koszul','homological perturbation','cyclic resolution','fourfold'],
 'F.2.34':['Kuhn','standard grid','rank-three','rank three','collapse map','170','199','fourfold'],
 'F.2.35':['Fox','4003','marked gluing','integral homology','Kuhn','higher coherence','fourfold'],
 'F.2.37':['canonical representative','simultaneous conjugacy','Hecke','involution','height bound','fourfold'],
 'F.2.38':['involution','56','binary similarity','centralizer','free affine','fourfold'],
 'F.2.39':['effective classification','simultaneous conjugacy','Kuhn','4003','56','fourfold'],
 'MODULAR_COLLISION_50_56':['I_1^*','I_1^{*}','I_5','50/II','56/II','1/12','1/30','collision','modular cover'],
}
logs=[]
for sid,terms in queries.items():
    for key,path in paths.items():
        lines=(ROOT/path).read_text(errors='replace').splitlines()
        found=[]
        for term in terms:
            pat=re.compile(r'(?<![A-Za-z0-9])'+re.escape(term)+r'(?![A-Za-z0-9])',re.I)
            hits=[i+1 for i,line in enumerate(lines) if pat.search(line)]
            found.append(dict(term=term,count=len(hits),line_numbers=hits))
        logs.append(dict(source_id=sid,source=key,index_source=path,index_sha256=sha(ROOT/path),terms=found,**META))
save('maps_F_and_repair_credit_search_log.json',logs)
lookup={(r['source_id'],r['source']):r for r in logs}

def scoped(sid,key):
    r=lookup[sid,key]
    out=dict(status='not_found_in_scoped_comparison',full_statement_found=False,
        index_source=r['index_source'],index_sha256=r['index_sha256'],
        search_scope=dict(search_log='work/invariants_arithmetic/maps_F_and_repair_credit_search_log.json',
            record_key=sid+'|'+key,terms_searched=queries[sid],
            hit_counts={x['term']:x['count'] for x in r['terms']}),
        relation='No complete statement of this exact marked result was found in the declared whole-source term search and bounded original-source readings. This is not a claim about unsearched literature.')
    if key in baseline_keys:
        b=base[baseline_keys[key]]
        for field in ['citation_key','local_source','source_sha256','opened_locator']:
            if field in b:out[field]=b[field]
    return out

ao=read('maps_F_references_verified.json')[0]
bhj=json.loads((D/'work/root/BHJ22_source_check.json').read_text())
yang=copy.deepcopy(modern['manYang26'])
yang['opened_locator']+=' Additional opening for F2.34: full subsection Periodic toroidal quotients in arbitrary dimension, original lines4676–4849; complete Theorem higher-dimensional-periodic and its proof, complete Corollary kuhn-euler (The standard grid family) and proof.'
yang['actual_use']='F2.34 precursor: actual higher-dimensional periodic toric quotient, properness, smoothness, normal-crossing charts, canonical form, component/monodromy data and Euler n!d for the standard Kuhn grid. It does not supply the full marked cap/boundary integral chain complexes, their inclusion, the 26/170/flag counts, or the torsion table.'
yang['hypotheses_and_normalization_check']='The original assumes a locally finite Z^n-periodic unimodular triangulation with vertex set Z^n and a finite-index sublattice Gamma=B Z^n. The primitive rank-three Kuhn model has n=3 and B=I3, so its Euler number is6. The original local proof was read and matches precisely this geometric scope; the F2.34 chain calculation remains separately proved.'
refs=read('maps_F_references_verified.json')
refs=[r for r in refs if r['citation_key']!='manYang26']+[yang]
save('maps_F_references_verified.json',refs)

rows=[]
for audit in read('maps_F_receiving_audit.json'):
    sid=audit['source_id']
    out=dict(source_run=audit['source_run'],source_id=sid,printed_label='maps:src:'+sid,
        complete_statement_and_proof=audit['complete_proof_file'],**META)
    for key,field in [('AC26','found_in_AC26'),('E26','found_in_E26'),('DGKX_v1','found_in_DGKX_v1')]:
        out[field]=scoped(sid,key)
    out['found_in_DGKX_v1']['additional_hit_check']='The involution hits were opened at original lines3290–3360 and7118–7163; they concern the sign involution of a normalized double cover, not the ordered rank-six tuple classification.'
    if sid in ['F.2.33','F.2.35','F.2.39']:
        out['found_in_E26'].update(status='found_antecedent',
            locator='S6.tex §3, Proposition reduction/Corollaries fill and fill2 lines598–703; Construction con-log and Lemma twist with full proof lines771–842; §7 integral homology lines1232–1643.',
            relation='The original rank-four torus finite logarithmic caps and marked translations are geometric predecessors. They do not state the arbitrary-r finite chain algorithm or the complete marked rank-six eight-manifold computation.')
    else:
        out['found_in_E26']['additional_opened_scope']='Additional remarks, original lines1640–1763, opened in full; rank-three subtorus there is a subtorus of a real rank-four threefold fibre, not the present rank-three complex cusp.'
    elsewhere=dict(status='not_found_in_scoped_comparison',full_statement_found=False,
        additional_search_scope=[scoped(sid,key) for key in paths if key not in ['AC26','E26','DGKX_v1']],
        sources_checked=[],relation='No exact complete result found in the six declared additional whole-source searches. Ingredient credit is distinguished from credit for the complete statement.')
    if sid in ['F.2.34','F.2.35','F.2.39']:
        elsewhere['status']='found_antecedent'
        elsewhere['sources_checked'].append(dict(citation_key='manYang26',opened_locator=yang['opened_locator'],
            local_source=yang['local_source'],source_sha256=yang['source_sha256'],scope=yang['actual_use']))
        elsewhere['sources_checked'].append(dict(citation_key='ffAchingerOgus20',opened_locator=ao['opened_locator'],
            local_source=ao['local_source'],source_sha256=ao['source_sha256'],
            scope='The logarithmic mapping-cylinder theorem supplies the actual proper vertical log-smooth degeneration comparison, retaining a chosen boundary trivialization. It does not compute the finite chain complexes or their marked integral maps.'))
    if sid in ['F.2.37','F.2.39']:
        elsewhere['status']='found_antecedent'
        elsewhere['sources_checked'].append(dict(citation_key='rootBHJ22',opened_locator=bhj['locator'],
            source_sha256=bhj['source_sha256'],review_ledger='work/root/BHJ22_source_check.json',
            scope='General lattice-isomorphism algorithm under the exact split-algebra hypotheses verified for F2.36. The receiving proof here uses that checked prerequisite; it does not claim that BHJ prints this bounded lexicographic rank-six classifier.',
            reader_scope='Root opened the original; this reader read its exact original-source check and the complete receiving F2.36 dependency audit.'))
    if sid=='F.2.38':
        elsewhere['additional_hit_check']='Wang scalar involution and fixed-set lemma lines1660–1706, and Liu–Rollenske deck involution lines539–558 were opened and are distinct from this ordered simultaneous GL6 classification. The elementary integral involution/glue proof is fully retained in this result.'
    out['found_elsewhere']=elsewhere
    out['credit_summary']='Preceding family geometry is credited to its original sources; the exact complete scope and all six receiving proofs remain printed. No global novelty claim is inferred from a bounded comparison.'
    rows.append(out)
save('maps_F_credit_comparison.json',rows)
fields=['source_run','source_id','printed_label','checker','effort','date','found_in_AC26','found_in_E26','found_in_DGKX_v1','found_elsewhere','credit_summary']
with (W/'maps_F_credit_comparison.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for r in rows:w.writerow({k:json.dumps(r[k],ensure_ascii=False) if isinstance(r[k],(dict,list)) else r[k] for k in fields})

# The writing repair has one statement and one full provider proof, with a
# separately identified independent same-model receiving review.
review_path=D/'work/cdp_audit/modular_collision_review/independent_review.json'
review=json.loads(review_path.read_text());closure=read('maps_modular_collision_closure.json')
proof=ROOT/closure['source_file'];s=proof.read_text();assert sha(proof)==review['source_sha256']==closure['source_sha256']
closure['current_check']='Authorial full rederivation plus independent receiving review passed in /root/cdp_audit; all524 source lines and all413 verifier lines read, originals reopened and unchanged isolated rerun matched certificate and stdout byte for byte.'
closure['independent_review']=dict(file=str(review_path.relative_to(D)),sha256=sha(review_path),
    reader=review['reader'],outcome=review['outcome'],source_lines=review['source_lines'],
    program_rerun='code/cdp_audit/modular_collision_review/execution_manifest.json',
    references='work/cdp_audit/modular_collision_review/references_verified.json')
save('maps_modular_collision_closure.json',closure)
credits={field:scoped('MODULAR_COLLISION_50_56',key) for field,key in [('found_in_AC26','AC26'),('found_in_E26','E26'),('found_in_DGKX_v1','DGKX_v1')]}
credits['found_in_E26'].update(status='found_antecedent',locator='Remark8.5, original S6.tex lines1738–1759',
    relation='Known general elliptic section-line construction and the manifold question; not an exact based realization of these two archived profiles.')
credits['found_elsewhere']=dict(status='found_configuration_and_lattice',full_statement_found=False,
    sources_checked=[{k:modern[key].get(k) for k in ['citation_key','local_source','source_sha256','opened_locator','actual_use']}
        for key in ['manMiranda90','manFukae02','mapsMilne2017','manSS10','manExplorer26']],
    additional_search_scope=[scoped('MODULAR_COLLISION_50_56',key) for key in paths if key not in ['AC26','E26','DGKX_v1']],
    relation='The fibre configurations and rank-one MW groups/heights are explicitly in Miranda §4 and Fukae Table3 rows50 and56. The archived exact matrices/cocycles are Explorer data. This provider supplies the missing based geometric realization of those data, with the modular, Weierstrass and junction prerequisites credited separately.')
save('maps_modular_collision_credit_comparison.json',dict(source_run='WRITING_REPAIR',source_id=closure['source_id'],printed_label=closure['printed_label'],**META,**credits))
with (D/'S6_09_PAPERS_inventory.csv').open(newline='') as f:fields=csv.DictReader(f).fieldnames
assert len(fields)==17
start=s.index('\\begin{theorem}');end=s.index('\\end{theorem}',start)+len('\\end{theorem}')
row={k:'' for k in fields}
row.update(source_run='WRITING_REPAIR',source_id=closure['source_id'],source_file=str(proof.relative_to(D)),paper='III',
 printed_label=closure['printed_label'],kind='Gap filled; exact marked realization',statement_as_printed=s[start:end],
 wording_vs_source='Complete writing-stage provider for absent geometric-monodromy-proof.md; the archived matrix/cocycle data and known configurations are unchanged.',
 recorded_checks=json.dumps(closure['independent_review'],ensure_ascii=False),
 your_check=json.dumps(dict(**META,proof_scope=closure['proof_scope'],computation=closure['computation']),ensure_ascii=False),
 check_outcome=review['outcome']+' No unresolved mathematical objection. Source-to-print check remains a separate editorial gate.',
 credited_to='Miranda1990 §4: configurations; Fukae2002 Table3 rows50,56 and §§3–4: MW lattices and natural junction identification; Milne2017 §§2,4: modular covers; Schuett–Shioda2010 §§4.5,8.2–8.4: Weierstrass/rationality; archived Explorer: exact input matrices/cocycles.',
 notes='Source SHA256 '+sha(proof)+'. Complete proof lines1–524. Independent /root/cdp_audit receiving review: same model, effort and date in a separate agent; not a human or cross-model review. Closes the exact D2.1 geometric marking dependency for50/II and56/II only.')
for field,value in credits.items():row[field]=json.dumps(value,ensure_ascii=False)
save('maps_modular_collision_inventory.json',[row])
with (W/'maps_modular_collision_inventory.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerow(row)
audits=read('maps_F_receiving_audit.json')
for r in audits:
    r['credit_comparison']='work/invariants_arithmetic/maps_F_credit_comparison.json#'+r['source_id']
    r['printed_label']='maps:src:'+r['source_id']
save('maps_F_receiving_audit.json',audits)
print('Saved six complete F credit rows,63 whole-source search records, one exact17-column writing-repair row, and the independent provider closure.')
