"""Synchronize the completed proof/source/computation checks without resetting prior reviews."""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
D = ROOT/'deliverables/work/invariants_arithmetic'
C = ROOT/'deliverables/code/invariants_arithmetic/arithmetic'
refs = {r['citation_key']:r for r in json.loads((D/'references_verified.json').read_text())}

def write_rows(name, rows):
    (D/(name+'.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    keys=list(dict.fromkeys(k for r in rows for k in r))
    with (D/(name+'.csv')).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
        for row in rows:
            w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in row.items()})

notes={
'C3.2':'Recomputed the clockwise collar Cech winding sum -p and the factor12, with standard p=-1. The working edition also states exp(12g)=f*O(1) with the positive complex orientation of the base; its optional reversed-generator clause is not a different default marking. The earlier audit note asserting an opposite gamma sign was corrected; the mathematical candidate already had the correct convention.',
'C.6.R1':'Reran exact PARI ranks (2,1,1,1,1,1,1,2,1,1,1), local torsion and Simon descent where needed. Compiled and ran the original eclib saturation program against eclib20221012; all nine rank-one points have index1, with no remaining primes. The automatic integral bounds are (1,1,1,2,2,2,3,5,5); all Tamagawa-index primes are included. The largest bound5.15488504017589 and the p=2,3,5 residue certificates (q=17,17,59) reproduce. Cremona–Siksek Theorem1 and its everywhere-good-reduction normalization were checked in the original.',
'C.6.R2':'Reran all ten 1024-bit exact-coefficient derivative sums and the CM streams at D67,d217 and D163,d185801. Both original largest configurations (384-bit,R128,cutoff170;512-bit,R96,cutoff190) reproduce, with difference3.384858105016425490223e-79. The latter covers915818441 coefficients; tail3.09321800754876143967e-78. Independently enclosed all eleven real periods by Arb E4 Fourier tails and all derivative/period ratios with conservative audited truncation and arithmetic radii; every printed ratio agrees to more than65 decimal places. Checked the Coates–Wiles hypothesis through Rubin1999 Theorem10.1 and the nonmaximal-order isogeny reduction.',
'C.6.R3':'Opened the original Gross–Zagier TheoremI.7.3 and its modularity hypotheses, Gross1991 Theorem1.3 including the Heegner condition, and Jetchev2008 Theorem1.1. The first supplies rationality of the height/period factor; a nonzero Heegner height supplies rank1 and finite Sha via Kolyvagin. The non-CM hypothesis later in Gross applies only to the subsequent alternative proof, not to Theorem1.3. Positivity and primitivity were independently rerun. No rank-two Sha conclusion is asserted.',
'C.6.R4':'Reran the original exact Bezout/coarse-height Arb certificates. Opened Miller2011 Definition1.1, Theorem1.2 and its full finite exception list; conductors3136,3136,361 satisfy the theorem and are not exceptions. The intervals isolate the exact BSD quotient1 and hence q=4 for i=3,5,7; only these three cases are asserted to have trivial Sha.',
'C.6.R5':'All twelve omitted interval inputs were regenerated using the original unmodified directed-rounding MPFR C++ generator, exact GP coefficients for rows2,4 and CM theta coefficients for6,9,10,11. The original B_C6_exact_factors.py verifier now passes all six rows: q=(8,32,8,16,16,576), auxiliary ratios(64,64,8,16,400,64), denominator bounds(256,256,32,64,1600,256). Exact GP twist/conductor/Heegner/torsion and coefficient/Sturm tests reran. Opened Cai–Shu–Tian Theorem1.1, YZZ Section7.1.1 (field-degree/pairing factor4), BBPR printed p.102 (degree59368,Manin1) and Stein Theorem9.18. This proves exact analytic factors, not actual Sha order9 for the last curve.',
'C.7.5':'Regenerated PARI high-precision heights and periods with the supplied C_cm_250.gp mathematics, reran all eleven independent theta calculations and the specified logarithmic PSLQ lists, and reran all66 polynomial PSLQ calls for N and N^12. Every theta/height identity agrees beyond245 digits and every prescribed PSLQ call returns None. Null returns are algorithm outputs, not exhaustive bounded-degree polynomial exclusion certificates and not transcendence proofs.',
'C.7.11':'Re-derived the paired rank-four lattice, first-jet cancellation, transcendental second jet and function-field degree3. Visually checked Waldschmidt1975 Theorem1 p.24 and its full inequality (d-1)ell>sum rho+2d(n-1)(lambda+1); proposed values would require8>12+6lambda, while actual packing requires lambda>=1. Opened Schneider–Lang, Xie, Noguchi and Bost original hypotheses. The statement proves failure of these specified criteria and retains the unconditional norm question.',
'C.7.12':'Re-derived division-norm algebraicity propagation, real/complex degree envelopes, uniform height bounds, torsion limits and the translate transcendence-degree cap3. Visually checked GMW Theorem2.1 pp.101–102, including joint degree and monotonicity hypotheses; opened Herblot6.1, Gasbarri4.16/LG definition, Mahler1.1, entropy5.1 and the original period-refined rank theorems. The supplied estimates fail the sufficient inequalities; this does not establish degree lower bounds or impossibility of every interpolation route. The germ has a transcendental slope, and the available rank2 is permitted by the rank bound3.',
}
rows=json.loads((D/'result_audit.json').read_text())
for r in rows:
    sid=r['source_id']
    if sid in notes:r['own_check']['details']=notes[sid]
    if sid not in ['C3.8','C.7.4']:
        r['own_check']['proof_outcome']='complete proof rederived; operative original-source dependencies checked; applicable mathematical computations reproduced'
    p=ROOT/'deliverables'/r['candidate_file']
    r['own_check']['candidate_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
    r['reference_evidence']=[{'citation_key':k,'status':refs[k]['status'],'opened_locator':refs[k]['opened_locator']} for k in r.get('reference_dependencies',[]) if k in refs]
    r['reference_record_file']='work/invariants_arithmetic/references_verified.json'
    if sid.startswith('C.6.R') or sid=='C.7.5':
        r['numerical_evidence_manifest']='code/invariants_arithmetic/arithmetic/writing_complete_computations.json'
    if sid=='C.6.R2':
        r['numerical_or_code_locators']+=['code/invariants_arithmetic/certify_period_derivative_table.py','code/invariants_arithmetic/arithmetic/records/writing_period_derivative_certificate.json']
write_rows('result_audit',rows)

wbnotes={
'prop:workbench-holomorphic-form-vanishing':'Checked the full period-column proof: a fibrewise holomorphic form has constant period coefficients and the moving columns force vanishing; at the cusp the residue condition divides out the logarithmic pole. Degree1/2/3 cases and the cubic weight O(-1) are treated. This is a distinct direct proof of the known AC26 holomorphic-form vanishing, retained beside the INV direct-image proof.',
'thm:parametric-hodge-diamond':'Recomputed HRR with c1=c2=0 and c3=2, h0q=(1,1,0,0), holomorphic-form vanishing and Serre duality. The result has h11=h22=m+1,h12=h21=m; it is an earlier parameterized derivation, not an open numerical value after INV A2.4 fixes m=1.',
'thm:frolicher-e2-candidate':'Checked all bidegree possibilities for d_r,r>=2 and exactness of the two middle E1 rows from b1,...,b5=0. Ranks(1,m),(m,1) and E2=Einf are correct, independent of evaluating m.',
'prop:period-derivative-determinant':'Read the global degree proof in full: K=6mu_prime^2-tau_prime beta_prime, nonzero cusp limit, root-character vanishing and the degree2 determinant force orders2,0. This is genuinely distinct from the modular-identity calculation of INV A2.1 and must be retained.',
'prop:log-relative-direct-images':'Checked the equivariant tensor-lattice bases, coarse t=s^M powers, four filtration degrees0,-1,-1,0 and splitting Ext groups. Reynolds invariants are base-linear and retain full nonreduced scheme-fibre base change. The dual lattice is not silently identified with the dual of the direct-image lattice. This filtration proof is distinct from INV upper modifications/duality.',
'prop:log-ks-divisor':'Recomputed kappa0 and kappa1 in invariant frames: kappa1 row(-C,A,-D,B), and kappa0 matrix(A,tB;C,D) at finite centres. Coarse determinant has exactly the two simple zeros and the cusp B0 t factor is a unit in its logarithmic frame. No local symmetry alone is used to claim mu_prime(z2) nonzero.',
'prop:absolute-cotangent-direct-images':'Checked the complete residue long exact sequence, finite skyscraper cancellation, cusp normalization quotient and extension splitting. The ordinary cotangent direct images are O(-2),O+O(-1)^2,O+O(-1); the proof depends on the separately established nonzero scalar, not on the conclusion it is proving.',
'hodge_frolicher:remark:8':'Recomputed the whole degree-one local-module and residue calculation, including cusp quotient generators q1=(-1,0,1),q2=(0,-1,-1), signed boundary row(0,1,-1,0), finite torsion R/(s^(M-1))ds and the explicit kernel bases. Reopened and visually checked the actual AC26 PDF p.81: Remark9.21 explicitly asserts degree-one torsion also on W, so the workbench refutes that original sentence, not merely a transcription. Remark1.3 p.5 speaks of Omega^p and needs qualification by degree because Omega² has nonzero cusp torsion. The complete local proof remains valid.',
'thm:h12-scalar':'Checked the normalized section h=(a,1), a(z2)=1/2, u2(0)=1, and scalar kappa1(h tensor gamma)=-mu_s/4. Global degree ensures nonzero mu_s; INV additionally supplies its independent Gamma-value evaluation. The finite scheme-fibre character and sign are preserved.',
'cor:exact-hodge-diamond':'Recomputed every Leray cohomology group from the complete direct-image list and its Serre dual; exact diamond agrees with INV A3.1. Retain the earlier proof after aliasing the repeated theorem statement.',
'thm:exact-bott-chern-aeppli':'Opened McHugh Theorem6.3, Proposition6.4 and Section7.1, and Angella Section4; verified the substitutions. The needed statement is that de Rham representatives surject onto K^(p,q), hence k<=b, not a generally false injection of Bott–Chern into de Rham. Recomputed the full BC/A tables and Schweitzer duality; distinct from the double-complex decomposition proof.',
'record:h12-direct-images':'Historical audit/provenance record only. Its once-outstanding independent replication is supplied by the full INV A1–A2 recalculation and the present source-to-source check. Do not promote absence of a human review to an unresolved mathematical hypothesis.',
'lem:bcpr-degree-one-input':'Checked monodromy-invariant primitive gamma, its nonzero image in R1 f_*O, coherent Leray and exact marked-fibre Gamma formula. The generator agrees with the positive factor12 convention; AC26 already supplies the underlying structure-sheaf cohomology.',
'lem:bcpr-eta-extension':'Checked the full finite/cusp class extension using invariant bases, logarithmic cusp forms modulo dlog t, zero Higgs image and ker(kappa1)=R1 f_*Omega1. The Leray edge surjects and yields a global Dolbeault class Q modulo d1g. This proves existence and the restriction class, not an evaluated coefficient atlas.',
'rem:bcpr-literal-gauge':'Read as the exact scope boundary: coherent Leray specifies classes and restriction data, not a unique smooth gauge or literal coefficient functions. This maps to INV C3.8; its underlying existence is proved.',
'prop:bcpr-generators-are-bases':'Rechecked the nine positive-degree classes, nonzero fibre trace and Serre pairings, d1 injectivity/surjectivity and all dimension comparisons. The natural BC-to-Dolbeault map in(3,2) is justified rather than assumed globally injective.',
'thm:bcpr-square-zero-algebra':'Checked every possible bidegree product. Leibniz gives AB=0 and A²+B²=0; injectivity of d1 on H^(1,2) supplies the required primitive for A². AC vanishes by the trace pairing; all top-degree products vanish by d-exactness and Stokes. No literal coefficient atlas is needed for the algebra calculation.',
'rem:bcpr-global-gauge-boundary':'Historical precise distinction between the proved global classes/products and the unevaluated finite coefficient atlas. Retain as source provenance or merge with INV C3.8; it is not a second unresolved invariant.',
'formula:bcpr-fibre-representatives':'Recomputed x_gamma=(y Im zeta2-m Im zeta1)/(y Delta), x_u=(r Im zeta1-6m Im zeta2)/(y Delta), their (0,1) derivatives Gamma,U, Q_F=-dzeta1 wedge U-6 dzeta2 wedge Gamma, Q_F Gamma coefficient1/(4y Delta), Q_F² coefficient3/(y Delta). Since y Delta<0, complex and marking orientations are opposite and the complex integral is -12. Preserve the complete coordinate derivation.',
'formula:bcpr-factor-twelve-chern':'Checked the exponential/Leray/transgression comparison and unitary connection d-2pi i(zG+bar(z)bar(G)). The main convention is exp(12g)=f*O(1), the same as INV C3.2. Reversing the base generator reverses both signs together. The real Chern map is zA+bar(z)B and is an isomorphism of real vector spaces.',
'lem:hodge-line-audit':'Checked canonical modular factor E4² sqrt(E6)/Delta and finite characters. The evaluation order is M-1-a; invariant direct-image frame and actual canonical section must be distinguished. Cusp logarithmic base contributes exactly the degree yielding f_*omega_f=O(1). Distinct canonical-form proof retained.',
'lem:finite-normal-order-audit':'Recomputed the exact normal character of the cyclic covering and proved its order is M, using constancy of a holomorphic unit on the compact torus. This is a separate dependency even when its conclusion is included in the shared finite-filling theorem.',
'lem:cusp-structure-sheaf-audit':'Read the complete normalization and conductor resolution: C -> C³ -> C², rank1 boundary row(1,-1,1), hence hq(O_W)=(1,2,1). The degree2 class is the kernel of normalization pullback; the cup product is nonzero by intrinsic nearby-cycle calculation. This is a distinct proof from the later explicit Alexander–Whitney construction.',
'thm:structure-direct-images-audit':'Checked all smooth, finite multiple scheme-fibre and cusp dimensions, local freeness and canonical base-change maps. Gamma spans a saturated trivial subline, relative duality determines determinant O(-1), and H1(O(1))=0 splits R1=O+O(-1). The complete proof is preserved as a known-source duplicate of AC26 Proposition9.13 and INV A1.0.',
'cor:picard-line-audit':'Checked the exponential exact sequence with H1(X,Z)=H2(X,Z)=0 and H1(O)=C, then the fibrewise injection, including both nonreduced finite fibres and the cusp. Exact AC26 Theorem10.5(b) credit is retained.',
'thm:uniform-nontorsion-audit':'Read the complete countability proof. A relation c tau+d mu-b can vanish identically only when all coefficients vanish. For every integral class outside Q gamma its zeros are discrete; the countable union of exceptional fibres is countable. The remaining rank1 fibres exclude real Picard parameters; exceptional rank2 fibres contribute only countably many more bad parameters. Injectivity on full scheme fibres and the exact finite normal orders handle reduced S1,S2. This is known AC26 Proposition10.8, with a distinct expanded proof.',
'analytic_picard:remark:7':'Provenance remark, not an additional theorem. Its claims are mapped to the preceding direct-image, Picard and non-torsion results; the source-status vocabulary is not counted as an independent correctness review.',
}
wb=json.loads((D/'working_edition_inventory.json').read_text())
for r in wb:
    sid=r['source_id'];assert sid in wbnotes,sid
    p=ROOT/'sources'/r['source_file']
    block=(D/r['extracted_file'].split('work/invariants_arithmetic/',1)[1]).read_text()
    r['own_check']={'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17',
                    'proof_read':'entire source statement and all associated proof paragraphs',
                    'details':wbnotes[sid], 'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                    'proof_block_sha256':hashlib.sha256(block.encode()).hexdigest(),
                    'candidate_comparison':'Compared the entire extracted proof against the corresponding INV candidate and retained every genuinely distinct proof method; root owns the final combined working-edition appendix and statement aliases.'}
    r['check_outcome']='verified complete proof; duplicate statement/credit mapping retained'
    if 'gauge' in sid:r['check_outcome']='proved existence and precise unresolved coefficient-atlas boundary'
    if sid in ['record:h12-direct-images','analytic_picard:remark:7']:r['check_outcome']='historical provenance; no additional mathematical assertion'
    if sid=='hodge_frolicher:remark:8':r['check_outcome']='local proof verified; exact degree-one error in original AC26 Remark9.21 confirmed visually'
    section='§1.2 and §§2.B-9/B-10' if r['source_file'].endswith('analytic_picard.tex') else ('§1.5 and §§2.B-1/B-2/B-4' if r['source_file'].endswith('hodge_frolicher.tex') else '§1.6 and §2.B-3')
    r['recorded_checks']=[{'reviewer':'Claude Fable 5.2','effort':'Not separately stated for Reader B; aggregate survey identifies high effort.','date':'2026-11-12','locator':'sources/survey_20261112/work/B_notes.md, '+section,
                          'scope':'Source reading and scoped first assessment; its explicitly unrecomputed geometric steps are not represented as a full independent proof check.'},
                         {'reviewer':'Unidentified internal AI reviewers','effort':'not recorded','date':'2026-08-27' if 'hodge_frolicher' in r['source_file'] else ('2026-08-26' if 'analytic_picard' in r['source_file'] else '2026-08-30 through 2026-09-04'),
                          'locator':'sources/overleaf_working_edition/supporting_materials/workbench/research/ledgers/claim_ledger.txt, S6-HODGE-H1/S6-HODGE-BCA/S6-OPEN-HODGE-REPRESENTATIVES/S6-CDP-10.8 as applicable',
                          'scope':'Historical ledger reports internal audits but does not preserve full model/effort metadata for them. No identity or correctness check is inferred from a VERIFIED badge.'}]
    r['reference_dependencies']=list(dict.fromkeys(k.strip() for x in re.findall(r'\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}',block) for k in x.split(',')))
    r['source_credit']='Compare exact AC26 original-PDF locators and modern-source exclusions in work/invariants_arithmetic/source_credit_map.json and references_verified.json; attribution notes above control.'
write_rows('working_edition_inventory',wb)
print('updated',len(rows),'run results and',len(wb),'working-edition rows')
