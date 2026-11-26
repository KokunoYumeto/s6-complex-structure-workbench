from pathlib import Path
import datetime as dt, hashlib, json

R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
def bind(p):
    q=R/p;b=q.read_bytes();return dict(path=p,bytes=len(b),sha256=sha(b))
ai='agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_Y6_global_counterexample_v1_index.json'
ci='agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_R13_compact_construction_final_v1/S6_SERIES_PUBLISH_II_C2_R13_construction_index_final_v1.json'
si='agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_R13_scope_final_v1/S6_SERIES_PUBLISH_II_C2_R13_scope_index_final_v1.json'
rel='agents/ii_infra/released_proofs/02Y6/e2c1bb7f36a82389/S6_SERIES_PUBLISH_release_receipt.json'
assert bind(ai)['sha256']=='d6cd44f562210839139cfd43bb1b18d65508d78593db5438d990451384e9ccf6'
assert bind(ci)['sha256']=='80399cef4900c2f5d116e907b5b0f20b85afdce60929140c1ac51aea1cd6ad5f'
assert bind(si)['sha256']=='4d611657341686c0485e8757fd7a4a74673072a6e532b2d00655eaca10e7cb24'
evidence={}
def walk(x):
    if isinstance(x,dict):
        if 'path' in x and 'sha256' in x:
            b=bind(x['path'])
            if x['path']=='S6_SERIES_PUBLISH_II.tex' and b['sha256']!=x['sha256']:
                historical=(R/x['path']).read_text()
                title_guards=json.loads((R/'records/S6_SERIES_PUBLISH_II_titles_02/guards.json').read_text())
                for guard in reversed(title_guards):
                    assert historical.count(guard['new'])==1
                    historical=historical.replace(guard['new'],guard['old'],1)
                assert sha(historical.encode())==x['sha256']
                b=dict(path=x['path'],bytes=len(historical.encode()),sha256=x['sha256'],
                    historical_source_verified_by_exact_inverse='records/S6_SERIES_PUBLISH_II_titles_02/manifest.json')
            else:
                assert b['sha256']==x['sha256'],x['path']
            if 'bytes' in x:assert b['bytes']==x['bytes']
            evidence[b['path']]=b
        for v in x.values():walk(v)
    elif isinstance(x,list):
        for v in x:walk(v)
