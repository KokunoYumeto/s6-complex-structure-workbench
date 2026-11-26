#!/usr/bin/env python3
"""Admit the fully compared nodal-family consolidation, retaining every identity."""
from pathlib import Path
import collections,csv,datetime as dt,difflib,hashlib,importlib.util,io,json,re
from S6_SERIES_PUBLISH_II_D10_census import valid as d10valid, fingerprint as d10fp
R=Path(__file__).resolve().parents[1]
P=R/'agents/continuation2_B/structure_global_01/nodal_01/final_v1'
PRE='S6_SERIES_PUBLISH_II_B2_nodal_'
O=R/'records/S6_SERIES_PUBLISH_II_nodal_admission_01'
MAN=str((O/'manifest.json').relative_to(R));csv.field_size_limit(100_000_000)
sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
def table(n,sep='\t'):
 b=(R/n).read_bytes();rd=csv.DictReader(io.StringIO(b.decode()),delimiter=sep);return b,list(rd),rd.fieldnames
def tab(rows,fields,sep='\t',header=True):
 o=io.StringIO(newline='');w=csv.DictWriter(o,fieldnames=fields,delimiter=sep,lineterminator='\n')
 if header:w.writeheader()
 w.writerows(rows);return o.getvalue().encode()
assert not O.exists()
idxp=P/(PRE+'final_index.json');assert sha(idxp.read_bytes())=='e8739a881f18cf7bf183a0c60fab9b611511e2579bfa6921d8a5ad9a7af2a9ca'
ix=json.loads(idxp.read_text())
for f in ix['files']:
 b=(R/f['path']).read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['path']
before=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=before.decode()
assert sha(before)=='85019794d2d5c67f432eb59525958512b8bd90a53fe9aa6a700d77a35259e37c'
guards=json.loads((P/(PRE+'guards.json')).read_text())
entry=guards[0]['new'];assert guards[0]['id']=='further:wbII:lem:gluing-bundle'
guards[0]['new']='';guards[0]['new_sha256']=sha(b'')
anchor='\\item \\SeriesRef{cdp:st:B2}\\quad A projective example with twelve length-one contributions.\n'
guards.append(dict(id='root-further-B1-in-body-order',old=anchor,new=entry+anchor,old_sha256=sha(anchor.encode()),new_sha256=sha((entry+anchor).encode())))
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
for name,pat,extra in [('labels',r'\\label\{[^}]+\}',None),('targets',r'\\hypertarget\{[^}]+\}',None),('records',r'\\StatementRecord\{[^}]+\}\{[^}]+\}\{[^}]+\}',r'\StatementRecord{wbII:rem:scope}{proved}{03IS}')]:
 a=collections.Counter(re.findall(pat,s));b=collections.Counter(re.findall(pat,new));assert not a-b
 assert b-a==(collections.Counter({extra:1}) if extra else collections.Counter()),name
 identities[name]=dict(original=sum(a.values()),added=extra)
assert new.count(entry)==1 and new.index(entry)<new.index(anchor)
assert d10valid(new) and d10fp(s)==d10fp(new)
scanner=R/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_scan.py'
spec=importlib.util.spec_from_file_location('nodal_current_equations',scanner);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
aa,ab=m.inventory(s);bb,bc=m.inventory(new);ab={x['start']:x for x in ab};bc={x['start']:x for x in bc}
aliases=json.loads((P/(PRE+'equation_alias_map.json')).read_text());am={x['old_tag']:x for x in aliases}
def payload(text,b):
 p=text[b['begin_end']:b['end_start']];p=re.sub(r'\\hypertarget\{[^{}]+\}\{\}','',p);p=re.sub(r'\\label\{[^{}]+\}','',p)
 return p.replace(r'\SsixEquationAliases{}','').strip()
