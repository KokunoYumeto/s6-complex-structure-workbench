#!/usr/bin/env python3
"""Admit the sealed comparative Picard packet on the current exact source."""
from pathlib import Path
import collections,csv,datetime as dt,difflib,hashlib,io,json,re
R=Path(__file__).resolve().parents[1]
P=R/'agents/continuation2_B/Picard_D12/final_v1'
PRE='S6_SERIES_PUBLISH_II_B2_Picard_D12_'
O=R/'records/S6_SERIES_PUBLISH_II_Picard_admission_01'
csv.field_size_limit(100_000_000)
sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
def readtab(n,sep='\t'):
 b=(R/n).read_bytes();r=csv.DictReader(io.StringIO(b.decode()),delimiter=sep);return b,list(r),r.fieldnames
def tab(rows,fields,sep='\t',header=True):
 o=io.StringIO(newline='');w=csv.DictWriter(o,fieldnames=fields,delimiter=sep,lineterminator='\n')
 if header:w.writeheader()
 w.writerows(rows);return o.getvalue().encode()
assert not O.exists()
idxp=P/(PRE+'final_index.json');assert sha(idxp.read_bytes())=='3e5ce9b39732547c26b00adae12a90bdad8d9743e4524091692fdd33735205ff'
ix=json.loads(idxp.read_text())
for f in ix['files']:
 b=(R/f['path']).read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['path']
before=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=before.decode()
assert sha(before)=='c49aa9aabb0f14df27f7bcaa0b6392d9d57abe9a07c1c33607193ebefe760ee8'
guards=json.loads((P/(PRE+'guards.json')).read_text());ranges=[]
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
assert back==s and sha(new.encode())=='83a729acc0dbd5de32e7186b91c1c2eb3f4b8d302c6098628e94cf454393f028'
identity_counts={}
for name,pat in [('labels',r'\\label\{[^}]+\}'),('hypertargets',r'\\hypertarget\{[^}]+\}'),('statement_record_triples',r'\\StatementRecord\{[^}]+\}\{[^}]+\}\{[^}]+\}')]:
 a=collections.Counter(re.findall(pat,s));b=collections.Counter(re.findall(pat,new))
 if name=='statement_record_triples':
  assert not a-b and b-a==collections.Counter({r'\StatementRecord{wbII:rem:local-cusp-picard-obstruction}{proved}{03IQ}':1})
 else:assert a==b,name
 identity_counts[name]=sum(a.values())
now=dt.datetime.now(dt.timezone.utc).isoformat()
db,defects,df=readtab('S6_SERIES_PUBLISH_defects_II.tsv');added=[]
proposal=json.loads((P/(PRE+'defect_proposals.json')).read_text())
owner_map=json.loads((P/(PRE+'current_owner_title_map.json')).read_text())
aliases={a:g['primary'] for g in owner_map['groups'] for a in [g['primary']]+g['aliases']}
byguard={g['id']:g for g in guards}
for d in proposal['instances']:
 g=byguard[d['guard_id']];m=re.search(r'\\StatementRecord\{([^}]+)\}',g['old']);owner=m.group(1) if m else 'II:Picard:'+d['guard_id']
 for typ in d['type'].split(','):
  row={k:'' for k in df};row.update(change_id=f'II-PICARD-01-{len(added)+1:03}',type=typ,statement_id=owner,old_location=d['guard_id']+' / '+d['scope'],old_page='historical numbering; exact source guard bound',new_location=aliases.get(owner,owner),new_page='pending integrated build',old_text=d['old_text'],new_text=d['new_text'],reason=d['reason'],review_status='Admitted after full B original/receiving proof comparison and root full receiving-block/map review. Exact guards, inverse and identities verified. Final integrated page review pending.');added.append(row)
eb,events,ef=readtab('CHECK_EVENTS.tsv');ev=list(csv.DictReader((P/(PRE+'event_proposals.tsv')).open(),delimiter='\t'))
assert len(ev)==14 and len({e['evidence_group'] for e in ev})==7
for e in ev:
 assert e['type']=='used and rechecked in this run' and e['event_id'] not in {x['event_id'] for x in events}
 e['who']='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; S6_SERIES_PUBLISH continuation2 track B, root admission review'
 e['source_file']=str(P.relative_to(R))+'/'+Path(e['source_file']).name
 e['publish_input_file']='records/S6_SERIES_PUBLISH_II_Picard_admission_01/manifest.json'
