# 02WJ / night:P4.12: prereading derivation

Checker: restore_build. Written after checkpoint-14 restoration on 21 November 2026, from the original statement and the root's exact v2 standing-hypothesis packet. The target printed proof, A's reconstructed proposals and A's Grauert repair have not been opened. The unused full-headline export was not read. This record makes a current before-release claim only.

## Exact inputs and scope

The standing data are a connected smooth compact complex threefold Y, b1(Y)=b2(Y)=0, a proper surjective holomorphic map f:Y→B with connected fibres onto a smooth compact curve, and smooth general fibre a two-dimensional complex torus. The specified fibre is mS, where S is irreducible and reduced. Its full multiplicity remains m throughout. The safe E1 statement also identifies the meromorphic function field with that of the base, but the calculation below uses only the explicitly listed geometric hypotheses.

The original target packet is `agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_02WJ_statement_inputs.tex`. The additional exact scope is `agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_02WJ_global_hypotheses_inputs_v2.tex`, SHA-256 8f449aac3eb41173c7c81794296c07a976f5db2a256cf80589a68520710ab600. The companion root receipt has SHA-256 3b8dd58d383b280005367688da5258b4c4743e26ad2933aa2a2c7fd926602767. No conclusion of Theorem C or C.2.G.1 is used.

For compact smooth surface classification I use Peters, *Compact Complex Surfaces*, Theorem 3.1, printed p.10, and its definitions on p.9, together with the Hodge/Euler formulas on pp.5–6. I reopened the author's primary PDF at https://www-fourier.univ-grenoble-alpes.fr/~peters/ConfsAndSchools/Canada/surface.pdf. The same classification input was already read and recorded before the second C group. The negative definiteness needed below is derived directly from a pulled-back local function, rather than attributed to an unread repair.

## 1. The dualizing line and its exact torsion exponent

Take a sufficiently small disc Δ about b, with no other singular values. On X=f^{-1}(Δ), the smooth fibres are tori. The exact tangent sequence of a smooth fibre F identifies K_X|F with K_F after the trivial base tangent factor is chosen. Thus h0(F,K_X|F)=1. Proper direct image makes f_*K_X coherent; it is torsion free because a section of the line K_X killed by a nonzero base function vanishes on the dense open complement of a fibre and hence vanishes everywhere. It is therefore a rank-one locally free sheaf on Δ.

Choose a local generator of f_*K_X. Its evaluation is a holomorphic section s of K_X. On every sufficiently general fibre it is a nonzero canonical form of a torus and has no zero. Its divisor has no horizontal component. Shrinking Δ leaves only the central fibre, so div(s)=aS for an integer a≥0. The section defines the actual line-bundle isomorphism K_X≅O_X(aS).

Set N=O_X(S)|S. The local base coordinate t has divisor mS, so its principal-divisor trivialization gives N^m≅O_S. Since Y is smooth, S is a Cartier hypersurface and is Gorenstein. Adjunction is the isomorphism

    ω_S ≅ (K_X ⊗ O_X(S))|S ≅ N^(a+1).

Taking the mth tensor power yields ω_S^m≅O_S, with exactly the exponent in the statement. This argument neither replaces the full fibre by its support in a sheaf calculation nor identifies a numerically trivial line with a trivial line.

## 2. Euler characteristic and first cohomology

The global Cartier sequence is 0→O_Y(-S)→O_Y→O_S→0. Write s=c1(O_Y(S)). The hypothesis b2(Y)=0 gives s=0 in H2(Y,Q). Hirzebruch–Riemann–Roch consequently gives

    χ(O_S)=∫_Y td(T_Y)(1-exp(-s))=0.

The reduced irreducible compact S has H0(O_S)=C. Gorenstein duality gives h2(O_S)=h0(ω_S). A nonzero section u of the torsion line ω_S has u^m a nonzero constant under the fixed trivialization of ω_S^m: it cannot be the zero constant because S is reduced and u is nonzero on a dense open subset. It therefore has no zero and trivializes ω_S. Hence h0(ω_S) is either zero or one, and χ=0 gives h1(O_S)=1+h0(ω_S)∈{1,2}.

