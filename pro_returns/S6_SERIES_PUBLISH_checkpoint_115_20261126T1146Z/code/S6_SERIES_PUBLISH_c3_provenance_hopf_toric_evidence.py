#!/usr/bin/env python3
"""Record the exposed full-unit reads and exact source applications."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_provenance/hopf_toric'
TMP=ROOT.parents[1]/'tmp/c3_provenance_primary'
now=datetime.now(timezone.utc).isoformat()


def read(name):
    with (OUT/name).open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))


def write(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)


rows=read('S6_SERIES_PUBLISH_hopf_toric_defects.tsv')
for row in rows:
    row['review_status']='Complete original and receiving owner proofs read; final bounded receiving corrections reread. Exact input/application comparison completed after proof exposure. Used and rechecked; no independent, final-PDF or untouched-consumer full-proof credit.'
    # Locate small cleanup rows in their unique owner in the complete guarded source.
    if not row['statement_id']:
        candidates=[]
        for family in ['hopf','toric']:
            guards=read('S6_SERIES_PUBLISH_hopf_toric_guards.tsv')
            whole=next(g['old_text'] for g in guards if g['change_id']==f'II-C3-HOPF-UNIT-{family}')
            for m in re.finditer(r'\\begin\{proposition\}.*?\\label\{(cdp:st:C\.2\.UN\.\d+)\}([\s\S]*?)\\end\{proof\}',whole):
                if row['old_text'] in m.group():candidates.append(m.group(1))
        row['statement_id']=';'.join(candidates) or 'bounded Hopf/toric receiving unit, exact text in row'
write('S6_SERIES_PUBLISH_hopf_toric_defects.tsv',rows)

sources=[]


def source(key,url,path,version,locus,paraphrase,application,extent):
    raw=path.read_bytes()
    sources.append(dict(source_key=key,url=url,version=version,locus_read=locus,
        sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),own_paraphrase=paraphrase,
        exact_application=application,read_extent=extent,date_utc=now))


source('GHK2015','https://www.numdam.org/item/10.1007/s10240-015-0073-1.pdf',TMP/'GHK2015.pdf',
    'Published IHES122 (2015), pp.65–168; Numdam primary facsimile',
    'Definition1.1 pp.75–76; Definition1.2 and complete Proposition1.3 statement/proof pp.76–77',
    'A smooth rational projective surface with an anticanonical nodal cycle admits a toric blowup that maps birationally to a smooth toric pair, with the map on the specified boundary an isomorphism. The proof uses ordinary contractions, node blowups and ruled-surface elementary transformations.',
    'UN68 passes the proved projective rational pair (V,D) to the theorem. The maps rho and tau are retained. The anticanonical intersection D.E=1 forces rho to factor through boundary-node blowdowns, while tau contracts curves outside the boundary meeting a smooth boundary point. Their Euler changes give Q(V,D)=number of tau steps. At Q=0, toric fan deletion of each boundary (-1)-ray descends the action along rho to exactly (V,D). All original P2/Hirzebruch coordinate maps remain.',
    'Entire cited definitions, proposition and its printed proof read; online primary PDF and publisher/archive metadata opened; application proof exposed and rechecked.')
source('Khaled2024Hopf','https://arxiv.org/pdf/2310.05265v2',Path('/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/Khaled2024_v2.pdf'),
    'arXiv2310.05265v2, 4December2023',
    'Normal-form list(1), p.3; full Theorem2.1 and Remark2.2, p.5',
    'The recalled primary Hopf classification gives scalar, resonant diagonal, nonlinear resonant, linear Jordan and nonresonant diagonal contractions, with the listed parameter identifications.',
    'UN38 uses F(z,w)=(beta^r z+w^r,beta w): r>=2 is typeIIa with beta=delta, and r=1 is typeIIb. Its diagonal quotient is the corresponding diagonal normal form. The proof retains the Laurent normal-power criterion and the complete higher-jet obstruction.',
    'Complete listed forms and cited theorem/context read. The theorem recalls the classification and prints no separate classification proof; none is claimed read.')
source('Nakamura2008VII','https://www.math.sci.hokudai.ac.jp/~nakamura/70surfaces080306.pdf',TMP/'Nakamura2008VII.pdf',
    'Author PDF titled Survey on VII0 surfaces, dated14April2008',
    'Title/date p.1; complete §1.1, including Theorems1.1.1–1.1.2, p.2',
    'The survey recalls the primary contraction form and the meromorphic-function criterion. Its finite-cover characterization identifies the b1=1,b2=0,a=0 surfaces containing a curve with surfaces admitting a finite unramified primary Hopf cover.',
    'UN38 takes the finite unramified primary cover pi:Hprime→H of its given Hopf normalization. The receiving proof verifies a(Hprime)=0 by the elementary symmetric functions of the local sheets and identifies K_Hprime=pi* K_H before applying the primary axis obstruction.',
    'Complete cited statements and local setup read; these recalled theorems have no proofs printed in §1.1, and no unprinted proof is claimed.')
source('Kurdyka1998','https://www.numdam.org/article/AIF_1998__48_3_769_0.pdf',TMP/'Kurdyka1998.pdf',
    'Original AIF48(3) (1998), pp.769–783; Numdam facsimile',
    'Theorem(LI), p.775; equivalence discussion pp.775–776; complete Theorem1 proof pp.776–778',
    'Near the zero set of the stated subanalytic function, the gradient has a lower bound by a positive constant times a power of the function with exponent strictly between zero and one. The analytic local case follows from the stated formulation.',
    'UN44 takes phi=|f|² in each real analytic coordinate chart, uses compactness and norm equivalence to choose uniform c and theta, and integrates the length of V=−grad(phi)/||grad(phi)||² below a positive level. Its group maps use the earlier P233 inclusion/retraction, preserving both old labelled quantitative estimates.',
    'Complete cited inequality and its displayed deduction from Theorem1 read, with the full printed Theorem1 proof. No claim to reread all of §3 is made.')
source('Lojasiewicz1964','https://www.numdam.org/item/ASNSP_1964_3_18_4_449_0.pdf',
    ROOT.parent/'S6_PUBLISH_c3_foundations_sources/S6_SERIES_PUBLISH_Lojasiewicz1964.pdf',
    'Original Annali SNS Pisa ser.3,18(4) (1964), pp.449–474; Numdam facsimile',
    '§3 Theorem1 statement, pp.463–464; complete Theorem2 and its printed reduction, p.464',
    'A locally finite family of semianalytic sets in a countable real analytic manifold has a compatible locally finite triangulation. The map is analytic on open simplices; the manifold statement is deduced from the preceding affine theorem via an analytic embedding.',
    'UN44 applies the theorem to the finite family of compact SNC components and all their intersections in the ambient real analytic manifold. Compactness gives a finite complex; closed intersections are closed subcomplexes. These are the exact cofibrations passed to P294 for P→E.',
    'Complete cited Theorem2 and its printed reduction read, together with the full preceding statement specifying properties(a)–(c). Portions of the supporting §4 proof were inspected; a complete fresh rereading of that proof is not claimed.')
source('HuybrechtsK3Draft','https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf',
    Path('/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/HuybrechtsK3Global.pdf'),
    '449-page author draft; title page2 identifies pre-publication copy and copyright2015; published-book metadata retained',
    'Chapter7 Corollary1.4 and complete proof, pp.127–128; immediately preceding proof of Theorem1.1, p.127, read for its deformation comparison',
    'Every complex K3 surface is simply connected. The corollary uses the deformation comparison with a smooth quartic and the vanishing of the relevant relative homotopy group for the quartic inclusion in projective three-space.',
    'UN47 applies the corollary to the stated K3 minimal model. The point-blowup maps from P234 identify its fundamental group with that of the given normalization resolution; the existing surjection to Gamma then gives Gamma=1.',
    'Complete cited corollary/proof and its immediate preceding deformation argument read; exact author-draft pagination and online primary PDF verified.')
source('AbashevaDeev2024AB','https://arxiv.org/pdf/2303.10764v1',TMP/'AbashevaDeev_v1.pdf',
    'arXiv2303.10764v1, 19March2023; published IMRN2024 metadata retained',
    'Complete §2.2.2, p.4, and §2.2.6, p.5; intervening primary normal-form definitions §2.2.1–5 also read',
    'The nonlinear primary normal form has one irreducible compact curve, the image of its axis. A diagonal primary Hopf surface with no nonzero-integer multiplicative relation between its two contraction eigenvalues has exactly the two axis curves. The resonant diagonal alternative carries the specified elliptic fibration.',
    'In UN38 the finite primary cover Hprime is first proved to have algebraic dimension zero. A positive relation alpha^q=beta^p would descend z^q/w^p as a nonconstant meromorphic function. Absolute values of the contraction multipliers put every nonzero-integer relation in this positive form after inversion. The exact nonresonant axis-list clause therefore applies. P248 is cited separately only for disjointness. No statement at P248 is enlarged.',
    'Complete named paragraphs and setup freshly read in the exact primary PDF. Fresh direct online retrieval returned HTTP200 application/pdf, 265648 bytes, identical to the recorded cached hash. The paragraphs recall curve classification and print no classification proof; none is claimed read.')
source('PopescuPampu2016','https://www.numdam.org/item/10.5802/wbln.14.pdf',
    ROOT.parent/'S6_PUBLISH_c3_foundations_sources/S6_SERIES_PUBLISH_PopescuPampu2016.pdf',
    'Winter Braids Lecture Notes3 (2016), CourseIII, pp.1–74; original Numdam PDF',
    'Complete Propositions3.10 and3.12 with their setup, printed p.III–20; intervening Proposition3.11 and its complete proof also read',
    'A normal complex surface singularity has a unique minimal resolution dominated by every resolution. Every proper holomorphic modification between smooth complex surfaces factors as point blowups. The source expressly states the analytic category for the second result.',
    'UN47 uses the same normal surface S_i^nu for V and Z, glues the local minimal-resolution factorizations over its smooth locus, and resolves their graph over that surface. The projections from W are proper holomorphic modifications between smooth surfaces, so Proposition3.12 gives the exact two point-blowup sequences. Pullback of two-forms and P234 compare p_g and fundamental groups, while equality of the two maps to U preserves the specified vertex-group image.',
    'Entire named statements and context freshly read in the original PDF, with online primary opening. The named propositions cite their proofs elsewhere; no unprinted proof is claimed read. The intervening explicit one-step self-intersection proof was read in full.')
write('S6_SERIES_PUBLISH_hopf_toric_sources.tsv',sources)

outcomes={
38:'Complete original and receiving UN38 statements/proofs read. Same proper family, full multiplicities, compact-subset canonical-neighbourhood scope and finite-primary-cover conclusion. Apply UN17 to the identical canonical evaluation and P222 to the hypersurface conductor. The complete primary axis list uses the freshly read Abasheva–Deev arXiv-v1 §§2.2.2/2.2.6; z^q/w^p excludes resonance at a=0. P248 supplies only its stated disjointness conclusion. Keep the full Laurent normal-power criterion, nonlinear canonical divisor and j+r coefficient contradiction. Order the finite-cover meromorphic-function argument before the axis list and identify K_Hprime=pi*K_H. The root-flagged citation scope was corrected in the proposal and reread. No new theorem scope or independent derivation claimed.',
39:'Complete original and receiving UN39 statements/proofs read. Keep every index term, all19 polynomial/order/average/zero-index rows and both geometric point/quartic examples. Read the complete newly admitted P413 and apply its same f, resolution and cohomology T, with the exact cup-product exterior-power maps. Compare finite companion determinants via their common eigenvalue product. Transfer the identical full-inverse-image Euler display C.ZC.8 to P234 and retain its c=r point/curve and arbitrary-multiplicity application. Resolution independence remains for the same proper family.',
44:'Complete original and receiving UN44 statements/proofs read. Preserve all meridian, semidirect, root-cover, integral R_d, abelianization, resolution, dual-complex, cup-product and rank-two conclusions at every multiplicity. Read P233/P234/P294 completely. The group comparison uses the same inclusion i:S→U; any strong retraction induces i_* inverse. Retain both old gradient estimates and V; transfer only the second complete gradient-retraction proof to the exposed old/new record. The explicit homotopy r_P233∘H_gradient identifies the old and receiving retraction maps relative to S. Check every lifted meridian, w elimination and inverse map, the normal cyclic-cover kernel, both hocolim maps, the finite-index graph formula and finite cover of the dual complex. Add the precise transpose/inverse-transpose determinant comparison. No finite program sample is used as the general proof.',
47:'Complete original and receiving UN47 statements/proofs read. Retain finite étale tube cover, its connected Stein disc t=s^a, fibre lattice cover, component pullbacks of degree e and count N/e, all p_g and chi inequalities, subgroup separability, residual finiteness, product finite quotient, double-cover invariants and uniqueness conclusion. Apply P233 and P234 through the same central inclusions and common-resolution maps. Cite the freshly opened author-draft K3 corollary at its exact locus. The two chi=1 image alternatives are stated directly with unchanged mathematical scope.',
68:'Complete original and receiving UN68 statements/proofs read, together with the full UN65 input and UN19 Hopf-minimal-model input. Retain the exact residue, adjunction, component blowdown, rationality propagation, SNC cochain, orientability, incidence, HRR and charge-sum arguments. Every old displayed mathematical formula survives. Replace the general charge proof by the complete exact application of opened GHK definitions/proposition to the proved projective pair. Check rho boundary blowdowns through D.E=1 and the full inverse-image divisor, tau interior blowdowns through boundary isomorphism, Q as the tau length, and the ray-deletion descent back to the given pair. Retain the P2 coordinate triangle, Hirzebruch quotient splitting, transition/action formulas and both node-blowup charts.'
}
events=[]
for n,outcome in outcomes.items():
    events.append(dict(statement_id=f'cdp:st:C.2.UN.{n}',date=now[:10],
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 provenance',
        type='used and rechecked in this run',outcome=outcome,event_id=f'publish:c3:hopf-toric:UN{n}',
        phase='publication complete-unit comparison',source_file='agents/continuation3_provenance/hopf_toric/S6_SERIES_PUBLISH_hopf_toric_CHECK_EVENTS.tsv',
        source_row='',source_event_type='used and rechecked in this run',evidence_group=f'publish:c3:hopf-toric:UN{n}',
        publish_input_file='',publish_input_row='',date_utc=now,where='Complete original and receiving bounded owner; exact input/application maps'))
events.append(dict(events[0],statement_id='lem:II:blowup-topology;cdp:st:C.2.UN.39',
    outcome='Read the entire existing P234 statement/proof. Its C.VR.4 full-inverse-image formula is the identical owner of removed C.ZC.8 under (Y,Z,S,Yprime,Sprime,r)=(U0,Z,S0,Uprime,Sprime,c). The receiving equation has both permanent targets and labels through SsixEquationAliases. No mathematical hypothesis or formula changes.',
    event_id='publish:c3:hopf-toric:Euler-alias',evidence_group='publish:c3:hopf-toric:Euler-alias'))
write('S6_SERIES_PUBLISH_hopf_toric_CHECK_EVENTS.tsv',events)

units={38:'subsec:II:hopf-component-boundaries',39:'subsec:II:resolution-euler-index',
44:'subsec:II:fibre-fundamental-groups',47:'subsec:II:component-geometric-genus',68:'subsec:II:rational-toric-components'}
classes={
'D01':'No earlier-run/draft narration remains in these owner proofs.',
'D02':'Negative workflow contrasts and imagined scope objections removed; positive mathematical scope and exact maps retained.',
'D03':'No proposal-refutation statement occurs.',
'D04':'All printed legacy-number references replaced by resolving labels; equation identities preserved.',
'D05':'No prompt item is a mathematical premise.',
'D06':'No outside-compendium reference remains in the units.',
'D07':'No agents/workers/runs named in the mathematics.',
'D08':'Workflow emphases removed occurrence by occurrence; mathematical original/support/multiplicity language retained where it names a map.',
'D09':'UN39/UN44 body paths and outputs removed; exact programs are in admitted appendix157/158.',
'D10':'Inherited done: hidden StatementRecord renderer and existing tag renderer unchanged.',
'D11':'Repeated closing scope disclaimers removed; every original mathematical hypothesis remains.',
'D12':'Repeated canonical evaluation, Hopf curve classification, full-support blowup Euler/π1 and pushout proofs transferred to exact earlier owners. Gradient alternative is preserved in exposed comparison with explicit relative homotopy.',
'D13':'All arguments remain within their numbered owner/proof; no new orphan result.',
'D14':'Five descriptive subsections, one complete owner/proof each. UN11 now precedes them; all applications use earlier inputs. Global structure remains root-owned.',
'D15':'Body units contain no front-matter/methodology block; global first-part revision remains root-owned.',
'D16':'Inherited done; every existing proposition remains titled and all tags remain unchanged.',
'D17':'Known normal forms, curve geometry, triangulation, gradient inequality, K3 theorem and toric model used at exact cited/receiving owners. Short remaining arguments identify the precise application maps.',
'D18':'All new or sharpened printed primary locators opened at the named version/page; existing bibliography keys/publication metadata retained.',
'D19':'Every old manual tag converted to section-numbered display; C.ZC.8 transfers to the identical P234 formula. All old targets and labels survive.',
'D20':'Explicit cover/canonical pullback, determinant transpose conventions, component covering degrees, and distinct toric/ruling maps fixed.',
'D21':'No computational agreement is stated as a new mathematical result; identities and maps remain.',
'D22':'Finite-cover premise order, current pullback f0, logical group alternatives, toric map factors and action descent are explicit.',
'D23':'Source-level article agreement, paragraph controls, nested lists and display blank lines checked; integrated build/page reading remains root-owned.',
'D24':'No description of the paper structure occurs locally; global §1 concordance remains root-owned.',
'D25':'No original statement was refuted or narrowed. Receiving application gaps were filled explicitly before admission; all mathematical conclusions and scopes were compared.'}
statusrows=[]
for n,unit in units.items():
    for kind,outcome in classes.items():
        status=('inherited done' if kind in ['D10','D16'] else
                'not applicable locally; global pending' if kind in ['D15','D24'] else
                'source ready; integrated build and page reading pending' if kind=='D23' else
                'locally ready for source admission')
        statusrows.append(dict(unit=unit,statement_id=f'cdp:st:C.2.UN.{n}',defect_type=kind,status=status,
            outcome=outcome,credit='Exposed complete original/receiving proof comparison; no independent or final-page credit.',date_utc=now))
write('S6_SERIES_PUBLISH_hopf_toric_unit_status.tsv',statusrows)

status=json.loads((OUT/'S6_SERIES_PUBLISH_hopf_toric_status.json').read_text())
status.update(complete_receiving_read='complete; each final bounded correction reread',source_rows=len(sources),
    exposed_check_events=len(events),unit_class_rows=len(statusrows),ready=True)
(OUT/'S6_SERIES_PUBLISH_hopf_toric_status.json').write_text(json.dumps(status,indent=2)+'\n',newline='\n')
print(json.dumps(status,indent=2))
