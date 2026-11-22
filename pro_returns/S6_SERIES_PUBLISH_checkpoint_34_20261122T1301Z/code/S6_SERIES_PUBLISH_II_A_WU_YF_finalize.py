from pathlib import Path
import datetime
import hashlib
import json

R = Path('agents/ii_checks_A/recovery_20261121T195642Z')
G = R / 'group08_WU_YF'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()

def digest(data):
    return hashlib.sha256(data).hexdigest()

def bind(path):
    p = Path(path)
    return {'path': str(p), 'sha256': digest(p.read_bytes())}

def write(name, data):
    p = G / name
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    return p

manifest = G / 'S6_SERIES_PUBLISH_II_A_WU_YF_editorial_proposals.json'
guards = json.loads(manifest.read_text())['guards']
validation = []
for tag in ('02WU', '02YF'):
    own = [g for g in guards if g['tag'] == tag]
    old = G / f'S6_SERIES_PUBLISH_II_{tag}_full_original.tex'
    new = G / f'S6_SERIES_PUBLISH_II_{tag}_full_proposed.tex'
    s = old.read_text()
    for g in own:
        assert digest(s.encode()) == g['intermediate_before_sha256']
        assert s.count(g['literal_old']) == 1
        pos = s.index(g['literal_old'])
        assert pos == g['offset_before']
        s = s[:pos] + g['literal_new'] + s[pos + len(g['literal_old']):]
        assert digest(s.encode()) == g['intermediate_after_sha256']
    assert s.encode() == new.read_bytes()
    for g in reversed(own):
        pos = g['offset_before']
        assert s[pos:pos + len(g['literal_new'])] == g['literal_new']
        s = s[:pos] + g['literal_old'] + s[pos + len(g['literal_new']):]
    assert s.encode() == old.read_bytes()
    validation.append({'tag': tag, 'guards': len(own),
                       'original': bind(old), 'proposed': bind(new),
                       'forward_exact': True, 'inverse_exact': True,
                       'all_intermediate_hashes_and_offsets_exact': True})
vpath = write('S6_SERIES_PUBLISH_II_A_WU_YF_guard_validation.json',
              {'completed_utc': now, 'canonical_writes': False, 'blocks': validation})

correction = R / 'S6_SERIES_PUBLISH_II_A_02YF_postrelease_correction.md'
frozen = R / 'S6_SERIES_PUBLISH_II_A_02YF_derivation.md'
assert digest(frozen.read_bytes()) == 'e288245f431add9a6d7a5e5487e348da7cb548d58a7418d5942c05f1aed7d7df'
comparison = R / 'S6_SERIES_PUBLISH_II_A_WU_YF_comparison.md'
marker = '## Postrelease correction to my frozen YF derivation'
assert marker not in comparison.read_text()
with comparison.open('a') as f:
    f.write('\n' + marker + '\n\n')
    f.write('The frozen YF Section 2 overstates the contraction R0→H as a homotopy equivalence. '
            'The separately bound correction preserves that frozen text and proves the exact maps: '
            'q is identity on H and constant on each attached P1; i is inclusion; q∘i=id; '
            'van Kampen gives inverse isomorphisms q_* and i_* on π1. '
            'On H2(R0;Z)=H2(H;Z)⊕Z^v the actual map q_* is (a,b1,...,bv)↦a, '
            'so each P1 fundamental class is killed. Thus the stronger assertion in my derivation '
            'requires this correction, while every original printed conclusion and the proposed source use only the valid π1 statement. '
            'The postrelease cellular-map program and its complete read output bind the same quotient and section. '
            'No additional prereading event is proposed. This disclosure qualifies the earlier comparison of the independent derivation; '
            'the finding that neither original manuscript block contains this error is unchanged.\n\n')
    f.write('Correction record: ' + str(correction) + '. Final whole-block rereading was repeated '
            'after the last definition of the rank-two bundle V and after the stage-conductor wording change. '
            'The observed reread began at 21:57:35 UTC; all remaining YF paragraphs, both complete originals '
            'and all 21 literal guards were then opened and read before this record was finalized at ' + now + '.\n')

wu_reread = ('Read the complete original five-item proof, final five-item proposed proof and all eight literal guards. '
             'Checked the identity-resolution conductor map, elliptic ruling base renaming, horizontal degree two, '
             'adjunction and branch-exponent reason for finite rank drop, the exact genus-one transport of the conductor '
             'pushout and curve-graph argument, every coefficient μ−1 graph move, both directions of minimality and '
             'zero Euler number, and the cusp/tacnode/triple branch cases. The proposed statement retains all original '
             'hypotheses and its equality criterion. Its uses of P4.15 are confined to the proved elliptic-ruled alternative.')
