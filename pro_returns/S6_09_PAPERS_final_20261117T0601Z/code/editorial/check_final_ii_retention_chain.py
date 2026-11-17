"""Verify exact final II retention by reversing only recorded final edits.

This byte check links the final paper to the fully read build12 source.
It complements, and does not replace, the independent proof/source readings.
"""
from pathlib import Path
import hashlib, json
D = Path(__file__).resolve().parents[2]
load = lambda name: json.loads((D/'records'/name).read_text())
sha = lambda text: hashlib.sha256(text.encode()).hexdigest()
current = (D/'S6_09_PAPERS_II.tex').read_text()
text = current
events = []
b = load('II_final_inline_bibliography_refresh.json')
assert sha(text) == b['after_tex_sha256']
assert text.count(b['current_bibliography']) == 1
text = text.replace(b['current_bibliography'], b['previous_bibliography'], 1)
assert sha(text) == b['before_tex_sha256']
events.append('Complete bibliography replacement reversed exactly')
c = load('II_final_credit_index_refresh.json')
assert sha(text) == c['after_tex_sha256']
assert text.count(c['after_complete_result_index']) == 1
text = text.replace(c['after_complete_result_index'], c['before_complete_result_index'], 1)
for r in reversed(c['exact_credit_insertions']['replacements']):
    assert text.count(r['new']) == r['expected_occurrences'], r['name']
    text = text.replace(r['new'], r['old'])
assert sha(text) == c['before_tex_sha256']
events.append('Six exact credit paragraphs and complete result index reversed exactly')
a = load('II_final_attribution_and_locator_repairs.json')
assert sha(text) == a['after_tex_sha256']
for r in reversed(load('II_external_reference_wording_repairs.json')):
    assert text.count(r['after']) == r['occurrences']
    text = text.replace(r['after'], r['before'])
for r in reversed(a['BS76_correction']['replacements']):
    assert text.count(r['new']) == r['expected_occurrences']
    text = text.replace(r['new'], r['old'])
assert text.count(a['appendix_addition']) == 1
text = text.replace(a['appendix_addition'], '', 1)
assert text.count(a['body_credit_and_location']) == 1
text = text.replace(a['body_credit_and_location'], a['full_proof'], 1)
assert text.count(a['new_title']) == 1
text = text.replace(a['new_title'], a['old_title'], 1)
assert sha(text) == a['before_tex_sha256']
old = load('II_validation_before_final_credit_pass.json')
assert sha(text) == old['tex_sha256']
events.append('Exact E1.1 proof move, two source locators, title and duplicated reference-kind word reversed exactly')
record = {
    'reader': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026',
    'passed': True,
    'final_tex_sha256': sha(current),
    'reconstructed_fully_read_tex_sha256': sha(text),
    'fully_read_baseline_validation': 'records/II_validation_before_final_credit_pass.json',
    'steps': events,
    'complete_E1_1_proof_retained_byte_identically_once': current.count(a['full_proof']) == 1,
    'canonical_CDP_blocks_retained': old['canonical_complete_blocks_retained'],
    'independent_readings': old['proof_review_evidence'],
    'meaning': 'Every byte outside the enumerated exact edits is unchanged from the fully read baseline. The only moved proof is present exactly once with identical bytes; all six attribution additions and the known-result relocation have their separate source/hypothesis checks.'
}
(D/'records/II_final_exact_retention_chain.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'passed': True, 'canonical_blocks': record['canonical_CDP_blocks_retained'], 'tex_sha256': sha(current)}))
