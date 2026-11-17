from pathlib import Path
import json,csv,hashlib,re
O=Path('deliverables/work/maps_audit');SRC=Path('sources/codex_workspace/courses/CG-S6')
pro={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','independent_review_kind':'new full proof reading and rederivation by this writing session; no human review'}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
manifest=json.loads((O/'paperI_course_foundations_manifest.json').read_text())
for r in manifest:
 r.update(pro)
 r['current_read_scope']='All 261 lines of the CW/Hurewicz receiving companion; all 544 lines of the path-fibre receiving companion; Thom/Euler provider sections 1–4, lines 7–170, complete. The remainder of the Thom/Euler provider is not included or certified by this record.'
 r['source_provider']={'model':'GPT-6.1 Sol (OpenAI)','effort':'Ultra','month':'October 2026','date_precision':'month only; no day inferred','basis':'Explicit original header for Frame fields and primary obstructions and Thom classes and Euler classes; the unchanged Homotopy fibres source header names model and Ultra but gives no month, so its receiving companion date is recorded separately rather than inferred as an exact source date.','receiving_model':'GPT-6 Astra (OpenAI)','receiving_effort':'Ultra','receiving_month':'October 2026','source_self_checks_are_not_current_checks':True}
 r['original_provider_files']=[]
 for name in ['thom-classes-and-euler-classes.source.txt','frame-fields-and-primary-obstructions.source.txt','homotopy-fibres-and-the-serre-spectral-sequence.source.txt']:
  p=SRC/'sources'/name
  r['original_provider_files'].append({'file':str(p),'sha256':sha(p),'raw_header':p.read_text().splitlines()[2],'current_read_scope':'Header/provenance opened. The full original provider is not claimed independently read by this record; the complete receiving proof ranges above were read.'})
 r['independent_reruns']={'cw_hurewicz':'deliverables/code/maps_audit/course/CW_HUREWICZ_CHECKS.json (34 PASS)','path_fibre':'deliverables/code/maps_audit/course/PATH_FIBRE_CHECKS.json (38 PASS)','scope':'Formal finite certificates supplement the complete written all-degree proofs; no inference of global theorem correctness from finite sampling alone.'}
 r['output_sha256']=sha(r['output'])
(O/'paperI_course_foundations_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
ws=json.loads((O/'working_results_inventory.json').read_text())
for r in ws:
 if r['source_id'] not in ['CG-S6-07-HOMOLOGY','CG-S6-07-HOMOTOPY']:continue
 ishom=r['source_id'].endswith('HOMOLOGY')
 r['your_check']='new-course-homology-homotopy-full-20261117: Complete course sections 7 and 9 read step by step. Integral homology proof compared with the existing Leray/UCT/PD blocks; actual degree-one map, path fibration, both homology edges and original inverse maps rederived. Full CW/Hurewicz and path-fibre receiving companions read, chain prerequisite sections 1–4 read, and original exact checkers rerun (34 and 38 PASS).'
 r['check_outcome']='Checked duplicate, full proof already printed in the mapped two topology results.' if ishom else 'Complete distinct proof checked and supplied with every operative receiving classical prerequisite in full.'
 r['printed_label']='mapsI:top:lem:cohomological-closure' if ishom else 'mapsI:course:CG-S6-07-HOMOTOPY'
 r['taken_over_by']='WORKING_EDITION:thm:h2-vanishing; WORKING_EDITION:lem:cohomological-closure' if ishom else 'Full distinct alternate proof retained alongside the known sphere-recognition conclusion.'
 r['paper']='I'
 r['proof_output']='deliverables/work/maps_audit/paperI_course_homology_concordance.json' if ishom else 'deliverables/work/maps_audit/paperI_course_homotopy.tex'
 r['check_event_ids']=list(dict.fromkeys(r.get('check_event_ids',[])+['new-course-homology-homotopy-full-20261117']))
(O/'working_results_inventory.json').write_text(json.dumps(ws,indent=2)+'\n')
with (O/'working_results_inventory.csv').open('w',newline='') as f:
 fields=list(dict.fromkeys(k for r in ws for k in r));w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()} for r in ws)
