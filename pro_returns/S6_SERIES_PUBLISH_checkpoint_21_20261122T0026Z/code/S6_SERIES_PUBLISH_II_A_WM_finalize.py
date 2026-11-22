from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

B = Path('/workspace/scratch/08a92fb2355d/S6_SERIES_PUBLISH')
R = Path('agents/ii_checks_A/recovery_20261121T195642Z')
G = R / 'group09_WM'
now = datetime.now(timezone.utc).isoformat()

def sha(p):
    return hashlib.sha256((B/p).read_bytes()).hexdigest()

def digest(s):
    return hashlib.sha256(s.encode()).hexdigest()

def save(p, a):
    (B/p).write_text(json.dumps(a, indent=2)+'\n')

def bind(p):
    return {'path':str(p), 'sha256':sha(p)}

manifest_path = G/'S6_SERIES_PUBLISH_II_A_WM_editorial_proposals.json'
m = json.loads((B/manifest_path).read_text())
old_path = G/'S6_SERIES_PUBLISH_II_02WM_full_original.tex'
new_path = G/'S6_SERIES_PUBLISH_II_02WM_full_proposed.tex'
old = (B/old_path).read_text(); new = (B/new_path).read_text()
current = old
for g in m['guards']:
    assert digest(current) == g['intermediate_before_sha256']
    assert current.count(g['literal_old']) == 1
    assert current.index(g['literal_old']) == g['offset_before']
    current = current.replace(g['literal_old'],g['literal_new'],1)
    assert digest(current) == g['intermediate_after_sha256']
assert current == new
for g in reversed(m['guards']):
    pos = g['offset_before']; text = g['literal_new']
    assert current[pos:pos+len(text)] == text
    current = current[:pos]+g['literal_old']+current[pos+len(text):]
assert current == old
source = (B/'S6_SERIES_PUBLISH_II.tex').read_text()
assert source.count(old) == 1
for g in m['bibliography_guards']:
    assert source.count(g['literal_old']) == 1
    assert (B/g['full_original_path']).read_text() == g['literal_old']
    assert (B/g['full_proposed_path']).read_text() == g['literal_new']

freeze_path = Path('agents/ii_infra/derivation_freezes/02WM/20261121T220857561650Z/S6_SERIES_PUBLISH_derivation_freeze_receipt.json')
release_path = Path('agents/ii_infra/released_proofs/02WM/230b85aca88a0ae7/S6_SERIES_PUBLISH_release_receipt.json')
derivation_path = R/'S6_SERIES_PUBLISH_II_A_02WM_derivation.md'
f = json.loads((B/freeze_path).read_text())
assert sha(derivation_path) == f['derivation_sha256'] == 'd48cff5871f3b583e612106e8b94f5d26b4d9792296d5612e4760d9be16255ec'
assert sha(Path(f['frozen_derivation_path'])) == f['derivation_sha256']

precision_path = R/'S6_SERIES_PUBLISH_II_A_02WM_postrelease_precision.json'
save(precision_path, {
  'recorded_utc': now, 'tag':'02WM','statement_owner':'night:P4.15',
  'timing':'Postrelease precision correction following root whole-derivation review.',
  'frozen_derivation': bind(derivation_path), 'frozen_bytes_changed':False,
  'literal_frozen_sentence':'Its exact conductor normalization η_R has Euler number 6; a disjoint union of smooth elliptic curves has Euler number zero.',
  'location':'Frozen derivation section 1, second scope-test paragraph.',
  'correction':'The domain of η_R is the disjoint union of six P1 curves and has Euler number 12. Its target R is their hexagon quotient and has Euler number 6.',
  'exact_map':'η_R: disjoint union over the six boundary curves C_e^ε ≅ P1 → R, restricting to the corresponding boundary normalization map ρ_e^ε. Each of the six nodes of R has two preimages; η_R is one-to-one away from these twelve preimages.',
  'calculation':'e(domain η_R)=6·2=12. Removing the twelve preimages and restoring the six image nodes gives e(R)=12−12+6=6.',
  'unaffected_evidence':bind(R/'S6_SERIES_PUBLISH_II_A_02WM_scope_counterexample_preproof.md'),
  'effect':'The separate detailed preproof witness already computes e(R)=6 correctly. The proposed statement and proof use R throughout. Its rational-conductor refutation and the two D25 source-scope repairs are unchanged.',
  'new_independent_credit':0, 'canonical_events_added':0
})

