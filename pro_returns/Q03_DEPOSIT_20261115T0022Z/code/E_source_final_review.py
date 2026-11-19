#!/usr/bin/env python3
"""Final source-integration and research-input exclusion inventory.
It reads the post and metadata, checks identifiers and hashes, and never
redistributes fetched source contents. Semantic review is in the Markdown note.
"""
import hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
DEP=ROOT/'Q03_DEPOSIT';CACHE=ROOT/'retrieved_sources'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
required=['S-P','S-F','S-D','S-N','S-A','S-FKN','S-FKN-e','S-CG','S-U','S-GJ','S-L','S-J','S-G']
post=(DEP/'Q03_DEPOSIT_post.tex').read_text()
sources=(DEP/'Q03_DEPOSIT_sources.md').read_text()
report=(DEP/'Q03_DEPOSIT_report.md').read_text()
literature=(DEP/'Q03_DEPOSIT_literature.md').read_text()
counterparts=json.loads((DEP/'code/C_dependency_source_map.json').read_text())
post_counterparts={}
for line in post.splitlines():
 m=re.match(r'(?:Lemma|Proposition|Corollary|Theorem|Definition) (\d+\.\d+) & (.*?) &',line)
 if m:post_counterparts[m[1]]=m[2]
counterpart_mismatches=[{'id':x['q03_id'],'expected':x['source_display'],'post':post_counterparts.get(x['q03_id'])} for x in counterparts if x['source_display'] not in post_counterparts.get(x['q03_id'],'')]
source_rows={s:bool(re.search(r'(?<![A-Za-z0-9-])'+re.escape(s)+r'(?![A-Za-z0-9-])',post)) for s in required}
source_report_rows={s:bool(re.search(r'^\| '+re.escape(s)+r' \|',sources,re.M)) for s in required}
external=[]
for p in sorted(CACHE.rglob('*')):
 if p.is_file():external.append({'external_path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':digest(p)})
deposit_hashes={}
for p in DEP.rglob('*'):
 if p.is_file():deposit_hashes.setdefault(digest(p),[]).append(str(p.relative_to(DEP)))
duplicates=[{'external_path':x['external_path'],'deposit_paths':deposit_hashes[x['sha256']]} for x in external if x['sha256'] in deposit_hashes]
manifest={'date':'2026-11-15','purpose':'Exact excluded research-cache inventory; source bytes are not included in this manifest.','files':external}
(DEP/'code/E_source_excluded_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
summary={
 'date':'2026-11-15','post_sha256':digest(DEP/'Q03_DEPOSIT_post.tex'),
 'source_check_ids_present_in_post':source_rows,'source_check_rows_in_source_report':source_report_rows,
 'source_counterpart_count':len(counterparts),'post_source_counterpart_rows':len(post_counterparts),'source_counterpart_mismatches':counterpart_mismatches,
 'search_batches':len(json.loads((DEP/'code/C_search_history_complete.json').read_text())),
 'search_queries':sum(len(x['queries']) for x in json.loads((DEP/'code/C_search_history_complete.json').read_text())),
 'excluded_research_files':len(external),'excluded_research_bytes':sum(x['bytes'] for x in external),
 'byte_identical_research_files_found_inside_deposit':duplicates,
 'deposit_pdfs':[str(p.relative_to(DEP)) for p in DEP.rglob('*.pdf')],
 'deposit_lean_sources':[str(p.relative_to(DEP)) for p in DEP.rglob('*.lean')],
 'report_lines':len(report.splitlines()),'report_sha256':digest(DEP/'Q03_DEPOSIT_report.md'),
 'source_check_ids_present_in_main_report':{s:bool(re.search(r'(?<![A-Za-z0-9-])'+re.escape(s)+r'(?![A-Za-z0-9-])',report)) for s in required},
 'report_completion_rows':[l for l in report.splitlines() if re.search(r'^\| (?:C(?:\.[12])?|D(?:\.1)?) \|',l)],
 'literature_date_present':'15 November 2026' in literature,
 'limitations_in_post':{'original_fkn_unavailable':'original 1969 article' in post and 'unavailable' in post,'course_provenance_404':'provenance.json' in post and 'HTTP 404' in post,'no_lean_replay':'No independent Lean replay' in post,'jansen_full_proof_not_audited':'Complete proof not independently re-derived' in post},
}
(DEP/'code/E_source_final_review_output.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
