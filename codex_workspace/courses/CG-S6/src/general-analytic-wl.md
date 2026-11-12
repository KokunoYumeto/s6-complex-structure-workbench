# Weighted solutions and local approximation {#general-analytic-wl}

Written by GPT-6 Astra (OpenAI), at Ultra, October 2026. Independent exposition: CC0-1.0.

Read this argument with the [general surface theorem](general-proper-flat-surface-base-change.md#general-surface-theorem) and its [prerequisite guide](general-proper-flat-surface-base-change.md#general-prerequisites). Result identifiers link to the exact arguments in this companion family.

The supporting arguments retain linear mathematical notation: `->` denotes a map, `^` an exponent or cohomological degree, `_` a subscript, and `direct_sum` a direct sum. Parentheses specify grouping. Algebraic quotients and completed topological tensor products are distinguished explicitly; a quotient is not silently replaced by its completion.

The curvature identity used in WL-4–WL-6 is supplied in [BK-5](general-analytic-bk.md#BK-5). The conditional wording in the argument identifies that exact input; it is not an instruction to assume the identity without its proof.

## Conventions {#WL-conventions}

<p>For each form degree k, D_k is maximal distributional dbar: L2_(n,k)(M,E,h exp(-Phi),omega_tilde) -&gt; L2_(n,k+1), with domain those forms whose distributional derivative is in the target L2 space. D_n=0 on the entire top-degree space. The formal weighted adjoint from degree k to k-1 is delta_k; <a href="general-analytic-wl.md#WL-1">WL-1</a> proves delta_k=D_(k-1)^* on the relevant maximal domain.</p>

<p>The compactly supported Hilbert inner product is linear in its first variable. Adjoint identities use that convention. Let L be exterior multiplication by omega_tilde and Lambda=L*. For operators of total-degree parity a,b, [A,B]=AB-(-1)^(ab)BA. A differential form inside a commutator denotes its exterior-multiplication operator.</p>

<p>The Chern curvature convention is D_E^2=Theta(E); in a holomorphic frame with metric matrix h, its (1,0) connection matrix is h^(-1) partial h. For h_Phi=exp(-Phi)h, Theta(E_Phi)=Theta(E)+partial dbar Phi times Id. The real (1,1) curvature form is iTheta.</p>

<p>For the fixed base metric omega_tilde, T=[Lambda,[Lambda,(i/2)partial dbar omega_tilde]]-[partial omega_tilde,(partial omega_tilde)*]. This is a smooth zero-order self-adjoint endomorphism in the source identity. It acts trivially on the E factor and therefore does not change when the bundle metric is multiplied by exp(-Phi). Its occurrence is not suppressed by pretending omega_tilde is Kahler.</p>

## WL-0. An adapted metric with quantitative sums of Levi eigenvalues {#WL-0}

<p class="statement"><strong>Statement.</strong> For 1&lt;=q&lt;=n and epsilon=1/(2q), there is a smooth Hermitian metric omega for which every Levi eigenvalue of psi is &gt;=-epsilon and the largest n-q+1 equal 1. Consequently every sum of k&gt;=q eigenvalues is &gt;=c_q=1-(q-1)/(2q)&gt;1/2.</p>

**Proof.**

<p id="WL-0-p1">Start with any smooth Hermitian metric omega_0, constructed by locally finite positive partitions of chart metrics. Write its Levi endomorphism as A_0 and its ordered eigenvalues as gamma_1&lt;=...&lt;=gamma_n. The finite Hermitian spectral theorem follows by maximizing the real Rayleigh quotient on the complex unit sphere: variations in w and iw show that a maximizer is an eigenvector, its orthogonal complement is invariant, and induction diagonalizes A_0. The eigenvalue min-max characterization follows by intersecting a test subspace with the spans of the first or last eigenvectors. It gives |gamma_j(A)-gamma_j(B)|&lt;=||A-B||, so gamma_q is continuous and strictly positive. Refine into precompact sets on each of which gamma_q exceeds a positive constant 2b_alpha, take a subordinate partition lambda_alpha, and put eta=sum lambda_alpha b_alpha. Then eta is smooth and 0&lt;eta&lt;=gamma_q/2.</p>

<p id="WL-0-p2">Choose a smooth function beta equal to 1 for t&lt;=0, equal to 0 for t&gt;=1, and between 0 and 1. Put a=1+epsilon^(-1) and theta(t)=t+beta(t) exp(-at). It is positive: for t&lt;0, exp(a|t|)&gt;=a|t|, hence theta(t)&gt;=|t|/epsilon; at t=0 it is 1; and for t&gt;0 it is at least t. Also theta(t)=t for t&gt;=1. Define the positive endomorphism A=eta theta(eta^(-1) A_0), and set omega(v,w)=omega_0(Av,w).</p>

<p id="WL-0-p3">This construction is smooth even at repeated eigenvalues. In a smooth omega_0-orthonormal frame over a precompact chart, the spectra of eta^(-1)A_0 stay in one compact interval. Replace theta outside that interval by a compactly supported smooth scalar function f. The exact spectral formula f(B)=(2pi)^(-1) integral Ff(t) exp(itB)dt follows by diagonalizing the fixed matrix B and applying the one-dimensional inversion theorem. Differentiating exp(itB(x)) once gives i integral_0^t exp(i(t-s)B)(partial B)exp(isB)ds; repeated parameter derivatives have polynomial growth in |t| on the chart because the exponentials are unitary. Ff decreases faster than each inverse polynomial, so differentiation under the integral is justified to every order. The formula is equivariant under frame changes, proving smoothness of A independently of eigenvector choices.</p>

<p id="WL-0-p4">The new eigenvalues are lambda_j=gamma_j/[eta theta(gamma_j/eta)]. If gamma_j&lt;0, the bound on theta gives lambda_j&gt;=-epsilon. If gamma_j&gt;=0, lambda_j&gt;=0. For j&gt;=q, gamma_j/eta&gt;=1, so lambda_j=1. A set of k indices contains at least k-q+1 of these last indices; its sum is therefore at least k-q+1-(q-1)epsilon&gt;=c_q. This proves the stated bound without adding two unrelated q-positive forms.</p>

∎

## WL-1. A complete metric and the actual joint graph domain {#WL-1}

<p class="statement"><strong>Statement.</strong> The adapted metric admits a complete conformal enlargement. For every fixed smooth bundle weight, compactly supported smooth forms are dense for the joint graph norm of D and its weighted formal adjoint, which equals the Hilbert adjoint on its maximal distributional domain.</p>

**Proof.**

<p id="WL-1-p1">Shift psi so psi&gt;=0. With the real Riemannian norm induced by omega, set rho=log(1+|dpsi|_omega^2) and omega_tilde=exp(rho)omega. Then |dpsi|_omega_tilde&lt;=1. Along any piecewise smooth path, the change of psi is no greater than its length. Thus a metric Cauchy sequence in a connected component has bounded psi and lies in a compact closed sublevel. It has a convergent subsequence in the manifold topology, which agrees locally with the metric topology; its Cauchy property gives convergence of the whole sequence. This proves completeness. Disconnected components cause no difficulty, since all arguments are componentwise and the exhaustion still has compact sublevels.</p>

<p id="WL-1-p2">Take a smooth kappa equal to 1 on (-infinity,1], zero on [2,infinity), between 0 and 1, with bounded derivative, and set eta_j=kappa(psi/j), j&gt;=1. Its support is compact, it tends locally to 1, and |deta_j|_omega_tilde&lt;=||kappa&#x27;||_infinity/j. Distributional Leibniz rules give D(eta_j u)=eta_j Du+(dbar eta_j) wedge u and delta(eta_j u)=eta_j delta u-(exterior multiplication by dbar eta_j)*u. The adjoint in the last term is pointwise; it is unaffected by a common scalar bundle weight in adjacent degrees. Exterior multiplication and contraction have operator norm at most the covector norm. Hence the extra terms tend to zero in L2, and dominated convergence handles the three terms multiplied by eta_j. This proves graph approximation by compactly supported forms, with no uniform bound on derivatives of Phi required.</p>

<p id="WL-1-p3">For such a compact support, choose finitely many relatively compact charts, smooth bundle frames and a subordinate partition. Each localized component has D and delta in L2 because partition commutators are zero-order. In a chart these are finite matrices of first-order operators with smooth coefficients. Apply the complete commutator proof of the imported Friedrichs Lemma 3.1 entry by entry to ordinary convolution. Both operators then converge in L2 together with the form; the finitely many chart metrics and weights are bounded above and below, so the same holds in their weighted norms. Sum the smooth approximants and choose a diagonal sequence after the eta_j cutoff. This proves density in the joint maximal graph domain, and separately in the maximal D graph domain.</p>

<p id="WL-1-p4">If u is in the Hilbert-adjoint domain of D, testing against compactly supported smooth forms identifies D*u with the formal adjoint delta u as a distribution. Conversely, if u and delta u are in L2, integrate by parts against compactly supported smooth v and pass to every v in the maximal D domain using the just-proved graph density. The identity (Dv,u)=(v,delta u) gives u in Dom D* with D*u=delta u. Maximal distributional D is closed: convergence of u_j and Du_j in L2 implies convergence on compactly supported distribution tests. Its kernel is closed, its domain is dense, and D_(k+1)D_k=0 whenever the first derivative lies in L2, because dbar squared is zero in each holomorphic frame. These are the exact Hilbert-complex hypotheses used in <a href="general-analytic-wl.md#WL-4">WL-4</a>.</p>

∎

## WL-2. Local first-order ellipticity from L2, with fixed-coefficient interior bounds {#WL-2}

<p class="statement"><strong>Statement.</strong> For Q=(D,delta) at any fixed degree and with fixed smooth metrics and weight, u in L2_loc and Qu smooth imply u smooth. If Qu=0 on an open V containing a compact K, every C^ell(K) norm of u is bounded by C_(ell,K,V)||u||_L2(V&#x27;) for a relatively compact intermediate neighbourhood V&#x27; of K in V. The constants depend on the fixed local coefficients, not on u.</p>

**Proof.**

<p id="WL-2-p1">For a real cotangent vector xi, the two principal symbols are exterior multiplication by zeta=xi^(0,1), up to a unit scalar, and its adjoint contraction. Their squared norms on a vector v add to |zeta|^2|v|^2. To verify this, if zeta is nonzero extend zeta/|zeta| to a unitary coframe and write v as the sum of its first-covector factor and its part with no such factor; these two parts are orthogonal, and the two operations extract their complementary norms. For real xi, zeta is nonzero whenever xi is nonzero, with |zeta|^2 a fixed positive multiple of |xi|^2 in the induced convention. Bundle and (n,0) factors are spectators. Thus Q has an injective real principal symbol in every degree, including degree zero and top degree.</p>

<p id="WL-2-p2">Write Q=sum A_j(x)partial_j+B(x) in smooth coordinate frames and freeze its principal coefficients at a point x_0. Plancherel from the imported Fourier theorem, applied to compactly supported smooth vector functions, gives ||grad v||_2&lt;=C||sum A_j(x_0)partial_j v||_2. Indeed the pointwise symbol lower bound controls |xi|^2|Fv(xi)|^2, and the common (2pi)^d factor cancels upon integration. Shrink the ball so C sum_j sup||A_j(x)-A_j(x_0)||&lt;1/2. The difference from Q is the small principal part plus bounded Bv. Move the former term to the left to obtain ||v||_H1&lt;=C_1(||Qv||_2+||v||_2) for compactly supported smooth v in this ball. Smooth densities and fibre norms are uniformly comparable on its closure; they change C_1 but not the estimate.</p>

<p id="WL-2-p3">Now suppose only u and Qu are L2 locally. Multiply by a compact cutoff in the ball; Q(chi u)=chi Qu+[Q,chi]u is L2. By the matrix Friedrichs argument in <a href="general-analytic-wl.md#WL-1">WL-1</a>, its smooth convolutions v_j converge with Qv_j in L2 and have support in a fixed smaller ball. Apply the preceding estimate to v_j-v_l. They are Cauchy in H1, and their L2 limit is chi u; closedness of distributional derivatives identifies the H1 limit. Thus u is H1 on the region where chi=1. This supplies the missing initial derivative, rather than assuming it.</p>

<p id="WL-2-p4">If u is H^m locally and Qu is H^m locally, differentiate a multi-index alpha of length m: Q partial^alpha u=partial^alpha(Qu)-[partial^alpha,Q]u as distributions. Expanding the commutator by the finite Leibniz rule gives only derivatives of u of order at most m: whenever a derivative hits a principal coefficient, the order on u drops by at least one before the one derivative already in Q is counted. All coefficients and their finitely many derivatives are bounded on a smaller compact chart. The base H1 argument applied to each partial^alpha u proves u in H^(m+1) locally. Induction gives all Sobolev orders when Qu is smooth. The same estimates, with nested cutoffs and a finite chart cover, give ||u||_Hm(K_neighbourhood)&lt;=C_m||u||_L2(V&#x27;) in the homogeneous case; at step m each cutoff or coefficient commutator is bounded by the preceding Hm norm on a slightly larger neighbourhood. One chooses finitely many nested neighbourhoods for each specified m, not a single constant for all m.</p>

<p id="WL-2-p5">For compactly supported smooth v on R^d and s&gt;ell+d/2, the imported Fourier weight formula and Cauchy-Schwarz give integral |xi|^ell|Fv(xi)|dx&lt;=C||v||_Hs: the square of |xi|^ell(1+|xi|^2)^(-s/2) is integrable by the same annular estimate as in Section 2. Fourier inversion therefore bounds all derivatives through order ell uniformly. Extend to Hs by smooth convolution and cutoff approximation; the uniform derivative limits agree with distributional derivatives. Apply this to local cutoffs of u and the preceding Hs estimate. This proves smoothness and the asserted C^ell interior bound. The proof is local on a possibly noncompact manifold and does not import a compact-manifold Garding statement with incompatible hypotheses.</p>

∎

## WL-3. Levi action on top holomorphic degree and actual weight selection {#WL-3}

<p class="statement"><strong>Statement.</strong> For every holomorphic Hermitian E on M with 1&lt;=q&lt;=n, one can choose a smooth convex increasing chi_0 such that A_(chi_0,k)=[iTheta(E_(chi_0 composed with psi)),Lambda]+T&gt;=Id on (n,k)-forms for every k&gt;=q. Adding any convex nondecreasing function of psi preserves this. Given smooth g, an additional such weight can make g square integrable.</p>

**Proof.**

<p id="WL-3-p1">At one point choose a unitary coframe zeta_j diagonalizing a real (1,1) form beta=i sum lambda_j zeta_j wedge bar(zeta_j). The identities for exterior multiplication e_j and its adjoint i_j are e_j i_j+i_j e_j=Id and anticommutation between different indices. Thus [beta wedge,Lambda] on zeta_I wedge bar(zeta_J) has eigenvalue sum_(j in I)lambda_j+sum_(j in J)lambda_j-sum_all lambda_j: in each index the pair commutator is +1 if both covectors occur, -1 if neither occurs, and zero if exactly one occurs; different pair indices commute. For holomorphic degree n, this becomes sum_(j in J)lambda_j. Under omega_tilde=exp(rho)omega, every Levi eigenvalue scales by exp(-rho), so <a href="general-analytic-wl.md#WL-0">WL-0</a> gives the lower bound c_q exp(-rho) on every (n,k), k&gt;=q. A positive semidefinite (1,1) form likewise has nonnegative action in these degrees; that assertion is not being extended to arbitrary (p,k).</p>

<p id="WL-3-p2">In a holomorphic frame, h_Phi^(-1)partial h_Phi=h^(-1)partial h-partial Phi Id. Differentiating with dbar gives Theta(E_Phi)=Theta(E)+partial dbar Phi Id, since dbar partial Phi=-partial dbar Phi. The chain rule for Phi=chi(psi) gives i partial dbar Phi=chi&#x27;(psi)i partial dbar psi+chi&#x27;&#x27;(psi)i partial psi wedge dbar psi. The latter summand is positive semidefinite if chi&#x27;&#x27;&gt;=0. The zero-order endomorphisms B_k=[iTheta(E),Lambda]+T have locally bounded norms for the fixed metric. Choose a positive smooth function a larger than all these finitely many norms by a locally finite partition with upper bounds on precompact supports. Then A_(chi,k)&gt;=(-a+c_q exp(-rho)chi&#x27;(psi))Id for k&gt;=q. This is only an algebraic inequality between zero-order operators; the analytic basic inequality is the separate input in <a href="general-analytic-wl.md#WL-4">WL-4</a>.</p>

<p id="WL-3-p3">Here is an explicit smooth convex majorant construction. For every integer j&gt;=0 let a_j&gt;=1 be a nondecreasing sequence exceeding the supremum of (a+1)exp(rho)/c_q on {psi&lt;=j+2}. Let sigma be smooth nondecreasing, zero for t&lt;=0 and one for t&gt;=1. Set h(t)=a_0+sum_(j&gt;=1)(a_j-a_(j-1))sigma(t-j+1), a locally finite smooth sum, and chi_0(t)=integral_0^t h(s)ds. For t in [j,j+1], h(t)&gt;=a_j; also h&#x27;&gt;=0. Thus chi_0 is increasing and convex and the desired operator lower bound is &gt;=1. Adding chi_1 with nonnegative first and second derivatives contributes a nonnegative operator by the sum-of-eigenvalues bound just proved, even though the Levi form itself need not be positive semidefinite.</p>

<p id="WL-3-p4">For a smooth g in any of the relevant degrees, set M_j=integral_(psi&lt;=j+1)|g|^2 exp(-chi_0(psi))dV, finite by compactness. Choose nonnegative b_j&gt;=j+log(1+M_j). Apply the preceding smooth nondecreasing construction to produce h_1 with h_1(t)&gt;=b_(j+1) on [j,j+1], taking nondecreasing maxima of the b values first. Put chi_1(t)=b_0+integral_0^t h_1(s)ds. It is convex nondecreasing, and chi_1(j)&gt;=b_j for every integer j (for j&gt;=1 use its last unit interval). On the shell j&lt;=psi&lt;j+1, the new integral is at most exp(-b_j)M_j&lt;=exp(-j). Summing proves g in L2 for Phi=(chi_0+chi_1)(psi), while preserving A&gt;=Id. The weight depends on g; no unjustified universal integrability claim is made.</p>

∎

## WL-4. Weighted solvability and smooth minimal solutions, conditional only at the indicated curvature step {#WL-4}

<p class="statement"><strong>Statement.</strong> Assume the compact-support Hermitian curvature inequality BKN-HERMITIAN-TORSION below. For any weight in <a href="general-analytic-wl.md#WL-3">WL-3</a>, every closed g in L2_(n,k), k&gt;=q, has a distributional solution f in L2_(n,k-1) with Df=g and ||f||&lt;=||g||. The minimal-norm solution satisfies delta f=0 and is smooth when g is smooth.</p>

**Proof.**

<p id="WL-4-p1">The explicitly retained input is ||Du||^2+||delta u||^2&gt;=integral &lt;A_(Phi,k)u,u&gt;dV for every smooth compactly supported u. For clarity, the right side includes the bundle weight through the fibre metric. It follows from the full non-Kahler identity with T, not the Euclidean scalar identity. Given this input, A&gt;=Id implies ||Du||^2+||delta u||^2&gt;=||u||^2 on compact forms. <a href="general-analytic-wl.md#WL-1">WL-1</a> passes this inequality to Dom D_k intersect Dom D_(k-1)^* by joint graph convergence. No unbounded-curvature integral limit is needed after the pointwise lower bound has been applied.</p>

<p id="WL-4-p2">Use the existing Hilbert Lemma 1.1 with H_1 degree k-1, H_2 degree k, H_3 degree k+1, T=D_(k-1), S=D_k and C=1. Its orthogonal decomposition uses the closed space ker S, not a presumed closed range of T. <a href="general-analytic-wl.md#WL-1">WL-1</a> verifies every domain and adjoint hypothesis. The lemma supplies f with (f,T*u)=(g,u); testing compact forms identifies Tf=g distributionally, and since g belongs to H_2 this places f in the maximal domain. The bound is ||f||&lt;=||g||.</p>

<p id="WL-4-p3">The solution set is a nonempty closed affine translate of ker T in H_1. Orthogonal projection gives its unique minimum-norm element f_min, which is perpendicular to ker T. The image of R=D_(k-2) lies in ker T, so (Rv,f_min)=0 for every v in Dom R. By the definition of the Hilbert adjoint, f_min is in Dom R* and R*f_min=0; if k=1 there is no preceding degree and this equation is vacuous. Thus Qf_min=(g,0), with Q=(D,delta) at degree k-1. It is initially L2_loc, and all the metric and weight coefficients are smooth. <a href="general-analytic-wl.md#WL-2">WL-2</a> proves it smooth whenever g is smooth, without assuming the initial H1 regularity or first asserting an unproved second-order elliptic estimate.</p>

∎

## WL-5. The full bundle twist and the degree endpoints for manifold vanishing {#WL-5}

<p class="statement"><strong>Statement.</strong> Assuming the same curvature input, H^k(M,O(E))=0 for k&gt;=q on a strongly q-complete complex n-manifold, without assuming K_M trivial or the metric Kahler.</p>

**Proof.**

<p id="WL-5-p1">For 1&lt;=q&lt;=n, replace E in <a href="general-analytic-wl.md#WL-0">WL-0</a> through <a href="general-analytic-wl.md#WL-4">WL-4</a> by F=K_M^(-1) tensor E. There is a canonical holomorphic-bundle identification Lambda^(n,k)T*M tensor F = Lambda^(0,k)T*M tensor E: contract K_M with its dual. In local holomorphic frames the contraction commutes with dbar, so it is an isomorphism of the entire smooth Dolbeault complexes, not just of their fibres. Equip F with any smooth Hermitian metric. For each smooth closed E-valued (0,k) form, k&gt;=q, use this identification, choose its integrability weight by <a href="general-analytic-wl.md#WL-3">WL-3</a>, and obtain a smooth primitive by <a href="general-analytic-wl.md#WL-4">WL-4</a>. Transport back. The existing Dolbeault Theorem 3.2 identifies the resulting vanishing quotient with H^k(M,O(E)).</p>

<p id="WL-5-p2">When k&gt;n, the smooth resolution has no term of that degree and the same programme theorem gives zero directly. Hence q&gt;n is fully included without inventing a positive gamma_q eigenvalue. The case n=0 is also covered by this last observation for every q&gt;=1. These statements concern arbitrary finite-rank holomorphic bundles. They do not by themselves prove coherent-sheaf vanishing on singular spaces or derived base change; those remain separate steps.</p>

∎

## WL-6. Degree-(q-1) approximation with uniform inner estimates {#WL-6}

<p class="statement"><strong>Statement.</strong> Suppose U is an open subset of M such that for every compact L in U there is a strongly q-complete exhaustion psi of M and numbers b_0&lt;b with L subset M_(b_0), closure M_(b_0) subset M_b, and closure M_b compact in U, where M_c={psi&lt;c}. Then every smooth closed E-valued (0,q-1)-form h on U is the C-infinity-local limit of restrictions of globally closed smooth forms on M.</p>

**Proof.**

<p id="WL-6-p1">First take 1&lt;=q&lt;=n and one such compact L. Perform the K_M^(-1) twist from <a href="general-analytic-wl.md#WL-5">WL-5</a>. Choose eta smooth compactly supported in U, equal to 1 on a neighbourhood of closure M_b. Extend eta h by zero to M and put g=D(eta h). Since Dh=0 on U, g is smooth, compactly supported, D-closed, and vanishes on a neighbourhood of closure M_b. Choose the metric and chi_0 from <a href="general-analytic-wl.md#WL-0">WL-0</a> through <a href="general-analytic-wl.md#WL-3">WL-3</a> for this exhaustion and bundle. The weight chi_0 alone suffices for the compactly supported g.</p>

<p id="WL-6-p2">Let a smooth nonnegative function alpha vanish on (-infinity,b_0] and be strictly positive on (b_0,infinity), for example alpha(t)=exp(-1/(t-b_0)^2) there. Define theta(t) as zero for t&lt;=b_0 and c integral_(b_0)^t (t-s)alpha(s)ds otherwise, with c&gt;0 chosen so theta(b)=1. It is smooth, convex, nondecreasing, identically zero on t&lt;=b_0 and &gt;=1 on t&gt;=b. The correctly typed scalar weights are chi_nu(t)=chi_0(t)+nu theta(t) and Phi_nu(x)=chi_nu(psi(x)); neither rho composed with psi nor a mixture of scalar and manifold variables is used.</p>

<p id="WL-6-p3"><a href="general-analytic-wl.md#WL-3">WL-3</a> keeps A&gt;=Id for all nu. Let f_nu be the smooth minimum-norm solution of Df_nu=g supplied by <a href="general-analytic-wl.md#WL-4">WL-4</a> with weight Phi_nu. Since support g is in {psi&gt;=b}, its squared norm is &lt;=C exp(-nu), where C=integral |g|^2 exp(-chi_0(psi))dV is independent of nu. The same bound holds for f_nu in its global weighted norm. On M_(b_0), Phi_nu=Phi_0 as smooth functions, including all derivatives; thus the weighted adjoints there are exactly the fixed delta_0, not just bounded relatives. Consequently Df_nu=0 and delta_0 f_nu=0 there, and ||f_nu||^2_(L2(M_(b_0),Phi_0))&lt;=C exp(-nu).</p>

<p id="WL-6-p4">Choose fixed compact neighbourhoods L subset V&#x27; with closure V&#x27; in M_(b_0). Smooth metric and weight equivalence on V&#x27;, followed by <a href="general-analytic-wl.md#WL-2">WL-2</a> for the fixed system (D,delta_0), gives ||f_nu||_(C^ell(L))&lt;=C_ell exp(-nu/2) for every ell. No coefficient in this interior estimate varies with nu. The forms h_nu=eta h-f_nu are globally D-closed; on L, eta=1, so h_nu-h=-f_nu. This proves approximation on L to any finite list of derivatives.</p>

<p id="WL-6-p5">Choose a compact exhaustion L_j of U with interiors covering U and increasing. For each j perform the preceding construction anew, and choose nu_j so the difference is &lt;2^(-j) in all the first j prescribed chart C^ell seminorms on L_j. A fixed enumeration of relatively compact chart seminorms defines the C-infinity-local topology. Its first r seminorms are controlled once j&gt;=r; therefore this diagonal sequence converges to h in that topology. The metrics and exhaustions can vary with j, because the constants are required to be uniform only in nu within each individual construction.</p>

<p id="WL-6-p6">If q=n+1, h has top antiholomorphic degree n, so D of any such smooth form is zero for degree reasons. Compactly supported cutoffs eta_j equal to 1 on L_j give globally smooth, globally closed extensions eta_j h and exact agreement on each eventual compact set. If q&gt;n+1 the form space itself is zero. These cases include n=0 and prove the endpoints without misusing the eigenvalue or solvability argument.</p>

∎

## Sources {#WL-sources}

Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), author edition of 21 June 2012. VI.2.3, printed 289; VII.1.1-1.6 and VII.2.1, printed 329-332; VIII.4.1-4.8, printed 370-372; IX.3.1, printed 414-415; IX.4.1, printed 419-420. The independently written arguments above follow the cited mathematics, with the explicit domains, signs and comparisons given here.
