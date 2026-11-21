# Paper I: comparison of the four initial analytic checks

## Access and scope

The source snapshot is SHA256 d2e6c3bec1500144bfc0ef85e636ded534f2abc998cf58fdaf521b1e8a183169. The access log discloses the initial extractor overrun. No target's own expanded proof was exposed by that overrun. Dependency ari:C.7.6 and adjacent source-scope discussions were exposed and are treated as inputs.

The preread derivations, amended with exact algebraic-chart and primary-locator details, were sealed at 2026-11-21T00:54:46.032566+00:00, SHA256 cf08f10105dc52a9513b98897c69f613cedc14d346df0a55cceb64b46f97e68f. The fresh program had already run successfully. Only after that stamp were the four expanded compendium proofs extracted and read. Their exact source spans, text, source hash and first-read timestamp are in the printed-proofs JSON. The accompanying event rows claim scoped targeted proof checks, not independent reconstruction of the external literature theorems.

## ari:C.4.1

**Outcome: the statement and normalization agree.** The preread derivation establishes the exact complex phase \(i e^{\pi ia_1v}\), the Gaussian modulus, the rational Fourier exponent and field, modular-unit assertion from Shin's stronger exponent, the Haar-mean-zero normalization, and the sign/constant in \(D_{\rm part}\).

The printed proof takes a more explicit generator route through the transformations under \(S,T\). Those displayed generator formulas were first read in the comparison; they are not given preread credit. The preread modularity argument instead applies Shin Remark2.2 and Proposition2.3 with their verified hypotheses. The source's integer-translation multiplier is exactly Shin's: its exponent \(a_1b_2-a_2b_1+b_1b_2+b_1+b_2\) equals the exponent obtained from Shin's sign factor and \(-\pi i(b_1a_2-b_2a_1)\).

