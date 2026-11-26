#!/usr/bin/env python3
"""Admit the completely compared minimal-boundary calculation with two owners."""
from pathlib import Path
import collections,csv,datetime as dt,difflib,hashlib,importlib.util,io,json,re
from S6_SERIES_PUBLISH_II_D10_census import valid as d10valid, fingerprint as d10fp
R=Path(__file__).resolve().parents[1]
P=R/'agents/continuation2_B/structure_global_01/minimal_mh_01/minimal_final_v1'
PRE='S6_SERIES_PUBLISH_II_B2_minimal_'
O=R/'records/S6_SERIES_PUBLISH_II_minimal_admission_01'
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
idxp=P/(PRE+'final_index.json');assert sha(idxp.read_bytes())=='a93d98717ea5da37d4e12802fae2d15ecc5f4f54d3b1f43daac355f24661a55f'
ix=json.loads(idxp.read_text())
for f in ix['files']:
 b=(R/f['path']).read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['path']
before=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=before.decode()
assert sha(before)=='49cb87dd0fa6873b099dd588e0cd22156d2b8c092bff8f7184c271eabc78b275'
tp=json.loads((P/(PRE+'tag_and_front_proposals.json')).read_text())
guards=json.loads((P/(PRE+'guards.json')).read_text())
anchor=r'\expandafter\def\csname SRef@cdp:st:A.5.16\endcsname{\hyperlink{tag-01B6}{II.\ref*{cdp:st:A.5.16}}}'+'\n'
front=r'\item \SeriesRef{cdp:st:A.5.16}\quad Rational normalization bounds with the exact constant-sheaf map.'+'\n'
extra=''.join('\\item \\SeriesRef{'+p['label']+'}\\quad '+p['further_description']+'\n' for p in tp['rows'])
for name,old,new in [('new-reference-definitions',anchor,anchor+'\n'.join(tp['series_ref_definitions'])+'\n'),('Further-two-minimal-owners',front,front+extra)]:
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
for name,pat,adds in [('labels',r'\\label\{[^}]+\}',[r'\label{'+p['label']+'}' for p in tp['rows']]),('targets',r'\\hypertarget\{[^}]+\}',[r'\hypertarget{tag-'+p['tag']+'}' for p in tp['rows']]),('records',r'\\StatementRecord\{[^}]+\}\{[^}]+\}\{[^}]+\}',[r'\StatementRecord{'+p['label']+'}{proved}{'+p['tag']+'}' for p in tp['rows']])]:
 a=collections.Counter(re.findall(pat,s));b=collections.Counter(re.findall(pat,new));assert not a-b and b-a==collections.Counter(adds),name
 identities[name]=dict(original=sum(a.values()),added=adds)
assert d10valid(new) and d10fp(new)==d10fp(s)
scanner=R/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_scan.py'
spec=importlib.util.spec_from_file_location('minimal_equation_scan',scanner);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
aa,_=mod.inventory(s);bb,_=mod.inventory(new)
assert len(aa['numbered_equations'])==len(bb['numbered_equations'])==1817
def payloads(text,inv):return collections.Counter(sha(text[x['display_start']:x['display_end']].encode()) for x in inv['numbered_equations'])
assert payloads(s,aa)==payloads(new,bb)
db,defects,df=readtab('S6_SERIES_PUBLISH_defects_II.tsv');added=[]
proposal=json.loads((P/(PRE+'defect_proposals.json')).read_text())
for i,d in enumerate(proposal['instances']):
 for typ in d['types']:
  row={k:'' for k in df};owner=tp['rows'][0 if i==0 else 1]['label'];row.update(change_id=f'II-MINIMAL-01-{len(added)+1:03}',type=typ,statement_id=owner,old_location=d['location'],old_page='original source bound by exact guard',new_location=owner,new_page='pending integrated build',old_text=guards[0]['old'],new_text=guards[0]['new'],reason=d['reason']+' Complete original text, exact maps and receiving proof are preserved in the sealed packet.',review_status='Admitted after full original/receiving comparative reading by B and root. Final pages remain unread.');added.append(row)
