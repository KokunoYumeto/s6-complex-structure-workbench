# Paper I night:P5.7 — frozen statement-directed source/parameter derivation

## Exposure and exact scope

Checker: `/root/i_marking_fresh`. The receiving target proof and all earlier parameter-comparison reports remain unopened at this freeze. The prior inv:B1.0 task exposed the receiving period/parameter definitions and affine covariance. The root's follow-on brief named the expected relation a=c+delta; it supplied no definition of delta or proof. Thus this check claims a pre-target-proof derivation with that disclosed conclusion exposure, rather than claiming the expected formula was unknown.

Inputs are the exact target remark, its cited receiving theorem statements, literal receiving construction definitions, primary DGKX period/generator data, and the AC2026 uniqueness/cusp conditions. I actually viewed DGKX v1 pp. 3,81,82,85,95; DGKX v2 pp. 1–3; AC2026 pp. 14–15. Those page views included surrounding primary proof text. I reviewed all 42 mathematical statement environments in the complete supplied DGKX v2 source and every extracted whole-source context for the relevant concepts. I read the retained official arXiv v1 HTML date text. I did not independently re-prove the cited tangent-cohomology, Kuranishi, or full-automorphism theorems, nor authenticate the claimed 8 September public posting.

The exact task is to compare the fixed standard (3,4,infinity) receiving conclusions with primary assertions and to exhibit the parameter/atlas morphism that makes that comparison precise. The larger multiplicity and arbitrary-twist assertions in some cited receiving theorems receive no additional check credit here. No alias receives an automatic event.

A temporary image-reading mistake is explicitly resolved: I initially read AC p.15(iv)'s scaled sign as +infinity. A new 3x PDF-region render and text extraction both show -infinity. I retracted the caveat before this freeze. There is no source-sign defect.

## 1. Fix the same standard data by their actual construction

The receiving introduction explicitly adopts the Claude–Alpöge construction with its specified periodic cusp fan, clockwise finite-root generators, affine translations, ordered lattice, and untwisted cusp collar. It fixes the same base points p1=0,p2=1,p0=infinity and the ordered lattice (hatgamma,hatu,hatw,hatdelta). Its mu is the cusp-selected solution, and its particular beta satisfies (beta_part+tau)(p0)=0.

DGKX's primary Proposition period-data-existence adopts AC Theorem 3.4 in that same ordered basis. AC Definition 3.1 and Theorem 3.4(i) specify tau by j(tau)=1728t and the two generator laws, with tau(z1)=exp(pi*i/3), tau(z2)=i. Theorem 3.4(ii) specifies mu by its two affine laws and boundedness on the distinguished g0-invariant cusp component U_r. These uniqueness statements identify the tau and mu in the two adopted constructions through the identity base/lattice marking; equality does not follow merely from reusing the symbols.

The standard translations are the same actual columns

v1=(1,2,-4,0), v2=(-1,-3,3,0), (m1,m2)=(3,4).

The receiving standard-data definition and the primary DGKX twist display give these exact vectors. The primary construction also specifies untranslated cusp gluing. This is the fixed standard scope of night:P5.7.

## 2. Reconstruct the receiving generator equations from covariance

Write t=tau(z), m=mu(z), b=beta(z), and set

Yt=t*tau(g_j z), Ym=t*mu(g_j z), Yb=t*(beta(g_j z)-beta(z)).

The factor t is nonzero because Im(t)>0. The receiving covariance R_j Pi=Pi(g_j z) A_j is supplied in the prior definition input. Clearing its denominator gives a linear system for Yt,Ym,Yb with polynomial right sides in t,m. The new exact program forms these equations before choosing the transformed functions and solves the coefficient systems with integer minors and Cramer's rule.

For j=1 the nonzero scalar equations reduce to

6Yt+6Ym=6t-6m,
Yt=t-1,
6Ym+Yb=6m-6m^2+2t,
Ym=1-m.

Their unique solution is

Yt=t-1, Ym=1-m, Yb=2t-6(1-m)^2.

For j=2 the corresponding equations yield

