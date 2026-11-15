INCOMPLETE

| Item | Statements | State at checkpoint 01 |
|---|---|---|
| A.1 | A.1.1–A.1.4 | Proved: bijections, boundary/Pell corrections, independent census through 10^7. |
| A.2 | A.2.1–A.2.5 | Proved: arithmetic/reflection group, two norm −2 orbits, geodesic lengths, main-term normalization, absence of exceptional spectrum. |
| A.3 | A.3.1–A.3.2 | Proved: unrestricted 2/3 error with finite-cover and spectral bookkeeping. |
| A.4 | A.4.1–A.4.2 | Required 2/3+epsilon error remains undecided. Sharp-arc 7/8+epsilon and the exact twisted reduction proved. |
| A.5 | A.5.1–A.5.4 | Census through 10^9 and finite discrepancy certificate proved; arc mean-square and Omega/Omega± unresolved. |
| B.1 | B.1–B.2 | Exact glue, J, discriminant form, eight extensions and action of r proved. |
| B.2 | B.3–B.5 | J, theta form, full automorphism group and its Co0 plane stabilizer proved. Global isotropic-plane classification underway. |
| B.3 | B.6 | Refuted and corrected: eleven exceptions among all 96 divisor-neighbour cases. |
| B.4 | B.7–B.8 | Full Wilson cubic stabilizer and explicit E8^3 embedding/value-group dependence established; literature audit continuing. |
| C.1 | C.1 statements in C_special.tex | Exact phases, values, general isogeny identity and numerical checks completed. |
| C.2 | C.2 statements in C_special.tex | Nomes, signs, branches, real structures completed; K2 checked at the step used. |
| C.3 | C.3 statements in C_special.tex | Next terms at i and rho proved; t=0 is neither a local maximum nor a minimum. |
| C.4 | C.4 statements in C_special.tex | Division identities, all-order torsion algebraicity, exact polynomials and all roots for n=2–8 completed. |
| C.5 | C.5 statements in C_special.tex | CM torsion theorem applied with twists and exceptional orders checked. |
| C.6 | C.6.1–C.6.4; C.6.R1–R3 | Global/local heights, ranks, saturation and independent L-values complete for the eleven CM fibres. Explicit BSD factors remain numerical, and rank-two leading-coefficient relations are not claimed from a rank-one theorem. Quadratic torsion data being integrated. |
| C.8 | C.8.1–C.8.5 | Analytic R4 proof without enumeration completed. Remaining integral/measure identities being written; all critical points and global level topology still unresolved. |
| C.7 | C.7.1–C.7.5 | Sigma/compact criterion and conditional transcendence theorem proved; unconditional transcendence unresolved even for the specified conductor-361 example. |

# S6_05_ARITHMETIC research record

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. Work began on 15 November 2026 at approximately 14:39 UTC. This is an hourly research checkpoint, not a completed answer. The first user-requested three-hour progress assessment is due around 17:39 UTC and has not yet occurred.

## Computations and corrections

R(10^9)=35,363,970. An independent (s,t,z) census through 10^7 agrees with the original-coordinate calculation. Arb plus signed 128-bit comparisons certify |R(x)−C0 x|<0.172 sqrt(x) for every real x in [10^4,10^9], including one-sided values at jumps. This finite certificate is not an asymptotic theorem.

Lead 2 is literally correct about an interval representative of an ideal generator. An early draft overread it as asserting positive field norm for every ideal norm. That extra assertion is false but was not in the lead. The draft is corrected, and the norm-2 example is retained only as a caution. For m=18z^2−2 the positive-norm property is proved.

J has minimum 4, kissing number 23,058, norm-6 shell 1,849,032 and norm-8 shell 44,291,124. Its full automorphism group has order 12,597,120, and its Co0 plane stabilizer has order 2,099,520. The two rooted extensions share the same 72 ambient roots, making the code reduction intrinsic. Exact exhaustive code-automorphism enumeration verifies the upper bound. The Wilson cubic stabilizer has order 252, with exact triality and glue upper bounds.

The Weyl-neighbour h/d assertion is false: for E8^3, h=30, d=2 gives D8^3 with Coxeter number 14, not 15. All eleven exceptions among 96 cases have exact bases and root enumerations.

The expansion at rho has a nonzero harmonic cubic. In the t-coordinate,
L(t)=log(3)/4+(7/192)Re(t)−B|t|^(4/3)+O(|t|^(5/3)), B>0.
Thus t=0 is neither a maximum nor a minimum. It must not be counted as a second maximum in the suggested critical-point route.

For mu=a tau+b the positive Betti form is db wedge da, not da wedge db. The measure m_P has mass 1/12, so its associated probability measure is 12 m_P. Unnormalized torsion divisors divided by n^2 converge to m_P. The full proof and local densities are being written.

Our canonical height is for (O), half the Mordell–Weil self-pairing. The generic height is 1/12. PARI ellheight is divided by two; the L-value denominator is the full real Néron period, with both real components when present. At every rational CM fibre, independent theta and height calculations agree beyond 245 decimals at 270-digit working precision.

Two CM fibres, j=8000 and j=−12288000, have rank two; the other nine have rank one and P is primitive by full saturation. Independent truncated L-series calculations agree beyond 65 digits. The numerical BSD quotient is 9 at discriminant −163 and 1 at the other rank-one curves. These decimals do not prove the order of Sha.

