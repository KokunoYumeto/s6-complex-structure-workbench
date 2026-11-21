from pathlib import Path
import csv, datetime, hashlib, json

ROOT=Path('/workspace/scratch/653608133b22')
OUT=ROOT/'work/agents/i_analytic'
archive_path=OUT/'S6_SERIES_PUBLISH_I_final_residual_archive.json'
guard_path=OUT/'S6_SERIES_PUBLISH_I_final_residual_guards.json'
archive=json.loads(archive_path.read_text())
guards=json.loads(guard_path.read_text())
sha=lambda b:hashlib.sha256(b).hexdigest()
scopes={
'ari:C.8.3': 'Complete Rouché coverage proof and lattice-homothety transport compared. The two zero counts, radius 1/500, section-zero identification and norm invariance remain unchanged; only the final coverage sentence is stated directly.',
'ari:C.8.4': 'Complete division ladder proof compared. The displayed first three polynomials, all-k recurrence, 1/28 domain and norm identity remain unchanged; the redundant first-three-steps contrast is removed.',
'ari:C.3.2': 'Complete elliptic-point expansion and stabilizer proof compared. The explicit gamma/tau and mu transformation, Gaussian cancellation, cubic/radial terms and non-extremum argument remain unchanged.',
'ari:C.6.5': 'Complete CM norm/height enclosure proof compared. Integer singular-modulus identification, theta/Fourier tails, branch brackets, working bounds and resulting enclosures remain unchanged; only numerical-closeness and completeness epithets are removed.',
'fam:src:B.1.4': 'Complete theta line-bundle morphism and linearization proof compared. The map W*s_(P-O)/F_theta, frame limit at O, pointed cubic/sign transport, finite units and cusp divisor computation remain unchanged; specified replaces actual for the period identifications.',
'inv:A1.1': 'Complete ordinary/logarithmic cotangent and evaluation-divisor proof compared. The cyclic quotient map, m_j ds/s, full scheme fibre and local evaluation exponents remain unchanged; only the quotient epithet changes.',
'inv:A1.2': 'Complete direct-image and duality proof compared. The vertical twist, full scheme fibres, duality/trace, bundle tables, connecting maps and extension groups remain unchanged. The opening contrast and concluding workbench-method comparison are removed.',
'inv:A1.3': 'Complete residue/torsion cancellation proof compared. The actual residue maps with multipliers 1,3,4, character layers, connecting maps and absolute direct-image table remain unchanged; the defensive torsion and Euler-characteristic comments are removed.',
'inv:A2.4': 'Complete cup-product rank proof compared. The variable invariant frame v(s), v(0)=1, Reynolds construction, coefficient -mu_s/4 and nonzero C_4 remain unchanged. The mathematical warning that v=1 need not be invariant away from zero is retained.',
'inv:A3.2': 'Complete eta-extension and Leray lift proof compared. The pullback isomorphism, extension maps and Dolbeault representative remain unchanged; only actual before pullback is removed.',
'inv:C3.2': 'Complete integral degree-one/factor-twelve proof compared. The finite cyclic divisibility, cusp specialization, collar sum, full root-character data and exact power identity remain unchanged.',
'inv:C3.8': 'Complete fourteen-part coefficient-atlas proof compared. All chart/inverse maps, line multipliers, finite phases, cusp units and connections, averaging, locally finite weights, global forms and products remain. The additive-cocycle conclusion is written as f_ab+f_bc=f_ac on each overlap component. A vague backward reference becomes the existing exact fibre-form label.',
'wb:rem:bcpr-global-gauge-boundary': 'Complete current numbered remark compared with the original unnumbered paragraph. Both changes of weights and holomorphic cocycles retain their exact global Dolbeault coboundaries, factors 1/12 and signs; only actual is removed.',
'inv:D4.1': 'Complete twisted direct-image proof compared. The root-line pullback, projection formula, coherent torsion module, finite exponent ranges and invariant lengths remain unchanged.',
'inv:D4.3': 'Complete resonance existence and nonintegrality proof compared. The receiving Weierstrass identification, q*tau+4*mu=p, r=4 twist equation, nonintegrality and tangent-rank conclusion remain unchanged; the twist is explicitly named M_z.',
'inv:D4.4': 'Complete nine-part invariant Dolbeault-complex/stalk proof compared. The tangent cocycle, raw/exponential frame chain maps F_V^j=(2pi i)^(-j), F_L^j=(2pi i)^(-j-1), inverses, contractions, finite characters and all nilpotent layers remain unchanged. Taking finite invariants is described as computing the coarse stalks.',
'inv:D4.5': 'Complete cohomology/jump-locus/index proof compared. Every resonance congruence, multiplicity, finite support assertion, upper-semicontinuity argument and c_3/2 index remains unchanged; only three epithets are removed.',
'inv:B3.3': 'Complete rational topology/attachment proof compared. The transfer-normalized Mayer–Vietoris matrices, meridians, attachment-cycle matrix and differential-topological conclusion remain unchanged; actual is removed twice.',
'fam:src:A.2.1': 'Complete merged parameter/lattice proof compared with both original fam:A.2.1 and the complete wb:pshift:lem:centralizer proof. The exact identity on C^2, source-to-target lattice map S_-n, simultaneous centralizer, finite translation equations and parity obstruction remain unchanged; one epithet and one article are corrected.',
'fam:src:A.4.2': 'Complete merged deformation proof compared with original fam:A.4.2 and the complete wb:thm:retained-period-deformation statement/proof. Uniform filling/properness, real period map, plus-graph coefficient, KS=-[dot nu] conversion, infinitesimal pencil and critical-scheme argument remain unchanged; only actual and For completeness are removed.',
'ari:C.6.R2': 'Complete analytic-rank/enclosure proof compared. Fourier/Cauchy tail bounds, exact cutoffs, period conventions and rank implications remain unchanged. Statement C.5 is replaced by ari:C.5.1, the smooth CM non-torsion result used for these eleven fibres.',
'ari:C.6.R5': 'Complete twisting/genus-trace/height proof compared. The factor-four height normalization, explicit differential transports, integral genus trace, denominator lattice, all exact integer cutoffs and outward tail bounds remain unchanged. The trace is explicitly stated to be a sum in E_0(Qbar); repeated cutoff prose and the remainder contrast are removed. Root’s separate new primary-source verification is not attributed to this reread.',
'ari:C.7.1': 'Complete current sigma/compact-logarithm proof compared with the original, including the previously repaired lift-transport clause. This pass only states that the period signs use the displayed exponential convention. The earlier eta-power slip/exposure and refuted all-logarithm clause remain disclosed in their original records; no pristine or independent normalization credit is claimed here.',
'ari:C.7.9': 'Complete endomorphism/period-slope proof compared. The polarization/dual map, doubling transport P to Q, algebraic Lie coordinates, AST period argument and exact compact point remain unchanged. The stale C.4 reference becomes ari:C.4.2; the concluding narrative becomes the proved transcendental-slope assertion. R_N is still specified as a complex point, with its algebraicity equivalent to the open norm question.',
'ari:C.7.10': 'Complete ten-part enlarged CM action proof compared. Extension-class pushout/pullback, matrix dB, Gaussian projector, spectral gap, explicit kernel polynomials and r_2 evaluation remain unchanged. The existing scope separating the algebraic second lift from the norm-dependent first lift is retained.',
'ari:C.7.11': 'Complete ten-part complexification proof compared. Periodicity, fixed number field, exact first/second derivatives, transcendence of k, rank inequality and planar packing bound remain unchanged; only the geometry comparison is stated directly.',
'ari:C.7.12': 'Complete division-hull, height, translated-function, joint-degree and tangent proof compared. Every scalar change, exact norm ratio, finite-isogeny map, degree upper bound, coefficient estimate and open algebraicity qualification remains unchanged. Actual values are explicitly identified with the already proved lambda=N_0 specialization; no lower bound on the sampling-field degrees is asserted.',
'ari:C.5.1': 'Complete current operative proof compared with the original cited statement and the complete expanded proof at app:rederive:ari-C.5.1. The exact field Q(t)=Q(j), receiving equation/section, finite order enumeration, integrality exclusion and smooth boundary scaling maps remain unchanged; only actual is removed.'
}
keys=[x['statement_id'] for x in archive['comparisons']]
assert set(keys)==set(scopes)
group='eg:publish-ianalytic-final-residual-'+sha(archive_path.read_bytes())[:16]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
md_path=OUT/'S6_SERIES_PUBLISH_I_final_residual_comparison.md'
json_path=OUT/'S6_SERIES_PUBLISH_I_final_residual_comparison.json'
ledger_path=OUT/'S6_SERIES_PUBLISH_I_final_residual_CHECK_EVENTS.tsv'

