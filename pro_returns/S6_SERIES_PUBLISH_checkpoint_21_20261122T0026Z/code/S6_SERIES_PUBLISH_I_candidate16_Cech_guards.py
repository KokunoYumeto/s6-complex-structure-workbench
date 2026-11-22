#!/usr/bin/env python3
"""Bind eight accent corrections to the complete source blocks read by root."""
from pathlib import Path
import hashlib
import json
import re
import fitz

ROOT = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
source = ROOT / 'S6_SERIES_PUBLISH_I.tex'
expected = '61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc'
assert sha(source) == expected
text = source.read_text()
hits = list(re.finditer(r'(?<!\\v )\bCech\b', text))
assert len(hits) == 8
pdf = ROOT / 'build/I_candidate16/S6_SERIES_PUBLISH_I.pdf'
with fitz.open(pdf) as doc:
    pdf_hits = [(p.number + 1, m.start()) for p in doc for m in re.finditer(r'\bCech\b', p.get_text())]
assert [p for p, _ in pdf_hits] == [20, 48, 79, 87, 92, 210, 321, 329]
guards = []
for k, (hit, (page, _)) in enumerate(zip(hits, pdf_hits), 1):
    line = text.count('\n', 0, hit.start()) + 1
    a = text.rfind('\n', 0, hit.start()) + 1
    b = text.find('\n', hit.end())
    before = text[a:b]
    after = before[:hit.start()-a] + r'\v Cech' + before[hit.end()-a:]
    assert text.count(before) == 1
    starts = list(re.finditer(r'\\begin\{(?:theorem|proposition|lemma|corollary|remark|definition)\}', text[:hit.start()]))
    start = starts[-1].start()
    end = text.index('\\end{proof}', hit.end()) + len('\\end{proof}')
    block = text[start:end]
    original = ROOT / f'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_Cech_{line}_before.tex'
    assert original.read_text() == block
    assert block.count(before) == 1
    proposed_text = block.replace(before, after, 1)
    proposed = original.with_name(original.name.replace('_before.tex', '_proposed.tex'))
    proposed.write_text(proposed_text)
    math_pattern = r'(?<!\\)\$.*?(?<!\\)\$|\\\[.*?\\\]|\\\(.*?\\\)'
    assert re.findall(math_pattern, block, re.S) == re.findall(math_pattern, proposed_text, re.S)
    for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\(?:cite\w*|ref|cref|eqref|SeriesRef)(?:\[[^\]]*\])?\{[^}]*\}']:
        assert re.findall(pattern, block) == re.findall(pattern, proposed_text)
    label = re.findall(r'\\label\{([^}]+)\}', block)[0]
    guards.append({
        'id': f'I16-root-C{k:02}', 'type': 'D23', 'page': page,
        'statement_id': label, 'before': before, 'after': after,
        'source_line': line, 'source_sha256': expected, 'pdf_sha256': sha(pdf),
        'reason': 'Restore the caron in Cech using the exact TeX spelling already established in this paper. The cocycle, cochain, cohomology class and every mathematical map in the complete owning statement/proof remain unchanged.',
        'original_full_block': str(original.relative_to(ROOT)), 'original_full_block_sha256': sha(original),
        'proposed_full_block': str(proposed.relative_to(ROOT)), 'proposed_full_block_sha256': sha(proposed),
        'all_mathematical_segments_identical': True,
        'all_labels_targets_citations_and_reference_commands_identical': True,
        'root_review': 'Root read all eight complete original statements/proofs and the exact accent maps; fam:src:A.4.2 was read in the provenance guard review. Complete block bytes outside each exact accent replacement are identical.',
        'status': 'approved by root, awaiting combined guarded application', 'mathematical_events_added': 0,
    })
out = ROOT / 'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_Cech_guards.json'
out.write_text(json.dumps(guards, indent=2) + '\n')
assert sha(source) == expected
print(json.dumps({'guards': len(guards), 'path': str(out.relative_to(ROOT)), 'sha256': sha(out), 'pages': [g['page'] for g in guards], 'source_unchanged': True}))
