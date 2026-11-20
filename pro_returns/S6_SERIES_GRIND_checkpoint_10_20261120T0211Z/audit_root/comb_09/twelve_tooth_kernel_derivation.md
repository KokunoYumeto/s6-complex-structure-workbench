# The actual flat kernel on a twelve-tooth comb

**Proposed complete derivation, pending receiving review.** Root: GPT-6 Astra, ChatGPT Pro mode, inherited effort not separately exposed. All work here follows reading the current E2.2/E2.3/E15 and I D1.1/D1.2 proofs and the attached Viaclovsky comb construction. No before-reading or cross-family claim is made. No canonical status or manuscript is changed by this file.

The conclusion established by the construction below is a nonempty open family of admissible twelve-tooth smoothings whose actual coarse bundle is

\[
K_{12}\simeq\mathcal O_{\mathbb P^1}(-8)
 \oplus\mathcal O_{\mathbb P^1}(-9)^{\oplus2},
\qquad e_{12}=0.
\]

It gives `h11=49` and `h12=48` for those actual compact threefolds, using the proved formula E.5. It does not assign this splitting to every member of the comb family. The construction is by an open set of explicitly described conic and jet data; no absent numerical transition matrix or solved numerical smoothing equation is asserted.

## 1. The original kernel, in the actual root marking

Use precisely the root curve and the line generator of I D1.1. Thus `x` has weight3 and vanishes at the order-four point, `y` has weight4 and vanishes at the order-three point. The original seed has

\[
E_0=G_0=\mathcal O\oplus\mathcal O(-1),\quad
F_0=E_0^*=\mathcal O\oplus\mathcal O(1),\quad
D_0=\det G_0=\mathcal O(-1),\quad L=\mathcal O(-5).
\]

These are the actual vertical/Hodge bundles and their identified trivial summands from I D1.2. In the ordered `E_i tensor G_j` bases the logarithmic period derivative has form

\[
\delta_0=
\begin{pmatrix}0&b y\\c y&d x\end{pmatrix}.
\]

The four entries have weights5,4,4,3; the weight-five section space is zero and each of the weight-four and weight-three spaces is one-dimensional. The actual logarithmic derivative is invertible at the cusp, so `b c != 0`. This proves the asserted shape and nonvanishing from the already identified map, without substituting an arbitrary map for it.

With the wedge convention proved in `II_comb_dual_cup_map_08.md`, the dual cup row on `F tensor G`, ordered by `(11,12,21,22)`, is

\[
\kappa_0=(b y,0,d x,-c y).
\]

The coarse source and target are

\[
\rho_*(F_0\otimes G_0)
 =\mathcal O^{\oplus2}\oplus\mathcal O(-1)^{\oplus2},
\qquad
\rho_*(D_0\otimes L^*)=\rho_*\mathcal O(4)=\mathcal O.
\]

The constant-source block is the nonzero constant row `(b,-c)`: the canonical section `y` is the global coarse frame of the weight-four line. Hence this coarse map is surjective everywhere, including both finite points. Choose its explicit right inverse `1 -> (1/b,0)` in these two constant coordinates. Subtracting the image of that inverse from the other source columns produces the actual kernel isomorphism

\[
K_0\simeq\mathcal O\oplus\mathcal O(-1)^{\oplus2}.
\]

The constant kernel generator is `(c,0,0,b)`. The other two kernel columns are the two weight±1 coarse generators minus their displayed images through the right inverse. This records the sheaf maps, including the possible `d x` column. In particular the argument does not require `d` to be nonzero.

At every ordinary point the usual derivative matrix `H:F_0 -> G_0` is invertible, because its determinant is `-bc y^2` and `y` vanishes only at the removed finite point. The matrix of `H` in row-G/column-F convention is the transpose of the displayed tensor matrix.

## 2. The relative kernel on an actual smoothing

Take twelve distinct ordinary base points. In a coarse coordinate with the critical values `0,1,infinity`, use `2,3,...,13`. At each point attach one of the admissible deformed twistor conics supplied by the original comb lemma. The conic choices will be made more precisely in sections4–6. They belong to the nonempty open set for which the supplied comb theorem gives a simultaneous embedded smoothing with its three critical values and limiting period planes fixed.

Near the fixed critical points, the finite-character graph conditions in E15 identify these coarse sections with actual root-period sections: the indicated invariant-generator divisions are holomorphic because the central values remain fixed. At ordinary nodes this lift is an identity. Thus the family of comb curves carries the pullbacks `F,G` of the tautological subbundle and quotient of the actual root cohomology bundle. Their finite stabilizer characters remain constant. The Gauss–Manin connection has its stated logarithmic pole at the cusp and no pole at an ordinary tooth node.

