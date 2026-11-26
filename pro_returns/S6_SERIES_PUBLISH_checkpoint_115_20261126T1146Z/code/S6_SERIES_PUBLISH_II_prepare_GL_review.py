"""Bind the complete GL proof comparison with occurrence-specific guards."""
from pathlib import Path
import datetime
import hashlib
import json
import re

R = Path(__file__).resolve().parents[1]


def sha(value):
    return hashlib.sha256(value.encode() if isinstance(value, str) else value).hexdigest()


def bound(path):
    return dict(path=path, sha256=sha((R / path).read_bytes()))


def read(path):
    return json.loads((R / path).read_text())


def write(path, value):
    p = R / path
    assert not p.exists(), p
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


base = 'agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group12/'
gp = base + 'S6_SERIES_PUBLISH_II_clean_group12_final_proposals.json'
ep = base + 'S6_SERIES_PUBLISH_II_clean_group12_event_proposals.json'
execution = base + 'S6_SERIES_PUBLISH_II_clean_group12_execution_receipt.json'
assert bound(gp)['sha256'] == '2f11dad2f7ddd5f35992cee0c96025c8a089b80f84c2f9b2e190e4ed4b03a7c9'
assert bound(ep)['sha256'] == '8ac6f676ccd357a2d1ddc909822395bf5dc6d75738e0a328ccfba3be86f73470'
assert bound(execution)['sha256'] == 'e1437d02ca0f679bc0a058f94b71a4435311965284584ddd7d23ed193f2c5ca9'
d, ev = read(gp), read(ep)
t, = d['targets']
inputs = [bound(gp), bound(ep), bound(execution)]
for parent in [d, t]:
    for key, item in parent.items():
        if key == 'source_at_final_review':
            continue
        if isinstance(item, dict) and 'path' in item and 'sha256' in item:
            assert bound(item['path'])['sha256'] == item['sha256'], key
            inputs.append(bound(item['path']))
assert read(d['preparation']['path'])['guards'] == t['guards']
source = bound('S6_SERIES_PUBLISH_II.tex')
assert source['sha256'] == '0451c788c5cfab04e0a2b0ec8075f440752f26ae8b19395aae5a975227dd6cf1'
s = (R / source['path']).read_text()
cur = (R / t['original_full_block']['path']).read_text()
assert s.count(cur) == 1
guards = []
for g in t['guards']:
    old, new = g['old'], g['new']
    expected = g['expected_occurrences_in_owning_block']
    starts = [m.start() for m in re.finditer(re.escape(old), cur)]
    assert len(starts) == expected
    for occurrence, start in enumerate(reversed(starts), 1):
        end = start + len(old)
        left, right = start, end
        while cur.count(cur[left:right]) != 1:
            left = max(0, left - 32)
            right = min(len(cur), right + 32)
        exact_old = cur[left:right]
        exact_new = cur[left:start] + new + cur[end:right]
        suffix = f'-occ{expected-occurrence+1}' if expected > 1 else ''
        guards.append(dict(change_id=g['change_id'] + suffix,
            old=exact_old, new=exact_new, defect_type=g['defect_type'],
            reason=g['reason'] + ' Context identifies this exact occurrence; the changed text is precisely the reviewed agent literal.'))
        cur = cur[:left] + exact_new + cur[right:]
assert len(guards) == 27
assert cur == (R / t['proposed_full_block']['path']).read_text()
assert not d['bibliography_guards']
fp, rp = t['freeze_receipt']['path'], t['release_receipt']['path']
freeze, release = read(fp), read(rp)
assert freeze['created_utc'] < release['created_utc']
assert release['freeze_receipt_sha256'] == bound(fp)['sha256']
assert bound(freeze['frozen_derivation_path'])['sha256'] == t['derivation']['sha256']
inputs.append(bound(freeze['frozen_derivation_path']))
methods = read(d['computation_methods']['path'])
for item in methods.values():
    if isinstance(item, dict) and 'path' in item:
        assert bound(item['path'])['sha256'] == item['sha256']
        inputs.append(bound(item['path']))
binding_path = 'records/S6_SERIES_PUBLISH_II_GL_code_and_programs_binding.json'
binding = read(binding_path)
assert bound(binding_path)['sha256'] == 'd5250cb6c4b77d5d0aa8881c9f786a66a819fdf162860b5e159b38bad6833730'
for copy in binding['copies']:
    assert bound(copy['source'])['sha256'] == copy['sha256']
    assert bound(copy['destination'])['sha256'] == copy['sha256']
oldtable = (R / binding['program_table_before']['path']).read_text()
newtable = (R / binding['program_table_after']['path']).read_text()
assert s.count(oldtable) == 1
assert oldtable.count('\\href{') == 19 and newtable.count('\\href{') == 21
inputs.append(bound(binding_path))
extra = dict(change_id='II-GL-PROGRAMS', statement_owner='tab:II:programs',
    old=oldtable, new=newtable, defect_type='D09',
    reason='Retain all nineteen current Programs rows and append the two exact GL certificate paths through the common repository commit macro.')