tb,tags,tf=readtab('S6_SERIES_PUBLISH_tags.tsv');ib,inv,inf=readtab('S6_SERIES_PUBLISH_inventory.csv',',')
for g in owner_map['groups']:
 for row in tags:
  if row['paper']=='II' and row['tag'] in g['tags']:
   row['current_owner']=g['primary'];row['publication_disposition']='Consolidated at '+g['primary']+'; exact original/receiving maps and complete alternative proofs in records/S6_SERIES_PUBLISH_II_Picard_admission_01/manifest.json'
 for row in inv:
  if row['paper']=='II' and row['label'] in [g['primary']]+g['aliases']:
   row['current_statement_owner']=g['primary'];row['writing_state']='Complete comparative consolidation; historical identity and proof evidence retained.'
   cr=json.loads(row['check_record']);cr['picard_editorial_transport_20261122']={'current_owner':g['primary'],'manifest':'records/S6_SERIES_PUBLISH_II_Picard_admission_01/manifest.json','exact_mathematical_map':str(P.relative_to(R))+'/'+PRE+'mathematical_map_v1.md'};row['check_record']=json.dumps(cr,ensure_ascii=False)
for row in tags:
 if row['tag']=='03IQ':row['current_owner']='wbII:rem:local-cusp-picard-obstruction';row['kind']='remark';row['publication_disposition']='Existing target now a numbered proved remark on Pic(X)->Pic(N0)->Pic(E0); exact nonextension argument retained.'
for row in inv:
 if row['paper']=='II' and row['label']=='wbII:rem:local-cusp-picard-obstruction':row['current_statement_owner']=row['label'];row['kind']='Remark';row['writing_state']='Existing target is a numbered remark with the exact restriction composition and nonextension proof.'
