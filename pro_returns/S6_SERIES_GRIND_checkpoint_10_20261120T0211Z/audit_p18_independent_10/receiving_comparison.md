# Full receiving comparison: P1.8

## Status and the before-reading gate

The complete independent derivation of P1.8 was frozen at **2026-11-20T02:04:36.790861+00:00**, before reading the target. The frozen proof hash is **a92196729a9b29da5b4e43c95fc830d8a40b2b0bf5b4fa6490f398bf5ee3c5f0**. Its code, exact output, exposure log, and self-audit were frozen at the same time. All five hashes were checked unchanged by the post-freeze receiving script.

The whole target theorem and its balanced six-part proof were then read from `audit_root/P18_fresh_inputs_09/target_P18_receiving_10.tex`, hash **0a397ce2ac20d36abfdf2117ff6b78d914f5fe65cda20ac7b337aba467c882c4**. Its extraction receipt records preparation at 02:05:35.042958 UTC, after the independent freeze. The reference producer was read only after the target. Actual later exposure is recorded separately in `postfreeze_exposure.md`.

**Result:** the mathematical assertions of the supplied P1.8 statement are proved by the complete independent derivation, and each substantive step of the received proof agrees with that derivation. One precise normalization convention remains ambiguous in the received text: step 3 uses “at z=1/2” without supplying the base-coordinate map from z to lambda. This does not obstruct the theorem for a specified splitting, since the proof constructs the family for every canonical-regular splitting. It does matter when the particular splitting is compared with later algebraic normalizations. The exact issue and an explicit repair are recorded in Section 9 below.

## 1. Global Hodge sequence and the corrected rank-three P

Target step 1 uses the exact sequence

\[
0\to H\to E\to H^\vee\to0
\]

on the order-five/order-eight root orbifold, including the logarithmic cusp. Independent Sections 2 and 7 establish precisely that extension. The normalization map of the nodal curve is

\[
(x,z)\mapsto(x,(x-r)z),\qquad
z^2=x^3+2rx^2+3r^2x+4r^3,
\]

and the two limiting Hodge classes are distinguished by the explicit nonzero residue of dx/y and the nonzero elliptic differential (x-r)dx/y. The actual plumbing integration removes only the logarithmic term and leaves holomorphic periods. The symplectic matrix stays nondegenerate in the nilpotent frame. Hence the map

\[
E/H\longrightarrow H^\vee,
\quad[v]\longmapsto(h\mapsto\operatorname{contr}(h\wedge v))
\]

is an isomorphism at the cusp as well as on the smooth locus. This supplies the boundary justification summarized in the target by “residue pairing.”

The target sequence

\[
0\to T^4\to P\to\mathcal O\oplus T^2\to0
\]

is the quotient of the actual wedge injection by the Hodge subline. Its maps are made explicit in independent (6), (8), and (9). The independent proof further separates the contraction kernel:

\[
0\to T^4\to K\to T^2\to0,
\qquad 0\to K\to P\xrightarrow{\alpha}\mathcal O\to0.
\]

The target's contraction is exactly independent (7): it is evaluated on the unique representative in u wedge E. Both proofs use the injective map supplied by P1.5 and independently justify that the polarization line has zero intersection with this wedge subspace. Neither proof applies the contraction to an unspecified quotient representative.

**Receiving conclusion for step 1:** correct, including the cusp extension and the rank-three morphism. The independent proof provides the local residue map and the filtration maps in full.

## 2. Bundle cohomology, splitting, and the global section g

Target step 2 takes floors for T exponents 2, 4, -2, -4. Under the exact root-stack morphism d with local formula t=s² at zero, these are the pullbacks of L, L², L⁻¹, L⁻². Independent Section 3 computes the actual coarse direct images:

\[
\rho_*L^k=\mathcal O\bigl(\lfloor4k/5\rfloor[\infty]
+\lfloor-3k/4\rfloor[0]\bigr).
\]

Each of the four required nonzero exponents gives coarse degree -1. The local invariant-monomial map and finite-group averaging are explicitly supplied. Independent (14) is a two-chart Laurent cocycle subtraction for degrees -1 and 0. Thus it proves both the target's H⁰ and H¹ vanishings.

The target splitting agrees with independent (15):

\[
P=L^2\oplus L\oplus\mathcal O,
\quad \alpha=(0,0,1),
\quad H^1(P^\vee)=0,
\quad H^0(P^\vee)=\mathbb C\alpha.
\]

The same vanishings give H⁰(P)=C g, with alpha(g)=1. The independent proof also shows that the filtration-respecting splittings are unique: the difference spaces H⁰(L), H⁰(L²), and H⁰(K) vanish. Therefore the target's g is a well-defined global section, rather than an unexplained local choice.

