# Paper I: derivations recorded before the four expanded target proofs

Source: `source/S6_SERIES_GRIND_I.tex`, SHA256 `d2e6c3bec1500144bfc0ef85e636ded534f2abc998cf58fdaf521b1e8a183169`.

This record precedes access to the expanded target derivations in the attached compendium. The exact exposure qualification in `S6_SERIES_PUBLISH_I_analytic_access_log.md` applies. In particular, the proof of dependency ari:C.7.6 was exposed; it is an input here, not an independently checked target. The source statements and primary-source statements below were read. No claim is made to have reproved the external transcendence or nonlinear PDE theorems.

## ari:C.4.1: theta/Siegel identity, modularity and the local-height constant

Write (q=e^{2\pi i\tau}), (v=a_1\tau+a_2), (T=\operatorname{Im}\tau). With the source's period-one theta convention, the Jacobi product is

\[
 \vartheta _1(v,\tau)=i q^{1/8}e^{-\pi iv}
 (1-e^{2\pi iv})\prod_{r\ge1}(1-q^r)
 (1-q^re^{2\pi iv})(1-q^re^{-2\pi iv}).
\]

Divide by \(\eta=q^{1/24}\prod_{r\ge1}(1-q^r)\) and multiply by \(i e^{\pi ia_1v}\). The scalar becomes

\[
 -q^{1/12}e^{\pi i(a_1-1)v}
 =-e^{\pi ia_2(a_1-1)}q^{(a_1^2-a_1+1/6)/2},
\]

which proves the complex identity with its sign and phase. Its modulus is exactly
\(e^{-\pi a_1^2T}|\vartheta _1/\eta|\), since (a_1,a_2) are real. As \(\operatorname{Im}v=a_1T\), this is the source's (N(v,\tau)). No rescaling of theta or of the lattice coordinate has been made.

For (a=(k/n,l/n)), Shin v6 Remark 2.2 (p.3) gives modularity and the modular-unit assertion already for exponent (12n/\gcd(6,n)). Raising that result to \(\gcd(6,n)\) gives the claimed exponent. The Fourier field can also be checked directly: the exponent of (Q=q^{1/n}) in the initial factor of (g_a^{12n}) is
\(6k^2-6kn+n^2\in\mathbb Z\); the initial phase is \(\zeta_n^{6l(k-n)}\), and the remaining factors are integer powers of terms (1-\zeta_n^{\pm l}Q^{rn\pm k}\). For (0\le k<n) these define a Laurent expansion with coefficients in \(\mathbb Q(\zeta_n)\), and Shin Proposition 2.3(iii), pp.3–4, gives the exact root-of-unity transport for arbitrary representatives. Raising the transport factor to (12n) gives 1. There are no zeros or poles on the upper half-plane, because (v\notin\mathbb Z+\tau\mathbb Z), and the products converge normally locally.

For the local height, set \(\lambda=-\log N\). The theta zero at the origin is simple, so \(\lambda=-\log|z|+O(1)\). Away from the lattice, the logarithm of the holomorphic nonzero theta quotient is harmonic and the Gaussian supplies the constant curvature of the Haar probability form. Its additive normalization is fixed, not arbitrary: with (v=x+y\tau), (0<y<1), averaging the Siegel-product logarithm over (0\le x\le1) kills the logarithms of all factors (1-re^{2\pi ix}) with (r<1); the remaining average is \(-\pi T B_2(y)\). Since \(\int_0^1B_2(y)dy=0\), \(\int_E\log N\,d\mu=0\). Thus \(-\log N\) is the mean-zero Green/Néron function of the origin. The source defines the general-lattice function through (z\mapsto z/\omega); an oriented basis change is accompanied by its usual modular coordinate map and has unit modulus after the Gaussian correction. Under scaling \((\Lambda,z)\mapsto(c\Lambda,cz)\), (z/\omega) is unchanged. This proves the stated model independence with an explicit transport.

The source formula is \(D_{\rm part}=(6/\pi)\log(N/(2\sqrt3))\). Substituting \(\log N=-\lambda\) gives the stated sign and additive constant. A new computation will compare the product with a directly summed theta Fourier series, and verify the rational exponents/phase; this is supplementary arithmetic verification, not a substitute for the identities above.

