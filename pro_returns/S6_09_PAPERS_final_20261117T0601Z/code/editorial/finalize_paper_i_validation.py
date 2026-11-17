"""Record the performed Paper I review and deterministic delivery checks.

This script does not perform a mathematical or visual review. The explicit
review declaration below records the inspections actually made by the authoring
agent; the other checks only compare files and enumerate editorial diagnostics.
"""
from pathlib import Path
import csv, hashlib, json, re

OUT = Path(__file__).resolve().parents[2]
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
tex = OUT / 'S6_09_PAPERS_I.tex'
pdf = OUT / 'S6_09_PAPERS_I.pdf'
log = OUT / 'editorial/S6_09_PAPERS_I_build_24.stdout.txt'
gate = json.loads((OUT / 'work/root/I_citation_gate.json').read_text())
render = json.loads((OUT / 'validation/I_a9755df2189f/render_manifest.json').read_text())
comparison = json.loads((OUT / 'records/I_final_visual_comparison.json').read_text())
rows = [r for r in csv.DictReader((OUT / 'S6_09_PAPERS_inventory.csv').open()) if r['paper'] == 'I']
s, ls = tex.read_text(), log.read_text()
boxes = [float(v) for v in re.findall(r'Overfull \\[hv]box \(([\d.]+)pt', ls)]
warnings = re.findall(r'(?:LaTeX|Package [^\n]+) Warning[^\n]*', ls)
assert len(rows) == 348
assert all(r['printed_label'] and r['your_check'] and r['check_outcome'] for r in rows)
assert not gate['missing_bibliography'] and not gate['undefined_labels'] and not gate['duplicate_labels']
assert set(gate['unverified_cited']) == {'CrRubin1991','bertrand1984','pham2025sigma','silverman1983specialization','tate1983variation'}
assert not boxes and not warnings
assert render['pdf_sha256'] == digest(pdf) and render['pages'] == 530
assert len(render['rendered']) == 54
assert not re.search(r'\\(?:input|include|bibliography)\s*\{', s)
assert s.count('github.com/KokunoYumeto/s6-complex-structure-workbench') == 1
for item in comparison['same_as_visually_reviewed']:
    assert (OUT / item['new']).read_bytes() == (OUT / item['reviewed_identical_image']).read_bytes()

record = {
  'paper': 'I',
  'status': 'Complete: proof/inventory, citation, clean LuaLaTeX and sampled visual checks passed; final companion-number synchronization remains at the three-paper gate',
  'checked_by': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, 17 November 2026',
  'completed_at_utc': '2026-11-17 02:17 UTC',
  'tex_sha256': digest(tex), 'pdf_sha256': digest(pdf),
  'build_log': str(log.relative_to(OUT)), 'pages': 530,
  'overfull_boxes': len(boxes), 'overfull_over_2pt': sum(v > 2 for v in boxes),
  'latex_or_package_warnings': warnings,
  'assigned_inventory_rows': len(rows), 'citations': gate['citations'],
  'unverified_comparison_references_not_used_in_proofs': gate['unverified_cited'],
  'undefined_labels': [], 'duplicate_labels': {},
  'self_contained_tex': True, 'repository_occurrences': 1,
  'visual_review': {
    'scope': '54 selected pages, not all 530 pages; former overflow locations, front matter, spread sample, course examples, result/program indices, separated open part and references',
    'render_manifest': 'validation/I_a9755df2189f/render_manifest.json',
    'pages': [r['page'] for r in render['rendered']],
    'previously_reviewed_pixel_identical_pages': [r['page'] for r in comparison['same_as_visually_reviewed']],
    'changed_pages_reviewed_in_final_contact_sheets': [r['page'] for r in comparison['changed_requires_review']],
    'final_contact_sheets_actually_inspected': [f'validation/I_a9755df2189f/contact_{i:02d}.png' for i in range(7,14)],
    'additional_full_page_inspections': [374,384],
    'findings': 'No clipping, overlapping text, or protruding formula/table at the reviewed locations. Distinct worked-example numbers, correct typed references, complete readable credit entries and visible spaces in program commands confirmed.'
  },
  'proof_review_evidence': [
    'work/root/proof_audit.md',
    'work/invariants_arithmetic/result_audit.json',
    'work/maps_audit/paperI_audit_closure.json',
    'S6_09_PAPERS_inventory.csv'
  ],
  'scope_qualification': 'Proof review is documented by the independent reading/rerun events in the inventory and detailed source records, not inferred from hashes or typesetting checks. Two questions remain in the explicitly separate final part with their exact known arguments and remaining gaps.',
  'historical_log_exclusions': 'Build 13 and 17 stdout files affected by the report-path bug are retained as misdirected reports, excluded from build evidence; see records/report_path_repair.json.'
}
(OUT / 'records/I_final_validation.json').write_text(json.dumps(record, indent=2) + '\n')
render['visual_inspection_status'] = '54-page selected review completed at its stated scope; see records/I_final_validation.json.'
(OUT / 'validation/I_a9755df2189f/render_manifest.json').write_text(json.dumps(render, indent=2) + '\n')
print(json.dumps({k:record[k] for k in ['paper','status','pages','assigned_inventory_rows','overfull_boxes','citations']},indent=2))
