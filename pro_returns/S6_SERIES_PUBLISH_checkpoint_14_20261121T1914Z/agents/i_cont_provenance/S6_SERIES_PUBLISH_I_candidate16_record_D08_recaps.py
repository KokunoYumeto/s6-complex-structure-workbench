#!/usr/bin/env python3
"""Record the final bounded recap pass and exact p124 prose-only guard."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json
import re
from S6_SERIES_PUBLISH_I_cont_recount import proof_end
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
SOURCE_SHA='61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc'
PDF_SHA='4a1633d9e19a82e3df92a0e3c31ada306b3e801f3051b0c1b7f0018d873f51a2'
source=ROOT/'S6_SERIES_PUBLISH_I.tex';assert sha(source)==SOURCE_SHA
text=source.read_text(); scan_path=OUT/'S6_SERIES_PUBLISH_I_candidate16_D08_recap_scan.json'
scan=json.loads(scan_path.read_text()); assert scan['source_sha256']==SOURCE_SHA
pattern=re.compile(scan['pattern'],re.I)
hits=[{'line':text.count('\n',0,m.start())+1,'hit':m[0]} for m in pattern.finditer(text)]
assert [r['hit'] for r in hits]==[r['hit'] for r in scan['rows']]
assert len(hits)==3 and not any('completes' in r['hit'].lower() for r in hits)
old='We have now verified all\nthree comparisons and their inverses.'
assert text.count(old)==1 and '$' not in old and '\\' not in old
sid='push:src:C.3.5';position=text.index('\\label{'+sid+'}',text.index(r'\begin{document}'))
start=list(re.finditer(r'\\begin\{(proposition|theorem|lemma|remark)\}',text[:position]))[-1]
se=text.index('\\end{'+start[1]+'}',position)+len('\\end{'+start[1]+'}')
end=proof_end(text,text.index(r'\begin{proof}',se))
before=text[start.start():end];after=before.replace(old,'',1)
assert before[:se-start.start()]==after[:se-start.start()]
directory=OUT/'candidate16_recap_review_blocks';directory.mkdir(exist_ok=True)
bp=directory/'block_01_before.tex';ap=directory/'block_01_proposed.tex'
bp.write_text(before+'\n');ap.write_text(after+'\n')
(directory/'block_01.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before',tofile='proposed')))
guard={
 'id':'I16-prov-19','page':124,'type':'D08','statement_id':sid,
 'line':text.count('\n',0,text.index(old))+1,'before':old,'after':'',
 'reason':'Remove the standalone retrospective verification sentence. The complete ordinary, finite-root and cusp translations, their inverse extensions, lattice/deck comparisons, composition identity, scalar-versus-unit comparison and final overlap obstruction remain verbatim. The full proposition and proof were actually read. This also reopens the inherited bounded D08 disposition at scan row 127.',
 'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,
 'original_full_block':str(bp.relative_to(ROOT)),'original_full_block_sha256':sha(bp),
 'proposed_full_block':str(ap.relative_to(ROOT)),'proposed_full_block_sha256':sha(ap),
 'statement_byte_identical':True,'all_mathematical_segments_and_commands_identical':True,
 'full_statement_and_proof_actually_read':True,
 'status':'proposed, not applied','mathematical_events_added':0,'full_page_reading_credit_added':0}
gp=OUT/'S6_SERIES_PUBLISH_I_candidate16_recap_guards.json';gp.write_text(json.dumps([guard],ensure_ascii=False,indent=2)+'\n')
reasons={
1:'Retain: the sentence states the exact equality Gamma intersect N_Z = H, and the next sentences use that equality to identify Gamma with ker chi. The mathematical conclusion and its named groups are substantive.',
2:'Confirmed D08: the sentence only recaps verification of three preceding comparisons. I16-prov-19 removes it while the complete maps, inverses and every later identity remain.',
3:'Retain: the phrase immediately introduces the exact higher-direct-image isomorphism and its natural restriction/Atiyah map. The displayed conclusion is substantive and used in the next steps.'}
rows=[]
for r,h in zip(scan['rows'],hits):
    rows.append({**r,'source_line':h['line'],'row_id':f"P{r['index']:03d}",
                 'context_actually_read':True,'reason':reasons[r['index']],
                 'disposition':'confirmed D08; exact guard pending application' if r['index']==2 else 'retained explicit mathematical conclusion',
                 'guard_ids':['I16-prov-19'] if r['index']==2 else [],
                 'mathematical_events_added':0,'full_page_reading_credit_added':0})
result={
 'created_utc':datetime.now(timezone.utc).isoformat(),'paper':'I','candidate':16,
 'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,
 'scan':{'path':str(scan_path.relative_to(ROOT)),'sha256':sha(scan_path)},
 'pattern':scan['pattern'],'source_and_PDF_hit_sequences_identical':True,
 'source_hits':hits,'contexts_actually_read':3,'this_completes_count_source_and_PDF':0,
 'rows':rows,'guard_file':str(gp.relative_to(ROOT)),'guard_sha256':sha(gp),
 'complete_block':{'before':str(bp.relative_to(ROOT)),'before_sha256':sha(bp),'proposed':str(ap.relative_to(ROOT)),'proposed_sha256':sha(ap)},
 'prior_bounded_scan_row_reopened':127,
 'earlier_expanded_dispositions':{'path':'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate16_D08_expanded_dispositions.json','sha256':sha(OUT/'S6_SERIES_PUBLISH_I_candidate16_D08_expanded_dispositions.json')},
 'D08_final_type_closed':False,'source_changes_applied':False,
 'mathematical_events_added':0,'full_page_reading_credit_added':0,
 'scope':'All remaining explicit we-have-verified/shown/proved/computed and this-completes occurrences were scanned in the entire current source and current PDF, their complete hit sequences compared, and every resulting context actually read. Two exact mathematical conclusions remain. The one prose-only recap has a complete-block guarded proposal. No keyword-absence or final-page certificate is asserted.'}
dest=OUT/'S6_SERIES_PUBLISH_I_candidate16_D08_recap_dispositions.json';dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
md=['# Candidate16: final bounded recap dispositions','',f'Source `{SOURCE_SHA}`; PDF `{PDF_SHA}`.','',
    'The source and PDF contain the same three matched recaps. All three contexts were read. The two recaps introducing explicit formulas/maps remain; the standalone p124 recap has an exact deletion guard. No full-page reading or mathematical event is added.','']
for r in rows:md.extend([f"## {r['row_id']} — page {r['page']}",'',r['reason'],''])
md.extend(['## I16-prov-19','','Before:','','```tex',old,'```','','After: delete only the exact prose above. The complete statement and proof maps remain.',''])
dest.with_suffix('.md').write_text('\n'.join(md)+'\n')
assert sha(source)==SOURCE_SHA
print(json.dumps({'guard_file':str(gp.relative_to(ROOT)),'guard_sha256':sha(gp),'receipt':str(dest.relative_to(ROOT)),'receipt_sha256':sha(dest),'contexts_actually_read':3},indent=2))
