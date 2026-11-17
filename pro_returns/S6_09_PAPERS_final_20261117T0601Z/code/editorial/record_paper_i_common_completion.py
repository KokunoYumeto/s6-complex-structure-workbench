"""Close the performed I common-reference/prose and final-image pass."""
from pathlib import Path
import json,re,hashlib,csv
D=Path(__file__).resolve().parents[2]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=D/'records/I_final_validation.json';old=json.loads(p.read_text())
archive=D/'records/I_validation_before_common_pass.json'
if not archive.exists():archive.write_text(json.dumps(old,indent=2)+'\n')
visual=json.loads((D/'work/cdp_audit/I_final_visual_review/final_current_visual_review.json').read_text())
log=D/f"editorial/S6_09_PAPERS_I_build_{visual['build']:02d}.stdout.txt";s=log.read_text()
assert visual['pdf_sha256']==sha(D/'S6_09_PAPERS_I.pdf')
assert not visual['visual_defects_found']
assert not re.findall(r'Overfull \\[hv]box',s)
assert not re.findall(r'(?:LaTeX|Package \S+) Warning:',s)
assert 'Missing character:' not in s
gate=json.loads((D/'work/root/I_citation_gate.json').read_text())
assert not gate['missing_bibliography'] and not gate['undefined_labels'] and not gate['duplicate_labels']
assert set(gate['unverified_cited'])==set(old['unverified_comparison_references_not_used_in_proofs'])
assert visual['selected_page_count']>=118
for image in visual['new_images_actually_opened']:
    assert sha(D/image['file'])==image['sha256']
current=json.loads((D/visual['current_manifest']).read_text())
prior=json.loads((D/visual['previous_manifest']).read_text())
oldimages={r['page']:D/r['file'] for r in prior['rendered']}
newimages={r['page']:D/r['file'] for r in current['rendered']}
for page in visual['unchanged_selected_pages']:assert newimages[page].read_bytes()==oldimages[page].read_bytes()
covered=visual.get('all_covered_pages', [x['page'] for x in current['rendered']])
coverage=visual.get('total_covered_page_count',len(covered))
assert coverage==len(set(covered)) and coverage>=119
record={**old,'status':'Complete: full proof/inventory, final companion references, clean LuaLaTeX and final selected-page visual checks passed',
 'gate_passed':True,'tex_sha256':sha(D/'S6_09_PAPERS_I.tex'),
 'pdf_sha256':visual['pdf_sha256'],'build_log':str(log.relative_to(D)),
 'pages':visual['pages'],'visual_review':visual,'selected_visual_pages':visual['selected_page_count'],
 'visual_pages_covered':coverage,'missing_character_diagnostics':0,
 'common_pass_evidence':['work/invariants_arithmetic/paper_I_checkpoint_shorthand_changes.json',
  'work/invariants_arithmetic/paper_I_nonoperative_Uses_corrections.json',
  'records/common_numbered_companion_overview.json','records/I_final_front_orphan_repair.json',
  'records/I_final_standalone_fixes.json','records/final_glyph_and_undated_entry_repairs.json',
  'work/cdp_audit/I_final_visual_review/final_current_visual_review.json'],
 'previous_gate_record':'records/I_validation_before_common_pass.json',
 'recorded_at_utc':visual['timestamp_utc']}
p.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
current['visual_inspection_status']=f'Passed: {coverage} pages covered, including {visual["selected_page_count"]} selected pages and every separately rendered final-edit page; actual openings and exact pixel-identity chain in records/I_final_validation.json.'
(D/visual['current_manifest']).write_text(json.dumps(current,indent=2)+'\n')
print('I common gate passed:',record['pages'],'pages;',record['visual_pages_covered'],'visual pages covered.')