exposure=(
 'All targets in this pass were already exposed through earlier checking/editorial work. '
 'The complete current statement and proof/argument was read for every affected container. '
 'The complete original/current differences were read; identical spans were read once. '
 'For merged A.2.1/A.4.2 the original supplementary centralizer/deformation proofs were also read in full. '
 'For C.5.1 the original cited statement and the expanded compendium proof were both read. '
 'The complete proposed affected proofs were compared using their unchanged full text and every exact new guard. '
 'This is exposed used-and-rechecked evidence only, not derivation before target-proof access. '
 'No numerical algorithm or mathematical certificate was rerun in this editorial pass.'
)
dispositions=[
 {'item':'fam:src:C.1.1 and push:src:E.3.1','outcome':'Fully read and compared during preparation; root then applied its own exact wording and owns the corresponding four exposed rows. Those deltas were read. This file adds no duplicate guards or events for them.'},
 {'item':'wb:pshift:eq:actual-overlap-difference','outcome':'The candidate actual occurs inside a permanent equation label. The exact overlap identity is retained and the label is unchanged. No new event for this no-edit disposition.'},
 {'item':'corrected divisor class / corrected Table 2','outcome':'These specify mathematical correction terms or the identified edition of a cited table. They are not removed by the process-word cleanup.'},
 {'item':'mathematical contrast clauses','outcome':'Full scheme fibres, the variable invariant frame, algebraic/exponential period signs, finite invariants, integral points, and the distinction between upper degree envelopes and unproved lower bounds were reviewed contextually. Their exact maps and substantive qualifications remain.'},
 {'item':'accidental adjacent exposure','outcome':'An overlong original E.3.1 extraction also displayed the original inv:B1.0 proof. No independence or event credit is claimed for inv:B1.0 in this pass; root’s fresh-context check is separate. A C.5.1 compendium extraction also displayed the preceding modular-unit/local-height proof; no new credit is assigned to it.'},
 {'item':'research/program scope','outcome':'No additional literature search, external source opening, mathematical computation or historical-program execution was performed. Guard replay and label/tag checks are editorial validations only.'},
]
rows=[]
for key in keys:
    outcome='PASS: EXPOSED-PROOF REREAD ONLY. '+scopes[key]+' No new independent or computational credit.'
    rows.append({'statement_id':key,'date':'2026-11-21',
      'who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, S6_SERIES_PUBLISH/v_analytic_check',
      'type':'used and rechecked in this run','outcome':outcome,
      'event_id':'ce:publish-ianalytic-fres-'+sha((key+'\n'+group).encode())[:16],
      'phase':'S6_SERIES_PUBLISH','source_file':str(md_path),'source_row':'',
      'source_event_type':'used and rechecked in this run','evidence_group':group})
