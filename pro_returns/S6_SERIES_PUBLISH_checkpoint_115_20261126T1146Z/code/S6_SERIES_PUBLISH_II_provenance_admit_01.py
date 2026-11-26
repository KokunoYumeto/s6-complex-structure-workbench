#!/usr/bin/env python3
"""Admit II-only provenance/deposit fields with a fresh bound ledger census."""
from pathlib import Path
import csv,datetime as dt,difflib,hashlib,importlib.util,io,json,re
from S6_SERIES_PUBLISH_II_title_census import fingerprint as titlefp
from S6_SERIES_PUBLISH_II_D10_census import fingerprint as apparatusfp
R=Path(__file__).resolve().parents[1];P=R/'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_provenance_v1'
V=P/'S6_SERIES_PUBLISH_II_C2_provenance_review_v2';PRE='S6_SERIES_PUBLISH_II_C2_'
O=R/'records/S6_SERIES_PUBLISH_II_provenance_admission_01';MAN=str((O/'manifest.json').relative_to(R))
sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
def tab(rows,fields,header=True):
 out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=fields,delimiter='\t',lineterminator='\n')
 if header:w.writeheader()
 w.writerows(rows);return out.getvalue().encode()
csv.field_size_limit(100_000_000);assert not O.exists()
ip=P/(PRE+'provenance_final_v2_index.json');assert sha(ip.read_bytes())=='7a327f2b1c406531e6ddb3d57f6fe58f64f84e55d9b447cc9d3a9cca892ff933'
ix=json.loads(ip.read_text());verified=0
for key in ['active_files','preserved_draft_files','existing_root_primary_receipts']:
 for f in ix[key]:
  b=(R/f['path']).read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['path'];verified+=1
snapshot={n:(R/n).read_bytes() for n in ['S6_SERIES_PUBLISH_II.tex','CHECK_EVENTS.tsv','S6_SERIES_PUBLISH_inventory.csv','S6_SERIES_PUBLISH_tags.tsv','S6_SERIES_PUBLISH_provenance_checks.tsv','S6_SERIES_PUBLISH_deposit_fields.md','S6_SERIES_PUBLISH_defects_II.tsv']}
s=snapshot['S6_SERIES_PUBLISH_II.tex'].decode();assert sha(s.encode())=='282df10393e3d7eb725e1d39575f33099967ef9bdf6a66f12bcf6ab9f7b3f9e6'
for part in ['abstract','main_statements','literature_status']:
 assert s.count((V/(PRE+'provenance_current_'+part+'.tex')).read_text())==1,part
builder=R/'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_frontmatter_v1/S6_SERIES_PUBLISH_II_C2_frontmatter_build_v2.py'
assert sha(builder.read_bytes())=='72fcff48aea18b8cb0b4faa3f2e77044b3fea482a07bd6041f70869a33dad985'
spec=importlib.util.spec_from_file_location('provenance_admission_census',builder);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
counts=mod.census({n:snapshot[n] for n in ['S6_SERIES_PUBLISH_II.tex','CHECK_EVENTS.tsv','S6_SERIES_PUBLISH_inventory.csv','S6_SERIES_PUBLISH_tags.tsv']})
assert counts['statement_linked_rows']==2640 and counts['statement_linked_unique_evidence_groups']==2310
assert counts['by_type']['used and rechecked in this run']==1010 and counts['series_ledger_rows']==8508
guards=json.loads((V/(PRE+'provenance_program_scope_guards.json')).read_text());g=guards['guards'][0]
assert len(guards['guards'])==1 and s.count(g['old'])==1 and s.count(g['new'])==0
assert guards['full_url_reading']['exact_bytes_agree'] and guards['full_url_reading']['sha256']==guards['full_url_reading']['short_url_sha256']
new=s.replace(g['old'],g['new']);assert new.replace(g['new'],g['old'])==s
assert titlefp(s)==titlefp(new) and apparatusfp(s)==apparatusfp(new)
assert guards['superseded_E5_scope_guard']['current_exact_row'] in s
pinmap=json.loads((V/(PRE+'current_program_final_pin_map.json')).read_text());assert len(pinmap['rows'])==87 and not pinmap['closed']
for row in pinmap['rows']:
 f=row['local_file'];b=(R/f['path']).read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['path'];assert row['final_url'] is None and row['old_exact'] in s
