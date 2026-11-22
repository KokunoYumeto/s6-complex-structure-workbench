#!/usr/bin/env python3
"""Admit sealed front matter, exact Further-list permutation and actual rereads."""
from pathlib import Path
import collections,csv,datetime as dt,difflib,hashlib,importlib.util,io,json,re
from S6_SERIES_PUBLISH_II_title_census import headers,fingerprint
R=Path(__file__).resolve().parents[1];P=R/'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_frontmatter_v1';Q=P/'S6_SERIES_PUBLISH_II_C2_frontmatter_review_v2';PRE='S6_SERIES_PUBLISH_II_C2_frontmatter_';O=R/'records/S6_SERIES_PUBLISH_II_frontmatter_admission_01'
csv.field_size_limit(100_000_000);sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
def rd(n):
 b=(R/n).read_bytes();r=csv.DictReader(io.StringIO(b.decode()),delimiter='\t');return b,list(r),r.fieldnames
def tab(rows,fields,header=True):
 o=io.StringIO(newline='');w=csv.DictWriter(o,fieldnames=fields,delimiter='\t',lineterminator='\n')
 if header:w.writeheader()
 w.writerows(rows);return o.getvalue().encode()
assert not O.exists();idxp=P/(PRE+'final_v2_index.json');assert sha(idxp.read_bytes())=='56c26206b8478a06731c218c2a8f3d05afe3da1b1523813745ae146d089c3b0e';idx=json.loads(idxp.read_text());verified={}
def check_nodes(x):
 if isinstance(x,dict):
  if all(k in x for k in ['path','sha256','bytes']):
   b=(R/x['path']).read_bytes();assert len(b)==x['bytes'] and sha(b)==x['sha256'],x['path'];verified[x['path']]=x['sha256']
  for v in x.values():check_nodes(v)
 elif isinstance(x,list):
  for v in x:check_nodes(v)
check_nodes(idx);verify=json.loads((Q/(PRE+'verification.json')).read_text());check_nodes(verify['read_evidence_bindings']);check_nodes(json.loads((P/(PRE+'full_read_transport_v2.json')).read_text()))
before=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=before.decode();assert sha(before)=='670349f54976a06da6cd2f04c059f00c198bad902859bd2c668f7ee2fdafc561'
oldfront=(Q/(PRE+'original.tex')).read_text();proposed=(Q/(PRE+'proposed.tex')).read_text();assert s.count(oldfront)==1
g=json.loads((Q/(PRE+'guards.json')).read_text());new=s;inverse=[]
def change(key,old,newtext):
 global new
 assert new.count(old)==1,key;a=new.index(old);inverse.append(dict(id=key,offset=a,old=old,new=newtext));new=new[:a]+newtext+new[a+len(old):]
for v in g:
 assert sha(v['old'].encode())==v['old_sha256'] and sha(v['new'].encode())==v['new_sha256'];change(v['id'],v['old'],v['new'])
assert new.count(proposed)==1
further=next(v['new'] for v in g if v['id']=='FM13-Further-list');assert further.count(r'\item ')==332
change('ROOT-FM20-remove-list-before-outline',further,'')
tail='\\bottomrule\\end{tabularx}\\endgroup\\end{figure}\n\n\\clearpage\n'
change('ROOT-FM20-insert-list-after-organization',tail,tail.replace('\\clearpage\n',further+'\\clearpage\n'))
_,hs=headers(s);bylabel={lab:h for h in hs for lab in h['labels']};mapping=json.loads((Q/(PRE+'Further_map.json')).read_text())
assert len(mapping['old_entries'])==337 and len(mapping['new_entries'])==332
for row in mapping['old_entries']:
 h=bylabel[row['receiving_owner']]
 if row['merged_group'] is None:assert h['header_sha256']==row['unchanged_header_sha256'] and h['title']==row['old_title']
