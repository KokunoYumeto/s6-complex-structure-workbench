"""Record completed whole-proof reviews, separate executions, and bounded source readings."""
from pathlib import Path
import csv, datetime, hashlib, json

P=Path(__file__).resolve().parents[2]
R=P.parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS'
idx=json.loads((P/'analysis/inventory_source_index.json').read_text())
proofs={
'P3F.47': 'Read and rederived the entire joint III-star/II construction and topology proof. Checked the literal E7-B source and marked section, both kinds of star and II roots, full resolved Cartier and norm maps, the retained finite characters, and the global closing cocycle. Reconstructed the integral E7 source cone with both physical boundaries, torsion and graph integers. The exact primitive cap maps give the joint determinant D=m_II*n_star+m_star*n_II; the first three Smith factors are one, including the D=0 case. The trace-one nodal vanishing-cycle pairing kills the remaining elliptic fundamental group, and the actual Hopf-meridian filling proves the stated sphere criterion D=plus or minus one. No return formula is inferred from the topology alone.',
'P3F.48': 'Read and rederived the whole weighted extra-site exclusion, keeping all integral order-one clutches. Checked the oriented Thom representatives and both zero connecting maps, the actual source inversion on the localized exterior and its extension across the extra smooth sites. Its square forces the cross block to vanish over the torsion-free ring Z_(p), including p=2. The marked smooth meridian quotient is (R/m)^2 by the explicit invertible row map. For a multiplicative site, the actual Tate product retains the physical graph coefficient, isotropy fixes both exterior columns, and the written unimodular target and source maps give diag(1,1,-m,-m). The Seifert quotient makes effective orders pairwise coprime and excludes the old torsion primes; thus every additional smooth or multiplicative effective order is one, with its full integer collar data retained.',
'P3F.49': 'Read and rederived the complete affine-conjugacy proof. Checked the central (1-D) maps on the good IV elliptic curve, reduced IV component and identity groups, and the quadratic star identity C-star group. The explicit finite norm homotopy supplies the analytic coboundary after taking the local logarithm. In the quadratic Tate model the actual even root U satisfies U(z)U(-z)R_0=R and induces the source conjugacy, with all blowup centres transported. The degree-zero line extensions commute on the generic fibre; the scalar cochain has the displayed ratio b(z)/b(zeta^-1 z), and its central character chi is retained through the norm. These are actual source, resolved Cartier and annular arrows.',
'P3F.50': 'Read and rederived the complete inverse-action comparison. B_lambda inverse equals mu times B_0 inverse with mu=lambda inverse, so the cyclic quotient and physical line are literally the same; the cap relation changes n to -n. The valuation matrix changes by diag(1,-1), while the physical monomial chart map is the identity. The separate source inversion has its stated line and fan maps. The positive parameter loop maps to the reversed loop, giving the inverse relative return. Reopened the retained K23 local generator proof: left and right quaternion multiplications commute pointwise, and the supported-disc factor is central; hence inverse negates all three relative coordinates. The characteristic pair uses the corrected physical line of K68. No refuted historical K23 scalar coefficient is used. Read Engel Remark8.5 in the attached TeX and matched the whole remark on page24 of its attached-source PDF build.',
'P3F.51': 'Read and rederived the full coefficient-generic source theorem. Derived both marked Weierstrass models, discriminants, special-profile loci and literal coefficient scalings. Checked the good and reduced root substitutions with every coefficient and section exponent, formal contact of 2G and 3G, invariant resolutions and crepant section rays. The full Cartier diagrams, component degrees, whole-fibre descent and arbitrary Tate units supply the line and root comparisons. The explicit unimodular source-lattice and boundary maps identify the needed source pairs, and the stated vanishing-cycle arguments prove the sphere criteria on every fixed source. The current K26/K28/K30 comparisons retain the actual root parameter, chosen reference fan, physical line and annular data. Replaced the historical running sentence by the independently rederived K38 intrinsic-scalar subgroup and actual shorter quotient, with precisely its signed and marked scope.',
'P3F.54': 'Read and rederived the entire marked source-moduli closing proof. Checked the selected-node parametrization, exact factorization, local Jacobian and selected cusp derivative, the proper exterior family and uniform finite-cap choices. Continued the node coordinates and Tate parameter through the cusp, including the exact theta-Cartier identity and cancelling Tate deck factor. The actual line map is (Z,V)->(q_T/Z,V); the height map sends (v_Z,v_V,h) to (-v_Z+h,v_V,h). Its edge reflection is the identity modulo two and cannot preserve all three distinct primitive edge lines of a unimodular triangular fan. Its square literally closes every source, line and cap transition on the rho double cover. The receiving text now identifies F56 as the separate full trace calculation of the physical vertical-fan return.',
'P3F.55': 'Read and rederived the complete local lifted-link proof. The exact normalization germ, positive radial derivative and Jacobian-minor ideal (s,rho^2) give the oriented smooth three-sphere link and immersion. Computed both ordered double circles, their positive mutual linking, the two self-framings of -1 and the summed pushed vector; restriction of the image equation gives the Ekholm number +2. Matched the actual Némethi–Pintér quaternion maps and realification [u]->-[L]; directly checked that q i q^-1 has Hopf invariant -1 in q=z+w j coordinates, so the Whitehead square maps to -4[L]. This gives Omega_S2=1/2 and the Gauniyal–Turchin value one. Read the precise primary formulas and proved the normalization bridge by the same punctured Kummer embedding: sigma=-16, e=0 gives value two in both group isomorphisms. This event proves the local link only; the family-line comparison is the separate F56 review.',
'P3F.56': 'Read and rederived the entire 32,226-character selected-cusp trace proof, including every ambient, normal and circle-line comparison. Checked the second critical value, exact right Hurwitz word, punctured-torus boundary twist, actual weighted resolution and unimodular fibre-section-E8 plumbing. Constructed the disc-extending exterior suspension, exact local source shear, ordered-height isotopy and the actual inner rounded-ball link. Identified the complex normal line, determinant-trivial rank-two bundle, anti-linear Cox spinor and Hermitian dual M=U inverse on the full overlaps. The Thom and outer Wang maps prove the extension of the actual meridian line; the explicit positive-Hermitian Mobius ball map supplies the outer cap without erasing its normal clutch. Tracked both bordism boundary signs and the zero-index S(ad E) cap. Repaired the receiving Hopf paragraph with K68’s literal R4 reflection and full two-piece inverse-clutch maps. Thus A_U=1, A_M=-1 and the actual physical return has class -1. The cut-and-paste mapping torus has Eells–Kuiper value -1/28 for both spin structures; the actual degree-two clutch pullback has only even image, proving the specified descent obstruction.'
}
computations={
'P3F.47':'Unchanged iii_star_ii_joint.py and its fully read integer-chain helper pass: exact source Gram and translation, both mapping cones, all marked inclusion maps and torsion representatives, symbolic joint determinants, and supplementary Smith cases. The geometric roots and vanishing cycles were checked in the separate full-proof event.',
'P3F.48':'Unchanged weighted_extra_sites.py passes: exact localized smooth quotient, full multiplicative unimodular changes, involution-square block and supplementary prime cases. Its four source-inversion inputs are exact outputs of previously recorded current executions; their producing programs receive no new execution credit here.',
'P3F.49':'Unchanged os50_affine_conjugacy.py passes: finite norm/coboundary identity for 120 orders, central squaring, exact quadratic Tate conjugacy and telescoping scalar norm. Analytic extension, transported centres and actual line comparisons were checked separately.',
'P3F.50':'Unchanged expanding_action_comparison.py passes: signed determinant, actual basis inversion, cap relation and all three fan-recurrence inverse identities. The quotient, chart and parameter-loop maps were checked separately.',
'P3F.51':'Unchanged generic_source_models.py passes all 43 exact discriminant, coefficient-root, marked-section, formal-character and Cartier identities. The geometric quotient, section/component and source-pair arguments were checked separately.',
'P3F.54':'Unchanged source_moduli_nodes.py passes the exact node, Tate-Cartier, height-reflection, six mod-two edge-basis and zoom identities. Its saved unresolved field is historical source text; it grants no current status and is superseded at the stated vertical-fan scope by the separate F56 proof.',
'P3F.55':'Unchanged source_cusp_link.py and haefliger_normalization_bridge.py both pass the exact minor ideals, push-off polynomial, crosscap perturbation and rational normalization arithmetic. Quaternion orientation and the actual primary-source Kummer embedding are inputs verified in the separate full-proof/source-read events, not conclusions established by assigned program constants.',
'P3F.56':'Unchanged source_cusp_trace.py passes the exact normalization/shear, critical value, free-group Hurwitz word, Mobius ball inverse, integral E8 plumbing and degree-two residue computations. The actual ambient trace, line extension, orientation and Hopf-transfer identifications were checked separately.'
}
replay=json.loads((P/'analysis/IV/root_F47_56_certificate_replays.json').read_text())
assert replay['all_pass'] and len(replay['runs'])==9
events=[];details=[]
for sid,scope in proofs.items():
 loc=idx['S6_06_BLIND:'+sid]
 whole=(R/loc['file']).read_text();raw=whole[loc['start']:loc['end']]
 digest=hashlib.sha256(raw.encode()).hexdigest()
 details.append({'statement_id':'night:'+sid,'source_checkpoint':29,'source_file':loc['file'],
                 'start':loc['start'],'end':loc['end'],'source_proof_sha256':digest,
                 'whole_source_block_read':True,'full_argument_review':scope,
                 'receiving_repairs':'analysis/IV/root_F47_56_receiving_replacements.json',
                 'separate_computation_scope':computations[sid]})
 for typ,verdict,explanation in [('targeted proof check','proved',scope),
                                ('computation or formal certificate','PASS',computations[sid])]:
  events.append({'statement_id':'night:'+sid,'date':now,'who':who,'type':typ,
                 'verdict':verdict,'scope':explanation,'source_checkpoint':29,
                 'source_proof_sha256':digest,
                 'artifacts':'analysis/IV/root_F47_56_reviews.json; analysis/IV/root_F47_56_certificate_replays.json; analysis/IV/root_F47_56_receiving_replacements.json'})
