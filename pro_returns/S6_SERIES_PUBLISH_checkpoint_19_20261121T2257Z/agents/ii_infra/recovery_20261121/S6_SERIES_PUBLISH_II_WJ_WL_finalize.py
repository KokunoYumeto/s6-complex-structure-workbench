#!/usr/bin/env python3
"""Freeze new complete comparisons and two proposals; no canonical mutation."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[3]
AREA=ROOT/'agents/ii_infra/recovery_20261121'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):
 p=ROOT/p if isinstance(p,str) else p
 return {'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size}
def save(name,value):
 p=AREA/name
 with p.open('x') as f:json.dump(value,f,indent=2,ensure_ascii=False);f.write('\n')
 return bind(p)
now=datetime.now(timezone.utc).isoformat()
gpath=AREA/'S6_SERIES_PUBLISH_II_WJ_WL_guards_v2.json'
g=json.loads(gpath.read_text())
assert sha(gpath)=='cc0319cc8d15a597b02405e933ecc4e0ab8c4b6185cab55c349ef053e15ab985'
assert len(g['guards'])==18
evidence=[bind(AREA/name) for name in [
 'S6_SERIES_PUBLISH_II_WJ_WL_comparison.md',
 'S6_SERIES_PUBLISH_II_WJ_WL_fresh_exact.py',
 'S6_SERIES_PUBLISH_II_WJ_WL_fresh_exact_output.json',
 'S6_SERIES_PUBLISH_II_WJ_WL_postrelease_exact.py',
 'S6_SERIES_PUBLISH_II_WJ_WL_postrelease_exact_output.json',
 'S6_SERIES_PUBLISH_II_WL_prior_program_reexecution.txt',
 'primary_inputs/S6_SERIES_PUBLISH_II_WJ_primary_verification_receipt.json',
 'S6_SERIES_PUBLISH_II_02WJ_global_hypotheses_inputs_v2.json',
 'S6_SERIES_PUBLISH_II_02WJ_global_hypotheses_inputs_v2.tex']]
post_input_data={
 'archived_utc':now,'source':'Collaboration messages from /root/ii_check_a, received after both new releases.',
 'historical_file_bytes_recovered':False,
 'formal_functions_input':'A described the coherent F/m_s^k F, finite nilradical filtration, point torsion, finite normalization/vector-bundle and length-one Dolbeault argument, followed by Grauert1960 Section6 HauptsatzIIa p59, coherence and Nakayama, with the1963 corrigendum. The receiver then opened those primary loci and verified every step.',
 'cyclic_quotient_input':{
  'tacnode':'The two normalized P1 components have equal t parameter and local subring f=g mod t^2; their swap gives the global cubic involution, locally (x,y)->(x,x^2-y).',
  'triple':'sigma3[X:Y:Z]=[-Y:X-Y:Z], order3, permuting all3 components.',
  'base':'Eprime=C/(Z+iZ); translation tau_r by1/r; diagonal quotient (C_r x Eprime)/<(sigma_r,tau_r)> forr2,3.',
  'normalization':'Choose one normalized component; its product with Eprime is isomorphic to the normalized quotient. The conductor is twice the single Eprime section and maps by the exact degree-r unramified cover to E.',
  'locality_clarification':'After restore_build raised the nontrivial action on nilpotent directions, A confirmed that O_E[u]/u^2 and O_E[u,v]/(u,v)^2 describe analytic local algebras only, with no global untwisted-algebra assertion.'},
 'receiver_independent_verification':'Explicit parameter maps, the normalized-quotient inverse and all local-ring/conductor relations are written in the complete proposed proof and comparison. Postrelease exact identities are separately executed.',
 'events_added':0}
post_input_path=AREA/'S6_SERIES_PUBLISH_II_WJ_WL_postrelease_collaboration_input.json'
post_input=bind(post_input_path) if post_input_path.exists() else save(post_input_path.name,post_input_data)
evidence.append(post_input)
cdp=ROOT.parent/'S6_SERIES_PUBLISH_work/S6_GRIND_6_literature/papers/arXiv_1904.11179v2_CDP20_corrigendum_src/main.tex'
lines=cdp.read_text().splitlines(keepends=True)
external=[]
for name,first,last,phase in [('WL_curve_inference',1093,1097,'before new freeze'),('WJ_conductor_input',583,609,'after new release')]:
 text=''.join(lines[first-1:last]);p=AREA/f'S6_SERIES_PUBLISH_II_{name}_external_input.tex'
 if p.exists():assert p.read_text()==text
 else:p.write_text(text)
 external.append({'source_path':str(cdp),'source_sha256':sha(cdp),'line_span_inclusive':[first,last],
                  'opened_phase':phase,'excerpt':bind(p),'attached_source_edition':'arXiv:1904.11179v2'})
checks=[]
for tag,h in [('02WJ','256e001174e38219a4030cd696f599d400e57b8994acc961c25b701fc0ff7372'),('02WL','20e84c046cc4d418268747fe28f231744f5a3806a5d4ba2d9fa7e1d6ecb0e398')]:
 fs=[p for p in (ROOT/'agents/ii_infra/derivation_freezes'/tag).glob('*/S6_SERIES_PUBLISH_derivation_freeze_receipt.json') if sha(p)==h]
 assert len(fs)==1
 fp=fs[0];f=json.loads(fp.read_text());dp=ROOT/f['frozen_derivation_path'];assert sha(dp)==f['derivation_sha256']
 rp=ROOT/'agents/ii_infra/released_proofs'/tag/h[:16]/'S6_SERIES_PUBLISH_release_receipt.json';r=json.loads(rp.read_text())
 assert r['freeze_receipt_sha256']==h and r['derivation_sha256']==sha(dp)
 assert datetime.fromisoformat(f['created_utc'])<datetime.fromisoformat(r['created_utc'])
 b=next(x for x in g['blocks'] if x['tag']==tag)
 before=(ROOT/b['original_full_block']).read_text();after=(ROOT/b['proposed_full_block']).read_text()
 assert sha(ROOT/b['original_full_block'])==b['original_full_block_sha256']==r['full_owning_block_sha256']
 assert sha(ROOT/b['proposed_full_block'])==b['proposed_full_block_sha256']
 forward=before;forward_steps=[]
 guards=[z for z in g['guards'] if z['tag']==tag]
 for guard in guards:
  assert forward.count(guard['before'])==1
  offset=forward.index(guard['before'])
  forward_steps.append({'id':guard['id'],'offset_at_application':offset,'before':guard['before'],'after':guard['after']})
  forward=forward[:offset]+guard['after']+forward[offset+len(guard['before']):]
 assert forward==after
 inverse=after
 for step in reversed(forward_steps):
  offset=step['offset_at_application']
  assert inverse[offset:offset+len(step['after'])]==step['after'],(tag,step['id'],'exact inverse span')
  inverse=inverse[:offset]+step['before']+inverse[offset+len(step['after']):]
 assert inverse==before,(tag,'exact inverse')
 stat_before=before[:before.index(r'\end{proposition}')]
 stat_after=after[:after.index(r'\end{proposition}')]
 assert re.findall(r'\\\[(.*?)\\\]',stat_before,re.S)==re.findall(r'\\\[(.*?)\\\]',stat_after,re.S)
 checks.append({'tag':tag,'statement_id':b['statement_id'],'freeze_receipt':bind(fp),'frozen_derivation':bind(dp),
                'release_receipt':bind(rp),'original_full_block':bind(ROOT/b['original_full_block']),
                'proposed_full_block':bind(ROOT/b['proposed_full_block']),
                'actual_full_original_and_v2_proposed_reading':True,'actual_every_printed_step_comparison':True,
                'displayed_statement_conclusions_identical':True,'exact_forward_and_inverse_reconstruction':True,
                'exact_inverse_offsets':[{'id':x['id'],'offset_at_application':x['offset_at_application']} for x in forward_steps],
                'full_global_math_reference_identity_claimed':False,'named_guard_maps':[{'id':z['id'],'math':z.get('literal_math_map'),'references':z.get('literal_reference_map')} for z in guards],
                'unresolved_mathematical_issue':None,'root_application_pending':True})
record={'created_utc':now,'checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode | restore_build',
        'new_independent_freezes':True,'historical_lost_blind_check_reconstructed':False,
        'verification_refinement':'The first receipt run rejected reverse global replacement of the one-character period. No comparison/event receipt was written. The final verifier uses recorded forward offsets and exact reverse spans for all guards, including deletions and nonunique replacement strings.',
        'guard_file':bind(gpath),'guard_count':18,'checks':checks,'evidence':evidence,'external_inputs':external,
        'program_source':bind('records/S6_SERIES_PUBLISH_II_opened_programs_recovery_01/genus_one_conductor.py'),
        'program_source_receipt':bind('records/S6_SERIES_PUBLISH_II_opened_programs_recovery_01/receipt.json'),
        'program_table':{k:bind(ROOT/g['program_table'][k]) for k in ['original_full_block','proposed_full_block']},
        'program_table_complete_actual_reading':True,
        'fresh_method':'Fraction elimination plus simultaneous annihilator/ideal conditions, versus prior SymPy augmented-matrix ranks; arbitrary-series normalization inverse proofs precede release.',
        'source_binding':g['source_sha256'],'events_added':0,'canonical_files_modified':False,
        'WI_WK_credit':'Excluded here; transferred to B because prior conceptual input exposure was declared.'}
comp=save('S6_SERIES_PUBLISH_II_WJ_WL_comparison.json',record)
events=[]
for check in checks:
 events.append({'paper':'II','tag':check['tag'],'statement_id':check['statement_id'],'date':now[:10],
                'who':record['checker']+' | S6_SERIES_PUBLISH continuation','type':'targeted proof check',
                'outcome':'New statement-first derivation frozen before target release; every complete printed proof step checked, primary input scopes verified, fresh computational method completed, and full proposed publication block reread. Root review/application and final block binding pending.',
                'evidence_group':'S6_SERIES_PUBLISH_II_INFRA_RECOVERY_'+check['tag'],
                'freeze_receipt':check['freeze_receipt'],'release_receipt':check['release_receipt'],
                'comparison_receipt':comp,'proposed_full_block':check['proposed_full_block'],
                'proposal_only':True,'one_event_for_this_printed_owner':True,'required_final_applied_block_binding':True,
                'do_not_duplicate_any_accepted_owner_event':True})
proposal=save('S6_SERIES_PUBLISH_II_WJ_WL_event_proposals.json',{'created_utc':now,'events':events,
              'status':'Root review only; no ledger append','events_added':0,'canonical_ledger_modified':False})
print(json.dumps({'comparison':comp,'event_proposals':proposal,'guards':bind(gpath),'owners':2,'guards_count':18},indent=2))
