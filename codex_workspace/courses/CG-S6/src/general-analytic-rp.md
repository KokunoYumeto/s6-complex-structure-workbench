# Relative nuclear perturbation {#general-analytic-rp}

Written by GPT-6 Astra (OpenAI), at Ultra, October 2026. Independent exposition: CC0-1.0.

Read this argument with the [general surface theorem](general-proper-flat-surface-base-change.md#general-surface-theorem) and its [prerequisite guide](general-proper-flat-surface-base-change.md#general-prerequisites). Result identifiers link to the exact arguments in this companion family.

The supporting arguments retain linear mathematical notation: `->` denotes a map, `^` an exponent or cohomological degree, `_` a subscript, and `direct_sum` a direct sum. Parentheses specify grouping. Algebraic quotients and completed topological tensor products are distinguished explicitly; a quotient is not silently replaced by its completion.

## Conventions {#RP-conventions}

<p>Algebras and modules are complex, unital and complete; the algebras in scalar extension are commutative and their multiplication and module actions are jointly continuous. All linear morphisms are continuous. Frechet spaces are Hausdorff unless an algebraic cokernel is explicitly being discussed.</p>

<p>For scalar Frechet tensors use the completed projective tensor; with a nuclear factor it agrees with the injective tensor by <a href="general-analytic-ns.md#NS-3">NS-3</a>. A balanced tensor is the quotient by the actual image of the balancing differential as in <a href="general-analytic-bt.md#BT-0">BT-0</a>, not by its closure. It is only treated as a nuclear Frechet space once transversality or the free-module formula has proved it Hausdorff.</p>

<p>A-nuclear means T(x)=sum_j lambda_j xi_j(x)y_j with summable complex lambda_j, equicontinuous A-linear xi_j into A, and a bounded sequence y_j. For a nuclear domain, A-subnuclear means that precomposition with some open surjection from a nuclear Frechet A-module is A-nuclear. These are the definitions established in <a href="general-analytic-ns.md#NS-6">NS-6</a> and <a href="general-analytic-bt.md#BT-6">BT-6</a>, not scalar compactness assertions.</p>

<p>The open mapping theorem and the exact topologies of coherent sections are supplied by the pinned programme providers. Source references identify the mathematical route; the proof paragraphs here give the needed argument rather than treating a citation as proof closure.</p>

## RP-0. Closed corestriction becomes subnuclear after a scalar-nuclear change of algebra {#RP-0}

<p class="statement"><strong>Statement.</strong> Let A,B be nuclear Frechet algebras, rho:A-&gt;B a scalar-nuclear unital homomorphism, E,F nuclear Frechet A-modules, and F_1 a closed A-submodule of F. Suppose B is transverse over A to E, F and F/F_1. If f:E-&gt;F is A-subnuclear and f(E) is contained in F_1, then the induced map f_(1,B):B hat_tensor_A E -&gt; B hat_tensor_A F_1 is B-subnuclear.</p>

**Proof.**

<p id="RP-0-p1">Write F_B=B hat_tensor_A F and E_B=B hat_tensor_A E. Apply <a href="general-analytic-bt.md#BT-4">BT-4</a> to 0-&gt;F_1-&gt;F-&gt;F/F_1-&gt;0. The two assumed transverse modules on the right imply that F_(1,B) is nuclear Frechet and embeds as a closed submodule of F_B. This step supplies the closed topology needed below; no such conclusion about balanced F_1 was assumed beforehand.</p>

<p id="RP-0-p2">First assume f is A-nuclear. Choose f(e)=sum_j lambda_j xi_j(e)y_j and a scalar-nuclear representation rho(a)=sum_k mu_k eta_k(a)b_k. The map nu:E-&gt;F_B, nu(e)=1 tensor_A f(e), is represented by sum_(j,k) lambda_j mu_k (eta_k composed with xi_j)(e) (b_k tensor_A y_j). Indeed balancing moves xi_j(e) to the B factor, and the expansion of rho gives the displayed double sum. Its coefficients have finite absolute sum. The eta_k have a common bound by a single seminorm p of A; equicontinuity of the xi_j for p gives a single seminorm q of E bounding every eta_k xi_j. Boundedness of b_k and y_j makes their tensor products bounded for every projective seminorm and then for the quotient topology of F_B. Absolute convergence with these estimates proves that nu is scalar-nuclear and justifies both orders of summation.</p>

<p id="RP-0-p3">For subnuclear f, let p:P-&gt;E be its witnessing open surjection with P nuclear and fp A-nuclear. The previous calculation makes nu p:P-&gt;F_B scalar-nuclear. This map kills the closed kernel of p. <a href="general-analytic-ns.md#NS-2">NS-2</a> therefore makes its descent P/ker(p)-&gt;F_B scalar-nuclear. Open mapping identifies P/ker(p) topologically with E, so nu itself is scalar-nuclear. This use of descent has a nuclear domain; it is not a general assertion about arbitrary nuclear operators on arbitrary Banach quotients.</p>

<p id="RP-0-p4">The range of nu lies in the closed subspace F_(1,B) found in the first paragraph. Since E is nuclear, <a href="general-analytic-ns.md#NS-2">NS-2</a> gives a scalar-nuclear corestriction nu_1:E-&gt;F_(1,B). The map q:B hat_tensor E-&gt;E_B, b tensor e |-&gt; b tensor_A e, is an open surjection between nuclear Frechet spaces: E_B is Hausdorff by the transversality assumption. On its source, f_(1,B) q is the composite of Id_B hat_tensor nu_1:B hat_tensor E-&gt;B hat_tensor F_(1,B) and the module action B hat_tensor F_(1,B)-&gt;F_(1,B). <a href="general-analytic-ns.md#NS-6">NS-6</a> makes the first map B-nuclear; the composition rule makes the composite B-nuclear. Thus q witnesses B-subnuclearity of f_(1,B). There has been no assertion that f:E-&gt;F_1 was already A-subnuclear before shrinking the algebra.</p>

∎

## RP-1. The radius system of a fully nuclear algebra {#RP-1}

<p class="statement"><strong>Statement.</strong> Let A carry an increasing defining family p_r, 0&lt;r&lt;1, of submultiplicative seminorms. Write B_r for the Banach completion for p_r and assume B_v-&gt;B_u is scalar-nuclear whenever u&lt;v. Let A_t be the Hausdorff completion of A for the seminorms p_r with r&lt;t, and set A_1=A. Then A_t is fully nuclear, (A_t)_s=A_(st), and A_t&#x27;-&gt;A_t is scalar-nuclear for 0&lt;t&lt;t&#x27;&lt;=1. If E is fully A-transverse, E_t=A_t hat_tensor_A E is fully A_t-transverse.</p>

**Proof.**

<p id="RP-1-p1">Choose a countable increasing sequence of radii cofinal below t. Those seminorms define the same topology as all p_r with r&lt;t, so the indicated separated completion is Frechet. Submultiplicativity extends multiplication to it. For a fixed r&lt;t, the seminorm p_r extends to A_t and its Banach completion is B_r: the image of A is dense in both. Consequently the family q_s=p_(st), 0&lt;s&lt;1, on A_t has the same nuclear Banach transition maps as the original family. It makes A_t fully nuclear and, in particular, a nuclear Frechet space. The same argument with t=1 establishes nuclearity of A itself.</p>

<p id="RP-1-p2">Completing A_t for q_r with r&lt;s amounts to completing the dense image of A for p_u with u&lt;st. Completion of that same separated seminormed system gives (A_t)_s=A_(st), with the canonical map induced by A. This identifies the maps, not merely isomorphic vector spaces.</p>

<p id="RP-1-p3">For t&lt;t&#x27;, select radii u,v with t&lt;=u&lt;v&lt;t&#x27;. There are continuous maps A_t&#x27;-&gt;B_v-&gt;B_u-&gt;A_t. The first uses the seminorm p_v. The last exists because p_r&lt;=p_u for each r&lt;t and A_t is complete. Their composite agrees on the dense image of A with its natural restriction map. The middle map is nuclear by assumption, hence the composite is scalar-nuclear by the ideal property <a href="general-analytic-ns.md#NS-1">NS-1</a>. For t&#x27;=1 the same argument works directly from A. The direction is always from a larger radius to a smaller radius.</p>

<p id="RP-1-p4">If E is fully transverse, every E_t is a Hausdorff quotient of the nuclear scalar tensor A_t hat_tensor E, and hence is nuclear Frechet. Given 0&lt;s&lt;1, both A_t and A_(st) are transverse to E over A. Apply the successive-base argument <a href="general-analytic-bt.md#BT-4">BT-4</a> to A-&gt;A_t-&gt;A_(st); it identifies A_(st) hat_tensor_(A_t) E_t with E_(st) and kills its positive Tor. Using (A_t)_s=A_(st), this is precisely full A_t-transversality of E_t. No flatness statement for the Banach stages B_t is needed.</p>

∎

## RP-2. Analytic radius algebras and full coherent modules {#RP-2}

<p class="statement"><strong>Statement.</strong> For a polydisc D compactly contained in a larger polydisc D_0 and a closed full analytic subspace X of D_0, A=O(X intersection D) is fully nuclear for the quotient sup seminorms, and A_t=O(X intersection tD). If Y is a Stein manifold, V is a relatively compact Stein open in Y, and G is coherent on X x Y, then Gamma((X intersection D) x V,G) is fully A-transverse. These examples include the ambient-chart modules in the retained S6 construction and do not remove nilpotents from X or from the support of G.</p>

**Proof.**

<p id="RP-2-p1">Start with H=O(D), p_r(h)=sup_(closure(rD))|h|, where rD has the same centre as D and all its radii multiplied by r. The p_r are submultiplicative and define compact convergence. Taylor expansion at that centre gives nuclear maps between their Banach completions for u&lt;v: the coefficient bound on vD and monomial norm on uD produce the summable multi-index weights (u/v)^|alpha|, exactly as proved in <a href="general-analytic-ns.md#NS-4">NS-4</a>. Taylor polynomials show O(D) is dense in O(tD) for compact convergence, so H_t=O(tD).</p>

<p id="RP-2-p2">Let J be the full coherent ideal defining X in D_0. Cartan B on D gives A=H/J(D) as a topological quotient; the coherent section topology makes J(D) closed. Use quotient seminorms bar_p_r(h+J)=inf_(j in J(D)) p_r(h+j). They are submultiplicative: multiply arbitrary representatives of two classes, apply submultiplicativity of p_r, and take the two infima independently. The Banach stage of A for bar_p_r is H_r/J_r, where H_r is the p_r completion of H and J_r is the closure of the image of J(D) in H_r. The quotient norm formula and density verify this identification, as in <a href="general-analytic-ns.md#NS-2">NS-2</a>.</p>

<p id="RP-2-p3">For u&lt;v choose w strictly between them. The maps H_v-&gt;H_w and H_w-&gt;H_u-&gt;H_u/J_u are nuclear Banach maps. Their composite kills J_v, because it kills the dense image of J(D) there. The binuclear descent of <a href="general-analytic-ns.md#NS-1">NS-1</a> gives a nuclear map H_v/J_v-&gt;H_u/J_u. Thus the quotient algebra A is fully nuclear. Using two nuclear transitions here is important: we have not presumed that an arbitrary single nuclear Banach operator remains nuclear after arbitrary quotient descent.</p>

<p id="RP-2-p4">To identify its radius completion, Cartan A on D_0 and compactness of closure(D) supply finitely many sections g_1,...,g_m of J generating J near closure(D). Cartan B for the coherent kernel of O^m-&gt;J gives J(D)=sum_i O(D)g_i and J(tD)=sum_i O(tD)g_i. Polynomial approximation of each coefficient on compact subsets of tD shows that the image of J(D) is dense in J(tD). The latter is closed in O(tD). Therefore, for every r&lt;t and every h in O(D), the infimum defining bar_p_r(h+J(D)) is unchanged if J(D) is replaced by J(tD). The dense image of A in O(tD)/J(tD) has exactly these quotient seminorms. That quotient is complete and Hausdorff by <a href="general-analytic-ns.md#NS-2">NS-2</a>, so its identification with A_t follows. The ideal used throughout is J, never its radical.</p>

<p id="RP-2-p5">For the transversality assertion, put U=X intersection D and U_t=X intersection tD. Closed analytic embedding i:X x Y-&gt;D_0 x Y identifies sections of a coherent G with sections of coherent i_*G. Exactness of i_* is checked on stalks, which are G at points of the closed subspace and zero elsewhere. A flabby resolution remains flabby under i_* because sections on ambient opens are sections on their intersections with X x Y. Thus sheaf cohomology is also preserved by i_*. Cartan A and B on the ambient Stein products therefore give the corresponding generation and acyclicity statements for these full closed analytic pieces. Coherence here is the usual finite local module presentation over the coherent quotient by J; regarding that presentation over the ambient structure sheaf gives coherence of i_*G.</p>

<p id="RP-2-p6">Apply Cartan A on D_0 x Y to i_*G and select finitely many global sections generating near closure(D) x closure(V). They give O_(X x Y)^r-&gt;G, surjective on U x V, with coherent kernel on X x Y. Repeat this construction for each successive kernel, using the same compact set, to obtain a resolution by finite free sheaves in each degree. It can extend indefinitely to the left; no finite length is claimed. Each generation neighbourhood contains U x V, so the construction takes no infinite intersection of shrinking opens. Cartan B makes its section complexes exact on U x V and on every U_t x V.</p>

<p id="RP-2-p7">By <a href="general-analytic-ns.md#NS-5">NS-5</a> their free terms are A hat_tensor O(V)^r and A_t hat_tensor O(V)^r, respectively. They are nuclear by <a href="general-analytic-ns.md#NS-2">NS-2</a> and <a href="general-analytic-ns.md#NS-4">NS-4</a>. <a href="general-analytic-bt.md#BT-2">BT-2</a> computes the balanced Tor of Gamma(U x V,G) from the first free section resolution; after balancing with A_t it is the second, exact resolution. Thus all positive Tor vanish and the degree-zero balanced tensor is canonically Gamma(U_t x V,G), including its quotient topology. That section space is Hausdorff nuclear Frechet. This proves full transversality. It does not assert restriction to a point or a finite relative complex; those remain separate obligations.</p>

∎

## RP-3. A Banach-module perturbation has an explicit finite-generator identity {#RP-3}

<p class="statement"><strong>Statement.</strong> Let B be a Banach algebra, S a Frechet B-module and v:S-&gt;S B-nuclear. There are an integer N, continuous B-linear R:S-&gt;S, gamma:S-&gt;B^N and Y:B^N-&gt;S with I_S=(I_S-v)R+Y gamma. Consequently S/(I_S-v)S is generated algebraically by the N vectors Y(e_j). The quotient is not asserted Hausdorff, and S need not be a scalar-nuclear space.</p>

**Proof.**

<p id="RP-3-p1">Choose v(x)=sum_j lambda_j xi_j(x)y_j. Equicontinuity into the normed algebra B gives a continuous seminorm p on S with ||xi_j(x)||&lt;=p(x) for all j. Let T=ell^1(B), alpha:S-&gt;T be alpha(x)=(lambda_j xi_j(x))_j, and beta:T-&gt;S be beta(c)=sum_j c_j y_j. Then ||alpha(x)||_1&lt;=p(x)sum_j|lambda_j|. For every seminorm q on S, continuity of the B action gives a seminorm r and a constant C with q(by)&lt;=C||b||r(y). Boundedness of y_j implies q(beta(c))&lt;=C sup_j r(y_j)||c||_1. Completeness of S therefore makes beta a well-defined continuous B-linear map. We have v=beta alpha.</p>

<p id="RP-3-p2">Set w=alpha beta:T-&gt;T. It is bounded. Let P_N:T-&gt;T keep the first N coordinates and set w_tail=(I_T-P_N)w. Since p(beta(c))&lt;=C_p||c||_1, we obtain ||w_tail(c)||_1&lt;=C_p(sum_(j&gt;N)|lambda_j|)||c||_1. Choose N so that the coefficient on the right is less than one. The Banach operator D=I_T-w_tail is invertible with Q=D^(-1)=sum_(k&gt;=0)w_tail^k. The series converges in operator norm by its geometric bound; multiplying its partial sums by D and passing to the limit proves both inverse identities. Every term is B-linear, so Q is B-linear as well.</p>

<p id="RP-3-p3">Let j_N:B^N-&gt;T be inclusion into the first N coordinates and pi_N:T-&gt;B^N the projection, so P_N=j_N pi_N. Define Y=beta j_N, gamma=pi_N w Q alpha, and R=I_S+beta Q alpha. All are continuous B-linear maps with exactly the domains and codomains in the statement. Since (I_S-v)beta=beta(I_T-w) and D=I_T-w+P_Nw, direct multiplication gives (I_S-v)R=I_S-beta alpha+beta(I_T-w)Q alpha=I_S-beta P_N w Q alpha. Adding Y gamma gives I_S, as required.</p>

<p id="RP-3-p4">For each x in S the identity expresses x as (I_S-v)R(x)+sum_(j=1)^N gamma_j(x)y_j. Passing to the algebraic quotient therefore gives a surjection B^N-&gt;S/(I_S-v)S. This is finite generation without a closed-image inference. We retain the continuous maps R,gamma,Y rather than tensoring this quotient, which may fail to be a Frechet space. In particular a scalar finite-rank conclusion was neither used nor obtained when B is infinite dimensional.</p>

∎

## RP-4. Free scalar extension and the reductions used by perturbation {#RP-4}

<p class="statement"><strong>Statement.</strong> Continuous algebra homomorphisms extend maps between topologically free modules functorially. This extension preserves nuclear representations and finite-generator identities in the cases below. An A-subnuclear u:E-&gt;F, with a surjective f:E-&gt;F and fully transverse nuclear E,F, can be reduced after every transverse base change to f&#x27;:P-&gt;F surjective and u&#x27;=f&#x27;v, where P=A hat_tensor M is nuclear free and v:P-&gt;P is A-nuclear.</p>

**Proof.**

<p id="RP-4-p1">For a continuous unital algebra map rho:A-&gt;B and a nuclear Frechet space M, set P_A(M)=A hat_tensor M and P_B(M)=B hat_tensor M. In this paragraph B can be Banach and need not be nuclear. The projective tensor suffices. A continuous A-linear T:P_A(M)-&gt;P_A(N) is determined by t(m)=T(1 tensor m). Compose t with iota_N=rho hat_tensor Id_N into P_B(N), then use the continuous B action to extend b tensor m |-&gt; b iota_N(t(m)) to a continuous B-linear T_B:P_B(M)-&gt;P_B(N). Joint continuity gives the needed projective tensor estimate, and the complete target gives the extension. On pure tensors T_B iota_M=iota_N T; density extends this equality to P_A(M). Applying that intertwining identity once more proves (T&#x27;U)_B=T&#x27;_B U_B whenever the composition is defined. Identity maps are preserved. This also applies to finite free modules by taking M or N to be a finite-dimensional space.</p>

<p id="RP-4-p2">If A-&gt;B-&gt;C is a second change of algebra, the same construction over B extends every continuous B-linear map P_B(M)-&gt;P_B(N). The defining formulas on 1 tensor m show (T_B)_C=T_C. Thus any finite identity between such maps extends to C, whether or not B or C is flat over the previous algebra. No tensor functor on a non-Hausdorff quotient is involved.</p>

<p id="RP-4-p3">Suppose v:P_A(M)-&gt;P_A(M) has an A-nuclear representation. For each coefficient xi_j, its B-valued extension is determined by m |-&gt; rho(xi_j(1 tensor m)). Given a seminorm b on B, continuity of rho bounds b(rho(a)) by a seminorm a_0 on A. Equicontinuity of the xi_j bounds a_0(xi_j(1 tensor m)) uniformly by a seminorm r on M. Joint continuity of multiplication in B then gives, for every output seminorm, a projective input seminorm controlling all the extended coefficient maps. The images of the bounded vectors y_j remain bounded in P_B(M). The summable coefficient sequence is unchanged. The resulting nuclear series agrees on the dense pure tensors with v_B, so v_B is B-nuclear. For Banach B this says in particular that all coefficient norms are bounded by one continuous seminorm on P_B(M). The same argument works when the target is a Hausdorff base-changed module F_B rather than free: extend the map m |-&gt; 1 tensor_A u(1 tensor m) using its B action.</p>

<p id="RP-4-p4">Now take the subnuclear witness p:M-&gt;E with M nuclear and up A-nuclear. The action epsilon:A hat_tensor M-&gt;M is onto, since epsilon(1 tensor m)=m; its continuous complex-linear section shows it is open. The composite g=p epsilon:P=A hat_tensor M-&gt;E is an open surjection, and u&#x27;=ug is A-nuclear by the composition property. Put f&#x27;=fg, also surjective. P is nuclear and fully A-transverse by the free formula and contracted bar complex in <a href="general-analytic-bt.md#BT-0">BT-0</a>-<a href="general-analytic-bt.md#BT-2">BT-2</a>. For every transverse base algebra A_t, balanced right exactness <a href="general-analytic-bt.md#BT-1">BT-1</a> makes g_t:P_t-&gt;E_t onto. The images of (f_t-u_t)g_t and f_t-u_t therefore coincide. Their cokernels are the same algebraic A_t-module.</p>

<p id="RP-4-p5">We can arrange an A-nuclear representation u&#x27;(x)=sum_j lambda_j xi_j(x)y_j in which y_j tends to zero. Starting with bounded y_j, choose integers N_k increasing to infinity so that sum_(j&gt;=N_k)|lambda_j|&lt;=2^(-2k). Put c_j=2^k for N_k&lt;=j&lt;N_(k+1), and c_j=1 on the initial block. Then c_j tends to infinity and sum_j c_j|lambda_j| is finite. Replace lambda_j by c_j lambda_j and y_j by y_j/c_j; this changes neither u&#x27; nor the equicontinuous coefficients, and makes y_j tend to zero in every target seminorm. Finite nonzero representations can be treated by appending zero terms.</p>

<p id="RP-4-p6">Open surjectivity of f&#x27;:P-&gt;F lets this null sequence be lifted to a null sequence x_j in P. Explicitly choose a decreasing neighbourhood basis V_n of zero in P that controls the first n defining seminorms by 2^(-n). Each f&#x27;(V_n) is a neighbourhood in F. Select increasing indices J_n such that y_j belongs to f&#x27;(V_n) whenever j&gt;=J_n. For J_n&lt;=j&lt;J_(n+1), choose x_j in V_n with f&#x27;(x_j)=y_j; choose the finitely many initial lifts arbitrarily. These x_j tend to zero, hence form a bounded sequence. The series v(x)=sum_j lambda_j xi_j(x)x_j defines an A-nuclear endomorphism of P. Continuity of f&#x27; and convergence of the series give f&#x27;v=u&#x27;. Thus f&#x27;-u&#x27;=f&#x27;(I_P-v).</p>

<p id="RP-4-p7">For any transverse A_t, f&#x27;_t remains surjective by <a href="general-analytic-bt.md#BT-1">BT-1</a>. Hence it induces a surjection from P_t/(I_(P_t)-v_t)P_t onto F_t/(f&#x27;_t-u&#x27;_t)P_t. Together with the earlier equality of images, proving finite generation for I-v on the free module after shrinking proves it for the original f-u. The same free-witness argument and extension of its nuclear representation show that base-changing an A-subnuclear map between transverse nuclear modules yields a subnuclear map over the new nuclear algebra. Its source witness is the Hausdorff free module B hat_tensor M, even when B hat_tensor_A M itself has not been proved Hausdorff.</p>

∎

## RP-5. Subnuclear perturbation after shrinking a fully nuclear algebra {#RP-5}

<p class="statement"><strong>Statement.</strong> Let A be fully nuclear, E,F fully A-transverse nuclear Frechet A-modules, f:E-&gt;F surjective and u:E-&gt;F A-subnuclear. For every 0&lt;t&lt;1, F_t/(f_t-u_t)E_t is finitely generated as an algebraic A_t-module. Neither closedness of (f_t-u_t)E_t nor Hausdorffness of this cokernel is claimed.</p>

**Proof.**

<p id="RP-5-p1">Use <a href="general-analytic-rp.md#RP-4">RP-4</a> to reduce to P=A hat_tensor M and an A-nuclear endomorphism v of P, where it suffices to prove that the cokernel of I_(P_t)-v_t is a finitely generated A_t-module. Fix t&lt;1 and let B_t be the Banach completion of A for p_t. The canonical A-&gt;B_t followed by B_t-&gt;A_t equals A-&gt;A_t: the latter map from B_t exists because p_r&lt;=p_t for r&lt;t, as established in <a href="general-analytic-rp.md#RP-1">RP-1</a>.</p>

<p id="RP-5-p2">Extend v to the free Frechet B_t-module S=B_t hat_tensor M using <a href="general-analytic-rp.md#RP-4">RP-4</a>. The extension v_B is B_t-nuclear. <a href="general-analytic-rp.md#RP-3">RP-3</a> gives an integer N and continuous B_t-linear maps R_B:S-&gt;S, gamma_B:S-&gt;B_t^N and Y_B:B_t^N-&gt;S satisfying I_S=(I_S-v_B)R_B+Y_B gamma_B. These are maps between free modules over B_t, including its finite free module B_t^N.</p>

<p id="RP-5-p3">Extend those maps along B_t-&gt;A_t by <a href="general-analytic-rp.md#RP-4">RP-4</a>. Their domains and codomains become P_t=A_t hat_tensor M and A_t^N. Functoriality preserves both composition and addition, and (v_B)_(A_t)=v_t. Therefore I_(P_t)=(I_(P_t)-v_t)R_t+Y_t gamma_t. For every z in P_t this identity writes its cokernel class as the A_t-linear combination, with coefficients gamma_t(z), of the N classes of Y_t(e_1),...,Y_t(e_N). It is an actual equality before taking the quotient, not a statement about density of a finitely generated image in a completion.</p>

<p id="RP-5-p4">The surjection of cokernels from <a href="general-analytic-rp.md#RP-4">RP-4</a> now gives finite generation for F_t/(f_t-u_t)E_t. No step forms a completed tensor of the possibly non-Hausdorff Banach-stage cokernel. The assertion is therefore at exactly its algebraic strength. It supplies the perturbation input for the next finite-complex argument, but does not itself identify cohomology sheaves, give a point-fibre comparison or prove the retained S6 theorem.</p>

∎

## Sources {#RP-sources}

Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), author edition of 21 June 2012. IX.5.38-5.43, pp. 443-446; IX.5.44(a), p. 446: immediate next consumer. The independently written arguments above follow the cited mathematics, with the explicit domains, signs and comparisons given here.
