# Global gluing and the compact coherent dimension bound {#general-analytic-qg}

Written by GPT-6 Astra (OpenAI), at Ultra, October 2026. Independent exposition: CC0-1.0.

Read this argument with the [general surface theorem](general-proper-flat-surface-base-change.md#general-surface-theorem) and its [prerequisite guide](general-proper-flat-surface-base-change.md#general-prerequisites). Result identifiers link to the exact arguments in this companion family.

The supporting arguments retain linear mathematical notation: `->` denotes a map, `^` an exponent or cohomological degree, `_` a subscript, and `direct_sum` a direct sum. Parentheses specify grouping. Algebraic quotients and completed topological tensor products are distinguished explicitly; a quotient is not silently replaced by its completion.

## Conventions {#QG-conventions}

<p>All complex spaces are Hausdorff and countable at infinity as in the bound programme providers. The structure sheaf may have nilpotents. F denotes a coherent module for that full structure sheaf; no radicalization of F or of its local defining ideal is performed.</p>

<p>Fix an integer q&gt;=1. Strong q-convexity means that locally a smooth real function has an ambient smooth extension whose Levi form has at least N-q+1 positive directions in ambient dimension N. When N&lt;q the requirement is vacuous. Geometry on the reduced support is transferred by the local-embedding comparison <a href="general-analytic-qn.md#QN-0">QN-0</a>; this does not replace coherent coefficients by their reduction.</p>

<p>An exhaustion is bounded below and has compact closed sublevel sets. Write X_t={psi&lt;t}. A q-Runge-complete open W in U has the following property: each compact L in W lies inside a sublevel {h&lt;b} compactly contained in W for some strongly q-convex exhaustion h of U.</p>

<p>Use alternating ordered Cech cochains, with zero on repeated indices and delta c at an increasing tuple equal to the alternating sum of restrictions after deletion of one index. Negative cochain degrees are zero. Cohomology carries the quotient topology on cocycles modulo coboundaries. It need not be Hausdorff before <a href="general-analytic-qg.md#QG-3">QG-3</a>.</p>

<p>Every cochain map below is continuous and complex-linear. Global cohomology is not assigned an O(X)-module structure stronger than the natural compatible one without specifying the underlying ring; the topological arguments need only complex-linearity.</p>

## QG-0. A Frechet model of the two-open Mayer-Vietoris sequence {#QG-0}

<p class="statement"><strong>Statement.</strong> For T=G union U and W=G intersect U, construct topological cochain models giving the Mayer-Vietoris sequence for coherent F. In these models the connecting map is induced by a continuous shifted inclusion, without assuming closed coboundary spaces.</p>

**Proof.**

<p id="QG-0-p1">Choose countable Stein-piece covers (G_i) indexed by I and (U_j) indexed by J. Each piece is an open subset of T contained in the indicated side. Every finite intersection is coherent-acyclic by the imported full-space intersection lemma. Order all I indices before all J indices, retaining an order within each set. Let P=C(G_i,F), Q=C(U_j,F), and C=C((G_i),(U_j);F). All three are nonnegative Frechet complexes: each degree is a countable product of section Frechet spaces, with a continuous finite-coordinate differential. They compute H(G,F), H(U,F), and H(T,F), respectively.</p>

<p id="QG-0-p2">Introduce the double complex R^(a,b)=product F(G_(i0...ia) intersect U_(j0...jb)) for a,b&gt;=0, with differential d_R=delta_G+(-1)^a delta_U. Its total degree is a+b; the direct sum in each total degree is finite. Restriction of a pure G cochain to intersections with each U_j defines a continuous cochain map j_G:P-&gt;Tot R in row b=0. Likewise j_U:Q-&gt;Tot R occupies column a=0. The unused differential annihilates these restrictions because two successive restrictions agree. Put rho(p,u)=j_U(u)-j_G(p).</p>

<p id="QG-0-p3">A mixed cochain in C^n has a+1 G indices and b+1 U indices, where a+b=n-1. Multiply its coordinate by (-1)^a and call the resulting element r of (Tot R)^(n-1). This produces a degreewise topological isomorphism C^n=P^n direct-sum Q^n direct-sum (Tot R)^(n-1). Under it the differential is D(p,u,r)=(d_P p,d_Q u,rho(p,u)-d_R r). To check the signs, deletion of a G index in a mixed tuple changes a by one, producing -delta_G after conjugation. Deletion of a U index contributes (-1)^(a+1), producing -(-1)^a delta_U. At an edge with only one U index, deleting it sends a pure G cochain to -j_G(p); at the edge with only one G index it sends a pure U cochain to j_U(u). These formulas include the n=0 edge, whose mixed degree is -1 and is zero.</p>

<p id="QG-0-p4">Since rho is a cochain map, D^2=0: the mixed component of D^2 is rho(d_P p,d_Q u)-d_R rho(p,u)+d_R^2 r=0. Projection C-&gt;P direct-sum Q and inclusion (Tot R)[-1]-&gt;C, r-&gt;(0,0,r), form a degreewise split short exact sequence of topological vector spaces. The shifted differential on (Tot R)[-1] is -d_R. The splitting is only degreewise; no false cochain splitting is asserted.</p>

<p id="QG-0-p5">The resulting long exact sequence contains H^k(C)-&gt;H^k(P) direct-sum H^k(Q) --H(rho)--&gt; H^k(Tot R) --partial--&gt; H^(k+1)(C). This can be checked directly: a closed pair (p,u) lifts to a cocycle of C exactly when rho(p,u)=d_R r; a closed mixed z maps to a boundary exactly when its class is the rho image of a closed pair. The kernel of projection on H(C) consists of mixed classes after subtracting a boundary lifting any exact pure components. These are the three exactness assertions and repeat in each degree.</p>

<p id="QG-0-p6">In this convention partial sends [z] to [(0,0,z)]. The linear map Z^k(Tot R)-&gt;Z^(k+1)(C) used here is continuous. A boundary z=d_R w maps to D(0,0,-w), so the map descends continuously to the quotient cohomology spaces. This proves continuity of the connecting map directly; it is not a restriction map. Identification of H(Tot R) with the canonical H(W,F), including topology and natural restrictions, is supplied next.</p>

∎

## QG-1. Topological comparison for the mixed overlap complex {#QG-1}

<p class="statement"><strong>Statement.</strong> The complex Tot R in <a href="general-analytic-qg.md#QG-0">QG-0</a> computes H(W,F) with its canonical quotient topology, and j_G and j_U induce the ordinary restriction maps. Thus all Mayer-Vietoris maps in <a href="general-analytic-qg.md#QG-0">QG-0</a> are continuous in the canonical coherent-cohomology topologies.</p>

**Proof.**

<p id="QG-1-p1">Cover W by D_(i,j)=G_i intersect U_j, retaining empty members as zero factors if convenient. This countable cover and all its finite intersections consist of Stein pieces, so its Cech complex A=C(D,F) computes H(W,F). Form the triple complex T^(a,b,c)=product F(G_I intersect U_J intersect D_K), with increasing nonempty I,J,K of lengths a+1,b+1,c+1. Its total differential is delta_G+(-1)^a delta_U+(-1)^(a+b) delta_D. Restriction gives continuous augmentations Tot R-&gt;Tot T and A-&gt;Tot T, the latter occupying a=b=0. They are cochain maps because the newly introduced Cech differentials of an augmented section are zero.</p>

<p id="QG-1-p2">For fixed I,J, the cover by D_(i,j) restricted to G_I intersect U_J contains that whole open set as a member: choose the first i in I and the first j in J. Consequently its augmented Cech complex, starting with F(G_I intersect U_J), is contractible. Explicitly extend cochains alternately to all ordered tuples and insert that chosen member as the first index; restriction to the other indices then gives h delta+delta h=identity, with the augmentation included. Repeated indices give zero. All restrictions and insertions are continuous.</p>

<p id="QG-1-p3">For fixed K, the intersection D_K is contained in G_i and U_j for the first pair (i,j) in K. Thus the G cover restricted to D_K, and then the U cover restricted to D_K, each contain the entire set as a member. The same insertion homotopy makes both augmented directions exact. This proves exactness without selecting holomorphic splittings or assuming cohomology is Hausdorff.</p>

<p id="QG-1-p4">These exact augmented directions prove both augmentations are quasi-isomorphisms. One explicit total-complex argument is to remove a component in the highest positive augmented direction by subtracting the total differential of its insertion-homotopy preimage; the cycle equation makes the component closed in that direction. The subtraction removes it and can move components only one step toward the next direction. Repeat until the augmented degree is zero, where the remaining kernel is precisely the augmented section. Apply the same elimination to a total boundary to prove injectivity. For the second map eliminate the G and U augmented directions successively. In total degree n there are only finitely many triples a+b+c=n, so the algorithm terminates. The chosen insertions need not commute with the other differential; those discrepancies are precisely the lower-direction components removed at the next step.</p>

<p id="QG-1-p5">Each augmentation is a continuous map of Frechet complexes. <a href="general-analytic-cl.md#CL-1">CL-1</a> therefore turns its algebraic cohomology isomorphism into a homeomorphism, by applying the Frechet open mapping theorem to the map from source cocycles plus target lower-degree cochains onto target cocycles. The common identification H(Tot R)=H(A)=H(W,F) is consequently topological even when these spaces are non-Hausdorff. The augmentations agree on an ordinary section and all their coordinates are restrictions. Composing the G or U cover comparison through this common refinement consequently gives exactly restriction to W, not a different abstract isomorphism. <a href="general-analytic-qg.md#QG-0">QG-0</a> is the canonical two-open sequence with the stated sign convention for its difference and connecting maps.</p>

∎

## QG-2. Finite q-convex bumps with common positive Levi directions {#QG-2}

<p class="statement"><strong>Statement.</strong> Let psi be a smooth exhaustion of X, strongly q-convex off compact K. If K is contained in X_c and d&gt;c, the inclusion X_c subset X_d factors into finitely many G_j subset G_(j+1)=G_j union U_j. Each G_j is a global sublevel of such an exhaustion with the same exceptional compact K. Each U_j lies in a distinguished patch for F, and U_j and W_j=G_j intersect U_j are strongly q-complete; W_j is q-Runge-complete in U_j.</p>

**Proof.**

<p id="QG-2-p1">The closed band B={c&lt;=psi&lt;=d} is compact and avoids K. Cover it by finitely many distinguished patches A_j, each a full closed analytic subspace of a Euclidean ball Omega_j=B(z_j,r_j), with a finite ambient free resolution of F on a slightly larger ball. Shrink these patches inside charts on which psi has a strongly q-convex ambient extension; arrange their closures to avoid K. <a href="general-analytic-qn.md#QN-1">QN-1</a> gives smooth theta_j&gt;=0, with compact support in A_j, sum theta_j&lt;=1 everywhere, and sum theta_j=1 on a neighbourhood of B. For example take a finite partition on a neighbourhood of B and multiply it by a cutoff supported in that neighbourhood and equal to one near B.</p>

<p id="QG-2-p2">Fix finitely many common ambient charts covering the union of those supports and the closures of the small patch balls. On a smaller chart, the Levi form of psi is positive on a fixed subspace with a uniform strictly positive lower bound, by continuity; <a href="general-analytic-qn.md#QN-0">QN-0</a> permits use of one ambient embedding. The finitely many theta_k have ambient extensions with bounded second derivatives on these compact chart closures. Choose epsilon_0&gt;0 so the sum of the perturbation norms, multiplied by epsilon_0, is below half every required positive lower bound. Then, for every partial sum and alpha in [0,1], psi-epsilon sum_(k&lt;j)theta_k-alpha epsilon theta_j is positive on the SAME chosen subspace when 0&lt;epsilon&lt;=epsilon_0. Outside the compact supports there is no change. In charts of dimension less than q the required index condition is empty. This establishes common directions, not merely separate q-convexity of two functions.</p>

<p id="QG-2-p3">For t in [c,d) and epsilon&lt;=min(epsilon_0,d-t), put psi_j=psi-epsilon sum_(k&lt;j)theta_k and G_j={psi_j&lt;t}. All psi_j are bounded below proper exhaustions: their difference from psi is bounded and has compact support. They agree with psi near K. The sets G_j increase, G_0=X_t and G_s=X_(t+epsilon). For the last equality, points with psi&lt;t are in both; in the band t&lt;=psi&lt;t+epsilon the full sum equals one; and when psi&gt;=t+epsilon the inequality sum theta&lt;=1 prevents entry into G_s. Since psi_(j+1)-psi_j is supported in A_j, putting U_j=A_j intersect G_(j+1) gives G_(j+1)=G_j union U_j and W_j=A_j intersect G_j.</p>

<p id="QG-2-p4">On U_j use phi_j=1/(t-psi_(j+1))+1/(r_j^2-|z-z_j|^2), restricting the indicated ambient functions to A_j. On W_j use the analogous formula with psi_j in the first denominator. Both denominators are positive. For f(s)=1/(t-s), f&#x27;&gt;0 and f&#x27;&#x27;&gt;0 on s&lt;t. Its Levi form is f&#x27;(psi)H_psi plus the nonnegative rank-one gradient term. The radial reciprocal is strictly plurisubharmonic. Thus the chosen positive subspaces remain positive, proving strong q-convexity. A bounded sublevel keeps both denominators bounded away from zero and z inside a smaller closed ball. Closedness of the analytic model then makes that sublevel compact within U_j, or within W_j respectively. Hence these functions are exhaustions.</p>

<p id="QG-2-p5">Given nonempty compact L in W_j, let a=max_L psi_j and choose b with a&lt;b&lt;t. On U_j put h_eta=psi_j+eta phi_j for eta&gt;0. The function psi_j has a global lower bound, while phi_j is nonnegative and proper, so h_eta is a bounded-below exhaustion. Its Levi form is the Levi form of psi_j plus a positive multiple of H_(psi_(j+1)), nonnegative gradient terms and a positive radial term. The common positive directions fixed above therefore prove strong q-convexity. Choose eta so that eta max_L phi_j&lt;b-a. Then L subset {h_eta&lt;b}; also psi_j&lt;=h_eta, so its closure lies in {psi_j&lt;=b}, strictly inside W_j. Since h_eta is proper, that closure is compact in U_j and hence compact in W_j. This is the required q-Runge witness. Empty L is automatic if W_j is nonempty by choosing any such witness; if W_j is empty all its cohomology and approximation requirements are trivial.</p>

<p id="QG-2-p6">Choose a finite partition c=t_0&lt;...&lt;t_N=d with increments at most epsilon_0 and repeat the same finite-cutoff construction for each adjacent pair. The estimates were uniform on the original compact band. Concatenating the finite lists proves the assertion for X_c subset X_d. No smoothness of the boundary levels, regular-value theorem, reducedness of the structure sheaf, or closure of arbitrary sums of q-convex functions is used.</p>

∎

## QG-3. Coarse sublevel comparison and noncircular finiteness {#QG-3}

<p class="statement"><strong>Statement.</strong> Under the hypotheses of <a href="general-analytic-qg.md#QG-2">QG-2</a>, restriction H^k(X_d,F)-&gt;H^k(X_c,F) is surjective for k=q and bijective for k&gt;q. For every c with K subset X_c and every k&gt;=q, H^k(X_c,F) is finite-dimensional and Hausdorff. This conclusion does not use density or injectivity in degree q.</p>

**Proof.**

<p id="QG-3-p1">For one bump put T=G union U and W=G intersect U as in <a href="general-analytic-qg.md#QG-2">QG-2</a>. <a href="general-analytic-cl.md#CL-0">CL-0</a> applies on the same distinguished ambient patch to both U and W and gives H^k(U,F)=H^k(W,F)=0 for k&gt;=q. In the exact sequence of <a href="general-analytic-qg.md#QG-0">QG-0</a>, the zero group H^k(W,F) implies surjectivity of H^k(T,F)-&gt;H^k(G,F) for k&gt;=q. If k&gt;q, the preceding H^(k-1)(W,F) also vanishes, proving injectivity. Compose these maps over the finite list of bumps. No topological conclusion about any cohomology group has been used here.</p>

<p id="QG-3-p2">Fix c and choose d&gt;c. The closure of X_c is compact and lies in X_d. Choose a countable Stein-piece cover V=(V_i) of X_d and a finite family of shrunk open sets V&#x27;_ell compactly contained in selected V_(a(ell)), covering the closure of X_c. Choose a countable Stein-piece cover W of X_c refining (V&#x27;_ell intersect X_c). All endpoint covers are Leray by the imported intersection lemma; the intermediate finite cover is not asserted to be Leray. The refinement maps define a continuous cochain map C(V,F)-&gt;C((V&#x27;_ell intersect X_c),F)-&gt;C(W,F), which induces ordinary restriction on sheaf cohomology.</p>

<p id="QG-3-p3">In each fixed cochain degree the first target is a finite product. Its component maps restrict F(V_(a(ell_0)) intersect ... intersect V_(a(ell_k))) to F(V&#x27;_ell_0 intersect ... intersect V&#x27;_ell_k intersect X_c), with the alternating sign determined by index order; repeated source indices give zero. The latter open has compact closure inside the former, because each closure(V&#x27;_ell) is compact in its assigned V_(a(ell)). Proposition 5.2(3) of the Frechet provider makes each nonzero component compact. Only finitely many source coordinates are used. The intersection of their witnessing zero-neighbourhoods is a zero-neighbourhood in the source product, whose image has compact closure in the finite target product. Thus the first map is compact in each degree. Composition with the continuous second refinement remains compact, even though its target can have infinitely many factors.</p>

<p id="QG-3-p4">The cohomology map of this compact cochain map is surjective in degree k&gt;=q by the coarse comparison already proved. Apply the bound Schwartz finiteness criterion to the two endpoint Frechet complexes. It shows that the target coboundaries are closed in the cocycles and that H^k(X_c,F) is finite-dimensional. The quotient topology of <a href="general-analytic-cl.md#CL-1">CL-1</a> is therefore Hausdorff. This proof applies to any smooth exhaustion strongly q-convex outside its compact exceptional set. In particular each intermediate G_j of <a href="general-analytic-qg.md#QG-2">QG-2</a> is a permitted target: its defining psi_j is such an exhaustion, and its level contains K. Hence H^q(G_j,F) is Hausdorff before <a href="general-analytic-qg.md#QG-4">QG-4</a> uses any dense image.</p>

∎

## QG-4. Sharp sublevel comparison and approximation in the boundary degree {#QG-4}

<p class="statement"><strong>Statement.</strong> For K subset X_c and d&gt;c, restriction H^k(X_d,F)-&gt;H^k(X_c,F) is a topological isomorphism for k&gt;=q and has dense image for k=q-1. The density assertion does not require H^(q-1) to be Hausdorff.</p>

**Proof.**

<p id="QG-4-p1">Consider a single bump T=G union U and W=G intersect U. By <a href="general-analytic-cl.md#CL-5">CL-5</a> and <a href="general-analytic-qg.md#QG-2">QG-2</a>, the map H^(q-1)(U,F)-&gt;H^(q-1)(W,F) has dense image. Exactness makes its composite with partial:H^(q-1)(W,F)-&gt;H^q(T,F) zero. <a href="general-analytic-qg.md#QG-0">QG-0</a> and <a href="general-analytic-qg.md#QG-1">QG-1</a> prove partial continuous, while <a href="general-analytic-qg.md#QG-3">QG-3</a> proves H^q(T,F) Hausdorff. The kernel of partial is consequently closed and contains a dense subset, so partial=0. Exactness now makes H^q(T,F)-&gt;H^q(G,F) injective, supplementing the surjectivity from <a href="general-analytic-qg.md#QG-3">QG-3</a>. In degrees greater than q bijectivity was already proved. These restrictions are induced by continuous Frechet cochain maps; <a href="general-analytic-cl.md#CL-1">CL-1</a> makes their cohomology bijections homeomorphisms.</p>

<p id="QG-4-p2">Put r=q-1. The now-zero connecting map also makes rho:H^r(G,F) direct-sum H^r(U,F)-&gt;H^r(W,F), rho(g,u)=u|W-g|W, surjective. This map is induced by the continuous cochain map P direct-sum Q-&gt;Tot R of <a href="general-analytic-qg.md#QG-0">QG-0</a>. <a href="general-analytic-cl.md#CL-1">CL-1</a> and the topological identification <a href="general-analytic-qg.md#QG-1">QG-1</a> therefore make rho open. This is an application of the Frechet open mapping theorem on cocycles plus lower-degree cochains, not an assumption that these possibly non-Hausdorff cohomology spaces themselves are Frechet.</p>

<p id="QG-4-p3">To prove density of restriction from T to G, fix g in H^r(G,F) and an open neighbourhood O of g. Choose a symmetric zero-neighbourhood V with g-V subset O, and any zero-neighbourhood N in H^r(U,F). Openness makes rho(V direct-sum N) an open zero-neighbourhood in H^r(W,F). Since restrictions from U are dense, there is u with rho(g,u)=u|W-g|W in this neighbourhood. Choose (g&#x27;,u&#x27;) in V direct-sum N whose rho image is rho(g,u). Then rho(g-g&#x27;,u-u&#x27;)=0. Exactness supplies a class f in H^r(T,F) restricting to g-g&#x27; on G and u-u&#x27; on U. Its G restriction belongs to O. This proves density without a continuous splitting, without chosen lifts of an entire convergent sequence, and without Hausdorffness of H^r.</p>

<p id="QG-4-p4">A finite composite of continuous maps with dense image again has dense image: continuity puts the image of the closure of a set inside the closure of its image, and the intermediate image is dense in the next target. Apply this to the bump factorization. The topological isomorphisms in higher degrees compose as well. This proves both conclusions for X_d-&gt;X_c. For q=1 the argument uses r=0; the negative cochain groups in the open-mapping construction are zero, so no exceptional negative-degree term has been assumed.</p>

∎

## QG-5. Global coherent vanishing by a cochain exhaustion limit {#QG-5}

<p class="statement"><strong>Statement.</strong> If X admits a smooth strongly q-convex exhaustion everywhere, then H^k(X,F)=0 for every coherent F and every k&gt;=q, including nonreduced full complex spaces.</p>

**Proof.**

<p id="QG-5-p1">Set K=empty. Choose c below the lower bound of the exhaustion psi. Then X_c is empty. For each d&gt;c, <a href="general-analytic-qg.md#QG-4">QG-4</a> identifies H^k(X_d,F) with H^k(X_c,F)=0 for k&gt;=q. Hence every finite sublevel has the claimed vanishing. This does not by itself imply vanishing on the union; the following cochain argument supplies the missing step.</p>

<p id="QG-5-p2">Take a countable basis W of relatively compact Stein pieces of X, subordinate to distinguished patches for F. Let W_n consist of those basis members whose compact closures lie in X_(c+n), for n&gt;=0. These subfamilies cover the respective sublevels, are nested and have union W. Indeed any basis member has compact closure in X and the increasing sublevels eventually contain that closure. Define E_n=C(W_n,F). Each is a Frechet complex computing the corresponding coherent cohomology, and every degree of E_(n+1)-&gt;E_n is the coordinate projection that forgets tuples involving new indices. It is surjective: extend a cochain by zero on those tuples. Zero extension is NOT claimed to preserve cocycles or commute with the differential.</p>

<p id="QG-5-p3">The complex E=C(W,F) is the topological inverse limit of the E_n. Each finite tuple of indices occurs at one finite stage, so a compatible inverse-limit element specifies exactly its section coordinate. Each basic product neighbourhood involves finitely many coordinates and finitely many seminorms and is therefore detected at some stage. These two facts prove the algebraic and topological identification degreewise. The differentials also agree coordinatewise. No commutation of cohomology with inverse limits has been inferred.</p>

<p id="QG-5-p4">Fix k&gt;=q. The transition maps on H^k(E_n) are injective because both groups are zero. The transitions on H^(k-1)(E_n) have dense image: for k=q this is <a href="general-analytic-qg.md#QG-4">QG-4</a>, and for k&gt;q both groups are zero. Together with degreewise surjectivity, these verify the hypotheses of the imported Frechet Proposition 3.1(3), which makes H^k(E)-&gt;H^k(E_0)=0 injective. Here is its needed special case explicitly, to show how the exact projection maps are used.</p>

<p id="QG-5-p5">Let x be a closed degree-k cochain of E. Write x_n for its projection. Since H^k(E_n)=0, choose y_n in E_n^(k-1) with d y_n=x_n. Cocycles of degree k-1 from E_(n+1) have dense image among cocycles of E_n: density on quotient cohomology lets one approximate a target cocycle by a restricted cocycle plus d b with b in E_n^(k-2), and surjectivity in degree k-2 lifts b to E_(n+1), absorbing that coboundary into the approximating cocycle. If k=1, there is no degree -1 and no coboundary to absorb; H^0=Z^0, so the assertion is the given density directly.</p>

<p id="QG-5-p6">Choose complete translation-invariant metrics on the degree-(k-1) spaces, successively enlarged by the finitely many pullbacks of earlier metrics so that every projection has Lipschitz constant at most one. Having chosen y_n, choose any primitive v in E_(n+1)^(k-1) for x_(n+1). The difference v|n-y_n is a cocycle. By the just-proved density, subtract a cocycle z from v so the new primitive y_(n+1)=v-z satisfies d_n(y_(n+1)|n,y_n)&lt;2^(-n). This subtraction leaves d y_(n+1)=x_(n+1). For each fixed stage m, the projected primitives form a Cauchy sequence, because the tail distances are bounded by the summable series of these errors. Completeness gives a limit y^m. Continuity of all projections makes the limits compatible, and continuity of d gives d y^m=x_m. They thus define y in E^(k-1) with d y=x. This proves vanishing directly.</p>

<p id="QG-5-p7">All terms throughout are sections of the original F on the full complex space. The geometry determines which open subsets are used but never passes cohomology to reduced coefficients. The conclusion is the full strongly q-complete coherent vanishing theorem needed for the compact-fibre deduction. It does not prove that every noncompact n-dimensional space has the particular exhaustion required by a separate general dimension theorem.</p>

∎

## QG-6. Compact analytic dimension bound with full coherent coefficients {#QG-6}

<p class="statement"><strong>Statement.</strong> For a compact complex analytic space Z with dim Z&lt;=n and any coherent O_Z-module F, H^k(Z,F)=0 when k&gt;n. In particular this supplies the exact dimension-two full-fibre input retained for S6, without assuming smooth or reduced fibres.</p>

**Proof.**

<p id="QG-6-p1">First construct a strongly (n+1)-convex smooth function on the reduced support of Z by induction on dimension. The empty case is immediate. In dimension zero the compact support is a finite discrete set. The constant zero function has, near each point, the ambient extension |z|^2 after centering coordinates at that point, so it is strongly 1-convex. Every continuous function on this finite compact support is an exhaustion under the bounded-below compact-sublevel convention.</p>

<p id="QG-6-p2">For the induction step, the finite analytic stratification of <a href="general-analytic-qn.md#QN-1">QN-1</a> gives a compact analytic subset Y of dimension at most n-1 whose complement in Z_red is a smooth manifold of pure dimension n: take the singular locus together with all lower-dimensional components. If the whole space has smaller dimension, the preceding induction statement already applies and strong (n+1)-convexity follows from the stronger lower-index property. Otherwise apply induction to Y. It has a strongly n-convex exhaustion, since any stronger index obtained in lower dimension also meets the n-convex condition.</p>

<p id="QG-6-p3">If Y is nonempty, <a href="general-analytic-qn.md#QN-5">QN-5</a> supplies an open neighbourhood V of Y in Z_red and a strongly n-convex smooth exhaustion phi of V. By compactness of Y and <a href="general-analytic-qn.md#QN-1">QN-1</a>, choose a smooth cutoff eta supported compactly inside V and equal to one on a neighbourhood of Y. Set h=eta phi on V and h=0 outside the support. Because the support stays inside V this is globally smooth. Near Y it equals phi and is strongly n-convex, hence strongly (n+1)-convex. At every point outside Y the space is a smooth n-manifold; strong (n+1)-convexity is vacuous in its intrinsic n-dimensional chart. <a href="general-analytic-qn.md#QN-0">QN-0</a> transfers that property to any larger ambient embedding. If Y is empty simply use h=0 on the smooth n-manifold. In either case h is strongly (n+1)-convex everywhere and is a bounded-below exhaustion by compactness of Z.</p>

<p id="QG-6-p4">Smooth real functions and their Levi index on a full analytic space are defined on its support by local ambient extensions. Consequently the function just constructed also supplies strong (n+1)-completeness for the original full Z. This step transfers geometric data only: O_Z, its possibly nonradical local ideal, and F are unchanged. Apply <a href="general-analytic-qg.md#QG-5">QG-5</a> on this full space with q=n+1. It gives H^k(Z,F)=0 for k&gt;=n+1, which is the claimed dimension bound. The deduction uses the neighbourhood construction <a href="general-analytic-qn.md#QN-5">QN-5</a> and the global vanishing theorem <a href="general-analytic-qg.md#QG-5">QG-5</a>, with the full coherent coefficients unchanged.</p>

<p id="QG-6-p5">For the retained S6 map f:X-&gt;B, properness makes the support of each full fibre Z=X_b compact, and its assigned pure dimension is two. The restricted coefficient E|Z=E tensor_(O_X) O_Z is a coherent, indeed locally free, O_Z-module. Apply the proved result with n=2 to obtain H^k(X_b,E|X_b)=0 for all k&gt;2. Flatness is not needed for this fibrewise vanishing lemma; it remains a hypothesis of the separate proper-flat relative-complex and base-change argument. No compactness of X, smoothness or reducedness of a fibre, constant h^2, or locally free higher direct image has been introduced.</p>

<p id="QG-6-p6">Fibrewise vanishing alone does not assert R^k f_*E=0 or identify the canonical base-change map. Those conclusions still require the retained general relative finite-complex construction and its canonical derived-fibre comparison, together with the previously recorded algebraic deduction. The general noncompact dimension theorem and the source&#x27;s separate top-degree conclusions remain outside this compact-fibre proof; they are neither declared false nor silently discarded.</p>

∎

## Sources {#QG-sources}

Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), author edition of 21 June 2012. IX.4, Lemma 4.12, Proposition 4.13 and the subsequent inverse-limit argument, printed pp. 426-428. The independently written arguments above follow the cited mathematics, with the explicit domains, signs and comparisons given here.