yf_reread = ('Read the complete original eight-item proof, final eight-item proposed proof and all thirteen literal guards. '
             'Checked the full conductor multiplicities through the identity resolution, the declared rank-two bundle V '
             'and Beauville intersection basis, the genus comparison, every μ−1 blowup case, the actual inclusion maps '
             'on fundamental groups, compact normalization pushout and its cofibration, all repeated-image identifications, '
             'surface-factor quotient and finite-cover genus formula, curve Euler count, and the final strict-positivity '
             'contradiction. The manuscript claims only the valid fundamental-group conclusion; my stronger frozen '
             'homotopy-equivalence sentence is explicitly corrected with q, i and the killed P1 H2 classes. '
             'The inherited historical phrase excluding coefficient-one exceptional curves is also explicitly corrected: μ=2 gives μ−1=1.')
rpath = write('S6_SERIES_PUBLISH_II_A_WU_YF_reread.json', {
    'completed_utc': now, 'checker': 'ii_check_a',
    'observed_final_reread_start_utc': '2026-11-21T21:57:35+00:00',
    'scope': 'complete owning statements, all five WU proof items, all eight YF proof items, all 21 literal guards',
    'records': [dict(validation[0], actual_comparative_record=wu_reread),
                dict(validation[1], actual_comparative_record=yf_reread)],
    'frozen_derivation_correction': bind(correction),
    'unchanged_frozen_YF': bind(frozen),
    'original_mathematical_statement_changed': False,
    'global_enumeration_mapping_remaining': True,
    'following_YF_broader_paragraph': 'root-owned and not opened by this checker'})

freeze_paths = {
    '02WU': Path('agents/ii_infra/derivation_freezes/02WU/20261121T214628857992Z/S6_SERIES_PUBLISH_derivation_freeze_receipt.json'),
    '02YF': Path('agents/ii_infra/derivation_freezes/02YF/20261121T214629219523Z/S6_SERIES_PUBLISH_derivation_freeze_receipt.json')}
release_paths = {
    '02WU': Path('agents/ii_infra/released_proofs/02WU/668d97539b684d0d/S6_SERIES_PUBLISH_release_receipt.json'),
    '02YF': Path('agents/ii_infra/released_proofs/02YF/f9f16d06e9d694ee/S6_SERIES_PUBLISH_release_receipt.json')}

# These six outcomes are written separately for the actual two proofs and the
# corresponding evidence; the loop below only serializes shared field names.
descriptions = [
('02WU', 'night:P4.22', 'targeted proof check', 'targeted',
 'Independently derived the elliptic-ruled normalization Euler inequality and its exact minimality criterion before opening either WU or the cited YF proof. Derived the effective horizontal degree-two alternatives, μ−1 conductor blowup rule, the actual conductor inclusion and finite pushout maps, virtually abelian curve-graph constraints, and every cusp/tacnode/triple zero-Euler case. Opened the original Beauville primary formulas and wrote the fresh cell/branch certificate; froze at 21:46:28 UTC. After release compared every one of the five printed proof items, including the exact use of the last-two-alternatives part of P4.15.'),
('02WU', 'night:P4.22', 'used and rechecked in this run', 'wording', wu_reread),
('02WU', 'night:P4.22', 'computation or formal certificate', 'computation',
 'The prerelease program performs weighted conductor-tree blowups and leaf contractions, Euler-cell counts, the Chern coefficient identity, and degree-bounded finite-evaluation certificates for the exact cusp, tacnode and ordinary-triple conductor maps. After release, read and reran the positively related pinned genus_one_conductor.py, whose declared owner is P4.14, then compared all its jet orders 2,3,4,6,8 and final arithmetic. The old algorithm uses SymPy matrix and augmented ranks; the new supplement uses explicit quotient maps and right inverses. The triple branches are transported by exchanging the first two normalization factors while fixing ambient x,y. The complete bounded association findings and every run/output hash are recorded; no historical WU program ownership or broader absence claim is invented.'),
('02YF', 'night:P4R.3', 'targeted proof check', 'targeted',
 'Independently derived the higher-genus ruling obstruction, double section with vertical fibres, μ−1 graph transformations, conductor inclusion on π1, finite-normalization pushout including repeated component images, curve free-product/Euler formulas and strict positivity before either target proof was opened; froze at 21:46:29 UTC. Compared all eight printed items after release. A stronger auxiliary sentence in my frozen derivation calling R0→H a homotopy equivalence is explicitly corrected postrelease: q∘i=id, van Kampen gives the required π1 isomorphism, and q_* kills each attached P1 H2 class. The frozen bytes are preserved and no extra independent event is credited. The source conclusion needs only the proved π1 assertion.'),
('02YF', 'night:P4R.3', 'used and rechecked in this run', 'wording', yf_reread),
('02YF', 'night:P4R.3', 'computation or formal certificate', 'computation',
 'The fresh prerelease weighted-tree program executes the precise coefficient μ−1 graph operations and actual leaf contractions, evaluates the curve Euler formula c+1−2Σg_i−b, and checks the exact zero-case identity 2−2g=−2(g−1). The first μ=2 blowup creates a coefficient-one exceptional curve, correcting the inherited historical summary while preserving its bytes. A separately dated postrelease cellular-map certificate gives q_* on H2 and i_* for the auxiliary derivation correction; it adds no prereading credit. The complete target, adjacent-scope receipt and three historical rows provide no named old routine within that bounded scope; the related conductor-jet program is compared under its explicit WU maps rather than assigned to YF.')]
