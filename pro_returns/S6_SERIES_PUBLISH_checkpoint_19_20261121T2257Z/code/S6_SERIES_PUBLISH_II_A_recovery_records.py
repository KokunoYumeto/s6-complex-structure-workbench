"""Bind the actual completed recovery rereadings and propose, never append, events."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'agents/ii_checks_A/recovery_20261121T195642Z'
NOW = datetime.now(timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

# These are individual records of the full block readings actually performed.
notes = {
 '01FY': 'Read all six original proof items and the complete proposed block, then reread the complete proposed block after clarifying the line-bundle projection to S. Checked canonical descent through both rank-one fillings, the rank-two toric charts and cubic infinity chart; the determinant weights and all forms are unchanged. Compared relative Serre duality with the frozen absolute-duality/Leray trace map. Verified the extension group, rank-one evaluation, explicit universal-coefficient maps and the H_2 comparison with maps:src:B.5.2. Reopened published CDP Corollary 5.2 p.688 and Proposition 5.5 pp.688–689. The 01FY postrelease exterior certificate settles the identified old determinant-method overlap through z=log(w), w=exp(z).',
 '02WG': 'Read the complete original and proposed statement and all four proof items. Checked the blowup-coordinate overlap, line-frame coefficient map lambda_B=v lambda_A and product trivialization lambda_A/u=lambda_B/s. The added primitive Euler-class presentation gives H_1 of the circle bundle Z^2, and the norm circle adds the third generator. The same trivial-canonical surface is identified using the opened BHPV locator. The tautological evaluation map and uv=t intersection prove the identical Hopf component, multiplicity and transversality conclusions.',
 '02WR': 'Read both complete blocks and all three proof items. Matched the expanded statement to the isolated construction data and the preceding E,A,q,Lambda setup. Composed all three printed maps with the new explicit inverses and checked their real-lattice determinant one. The ell logarithm ambiguity remains a lattice period, and its translation inverse is subtraction. Rechecked Hausdorff gluing, local properness, compactness, connected fibres, the three singular values, and identity monodromy via translation isotopy. All original labels and gluing data remain.',
 '02X2': 'Read both complete blocks and all three proof items. Traced the same blowup homotopy model and Chern-class basis change to the local torus subcomplex. The proposed chain contraction sends a to r and a wedge c to rc; the fresh program proves dh+hd=id-ip on every cell and the two exact primitive inclusion kernels. The free ranks, torus inclusion maps and all meridian bounding chains agree with the frozen Serre derivation. The absent external differential display is replaced by this explicit integral map.',
 '02XO': 'Read both complete blocks and both proof items. The construction is now named by P4.2 and the integral input by P4.4. Rechecked Euler additivity on the regular and special strata, c_3 as the complex Euler class, Poincare/UCT torsion transport and b_3=2. The horizontal-divisor exclusion uses the restriction map and positive Kahler pairing on the same general torus. Multiplication by a base-coordinate power removes all vertical poles, and connected-fibre descent gives the identical field isomorphism C(Y)=f^*C(P1).',
 '02XY': 'Read both complete blocks and all three proof items. Checked the normal derivative map N_i=nu_i^*O_X(F)(-D_i), all Chern identities, the ordered-branch double cover and the triple-point nodal contributions. The sign line is the anti-invariant character of that exact double cover and has degree zero. The HRR and Cartier sequence give chi(O_F)=0, hence T=2a and e(F)=T. The final local count r-binomial(r,2)+binomial(r,3)=1 is evaluated on the same strata. The statement now identifies the reduction map from sum m_jF_j to sum F_j, preserving every multiplicity scope.',
 '02XZ': 'Read both complete blocks, including the single complete printed proof step. Checked connected-fibre constant direct image, the H^1 Leray injection, trivial normal line of a smooth fibre, vanishing c_2 restriction, finite critical values, Euler additivity and the alternating H^3 pairing. Their conjunction gives the same nonnegative even sum at most two. Removing the repeated negative scope sentence leaves the broad original hypotheses exactly intact, with no torus assumption. Only the duplicated manual heading and unresolved reference are otherwise changed.',
 '02Y0': 'Read all six original proof items and the complete proposed block; reread the complete revised block after the explicit finite-cover maps and again after the Catanese unnumbered-definition locator correction. Checked every rational/ruled/non-Kahler blowup formula, the conductor pullback under p, the composite Hopf universal covering, the torsion canonical argument, the reducible-component restriction divisor, elliptic conductor adjunction and the cyclic base-change charts. The Catanese family is precisely this proper submersion, matching its opened definition and theorem proof. The full Euler and normalization classification and arbitrary fibre multiplicities remain.',
 '02Y1': 'Read the complete original statement and its one-item proof, and the entire proposed remark. The durable derivation checks only P4.58 implies P4.9 under the identity on f,Y,B and each reduced support. Both explicit Euler values and the sign/equality classification reference remain. The duplicate proposition and proof outline become a numbered remark, retaining labels, tag and StatementRecord arguments. No check credit for the separate proof of P4.58 or its auxiliary targets is claimed.',
 '02WH': 'Read the complete original and proposed statements and all five proof items. Checked the exact w^4=-1/3 isomorphism from the independent Weierstrass model, its infinity chart, and its induced Rees-algebra isomorphism on diagonal blowups. Rechecked the printed nodal cubic, both resolution charts, overlap inverses, canonical line, rationality of S, stronger pi_1 proof, Euler replacement and nonzero ample class. The new degree-bounded interpolation and relative-cell programs settle the acknowledged overlap with the old gcd/substitution arithmetic. All geometric conclusions and the full pi_1 argument remain.',
}

target_outcomes = {
 '01FY': 'The durable prerelease derivation proves all local canonical-form extensions, the direct-image splitting, Leray dimensions, restriction rank and integral cohomology; all six printed steps and their exact trace/coordinate maps were fully compared. The recovered comparison and postrelease exterior-method addendum settle the identified computational overlap.',
 '02WG': 'The durable prerelease derivation constructs the line-bundle quotient and exact chart transitions, proves properness and the two central-component identifications, then matches all four printed steps. The local primitive Euler relation makes b_1=3 explicit in the proposed proof.',
 '02WR': 'The durable prerelease derivation verifies the three independently supplied marking definitions, their inverses, the logarithmic clutch, all gluing axioms and identity monodromy before release. All three target steps are fully compared with those identical data.',
 '02X2': 'The durable prerelease integral Serre derivation establishes the local groups and inclusion/meridian maps before release. The complete printed cellular proof is compared by the exact Chern-class basis map; the postrelease chain contraction verifies integral freeness and both primitive kernels without Smith or rank elimination.',
 '02XO': 'The durable prerelease derivation gives the Euler/duality/UCT calculation and the exact pullback isomorphism of meromorphic fields before release. Both complete printed proof items agree under the same construction and fibre maps.',
 '02XY': 'The durable prerelease normalization-immersion derivation proves the reduced normal-crossing Euler identity and parity, including self-intersections of global components. The complete printed HRR/sign-line proof is compared through the same branch cover and triple-point strata; both give T=2 sum chi and e(F)=T.',
 '02XZ': 'The durable prerelease derivation proves the genus-zero base, smooth-fibre Euler zero, triple-point sum and symplectic parity bound. The complete printed proof agrees for the full stated general-fibre scope.',
 '02Y0': 'The durable prerelease classification proof treats every smooth, singular irreducible and reducible normal-crossing support, with explicit conductor and cover maps. All six printed items are fully compared, including the Catanese deformation route on the same cyclic base-change family and the original torsion-canonical classification route.',
 '02Y1': 'Scoped logical consequence only: from the full input statement of P4.58, the identity on the fibration and reduced supports gives every P4.9 conclusion. The complete printed outline adds no hypothesis. No independent credit for P4.58 or its auxiliary proofs is inferred.',
 '02WH': 'The durable prerelease explicit elliptic self-product resolution proves all required properties. The exact w-scale map and induced Rees-algebra isomorphism identify it with the printed construction; all five proof items, including the stronger pi_1 argument, are compared. Postrelease interpolation/exterior/relative-cell certificates settle the old algorithm overlap.',
}

groups = {'group02': ['01FY','02WG','02WR','02X2','02XO','02XY'],
          'group03': ['02XZ','02Y0','02Y1','02WH']}
all_evidence = []
for group, tags in groups.items():
    manifest_path = OUT / group / f'S6_SERIES_PUBLISH_II_A_recovery_{group}_editorial_proposals.json'
    manifest = json.loads(manifest_path.read_text())
    records = []
    events = []
    for proposal in manifest['proposals']:
        tag = proposal['tag']
        release_path = ROOT / proposal['release_receipt']
        release = json.loads(release_path.read_text())
        freeze_candidates = list((ROOT / f'agents/ii_infra/derivation_freezes/{tag}').glob('*/S6_SERIES_PUBLISH_derivation_freeze_receipt.json'))
        assert len(freeze_candidates) == 1, (tag, freeze_candidates)
        freeze_path = freeze_candidates[0]
        freeze = json.loads(freeze_path.read_text())
        derivation_path = ROOT / freeze['frozen_derivation_path']
        assert sha(derivation_path) == freeze['derivation_sha256']
        original_path = ROOT / proposal['original_block_path']
        proposed_path = ROOT / proposal['proposed_block_path']
        assert sha(original_path) == proposal['original_block_sha256']
        assert sha(proposed_path) == proposal['proposed_block_sha256']
        record = {'tag': tag, 'statement_owner': proposal['statement_owner'], 'record_created_utc': NOW,
                  'read_timing': 'Actual complete recovery rereading after the original durable freeze/release and after reconstruction; not a new blind derivation.',
                  'original_full_block_path': proposal['original_block_path'], 'original_full_block_sha256': sha(original_path),
                  'proposed_full_block_path': proposal['proposed_block_path'], 'proposed_full_block_sha256': sha(proposed_path),
                  'full_original_owning_block_read': True, 'full_proposed_owning_block_read': True,
                  'comparative_rereading_notes': notes[tag],
                  'freeze_receipt_path': str(freeze_path.relative_to(ROOT)), 'freeze_receipt_sha256': sha(freeze_path),
                  'original_freeze_utc': freeze['created_utc'], 'frozen_derivation_sha256': freeze['derivation_sha256'],
                  'release_receipt_path': proposal['release_receipt'], 'release_receipt_sha256': sha(release_path),
                  'all_25_register_types_considered_in_complete_block': True,
                  'canonical_source_changed': False, 'canonical_events_added': 0}
        records.append(record)
        comp = ('agents/ii_checks_A/comparisons/S6_SERIES_PUBLISH_II_A_group02_comparisons.md' if group == 'group02'
                else str((OUT/'S6_SERIES_PUBLISH_II_A_recovery_group03_comparisons.md').relative_to(ROOT)))
        base = {'statement_id': proposal['statement_owner'], 'date': '2026-11-21',
                'who': 'GPT-6 Astra Pro (OpenAI), inherited effort, S6_SERIES_PUBLISH checker ii_check_a',
                'phase': 'publish-II', 'source_file': proposal['proposed_block_path'],
                'evidence_group': f'II-A-{group}-{tag}', 'date_utc': NOW,
                'where': comp+'; '+str(freeze_path.relative_to(ROOT))+'; '+proposal['release_receipt']}
        events.append(dict(base, type='targeted proof check', outcome=target_outcomes[tag],
                           event_id=f'S6_SERIES_PUBLISH_II_A_{tag}_targeted_20261121'))
        events.append(dict(base, type='used and rechecked in this run', outcome=notes[tag],
                           event_id=f'S6_SERIES_PUBLISH_II_A_{tag}_wording_20261121'))
    record_path = OUT/group/f'S6_SERIES_PUBLISH_II_A_recovery_{group}_actual_rereading_records.json'
    record_path.write_text(json.dumps({'created_utc': NOW, 'records': records,
                                      'canonical_events_added': 0}, ensure_ascii=False, indent=2)+'\n')
    for proposal in manifest['proposals']:
        proposal['actual_comparative_rereading_record'] = {'path': str(record_path.relative_to(ROOT)),
                                                         'sha256': sha(record_path), 'tag': proposal['tag']}
    manifest['recovery_full_rereading_completed_utc'] = NOW
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    computation_tags = ['01FY','02WR'] if group == 'group02' else ['02WH']
    descriptions = {
        '01FY': 'Restored prerelease local canonical-form/Leray code rerun with bound bytes. Identified related old determinant routine and its exact logarithm-coordinate transport; postrelease bitmask Laurent exterior algebra, degree-bounded 228-point equation interpolation and Cech monomial enumeration give a different-method certificate. Every output is exact; no new prereading credit is claimed.',
        '02WR': 'Restored prerelease explicit inverse matrices and 24-term permutation determinant rerun for the exact three marking matrices. Compared with recovered pinned SymPy inverse/determinant routine; identical integer inputs and different inverse/determinant algorithms. Related 02X2 local cells are checked in the bound addendum by an explicit integral contraction, with no extra event.',
        '02WH': 'Restored prerelease construction code and its overlap with old gcd/substitution acknowledged. The recovered postrelease program proves both discriminant Bezout identities by bounded-degree interpolation, both exact resolution charts and overlap inverses by finite grids, the canonical transition by Laurent exterior multiplication, and Euler 24 by relative/tensor cell counts. No extra prereading credit is claimed.',
    }
    for tag in computation_tags:
        proposal = next(p for p in manifest['proposals'] if p['tag'] == tag)
        events.append({'statement_id': proposal['statement_owner'], 'date': '2026-11-21',
                       'who': 'GPT-6 Astra Pro (OpenAI), inherited effort, S6_SERIES_PUBLISH checker ii_check_a',
                       'phase': 'publish-II', 'source_file': proposal['proposed_block_path'],
                       'evidence_group': f'II-A-{group}-{tag}', 'date_utc': NOW,
                       'where': str((OUT/'S6_SERIES_PUBLISH_II_A_recovery_group02_03_method_addendum.md').relative_to(ROOT)),
                       'type': 'computation or formal certificate', 'outcome': descriptions[tag],
                       'event_id': f'S6_SERIES_PUBLISH_II_A_{tag}_computation_20261121'})
    event_path = OUT/group/f'S6_SERIES_PUBLISH_II_A_recovery_{group}_event_proposals.json'
    event_path.write_text(json.dumps({'created_utc': NOW, 'canonical_events_added': 0,
                                     'root_review_required': True, 'events': events}, ensure_ascii=False, indent=2)+'\n')
    row={'group': group, 'manifest': str(manifest_path.relative_to(ROOT)), 'manifest_sha256': sha(manifest_path),
         'reread_record': str(record_path.relative_to(ROOT)), 'reread_sha256': sha(record_path),
         'event_proposals': str(event_path.relative_to(ROOT)), 'events_sha256': sha(event_path),
         'event_count': len(events), 'literal_guard_count': sum(len(p['literal_edits']) for p in manifest['proposals'])}
    all_evidence.append(row)
    print(json.dumps(row))
index=OUT/'S6_SERIES_PUBLISH_II_A_recovery_group02_03_final_index.json'
index.write_text(json.dumps({'created_utc': NOW, 'groups': all_evidence, 'canonical_events_added': 0},indent=2)+'\n')
print('INDEX',str(index.relative_to(ROOT)),sha(index))