comparison_path = R/'S6_SERIES_PUBLISH_II_A_WM_comparison.md'
comparison = (B/comparison_path).read_text()
addition = '''\n\n## Dated postrelease precision correction\n\nRoot's whole-derivation review identified the wording of the frozen Section 1\nsummary: “Its exact conductor normalization η_R has Euler number 6.” The\nmap's domain is the disjoint union of six P1 curves, with Euler number 12;\nits target R is the hexagon, with Euler number 6. The exact finite map has\ntwelve preimages of six nodes and is one-to-one elsewhere, giving\n12−12+6=6 for R. The detailed preproof counterexample already uses this\ncorrect target calculation. The separately dated precision JSON records the\ncorrection without changing any frozen bytes or awarding another independent\ncheck. The source proposal and both scope repairs are unchanged.\n'''
assert '## Dated postrelease precision correction' not in comparison
(B/comparison_path).write_text(comparison+addition)

reread_path = G/'S6_SERIES_PUBLISH_II_A_WM_reread.json'
save(reread_path, {
  'recorded_utc':now, 'checker':'ii_check_a', 'tag':'02WM',
  'full_original':bind(old_path), 'full_proposed':bind(new_path),
  'actual_reading':'Read the complete original statement and all five proof items after release. Read the complete final proposed block, including the unchanged Hopf item, after the last two notation/section-map edits. Read every bibliography original/proposed pair and all ten target guard transformations. All 36 postrelease ruled rows, all four conductor rows and the final Euler row were read, with the complete new source.',
  'step_comparison':bind(comparison_path), 'postrelease_precision':bind(precision_path),
  'statement_unchanged':False,
  'mathematical_scope':'Singular reduced support is required for classification; the elliptic conductor and image conclusion is confined to the last two alternatives. The numerical identity, all numerical bounds, immersion conclusion and exact finite unramified maps in that range are retained.',
  'receiving_audit':bind(Path('records/S6_SERIES_PUBLISH_II_WM_root_receiving_scope.json')),
  'new_independent_credit_from_rereading':0,
  'global_enumeration_D04_closed':False
})
validation_path = G/'S6_SERIES_PUBLISH_II_A_WM_guard_validation.json'
save(validation_path, {
  'completed_utc':now,'canonical_writes':False,'target_guards':len(m['guards']),
  'bibliography_guards':len(m['bibliography_guards']), 'original':bind(old_path),
  'proposed':bind(new_path), 'forward_exact':True,'inverse_exact':True,
  'all_intermediate_hashes_and_offsets_exact':True,
  'original_whole_block_occurs_once_in_current_source':True,
  'all_bibliography_old_blocks_occur_once':True,
  'canonical_source_sha256':sha(Path('S6_SERIES_PUBLISH_II.tex')),
  'frozen_derivation_sha256_unchanged':f['derivation_sha256']
})