events = []
for tag, owner, kind, suffix, outcome in descriptions:
    derivation = R / f'S6_SERIES_PUBLISH_II_A_{tag}_derivation.md'
    where = [derivation, freeze_paths[tag], release_paths[tag], comparison, rpath]
    if tag == '02YF':
        where += [correction, R / 'S6_SERIES_PUBLISH_II_A_02YF_quotient_cells_postrelease_run.json']
    events.append({
        'statement_id': owner, 'date': '2026-11-21',
        'who': 'GPT-6 Astra Pro (OpenAI), inherited effort, S6_SERIES_PUBLISH checker ii_check_a',
        'phase': 'publish-II',
        'source_file': str(G / f'S6_SERIES_PUBLISH_II_{tag}_full_proposed.tex'),
        'evidence_group': f'II-A-recovery-group08-{tag}', 'date_utc': now,
        'where': '; '.join(map(str, where)), 'type': kind, 'outcome': outcome,
        'event_id': f'S6_SERIES_PUBLISH_II_A_recovery_group08_{tag}_{suffix}_20261121'})
epath = write('S6_SERIES_PUBLISH_II_A_WU_YF_event_proposals.json', {
    'created_utc': now, 'canonical_events_added': 0, 'root_review_required': True, 'events': events})

files = [manifest, comparison, rpath, vpath, epath, correction,
         R / 'S6_SERIES_PUBLISH_II_A_WU_YF_ruled_cells_run.json',
         R / 'S6_SERIES_PUBLISH_II_A_WU_related_prior_run.json',
         R / 'S6_SERIES_PUBLISH_II_A_WU_related_jets_compare_run.json',
         R / 'S6_SERIES_PUBLISH_II_A_02YF_quotient_cells_postrelease_run.json',
         R / 'S6_SERIES_PUBLISH_Beauville_1978_opened_scope_01.json',
         R / 'group07_WT/S6_SERIES_PUBLISH_II_A_02WT_reading_precision.json',
         Path('records/S6_SERIES_PUBLISH_II_WU_prior_program_scope.json'),
         Path('records/S6_SERIES_PUBLISH_II_YF_prior_program_scope.json')]
for tag in ('02WU', '02YF'):
    files += [R / f'S6_SERIES_PUBLISH_II_A_{tag}_derivation.md', freeze_paths[tag], release_paths[tag],
              G / f'S6_SERIES_PUBLISH_II_{tag}_full_original.tex',
              G / f'S6_SERIES_PUBLISH_II_{tag}_full_proposed.tex']
for name in ('S6_SERIES_PUBLISH_II_A_WU_YF_ruled_cells',
             'S6_SERIES_PUBLISH_II_A_WU_related_jets_compare',
             'S6_SERIES_PUBLISH_II_A_02YF_quotient_cells_postrelease'):
    files += [Path('code') / (name + '.py'), Path('code') / (name + '.out')]
files += [Path('code/S6_SERIES_PUBLISH_II_A_WU_related_prior_genus_one_conductor.out'),
          Path('records/S6_SERIES_PUBLISH_II_opened_programs_recovery_01/genus_one_conductor.py'),
          Path('records/S6_SERIES_PUBLISH_II_opened_programs_recovery_01/receipt.json')]
index = R / 'S6_SERIES_PUBLISH_II_A_recovery_group08_WU_YF_final_index.json'
index.write_text(json.dumps({'created_utc': now, 'owners': ['02WU', '02YF'],
                            'guard_count': len(guards), 'event_proposal_count': len(events),
                            'canonical_writes': False, 'files': [bind(p) for p in files]}, indent=2) + '\n')
print(json.dumps({'final_index': bind(index), 'guards': len(guards), 'events': len(events),
                  'frozen_YF_unchanged': bind(frozen)}, indent=2))
