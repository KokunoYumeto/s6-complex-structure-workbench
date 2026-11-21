#!/usr/bin/env python3
"""Archive three exact root findings after complete candidate16 page/proof reading."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
source = ROOT / 'S6_SERIES_PUBLISH_I.tex'
expected = '61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc'
assert sha(source) == expected
text = source.read_text()
items = [
    (53, 'fam:src:B.2.1', 'We prove the precise cusp necessity used next. ', '',
     'Remove the announcement preceding the exact local-lift assertion. The complete cusp-lift map, its hypotheses, toric-chart proof, winding comparison and global gluing argument remain byte-identical.'),
    (157, 'fam:src:E.2.1', 'We recall its charts to make the extension\nexplicit. ', '',
     'Remove the announcement preceding the actual node-chart construction. Every Tate parameter, chart, overlap map, quotient, finite action and integral topological calculation remains byte-identical.'),
    (261, 'inv:B3.2',
     'For clarity relative duality must now be used in its derived form.\nFor a sheaf $F$ locally free on the total space, it gives',
     'For a sheaf $F$ locally free on the total space, relative duality\nin its derived form gives',
     'State the same derived-duality application positively. The locally free sheaf F, displayed derived isomorphism, torsion Ext contribution, skyscraper length and complementary-degree calculation are unchanged.'),
]
guards = []
for k, (page, label, before, after, reason) in enumerate(items, 1):
    assert text.count(before) == 1
    original = ROOT / f'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_root_block_{k}_original.tex'
    offset = text.index(before)
    starts = list(re.finditer(r'\\begin\{(?:theorem|proposition|lemma|corollary|remark|definition)\}', text[:offset]))
    block_start = starts[-1].start()
    block_end = text.index('\\end{proof}', offset) + len('\\end{proof}')
    block = text[block_start:block_end]
    if original.exists():
        assert original.read_text() == block
    else:
        original.write_text(block)
    assert text.count(block) == 1 and block.count(before) == 1
    proposed_text = block.replace(before, after, 1)
    proposed = original.with_name(original.name.replace('_original.tex', '_proposed.tex'))
    proposed.write_text(proposed_text)
    # All mathematical segments and all control commands are unchanged.
    math_pattern = r'(?<!\\)\$.*?(?<!\\)\$|\\\[.*?\\\]|\\\(.*?\\\)'
    assert re.findall(math_pattern, block, re.S) == re.findall(math_pattern, proposed_text, re.S)
    assert re.findall(r'\\[A-Za-z@]+', block) == re.findall(r'\\[A-Za-z@]+', proposed_text)
    statement_end = block.index('\\end{proposition}') + len('\\end{proposition}')
    assert block[:statement_end] == proposed_text[:statement_end]
    guards.append({
        'id': f'I16-root-{k:02}', 'type': 'D08', 'page': page, 'statement_id': label,
        'before': before, 'after': after, 'reason': reason,
        'source_line': text.count('\n', 0, text.index(before)) + 1,
        'source_sha256': expected,
        'pdf_sha256': sha(ROOT / 'build/I_candidate16/S6_SERIES_PUBLISH_I.pdf'),
        'original_full_block': str(original.relative_to(ROOT)),
        'original_full_block_sha256': sha(original),
        'proposed_full_block': str(proposed.relative_to(ROOT)),
        'proposed_full_block_sha256': sha(proposed),
        'all_mathematical_segments_and_commands_identical': True,
        'statement_byte_identical': True,
        'root_review': 'Root read the complete original statement/proof and the exact proposed textual map after actual full-page reading. All content outside the exact replacement is identical.',
        'status': 'approved by root, awaiting combined guarded application',
        'mathematical_events_added': 0,
    })
out = ROOT / 'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate16_root_guards.json'
out.write_text(json.dumps(guards, indent=2) + '\n')
assert sha(source) == expected
print(json.dumps({'guards': len(guards), 'guard_file': str(out.relative_to(ROOT)), 'sha256': sha(out), 'source_unchanged': True}))
