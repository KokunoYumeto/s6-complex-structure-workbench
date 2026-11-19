"""Full current retained-argument corrections; historical compounds stay refuted."""
retained_repairs=[]
for relative in ['analysis/IV/retained_batch_9/receiving_replacements.json','analysis/IV_root_retained/receiving_replacements.json','analysis/IV_sign_second_replacements.json','analysis/IV_retained_batch/receiving_replacements.json','analysis/IV_sign_third_replacements.json']:
 p=W/relative
 if not p.exists():continue
 for e in json.loads(p.read_text()):
  old=e.get('old',e.get('exact_old'));new=e.get('new',e.get('exact_new'))
  if (e['label']=='night:P3K.60'
      and old.startswith('The old absolute pair is refuted; K69 proves')):
   # The earlier deterministic correction already removes the source's
   # obsolete prefatory paragraph. Transport the peer's completed-scope
   # clarification to the actual corrected statement, preserving its
   # existing absolute-calculation locator and the full raw source repair.
   e=dict(e,source_prefatory_old=old,source_prefatory_new=new)
   old=r'''The same \(e\) occurs in the two entries of a given pair. This particular sum-and-difference argument does not select its value; the completed absolute calculation is \cref{night:P3K.88}. No class in \(\Theta_7\) is divided by two.'''
   new=r'''The same \(e\) occurs in both entries. This sum-and-difference
argument, and the corresponding argument in \cref{night:P3K.69},
leave its value unselected. The separate compact attachments of
\cref{night:P3K.80,night:P3K.83} select \(e=0\) in their stated
reduced and good branches, respectively, retaining their realized
norm signs and finite characters. The complete fan witnesses are
given in \cref{night:P3K.88}. No class in \(\Theta_7\) is divided by two.'''
   e.update(old=old,new=new,reason=e['reason']+' Transport this clarification from the already removed source preface to the actual corrected receiving statement.')
  def replace(t,e=e,old=old,new=new):
   expected=e.get('expected_count',1);assert t.count(old)==expected,(e['label'],t.count(old),expected,old[:100])
   return t.replace(old,new) if e.get('replace_all') else t.replace(old,new,1)
  change(e['label'],replace,e['reason']);retained_repairs.append(dict(source=relative,**e))
uses_path=W/'analysis/IV_root_retained/uses_receiving_replacements.json'
if uses_path.exists():
 for e in json.loads(uses_path.read_text()):
  def replace_uses(t,e=e):
   assert t.count(e['exact_old_uses'])==1,(e['label'],'Uses',t.count(e['exact_old_uses']))
   return t.replace(e['exact_old_uses'],e['exact_new_uses'],1)
  change(e['label'],replace_uses,e['reason'])
  retained_repairs.append(dict(source=str(uses_path.relative_to(W)),**e))
for lab,extra in {
 'night:P3F.25':r'\cref{night:P3K.68,night:P3K.69}',
 'night:P3F.53':r'\cref{night:P3F.54,night:P3F.56,night:P3K.45,night:P3K.46,night:P3K.65,night:P3K.68,night:P3K.71,night:P3K.77}; \cite[Remark~8.5, p.~24]{Engel2026}',
 'night:P3K.40':r'\cref{night:P3K.68}',
 'night:P3K.41':r'\cite[Remark~8.3, pp.~22--23]{Engel2026}',
 'night:P3K.44':r'\cref{night:P3K.65,night:P3K.77}',
 'night:P3K.45':r'\cref{night:P3K.68}',
 'night:P3K.46':r'\cref{night:P3K.68}'
 ,'night:P3K.60':r'\cref{night:P3K.68,night:P3K.69}; the separately completed absolute branch attachments of \cref{night:P3K.80,night:P3K.83} and full fan witnesses of \cref{night:P3K.88}'
}.items():
 change(lab,lambda t,u=extra:add_uses(t,u),'Record the actual corrected line, fan, endpoint or exact known-construction dependency used by the complete retained proof.')
(W/'analysis/IV/retained_batch_9/integration_reconciliation.json').write_text(json.dumps(retained_repairs,indent=2)+'\n')
