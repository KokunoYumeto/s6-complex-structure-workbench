"""Apply the independently established final II attribution/locator repairs.

The original complete E1.1 proof is moved, byte for byte, into the existing
known-results appendix.  Its statement label and number are preserved.  This
script does not reassemble II from any earlier source or overwrite its later
mathematical repairs.
"""
from pathlib import Path
import json
import hashlib
import re
from normalize_external_reference_words import transform as refwords

D = Path(__file__).resolve().parents[2]
p = D / 'S6_09_PAPERS_II.tex'
s = p.read_text()
before = s
archive = D / 'records/II_validation_before_final_credit_pass.json'
if not archive.exists():
    archive.write_text((D / 'records/II_final_validation.json').read_text())

key = r'\label{inv:E1.1}'
at = s.index(key)
a = s.index(r'\begin{proof}', at)
b = s.index(r'\end{proof}', a) + len(r'\end{proof}')
proof = s[a:b]
assert 'relative root divisors' in proof
credit = json.loads((D / 'work/invariants_arithmetic/inv_E_credit_insertions.json').read_text())[0]['credit_sentence']
front_credit = credit.split(' The following complete proof')[0]
replacement = (front_credit + '\nThe complete expanded proof, including the relative root-divisor and meromorphic-descent arguments, is retained in '
               r'\hyperref[app:II:inv-E1.1-rederivation]{the credited re-derivation in Appendix~\ref{app:II:known}}.' + '\n')
s = s[:a] + replacement + s[b:]
old_title = r'\begin{proposition}[Stability of the pencil for the standard family]'
new_title = r'\begin{proposition}[Credited re-derivation: stability of the pencil for the standard family]'
assert s.count(old_title) == 1
s = s.replace(old_title, new_title)
appendix_anchor = r'\label{app:II:known}'
addition = ('\n\n' + r'\subsection*{Complete re-derivation of standard-pencil stability}' + '\n'
            + r'\label{app:II:inv-E1.1-rederivation}' + '\n'
            + r'This is the full expanded proof of Proposition~\ref{inv:E1.1}. ' + credit + '\n\n'
            + proof + '\n\n')
assert s.count(appendix_anchor) == 1
s = s.replace(appendix_anchor, appendix_anchor + addition)
assert s.count(proof) == 1

bs = json.loads((D / 'work/cdp_audit/II_working_credit/BS76_exact_locator_replacements.json').read_text())
for r in bs['replacements']:
    assert s.count(r['old']) == r['expected_occurrences'], (r['old'], s.count(r['old']))
    s = s.replace(r['old'], r['new'])
s = refwords(s, 'II')
p.write_text(s)
record = {
    'before_tex_sha256': hashlib.sha256(before.encode()).hexdigest(),
    'after_tex_sha256': hashlib.sha256(s.encode()).hexdigest(),
    'E1.1_statement_label_preserved': 'inv:E1.1',
    'known_proof_destination': 'app:II:inv-E1.1-rederivation',
    'full_proof': proof,
    'full_proof_sha256': hashlib.sha256(proof.encode()).hexdigest(),
    'proof_occurrences_after_move': s.count(proof),
    'proof_mathematics_changed': False,
    'body_credit_and_location': replacement,
    'appendix_addition': addition,
    'old_title': old_title, 'new_title': new_title,
    'credit_source_record': 'work/invariants_arithmetic/inv_E_credit_comparison_5.json',
    'BS76_correction': bs,
    'external_reference_wording_record': 'records/II_external_reference_wording_repairs.json',
}
(D / 'records/II_final_attribution_and_locator_repairs.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print('Preserved the complete E1.1 proof in the known-results appendix; corrected the two BS76 locators and one duplicated reference kind.')