nt={x['old_tag']:x for x in bb['numbered_equations'] if x['old_tag']};nl={l:x for x in bb['numbered_equations'] for l in x['labels']}
same=0;changed=[]
for x in aa['numbered_equations']:
 target=am[x['old_tag']]['target_tag'] if x['old_tag'] in am else x['old_tag'];y=nt[target] if target else nl[x['labels'][0]]
 pa=payload(s,ab[x['display_start']]);pb=payload(new,bc[y['display_start']])
 if pa==pb:same+=1
 else:
  assert x['old_tag'] in set(am)|{'W.161'},x['old_tag']
  changed.append(dict(original_tag=x['old_tag'],receiving_tag=y['old_tag'],old_sha256=sha(pa.encode()),new_sha256=sha(pb.encode())))
assert len(aa['numbered_equations'])==1822 and len(bb['numbered_equations'])==1817 and same==1816
late=(P/(PRE+'nodal_original_region.tex')).read_text();receiver=(P/(PRE+'B1_proposed.tex')).read_text()
for n in ['IB_original.tex','I9_original.tex']:assert (P/(PRE+n)).read_text() in late
def oldproof(heading):
 a=late.index(heading);b=late.index(r'\end{proof}',a)+len(r'\end{proof}');return late[a:b]
oldtexts=[oldproof(r'\subsubsection*{Conductor proof'),oldproof(r'\subsubsection*{Explicit normalization'),(P/(PRE+'IB_original.tex')).read_text(),(P/(PRE+'I9_original.tex')).read_text(),oldproof(r'\subsubsection*{The local torsion'),late[late.index(r'\paragraph{what the theorem'):]]
oldtexts += [x['old_formula'] for x in aliases]
oldtexts += [late[:late.index(r'\begin{proof}')],guards[0]['old'],guards[1]['old']]
proposal=json.loads((P/(PRE+'defect_proposals.json')).read_text());assert len(oldtexts)==len(proposal['instances'])==14
db,defects,df=table('S6_SERIES_PUBLISH_defects_II.tsv');added=[]
for d,old in zip(proposal['instances'],oldtexts):
 assert old in s,d['id']
 for typ in d['types']:
  row={k:'' for k in df};row.update(change_id=f'II-NODAL-01-{len(added)+1:03}',type=typ,statement_id='cdp:st:B1',old_location=d['location'],new_location='cdp:st:B1',old_page='historical source bound by exact guard',new_page='pending integrated build',old_text=old,new_text=entry if d['id'] in ['nodal-013','nodal-014'] else receiver,reason=d['reason']+' All exact morphisms and full alternatives are preserved in the sealed packet.',review_status='Complete original/receiving proof comparison by B and root; final rendered pages remain pending.');added.append(row)
for g in [guards[0],guards[1],guards[-1]]:
 row={k:'' for k in df};row.update(change_id=f'II-NODAL-01-{len(added)+1:03}',type='D24',statement_id='cdp:st:B1',old_location='Further results / '+g['id'],new_location='Further results before B2',old_page='prior source',new_page='pending integrated build',old_text=g['old'],new_text=g['new'],reason='Transport both old list consequences to one receiving entry and put it immediately before B2, following the body order.',review_status='Exact list/owner transport; no additional mathematical event.');added.append(row)
eb,events,ef=table('CHECK_EVENTS.tsv');ev=list(csv.DictReader((P/(PRE+'event_proposals.tsv')).open(),delimiter='\t'))
assert len(ev)==4 and len({e['evidence_group'] for e in ev})==1
for e in ev:
 assert e['type']=='used and rechecked in this run' and e['event_id'] not in {x['event_id'] for x in events}
 e['who']='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation2 track B and root comparative review';e['publish_input_file']=MAN
tb,tags,tf=table('S6_SERIES_PUBLISH_tags.tsv');owners=json.loads((P/(PRE+'owner_alias_map.json')).read_text())['rows'];by={x['label']:x for x in owners}
for row in tags:
 if row['label'] in by:
  o=by[row['label']];row.update(current_owner=o['current_owner'],publication_disposition=o['publication_disposition']);assert row['tag']==o['tag']