Write `C -> Delta` for a one-parameter smoothing with every node smoothed to first order. At an ordinary node choose the actual semistable coordinates `xy=s`, with the handle `y=0` and the tooth `x=0`. In a flat cohomology frame the subspace is the graph of a holomorphic matrix `Z(x,y)`. The relative dualizing generator is `dx/x=-dy/y`; the corresponding period derivative is

\[
\Theta=x Z_x-y Z_y.
\]

The relative dual cup map is the map on `F tensor G` obtained by contracting this derivative with the alternating quotient pairing. It takes values in `D tensor omega_(C/Delta)(p0)`. Taking exact finite-group invariants gives a map of actual coarse bundles away from the ordinary nodes, where no averaging is necessary.

The first node coefficients are `H=Z_x(0,0)` and `B=Z_y(0,0)`. The conic direction will be chosen with `B` invertible and linearly independent of `H`. The four entries of `Theta` then generate exactly the ideal `(x,y)` in the regular two-dimensional total-space ring. Indeed they belong to that ideal, and two independent linear coefficients generate its cotangent space; an invertible local row/column operation gives the exact row `(x,y,0,0)`. Its kernel is free, with generators `(-y,x,0,0)`, `e3`, `e4`. This proves local freeness of the rank-three relative kernel at the node.

Away from nodes the central coarse cup row is surjective: on the handle this was proved in section1, and on each tooth it is the nonzero derivative of the immersed conic. Compactness and openness preserve that surjectivity near the central curve. At a smoothed node `xy=s != 0`, the ideal `(x,y)` is the unit ideal. Consequently the relative kernel is locally free around the entire family, and on every sufficiently small noncentral fibre it is exactly the desired bundle `K_12`. The coarse cokernel vanishes there, so `e_12=0`.

## 3. Two conditions, with the mixed term retained

For a derivative matrix `T` in row-G/column-F convention and a tensor matrix `eta` in row-F/column-G convention, set

\[
\langle T,\eta\rangle
 =\sum_i\bigl(T_{2i}\eta_{i1}-T_{1i}\eta_{i2}\bigr).
\]

This is the actual cup row, with its values in the determinant line retained. It is a perfect pairing between `Hom(F,G)` and `F tensor G`, after the determinant twist.

The central kernel restricts to a negative elementary modification of the ordinary kernel on each branch. Its handle section `eta_h` and tooth section `eta_t` must first have the same value `eta_0`, which obeys

\[
\langle H,\eta_0\rangle=\langle B,\eta_0\rangle=0.
\]

There is a second condition. Expand a lifted relative kernel section and the period graph through order `xy`. Since

\[
Z(x,y)=Z_h(x)+Z_t(y)-Z(0,0)+xy R(x,y),
\]

the coefficient of `xy` in `xZ_x-yZ_y` is zero. This is an exact cancellation; the arbitrary mixed graph term is retained in the formula. The coefficient of `xy` in the kernel equation is therefore

\[
\langle H,\eta_t'(0)\rangle
 -\langle B,\eta_h'(0)\rangle=0.                 \tag{*}
\]

Changing the dualizing generator by a unit adds multiples of the two already zero value equations. Thus this is a condition on the actual first jet. It cannot be removed by keeping only the kernel of the map on the singular fibre: that larger kernel permits the two Koszul branch coefficients independently, whereas the flat relative kernel identifies them.

## 4. Explicit conics and their first-jet map

Use the flat vector space `F_b direct-sum G_b`. An open chart of conics through its reference plane has tautological columns and quotient map

\[
S(y)=\binom{I+yA}{yB},\qquad
q(y)=(-yB,\ I+yBAB^{-1}),\qquad \det B\ne0.
\]

Both are written homogeneously by replacing `I+yA,yB` with `uI+vA,vB`. The columns have rank two for every `[u:v]`: for `v != 0` the bottom block is invertible, and for `v=0` the top block is invertible. The quotient map has rank two by the same check. The exact products are

\[
qS=0,\qquad q\frac{dS}{dy}=B.
\]

Thus the tautological and quotient bundles are literally `O(-1)^2` and `O(1)^2`, with their indicated maps. Small complex changes of `(A,B)` around any twistor conic remain admissible by compactness. Reparameterizations fixing `y=0` remove a common scale in `B` and a scalar multiple of `I` in `A`. The resulting six parameters are the full local space of conics through the point; their tangent and second normal jets have the dimensions and surjectivity stated in the original conic lemma.

On the graph chart,