## Exact remaining obstructions and next attacks

### A.4–A.5

The directly proved Cheeger bound is h≥1 for every compact orbifold of signature (0;2,2,2,2,2), independently of moduli, so exceptional eigenvalues are no longer the obstruction. The unrestricted relative trace formula gives 2/3 after the explicit finite-cover comparison. A sharp fixed arc needs a uniform estimate for the foot character and its summation. The current sharp-domain exponent is 7/8+epsilon. Good, Lekkas–Petridis, Voskou, Parkkonen–Paulin, Bourgain–Kontorovich–Sarnak and Gorodnik–Nevo were checked for their actual scopes; a full-geodesic theorem is not treated as a sharp-arc theorem. The next step is the uniform Fourier-mode period bound. The same restriction problem prevents transferring the known full-geodesic mean-square and Omega results. Exact attempts are recorded in records/A_progress.md.

### B.2

The J configuration is classified, but all isotropic planes constitute a separate finite problem, with total 61,549,107,892,647,466,000. The A2-line stratification has been searched exactly: 147 nonzero flag orbits, whose sizes sum to all 5,230,235,650 isotropic lines in the 22-dimensional quotient. Their eight extensions are being root-enumerated and equivalent flags fused. A1-line strata and the all-Leech cases are the next steps. Bases, actions, orbit arrays, and ongoing outputs are preserved.

### C.6

Gross–Zagier/Kolyvagin give a rational relation between a rank-one point height and L′/Omega, with rank and finiteness assertions under the stated hypotheses. An exact full BSD factor requires more than a numerical match. Rank-two fibres cannot use the rank-one theorem. At the irrational order-six parameters, E_t(Q) is not defined because j is irrational; the meaningful rank is over Q(sqrt(3)). Its exact local minimal models are computed and the rank calculation is underway.

### C.8

The R4 proof uses scalar Fourier estimates, a local radius |tau−i|≤1/50 and the n=2,4,8 division ladder. No grid, interval enumeration or box certificate is used. The separate demand to locate every critical point and determine every level set remains unresolved. The suggested saddle on (0,1) is not accepted without proof. The next attack combines the two-factor derivative formula with explicit Fourier estimates; numerical diagnostics may guide but cannot prove exclusion.

### C.7(c)

A concrete undecided instance is E:y^2+y=x^3−38x+90, P=(0,9), conductor 361, CM discriminant −19. Every finite normalized local height of P is zero, so N(P)=exp(−hhat_O(P)), where hhat_O(P)=0.0906458370178996370789407706918816499305194812232182.... No unconditional proof of algebraicity or transcendence has been obtained. The discriminant −7 example E:y^2=x^3−140x+784, P=(0,28) gives N=2exp(−hhat_O(P)).

The conditional proof computes the motivic group, including the conjugate motive and positive Rosati bracket. Algebraicity cuts the central period torsor by a proper affine hyperplane. The named weaker sufficient hypothesis is Bertolin–Philippon–Saha–Saha Conjecture 4.7. Their weak Conjecture 4.9 gives no positive bound here. The linear 1-period theorem does not exclude the required nonlinear relation.

Attacks tried include CM multiplication on the rank-two endomorphism orbit, Schneider–Lang growth and derivative criteria, complexifying the theta norm, eliminating the Gaussian for real t>1, and the maximal compact algebraic-point criterion. The corresponding obstacles are the rank/growth threshold; absence of an algebraic logarithmic derivative; the transcendental pi/area coefficient in the complexified Gaussian; and a real compact subgroup instead of an algebraic complex subgroup. Bertrand's original theta and p-adic theorems are still being located and checked. His opened primary-author 2017 slides distinguish the holomorphic theta value from the archimedean metric. These are failures of specific approaches, not a proof that no method can work. The requested 200-digit PSLQ tests, coefficient bound 10^8, tolerance 10^-185, found no relation; no transcendence conclusion is drawn.

## Sources and literature status

The supplied sections used, including K1–K6, were read at the relied-on steps. Version 1 of Du–Guo–Kusakabe–Xie is cited for its classification statements; version 2 drops them and no inference is drawn from that omission. Attached primary papers are supplemented by primary-source browsing. Bibliography entries state whether the theorem text was opened; metadata alone is marked unverified for theorem use. The bibliography and per-part records retain exact URLs, theorem numbers and hypotheses. No priority or novelty claim follows from a failed search.

## Preservation

Each hourly checkpoint has a distinct sequential name and contains current deliverables, code and research records, excluding the supplied attachments. code/A_census_1e9.d16m8.gz losslessly replaces the raw A_census_1e9.u32 and the larger A_census_1e9_height_multiplicity.u32.gz; its decoder and checksums are retained. The two redundant encodings remain locally and are omitted from the ZIP. Part B orbit arrays are gzip-compressed losslessly with SHA256 manifests; their uncompressed copies are redundant. No earlier checkpoint is overwritten or deleted. The initial all-pending report is superseded by this exact state report.

## Typesetting

The first integrated manuscript builds as a 56-page LuaLaTeX PDF. Build logs are retained. Publication QA is underway: overfull boxes above 2pt are being corrected, followed by rendering all affected pages and a distributed sample. The checkpoint includes the current working PDF and records its unfinished layout audit; the final PDF will satisfy the requested clean-build and visual-inspection requirement.

