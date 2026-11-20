"""Record bounded current conclusions without changing publication source files."""
from pathlib import Path
import csv, hashlib, json

P = Path(__file__).resolve().parent
A = json.loads((P / 'row_assessments.json').read_text())
who = 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family'

def put(label, conclusion, routes, risk, form, state='high; mathematical receiving gate closed at the stated scope'):
    A[label] = dict(confidence_state=state, confidence_line=conclusion,
                    independent_routes=routes, remaining_risk=risk, format_check=form)

put('inv:A2.1',
    'The raw determinant K=6 mu_z^2-tau_z beta_z equals tau_z^2 E4^2/E6 in the prescribed marking, descends through the actual order-four kernel, has root orders 2 and 0, and gives the coarse logarithmic degeneracy divisor p1+p2 with a cusp unit.',
    ['Retained full-proof checks include Claude Fable 5.2 (Anthropic), high/max, 16 November, and GPT-6 Astra, 17 and 18 November; retain their recorded scopes and chronology. Source-to-print comparisons are not additional mathematical proofs.',
     'The retained modular-identity route and the separate WORKING_INV global-degree route give the same divisor: nonzero cusp value, forced root-character zeros, and degree two leave no further zero.',
     'Fresh after-reading priority_rows_exact.py differentiates both full affine period actions, checks the rational Q transformation and g2 squared kernel, both leading constants, coarse root exponents and cusp determinant; complete 79-check output includes this scope.'],
    'No unresolved mathematical determinant gate identified. Classical modular and canonical-extension inputs remain cited dependencies. The fresh finite algebra supplements, and does not replace, the analytic global identity proof.',
    'Entire current four-step proof reread. A unique guarded patch replaces the absent a_calculations.py assertion with the actual new program/output. All three inventory aliases share this conclusion; root owns final integration/layout.')

put('fam:src:A.5.1',
    'For the fixed original standard period marking, finite vectors and untranslated cusp fan, X_c and X_cprime are biholomorphic exactly when cprime-c lies in 2Z; the pair and bare classifications agree, and the quotient parameter is the stated punctured disc.',
    ['Retained full independent/rederived proofs from the November intake and 17–18 November are preserved at their recorded whole-proof scope.',
     'Current complete classification proof reviewed through the centralizer, finite affine corrections, cusp units and fan maps, translation-torsor correction and coherent 2Z action.',
     'Fresh 79-check program verifies the centralizer, finite norms and integral lattice obstruction used in the classification. Fresh original DGKX v1 opening checks the standard source family and classification conclusions, including pp.92 and 95.'],
    'No remaining mathematical gate identified in the standard-family classification. The exact source parameter is a=c+delta, delta=beta_part-beta_0; equality a=c is not assumed. Properness and Kodaira–Spencer conclusions use the named family/deformation proofs.',
    'Credited re-derivation appendix scope is explicit. Original finite vectors, fan, marking and both parameter directions are retained; root owns final layout.')

put('fam:src:A.5.2',
    'The tangent tuple is (1,1,1,0), the reduced miniversal germ is a smooth disc, and the stated coarse tangent direct images and nonzero Kodaira–Spencer generator follow from the displayed root-Koszul and cusp base-change maps.',
    ['Retained complete Fable/Astra reviews and the 18 November cusp-module/top-degree-base-change check remain evidence; they are not reset by the current targeted source review.',
     'Current full receiving proofs reread, including the root matrix, coarsening of the doubled-point quotient, normalization kernel, rank-one DVR residue and nonzero six-arrow Kodaira–Spencer class.',
     'A distinct ordinary logarithmic-ideal calculation in P5.3 gives the same tangent tuple; fresh 79-check computation verifies every coarse-degree row and incidence rank.',
     'Original DGKX v1 Theorem6.12 with proof pp.81–82 and Proposition6.16 with proof p.85 freshly read. The source proves the standard tuple and smooth reduced germ; the additional displayed direct-image formulas retain their receiving derivation.'],
    'No unresolved mathematical gate identified. The miniversal assertion does not assert a fine universal moduli object. Canonical aliases in the family and deformation records retain the same actual statement.',
    'Current statements and both complete proofs reviewed; exact source statement/page locators and a=c+delta transport are retained. Final layout belongs to root.')

