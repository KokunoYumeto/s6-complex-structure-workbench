#!/usr/bin/env python3
"""Admit the complete push-stability orphan comparison and period definition."""
from pathlib import Path
import collections,csv,datetime as dt,difflib,hashlib,io,json,re
from S6_SERIES_PUBLISH_II_D10_census import valid as d10valid,fingerprint as d10fp
R=Path(__file__).resolve().parents[1]
P=R/'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_D13_push_v1';V=P/'S6_SERIES_PUBLISH_II_C2_D13_review_v2'
PRE='S6_SERIES_PUBLISH_II_C2_D13_';O=R/'records/S6_SERIES_PUBLISH_II_push_structure_admission_01';MAN=str((O/'manifest.json').relative_to(R))
csv.field_size_limit(100_000_000);sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
def readtab(n,sep='\t'):
 b=(R/n).read_bytes();rd=csv.DictReader(io.StringIO(b.decode()),delimiter=sep);return b,list(rd),rd.fieldnames
def tab(rows,fields,sep='\t',header=True):
 out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=fields,delimiter=sep,lineterminator='\n')
 if header:w.writeheader()
 w.writerows(rows);return out.getvalue().encode()
assert not O.exists();index=P/(PRE+'final_v2_index.json');assert sha(index.read_bytes())=='ddbc93a1be08aea2b920db862a91bd697c319c33bae118782ad8a3e78b25d95b'
ix=json.loads(index.read_text());verified={}
def verify_tree(value):
 if isinstance(value,dict):
  if {'path','bytes','sha256'}<=value.keys():
   p=R/value['path'];b=p.read_bytes();assert len(b)==value['bytes'] and sha(b)==value['sha256'],value['path'];verified[value['path']]=value['sha256']
  for v in value.values():verify_tree(v)
 elif isinstance(value,list):
  for v in value:verify_tree(v)
verify_tree(ix)
review=json.loads((R/ix['review_index']['path']).read_text());verify_tree(review)
before=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=before.decode();assert sha(before)=='be370468779bb61f7445fd062bbcecf1b0054cc190789e5dab79466636dc5155'
intake=json.loads((R/ix['intake']['path']).read_text());owners=intake['owners'];assert len(owners)==26
for row in owners:
 b=(R/row['path']).read_bytes();assert sha(b)==row['sha256'] and len(b)==row['bytes'];assert s.count(b.decode())==1,row['owner']
guards=json.loads((R/ix['guards']['path']).read_text());assert len(guards)==17
anchor=r'\item \SeriesRef{push:src:E.5.3}\quad Biholomorphism classes in the two-parameter family.'+'\n'
entry=r'\item \SeriesRef{def:II:two-parameter-period-data}\quad Two-parameter period data.'+'\n'
guards.append(dict(id='Further-P208',old=anchor,new=entry+anchor,old_sha256=sha(anchor.encode()),new_sha256=sha((entry+anchor).encode())))
ranges=[]
for g in guards:
 assert sha(g['old'].encode())==g['old_sha256'] and sha(g['new'].encode())==g['new_sha256']
 assert s.count(g['old'])==1,g['id'];a=s.index(g['old']);ranges.append((a,a+len(g['old']),g['id']))
for a,b in zip(sorted(ranges),sorted(ranges)[1:]):assert a[1]<=b[0],(a,b)
new=s;inverse=[]
for g in guards:
 a=new.index(g['old']);inverse.append(dict(id=g['id'],offset=a,old=g['old'],new=g['new']));new=new[:a]+g['new']+new[a+len(g['old']):]
phrase_old='Thus they identify the two presentations of the same\n$\\lambda$-labelled family, and differences of $c$ at fixed $\\mu$\nare unchanged.'
phrase_new='Thus they identify the two presentations over the displayed\nparameter-coordinate map, and differences of $c$ at fixed $\\mu$\nare unchanged.'
assert new.count(phrase_old)==1;a=new.index(phrase_old);inverse.append(dict(id='root-exact-parameter-map-wording',offset=a,old=phrase_old,new=phrase_new));new=new[:a]+phrase_new+new[a+len(phrase_old):]
back=new
for g in reversed(inverse):
 a=g['offset'];assert back[a:a+len(g['new'])]==g['new'];back=back[:a]+g['old']+back[a+len(g['new']):]
