from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,subprocess
R=Path('/workspace/scratch/653608133b22');B=R/'work/agents/i_provenance';L=B/'literature'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
pattern='8 September 2026|September 8,? 2026|2026-09-08|20260908|2026/09/08'
cmd=['rg','-n','-i','--glob','*.md','--glob','*.json','--glob','*.tsv','--glob','*.txt','--glob','*.tex',pattern,'source']
r=subprocess.run(cmd,cwd=R,capture_output=True,text=True)
files=subprocess.run(['rg','--files','source'],cwd=R,capture_output=True,text=True,check=True).stdout.splitlines()
namehits=[x for x in files if re.search(r'20260908|2026.?09.?08|september.?8|sep.?8',x,re.I)]
manifestrows=[]
for f in ['source/S6_SERIES_GRIND_filelist.tsv','source/S6_GRIND_6_literature/MANIFEST.tsv','source/S6_GRIND_5_research_runs_tex/MANIFEST.tsv']:
 p=R/f
 matches=[dict(line=i,text=x) for i,x in enumerate(p.read_text().splitlines(),1) if re.search(pattern,x,re.I)]
 manifestrows.append(dict(file=f,sha256=sha(p),matches=matches))
receipt={'created_utc':now,'scope':'Bounded historical-date provenance lookup only; Paper I night:P5.7. No previous conversations or Library searched.',
'attachment_scope':{'filename_count':len(files),'filename_date_hits':namehits,'text_command':cmd,'text_hits':r.stdout.splitlines(),'manifest_checks':manifestrows},
'primary_online_scope':{'exact_search_queries':['"s6-complex-structure-workbench" "2026-09-08"','"KokunoYumeto" "8 September 2026"','"10.5281/zenodo.22235523"','"s6-complex-structure-workbench" "September"'],
'search_receipts':['S6_SERIES_PUBLISH_I_September8_status_search_raw.json','S6_SERIES_PUBLISH_I_September8_S6_status_search_raw.json'],
'GitHub_API_receipt':'S6_SERIES_PUBLISH_I_September8_GitHub_retrieval_receipt.json','GitHub_API_result':'The repository endpoint and bounded commits-until-2026-09-08 endpoint both returned HTTP403; no historical commit conclusion is drawn.',
'linked_Zenodo_record':{'url':'https://zenodo.org/records/22666541','opened_ref':'turn835769320view0','scope':'Opened metadata has creation/publication date8September2026 and a backlink to the S6 research record DOI10.5281/zenodo.22235523. Its described/files-listed checkpoint is a different mathematical project; it is used here only to discover the explicitly linked S6 record. No contents or proof date of the S6 record follow from that backlink.'},
'S6_target_record':{'doi':'10.5281/zenodo.22235523','record_url':'https://zenodo.org/records/22235523','web_open_result':'not accessible','REST_receipt':'S6_SERIES_PUBLISH_I_September8_S6_zenodo_receipt.json','REST_result':'HTTP410 Gone'},
'DGKX_v1_date':{'source':'S6_SERIES_PUBLISH_I_DGKX_v1_abs.html','scope':'Official arXiv metadata already retained in current primary prerequisites: v1 submitted23September2026,17:09:17UTC.'}},
'disposition':'The8September claim remains attributed to the supplied working-edition history. This bounded search did not independently authenticate public posting of the exact period-equivalence proof by that date. The later pinned repository copy and a backlink in another deposit do not supply that missing publication timestamp. No exhaustive absence or priority claim is made.',
'proposed_chronology_wording':'The supplied history dates the public working-edition proof of the exact2Z equivalence to8September2026; DGKX version1 was submitted on23September2026 and states that equivalence as Theorem1.4.',
'mathematical_check_events_added':0}
(L/'S6_SERIES_PUBLISH_I_September8_historical_scope_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
(L/'S6_SERIES_PUBLISH_I_September8_historical_scope_receipt.md').write_text('''# Historical date scope for Paper I\n\nThe attached original Paper I, compendium Paper I/report, and supplied prompt attribute the public working-edition period-equivalence proof to 8 September 2026. A bounded filename, manifest, and text search found no separately dated proof artifact.\n\nFour exact public searches and the linked primary records were checked. The public checkpoint at Zenodo 22666541 is dated 8 September and links S6 DOI 10.5281/zenodo.22235523. The linked S6 record is currently unavailable, with its REST endpoint returning HTTP410. The historical GitHub API request returned HTTP403. These results do not authenticate when the exact S6 proof first became public. The existing official arXiv metadata confirms DGKX v1 was submitted on 23 September 2026.\n\nThe proposed wording therefore attributes the 8 September date to the supplied history. This is a bounded result, with no exhaustive absence or priority inference and no new mathematical check event. Exact commands, URLs, hashes, results and search receipts are in the JSON file.\n''')
readme=json.loads((L/'S6_SERIES_PUBLISH_I_pinned_README_receipt.json').read_text())
source=R/'work/S6_SERIES_PUBLISH_I.tex';s=source.read_text()
old='''GPT-5.6 Sol (OpenAI), in Codex at reasoning effort ultra, wrote
the working edition on 24 August--9 September 2026.'''
new='''The supplied history credits GPT-5.6 Sol (OpenAI), in Codex at
reasoning effort ultra, with the working edition of
24 August--9 September 2026. The pinned repository's authorship
record also reports GPT-6 Astra at effort ultra from 5 September,
and occasional GPT-5.6 Luna and GPT-5.6 Terra sessions whose
individual effort settings and dates are not specified there.'''
assert s.count(old)==1,s.count(old)
model={'created_utc':now,'source_sha256':sha(source),'kind':'Historical provenance qualification; root decides incorporation before final binding',
'user_supplied_fact':'Publication prompt section4.1 credits GPT-5.6 Sol in Codex at effortultra for the working edition24August–9September2026.',
'primary_record':{'url':readme['url'],'sha256':readme['sha256'],'http_status':readme['http_status'],'scope':'Pinned README section Who produced what opened directly; its model account explicitly attributes its dates/settings to named summarized records. Raw conversation or session records were not opened.'},
'comparison':'The supplied fact does not identify every historical session; the pinned README reports a Sol-to-Astra change from5September and a few Luna/Terra sessions. No receiving statement is newly attributed to an unexamined session.',
'changes':[{'id':'I-historical-model-account-qualification','old':old,'new':new,'reason':'Retain the user-supplied Sol/ultra attribution while adding the bounded pinned-README account; do not invent missing Luna/Terra settings or dates.'}],
'mathematical_check_events_added':0,'requires_final_deposit_sync_after_root_decision':True}
(B/'S6_SERIES_PUBLISH_I_historical_model_qualification_guard.json').write_text(json.dumps(model,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'date_text_hits':len(r.stdout.splitlines()),'filename_date_hits':len(namehits),'receipt':'S6_SERIES_PUBLISH_I_September8_historical_scope_receipt.json','model_guard_source_sha256':sha(source)},indent=2))
