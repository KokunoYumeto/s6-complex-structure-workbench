# Local coherent approximation on full complex spaces {#general-analytic-cl}

Written by GPT-6 Astra (OpenAI), at Ultra, October 2026. Independent exposition: CC0-1.0.

Read this argument with the [general surface theorem](general-proper-flat-surface-base-change.md#general-surface-theorem) and its [prerequisite guide](general-proper-flat-surface-base-change.md#general-prerequisites). Result identifiers link to the exact arguments in this companion family.

The supporting arguments retain linear mathematical notation: `->` denotes a map, `^` an exponent or cohomological degree, `_` a subscript, and `direct_sum` a direct sum. Parentheses specify grouping. Algebraic quotients and completed topological tensor products are distinguished explicitly; a quotient is not silently replaced by its completion.

## Conventions {#CL-conventions}

<p>Complex spaces are Hausdorff and second countable with their full coherent quotient structure sheaves. A local model i:A-&gt;Omega is a closed embedding defined by a coherent ideal J, with Omega open in C^N. The ideal is not replaced by its radical.</p>

<p>Fix an integer q&gt;=1. Strong q-completeness means the existence of a smooth exhaustion, bounded below with compact sublevel closures, which is strongly q-convex everywhere in the ambient-extension sense of the QN package.</p>

<p>For open U&#x27; contained in U, q-Runge completeness in this argument means: for each compact L contained in U&#x27;, there are a smooth strongly q-convex exhaustion psi of U and a real b with L contained in {psi&lt;b} and closure of {psi&lt;b} compact in U&#x27;. This is the complete local version, not mere q-convexity outside a compact exceptional set.</p>

<p>A coherent sheaf F has a distinguished patch A when i_*F admits a finite free resolution on Omega. Such patches form a local basis by the pinned programme providers. All sheaf maps below are O-linear before passing to cohomology; all cohomology maps are complex-linear and use quotient topologies, possibly non-Hausdorff.</p>

<p>Cech cochains use alternating indices, with C^r(W,F)=product over i_0&lt;...&lt;i_r of F(W_i0 intersect ... intersect W_ir). Empty intersections contribute zero. The differential is the alternating sum of restriction maps. Negative degrees of these ordinary complexes are zero.</p>

## CL-0. Discharge of local coherent vanishing and the free-to-coherent lift {#CL-0}

<p class="statement"><strong>Statement.</strong> Let A be a distinguished patch for F, with finite free ambient resolution 0-&gt;E_m-&gt;...-&gt;E_0-&gt;i_*F-&gt;0. If U is strongly q-complete and open in A, then H^k(U,F)=0 for k&gt;=q. If V is any strongly q-complete ambient neighbourhood with A intersect V=U, the natural map H^(q-1)(V,E_0)-&gt;H^(q-1)(U,F) is surjective.</p>

**Proof.**

<p id="CL-0-p1">The finite ambient resolution is the one in the pinned distinguished-patch provider, not a finite free resolution over the possibly singular or nonreduced ring O_A. Put Omega&#x27;=Omega minus (A minus U). Since A is closed in Omega and A minus U is closed in A, Omega&#x27; is open and U=A intersect Omega&#x27; is a full closed complex subspace of Omega&#x27;. <a href="general-analytic-qn.md#QN-5">QN-5</a> supplies a strongly q-complete neighbourhood V of U inside Omega&#x27;. Thus A intersect V=U, and restriction of the ambient resolution remains exact on V.</p>

<p id="CL-0-p2">On this neighbourhood, <a href="general-analytic-wl.md#WL-5">WL-5</a>, using the curvature identity <a href="general-analytic-bk.md#BK-5">BK-5</a>, gives H^r(V,E_j)=0 for every r&gt;=q and every finite free E_j. The exact dimension shift is as follows. Set K_-1=i_*F|V, and K_j=ker(E_j|V-&gt;K_(j-1)) for 0&lt;=j&lt;m; exactness identifies K_(m-1) with E_m|V. The sequence 0-&gt;K_j-&gt;E_j|V-&gt;K_(j-1)-&gt;0 gives H^r(V,K_(j-1)) isomorphic to H^(r+1)(V,K_j) for r&gt;=q. Starting with the free final syzygy and descending in j kills every H^r(V,K_j), r&gt;=q, including H^r(V,i_*F). When m=0, i_*F|V is already E_0|V and the same vanishing is immediate.</p>

<p id="CL-0-p3">Exact closed pushforward gives H^r(V,i_*F|V)=H^r(U,F|U). For the lifting assertion, if m&gt;=1, the tail resolution just considered gives H^q(V,K_0)=0. The connecting part H^(q-1)(V,E_0)-&gt;H^(q-1)(V,i_*F)-&gt;H^q(V,K_0) of the long exact sequence therefore makes the first arrow surjective. If m=0 this arrow is an isomorphism. Nothing here sets F equal to a sheaf on A_red: both the quotient ideal J and the actual O_A-module survive all restrictions and pushforwards. This proves local vanishing and the free-to-coherent lift. The global coherent dimension bound requires the additional gluing arguments ending in <a href="general-analytic-qg.md#QG-6">QG-6</a>.</p>

∎

## CL-1. The cohomology topology and the precise open mapping argument {#CL-1}

<p class="statement"><strong>Statement.</strong> Countable Stein-piece covers give a canonical quotient topology on coherent cohomology of a full complex space. Restrictions, coherent sheaf morphisms and closed-embedding cohomology comparisons are continuous. A surjection on cohomology induced by a continuous map of Frechet complexes is open, even when the cohomology spaces are not Hausdorff.</p>

**Proof.**

<p id="CL-1-p1">By Frechet Propositions 5.1-5.2, F(W) has its canonical Frechet topology for every open W, and restriction and sheaf morphisms act continuously. Small chart balls intersected with full complex models give a countable Stein-piece basis. Finiteness Lemma 1.1 embeds each finite intersection as a closed complex subspace of a product of Stein manifolds; its graph ideal retains J and the equations of the other chart maps, rather than a radicalized ideal. Closed pushforward and Cartan B on that smooth product give vanishing of positive coherent cohomology on the intersection. Thus Corollary 1.2 makes the cover Leray on full complex spaces, not just manifolds.</p>

<p id="CL-1-p2">For a countable such cover W, each C^r(W,F) is a countable product of Frechet spaces. The differential delta is continuous because each coordinate is a finite sum of continuous restrictions. Consequently Z^r=ker(delta:C^r-&gt;C^(r+1)) is a closed Frechet subspace. Give H^r=Z^r/delta C^(r-1) the quotient topology; no closedness of the denominator is asserted.</p>

<p id="CL-1-p3">Here is the open-mapping mechanism used from Remark 2.3. Let rho:E^bullet-&gt;D^bullet be a continuous cochain map of Frechet complexes, inducing a surjection in degree r. Then T:Z^r(E) direct-sum D^(r-1)-&gt;Z^r(D), T(x,y)=rho(x)+d_D y, is continuous and surjective. Its domain and target are Frechet, so Theorem 1.1 makes T open. If W is open in H^r(E), its inverse image under pi_E:Z^r(E)-&gt;H^r(E) is open. The image T(pi_E^(-1)(W) times D^(r-1)) is exactly pi_D^(-1)(H^r(rho)(W)): equality follows by expressing equality of classes as a coboundary. Hence H^r(rho)(W) is quotient-open. This also proves that a cohomology bijection induced by rho is a homeomorphism. For r=0 the negative-degree summand is zero and the argument still applies.</p>

<p id="CL-1-p4">Given two countable Stein-piece covers, choose a countable Stein-piece common refinement. A choice assigning each smaller open to a containing larger one induces a continuous cochain map by restriction, with alternating reordering and zero for repeated indices. Leray comparison makes its cohomology map the canonical bijection; the preceding paragraph makes it a homeomorphism. Thus the topology does not depend on the cover. For an open restriction or a coherent sheaf map, refine the relevant covers so that the actual cochain map consists of continuous section maps; its cohomology map is therefore continuous.</p>

<p id="CL-1-p5">For a full closed embedding i:A-&gt;V choose a countable Stein open cover W of V. The intersections A intersect W_i are Stein pieces of A. On every multiple intersection, (i_*F)(W_I)=F(A intersect W_I). These equalities respect the canonical section topologies: locally both are quotients of the same ambient free-section space by the same relation module, and the global topologies are the closed compatible-family topologies of those local quotients. Therefore the two Cech complexes are degreewise identical as topological complexes. This realizes H^r(V,i_*F)=H^r(A,F) as a topological isomorphism and verifies its compatibility with restriction. No continuous linear splitting of any quotient is claimed.</p>

∎

## CL-2. Transport from smooth-form approximation to the Cech quotient topology {#CL-2}

<p class="statement"><strong>Statement.</strong> On an open subset V of C^N, the Dolbeault and Cech realizations of H^r(V,O^p) are topologically isomorphic for the natural quotient topologies, and this comparison commutes with restriction to open subsets.</p>

**Proof.**

<p id="CL-2-p1">Choose a countable locally finite cover W of V by sufficiently small Stein opens and a smooth locally finite partition (theta_i) subordinate to it, with supports closed in V and contained in W_i. Such a cover and partition are available from the smooth partition provider already used in Dolbeault Lemma 3.1. Form D^(a,b)=product over increasing (a+1)-tuples I of smooth C^p-valued (0,b)-forms on W_I. With delta the Cech differential and dbar acting on coefficients, restriction implies delta dbar=dbar delta. Set the total differential on D^(a,b) to delta+(-1)^a dbar. The mixed terms have opposite signs, so its square is zero. Each total degree is a finite direct sum of Frechet spaces.</p>

<p id="CL-2-p2">There are continuous cochain maps j:Gamma(V,E^(0,bullet) tensor C^p)-&gt;Tot(D), given by restriction into column a=0, and k:C^bullet(W,O^p)-&gt;Tot(D), given by inclusion into row b=0. For the horizontal rows, the operation (hc)_I=sum_j theta_j c_(jI) gives the augmented Cech contraction delta h+h delta=identity, as in Dolbeault Lemma 3.1. Multiplication is extended by zero outside W_j. It is continuous: on a compact set in an output intersection, only finitely many supports meet that compact set, and each required derivative is controlled by finitely many input seminorms on compact subsets of the corresponding W_j intersect W_I.</p>

<p id="CL-2-p3">The map j is a quasi-isomorphism by finite diagonal elimination, which can be seen without an infinite spectral-sequence limit. For a total cocycle of degree r, its component with largest positive horizontal degree a is delta-closed by the total cocycle equation. Subtract the total differential of its horizontal primitive, using h, to remove that component. The subtraction creates components only in smaller horizontal degree. Repeat until only column a=0 remains. That column is horizontally closed, hence glues to a global form, and the remaining total equation says the global form is dbar-closed. If such a global closed form is a total boundary, apply the same elimination to its total primitive; all components of positive horizontal degree can be removed without changing its total differential. What remains is a global primitive. This proves both surjectivity and injectivity for j.</p>

<p id="CL-2-p4">For k use vertical elimination. Every W_I is Stein and H^b(W_I,O^p)=0 for b&gt;0, by the pinned Stein and Dolbeault providers. Thus each column has cohomology O(W_I)^p in degree zero and none above. Given a total cocycle, its component with smallest horizontal degree a and positive vertical degree b is dbar-closed. Choose a vertical primitive on each W_I and subtract its total differential, inserting the sign (-1)^a in the primitive. This removes that component and can create one only in the next horizontal degree. Repetition terminates on this finite diagonal at b=0, where the remaining entries are holomorphic Cech cocycles. The identical elimination applied to a primitive of a boundary proves injectivity. No continuous choice of vertical primitives is needed for this algebraic quasi-isomorphism.</p>

<p id="CL-2-p5">Both j and k are continuous maps of Frechet complexes and induce cohomology bijections. <a href="general-analytic-cl.md#CL-1">CL-1</a> therefore makes both induced maps homeomorphisms, even if their boundary subspaces are not closed. The resulting comparison is the usual Dolbeault identification from the two resolutions. To check restrictions, compare covers using a common subordinate cover on the smaller open set: all inclusions into the double complex and all restriction maps commute before taking cohomology. Refinement comparisons from <a href="general-analytic-cl.md#CL-1">CL-1</a> then give the canonical commuting restriction square. Consequently the C-infinity-local approximation of closed forms in <a href="general-analytic-wl.md#WL-6">WL-6</a> yields density in the Cech quotient topology used in <a href="general-analytic-cl.md#CL-1">CL-1</a>; no unproved identification of topologies is being inserted.</p>

∎

## CL-3. Ambient sublevels with a strict, quantified margin {#CL-3}

<p class="statement"><strong>Statement.</strong> Let U&#x27; be q-Runge complete in U inside a distinguished patch A. For each compact L in U&#x27;, there are a strongly q-complete ambient open V with A intersect V=U, a strongly q-convex exhaustion h of V, and c such that L is contained in U_c=A intersect {h&lt;c}, whose closure is compact in U&#x27;. Both V and V_c={h&lt;c} are strongly q-complete.</p>

**Proof.**

<p id="CL-3-p1">If U&#x27; is empty, all its cohomology groups are zero and the final approximation theorem is immediate. Otherwise an empty compact L can be enlarged by one point of U&#x27;. Choose the exhaustion psi and level b supplied by the definition for the resulting nonempty compact L. Put a=max_L psi, epsilon=(b-a)/3 and c=b-epsilon. These satisfy a+epsilon&lt;c&lt;b.</p>

<p id="CL-3-p2">Use Omega&#x27;=Omega minus (A minus U), so U is closed in Omega&#x27;. The proof of <a href="general-analytic-qn.md#QN-5">QN-5</a> works with arbitrary constant upper margin epsilon: apply <a href="general-analytic-qn.md#QN-3">QN-3</a> with delta=epsilon instead of 1; all remaining steps are unchanged, and the resulting h equals its extended function phi near U. Thus obtain a strongly q-complete neighbourhood V of U inside Omega&#x27; with psi&lt;=h|U&lt;psi+epsilon. For x in L, h(x)&lt;a+epsilon&lt;c. For x in U_c, psi(x)&lt;=h(x)&lt;c&lt;b. Since {psi&lt;=c} is compact and contained in {psi&lt;b}, the closure of U_c is compact in U&#x27;. Importantly, V contains all of U, whereas only its selected sublevel cuts out U_c inside U&#x27;; it is not asserted that U&#x27;=A intersect V.</p>

<p id="CL-3-p3">The function t-&gt;1/(c-t) on (-infinity,c) has positive first and second derivatives. Hence 1/(c-h) is strongly q-convex on V_c: its Levi form retains a positive multiple of the same positive subspace as the Levi form of h and adds a nonnegative rank-one term. Its sublevels are contained in compact h-sublevels strictly below c, and are closed there, so it is an exhaustion of V_c. For any compact K in V_c, choose max_K h&lt;b_0&lt;b_1&lt;c. The h-sublevels at b_0 and b_1 then have compact closures nested inside V_c. This checks exactly the q-Runge hypothesis needed by <a href="general-analytic-wl.md#WL-6">WL-6</a> for V_c inside V, including its two inner levels. Restricting the original finite ambient free resolution to these opens preserves its exactness.</p>

∎

## CL-4. Dense coherent restriction at each selected sublevel {#CL-4}

<p class="statement"><strong>Statement.</strong> For the opens in <a href="general-analytic-cl.md#CL-3">CL-3</a> and r=q-1, the restriction H^r(U,F)-&gt;H^r(U_c,F) has dense image in the canonical quotient topology.</p>

**Proof.**

<p id="CL-4-p1">Let E_0=O^p be the initial free module in the fixed ambient resolution. Form the square with top row H^r(V,E_0)-&gt;H^r(U,F), bottom row H^r(V_c,E_0)-&gt;H^r(U_c,F), and vertical arrows given by restriction. Closed-embedding identifications in <a href="general-analytic-cl.md#CL-1">CL-1</a> identify these rows with the maps induced by E_0-&gt;i_*F. The square commutes by functoriality of restriction. The two horizontal arrows are surjective by <a href="general-analytic-cl.md#CL-0">CL-0</a> applied on V and V_c, using the tails of the same restricted resolution. All arrows are continuous by <a href="general-analytic-cl.md#CL-1">CL-1</a>; the horizontal surjections are also open, although their openness is not needed for the following density argument.</p>

<p id="CL-4-p2">The left restriction has dense image: represent a class in H^r(V_c,E_0) by a closed smooth form, apply <a href="general-analytic-wl.md#WL-6">WL-6</a> using the verified inner levels from <a href="general-analytic-cl.md#CL-3">CL-3</a>, and pass through the topological comparisons of <a href="general-analytic-cl.md#CL-2">CL-2</a>. The WL degree endpoints q&gt;N are included in that existing proof, so there is no new dimension restriction here.</p>

<p id="CL-4-p3">To prove density on the right, take a nonempty open set O in H^r(U_c,F). Surjectivity of the bottom horizontal map makes its inverse image nonempty, and continuity makes that inverse image open. Density on the left gives a class from H^r(V,E_0) whose restriction lies in that inverse image. Its image along the top row is a class on U restricting into O. This argument uses neither Hausdorffness of cohomology nor a splitting of the coherent quotient.</p>

∎

## CL-5. Exhaustion, exact cochain lifting, and local coherent approximation {#CL-5}

<p class="statement"><strong>Statement.</strong> Under the hypotheses of <a href="general-analytic-cl.md#CL-3">CL-3</a>, H^(q-1)(U,F)-&gt;H^(q-1)(U&#x27;,F) has dense image. In a common countable Stein-piece model, the restrictions of cocycles from U are already dense in the cocycle space over U&#x27;.</p>

**Proof.**

<p id="CL-5-p1">Choose compact sets K_n exhausting U&#x27;, with their interiors covering U&#x27;. Apply <a href="general-analytic-cl.md#CL-3">CL-3</a> inductively, including K_n and the compact closure of the preceding chosen open in the next compact set. This gives opens U_n with closure(U_n) contained in U_(n+1), each closure compact in U&#x27;, and union U_n=U&#x27;. The ambient V and exhaustion h can vary with n; <a href="general-analytic-cl.md#CL-4">CL-4</a> applies to every resulting restriction from the fixed U to U_n. No common ambient exhaustion for all n is assumed.</p>

<p id="CL-5-p2">Choose a countable basis W of relatively compact Stein pieces in U, small enough to lie in distinguished patches for F. Let W&#x27; be the subfamily with compact closure in U&#x27;, and W_n the subfamily with compact closure in U_n. These are Leray covers of U&#x27;, U_n; W covers U. The W_n are nested and their union is W&#x27;: the compact closure of any member of W&#x27; is covered by the nested U_n and is contained in one of them. Put P^bullet=C^bullet(W,F), E^bullet=C^bullet(W&#x27;,F), and E_n^bullet=C^bullet(W_n,F). Every projection P^r-&gt;E_n^r and E_(n+1)^r-&gt;E_n^r simply forgets factors, and is surjective. A cochain can be extended by setting the missing coordinates to zero. This is only a degreewise lift: zero extension need not commute with delta and must not be used to lift cocycles.</p>

<p id="CL-5-p3">There is a degreewise topological isomorphism E^bullet=lim_n E_n^bullet. Every finite tuple of indices in W&#x27; lies entirely in some W_n; compatible families therefore specify exactly all the coordinates of E. A basic product neighbourhood involves only finitely many coordinates and finitely many seminorms on them, all visible at one such n, which proves the topological assertion. The differentials agree because their coordinate formulas use finitely many restrictions. This identifies complexes, not cohomology with an inverse limit of cohomology groups.</p>

<p id="CL-5-p4">Set r=q-1 and let z be a cocycle of E. Given a basic neighbourhood of z in Z^r(E), choose n large enough to contain all its tested coordinates, and choose a zero-neighbourhood N in Z^r(E_n) whose pullback is inside that neighbourhood translated by -z. The quotient map pi_n:Z^r(E_n)-&gt;H^r(E_n) is open: the saturation of any open set is the union of its translates by coboundaries. By <a href="general-analytic-cl.md#CL-4">CL-4</a>, H^r(P)-&gt;H^r(E_n) has dense image. Hence there is x in Z^r(P) with [x_n] in pi_n(z_n+N). Equivalently z_n-x_n-delta a is in N after replacing N by a symmetric smaller zero-neighbourhood if necessary, for some a in E_n^(r-1).</p>

<p id="CL-5-p5">If r&gt;=1, use degreewise surjectivity to choose b in P^(r-1) with b_n=a, and put x&#x27;=x+delta b. Then delta x&#x27;=0 because delta x=0 and delta^2=0; moreover z_n-x&#x27;_n=z_n-x_n-delta a lies in N. Thus the restriction of x&#x27; to E lies in the prescribed neighbourhood of z. If r=0 there are no coboundaries or negative-degree cochains, and the same argument works with a=b=0. This proves density of Z^r(P)-&gt;Z^r(E), and passage to quotient gives the stated density of H^r(U,F)-&gt;H^r(U&#x27;,F). It is the concrete coordinate-surjective case of the already supplied Frechet Proposition 3.1(4), with its lifting hypotheses now checked on the actual complexes.</p>

<p id="CL-5-p6">If desired, a convergent sequence of cocycles is obtained by applying the preceding construction to a decreasing countable neighbourhood basis at z. The cocycle space is Frechet, so it is first countable. This does not require cohomology itself to be Hausdorff. The proof retains F and every original nilpotent or torsion direction throughout. It proves the local approximation lemma only: global q-bump comparison, its connecting-map continuity, the final global inverse-limit vanishing, and the separate relative finite-complex theorem are not concluded from it.</p>

∎

## Sources {#CL-sources}

Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), author edition of 21 June 2012. IX.4.C, printed p. 423, quotient topologies and Dolbeault comparison; IX.4.E, Lemma 4.9, printed pp. 424-425, local coherent approximation. The independently written arguments above follow the cited mathematics, with the explicit domains, signs and comparisons given here.