assert back==s
old53=(V/(PRE+'E53-period-comparison_old.tex')).read_text();sealed53=(V/(PRE+'E53_proposed.tex')).read_text();new53=sealed53.replace(phrase_old,phrase_new)
assert new.count(new53)==1 and s.count(old53)==1
tail=r'\item The intrinsic fibration is the anticanonical pencil.'
assert old53[old53.index(tail):]==new53[new53.index(tail):]
assert old53.count(r'\item')==new53.count(r'\item')==9
math=lambda x:re.findall(r'\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$(?!\$).*?(?<!\\)\$',x,re.S)
oldstatement=old53[:old53.index(r'\end{theorem}')];newstatement=new53[:new53.index(r'\end{theorem}')]
assert math(oldstatement)==math(newstatement)
ds=lambda x:re.findall(r'\\\[(.*?)\\\]',x,re.S)
it=iter(ds(new53));assert all(any(z==d for z in it) for d in ds(old53))
p208=(V/(PRE+'P208_proposed.tex')).read_text();gap127=(V/(PRE+'gap-127_old.tex')).read_text();assert ds(p208)==ds(gap127) and len(ds(p208))==2
for row in owners:
 if row['owner']!='push:src:E.5.3':assert new.count((R/row['path']).read_text())==1,row['owner']
identities={}
for name,pat,add in [('labels',r'\\label\{[^}]+\}',r'\label{def:II:two-parameter-period-data}'),('targets',r'\\hypertarget\{[^}]+\}',r'\hypertarget{tag-P208}'),('records',r'\\StatementRecord\{[^}]+\}\{[^}]+\}\{[^}]+\}',r'\StatementRecord{def:II:two-parameter-period-data}{proved}{P208}')]:
 aa=collections.Counter(re.findall(pat,s));bb=collections.Counter(re.findall(pat,new));assert not aa-bb and bb-aa==collections.Counter({add:1});identities[name]=dict(preserved=sum(aa.values()),added=add)
assert d10valid(new) and d10fp(new)==d10fp(s)
db,defs,df=readtab('S6_SERIES_PUBLISH_defects_II.tsv');added=[];classes=json.loads((R/ix['final_instance_classifications']['path']).read_text());byguard={g['id']:g for g in guards}
for row in classes['rows']:
 g=byguard[row['guard_id']]
 for typ in row['final_defect_types']:
  d={k:'' for k in df};d.update(change_id=f'II-PUSH-STRUCTURE-01-{len(added)+1:03}',type=typ,statement_id=row['owner'],old_location=row['guard_id'],old_page='source guard and complete original owner bound',new_location=row['owner']+' / '+row['reason_locus'],new_page='pending integrated build',old_text=g['old'],new_text=new53 if row['guard_id']=='D13-E53-period-comparison' else g['new'],reason='Complete exact mathematical ownership map: '+str((P/(PRE+'comparison_v2.md')).relative_to(R))+' / '+row['reason_locus'],review_status='All26 supplying/owning proofs and16 original gaps fully read by C. Root read all16 original gaps, complete old/new E5.3, P208, full E5.2 and the full comparison; exact rebase/inverse verified. No independent, required, class or final-page credit.');added.append(d)
