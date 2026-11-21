#!/usr/bin/env python3
"""Propose three disjoint statement-owner allocations from proof metadata only."""
from pathlib import Path
import collections,csv,datetime,hashlib,json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/ii_infra'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
index_path=OUT/'S6_SERIES_PUBLISH_II_packet_index.json'
index=json.loads(index_path.read_text());rows=index['candidates']
domains={
 'A':{'name':'Irreducible-support topology and integral specialization',
      'sections':{'Irreducible supports: topology, conductor and equality',
                  'Integral specialization, coherent restrictions and component counts'}},
 'B':{'name':'Conductor, normalization and analytic Picard restriction',
      'sections':{'Cotangent torsion, conductor and the printed endpoint error',
                  'Normalization, conductor genus and local torus exclusions',
                  'Index, Picard components and endpoint cohomology',
                  'Normal-crossing topology and canonical-flat component comparisons',
                  'Global CDP replacement and normalization resonance',
                  'Uniform non-torsion on every full fibre',
                  'The Liu--Rollenske parameter covering',
                  'Analytic duality and the exact Picard restriction maps'}},
 'C':{'name':'Fibre classification, periods and deformation families',
      'sections':{'Irreducible and reducible torus-fibre Euler criteria',
                  'Complete smooth-fibre classification and actual Hopf occurrence',
                  'Constant-monodromy period comparison and compact examples',
                  'Fibration stability and explicit deformation calculations',
                  'Comb invariants and the precise vector-field correction',
                  'Connected deformation chains and two independent periods'}}}
owner_to_group={};out=[]
for row in rows:
 section=row['heading_path'].get('section','')
 matches=[k for k,d in domains.items() if section in d['sections']]
 assert len(matches)==1,(row['current_statement_owner'],section,matches)
 g=matches[0];owner=row['current_statement_owner'];owner_to_group[owner]=g
 out.append({'allocation':g,'domain':domains[g]['name'],'tag':row['tag'],'label':row['label'],
             'current_statement_owner':owner,'environment':row['environment'],'title':row['title'],
             'source_section':section,'source_subsection':row['heading_path'].get('subsection',''),
             'proof_chars':row['proof_chars'],'proof_lines':row['proof_lines'],
             'proof_environment_count':len(row['proofs']),
             'statement_start_line':row['statement_start_line'],'statement_end_line':row['statement_end_line'],
             'statement_packet':row['packet_path'],'statement_packet_sha256':row['packet_sha256'],
             'packet_readiness':row['packet_readiness'],
             'embargoed_proof':row['target_proof_path'],'embargoed_proof_sha256':row['target_proof_sha256']})
assert len(out)==197 and len(owner_to_group)==197
edges=collections.Counter()
for row in rows:
 a=owner_to_group[row['current_statement_owner']]
 for dep in set(row['proof_refs']):
  if dep in owner_to_group and dep!=row['current_statement_owner']:edges[(a,owner_to_group[dep])]+=1
summary=[]
for g in domains:
 selected=sorted([x for x in out if x['allocation']==g],key=lambda x:x['statement_start_line'])
 p=OUT/f'S6_SERIES_PUBLISH_II_allocation_{g}.json'
 maximum=max(selected,key=lambda x:x['proof_chars'])
 info={'allocation':g,'domain':domains[g]['name'],'owner_count':len(selected),
       'proof_chars':sum(x['proof_chars'] for x in selected),'proof_lines':sum(x['proof_lines'] for x in selected),
       'max_proof_owner':maximum['current_statement_owner'],'max_proof_chars':maximum['proof_chars'],
       'max_proof_lines':maximum['proof_lines'],
       'held_packet_owners':[x['current_statement_owner'] for x in selected if x['packet_readiness']!='statement_inputs_ready'],
       'suggested_order':'Source order within each cohesive section; all other required proof bodies stay embargoed until their own derivation freeze.',
       'rows':selected}
 assert not p.exists();p.write_text(json.dumps(info,ensure_ascii=False,indent=2)+'\n')
 summary.append({k:v for k,v in info.items() if k!='rows'}|{'path':str(p.relative_to(ROOT)),'sha256':sha(p)})
result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'proposal_for_root_assignment',
        'source_sha256':index['source_sha256'],'packet_index_path':str(index_path.relative_to(ROOT)),'packet_index_sha256':sha(index_path),
        'required_rows':197,'distinct_owners':197,'disjoint':True,'all_rows_assigned_once':True,
        'total_proof_chars':sum(x['proof_chars'] for x in out),'total_proof_lines':sum(x['proof_lines'] for x in out),
        'allocations':summary,'candidate_reference_edges_by_allocation':[{'from':a,'to':b,'count':n} for (a,b),n in sorted(edges.items())],
        'allocation_rationale':'Keep printed sections and dependency domains together; balance exact proof-character totals, with line counts and the maximum proof exposed. Three blocks without separate proof environments are included exactly once but held for root statement/argument disposition.',
        'credit_policy':'One check event per current printed statement owner only after actual derivation, comparison, required independent computations and resolution; extraction/allocation/release add no events.',
        'presentation_policy':'After derivation freeze and complete proof comparison, prepare exact presentation guards and complete original/proposed owning blocks while context is open, with mathematical/reference preservation maps and an actual comparative-rereading record.',
        'source_proofs_displayed':False,'events_added':0}
p=OUT/'S6_SERIES_PUBLISH_II_allocation_proposal.json';assert not p.exists();p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
p=OUT/'S6_SERIES_PUBLISH_II_allocation_proposal.csv';assert not p.exists()
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=out[0]);w.writeheader();w.writerows(sorted(out,key=lambda x:(x['allocation'],x['statement_start_line'])))
md=['# Paper II allocation proposal','',f'All 197 required labels have distinct owners and occur in exactly one proposed allocation. Exact archived proof size totals {result["total_proof_chars"]:,} characters / {result["total_proof_lines"]:,} source lines.','',
    '| Allocation | Domain | Owners | Proof characters | Proof lines | Largest proof |','|---|---|---:|---:|---:|---|']
for x in summary:md.append(f'| {x["allocation"]} | {x["domain"]} | {x["owner_count"]} | {x["proof_chars"]:,} | {x["proof_lines"]:,} | {x["max_proof_owner"]}: {x["max_proof_chars"]:,} chars / {x["max_proof_lines"]:,} lines |')
md+=['',result['allocation_rationale'],'',result['credit_policy'],'',result['presentation_policy'],'',
      'The statement packets contain no proof environment. Formula references inside any required target proof are held until the relevant independent derivation is frozen. This is a recorded reading workflow; it does not assert that filesystem access is technically blocked.','',
      'Root assigns the checkers. No target proof was displayed during extraction/allocation; no mathematical check or page-reading credit is generated.']
p=OUT/'S6_SERIES_PUBLISH_II_allocation_proposal.md';assert not p.exists();p.write_text('\n'.join(md)+'\n')
print(json.dumps(result,indent=2))
