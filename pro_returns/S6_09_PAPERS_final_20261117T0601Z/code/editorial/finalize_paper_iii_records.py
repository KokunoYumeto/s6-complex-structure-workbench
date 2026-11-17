"""Merge current III evidence without changing completed companion records.

Historical partial readings are preserved in their original records. Credit
searches never promote a proof to checked; full receiving/dependency events
and the source-to-print gate remain distinct.
"""
from pathlib import Path
import csv, json, re, collections, bisect
D=Path(__file__).resolve().parents[2]; W=D/'work'
path=D/'S6_09_PAPERS_inventory.csv'
with path.open(newline='') as f:rd=csv.DictReader(f);fields=rd.fieldnames;rows=list(rd)
index={(r['source_run'],r['source_id']):r for r in rows}
original_companions={k:dict(r) for k,r in index.items() if r['paper']!='III'}
def serial(x):return x if isinstance(x,str) else json.dumps(x,ensure_ascii=False)
def add(r,k,x):
    if x and serial(x) not in r[k]:r[k]=(r[k]+' | '+serial(x)).strip(' |')
def load(rel):
    p=D/rel
    if not p.exists():return []
    o=json.loads(p.read_text())
    if isinstance(o,list):return o
    if 'source_id' in o:return [o]
    return o.get('rows',o.get('results',o.get('records',o.get('comparisons',[]))))
def target(x,default_run=None):
    run=x.get('source_run',default_run);sid=x.get('source_id',x.get('id'))
    r=index.get((run,sid))
    if r is None:
        candidates=[r for r in rows if r['source_id']==sid and r['paper']=='III']
        assert len(candidates)==1,(run,sid)
        r=candidates[0]
    return r

events=[]
for rel,default in [
 ('work/invariants_arithmetic/maps_D_independent_audit.json','S6_04_MAPS_MANIFOLDS'),
 ('work/cdp_audit/maps_E/result_audit.json','S6_04_MAPS_MANIFOLDS'),
 ('work/root/maps_F_final_result_checks.json','S6_04_MAPS_MANIFOLDS'),
 ('work/invariants_arithmetic/maps_F_receiving_audit.json','S6_04_MAPS_MANIFOLDS'),
 ('work/maps_audit/III_maps60_final_closure.json','S6_04_MAPS_MANIFOLDS'),
 ('work/maps_audit/III_final_closure_overlay.json',None),
]:
    for x in load(rel):
        r=target(x,default)
        if r['paper']!='III':continue
        own=x.get('own_check',x.get('your_check',x.get('checks',x.get('new_check_events'))))
        if not own and x.get('full_receiving_proof_read'):
            own={k:x[k] for k in ['reader','effort','date','full_receiving_proof_read',
               'current_check_event_ids','receiving_read_records','source_dependency_status',
               'exact_source_check_records','additional_source_ledgers','program_check_records',
               'program_ledgers'] if k in x}
            own['record']=rel
        if own:r['your_check']=serial(own)
        outcome=x.get('check_outcome',x.get('outcome',x.get('audit_state',x.get('status'))))
        if outcome:r['check_outcome']=serial(outcome)
        for k in ['recorded_checks','recorded_check_absence','source_blocks','proof_comparison','unresolved_claims','explicit_scope_limitations']:
            if x.get(k):add(r,'notes',k+': '+serial(x[k]))
        add(r,'notes','Final receiving/dependency event: '+rel)
        events.append({'source_run':r['source_run'],'source_id':r['source_id'],'record':rel})