for p in tp['rows']:
 row={k:'' for k in df};row.update(change_id=f'II-MINIMAL-01-{len(added)+1:03}',type='D24',statement_id=p['label'],old_location='Further results after A.5.16',new_location='Further results in body order',old_page='prior source',new_page='pending integrated build',old_text=front,new_text='\\item \\SeriesRef{'+p['label']+'}\\quad '+p['further_description'],reason='Synchronize the newly numbered owner with the front list and exact local-reference definition.',review_status='Exact statement identity and body-order comparison; no separate mathematical event.');added.append(row)
eb,events,ef=readtab('CHECK_EVENTS.tsv');ev=list(csv.DictReader((P/(PRE+'event_proposals.tsv')).open(),delimiter='\t'))
assert len(ev)==2 and len({e['evidence_group'] for e in ev})==1
for e in ev:
 assert e['type']=='used and rechecked in this run' and e['event_id'] not in {x['event_id'] for x in events}
 e['who']='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation2 track B and root comparative review'
 e['source_file']=str(P.relative_to(R))+'/'+Path(e['source_file']).name;e['publish_input_file']=MAN
tb,tags,tf=readtab('S6_SERIES_PUBLISH_tags.tsv');ib,inv,inf=readtab('S6_SERIES_PUBLISH_inventory.csv',',');cb=(R/'S6_SERIES_PUBLISH_checks_II.md').read_bytes();checkadd=''
for p in tp['rows']:
 assert not any(x['tag']==p['tag'] or x['label']==p['label'] for x in tags)
 tags.append({k:p.get(k,'') for k in tf});assert not any(x['label']==p['label'] for x in inv)
 row={k:'' for k in inf};row.update(paper='II',label=p['label'],source_run='S6_SERIES_PUBLISH',source_id=p['label'],kind=p['kind'].title(),status='proved',main_or_supporting='supporting',check_record='{}',source_paper='II',tag=p['tag'],placement_state='printed in II',current_statement_owner=p['label'],current_number='pending build',current_page='pending build',writing_state=p['publication_disposition'],confidence_state='Full exposed original/receiving comparison recorded; no independent derivation asserted.',completion_state='Full paper publication gates remain open.',layout_check='pending integrated rendered-page review',remaining_risk='D12 overlaps and final source-wide, provenance, build and rendered-page review remain open.',assessment_source=MAN,current_source_sha256=sha(new.encode()));inv.append(row)
 assert ('<a id="tag-'+p['tag']+'"></a>').encode() not in cb
 checkadd+='\n<a id="tag-'+p['tag']+'"></a>\n\n## '+p['tag']+' — II, number pending build\n\nLabel: `'+p['label']+'`. Page: pending build.\n\nRecorded mathematical status: proved.\n\n### Recorded routes and present scope\n\n'+p['publication_disposition']+'. Complete comparative reading and exact maps: `'+MAN+'`.\n\n<a id="uses-'+p['tag']+'"></a>\n### Uses and used by\n\nUses: A.5.16 and the fixed contraction data; the proposition also uses D.1.9.\n\nUsed by: the subsequent rational-normalization boundary analysis; graph regeneration pending.\n\n### Entry provenance\n\nPermanent owner of the existing complete calculation; all eleven numbered displays are unchanged.\n\n### Check events\n\n'