ib,inv,inf=table('S6_SERIES_PUBLISH_inventory.csv',',');assert not any(x['label']=='wbII:rem:scope' for x in inv)
row={k:'' for k in inf};row.update(paper='II',label='wbII:rem:scope',source_run='CORRECTION_NOTE_20260901',source_id='rem:scope',kind='Reference target (proof alias)',status='proved',main_or_supporting='supporting',check_record='{}',source_paper='II',tag='03IS',placement_state='Permanent alias in the combined nodal proposition; existing target retained.',current_statement_owner='cdp:st:B1',current_number='pending build',current_page='pending build');inv.append(row)
for row in inv:
 if row['paper']=='II' and row['label'] in by:
  record=json.loads(row['check_record']) if row['check_record'].startswith('{') else {'retained_source_record':row['check_record']}
  record['nodal_editorial_transport_20261122']=dict(current_owner='cdp:st:B1',manifest=MAN,exact_map=str((P/(PRE+'mathematical_map.md')).relative_to(R)),historical_statement_identity_preserved=True)
  row.update(check_record=json.dumps(record,ensure_ascii=False),current_statement_owner='cdp:st:B1',assessment_source=MAN,current_source_sha256=sha(new.encode()),writing_state='Original nodal claim received by exact coordinate, sheaf and cohomology maps in the combined proposition.',layout_check='pending integrated rendered-page review')
