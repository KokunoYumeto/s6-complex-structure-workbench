from pathlib import Path
import json,csv,re,hashlib
ROOT=Path(__file__).resolve().parents[3]; D=ROOT/'deliverables/work/invariants_arithmetic'
notes={}
def add(prefix,text):
 for line in text.strip().splitlines():
  key,value=line.split('|',1);notes[prefix+key]=value
add('INV ',r'''
A1.0|Re-derived root Picard group and determinant line Q^12=O(-p0), hence Q=R^-1. Checked finite characters (1,zeta^-a), full scheme-fibre dimensions, cusp normalization resolution and nonzero cup product. Original structure-sheaf result also occurs in AC26 Proposition 9.13.
A1.1|Checked each t=x,xy,xyz,s^m chart, the direct-summand logarithmic base form, nonzero vertical logarithmic vector, and det E=omega_f(-2S1-3S2).
A1.2|Recomputed upper modification exponents for (m,a)=(3,2),(4,1), duality on full Gorenstein scheme fibres, vanishing of connecting maps on dense open and extension groups H1(O(-1),O,O(1)).
A1.3|Recomputed kappa0 cokernel at both finite centres, kappa1 global rank, residue skyscraper cancellation and all six direct images. Dependence on A2.1-A2.4 is explicit and noncircular.
A2.1|Re-derived modular determinant identity and weight/constant normalization; checked local orders 2,0 on root coordinates and coarse degeneracy divisor p1+p2. Exact source calculations rerun.
A2.2|Checked determinant and independent Abel-integral derivations of mu_s(0)=4i sqrt(pi)/(3^(3/4)Gamma(1/4)^2), including fourth-root sign; exact/numerical source calculations rerun.
A2.3|Checked Shioda height 1/6, primitivity of section, division-polynomial identity and order-two residual at rho. Opened Duke-Imamoglu Theorem 1 and Eichler-Zagier original formula; matched mu=1-z0 branch, not its complement.
A2.4|Computed kappa1 row (-C,A,-D0,B), local simple-zero units, scalar -mu_s/4 and eta annihilation; global rank exactly one. Original symbolic and sign checks rerun.
A3.1|Recomputed every Leray contribution and Serre duality entry from six direct images; h11=h22=2,h12=h21=1. Checked dependence on nonzero A2.4 scalar.
A3.2|Checked associated-graded generators, fibre trace pairings, base Cech class and surjective edge map yielding global Dolbeault lift Q; literal chosen representative is not unique.
A4.1|Re-derived local syzygies for xy,xyz,s^m. Degree-one cusp module is torsion-free but not locally free; degree-two cusp torsion and finite multiple-fibre torsion follow from explicit annihilators.
A4.2|Compared original attached AC26 PDF Remark 1.3 p.5 and Remark 9.21 p.81 visually and as text. Correction concerns relative differential torsion, not a change to AC26 Hodge computation.
B1.0|Rechecked exact marking matrices and theta quotient. Corrected source reversed-meridian Q to family P_mark via explicit Q=P_mark S, det S=1; reference lambda0=1 yields u=w^2. Source Q is not used interchangeably with P_mark.
B1.1|Checked cyclic base-change invariant exponents, translation action on fibre cohomology, cusp dlog base term and dense-open equality of connecting maps. Covers all stated admissible k,l.
B1.2|Checked residue direct-image calculation for finite bielliptic reductions and one-component cusp; unchanged logarithmic data yields same Hodge diamond.
B2.1|Recomputed finite canonical evaluation orders m-1-a and K=f*O(-1)+(k-1)S1+(3l-1)S2. h0q and hp0 deductions follow by direct images and negative degree.
B2.2|Re-derived all floor functions and weighted Veronese degree d=4l+3k-kl; checked d=0 exclusion under stated coprimality and every requested small pair. Exact source script rerun.
B3.1|Checked central presentation, Smith determinant p, fibre-surjectivity and connected cover fibres; gcd(n,12)=1 maintains finite fillings while cusp cycle has n components.
B3.2|Checked extra C_(p0)^(n-1) residue term, dual torsion contribution and resulting h11=n+1,h12=1; no ordinary-fibre local-freeness assertion is made for torsion direct images.
B3.3|Re-derived Mayer-Vietoris ranks, collapsing flow estimates, relative torus boundaries and attaching determinant -p/2. Exact topology script rerun. Canonical/ring statements checked under connected cover; E2 degeneration from resulting Betti/Hodge data.
C1.1|Checked every possible higher Frolicher differential vanishes by bidegree, and exactness/ranks of middle E1 rows using Betti vanishing. This is a specialization of general double-complex facts.
C1.2|Checked algebraic bases for every d1 map and geometric representatives g,q,gq,q^2 using nonzero trace pairings; source double-complex calculation rerun.
C2.1|Applied bounded-double-complex structure theorem with arbitrary cardinal square multiplicities; verified only dots and length-two zigzags survive and recounted BC/A dimensions.
C2.2|Opened McHugh original source Theorem 6.3, Proposition 6.4, equation for hBC22 and Section 7.1; opened Angella Section 4. Substituted h02=h20=0, b1=b2=0, E2^31=0 and all k^{p,q}=0 to recover the same table.
C3.1|Checked real-linear Chern map zA+bar(z)B injectivity and surjectivity, Green-operator representative, maximum-principle nontriviality and exp(G0)=f*O(1). All conventions explicit.
C3.2|Recomputed clockwise collar Cech winding sum -p and factor 12, with standard p=-1. Separate working-edition gamma uses opposite sign and must be transported, not identified.
C3.3|Checked all products by bidegree and Leibniz identities, then injectivity of d1 for the remaining A^2 primitive and Stokes for the top product. Square-zero ideal proved without a coefficient atlas.
C3.4|Recomputed all seven Delta values and distinguished degreewise BC/de Rham comparison from weaker d-exact ddbar statements.
C3.5|Checked positive exact pullback curvature obstruction, Stokes pairing with closed positive (2,2) forms, and b1=b2 implications for each listed Hermitian metric class.
C3.6|Opened Gauduchon original Theorem 2 and STW Theorem 1.3. Matched compact complex threefold, Gauduchon Aeppli class and prescribed real c1BC representative; c1BC nonzero excludes Ricci flatness.
C3.7|Recomputed invariant fibre form eta^2=-12, image of real Aeppli classes and averaged positive-form contradiction; in complex dimension three the stated astheno-Kahler condition equals SKT.
C3.8|The operator existence statements are proved; a finite evaluated local coefficient atlas remains unresolved. This is retained explicitly as a question, not advertised as a completed representative calculation.
D1.1|Checked all integer residue classes and weighted Cech monomials for rho_*O(n); source exact enumeration n=-240,...,240 rerun.
D1.2|Re-derived actual root lift and logarithmic tangent sequence, E=O+O(-1), horizontal O(-5), full root-fibre cohomology and cusp normal quotient.
D1.3|Recomputed KS matrices, delta0/delta1, length-two root torsion at p1, coarse invariants and normal-quotient residue. Obtained (1,1,1,0); source Koszul code rerun. Known DGKX v1 theorem, re-derived here.
D2.1|Computed actual c-gluing derivative, sign and generator xi tensor gamma; nonzero at every admissible point. Known DGKX v1 Kodaira-Spencer conclusion, with explicit cocycle retained.
D3.1|Checked that actual one-parameter family with isomorphic tangent map kills the Kuranishi ideal including nilpotents; no inference from dimension alone. Known DGKX v1 smooth reduced Kuranishi line.
D4.1|Checked all integral root-weight cases, p1 torsion invariant epsilon_n and displayed direct-image/cohomology formula; exact script rerun.
D4.2|Checked nonintegral cusp character (e^(2pi iz),1) acyclicity and normal quotient C{q}/(q), plus countable-exception argument. No claim of uniform vanishing at all nonintegral twists.
D4.3|Re-derived resonance equations q tau+r mu=p, z=n-6qmu-r beta and Im z=-rD. Checked special lattices and t=32/5 nonintegral regular jump by exact division polynomial.
D4.4|Re-derived Fourier-mode contraction, equivariant Koszul reduction and tangent extension perturbation; computed regular lengths 2,2 and finite invariant lengths. All source exact stalk scripts rerun.
D4.5|Checked finite coherent support for each fixed nonintegral z and sum J=2N+ell1+ell2, yielding h=(0,J,1+J,0). Combined with integral formula exhausts Picard twists.
''')
add('ARI ',r'''
C.1.1|Re-derived zero-mean Green distribution and local logarithmic constant for every complex isogeny; kernel product follows by taking limit at zero.
C.1.2|Checked exact phases and beta values at rho and i with lattice actions. Corrected explanatory phrase at y=T from a pole to another half-period zero; numerical and exact values unchanged.
C.1.3|Reran original independent 110-digit special-value program; all stated comparisons pass.
C.2.1|Recomputed q1=-w^2/48^3, q2=iw/216 and q1=27q2^2/64; natural boundary uses dense rational cusps of j, distinguished from admissible-family radius.
C.2.2|Checked affine reflection matrix/cocycles, Cech vanishing for global extension and involution square normalization; original exact reflection program rerun. Overlaps FAM B.4.2 and MAPS real-form statements.
C.3.1|Re-derived theta heat/Ramanujan expansions through the stated orders at i, including h^2=2i delta/(3pi)+delta^2/(3pi) and leading strict norm term; original symbolic/numerical expansion check rerun.
C.3.2|Re-derived rho coefficient 3p/(16pi^2), t~ip^2 delta^3/pi^3, Re(t) coefficient 7/192 and |t|^(4/3) term; hence neither maximum nor minimum.
C.4.1|Opened Shin original definition, Remark 2.2 and Proposition 2.3(ii),(iii); matched Siegel product, multipliers, modular-unit power and mean-zero local-height normalization.
C.4.2|Re-derived divisor and leading coefficient of sigma division function, constant via harmonic comparison, and torsion n+/-1 formula; exact division source checks rerun.
C.4.3|Checked nonzero division polynomials, formal-group multiplicities, resultant support and radical field with positive real root choices; original relation program rerun.
C.4.4|Reran exact division recurrences, squarefree factors F4,...,F8 and all 13 finite roots through order eight.
C.4.5|Reran independent analytic root/norm checks; these certify the reported numerical comparisons and do not establish transcendence.
C.5.1|Opened BCS Theorem 4.15(a) (all CM orders over Q(j)) and Sutherland Theorem 20.12/Corollary 20.13. Matched Olson torsion list, excluded n=4,6 by nonintegral j, and checked completed t=0,1 exceptions.
C.6.1|Checked degree-one canonical height normalization, product formula weights, finite local multiplication formula and algebraicity of the finite factor A.
C.6.2|Checked nonsingular-reduction identity-component test, valuation signs and division-function correction, including primes 2 and 3.
C.6.3|Original PARI minimal-model and exact local-height programs rerun for all eleven CM rows; all models, point changes, discriminants, component orders and finite local factors reproduce.
C.6.4|Checked generic height 1/12 and divisor infinity/12 by fibre corrections; opened DeMarco-Mavraki original Theorem 1.1/Corollary 1.2 and Section 2 normalization. Maximum reformulation is conditional only on the already proved analytic maximum.
C.6.5|Reran original 1152-bit Arb enclosure with 350 Fourier terms for all eleven fibres. All endpoint signs, tail inequalities, global-height comparisons and width <1e-236 pass.
C.6.R1|Original PARI exact descent rerun for all eleven rows, reproducing ranks 2,1,1,1,1,1,1,2,1,1,1. Automatic eclib saturation and its index bound are a separate dependency currently being rerun; proof of primitivity checked against the stated bound/residue argument.
C.6.R2|Original PARI analytic-rank and period calculations rerun for rows 1-10; exact rank/root-number and CM coefficient comparison rerun. Full long MPFR stream and printed fifty-digit central derivative accuracy are separate checks still in progress, not inferred from PARI decimals.
C.6.R3|Checked implication from positive simple derivative and modularity through Gross-Zagier/Kolyvagin, rationality under period normalization, and primitive point substitution; external theorem statements still undergoing original-source verification.
C.6.R4|Reran original exact Bezout/coarse-height Arb certificate for all three rows; each interval isolates integer one after the stated BSD theorem. Miller Theorem 1.2 and exact exception list are an external source check in progress.
C.6.R5|Re-derived genus-character denominator argument and normalization; exact PARI twist identities, conductors, Heegner splitting, torsion and CM/Sturm coefficient audits all rerun. Original bundle omitted central/derivative interval inputs; regenerating all twelve with unmodified directed-rounding C++ generator. Do not treat a saved JSON conclusion as a rerun.
C.6.T1|Original PARI model, Tate reduction, rational rank/torsion, local-height, modular-symbol and derivative programs rerun; order four and finite sum log10/12 reproduce.
C.6.T2|Original PARI number-field model/local-height and deterministic Sage/Simon descent rerun, with bnfcertify=1 and quotient indices 2,4 giving rank one. Exact order six and weighted finite sum log11/12 reproduce; number-field L derivative also rerun.
C.8.1|Re-derived Poisson Gaussian maximum, convex F endpoints, eta error and cusp wp exclusion. Checked scalar rational bounds via specified Taylor majorants and reran independent diagnostics.
C.8.2|Checked theta polydisc estimates, all derivative constants, Rouche inequality, |delta|<7|h|^2 and quartic error C<150. Strict local maximum follows with explicit radius 1/50.
C.8.3|Checked lower bound on E6 boundary, Delta upper bound and two Rouche applications; these prove actual coverage of t-disc, not only a boundary inequality.
C.8.4|Reran exact duplication ladder polynomial program, re-derived all constants and all-k removable limit, and checked positive A3 lower bound on 1/28 disc.
C.8.5|Checked each of the three annular inequalities and residual local disc, including exclusion of division-polynomial zeros. Entire proof preserved as alternative to interval-grid proof; maximum statement merged with FAM C.2.3/PUSH E.4.3.
C.8.6|Re-derived logarithmic-divisor mean identities and pushforward Jacobian 2/(A|4x^3-g2x-g3|); checked u=1/wp density and all constants in equivalent maximum formulations.
C.8.7|Re-derived complex beta integral via positive Gaussian double integral and Tonelli, differentiation strip and digamma duplication/triplication values.
C.8.8|Recomputed Fourier coefficients for four half-period Gaussian translates minus twice the lattice sum; sign is + when both indices even and - otherwise; theta series has identical coefficients.
C.8.9|Re-derived dd^c normalization, db wedge da sign, both elliptic density coefficients and cusp logarithmic mass 1/12. Integrable residual densities imply no atoms in m_P.
C.8.10|Opened DeMarco-Mavraki precise small-height equidistribution theorem and matched all hypotheses. Re-derived normalization 12m_P, O(1) singular/local multiplicities and orbit-to-full-divisor passage.
C.8.11|Re-derived both first-derivative identities, determinant square and theta-heat reduction with correct Wirtinger factor 1/2. Half-period chart treated without division by zero.
C.8.12|Re-derived (t-1)L_t=X(X-2)/24 and ray derivative, plus X(0)=1/4 and X(1)=0 from previous expansions.
C.8.13|Checked cusp Cauchy bounds |q|<1/6600 and auxiliary radius 1/2000, all numerical rational constants and final |F|<17/20.
C.8.14|Re-derived Cayley/Ramanujan ODE, holomorphic cancellation at z=-z0 and formula for F. Checked Cauchy tails and scalar Bernstein reduction. Original flint exact-rational certificate and independent Fraction port both pass, as do scalar/identity programs.
C.8.15|Checked fundamental-domain coverage by cusp and Cayley discs, all critical-factor exceptions, strict ray monotonicity and uniform cusp limit. Retain as stronger theorem giving star-shaped Jordan level curves; no interval-grid hypothesis used.
C.7.1|Checked sigma normalization, third-kind algebraic differential, quasi-periods and relative period modulo algebraic logarithms; algebraic/real normalizations distinguished.
C.7.2|Re-derived compact-character real linear form and its kernel dimension, algebraic compact-lift equivalence and rectangular real formula.
C.7.3|Opened Bertolin et al. Construction 3.4/Lemma 3.5; re-derived diagonal positive bracket, CM/non-CM reductive dimensions and conjugate-pair/isogeny cases. Field of definition and algebraically closed base hypotheses matched.
C.7.4|Checked period-conjectural argument, algebraic compact lift, positive central bracket and codimension-one period relation; result remains explicitly conditional on the stated period conjecture.
C.7.5|Numerical claim only. Original 250-digit PARI period/height input regenerated; theta and PSLQ programs being rerun at stated precision and bounds. Null PSLQ return is not a proof of transcendence.
C.7.6|Re-derived squared CM multiplication rational function, degree and Laurent comparison giving algebraic s2; retained unsquared branch distinction and alpha=1+i example.
C.7.7|Opened Waldschmidt sigma theorem and Huber-Wustholz analytic subgroup theorem. Checked duplication specialization and nonsplitting of universal vector extension after isogeny. Printed theorem deliberately excludes the unverified unrestricted theta-lift criterion and the norm.
C.7.8|Checked ordinary p=5 example and separation of p-adic/nonarchimedean height from real exponential. Rubin Appendix A hypotheses still undergoing original-source verification.
C.7.9|Re-derived End(G_Q)=Z from extension class and isogeny argument, exact E361 doubling/norm relations, transcendental compact slope via AST, and why functional graph transcendence does not settle pointwise norm algebraicity.
C.7.10|Original exact PARI degree-nine CM map/kernel witness rerun: zero polynomial residuals, coprime/squarefree factors, s2=-2,a=-21beta/703,r2=-165/74+1839beta/1406. Analytic 110-digit residuals ~1e-114. Re-derived End_Q=Q(beta), eigencoordinate and projector obstruction.
C.7.11|Checked paired rank-four lattice, cancellation of first jet and transcendental second jet, function-field degree three and failure of strict numerical Waldschmidt criterion. Primary criterion source still undergoing original scan check.
C.7.12|Re-derived division-norm algebraicity propagation, real/complex polynomial degree envelopes, uniform height bounds, torsion limits and translate trdeg cap. Explicitly proves only insufficiency of these envelopes for the cited criteria, not impossibility of all approaches; original criterion sources still undergoing checks.
''')
rows=json.loads((D/'result_audit.json').read_text())
full_intake=set('A1.3 A2.1 A2.2 A2.4 A3.1 C1.1 C3.3 B2.1 B3.2'.split())
partial={'A2.3':'opening only','C2.1':'statement and first half of proof; BC/A arrows recounted','B3.3':'statement and first half of proof'}
for row in rows:
 inv=row['source_run']=='S6_01_INVARIANTS';ident=('INV ' if inv else 'ARI ')+row['source_id'];proof=ROOT/'deliverables'/row['source_proof_file'];candidate=ROOT/'deliverables'/row['candidate_file']
 row['own_check']={'checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','proof_read':'whole source statement and complete proof','proof_outcome':'rederived; external and computational dependencies tracked separately','details':notes[ident],'candidate_comparison':'Full source text retained with namespaced labels and explicit changes in corrections.json; no proof substituted by a pointer.','candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest()}
 if ident=='INV C3.8':row['own_check']['proof_outcome']='operator formulas proved; exact unresolved coefficient-atlas claim isolated'
 if ident=='ARI C.7.4':row['own_check']['proof_outcome']='conditional theorem; period conjecture not asserted'
 checks=[]
 if inv and row['source_id'] in full_intake|set(partial):
  checks.append({'reviewer':'Claude Fable 5.2 (Anthropic)','effort':'high','date':'2026-11-16 13:58 UTC','locator':'sources/reviews/S6_FINAL_INTAKE_20261116/INTAKE_S6_01.md, opening scope and §2','scope':'complete proof and explicit checks' if row['source_id'] in full_intake else partial[row['source_id']],'outcome':'holds in stated checked scope; not an all-results review'})
 if inv and row['source_id'] in ['A1.0','A1.1','A1.2','A1.3']:
  checks.append({'reviewer':'Claude Fable 5.2 (Anthropic)','effort':'max','date':'2026-11-16 14:25 UTC','locator':'sources/reviews/S6_FINAL_INTAKE_20261116/READING_S6_01_A1.md, full file; source lines 1-302','scope':'full A1.0-A1.3 reading; independent character, degree, extension and duality checks','outcome':'holds; A1.3 depends on scalar/map checks read by intake reviewer'})
 if not inv and row['source_id']=='C.8.5':
  checks.append({'reviewer':'Claude Fable 5.2 (Anthropic)','effort':'high','date':'2026-11-15','locator':'sources/reviews/S6_INTAKE_CHECKPOINTS_20261115/INTAKE_S6_05_FINAL.md, opening scope and §1 row C.8','scope':'full C.8.5 proof and every displayed inequality; C.8.1-C.8.3 not read line by line','outcome':'inequalities hold; input lemmas still needed their separate writing-run checks'})
 row['recorded_checks']=checks
 row['recorded_check_absence']='No other independent correctness review located for this exact full proof; source self-checks are recorded as proof evidence.' if not checks else ''
 text=proof.read_text();row['reference_dependencies']=sorted(set(k.strip() for m in re.finditer(r'\\cite\w*\*?(?:\[[^\]]*\]){0,2}\{([^}]*)\}',text) for k in m[1].split(',')))
 row['numerical_or_code_locators']=sorted(set(re.findall(r'(?:code|outputs|records)/[A-Za-z0-9_./-]+',text)))
 if ident in ['INV D1.3','INV D2.1','INV D3.1']:row['taken_over_by']='FAM A.5.2 (shared statement; full INV proof retained)';row['credit_checks']=[{'source':'DGKX v1','locator':'Theorem 1.3; §6 Theorem 6.12, Corollary 6.13, Proposition 6.16','outcome':'known statement, re-derived; supplied v2 omits these deformation theorems'}]
 if ident=='ARI C.8.5':row['taken_over_by']='FAM C.2.3 (shared maximum; full duplication-ladder proof retained)'
 if ident=='INV A1.0':row['credit_checks']=[{'source':'AC26 original PDF','locator':'Lemma 9.12, Proposition 9.13','outcome':'structure cohomology/direct images already stated; explicit discriminant/root/cup computation retained'}]
 if ident=='INV A4.2':row['credit_checks']=[{'source':'AC26 original PDF','locator':'Remark 1.3 p.5; Remark 9.21 p.81','outcome':'printed text checked visually; precise torsion correction confirmed'}]
(D/'result_audit.json').write_text(json.dumps(rows,indent=2)+'\n')
fields=list(dict.fromkeys(k for row in rows for k in row))
with (D/'result_audit.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in row.items()} for row in rows)
print('Updated',len(rows),'complete proof audit records.')
