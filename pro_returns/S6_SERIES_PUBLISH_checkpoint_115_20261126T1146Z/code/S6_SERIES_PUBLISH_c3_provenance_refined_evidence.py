#!/usr/bin/env python3
"""Record the exposed complete consumer comparison, without shared writes."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_provenance/refined_consumers'
status = json.loads((OUT / 'S6_SERIES_PUBLISH_refined_status.json').read_text())
assert status['complete_receiving_reading'] is True
now = datetime.now(timezone.utc).isoformat()


def tsv(name, rows):
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, list(rows[0]), delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


comparisons = {
'lem:II:horizontal-primary-conductor': (
    'The full restriction construction formerly in P4R.13 and repeated in P4R.18: arbitrary positive ruling genus, noncontracted doubled horizontal section, whole image conductor on the left, its component along the section on the right, canonical algebra injections, every blowup pushforward, H0 injectivity and H1 surjectivity. No elliptic image assumption is added.',
    'Read all old and receiving arguments. Apply the earlier ruled-boundary owner to the same minimal model, blowups and pole divisor; P4.33 then gives rational singularities and g. Greb Remark2.1 applies to the same normal Cohen–Macaulay surface and proper resolution. Residue and trace give sigma_*O(-D)=I_N as ideal subsheaves. The beta direct images identify functions on D with functions on 2H0+V0, whose vertical kernel has O_P1(-2) layers. Generic determination on the Cartier double section gives H0 injectivity; dimension-one support gives H1 surjectivity. At a multibranch point of the global image component, intersect IR_p∩R over every relevant minimal prime over I. This retains all rational self-identification branches in later applications. The three old equation labels move to this owner.'),
'night:P4R.13': (
    'The complete refined statement is byte-identical: standing torus fibration; irreducible reduced singular support with ruled normalization resolution and an elliptically normalized conductor component; smooth minimal elliptic ruled normalization, one or two smooth elliptic image curves, product germs, Euler zero, no attached rational component, and the full two-image-component double-cover clause.',
    'Read the complete original and receiving proofs. Preserve the rational-resolution exclusion, degree-two unramified elliptic covering, local hypersurface branch count, exact difference-of-restrictions conductor square and H1 contradiction. Use P252/R7 on the identical D,beta,T0 for the reduced-horizontal classification, retaining rank-drop zero and all three finite component maps. The double-horizontal case applies P313 with C_H=C_E and sigma=rho_N. Preserve the A2/A3/D4 primary Euler bounds, zero-Euler chain, null cubic and fourth-jet transition checks, cubic discriminant line, explicit local product coordinates, attachment exclusion and minimality argument. P282 supplies the exact branch conductor formula; the same exponent-two plane-branch ring calculation remains accessible through P4.32. No full-fibration global support hypothesis is imported into this refined theorem.'),
'lem:II:positive-ruled-conductor-graph': (
    'The already used positive-ruled reduction now has one owner: all reduced supports irreducible or normal crossing, e(S)>0, positive ruling genus, doubled pole section with rational trees, two rational normalized image components, one graph cycle, and the inclusion-induced fundamental-group isomorphism to Z.',
    'Transfer the complete last item of P4.51 and the same one-component exclusion used in P4.40/R18. P4.26 gives e(S)≤2 using the entire fibration. The same pole pair satisfies P252/R7. P294 applies to (T,S,A,C,rho); its inverse is identity on pi1(C) and (rho|A)_*j_*^{-1} on pi1(T). P245 gives the exact genus/graph alternatives. P4R.13 applies only when an elliptic normalized component occurs, with all its hypotheses checked. The b=0 alternative gives m=1 by R1 and positive det(I−A) by P4.13, hence e(S)≥3. Thus b=1. P4.35 applies to the same exceptional subtree contraction and excludes c=1, while c≤e(S)≤2 gives c=2. The proof imposes no local transverse-type assumption.'),
'night:P4.51': (
    'Its entire statement is byte-identical, including every reduced local equation, the b1(S)>0 scope and the ruled positive-Euler application under the full global support hypothesis.',
    'Read the whole old and receiving proof. Preserve the full tube and regular-fibre maps, cyclic cokernel, unit-removing flow with its gradient bound, orientation-preserving compact Milnor-fibre embedding, lift to R4/H and its wedge-square homology map, and equality of the local and ambient intersection pairings. The final application now uses P314 with precisely the stated full fibration, mS, e(S)>0 and positive ruling genus, obtaining b1(S)=1 before applying the same first four items.'),
'night:P4.40': (
    'Its complete refined statement is byte-identical, including the full irreducible-or-normal-crossings fibration hypothesis, e(S)>0, positive ruling genus and ordinary-double type on every critical-curve component.',
    'Read both full proofs. P314 supplies the same doubled section and two-rational-component one-cycle curve. Exponent two of a noncontracted section contradicts the exponent-one transverse-node formula, so P4.33 gives chi(C_sch)=−1 in its contracted-section clause. Its CM conductor and generic reduction kill the finite-support nilradical. Keep the exact delta sum3, branch-identification sum2, unique excess-one point and r≤3. Apply the same P206 analytic curve-germ classification and P4.38 local exclusions. No outward mathematical application of P4.40 occurs elsewhere in II: the additional hits are its dictionaries, further-result listing and program row.'),
'night:P4.43': (
    'The uniform A2 exclusion has its intended full global fibration class stated explicitly. The same positive Euler and positive ruling-genus scope is preserved.',
    'Read the full old and receiving proofs. Pairwise hypersurface intersections show that uniform cusps make finite normalization bijective, hence a homeomorphism. Apply P314 before using the doubled section. Keep the fibration base B distinct from the ruling base B0. The point-blowup and section maps identify pi1(T)=pi1(B0); contracting rational trees preserves it, while contracting the section kills it. The normalization homeomorphism would identify either resulting group with Z, contradicted by abelianization ranks0 or2g versus1. Every quotient and comparison uses the same T→N→S.'),
'night:P4.42': (
    'All original scope is preserved: no Euler-positivity assumption is added; the two two-branch points may be nonordinary, and additional unibranch singular points remain allowed.',
    'Read both complete proofs. P4.26 gives nonnegative Euler number. In the zero case the unchanged P4.32 statement makes the uniform-A3 image conductor smooth elliptic, with identity normalization and no identifications, so the asserted configuration has e(S)>0. P314 then supplies exactly the two rational components. Preserve every local symmetric-square estimate, the cusp-plus-line symbolic-square calculation, all 9/2,6,5,8 bounds and the equality analysis. The derivative kernels are K_i=ker(j_i^*OmegaY→OmegaP1(−R_i)); the relevant nilradical belongs to the full conductor scheme, and q_p remains its full descent defect. P4.41 supplies the nodal equality condition, and R14 the smooth-critical-curve alternatives. P4.41 remains an external deformation gate; this package does not close it.'),
'night:P4R.18': (
    'Full global support hypotheses are explicit; the noncontracted section maps with degree2 or3 to a rational normalized component of type D4, with every other-component transverse type and conductor-exponent pattern allowed.',
    'Read the entire old and receiving proof. P314 replaces the repeated global graph calculation. The same exponent-two branch formula gives A3 or D4. For the A3 exclusion, P313 applies to the identical nu,sigma,D,H,C_H, giving the whole-conductor-to-primary Euler inequality even at multibranch rational image points. The normalized derivative is j^*OmegaY→OmegaP1(−R), and the primary nilradical remains the primary one. Preserve all primary defect estimates and all graph distributions: two intersections; one self-identification plus an intersection; one three-branch point. Retain the exact quadric resolution chart (s,v)↦(−sv²,sv,s), its strict conductor coordinate s, and the at-most-three branch-value contradiction to degree-two Riemann–Hurwitz. R14/R15 applications retain their exact hypotheses; both now have separately admitted multiplicity repairs.'),
'night:P4.55': (
    'Smooth rational horizontal image, degree exactly2, unique rational third sheet of degree1, unrestricted transverse type on the other image component, and no separated self-identification on either component.',
    'Read the complete old and receiving proof. Name nu and sigma. P4.33 supplies q:N→E and s=sigma∘h with q∘s=id, giving the precise identification of H on T with its embedded image on N. The reduced conductor D⊂N and pole divisor D_T on T are separate; P313 uses D_T and C_H=A. Apply P4.35’s local branch count to D_B→B at p outside A and to D_A→A at p outside B, with eta∘phi=(nu|D_B)∘kappa and the explicit r±/r_q fibre counts. Preserve the primary symbolic-square formula, all singular-A defect estimates, pullback conormal degree0, cubic spectral morphisms and finite birational normalizations, projective-bundle adjunction, all three degree-three graph cases, both common cubic zeros, analytic simple-root factor x−y alpha and the last genus contradiction. The former final arithmetic repeats now accompany the genus formula; the integral ceiling bounds still follow from the displayed graph inequalities.'),
'night:P4.58': (
    'The entire torus-fibre support classification and all Euler/parity/equality conclusions remain: the explicit standing setting replaces the undefined Part4.2 reference and the full support hypothesis stays.',
    'Read the full original and receiving proof. P314 is applied to the same full fibration and positive-ruled support, then the complete P4.54→R18→P4.55→P4.56→P4.57/R20 chain is preserved with no transverse restriction on the other component. Retain rational and class-VII alternatives, all zero-Euler normalization forms, nonnegative Euler additivity and the equality criterion. The repeated final discussion of omitted hypotheses is already stated and proved in the fully read P4.10/P4.11 examples, including the exact finite-cover group obstruction; their mathematical content stays at those owners. Full-chain closure still depends on the separately managed P4.41/P4.45 gates.'),
}

events = []
for label, (scope, comparison) in comparisons.items():
    events.append(dict(statement_id=label, date='2026-11-22',
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 provenance',
        type='used and rechecked in this run',
        outcome=comparison + ' Exposed complete original/receiving comparison; no independent derivation, program execution or final-page credit.',
        event_id='publish:c3:refined-consumer:' + label, phase='publication proof and consumer comparison',
        source_file='agents/continuation3_provenance/refined_consumers/S6_SERIES_PUBLISH_refined_CHECK_EVENTS.tsv',
        source_row='', source_event_type='used and rechecked in this run',
        evidence_group='publish:c3:refined-consumer:' + label, publish_input_file='',
        publish_input_row='', date_utc=now, where='Complete bounded owner and exact prerequisite/application maps'))
tsv('S6_SERIES_PUBLISH_refined_CHECK_EVENTS.tsv', events)

consumer_rows = []
for label in ['night:P4.51','night:P4.40','night:P4.43','night:P4.42','night:P4R.18','night:P4.55','night:P4.58']:
    target = 'lem:II:horizontal-primary-conductor' if label in ['night:P4R.18','night:P4.55'] else 'lem:II:positive-ruled-conductor-graph'
    consumer_rows.append(dict(refined_source='night:P4R.13', consumer=label,
        receiving_owner=target, preserved_scope=comparisons[label][0],
        exact_application_and_outcome=comparisons[label][1],
        reading='Complete original and receiving statement/proof read; exposed comparison.'))
consumer_rows.append(dict(refined_source='night:P4.40', consumer='Paper II outward references',
    receiving_owner='night:P4.40 unchanged refined statement',
    preserved_scope='All aliases and the full statement are preserved.',
    exact_application_and_outcome='Exhaustive searches of both labels, both descriptive aliases, tags02XE/02Y6, bare printed names and all five P4R.13 equation labels found no additional mathematical consumer. P4.40 has no outward mathematical consumer in II. Its further-result listing and the excess-one program row have matching scopes and remain unchanged.',
    reading='Full refined proof read; other mentions classified by their actual function.'))
tsv('S6_SERIES_PUBLISH_refined_consumer_maps.tsv', consumer_rows)

evidence = {
'D01':'No account of drafts, readings or runs remains in these owners; mathematical uses of original local equation and new blowup coefficient describe explicit maps.',
'D02':'State all global hypotheses positively; retain unrestricted other-component scope in the statements. Replace defensive primary-quotient wording by the exact restriction maps.',
'D03':'Every owner states a mathematical conclusion; no proposal from the workflow is the object of a theorem.',
'D04':'All printed internal statement names are converted to existing numbered references; dictionary and label keys remain unchanged.',
'D05':'Requested or remaining classes are replaced by the numbered standing setting, including the full irreducible-or-normal-crossings hypothesis where needed.',
'D06':'No compendium or inaccessible numbering remains in the receiving fragments.',
'D07':'No worker, model, run or file-history language occurs in these mathematical owners.',
'D08':'Remove process emphasis and the completed section title; keep each concrete mathematical map and object.',
'D09':'No body program path or bookkeeping is introduced. Existing R13/P440 program rows have matching scopes and remain unchanged; the editorial driver is not a paper program.',
'D10':'Inherited tag-only statement renderer and hidden metadata mechanism are untouched; all old tags remain.',
'D11':'Each scope is stated once with exact hypotheses; no additional transverse condition is placed on other components.',
'D12':'P313 owns primary restriction; P314 owns the positive-ruled graph reduction. P4.55 applies P4.35’s exact local branch count and P4.33’s section/ruling maps. Remove its repeated last arithmetic and P4.58’s repeated example summary.',
'D13':'All new mathematical assertions are in numbered lemmas or their receiving proofs; the two inserted owners carry complete proofs and their labels.',
'D14':'Place P313 before R13 and P314 before P4.51. All shared premises precede their applications. Full-paper order, proportions and final page concordance remain root gates.',
'D15':'No front-matter or methodological count is changed. The two further-result descriptions match their unchanged refined statements; final front-matter gate remains with root.',
'D16':'Inherited titles and tags remain; the two new lemmas have short mathematical titles. The inherited D16 closure is not reopened.',
'D17':'Greb’s exact analytic criterion is cited and applied through the same trace map; existing known-result applications remain. The blowup calculation identifies the particular divisor quotient and its algebra map.',
'D18':'Freshly opened Greb2011 §2.1 and complete Remark2.1 p.415; exact publisher/Numdam edition and PDF hash recorded. No unversioned replacement citation is introduced.',
'D19':'Every manual equation number in these fragments is converted to the section counter; all original equation labels are preserved, including three transferred with P313.',
'D20':'Distinguish B from ruling base B0, D⊂N from pole divisor D_T⊂T, and the H sections through sigma and q,s. Use consistent component indices K_i,R_i,L_i.',
'D21':'The arguments retain exact integer graph counts, conductor lengths, polynomial identities and intersection forms; no numerical agreement is substituted for proof.',
'D22':'Each number2,3,9/2 and the spectral genus is supported at its use; the adjunction intersection product is moved beside its genus formula.',
'D23':'All environments balance; display conversion preserves mathematical tokens and removes blank paragraphs inside display math. Sentence-start generated references are capitalized. Final rendered-page reading remains a root gate.',
'D24':'The refined statement scopes and further-result wording remain aligned. The full-paper final structural description is outside these bounded guards.',
'D25':'Read all complete original and receiving proofs and exact maps. Preserve zero-Euler scope in P4.42, all primary branches at self-identifications, and all global support hypotheses. P4.41/P4.45 remain separately managed deformation premises; their closure is not credited here.',
}
unit_rows = []
for label in comparisons:
    for kind, detail in evidence.items():
        gate = 'source comparison complete; final integrated gates pending'
        if kind in ['D10','D16']:
            gate = 'inherited closure preserved'
        elif kind == 'D25':
            gate = 'complete local exposed comparison; separate P4.41/P4.45 premise gates remain'
        unit_rows.append(dict(unit=label, type=kind, status=gate, evidence=detail, owners=label))
tsv('S6_SERIES_PUBLISH_refined_unit_status.tsv', unit_rows)

primary = ROOT.parents[1] / 'tmp/c3_provenance_primary/Greb2011.pdf'
raw = primary.read_bytes()
tsv('S6_SERIES_PUBLISH_refined_sources.tsv', [dict(
    source_id='II-C3-REFINED-S01', url='https://www.numdam.org/item/ASNSP_2011_5_10_2_413_0.pdf',
    version='Greb, Annali della Scuola Normale Superiore di Pisa, Classe di Scienze (5)10(2),2011,413–426; Numdam publisher copy',
    exact_locus='§2.1, full setup and Remark2.1, printed p.415',
    source_sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw),
    established_scope='For normal complex spaces, rational singularities are equivalent to the Cohen–Macaulay condition together with equality of the resolution pushforward of the canonical sheaf and the canonical sheaf downstairs. In complex dimension two the rational and 1-rational notions coincide.',
    exact_application='P4.33 gives R1 sigma_*O_T=0 for the same noncontracted-section normal surface N; N is Cohen–Macaulay and sigma is a proper resolution. Apply the surface criterion, then identify its canonical map with the identity on the smooth locus. Tensor by nu*omega_S inverse and use the residue pole identity to obtain sigma_*O_T(−D)=I_N as ideal subsheaves.',
    reading_extent='Fresh online primary opening and full §2.1/Remark2.1 read; the remark states the criterion without a separate proof there. No proof of Greb’s quotient theorem is claimed.', date_utc=now)])

report = [
'# Refined-conductor consumers: complete exposed comparison', '',
'The complete original and receiving statements and proofs of all eight existing bounded owners, together with both extracted owners, were read. The credit is **used and rechecked in this run**. This is an exposed comparison, not an independent proof or an executed mathematical computation.', '',
'## Exhaustive Paper II coverage', '',
'The search covered both numbered labels and statement aliases, both descriptive refined aliases, tags02Y6/02XE, all bare printed names, and all five equations defined by the elliptic-conductor owner. It found the seven mathematical relationships listed in the consumer-map table. There are no external consumers of the five equation labels, and no outward mathematical consumer of P4.40 elsewhere in II. Dictionary entries, the further-result descriptions and the two program rows were checked in their actual roles.', '',
'The old ranges in the preserved snapshot are R13:19013–19479; P4.51:21064–21248; P4.40:21410–21516; P4.43:21520–21581; P4.42:21775–21889; R18:22959–23146; P4.55:24421–24668; P4.58:25619–25701. Integration uses complete content guards, not line numbers. P313 is inserted before R13; P314 before P4.51. The two adjacent subsection-title guards are also included. P280 remains unused.', '',
'The refined statements R13 and P4.40 and the full P4.51 statement are byte-identical. The protected E.5.2/E.5.3 statement bytes are unchanged. Every original label and tag multiplicity is preserved. No shared source or central register was written.', '',
'## Full owner comparisons', '',
]
for label, (scope, comparison) in comparisons.items():
    report.extend(['### ' + label, '', '**Preserved scope.** ' + scope, '', '**Complete comparison.** ' + comparison, ''])
report.extend([
'## Remaining integration and premise gates', '',
'Root separately admitted the zero-Euler/P253 and Hessian consolidations and the updated P4.33. Its full receiving statement/proof was reopened for the P313 and P4.55 applications. R14 and R15 now have separately admitted full-multiplicity repairs. P4.41 and P4.45 remain open factor-preserving-deformation premises; no closure of those owners or their dependent main chain is claimed here.', '',
'The local application checks and bounded source guards are complete. Root still owns integrated builds, rendered-page checking, final-page concordances, the full paper’s structural gate, the final provenance/records pass and counts. The two new owners count as extraction and comparison work, not independent results or independent proofs.', '',
'## Primary-source reading', '',
'Greb2011 was freshly opened online at https://www.numdam.org/item/ASNSP_2011_5_10_2_413_0.pdf, §2.1/Remark2.1 p.415. The PDF hash and exact application are in the source table. Only our paraphrase and source metadata are stored in the checkpoint; the PDF remains outside it.', '',
])
(OUT / 'S6_SERIES_PUBLISH_refined_comparison.md').write_text('\n'.join(report), newline='\n')
print('Recorded complete exposed comparisons, ten actual check events, all25-class unit statuses, consumer outcomes and the exact primary-source opening; shared records unchanged.')