Yt=-1, Ym=t+m, Yb=-3t-6m^2.

Consequently both receiving and primary functions have the exact laws

tau(g1 z)=(tau-1)/tau, tau(g2 z)=-1/tau,
mu(g1 z)=(1-mu)/tau, mu(g2 z)=1+mu/tau,
beta(g1 z)-beta=2-6(1-mu)^2/tau,
beta(g2 z)-beta=-3-6mu^2/tau.

The program verifies every original covariance entry after reconstructing the numerators, with zero exact polynomial residuals. The two beta increments are exactly the primary phi1,phi2.

## 3. Derive the constant difference, including its sign

Define h=beta_part-beta0 on the common uniformizing cover. The equal generator increments give h(g1 z)=h(z) and h(g2 z)=h(z). These generators generate the specified group, so h is invariant under every group element.

At a finite root point, expand h in its holomorphic root coordinate s. Invariance under s -> exp(-2*pi*i/m_j)*s makes the coefficient of s^n vanish unless m_j divides n. Thus h is a holomorphic function of the quotient coordinate s^(m_j) there. This gives an explicit descent across the two finite points.

At the distinguished cusp, beta_part+tau and beta0+tau extend holomorphically by the adopted AC cusp conditions and the primary DGKX cusp decomposition. Their difference h therefore extends there as well. The descended h is holomorphic on the complete base P1. By the maximum principle on that compact connected surface, h is constant. Denote the constant by

delta=beta_part-beta0.

The receiving cusp value now determines its sign:

0=(beta_part+tau)(p0)=(beta0+tau)(p0)+delta,
so delta=-(beta0+tau)(p0).

This also supplies a direct derivation of the relevant conclusion of AC Theorem 3.4(iii) for these two actual solutions; all its distinguished-cusp hypotheses are retained.

## 4. Solve the parameter map and its domain exactly

The two period matrices are

Pi_c=[[6mu,tau,1,0],[beta_part+c,mu,0,1]],
Omega_a=[[6mu,tau,1,0],[beta0+a,mu,0,1]].

The identity of their lower-left entries is beta0+a=beta0+delta+c, hence

F(c)=a=c+delta, F^(-1)(a)=a-delta,
Omega_(c+delta)=Pi_c.

The other seven entries coincide through the already specified identity of tau,mu and ordered basis. The new program reconstructs the coefficients of the affine map a=alpha*c+kappa*delta+eta by coefficient comparison and obtains (alpha,kappa,eta)=(1,1,0). It verifies the full potentially varying period entry as a zero polynomial residual.

For the admissible domains, let

D0=Im(beta0)-6(Im(mu))^2/Im(tau),
Dpart=Im(beta_part)-6(Im(mu))^2/Im(tau).

Then Dpart=D0+Im(delta). Adding this fixed real number gives an order-preserving bijection between the sets of upper bounds of D0 and Dpart. Taking their infima yields

M=M0+Im(delta).

Both suprema are finite in the actual cusp-bounded construction: beta0=-tau+bounded, mu is bounded, and Im(tau) tends to +infinity on U_r, so D0 tends to -infinity; continuity on the remaining compact base region supplies an upper bound. This agrees with the correctly read primary AC(iv) and DGKX admissibility statements.

The half-plane map is therefore exact:

Im(F(c))+M0=Im(c)+M,
F:{Im(c)<-M} -> {Im(a)<-M0}.

The displayed inverse a -> a-delta maps back, so F is a biholomorphism of the actual admissible half-planes. Its derivative is 1.

## 5. Exhibit the morphism on the actual compactified charts

On the common universal core chart the map is

Phi(z,c,zeta)=(z,c+delta,zeta).

For every lattice vector lambda, the lattice arrow is zeta -> zeta+Pi_c(z)lambda on the receiving chart and zeta -> zeta+Omega_(c+delta)(z)lambda on the primary chart. The equality of periods makes these arrows identical under Phi. The deck matrices R_g and A_g are the same standard data, so Phi also respects every deck arrow.

On a finite root chart, the actual affine arrow is