**Receiving conclusion for step 2:** correct. The full cohomology calculation, the invariant descent, and the exact splitting maps agree.

## 3. The rank-six extension, actual lifting, and scalar freedom

Target step 3 uses the nilpotent canonical extension at the cusp and finite equivariant flat extensions at the roots. Independent Section 1 records the exact frame relation

\[
p_V\exp(sN_V)=\exp(sN_W)p_V,
\qquad N_Ve=0.
\]

Hence the sequence remains the same constant projection in canonical frames. Finite stabilizer averaging gives equivariant local lifts. Independent Section 4 constructs the pullback extension V_P, takes the differences of local lifts as P-dual-valued cocycles, and subtracts the invariant Laurent cochains. This is an actual holomorphic splitting procedure on the compact canonical extension.

The target's full scalar freedom agrees with independent (20):

\[
\sigma'=\sigma+a\alpha e,\qquad a\in\mathbb C.
\]

The scope here is the compact orbifold bundle with its canonical extension at the cusp. Its restriction supplies the splittings used on the punctured/transversality base. This scope is necessary for the H⁰(P-dual)=C alpha calculation and is fixed in both constructions by their boundary extensions.

For a fixed marked base point b and the global section g, the unique lift with zero central coordinate at b is explicitly

\[
\sigma_b^{\rm point}
=\sigma-(\sigma(g)(b))_e\,\alpha e.
\tag{R1}
\]

This gives the actual morphism implementing the target normalization. The target's identification of the point b by “z=1/2” needs the coordinate clarification discussed in Section 9.

**Receiving conclusion for step 3:** the extension, the holomorphic lift, and its complete scalar freedom are correct. The particular base-point notation is incompletely specified in the isolated proof and in the searched source context.

## 4. Exact comparison of the two real-line conventions and h

The target uses

\[
r_T=i\pi(u\wedge\bar u),\qquad
A_T=\alpha(r_T)=i\beta>0,
\qquad \beta=\operatorname{contr}(u\wedge\bar u).
\]

The independent proof uses

\[
j_I=\frac{\pi(u\wedge\bar u)}{\beta}.
\]

The exact morphism between the conventions is

\[
r_T=A_Tj_I,
\qquad \alpha(j_I)=1.
\tag{R2}
\]

Consequently the target equality

\[
\sigma(r_T)-\overline{\sigma(r_T)}=2iA_T h_Te
\]

is exactly the independent equality

\[
\sigma(j_I)-\overline{\sigma(j_I)}=2ih_Ie,
\]

and h_T=h_I for the same splitting and marking. No scale factor or sign is left undetermined.

Both proofs use the symplectic direct-sum map from span(u,bar u) plus its symplectic orthogonal complement to E. The component in the exterior square of the complement forces the multiple of omega to vanish; the remaining intersection is the line generated by u wedge bar u. The independent proof explicitly checks J Omega=-I, identifying the polarization bivector in that decomposition. Thus the target's quotient-intersection argument is correct.

Comparing the two lifts of j gives exactly 2i(h+c)e. Projection is injective on each lifted plane, so the target's pointwise equivalence agrees with independent (28):

\[
F_c\cap\bar F_c=0\quad\Longleftrightarrow\quad h+c\ne0.
\]

**Receiving conclusion for step 4:** exact agreement, including real structure, scale, polarization sign, and the obstruction scalar.

## 5. Target cusp scalar identity and the complete log-growth argument

The target uses D=C_f C_g⁻¹-I and N_V=(BA)⁻¹-I. These are the same literal matrices as independent (35) and (37). In particular D=d₀e₀ᵗ with d₀=(0,1,1,1)ᵗ, and Jd₀=e₀. Therefore for arbitrary four-vectors a,b,

\[
\operatorname{contr}(a\wedge Db)=a_0b_0.
\]

The target's more specific extension identity is

\[
N_V(0,\pi(a\wedge Db))=(a_0b_0,0,0,0,0,0)^t.
\tag{R3}
\]

The pre-reading graph calculation independently determines the same central coefficient. After target reading, the separate receiving script also checked (R3), the contraction equality, and N_W pi(a wedge Db)=0 symbolically for arbitrary a,b. All checks passed. That supplemental script is explicitly post-freeze; it is not substituted for the frozen derivation.

The target writes u=exp(sD)a(q), with a holomorphic and a₀(0) nonzero. Independent Section 7 proves this exact form by the actual plumbing map and the termwise integral formula; it does not infer holomorphy solely from unipotent monodromy. Thus the target's brief appeal to the nonzero residue has a complete independent justification.

The target's canonical-frame formula is algebraically exact:

\[
\exp(-sN_W)r_T=i\pi(a\wedge\bar a)+2y\pi(a\wedge D\bar a),
\quad y=\operatorname{Im}s.
\tag{R4}
\]

