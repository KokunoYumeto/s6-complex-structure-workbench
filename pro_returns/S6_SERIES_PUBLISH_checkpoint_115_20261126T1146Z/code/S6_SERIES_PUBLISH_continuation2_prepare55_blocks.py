from pathlib import Path
import datetime as dt,hashlib,json,re
R=Path(__file__).resolve().parents[1]
def bind(p):return {'path':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()}
def read(p):return json.loads((R/p).read_text())
def verify(o):
 if isinstance(o,dict):
  if 'path' in o and 'sha256' in o:assert bind(o['path'])['sha256']==o['sha256'],o['path']
  for v in o.values():verify(v)
 elif isinstance(o,list):
  for v in o:verify(v)
scope='records/S6_SERIES_PUBLISH_II_FK_FL_FM_root_scope_disposition.json'
assert not (R/scope).exists()
s=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
a=s.index('\\paragraph{Standing torus-fibration setting.}');b=s.index('\\subsection',a)
standing=s[a:b]
assert 'The ambient space is a smooth compact complex threefold $Y$' in standing
(R/scope).write_text(json.dumps(dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),standing_paragraph=standing,
 source=bind('S6_SERIES_PUBLISH_II.tex'),scope_audit=bind('agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_FK_FL_FM_scope_review_v1.md'),
 decision='Restate the already supplied smooth ambient assumption in each of the three statement openings, resolving its ambiguous reach across the intervening section heading. The three proofs use exactly that standing Y. The direct identity map on Y, on f, on every full fibre and on Pic(Y) transports the objects; no desingularization, base change or changed ambient space is involved. FL imports only smoothness in its first assertion; its torus-general-fibre hypothesis remains solely in its later clause.',
 mathematical_scope='The proved statements concern smooth compact complex threefolds with the listed Betti and fibration assumptions. No assertion that fibre forms alone imply smoothness is made. The local uv=q^m example fails the implication from fibre form alone but supplies no global counterexample with all these hypotheses. No broader singular-space claim or refutation is credited.',
 changes=[{'owners':['cdp:st:C4a','cdp:st:C4b','cdp:st:C4c'],'kind':'explicit restatement of existing smooth standing domain','reason':'Remove cross-section ambiguity and expose the domain of the tangent-bundle, Cartier-duality and index inputs.'},{'owner':'cdp:st:C4c','kind':'complete an omitted proof deduction','reason':'The original statement cites A.3.5 for irreducibility; the final proof now applies it through L -> K_Y tensor L^-1, as already established before release.'}],
 unchanged='All conclusions, displayed numbers, original proof steps, full-fibre multiplicities, labels and permanent tags are preserved. No statement-refutation event is justified by this scope clarification.',new_check_events=0),indent=2)+'\n')
titles={'01FK':('A geometric replacement on an explicit fibre class','Generic tangent cohomology vanishing'),'01FL':('An unavoidable failure on a rational homology six-sphere','Twisted tangent cohomology on rational homology six-spheres'),'01FM':('The finite singular-fibre test and a fixed unavoidable fibre','A finite cohomology test and a fixed fibre')}
blocks=[]
for tag,items in [('01FK',7),('01FL',2),('01FM',5)]:
 p=f'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_{tag}_final_v1'
 idx=read(p+'_index.json');verify(idx)
 pr=read(p+'_proposals.json')['blocks'][0];o=(R/pr['original_full_block']['path']).read_text();v1=(R/pr['proposed_full_block']['path']).read_text();w=o
 guards=[dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason']) for g in pr['guards']]
 for g in guards:assert w.count(g['old'])==1;w=w.replace(g['old'],g['new'])
 assert w==v1
 extra=[]
 def add(old,new,typ,reason):
  global w
  assert w.count(old)==1,(tag,old)
  w=w.replace(old,new);extra.append(dict(old=old,new=new,type=typ,reason=reason))
 old='compact connected complex threefold' if tag=='01FK' else 'compact complex threefold'
 new='smooth compact connected complex threefold' if tag=='01FK' else 'smooth compact complex threefold'
 add(old,new,'D20,D22','Expose the existing smooth ambient domain in the statement itself; exact scope disposition is separately recorded.')
 add('We use the smooth ambient setting stated at the beginning of\nSection~\\ref{sec:II:night-sign}.\n\n','','D18,D22','The statement now explicitly gives the existing smooth ambient assumption; remove the redundant cross-section import.')
 add('['+titles[tag][0]+']','['+titles[tag][1]+']','D02,D16','Use a mathematical title naming the result.')
 if tag=='01FL':add('Within the fibre class of \\ref{cdp:st:C4a},','For the two fibre forms listed in \\ref{cdp:st:C4a},','D20,D22','Make the same fibre-form scope explicit in the statement; the additional normalization condition is not part of this clause.')
 if tag=='01FM':add('computed in A.2.','computed in \\ref{cdp:st:A.2.1}.','D04,D18','Resolve the coefficient-ideal input by its statement label.')
 assert o.count('\\item ')==w.count('\\item ')==items
 assert re.findall(r'\\\[(.*?)\\\]',o,re.S)==re.findall(r'\\\[(.*?)\\\]',w,re.S)
 assert re.findall(r'\\label\{[^}]+\}',o)==re.findall(r'\\label\{[^}]+\}',w)
 assert re.findall(r'\\hypertarget\{[^}]+\}\{\}',o)==re.findall(r'\\hypertarget\{[^}]+\}\{\}',w)
 dest=f'agents/continuation2_root/S6_SERIES_PUBLISH_II_{tag}_root_v2_proposed.tex';assert not (R/dest).exists();(R/dest).write_text(w)
 blocks.append(dict(tag=tag,owner=pr['statement_owner'],index=bind(p+'_index.json'),original=pr['original_full_block'],proposed=bind(dest),agent_proposed=pr['proposed_full_block'],freeze=idx['freeze_receipt'],release=idx['release_receipt'],events=bind(p+'_event_proposals.json'),comparison=idx['comparison'],guards=guards+extra,original_items=items,root_extension_guards=extra))
out='records/S6_SERIES_PUBLISH_II_batch55_prepared_blocks.json';assert not (R/out).exists();(R/out).write_text(json.dumps(dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),scope_disposition=bind(scope),blocks=blocks,root_complete_final_v2_reading_pending=True),indent=2)+'\n')
print(json.dumps({'prepared':bind(out),'blocks':[{k:v for k,v in x.items() if k in ['tag','proposed','original_items']} for x in blocks]},indent=2))