where = '; '.join(map(str,[derivation_path,freeze_path,release_path,comparison_path,reread_path,precision_path]))
common = {
  'statement_id':'night:P4.15','date':'2026-11-21',
  'who':'GPT-6 Astra Pro (OpenAI), inherited effort, S6_SERIES_PUBLISH checker ii_check_a',
  'phase':'publish-II','source_file':str(new_path),'evidence_group':'II-A-recovery-group09-02WM',
  'date_utc':now,'where':where
}
events = [
 dict(common, type='targeted proof check',
      event_id='S6_SERIES_PUBLISH_II_A_recovery_group09_02WM_targeted_20261121',
      outcome='Independently derived the signed-minor exact sequence, e(T)=K_T^2−ell, all rational/elliptic-ruled/class-VII restrictions, the finite-etale-cover Hopf conclusion and the last-two-alternatives conductor and image maps before opening WM. Opened the exact Kodaira, Beauville, OVV v3, BBK v3 and Inoue primary inputs; froze at 22:08:57 UTC. The preproof records exhibit two actual counterexamples to broader original wording: smooth reductions of full fibres 3S1/4S2 and the rational cusp normalization dP6→W. Compared every printed proof item after release and settled both as explicit D25 scope repairs. A frozen summary sentence about the conductor normalization was corrected postrelease: its domain has Euler number 12 and its nodal hexagon target R has Euler number 6; the detailed preproof witness already used e(R)=6. Frozen bytes remain unchanged, with no extra independent credit.'),
 dict(common, type='used and rechecked in this run',
      event_id='S6_SERIES_PUBLISH_II_A_recovery_group09_02WM_wording_20261121',
      outcome='Read the full original and final proposed five-item proof and all ten target guards, plus three complete bibliography pairs. The source now specifies singular reduced S, j=iota composed with nu, the actual minor scheme, identity-resolution conductor and torsion line, the embedding and elliptic tangent-quotient classification maps, the finite Hopf cover, the coefficient-one bisection and coefficient-two section, and nu restricted from R to C. The conductor conclusion is explicitly confined to the last two alternatives. Audited the P4.18 minor ideal (u), both P4.22 applications, front index and aliases through the exact root receiving record. Preserved the numerical identity, all bounds and the proved conclusions; preserved both refuted original scopes and the postrelease 12-versus-6 precision correction in immutable evidence. OVV2020 and BBK2019 keys retain their identities with exact v3 data, and Kodaira1954 identifies the opened PNAS theorem.'),
 dict(common, type='computation or formal certificate',
      event_id='S6_SERIES_PUBLISH_II_A_recovery_group09_02WM_computation_20261121',
      outcome='The prerelease program uses additive Chern characters, exact degree-one elimination, coordinate-plane minors, the six-curve hexagon incidence, the dP6 intersection basis and exact quadratic-ring rotation/character maps for the degree-nine and degree-eight elliptic-product covers. Its full output was read before freeze. A postrelease supplement computes the ruled Euler counts from base-cell filtrations and the canonical self-pairing in the primary basis, with all 36 rows, four conductor rows and final Euler row read. The geometric derivation proves the universal formulas; samples supplement it. The three exact-owner historical rows, complete printed WM proof and ten Programs rows name no WM routine; no adjacent-program ownership, old-WM rerun or broader absence claim is asserted. All input/output hashes and actual run times are bound. The postrelease supplement and frozen-summary precision correction add no independent-check credit.')
]
event_path = G/'S6_SERIES_PUBLISH_II_A_WM_event_proposals.json'
save(event_path, {'created_utc':now,'canonical_events_added':0,'root_review_required':True,'events':events})

files = [manifest_path,comparison_path,reread_path,validation_path,event_path,precision_path,
         derivation_path,freeze_path,release_path,old_path,new_path,
         R/'S6_SERIES_PUBLISH_II_A_02WM_scope_counterexample_preproof.md',
         R/'S6_SERIES_PUBLISH_II_A_02WM_multiple_smooth_fibre_preproof.md',
         R/'S6_SERIES_PUBLISH_II_A_02WM_primary_scope.json',
         R/'S6_SERIES_PUBLISH_II_A_02WM_chern_character_cells_run.json',
         R/'S6_SERIES_PUBLISH_II_A_02WM_ruled_cells_postrelease_run.json',
         R/'S6_SERIES_PUBLISH_II_A_02WM_incoming_uses.json',
         Path('records/S6_SERIES_PUBLISH_II_WM_root_receiving_scope.json'),
         Path('records/S6_SERIES_PUBLISH_II_WM_root_program_association_scope.json'),
         Path('code/S6_SERIES_PUBLISH_II_A_02WM_chern_character_cells.py'),
         Path('code/S6_SERIES_PUBLISH_II_A_02WM_chern_character_cells.out'),
         Path('code/S6_SERIES_PUBLISH_II_A_02WM_ruled_cells_postrelease.py'),
         Path('code/S6_SERIES_PUBLISH_II_A_02WM_ruled_cells_postrelease.out'),
         Path('code/S6_SERIES_PUBLISH_II_A_WM_prepare.py'),
         Path('code/S6_SERIES_PUBLISH_II_A_WM_finalize.py')]
for g in m['bibliography_guards']:
    files += [Path(g['full_original_path']),Path(g['full_proposed_path'])]
index_path = R/'S6_SERIES_PUBLISH_II_A_recovery_group09_WM_final_index.json'
save(index_path, {'created_utc':now,'owners':['02WM'],
 'target_guard_count':len(m['guards']),'bibliography_guard_count':len(m['bibliography_guards']),
 'event_proposal_count':3,'canonical_writes':False,'files':[bind(p) for p in files]})
print(json.dumps({'final_index':str(index_path),'sha256':sha(index_path),
                  'guards':len(m['guards'])+len(m['bibliography_guards']),
                  'events':3,'proposed_sha256':sha(new_path),'time':now}))
