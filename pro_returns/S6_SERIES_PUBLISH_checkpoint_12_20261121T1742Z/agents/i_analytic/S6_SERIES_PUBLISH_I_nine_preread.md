# Paper I: preread derivations for nine main-reference candidates

## State and exposure

Source snapshot: source/S6_SERIES_GRIND_I.tex, SHA256 d2e6c3bec1500144bfc0ef85e636ded534f2abc998cf58fdaf521b1e8a183169.

Targets: ari:C.6.1, C.6.2, C.7.1, C.8.1, C.8.2, C.8.3, C.8.4, C.8.11, C.8.12. Their statements were extracted separately, without their proof bodies. The earlier first-four access note remains applicable; in particular C.7.1's statement was already read as a dependency, and C.7.6's proof was exposed as an input. The earlier broad search for occurrences of the norm displayed isolated formulas from later C.8 material around source lines30930–31134; ownership was checked separately and these are outside the nine target proofs. They are not represented as unseen material.

The cited anchors cp-periods, ca-sup, ca-exp, ca-derivatives, ca-GHbounds, ca-H and ca-delta-h are inside the respective target's own proof, rather than independent input statements. Their ownership and line spans were located without displaying their contents. They have not been read as inputs to the derivations below.

Read inputs include the exact statements ari:C.4.2, C.3.1, C.3.2 and fam:src:C.1.1, plus the primary DeMarco–Mavraki §2.1 and Bertolin–Philippon–Saha–Saha §2.3/Definitions2.3–2.4/§6. The two new programs use no attached verification code. The numerical majorants below were devised before their corresponding target proofs were opened.

## 1. ari:C.6.1: global height formula

Write \(\lambda_v\) for the local Néron function with the discriminant normalization used by DeMarco–Mavraki §2.1. Their canonical height is exactly \(\frac12\lim n^{-2}h(x(nP))\), and their duplication law on a general Weierstrass equation is
\[
 \lambda_v(2P)=4\lambda_v(P)-\log|2y+a_1x+a_3|_v
                         +\frac14\log|\Delta|_v.
\]
For the standard division function \(\psi_n\), whose divisor is \([n]^*(O)-n^2(O)\) and whose leading formal-parameter term is \(n z^{1-n^2}\), the corresponding identity for all \(n\) follows by comparing divisors/local Green curvatures. The difference is constant, and its value at the origin fixes it exactly. Indeed
\[
 \lambda_v(P)=-\log|z(P)|_v-\frac1{12}\log|\Delta|_v+o(1),
 \quad z(nP)=nz(P)+O(z(P)^2),
\]
so
\[
 \lambda_v(nP)-n^2\lambda_v(P)+\log|\psi_n(P)|_v
       =\frac{n^2-1}{12}\log|\Delta|_v.
\]
This also gives the precise change of model. Under the homothety
\((x,y,\Delta,\psi_n)\mapsto(c^{-2}x,c^{-3}y,c^{-12}\Delta,
c^{1-n^2}\psi_n)\), the two added logarithmic terms cancel exactly, while the normalized local function is transported unchanged. Translation/completion of the square is an algebraic isomorphism preserving the invariant differential and the canonical division function. On a long Weierstrass equation \(\psi_2=2y+a_1x+a_3\); the earlier short-model notation \(\psi_2=2y\) is transported by the exact completion of the square, not silently reused.

The global decomposition is
\[
 [K:\mathbb Q]\widehat h_O(P)=
      \sum_{v\nmid\infty}n_v\lambda_v(P)
      +\sum_{\sigma:K\hookrightarrow\mathbb C}\lambda_\infty(P^\sigma).
\]
At infinity, the theta/Siegel calculation already checked in C.4.1 gives
\(\lambda_\infty=-\log N\). A complex place contributes two conjugate embeddings, whose real norm values agree; a real place contributes one. Rearrangement proves exactly the displayed global formula. For rational \(t\), each finite contribution is a rational multiple of \(\log p\) and only finitely many are nonzero, by the local intersection/component formula for the Néron function. Thus \(A_t=\prod p^{r_p}\) is positive and algebraic. Exponentiation gives \(N=A_te^{-\widehat h_O}\), and substitution in \(D_{\rm part}=(6/\pi)\log(N/(2\sqrt3))\) gives the asserted formula. Multiplication/division by the nonzero algebraic \(A_t\) proves the stated equivalence of algebraicity.