put('wb:thm:retained-period-deformation',
    'The retained period family is a proper holomorphic submersion on every relatively compact parameter domain. Its exact real marking gives the displayed Beltrami graph and tangent-lift Kodaira–Spencer class, nonzero in every admissible standard member.',
    ['Retained 17–18 November complete-proof rederivations are preserved. The actual PD7–PD12 finite/cusp domains and properness maps were also fully reviewed for the new atlas and independently checked by root after reading.',
     'Direct algebra of the stated period marking: P squared equals P, the real map is A_delta zeta+B_delta conjugate(zeta), the lattice difference is delta r_gamma e_2, and inversion gives delta/(2iD+delta) P. Admissibility excludes vanishing denominator; the tangent-lift convention contributes the stated minus sign.',
     'Fresh original DGKX v1 Theorem2.24 p.20, scalar class/Lemma6.14 p.84 and Proposition6.16 p.85 read at their proper-family and deformation scopes.'],
    'No remaining mathematical gate identified for the exact standard-family deformation statement. The coefficient and sign convention of the explicit Beltrami representative remains the receiving formula, with its exact marking map, not an unproved normalization.',
    'Actual parameter domain, both real-map matrices, graph convention and all finite/cusp extension maps remain explicit. Final rendered proof not separately certified here.')

appendix = {
 'night:P5.1': ('The vertical tangent and ordinary logarithmic tangent sequence are computed by the actual xy, xyz and multiple-fibre maps; the vertical bundle and quotient retain their stated line characters.',
    'Fresh 79-check code verifies the complete local polynomial maps and all torsion-annihilator identities. Original DGKX v1 Proposition6.6 pp.77–78 and Lemma6.7 p.78, including full proofs, freshly reopened.'),
 'night:P5.2': ('The logarithmic Leray direct images and cup-product maps have the stated root/coarse degrees, with the full cusp normalization and scheme-fibre contributions.',
    'Fresh 79-check code verifies the five coarse direct-image degree rows and cusp incidence ranks. Original DGKX v1 Lemmas6.8–6.9 pp.78–79 and Proposition6.10 pp.79–80 freshly read with proofs.'),
 'night:P5.3': ('The ordinary logarithmic-ideal route yields tangent dimensions (1,1,1,0) through the exact branch-normal quotient, cusp maps and coarse-degree calculations.',
    'Fresh 79-check code checks all five degree rows, the (1,2,1) cusp normalization dimensions and rank-two conductor incidence. Original DGKX v1 Lemma6.11 p.81 and Theorem6.12 pp.81–82 freshly read with proofs.'),
 'night:P5.4': ('The actual proper family has nonzero Kodaira–Spencer map, and its one-dimensional miniversal base is a smooth reduced disc by the local-ring ideal argument.',
    'Fresh original DGKX v1 scalar cocycle and Lemma6.14 p.84 and Proposition6.16 p.85 fully read. The exact family map is a=c+delta, so tangent parameters and differences agree.'),
 'night:P5.5': ('For every admissible twist in the stated (3,4) construction, the full automorphism group is the fixed vertical C/Z subgroup, hence C*. The centralizer and all finite/cusp extension constraints are retained.',
    'Fresh 79-check program solves the full 32-equation centralizer (rank14, basis I and E41), checks actual finite norms and constructs the complete integral 14-to-28-to-20-to-8 mapping cone, proving H1=0. Original DGKX v1 Lemma6.17 p.85, Proposition6.18 pp.85–86 and Theorem7.14 p.95 are reopened at their standard-family scope.'),
 'night:P5.6': ('For each fixed admissible twist datum, the full sheaf/torsor obstruction is the nonzero order-two class, so the exact parameter equivalence is cprime-c in 2Z, with extension through every original finite and cusp chart.',
    'Fresh 79-check program computes integral H2=Z plus Z/2 from the full mapping cone using verified unimodular Smith transformations. Its five-generator presentation, primitive generator and mod-two detector identify the actual class delta1-delta2; all full matrices are saved.'),
 'night:P5.7': ('The credited source comparison identifies the original standard family by the exact map a=c+delta, inverse c=a-delta, with equal period matrices, matching half-planes and identical original finite and cusp constructions.',
    'Current full comparison proof reread. Fresh original DGKX v1 pp.4–12,18–22,77–85,92,95 opened at the precise family/cohomology/deformation/classification loci; attached v2 and the bounded source-comparison record retain their original scope.')
}
for label,(line,special) in appendix.items():
    routes = ['Retained complete November proof reviews and rederivations remain evidence at their documented scopes. Current entire receiving proof reread; no new before-reading independence is claimed.',special]
    risk = 'No remaining mathematical gate identified at the stated scope. Classical geometric and coherent-cohomology inputs remain explicit dependencies.'
    if label in ('night:P5.5','night:P5.6'):
        risk += ' The receiving statement ranges over every admissible fixed twist datum; the opened standard-family source is credited only on its exact standard specialization, not for this larger quantifier.'
    put(label,line,routes,risk,
        'This is a deliberately credited re-derivation appendix, so the full proof is retained. The unsupported blind-control sentence and absent historical-program assertions have exact guarded replacements; removed history is preserved in the patch receipt. Final integration/layout is root-owned.')