## ari:C.7.7: both unconditional normalized values

An algebraic invariant differential determines Weierstrass invariants (g_2,g_3\in\overline{\mathbb Q}). Waldschmidt's 1979 Corollary 1, as read in the author-hosted 2015 English translation p.3, says that
\(\sigma(u)^2\exp(\eta u+(u+\omega)(\beta-\zeta(u)))\)
is transcendental under the stated algebraicity and nontorsion assumptions. Put \(\omega=0\), so \(\eta=0\), and \(\beta=0\). The resulting number is the square of \(\sigma(u)e^{-u\zeta(u)/2}\). If the latter were algebraic, its square would be algebraic, a contradiction. The actual original French printed-page locator remains to be opened before final citation delivery.

For the second assertion, use (s_2\in\overline{\mathbb Q}), supplied by the already exposed cited dependency ari:C.7.6. Here is an explicit algebraic-group implementation of the analytic-subgroup argument. The nontrivial vector extension (G\) of (E\) has analytic uniformization
\[
 G(\mathbb C)=\mathbb C^2/\{(\omega,\eta(\omega)):\omega\in\Lambda\}.
\]
On the inverse image of (E\setminus\{O\}), the coordinates
\(x=\wp(z),y=\wp'(z),t=w-\zeta(z)\)
are invariant under this lattice. The addition formula
\[
 \zeta(z+z')-\zeta(z)-\zeta(z')
 =\frac12\frac{\wp'(z)-\wp'(z')}{\wp(z)-\wp(z')}
\]
gives an algebraic addition law over \(\overline{\mathbb Q}\) for (t). Around the identity use (w-\zeta(z)+1/z\); the Laurent expansion has algebraic coefficients in the algebraic formal parameter, so this is the usual vector extension over the same field. The Lie coordinates ((z,w)) are algebraic: at the identity the correction \(\zeta(z)-1/z\) has no linear term in the Weierstrass logarithm coordinate. The resulting group and the algebraic tangent line (L=\{(z,s_2z)\}) are therefore defined over \(\overline{\mathbb Q}\).

Suppose \(\alpha=\zeta(u)-s_2u\) were algebraic. The exponential image of ((u,s_2u)\in L_{\mathbb C}) then has coordinates ((\wp(u),\wp'(u),-\alpha)\), all algebraic, and is nonidentity because its projection is the nontorsion point (P). Huber–Wüstholz arXiv v8 Theorem6.1, printed p.43/PDF p.59, produces a positive-dimensional connected algebraic subgroup (H\) with \(\operatorname{Lie}H\subset L\). Thus (H) is one-dimensional and its projection to (E) has nonzero differential. A connected one-dimensional linear algebraic group has no nonconstant algebraic homomorphism onto an elliptic curve, so (H) is elliptic and its projection is an isogeny. Analytically a lift of this homomorphism is (z\mapsto(z,cz)\) after choosing the covering coordinate by its projection, and its period lattice is finite index in \(\Lambda\). It would force \(\eta(\omega)=c\omega\) on two independent periods and then on all of \(\Lambda\). This contradicts the Legendre determinant \(\eta_1\omega_2-\eta_2\omega_1=2\pi i\). Hence \(\zeta(u)-s_2u\) is transcendental.

Scope: this proves the two displayed values, using the cited theorems. The expression for (N(P)) contains an additional real Gaussian contribution, and no inference about its algebraicity is made. There is no numerical computation essential to this argument. The algebraic Lie-coordinate justification will be scrutinized against the printed proof; the formal parameter must be algebraic, not an unsupported analytic replacement.

## ari:C.7.8: heights and the arithmetic example

Rubin's Appendix A in Agboola–Howard, printed pp.1042–1043, defines the three heights by quotient maps from the same two-variable height. Its Theorem A.1 on p.1043 gives nonzero \(\mathfrak p\)-height for every point of infinite order under the paper's CM ordinary hypotheses. For (P\in E(\mathbb Q)\), the canonical ordinary height is Galois-equivariant. Complex conjugation fixes (P) and acts by (-1) on the anticyclotomic quotient. Therefore
\(h_{K,\mathrm{anti}}(P)=h_{K,\mathrm{anti}}(\bar P)=\overline{h_{K,\mathrm{anti}}(P)}=-h_{K,\mathrm{anti}}(P)\), hence this height is zero. The diagonal is formed using the principal polarization, which exchanges the two CM components under conjugation; the canonical symmetric pairing makes that exchange harmless. The local unit-root splittings are transported under conjugation because they are the unique ordinary Frobenius-stable complements. Lemma A.2 now implies the cyclotomic height is nonzero, since otherwise both cyclotomic and anticyclotomic quotients would vanish and so would the \(\mathfrak p\)-quotient. The functional-equation sign assumption is retained exactly; no stronger theorem is claimed by dropping it.

For the displayed example, use (a_1=a_2=0,a_3=1,a_4=-38,a_6=90). Direct invariant formulas yield
\[
 b_2=0,\ b_4=-76,\ b_6=361,\ b_8=-1444,
 \quad c_4=1824,\ c_6=-77976,\ \Delta=-19^3,
 \quad j=-884736.
\]
The reduced-form inequalities \(|b|\le a\le c\), \(b^2-4ac=-19\), (a\le\sqrt{19/3}\), leave the single reduced form ((1,1,5)). Thus the maximal order of discriminant (-19) has class number one. Its singular (j)-value can be identified exactly by the integral class polynomial and a certified (q\)-expansion at \((1+i\sqrt{19})/2\); the new computation will implement that identification with an explicit tail bound. Equal (j)-invariants give an isomorphism over \(\overline{\mathbb Q}\), so the displayed curve has the same full endomorphism ring.

The model is minimal at 19 since (v_{19}(\Delta)=3<12\). Since (j\) is integral and (c_4\) vanishes at 19, reduction is additive potentially good. The only bad prime is19. The known local-root formula at residual characteristic at least5 gives \(w_{19}=(-1)^{\lfloor 3\cdot19/12\rfloor}=+1\); the real place contributes (-1), all good primes (+1), so the global sign is (-1). The precise primary source for that formula is being opened separately; the formula is not being inferred from rank parity.

Point membership is immediate from (9^2+9=90). Direct counts at the good primes3 and5 are expected to give4 and7 points respectively; these are to be recomputed before comparison, and together imply trivial rational torsion by prime-to-residue-characteristic injectivity. Thus (P\ne O\) has infinite order. At5, trace (-1\) is prime to5, proving ordinary reduction. The polynomial of \((1+\sqrt{-19})/2\) is (X^2-X+5\), which factors as (X(X-1)\bmod5\); hence5splits. A fresh exact program will verify every numerical claim in this paragraph without importing the old programs.

## inv:C3.6: exact Ricci normalization and nonvanishing

Gauduchon1985 Theorem2, printed pp.132–133, applies to every compact almost-complex manifold of real dimension (2m\); the standard condition on p.131 is (dd^c\omega^{m-1}=0\). For this integrable complex threefold it is precisely \(\partial\bar\partial\omega^2=0\). Thus a Gauduchon metric exists.

For the standard (k=l=1\) threefold, inv:B2.1 gives
\(K_X=f^*\mathcal O(-1)\otimes\mathcal O(2S_2)\), and the fibre divisor relation is \(4S_2=f^*(\mathrm{pt})\). Tensoring twice gives the exact line-bundle isomorphism
\[
 K_X^{\otimes2}\simeq f^*\mathcal O(-1).
\]
For the convention (c_1^{BC}(L)=[iF/(2\pi)]\), this gives
\(c_1^{BC}(X)=\tfrac12[f^*\omega_{FS}]\), where \(\int_{\mathbb P^1}\omega_{FS}=1\). The Ricci class is (2\pi c_1^{BC}(X)\), so the closed real form \(\Psi=\pi f^*\omega_{FS}\) has exactly that class.

STW arXiv v2 Theorem1.3, p.3, uses the unscaled class \([\operatorname{Ric}]\), as explicitly defined on p.2. The conversion is multiplication by (2\pi\); no conflicting (c_1\) convention is silently identified. Its hypotheses hold for any prescribed Gauduchon (\omega_0\), and it produces a Gauduchon (\omega\) with the same Aeppli class of (\omega^2\) and Ricci form \(\Psi\). Pullback of the Fubini–Study form is semipositive, with rank one wherever (df\) has rank one.

For the final obstruction, choose any Gauduchon metric \(\omega_0\). Then
\(\int_X f^*\omega_{FS}\wedge\omega_0^2>0\): the integrand is nonnegative everywhere and strictly positive on the nonempty regular locus of the surjection (f\). Every (i\partial\bar\partial\)-exact (1,1) form pairs to zero with \(\omega_0^2\) by Stokes. Hence the Ricci Bott–Chern class is nonzero. A Chern–Ricci-flat Hermitian metric would represent this same class by zero, a contradiction. This argument does not require the flat metric itself to be Gauduchon.

## Remaining before proof comparison

Finish fresh computations; open the exact original Waldschmidt and local-root locators; record any limitation of the ordinary-height Galois compatibility source. Only then open the four expanded target proofs. These pending checks are not counted as completed events in this preread record.

### Pre-comparison computation and primary-source completion

The fresh program `S6_SERIES_PUBLISH_I_initial_four_compute.py` ran successfully at 2026-11-21 00:52:41 UTC; its output and JSON are retained. Every exact invariant above agrees. Direct enumeration gives \(\#E(\mathbb F_3)=4\), \(\#E(\mathbb F_5)=7\), and the ordinary trace is \(-1\). It also gives \(2P=(4,-2)\) and \(3P=(57/16,-13/64)\). The directed interval for the singular modulus is contained in \((-884736-10^{-70},-884736+10^{-70})\), with explicit E4 and product tail bounds, proving the claimed integer by CM integrality and class number one. Three independently evaluated theta/product comparisons have relative discrepancies below \(2\cdot10^{-90}\); the finite comparisons are supplementary, while the displayed algebraic product argument proves the identity generally.

The original French Waldschmidt paper has now been opened and visually read at printed pp.113–114 (PDF pp.3–4). The theorem on p.113 is unnumbered, in §3. Corollary1 is on p.113, in §4; the exact displayed normalized value is stated at the top of p.114. Thus “Theorem1” is the translation's numbering and should not be silently assigned to the original French source.

Rohrlich1996 Theorem2(i),(iii), printed pp.329–330, was also visually read. Directly in that theorem's notation, for the trivial representation at19 we have \(e=12/\gcd(3,12)=4\), \(q=19\equiv-1\pmod4\), and \(\epsilon=(-2/19)=1\). The exponent \(\langle1,1\rangle+\langle\eta,1\rangle+\langle\widehat\sigma_4,1\rangle\) is \(1+0+0=1\), so its formula gives \((-\epsilon)(-1)=\epsilon=1\). This proves the local sign directly from the opened primary result; the real-place part gives \(-1\). The floor formula above agrees but is unnecessary for the argument.

Mazur–Stein–Tate, author-hosted primary version, §2.9 and Remark2.2 (printed pp.595–596 in that specific version), explicitly state the Galois-equivariant ordinary height and derive the vanishing of the anticyclotomic diagonal for rational points. These are exactly the compatibility and projection steps derived above. The published version has separate pagination and has been retrieved for direct locator verification.

### Pre-comparison clarification of the vector-extension chart

The preceding mention of (1/z) identifies the principal part only; it must not be used as an algebraic transition function. The exact algebraic chart is obtained with the rational function (R(P)=-y/(2x)), where (x=\wp(z),y=\wp'(z)). Its expansion is (R(P)=1/z+O(z^3)). Define (t_O=t_U+R(P)=w-\zeta(z)-y/(2x)). Then (t_O=w+O(z^3)), and the transition (t_O-t_U=R(P)) is rational over the field of the curve. The algebraic local parameter (-2x/y=z+O(z^5)) has tangent (dz). Consequently the algebraic tangent coordinates are precisely ((z,w)), with no additional linear coefficient. Other poles of (R) are excluded from this identity chart and covered by the original chart. This supplies the exact morphism and replaces the informal principal-part wording before access to the target printed proof.

### Final pre-comparison locator note

The published Mazur–Stein–Tate PDF has now also been visually read: §2.9 pp.587–588 and Remark2.2 p.588 (PDF pp.11–12). This confirms the same equivariance formula in the published pagination. All pending checks specified above have been completed, and the four target expanded proofs are still unopened as of this stamp.
