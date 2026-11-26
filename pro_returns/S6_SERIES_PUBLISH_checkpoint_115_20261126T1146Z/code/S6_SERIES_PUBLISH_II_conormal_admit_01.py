#!/usr/bin/env python3
"""Admit the exact conormal comparison and its permanent definition identity."""
from pathlib import Path
import collections,csv,datetime as dt,difflib,hashlib,importlib.util,io,json,re
from S6_SERIES_PUBLISH_II_D10_census import valid as d10valid, fingerprint as d10fp
R=Path(__file__).resolve().parents[1]
P=R/'agents/continuation2_B/structure_global_01/conormal_01/final_v1'
PRE='S6_SERIES_PUBLISH_II_B2_conormal_'
O=R/'records/S6_SERIES_PUBLISH_II_conormal_admission_01'
MAN=str((O/'manifest.json').relative_to(R))
csv.field_size_limit(100_000_000)
sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
def readtab(n,sep='\t'):
 b=(R/n).read_bytes();rd=csv.DictReader(io.StringIO(b.decode()),delimiter=sep);return b,list(rd),rd.fieldnames
def tab(rows,fields,sep='\t',header=True):
 out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=fields,delimiter=sep,lineterminator='\n')
 if header:w.writeheader()
 w.writerows(rows);return out.getvalue().encode()
assert not O.exists()
idxp=P/(PRE+'final_index.json');assert sha(idxp.read_bytes())=='a68e5e9bae143f3ff35d94a06e6be01dbfb28d0971a4f87233de199c6bea2e1e'
ix=json.loads(idxp.read_text())
for f in ix['files']:
 b=(R/f['path']).read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['path']
before=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=before.decode()
assert sha(before)=='801959d21c1cd73b2ed826bdd466f359bc95808bfbbfe132c31389da1b0d2690'
guards=json.loads((P/(PRE+'guards.json')).read_text())
torsion=r'\item \SeriesRef{wbII:lem:torsion-identification}\quad Identification of the torsion subsheaf.'+'\n'
anchor=r'\item \SeriesRef{cdp:st:A.2.1}\quad The Jacobian fractional ideal for every reduced hypersurface.'+'\n'
definition=r'\item \SeriesRef{def:II:conormal-data}\quad Conormal and torsion notation.'+'\n'
for name,old,new in [('Further-remove-relocated-torsion',torsion,''),('Further-insert-definition-and-torsion',anchor,definition+torsion+anchor)]:
 guards.append(dict(id=name,old=old,new=new,old_sha256=sha(old.encode()),new_sha256=sha(new.encode())))
ranges=[]
for g in guards:
 assert s.count(g['old'])==1,g['id'];a=s.index(g['old']);ranges.append((a,a+len(g['old']),g['id']))
 assert sha(g['old'].encode())==g['old_sha256'] and sha(g['new'].encode())==g['new_sha256']
for a,b in zip(sorted(ranges),sorted(ranges)[1:]):assert a[1]<=b[0],(a,b)
new=s;inverse=[]
for g in guards:
 a=new.index(g['old']);inverse.append(dict(id=g['id'],offset=a,old=g['old'],new=g['new']))
 new=new[:a]+g['new']+new[a+len(g['old']):]
back=new
for g in reversed(inverse):
 a=g['offset'];assert back[a:a+len(g['new'])]==g['new'];back=back[:a]+g['old']+back[a+len(g['new']):]
assert back==s
identities={}
for name,pat,addition in [('labels',r'\\label\{[^}]+\}',r'\label{def:II:conormal-data}'),('targets',r'\\hypertarget\{[^}]+\}',r'\hypertarget{tag-P207}'),('records',r'\\StatementRecord\{[^}]+\}\{[^}]+\}\{[^}]+\}',r'\StatementRecord{def:II:conormal-data}{proved}{P207}')]:
 a=collections.Counter(re.findall(pat,s));b=collections.Counter(re.findall(pat,new));assert not a-b and b-a==collections.Counter({addition:1}),name
 identities[name]=dict(original=sum(a.values()),added=addition)
