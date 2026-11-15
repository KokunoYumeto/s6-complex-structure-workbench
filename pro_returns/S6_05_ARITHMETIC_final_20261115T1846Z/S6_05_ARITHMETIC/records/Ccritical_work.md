# C.8 critical-point and level-set work

## Outcome

Statements C.8.12–C.8.15, in `sections/C_critical.tex`, prove the exact zero sets of the two critical factors and strict radial monotonicity of L about t=1. Every lower level is one star-shaped Jordan curve. The prompt's proposed saddle on (0,1) is absent. This also supplies an independent analytic proof of R4 after the duplication proof already written by root.

The invariant is X=3W*wpprime/g2, F=1-X. The exact identity is (t-1)L_t=X(X-2)/24. The global bound |F|<1 is obtained from one Cayley disc and one cusp half-plane. There is no parameter grid, box cover, or root-search input in the proof.

## Exact scalar verification

`Ccritical_certificate.py,out` obtains all modular differential-equation coefficients as exact FLINT rationals, gives explicit Cauchy tails, and encloses the finite scalar coefficient sums with Arb. `Ccritical_rational_certificate.py,out` independently rechecks all coefficients and inequalities using only exact integers/rationals, with outward rounding on the denominator 10^100. The constants are bounded by Machin's arctangent identity, exponential Taylor series and a Lambert-series geometric tail; no gamma-function routine or numerical root solver enters this check.

`Ccritical_scalar.py,out` proves the one remaining scalar inequality by an exact degree-14 Bernstein expansion over Q(sqrt(3)); all 15 coefficients have explicit positive rational lower bounds. Full expressions are retained in `records/Ccritical_scalar.json`. This is one exact polynomial identity, not enumeration of any domain.

The manuscript displays the differential recurrences, four analytic radii, all tail formulas, both finite scalar tables, the factored polynomial, the Bernstein conversion formula and rational lower bounds. The programs make the arithmetic reproducible but are not substituted for the analytic proof.

Attempt files preserve a variable-name typo (`Ccritical_certificate_attempt1.py,out`) and decimal parsing / constant enclosure setup errors in `Ccritical_rational_attempt1.py,out` and `Ccritical_rational_attempt2.py,out`. They are superseded by the passing certificate scripts. The first typo's traceback was returned in the tool output (NameError: nubound; the saved stdout stops at the preceding bound); no mathematical assertion depended on that aborted execution.

## Exploratory computations, not proofs

`Ccritical_guide.py,out` and `records/Ccritical_guide.json` used Fourier-series Newton solutions and root searches only to identify a candidate inequality. They suggested no ordinary critical point and the stronger disc bound |F|<1. They are explicitly marked nonproof evidence.

`Ccritical_cayley.py,out` and its JSON record derive the initial exact rational series. `Ccritical_factor_guide.py,out` guided the removal of the E4 zero at the equianharmonic boundary. An initial triangle bound reached 1.025 and therefore failed. The successful step combines the numerator terms orthogonally:

|dH+q(H-conj(H))|^2=d^2|H|^2+4q(d+q)(Im H)^2.

It also uses |Im z|/|1+z/z0|<=|z|. The resulting analytic majorant has a large margin away from w=0, and the Bernstein polynomial proves its strict sign down to that endpoint.

## Other attempted reductions

The coupled PDE for X and the period-area function gave a weak maximum principle for |1-X| but no global bound near i and rho, so it was not used. Averaging the zeta addition formula gives the formal integral identity X=-(3g3/(2g2))*integral_E(1/wp(z))dnu(z); no positivity theorem sufficient for the desired disc bound was found. The integral itself is locally integrable at wp=0. Neither route is a dependency of the final proof.

Fixed-torus Green-function theorems count critical points as the elliptic argument varies at fixed tau. They do not by themselves classify the moving wp-zero section as tau varies. In particular results concerning wp'' at a Green critical point are not results concerning wp=0. We did not substitute these distinct conditions.

## Primary literature opened and checked

- Eichler and Zagier (1982), *On the zeros of the Weierstrass wp-function*, Mathematische Annalen 258, 399–407, DOI 10.1007/BF01453974. Full original paper opened at https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01453974/fulltext.pdf. Unnumbered theorem p.399, Fourier corollary p.400, and first proof pp.400–403 were checked. Its branch is the cusp branch specified by the prompt.
- Duke and Imamoglu (2008), *The zeros of the Weierstrass wp-function and hypergeometric series*, Mathematische Annalen 340(4), 897–905, DOI 10.1007/s00208-007-0174-3. Full author preprint at https://www.math.ucla.edu/~wdduke/preprints/zeros.pdf opened. Theorem 1, Corollary 1, the unnumbered Eichler–Zagier theorem in Section 2, and equation (6) checked. Their variable 1728/j is the reciprocal of ours.
- Bergweiler and Eremenko, *Green function and antiholomorphic dynamics on a torus*: https://www.math.purdue.edu/~eremenko/dvi/greenfunction-ams-eps.pdf, full 11-page primary text opened. Its 3-versus-5 criterion is on a fixed torus; not used for the moving section.
- Eremenko (6 September 2026), *Remarks on a theorem of Lin and Wang*: https://www.math.purdue.edu/~eremenko/Pdf/remarks.pdf, full 7-page text opened. Its unitary Lamé accessory-parameter uniqueness does not classify the accessory value zero across all moduli; not used.
- Chen, Fu and Lin, arXiv:2508.17604v2, https://arxiv.org/pdf/2508.17604, 39-page current primary text opened. Nondegeneracy and fixed-torus classification checked for relevance; not used in the proof.
- Lin and Wang (2010), *Elliptic functions, Green functions and the mean field equations on tori*, Annals of Mathematics 172, 911–954: https://www.math.purdue.edu/~eremenko/Pdf/Lin/lin-annals.pdf, search text checked for Lemma 6.5; the condition there involves wp'', not wp. Do not mark this entry as fully opened in a bibliography unless opened subsequently.