d={k:'' for k in df};d.update(change_id=f'II-PUSH-STRUCTURE-01-{len(added)+1:03}',type='D24',statement_id='def:II:two-parameter-period-data',old_location='Further results',old_page='prior source',new_location='Further results before E.5.3',new_page='pending integrated build',old_text=anchor,new_text=entry+anchor,reason='Synchronize the front list with numbered Definition P208 and its exact current title.',review_status='Exact owner/title insertion; no mathematical event.');added.append(d)
eb,events,ef=readtab('CHECK_EVENTS.tsv');ev=[]
for e in json.loads((R/ix['event_proposals']['path']).read_text())['events']:
 assert e['type']=='used and rechecked in this run' and e['event_id'] not in {x['event_id'] for x in events}
 row={k:e.get(k,'') for k in ef};row.update(who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation2_C, with root admission review',phase='publication editorial comparison',source_event_type=e['type'],source_file=ix['comparison']['path'],publish_input_file=MAN);ev.append(row)
assert len(ev)==27 and len({x['evidence_group'] for x in ev})==3
tb,tags,tf=readtab('S6_SERIES_PUBLISH_tags.tsv');assert not any(x['tag']=='P208' for x in tags)
row={k:'' for k in tf};row.update(tag='P208',paper='II',number='pending build',page='pending build',label='def:II:two-parameter-period-data',status='proved',kind='definition',current_owner='def:II:two-parameter-period-data',publication_disposition='Existing period data numbered with exact formulas and domain; coordinate comparison moved to its owning proof.');tags.append(row)
ib,inv,inf=readtab('S6_SERIES_PUBLISH_inventory.csv',',');assert not any(x['label']=='def:II:two-parameter-period-data' for x in inv)
row={k:'' for k in inf};row.update(paper='II',label='def:II:two-parameter-period-data',source_run='S6_SERIES_PUBLISH',source_id='def:II:two-parameter-period-data',kind='Definition',status='proved',main_or_supporting='supporting',check_record='{}',source_paper='II',tag='P208',uses='push:src:E.5.2',placement_state='printed in II',current_statement_owner='def:II:two-parameter-period-data',current_number='pending build',current_page='pending build',writing_state='Existing exact period data numbered immediately before use.',confidence_state='Exposed complete comparative review; two original displays transported verbatim.',completion_state='Full paper publication gates remain open.',layout_check='pending integrated rendered-page review',remaining_risk='Final source-wide, provenance, build and rendered-page review remain open.',assessment_source=MAN,current_source_sha256=sha(new.encode()));inv.append(row)
cb=(R/'S6_SERIES_PUBLISH_checks_II.md').read_bytes();assert b'<a id="tag-P208"></a>' not in cb
checkadd='\n<a id="tag-P208"></a>\n\n## P208 — II, number pending build\n\nLabel: `def:II:two-parameter-period-data`. Page: pending build.\n\nRecorded mathematical status: proved.\n\n### Recorded routes and present scope\n\nExact existing period data, with two displays retained verbatim. Admission: `'+MAN+'`.\n\n<a id="uses-P208"></a>\n### Uses and used by\n\nUses: `push:src:E.5.2`.\n\nUsed by: `push:src:E.5.3`; final graph regeneration pending.\n\n### Entry provenance\n\nThe coordinate comparison shares its exposed reading with E.5.3.\n\n### Check events\n\n'
rp=R/'records/S6_SERIES_PUBLISH_additional_event_bundles.json';rb=rp.read_bytes();reg=json.loads(rb);bundle=tab(ev,ef);reg['bundles'].append(dict(path=str((O/'event_rows.tsv').relative_to(R)),bytes=len(bundle),sha256=sha(bundle),admission_manifest=MAN))
now=dt.datetime.now(dt.timezone.utc).isoformat();O.mkdir();(O/'inverse.json').write_bytes(enc(inverse));(O/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before push structure01',tofile='II after push structure01')));(O/'defect_rows.tsv').write_bytes(tab(added,df));(O/'event_rows.tsv').write_bytes(bundle)
(O/'root_reading.json').write_bytes(enc(dict(recorded_utc=now,full_comparison=bind(P/(PRE+'comparison_v2.md')),full_root_original_gaps=[bind(V/(PRE+f'gap-{i}_old.tex')) for i in list(range(114,129))+[130]],full_E53_original=bind(V/(PRE+'E53-period-comparison_old.tex')),full_E53_sealed_receiving=bind(V/(PRE+'E53_proposed.tex')),full_P208=bind(V/(PRE+'P208_proposed.tex')),full_supporting_E52=bind(P/(PRE+'push_src_E_5_2_original.tex')),root_phrase_guard=dict(old=phrase_old,new=phrase_new,reason='The exact parameter map changes the numeric lambda coordinate while preserving lambda times the chosen generator; wording now explicitly names that base map.'),covariance='Root checked all four products against the displayed H_i column by column: i1/i3 give Pi; i2 and i* give exactly the four common columns in C comparison. Exposed algebraic verification, no additional event.',limits='C read all26 originals; root does not claim another complete26-proof reading. Root read the new first-item insertion, full receiving block and every unchanged remaining item. No unopened I/V claim is imported.')))
changes=[('S6_SERIES_PUBLISH_II.tex',before,new.encode()),('S6_SERIES_PUBLISH_defects_II.tsv',db,db+tab(added,df,header=False)),('CHECK_EVENTS.tsv',eb,eb+tab(ev,ef,header=False)),('S6_SERIES_PUBLISH_tags.tsv',tb,tab(tags,tf)),('S6_SERIES_PUBLISH_inventory.csv',ib,tab(inv,inf,',')),('S6_SERIES_PUBLISH_checks_II.md',cb,cb+checkadd.encode()),(str(rp.relative_to(R)),rb,enc(reg))]
for n,b,a in changes[3:]:(O/(Path(n).name+'.diff')).write_text(''.join(difflib.unified_diff(b.decode().splitlines(True),a.decode().splitlines(True),fromfile=n+' before',tofile=n+' after')))
manifest=dict(created_utc=now,sealed_index=bind(index),sealed_bindings_verified=len(verified),source_before_sha256=sha(before),source_after_sha256=sha(new.encode()),sealed_guards=17,additional_front_guard=1,root_exact_map_wording_guard=1,exact_inverse=True,original_owners_checked=26,unchanged_owner_blocks=25,E53_original_items_preserved=9,E53_statement_mathematics_unchanged=True,E53_downstream_statement_change_trigger=False,new_permanent_tag='P208',identities_preserved=identities,events_added=27,event_groups=3,ledger_rows_before=len(events),ledger_rows_after=len(events)+27,defect_rows_added=len(added),defect_rows_after=len(defs)+len(added),required_rows_closed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,new_mathematical_errors=0,D10_fingerprint_unchanged=d10fp(new),D16_next_step='Explicitly bind the new P208 header to the full reading and transport all prior projections.',canonical_changes=[dict(path=n,before_sha256=sha(b),after_sha256=sha(a),before_bytes=len(b),after_bytes=len(a)) for n,b,a in changes],evidence=[bind(p) for p in sorted(O.iterdir())],code=bind(Path(__file__)))
mp=O/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
for n,b,a in changes:assert (R/n).read_bytes()==b,n
for n,b,a in changes:(R/n).write_bytes(a)
note=f'''\n\n## Paper II: period data and deformation-proof organization — {now}\n\nSixteen interstatement spans were compared with26 complete owning/supplying proofs. Repeated scope recaps and production/search history are archived through exact guards and mathematical owner maps. Existing period data are numbered P208, with both original displays unchanged; the generator-change and four covariance identities are in E.5.3's first proof item. Their explicit maps and inverses preserve the period matrix and scaled generator. The wording identifies the actual parameter-coordinate change. All nine original E.5.3 items remain, and its hypotheses and conclusions are unchanged; the downstream statement-change trigger is inactive. Twenty-five other complete proof blocks remain byte-identical.\n\nThe admission `{mb['path']}` (SHA-256 `{mb['sha256']}`) adds27 actual used-and-rechecked associations in three shared groups and {len(added)} individual class records. Source SHA-256 `{sha(new.encode())}`; ledger {len(events)+27} rows. Root read every original gap, the full original/receiving E.5.3, P208, complete E.5.2 and the entire comparison map; C read all26 originals. No independent/computation event, required-row closure, global-class closure or final-page credit is claimed. D16 requires its explicit new-definition header binding.\n'''
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(O/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,canonical_after_bindings=[bind(R/n) for n,_,_ in changes],no_prior_events_changed_or_deleted=True)))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','ledger_rows_after','defect_rows_added','defect_rows_after']},indent=2));print('Manifest',mb['sha256'])