cb=(R/'S6_SERIES_PUBLISH_checks_II.md').read_bytes();assert b'<a id="tag-03IS"></a>' not in cb
checkadd='\n<a id="tag-03IS"></a>\n\n## 03IS — II, number pending build\n\nLabel: `wbII:rem:scope`. Page: pending build.\n\nRecorded mathematical status: proved as a scope clause of `cdp:st:B1`.\n\n### Recorded routes and present scope\n\nThe existing reference target is a permanent alias of the combined nodal proposition. The exact Serre-dual evaluation map and compactness comparison are recorded in `'+MAN+'`.\n\n<a id="uses-03IS"></a>\n### Uses and used by\n\nUses: the explicit extending divisor and dual tensor evaluation.\n\nUsed by: final reference graph regeneration pending.\n\n### Entry provenance\n\nExisting permanent target; added check entry records the merged proof clause without a new mathematical-result claim.\n\n### Check events\n\n'
rp=R/'records/S6_SERIES_PUBLISH_additional_event_bundles.json';rb=rp.read_bytes();reg=json.loads(rb);bundle=tab(ev,ef)
reg['bundles'].append(dict(path=str((O/'event_rows.tsv').relative_to(R)),bytes=len(bundle),sha256=sha(bundle),admission_manifest=MAN))
now=dt.datetime.now(dt.timezone.utc).isoformat();O.mkdir();(O/'inverse.json').write_bytes(enc(inverse));(O/'applied_guards.json').write_bytes(enc(guards))
(O/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before nodal admission01',tofile='II after nodal admission01')))
(O/'defect_rows.tsv').write_bytes(tab(added,df));(O/'event_rows.tsv').write_bytes(bundle)
primary=json.loads((P/(PRE+'primary_receipt.json')).read_text());pb=Path(primary['source']['path']).read_bytes();assert sha(pb)==primary['source']['sha256']
reading=dict(recorded_utc=now,full_root_reading=[bind(P/(PRE+n)) for n in ['mathematical_map.md','B1_original.tex','B1_proposed.tex','nodal_original_region.tex','equation_alias_map.json','owner_alias_map.json','comparison_receipt.json','map_certificate.py','map_certificate.json','focused_tex_receipt.json','statement_alias_receipt.json','primary_receipt.json','reading_receipt.json']],IB_and_I9='Both complete original blocks were read inside the complete late region; exact substring identity is verified.',primary_source=primary['source'],primary_intervals_actually_read_by_root=[[255,340],[969,1045]],focused_images='Three actual focused page readings belong to B, as recorded in the sealed reading receipt; root claims receipt review only.',scope='Exposed comparison of all six original proofs and the full receiver; no independent check.',numbered_equations_before=1822,numbered_equations_after=1817,identical_surviving_payloads=same,changed_equation_maps=changed,root_list_transport='Move the single receiving entry before the exact B2 entry.',final_page_credit=0)
(O/'root_reading.json').write_bytes(enc(reading))
changes=[('S6_SERIES_PUBLISH_II.tex',before,new.encode()),('S6_SERIES_PUBLISH_defects_II.tsv',db,db+tab(added,df,header=False)),('CHECK_EVENTS.tsv',eb,eb+tab(ev,ef,header=False)),('S6_SERIES_PUBLISH_tags.tsv',tb,tab(tags,tf)),('S6_SERIES_PUBLISH_inventory.csv',ib,tab(inv,inf,',')),('S6_SERIES_PUBLISH_checks_II.md',cb,cb+checkadd.encode()),('records/S6_SERIES_PUBLISH_additional_event_bundles.json',rb,enc(reg))]
for n,b,a in changes[3:]:(O/(Path(n).name+'.diff')).write_text(''.join(difflib.unified_diff(b.decode().splitlines(True),a.decode().splitlines(True),fromfile=n+' before',tofile=n+' after')))
manifest=dict(created_utc=now,source_before_sha256=sha(before),source_after_sha256=sha(new.encode()),sealed_index=bind(idxp),sealed_bindings_verified=len(ix['files']),unique_disjoint_guards=len(guards),exact_inverse=True,identities_preserved=identities,old_proofs=6,receiving_proofs=1,retired_numbered_equations=5,surviving_identical_payloads=same,all_scalar_formula='W.161 receives the original restricted conclusion by the explicit gluing and tensor maps.',events_added=4,event_groups=1,ledger_rows_before=len(events),ledger_rows_after=len(events)+4,defect_rows_added=len(added),defect_rows_after=len(defects)+len(added),inventory_alias_added='03IS',new_mathematical_errors=0,required_rows_closed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,D10_fingerprint_unchanged=d10fp(new),D16_next_step='Renew the changed B1 header projection and retire its two now-aliased lemma projections.',canonical_changes=[dict(path=n,before_bytes=len(b),before_sha256=sha(b),after_bytes=len(a),after_sha256=sha(a)) for n,b,a in changes],evidence=[bind(p) for p in sorted(O.iterdir())],code=bind(Path(__file__)))
mp=O/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
for n,b,a in changes:assert (R/n).read_bytes()==b,n
for n,b,a in changes:(R/n).write_bytes(a)
note=f'\n\n## Paper II: complete nodal-family consolidation — {now}\n\nAll six original proofs and the full receiving proof were compared by B and root. Coordinate inverses, normalization, gluing scalars, tensor products, differential maps, cohomology-table projections and the extending divisor identify every received assertion. Five repeated equations retain their literal labels and targets as exact receiving aliases; 1816 surviving equation payloads are identical, and W.161 displays the all-scalar calculation containing its old restricted conclusion. The four original statement identities and every historical event remain. The existing03IS scope target now has a minimal visible alias record and its own inventory/check entry. The merged Further entry precedes B2 in body order.\n\nAdmission `{mb["path"]}` (SHA-256 `{mb["sha256"]}`) adds four exposed-reread associations in one evidence group and {len(added)} individual defect rows. Source SHA-256 `{sha(new.encode())}`; ledger {len(events)+4} rows. The exact 28 computations and three focused-page readings are preserved under their actual exposure and checker. No mathematical error, independent event, required-row closure, global-class closure or final-page credit is asserted. D10 remains validated; the changed B1 title projection awaits explicit renewal.\n'
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(O/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,canonical_after_bindings=[bind(R/n) for n,_,_ in changes],no_prior_events_changed_or_deleted=True)))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','unique_disjoint_guards','ledger_rows_after','defect_rows_added','defect_rows_after']},indent=2));print('Manifest',mb['sha256'])
