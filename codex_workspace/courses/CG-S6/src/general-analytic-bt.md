# Balanced nuclear tensors and analytic restriction {#general-analytic-bt}

Written by GPT-6 Astra (OpenAI), at Ultra, October 2026. Independent exposition: CC0-1.0.

Read this argument with the [general surface theorem](general-proper-flat-surface-base-change.md#general-surface-theorem) and its [prerequisite guide](general-proper-flat-surface-base-change.md#general-prerequisites). Result identifiers link to the exact arguments in this companion family.

The supporting arguments retain linear mathematical notation: `->` denotes a map, `^` an exponent or cohomological degree, `_` a subscript, and `direct_sum` a direct sum. Parentheses specify grouping. Algebraic quotients and completed topological tensor products are distinguished explicitly; a quotient is not silently replaced by its completion.

## Conventions {#BT-conventions}

<p>A and the other base algebras are commutative unital nuclear Frechet algebras over C. Their multiplication, and all module actions, are jointly continuous. All modules in this packet are nuclear Hausdorff Frechet spaces before a balanced quotient is formed.</p>

<p>The completed scalar tensor is the common projective/injective tensor of <a href="general-analytic-ns.md#NS-3">NS-3</a>. A nuclear free A-module is A hat_tensor V for a nuclear Frechet space V, with A acting in the first factor; it need not have finite rank.</p>

<p>E hat_tensor_A F denotes (E hat_tensor F)/im(delta), where delta:E hat_tensor A hat_tensor F -&gt; E hat_tensor F sends x tensor a tensor y to ax tensor y minus x tensor ay. The image is not silently replaced by its closure. This quotient, with its quotient topology, can be non-Hausdorff; no further Hausdorff completion is taken.</p>

<p>Chain differentials lower the index. Homology is ker(d_q)/im(d_(q+1)), with the quotient topology, which need not be Hausdorff. The long exact sequences and the positive-degree resolution comparison below assert algebraic exactness/isomorphisms, not unproved topological strictness.</p>

<p>E and F are transverse over A if their balanced tensor is Hausdorff and all positive-degree bar-derived Tor groups vanish. In that case their degree-zero balanced tensor is a nuclear Frechet space.</p>

<p>For cochain complexes, bounded on the right means E^q=0 for q&gt;N for some finite N. No lower bound is implied.</p>

<p><a href="general-analytic-bt.md#BT-3">BT-3</a> is formulated on ambient Stein manifolds, with arbitrary coherent modules, exactly as used in the graph-chart construction of the retained S6 theorem. It does not require the original total space or its fibres to be smooth or reduced. The statement is about open subsets of the base, not points or arbitrary analytic base changes.</p>

## BT-0. The balanced quotient and a split underlying-vector-space bar resolution {#BT-0}

<p class="statement"><strong>Statement.</strong> Every nuclear A-module has a nuclear free augmented bar resolution split as a complex of topological C-vector spaces. Balancing a nuclear free module against any nuclear module gives the ordinary completed scalar tensor of its generator space with that module, as a topological isomorphism.</p>

**Proof.**

<p id="BT-0-p1">For a nuclear A-module F set L_q=A^(hat_tensor(q+1)) hat_tensor F for q&gt;=0 and L_(-1)=F. Let A act on the first A-factor. The augmentation is d_0(a_0 tensor y)=a_0 y. For q&gt;=1, d_q is the sum of the q adjacent-product maps, indexed i=0,...,q-1 with coefficient (-1)^i, and the final action map with coefficient (-1)^q: the latter sends a_0 tensor ... tensor a_q tensor y to a_0 tensor ... tensor a_(q-1) tensor a_q y. Joint continuity of multiplication and action, followed by the projective tensor universal property, defines each of these maps on the completed tensors. Each map is A-linear; the spaces L_q are nuclear free by <a href="general-analytic-ns.md#NS-2">NS-2</a>.</p>

<p id="BT-0-p2">Write face_i for the unsigned adjacent-product or final-action map. Associativity of multiplication and of the module action gives face_i face_j=face_(j-1) face_i whenever i&lt;j, with source in the appropriate bar degree. The terms of d_(q-1)d_q pair off using this identity and have opposite signs. Thus d squared is zero, including the augmentation equation. These identities hold first on pure tensors and then on the completions by continuity and density.</p>

<p id="BT-0-p3">Define h_q:L_q-&gt;L_(q+1) by inserting 1_A at the front, also for q=-1. In d_(q+1)h_q the first face removes the inserted unit and gives the identity. Every other face is minus the matching term of h_(q-1)d_q. Hence d_(q+1)h_q+h_(q-1)d_q=Id_(L_q), with d_0 h_(-1)=Id_F at the augmented degree. These are continuous C-linear maps; h is not asserted to be A-linear. For q&gt;=0, the image of d_(q+1) equals ker(d_q), which is closed. The map d_(q+1)h_q is a continuous projection onto that kernel. The augmentation is likewise split by h_(-1). This proves both exactness and the claimed underlying topological splitting.</p>

<p id="BT-0-p4">Now let P=A hat_tensor V. On P hat_tensor F define Q((a tensor v) tensor y)=v tensor ay and S(v tensor y)=(1 tensor v) tensor y. Both maps are continuous and QS=Id. Define H:P hat_tensor F -&gt; P hat_tensor A hat_tensor F by H((a tensor v) tensor y)=(1 tensor v) tensor a tensor y. If delta is the balancing map, then delta H=Id-SQ; also Q delta=0. These identities extend from pure tensors to the completions. Consequently ker(Q)=im(delta), not merely its closure. This image is closed because Q has Hausdorff target. The quotient P hat_tensor_A F is canonically V hat_tensor F, with a continuous inverse induced by S. Symmetry gives E hat_tensor_A (A hat_tensor V)=E hat_tensor V. In particular these free balanced products are Hausdorff and nuclear.</p>

∎

## BT-1. Bar-derived Tor, signed symmetry and the long exact sequence {#BT-1}

<p class="statement"><strong>Statement.</strong> The bar complex defines balanced Tor with degree zero equal to the actual balanced quotient. It is symmetric for the commutative algebra A, has zero positive groups when either module is nuclear free, and gives the long exact Tor sequence for a short exact sequence of nuclear Frechet modules.</p>

**Proof.**

<p id="BT-1-p1">Using <a href="general-analytic-bt.md#BT-0">BT-0</a> on E hat_tensor_A L_q(F), identify its qth term with T_q(E,F)=E hat_tensor A^(hat_tensor q) hat_tensor F. For q&gt;=1 its differential on x tensor a_1 tensor ... tensor a_q tensor y is a_1 x tensor a_2 tensor ... tensor a_q tensor y, plus the adjacent interior products a_i a_(i+1) with coefficient (-1)^i for 1&lt;=i&lt;q, plus x tensor a_1 tensor ... tensor a_(q-1) tensor a_q y with coefficient (-1)^q. This formula follows by absorbing the first free A-factor into E. It also follows directly from <a href="general-analytic-bt.md#BT-0">BT-0</a> that the differential squares to zero. Define Torhat_q^A(E,F)=H_q(T(E,F)); since the degree-one differential is precisely delta, Torhat_0 is the balanced quotient as defined, without closing its relations.</p>

<p id="BT-1-p2">The symmetry is an actual signed chain map, not an unspecified equality up to sign. In degree q put R_q(x tensor a_1 tensor ... tensor a_q tensor y)=(-1)^(q(q+1)/2) y tensor a_q tensor ... tensor a_1 tensor x. For the unsigned reversal, the face indexed i becomes the face indexed q-i, so its differential gains the factor (-1)^q. The prefactors satisfy (-1)^(q(q+1)/2) (-1)^q=(-1)^((q-1)q/2). Therefore d R_q=R_(q-1) d. Each R_q is a topological isomorphism and its inverse is the same signed reversal in the other direction. It induces symmetry of Tor, including the quotient topology in degree zero.</p>

<p id="BT-1-p3">If E=A hat_tensor V, its balanced tensor with the augmented bar resolution of F is V hat_tensor L(F). The contraction Id_V hat_tensor h from <a href="general-analytic-bt.md#BT-0">BT-0</a> is well-defined as a C-linear contraction after this free identification. Thus positive homology vanishes and degree zero is V hat_tensor F. If F is nuclear free, apply the just-proved symmetry. In particular nuclear free modules are transverse to every nuclear module.</p>

<p id="BT-1-p4">Let 0-&gt;E_1 --i--&gt; E_2 --p--&gt; E_3-&gt;0 be a short exact sequence of nuclear Frechet A-modules. For fixed F every bar degree is a scalar tensor with the nuclear space A^(hat_tensor q) hat_tensor F. <a href="general-analytic-ns.md#NS-3">NS-3</a> gives a short exact sequence of the three bar complexes in each degree, with a closed inclusion and an open surjection. The usual connecting map can be constructed explicitly: lift a cycle c in the E_3 complex to b in the E_2 term; then db=i(a) for a unique a in the E_1 term. Injectivity of i and d squared zero show da=0. Set the connecting class to [a]. Replacing b by b+i(a&#x27;) changes a by da&#x27;; replacing c by c+dc&#x27; and lifting c&#x27; changes b by a boundary and does not change its connecting class.</p>

<p id="BT-1-p5">The element chase proves exactness at all three types of positions. If the image of a cycle b from the middle complex is a boundary dc&#x27;, lift c&#x27; and subtract that lifted boundary from b; the result is the image of a cycle of the first complex. If a cycle c has connecting class zero, db=i(da&#x27;) for a lift b, so b-i(a&#x27;) is a cycle lifting c. If a cycle a in the first complex becomes a boundary db=i(a), then p(b) is a cycle and its connecting class is [a]. Degree-zero surjectivity follows from degree-zero surjectivity of p. These statements give the whole algebraic long exact sequence, ending with E_1 hat_tensor_A F -&gt; E_2 hat_tensor_A F -&gt; E_3 hat_tensor_A F -&gt; 0. Symmetry supplies the analogous sequence in the other variable.</p>

<p id="BT-1-p6">In particular the balanced tensor functor is right exact in this algebraic sense. The last map of a balanced right-exact sequence is also open for the quotient topologies: the corresponding map of unbalanced completed scalar tensors is open by <a href="general-analytic-ns.md#NS-3">NS-3</a>, the two balancing quotient maps are open, and the image of an open saturated set can be computed through these maps. Thus a balanced cokernel may be calculated with its actual quotient topology. None of this asserts that arbitrary higher Tor groups are Hausdorff, or that the complete long exact sequence is topologically strict.</p>

∎

## BT-2. Computing Tor with a nuclear free resolution without assuming an A-linear splitting {#BT-2}

<p class="statement"><strong>Statement.</strong> If L_*-&gt;F is any exact resolution by nuclear free A-modules and continuous A-linear maps, then H_q(E hat_tensor_A L_*) is canonically Torhat_q^A(E,F). In degree zero the comparison respects the quotient topologies. The positive-degree assertion required here is algebraic.</p>

**Proof.**

<p id="BT-2-p1">Let B_(-1)=F and B_j=ker(L_j-&gt;L_(j-1)) for j&gt;=0, interpreting the degree-zero map as the augmentation. Exactness says B_j=im(L_(j+1)-&gt;L_j). Since it is a kernel of a continuous map to a Hausdorff space, B_j is closed and nuclear by <a href="general-analytic-ns.md#NS-2">NS-2</a>. The induced maps L_j-&gt;B_(j-1) are surjective maps of Frechet spaces and therefore open. We have short exact sequences 0-&gt;B_j-&gt;L_j-&gt;B_(j-1)-&gt;0 in the precise category used by <a href="general-analytic-bt.md#BT-1">BT-1</a>. No complementary A-submodule or continuous A-linear section has been assumed.</p>

<p id="BT-2-p2">Because L_j is nuclear free, its positive Tor with E vanishes. The long exact sequence gives Torhat_m(E,B_(j-1))=Torhat_(m-1)(E,B_j) canonically for m&gt;1, and Torhat_1(E,B_(j-1)) identifies with ker(E hat_tensor_A B_j -&gt; E hat_tensor_A L_j). Iterating the first equality shows for q&gt;=1 that Torhat_q(E,F) identifies with ker(E hat_tensor_A B_(q-1) -&gt; E hat_tensor_A L_(q-1)); for q=1 this is just the second assertion with j=0.</p>

<p id="BT-2-p3">To compare with the proposed complex, factor its differential in degree q as r_q:E hat_tensor_A L_q -&gt; E hat_tensor_A B_(q-1), followed by j_(q-1):E hat_tensor_A B_(q-1) -&gt; E hat_tensor_A L_(q-1). Right exactness makes r_q surjective and says ker(r_q) is the image of E hat_tensor_A B_q. That image is also im(d_(q+1)), because L_(q+1)-&gt;B_q is surjective and stays surjective after balanced tensor. It follows directly that ker(d_q)/im(d_(q+1)) maps bijectively by r_q onto ker(j_(q-1)). This is exactly the group found by dimension shifting. In degree zero, right exactness identifies the cokernel of d_1 with E hat_tensor_A F, and the open-quotient observation of <a href="general-analytic-bt.md#BT-1">BT-1</a> makes that identification topological.</p>

<p id="BT-2-p4">The identifications are canonical for the given augmentation: their connecting maps were defined from lifts with an independence proof in <a href="general-analytic-bt.md#BT-1">BT-1</a>, and r_q is induced by the actual differential. If a chain map between two such resolutions respects their augmentations, applying the same lifts to that map shows that it commutes with all these identifications. No general lifting property for nuclear free modules, which would require additional hypotheses, was used. When the resulting positive Tor groups vanish and degree zero is Hausdorff, this comparison does give a strict augmented resolution: all differential images are then kernels in Frechet terms and the augmentation target is Frechet.</p>

∎

## BT-3. Transverse restriction to a Stein open subset of the base {#BT-3}

<p class="statement"><strong>Statement.</strong> Let X,Y be Stein manifolds, U contained relatively compactly in X and V contained relatively compactly in Y be Stein open sets, and U&#x27; be any Stein open subset of U. If F is coherent on X x Y, then B=O(U&#x27;) and M=Gamma(U x V,F) are transverse over A=O(U), and the canonical map B hat_tensor_A M -&gt; Gamma(U&#x27; x V,F) is a topological isomorphism. Coherent modules supported on full nonreduced analytic subspaces are included.</p>

**Proof.**

<p id="BT-3-p1">Put W=X x Y and K=closure(U) x closure(V), a compact subset of W. The pinned Stein product proposition makes W Stein. Construct a resolution on the fixed U x V as follows. Cartan A supplies global sections of F whose germs generate at every point. At any one point finitely many suffice; the coherent cokernel of their generating map has zero stalk there and therefore vanishes on a neighbourhood. A finite subcover of K consequently selects finitely many global sections giving a map u_0:O_W^(r_0)-&gt;F which is surjective near K. Its kernel F_0 on the entire W is coherent. Apply the same argument to F_0, obtaining u_1:O_W^(r_1)-&gt;F_0 surjective near K. Repeat with F_j=ker(u_j) on W. Compose u_j with the inclusion F_(j-1)-&gt;O_W^(r_(j-1)) to obtain d_j for j&gt;=1.</p>

<p id="BT-3-p2">These maps form a complex globally, and its augmentation and every differential are exact on U x V because every chosen map is surjective at every point of K. Although the neighbourhood of K on which a particular map is surjective can vary with j, the fixed set U x V is contained in each such neighbourhood. Thus no infinite intersection of shrinking neighbourhoods is needed. Every free term has finite rank, but the sequence may continue indefinitely to the left; no bounded finite resolution or uniform length has been claimed.</p>

<p id="BT-3-p3">Restrict this sheaf resolution to U x V. Its kernels are coherent, and this product is Stein. Cartan B applied separately to 0-&gt;F_j-&gt;O^(r_j)-&gt;F_(j-1)-&gt;0 on that open set gives an exact sequence of global sections in every degree, including the augmentation. The section spaces are nuclear Frechet by <a href="general-analytic-ns.md#NS-4">NS-4</a>, and the maps to their closed cycle spaces are open. Moreover <a href="general-analytic-ns.md#NS-5">NS-5</a> gives O(U x V)^(r_j)=A hat_tensor O(V)^(r_j), so the resolution is nuclear free over A. The same statements hold after restriction to U&#x27; x V, since U&#x27; is Stein; relative compactness of U&#x27; in U is not required.</p>

<p id="BT-3-p4">Apply B hat_tensor_A to the section complex. <a href="general-analytic-bt.md#BT-0">BT-0</a> identifies each resulting term with B hat_tensor O(V)^(r_j), and <a href="general-analytic-ns.md#NS-5">NS-5</a> identifies that space with O(U&#x27; x V)^(r_j). These identifications send b tensor s to the product of b with the restricted section. They commute with the differentials: for a separated holomorphic coefficient this follows from multiplication and restriction, and general coefficients follow by the dense product-section identification and continuity of multiplication. Thus the tensor complex is exactly the restricted section resolution, with its actual matrices, not merely a complex having isomorphic terms.</p>

<p id="BT-3-p5">That restricted resolution has zero positive homology and degree-zero cokernel Gamma(U&#x27; x V,F). <a href="general-analytic-bt.md#BT-2">BT-2</a> therefore gives vanishing of all positive Torhat groups and the claimed degree-zero identification. It is topological because both sides are the same quotient of the degree-zero free section space by the image of its preceding differential. The image is closed, being the kernel of the surjective map to the Frechet section space Gamma(U&#x27; x V,F). Thus the balanced tensor is Hausdorff, proving transversality.</p>

<p id="BT-3-p6">The ambient hypotheses do not impose smoothness on a space supporting F. In the proper-map construction a local full analytic space is embedded, together with its map to a base chart, as a closed analytic graph in a product of Stein manifolds. Its coherent sheaf pushes forward to a coherent module on that ambient product. All equations, nilpotents and module relations stay in that module, so <a href="general-analytic-bt.md#BT-3">BT-3</a> applies to it without replacing the graph by its reduced space. The finite-intersection graph construction is supplied by the pinned Stein-piece lemma. This explains why the lemma covers the chartwise construction needed for the original S6 scope. It does not prove the entire finite-complex construction or extend this open-restriction statement to a point of the base.</p>

∎

## BT-4. Transversality through kernels, successive base algebras and bounded-right acyclic complexes {#BT-4}

<p class="statement"><strong>Statement.</strong> Transversality is preserved in the kernel of a short exact sequence whose middle and last terms are transverse. It composes under transverse scalar extension. Tensoring a bounded-right cochain complex of transverse modules preserves acyclicity in any specified upper range.</p>

**Proof.**

<p id="BT-4-p1">Let 0-&gt;E_1-&gt;E_2-&gt;E_3-&gt;0 be a short exact sequence and suppose E_2,E_3 are transverse to M. Their higher Tor groups vanish, so the long exact sequence makes all positive Tor groups of E_1 vanish and gives an algebraically exact sequence 0-&gt;M hat_tensor_A E_1-&gt;M hat_tensor_A E_2-&gt;M hat_tensor_A E_3-&gt;0. The first map is a continuous injection into a Hausdorff space. This forces its domain to be Hausdorff: distinct domain points have distinct images, which have disjoint open neighbourhoods whose preimages separate the points. Hence the balancing relation space defining M hat_tensor_A E_1 is closed. This domain is now nuclear Frechet by <a href="general-analytic-ns.md#NS-2">NS-2</a>. Its image is the closed kernel of the last map; the open mapping theorem applied to its continuous bijection onto that kernel proves that it has exactly the subspace topology. The last map is open as well. This proves transversality of E_1 and strictness of the resulting short exact sequence, without assuming Hausdorffness at the start.</p>

<p id="BT-4-p2">Let A-&gt;A_1-&gt;A_2 be continuous unital algebra maps, and suppose both A_1 and A_2 are transverse to the A-module E. Use the bar resolution L_q=A hat_tensor V_q of E. By <a href="general-analytic-bt.md#BT-2">BT-2</a> and transversality, A_1 hat_tensor_A L_* is an exact augmented nuclear free A_1-resolution of E_1=A_1 hat_tensor_A E, with terms A_1 hat_tensor V_q. Apply <a href="general-analytic-bt.md#BT-2">BT-2</a> once more over A_1. In every degree, balancing its free terms with A_2 gives A_2 hat_tensor V_q, exactly the complex obtained by balancing the original L_* with A_2 over A. The identifications commute with the differential because they are the maps induced by multiplication in A_2. Thus Torhat_q^(A_1)(A_2,E_1) is Torhat_q^A(A_2,E) for q&gt;=0. In degree zero this is an identification of quotient topologies, by <a href="general-analytic-bt.md#BT-2">BT-2</a>, so it is Hausdorff; in positive degrees it is zero. Therefore A_2 is transverse to E_1 over A_1. This argument uses free-term identifications, not an unproved associativity rule for arbitrary non-Hausdorff balanced quotients.</p>

<p id="BT-4-p3">Now let E^* be a cochain complex with E^q=0 for q&gt;N, and suppose each E^q is transverse to M. Suppose also H^q(E)=0 for q&gt;=k. Its cycle spaces Z^q=ker(d^q) are closed nuclear submodules. For q&gt;=k-1, the sequence 0-&gt;Z^q-&gt;E^q-&gt;Z^(q+1)-&gt;0 is exact because H^(q+1)(E)=0. Start above N with the zero cycle space. Descending one degree at a time, apply the first paragraph to this sequence; it shows Z^q is transverse to M for all q&gt;=k-1 and that each tensored sequence is strict exact. Each individual degree is reached in finitely many steps from N; there is no assertion about an inverse limit of this induction.</p>

<p id="BT-4-p4">For q&gt;=k, factor the tensored differential through M hat_tensor_A Z^(q+1). The second map into M hat_tensor_A E^(q+1) is injective by the just-proved exact sequence in degree q+1. Its kernel at degree q is therefore precisely M hat_tensor_A Z^q, embedded by the sequence in degree q. The differential from degree q-1 surjects onto that same subspace by the sequence in degree q-1. Hence the tensored complex has zero cohomology in every degree q&gt;=k, as claimed. The bound above is essential to this argument and has not been omitted.</p>

∎

## BT-5. The correctly signed comparison cone and preservation of a quasi-isomorphism range {#BT-5}

<p class="statement"><strong>Statement.</strong> For bounded-right complexes E,F with all terms transverse to M, tensoring an A-linear chain map preserves the property of being an isomorphism on cohomology in degrees q&gt;=k and a surjection in degree k-1.</p>

**Proof.**

<p id="BT-5-p1">For f:E^*-&gt;F^* define C^q=E^q direct_sum F^(q-1) and D^q(e,y)=(d_E e, f(e)-d_F y). The second component of D^(q+1)D^q is f(d_E e)-d_F(f(e))+d_F squared(y), which is zero because f is a cochain map. The first component is zero as well. Let F[-1]^q=F^(q-1) with differential -d_F. Then y-&gt;(0,y) and (e,y)-&gt;e give a short exact sequence of complexes 0-&gt;F[-1]-&gt;C-&gt;E-&gt;0. The connecting map H^q(E)-&gt;H^q(F) is H^q(f): a closed e lifts to (e,0), and its differential is (0,f(e)). This specifies both the shift and its differential rather than writing an unspecified equivalence up to sign.</p>

<p id="BT-5-p2">The associated exact sequence has segment H^(q-1)(E) --H^(q-1)(f)--&gt; H^(q-1)(F) -&gt; H^q(C) -&gt; H^q(E) --H^q(f)--&gt; H^q(F). The connecting-map construction and the three element chases are exactly those given in <a href="general-analytic-bt.md#BT-1">BT-1</a>, with degrees reindexed. This segment shows H^q(C)=0 if and only if H^(q-1)(f) is surjective and H^q(f) is injective. Therefore the stated isomorphism/surjection range for f is equivalent to acyclicity of C in degrees q&gt;=k.</p>

<p id="BT-5-p3">A finite direct sum of modules transverse to M is transverse: its two-sided bar complex is the finite direct sum of their bar complexes, and its degree-zero quotient is the corresponding finite direct sum of Hausdorff balanced quotients. Thus every term of C is transverse to M. The cone is bounded on the right because E and F are. <a href="general-analytic-bt.md#BT-4">BT-4</a> shows that M hat_tensor_A C is acyclic in degrees q&gt;=k. The same finite direct-sum and differential formulas identify it with the cone of Id_M hat_tensor_A f. Applying the preceding exact-sequence criterion gives injectivity of the tensor map on H^q for q&gt;=k and surjectivity for q&gt;=k-1; combining them gives the required isomorphisms. The known incorrect matrix with second row (-f,+d_F) is not used, and no new source correction is being claimed here.</p>

∎

## BT-6. Coherent vertical restriction is subnuclear over the base algebra {#BT-6}

<p class="statement"><strong>Statement.</strong> In the ambient Stein setting, let S be relatively compact and Stein in a Stein manifold Y, let U&#x27; be relatively compact in U and U relatively compact in a Stein manifold Z, with U,U&#x27; Stein. For coherent F on Y x Z, restriction Gamma(S x U,F)-&gt;Gamma(S x U&#x27;,F) is O(S)-subnuclear. The nuclear and subnuclear classes have the composition properties needed in the relative construction.</p>

**Proof.**

<p id="BT-6-p1">Use the A-nuclear definition and free restriction formula of <a href="general-analytic-ns.md#NS-6">NS-6</a>. Call a continuous A-linear map f:E-&gt;F A-subnuclear if there is a nuclear Frechet A-module P and an open surjection p:P-&gt;E such that fp is A-nuclear. For an A-nuclear representation, precomposition by a continuous A-linear map preserves equicontinuity of the coefficient maps, and postcomposition preserves boundedness of the target vectors. The represented series is therefore A-nuclear after either composition. Concatenation of finitely many representations proves closure under finite sums.</p>

<p id="BT-6-p2">For precomposition of a subnuclear map f with u:T-&gt;E, use the pullback P&#x27;={(t,z) in T x P:u(t)=p(z)}. It is closed in a product of nuclear Frechet modules, hence nuclear by <a href="general-analytic-ns.md#NS-2">NS-2</a>. Its projection pi:P&#x27;-&gt;T is surjective. It is also open: the image of a basic product neighbourhood, intersected with P&#x27;, is O_T intersection u^(-1)(p(O_P)), which is open because p is open; translations give the assertion at every point. The map (fu)pi equals (fp) followed by projection P&#x27;-&gt;P on the input, so is A-nuclear. This proves subnuclearity of fu. Postcomposition keeps the same surjection p and follows from the nuclear case. Finite sums follow by taking the fibre product of finitely many witnessing surjections over the same domain; the same closedness and openness argument applies. No automatic corestriction to an arbitrary closed target submodule is asserted.</p>

<p id="BT-6-p3">For the analytic restriction, Cartan A on the Stein product Y x Z and compactness of closure(S) x closure(U) select finitely many global sections of F generating near that compact set, exactly as in <a href="general-analytic-bt.md#BT-3">BT-3</a>. They give a finite free sheaf L_0 and a surjection L_0-&gt;F on S x U. Its coherent kernel has zero positive cohomology there by Cartan B. Thus p:Gamma(S x U,L_0)-&gt;Gamma(S x U,F) is a continuous open surjection of nuclear Frechet A-modules, A=O(S). Its source is A hat_tensor O(U)^r by <a href="general-analytic-ns.md#NS-5">NS-5</a>.</p>

<p id="BT-6-p4">In the commutative restriction square, the free vertical arrow Gamma(S x U,L_0)-&gt;Gamma(S x U&#x27;,L_0) is A-nuclear by <a href="general-analytic-ns.md#NS-6">NS-6</a> because U&#x27; is relatively compact in U. The bottom arrow to Gamma(S x U&#x27;,F) is continuous and A-linear. Its composition with the free vertical arrow is the coherent restriction composed with p. The ideal property from the first paragraph makes that composition A-nuclear. The surjection p is therefore a witness to the claimed subnuclearity. Coherent support, nilpotents and singularities remain in F; they are not removed by the free presentation.</p>

<p id="BT-6-p5">This finishes the coherent restriction input but not the next corestriction theorem: an A-subnuclear map whose range lies in a closed submodule is not here declared subnuclear into that smaller codomain. The remaining source argument adds scalar-nuclear shrinking of the base algebra and transversality of the target quotient. Those hypotheses and their proof remain part of the open relative perturbation chain.</p>

∎

## Sources {#BT-sources}

Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), author edition of 21 June 2012. . The independently written arguments above follow the cited mathematics, with the explicit domains, signs and comparisons given here.