The printed local-height limit follows from \(\wp(z)\sim z^{-2}\) and \(\Delta_\Lambda=(2\pi)^{12}\omega^{-12}\eta(\tau)^{24}\). Since \(\vartheta_1'(0,\tau)=2\pi\eta(\tau)^3\), \(U_\Lambda(z)=\log|z|+\frac1{12}\log|\Delta_\Lambda|+o(1)\). Under \((\Lambda,z)\mapsto(c\Lambda,cz)\), \(x\mapsto c^{-2}x\), \(\Delta\mapsto c^{-12}\Delta\), and both sides of the displayed local-height limit change by \(\log|c|\); \(U\) itself is unchanged. This explicit transport should replace the vague word “cancels” if the proof is rewritten.

The new program compares a Siegel product with an independently summed theta Fourier series and Euler pentagonal expression for eta. The largest recorded relative discrepancy is below \(2\cdot10^{-90}\). It also verifies 3960 exact rational exponent/phase specializations. These finite checks supplement the general algebraic proof and are not called a certificate of modularity for all parameters.

## ari:C.7.7

**Outcome: both displayed transcendence assertions agree.** The preread route to the first is Corollary1 with \(\omega=\beta=0\), followed by taking the square. The printed proof applies the theorem with \(v=u\) and then sigma duplication. These routes give the same square. Its extra factor is \(-\wp'(u)\), which is algebraic and nonzero because a point with \(\wp'(u)=0\) is 2-torsion. The duplication formula can also be checked by observing that \(\sigma(2u)/\sigma(u)^4\) is an odd elliptic function with the same principal part as \(-\wp'(u)\). This comparison was made after opening the printed step and receives reread scope, not preread scope.

For the second assertion the preread argument builds the vector extension in exact coordinates and uses Legendre's determinant to exclude an elliptic subgroup. The printed proof uses the nonzero class in \(H^1(E,\mathcal O_E)\) and injectivity of pullback under isogeny. The latter follows from the trace identity \(\operatorname{Tr}\circ\phi^*=\deg(\phi)\), so it agrees with the analytic obstruction.

The printed phrase “with a possible algebraic linear change of the second coordinate” should be made concrete in a rewrite. One exact choice is \(t=w-\zeta(z)\) on the affine Weierstrass chart and \(t_O=t-y/(2x)\) around the identity; \(t_O=w+O(z^3)\). Thus \((z,w)\) are algebraic tangent coordinates. For an algebraic lift with \(b=\zeta(u)-s_2u\), the chosen fibre coordinate is \(t=-b\). The line has precisely slope \(s_2\). This fixes the sign and scalar instead of silently identifying two normalizations.

No new numerical calculation is essential to these two consequences. The external transcendence theorems and the already exposed proof of CM algebraicity of \(s_2\) are inputs. No inference about transcendence of \(N(P)\) or of the differently normalized theta value is made.

**Citation correction:** in the original French 1979 paper the theorem is unnumbered, §3 p.113; Corollary1 is §4 p.113, and the displayed sigma value is explicitly stated on p.114. “Theorem1” belongs to the 2015 translation. Huber–Wüstholz arXiv v8 Theorem6.1 is printed p.43 (PDF p.59); its publication is Cambridge Tracts227 (2022), not the venue/year in the original bibliography.

## ari:C.7.8

**Outcome: the height application and concrete example agree.** The preread argument uses Rubin AppendixA TheoremA.1, vanishing of the anticyclotomic height of a rational point by Galois equivariance, and LemmaA.2. The published Mazur–Stein–Tate §2.9/Remark2.2, pp.587–588, explicitly supplies the equivariance/projection property. The height is the canonical ordinary polarized height; exchanging the CM components under conjugation is the corresponding exchange of the two arguments of the symmetric pairing. Only vanishing/nonvanishing is asserted, with Agboola–Howard's normalization retained.

All standing CM, class-number, sign, splitting, and ordinary hypotheses were retained. The proof does not invoke the conditional result ari:C.7.4 despite that label appearing in the source's overinclusive dependency record. That label and the unrelated scope discussions should not be represented as mathematical inputs to this unconditional assertion.

The fresh method for the example uses exact Weierstrass invariants, finite-field enumeration at3 and5 to exclude all rational torsion, a complete reduced-form enumeration for discriminant−19, and a directed interval singular-modulus computation with explicit infinite tails. It verifies \(\Delta=-19^3\), \(j=-884736\), \(2P=(4,-2)\), \(\#E(\mathbb F_3)=4\), \(\#E(\mathbb F_5)=7\), \(a_5=-1\), and splitting of \(X^2-X+5\) modulo5.

The printed proof obtains the sign from the analytic-rank statement ari:C.6.R2. This check does not claim to reprove that analytic-rank result. Instead, it obtains the sign directly from the primary local-root formula: Rohrlich1996 Theorem2(i),(iii), pp.329–330. At19, \(e=4\), the trivial-representation specialization gives \((-2/19)=+1\); the real place gives−1 and every good prime gives+1. Thus the concrete example has the required sign independently of the analytic-rank input. The elementary finite-field count is freshly implemented; the different overall method concerns torsion, CM identification and the sign rather than an invented claim that point-counting formulas are unrelated.

## inv:C3.6

**Outcome: all assertions agree.** The preread application takes Gauduchon1985 Theorem2 as an input, gives the exact line-bundle isomorphism \(K_X^{\otimes2}\simeq f^*\mathcal O(-1)\), converts the normalized Bott–Chern class to the unnormalized Ricci class by multiplication by \(2\pi\), and applies STW Theorem1.3 with every prescribed Gauduchon background. It proves rank-one semipositivity and rules out a flat Chern–Ricci form using positive pairing against a Gauduchon square.

The printed proof additionally sketches Gauduchon's Fredholm/maximum-principle proof. That sketch was not independently reconstructed in the preread record; the same primary proof was read as a cited input. Its sign-change argument and exponent \(u^{1/2}\) agree with primary printed p.133. The source's alternative nonvanishing proof through inv:C3.1 also agrees with the direct positive-pairing route.

No counterexample or false target statement was found. Proposed changes concern exact citation locators, an explicit vector-extension coordinate map, a precise scaling explanation, and a dependency record that distinguishes operative inputs from later scope discussions. These require ordinary rewrite comparisons when integrated; no refutation event is warranted.

## New computational method and limits

The program uses Python exact fractions and direct residue enumeration, with no attached code imported and no Sage/PARI call. For the CM identification it uses mpmath directed intervals at90 decimal digits, twenty E4/product terms, the bound \(\sigma_3(n)\le n^4\), and an explicit logarithmic tail for the product. The resulting interval has width less than \(2\cdot10^{-82}\). The exact conclusion uses the standard CM integrality/class-field fact together with the independently enumerated class number one. It is not an unsupported rounding of a floating-point value.

The sigma transcendence and nonlinear PDE existence theorems remain cited external inputs. These records establish their stated applications and exact normalization checks, not independent proofs of those literature results.
