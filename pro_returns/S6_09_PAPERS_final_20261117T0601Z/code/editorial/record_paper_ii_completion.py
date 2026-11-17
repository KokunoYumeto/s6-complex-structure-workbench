"""Record the observed II proof, reference, build and visual-review gate.

The inspection pages below were actually opened by the writing reader.
This script checks consistency of the retained evidence; it does not itself
perform a mathematical proof reading or visual inspection.
"""
from pathlib import Path
import csv,json,re,hashlib
D=Path(__file__).resolve().parents[2]
V=D/'validation/II_c8feaaa21980'
manifest=json.loads((V/'render_manifest.json').read_text())
comparison=json.loads((V/'comparison_to_build09.json').read_text())
opened=[600,601,611,619,623,635,636,643,644,645,650,653,654,655]
covered=set(opened)|set(comparison['pixel_identical_png_pages'])
assert covered==set(x['page'] for x in manifest['rendered'])
reader='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, 17 November 2026'
review={'reader':reader,'pdf_sha256':manifest['pdf_sha256'],
 'scope':'82 selected final pages: all former overflow loci plus the document-wide sample. Seventy render images are byte-identical to previously opened build09 images; fourteen final pages were actually opened in contact sheets18–21, with two also in that identical set.',
 'previously_reviewed_pixel_identical_pages':comparison['pixel_identical_png_pages'],
 'actual_final_contact_pages':opened,'actual_final_contacts':[f'validation/II_c8feaaa21980/contact_{i:02d}.png' for i in range(18,22)],
 'findings':'No clipping, overlapping text or protruding formula/table in the reviewed pages; the three formerly overfull credit-locator strings now wrap within their column.',
 'previous_review':'validation/II_665a15babe20/visual_review.json'}
(V/'visual_review.json').write_text(json.dumps(review,indent=2)+'\n')
s=(D/'S6_09_PAPERS_II.tex').read_text();log=(D/'S6_09_PAPERS_II.log').read_text()
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([\d.]+)pt',log)]
warnings=re.findall(r'^.*(?:LaTeX|Package \S+) Warning:.*$',log,re.M)
assert max(over,default=0)<=2 and not warnings,(over,warnings)
labels=re.findall(r'\\label\{([^}]+)\}',s)
rows=[r for r in csv.DictReader((D/'S6_09_PAPERS_inventory.csv').open()) if r['paper']=='II']
assert len(rows)==313 and all(r['printed_label'] in labels for r in rows)
assert not any('being completed' in r['check_outcome'] for r in rows)
assert not re.search(r'\\(?:input|include|bibliography)\{',s)
assert s.count('https://github.com/KokunoYumeto/s6-complex-structure-workbench')==1
ret=json.loads((D/'records/II_source_to_print_retention.json').read_text())
assert len(ret['canonical_blocks'])==237 and all(x['complete_block_retained'] for x in ret['canonical_blocks'])
programs=json.loads((D/'records/II_program_index.json').read_text())
assert len(programs)==89 and all((D/r['program']).exists() and r['exit_code']==0 for r in programs)
for r in programs:
 for p in r['output'].split('; '):assert (D/p).exists(),p
record={'paper':'II','status':'Complete: proof/inventory, citation, clean LuaLaTeX and sampled visual checks passed; final companion-number synchronization remains at the three-paper gate',
 'checked_by':reader,'tex_sha256':hashlib.sha256(s.encode()).hexdigest(),
 'pdf_sha256':hashlib.sha256((D/'S6_09_PAPERS_II.pdf').read_bytes()).hexdigest(),
 'build_log':'editorial/S6_09_PAPERS_II_build_12.stdout.txt','pages':manifest['pages'],
 'overfull_boxes':len(over),'overfull_over_2pt':sum(v>2 for v in over),'maximum_overfull_pt':max(over,default=0),
 'latex_or_package_warnings':warnings,'assigned_inventory_rows':len(rows),'citations':101,
 'unverified_cited':[],'undefined_labels':[],'duplicate_labels':{},'self_contained_tex':True,
 'repository_occurrences':1,'known_statements_in_credited_appendix':ret['whole_known_ids'],
 'canonical_complete_blocks_retained':237,'actual_executed_programs_with_outputs':89,
 'visual_review':review,'proof_review_evidence':['work/cdp_audit/result_audit.json',
 'work/cdp_audit/dependency_closure_events.json','work/root/II_push_E5_full_checks.json',
 'work/root/II_comb_full_check.json','records/II_working_supplement_root_changes.json',
 'records/II_editorial_mathematical_changes.json','records/II_positive_credit_changes.json',
 'records/II_source_to_print_retention.json','S6_09_PAPERS_inventory.csv'],
 'scope_qualification':'The specified comb kernel splitting remains in the plainly separated final part, with the full partial argument, proven bounds and exact missing period-section data. Its previously open Kuranishi clause is closed by the complete period-section proof. Proof checks are the recorded independent reading and derivation events, never inferred from this script, hashes or layout.',
 'recorded_at_utc':'2026-11-17 03:28 UTC'}
assert record['pdf_sha256']==manifest['pdf_sha256']
(D/'records/II_final_validation.json').write_text(json.dumps(record,indent=2)+'\n')
print('Paper II gate passed:',len(rows),'rows;',manifest['pages'],'pages;',len(covered),'selected pages visually covered.')
