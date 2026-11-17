"""Save an independent receiving review, without changing the provider proof."""
import hashlib
import json
from pathlib import Path

ROOT = Path('/workspace/scratch/037cd144174c')
OUT = ROOT / 'deliverables/work/cdp_audit/modular_collision_review'
OUT.mkdir(parents=True, exist_ok=True)
proof = ROOT / 'deliverables/work/invariants_arithmetic/maps_modular_collision_realizations.tex'
meta = {'model': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode)', 'effort': 'Pro', 'date': '2026-11-17', 'timezone': 'UTC', 'reader': '/root/cdp_audit'}
checks = [
 {'step': 1, 'source_lines': [1,125],
  'scope': 'All conventions, complete theorem, coset tables and genus calculation.',
  'reasoning': 'Checked both s involutions, r cycles, transitivity and sr cusp widths. The resulting modular subgroups have indices 4 and 10 in PSL2Z, one order-three elliptic point, no order-two point, and 2 or 3 cusps. The ramification sums are 6 and 18, so both compact bases have genus zero. The inverse-image subgroup in SL2Z contains -I; only the modular curve is imported at this stage, not an unavailable universal elliptic surface for a subgroup containing -I. The later Weierstrass construction supplies the actual elliptic surface.',
  'outcome': 'passes'},
 {'step': 2, 'source_lines': [126,224],
  'scope': 'Complete ribbon graph, peripheral paths, full free group and positive orientation.',
  'reasoning': 'Independently traced the non-tree half-edges. For index 4, T^3=ea^-1, V=a and H=e^-1 in a free group of rank 2. For index 10, T^5=eb^-1, B=a, C=a^-1b and H=e^-1 in rank 3. These are equalities before imposing the elliptic order-three relation. The retained trees have 7 edges on 8 vertices and 18 on 19 respectively and are connected. The root stems land at 1,3,7 as claimed. At the order-three fixed point, R has derivative exp(-2pi*i/3), hence a positive local j-loop lifts to R^-1; at a cusp q=exp(2pi*i*tau) gives T. Thus the order and signs are geometric, not inferred merely from a product of matrices.',
  'outcome': 'passes'},
 {'step': 3, 'source_lines': [225,291],
  'scope': 'Explicit index-four equation and divisor construction for the index-ten cover.',
  'reasoning': 'Checked c4^3-c6^2=1728 Delta, all three index-four valuations including the homogenized infinity valuations, and the resulting I1*, II, I3 fibres. For the degree-four passport, the three fixed-point-free involutions are permuted transitively by the centralizer of the indicated 3-cycle, giving the required marked-cover identification. For degree ten, the divisors of j Delta and (j-1728) Delta have multiplicities divisible by 3 and 2 respectively and total degree 12. Pic(P1)=Z and complex scalar roots therefore give global sections c4 in O(4), c6 in O(6). The resulting identity is exact, not only a divisor equality. Minimality holds locally at every point, with II at the simple point over zero and I5,I3,I2 at the poles. The degree-one fundamental line bundle and singular fibres meet the opened rationality criterion.',
  'outcome': 'passes'},
 {'step': 4, 'source_lines': [292,332],
  'scope': 'Projective monodromy, integral signs and simultaneous conjugation.',
  'reasoning': 'The constructed j-cover determines projective monodromy on the complement of the elliptic values. Smooth preimages introduce no additional local sign. Kodaira types fix the two possible SL2 lifts: the type-II trace is 1, the multiplicative lift is positive unipotent and the starred lift is negative. All punctured-sphere generators have specified signs, so no quadratic-character ambiguity remains. Cyclic starting-arc changes give the stated canonical tuples. Both tuples and their simultaneous V/B conjugacies were recomputed and match every archived matrix.',
  'outcome': 'passes'},
 {'step': 5, 'source_lines': [333,447],
  'scope': 'Full integral junction conversion, natural logarithm interpretation and section realization.',
  'reasoning': 'For P_i=A1...A_(i-1), K_i=P_i Ai^-1 P_i^-1, verified K1...Ki=P_(i+1)^-1. Reversing the circuit list therefore satisfies Fukae’s reverse-product convention, and the ordinary reversed peripheral basis is obtained by the indicated Hurwitz moves. The integral transformation y_i=P_i q_i preserves saturated local images and transforms the closing relation into sum y_i=0. For an integral coboundary, y_i=(I-K_i)P_(i+1)v, which is exactly the opened null-junction formula in the reversed order. The cut-and-logarithm argument identifies this with actual section jumps, rather than only an abstract lattice isometry. On a rational surface Pic=H2 integrally, and restriction of a degree-zero divisor to the generic elliptic fibre gives a rational point, extending to a section by properness over the nonsingular base curve. The kernel consists of the stated vertical/zero/fibre adjustments. Finally, the determinant-one type-II difference gives a unique integral gauge q_II=0. The two remaining primitive kernels are Z, with no torsion; both archived cocycles are generators.',
  'outcome': 'passes'},
 {'step': 6, 'source_lines': [448,524],
  'scope': 'Complete height normalization, rational arithmetic, certificate specification and limits.',
  'reasoning': 'Verified (I-K_i)P_i(z_i+q_i)=P_i q_i and the diagonal wedge equality. Reversal negates the ordered cross term. The unipotent test A=T^n yields the original -t^2/n convention, fixing the sign. The two diagonal/cross totals are -97/12 and -8, and -31/30 and -1, so the junction squares are -1/12 and -1/30. Opposite pairing gives exactly the asserted positive heights. These agree with the original Fukae row-50 and row-56 lattices. The certificate only checks finite exact statements and does not purport to replace the geometric proof.',
  'outcome': 'passes'}
]