links=json.loads((P/(PRE+'provenance_snapshot_01')/(PRE+'provenance_links.json')).read_text())['results']
addon=json.loads((P/(PRE+'provenance_snapshot_02')/(PRE+'provenance_links_addendum.json')).read_text())
hist=[x for x in links if x.get('kind')=='historical_program'];assert len(hist)==30 and all(x['http_status']==200 for x in hist)
assert len(addon['new_results'])==6 and all(x['http_status']==200 for x in addon['new_results'])
dep=json.loads((V/(PRE+'deposit_fields_proposed.json')).read_text());append=json.loads((V/(PRE+'deposit_append_proposal.json')).read_text())
assert sha(snapshot['S6_SERIES_PUBLISH_deposit_fields.md'])==append['old_binding']['sha256']
assert len(snapshot['S6_SERIES_PUBLISH_deposit_fields.md'])==append['old_binding']['bytes']
assert list(dep)==list(json.loads((R/'agents/provenance/S6_SERIES_PUBLISH_deposit_fields_V.json').read_text()))
abstract=re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}',s,re.S).group(1)
assert re.sub(r'\s+','',abstract)==re.sub(r'\s+','',dep['abstract'])
numeric=[('2,638','2,640'),('1,008','1,010'),('2,309','2,310')]
block=append['append'];oldprov=dep['provenance']
for a,b in numeric:
 assert dep['provenance'].count(a)==1 and block.count(a)==1
 dep['provenance']=dep['provenance'].replace(a,b);block=block.replace(a,b)
assert '## Paper II' not in snapshot['S6_SERIES_PUBLISH_deposit_fields.md'].decode()
depositbytes=snapshot['S6_SERIES_PUBLISH_deposit_fields.md']+block.encode()
pr=csv.DictReader(io.StringIO(snapshot['S6_SERIES_PUBLISH_provenance_checks.tsv'].decode()),delimiter='\t');existing=list(pr);fields=pr.fieldnames
pu=json.loads((V/(PRE+'provenance_existing_P01_update.json')).read_text());oldrow=next(x for x in existing if x['claim_id']=='II-C2-P01');assert oldrow==pu['exact_old_row']
updated=pu['proposed_new_row'].copy()
for beforekey,afterkey in [('against_records','prior_records_assessment'),('by_recomputation','prior_recomputation_assessment'),('against_primary_source','prior_primary_assessment')]:updated[afterkey]=oldrow[beforekey]
updated['current_deposit_location']='S6_SERIES_PUBLISH_deposit_fields_II.json; S6_SERIES_PUBLISH_deposit_fields.md, Paper II'
oldline=tab([oldrow],fields,False);newline=tab([updated],fields,False);assert snapshot['S6_SERIES_PUBLISH_provenance_checks.tsv'].count(oldline)==1
rows=list(csv.DictReader((V/(PRE+'provenance_claim_rows.tsv')).open(),delimiter='\t'));assert len(rows)==30
assert not {x['claim_id'] for x in rows}&{x['claim_id'] for x in existing}
now=dt.datetime.now(dt.timezone.utc).isoformat()
for row in rows:
 row['current_deposit_location']=updated['current_deposit_location']
 row['current_resolution']='Admitted at '+now+' after root review of the complete proposal. Exact historical evidence retains its recorded scope. Final publication and dynamic refresh gates remain open.'
 if row['claim_id']=='II-C2-P13':
  row['prior_claim']=row['claim'];row['claim']='Admission snapshot: 2640 statement associations in 2310 nonempty recorded groups; types '+json.dumps(counts['by_type'],sort_keys=True)+'.'
  row['prior_records_assessment']=row['against_records'];row['against_records']='Current source, ledger, inventory and tags are bound in '+MAN+'.'
  row['evidence']+='; '+str((O/'current_counts.json').relative_to(R))
 if row['claim_id']=='II-C2-P18':
  row['prior_records_assessment']=row['against_records'];row['against_records']+=' Admission expands the sole abbreviated pin to the verified full commit; returned program bytes are identical.'
 if row['claim_id']=='II-C2-P30':
  row['resolution_status']='admitted_final_pin_and_refresh_open';row['remaining_gate']='Final user-set publication pin and final count/abstract refresh.'
