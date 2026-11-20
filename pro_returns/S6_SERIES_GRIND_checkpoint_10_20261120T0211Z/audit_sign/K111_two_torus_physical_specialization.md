# K111: localization inside each actual physical fixed component

This derivation belongs to the newly constructed auxiliary atlas. It explains the exact comparison between its two-torus calculation and its physical-circle contribution. The original unavailable CFL computation retains its separate verification scope.

## The actual second action and its source/line arrows

On the common characters define

\[
(\lambda,\zeta):(X_c,Z_c,P,p)\longmapsto
(\lambda X_c,\zeta Z_c,P,p).
\]

Every full period coefficient \(p,f_0,\eta,c_{12},u_s,u_t,c_q\) is a function of the fixed source parameters. Therefore this action commutes with the actual L and T maps, including their full units and reciprocal arrows. Each fan chart is an invariant affine toric chart in the original lattice. Thus the action descends to the complete periodic atlas wherever its endpoint gluing has been constructed.

The two cocharacters are the physical \(\delta=(1,0,0)\) and \(a=(0,1,0)\) in the common three-lattice. Their exact native images are

| Endpoint | Physical \(\delta\) | Second cocharacter \(a\) |
|---|---|---|
| Zero \((X_0,Y_0,P,p)\) | \((-1,0,0,0)\) | \((-1,1,0,0)\) |
| One \((X_1,Y_1,P,v)\) | \((0,1,0,0)\) | \((-1,0,0,0)\) |
| Infinity \((X,Z,R,u)\) | \((1,0,0,0)\) | \((0,1,0,0)\) |

These are obtained by the displayed reciprocal character maps. Every actual endpoint period matrix fixes both vectors: its nonidentity columns involve only the two base coordinates. This proves the exact equivariance of the full period gluings.

The source and genuine point coefficient on common band one obey

\[
x_1=pP^3Z_c,\qquad
v_2=\frac{\eta P^2X_cZ_c}{f_{P^2}(x_1)}.
\]

Transporting the action through this actual arrow gives

\[
x_1'=\zeta x_1,\qquad
v_2'=\lambda\zeta\,
\frac{f_{P^2}(x_1)}{f_{P^2}(\zeta x_1)}v_2.
\]

Its inverse is the reciprocal evaluated at \(x_1'\). Composition of two such arrows cancels the middle theta factor and gives the product \((\lambda_1\lambda_2,\zeta_1\zeta_2)\). The numerator and denominator have exactly the translated point/O Cartier types; the I2P graph charts carry these types with their full generators. For \(\zeta=1\), the coefficient is literally \(v_2'=\lambda v_2\), so the physical nonzero-vector circle and its associated line are unchanged. This is the precise source and line morphism connecting the auxiliary torus action to the physical bundle.

## Assign physical components before any localization

For a full regular endpoint chart B, first compute \(B^{-1}\delta\). Its nonzero coordinate weights determine the actual normal face; coordinates with zero weight are the tangent coordinates of the physical fixed component. Internal face identifications and the complete saved period maps identify these faces. A full component record consists of that entire orbit, its chart owners and the exact period matrices and units aligning them.

Faces at endpoint-disc height zero belong to completed generic physical components. Their correspondence is made through the saved full character maps and native upper-face owners. Faces with original source height zero give the prescribed noncompact lower components: the twelve one-end faces \(\langle E_l,E_{l+1}\rangle\), and the zero-end physical faces joined by the actual T0 map. Every other physical component has both endpoint base functions zero and its full compact corner star.

This ownership assignment precedes the second-action calculation. All two-torus fixed pieces are assigned to their physical component through these same face maps. A piece in a noncompact physical component retains that owner's identifier and is reserved for its own framed lower or moving-cap calculation.

The two-torus preserves each compact physical component F. Indeed it commutes with the physical circle and hence maps the physical fixed locus to itself. The torus is connected, and the finite full face inventory gives finitely many connected physical components. The induced continuous action on that finite component set is constant. Its identity element fixes F, so the whole torus fixes F setwise.

## Localization on one compact physical component

