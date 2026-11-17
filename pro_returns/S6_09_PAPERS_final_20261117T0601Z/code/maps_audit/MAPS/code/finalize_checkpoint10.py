"""Record actual completed visual QA; invoke only after image inspection."""
from pathlib import Path
import json,datetime,shutil

root=Path(__file__).resolve().parents[1]
stage=root.parent/'checkpoint_build_10'/root.name
qa=json.loads((stage/'records/pdf_qa/qa.json').read_text())
extra=json.loads((stage/'records/pdf_qa/checkpoint_10_extra_pages.json').read_text())
audit=json.loads((stage/'records/register_audit.json').read_text())
spread=qa['rendered_pages'];new=extra['extra_rendered_pages']
qa['rendered_pages']=sorted(set(spread+new))
qa['preliminary_overflow_values_pt']=[44.37526,3.58476,2.04002]
qa['preliminary_max_overflow_pt']=44.37526
qa['repairs']=['Split D.WP5 into two gathered rows.',
 'Split E.T1 curve-class display into two aligned rows.',
 'Shortened the sentence introducing D.GC5.',
 'Expanded the undeclared Fix shorthand in D.2.41.',
 'Removed an unescaped filename from the Thomas bibliography note and rebuilt the stale generated BBL; preserved all failed logs and the previous BBL.',
 'The isolated E21 build split its E.H9a bank formula before integration.']
qa['visual_review']=(f'Passed: {len(spread)} spread pages and {len(new)} additional pages, '
 f'{len(qa["rendered_pages"])} distinct pages, inspected as rendered images. '
 'They cover the complete proofs of all ten newly registered statements, both changed scope conclusions, '
 'all repaired mathematical displays and the complete bibliography. No clipping, overlap or displaced labels was observed.')
qa['enlarged_pages']=[161,179,235]
qa['reviewed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
assert qa['pages']==316 and qa['overfull_boxes']==0 and not qa['unresolved_citations']
assert audit['manuscript_statement_count']==audit['register_statement_count']==188
assert audit['open_statements']==['D.2.4'] and audit['report_prompt_rows']==19
freeze=json.loads((stage/'records/checkpoint_10_manifest.json').read_text())['source_frozen_utc']
text=f'''

## Checkpoint10 typesetting and consistency verification

The frozen manuscript has 316 pages and 188 numbered statements. The global preflights found three distinct overfull regions: 44.37526pt, 3.58476pt and 2.04002pt. We split the D.WP5 and E.T1 displays and shortened the D.GC5 introductory sentence. We also expanded one undeclared notation macro, corrected an unescaped filename in a bibliography note, and rebuilt the obsolete generated bibliography that still contained the earlier faulty text. The isolated E.2.21 build had already split its bank-coordinate formula. All failed outputs and the superseded generated bibliography are retained. The final four-pass LuaLaTeX/BibTeX build has zero overfull boxes and zero unresolved citations.

We inspected {len(qa['rendered_pages'])} distinct rendered pages: {len(spread)} spread pages and {len(new)} additional pages, with overlaps removed. These cover all ten newly registered statements and their complete proofs, the updated D.2.4 and E.2.4 conclusions, every repaired mathematical display and the complete current bibliography. Pages161,179 and235 were additionally inspected enlarged. No clipping, overlap or displaced labels was observed. The first statement audit missed the newly worded E.2.4 heading; we changed it to the established Conclusion heading and retained the failed audit output. The final audit finds 188 manuscript statements and 188 CSV rows, with no missing or duplicate identifiers and all 19 prompt items in the opening report table. D.2.4 is the sole open statement.

The source freeze is recorded as {freeze}. D.2.37–43 and E.2.19–21 are included as audited statements. Later general-initial-pair and two-primary frame-parity work is retained as research, without a claimed invariant value or an unproved global extension. E.2 is complete by the explicit ordinary framed-handle comparison; D.2 remains open. The ten-hour decision is CONTINUE for the main-item advances recorded above.
'''
for location in [root,stage]:
 (location/'records/checkpoint_10_qa.json').write_text(json.dumps(qa,indent=2)+'\n')
 with (location/'S6_04_MAPS_MANIFOLDS_report.md').open('a') as f:f.write(text)
(stage/'records/pdf_qa/qa.json').write_text(json.dumps(qa,indent=2)+'\n')
shutil.copy2(__file__,stage/'code/finalize_checkpoint10.py')
print(json.dumps(qa,indent=2))