for p in [ai,ci,si]:walk(json.loads((R/p).read_text()))
release=json.loads((R/rel).read_text())
freeze=json.loads((R/release['freeze_receipt']).read_text())
assert freeze['created_utc']<release['created_utc']
original=bind(release['full_owning_block_path'])
assert original['sha256']==release['full_owning_block_sha256']
s=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
old=(R/original['path']).read_text();assert s.count(old)==1
at=s.index(r'\hypertarget{tag-02XE}')
a=s.rfind(r'\begin{proposition}',0,at);b=s.index(r'\end{proof}',at)+len(r'\end{proof}')
xe=s[a:b]
now=dt.datetime.now(dt.timezone.utc).isoformat()
record='records/S6_SERIES_PUBLISH_II_R13_root_research_08.json'
assert not (R/record).exists()
out=dict(created_utc=now,A_index=bind(ai),C_construction_index=bind(ci),C_scope_index=bind(si),release=bind(rel),
    evidence=list(evidence.values()),original_R13=original,current_02XE_block=dict(bytes=len(xe.encode()),sha256=sha(xe.encode())),
    reading_scope=[
      'Root read every byte of A’s39959-byte frozen whole compact derivation in two bounded untruncated returns, then the full11639-byte index,4837-byte program and4041-byte output.',
      'Root read the full C final overview3643, period10905, local14912 and global6416 bytes, the final index, and the1886-byte root-chart program with its533-byte output. All four complete mathematical construction derivations and the expanded local specialization maps have actually been read.',
      'After A freeze at11:07:21.034256UTC and release at11:07:58.769404UTC, root read the complete12272-byte original R13 owning block and the complete4235-byte current02XE owning block. R13 occurs byte-for-byte once in the current source. Root also fully read C’s10512-byte scope report and its index. The separate scope JSON/extract and consumer proofs are hash-bound here but this record does not claim root read them in full.',
      'Earlier root research06 covers all A rational, doubled-horizontal and reduced-horizontal partial derivations. Root research07 covers the original fixed C extracts, corrections, orientation program and actual primary Grauert printed62–64 reading. Those prior reading scopes are retained, not newly counted.'
    ],
    original_R13_item_comparison=[
      dict(item=1,result='Scope failure',comparison='R9 gives the reduced-horizontal geometry and Euler zero but does not give one image curve. The explicit compact construction realizes its two-section/two-image case. The whole phrase ruled resolution also includes genus zero; A’s separate rational-case exclusion supplies that omitted entry. The later connectedness and unique positive-genus component deductions apply to the double-horizontal section/tree configuration and remain there.'),
      dict(item=2,result='Retained on the double-horizontal domain',comparison='Coefficient2 on every sheet leaves A2, A3 or D4 and horizontal cover degrees1,2,3 by the exact branch conductor exponent and intersection formula.'),
      dict(item=3,result='Retained',comparison='Noncontracted H gives rational normalization singularities. Canonical trace/projection formula identifies the same ideal and finite-conductor injection with the section maps used in the pre-target derivation.'),
      dict(item=4,result='Retained',comparison='The blowup maps O(E) and O have the stated direct images. The exact divisor sequence gives pushforward O_D and R1 vanishing. On the minimal ruled surface every thick vertical-fibre layer of O_V(-2H) is O_P1(-2), so its H0 vanishes. Purity of2H finishes generic restriction injectivity. This valid original route is preserved; the alternate vertical duality route stays in research records.'),
      dict(item=5,result='Retained',comparison='The primary quotient is coherent, its H0 kernel vanishes by the actual map to O_D and item4, and its H1 map is onto by dimension. The original Euler inequality is correct.'),
      dict(item=6,result='Retained',comparison='Purity makes the A2 primary conductor reduced; the D4 branch-value calculation gives the symbolic square. The existing elliptic normalization and symbolic-square inequalities give nonpositive Euler characteristic and the equality smoothness condition.'),
      dict(item=7,result='Retained',comparison='The A3 primary ideal, saturated Hessian line and quotient conormal map agree with the pre-target primary construction. The displayed delta, ramification, Hessian, lattice and descent formula has the same signs and equality condition.'),
      dict(item=8,result='Retained',comparison='The original chain0<=g-1<=chi_primary<=0 gives genus1, a smooth elliptic image, an unramified H-cover and the nowhere-zero A3 Hessian.'),
      dict(item=9,result='Retained',comparison='The conormal degree is zero by the actual smooth elliptic inclusion and c1(TY) pairing; the normal line degree is zero because a positive multiple of the support is principal locally over the base.'),
      dict(item=10,result='Retained',comparison='The saturated quadratic and null-cubic lines have opposite degree inequalities forcing degree zero and nowhere-vanishing tensors. The stated coordinate/lift comparison makes the cubic intrinsic, and the Morse/cube-root coordinate map gives the product cusp.'),
      dict(item=11,result='Retained',comparison='The residual fourth coefficient is c-b²/(4a), invariant under x↦x+vy² and transforming in Q4 tensor N. Degree zero and generic A3 make it a unit; the original completion-of-square/product-tacnode proof remains, instead of replacing it by the shorter R15 route.'),
      dict(item=12,result='Retained',comparison='Primary I_E³ membership and the discriminant line(detK)^6 tensor N4 give three everywhere-distinct tangent directions. The exact unit coordinate changes produce XY(X-Y).'),
      dict(item=13,result='Retained on the connected double-horizontal domain',comparison='The entire local singular locus is the smooth elliptic image. Connectedness removes all attached components. Product normalizations and R6 make N smooth; finite normalization removes vertical rational curves. A first blowup of2H0 would leave a positive vertical strict transform, so the normalization is minimal. The Euler pushout yields0. The final program bookkeeping is editorial material for the program table/records.')
    ],
    local_cohomology_review='The nearby I2 fundamental class maps to[P]+[Q]; eta=(etaP+etaQ)/2 restricts to primitive area. The graph class changes sign and component classes interchange. Transfer through the free degree4 tube cover and degree2 generic translation cover identifies all restriction maps with monodromy invariants. The parameter-preserving tube/fibre/boundary flow carries the actual maps. The conductor pushout gives H1 free generators t,b with a↦2t; the zero-section inverse-translation loop has class t. Thus local values are u/2 and global values(-1/2,-1/2,1/2), with sum-1/2. The exact rank9 matching matrix, integral image2Zalpha, primitive transgression and exterior kernels prove b1=b2=0 in the complete compact construction.',
    confirmed_errors=[
      dict(id='II-R13-ELLIPTIC-CONDUCTOR-COUNT',owner='night:P4R.13',tag='02Y6',error='The universal one-image-curve conclusion is false on the stated full domain.',witness='The completed compact construction has three full fibres2S, each with two disjoint smooth elliptic conductor images, smooth minimal elliptic ruled normalization and e(S)=0.',correction_gate='Preserve the valid double-horizontal proof; add the rational exclusion and complete reduced-horizontal cases; state one or two elliptic image components and the product germs. Canonical proposal/comparison remains pending.'),
      dict(id='II-P440-REDUCED-HORIZONTAL-OMISSION',owner='night:P4.40',tag='02XE',error='The blanket exclusion of uniform-A1 positive-genus ruled supports is false. Item3 presumes a coefficient-two horizontal section and omits the reduced-horizontal case.',witness='The same compact construction meets the extra global irreducible-or-normal-crossing hypothesis and has two coefficient-one conductor sections with uniform product-node germs.',correction_gate='Correct the Euler scope before entering the doubled-section argument. Preserve local excess-one ring items1–2 and their four consumers, with explicit receiving maps. A’s correction and C’s complete example are in preparation.')
    ],
    source=bind('S6_SERIES_PUBLISH_II.tex'),ledger=bind('CHECK_EVENTS.tsv'),
    execution_history='The first replay stopped before writing any record because A’s source-at-reading binding predates title pass02. The retry verifies that historical source by the exact inverse of every title guard; immutable evidence is still checked against its current bytes. No source, event or row was modified by the failed attempt.',
    original_proof_comparison_completed_by_root=True,
    events_added=0,canonical_source_changes=0,required_rows_completed=0,global_defect_classes_closed=0,final_candidate_pdf_pages_credited=0,
    event_boundary='C’s construction is post-target research; A’s new full derivation and verification is frozen before its original target reading, with collaborative construction exposure explicitly disclosed. This record creates no independent rediscovery or whole-target proof event. Corrected-source admission and exact event categories remain separate.')
