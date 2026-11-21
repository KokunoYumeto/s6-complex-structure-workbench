#!/usr/bin/env python3
"""Exact, unapplied guards from the candidate16 full-page reading."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json
import re
from S6_SERIES_PUBLISH_I_cont_recount import proof_end

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SOURCE_SHA = '61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc'
PDF_SHA = '4a1633d9e19a82e3df92a0e3c31ada306b3e801f3051b0c1b7f0018d873f51a2'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
source = ROOT / 'S6_SERIES_PUBLISH_I.tex'
assert sha(source) == SOURCE_SHA
text = source.read_text()
specs = [
    (1, 318, 'fam:src:A.2.1',
     'We first justify why a local isomorphism must satisfy the exact affine\nequations on the marked finite cover. ', '',
     'Remove the standalone proof announcement. The preceding explicit cyclic norm matrices and the following ramified base-change equation, normalization map, local-ring lift, deck-equivariance identity, iteration and parity quotient remain verbatim. Those retained steps give the exact necessity asserted in the announcement. The complete statement and proof were read in full on pages 316--318.'),
    (2, 320, 'fam:src:A.4.2',
     'Here is a scheme-sensitive check. ', '',
     'Remove the standalone check announcement. The positive claim that the three distinguished points are fixed to first order remains, followed by the same finite and cusp critical ideals, parameter-ring injections, critical-value sections and first-order automorphism. The complete period-deformation statement and proof were read in full on pages 319--321.'),
]
archive = OUT / 'candidate16_review_blocks'
archive.mkdir(exist_ok=True)
guards = []
proposed = text
for number, page, sid, old, new, reason in specs:
    assert text.count(old) == 1 and '$' not in old and '\\' not in old
    position = text.index('\\label{'+sid+'}', text.index(r'\begin{document}'))
    start = list(re.finditer(r'\\begin\{(proposition|theorem|lemma|remark|definition|cited)\}', text[:position]))[-1]
    statement_end = text.index('\\end{'+start[1]+'}', position)+len('\\end{'+start[1]+'}')
    proof_start = text.index(r'\begin{proof}', statement_end)
    end = proof_end(text, proof_start)
    before = text[start.start():end]
    after = before.replace(old, new, 1)
    assert before.count(old) == 1
    assert before[:statement_end-start.start()] == after[:statement_end-start.start()]
    # The exact removed fragment is plain prose and contains neither TeX commands
    # nor math delimiters; the complete block is identical outside that fragment.
    assert after == before[:before.index(old)] + new + before[before.index(old)+len(old):]
    commands = lambda s: re.findall(r'\\[A-Za-z]+\*?|\\[^A-Za-z\s]', s)
    assert commands(before) == commands(after)
    before_path = archive / f'block_{number:02d}_before.tex'
    after_path = archive / f'block_{number:02d}_proposed.tex'
    before_path.write_text(before+'\n')
    after_path.write_text(after+'\n')
    (archive / f'block_{number:02d}.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True), after.splitlines(True), fromfile='before', tofile='proposed')))
    guards.append({
        'id': f'I16-prov-{number:02d}', 'page': page, 'type': 'D08',
        'statement_id': sid, 'line': text.count('\n', 0, text.index(old))+1,
        'before': old, 'after': new, 'reason': reason,
        'source_sha256': SOURCE_SHA, 'pdf_sha256': PDF_SHA,
        'original_full_block': str(before_path.relative_to(ROOT)),
        'original_full_block_sha256': sha(before_path),
        'proposed_full_block': str(after_path.relative_to(ROOT)),
        'proposed_full_block_sha256': sha(after_path),
        'statement_byte_identical': True,
        'all_mathematical_segments_and_commands_identical': True,
        'exact_plain_prose_fragment_deletion': True,
        'status': 'proposed, not applied', 'mathematical_events_added': 0,
    })
    proposed = proposed.replace(old, new, 1)
dest = OUT / 'S6_SERIES_PUBLISH_I_candidate16_provenance_guards.json'
dest.write_text(json.dumps(guards, ensure_ascii=False, indent=2)+'\n')
receipt = {
    'created_utc': datetime.now(timezone.utc).isoformat(), 'paper': 'I', 'candidate': 16,
    'source_sha256': SOURCE_SHA, 'pdf_sha256': PDF_SHA,
    'guard_file': str(dest.relative_to(ROOT)), 'guard_sha256': sha(dest),
    'proposals': 2, 'types': {'D08': 2},
    'proposed_whole_source_sha256': hashlib.sha256(proposed.encode()).hexdigest(),
    'reading_record': 'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_final_candidate16_reading_provenance.json',
    'reading_record_sha256': sha(OUT / 'S6_SERIES_PUBLISH_I_final_candidate16_reading_provenance.json'),
    'all_statements_byte_identical': True,
    'all_mathematical_segments_and_commands_identical': True,
    'no_hypothesis_quantifier_map_or_value_removed': True,
    'source_changes_applied': False, 'shared_files_modified': False,
    'mathematical_events_added': 0,
    'scope': 'Two exact prose-only announcements removed in complete proposed blocks. The full statements and proofs were actually read. Every byte outside the exact plain-prose fragments is preserved; this record adds no mathematical checking event.',
}
receipt_path = OUT / 'S6_SERIES_PUBLISH_I_candidate16_provenance_guard_receipt.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+'\n')
md = ['# Candidate16: exact provenance-agent D08 proposals', '',
      f'Source `{SOURCE_SHA}`; PDF `{PDF_SHA}`.', '',
      'The two proposals are unapplied. Each removes a plain-prose announcement before its complete mathematical argument. All statements, maps, hypotheses, quantifiers, values, mathematical segments and TeX commands are unchanged.', '']
for g in guards:
    md.extend([f"## {g['id']} — page {g['page']}", '', g['reason'], '',
               'Before:', '', '```tex', g['before'], '```', '',
               'After: delete the exact fragment above.', ''])
dest.with_suffix('.md').write_text('\n'.join(md)+'\n')
assert sha(source) == SOURCE_SHA
print(json.dumps({'guard_file': str(dest.relative_to(ROOT)), 'guard_sha256': sha(dest),
                  'receipt': str(receipt_path.relative_to(ROOT)), 'receipt_sha256': sha(receipt_path),
                  'proposals': 2, 'source_changes_applied': False}, indent=2))