for row in mapping['new_entries']:assert r'\label{'+row['owner']+'}' in s
labels=[row['owner'] for row in mapping['new_entries']];assert labels==sorted(labels,key=lambda lab:s.index(r'\label{'+lab+'}'))
now=dt.datetime.now(dt.timezone.utc).isoformat();eb,events,ef=rd('CHECK_EVENTS.tsv');ev=[];readinputs=[]
receipt=P/(PRE+'full_read_receipt_v1.json');assert sha(receipt.read_bytes())=='9cb9de6aa5956e110fc9aaa780fda4c7a1663204ab34c86133a14ecf5baa18ab'
proofs=[('ii:LR:covering','S6_SERIES_PUBLISH_II_C2_01RO_full_for_outline_review_v1.tex','outline'),('cdp:st:C.3.1','S6_SERIES_PUBLISH_II_C2_front_dependency_C_3_1.tex','figure'),('cdp:st:A.4.9','S6_SERIES_PUBLISH_II_C2_front_dependency_A_4_9.tex','figure'),('cdp:st:C4e','S6_SERIES_PUBLISH_II_C2_front_dependency_C4e.tex','figure'),('cdp:st:C4f','S6_SERIES_PUBLISH_II_C2_front_dependency_C4f.tex','figure')]
for owner,fn,group in proofs:
 p=P/fn;b=p.read_text();current=b.replace(r'label={$\langle1\rangle$\arabic*.}',r'label=\arabic*.').replace(r'label={$\langle2\rangle$\arabic*.}',r'label=(\arabic*)');assert s.count(current)==1,owner
 e={k:'' for k in ef};e.update(statement_id=owner,date='2026-11-22',date_utc=now,who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; S6_SERIES_PUBLISH continuation2 track C',type='used and rechecked in this run',event_id='publish:front01:'+owner,phase='publication outline and dependency comparison',source_file=str(p.relative_to(R)),source_row='1',source_event_type='used and rechecked in this run',evidence_group='publish:front01:'+group,publish_input_file='records/S6_SERIES_PUBLISH_II_frontmatter_admission_01/manifest.json',where='Complete original statement/proof, read for '+group,outcome=('Read the complete current01RO statement and all four proof items to compare the revised complete TheoremG outline with the retained body argument. The inverse period-scaling maps, half-integer shift, SL2Z obstruction, source-line square and quotient closing map are explicit. The historical j-series argument remains in the records.' if group=='outline' else 'Read the complete supplying/receiving statement and proof for the five explicitly mapped arrows in the TheoremA dependency figure. The C4e-to-C4f arrow uses the exact fixed-fibre-persistence subargument after its Euler hypothesis has ceased to be used. No body proof is rewritten by the figure.')+' This is an exposed comparative rereading. No independent derivation, required-row closure or final-page credit. The later D10 glyph-only map preserves every mathematical proof byte.')
 assert e['event_id'] not in {x['event_id'] for x in events};ev.append(e);readinputs.append(dict(owner=owner,original_read=bind(p),current_format_transport_sha256=sha(current.encode())))
builder=P/(PRE+'build_v2.py');spec=importlib.util.spec_from_file_location('C_front_census',builder);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
snap={n:(R/n).read_bytes() for n in ['S6_SERIES_PUBLISH_II.tex','CHECK_EVENTS.tsv','S6_SERIES_PUBLISH_inventory.csv','S6_SERIES_PUBLISH_tags.tsv']};snap['CHECK_EVENTS.tsv']=eb+tab(ev,ef,False);count=mod.census(snap)
assert count['statement_linked_rows']==2585 and count['statement_linked_unique_evidence_groups']==2299 and count['by_type']['used and rechecked in this run']==955
oldmeth=next(v['new'] for v in g if v['id']=='FM18-methodology');newmeth=mod.methodology(count);change('ROOT-FM21-actual-reading-counts',oldmeth,newmeth)
assert fingerprint(s)==fingerprint(new)
back=new
for v in reversed(inverse):
 a=v['offset'];assert back[a:a+len(v['new'])]==v['new'];back=back[:a]+v['old']+back[a+len(v['new']):]
assert back==s
for pat in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\\StatementRecord\{[^}]+\}\{[^}]+\}\{[^}]+\}']:assert collections.Counter(re.findall(pat,s))==collections.Counter(re.findall(pat,new))
oldmain=re.findall(r'\\begin\{maintheorem\}.*?\\end\{maintheorem\}',s,re.S);newmain=re.findall(r'\\begin\{maintheorem\}.*?\\end\{maintheorem\}',new,re.S);mathpat=r'\\\[.*?\\\]|(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$';assert len(oldmain)==len(newmain)==7
for a,b in zip(oldmain,newmain):assert re.findall(mathpat,a,re.S)==re.findall(mathpat,b,re.S)
db,defs,df=rd('S6_SERIES_PUBLISH_defects_II.tsv');dr=[]
for v in g:
 for typ in v['defect_classes']:
  row={k:'' for k in df};row.update(change_id=f'II-FRONT-01-{len(dr)+1:03}',type=typ,statement_id='II:frontmatter',old_location=v['id'],old_page='exact original front source bound',new_location=v['id'],new_page='pending integrated build',old_text=v['old'],new_text=v['new'],reason=v['reason']+' '+v['mathematical_disposition'],review_status='C complete original/revised front reading with exact v2 count transport; root read all main statements, outlines, source table, methodology and organization, full comparison and selected complete map/metadata. Every original descriptor has an exact current-header or proved owner-transport binding. Final provenance and page review remain open.');dr.append(row)