main = {
 'inv:A1.0': ('The structure-sheaf direct images and full scheme-fibre cohomology agree with the cited AC26 construction, including the nonzero cup product and fixed root characters.',
   ['Retained Fable high/max character, degree, extension and duality checks; retained Astra whole-proof rederivation of the determinant line, full fibres and cusp normalization.',
    'The opened original AC26 source is the named known input. The receiving proof is a short cited specialization; its longer derivation is retained in the credited appendix.']),
 'inv:A2.2': ('The actual residue connecting scalar is nonzero, with the specified fourth-root phase and exact beta/gamma evaluation; the displayed numerical constants lie in the certified intervals.',
   ['Retained complete modular and independent Abel-period derivations, with the exact differential and fourth-root transport.',
    'Fresh a2_scalar_arb.py uses 100 q-series terms, proved divisor-sum tails and 120-digit Arb balls; all12 checks pass, including an independent gamma evaluation and strict rational bounds for C4 and both components of K2.']),
 'inv:A2.4': ('The explicit root Kodaira–Spencer row and its residue pairing give h^{1,2}=1 with the full stated frame and normalization.',
   ['Retained whole-proof exact root-character and connecting-map review, including the row (-C,A,-D0,B), Reynolds frame and coefficient mu_s/4.',
    'The nonzero scalar is independently supported by the fresh 12-check Arb enclosure; this numerical check supplements the exact nonvanishing proof.']),
 'inv:A3.1': ('Every admissible standard sphere member has the full stated Dolbeault table; all cohomology entries and holomorphic-form vanishings follow from the specified direct images and duality.',
   ['Retained full Leray/duality entrywise rederivations, with the separate earlier parameterized Hodge/HRR route preserved at its documented scope.',
    'The evaluated h=1 scalar and exact logarithmic residue map fix the former free integer. Fresh 54-check rational models reproduce the complete column-cohomology table after that geometric input.']),
 'inv:A4.1': ('The ordinary relative modules for xy, xyz and s^m retain their exact degrees and multiplicities; the displayed xyz degree-two torsion sequence and annihilator are correct.',
   ['Retained complete local syzygy and exterior-power reviews, including degree-two torsion and faithful finite-chart descent.',
    'Fresh 79-check code verifies the actual xyz wedge row, syzygy matrix, relation matrix and all six ideal-annihilator identities; full exact matrices are saved.']),
 'inv:A4.2': ('The ordinary degree-one relative module is torsion-free but nonfree at the semistable cusp, whereas degree two has the stated nonzero double-locus torsion; the multiple-fibre support retains its exact nilpotent thickness.',
   ['Retained full local-module proof and exact original AC26 Remark9.21 p.81/Remark1.3 p.5 comparison, including the earlier visual original-PDF check.',
    'The fresh 79-check local polynomial calculation verifies the receiving maps and torsion support. The new three-step mathematical proof retains the complete faithful etale-descent argument.']),
 'inv:C1.1': ('The only nonzero Frolicher d1 maps are the four stated rank-one arrows, and E2 equals E-infinity with the S6 de Rham groups.',
   ['Retained whole-proof middle-row and bidegree derivation from the exact Dolbeault table and Betti groups.',
    'Fresh Fraction-based double-complex code directly computes induced d1 maps, total cohomology and all column groups for the receiving arrow pattern.']),
 'inv:C2.1': ('The Bott–Chern and Aeppli tables follow from the stated four-arrow pattern and endpoint dots, with the exact h-dependent multiplicities and the h=1 specialization.',
   ['Retained full double-complex derivation and earlier independent quotient-formula comparison are preserved at their recorded scopes.',
    'Fresh primary opening of Stelzig v3: Theorem3 p.7 and proof pp.8–11, Proposition6/Corollary7 p.16 and Lemma8 p.17. Bounded bidegree is sufficient, with arbitrary cardinal dimensions of cochain spaces.',
    'Fresh main_D_double_complex.py uses its own Fraction Gaussian elimination, kernels/images and induced maps, plus independent corner counts; all54 checks pass for h=0 through5. These finite instances corroborate the universal cited decomposition proof.']),
 'inv:C3.3': ('The listed Bott–Chern generators form the stated bases, and every product of positive-degree classes is zero.',
   ['Retained full nine-class basis and product review, including the explicit mixed Leibniz identity, pulled-back Chern square, injective Frolicher arrow, Serre pairing and Stokes arguments.',
    'The product proof uses the already established abstract Dolbeault classes and exact primitives; it does not require the new coefficient-atlas construction, so no new circular dependency is introduced.'])
}
for label,(line,routes) in main.items():
    put(label,line,routes,
        'No remaining mathematical gate identified from the retained complete checks and current targeted evidence. Classical source inputs remain stated dependencies; fresh code is attributed only to its executed scope.',
        'Exact source/convention scope retained. Where a known-source proof is shortened, the complete receiving specialization and its maps remain explicit. Root owns current integration and final visual/layout completion.')