rb=(R/'records/S6_SERIES_PUBLISH_additional_event_bundles.json').read_bytes();registry=json.loads(rb);bundle=tab(ev,ef)
registry['bundles'].append(dict(path='records/S6_SERIES_PUBLISH_II_Picard_admission_01/event_rows.tsv',bytes=len(bundle),sha256=sha(bundle),admission_manifest='records/S6_SERIES_PUBLISH_II_Picard_admission_01/manifest.json'))
O.mkdir();(O/'preflight_development.json').write_bytes(enc({'failed_pre_mutation_run':'The first preflight required equality of StatementRecord triples; it stopped before creating any admission directory or canonical mutation. Exact difference inspection showed zero removed triples and the one intended new proved record for existing tag03IQ. The corrected check requires exactly that singleton addition and all380 existing triples unchanged.'}));(O/'inverse.json').write_bytes(enc(inverse));(O/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before Picard admission01',tofile='II after Picard admission01')))
(O/'defect_rows.tsv').write_bytes(tab(added,df));(O/'event_rows.tsv').write_bytes(bundle)
reading=dict(recorded_utc=now,previous_root_full_reading=bind(R/'records/S6_SERIES_PUBLISH_II_Picard_root_draft_reading_01.json'),exact_reading_transports=['IO','IX','I6','IN'],new_complete_final_block_readings=[bind(P/(PRE+k+'_proposed.tex')) for k in ['IW','DR','IC']],IC_final_line='The complete IC file was read in contiguous ranges 1–882; the final end-of-proof marker and surrounding guard boundary were explicitly read before admission. Guard and file are byte-identical.',full_comparison_map=bind(P/(PRE+'mathematical_map_v1.md')),full_final_supplement=bind(P/(PRE+'final_supplement.md')),full_alias_technical_receipt=bind(P/(PRE+'alias_macro_technical_receipt.json')),original_proof_reading='B read all fourteen complete originals and all complete receiving blocks. Root does not claim a second full reading of all fourteen originals.',scope='Comparative exposed reading; no independent derivation credit.',limits='Focused alias evidence imports external auxiliary numbers; final integrated D19 and final page images remain open. The source retains unresolved inherited CompendiumRef uses for the separate exact-reference pass.')
(O/'root_reading.json').write_bytes(enc(reading))
changes=[('S6_SERIES_PUBLISH_II.tex',before,new.encode()),('S6_SERIES_PUBLISH_defects_II.tsv',db,db+tab(added,df,header=False)),('CHECK_EVENTS.tsv',eb,eb+tab(ev,ef,header=False)),('S6_SERIES_PUBLISH_tags.tsv',tb,tab(tags,tf)),('S6_SERIES_PUBLISH_inventory.csv',ib,tab(inv,inf,',')),('records/S6_SERIES_PUBLISH_additional_event_bundles.json',rb,enc(registry))]
for name,b,a in changes[3:]:(O/(Path(name).name+'.diff')).write_text(''.join(difflib.unified_diff(b.decode().splitlines(True),a.decode().splitlines(True),fromfile=name+' before',tofile=name+' after')))
manifest=dict(created_utc=now,source_before_sha256=sha(before),source_after_sha256=sha(new.encode()),sealed_index=bind(idxp),sealed_bindings_verified=len(ix['files']),guards=len(guards),exact_inverse=True,identities_preserved=identity_counts,old_grouped_owners=11,new_grouped_owners=4,equation_aliases=10,external_dynamic_reference_occurrences=148,exact_certificate_checks=73,events_added=len(ev),event_groups=7,event_types={'used and rechecked in this run':14},ledger_rows_before=len(events),ledger_rows_after=len(events)+len(ev),proposed_instance_records=40,defect_rows_added=len(added),class_list_split='Each comma-separated proposed class is a separate defect row; exact proposal identity is retained by guard and scope.',defect_rows_before=len(defects),defect_rows_after=len(defects)+len(added),mathematical_error='W.32 omitted the quotient-to-cover pullback; the receiving W.107 writes p_log^*(L|N_j^*) = h_j^* p_lin^*(L|J_j^*) using p_lin h_j = bar h_j p_log. The existing complete proof gives this square; no theorem is refuted.',required_rows_closed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,canonical_changes=[dict(path=n,before_bytes=len(b),before_sha256=sha(b),after_bytes=len(a),after_sha256=sha(a)) for n,b,a in changes],evidence=[bind(p) for p in sorted(O.iterdir())],code=bind(Path(__file__)))
mp=O/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
for n,b,a in changes:assert (R/n).read_bytes()==b,n
for n,b,a in changes:(R/n).write_bytes(a)
assert (R/'CHECK_EVENTS.tsv').read_bytes().startswith(eb)
note=f'''\n\n## Paper II: exact Picard consolidation — {now}\n\nFourteen complete original proof blocks were compared with seven receiving blocks. Eleven overlapping grouped owners are now four, with all original labels, permanent targets and statement-tag records preserved. The complete alternate proofs remain in the sealed record. Ten duplicate displayed equations are transported to their exact receiving equations, including number, page, hyperlink and cleveref identity in the focused build. Every one of 148 external dynamic reference occurrences has an exact transport. The full mathematical map includes the real factor cocycle, integral Chern class, graph edge, mixed slant sign, finite norm, cusp specialization, local support formula and global restriction maps.\n\nThe mathematical notation error in W.32 was its omitted pullback from the quotient to the vector cover. The corrected identity is the already proved W.107 pullback square; no theorem conclusion or hypothesis changes. Existing local/global commentary is now the numbered restriction-composition and nonextension remark03IQ. The final exact-reference pass retains the unresolved inherited compendium calls.\n\nAdmission `{mb['path']}` (SHA-256 `{mb['sha256']}`) binds all twenty unique disjoint guards, their current-source inverse, {len(added)} class-specific defect rows and fourteen exposed-reread events in seven evidence groups. Root read the complete receiving blocks and full comparison map; B read all fourteen originals. The ledger has {len(events)+len(ev)} rows and source SHA-256 is `{sha(new.encode())}`. No required row, global defect class or final-PDF page is closed by this admission. D16's prior header fingerprint needs an explicit fresh audit after the changed owner layout; final numbering and page inspection remain open.\n'''
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(O/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,canonical_after_bindings=[bind(R/n) for n,_,_ in changes],no_prior_events_changed_or_deleted=True)))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','guards','ledger_rows_after','defect_rows_added','defect_rows_after']},indent=2));print('Manifest',mb['sha256'])