rp=R/'records/S6_SERIES_PUBLISH_additional_event_bundles.json';rb=rp.read_bytes();reg=json.loads(rb);bundle=tab(ev,ef)
reg['bundles'].append(dict(path=str((O/'event_rows.tsv').relative_to(R)),bytes=len(bundle),sha256=sha(bundle),admission_manifest=MAN))
now=dt.datetime.now(dt.timezone.utc).isoformat();O.mkdir()
(O/'inverse.json').write_bytes(enc(inverse));(O/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before minimal admission01',tofile='II after minimal admission01')))
(O/'defect_rows.tsv').write_bytes(tab(added,df));(O/'event_rows.tsv').write_bytes(bundle)
reading=dict(recorded_utc=now,full_root_reading=[bind(P/(PRE+n)) for n in ['mathematical_map.md','original.tex','definition_proposed.tex','proposition_proposed.tex','replacement.tex','map_certificate.py','map_certificate.json','reading_receipt.json','tag_and_front_proposals.json','defect_proposals.json','event_proposals.tsv']],full_supporting_inputs=[bind(P/n) for n in ['S6_SERIES_PUBLISH_II_B2_A516_structural_original.tex','S6_SERIES_PUBLISH_II_B2_D19_transgression_input.tex']],chronology='Complete old gap, full replacement, mathematical map and A.5.16 read before context compaction; transgression, metadata proposals, full certificate code and all27 output checks read after compaction. The previously truncated combined output was explicitly reread in bounded complete outputs.',agent_full_reading=bind(P/(PRE+'reading_receipt.json')),scope='Full exposed comparative reading with no independent, targeted or required-row credit.',all1817_numbered_payloads_byte_identical=True,scanner=bind(scanner))
(O/'root_reading.json').write_bytes(enc(reading))
changes=[('S6_SERIES_PUBLISH_II.tex',before,new.encode()),('S6_SERIES_PUBLISH_defects_II.tsv',db,db+tab(added,df,header=False)),('CHECK_EVENTS.tsv',eb,eb+tab(ev,ef,header=False)),('S6_SERIES_PUBLISH_tags.tsv',tb,tab(tags,tf)),('S6_SERIES_PUBLISH_inventory.csv',ib,tab(inv,inf,',')),('S6_SERIES_PUBLISH_checks_II.md',cb,cb+checkadd.encode()),('records/S6_SERIES_PUBLISH_additional_event_bundles.json',rb,enc(reg))]
for n,b,a in changes[3:]:(O/(Path(n).name+'.diff')).write_text(''.join(difflib.unified_diff(b.decode().splitlines(True),a.decode().splitlines(True),fromfile=n+' before',tofile=n+' after')))
manifest=dict(created_utc=now,source_before_sha256=sha(before),source_after_sha256=sha(new.encode()),sealed_index=bind(idxp),sealed_bindings_verified=len(ix['files']),unique_disjoint_guards=len(guards),exact_inverse=True,identities_preserved=identities,new_permanent_tags=['P209','P210'],numbered_equation_payloads_preserved=1817,events_added=2,event_groups=1,ledger_rows_before=len(events),ledger_rows_after=len(events)+2,defect_rows_added=len(added),defect_rows_after=len(defects)+len(added),new_mathematical_errors=0,required_rows_closed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,D10_fingerprint_unchanged=d10fp(new),D16_next_step='Transport all prior headers and explicitly bind the two full new headers already read.',D12_overlap_status='WT/WY/X8/P4R1 overlaps remain pending.',canonical_changes=[dict(path=n,before_bytes=len(b),before_sha256=sha(b),after_bytes=len(a),after_sha256=sha(a)) for n,b,a in changes],evidence=[bind(p) for p in sorted(O.iterdir())],code=bind(Path(__file__)))
mp=O/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
for n,b,a in changes:assert (R/n).read_bytes()==b,n
for n,b,a in changes:(R/n).write_bytes(a)
note=f'''\n\n## Paper II: minimal-boundary owners — {now}\n\nDefinition P209 and Proposition P210 now own the complete existing contraction and conductor-image calculation. The specified contraction sequence, coefficient identity, Euler tables, actual pushout map, group obstruction and endpoint argument are preserved with full old/receiving comparison. All1817 numbered display payloads remain byte-identical. The front list, permanent tags and checks entries follow the two new owners. The sealed map retains the original introduction and recap.\n\nManifest `{mb['path']}` (SHA-256 `{mb['sha256']}`) adds two exposed-reread events in one group and {len(added)} class records. Source SHA-256 `{sha(new.encode())}`; ledger {len(events)+2} rows. No independent check, required-row closure, global defect-class closure or final-PDF page credit is claimed. D12 overlaps remain open. D10's projection is unchanged; D16's two new headers require the explicit current reading transport.\n'''
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(O/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,canonical_after_bindings=[bind(R/n) for n,_,_ in changes],no_prior_events_changed_or_deleted=True)))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','unique_disjoint_guards','ledger_rows_after','defect_rows_added','defect_rows_after']},indent=2));print('Manifest',mb['sha256'])