The displayed rational family has \(A=-3t^3(t-1)/4\), \(B=t^4(t-1)^2/4\); direct expansion of \(-16(4A^3+27B^2)\) gives \(27t^8(t-1)^3\). This was independently checked symbolically.

## 2. ari:C.6.2: exact finite contribution

On a minimal model, the normalized local function on the identity component is
\[
 \frac{\lambda_p(Q)}{\log p}
 =\frac12\max(0,-v_p(x(Q)))+\frac{v_p(\Delta)}{12}.
\]
Insert \(Q=mP\) into the preceding multiplication law. Since \(\log|\psi_m|_p=-v_p(\psi_m)\log p\) and \(\log|\Delta|_p=-v_p(\Delta)\log p\), it reads
\[
 \frac12\max(0,-v_p(x(mP)))+\frac{v_p(\Delta)}{12}
 =m^2\frac{\lambda_p(P)}{\log p}+v_p(\psi_m(P))
                 -\frac{m^2-1}{12}v_p(\Delta).
\]
Solving gives exactly the target. The assumption \(mP\ne O\) ensures every displayed valuation of a rational function is finite. For \(m=1\), the formula specializes to the identity-component formula. This derivation verifies the formula itself; any later table entries require their own explicit input coordinates and are not claimed verified merely from the formula.

## 3. ari:C.7.1: sigma normalization and relative period

For \(z=u/\omega_1\), \(\tau=\omega_2/\omega_1\), the exact sigma–theta formula is
\[
 \sigma(u)=\frac{\omega_1}{2\pi\eta(\tau)^2}
 e^{\eta_1u^2/(2\omega_1)}\vartheta_1(z,\tau),
 \qquad
 \Delta=(2\pi)^{12}\omega_1^{-12}\eta(\tau)^{24}.
\]
Legendre's relation gives
\[
 \eta(u)=\eta_1 z-\frac{2\pi i}{\omega_1\,\Im\tau}\Im z.
\]
Taking absolute values and using these exact factors yields
\[
 N(P)=|\Delta|^{1/12}|\sigma(u)|
                  e^{-\frac12\Re(u\eta(u))}.
\]
Twice the logarithm is therefore
\[
 \frac16\log|\Delta|+\Re(2\log\sigma(u)-u\eta(u)),
\]
which becomes the stated expression after inserting and subtracting \(u\zeta(u)\).

