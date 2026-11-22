"""Bind the actually read CB/CC comparisons to occurrence-specific source edits."""
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


base = 'agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group13/'
gp = base + 'S6_SERIES_PUBLISH_II_clean_group13_final_proposals.json'
ep = base + 'S6_SERIES_PUBLISH_II_clean_group13_event_proposals.json'
assert bound(gp)['sha256'] == 'ca9c9ff83f9a3cc2d303e36386de8ddd7e68d647fb9794e08e029be9377f827b'
d, ev = read(gp), read(ep)
source = bound('S6_SERIES_PUBLISH_II.tex')
assert source['sha256'] == 'eddf628cd9e7cbc06077e87e14575f135952d13650c65712de07b2800fa4fcd8'
s = (R / source['path']).read_text()
inputs = [bound(gp), bound(ep)]
for parent in [d] + d['targets']:
    for key, item in parent.items():
        if isinstance(item, dict) and 'path' in item and 'sha256' in item:
            assert bound(item['path'])['sha256'] == item['sha256'], key
            inputs.append(bound(item['path']))

targets, freeze_times, release_times = [], [], []
for t in d['targets']:
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
                reason=g['reason'] + ' The surrounding context selects this reviewed literal occurrence exactly.'))
            cur = cur[:left] + exact_new + cur[right:]
    assert cur == (R / t['proposed_full_block']['path']).read_text()
    fp, rp = t['freeze_receipt']['path'], t['release_receipt']['path']
    freeze, release = read(fp), read(rp)
    freeze_times.append(freeze['created_utc'])
    release_times.append(release['created_utc'])
    assert release['freeze_receipt_sha256'] == bound(fp)['sha256']
    assert bound(freeze['frozen_derivation_path'])['sha256'] == t['derivation']['sha256']
    inputs.append(bound(freeze['frozen_derivation_path']))
    targets.append(dict(tag=t['tag'], statement_owner=t['statement_owner'],
        checker=t['checker'], freeze_receipt=bound(fp), release_receipt=bound(rp),
        frozen_derivation=bound(freeze['frozen_derivation_path']),
        original_full_block=t['original_full_block'], proposed_full_block=t['proposed_full_block'],
        actual_complete_original_proof_read=True, actual_complete_proposed_proof_read=True,
        comparison='Full frozen derivation and complete original/final proof comparison through the recorded adjunction, normal-line, Picard, differential and conormal-kernel maps.',
        full_comparison=d['comparison'], guards=guards,
        mathematical_statement_and_values_unchanged=True, proof_repairs=[], scope_repairs=[]))
assert max(freeze_times) < min(release_times)
assert sum(len(t['guards']) for t in targets) == 24

bib = []
for g in d['bibliography_guards']:
    original = (R / g['original_entry']['path']).read_text()
    proposed = (R / g['proposed_entry']['path']).read_text()
    assert s.count(original) == 1
    assert original.count(g['old']) == 1 and original.replace(g['old'], g['new'], 1) == proposed
    for key in ['original_entry', 'proposed_entry']:
        assert bound(g[key]['path'])['sha256'] == g[key]['sha256']
        inputs.append(bound(g[key]['path']))
    bib.append(dict(g, statement_owner='bib:' + g['key']))
assert len(bib) == 1

primary = read(d['primary_receipt']['path'])
actual_root_images = []
for item in primary['sources']:
    for key in ['pdf', 'text', 'retrieval', 'image']:
        assert bound(item[key]['path'])['sha256'] == item[key]['sha256']
        inputs.append(bound(item[key]['path']))
    actual_root_images.append(dict(source=item['name'], printed_page=item['printed_page'],
        pdf_page=item['pdf_page'], image=item['image'], actual_complete_image_read_by_root=True))
scope_path = 'records/S6_SERIES_PUBLISH_II_CB_CC_prior_program_scope_01.json'
assert bound(scope_path)['sha256'] == 'a945f6a2bb7c223eeee6c19a4ed1ad2c3eb9d30381f7cc346566686352081b80'
inputs.append(bound(scope_path))
scope = (
    'Root actually read both complete frozen derivations before the target comparison, both '
    'complete current original proofs and both complete final v2 proofs, all twenty-one owner '
    'guards and the bibliography guard, all four event proposals, the complete comparison and '
    'input/freeze/release/primary/reading/computation-scope/validation receipts. Root read the '
    'exact A.1.1 kernel input, the complete Peters bibliography pair and the unchanged complete '
    'BMS author-edition entry. Root actually viewed and read all of Peters journal page843 and '
    'BMS author-preprint page16. Earlier root reading of all eight exact historical rows and '
    'their bound complete twenty-one-row Programs table supplies the declared bounded old-code '
    'scope. No target routine was positively identified there; no repository-wide absence '
    'claim or computation execution is made. The frozen normal-line product and adjunction '
    'calculation was compared with the printed weighted Euler calculation; the local '
    'multiplicity/annulus maps, including self-double branches, now explain that equation. '
    'The Picard/Chern map, differential quotient, conormal kernel and projection formula '
    'identify the all-twist groups. The additional b1 hypothesis is used exactly in the final '
    'Betti deduction. Every original display, tag, label, mathematical hypothesis and '
    'conclusion is preserved. The historical safe packet C.3.1 wording is not given new '
    'singular-domain credit. Root makes no separate independent-check claim and adds no '
    'PaperII rendered-page credit. The checker original v1 files remain preserved; root '
    'claims full reading of the final v2 pair, not a separate full v1 reading.'
)
reading_path = 'records/S6_SERIES_PUBLISH_II_CB_CC_root_reading_01.json'
write(reading_path, dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    source=source, scope=scope, bound_inputs=inputs, actual_root_primary_images=actual_root_images,
    mathematical_events_added=0, canonical_mutations=0, rendered_manuscript_page_credit=0))
proposal = 'records/S6_SERIES_PUBLISH_II_CB_CC_reviewed_proposals.json'
write(proposal, dict(paper='II', targets=targets, bibliography_guards=bib,
    root_reading=bound(reading_path), root_reading_scope=scope, bound_inputs=inputs,
    mathematical_statement_and_values_unchanged=True))
events = 'records/S6_SERIES_PUBLISH_II_CB_CC_reviewed_event_proposals.json'
assert len(ev['events']) == 4
write(events, dict(original_checker_proposal=bound(ep), events=ev['events'],
    comparison=d['comparison'], root_reading=bound(reading_path), events_unchanged=True,
    extra_independent_or_computation_events=0))
config = 'records/S6_SERIES_PUBLISH_II_CB_CC_prepare_config.json'
write(config, dict(proposal=bound(proposal), source_before_sha256=source['sha256'],
    root_actual_complete_pairs_read=True, root_review_scope=scope,
    output='records/S6_SERIES_PUBLISH_II_CB_CC_editorial_guard.json',
    expected_patch_count=25, extra_guards=[], mathematical_statement_and_values_unchanged=True))
print(json.dumps(dict(proposal=bound(proposal), events=bound(events), prepare_config=bound(config),
    root_reading=bound(reading_path), owner_guards=21, literal_owner_edits=24, bibliography_edits=1), indent=2))