Indeed applying exp(-sD) to both exterior factors changes the second factor to exp((bar s-s)D)bar a, and i(bar s-s)=2y. The contraction is therefore

\[
A_T=i\operatorname{contr}(a\wedge\bar a)+2y|a_0|^2.
\]

The coefficient of the only y² contribution to the imaginary central coordinate is exactly 2|a₀|², by (R3). Every remaining term is bounded by a constant times y in a fundamental logarithm strip: the canonical splitting and a(q) are bounded; (R4) has degree at most one in y; and exp(sN_V)=I+sN_V has degree one because N_V²=0. The y-dependent quotient-kernel term contributes only the central vector in (R3). Its imaginary part is 2y Im(s)|a₀|²=2y²|a₀|². Dividing by A_T=2y|a₀|²+O(1) gives the target's exact sign and coefficient:

\[
h=y+O(1)=-\frac{\log|q|}{2\pi}+O(1).
\]

Independent Section 9 reaches the same expression through the explicit graph top projection, the beta and chi identities, and the central location of e. These are two fully specified calculations of the same h, identified by (R2).

The minimum argument is also exact: h extends across both finite root centers, tends uniformly to positive infinity at the only removed point, and therefore has a minimum on a compact complement of a cusp disc. Connectedness gives the whole image [h_min,infinity), not merely an upper bound. Hence the target's parameter domain c>-h_min, the failure at the endpoint, and the failure at every smaller c all agree with independent Section 9.

For a full complex change of lift, the exact comparison is

\[
h_{\sigma+a\alpha e}=h_\sigma+\operatorname{Im}a,
\qquad
F_c^{\sigma+a\alpha e}
=(\sigma+(a+ic)\alpha e)(P).
\tag{R5}
\]

The target's displayed comparison for a=ib is the real-line specialization of (R5). Its real-part dependence is retained in (R5) when identifying complex parameter families.

**Receiving conclusion for step 5:** correct. The arbitrary-vector extension identity, the growth coefficient, the attained minimum, and the exact global half-line all pass.

## 6. Rank-three cusp graph and integral period convention

Target step 6 says N_V maps the logarithmic lifted three-plane isomorphically onto ker N_V. The supplied matrix has rank three, square zero, and therefore image equal to kernel. On P(a), the quotient map N_W has rank exactly two when a₀ is nonzero: in the fresh literal matrix its two-by-two minor in the indicated columns is a₀², and N_W itself has rank two. Its kernel is generated by pi(a wedge Da), whose contraction is a₀². Formula (R3) sends any lift of this kernel generator to a₀²e; adding a central vector does not change the result because N_Ve=0. Thus the target's full rank-three claim is valid.

The independent proof gives the exact integral coordinate map behind “integral Jordan marking”:

\[
y_{\rm coh,new}=S^ty_{\rm coh,old},
\qquad
S^tT_VS^{-t}=\begin{pmatrix}I&0\\I&I\end{pmatrix},
\qquad
S^te=(0,e_1)^t.
\tag{R6}
\]

It computes the upper projection X(a) of three literal wedge lifts and proves det X=a₀³. The canonical lifted frame is (X,D_c)ᵗ. Multiplying on the right by X⁻¹ and applying the nilpotent exponential gives the exact graph

\[
\begin{pmatrix}I\\sI+C_c(q)\end{pmatrix},
\qquad C_c=D_cX^{-1}.
\tag{R7}
\]

Both D_c and X⁻¹ are holomorphic at the cusp, so this proves the bounded holomorphic correction, not only its asymptotic size. In the period convention with form rows evaluated on the homology basis S, the matrix is (I,(sI+C_c)ᵗ). Calling its second block Z yields the target's formula Z=sI+C with the correction transposed. Thus the possible row/column convention is resolved by the explicit transpose map and changes no assertion.

The exact graph contraction is

\[
\alpha(x)=\left(1,-1+2(a_1-a_3)/a_0,1-2(a_1-a_2)/a_0\right)x.
\]

Hence adding ic alpha e changes only the first lower row by a bounded holomorphic row, as the family formula requires.

The independent proof selected the explicit plumbing coordinate

\[
q_{\rm pl}(\lambda)=\lambda^4-4x_c(\lambda)^5.
\]

A coordinate such as q₀=lambda/lambda_star-1 is related by the exact holomorphic unit

\[
q_{\rm pl}=q_0U(q_0),\qquad
U(q_0)=\frac{q_{\rm pl}(\lambda_*(1+q_0))}{q_0},
\quad U(0)=\lambda_*q'_{\rm pl}(\lambda_*)\ne0.
\tag{R8}
\]

A holomorphic logarithm of U on a small disc changes C by (log U)/(2pi i) times I. It preserves holomorphy and boundedness, and changes the h comparison only by the corresponding bounded coordinate term. This is the precise local coordinate map needed to compare different cusp coordinate choices.

