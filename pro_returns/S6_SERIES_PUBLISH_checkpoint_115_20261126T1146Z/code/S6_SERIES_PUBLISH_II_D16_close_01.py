#!/usr/bin/env python3
"""Close D16 after all379 current headers were actually read and log coverage verified."""
from pathlib import Path
import csv,datetime as dt,hashlib,io,json,re
from S6_SERIES_PUBLISH_II_title_census import headers,projection,fingerprint
R=Path(__file__).resolve().parents[1]
OUT=R/'records/S6_SERIES_PUBLISH_II_D16_closure_01'
csv.field_size_limit(100_000_000)
sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
def tab(rows,fields,header=True):
 o=io.StringIO(newline='');w=csv.DictWriter(o,fieldnames=fields,delimiter='\t',lineterminator='\n')
 if header:w.writeheader()
 w.writerows(rows);return o.getvalue().encode()
assert not OUT.exists()
source=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=source.decode()
assert sha(source)=='41b87bdd719344b5c11f8485d1ec54382234e998ccea397fad3501e71fcacd42'
envs,current=headers(s);assert len(current)==379 and all(x['title'] and x['tags'] for x in current)
assert fingerprint(s)=='853a69049e21536543d9b80cf9a2d1dbd331958a1883860b3a58942319071d9c'
assert not any(re.search(r'actual|candidate|survivor|corrected|previously|retained|repaired|superseded|verification|audit|\bP[134](?:[ARKF])?\.',x['title'],re.I) for x in current)
test_hits=[x for x in current if re.search(r'\btest\b',x['title'],re.I)]
assert [(x['tags'][0],x['title']) for x in test_hits]==[('01FM','A finite cohomology test and a fixed fibre')]
db=(R/'S6_SERIES_PUBLISH_defects_II.tsv').read_bytes();reader=csv.DictReader(io.StringIO(db.decode()),delimiter='\t');rows=list(reader);fields=reader.fieldnames
by={x['change_id']:x for x in rows}
ids=['II-C2-62-02XS-002','II-C2-68-02XU-002','II-C2-71-02XV-002','II-C2-51-0336-002']
added=[]
for i,rid in enumerate(ids,1):
 old=by[rid];assert 'D16' not in re.findall(r'D\d+',old['type'])
 row=old.copy();row.update(change_id=f'II-D16-CLASSIFICATION-01-{i:03}',type='D16',reason='Supplement the D16 classification of the exact title edit already logged as '+rid+'. '+old['reason'],review_status='Record-only classification supplement. The existing exact old/new title change is unchanged; root read all379 current numbered headers. No source, mathematical event or page-reading mutation.')
 added.append(row)
after=db+tab(added,fields,False);allrows=rows+added
d16=[x for x in allrows if 'D16' in re.findall(r'D\d+',x['type'])];assert len(d16)==183
base=(R.parent/'S6_SERIES_PUBLISH_checkpoint_21/S6_SERIES_PUBLISH_II.tex').read_bytes();_,original=headers(base.decode());baseline_candidates=[]
for h in original:
 title=h['title'] or '';tag=h['tags'][0] if h['tags'] else '';label=h['labels'][0] if h['labels'] else ''
 defect=not title or bool(re.search(r'actual|candidate|survivor|corrected|previously|retained|repaired|superseded|verification|audit|\bP[134](?:[ARKF])?\.',title,re.I))
 if defect:
  matches=[x['change_id'] for x in d16 if (tag and (tag in x['old_text'] or tag in x['new_text'])) or (label and label in x['statement_id']) or (title and title in x['old_text'])]
  assert matches,(tag,title)
  baseline_candidates.append(dict(tag=tag,label=label,title=title,D16_rows=matches))
assert len(baseline_candidates)==62
now=dt.datetime.now(dt.timezone.utc).isoformat();OUT.mkdir()
(OUT/'classification_defect_rows.tsv').write_bytes(tab(added,fields))
census=dict(created_utc=now,source_sha256=sha(source),declared_environments=envs,header_count=379,current_headers=current,current_header_projection=projection(s),current_header_fingerprint=fingerprint(s),
 actual_root_reading='All379 current headers were displayed and read in two complete bounded outputs, indices1-195 and196-379, after the02UH/FH-title andR10/R14/R15 admissions. Earlier header readings and the exact2 final title maps were also recorded. This records title reading only, with no final PDF page credit.',
 environment_coverage='All19 declared theorem environment names included; every occurrence inspected, including cited and problem environments. No missing title or commented-out environment is included.',
 full_manual_verdict='Every current numbered statement has a mathematical title. No title names an internal run, prompt, proof-checking record, earlier draft or production status. The one lexical test hit at01FM is the mathematical finite cohomology criterion and fixed-fibre statement.',
 baseline_header_count=len(original),baseline_source_sha256=sha(base),baseline_search_candidates=baseline_candidates,
 limitations='Lexical hits support the complete manual header reading; they are not substituted for it. This closure covers D16 only; body text, other apparatus classes, integrated build and final page images remain under their separate gates.')