(z,c,zeta) -> (g_j z,c,R_gj(z)zeta+Pi_c(g_j z)*v_j/m_j).

The primary chart has the same formula with Omega_a and parameter a. The identified period matrices, the literal shared v_j, and the retained denominators 3 and 4 make Phi commute with each finite arrow, including the central root fibre. The identity root coordinate and identity zeta are the local morphism; its inverse uses a-delta.

For the cusp write the primary period block as

Z_a=s*B0+C0(q)+a*E21,
B0=[[0,1],[-1,0]],
C0(q)=[[6mu(q),h(q)],[beta0(q)+tau(q)-h(q),mu(q)]],
q=t_c=exp(2*pi*i*s), tau=s+h(q).

The receiving holomorphic cusp block is Cpart(q)=C0(q)+delta*E21. Hence

Cpart(q)+c*E21=C0(q)+(c+delta)*E21.

The standard periodic fan, integer shear B0, and untranslated cusp gluing are fixed inputs. Their toric action multiplies the dense coordinates by exp(2*pi*i*C_a(q)*lambda) and the monomial shear q^(B0*lambda); the equality above identifies both factors. The toric coordinates and q are unchanged by Phi. The source and receiving cusp maps therefore commute on every toric chart, with the displayed inverse. Taking common smaller valid collars yields the same gluing cover, so these local maps descend and glue to an isomorphism of compact pairs over the identity of B.

This establishes the exact chart morphism used by the comparison. It asserts only the fixed standard data specified by the target, with the stated identity marking and constant parameter translation.

## 6. Transport each of the four conclusions

The receiving tangent/Kuranishi theorem is specialized at k=l=1, so gcd(3k,4l)=gcd(3,4)=1, z=kl=1, and d=3k+4l=7. Its hypotheses and standard-data restrictions are retained. It gives the tuple (1,1,1,0), a smooth reduced one-dimensional Kuranishi germ, and local miniversality.

The actually viewed primary DGKX v1 Theorem 6.12 on pp.81–82 gives (h0,h1,h2,h3)=(1,1,1,0) for every a in its admissible half-plane. Proposition 6.16 on p.85 gives Kur(X_a) congruent to (C,0), smooth and reduced, and local miniversality after local reparametrization. Theorem 1.3 on p.3 states the same deformation conclusions. F maps the entire receiving admissible half-plane onto the primary half-plane, so these statements compare at precisely a=F(c).

The vector e=Pi_c*hatdelta=(0,1) is the primary vector u2. The chart morphism is the identity in zeta, and dF/dc=1; it therefore carries the receiving Kodaira–Spencer representative e tensor [gamma] for partial_c to the primary u2 tensor [gamma] for partial_a. This identifies the relevant tangent line and the parameter derivative explicitly.

The receiving automorphism theorem gives C/Z acting by zeta -> zeta+alpha*e, with exponential alpha mod Z -> exp(2*pi*i*alpha). The primary Theorem 7.14 on p.95 gives the full automorphism group, and its preceding Proposition 7.13 gives that same translation quotient. Conjugation by the constructed Phi maps each translation alpha to itself because Phi fixes zeta and e=u2. Thus the isomorphism of full groups is explicit, including the exponential identification with C*. The identity-component assertion in Theorem 1.3 is not substituted for the full-group statement; the latter is actually present at Theorem 7.14.

For two receiving parameters c,c', set a=c+delta and a'=c'+delta. Exact subtraction gives

a'-a=c'-c.

The primary Theorem 1.4 on p.3 states X_a congruent to X_a' exactly when a'-a is in 2Z, and also identifies the pair-isomorphism criterion. The receiving criterion is thereby the same exact subgroup condition c'-c in 2Z. The cited receiving theorem writes c-c' in 2Z; the explicit group automorphism 2n -> -2n identifies the two displayed signs. No change of lattice period is introduced.

On the quotient parameters,

F(c+2n)=F(c)+2n,
w_DGKX=exp(-pi*i*a)=exp(-pi*i*delta)*w_receiving.