put('series:I:D',
    'All Main D clauses match their full statements: the three cohomology tables, four rank-one arrows, square-zero algebra, ordinary relative modules with full multiplicity, and the complex coefficient representatives G and Q with primitive/factor-twelve normalization.',
    ['Retained complete source and receiving reviews of A1.0/A2.1–2.4/A3.1/A4.1–2/C1.1/C2.1/C3.3 support the original clauses; the three new 79/54/12-check programs independently corroborate their actual algebraic and numerical inputs.',
     'The new atlas has a complete constructive proof, separate first-jet verification, exact DGKX p.84 scalar comparison and root receiving review. Root is arranging a further statement-only receiving reconstruction, whose result is not presumed here.',
     'The five outline steps were checked clause by clause against their named full-statement targets. The product argument does not depend on the later coefficient construction.'],
    'No additional mathematical mismatch identified after correcting the local-line count. The atlas applies to the original standard family, Q is complex, and harmonic normalization retains its stated d1g ambiguity. Root owns independent receiving completion and final presentation/layout gates.',
    'One exact outline correction supplied: four local lines on the four pieces, with three overlap annuli. All table entries and bidegrees match the full statements; no whole-row completion/layout state assigned.')

# Root alone sets final row-completion and rendered-layout states.
for obj in A.values():
    obj.pop('completion_state', None)
    obj.pop('layout_check', None)
(P/'row_assessments.json').write_text(json.dumps(A,ensure_ascii=False,indent=2)+'\n')

rows=[]
def event(label,kind,outcome,event_id):
    rows.append(dict(statement_id=label,date='2026-11-19',who=who,type=kind,
                     outcome=outcome,event_id=event_id,phase='S6_SERIES_GRIND'))
for label in ['inv:A2.1','inv:A4.1','night:P5.3','night:P5.5','night:P5.6']:
    event(label,'computation or formal certificate',
      'Fresh after-reading priority_rows_exact.py, SymPy1.14.0, passes79 checks. Complete scope: universal affine-period differentiation/kernel/coarse orders; exact local wedge/syzygy/annihilator matrices; all five coarse-degree rows and cusp incidence; full centralizer and integral 14-to-28-to-20-to-8 cone with verified unimodular Smith maps. H1=0,H2=Z plus Z/2 and actual nonzero order-two obstruction. Full matrices/output saved; no historical executable replay.',
      'I-priority-exact79-'+label.replace(':','-'))