## 3. The normal case: resolve the singular points

Suppose S is normal. Its singular locus is finite. Let π:Z→S be the minimal smooth resolution and E_i its irreducible exceptional curves. The Gorenstein property makes all discrepancies integral, and outside the exceptional set π is an isomorphism. Therefore there is an actual identity of line bundles

    K_Z ≅ π*ω_S ⊗ O_Z(Σ a_i E_i),       a_i∈Z.

The pullback L=π*ω_S has L^m≅O_Z and zero intersection with every curve.

### 3a. Negative definiteness from a local principal divisor

For each connected exceptional fibre, choose a nonzero holomorphic function g in the maximal ideal of the singular point, with a curve of zeros through that point. Its pullback divisor is C'+Σ n_i E_i, with all n_i>0 and C' the strict transform. It meets the exceptional fibre: a component of the zero curve through the point has a proper transform whose closure meets the fibre by properness. For the intersection matrix M=(E_i·E_j), principal-divisor intersection gives

    M n = -(C'·E_i)_i ≤ 0,

with at least one strict inequality on each connected fibre. Distinct curves have nonnegative intersection. For any real vector v write x_i=v_i/n_i. Direct expansion gives

    v^t M v = Σ_i n_i (Mn)_i x_i²
                - Σ_(i<j) M_ij n_i n_j (x_i-x_j)².

The exceptional fibre is connected because π_*O_Z=O_S and Stein factorization applies to the normal S. Its intersection graph is connected. The displayed expression is negative for every nonzero v: equality would force x constant on that graph and zero at an index with (Mn)_i<0. Thus M is negative definite.

Minimality excludes a smooth rational exceptional (-1)-curve. Adjunction gives

    K_Z·E_i = 2p_a(E_i)-2-E_i² ≥ 0.

Indeed, an integral curve of arithmetic genus zero is a smooth rational curve, whose negative self-intersection is at most -2 here; all other curves have arithmetic genus at least one and negative self-intersection. Thus Ma=k≥0. If a_+ is the vector of positive parts of a, the disjoint supports and nonnegative off-diagonal entries give

    a_+^t k = a_+^t M a_+ + a_+^t M(a-a_+) < 0

whenever a_+ is nonzero, contradicting k≥0. Consequently every a_i≤0. Put D=-Σa_iE_i≥0. The preceding line identity becomes K_Z≅L⊗O_Z(-D).

### 3b. A nonzero discrepancy cycle contradicts χ(O_S)=0

Let P=Σ_p dim(R1π_*O_Z)_p. Leray gives χ(O_Z)=χ(O_S)-P=-P. The terms are finite length because they are supported at the finitely many singular points.

Suppose D is nonzero. Since K_Z^m≅O_Z(-mD), any pluricanonical section has an mth power which is a holomorphic function vanishing along a nonzero effective divisor; compactness forces it to vanish. Thus all plurigenera of Z vanish.

Surface Riemann–Roch for the exact sequence defining D gives

    χ(O_D)=-(D²+K_Z·D)/2=0,

since K_Z+D=L is numerically trivial. As D is nonempty, h0(O_D)≥1, so h1(O_D)≥1. Formal functions makes P at least h1(O_D). More explicitly, a sufficiently high infinitesimal exceptional neighbourhood contains D; restriction of its H1 onto H1(O_D) is surjective because the kernel is supported in dimension one and has H2=0. This also proves the same bound for any effective exceptional subcurve. Therefore P>0 and χ(O_Z)<0.

The compact surface classification, with κ(Z)=-∞ and negative holomorphic Euler characteristic, makes the minimal model of Z ruled over a curve B0 of genus g≥2. Blowdowns preserve χ, so χ(O_Z)=1-g and P=g-1. Compose the blowdown map with the ruling to obtain h:Z→B0. On a general ruling fibre F≅P1, K_Z·F=-2 and L·F=0, so D·F=2. Some component E_i of D therefore maps surjectively to B0. The induced finite map from the normalization of E_i to B0 has genus at least g by Riemann–Hurwitz. Hence h1(O_Ei)≥g. The exceptional-neighbourhood restriction just proved gives P≥h1(O_Ei)≥g, contradicting P=g-1. Thus D=0.

### 3c. Zero discrepancies leave no exceptional curve

Now K_Z≅L is torsion. Adjunction excludes every (-1)-curve on Z, so Z is minimal, and κ(Z)=0. Also χ(O_Z)=-P≤0. The classification list with these numerical properties consists of tori, bielliptic surfaces, primary Kodaira surfaces and secondary Kodaira surfaces, all with χ=0. K3 and Enriques surfaces have positive χ and do not meet this computed value.

Each of the remaining surfaces contains no rational curve. For a torus, a map from P1 lifts to C² and is constant. For a bielliptic surface or secondary Kodaira surface, a map from the simply connected P1 lifts through its finite unramified torus or primary-Kodaira cover. For a primary Kodaira surface, composition with its elliptic base is constant, and then the map factors through its elliptic fibre and is constant. These are actual lifting/factorization maps, not an identification of those surface types.

On the other hand, every exceptional E_i would satisfy 0=K_Z·E_i=2p_a(E_i)-2-E_i². Since E_i²<0, this forces p_a(E_i)=0 and E_i²=-2; E_i would be a rational curve. There are therefore no exceptional curves. A proper birational resolution of a normal surface with empty exceptional locus is an isomorphism, proving that S is smooth.

## 4. A singular nonnormal support has normalization of Kodaira dimension -∞

The preceding argument shows that a singular support cannot be normal. Let ν:Sbar→S be its normalization and π:Z→Sbar a smooth resolution. The hypersurface S is Cohen–Macaulay and hence satisfies S2. Failure of normality therefore occurs in codimension one, so its conductor has a nonempty curve in Sbar.

Finite duality for the Gorenstein surface identifies ν_*ω_Sbar with Hom_O_S(ν_*O_S,ω_S). The Hom module is the conductor multiplied by the invertible ω_S. At each generic conductor branch in the smooth locus of Sbar this is the explicit inclusion

    ω_Sbar ↪ ν*ω_S,

whose image vanishes to positive conductor order. Let u be a section of K_Z^k for any positive integer k. Over the smooth locus of Sbar, π is an isomorphism, so u maps by the kth power of that inclusion to a holomorphic section of (ν*ω_S)^k which vanishes along the conductor curve. The omitted singular points of the normal Sbar have codimension two; Hartogs extension for the line bundle ν*ω_S extends this section globally. Its mth power is a global holomorphic function, because (ν*ω_S)^m is trivial. This function vanishes on the conductor and is therefore zero. Thus u=0.

All plurigenera of Z vanish. The same is true on its minimal smooth model: under a blowup, the canonical divisor changes by the exceptional divisor and Hartogs extension identifies the pluricanonical section spaces in both directions. Hence that minimal resolved normalization has κ=-∞, as asserted.

## Pre-release status

The fresh standard-library program `S6_SERIES_PUBLISH_II_WJ_WL_fresh_exact.py` has SHA-256 d50c5b6e4fd18c272c4b3c265b313acccd46fb3b779b789360bafa8ec57b4beb. Its successful output has SHA-256 a46d2bcc167deb5d4eb6fe8d37318e796a8da8ed1ba381b4ac3441c90989c9f1. It independently expands the weighted symmetric-matrix identity in formal monomial dictionaries for sizes one through six. The arbitrary-size expansion and the sign argument are proved above; finite sizes are checks of the expression, not a replacement for that proof.

This derives every stated conclusion at the explicit smooth global scope. It does not invoke a negative-sign theorem, an equality classification, an assertion that every fibre is normal crossings, or any unreleased proof. The stronger normal-support conclusion is obtained through the explicit discrepancy/exceptional-cycle argument above. No target proof has yet been opened, no canonical source or ledger has been changed, and no event is claimed by writing this file.