\[
Z_t(y)=yB(I+yA)^{-1}.
\]

The literal transition of tensor coefficients from the displayed conic frames to graph frames is

\[
\eta_{\rm graph}(y)
 =(I+yA)\eta_{\rm conic}(y)
                 (I+yBAB^{-1})^{-t}.
\]

In the conic frames `F tensor G=O^4`, and the derivative cup row is the constant functional `eta -> <B,eta>`. Its kernel is `O^3`. Every global section of that kernel is constant and is uniquely determined by its value at the attaching point. Consequently the derivative forced by a shared value is

\[
\eta_t'(0)=A\eta_0-\eta_0(BAB^{-1})^t.
\]

Substitution into (*) gives the actual two-jet quotient on the handle:

\[
\langle B,\eta_h(0)\rangle=0,\qquad
\langle B,\eta_h'(0)\rangle
 =\left\langle H,
 A\eta_h(0)-\eta_h(0)(BAB^{-1})^t\right\rangle.       \tag{**}
\]

All matrices are maps in the actual flat cohomology chart. No equality between `E` and `G` is used. Changing a local frame of `K_0` introduces its actual derivative in the second equation; that is a fixed affine change of the first-jet coefficient and preserves the parameter freedom proved next.

## 5. Freedom of the two-jet quotient

The first equation of (**) is an arbitrary covector on `ker <H,->`, up to an open restriction. The map `B -> <B,->|_(ker<H,->)` is the quotient of the perfect four-dimensional pairing by the line spanned by `H`. Therefore it surjects onto the three-dimensional dual of the actual handle kernel fibre. Nonzero covectors form the required open set.

The second coefficient has full remaining freedom. Use the actual invertible map `H:F_b -> G_b` to identify these two fibres for this calculation, making its matrix `I`. Then a simultaneous basis change diagonalizes the endomorphism `H^-1 B` on the open set with distinct eigenvalues. Write its matrix as `diag(beta1,beta2)`, with `beta1 beta2 (beta1-beta2)(beta1+beta2) != 0`. The two value equations then say

\[
\eta_0=\begin{pmatrix}u&0\\0&v\end{pmatrix}.
\]

For `A=(p,q;r,s)`, direct multiplication gives

\[
\left\langle I,A\eta_0-
          \eta_0(BAB^{-1})^t\right\rangle
 =r(1+\beta_2/\beta_1)u
  -q(1+\beta_1/\beta_2)v.
\]

The two coefficients are independently arbitrary as `r,q` vary. This proves surjectivity onto the dual of the two-dimensional intersection kernel. Scalar changes of `A` contribute zero, agreeing with the reparameterization quotient. The diagonalization is used with its actual `H` and simultaneous change of bases; the calculation is an equality of the maps before and after that invertible transport.

It follows that the map from conic data to the length-two quotient of `K_0` supported at the node is dominant, and is a submersion on this explicit open set. In a local frame the quotient is represented by