event('inv:C2.1','computation or formal certificate',
 'Fresh after-reading main_D_double_complex.py uses Python Fraction and independent Gaussian elimination, kernel/image quotients and corner counts;54 checks pass for h=0,...,5. Complete Dolbeault, BC, Aeppli, induced d1 and total-cohomology data saved. Finite instances supplement the universal written specialization, not replace it.',
 'I-mainD-double-complex54')
event('inv:A2.2','computation or formal certificate',
 'Fresh a2_scalar_arb.py with python-flint0.9.0,120-digit balls and100 q-series terms passes12 checks. Explicit divisor-sum tail majorants certify C4,ReK2,ImK2; independent gamma evaluation overlaps. All printed decimals verified at their last place and strict rational enclosures saved. No historical quadrature/Newton program replay.',
 'I-A22-fresh-Arb12')
for label in ['night:P5.1','night:P5.2','night:P5.3','night:P5.4','night:P5.5','night:P5.6','night:P5.7','fam:src:A.5.1','fam:src:A.5.2']:
    event(label,'targeted proof check',
      'Current whole receiving proof reread, retaining prior complete independent/rederived checks at their actual scope. Original DGKX v1 primary PDF freshly reopened: Prop6.6 pp77–78,Lem6.7 p78,Lems6.8–6.9 pp78–79,Prop6.10 pp79–80,Lem6.11 p81,Thm6.12 pp81–82,Lem6.14 p84,Prop6.16 p85,Lem6.17 p85,Prop6.18 pp85–86 and classification pp92,95. Exact source map a=c+delta and unchanged finite vectors/cusp fan. Broader admissible-twist P5.5/P5.6 conclusions retain their own full receiving proofs; no blind chronology claimed.',
      'I-appendix-source-full-'+label.replace(':','-'))
event('inv:C2.1','targeted proof check',
 'Original Stelzig arXiv1812.00865v3 PDF freshly obtained and read: Theorem3 p7 and complete proof pp8–11,Prop6/Cor7 p16,Lemma8 p17. Arbitrary-cardinal bounded double-complex hypothesis matches smooth forms. Exact short three-step specialization supplied, preserving arrow-table label; old403-word proof becomes228 words.',
 'I-C21-Stelzig-primary-specialization')
event('series:I:D','targeted proof check',
 'Main D full statement and five-step outline compared clause by clause with all full body targets, original standard-family hypotheses, exact module maps, cohomology tables and new complex coefficient atlas. Corrected proposed local-line count from three to four pieces; three overlap annuli unchanged. No added mathematical gate or circular atlas dependency found. Final layout/completion left to root.',
 'I-mainD-complete-scope-review')

ep=P/'events.tsv'
with ep.open(newline='') as f:
    existing=list(csv.DictReader(f,delimiter='\t'))
ids={r['event_id'] for r in existing}
added=[r for r in rows if r['event_id'] not in ids]
with ep.open('a',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome','event_id','phase'],delimiter='\t')
    w.writerows(added)

old='three local twelfth-power lines.'
new='local twelfth-power lines on the four pieces.'
front=P/'frontmatter_I.tex'
assert front.read_text().count(old)==1
patch=[dict(label='step-I-D-5',old=old,new=new,
            reason='Four actual local lines L_*,L_1,L_2,L_0; retain the three overlap annuli.')]
(P/'main_D_outline_count_patch.json').write_text(json.dumps(patch,ensure_ascii=False,indent=2)+'\n')
receipt={
 'author':who,'phase':'S6_SERIES_GRIND','new_events':len(added),
 'assessment_count':len(A),'completion_and_layout':'left unset; root-owned',
 'fresh_outputs':{str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest()
                  for f in [P/'code/priority_rows_exact.output.json',P/'code/main_D_double_complex.output.json',P/'code/a2_scalar_arb.output.json']},
 'source_PDFs':{str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest()
                for f in [P/'open_atlas/DGKX_v1_primary.pdf',P/'Stelzig_1812_00865v3.pdf']},
 'shared_body_mutated':False}
(P/'priority_assessments_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
