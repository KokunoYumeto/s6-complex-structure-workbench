# Finite complexes and canonical full-fibre comparison {#general-analytic-fc}

Written by GPT-6 Astra (OpenAI), at Ultra, October 2026. Independent exposition: CC0-1.0.

Read this argument with the [general surface theorem](general-proper-flat-surface-base-change.md#general-surface-theorem) and its [prerequisite guide](general-proper-flat-surface-base-change.md#general-prerequisites). Result identifiers link to the exact arguments in this companion family.

The supporting arguments retain linear mathematical notation: `->` denotes a map, `^` an exponent or cohomological degree, `_` a subscript, and `direct_sum` a direct sum. Parentheses specify grouping. Algebraic quotients and completed topological tensor products are distinguished explicitly; a quotient is not silently replaced by its completion.

## Conventions {#FC-conventions}

<p>Use the nuclear algebra, balanced tensor, transverse module and radius conventions of RP and BT. Algebraic cohomology can be non-Hausdorff; no closure of a boundary space is inserted.</p>

<p>Complexes are cochain complexes. Bounded above means zero in degrees greater than one fixed integer. A finite-free-term complex may extend indefinitely towards negative degrees. It is called bounded only after both ends have been bounded.</p>

<p>For h:L-&gt;E the comparison complex is C(h)^k=L^k direct_sum E^(k-1), with D(l,e)=(d_L l,h(l)-d_E e). This is the verified <a href="general-analytic-bt.md#BT-5">BT-5</a> convention. Every shift and every new generator below uses this same differential.</p>

<p>Complex analytic spaces are Hausdorff and retain their full local quotient structure. Closed embeddings and coherent modules are understood scheme-theoretically, not after reduction.</p>

## FC-0. Finite generation of the highest remaining cohomology after shrinking {#FC-0}

<p class="statement"><strong>Statement.</strong> Let A be fully nuclear and f:E-&gt;F a quasi-isomorphism of bounded-above complexes of fully transverse nuclear A-modules. Assume every f^k is A-subnuclear. If E and F have zero cohomology above q, then H^q(E_t) and H^q(F_t) are finitely generated A_t-modules for every t&lt;1. The same statement applies after any initial radius restriction, with radii rescaled as in <a href="general-analytic-rp.md#RP-1">RP-1</a>.</p>

**Proof.**

<p id="FC-0-p1">For k&gt;=q, acyclicity in degree k+1 gives strict exact sequences 0-&gt;Z^k(E)-&gt;E^k-&gt;Z^(k+1)(E)-&gt;0. The cycle spaces are closed nuclear modules. Starting above a common upper bound and descending, <a href="general-analytic-bt.md#BT-4">BT-4</a> makes each Z^k(E), k&gt;=q, fully A-transverse; the same holds for F. These exact sequences also identify the base change of Z^k with the cycle space after restriction. In particular F^q/Z^q(F) is topologically Z^(q+1)(F), and is fully transverse. Surjectivity onto this closed cycle space gives the quotient topology by open mapping.</p>

<p id="FC-0-p2">Choose an intermediate radius s with t&lt;s&lt;1. Restricting f^q on its source to Z^q(E) preserves subnuclearity by <a href="general-analytic-bt.md#BT-6">BT-6</a>. Its image lies in Z^q(F), but subnuclearity into that closed target is not inferred directly. Apply <a href="general-analytic-rp.md#RP-0">RP-0</a> to the scalar-nuclear map A-&gt;A_s. Its transverse hypotheses hold for Z^q(E), F^q and F^q/Z^q(F) by the preceding paragraph. Thus g:Z^q(E_s)-&gt;Z^q(F_s) is A_s-subnuclear.</p>

<p id="FC-0-p3"><a href="general-analytic-bt.md#BT-5">BT-5</a> makes f_s a quasi-isomorphism. Hence a:F_s^(q-1) direct_sum Z^q(E_s)-&gt;Z^q(F_s), a(y,z)=d_F y+g(z), is surjective: the class of any target cycle has a preimage under H^q(f_s), and the remaining difference is a boundary. All three modules here are fully A_s-transverse, and a is a continuous open surjection of Frechet spaces. The map u(y,z)=g(z) is A_s-subnuclear by composition. <a href="general-analytic-rp.md#RP-5">RP-5</a> applied to a-u gives a finitely generated cokernel after passing from A_s to A_t; this is a permissible radius t/s in A_s by <a href="general-analytic-rp.md#RP-1">RP-1</a>.</p>

<p id="FC-0-p4">The changed map a-u is d_F on the first summand and zero on the second. The cycle identifications from the first paragraph show that its cokernel is exactly Z^q(F_t)/d_F(F_t^(q-1))=H^q(F_t), not its Hausdorff completion. <a href="general-analytic-bt.md#BT-5">BT-5</a> identifies that module with H^q(E_t). This proves the assertion at its algebraic strength and does not require a closed coboundary space.</p>

∎

## FC-1. Comparison of cones and attachment of one finite free term {#FC-1}

<p class="statement"><strong>Statement.</strong> A quasi-isomorphism f:E-&gt;F induces a quasi-isomorphism C(h)-&gt;C(fh), (l,e)|-&gt;(l,f(e)). For a finite-free partial complex L in degrees &gt;=q, generators of H^q(C(h)) represented by cycles specify an additional term L^(q-1), with the exact signs needed to kill that cohomology group while leaving all higher groups unchanged.</p>

**Proof.**

<p id="FC-1-p1">The displayed cone map is a chain map: applying its differential on either side gives (d_L l,f h(l)-f d_E e), since f d_E=d_F f. Its action on cohomology can be checked without a topological five-lemma assumption. For injectivity, suppose a closed (l,e) maps to D(a,b) in C(fh). Then l=d_L a and f(e-h(a))=-d_F b. Also d_E(e-h(a))=0 by the cycle and chain-map equations. Injectivity of H^(k-1)(f) implies e-h(a)=d_E c for some c. Thus (l,e)=D(a,-c) in C(h), proving injectivity.</p>

<p id="FC-1-p2">For surjectivity, take a cycle (l,z) of degree k in C(fh). Its equations are d_L l=0 and d_F z=f h(l). Injectivity of H^k(f) shows h(l)=d_E e for some e of degree k-1. Then (l,e) is a cycle of C(h). The difference z-f(e) is a cycle in F^(k-1). Surjectivity of H^(k-1)(f) supplies a closed c in E^(k-1) and b in F^(k-2) with z-f(e)-f(c)=d_F b. Hence (l,z) and the image of (l,e+c) differ by D(0,-b), so they define the same cohomology class.</p>

<p id="FC-1-p3">Now let L be zero below q, and suppose C(h) is acyclic in degrees greater than q. Choose finitely many cycles w_j=(a_j,b_j) in C(h)^q=L^q direct_sum E^(q-1) whose classes generate H^q(C(h)). Set L^(q-1)=A^r, d_L^(q-1)(e_j)=a_j and h^(q-1)(e_j)=b_j. The cycle equations say d_L^q a_j=0 and h^q(a_j)=d_E^(q-1)b_j. Therefore the enlarged L is a complex and the enlarged h is a chain map. Maps from finite free modules are continuous because they are finite sums of multiplication by the specified vectors.</p>

<p id="FC-1-p4">In the new comparison complex the only new summand is L^(q-1) in degree q-1. Its differential to degree q sends (v,e) to (d_L^(q-1)v,h^(q-1)v-d_E e). Thus the new degree-q boundary space is the old boundary space plus the A-span of w_j. Those classes generate all degree-q cohomology, so that group becomes zero. Degree-q cycles and all groups in larger degrees are unchanged. This proves the inductive attachment with the actual differential, not an unspecified identification up to sign.</p>

∎

## FC-2. Construction over one common final radius {#FC-2}

<p class="statement"><strong>Statement.</strong> Under the hypotheses on E,F,f in <a href="general-analytic-fc.md#FC-0">FC-0</a>, without its upper cohomological vanishing hypothesis, for every 0&lt;t&lt;1 there is a bounded-above complex L of finite free A_t-modules and a quasi-isomorphism h:L-&gt;E_t. No lower bound is asserted here.</p>

**Proof.**

<p id="FC-2-p1">Let N bound the degrees of E and F above. Set r_(N+1)=1 and r_q=t+(1-t)2^(q-N-1) for all integers q&lt;=N. Then t&lt;r_q&lt;r_(q+1)&lt;=1 and the decreasing radii tend to t as q tends to minus infinity. Each individual r_q is strictly greater than the final t. Start at q=N+1 with the zero partial complex L and its zero map into E over A. Its cone is E[-1] and vanishes above N+1. This gives the induction invariant with no unproved initial finite-generation assertion.</p>

<p id="FC-2-p2">Assume the finite partial complex in degrees &gt;=q has been constructed over A_(r_q), together with h into E_(r_q), and its cone M is acyclic above q. Let Ncone=C(f_(r_q) h). <a href="general-analytic-fc.md#FC-1">FC-1</a> gives a quasi-isomorphism M-&gt;Ncone. Both complexes are bounded above and their terms are fully transverse nuclear modules: each term is a direct sum of a finite free module and a term of E or F. The comparison in degree k is Id_(L^k) direct_sum f_(r_q)^(k-1). Identity on a finite free module is nuclear over the base algebra using its coordinate functionals and finitely many basis vectors. <a href="general-analytic-rp.md#RP-4">RP-4</a> preserves subnuclearity of f under radius restriction; <a href="general-analytic-bt.md#BT-6">BT-6</a> handles the two summands. Therefore this cone comparison satisfies <a href="general-analytic-fc.md#FC-0">FC-0</a>.</p>

<p id="FC-2-p3">Apply <a href="general-analytic-fc.md#FC-0">FC-0</a> from radius r_q to r_(q-1). It supplies finitely many generators for H^q(M_(r_(q-1))). Choose cycle representatives and use <a href="general-analytic-fc.md#FC-1">FC-1</a> to attach L^(q-1) and its maps. <a href="general-analytic-bt.md#BT-4">BT-4</a> preserves the previous acyclicity above q during this base change; the attachment kills degree q as well. The induction invariant therefore holds with q replaced by q-1. All previously chosen terms and maps are retained by restriction, not replaced by incompatible new choices.</p>

<p id="FC-2-p4">For each fixed degree k, restrict the finite free module L^k and its maps from their construction radius to A_t. This defines one complex over A_t with each rank finite. Its differentials square to zero and h is a chain map because each identity already held at a finite stage. There is no inverse limit of complexes or infinite intersection of arbitrary neighbourhoods in this definition; every term is specified at one radius containing the fixed final domain.</p>

<p id="FC-2-p5">To prove h is a quasi-isomorphism in degree k, choose an induction stage q&lt;=k-1. Its cone is acyclic in degree k and above q. <a href="general-analytic-bt.md#BT-4">BT-4</a> preserves this upper acyclicity on restriction to A_t. The final cone and that restricted partial cone have identical terms and differentials in degrees k-1,k,k+1, since later attachments occur below those degrees. Their degree-k cohomology is therefore identical and zero. As this applies to every integer k, C(h) is acyclic. The exact cone criterion <a href="general-analytic-bt.md#BT-5">BT-5</a> proves h is a quasi-isomorphism. The construction may continue indefinitely to the left; boundedness below will be obtained separately on the curve.</p>

∎

## FC-3. Finite acyclic-cover comparison with explicit signs {#FC-3}

<p class="statement"><strong>Statement.</strong> For a finite open cover U_1,...,U_m and a sheaf G whose positive cohomology vanishes on every nonempty finite intersection, the alternating Cech complex computes H^*(union U_i,G). Its comparison is natural under restrictions and refinements preserving the index order. The same construction gives a comparison of complexes of sheaves after direct image.</p>

**Proof.**

<p id="FC-3-p1">The alternating differential is (delta c)_(i_0,...,i_(p+1))=sum_(a=0)^(p+1)(-1)^a c_(i_0,...,omit i_a,...,i_(p+1)) restricted to the intersection. Each double omission occurs twice with opposite signs, so delta squared is zero. Degree p uses only increasing index tuples and is zero for p&gt;=m. Empty intersections contribute the zero group.</p>

<p id="FC-3-p2">First consider a flabby sheaf J. Its augmented alternating complex is exact for every finite cover. Prove this by induction on m. Degree-zero exactness is the sheaf gluing axiom. For a positive-degree cocycle, write a for components not involving the last index, and b for components involving it. If the degree is p, the second part has degree p-1 on the cover (U_i intersection U_m)_(i&lt;m), and the differential on the two parts is (delta a,delta b+(-1)^(p+1)res(a)). Induction makes a=delta u; subtract the coboundary of the cochain u with zero last-index components. The remaining second part b&#x27; is a cocycle. For p&gt;=2 it is a boundary by induction on the intersection cover. For p=1 it glues to a section on (union_(i&lt;m) U_i) intersection U_m. Flabbiness extends this section to U_m; its degree-zero cochain supported on U_m has precisely b&#x27; as its coboundary. Thus every positive cocycle is a boundary.</p>

<p id="FC-3-p3">Choose an injective resolution J^bullet of G as a sheaf of modules. Its restrictions to open sets are injective, since extension by zero for an open immersion is an exact left adjoint to restriction. Injective sheaves of modules are flabby: the inclusion of the extension by zero of the structure sheaf of an open subset into the structure sheaf of the whole space, followed by injectivity of J, shows that every section on the open subset extends. These facts also apply after restriction. Thus Gamma(U_I,J^bullet) computes H^*(U_I,G), and each augmented horizontal Cech row for J^q is exact by the previous paragraph.</p>

<p id="FC-3-p4">We also record why flabby resolutions, used below after closed pushforward, are acyclic resolutions. In a short exact sequence 0-&gt;J-&gt;M-&gt;N-&gt;0 with J flabby, every section s of N on an open W lifts to M(W). Choose local lifts on a covering and well-order its members. Given a lift on the union of earlier members, its difference from the next local lift is a J-section on the overlap. Extend that section to the new member by flabbiness and correct the new lift before gluing. At limit stages the previously compatible sections glue. This constructs a lift on all W. If M is also flabby, N is flabby: lift a section on a smaller open to M there, extend it using M, and take its image. Embed a flabby J in an injective sheaf and repeat on the quotient; the injectives and all successive quotients are flabby by these facts. The resulting injective resolution remains exact after sections on every open. Thus positive cohomology of a flabby sheaf vanishes. More generally an acyclic resolution computes derived sections: in each fixed positive degree, its successive kernel short exact sequences and the long exact derived-functor sequence dimension-shift finitely many times to identify the resolution cohomology with that of its initial sheaf. The same reasoning on inverse images of opens proves the direct-image version.</p>

<p id="FC-3-p5">Form C^(p,q)=product_(|I|=p+1) Gamma(U_I,J^q), with total differential delta+(-1)^p d_J. Restriction commutes with d_J, so the two mixed terms cancel and this differential squares to zero. The map Gamma(union U_i,J^bullet)-&gt;Tot(C) lands in column p=0. It is a quasi-isomorphism: in a total cocycle eliminate the highest nonzero positive-p component using horizontal exactness, subtracting a total coboundary at p-1. The new vertical contribution has smaller p. Repetition leaves p=0, where horizontal closedness identifies a global section; the total cycle equation then identifies a global cocycle. The identical elimination on a primitive proves injectivity on cohomology. There are finitely many columns, so the process terminates.</p>

<p id="FC-3-p6">On the other hand, positive cohomology of each intersection vanishes by hypothesis. The map Cech(U,G)-&gt;Tot(C) is a quasi-isomorphism: starting with the lowest-p component of a total cocycle that has q&gt;0, its vertical differential is zero, so vertical exactness supplies a primitive. Subtract its total differential, with the sign (-1)^p, to remove that component. The added horizontal contribution has larger p and smaller q. Repeating ends in q=0, where the vertical kernel is Gamma(U_I,G), giving a Cech cocycle. For injectivity apply the same elimination to a primitive whose differential is a q=0 Cech cochain; its positive-q components can again be removed, leaving a primitive in the Cech complex. Each fixed total degree has only finitely many bidegrees, so no convergence assertion about an infinite sum is used.</p>

<p id="FC-3-p7">Both arrows in this zigzag come from augmentations and restrictions, not from the choices made during the proof of exactness. They commute with restriction of opens and with index-preserving refinement. They therefore identify a cover-refinement map with the identity on sheaf cohomology of the same space. Applied on inverse images of base opens, the zigzag consists of morphisms of sheaf complexes on the base as well. This supplies the finite comparison needed here without leaving the Leray step as an unexamined external tag.</p>

∎

## FC-4. Properness supplies two compatible finite graph covers {#FC-4}

<p class="statement"><strong>Statement.</strong> Let f:X-&gt;B be a proper holomorphic map to a Riemann surface and G a coherent sheaf on the full analytic space X. Near any b in B there are finite alternating Cech complexes E,F of fully transverse nuclear O(D)-modules, bounded in nonnegative degrees, and a degreewise O(D)-subnuclear quasi-isomorphism E-&gt;F. Their terms restrict by balanced tensor to the actual section complexes over every Stein subopen of D.</p>

**Proof.**

<p id="FC-4-p1">Choose coordinate discs D compactly contained in D_0, with closure(D_0) contained in a further coordinate disc D_1 about b. Restrict X to f^(-1)(D_1), preserving properness over D_1. The set K=f^(-1)(closure(D_0)) is compact. Around each point choose an analytic chart U_i^0 closed in a Stein open Omega_i^0 and smaller Stein polydiscs Omega_i&#x27; compactly contained in Omega_i compactly contained in Omega_i^0. A finite selection can be made so that the U_i&#x27;=U_i^0 intersection Omega_i&#x27; cover K. Put U_i=U_i^0 intersection Omega_i. Both indexed families then cover f^(-1)(D). This uses compactness of K, not compactness of X.</p>

<p id="FC-4-p2">For an increasing tuple I, the diagonal chart map embeds U_I^0=intersection_(i in I) U_i^0 as a closed full analytic subspace of Omega_I^0=product_(i in I) Omega_i^0. This is precisely the full closed-intersection argument of the pinned finiteness provider, Lemma 1.1: a convergent tuple of images has a common limit because X is Hausdorff; locally the map is the graph of holomorphic coordinate representatives, with its original ideal and graph equations. Appending f gives a closed full graph embedding U_I^0-&gt;Omega_I^0 x D_1. Closedness follows also by continuity of f; locally its graph adds the equation for the base coordinate to the same full ideal. Let G_I be the coherent pushforward of G along that embedding.</p>

<p id="FC-4-p3">Write Omega_I=product Omega_i and Omega_I&#x27;=product Omega_i&#x27;. Restricting the graph to Omega_I x D gives U_I intersection f^(-1)(D), and restricting to Omega_I&#x27; x D gives the corresponding primed intersection. In particular their G sections are respectively Gamma(Omega_I x D,G_I) and Gamma(Omega_I&#x27; x D,G_I). Product Stein manifolds and closed coherent pushforward, followed by Cartan B, show that all these intersections are acyclic for G. The same holds after replacing D by any Stein open V contained in D. Their local ideals and coefficient modules retain all nilpotents.</p>

<p id="FC-4-p4">Use these sections as the factors of E^p=Cech^p(U intersection f^(-1)(D),G) and F^p for the primed cover. There are finitely many factors in each degree and no terms outside 0,...,m-1. <a href="general-analytic-ns.md#NS-4">NS-4</a> makes their section spaces nuclear; <a href="general-analytic-rp.md#RP-2">RP-2</a> makes them fully O(D)-transverse. More generally <a href="general-analytic-bt.md#BT-3">BT-3</a> applied to G_I on the ambient product identifies O(V) hat_tensor_(O(D)) each factor with Gamma(Omega_I x V,G_I), with positive Tor zero, for any Stein subopen V of D. Finite products preserve these statements. The identifications commute with all restriction maps in the Cech differential because they are induced by multiplication of holomorphic functions and section restriction.</p>

<p id="FC-4-p5">Each Omega_I&#x27; is relatively compact in Omega_I and both lie relatively compactly in Omega_I^0. <a href="general-analytic-bt.md#BT-6">BT-6</a> therefore makes the restriction of the I-th factor O(D)-subnuclear. The finite product of these restrictions is subnuclear by finite sums and composition. These maps form a chain map E-&gt;F. By the acyclic-cover comparison <a href="general-analytic-fc.md#FC-3">FC-3</a> both complexes compute H^*(f^(-1)(D),G), and the restriction chain map induces the identity under that identification. It is consequently a quasi-isomorphism. This verifies the needed hypotheses on every intersection, not only on the individual chart sections.</p>

∎

## FC-5. The analytic relative complex and coherent direct images {#FC-5}

<p class="statement"><strong>Statement.</strong> For the proper map and coherent sheaf of <a href="general-analytic-fc.md#FC-4">FC-4</a>, after shrinking about any base point there is a bounded-above finite-free-term holomorphic sheaf complex L representing Rf_*G. Its comparison with the finite Cech complex is a quasi-isomorphism on every Stein subopen of that neighbourhood. In particular all R^q f_*G are coherent there. This statement does not require flatness.</p>

**Proof.**

<p id="FC-5-p1">Apply <a href="general-analytic-fc.md#FC-2">FC-2</a> to the O(D)-complexes and restriction map constructed in <a href="general-analytic-fc.md#FC-4">FC-4</a>. For a fixed t&lt;1 it produces finite free O(D_t)-modules L^k, zero for k&gt;m-1, and a chain map h:L-&gt;E_t that is a quasi-isomorphism. Each differential is a finite matrix of functions holomorphic on D_t, so it defines a differential between finite free sheaves on D_t. Matrix multiplication and h&#x27;s equations show these are genuine complexes and sheaf morphisms. A map h^k from a finite free module is specified by finitely many sections of the k-th Cech term; their restrictions define h over every smaller open.</p>

<p id="FC-5-p2">For every Stein V contained in D_t, finite free L^k are transverse to O(V) by <a href="general-analytic-bt.md#BT-0">BT-0</a>-<a href="general-analytic-bt.md#BT-2">BT-2</a>. <a href="general-analytic-fc.md#FC-4">FC-4</a> and <a href="general-analytic-bt.md#BT-3">BT-3</a> make the E_t terms transverse as well and identify their balanced tensors with the actual Cech section terms over f^(-1)(V). Thus <a href="general-analytic-bt.md#BT-5">BT-5</a> applied to h gives a quasi-isomorphism L(V)-&gt;Cech(U intersection f^(-1)(V),G). The maps commute with restriction of V because both the free matrices and all comparison vectors are restrictions of their fixed sections on D_t. No point-fibre assertion is inferred from this open-restriction statement.</p>

<p id="FC-5-p3">For an explicit derived comparison, choose an injective resolution J of G on f^(-1)(D_t). The sheaf on D_t of k-th Cech sections assigns V the product of Gamma(U_I intersection f^(-1)(V),G). <a href="general-analytic-fc.md#FC-3">FC-3</a> supplies sheaf-complex maps from that Cech complex to Tot(Cech(U,J)) and from f_*J to the same total complex. On the Stein basis each is a quasi-isomorphism by the argument of <a href="general-analytic-fc.md#FC-3">FC-3</a> and the acyclicity of the intersections. Filtered colimits of modules are exact: a finite equation between germs holds on some common smaller neighbourhood, which proves both preservation of kernels in finite exact diagrams and lifting for cokernels. Passing to stalks therefore shows these maps, and h, are quasi-isomorphisms of sheaf complexes. This actual zigzag identifies L with Rf_*G, rather than merely giving abstract isomorphisms between its cohomology dimensions.</p>

<p id="FC-5-p4">In every fixed degree, H^q(L)=ker(d^q)/image(d^(q-1)) is coherent by Oka coherence and the kernel, image and cokernel properties in the pinned coherent-sheaf provider. Only three finite free terms enter this assertion, so infinitely many possible negative terms cause no problem. The derived comparison gives H^q(L)=R^q f_*G. These sheaves vanish for negative q, since f_*J has no negative terms. This proves direct-image coherence on the base curve with full analytic source structure, conditional only on the explicitly bound analytic prerequisites already supplied.</p>

∎

## FC-6. Bounded truncation on the curve without making cohomology locally free {#FC-6}

<p class="statement"><strong>Statement.</strong> The relative representative L of <a href="general-analytic-fc.md#FC-5">FC-5</a> can be replaced, near any chosen b, by a bounded complex P of finite free holomorphic sheaves. This supplies the boundedness required in the retained S6 obligation; it does not assert local freeness of any R^q f_*G.</p>

**Proof.**

<p id="FC-6-p1">Let I=image(d_L^(-1):L^(-1)-&gt;L^0). It is coherent and is a subsheaf of finite free L^0. The local ring A=O_(B,b) is a discrete valuation ring: in a coordinate z vanishing at b, every nonzero convergent power series is z^n times a unit, and the unit has a convergent inverse on a smaller disc. For completeness, the image of any finite matrix over this ring is finite free. If the matrix is nonzero, move an entry of least valuation to its upper left corner. It divides every other entry. Invertible row and column operations clear its column and row. Repeat on the smaller remaining matrix. This gives a diagonal matrix with nonzero diagonal entries and zero remainder, whose nonzero columns are a free basis for its image. The invertible operations transport that basis back. Apply this to d_L^(-1) on stalks to see I_b is finite free.</p>

<p id="FC-6-p2">Represent a basis of I_b by finitely many local sections of I, obtaining a morphism O^r-&gt;I that is an isomorphism at b. Its kernel and cokernel are coherent. A finite-type sheaf with zero stalk at b vanishes in a neighbourhood: take finitely many local generators and shrink until each of their zero germs is zero as a section. Apply this to kernel and cokernel, shrinking once more. Thus I is a finite free sheaf there. This is a local property of the image submodule over a smooth curve, not a claim that its quotient or the cohomology sheaves are free.</p>

<p id="FC-6-p3">Define P^q=0 for q&lt;-1, P^(-1)=I, and P^q=L^q for q&gt;=0, with its first differential the inclusion I-&gt;L^0 and all later differentials unchanged. It is a complex because d_L^0 kills I. Define L-&gt;P by d_L^(-1) with codomain I in degree -1, identity in nonnegative degrees, and zero below -1. The chain equations follow from d_L squared=0. The entering image in degree zero is unchanged, so the map induces isomorphisms in all nonnegative cohomological degrees. P has no negative cohomology because its first differential is injective; L has none by <a href="general-analytic-fc.md#FC-5">FC-5</a>. Hence L-&gt;P is a quasi-isomorphism. The complex P is finite free and lies in degrees [-1,m-1]. Together with the earlier zigzag it represents Rf_*G.</p>

∎

## FC-7. Canonical full-fibre comparison and the retained surface theorem {#FC-7}

<p class="statement"><strong>Statement.</strong> Let f:X-&gt;B be proper and flat with B a Riemann surface, all full fibres pure of dimension two, and E a holomorphic vector bundle. Then R^q f_*E=0 for q&gt;2, and at every b the canonical map (R^2 f_*E)_b tensor_(O_(B,b)) k(b)-&gt;H^2(X_b,E|_(X_b)) is an isomorphism. The bounded representative P of <a href="general-analytic-fc.md#FC-6">FC-6</a> has the canonical derived-fibre identification P_b tensor^L k(b) equivalent to RΓ(X_b,E|_(X_b)). No smoothness or compactness of X, reducedness of X_b, constancy of h^2, or local freeness of R^2 f_*E is imposed.</p>

**Proof.**

<p id="FC-7-p1">We identify the canonical comparison using the full fibre, including its nonreduced structure. Fix b, take a base coordinate z with zero set {b}, put V=f^(-1)(U), and let i:X_b-&gt;V and j:{b}-&gt;U be the closed inclusions. Flatness of f and local freeness of E give an exact sequence 0-&gt;E --f^*z--&gt; E -&gt; i_*E_b-&gt;0. The last term is E/(f^*z)E on the full fibre O_V/(f^*z), not the module on its reduction.</p>

<p id="FC-7-p2">Choose an injective resolution J of E on V and set K=f_*J. Multiplication by f^*z acts on J. The usual cone has Cone(z:J-&gt;J)^q=J^q direct_sum J^(q+1), with differential (a,c)|-&gt;(d_J a+z c,-d_J c). Its cohomology is concentrated in degree zero and equals i_*E_b, by the exact sequence above. Its terms are finite sums of flabby sheaves, hence acyclic for f_*: over every base open their sections are those of flabby sheaves on its inverse image. It therefore computes Rf_*i_*E_b. Applying f_* commutes with these finite sums and the scalar action, giving Cone(z:K-&gt;K) on the nose.</p>

<p id="FC-7-p3">Let T=[O_U --z--&gt; O_U] in degrees -1,0, resolving j_*k(b). A bounded complex of flat modules preserves acyclic complexes under tensor: one flat module preserves kernels and images of each differential in an exact complex, and a finite complex follows by its successive finite-term filtration. Thus T is K-flat and K tensor T computes K tensor^L j_*k(b). In total degree q write its components as (a,c) in K^q direct_sum K^(q+1); the differential is (d_K a+(-1)^(q+1)z c,d_K c). The map (a,c)|-&gt;(a,(-1)^(q+1)c) identifies it with Cone(z:K-&gt;K) with the differential in the previous paragraph. This checks the derived tensor identification including its sign.</p>

<p id="FC-7-p4">A flabby resolution on X_b stays flabby and exact after the closed pushforward i_*. Consequently Rf_*i_*E_b is j_*RΓ(X_b,E_b). Taking the stalk at b gives (Rf_*E)_b tensor_A^L k(b) equivalent to RΓ(X_b,E_b), where A=O_(B,b). Composing with the actual derived identification of P in <a href="general-analytic-fc.md#FC-6">FC-6</a> gives the asserted comparison for P. The map is induced by the restriction E-&gt;i_*E_b. In particular its map from ordinary cohomology modulo z is the canonical base-change map, not an isomorphism selected from a dimension count. If the coordinate changes to uz for a unit u, the chain map T_(uz)-&gt;T_z is multiplication by u in degree -1 and identity in degree zero; it commutes with the differentials and the augmentations. Thus the derived morphism is independent of that choice and of the chosen resolutions.</p>

<p id="FC-7-p5">Set M^q=(R^q f_*E)_b. The cone exact sequence now yields 0-&gt;M^q/zM^q-&gt;H^q(X_b,E_b)-&gt;M^(q+1)[z]-&gt;0, where M[z] is the kernel of multiplication by z. The first arrow is the canonical map just identified. This exact sequence retains the torsion term; it is not set to zero in all degrees. Coherence from <a href="general-analytic-fc.md#FC-5">FC-5</a> makes every M^q a finite A-module. Properness makes X_b compact, and its full dimension is two. The pinned QG compact coherent dimension proof gives H^q(X_b,E_b)=0 for q&gt;2, with the original nilpotent structure retained.</p>

<p id="FC-7-p6">For q&gt;2, the exact sequence implies M^q=zM^q. To see directly why this finite module is zero, take generators m_1,...,m_r and write m_i=z sum_j a_ij m_j. The matrix I-z(a_ij) annihilates the generator column. Multiplication by its adjugate shows det(I-z(a_ij)) annihilates every generator. Its residue is 1, so it is a unit of the local ring; therefore M^q=0. This works at every b and proves R^q f_*E=0 for q&gt;2. In degree two the same exact sequence has M^3[z]=0 and supplies the canonical isomorphism claimed. None of these steps uses local freeness of M^2 or constancy of the fibre cohomology dimension.</p>

∎

## Sources {#FC-sources}

Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), author edition of 21 June 2012. IX.5.44 and proof of IX.5.1, pp. 446-448. The independently written arguments above follow the cited mathematics, with the explicit domains, signs and comparisons given here.