events=json.loads((O/'check_events.json').read_text());eid='new-course-homology-homotopy-full-20261117'
if not any(e.get('id')==eid for e in events):events.append({'id':eid,'source_ids':['CG-S6-07-HOMOLOGY','CG-S6-07-HOMOTOPY'],'full_proof_reads':['course sections 7 and 9','CW/Hurewicz companion all 261 lines','path-fibre companion all 544 lines','Thom/Euler chain prerequisites lines 7–170'],'outcome':'Homology concordance exact; distinct actual path-fibration degree-one proof and full receiving prerequisites supplied; original checkers 34/34 and 38/38 PASS.','manifest':'deliverables/work/maps_audit/paperI_course_foundations_manifest.json',**pro})

for event_record in events:
 if 'event_id' not in event_record:
  event_record['event_id']=event_record['id']
  event_record['results']=['WORK:'+x for x in event_record['source_ids']]
  if 'scope' not in event_record:event_record['scope']='Complete source proof reads: '+'; '.join(event_record.get('full_proof_reads',[]))
  event_record['locator']=event_record['manifest']
  event_record['remaining_dependencies']=[]
(O/'check_events.json').write_text(json.dumps(events,indent=2)+'\n')
# Account for the formal classical results used by these proofs without changing parent inventory.
anc=[]
configs=[('chain','thom-euler-for-lesson11.md',[('Lemma','1.1'),('Lemma','2.1'),('Corollary','2.2'),('Lemma','4.1')]),('cw','cw-models-and-the-first-hurewicz-map.md',[('Theorem','4.1'),('Exercise','5.1'),('Exercise','5.2')]),('pf','path-fibres-and-integral-homotopy-equivalences.md',[('Theorem','5.1'),('Exercise','6.1'),('Exercise','6.2')])]
for ns,name,items in configs:
 p=SRC/'src'/name;lines=p.read_text().splitlines()
 for kind,num in items:
  start=next(i for i,l in enumerate(lines) if l.startswith('**'+kind+' '+num))
  if kind=='Exercise':
   end=next((i for i in range(start+1,len(lines)) if lines[i].startswith('**Exercise ') or lines[i].startswith('## ')),len(lines))
  else:end=next(i for i in range(start+1,len(lines)) if '∎' in lines[i] or '\\square' in lines[i])+1
  label='mapsI:'+ns+':'+kind.lower()+':'+num
  if ns=='cw' and kind=='Theorem':label='mapsI:cw:hurewicz-theorem-result'
  if kind=='Exercise':
   # Add an exact source alias to the already printed exercise paragraph.
   tex=O/('paperI_course_'+ns+'_foundations.tex');body=tex.read_text();pat=r'(\\textbf\{Exercise '+re.escape(num)+r'[^}]*\})';body,n=re.subn(pat,lambda m:m.group(1)+'\\label{'+label+'}',body,count=1);assert n==1,(name,num);tex.write_text(body)
  anc.append({'source_run':'WORKING_EDITION_COURSE_PROVIDER','source_id':'CG-S6-'+ns.upper()+'-'+kind.upper()+'-'+num,'source_file':str(p)+':'+str(start+1),'source_sha256':sha(p),'paper':'I','kind':'Classical rederivation' if kind!='Exercise' else 'Worked exact example','statement_as_source':lines[start],'printed_label':label,'full_proof_source_lines':[start+1,end],'recorded_checks':'Source author self-check preserved as such; it is not an independent check. Raw model/effort/month headers in the foundations manifest.','your_check':'Full receiving proof read and rederived in current session; exact CW/path checkers rerun where relevant.','check_outcome':'Complete classical proof/example retained; no novelty claim.','found_elsewhere':'Hatcher2002 Theorem4.32/Cor4.33 for the named homotopy principles; elementary singular-chain constructions are classical and printed in full. This record does not assert a universal literature search for each teaching exercise.','credited_to':'Classical topology; provider and receiving AI source provenance retained in the foundations manifest.',**pro})
(O/'paperI_course_ancillary_inventory.json').write_text(json.dumps(anc,indent=2)+'\n')
with (O/'paperI_course_ancillary_inventory.csv').open('w',newline='') as f:
 fields=list(dict.fromkeys(k for r in anc for k in r));w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()} for r in anc)
# Refresh hashes after the exercise aliases.
for r in manifest:r['output_sha256']=sha(r['output'])
(O/'paperI_course_foundations_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Saved current course checks, complete exact provenance, and',len(anc),'formal ancillary result rows.')
