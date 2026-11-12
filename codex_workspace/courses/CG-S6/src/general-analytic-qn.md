# Positive Levi directions and q-complete neighbourhoods {#general-analytic-qn}

Written by GPT-6 Astra (OpenAI), at Ultra, October 2026. Independent exposition: CC0-1.0.

Read this argument with the [general surface theorem](general-proper-flat-surface-base-change.md#general-surface-theorem) and its [prerequisite guide](general-proper-flat-surface-base-change.md#general-prerequisites). Result identifiers link to the exact arguments in this companion family.

The supporting arguments retain linear mathematical notation: `->` denotes a map, `^` an exponent or cohomological degree, `_` a subscript, and `direct_sum` a direct sum. Parentheses specify grouping. Algebraic quotients and completed topological tensor products are distinguished explicitly; a quotient is not silently replaced by its completion.

## Conventions {#QN-conventions}

<p>For a real C-infinity function u on an open subset of C^N, H_u(x)(xi,xi)=sum u_{z_j bar-z_k}(x) xi_j conjugate(xi_k). It is strongly q-convex when it has at least max(0,N-q+1) strictly positive directions. On a complex space this means local ambient smooth extensions with that property.</p>

<p>A real continuous function bounded below whose sublevel sets {u&lt;=c} are compact for every real c. A strongly q-complete space admits a smooth strongly q-convex exhaustion.</p>

## QN-0. Coordinate compatibility and the shared-positive-subspace rule {#QN-0}

<p class="statement"><strong>Statement.</strong> Strong q-convexity transfers between local embeddings. If H_u and H_w are positive on the same subspace F of dimension at least N-q+1, then u+theta(w) is strongly q-convex for every smooth convex nondecreasing theta.</p>

**Proof.**

<p id="QN-0-p1">For a complex submanifold of dimension k in C^N, a positive subspace F of dimension N-q+1 intersects its tangent space in dimension at least k-q+1. Pullback by the holomorphic inclusion restricts the Levi form; this proves the restriction assertion, including the vacuous case k&lt;q.</p>

<p id="QN-0-p2">For two local embeddings G:U-&gt;A in C^N and G&#x27;:U&#x27;-&gt;A&#x27; in C^M, lift the coordinate expressions of their inverse local isomorphisms to holomorphic maps P:W-&gt;C^M and Q:W&#x27;-&gt;W. They agree with G&#x27;G^{-1} and GG&#x27;^{-1} on the respective analytic sets. The smooth function U(z,w)=u(z)+|w-P(z)|^2 is the pullback of u(z)+|w|^2 by the biholomorphism (z,w)-&gt;(z,w-P(z)). It has at least N+M-q+1 positive directions. Restrict it along the holomorphic graph embedding w-&gt;(Q(w),w). The resulting extension u&#x27;(w)=u(Q(w))+|w-P(Q(w))|^2 has the required Levi index and equals the original function on A&#x27;. This also permits all functions in a comparison to be represented in a common ambient chart.</p>

<p id="QN-0-p3">The chain rule gives H_{u+theta(w)}=H_u+theta&#x27;(w)H_w+theta&#x27;&#x27;(w) partial-w tensor conjugate(partial-w). The last term is nonnegative and the middle term is nonnegative on F, while the first is positive there. Thus the same F works. The common subspace is essential: the two diagonal forms (-2,1,1) and (1,-2,1) on C^3 each have two positive directions, whereas their sum (-1,-1,2) has only one. We will not use a general closure of q-convex functions under addition.</p>

∎

## QN-1. Locally finite smooth constructions and closed strata {#QN-1}

<p class="statement"><strong>Statement.</strong> The local models supply smooth cutoffs, a proper exhaustion and a finite closed filtration Z_{-1}=empty subset Z_0 subset ... subset Z_d=Y with Z_k minus Z_{k-1} a smooth k-dimensional manifold.</p>

**Proof.**

<p id="QN-1-p1">The local models are locally compact and metrizable. A countable collection of precompact chart interiors gives compact sets K_j with K_j contained in the interior of K_{j+1} and union X: enlarge each finite union to include a precompact neighbourhood of the preceding compact set. Cover each compact annulus by finitely many still smaller chart balls, with supports confined to its neighbouring annuli. This constructs globally locally finite precompact refinements of any open cover, and the same construction works for a closed subset using its intersections with the annuli.</p>

<p id="QN-1-p2">Restrict ordinary smooth Euclidean bumps to X. For a locally finite family of bumps whose positive sets cover X, divide their squares by their positive sum of squares. The resulting partition is smooth, nonnegative and locally finite; its functions have nonnegative local ambient extensions, by the same squared formula. A finite version supplies a cutoff equal to one on a compact set and supported inside any specified open neighbourhood. The annular refinement supplies the analogous cutoff for a closed set in an open set. A smooth function on a closed analytic set extends to X: take local smooth extensions, multiply by a partition subordinate to those charts and X minus Y, and sum. On Y every summand extends the same value.</p>

<p id="QN-1-p3">Choose cutoffs chi_j equal to one near K_j and supported in the interior of K_{j+1}. The sum tau=sum_j(1-chi_j) is locally finite: all sufficiently large j have chi_j=1 near any fixed point. It is smooth and nonnegative. Outside K_{n+1}, its first n terms equal one, so {tau&lt;=c} lies in a compact K_{n+1} when n&gt;c. Its closed sublevels are therefore compact.</p>

<p id="QN-1-p4">Start with Z_d=Y. Given an analytic Z_k of dimension at most k, let Z_{k-1} consist of its singular locus and all its irreducible components of dimension less than k. These sets are analytic and closed. Locally this uses finitely many component germs from Proposition 1.2; after shrinking their representatives, the selections agree on overlaps because local irreducible components and their dimensions agree there. A locally finite union of such components is analytic. The singular locus has smaller dimension on each component, by Theorem 3.3 and Proposition 5.5. Thus dim Z_{k-1}&lt;=k-1, and the remaining regular components have dimension k. Iterate to Z_{-1}=empty; a reduced zero-dimensional analytic set is locally a point. Only this finite filtration is used below.</p>

∎

## QN-2. A small perturbation with an arbitrarily large normal Levi form {#QN-2}

<p class="statement"><strong>Statement.</strong> For a holomorphic vector g and 0&lt;epsilon&lt;=1/2 put f_epsilon(g)=epsilon^3 log(1+|g|^2/epsilon^4). On a fixed compact chart f_epsilon and its first derivatives tend to zero, its Levi form is nonnegative, and at g=0 that form is epsilon^{-1} times the squared differential of g. A nonnegative cutoff changes the lower Levi bound by at most C epsilon.</p>

**Proof.**

<p id="QN-2-p1">Write s=|g|^2. In the g coordinates the Levi matrix is epsilon^3[I/(epsilon^4+s) - conjugate(g) g^t/(epsilon^4+s)^2]. Its eigenvalues are epsilon^3/(epsilon^4+s) in directions perpendicular to g and epsilon^7/(epsilon^4+s)^2 in its radial direction. They are positive; holomorphic pullback therefore gives a nonnegative form. At g=0 the matrix is epsilon^{-1}I, giving the stated normal form even if g has a nontrivial kernel.</p>

<p id="QN-2-p2">If |g|&lt;=M and its differential is bounded on the chart, then 0&lt;=f_epsilon&lt;=epsilon^3 log(1+M^2/epsilon^4), which tends to zero. Its differential has norm at most a fixed constant times epsilon, because r/(epsilon^4+r^2)&lt;=1/(2 epsilon^2); this inequality is precisely (r-epsilon^2)^2&gt;=0. Also epsilon^3 log(1+M^2/epsilon^4)&lt;=C_M epsilon for 0&lt;epsilon&lt;=1/2. These constants depend on the chosen compact chart, not on epsilon.</p>

<p id="QN-2-p3">For a fixed nonnegative smooth theta, the product rule writes H_{theta f}=theta H_f+f H_theta+the two mixed first-derivative terms. The first term is nonnegative. The value and gradient bounds put the sum of the remaining terms above -C epsilon times the Euclidean Hermitian form. At g=0, both f and df vanish, so the exact identity is H_{theta f}=theta epsilon^{-1}(dg)^*dg. Thus a cutoff perturbation can be uniformly small in value and harmful Levi part while being arbitrarily positive in normal directions.</p>

∎

## QN-3. Stratified extension with simultaneous parameter choices {#QN-3}

<p class="statement"><strong>Statement.</strong> If psi is smooth and strongly q-convex on Y and delta:Y-&gt;(0,infinity) is continuous, there is a neighbourhood W_0 of Y and a smooth strongly q-convex phi on W_0 satisfying psi&lt;=phi|Y&lt;psi+delta.</p>

**Proof.**

<p id="QN-3-p1">Extend psi smoothly to X by <a href="general-analytic-qn.md#QN-1">QN-1</a>, calling the extension phi_{-1}. It is strongly q-convex along Y in the sense that its restriction to Y has the required ambient extensions. Set V_{-1}=empty. Inductively maintain a global smooth phi_{k-1}, a closed neighbourhood V_{k-1} of Z_{k-1}, strong q-convexity on an open neighbourhood of V_{k-1}, strong q-convexity of phi_{k-1}|Y, and psi&lt;=phi_{k-1}|Y&lt;psi+delta.</p>

<p id="QN-3-p2">Use the CLOSED set S=Z_k minus interior(V_{k-1}), not Z_k minus V_{k-1}. Since Z_{k-1} lies in the interior, S lies in the smooth k-dimensional stratum. Cover S by a globally locally finite family of precompact embedded charts A_lambda avoiding Z_{k-1}. In a larger ambient chart, Z_k is defined by normal coordinates g_lambda=(z_{k+1},...,z_N). Choose nonnegative smooth theta_lambda compactly supported in A_lambda, with sum theta_lambda=1 on S. A partition for the cover consisting of these charts and X minus S constructs these functions; the extra partition terms vanish on S. Choose the squared-bump construction so their local ambient extensions remain nonnegative.</p>

<p id="QN-3-p3">Set phi_k=phi_{k-1}+sum_lambda theta_lambda f_{epsilon_lambda}(g_lambda), extending each compactly supported summand by zero. This is a locally finite smooth sum. On Y the increments are nonnegative. Its residual upper margin R=psi+delta-phi_{k-1}|Y is positive. On each compact test patch meeting Y the minimum of R on the relevant closed part of Y is positive, so an appropriately small sum of the value bounds in <a href="general-analytic-qn.md#QN-2">QN-2</a> keeps the new increment below R/2 there.</p>

<p id="QN-3-p4">For preservation of the old positive directions, cover the closed set Y union V_{k-1} by locally finite precompact test patches. At a point of V_{k-1} choose a strongly q-convex ambient extension of phi_{k-1}; at other points of Y choose an extension of phi_{k-1}|Y. On a sufficiently small closed test patch its chosen positive subspace has a uniform positive lower bound a_j. All finitely many perturbations meeting that patch admit compatible holomorphic coordinate extensions and nonnegative cutoff extensions there, by <a href="general-analytic-qn.md#QN-0">QN-0</a> and <a href="general-analytic-qn.md#QN-1">QN-1</a>. The harmful Levi part is bounded by sum_lambda C_{j,lambda} epsilon_lambda. Require this to be less than a_j/2. This preserves positivity on that same subspace. Outside the union of the supports nothing changes.</p>

<p id="QN-3-p5">New positivity on S uses the exact zero-set identity of <a href="general-analytic-qn.md#QN-2">QN-2</a>. Fix a small test patch on S with one theta_mu&gt;=c_mu&gt;0. All g_lambda vanish on Z_k there, so all added Levi terms at Z_k are nonnegative, and the mu term is at least t times the normal metric, t=c_mu/epsilon_mu. The tangential restriction of H_{phi_{k-1}} has a positive subspace F of dimension max(0,k-q+1), by <a href="general-analytic-qn.md#QN-0">QN-0</a>. If F is nonzero, choose uniform bounds a&gt;0 for its positive part, b for its mixed tangent-normal block, and -c for the normal block. For u in F and normal v, the perturbed form is at least a|u|^2-2b|u||v|+(t-c)|v|^2, which is at least (a/2)|u|^2+(t-c-2b^2/a)|v|^2. Taking t&gt;c+2b^2/a makes it positive on F plus the whole normal space. If F is zero, t&gt;c suffices on the normal space. The resulting dimension max(0,k-q+1)+N-k is at least max(0,N-q+1). Positivity is open, so this proves strong q-convexity on a neighbourhood of S.</p>

<p id="QN-3-p6">Here is a simultaneous choice, not merely a pointwise instruction to take epsilon small. Use a globally locally finite precompact refinement of all the preceding preservation, margin and new-positivity test patches. Each such compact test patch meets only finitely many compact bump supports; each compact bump support meets only finitely many test patches. On a preservation patch with m_j incident bumps, allocate each at most a_j/(2m_j) of the harmful Levi bound, and similarly split the positive value margin. On a new-positivity patch impose the displayed upper bound on its chosen epsilon_mu. Consequently each individual epsilon_lambda is subject to only finitely many positive upper bounds. Choose it smaller than their minimum and 1/2. All conditions then hold at once, with no global uniform gap or zero parameter assumed.</p>

<p id="QN-3-p7">The resulting function is strongly q-convex on some open O containing V_{k-1} union Z_k. That union is closed. Shrink around it, using normality of the metrizable space, to a closed neighbourhood V_k contained in O and containing the union in its interior. This restores the precise induction hypothesis; a union of a closed set with an arbitrary open neighbourhood is not asserted to be closed. There are d+1 stages. The final function is strongly q-convex on an open W_0 containing Y, and all the inequalities persist. No infinite limiting induction is invoked in this finite-dimensional application.</p>

∎

## QN-4. A logarithmic pole barrier with a locally bounded negative Levi part {#QN-4}

<p class="statement"><strong>Statement.</strong> There is a function v on X, smooth off Y, with value minus infinity on Y, locally of the form log|g|^2+O(1) for generators of its ideal, and with a local ambient extension whose Levi form is bounded below off its pole set.</p>

**Proof.**

<p id="QN-4-p1">Fix a smooth nonnegative probability density rho on (-1/2,1/2) with mean zero. For finitely many real numbers t_i define M(t)=integral max_i(t_i+s_i) product_i rho(s_i) ds. Convolution makes M smooth; convexity, monotonicity in every coordinate and translation equivariance follow from the same properties of max. Jensen&#x27;s inequality and |s_i|&lt;1/2 give max t_i&lt;=M(t)&lt;=max t_i+1/2. If one t_i is less than the maximum of the others by more than one, it cannot realize the maximum for any s in the support. Integration over its unused density equals one, so that coordinate drops exactly, not just approximately.</p>

<p id="QN-4-p2">Choose a globally locally finite cover A_lambda=X intersect B(z_lambda,r_lambda) by precompact embedded balls, with larger charts around their closures. Coherence supplies finite holomorphic generator vectors g_lambda for the reduced ideal of Y on those larger charts. On A_lambda minus Y put v_lambda=log|g_lambda|^2-1/(r_lambda^2-|z-z_lambda|^2), and put v=M of the values whose patches contain the point. At a point of Y set v=-infinity.</p>

<p id="QN-4-p3">Check the change of index set locally. If x is a boundary point of A_lambda, choose another patch A_mu containing x. On a sufficiently small compact neighbourhood of x inside the larger charts, each generator vector is a holomorphic matrix times the other, so their norms are bounded above and below by fixed multiples on X minus Y. This is a local compact-overlap assertion, not a uniform assertion on every entire overlap. The mu boundary penalty is bounded there, whereas the lambda penalty tends to minus infinity. Hence v_lambda&lt;v_mu-1 sufficiently near that boundary. <a href="general-analytic-qn.md#QN-4">QN-4</a>&#x27;s exact coordinate-drop property removes lambda. Local finiteness leaves a fixed finite collection of active smooth expressions near every point off Y. Thus v is smooth there.</p>

<p id="QN-4-p4">Near a point of Y the active generator norms are comparable with one fixed generator norm. The active smooth penalties are bounded and M differs from their maximum by at most 1/2. This proves v=log|g|^2+O(1) locally and v tends to minus infinity at Y. If Y contains a whole local component, this permits v identically minus infinity there; the final construction is identically phi on a neighbourhood of each such point.</p>

<p id="QN-4-p5">Use holomorphic lifts of the active generators in one common ambient chart. Each logarithmic norm is plurisubharmonic: its Levi form is the nonnegative radial matrix obtained by differentiating log(|g|^2+eta) and letting eta decrease to zero. Add C|z|^2 to compensate the finitely many smooth penalties on a smaller relatively compact ambient chart. The chain rule for a smooth convex increasing M gives a sum of nonnegative Levi forms plus a nonnegative gradient quadratic form. Its translation property therefore shows H_v&gt;=-C I off the poles. At poles take the decreasing limit using log(|g|^2+eta); the submean inequality passes to the limit (subtract a local upper bound and use monotone convergence). This supplies the local almost-plurisubharmonic extension, allowing the identically minus-infinity case. No integral estimate, vanishing theorem or q-complete neighbourhood result was used.</p>

∎

## QN-5. The neighbourhood exhaustion, with its properness proof {#QN-5}

<p class="statement"><strong>Statement.</strong> If psi is a strongly q-convex exhaustion of Y, every open neighbourhood N of Y contains an open V on which there is a smooth strongly q-convex exhaustion h. It can be chosen with psi&lt;=h|Y&lt;psi+1.</p>

**Proof.**

<p id="QN-5-p1">Apply <a href="general-analytic-qn.md#QN-3">QN-3</a> with delta=1, giving phi on W_0. Its restriction to Y is an exhaustion: {phi|Y&lt;=c} is a closed subset of the compact set {psi&lt;=c}. It is bounded below. Choose m below its infimum and use the proper tau of <a href="general-analytic-qn.md#QN-1">QN-1</a>. There exists a positive increasing continuous function a on R with tau(y)&lt;a(phi(y)) for every y in Y: the suprema of tau on compact sublevels of phi|Y are finite, and an increasing polygonal majorant with a one-level look-ahead bounds them strictly. Thus O={x in W_0: phi(x)&gt;m and tau(x)&lt;a(phi(x))} is an open neighbourhood of Y.</p>

<p id="QN-5-p2">Choose an open W_1 containing Y whose closure in X is contained in O. On its closure phi is bounded below by m and proper: {x in closure(W_1):phi(x)&lt;=c} is closed in X and lies in the compact set {tau&lt;=a(c)}. This proves the thickening assertion rather than assuming it from properness only on Y. Now choose an open W with Y subset W and closure(W) subset W_1 intersect N. Its boundary is disjoint from Y.</p>

<p id="QN-5-p3">Take the pole barrier v from <a href="general-analytic-qn.md#QN-4">QN-4</a>. On each compact phi-sublevel in closure(W_1), finitely many common ambient charts give positive subspaces F_i for H_phi, positive gaps a_i, and lower bounds H_v&gt;=-b_i I. The subspaces are fixed on sufficiently small individual charts, not globally identified between charts. For an increasing convex smooth function chi, H_{v+chi(phi)}=H_v+chi&#x27;(phi)H_phi+chi&#x27;&#x27;(phi) partial-phi tensor conjugate(partial-phi). On F_i this is at least (-b_i+chi&#x27; a_i) times the metric. Choose chi&#x27; greater than all corresponding b_i/a_i. In charts with N_i&lt;q the positivity condition is vacuous.</p>

<p id="QN-5-p4">The choice can also impose v+chi(phi)&gt;1 on boundary(W). On each compact sublevel the boundary is compact and disjoint from Y, so v has a finite minimum there. Both the derivative requirements and these value requirements are bounded on each interval [m,m+j]. To construct chi, take a nondecreasing sequence D_j&gt;=1 dominating the derivative bounds and the positive parts of all required values on [m,m+j+3]. A nondecreasing smooth function exceeding D_j on [m+j,m+j+1] is obtained by summing nonnegative jumps times smooth increasing switches, each completed before m+j. Integrate this function to obtain chi. Choose chi(m) sufficiently large for the first compact interval. On every later interval the preceding unit interval contributes at least D_{j-1}, which dominates that interval&#x27;s value requirement. Thus chi, chi&#x27; and chi&#x27;&#x27; have all the required properties, including chi&#x27;&#x27;&gt;=0.</p>

<p id="QN-5-p5">Write nu=v+chi(phi). It tends to minus infinity at Y, is greater than one on boundary(W), and its Levi form is positive on the SAME F_i as H_phi. Choose a nonnegative smooth eta on (-infinity,0) which is zero on (-infinity,-2] and equals 2/(-s)^3 on [-1,0). Define theta(t)=integral from minus infinity to t of (t-s)eta(s) ds. Then theta is smooth, convex, nondecreasing, zero for t&lt;=-2 and diverges to positive infinity as t increases to zero; on [-1,0) it is -1/t plus an affine function. Put V={x in W:nu(x)&lt;0} and h=phi+theta(nu) there. Since nu tends to minus infinity locally at Y, h=phi near each point of Y and extends smoothly across Y. Away from Y <a href="general-analytic-qn.md#QN-0">QN-0</a> proves strong q-convexity using the same F_i; at Y it follows from phi. In particular psi&lt;=h|Y&lt;psi+1.</p>

<p id="QN-5-p6">For properness, h&gt;=phi&gt;m. A sequence in {h&lt;=c} has a subsequence converging in the compact set closure(W_1) intersect {phi&lt;=c}. Its limit lies in closure(W). It cannot lie on boundary(W), since nu&gt;1 there and nu is continuous off Y. If its limit lies in W minus Y, then nu&lt;=0; equality is impossible because theta(nu) would diverge while phi remains bounded below. A limit in Y already belongs to V and h is smooth near it. Thus every limit lies in V, and continuity makes {h&lt;=c} closed there. It is consequently compact. This proves that h is an exhaustion and that V is strongly q-complete. Since N was arbitrary the neighbourhoods form a fundamental family. If Y is empty, take V empty; this separate trivial case avoids taking an infimum over an empty set.</p>

∎

## Sources {#QN-sources}

Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), author edition of 21 June 2012. IX.2.1-2.6, printed pages 409-410; IX.2.11-2.13, printed pages 411-413. The independently written arguments above follow the cited mathematics, with the explicit domains, signs and comparisons given here.