provenancebytes=snapshot['S6_SERIES_PUBLISH_provenance_checks.tsv'].replace(oldline,newline)+tab(rows,fields,False)
dr=csv.DictReader(io.StringIO(snapshot['S6_SERIES_PUBLISH_defects_II.tsv'].decode()),delimiter='\t');defects=list(dr);df=dr.fieldnames
defect={k:'' for k in df};defect.update(change_id='II-PROVENANCE-01-001',type='D18',statement_id='push:src:E.2.19',old_location='Programs: d_push_cusp_torus_action.py commit',old_page='current source before admission',new_location='same Programs URL with full commit',new_page='pending integrated build',old_text=g['old'],new_text=g['new'],reason='Expand the sole abbreviated historical commit after exact byte-identity verification of both source responses. This corrects citation form without changing program or mathematical content.',review_status='Root read complete proposal and identity receipt; agent retrieval supplies availability evidence. No execution or proof reading is credited.')
O.mkdir();(O/'current_counts.json').write_bytes(enc(counts));(O/'prior_P01_row.json').write_bytes(enc(oldrow));(O/'admitted_claim_rows.tsv').write_bytes(tab(rows,fields));(O/'defect_rows.tsv').write_bytes(tab([defect],df))
(O/'source_guard.json').write_bytes(enc(g));(O/'deposit_count_transport.json').write_bytes(enc(dict(old_provenance=oldprov,new_provenance=dep['provenance'],exact_three_numeric_changes=numeric,other_fields_unchanged=True)))
(O/'root_reading.json').write_bytes(enc(dict(recorded_utc=now,complete_files_read=[bind(P/(PRE+'provenance_report_v2.md'))]+[bind(V/(PRE+n)) for n in ['deposit_append_proposal.json','deposit_fields_proposed.json','provenance_program_scope_guards.json','provenance_existing_P01_update.json','provenance_reading_receipt.json','deposit_proposal_receipt.json','provenance_claim_rows.tsv']],reading_scope='All30 claim rows read completely in two bounded outputs; the report, complete deposit fields, source guard and receipt read in full. Current counts independently recomputed by the existing bound census helper. Primary-page readings retain the exact earlier root/C receipt scope; no new primary-paper, program execution, mathematical-event or image credit.',agent_reading=bind(V/(PRE+'provenance_reading_receipt.json')))))
jsonp=R/'S6_SERIES_PUBLISH_deposit_fields_II.json';assert not jsonp.exists()
changes=[('S6_SERIES_PUBLISH_II.tex',snapshot['S6_SERIES_PUBLISH_II.tex'],new.encode()),('S6_SERIES_PUBLISH_deposit_fields.md',snapshot['S6_SERIES_PUBLISH_deposit_fields.md'],depositbytes),('S6_SERIES_PUBLISH_provenance_checks.tsv',snapshot['S6_SERIES_PUBLISH_provenance_checks.tsv'],provenancebytes),('S6_SERIES_PUBLISH_defects_II.tsv',snapshot['S6_SERIES_PUBLISH_defects_II.tsv'],snapshot['S6_SERIES_PUBLISH_defects_II.tsv']+tab([defect],df,False))]
for n,b,a in changes:(O/(n+'.diff')).write_text(''.join(difflib.unified_diff(b.decode().splitlines(True),a.decode().splitlines(True),fromfile=n+' before',tofile=n+' after')))
manifest=dict(created_utc=now,sealed_index=bind(ip),bindings_verified=verified,source_before_sha256=sha(s.encode()),source_after_sha256=sha(new.encode()),source_guards=1,exact_source_inverse=True,provenance_rows_added=30,existing_P01_chronology_preserved=True,other_provenance_rows_byte_unchanged=True,old_deposit_prefix_byte_unchanged=True,new_II_deposit_json_sha256=sha(enc(dep)),current_counts=dict(associations=2640,groups=2310,used=1010,ledger_rows=8508),historical_URLs_with_recorded_HTTP200=36,current_program_files_verified=87,final_publication_pin='open; user sets actual folder and commit at deposit',fresh_main_status_search='open; C task running',defect_rows_added=1,defect_rows_after=len(defects)+1,mathematical_events_added=0,required_rows_closed=0,classes_closed=0,final_pdf_page_credit=0,D10_fingerprint_unchanged=apparatusfp(new),D16_fingerprint_unchanged=titlefp(new),canonical_changes=[dict(path=n,before_sha256=sha(b),after_sha256=sha(a)) for n,b,a in changes],evidence=[bind(p) for p in sorted(O.iterdir())],code=bind(Path(__file__)))
(O/'manifest.json').write_bytes(enc(manifest));mb=bind(O/'manifest.json')
for n,b in snapshot.items():assert (R/n).read_bytes()==b,n
for n,b,a in changes:(R/n).write_bytes(a)
jsonp.write_bytes(enc(dep))
note=f'''\n\n## Paper II: provenance and deposit fields — {now}\n\nThe complete Paper II deposit block and JSON are admitted with 2640 statement associations in2310 recorded groups, including1010 exposed readings. Thirty claim-by-claim provenance records enter the central table. The earlier failed checkpoint-link openings remain in the prior assessments; the later successful exact-pin retrieval is added. Every pre-existing I/V deposit byte and every other provenance-row byte remains unchanged. The only manuscript change expands one historical program's commit after byte-identity verification.\n\nManifest `{mb['path']}` (SHA-256 `{mb['sha256']}`), source `{sha(new.encode())}`. All87 current program files exist and retain their bound hashes; their final user-set publication URLs remain open. Fresh A–G literature-status work is still in progress. Final counts and abstract must be rebound after later edits. No mathematical event, required-row closure, defect-class closure, final-page credit or external publication is asserted.\n'''
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(O/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,canonical_after=[bind(R/n) for n,_,_ in changes]+[bind(jsonp)],ledger_unchanged_sha256=sha(snapshot['CHECK_EVENTS.tsv']))))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','provenance_rows_added','defect_rows_after','current_counts']},indent=2));print('Manifest',mb['sha256'])