No priority is claimed for the global radial inequality. The references above did not state it, and the manuscript records the scope of that literature check.

## Additional C7 audit sent to root

C.7.6's squared CM multiplication formula and its proof of algebraicity of s2 check out, including the finite-character issue and the alpha=1+i example. The analytic-subgroup-theorem proof of transcendence of zeta(u)-s2u also checks out: the one-dimensional algebraic Lie line would supply an elliptic subgroup splitting the nontrivial universal vector extension after an isogeny.

The unrestricted iff wording for Bertrand's CM criterion needs a lift convention. Replacing v by v+omega changes g(u,v)-s2uv by (eta(omega)-s2omega)u. The point-only condition Ny=f(x) is unchanged. On a square lattice, the unrestricted converse for all lifts would imply algebraicity of exp(eta(omega)u) and its i-th power at algebraic non-torsion points, contradicting Gelfond–Schneider after choosing u real. The necessary direction used for the diagonal theta argument may still be valid; root was advised to state only that direction and check the original Corollary 3 convention. The exact slide is https://webusers.imj-prg.fr/~daniel.bertrand/Recherche/rpdf/DB_Fieldspos.pdf, final slide comment (c), independently opened. The universal-extension logarithm coordinates on slide9 were also checked. No edits were made to root's C_cm_transcendence.tex.

### C7 audit resolution

At root's request, `code/C7_revise_theta.py,out` replaced C.7.7's unresolved CM holomorphic-theta claim with Waldschmidt (1979), Theorem1/Corollary1: sigma(u) exp(-u zeta(u)/2) is transcendental at every algebraic non-torsion elliptic point. The full three-page author-hosted English translation and its Schneider–Lang proof were opened and downloaded. The AST derivative statement remains. The exact relation to N and the unresolved lift normalization are now explicit in `C_cm_transcendence.tex`. The original version is retained in `records/C_cm_transcendence_before_lift_audit.tex`; no unverified one-way implication from the slides is used.

The original French journal download returned HTML instead of a PDF. The received bytes are retained as `records/C_Waldschmidt1979_original_download.html`; `code/C7_source_fetch.py,out` documents the URL and format. Attempted pdftotext failed with “May not be a PDF file”; the failure was not used as source evidence. The author-hosted translation is retained as `records/C_Waldschmidt1979_translation.pdf` and its theorem was read in full through web retrieval. The original journal metadata were independently verified at https://mathreports.ca/article/nombres-transcendants-et-fonctions-sigma-de-weirstrass/.

The parent review corrected the cusp constant in C.8.15 from log(sqrt6) to log(2sqrt3), because cosh(log(5+2sqrt6)/2)=sqrt3. The critical-point estimates and their constants did not use the mistaken asymptotic constant; the manuscript is corrected.

### Current 2025 sigma-function paper

Duc Hiep Pham, *Semiabelian varieties and transcendence on Weierstrass sigma functions*, Glasgow Mathematical Journal 67(1) (2025), 107–113, DOI 10.1017/S0017089524000272, was identified in the current literature. The primary publisher abstract and references were opened. Both the full-HTML URL and its actual `citation_pdf_url` redirect to the abstract/access page. OpenAlex lists only the closed publisher location, with `any_repository_has_fulltext=false`; Semantic Scholar likewise lists no open PDF. Title/author/preprint searches did not locate an accessible manuscript. The exact metadata and retrieval record are retained in `C_Pham2025_*.json/html` and `code/C7_pham_*.py,out`.

At the root's request, `pham2025sigma` was added to the bibliography with its full-text verification limitation, and a manuscript paragraph records that no theorem from it is invoked and no assertion of inapplicability is made. The critical section also passed an isolated LuaLaTeX build with zero overfull boxes after the multiple-alignment displays were corrected; the source-fix and compile-check scripts and outputs are retained.

The abstract announces complex and p-adic linear independence and applications to sigma functions. No precise theorem or normalization was available, so this work is not used, and we make no assertion that its results either settle or fail to settle the metric norm. Its full statements remain a specific source-access task, rather than a conjecturally inferred theorem.

`code/Ccritical_identity_check.py,out` independently compares the Cayley expression with a direct 110-digit Fourier solution of wp(mu)=0. At two small Cayley points the residual is below 1e-110; near the outer boundary the 100-term Cayley series residual is below 2e-48. This is a branch/normalization check only. The analytic proof uses the explicit Cauchy bounds and exact scalar comparisons instead.