The multiplicative map is multiplication by the nonzero constant exp(-pi*i*delta). Its inverse multiplies by exp(pi*i*delta). The radii satisfy exp(-pi*M0)=exp(pi*Im(delta))*exp(-pi*M), so this is also the exact punctured-disc morphism. These equalities are included in the exact coefficient program.

## 7. Version 2's printed scope

I actually viewed the v2 title, abstract, contents, and introduction on pp.1–3. The title is `Oka Geometry of Complex Six-Spheres`. The contents has the period/compactification, Oka, and modifications sections plus two appendices.

A newly written environment-boundary scanner inventories the complete supplied v2 TeX source after replacing TeX line comments by spaces while preserving offsets. All six declared mathematical statement environments are included. I read all 42 blocks: 7 theorems, 15 propositions, 14 lemmas, 4 corollaries, 2 definitions, and 0 remarks. I also read every whole-source context for cohomology, Kuranishi, miniversality, automorphisms, parameter-period syntax, tangent dimensions, and deformations.

The printed v2 statement inventory omits the four v1 assertions under comparison. In particular, the whole-source contexts for local toric/lattice automorphisms concern the explicit cusp chart actions, and the integral H2 contexts concern covers and blow-up Chern classes. Their exact statements are in the inventory; none asserts the tangent tuple, the Kuranishi/miniversality conclusion, the full Aut(X_a)=C* theorem, or the exact 2Z member-equivalence theorem. No Kuranishi, miniversality, or cohomology term appears in the complete comment-stripped source. This is a textual comparison of the supplied versions and does not negate the mathematical assertions or claim that no mathematical relation exists.

The inventory program, its complete source contexts, and the full extracted statement text are retained. I have not claimed a rendered-page read of every v2 page or a re-proof of its 42 assertions.

## 8. Chronology and credit, with exact evidentiary limits

The retained official arXiv v1 HTML, whose hash is bound in the packet, visibly states `Submitted on 23 Sep 2026 (this version)` and `Wed, 23 Sep 2026 17:09:17 UTC`. The new program checks those exact retained text strings. The primary v1 p.3 actually states the equivalence as Theorem 1.4. Thus this part of the date/source comparison is directly supported by the supplied official record and theorem page.

The received original Paper I statement reports that the exact 2Z proof was in the public working edition by 8 September 2026. The current target says that the working-edition proof is dated 8 September 2026. The packet supplies the authorial historical assertion; it supplies no independently authenticated 8 September public deposit. A later repository commit records later file content and does not determine an earlier public-availability timestamp. Accordingly the September 8 sentence has authorial-testimony scope in this check. It is preserved as attributed history; it has not received independent date authentication.

The receiving statement also reports that the tangent/deformation calculations were re-derived after reading v1. This is the author's reported work history. Reading source texts and checking the mathematics does not independently authenticate that process chronology. Credit for the re-derived appendix and the sole September 8/September 23 comparison must retain these exact evidentiary scopes.

## 9. Pre-proof conclusion and computation scope

The mathematical/source comparison is established by the exact fixed-data chart map and the actually viewed primary statements. The source v2 omission is supported by the complete printed-statement inventory plus full-source context review. The chronology is supported as an official September 23 submission record and an attributed authorial September 8 report.

The new program `S6_SERIES_PUBLISH_I_nightP57_exact_reconstruction.py` reconstructs generator numerators from polynomial coefficient systems using integer minors, derives the affine parameter coefficients, and verifies all period, cusp, difference, 2Z-equivariance, and half-plane/radius coefficient identities exactly. Its output is `S6_SERIES_PUBLISH_I_nightP57_exact_reconstruction_output.json`. All assertions passed. It was written and run before the receiving target proof was read; no legacy comparison code was read or run for this target.

The documentary inventory is separately recorded in `S6_SERIES_PUBLISH_I_nightP57_v2_inventory.py`, `.json`, and `S6_SERIES_PUBLISH_I_nightP57_v2_statement_inventory.txt`. Exact text scans do not authenticate chronology or independently prove the cited geometric results.

This derivation will be content-hashed and frozen before opening the complete receiving target proof. Later proof comparison and any recommended wording guards belong in separate records.
