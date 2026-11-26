"""Bind GN's full proof reading, two coefficient repairs and exact maps."""
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


base = 'agents/ii_infra/recovery_20261121/'
gp = base + 'S6_SERIES_PUBLISH_II_01GN_guards_final.json'
cp = base + 'S6_SERIES_PUBLISH_II_01GN_comparison.json'
ep = base + 'S6_SERIES_PUBLISH_II_01GN_event_proposals.json'
ap = base + 'S6_SERIES_PUBLISH_II_01GN_public_locator_and_transpose_addendum.json'
assert bound(gp)['sha256'] == '2fe85cfefe18cabebffc4060a05649363220cab55c685cba47eae8556f3890ed'
assert bound(cp)['sha256'] == '828541b693b29eb43d0ecdf557d8c385d4a92d44df5d7c1f1199c2aa361fb80d'
assert bound(ep)['sha256'] == 'a45bc7028fe413dc02de6284da7c548c7a2f316ca6211eccb4c9213f2c13e931'
assert bound(ap)['sha256'] == 'f5ac77758d564edcebaf06916950291896a32edc1f109efa43c323c6b8f15c16'
d, c, ev, addendum = read(gp), read(cp), read(ep), read(ap)
source = bound('S6_SERIES_PUBLISH_II.tex')
assert source['sha256'] == '801f7d402b26585a0f86cdb4e501e09b000965bf9ff22941cc737b1e3804a532'
s = (R / source['path']).read_text()
checked = {}


def verify(value):
    if isinstance(value, dict):
        if 'path' in value and 'sha256' in value:
            actual = bound(value['path'])
            assert actual['sha256'] == value['sha256'], (value, actual)
            checked[value['path']] = actual
        for child in value.values():
            verify(child)
    elif isinstance(value, list):
        for child in value:
            verify(child)


verify(c)
verify(ev)
owner, = d['guards']
cur = owner['before']
assert s.count(cur) == 1
guards = []
for number, edit in enumerate(owner['literal_edits'], 1):
    assert cur.count(edit['before']) == 1
    assert cur.index(edit['before']) == edit['sequential_before_offset']
    cur = cur.replace(edit['before'], edit['after'], 1)
    guards.append(dict(change_id=f'II-GN-{number:03d}', old=edit['before'], new=edit['after'],
        defect_type=edit['type'], reason=edit['reason']))
assert len(guards) == 15 and cur == owner['after']
for key, field in [('original_full_block', 'before'), ('proposed_full_block', 'after')]:
    assert bound(owner[key])['sha256'] == owner[key + '_sha256']
    assert (R / owner[key]).read_text() == owner[field]
assert addendum['bound_final_full_block_sha256'] == owner['proposed_full_block_sha256']
assert bound(addendum['additive_record'])['sha256'] == addendum['additive_record_sha256']
images = []
for page in addendum['actual_complete_public_page_readings']:
    assert bound(page['image'])['sha256'] == page['image_sha256']
    if 'pdf' in page:
        assert bound(page['pdf'])['sha256'] == page['pdf_sha256']
    images.append(dict(bound(page['image']), printed_page=page['printed_page']))
primary = read(c['public_primary_reading']['path'])
assert bound(primary['pdf'])['sha256'] == primary['pdf_sha256']
for page in primary['pages']:
    if page['printed_page'] in [16, 22, 23]:
        assert bound(page['image'])['sha256'] == page['image_sha256']
        images.append(dict(bound(page['image']), printed_page=page['printed_page']))
assert len(images) == 5
binding_path = 'records/S6_SERIES_PUBLISH_II_GN_code_and_programs_binding.json'
assert bound(binding_path)['sha256'] == '0388d8cbfe669ef76729e93beb8d43347e4116647d872dd9f1538caa9c583f52'
binding = read(binding_path)
for copy in binding['copies']:
    assert bound(copy['source'])['sha256'] == copy['sha256']
    assert bound(copy['destination'])['sha256'] == copy['sha256']
oldtable = (R / binding['program_table_before']['path']).read_text()
newtable = (R / binding['program_table_after']['path']).read_text()
assert s.count(oldtable) == 1
assert oldtable.count('\\href{') == 21 and newtable.count('\\href{') == 23
extra = dict(change_id='II-GN-PROGRAMS', statement_owner='tab:II:programs',
    old=oldtable, new=newtable, defect_type='D09',
    reason='Preserve all twenty-one current Programs rows and append the two exact GN certificates through the common repository commit macro.')
fp, rp = c['freeze_receipt']['path'], c['release_receipt']['path']
freeze, release = read(fp), read(rp)
assert freeze['created_utc'] < release['created_utc']
assert release['freeze_receipt_sha256'] == bound(fp)['sha256']
assert bound(freeze['frozen_derivation_path'])['sha256'] == c['derivation']['sha256']
bibliography = []
for key in ['Viaclovsky2026Two', 'Viaclovsky2026Combs']:
    m = re.search(r'\\bibitem(?:\[[^\n]*\])?\{' + re.escape(key) + r'\}', s)
    assert m
    end = s.find('\\bibitem', m.end())
    if end < 0:
        end = s.index('\\end{thebibliography}', m.end())
    bibliography.append(dict(key=key, complete_entry_sha256=sha(s[m.start():end]),
        actual_complete_entry_read=True, changed=False))
