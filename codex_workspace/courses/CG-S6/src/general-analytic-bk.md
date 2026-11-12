# The complete Hermitian curvature identity {#general-analytic-bk}

Written by GPT-6 Astra (OpenAI), at Ultra, October 2026. Independent exposition: CC0-1.0.

Read this argument with the [general surface theorem](general-proper-flat-surface-base-change.md#general-surface-theorem) and its [prerequisite guide](general-proper-flat-surface-base-change.md#general-prerequisites). Result identifiers link to the exact arguments in this companion family.

The supporting arguments retain linear mathematical notation: `->` denotes a map, `^` an exponent or cohomological degree, `_` a subscript, and `direct_sum` a direct sum. Parentheses specify grouping. Algebraic quotients and completed topological tensor products are distinguished explicitly; a quotient is not silently replaced by its completion.

## Conventions {#BK-conventions}

<p>D=D&#x27;+D&#x27;&#x27; is the Chern connection, extended to E-valued exterior forms by the graded Leibniz rule. Set C=D&#x27;, B=D&#x27;&#x27;, a=(D&#x27;)*, b=(D&#x27;&#x27;)*, where star means formal L2 adjoint. The inner product is linear in its first argument. Put L=omega wedge and Lambda=L* pointwise.</p>

<p>P=(partial omega) wedge has bidegree (2,1) and total degree 3; Q=(dbar omega) wedge has bidegree (1,2). Define tau=[Lambda,P] and sigma=[Lambda,Q]. On scalar forms sigma is the conjugate of tau. On bundle-valued forms both act as these same scalar endomorphisms tensor Id_E. In particular sigma* and tau* are distinct operators and may not be interchanged.</p>

<p>The bracket is graded by total degree parity: [U,V]=UV-(-1)^(deg U deg V)VU. Thus all brackets between C,B,a,b,tau,sigma or their adjoints are anticommutators, while brackets involving L or Lambda are ordinary commutators. A form appearing inside a bracket denotes exterior multiplication by that form.</p>

<p>Theta=D^2=[C,B] is curvature exterior multiplication. Delta&#x27;&#x27;=[B,b], Delta&#x27;=[C,a], and Delta&#x27;_tau=[C+tau,a+tau*]. Define T=[Lambda,[Lambda,(i/2)partial dbar omega wedge]]-[P,P*].</p>

## BK-0. Exterior algebra and graded identities with their signs {#BK-0}

<p class="statement"><strong>Statement.</strong> On total degree r forms, H=[L,Lambda]=(r-n)Id. The graded Jacobi identity and adjoint reversal hold with the conventions above. For a constant unitary metric, [dbar*_0,L_0]=i partial and [Lambda_0,dbar*_0]=0.</p>

**Proof.**

<p id="BK-0-p1">In a unitary coframe write e_j=dz_j wedge and f_j=dbar z_j wedge, with adjoints e_j* and f_j*. Exterior anticommutation gives e_j e_k+e_k e_j=0, e_j* e_k+e_k e_j*=delta_jk Id, and the analogous formulas for all holomorphic and antiholomorphic covectors. Here L=i sum e_j f_j and Lambda=-i sum f_j* e_j*. For each index, the pair commutator has value 1 when both covectors occur, -1 when neither occurs, and 0 when exactly one occurs. Distinct even pairs commute. Adding over j gives H=(r-n)Id. Therefore [H,U]=sU for an operator increasing total degree by s; the identity holds for differential operators as well since H is constant on each degree.</p>

<p id="BK-0-p2">For homogeneous U,V,W of parities u,v,w, expand both sides of [U,[V,W]]=[[U,V],W]+(-1)^(uv)[V,[U,W]]. In the right side, the VUW terms cancel, as do the WUV terms. The terms left are UVW-(-1)^(vw)UWV-(-1)^(u(v+w))VWU+(-1)^(u(v+w)+vw)WVU, exactly the left side. This proves Jacobi without an external locator. Formal integration by parts and complex conjugation give (UV)*=V*U*, (iU)*=-iU*, and [U,V]*=[V*,U*].</p>

<p id="BK-0-p3">For constant omega_0=i sum dz_j wedge dbar z_j, integration by parts in real coordinates gives dbar*_0=-sum f_j* partial_(z_j), while partial=sum e_j partial_(z_j). Anticommutation gives [f_j*,L_0]=-i e_j. Since L_0 has constant coefficients, [dbar*_0,L_0]=i partial. The contraction f_j* commutes with every even contraction pair f_k*e_k*, so [Lambda_0,dbar*_0]=0. These computations are identities on arbitrary smooth forms; only the derivation of the formal adjoint uses compact test functions.</p>

∎

## BK-1. The scalar Hermitian commutation formula without a Kahler normalization {#BK-1}

<p class="statement"><strong>Statement.</strong> On scalar forms, [dbar*,L]=i(partial+tau), [partial*,L]=-i(dbar+sigma), [Lambda,dbar]=-i(partial*+tau*) and [Lambda,partial]=i(dbar*+sigma*).</p>

**Proof.**

<p id="BK-1-p1">Fix a point x_0. A complex-linear coordinate change makes omega(x_0)=omega_0=i sum dz_j wedge dbar z_j, but does not remove the first derivatives of omega. Write gamma=omega-omega_0, so gamma(x_0)=0. Let M_(p,q)(x) be the matrix comparing the actual pointwise inner product times volume with the constant one on (p,q)-forms. Then M=Id-[gamma wedge,Lambda_0]+O(|x-x_0|^2). To compute its first derivative, diagonalize gamma at one point with eigenvalues gamma_j relative to omega_0. The coefficient of a basis form dz_I wedge dbar z_J in this density is product_all(1+gamma_j) divided by product_I(1+gamma_j) product_J(1+gamma_j). Its linear term is sum_all gamma_j-sum_I gamma_j-sum_J gamma_j, the negative of the commutator eigenvalue established in <a href="general-analytic-wl.md#WL-3">WL-3</a>. This calculation determines the first derivative in every Hermitian direction. The actual matrix M is a smooth function of the entries of omega and their inverses, so its Taylor remainder is genuinely quadratic in smooth coordinates. No smooth choice of diagonalizing eigenvectors is assumed.</p>

<p id="BK-1-p2">Put delta_0=dbar*_0. The actual formal adjoint is M_(p,q-1)^(-1) delta_0 M_(p,q), by integration by parts with the two density matrices. At x_0 this becomes delta=delta_0-[delta_0,[gamma,Lambda_0]], since gamma(x_0)=0 and the quadratic Taylor remainder has zero first derivative there. By Jacobi and [delta_0,Lambda_0]=0, this is delta_0+[Lambda_0,C_0], where C_0=[delta_0,gamma]. The correction is allowed to be a first-order operator away from x_0; its principal coefficients vanish at x_0. This distinction matters when forming the next commutator.</p>

<p id="BK-1-p3">At x_0, expanding L=L_0+gamma gives [L,delta]=[L_0,delta_0]+[L_0,[Lambda_0,C_0]]+[gamma,delta_0]. The omitted correction with two factors gamma vanishes at x_0: its first-order part contains two zero factors, and differentiating at most one factor still leaves the other zero. Since [gamma,L_0]=0, Jacobi gives [C_0,L_0]=-[gamma,[delta_0,L_0]]=i(partial gamma) wedge. Thus [L_0,C_0]=-i(partial gamma) wedge. Also C_0 raises total degree by one, so [H_0,C_0]=C_0. Consequently [L_0,[Lambda_0,C_0]]=C_0-i[Lambda_0,partial gamma wedge]. The term C_0 cancels [gamma,delta_0]=-C_0. <a href="general-analytic-bk.md#BK-0">BK-0</a> now yields [L,delta]=-i partial-i[Lambda_0,partial gamma wedge]=-i(partial+tau) at x_0. Since x_0 was arbitrary, the first asserted identity holds everywhere.</p>

<p id="BK-1-p4">Complex conjugation commutes with L and with the real Riemannian metric on scalar forms, interchanges partial and dbar, and sends i to -i and tau to sigma. It yields the second identity. Taking formal adjoints of the first and second identities, using <a href="general-analytic-bk.md#BK-0">BK-0</a>, gives the third and fourth respectively. This establishes all four formulas with their conjugate-torsion terms. No coordinate system with vanishing metric derivatives, and hence no hidden Kahler assumption, has been used.</p>

∎

## BK-2. Chern connection and an explicit normal holomorphic bundle frame {#BK-2}

<p class="statement"><strong>Statement.</strong> The scalar identities extend to E-valued forms as [b,L]=i(C+tau), [a,L]=-i(B+sigma), [Lambda,B]=-i(a+tau*) and [Lambda,C]=i(b+sigma*). Moreover C^2=B^2=0 and [C,B]=Theta.</p>

**Proof.**

<p id="BK-2-p1">In a holomorphic frame let h be the positive Hermitian matrix and set A=h^(-1)partial h. Define C=partial+A wedge and B=dbar. Under a holomorphic frame change G, h becomes G^dagger h G and A becomes G^(-1)AG+G^(-1)partial G; dagger here means coefficientwise conjugate transpose, conjugating the differential for a matrix-valued form, not the formal operator adjoint. In particular partial G^dagger=0. These local formulas therefore define a connection on the bundle. Its metric compatibility follows from hA=partial h and A^dagger h=dbar h. The same identities show uniqueness among metric connections whose (0,1) part is the given holomorphic structure. Differentiating h^(-1) gives partial A=-A wedge A. Hence C^2=0, while B^2=0 in holomorphic frames. Their graded mixed commutator is dbar A wedge, which is the (1,1) Chern curvature Theta.</p>

<p id="BK-2-p2">At a chosen point x_0, first use a constant frame change so h(x_0)=Id; positive square roots exist by finite Hermitian diagonalization. In holomorphic coordinates z centered at x_0, write H_j=partial h/partial z_j evaluated at x_0 and take G(z)=Id-sum H_j z_j. It is holomorphic and invertible after shrinking. The transformed metric h_1=G* h G satisfies h_1(x_0)=Id and partial h_1/partial z_j(x_0)=H_j-H_j=0. Hermitian symmetry also makes all antiholomorphic first derivatives zero. Therefore h_1=Id+O(|z|^2) and its connection matrix is O(|z|). This proves the needed frame statement rather than referring to the source&#x27;s placeholder locator.</p>

<p id="BK-2-p3">In this frame C and B at x_0 agree with scalar partial and dbar on each coefficient. The bundle contribution to the formal adjoints is obtained from the same density-matrix integration by parts as in <a href="general-analytic-bk.md#BK-1">BK-1</a>; h_1-Id is quadratic and its first derivatives vanish, so the adjoints at x_0 also agree coefficientwise with the scalar ones. In a commutator with the zero-order L or Lambda, differences in these bundle operators vanish at x_0: their connection terms are zero-order O(|z|), and any principal metric correction has zero value and zero first derivative there. The base metric omega is unchanged and retains exactly the torsion terms proved in <a href="general-analytic-bk.md#BK-1">BK-1</a>. Applying <a href="general-analytic-bk.md#BK-1">BK-1</a> coefficientwise therefore yields all four bundle identities at x_0. The point and frame were arbitrary, so the equalities are global operator identities.</p>

∎

## BK-3. The preliminary bundle Laplacian identity {#BK-3}

<p class="statement"><strong>Statement.</strong> Delta&#x27;&#x27;=Delta&#x27;+[iTheta,Lambda]+[C,tau*]-[B,sigma*].</p>

**Proof.**

<p id="BK-3-p1"><a href="general-analytic-bk.md#BK-2">BK-2</a> gives b=-i[Lambda,C]-sigma*. Thus Delta&#x27;&#x27;=[B,b]=-i[B,[Lambda,C]]-[B,sigma*]. By Jacobi, [B,[Lambda,C]]=[[B,Lambda],C]+[Lambda,[B,C]]. Since [B,Lambda]=i(a+tau*), and the bracket of two odd operators is symmetric, the first term is i[C,a+tau*]. The second is [Lambda,Theta]. Multiplication by -i converts them to [C,a]+[C,tau*]+[iTheta,Lambda]. This is the asserted formula. Each term has bidegree (0,0); in particular the final term uses sigma*, not tau*.</p>

∎

## BK-4. Combining the first-order torsion terms into a nonnegative square {#BK-4}

<p class="statement"><strong>Statement.</strong> [L,tau]=3P, [Lambda,tau]=-2i sigma*, and -[B,sigma*]=[tau,a+tau*]+T, where T=[Lambda,[Lambda,(i/2)partial dbar omega wedge]]-[P,P*].</p>

**Proof.**

<p id="BK-4-p1">Even exterior multiplication by omega commutes with P, and P raises total degree by three. Jacobi and <a href="general-analytic-bk.md#BK-0">BK-0</a> give [L,tau]=[L,[Lambda,P]]=[[L,Lambda],P]+[Lambda,[L,P]]=[H,P]=3P.</p>

<p id="BK-4-p2">The identity [b,L]=i(C+tau) expresses tau=-i[b,L]-C. Also [B,L]=Q because the connection satisfies the graded Leibniz rule on a scalar even form; taking adjoints yields [Lambda,b]=Q*. Jacobi therefore gives [Lambda,[b,L]]=[Q*,L]+[b,-H]=sigma*-b: the first term is the adjoint of [Lambda,Q]=sigma, and [b,H]=b since b lowers degree by one. Substitute [Lambda,C]=i(b+sigma*) to obtain [Lambda,tau]=-i(sigma*-b)-i(b+sigma*)=-2i sigma*.</p>

<p id="BK-4-p3">Set A_1=[B,Lambda]=i(a+tau*) and R=(dbar partial omega) wedge. The Leibniz rule on the odd scalar form partial omega gives [B,P]=R. Jacobi now yields [B,tau]=[A_1,P]+[Lambda,R] and [B,[Lambda,tau]]=[A_1,tau]+[Lambda,[B,tau]]. Substituting the first into the second and applying Jacobi once more produces [B,[Lambda,tau]]=[Lambda,[Lambda,R]]+2[tau,A_1]+[P,[Lambda,A_1]]. The factor 2 arises because both tau and A_1 are odd, so their bracket is symmetric; it is not discarded.</p>

<p id="BK-4-p4">To evaluate the last bracket, [Lambda,A_1]=i[Lambda,a+tau*]=i[C+tau,L]*. Here [C,L]=P by the connection Leibniz rule, whereas [tau,L]=-3P by the first paragraph. Therefore [Lambda,A_1]=-2iP*. The preceding line becomes [Lambda,[Lambda,R]]+2i[tau,a+tau*]-2i[P,P*]. Since dbar partial omega=-partial dbar omega, its first term is 2i[Lambda,[Lambda,(i/2)partial dbar omega wedge]]. Finally sigma*=(i/2)[Lambda,tau] from the second paragraph, so multiplying by i/2 gives [B,sigma*]=-[tau,a+tau*]-T. This is the required torsion identity with every derivative order and factor retained.</p>

∎

## BK-5. The complete identity, energy inequality and exact receiver {#BK-5}

<p class="statement"><strong>Statement.</strong> Delta&#x27;&#x27;=Delta&#x27;_tau+[iTheta,Lambda]+T. For every compactly supported smooth E-valued (p,k)-form u, ||Bu||^2+||bu||^2&gt;=integral &lt;([iTheta,Lambda]+T)u,u&gt;dV. This discharges the curvature input of <a href="general-analytic-wl.md#WL-4">WL-4</a>, <a href="general-analytic-wl.md#WL-5">WL-5</a> and <a href="general-analytic-wl.md#WL-6">WL-6</a> for all the smooth weights and bundles used there.</p>

**Proof.**

<p id="BK-5-p1">Insert <a href="general-analytic-bk.md#BK-4">BK-4</a> into <a href="general-analytic-bk.md#BK-3">BK-3</a>. The terms Delta&#x27;+[C,tau*]+[tau,a+tau*] are exactly [C+tau,a+tau*] when expanded by bilinearity. This proves the operator identity. T is zero-order: all its factors are pointwise exterior multiplications or contractions; partial dbar omega differentiates the fixed metric coefficients, not u. Its coefficients are smooth and it depends only on omega. It acts on the bundle factor by the identity, so a scalar change of bundle weight leaves it unchanged.</p>

<p id="BK-5-p2">The operator a+tau* is the actual formal adjoint of C+tau. For compactly supported u, integration by parts gives (Delta&#x27;_tau u,u)=||(C+tau)u||^2+||(a+tau*)u||^2&gt;=0 and (Delta&#x27;&#x27;u,u)=||Bu||^2+||bu||^2. Subtract the two in the proved identity to obtain the asserted exact energy equality with those two nonnegative squares, and then discard the squares for the inequality. Formal self-adjointness is sufficient; no spectral theorem or choice of self-adjoint extension is being assumed.</p>

<p id="BK-5-p3">There is also no missing self-adjointness assumption on the pointwise curvature term. Apply the already-proved identity in a chart to the trivial line bundle with constant metric, for which Theta=0. T is the difference of two formally self-adjoint differential operators there. As a zero-order smooth operator it must therefore be pointwise self-adjoint: test its skew-adjoint part against arbitrary compactly supported vector functions and use continuity of its entries. For general E, the identity then shows that [iTheta,Lambda] is formally self-adjoint as well, hence pointwise self-adjoint because it too is zero-order. This justifies the operator inequalities and norms used in <a href="general-analytic-wl.md#WL-3">WL-3</a> without a further unproved fibrewise assertion.</p>

<p id="BK-5-p4">Apply the theorem to the complete metric omega_tilde and the smooth bundle metric h exp(-Phi) of <a href="general-analytic-wl.md#WL-0">WL-0</a>, <a href="general-analytic-wl.md#WL-1">WL-1</a>, <a href="general-analytic-wl.md#WL-2">WL-2</a> and <a href="general-analytic-wl.md#WL-3">WL-3</a>; nothing in <a href="general-analytic-bk.md#BK-0">BK-0</a> through <a href="general-analytic-bk.md#BK-5">BK-5</a> requires Kahlerness or compactness. For the twist F=K_M^(-1) tensor E, it applies to that holomorphic bundle itself, without trivializing K_M globally. The zero-order A_(Phi,k) is precisely [iTheta(F_Phi),Lambda]+T from <a href="general-analytic-wl.md#WL-3">WL-3</a>. Thus the compact-support premise explicitly singled out in <a href="general-analytic-wl.md#WL-4">WL-4</a> is now supplied. <a href="general-analytic-wl.md#WL-1">WL-1</a> extends the resulting A&gt;=Id estimate to the actual joint graph domain; <a href="general-analytic-wl.md#WL-4">WL-4</a> gives a smooth minimum-norm solution; and <a href="general-analytic-wl.md#WL-5">WL-5</a> and <a href="general-analytic-wl.md#WL-6">WL-6</a> give the full manifold vanishing and degree-(q-1) approximation, including their degree endpoints. This supplies the curvature hypothesis in those implications. Coherent-sheaf gluing and the proper-map finite-complex construction require the separate arguments <a href="general-analytic-cl.md#CL-0">CL-0</a> through <a href="general-analytic-qg.md#QG-6">QG-6</a> and <a href="general-analytic-fc.md#FC-0">FC-0</a> through <a href="general-analytic-fc.md#FC-7">FC-7</a>.</p>

∎

## Sources {#BK-sources}

Jean-Pierre Demailly, [*Complex Analytic and Differential Geometry*](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), author edition of 21 June 2012. VI.6.1-6.3, printed 304-305; VI.6.8-6.14, printed 306-309; VII.1.1-1.6 and VII.2.1, printed 329-332. The independently written arguments above follow the cited mathematics, with the explicit domains, signs and comparisons given here.