sources = [
 ('mapsMilne2017','Milne2017.pdf', 'https://www.jmilne.org/math/CourseNotes/MF.pdf',
  'Version 1.31, 22 March 2017: Proposition 2.16 and proof pp.34–35; Examples 2.19–2.20 and local quotient coordinates pp.35–36; Proposition 2.21 p.36; general finite-index compactification p.37; Theorem 2.22 and complete ramification proof pp.37–38; Proposition 4.3 and Remark 4.4 p.49.',
  'Arbitrary finite-index subgroup, PSL index, compact modular curve, local elliptic/cusp coordinates, genus and j=1728J. No congruence assumption or universal elliptic surface for a group containing -I is imported.'),
 ('manFukae02','Fukae2002.pdf','https://arxiv.org/pdf/math/0205062',
  'Original arXiv math/0205062v1: Section 2.1 p.3 and footnote 1; Section 3.1 pp.6–10, equations (4),(8),(9); Section 3.2 pp.11–13, Lemmas 3.1–3.2, their supplied proofs and equation (11); Section 4.1 pp.21–22, Lemma 4.1 with supplied proof, Theorem 4.2 and Corollaries 4.2–4.3; Table 3 p.35 rows 50 and 56 (also visually read).',
  'Exact inverse-circuit and reverse-product convention, integral rational-charge junction quotient, null junctions and opposite MW pairing. The rational-surface hypothesis is established by the provider. Only these scopes were reopened; the complete classification proof was not re-audited.'),
 ('manSS10','SchuettShioda2010.pdf','https://arxiv.org/pdf/0907.0298',
  'arXiv0907.0298v3, Section 4.5 Table 1 p.14; Sections 8.2–8.4 pp.38–39.',
  'Characteristic-zero minimal Weierstrass valuations for II, I_n and I_n*, plus rationality of a minimal degree-(4,6) equation with a singular fibre. c4,c6 differ from a4,a6 only by nonzero constants. The complete classification theory behind the table is not re-proved.'),
 ('manMiranda90','Miranda1990.pdf','https://www.math.colostate.edu/~miranda/preprints/Perssonslist.pdf',
  'Original Section 4: p.206 star-transfer abbreviation; p.207 degree-four entry *II31; p.210 degree-ten entry II532. All three pages were read visually.',
  'Credit comparison for the two known fibre configurations. The displayed permutation examples establish earlier existence; the new provider supplies the exact archived marking and section cocycles, not a new configuration. No claim of worldwide novelty is inferred.')
]
refs=[]
for key,name,url,locator,scope in sources:
    p=ROOT/'sources/audit_cache/inv_ari/maps_literature'/name
    refs.append({'key':key,'aliases':[],'url':url,'local_source':str(p.relative_to(ROOT)),
                 'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'verified in the specified scope',
                 'locator':locator,'verification':scope,'reader':meta})
(OUT/'references_verified.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n')
record={'source_run':'WRITING_REPAIR','source_id':'MODULAR_COLLISION_50_56',
        'printed_label':'mapsD:repair:collision-realization','source_file':str(proof.relative_to(ROOT)),
        'source_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'source_lines':[1,524],
        'reader':meta,'read_scope':'Every line of the full statement, all six proof steps, all pre-statement conventions and the complete executable-certificate description; all 413 lines of the authored verifier.',
        'outcome':'Independent receiving review passed for both exact marked profiles; the missing geometric realization is supplied.',
        'checks':checks,'unresolved_mathematical_objections':[],
        'required_proof_replacements':[],
        'references':'deliverables/work/cdp_audit/modular_collision_review/references_verified.json',
        'program_rerun':'deliverables/code/cdp_audit/modular_collision_review/execution_manifest.json',
        'credit':'Miranda1990 Section4 supplies the configurations; Fukae2002 Table3 supplies the rank-one MW lattices. The provider gives explicit archived markings and cocycle realization. Its conclusion is limited to profiles50/II and56/II.',
        'scope_limitations':['No independent worldwide novelty search is claimed for this two-profile receiving review.', 'The external source checks match the imported statements and supplied proofs; they are not audits of the whole cited books or papers.', 'The imported 893-line archived section engine was compared by the verifier, not independently re-read in full in this event. The independent gauge/kernel derivation in the proof was re-derived.']}
(OUT/'independent_review.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
report=['# Independent review of the two modular collision realizations','',
        '**Outcome:** both exact marked profiles pass the independent receiving review. The 524-line proof supplies the geometric realization previously absent from the archive. No replacement of the proof is required.','',
        'The receiving review read every line of the statement, all preceding conventions, all six proof steps and the complete certificate description. It also read all 413 verifier lines and reran an unchanged isolated copy. Both retained stdout and the full JSON certificate agree byte for byte.','']
for c in checks:
    report += [f"## Step {c['step']}: {c['scope']}",'',c['reasoning'],'']
report += ['## Credit and scope','',record['credit'],'',
           'The review imports only the exact primary-source statements recorded in references_verified.json. It does not promote the finite program to a geometric existence proof and does not infer realizability of arbitrary monodromy factorizations.','',
           'Reviewer: GPT-6 Astra (OpenAI, ChatGPT Pro mode); effort Pro; 17 November 2026 UTC. The author and receiving reader are separate agents using the same model, not an external human review.','']
(OUT/'independent_review.md').write_text('\n'.join(report))
print('Saved complete independent modular collision review and four exact primary-source scopes.')