Let \(E=N_{F/X}\) be the actual physical normal bundle of F in the completed atlas. Its equivariant splitting has nonzero physical weights \(w_i\), original normal Chern classes \(x_i\), and the second-action lifts supplied by the full coordinate derivatives. Write u for the physical equivariant parameter and v for the second parameter. The physical normal Euler factor is retained as

\[
e_{T^2}(E)=\prod_i(x_i+w_i u+\text{the actual second-action character}).
\]

The inverse exists as a formal power series in \(v/u\) after u is inverted, because every \(w_i\ne0\). Positive-degree ordinary Chern classes are nilpotent in the cohomology of the compact F. Thus

\[
\int_F\frac{u^3}{e_{T^2}(E)},\qquad
\int_F\frac{u\,[p_1(TF)+p_{1,T^2}(E)]}{e_{T^2}(E)}
\]

are regular at \(v=0\). The physical pair is minus their \(u^{-1}\) coefficients at \(v=0\), with the original physical M orientation and duality established in CFL.27–31.

Localize the second action **within this compact F**. For each connected second-fixed piece H in F, its tangent-normal bundle \(N_{H/F}\) has zero physical weight and its nonzero second weights. The exact tangent sequence gives

\[
T F|_H=T H+N_{H/F},\qquad
N_{H/X}=N_{H/F}+E|_H
\]

as equivariant complex bundle classes, with the coordinate/frame maps recorded by the aligned star. The Euler denominator therefore becomes

\[
e_{T^2}(N_{H/F})\,e_{T^2}(E|_H)
=e_{T^2}(N_{H/X}),
\]

while additivity of \(p_1\) gives the same complete tangent-plus-normal numerator. This supplies the actual map from the physical component integral to the sum over its two-torus pieces. Every pole in v introduced by the tangent Euler factors cancels within the sum for that F, because its unlocalized integral above is regular at \(v=0\). The finite implementation checks that cancellation separately for every compact physical owner before evaluating \(v=0\).

Set \(v=\varepsilon u\). For a two-torus fixed point, write the four full normal weights as \(W_i(\varepsilon)=w_i+\varepsilon a_i\). Its contributions to the owner sum are

\[
-\frac1{\prod_iW_i},\qquad
-\frac{\sum_iW_i^2}{\prod_iW_i}.
\]

For a compact two-torus fixed curve with its actual three normal degrees \(d_i\), put

\[
W=\prod_iW_i,\quad S=\sum_i d_i/W_i,
\quad Q=\sum_iW_i^2,\quad T=\sum_iW_i d_i.
\]

Its contributions are

\[
S/W,\qquad (Q S-2T)/W.
\]

These formulas retain every zero physical weight as \(\varepsilon a_i\); that weight is the second-action normal direction inside F. They follow by expanding the displayed full Euler factors to the actual dimension of H. The sum for each F has no negative \(\varepsilon\) coefficients. Its constant coefficient is exactly the original physical contribution of F.

## Why only curves and points occur for the second action

All common upper rays have positive original P height. The two-torus spans the original plane of zero P height. A two-ray cone cannot span that plane, because each of its rays has positive height. Every generic two-torus fixed normal face therefore has dimension three, so its component is a curve over the exceptional parameter sphere, with one owner for each complete generic three-cone.

At an endpoint, every ray has positive total base height \(r+z\). The two-torus plane is \(r=z=0\). Two rays spanning that plane would themselves lie in it, contradicting their positive base height. Endpoint two-torus fixed faces have dimension three or four; the pieces are curves or points. Their complete stars and physical component ownership determine which are compact and how their period arrows align.

## Exact generic curve clutches

For an ordered common cone N, each endpoint supplies the unique complete four-chart owner of its generic facet. Let \(l_e\) be that owner's transverse ray, with endpoint-disc height one. The complete generic normal coefficient arrow has order

\[
c_e=N^{-1}F_e l_e,
\qquad d=-c_0-c_1-c_\infty.
\]

Here the full character matrices are

\[
F_0=\begin{pmatrix}-1&-1&23i+11j&-i-j\\0&1&3i+3j&3i+2j\\0&0&1&0\end{pmatrix},
\]