with (P/'records/IV_root_F47_56_events.tsv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=list(events[0]),delimiter='\t');writer.writeheader();writer.writerows(events)
(P/'analysis/IV/root_F47_56_reviews.json').write_text(json.dumps(details,indent=2))

readings={
'NemethiPinter2015Root':{
 'exact_locator':'Comment.Math.Helv.90(2015), Theorem1.2.2 p515; Section2.4 pp519–521; Propositions4.2.2–4.2.3 p523; Theorem5.1.1 statement p525; complete Proposition6.1.1 pp526–528; Theorem8.1.1 p531; Theorem9.1.6 p534.',
 'scope':'Read the listed text and visually opened pp515,523,534. Matched the Jacobian-minor crosscap number, the exact q=z+w j quaternion convention and realification [u]->-[L], the complete common-extension comparison, and the positive sign in Omega_a=3 sigma/2. This is bounded source verification, not a full reading of the paper or its cited works.',
 'local_file':'analysis/IV/references/NemethiPinter2015Root.pdf','url':'https://ems.press/content/serial-article-files/43391?nt=1'},
'GauniyalTurchin2026Root':{
 'exact_locator':'Published paper, Section1 orientation/linking/intersection conventions pp1469–1470; Section2.1 p1471; Section4.1 pp1492–1493; equations4.1–4.3 and Theorem4.1 with the immediately preceding spherical-knot qualification p1493.',
 'scope':'Read these exact definitions and theorem; visually opened p1493. Checked the Ekholm orientation used for both sheets, zero-total-link framing, summed push-off vector, rational Whitehead generator and coefficients 1/2,1/6,1/3. The manuscript supplies its actual Whitehead-to-Stiefel map and Kummer normalization comparison. No reading of the entire theorem proof is claimed.',
 'local_file':'analysis/IV/references/GauniyalTurchin2026Root.pdf','url':'https://doi.org/10.1017/S0013091526101485'},
'Takase2005':{
 'exact_locator':'arXiv:math/0506356v1, corrected Theorem2.3 and Corollary2.6 pp2–3; Proposition4.1 and its proof pp7–8; Remark4.2 p8.',
 'scope':'Read the corrected Euler-square sign and the full punctured Kummer construction/proof; visually opened p8. The same actual punctured Kummer embedding in S5 has signature -16 and trivial normal bundle and gives corrected Haefliger value2. This is a preprint-page locator; no journal pagination or unrecorded reading of its cited sources is inferred.',
 'local_file':'analysis/IV/references/Takase2005v1.pdf','url':'https://arxiv.org/pdf/math/0506356v1'},
'Haefliger1966':{
 'exact_locator':'Ann.Math.83(1966), the framing/compression discussion in Section5.16 p420 and Theorem5.17 p421.',
 'scope':'Read the preceding framed surgery/compression paragraph and exact theorem; visually opened p421. It identifies the suspended subgroup as the even multiples of the Haefliger generator. Takase Remark4.2 supplies the particular punctured Kummer embedding used in the receiving comparison. Earlier readings at Theorem1.2 and Corollary6.6 remain separate.',
 'local_file':'analysis/IV/references/Haefliger1966.pdf','url':'https://www.maths.ed.ac.uk/~v1ranick/tda/haefliger.pdf'},
'Sakai2015Root':{
 'exact_locator':'Author preprint of Lin–Wang type formula for the Haefliger invariant, Proposition6.8 and its complete proof, PDF p19.',
 'scope':'Read the statement and full proof H=E=-Omega/12 for embeddings in R5 followed by R6, with Omega=3 sigma/2 and e=0. This directly corroborates the manuscript’s specified Kummer comparison. The locator is the opened author-preprint pagination.',
 'local_file':'analysis/IV/references/Sakai2015Root.pdf','url':'https://doi.org/10.4310/HHA.2015.v17.n2.a15'},
'Engel2026':{
 'exact_locator':'Attached original S6.tex, whole Remark8.5 at source lines1738–1760; matched whole remark on p24 of the attached-source PDF build.',
 'scope':'Read the exact fixed elliptic surface, degree-zero generic-fibre line and translation data, Hom line pi*O(plus or minus E), uniform contracting/expanding scaling and Mumford/log-transform construction. This verifies the precise input scope of F50/F51. The PDF is explicitly an attached-source build, not an independently downloaded journal edition.',
 'local_file':'build/literature/Engel/Engel.pdf','url':'https://arxiv.org/abs/2609.38442'}
}
for value in readings.values():
 value.update(date=now,checker=who,status='opened and matched at stated locus')
 value['sha256']=hashlib.sha256((P/value['local_file']).read_bytes()).hexdigest()
(P/'analysis/IV/root_cusp_primary_matches.json').write_text(json.dumps(readings,indent=2))

bib=P/'S6_10_PAPERS_references.bib';b=bib.read_text()
if '@article{NemethiPinter2015Root,' not in b:
 b+=r'''
@article{NemethiPinter2015Root,
 author={N{\'e}methi, Andr{\'a}s and Pint{\'e}r, Gerg{\H{o}}},
 title={Immersions associated with holomorphic germs},
 journal={Commentarii Mathematici Helvetici},
 volume={90}, number={3}, pages={513--541}, year={2015},
 doi={10.4171/CMH/363},
 url={https://ems.press/content/serial-article-files/43391?nt=1},
 verification={verified at listed scope},
 note={Current bounded reading is recorded in analysis/IV/root\_cusp\_primary\_matches.json; the listed exact loci support the explicit quaternion and Smale-invariant comparison.}
}
'''
 bib.write_text(b)
print('Recorded eight whole-proof reviews, eight separate replay-scope events, and six bounded primary-source readings.')
