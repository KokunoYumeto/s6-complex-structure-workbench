"""Assembly metadata only; no source, inventory, or proof-status mutation."""
import json
from pathlib import Path

WORK = Path(__file__).resolve().parents[2] / 'work' / 'maps_audit'
manifest = json.loads((WORK / 'course_geometric_provider_full_proof_ranges.json').read_text())
by_name = {Path(r['retained_complete_proof']).name: r for r in manifest}
groups = [
    ('Geometric framing prerequisites', [
        'framed-manifolds-and-the-pontryagin-thom-map.md',
        'spin-six-and-the-framing-comparison.md']),
    ('Actual handle constructions and their maps', [
        'relative-morse-functions-and-original-handles.md',
        'morse-cancellation-with-controlled-support.md',
        'creating-an-original-cancelling-handle-pair.md',
        'morse-trajectories-and-critical-value-lowering.md',
        'rearranging-the-original-framed-handles.md',
        'removing-the-original-zero-and-top-handles.md',
        'integral-handle-chains-and-signed-incidences.md',
        'belt-sphere-complements-and-the-whitney-disk.md',
        'whitney-move-with-controlled-support.md',
        'whitney-moves-in-the-receiving-dimensions.md',
        'framed-handle-slides-and-index-one-removal.md',
        'higher-index-framed-slides-and-chain-maps.md',
        'realizing-framed-handles-and-middle-cancellation.md']),
    ('Actual stable cooperation and cobar calculations', [
        'the-exact-characteristic-two-coordinate-calculation.md',
        'the-original-projective-coordinate-and-actual-cooperations.md',
        'the-actual-mod-two-cooperation-comparison-through-degree-eight.md',
        'the-actual-mod-two-adams-resolution-and-cooperation-maps.md',
        'the-degree-six-milnor-cobar-calculation.md',
        'coefficient-rings-and-the-original-degree-six-class.md',
        'the-original-odd-prime-cooperations-and-degree-six-adams-calculation.md']),
    ('Convergence, integral comparison and geometric invariant', [
        'the-adams-tower-and-exact-inverse-limits.md',
        'the-original-adams-tower-and-arithmetic-completion.md',
        'the-original-integral-stable-group-and-its-completion-maps.md',
        'the-original-six-dimensional-framing-invariant.md'])]
names = [n for _, ns in groups for n in ns]
assert len(names) == len(set(names)) == 26 and set(names) == set(by_name)
rows = []
for group, ns in groups:
    for n in ns:
        r = by_name[n]
        rows.append({'suggested_order': len(rows)+1, 'group': group,
                     'source': r['source'], 'retained_complete_proof': r['retained_complete_proof'],
                     'whole_proof_range': r['whole_proof_range'], 'sha256': r['sha256'],
                     'current_check_event': r.get('current_check_event')})
out = {
    'reader': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode)', 'effort': 'Pro', 'date': '2026-11-17',
    'purpose': 'Source-chunk handoff to parent assembler; this is not a Paper III assembly.',
    'chapter_count': 26, 'numbered_provider_units': 206,
    'ordering_scope': 'A readable presentation order. Chapters contain both operative dependencies and forward outcome links, so this is not claimed to be a topological sort of every hyperlink.',
    'before_these_chapters': [
        'Use Paper I chain, CW and path-fibration statements through the six exact aliases in course_geometric_PaperI_aliases.json; do not print those statements/proofs again.',
        'Retain the fourteen new characteristic-class providers already inventoried; four prior-I duplicates remain aliases.',
        'Retain the separate eight duality/Euler units from checked_course_providers/manifold-duality-through-euler.md, source lines 1–250, with source range and producer metadata in course_duality_euler_full_check.json.'
    ],
    'insertions': [
        {'file': 'deliverables/work/maps_audit/pt_relative_bordism_repair.tex', 'place': 'At the relative extension and framed-bordism-to-homotopy step of the Pontryagin–Thom chapter; retain its four individually inventoried repair lemmas and the root-independent review.'},
        {'file': 'deliverables/work/maps_audit/coefficient_h28_complete_certificate.tex', 'place': 'After the coefficient-ring receiving calculation; supplies the complete finite differential certificate in print. Standalone typesetting QA remains pending.'}
    ],
    'after_these_chapters': 'The working-edition sphere-twists-and-the-original-smooth-six-sphere-comparison.md receiving chapter is already a separately inventoried original working result; retain it once after its geometric and stable providers. Its inventory is not replaced by these 206 new provider units.',
    'historical_status_rule': 'Retain original open analyses and distinct proofs. Later full-read/program/source events supplement historical states rather than deleting them.',
    'source_dependency_graph': 'deliverables/work/maps_audit/course_source_dependency_graph.json',
    'exact_I_aliases': 'deliverables/work/maps_audit/course_geometric_PaperI_aliases.json',
    'chapters': rows}
(WORK / 'course_provider_assembly_handoff.json').write_text(json.dumps(out, indent=2, ensure_ascii=False)+'\n')
print(f'Wrote {len(rows)} complete-chapter handoff rows.')
