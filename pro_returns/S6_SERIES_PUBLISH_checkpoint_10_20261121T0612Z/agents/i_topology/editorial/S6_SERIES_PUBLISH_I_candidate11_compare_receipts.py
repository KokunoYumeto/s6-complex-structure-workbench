from pathlib import Path
import json,csv,datetime,hashlib
R=Path('/workspace/scratch/653608133b22');D=R/'work/agents/i_topology';E=D/'editorial';now=datetime.datetime.now(datetime.timezone.utc).isoformat();who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH topology-check agent';sha=lambda t:hashlib.sha256(t.encode()).hexdigest()
notes=r'''# Candidate11 topology prose: bounded comparison

## Reading and exposure

Every candidate11 page171–255 was actually viewed and read. The per-page image/PDF hashes and specific findings are in the separate reading ledger. The complete current proofs of the affected B2/B3/B4 statements lie in those pages. A4.9's full proof, which begins before this page assignment, had already been read for boundary batch7; its changed Step4 was reopened in source here. The complete current proof readings and exact preserved maps in the preceding boundary batches are recorded in boundary_batch7_comparison.md and residual_batch8_comparison.md. Those earlier readings are reused; they are not counted again as independent checks.

In this pass, the complete attached-original and candidate11 B3.8, B4.24 and B4.26 statements/proofs were explicitly reopened and read. The exact B4.18 Step3 receiving map was also reopened. All61 new guard passages were reread after generation. The adjacent full_blocks.json archives original, candidate11 and proposed complete statements/proofs for all26 affected IDs; archival extraction alone is not claimed as a new complete reading of all26 attached-original proofs.

The edits preserve every existing label, tag, equation, base value, finite-cover degree, marked deck, chart transition and statement hypothesis. The61 guards were simulated sequentially against parent source8560db26953b2669948b65cfc38a00e8be338538523c398275e75683d85ae864 with one exact match each and unchanged label/tag multisets. No main source was edited by this agent.

## Exact proof comparison

B4.26 previously displayed h_q−h_r=dF followed by an unspecified subtraction-convention clause. B4.18 Step3 sends the cusp affine coordinate ζ to the rotating coordinate ζ−σ+F. The cusp group coordinate is z_r=ζ−σ, and the rotating group coordinate is consequently z_q=z_r+F. The degree-d sums therefore satisfy h_q−h_r=dF exactly, including multiplicities. The right-hand r-loop Y-class is still dγ≠0. The guard retains the original equation and ghost contradiction and replaces only the unspecified convention by this exact map. Complete original/current B4.24/B4.26 proofs were read; the norm, finite-cover, bounded-character, branch and fibre-dimension steps are unchanged. This receives one exposed used-and-rechecked row; there is no new independent derivation, execution or error/refutation event.

B3.8 still quantifies over every compact smooth analytic genus-one surface locally isomorphic to the stated Jacobian as a torsor over every base disc. Removing the algebraicity/finite-order disclaimers adds no restriction. The proof retains the sheaf isomorphism R¹π_*Q≅R¹p_*Q including the I12 specialization maps, b1=6, Buchdahl's compact analytic surface criterion, the positive curvature form θ+Aπ*ω on every projective bundle, and the class-C/ddbar conclusion for every smooth compact bimeromorphic model. The last statement now names precisely those bundles and models as excluded normalization components. Both full originals/current proofs were reread; no new mathematical event is assigned to deleting redundant wording.

## Preserved content of the remaining copyedits

| ID | Exact object and retained content |
|---|---|
| A4.9 | The same exceptional Gysin maps glue surviving integral classes with unit coefficients; no group or map is changed. |
| B2.2 | All stated plain-cusp hypotheses and the same fan/chart maps remain; only repeated scope prose is removed. |
| B3.2 | Title capitalization only. |
| B3.3 | The same q=s^d,u=r^n, fractional period translation, integral r-shift and d/gcd(d,a,b) multiplicity remain; proposal language is replaced by the exact quantified statement. |
| B3.4 | Tr_sigma Q=12kP and (t_Q sigma)^12=t_TrQ remain. The geometric application now prints this exact twelfth iterate; the preceding impossibility of t6P remains. |
| B4.7 | The full integral topology and meromorphic-graph fundamental-group argument remain; its introduction is direct. |
| B4.8 | All normal-line Chern vectors, monodromy and elliptic-core plumbing arguments remain; title and two defensive sentences alone change. |
| B4.9 | Title only; all cocycle, exponential-sequence and period formulas remain. |
| B4.10 | The bound K is arbitrary finite; for each K the displayed inequality chooses a sufficiently small R. The weighted divisor, proper horizontal part, degree n and symmetric-power map remain. |
| B4.11 | The exact restriction/Atiyah map, tau-Kodaira–Spencer cocycle including extra-automorphism curves, regular local-to-global germ map, and lift of the specified analytic disc remain. |
| B4.12 | The same original parameter disc, cone and blow-up maps, two normal lines and three-piece products remain. The unused comparison to another smoothing component is deleted. |
| B4.13 | The derivative of the axis-preserving automorphism still induces t_b* N≅N; the exact multiplication-by-degree and finite-cycle arguments remain. |
| B4.14 | The applicable compact-complex-manifold hypothesis is stated positively; all weights and Lefschetz formulas remain. |
| B4.15 | The torsor section remains on Delta_z×Delta_r*, and its cocharacter remains on the specified ordinary disc. No map is extended. Rotations+4,−3,0 and component labels remain. |
| B4.17 | The compact-base Cartier-cocycle construction is unchanged. |
| B4.19 | The period addition preserves the quotient map exactly; the scalar gauge remains on the punctured family. The twelfth closing still translates by6P, and the component-cover cocycle is unchanged. |
| B4.21 | All six point/72 curve blow-ups, normal-line factors, exact product charts and Kato closing formula remain. |
| B4.22 | The proved charts near F=0 remain local completion charts. The report that a separate global attachment has not been established is removed; no global attachment is asserted. |
| B4.23 | The same smooth fourfold, holomorphic(Q,r), reduced NC divisor, specified complementary Kato component and conductor-disjoint curve remain. All normal-bundle/deformation maps are unchanged. |
| B4.24 | The stated log-torus hypotheses and proper-model theorem remain; no polarization hypothesis is introduced. |
| B4.25 | The same two multipliers, all finite-base-change and singular/nonreduced-completion scope, and explicit bivector automorphy calculation remain. |
| B4.28 | The exact secondary-Hopf scope, annular monodromy calculation, nearby torus period contradiction and unramified branch-cover splitting remain. |
| B4.29 | All three pullback equations and both distinct-limit examples remain. The unproved suggestion about adding an affine connection is removed. |
| inv:B2.1 | Citation locator only, using provenance's actual Viaclovsky v1p1 andpp5–6 receipt. |

The two Theorem-to-Proposition corrections point to the existing Proposition B4.30 without changing any dependency. Long-title changes and the Künneth spelling create no mathematical event. Global Needspace protection is parent-owned, so this package contains no redundant local heading guard.
'''
(E/'S6_SERIES_PUBLISH_I_candidate11_prose_comparison.md').write_text(notes)
field=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group']
event=dict(statement_id='push:src:B.4.26',date='2026-11-21',who=who,type='used and rechecked in this run',outcome='Full attached-original and candidate11 B4.24/B4.26 statements and proofs read; B4.18 Step3 exact receiving map reopened. The cusp group coordinate z_r=zeta−sigma and rotating coordinate z_q=zeta−sigma+F give z_q=z_r+F, hence the existing trace h_q−h_r=dF including multiplicities and ghost class dgamma. The unspecified subtraction-convention prose is replaced by this exact map. All other steps and conclusions unchanged. No independent, targeted, computation or refutation credit. Applied binding pending.',event_id='ce:publish-I-B426-trace-map-exposed-20261121',phase='Paper I rendered-reading proof clarification',source_file=str(E/'S6_SERIES_PUBLISH_I_candidate11_prose_comparison.md'),source_row='complete original/current B4.24/B4.26 and exact B4.18Step3 comparison',source_event_type='used and rechecked in this run',evidence_group='eg:publish-I-B426-trace-map-exposed')
with (D/'S6_SERIES_PUBLISH_I_candidate11_prose_CHECK_EVENTS.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=field,delimiter='\t');w.writeheader();w.writerow(event)
# Bind cusp extraction to its allocated tag without creating an additional event.
cur=(R/'work/S6_SERIES_PUBLISH_I.tex').read_text();d=json.loads((E/'S6_SERIES_PUBLISH_I_candidate11_cusp_guards.json').read_text());expected=(E/'S6_SERIES_PUBLISH_I_candidate11_source_snapshot.tex').read_text()
for p in d['patches']:expected=expected.replace(p['old'],p['new'].replace('TOPOLOGY-CUSP-TAG','PI19'))
def block(t,lab):
 i=t.index('\\label{'+lab+'}');a=t.rfind('\\begin{',0,i);b=t.index('\\end{proof}',i)+len('\\end{proof}');return t[a:b]
bind=dict(created_utc=now,source_sha256=sha(cur),allocated_tag='PI19',scope='Exact applied-block comparison to the already fully read old/new proof archive. Same exposed event/group; zero additional events.',event_id='ce:publish-I-cusp-contraction-exposed-20261121',evidence_group='eg:publish-I-cusp-contraction-exposed',new_check_events=0,blocks=[])
for lab in ['I:lem:cusp-tube-contraction','inv:B3.1','inv:B3.3']:
 a=block(cur,lab);b=block(expected,lab);assert a==b,lab;bind['blocks'].append(dict(statement_id=lab,exact_expected_block=True,applied_block_sha256=sha(a),complete_applied_block=a))
(E/'S6_SERIES_PUBLISH_I_candidate11_cusp_applied_binding.json').write_text(json.dumps(bind,indent=2)+'\n')
# Update existing outcomes, preserving row/event/evidence identities.
for name,needle,repl in [('S6_SERIES_PUBLISH_I_P26_component_resolution_CHECK_EVENTS.tsv','applied binding pending.','Applied at sourceeb211f10; full applied proof reread and exact replacement checked in the adjacent applied-binding receipt.'),('S6_SERIES_PUBLISH_I_candidate11_cusp_CHECK_EVENTS.tsv','Applied binding pending.','Applied with allocated tagPI19 at source8560db26; exact complete blocks match the previously read proposed proof archive.')]:
 p=D/name;t=p.read_text();assert needle in t;(p).write_text(t.replace(needle,repl))
print(json.dumps({'prose_check_rows':1,'cusp_applied_exact_blocks':len(bind['blocks']),'current_source':sha(cur),'new_independent_checks':0}))