primary = read(d['primary_receipt']['path'])
for key in ['LR_source', 'LR_aux', 'LR_compiled_pdf', 'root_construction_inputs',
            'root_construction_receipt', 'current_E7_statement',
            'postfreeze_E13_full_block', 'postfreeze_E13_comparison']:
    assert bound(primary[key]['path'])['sha256'] == primary[key]['sha256']
    inputs.append(bound(primary[key]['path']))
bibliography = []
for key in ['LiuRollenske2026', 'Viaclovsky2026Combs']:
    m = re.search(r'\\bibitem(?:\[[^\n]*\])?\{' + re.escape(key) + r'\}', s)
    assert m
    end = s.find('\\bibitem', m.end())
    if end < 0:
        end = s.index('\\end{thebibliography}', m.end())
    bibliography.append(dict(key=key, complete_entry_sha256=sha(s[m.start():end]),
        actual_complete_entry_read=True, changed=False))
scope = (
    'Root actually read the entire frozen GL derivation, complete current original and final v2 '
    'proofs, whole comparison, all twenty-five agent guards and two events, every old/fresh/postrelease '
    'program and complete output, all input/freeze/release/computation/reading/validation/execution '
    'receipts, the five exact historical owner rows, and both complete nineteen/twenty-one-row '
    'Programs tables. Root read both unchanged bibliography entries, the full primary Proposition '
    '2.1 and Theorem5.1 source statements at lines246--269 and1702--1706, their actual aux numbering, '
    'and the complete current E7 input statement. Earlier root readings of the supplied construction '
    'inputs and complete E13 proof remain their declared cited-input scope. The exact global '
    'Weierstrass and scale transport, relative line-homomorphism, root morphism, canonical and '
    'connection frames, Hartogs inverse, cusp quotient ring and normalization restriction, and '
    'Kuranishi ideal maps were compared. The frozen normalization cocycle gives2ix and its source '
    'basis map yields the printed determinant-i jet model. The old computation was actually run '
    'after release; the postrelease critical-root norm supplies a separately disclosed alternative '
    'to its discriminant call. Its run receipt retains observed enclosing bounds without invented '
    'process timestamps. All mathematical statement claims and original displays are retained. '
    'No independent root check, extra computation event or PaperII rendered-page credit is claimed.'
)
reading_path = 'records/S6_SERIES_PUBLISH_II_GL_root_reading_01.json'
write(reading_path, dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    source=source, scope=scope, bound_inputs=inputs, bibliography_reading=bibliography,
    program_table_before=binding['program_table_before'], program_table_after=binding['program_table_after'],
    events_added=0, canonical_mutations=0, rendered_manuscript_page_credit=0))
target = dict(tag='01GL', statement_owner='cdp:st:E14', checker='i_provenance_recovery',
    freeze_receipt=bound(fp), release_receipt=bound(rp),
    frozen_derivation=bound(freeze['frozen_derivation_path']),
    original_full_block=t['original_full_block'], proposed_full_block=t['proposed_full_block'],
    actual_complete_original_proof_read=True, actual_complete_proposed_proof_read=True,
    comparison='The complete original and final logarithmic/critical-curve proof is compared to the frozen normalization-cocycle and critical-scheme route through the explicit coordinate, sheaf, source-basis and interpolation maps.',
    full_comparison=d['comparison'], guards=guards, mathematical_statement_and_values_unchanged=True,
    proof_repairs=[], scope_repairs=[])
proposal = 'records/S6_SERIES_PUBLISH_II_GL_reviewed_proposals.json'
write(proposal, dict(paper='II', targets=[target], bibliography_guards=[],
    root_reading=bound(reading_path), root_reading_scope=scope, bound_inputs=inputs,
    bibliography_reading=bibliography, program_table_binding=bound(binding_path)))
events = 'records/S6_SERIES_PUBLISH_II_GL_reviewed_event_proposals.json'
assert len(ev['events']) == 2
write(events, dict(original_checker_proposal=bound(ep), events=ev['events'],
    comparison=d['comparison'], root_reading=bound(reading_path),
    program_table_binding=bound(binding_path), events_unchanged=True,
    extra_independent_or_computation_events=0))
config = 'records/S6_SERIES_PUBLISH_II_GL_prepare_config.json'
write(config, dict(proposal=bound(proposal), source_before_sha256=source['sha256'],
    root_actual_complete_pairs_read=True, root_review_scope=scope,
    output='records/S6_SERIES_PUBLISH_II_GL_editorial_guard.json',
    expected_patch_count=28, extra_guards=[extra], mathematical_statement_and_values_unchanged=True))
print(json.dumps(dict(proposal=bound(proposal), events=bound(events), prepare_config=bound(config),
    root_reading=bound(reading_path), agent_guards=25, literal_owner_edits=27, programs_edits=1), indent=2))