with ledger_path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)

record={'created_utc':now,'source_before_sha256':guards['base_sha256'],
 'original_source_sha256':sha((ROOT/'source/S6_SERIES_GRIND_I.tex').read_bytes()),
 'original_compendium_sha256':sha((ROOT/'source/S6_GRIND_4_s6_09_compendium/S6_09_PAPERS_I.tex').read_bytes()),
 'guard_file':str(guard_path),'guard_sha256':sha(guard_path.read_bytes()),
 'archive_file':str(archive_path),'archive_sha256':sha(archive_path.read_bytes()),
 'evidence_group':group,'event_count':len(rows),'event_types':{'used and rechecked in this run':len(rows)},
 'independent_event_count':0,'computational_event_count':0,'exposure':exposure,
 'validation':guards['validation'],'scopes':[{'statement_id':k,'scope':scopes[k]} for k in keys],
 'dispositions':dispositions,'applied_source_binding':'Pending root application; same-group receipt will be added without new event rows.',
 'ledger_file':str(ledger_path),'ledger_sha256':sha(ledger_path.read_bytes())}
json_path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
lines=['# Paper I: final analytic residual comparison','',
 f'Prepared: {now}',f'Before-source SHA256: `{guards["base_sha256"]}`',
 f'Evidence group: `{group}`','',
 '## Outcome','',
 f'The batch contains {len(guards["guards"])} exact guards in {len(rows)} statement/proof or remark containers. All guards replay uniquely against the frozen source. Every existing label and tag remains in its original order; proof-environment counts are unchanged. Root alone applies the source edits.','',
 '## Exposure and comparison method','',exposure,'',
 'The source archive retains each complete current-before and proposed-after block, its original source blocks, and the exact local changes. Original-source chronology and prior mathematical correction records are not replaced by this editorial receipt.','',
 '## Scoped comparisons','',
 '| Statement | Complete comparison and exact changed scope |','|---|---|']
for k in keys:lines.append('| `'+k+'` | '+scopes[k]+' |')
lines+=['','## Dispositions and limits','']
for x in dispositions:lines.append('- **'+x['item']+':** '+x['outcome'])
lines+=['','## Record files','',
 '- `S6_SERIES_PUBLISH_I_final_residual_guards.json`: exact old/new guards.',
 '- `S6_SERIES_PUBLISH_I_final_residual_archive.json`: complete old/current/proposed proof blocks.',
 '- `S6_SERIES_PUBLISH_I_final_residual_CHECK_EVENTS.tsv`: 28 exposed used-and-rechecked rows in one evidence group.',
 '- `S6_SERIES_PUBLISH_I_final_residual_comparison.json`: hashes, scopes, dispositions and validation.',
 '- `S6_SERIES_PUBLISH_I_final_residual_preview.tex`: replay preview, not the root source.',
 '',f'Ledger SHA256: `{record["ledger_sha256"]}`','',
 'Root application is not yet claimed. A same-group source-binding receipt will compare the applied blocks without adding rows.','']
md_path.write_text('\n'.join(lines))
print(json.dumps({'event_count':len(rows),'evidence_group':group,'ledger_sha256':record['ledger_sha256'],
                  'guard_sha256':record['guard_sha256'],'scopes':keys},indent=2))
