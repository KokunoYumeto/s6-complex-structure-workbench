"""Archive the two actually observed candidate19 recap proposals; never edit canonical files."""
from pathlib import Path
import datetime
import difflib
import hashlib
import json
import re

W = Path(__file__).resolve().parents[1]
A = W / 'agents/i_cont_edits'
SOURCE = W / 'S6_SERIES_PUBLISH_I.tex'
EXPECTED_SOURCE = 'f9e40fb592eb7f5c6d48070ba207e93d5b48ca71432176202041b88dd01278f7'
EXPECTED_PDF = 'e7a48c79d7bc5588f272b7d138f82fef8bbc504e86626f06a01c0bd86de32f7f'
SHA = lambda b: hashlib.sha256(b).hexdigest()
sha = lambda p: SHA(p.read_bytes())
source = SOURCE.read_text()
assert sha(SOURCE) == EXPECTED_SOURCE
reading = A / 'S6_SERIES_PUBLISH_I_final_candidate19_reading_edits.json'
assert sha(reading) == '597fd2ebcba965e17be3a276cc0d19537de34fc3725af5e772fe41228bd58671'
specs = [
    {
        'id': 'I19-edits-01', 'type': 'D08', 'statement_id': 'push:src:B.4.17', 'page': 222,
        'old': 'This proves the asserted strict inequality despite identity\nmonodromy.  ', 'new': '',
        'reason': 'Delete the pure closing recap after the homology display. The complete proposition, compact elliptic-bundle cocycle, punctured product, identity monodromy, two quotient maps, van Kampen argument, Mayer--Vietoris matrix, homology display and b1(H_-)=1 remain verbatim. The following b2(Z)=1 calculation and its Chern-class/spectral-sequence justification remain. The removed sentence adds no map, hypothesis, formula or reference.',
        'retained_witnesses': [r'b_1(Y)=0<1=b_1(H_-).', r' H_*(Y;\Z)=(\Z,0,0,\Z^3,\Z^2),\qquad b_1(H_-)=1.', r'the principal-bundle spectral sequence gives $b_2(Z)=1$.'],
    },
    {
        'id': 'I19-edits-02', 'type': 'D08', 'statement_id': 'push:src:B.4.24', 'page': 238,
        'old': ' This proves nonextension.', 'new': '',
        'reason': 'Delete the pure closing recap at the end of step8. The exact log-torus pairing and period lattice, prescribed axial origins, overlap section, quotient-sheaf sequence, injective ghost-order map, vanishing axial loop components and contradiction from a local section remain verbatim. The finite-coordinate/Kummer-cover and ordinary-gauge arguments also remain. The removed sentence adds no mathematical object, scope condition, formula or reference.',
        'retained_witnesses': [r'$Y=\Z u\oplus\Z\gamma$. Put', 'Consequently $F$ cannot be the difference of\nsections from $B_q$ and $B_r$.', 'section there; after shrinking the bidisc its\ntwo coordinate expressions would give precisely\nthe forbidden splitting.', r'The ghost calculation shows that $F$ lies outside this image.'],
    },
]

math_pattern = re.compile(r'(?<!\\)\$\$(?:[\s\S]*?)(?<!\\)\$\$|(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\\begin\{(?:equation|align|gather|multline|eqnarray)\*?\}[\s\S]*?\\end\{(?:equation|align|gather|multline|eqnarray)\*?\}')
command_pattern = re.compile(r'\\(?:[A-Za-z@]+\*?|.)')
reference_pattern = re.compile(r'\\(?:label|hypertarget|ref|eqref|autoref|pageref|SeriesRef|cite\w*)\*?(?:\[[^\]]*\])*\{[^}]*\}')
guards = []
comparisons = []
for number, spec in enumerate(specs, 1):
    assert source.count(spec['old']) == 1
    i = source.index(spec['old'])
    start = source.rfind('\\begin{proposition}', 0, i)
    end = source.index('\\end{proof}', i) + len('\\end{proof}')
    if source[end:end+1] == '\n':
        end += 1
    original = source[start:end]
    assert original.count('\\label{' + spec['statement_id'] + '}') == 1
    assert original.count(spec['old']) == 1
    proposed = original.replace(spec['old'], spec['new'], 1)
    assert original.split('\\begin{proof}', 1)[0] == proposed.split('\\begin{proof}', 1)[0]
    assert math_pattern.findall(original) == math_pattern.findall(proposed)
    assert command_pattern.findall(original) == command_pattern.findall(proposed)
    assert reference_pattern.findall(original) == reference_pattern.findall(proposed)
    assert '$' not in spec['old'] and '\\' not in spec['old']
    for witness in spec['retained_witnesses']:
        assert witness in original and witness in proposed, (spec['id'], witness)
    stem = A / f'S6_SERIES_PUBLISH_I_candidate19_edits_block_{number:02d}'
    paths = {name: Path(str(stem) + '_' + name + '.tex') for name in ['original', 'proposed']}
    diff_path = Path(str(stem) + '.diff')
    for name, text in [('original', original), ('proposed', proposed)]:
        assert not paths[name].exists()
        paths[name].write_text(text)
    diff_path.write_text(''.join(difflib.unified_diff(original.splitlines(True), proposed.splitlines(True), fromfile='original', tofile='proposed')))
    guard = dict(spec)
    guard.update({
        'source_sha256': EXPECTED_SOURCE, 'pdf_sha256': EXPECTED_PDF,
        'source_line': source[:i].count('\n') + 1,
        'original_full_block': str(paths['original'].relative_to(W)),
        'original_full_block_sha256': sha(paths['original']),
        'proposed_full_block': str(paths['proposed'].relative_to(W)),
        'proposed_full_block_sha256': sha(paths['proposed']),
        'full_block_source_start_line': source[:start].count('\n') + 1,
        'full_block_source_end_line': source[:end].count('\n'),
        'full_diff': str(diff_path.relative_to(W)), 'full_diff_sha256': sha(diff_path),
        'literal_source_block_archive_separator': 'Exact source slice includes its existing terminal newline; no extra separator was added.',
    })
    guards.append(guard)
    comparisons.append({
        'guard_id': spec['id'], 'statement_id': spec['statement_id'],
        'complete_statement_identical': True,
        'math_segments_identical': True, 'math_segment_count': len(math_pattern.findall(original)),
        'all_tex_command_sequences_identical': True, 'tex_command_count': len(command_pattern.findall(original)),
        'reference_label_target_sequences_identical': True, 'reference_label_target_count': len(reference_pattern.findall(original)),
        'removed_inline_math_mentions': [], 'added_references': [], 'removed_references': [],
        'exact_single_literal_deletion_reconstructs_proposed_full_block': True,
        'retained_witnesses_verified_in_both_full_blocks': spec['retained_witnesses'],
    })

result = {
    'paper': 'I', 'candidate': 19, 'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source_sha256': EXPECTED_SOURCE, 'pdf_sha256': EXPECTED_PDF,
    'reading_record': str(reading.relative_to(W)), 'reading_record_sha256': sha(reading),
    'guards': guards, 'full_block_preservation_comparisons': comparisons,
    'canonical_source_changed': False, 'canonical_status_changed': False,
    'mathematical_events_added': 0,
    'application_status': 'Proposed exact deletions only; root approval and canonical application remain separate.',
}
out = A / 'S6_SERIES_PUBLISH_I_candidate19_edits_guards.json'
assert not out.exists()
out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'guard_file': str(out.relative_to(W)), 'sha256': sha(out), 'guards': [g['id'] for g in guards], 'owners': [g['statement_id'] for g in guards], 'preservation_comparisons': comparisons}, indent=2))