row={k:'' for k in df};row.update(change_id=f'II-FRONT-01-{len(dr)+1:03}',type='D15',statement_id='II:frontmatter',old_location='Further results before subsection1.3',old_page='source order',new_location='Further results after subsection1.6',new_page='pending integrated build',old_text=further,new_text=further,reason='Exact permutation of the complete332-entry list, preserving every byte, to let the proof outlines, known/new table, methodology and organization follow the main statements in the requested order.',review_status='Exact removal/insertion guards and inverse; list bytes and all entry transports unchanged. Final visual review pending.');dr.append(row)
rb=(R/'records/S6_SERIES_PUBLISH_additional_event_bundles.json').read_bytes();reg=json.loads(rb);bundle=tab(ev,ef);reg['bundles'].append(dict(path='records/S6_SERIES_PUBLISH_II_frontmatter_admission_01/event_rows.tsv',bytes=len(bundle),sha256=sha(bundle),admission_manifest='records/S6_SERIES_PUBLISH_II_frontmatter_admission_01/manifest.json'))
O.mkdir();(O/'inverse.json').write_bytes(enc(inverse));(O/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before front01',tofile='II after front01')));(O/'event_rows.tsv').write_bytes(bundle);(O/'defect_rows.tsv').write_bytes(tab(dr,df));(O/'methodology_census.json').write_bytes(enc(count));(O/'supporting_reading_transport.json').write_bytes(enc(readinputs))
(O/'root_reading.json').write_bytes(enc(dict(recorded_utc=now,C_complete_front_reading=bind(P/(PRE+'full_read_transport_v2.json')),root_full_new_ranges='Proposed front lines1–421 (abstract, common series table, numbered notation and all seven main statements); lines759–1152 (all outlines, source table, Methodology, organization and figure). The first34 Further lines were also read; root does not claim a second full332-entry reading.',root_full_comparison_report=bind(Q/(PRE+'report.md')),further_complete_reading='C read every original and new entry. Root verified every one of337 old labels against its exact current header or the sealed mathematical Picard owner map and all332 receiving labels/order. Root moved the whole list verbatim after1.6.',whole_main_math_unchanged=True,G_outline='The complete old/new outline comparison and exact body maps are in the sealed report. The valid historical j-series computation remains archived; the current outline describes the already printed modular-period proof.',provenance_remaining='Final primary-source/status, online literature search, repository/authorship and rendered-page validation remain open.')))
changes=[('S6_SERIES_PUBLISH_II.tex',before,new.encode()),('S6_SERIES_PUBLISH_defects_II.tsv',db,db+tab(dr,df,False)),('CHECK_EVENTS.tsv',eb,eb+tab(ev,ef,False)),('records/S6_SERIES_PUBLISH_additional_event_bundles.json',rb,enc(reg))]
manifest=dict(created_utc=now,source_before_sha256=sha(before),source_after_sha256=sha(new.encode()),sealed_index=bind(idxp),verified_bindings=len(verified),sealed_guards=43,root_exact_guards=3,exact_inverse=True,main_theorem_math_sequences_unchanged=7,D16_projection_unchanged=True,Further_old_entries=337,Further_current_entries=332,Further_exact_permutation=True,events_added=5,event_groups=2,event_type='used and rechecked in this run',ledger_rows_after=len(events)+5,defect_rows_added=len(dr),defect_rows_after=len(defs)+len(dr),methodology_total=2585,methodology_groups=2299,methodology_used_readings=955,required_rows_closed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,canonical_changes=[dict(path=n,before_sha256=sha(b),after_sha256=sha(a)) for n,b,a in changes],evidence=[bind(p) for p in sorted(O.iterdir())],code=bind(Path(__file__)))
mp=O/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
for n,b,a in changes:assert (R/n).read_bytes()==b
for n,b,a in changes:(R/n).write_bytes(a)
note=f'''\n\n## Paper II: revised front matter — {now}\n\nThe abstract, mechanisms, precise source table, Methodology and organization have been revised while retaining all seven main-theorem mathematical sequences and the common series paragraph/table. TheoremG's outline now follows the current modular-period proof through its exact scaling and closing maps; the valid earlier series calculation remains in the check record. The dependency figure states five precise supplying/receiving proof uses, including the Euler-independent subargument of C4e used by C4f. The332-entry Further-results list is placed verbatim after1.6, and all337 original entries have exact receiving-owner/title transports.\n\nC actually reread the complete01RO and four dependency proofs; five used-and-rechecked events in two groups are now recorded, with no independent or targeted promotion. The current Methodology census is2,585 statement associations in2,299 groups, including955 proof/application readings. The ledger has {len(events)+5} rows. Final literature/status/authorship/link provenance and final rendered pages remain open.\n\nAdmission `{mb['path']}` (SHA-256 `{mb['sha256']}`) binds43 sealed guards plus the exact list permutation and count refresh, their inverse, {len(dr)} individual class rows, all main mathematics and identities, and the actual reading scope. Source SHA-256 is `{sha(new.encode())}`. No global defect class, required row or final page is closed by this packet.\n'''
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(O/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,canonical_after=[bind(R/n) for n,_,_ in changes])))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','sealed_guards','root_exact_guards','ledger_rows_after','defect_rows_added','defect_rows_after']},indent=2));print('Manifest',mb['sha256'])
