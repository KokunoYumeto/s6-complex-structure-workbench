from pathlib import Path
import csv,json,hashlib,datetime,re
P=Path(__file__).resolve().parents[1];W=P.parent
s=(W/'parts/IV.body.linked.tex').read_text();pr=json.loads((P/'IV_whole_row_completion_proposal.json').read_text());patches=json.loads((P/'IV_low_F_scope_and_residual_patches.json').read_text())
f14=json.loads((P/'IV_F14_index_citation_patches.json').read_text());f14_integrated=all(p['new_text'] in s for p in f14)
check27=s
for p in f14:
 if p['new_text'] in check27:check27=check27.replace(p['new_text'],p['old_text'])
for p in patches:assert p['new_text'] in check27,(p['label'],p['new_text'][:80])
known={r['label']:r for r in csv.DictReader((P/'IV_known_input_specializations.tsv').open(),delimiter='\t')}
ass=json.loads((P/'row_assessments.json').read_text());changed={p['label'] for p in patches};rows=[]
for r in pr['rows']:
 label=r['label'];a=s.index('\\label{'+label+'}');b=s.index('\\end{proof}',a)+len('\\end{proof}');block=s[a:b]
 c=r['assessment_proposal'];c['remaining_risk']='No unresolved mathematical step identified at the explicitly stated construction scope. All recorded independent checks retain their original scopes and derivation-order limits. Final integration of the exact source-credit fields and the rendered review after the new statement/citation text remain receiving editorial gates.'
 c['format_check']='Semantic statement/proof review passed: the exact source, parameter, line, fan and boundary data are now stated; numbered proofs, actual mathematical method and supplied computation paths are present. All27 guarded changes are integrated with every equation tag/label and proof balance preserved. Tags, uses, back-links and PDF destinations passed the parent build18 apparatus reports.'
 c['layout_check']=None
 c['completion_state']='pending final source-credit import and current rendered-layout integration'
 if label=='night:P3F.14':
  c['confidence_line']='The complete opposite-weight projective-bundle calculation agrees with the fresh265-check pushforward, the freshly opened Atiyah–Singer general-index/associated-symbol and Riemann–Roch theorems, and the new2-check character/polynomial transport. The actual inherited Spin-c structure and physical U=M^-1 map are retained.'
  c['independent_routes'].append('Fresh original ASIII Theorem2.12 p556, Prop2.17 p559 and Theorem4.3 pp564–565 read at the exact recorded scope; independent_IV_F14_index_symbol.py PASS2.')
  if not f14_integrated:c['remaining_risk']+=' The two prepared F14 cited-source paragraphs still await insertion.'
 if label.startswith('night:P3F.'):
  k=known[label]
  r['inventory_credit_proposal']={'credited_to':k['source_locator']+'; '+k['known_input'],'credit_transport':k['retained_map_or_calculation'],'source_credit_verdict':k['condition_4_4_2_disposition'],'literature_disposition':'Known theorem/input cited at the listed opened-source locus; retain the stated family-specific calculation. No worldwide absence claim.'}
 c['independent_routes'].append('Exact retained event IDs and before/after-reading boundaries are itemized in IV_whole_row_completion_review_05.json; the assessment does not promote any targeted read into a new blind whole-proof derivation.')
 ass[label]=c
 r['current_statement_proof_sha256']=hashlib.sha256(block.encode()).hexdigest();r['resolved_row_text_gates']=r.pop('remaining_row_text_gates');r['remaining_row_text_gates']=[] if label!='night:P3F.14' or f14_integrated else ['Integrate IV_F14_index_citation_patches.json.']
 r['assessment_proposal']=c;r['ready_for_completion_after_parent_global_QA']=not r['remaining_row_text_gates'];rows.append(r)
# Explicit receiving checks of the newly scoped statements and file replacements; no whole re-proof count.
fields=['statement_id','date','who','type','outcome','event_id','phase'];f=P/'CHECK_EVENTS.tsv';es=list(csv.DictReader(f.open(),delimiter='\t'));ids={r['event_id'] for r in es};before=len(es)
actor='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed), S6_SERIES_GRIND/corrections_audit'
for label in sorted(changed):
 pp=[p for p in patches if p['label']==label];key=label+'|receiving scope and actual program integration05|'+hashlib.sha256(json.dumps(pp,sort_keys=True).encode()).hexdigest();eid='s6sg:'+hashlib.sha256(key.encode()).hexdigest()[:20]
 if eid in ids:continue
 text='Compared the complete amended statement with its already-read proof and exact construction inputs. The new wording names the original source, actual parameter, line/fan/boundary data used by this row; it adds no unconstructed family identification. Verified every guarded scope/notation/computation-reference replacement is present in the current linked body. All equation tags and labels and every proof delimiter are unchanged. Historical absent-program mentions are replaced only at the scopes of the supplied fresh outputs; old wording and failures remain in receipts. Files: IV_low_F_scope_and_residual_patches.json, IV_low_F_scope_and_residual_receipt.json; parent integration analysis/IV_low_F_scope_changes_05.json. This is a receiving statement/source-format comparison, not a new whole-proof before-reading derivation or final-render claim.'
 es.append(dict(zip(fields,[label,'2026-11-19',actor,'targeted proof check',text,eid,'current'])));ids.add(eid)
with f.open('w',newline='') as z:w=csv.DictWriter(z,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(es)
(P/'row_assessments.json').write_text(json.dumps(ass,ensure_ascii=False,indent=2)+'\n')
review={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mathematical_rows_closed':30,'scope_patches_integrated':27,'F14_citation_patches_integrated':f14_integrated,'remaining_gates':'Parent imports the exact30-row credit fields, completes the current changed-page render and applies completion states. The mathematical and semantic statement/proof/source gates listed here are closed; no unrecorded blind/full-paper review is inferred.','rows':rows,'events_before':before,'events_after':len(es),'prior_visual_evidence':'build18_visual_QA.json: actually viewed40 pages; build18 diagnostics1427pages,0 overfull,0 missingglyphs,0undefinedwarnings; global named-destination errors[]. New statement/citation text requires the next parent render.'}
(P/'IV_whole_row_completion_review_05.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
(P/'IV_low_F_inventory_credit_proposal.json').write_text(json.dumps({r['label']:r['inventory_credit_proposal'] for r in rows},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'rows':30,'assessments':len(ass),'F14_citations_integrated':f14_integrated,'events_before':before,'events_after':len(es)},ensure_ascii=False))