**Receiving conclusion for the cusp portion of step 6:** correct, with the integral basis map, right multiplication, row/column transpose, and cusp coordinate unit all explicitly identified.

## 7. Both root charts and descent to orders five and four

The target's statement about the fourth power of the order-eight deck action is verified by the independent actual chart map

\[
(s,X,Y)\mapsto(\zeta_8s,\zeta_8^2X,\zeta_8Y).
\]

Its fourth power is (s,X,Y) mapsto (-s,X,-Y). The hyperelliptic involution acts as minus the identity on the rank-four cohomology, as is also checked algebraically by C_g⁴=-I. Its exterior square is the identity; the inclusion defining P and the contraction are equivariant; and the rank-six action satisfies B⁴=I. The exact descent map is t=s². Thus the target's order-four descent follows for the actual lifted bundle and plane, not only for their abstract ranks.

At infinity the map is

\[
(s,X,Y)\mapsto(\zeta_5s,\zeta_5^4X,Y),
\]

and the rank-six action satisfies A⁵=I. The relative differential formulas in independent (54) and (57) exhibit nonzero holomorphic Hodge generators at both smooth root fibers. The denominator beta stays nonzero there by polarization. Consequently j, h, the lift, and F_c extend on the root charts, and h descends as an invariant real analytic function. P1.1 gives the exact finite orders of the full rank-six system.

The target adds that the supplied affine translations are holomorphic on the resulting tori. The exact pointwise construction is the following: the transverse plane defines the complex quotient V_C/F, into which V_R maps by the real-linear quotient map. That map is an isomorphism of real vector spaces because F intersects its conjugate trivially. The real integral lattice maps to a full lattice. A translation vector maps to a constant vector in this complex quotient, and addition by that vector is holomorphic. The finite linear monodromy maps F to F by the chart equivariance, so it induces a complex-linear quotient map; composing it with the specified translation is holomorphic. This verifies the last target sentence at the level needed for P1.8 without using any later filling theorem.

**Receiving conclusion for the root portion of step 6:** correct; the precise chart morphisms, quotient maps, and affine action have all been identified.

## 8. Referenced producer and the independent code boundary

The entire referenced file `code/current_audits/audit_corrections/code/independent_V_markings_06.py` was inspected only after the independent freeze and the target read. Its final cusp portion constructs arbitrary symbolic a,b, computes the literal exterior quotient, and asserts the top scalar a₀b₀ and the vanishing of the remaining five components. This matches (R3). The earlier portions also check the wedge quotient and integral cusp marking. The script's own scope states that it was written after receiving proofs; this receiving comparison preserves that attribution.

The independent pre-reading code uses the supplied matrices directly and computes a different full graph determinant and contraction route, then verifies the beta/chi identities. It does not import the referenced producer or its output. The post-freeze `receiving_exact.py` checks the precise target scalar, contraction and rank-two claims, together with the frozen hashes. Its output is PASS. The existing referenced producer was not executed in place, and no pre-existing output was overwritten.

## 9. Precise normalization convention needing clarification

The received step 3 first uses z as the scalar in sigma+z alpha e and then says that sigma(g) has zero central coordinate “at z=1/2.” No relation identifying this base-coordinate z with lambda occurs in the isolated target. Targeted searches of the full linked source did not find z=lambda/lambda_star or another such coordinate definition. Later source excerpts identify the intended comparison point as lambda=lambda_star/2 and specify a path from lambda=1. Those later statements are not used to prove P1.8 and do not themselves define the missing earlier map.

The actual operation needed is (R1). A precise replacement that aligns with the later stated comparison is:

> In the fixed flat marking continued from lambda=1 along the specified upper-half-plane polygon to lambda=lambda_star/2, require the e-coordinate of sigma(g) at that point to be zero.

Equivalently, define the base coordinate z_base=lambda/lambda_star, reserve a different symbol for the scalar splitting parameter, and specify the flat marking/path at z_base=1/2. The defining coordinate morphism and point then become explicit.

This is a normalization specification issue. The proof of existence, the real analytic h for every specified splitting, its finite attained minimum, the exact admissible half-line, the bounded cusp graph, and finite-root descent have all been proved before this target was read. The issue becomes material when asserting an exact identity between the chosen P1.8 family and a later algebraic family, since the full complex splitting constant records the choice of marking and path.

## 10. Receiving disposition

The complete P1.8 result is independently established. The received proof's substantive geometric, analytic, and matrix steps pass comparison with the frozen derivation. The before-reading gate is fully satisfied by the complete written proof and fresh exact code, not by a partial mechanism. The specific normalization sentence should be clarified as above before relying on it to identify later numerical splitting constants. No source or canonical assessment was edited by this agent.