scope = (
    'Root actually read the entire frozen GNv2 derivation, complete released/current original '
    'and finalv2 five-item proof, all fifteen literal edits, both full comparisons, all successful '
    'programs and every output field, input/freeze/release/scope/validation/event and additive '
    'locator/transpose receipts, the four exact historical owner rows, both unchanged complete '
    'bibliography entries, and both complete twenty-one/twenty-three-row Programs tables. Root '
    'actually viewed/read full public Combs pages12,16,22,23 and Two page6. The additive record '
    'gives the exact inverse transpose maps between primary row frames/quotients and the final '
    'column graph, including entrywise derivative transport. The higher-root pullback, weighted '
    'entry factors, cusp coherent frames, finite-character lifts, determinant line and all-m '
    'exponent correspondence agree. The two coefficient errors are repaired explicitly: Dprime=aD '
    'gives coefficient a^2 and differential-frame square a^-2; the specified logarithmic derivative '
    'carries1/(2pi i). The program checks coefficient covariance and the graph/six-minor identities; '
    'the reciprocal differential factor is proved in the frame argument, not inferred from its '
    'printed output string. All theorem ranks, zero orders and polynomial conclusions, original '
    'displays and target identities remain. No extra independent/computation or PaperII rendered '
    'page credit is claimed. Failed prereading versions are preserved without success credit.'
)
reading = 'records/S6_SERIES_PUBLISH_II_GN_root_reading_01.json'
write(reading, dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    source=source, scope=scope, guard_proposal=bound(gp), comparison=bound(cp),
    additive_locator_and_transpose=bound(ap), checked_bindings=list(checked.values()),
    frozen_derivation=bound(freeze['frozen_derivation_path']),
    primary_images_actually_read_by_root=images, bibliography_reading=bibliography,
    programs_binding=bound(binding_path), proof_repairs=c['proof_errors'],
    mathematical_statement_unchanged=True, proof_coefficient_values_corrected=True,
    events_added=0, canonical_mutations=0, paper_II_rendered_page_reading_credit=0))
target = dict(tag='01GN', statement_owner='cdp:st:E16', checker='restore_build',
    freeze_receipt=bound(fp), release_receipt=bound(rp),
    frozen_derivation=bound(freeze['frozen_derivation_path']),
    original_full_block=c['original_full_block'], proposed_full_block=c['proposed_full_block'],
    actual_complete_original_proof_read=True, actual_complete_proposed_proof_read=True,
    comparison='All five complete proof items compared through the explicit root, coherent boundary, graph projection, transpose and determinant-frame maps; both coefficient repairs preserve the theorem conclusions.',
    full_comparison=bound(cp), guards=guards, mathematical_statement_unchanged=True,
    mathematical_statement_and_values_unchanged=False, proof_repairs=c['proof_errors'], scope_repairs=[])
proposal = 'records/S6_SERIES_PUBLISH_II_GN_reviewed_proposals.json'
write(proposal, dict(paper='II', targets=[target], bibliography_guards=[],
    root_reading=bound(reading), root_reading_scope=scope, bound_inputs=[bound(gp), bound(cp), bound(ep), bound(ap), bound(binding_path)],
    bibliography_reading=bibliography, proof_repairs=c['proof_errors']))
events = 'records/S6_SERIES_PUBLISH_II_GN_reviewed_event_proposals.json'
write(events, dict(original_checker_proposal=bound(ep), comparison=bound(cp),
    additive_locator_and_transpose=bound(ap), root_reading=bound(reading), events=[
    dict(statement_owner='cdp:st:E16', event_type='targeted proof check', event_count=1,
        scope='The complete prerelease derivation proves the original, higher-root, two-parameter, Liu-Rollenske and comb rank loci using exact root pullbacks, coherent cusp frames, lattice/pairing maps and weighted determinant polynomials. Original-family E8 and earlier completed checks are declared inputs. Two proof coefficient errors are repaired with the exact Hodge/tangent/differential and logarithmic maps; theorem conclusions are unchanged. Fresh polynomial convolution and explicit determinants, supplemented by a postrelease graph/six-minor covariance calculation, verify the finite arithmetic; the general exponent statement has a separate all-m proof.'),
    dict(statement_owner='cdp:st:E16', event_type='used and rechecked in this run', event_count=1,
        scope='Actually read every original/final proof item and all fifteen literal edits; all original displayed formulas, references and targets remain. Exact primary public locators, the row-to-column transpose/quotient map, and both coefficient repairs are bound. The complete21-row Programs table is retained and two certificate rows added; successful and failed computation versions/outputs remain byte-identical. No extra independent or computation event and no PaperII rendered-page credit.')], events_added=0))
config = 'records/S6_SERIES_PUBLISH_II_GN_prepare_config.json'
write(config, dict(proposal=bound(proposal), source_before_sha256=source['sha256'],
    root_actual_complete_pairs_read=True, root_review_scope=scope,
    output='records/S6_SERIES_PUBLISH_II_GN_editorial_guard.json',
    expected_patch_count=16, extra_guards=[extra], mathematical_statement_and_values_unchanged=False,
    mathematical_statement_unchanged=True, proof_repairs=c['proof_errors']))
print(json.dumps(dict(proposal=bound(proposal), events=bound(events), prepare_config=bound(config),
    root_reading=bound(reading), proof_coefficient_repairs=len(c['proof_errors']), owner_edits=15,
    program_table_edits=1), indent=2))