assert new.count(definition)==1 and new.count(torsion)==1
assert new.count((P/(PRE+'IF_original.tex')).read_text())==1
assert d10valid(new) and d10fp(new)==d10fp(s)
scanner=R/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_scan.py'
spec=importlib.util.spec_from_file_location('conormal_equation_scan',scanner);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
aa,_=mod.inventory(s);bb,_=mod.inventory(new)
assert len(aa['numbered_equations'])==len(bb['numbered_equations'])==1822
def payloads(text,inv):return collections.Counter(sha(text[x['display_start']:x['display_end']].encode()) for x in inv['numbered_equations'])
assert payloads(s,aa)==payloads(new,bb)
db,defects,df=readtab('S6_SERIES_PUBLISH_defects_II.tsv');added=[]
proposal=json.loads((P/(PRE+'defect_proposals.json')).read_text())
late=(P/(PRE+'five_unnumbered_original.tex')).read_text()
for i,d in enumerate(proposal['instances']):
 if i<5:
  needle=('\\begin{proof}['+d['location']+']') if i==1 else ('\\subsubsection*{'+d['location']+'}')
  a=late.index(needle);b=late.index(r'\end{proof}',a)+len(r'\end{proof}');old=late[a:b]
  owner=d['receiving_owner'];replacement=(P/(PRE+('AD' if i<3 else 'IK')+'_proposed.tex')).read_text()
 else:
  gid={5:'definition_and_torsion_lemma',6:'ambient_criterion_orphan',7:'IF'}[i];g=next(g for g in guards if g['id']==gid);old=g['old'];replacement=g['new']
  owner={5:'def:II:conormal-data',6:'cdp:st:A.2.4',7:'wbII:lem:torsion-identification'}[i]
  if i==6:replacement=(P/(PRE+'AI_proposed.tex')).read_text()
  if i==7:replacement=old
 for typ in d['types']:
  row={k:'' for k in df};row.update(change_id=f'II-CONORMAL-01-{len(added)+1:03}',type=typ,statement_id=owner,old_location=d['location'],old_page='historical source bound by exact guard',new_location=owner,new_page='pending integrated build',old_text=old,new_text=replacement,reason=d['reason']+' Full exact morphisms and alternative proofs are in the sealed conormal packet.',review_status='Admitted after full original/receiving comparison by B and root. Final page reading pending.');added.append(row)
for g in guards[-2:]:
 row={k:'' for k in df};row.update(change_id=f'II-CONORMAL-01-{len(added)+1:03}',type='D24',statement_id='def:II:conormal-data' if 'insert' in g['id'] else 'wbII:lem:torsion-identification',old_location='Further results / '+g['id'],new_location='Further results in current body order',old_page='prior source',new_page='pending integrated build',old_text=g['old'],new_text=g['new'],reason='Keep the front list synchronized with the new numbered standing definition and unchanged relocated lemma.',review_status='Exact existing title/owner transport; no mathematical event.');added.append(row)
eb,events,ef=readtab('CHECK_EVENTS.tsv');ev=list(csv.DictReader((P/(PRE+'event_proposals.tsv')).open(),delimiter='\t'))
assert len(ev)==5 and len({e['evidence_group'] for e in ev})==3
for e in ev:
 assert e['type']=='used and rechecked in this run' and e['event_id'] not in {x['event_id'] for x in events}
 e['who']='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation2 track B and root comparative review'
 e['source_file']=str(P.relative_to(R))+'/'+Path(e['source_file']).name;e['publish_input_file']=MAN