\[
\eta\longmapsto \ell(\eta(0))+
 t\bigl(\ell(\eta'(0))+\psi(\eta(0))\bigr)
                    \pmod{t^2},
\]

where `ell != 0` and `psi` is arbitrary modulo `ell`. The preceding displayed formula supplies the two free coefficients of `psi` on `ker ell`. The fixed derivative of a chosen handle frame merely translates `psi`.

## 6. A nonempty balanced open set for twelve teeth

Let `K'` be the subsheaf of `K_0` defined by the twelve length-two quotients (**). It is a vector bundle of rank three and degree `-26`. The parameter space of such nonzero covectors and first-jet coefficients, at the twelve fixed distinct nodes, is irreducible.

The desired balanced locus is nonempty. To see this with exact bundle maps, temporarily choose the explicit splitting

\[
K_0=\mathcal O\oplus\mathcal O(-1)\oplus\mathcal O(-1).
\]

Assign four nodes to each summand. At each assigned node take the corresponding coordinate covector and its derivative, with `psi=0` in that summand's frame. The quotient is restriction of that component modulo the square of the local parameter. Its kernel is the component tensored by the ideal of twice the sum of the four assigned points. Each such divisor has degree eight, so the literal kernel is

\[
\mathcal O(-8)\oplus\mathcal O(-9)\oplus\mathcal O(-9).
\]

Equivalently the coordinate multiplication maps are the three products of the four squared linear factors. Their inverses are division by those factors in the locally modified frames; this identifies the kernel as a bundle, including its fibres at the nodes.

The two properties

\[
H^0(K'(7))=0,\qquad H^1(K'(8))=0
\]

define an open set of these quotient parameters by semicontinuity. The displayed example belongs to it. The corresponding conic-parameter preimage is nonempty by the explicit dominance in section5. The original positive-modification condition needed to smooth the comb is also a nonempty Zariski-open condition in the conic tangent directions, by the supplied normal-sheaf proof and its bound `m=12`. Both preimages are dense open subsets of the same irreducible conic parameter chart. Their intersection meets the nonempty complex-open set of admissible conics: a proper algebraic closed subset has empty analytic interior. This selects actual admissible conics satisfying both conditions, while retaining all original finite-root and cusp data.

This use of the split-coordinate example proves nonemptiness of the open condition. It does not claim that its special coordinate covectors themselves lie in the admissible tangent image; the exact dominant map is what transports the open condition to actual conics.

## 7. Collapse of the teeth and cohomology of the flat kernel

Let `K_C` be the restriction of the locally free relative kernel to the nodal central curve. On the handle it is the length-one modification of `K_0` at each node, whose value condition is the first equation of (**). On a tooth its image in the ordinary constant kernel is its elementary modification at the node; hence it is

\[
K_C|_{C_i}\simeq\mathcal O(-1)\oplus\mathcal O^{\oplus2}.
\]

One can see this directly: `ker <B,->` is a constant three-dimensional space, and the additional node condition is the nonzero functional `<H,->` on it. Choose an explicit basis with that functional as the first coordinate. That coordinate must vanish at the node, giving `O(-1)`, and the other two coordinates remain constant. Their global sections evaluate to a two-dimensional subspace of the three-dimensional fibre of the flat kernel.

Collapse each tooth to its attaching point, by `pi:C -> B`. Apply the normalization exact sequence for the locally free `K_C`. The tooth `H^1` groups vanish, and the handle's full fibre evaluation is surjective onto every node fibre. Hence

\[
R^1\pi_*K_C=0.
\]

The two-dimensional images of the tooth sections impose one further condition on the already modified handle bundle. The coefficient comparison in section3 is exactly this further condition, so

\[
\pi_*K_C=K'.
\]

This is a sheaf identity via restriction to the handle and the unique extension to each tooth. It retains both conditions, not just their total colength. Tensoring by the pullback of a coarse base line and using this exact sequence gives

\[
H^j(C,K_C\otimes\pi^*\mathcal O(k))
 =H^j(B,K'(k)),\qquad j=0,1.
\]

The relative kernel is locally free and the family of curves is flat. Thus it is flat over the smoothing disc. Semicontinuity gives, for every sufficiently small nonzero smoothing parameter in the chosen family,

\[
H^0(K_{12}(7))=0,\qquad H^1(K_{12}(8))=0.
\]

Its degree is `-26`, already fixed by the actual surjective coarse cup map. These two vanishings force the displayed splitting without a numerical guess. For completeness, Riemann–Roch gives `h0(K_12(8))=1`. Its nonzero section is nowhere zero: a zero divisor would produce a section of `K_12(7)`. Its quotient `Q` has rank two, degree minus two and `H0(Q)=H1(Q)=0`. The evaluation map

\[
H^0(Q(1))\otimes\mathcal O\longrightarrow Q(1)
\]

is an isomorphism: the exact sequence at each point and `H1(Q)=0` make it surjective, and Riemann–Roch gives two source dimensions. Thus `Q=O(-1)^2`. The extension by `O` splits because its exact extension group is `H1(O(1))^2=0`. Twisting back gives the claimed actual bundle isomorphism.

The nonempty open family now has `h0(K_12)=0`, so the original proved formula E.5 gives `h11=49,h12=48` and the coarse cokernel length is zero. No splitting of special members, other tooth counts, or the entire original open row is inferred from this one proved construction.

## Sources and checks still to receive

The original attached Viaclovsky source supplies the actual admissible conics, their `O(-1)^2/O(1)^2/O(2)^3` splittings, tangent-direction openness, fixed-marking embedded smoothing, and the sufficient twelve-tooth bound. Exact opened source portions are the twistor-conic lemma and proof, the complete comb-smoothing proposition and proof, and equation `originalnormal` with its bound. I D1.1/D1.2 and II E15 supply the actual root/coarse transition maps and original bundles; the complete dual-cup adapter was already proved in `II_comb_dual_cup_map_08.md`.

The new work is the flat-kernel node calculation, its actual first-jet conic map, the dominance calculation and its cohomological transport through tooth collapse and smoothing. A fresh symbolic and Hermite-matrix certificate is to be executed separately. Independent receiving review must check the exact family lift, determinant conventions, local flat-kernel condition and dominance before any source/status integration.