# The separate full six-proof reader supplied the complete symbolic arguments.
# Parent-owned actual program executions and the exact Achinger–Ogus opening
# now close the explicitly reserved numerical/dependency clause.
for sid in ['F.2.33','F.2.34','F.2.35','F.2.37','F.2.38','F.2.39']:
    r=index[('S6_04_MAPS_MANIFOLDS',sid)]
    add(r,'your_check',{'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro),17November2026,/root',
         'event':'Parent-owned dependency and actual execution closure',
         'evidence':['code/root_maps_F/final_execution_reconciliation.json','work/invariants_arithmetic/maps_F_references_verified.json','work/invariants_arithmetic/maps_F_proof_insertions.json'],
         'scope':'Complete cap/global-chain and classification proof read by the separate receiving reader; both explicit cyclic comparison and logarithmic-cylinder hypothesis supplements retained. Every operative F computation completed at its recorded scope.'})
    r['check_outcome']='Passed complete independent receiving proof, source-hypothesis matching, full symbolic supplements and actual finite computations. No executed enumeration of an infinite parameter space is asserted.'

credits=[]
credit_sources=[
 'work/invariants_arithmetic/maps_D_credit_comparison.json',
 'work/invariants_arithmetic/maps_F_credit_comparison.json',
 'work/invariants_arithmetic/maps_modular_collision_credit_comparison.json',
 'work/invariants_arithmetic/push_C_and_family_credit_comparison.json',
 'work/cdp_audit/maps_credit/E_credit_comparison_22.json',
 'work/cdp_audit/maps_credit/F_credit_comparison_33.json',
 'work/cdp_audit/carrier_credit/working_credit_inventory_overlay_39.json',
 'work/cdp_audit/carrier_credit/prerequisite_credit_inventory_overlay_2.json',
 'work/maps_audit/maps60_credit_comparison.json',
 'work/maps_audit/course249_credit_comparison.json',
 'work/maps_audit/III_repair6_credit_comparison.json',
]
cols=['found_in_AC26','found_in_E26','found_in_DGKX_v1','found_elsewhere']
names={'AC2026':'Claude and Alpöge (2026)','AC26':'Claude and Alpöge (2026)',
       'Engel2026':'Engel (2026)','E26':'Engel (2026)',
       'DuEtAl2026v1':'Du, Guo, Kusakabe, and Xie (2026),version1',
       'DGKXv1':'Du, Guo, Kusakabe, and Xie (2026),version1'}
for rel in credit_sources:
    for x in load(rel):
        r=target(x,'S6_04_MAPS_MANIFOLDS')
        if r['paper']!='III':continue
        for k in cols:
            assert k in x,(rel,r['source_id'],k)
            r[k]=serial(x[k])
        # The fixed schema has no v2 column; preserve the separate v2 check.
        if x.get('found_in_DGKX_v2'):add(r,'notes','Separate DGKXv2 comparison: '+serial(x['found_in_DGKX_v2']))
        if x.get('credited_to'):r['credited_to']=serial(x['credited_to'])
        else:
            credit=[]
            for k in cols:
                d=x[k]
                if isinstance(d,str):continue
                if not isinstance(d,dict):continue
                if 'found' not in d.get('status','') or d.get('status','').startswith('not_found'):continue
                if d.get('matches'):
                    for m in d['matches']:
                        credit.append(' '.join(str(m.get(z,'')) for z in ['citation_key','locator','relation']).strip())
                elif d.get('relation'):
                    credit.append(names.get(d.get('citation_key'),d.get('citation_key',k))+': '+d.get('locator',d.get('opened_locator',''))+' '+d['relation'])
            if x.get('credit_summary'):credit.append(serial(x['credit_summary']))
            if x.get('standard_background_note'):credit.append(x['standard_background_note'])
            r['credited_to']=' | '.join(dict.fromkeys(credit)) or 'No identical full receiving conclusion found in the explicitly recorded comparisons. Classical ingredients are credited at their points of use; the negative search has only its recorded scope.'
        kind=x.get('credit_classification',x.get('kind',''))
        if kind=='Cited/re-derived' or x.get('novelty_classification')=='wholly_known_rederivation':r['kind']='Cited/re-derived'
        add(r,'notes','Final bounded source comparison: '+rel)
        credits.append({'source_run':r['source_run'],'source_id':r['source_id'],'record':rel})