For the period statement, use Serre's function with the primary source's sign convention:
\[
 f_u(z)=\frac{\sigma(z+u)}{\sigma(z)\sigma(u)}e^{-\zeta(u)z}.
\]
Its logarithmic derivative is the algebraic differential
\[
 d\log f_u(z)=\frac12\frac{\wp'(z)-\wp'(u)}
                         {\wp(z)-\wp(u)}\,dz,
\]
and its lattice multiplier is \(\exp(\eta(\omega)u-\omega\zeta(u))\). Bertolin et al. construct from this exact factor system the extension corresponding to \(P\), under their stated polarization identification. In an algebraic fibre chart its exponential is \((z,t)\mapsto(\exp_Ez,e^tf_u(z))\); an algebraic lift of \(P\) with fibre coordinate \(r\ne0\) has vertical logarithm \(\log r-\log f_u(u)\). Sigma duplication gives
\[
 f_u(u)=-\wp'(u)e^{\Lambda_1},
 \quad \Lambda_1=2\log\sigma(u)-u\zeta(u).
\]
The factor \(-\wp'(u)\) is algebraic and nonzero because \(2P\ne O\). Thus the relative period is \(-\Lambda_1\) modulo a logarithm of an algebraic number, with exactly the claimed sign. Replacing a differential representative by its sum with \(c\,dz+df\) adds \(cu+f(P)-f(O)\), with algebraic \(c\) and endpoint values; adding \(d\log r\) changes the already allowed logarithm of an algebraic number.

**Branch wording to check.** Changing a branch of the ordinary complex logarithm \(\log\sigma(u)\) changes \(2\log\sigma(u)\) by \(4\pi i\mathbb Z\), hence by a purely imaginary integral multiple of \(2\pi\). If “choices of logarithms” is meant to include changing the elliptic logarithm \(u\) to \(u+\omega\), the exact change is instead
\[
 u\eta(\omega)-\omega\eta(u)+2\log\chi(\omega)
                         \pmod{4\pi i\mathbb Z}.
\]
It is purely imaginary by the real-linear quasiperiod formula, but its first term need not be an integral multiple of \(2\pi i\). The safe exact statement distinguishes the ordinary logarithm branch from the period lift using this displayed transport. This is a wording issue to compare with the target proof, not a claim that the norm identity fails.

## 4. ari:C.8.1: uniform norm bounds and the cusp

The theta Fourier series gives, for \(z=x+iy\),
\[
 e^{-\pi y^2/T}|\vartheta_1(z,\tau)|
 \le \sum_{n\in\mathbb Z}
       e^{-\pi T(n+\frac12+y/T)^2}.
\]
Poisson summation shows that the shifted Gaussian sum is at most the unshifted one: in its dual Fourier expansion all coefficients are positive, and \(\cos(2\pi kx)\le1\). Also
\[
 |\eta(\tau)|\ge e^{-\pi T/12}
                    \prod_{n\ge1}(1-e^{-2\pi nT}).
\]
Consequently
\[
 N(z,\tau)\le U(T):=
 \frac{e^{\pi T/12}(1+2\sum_{n\ge1}e^{-\pi Tn^2})}
      {\prod_{n\ge1}(1-e^{-2\pi nT})}.
\]
The function \(\log U(T)\) is convex: the logarithm of a positive exponential sum is convex, as is each \(-\log(1-e^{-2\pi nT})\). On the interval \(\sqrt3/2\le T\le T_{\max}\), the upper bound is therefore the larger endpoint value. The fresh directed interval computation gives
\[
 U(\sqrt3/2)<1.425900,\quad U(2)<1.694403,\quad
 U(7/5)<1.478416,\quad U(11/10)<1.419343.
\]
These prove all three target strict bounds.

For the cusp, translate \(z\) so \(|y|\le T/2\). At a zero of \(\wp\), its Fourier expansion gives
\[
 \left|\csc^2(\pi z)-\frac13\right|
 \le 8\sum_{n\ge1}\frac{n r^n}{1-r^n}
                         (1+\cosh(\pi nT)),\qquad r=e^{-2\pi T}.
\]
With \(s=e^{-\pi T}\), this is bounded by
\[
 \frac8{1-s^2}\left(
 \frac{s^2}{(1-s^2)^2}
 +\frac{s}{2(1-s)^2}+\frac{s^3}{2(1-s^3)^2}\right).
\]
It decreases for \(T\ge2\), and at2 it is less than0.007526, hence less than1/100. It follows that \(|\sin\pi z|<9/5\) and \(|y|>1/3\), the latter because
\(|\sin\pi z|^2\le\cosh^2(\pi y)\) and
\((1/3+1/100)^{-1}>\cosh^2(\pi/3)\).
The theta product then gives
\[
 N(z,\tau)\le\frac{18}{5}
 \exp\left(-\frac{\pi T}{6}-\frac{\pi}{9T}
                  +\frac{s}{1-s}+\frac{s^3}{1-s^3}\right).
\]
Its logarithm decreases for \(T\ge2\). At2 the fresh bound is1.062978, strictly below541/500. This proves the claimed cusp bound with margin.

## 5. ari:C.8.2: an independent full-disc proof

Put \(c(\tau)=(1-\tau)/2\), \(h=z-c(\tau)\), \(\delta=\tau-i\), and
\[
 \Phi(h,\tau)=\log\frac{\vartheta_3(h,\tau)}{\eta(\tau)},
 \qquad w(h,\tau)=\wp_\tau(c(\tau)+h).
\]
The exact half-period theta translation gives
\[
 \log N(c(\tau)+h,\tau)=\Re\Phi(h,\tau)
                         -\frac{\pi(\Im h)^2}{\Im\tau},
 \qquad w=-\Phi_{hh}-\eta_1.
\]
Work on the closed polydisc \(|h|\le1/10\), \(|\delta|\le1/50\). Absolute Fourier bounds for theta3 and explicit tails give
\[
 |\vartheta_3|\ge0.889178,\quad
 |\Phi_{hhhh}|<350,\quad |\Phi_{hh\tau}|<20,\quad
 |\Phi_{\tau\tau}|<2,\quad |\eta_1'|<1.1.
\]
The actual calculated majorants are respectively308.944,18.769,1.472 and1.064. In particular \(|w_\tau|<22\). At \(h=0\), differentiation of the even theta series gives \(|e_3''(\tau)|<100\), where \(e_3=w(0,\tau)\); the actual majorant is59.357. All these are analytic majorants on the entire polydisc, not sampled derivative values.

Let \(G=g_2(i)\); the fresh E4 bound gives \(189<G<190\). The exact square-lattice identities give
\[
 e_3(i)=0,\quad e_3'(i)=\frac{iG}{6\pi},\quad
 \Phi(0,i)=\frac12\log2,\quad
 \Phi_\tau(0,i)=0,\quad \Phi_{hh}(0,i)=-\pi.
\]
Here \(e_3(i)=0\) follows from the order-four lattice symmetry; \(\eta_1(i)=\pi\) follows from Legendre and the same symmetry; the theta product relations at \(i\) give \(\vartheta_3(0,i)/\eta(i)=\sqrt2\). The derivative \(e_3'\) follows from the heat equation at the double zero. These exact identities are also consistent with the separately read C.3.1 statement.

First all zeros of \(\wp_\tau\) can be represented in this \(h\)-disc. At \(\tau=i\), \(w\) satisfies
\[
 w''=6w^2-G/2,\qquad w(0)=w'(0)=0.
\]
The integral equation and a first-crossing bootstrap give \(|w(h,i)|<1/2\) on \(|h|\le1/10\), since
\[
 190(1/10)^2/4+3(1/10)^2(1/2)^2=0.4825<1/2.
\]
Consequently on the boundary
\[
 |w(h,i)|\ge189(1/10)^2/4
                -3(1/10)^2(1/2)^2=0.465.
\]
The difference \(|w(h,\tau)-w(h,i)|<22/50=0.44\). Rouché's theorem gives exactly two zeros, counted with multiplicity, in the \(h\)-disc; at \(\tau=i\) the same ODE estimate compares with \(-Gh^2/4\), giving exactly its double zero. An elliptic \(\wp\)-function has total zero multiplicity2, so these account for every zero modulo periods.

At a zero, evenness in \(h\) and the fourth-derivative bound imply
\[
 |e_3(\tau)|\le175|h|^2.
\]
Taylor's theorem in \(\tau\) gives
\[
 |e_3(\tau)|\ge
 \left(\frac{189}{6\pi}-1\right)|\delta|,
 \qquad |\delta|<20|h|^2.
\]
Taylor expansion of the holomorphic even function \(\Phi\), with the uniform bounds above, gives
\[
 \left|\Phi(h,\tau)-\frac12\log2+\frac\pi2h^2\right|
 \le\frac{350}{24}|h|^4+10|\delta||h|^2+|\delta|^2.
\]
Combining with the Gaussian term and using \(|\delta|\le1/50\), \(|h|^2\le1/100\), \(|\delta|^2\le(20/50)|h|^2\), yields
\[
 \log N-\frac12\log2
 \le-\left(\frac\pi2-C\right)|h|^2,\quad
 C=\frac{350}{2400}+\frac15+\frac25+
                       \frac{\pi/50}{1-1/50}<0.810.
\]
The coefficient \(\pi/2-C\) is greater than0.760. Thus the inequality is strict unless \(h=0\), which forces \(\delta=0\) by the preceding lower bound. Conversely the square-lattice value is \(\sqrt2\). This proves exactly the full stated closed disc and equality set before reading the target proof.

## 6. ari:C.8.3: comparison of discs

On \(|\tau-i|\le1/50\), the fresh q-series majorant gives \(|E_6''|<60\) (actual54.331). Also \(E_4(i)>7/5\), \(E_6(i)=0\), and the Ramanujan identity gives \(E_6'(i)=-\pi iE_4(i)^2\). Therefore on the boundary
\[
 |E_6|\ge\left(\pi(7/5)^2-\frac{60}{100}\right)\frac1{50}
                    >0.111150.
\]
The discriminant product gives \(|\Delta_0|\le r\exp(24r/(1-r))<0.002229\), with \(r=e^{-2\pi(49/50)}\). Hence
\[
 |t-1|=\frac{|E_6|^2}{1728|\Delta_0|}>0.0032087>1/500.
\]
Rouché first compares \(E_6\) with its nonzero linear term and shows that \(E_6\) has one zero in the disc. Since \(\Delta_0\) never vanishes in the upper half-plane, \(t-1\) has exactly two zeros counted with multiplicity. Comparing \(t-t_0\) with \(t-1\) now gives a zero strictly inside the disc for every \(|t_0-1|\le1/500\). The norm conclusion and equality statement follow from C.8.2 and modular invariance.

## 7. ari:C.8.4: duplication functions and all-level limit

The exact rational tangent law reconstructs \(2^jP\) from the displayed short model. The composition identity
\[
 \psi_{2n}(P)=2y(nP)\psi_n(P)^4
\]
then reconstructs the division functions without the old division-polynomial program. For \(n=2^k\), \(k=1,2,3\), the new exact calculation gives
\[
 \psi_n(P)=
 \frac{n\,3^{n^2/4-1}}{2^{n^2/2-1}}\,
 t^{2(n^2-1)/3}(t-1)^{n^2/4}A_k(t-1),
\]
with each of the three displayed \(A_k\) exactly as in the target statement. Inserting \(\Delta=27t^8(t-1)^3\) into C.4.2 cancels the \(t\)-powers and leaves
\[
 (N(P)/\sqrt2)^{n^2}
  =\frac{3^{3/4}}{2n}\,
       N(nP)|t-1|^{-1/4}/|A_k(t-1)|.
\]
For \(|u|\le1/28\), the triangle inequality gives
\[
 |A_3(u)|\ge1-|u|\sum_{j=1}^5|[u^j]A_3|(1/28)^{j-1}.
\]
The exact rational sum is less than10, proving the stated lower bound.

For arbitrary \(k\), the identity defining \(E_k\) follows directly from C.4.2. The limiting constant does not require computing higher division polynomials. Near the square lattice, C.3.1 gives
\(\delta=-(3\pi i/2)h^2+O(h^4)\); the modular identity yields
\[
 t-1=(27G/16)h^4+O(h^6).
\]
For even \(n\), \(nP\) is represented by \(nh\) modulo the period lattice, exactly because \(n(1-\tau)/2\) is a period. The simple zero of the normalized norm at the origin gives
\[
 N(nP)=nG^{1/4}|h|(1+o(1)),\qquad N(P)\longrightarrow\sqrt2.
\]
Hence
\[
 E_k\longrightarrow
 \frac{(27G/16)^{1/4}}{nG^{1/4}}
 =\frac{3^{3/4}}{2n}.
\]
This also proves the limit through arbitrary complex directions and fixes the scalar without replacing the lattice normalization.

## 8. ari:C.8.11: derivative identities

Use the source period formula
\(\beta^{\rm part}=(6i/\pi)\log(\vartheta_1(\mu,\tau)/(2\sqrt3\eta))\).
Put \(V=\vartheta_1'/\vartheta_1\), \(W=V+2\pi ia\), \(a=\Im\mu/T\), and \(m=\mu'\), \(R=m-a\). The heat equation and
\(V_z=-\wp-\eta_1\), \(\eta'/\eta=i\eta_1/(4\pi)\), give on \(\wp(\mu)=0\)
\[
 \partial_\tau\log(\vartheta_1/\eta)=V^2/(4\pi i).
\]
Since \(L=\Re\log(\vartheta_1/\eta)-\pi(\Im\mu)^2/T\), Wirtinger differentiation gives
\[
 L_\tau=\frac{V^2}{8\pi i}+\frac{Vm}{2}
                  +\pi iam-\frac{\pi i a^2}{2}
       =\frac{W(W+4\pi iR)}{8\pi i}.
\]
The period formula gives
\[
 \frac{(\beta^{\rm part})'}6=\frac{V^2}{4\pi^2}
                                      +\frac{iVm}{\pi};
\]
subtracting \(m^2\) is exactly \((W+2\pi iR)^2/(4\pi^2)\). The new symbolic program checks these identities after treating conjugate variables as independent.

Differentiate \(V_z=-\wp-\eta_1\) using the heat equation. Substituting \(\wp''=6\wp^2-g_2/2\) and the Ramanujan relation for \(\eta_1'\) yields
\[
 2\pi i\,\wp_\tau=
 2\wp^2-2\eta_1\wp-g_2/3+V\wp'.
\]
At a zero, implicit differentiation gives
\[
 \mu'=\frac{g_2}{6\pi i\,p}-\frac{V}{2\pi i},
 \quad R=\frac{g_2}{6\pi i\,p}-\frac{W}{2\pi i}.
\]
Substituting this into the first derivative gives exactly
\(iW(3Wp-2g_2)/(24\pi p)\). The ordinary-chart hypothesis excludes the ramification where this division by \(p\) is unavailable.

## 9. ari:C.8.12: modular invariants, endpoint limits and radial decrease

Integer period translation fixes \(W\), since the theta logarithmic derivative and the Gaussian correction have opposite additive changes. Under \((z,\tau)\mapsto(z/(c\tau+d),(a\tau+b)/(c\tau+d))\), the theta transformation formula gives
\[
 W\mapsto(c\tau+d)W,\quad
 p\mapsto(c\tau+d)^3p,\quad g_2\mapsto(c\tau+d)^4g_2.
\]
Changing the zero branch \(\mu\mapsto-\mu\) changes both \(W,p\) by−1. Thus \(X=3Wp/g_2\) and \(F=1-X\) are well defined on the modulus wherever \(g_2\ne0\).

The modular identities give
\[
 \frac{t'}t=-\frac{9i}{\pi}\frac{g_3}{g_2},
 \quad p^2=-g_3,\quad
 \frac{t}{t-1}=\frac{g_2^3}{27p^4},
 \quad
 \frac{t-1}{t'}=-\frac{3\pi i\,p^2}{g_2^2}.
\]
Multiply the final formula by the C.8.11 expression for \(L_\tau\). The result is \(X(X-2)/24\), exactly as claimed. For a real function, radial differentiation along \(t=1+re^{i\theta}\) is twice the real part of \((t-1)L_t\), which proves the second formula with denominator12. The same substitution for \(R\) gives
\(6\pi ipR/g_2=1-3Wp/g_2=F\).

At \(t=1\), \(p\to0\), \(W\) remains bounded and \(g_2\ne0\), so \(X\to0\). At \(t=0\), let \(\delta=\tau-\rho\) and \(p_0=\wp'_\rho(\mu_0)\ne0\). The read C.3.2 statement gives
\[
 R=\frac{3p_0}{8\pi^2}\delta+O(|\delta|^2),\qquad
 g_2=\frac{3ip_0^2}{\pi}\delta+O(\delta^2).
\]
Here the nonholomorphic correction \(a+1/3\) is \(O(|\delta|^2)\), so it does not affect the linear term. The exact formula for \(F\) therefore gives \(F\to3/4\), hence \(X\to1/4\), in every complex direction. These limits are compatible with the branch and modular transports just proved.

Finally \(X(X-2)=F^2-1\). If \(|F|<1\), then \(\Re(F^2-1)\le|F|^2-1<0\), so the radial derivative is strictly negative. No unproved global bound \(|F|<1\) is asserted here.

## Computational records and pending comparison

Fresh programs:

- S6_SERIES_PUBLISH_I_nine_analytic_bounds.py/.json/.out: explicit entire-domain Fourier/product majorants and tails for C.8.1–3.
- S6_SERIES_PUBLISH_I_nine_symbolic.py/.json/.out: rational tangent doubling, exact \(A_k\), finite local-height algebra, Weierstrass scaling, Wirtinger identities and radial substitution.

The target proofs are still unopened when this derivation record is written. The primary source PDFs will be viewed at the precise cited locators, then a seal will record hashes before the target proof comparison. Any computation in the printed proof not covered by these alternative arguments will be separately identified and recomputed; it will not be retrospectively described as a preread step.

## Primary-locator completion before comparison

The downloaded v2 PDFs were actually viewed at DeMarco–Mavraki pp.5–6, §2.1, and Bertolin–Philippon–Saha–Saha pp.7–8 (§2.3, equations (2.10)–(2.13), Definitions2.3–2.4), p.24 (Table1 and the elliptic differential), pp.26–27 (§6.1 and the explicit one-motive). The latter section is §2.3, correcting the earlier provisional §2.2 pointer. The elliptic factor f_u has divisor (−P)−(O); the principal polarization used to identify its extension class with P is explicitly P↦t_P^*O(O)⊗O(O)^{-1}=O((−P)−(O)). Under the alternative identification P↦O((P)−(O)), the class is −P. This exact dual-identification map is part of the period comparison and should be stated if a sign convention is needed.