\[
F_1=\begin{pmatrix}0&1&23i+11j&12(2i+j)\\-1&0&3i+3j&0\\0&0&1&0\end{pmatrix},
\quad
F_\infty=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&1\end{pmatrix}.
\]

The zero \(f_0\) powers, one p and \(c_{12}\) powers, and infinity equality \(P=Ru\) are retained in their full coefficient and inverse arrows. The three generic columns of \(N^{-1}F_eB_e\) are their actual permutation columns. The remaining column is the written \(c_e\). Coefficient and frame transitions are reciprocal, giving the displayed negative sum. The full nonvanishing units on each endpoint disc have degree zero; their boundary values continue to be carried by the actual bundle morphism.

For a corner curve, the two complete aligned charts give the literal relation
\(t_0+t_\infty+\sum_i d_i n_i=0\), with saturated primitive opposite quotient rays. Its reciprocal tangent coordinate and complete normal derivatives give these degrees. Both base parameters vanish on a compact corner component, so the retained analytic units restrict to their actual nonzero constants; the complete period-cycle check retains their product.

## Completed execution and precise source-graph scope

The endpoint execution is complete: zero has 54,121 regular charts, one 2,022, and infinity 2,381. The complete compact certificate contains 35,908 physical owners, 1,926 three-end second-fixed curves and 52,546 compact corner second-fixed pieces. All 67 pieces in the thirteen prescribed noncompact physical owners retain their separate owner assignments. The producing program performs 983,447 exact checks; every owner has no negative epsilon coefficient, and the substitutions (u,v)=(1,epsilon) and (1+epsilon,2epsilon), retaining the original numerator, agree owner by owner. The compact pair is (895,139).

The parent independently replayed the saved exact chart/face/weight data with a separate Fraction Laurent implementation, without producer imports or reading that implementation first. Its 484,310 checks agree for all owners, both substitutions and every ordered generic clutch. This is a separate implementation within the same GPT-6 Astra model family.

The auxiliary action used here is the compact S1×S1 action on the regular toric filling. Full period functions depend only on the fixed base. Its point/O module realization is used on the unchanged exterior and actual twelve lower source stars. On invariant node domains the entire E products are units; on the invariant O annulus 1/2<|x|<2 with |P²|<1/4, both x-P² and zeta*x-P² remain units for |zeta|=1. The theta-ratio formulas there extend through the actual original sections and preserve every coefficient.

The complete toric interior does not all map to the proper point graph: the exact mixed-sign counts are 8,723 zero, 229 one and 184 infinity cones. Its further resolved-graph chart crossings are 11,051, 440 and 841. Those failures are retained in `K111_point_graph_lift_scope.json`; its 20,711 checks establish instead every localized exterior face and all thirty-six lower-source chart maps. No extra graph resolution is performed inside the counted filling. The toric action and tangent bundle used for the compact calculation are therefore exactly those of the counted atlas.

`K111_auxiliary_resolution_comparison.md` and `K111_new_auxiliary_proof.tex` give the complete received filling comparison: identity-character maps on the original exterior, actual point-module generators there, the NS outer normal derivative and interior divisor bundle for the moving component, and the resolved graph maps and source flows for the twelve lower doubles. The corrections branch independently verified that comparison in its full report `K111_auxiliary_boundary_comparison_05.md`, with 137,749 boundary/normal checks, 2,464 full period/cocharacter checks and 18 inherited identities. The parent has accepted that receiving comparison. Together with the separately replayed compact and moving arithmetic, it closes the new K111 route. The original unavailable CFL and IL arrays remain unreconstructed in the distinct final problem `iv:open:K111:original_auxiliary_arrays`, retaining their full original formulas and maps.

## Exact final-atlas linkage

`K111_same_atlas_link.json` passes286,678 checks. Every final endpoint chart occurs exactly once across generic, compact and explicitly capped pieces. Every physical-owner face is compared through its actual native/common character map; every corner weight and all31 moving ordered cones/full T0 alignments agree with the final fan. The SHA256 table links both parent independent input receipts to these unchanged compact and moving outputs. The separate parent moving calculation has378 checks and reproduces the full divisor matrix, chronological blowup coefficients, own-cap roots and pair(-906,-111).