tb,tags,tf=readtab('S6_SERIES_PUBLISH_tags.tsv');assert not any(x['tag']=='P207' or x['label']=='def:II:conormal-data' for x in tags)
tp=json.loads((P/(PRE+'tag_proposal.json')).read_text());tags.append({k:tp.get(k,'') for k in tf})
ib,inv,inf=readtab('S6_SERIES_PUBLISH_inventory.csv',',');assert not any(x['label']=='def:II:conormal-data' for x in inv)
row={k:'' for k in inf};row.update(paper='II',label='def:II:conormal-data',source_run='S6_SERIES_PUBLISH',source_id='def:II:conormal-data',kind='Definition',status='proved',main_or_supporting='supporting',check_record='{}',source_paper='II',tag='P207',placement_state='printed in II',current_statement_owner='def:II:conormal-data',current_number='pending build',current_page='pending build',writing_state='Existing standing notation numbered with unchanged domain and exact first-use order.',confidence_state='Full exposed original/receiving comparison recorded; no independent derivation asserted.',completion_state='Full paper publication gates remain open.',layout_check='pending integrated rendered-page review',remaining_risk='Final source-wide, provenance, build and rendered-page review remain open.',assessment_source=MAN,current_source_sha256=sha(new.encode()));inv.append(row)
cb=(R/'S6_SERIES_PUBLISH_checks_II.md').read_bytes();assert b'<a id="tag-P207"></a>' not in cb
checkadd='\n<a id="tag-P207"></a>\n\n## P207 — II, number pending build\n\nLabel: `def:II:conormal-data`. Page: pending build.\n\nRecorded mathematical status: proved.\n\n### Recorded routes and present scope\n\nThe existing standing definition is transported with its exact domain; complete original/receiving comparison is recorded in `'+MAN+'`.\n\n<a id="uses-P207"></a>\n### Uses and used by\n\nUses: the displayed definition of the conormal sheaves.\n\nUsed by: the conormal filtration and subsequent section; final graph regeneration pending.\n\n### Entry provenance\n\nNew permanent tag for the previously unnumbered standing definition.\n\n### Check events\n\n'
rp=R/'records/S6_SERIES_PUBLISH_additional_event_bundles.json';rb=rp.read_bytes();reg=json.loads(rb);bundle=tab(ev,ef)
reg['bundles'].append(dict(path=str((O/'event_rows.tsv').relative_to(R)),bytes=len(bundle),sha256=sha(bundle),admission_manifest=MAN))
now=dt.datetime.now(dt.timezone.utc).isoformat();O.mkdir()
(O/'inverse.json').write_bytes(enc(inverse));(O/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before conormal admission01',tofile='II after conormal admission01')))
(O/'defect_rows.tsv').write_bytes(tab(added,df));(O/'event_rows.tsv').write_bytes(bundle)
reading=dict(recorded_utc=now,full_root_reading=[bind(P/(PRE+n)) for n in ['mathematical_map.md','definition_proposed.tex','AD_original.tex','AD_proposed.tex','AI_original.tex','AI_proposed.tex','IK_original.tex','IK_proposed.tex','five_unnumbered_original.tex','AF_supporting_input.tex','AG_supporting_input.tex','AE_supporting_input.tex','IF_original.tex']],standing_definition_and_AJ_following_paragraph='Both complete original guards were displayed and read; the application moves verbatim to AI. Root does not claim another complete AJ reading.',agent_full_reading=bind(P/(PRE+'reading_receipt.json')),scope='Complete exposed comparative reading; the five alternative proofs remain in the sealed original. No independent, targeted or required-row credit.',numbered_equations=1822,all_numbered_payloads_byte_identical=True,scanner=bind(scanner))
(O/'root_reading.json').write_bytes(enc(reading))
changes=[('S6_SERIES_PUBLISH_II.tex',before,new.encode()),('S6_SERIES_PUBLISH_defects_II.tsv',db,db+tab(added,df,header=False)),('CHECK_EVENTS.tsv',eb,eb+tab(ev,ef,header=False)),('S6_SERIES_PUBLISH_tags.tsv',tb,tab(tags,tf)),('S6_SERIES_PUBLISH_inventory.csv',ib,tab(inv,inf,',')),('S6_SERIES_PUBLISH_checks_II.md',cb,cb+checkadd.encode()),('records/S6_SERIES_PUBLISH_additional_event_bundles.json',rb,enc(reg))]
for n,b,a in changes[3:]:(O/(Path(n).name+'.diff')).write_text(''.join(difflib.unified_diff(b.decode().splitlines(True),a.decode().splitlines(True),fromfile=n+' before',tofile=n+' after')))
manifest=dict(created_utc=now,source_before_sha256=sha(before),source_after_sha256=sha(new.encode()),sealed_index=bind(idxp),sealed_bindings_verified=len(ix['files']),unique_disjoint_guards=len(guards),exact_inverse=True,identities_preserved=identities,new_permanent_tag='P207',retired_duplicate_proofs=5,numbered_equation_payloads_preserved=1822,events_added=5,event_groups=3,ledger_rows_before=len(events),ledger_rows_after=len(events)+5,defect_rows_added=len(added),defect_rows_after=len(defects)+len(added),new_mathematical_errors=0,required_rows_closed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,D10_fingerprint_unchanged=d10fp(new),D16_next_step='Explicitly transport the complete header audit across the new definition and relocated model display before claiming current closure.',canonical_changes=[dict(path=n,before_bytes=len(b),before_sha256=sha(b),after_bytes=len(a),after_sha256=sha(a)) for n,b,a in changes],evidence=[bind(p) for p in sorted(O.iterdir())],code=bind(Path(__file__)))
mp=O/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
for n,b,a in changes:assert (R/n).read_bytes()==b,n
for n,b,a in changes:(R/n).write_bytes(a)
note=f'''\n\n## Paper II: conormal, torsion and conductor consolidation — {now}\n\nFive repeated unnumbered proofs are archived after complete original/receiving comparison. Their sheaf maps, stalk identifications, connecting morphisms and conductor-square maps are explicitly identified with the retained proofs. All1822 numbered equation payloads and every existing label, target and statement record remain unchanged. Four displays move to their actual receiving proofs or statement. Existing standing notation is now Definition P207; the unchanged torsion-identification lemma follows it before first use. The ordinary/cuspidal kernel application moves verbatim into its proving proposition. The Further results list follows these exact changes.\n\nThe sealed admission `{mb['path']}` (SHA-256 `{mb['sha256']}`) adds five exposed-reread events in three evidence groups and {len(added)} individual class records. Source SHA-256 `{sha(new.encode())}`; ledger {len(events)+5} rows. Root and B read all five retired proofs and the full receiving blocks. No mathematical error, independent check, required-row closure, global defect-class closure or final-PDF page credit is asserted. D10's current validator remains satisfied; D16's new header projection awaits the explicit renewed reading binding.\n'''
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(O/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,canonical_after_bindings=[bind(R/n) for n,_,_ in changes],no_prior_events_changed_or_deleted=True)))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','unique_disjoint_guards','ledger_rows_after','defect_rows_added','defect_rows_after']},indent=2));print('Manifest',mb['sha256'])