(OUT/'header_census.json').write_bytes(enc(census))
log_index=[dict(change_id=x['change_id'],type=x['type'],statement_id=x['statement_id'],canonical_row_sha256=sha(enc(x))) for x in d16]
(OUT/'D16_log_index.json').write_bytes(enc(log_index))
manifest=dict(created_utc=now,paper='II',defect_type='D16',status='done',source_sha256=sha(source),current_header_fingerprint=fingerprint(s),
 full_current_headers_read=379,missing_titles=0,remaining_workflow_titles=0,all_instances_logged=True,D16_log_records=183,classification_supplements=4,
 actual_title_changes_in_this_closure=0,source_changes=0,mathematical_events_added=0,required_rows_closed=0,final_pdf_page_credit=0,
 source_integrity='The source is byte-identical; only the four missing classifications and the reviewed class-closure registry are written.',
 current_scope_validation='Future reviews must recompute this exact full header projection. A changed projection reopens D16 until a new explicit complete audit admits it; an unchanged projection transports this title audit across body-only edits.',
 defect_table_before_sha256=sha(db),defect_table_after_sha256=sha(after),
 evidence=[bind(p) for p in sorted(OUT.iterdir())],code=bind(Path(__file__)),census_code=bind(R/'code/S6_SERIES_PUBLISH_II_title_census.py'))
mp=OUT/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
cp=R/'records/S6_SERIES_PUBLISH_defect_class_completion_manifest.json'
assert not cp.exists()
completion=dict(schema='source-wide-defect-class-completion',updated_utc=now,rows={'defect:II:D16':dict(paper='II',defect_type='D16',status='done',recorded_utc=now,evidence_path=mb['path'],evidence_sha256=mb['sha256'],
 header_fingerprint=fingerprint(s),header_count=379,log_index_path=str((OUT/'D16_log_index.json').relative_to(R)),log_index_sha256=sha((OUT/'D16_log_index.json').read_bytes()),
 scope='All379 numbered statement headers read; every current header has a mathematical title and all removed D16 instances are logged. Four existing title edits receive missing D16 classifications. No body/PDF claim.')})
assert (R/'S6_SERIES_PUBLISH_defects_II.tsv').read_bytes()==db and (R/'S6_SERIES_PUBLISH_II.tex').read_bytes()==source
(R/'S6_SERIES_PUBLISH_defects_II.tsv').write_bytes(after);cp.write_bytes(enc(completion))
note=f'''\n\n## Paper II: D16 title class completed — {now}\n\nRoot read every379 current numbered statement header, across all19 declared theorem environments, in two complete bounded outputs. Every header has a mathematical title; no production or internal-run title remains. The mathematical phrase “finite cohomology test” at01FM was read in its criterion sense. All183 D16 records are indexed by exact row hash. Four earlier title edits were already logged under other defect classes and now receive their missing D16 classifications; no source or mathematical event changes here. The62 baseline lexical candidates all map to logged D16 records, supplementing the complete current-header reading.\n\nThe class completion is `{mb['path']}` (SHA-256 `{mb['sha256']}`), with full header fingerprint `{fingerprint(s)}`. The scheduled review will record the open-to-done transition. Later source edits preserve this closure only when the complete header projection is unchanged; any changed projection reopens it until explicitly reviewed. This closes one of25 source-wide classes;24 remain open. All final PDF page readings, provenance, restructuring and integrated build remain open.\n'''
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(OUT/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,source_unchanged=True,canonical_after=[bind(R/'S6_SERIES_PUBLISH_defects_II.tsv'),bind(cp)])))
print(json.dumps({k:manifest[k] for k in ['created_utc','status','full_current_headers_read','missing_titles','remaining_workflow_titles','D16_log_records','classification_supplements','source_changes','mathematical_events_added','final_pdf_page_credit']},indent=2));print('Manifest:',mb['path'],mb['sha256'])