for sid in ['C.1.1','C.1.2','C.2.1','C.3.1','C.3.3']:
    index[('S6_02_PUSH',sid)]['kind']='Cited/re-derived'
add(index[('S6_02_PUSH','C.2.1')],'wording_vs_source',
    'Literal comma superscripts in the source spin-c formula corrected to ordinary second/fourth powers with thin-space TeX, as required by its unchanged proof and the opened original formula; see records/III_push_typography_and_reference_corrections.json.')
index[('S6_04_MAPS_MANIFOLDS','E.2.2')]['kind']='Cited/re-derived'
index[('working_edition_reader_extension','G2-8')]['kind']='Cited/re-derived'
index[('working_edition','cusp-cone-S12-almost-complex-obstruction')]['kind']='Cited/re-derived'

text=(D/'S6_09_PAPERS_III.tex').read_text()
labels=set(re.findall(r'\\label\{([^}]+)\}',text))
for x in load('work/root/III_source_placements.json'):
    r=target(x)
    if r['paper']=='III':r['printed_label']=x['printed_label']
statement_ranges=[];statement_stack=[]
statement_envs='theorem|proposition|lemma|corollary|claim|statement|remark|question|problem|conjecture|definition|example|computed|test'
for token in re.finditer(r'\\(begin|end)\{('+statement_envs+r')\}',text):
    if token[1]=='begin':statement_stack.append((token[2],token.start()))
    elif statement_stack and statement_stack[-1][0]==token[2]:
        env,start=statement_stack.pop();statement_ranges.append((start,token.end(),env))
statement_ranges.sort();statement_starts=[r[0] for r in statement_ranges]
label_positions={m[1]:m.start() for m in re.finditer(r'\\label\{([^}]+)\}',text)}
def printed_statement(label):
    pos=label_positions[label]
    i=bisect.bisect_right(statement_starts,pos)-1
    if i>=0:
        start,end,env=statement_ranges[i]
        if pos<end:return text[start:end],env
    # Course units have section labels: retain their actual printed first
    # complete unit rather than manufacturing a theorem not in the source.
    tail=text[pos:];m=re.search(r'\n\\(?:sub)*section\*?(?:\[[^\]]*\])?\{',tail)
    return tail[:m.start() if m else min(len(tail),6000)],'course unit'
missing=[]
for r in rows:
    if r['paper']!='III':continue
    if r['printed_label'] not in labels:
        missing.append((r['source_run'],r['source_id'],r['printed_label']));continue
    st,env=printed_statement(r['printed_label']);r['statement_as_printed']=st
    if r['kind'] in {'Result','result','theorem','proposition','lemma','corollary','remark','definition'}:
        r['kind']=env.title()
    if r['source_run']=='S6_04_MAPS_MANIFOLDS' and r['source_id']=='D.2.4':r['kind']='Open problem; established reductions retained'
    if r['source_run']=='S6_02_FAMILY' and r['source_id']=='E.2.3':r['kind']='Question settled by the printed companion results'
    add(r,'wording_vs_source','Exact final statement extracted from the printed label. All mathematical changes are identified by the full per-result and transform records; source/label normalization alone is not treated as a new proof.')
assert len(fields)==17
assert all(index[k]==v for k,v in original_companions.items()),'Completed companion inventory changed'
with path.open('w',newline='') as f:wr=csv.DictWriter(f,fields);wr.writeheader();wr.writerows(rows)
report={'rows':len(rows),'papers':dict(collections.Counter(r['paper'] for r in rows)),
 'III_rows':sum(r['paper']=='III' for r in rows),'missing_placements':missing,
 'receiving_closure_events':events,'credit_comparison_rows':credits,
 'credit_distinct_rows':len({(r['source_run'],r['source_id']) for r in credits}),
 'status':'Evidence integration; final source-retention, bibliography and typesetting gates remain separate.'}
(D/'records/III_inventory_finalization.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['receiving_closure_events','credit_comparison_rows']},indent=2))