(R/record).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
additional='records/S6_SERIES_PUBLISH_additional_required_checks_II.json'
assert not (R/additional).exists()
(R/additional).write_text(json.dumps(dict(schema='additional-required-checks-after-discovered-error',created_utc=now,historical_II_required_count=197,
    rows=[dict(id='check:night:P4.40',kind='required_check',paper='II',status='open',title='Correct the uniform-nodal ruled-support scope and compare every affected use',detail='A new compact counterexample refutes the current02XE statement; this owner was outside the inherited197 required rows. Add this correction/comparison gate without altering or deleting any historical event.',evidence=bind(record))]),ensure_ascii=False,indent=2)+'\n')
note=f'\n\n## Two established conductor-scope errors under correction — {now}\n\nThe full compact construction and local/global maps have been read and checked. Its three doubled irreducible supports each have two disjoint elliptic conductor images and smooth minimal elliptic ruled normalization, while the compact threefold has b1=b2=0. It refutes the one-image assertion in02Y6 and the unqualified uniform-node exclusion in02XE. All13 original R13 proof items have now been compared after the recorded pre-target freeze and proof release; the doubled-horizontal argument remains valid. The02XE proof omits the reduced-horizontal branch when it presumes a coefficient-two section. The exact four local-classification consumers and six R13 consumers are recorded by C.\n\nThe inherited required tally is196/197. A separate open correction/comparison row for02XE, which was outside those197, is now registered in `records/S6_SERIES_PUBLISH_additional_required_checks_II.json`; the scheduled row review will incorporate it without counting row creation as movement. The two canonical statements still await the full correction proposals and admission. No new check event or completion credit is assigned here. Record: `{record}`.\n'
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    with (R/name).open('a') as f:f.write(note)
print(json.dumps(dict(record=bind(record),additional=bind(additional),unique_bindings=len(evidence),events_added=0)))
