# Weighted OS45: actual fan and source-line charts, and the remaining global comparison

Recorded 2026-11-20 UTC by GPT-6 Astra, ChatGPT Pro mode; reasoning effort inherited from root and not separately exposed. This is a new local derivation after opening the receiving inputs. It is not a before-reading proof of D.2.53, and it does not assign the refined class 0 or 4.

## Exposure and exact inputs

I read the complete D.2.43 proof, the critical-cycle/reference-frame and literal-specialization parts of D.2.44, the current D.2.46 marked monodromy and cap maps, D.2.47's literal fan, D.2.48's reference-parity proof, and D.2.53's critical-chain, boundary-cochain, localization and remaining-gate text. Current locators in `parts/III.body.linked.tex` are D.GC1–14; D44.5–12; D.GI2–5; D47.1; D.WI6–13; D.PC3–5; D.OS5–8; and the final boundary-prism paragraph. The source-line input is the complete local Tate calculation D.FI2, currently near lines 6262–6305. The OS45 marked tuple is D.VC9. I also read the root local-thimble report and its orientation addendum, the root odd-cycle route report, and the boundary-prism output (not its producing program).

The relevant actual long-to-short columns are

\[
 l_1=(8,-6),\qquad l_2=(24,-16),\qquad
 L=\langle l_1,l_2\rangle=8\mathbb Z\oplus2\mathbb Z.
\]

The short basis is the manuscript's `(e1,delta)`. Its sign must be retained; the physical line coordinate is tracked below. The literal first finite matrix is `A1=I+E12`. The root's complete core certificate establishes that alpha=`e1 wedge delta` has order two in the cusp boundary, is killed in the filled exterior and in the cusp, and detects an odd class after gluing. That algebra does not specify a framed embedding or the local specialization intersections.

## 1. A cone in the specified fan, including its quotient position

D47.1 has directions `(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)`. Its triangles are exactly the translates of `(0,e1,delta)` and `(e1,e1+delta,delta)`. Thus the root's horizontal edge between `(0,0)` and `(1,0)` is an actual edge. Its two adjacent charts have the exact transition

\[
 (x',y',z')=(xz,yz,z^{-1}),\qquad xyz=x'y'z'.
\]

The product-node change `(X,Y,z)=(xz,y,z)` has determinant `z`, as the root recorded. It is not permissible to discard that winding. The standard complex disc in the root's map has boundary `-e1`; reversing its orientation gives the prescribed `+e1`.

A second edge is particularly useful because it lies in the actual source-line graph. The Tate calculation has `P=2G`, with component valuation `p=6` at I8. The extending flat-frame heights on the first six intervals are

\[
 F_i=\max(6-i,0),\quad 0\le i<8,\qquad F_{i+8}=F_i-6.
\]

Consequently `(0,6)` and `(1,5)` are consecutive vertices of that graph. They form a diagonal edge of the chosen fan. One adjacent regular cone has ordered rays

\[
 v_0=(1,0,5),\quad v_1=(1,1,5),\quad v_2=(1,0,6),\qquad
 \det(v_0,v_1,v_2)=1.
\]

Its edge labels in the actual quotient are `(0,0)` and `(1,1)`. They are distinct. The entire 32-triangle quotient was checked with its 16 actual component labels; no fan replacement was made.

The translation taking these representatives down by `(0,6)` is **not** suppressed:

\[
 (0,-6)=9l_1-3l_2.
\]

On the actual source and line it includes the unit factors of the ninth first period and inverse third second period. In particular its source multiplier is `q_E^9 Q^{-3}`, of valuation zero, and need not equal one. The report keeps the unshifted graph edge, so no uncomputed endpoint phase is removed.

## 2. The exact line-coordinate sign and local product-node map

Let `W` be the physical flat coordinate of `M=O(P-O)`. The complete Tate input says that its first period factor is `P`. In the manuscript's short marking the scalar coordinate is

\[
 V=W^{-1}.
\]

This is the actual fibrewise map to the dual nonzero line: a nonzero vector `ell` is sent to the unique dual vector taking value one on `ell`. It carries a multiplier `kappa` to `kappa^{-1}`. Thus it accounts for the negative scalar valuations in `(8,-6)` and `(24,-16)`. It is not an unexplained sign change in a lattice table.

In the graph cone above, the dense torus characters are

\[
 q=xyz,\qquad Z=y,\qquad V=x^5y^5z^6.
\]

D.FI2 gives the extending flat-frame factor `q^6/Z` on the source interval from component zero to component one. Hence the actual extending line coefficient is

\[
 W_{\rm ext}=\frac{q^6}{ZV}=x.
\]

Together with the source node coordinates this gives the full map

\[
 (x,y,z)\longmapsto (X=xz,\;Y=y,\;W_{\rm ext}=x),
 \quad XY=q,
 \quad(x,y,z)=(W_{\rm ext},Y,X/W_{\rm ext}).
\]

It is defined on `x!=0`, exactly the open orbit of the selected double curve. Its complex Jacobian is **`-x`**. The nonconstant winding is retained.

The weights in this chart are

\[
 e_1=(-1,1,0),\quad\delta=(-1,0,1),\quad
 e_1-\delta=(0,1,-1).
\]

In `(X,Y,W_ext)`, delta acts only by inverse physical line multiplication; `e1-delta` is the source vanishing circle and fixes `W_ext`. At the first I1 site the supplied cocycle is zero, so its source vanishing vector is literally `e1`, and its line degree is zero. These are two different primitive meridians in the **same** marked boundary torus; their exterior areas both equal alpha:

\[
 (e_1-\delta)\wedge\delta=e_1\wedge\delta,
 \qquad\det\begin{pmatrix}1&1\\-1&0\end{pmatrix}=1.
\]

No equality of two filled manifolds is inferred from this determinant alone.

## 3. Exact two-node local model and its source/line collars

There is an explicit complex local model for these two meridians:

\[
 \mathcal Q=\{(a,b,c,d):ad-bc=1\}=SL_2(\mathbb C),\qquad f=ad.
\]

Its two critical curves are `a=d=0` and `b=c=0`, at `f=0,1`. On the dense locus put

\[
 Z=ab,\qquad V=f^6/a.
\]

At the cusp this extends by the actual graph chart

\[
 (x,y,z)=(1/b,ab,d),\quad q=f,
\]

so `W_ext=1/b`. At the other node put

\[
 X=-c/a,\quad Y=ab,\quad W=a/f^6,\quad XY=1-f.
\]

These are actual invertible local charts near the two compact core circles. For the actual base parameters `q_0=f c_0(f)` and `q_1=(1-f)c_1(f)`, with the existing nonzero units retained, the cusp chart becomes

\[
 (x,y,z)=(c_0^6/b,\;ab,\;c_0^{-5}d),
\]

and the finite-node `X` acquires the factor `c_1`. These formulas exhibit the parameter transport, rather than declaring the base parameters equal. The source-line transition on the dense overlap, before the displayed base unit `f^6`, is exactly

\[
 W_1=Z W_0.
\]

It has winding one around the source equator. This is the endpoint line shear that an identity boundary gluing would miss.

The two short actions are `e1:(a,b,c,d)->(a,sb,s^{-1}c,d)` and
`delta:(a,b,c,d)->(s^{-1}a,sb,s^{-1}c,sd)`. Delta is right multiplication by `diag(s^{-1},s)`. On the compact real form `SU2`, its action is free. The fibrewise torus collapses by `e1-delta` at zero and by `e1` at one. The resulting compact model is literally `SU2`, a three-sphere, with its Hopf circle action. Equivalently its two disc-bundle charts have the displayed unit line transition `W1=Z W0`; the usual explicit Hopf parametrizations give the same sphere.

**Current comparison boundary:** these statements are proved for this explicit local model and its specified actual endpoint charts. To identify its entire compact sphere in the received weighted OS45 manifold, the based middle collar must be written using the original point and line uniformization, including the actual nonzero period functions and the translation of origins. An arbitrary identity identification of the two endpoint tori is not recorded as a proof. The candidate map on that collar is exactly `(f,a,b,c,d)->[t(f),Z=ab,V=f^6/a]`; its endpoint units are the formulas above. The remaining verification is that the chosen analytically continued short coordinates are the received based coordinates at **both** ends, with all constant source/line phases retained. No existing source file has yet supplied an evaluated two-end phase table for this new collar.

## 4. A complete local framing calculation, with its scope

This calculation was made independently in the explicit model after the receiving reference-frame inputs had been read. It must not yet be labelled a global OS45 framing result.

Move the compact real form by left multiplication with

\[
 L_\epsilon=\begin{pmatrix}1&\epsilon\\0&1\end{pmatrix},\qquad\epsilon>0.
\]

Writing a point of `SU2` as `(alpha,beta;-bar beta,bar alpha)`, the moved entries are

\[
 a=\alpha-\epsilon\bar\beta,\quad b=\beta+\epsilon\bar\alpha,
 \quad c=-\bar\beta,\quad d=\bar\alpha.
\]

The moved sphere avoids both critical curves: at `a=d=0`, alpha vanishes and then a is nonzero; at `b=c=0`, beta vanishes and then b is nonzero. Left multiplication commutes with the delta right action.

Use the complex left-invariant Lie frame. Delta is the constant diagonal generator. On the remaining two left Lie coordinates `(u,v)`,

\[
 df=ac\,u+bd\,v.
\]

The toric `e1` field has left coordinate matrix

\[
 \begin{pmatrix}bc&bd\\-ac&-bc\end{pmatrix}.
\]

Subtracting its delta multiple gives the vertical column `(B,-A)`, where `A=ac,B=bd`. The vertical/horizontal comparison is therefore the literal unit Bott matrix with first column `(B,-A)/sqrt(|A|^2+|B|^2)`.

On the moved sphere,

\[
 A=-\alpha\bar\beta+\epsilon\bar\beta^2,
 \qquad B=\beta\bar\alpha+\epsilon\bar\alpha^2.
\]

For every positive epsilon this pair has no common zero. In variables `z1=bar alpha,z2=bar beta`, a common zero with both coordinates nonzero forces `z1=-epsilon^2 z1`; the coordinate-axis cases are also nonzero. The homotopy epsilon to infinity consequently identifies its normalized degree with that of `(z1^2,-z2^2)`. Simultaneous conjugation has positive real orientation in complex dimension two. The proper holomorphic squaring pair has four positive regular preimages. Thus the Bott comparison has **degree 4**, with the displayed conventions, in particular even degree.

The complex left-invariant frame restricts to a tangent Lie parallelization and its imaginary normal parallelization on `L_epsilon SU2`. The receiving D2.48/Kaplan parity formula gives the actual tangent-parallelization parity `1+b1(S3;F2)=1`. The local reference frame consequently also has parity **one**, because its degree-four change is even. A different second abstract vertical vector retaining delta changes it through `C semidirect C*`; the target line changes through `C*`. On this three-sphere those changes are nullhomotopic, so they do not alter the result.

Again, this is a fully computed local-model result. The actual based middle-collar identification is the remaining transport needed before attaching this parity to the OS45 odd class.

## 5. The critical-specialization obligation remains

The root's `D.OS8` coefficients are all even. Their half is an actual integer vector and maps to half the displayed regular-fibre vector. This proves the corresponding even-chain statement in the regular/core presentation only.

The complete critical cycle includes 48 cusp double curves and the four actual I1 transverse curves. Its replacement by the five regular-fibre preimages uses local specialization chains. For the new sphere, the relevant chains in the selected cusp and first I1 cap have not been put into transverse position with the displayed embedding. The other transported pieces also require compatible supports. Their intersection number, including the normal push-off dictated by the reference frame, is not supplied by the even core vector.

Accordingly no parity for the total integral link, and no value of the refined class, is asserted. The exact outstanding integer is the intersection of the chosen odd three-sphere with the sum of those actual specialization chains, added to the complete core-chain contribution. One must retain the degree-four local Bott comparison and the winding-one line clutch in making that calculation.

## 6. Discarded or unpromoted routes

The earlier horizontal-edge proposal would glue meridians `e1,e1` and has the local topological model `S2 x S1`. Its global based gluing and reference parity were not completed. It is retained as a tentative route, not a second established embedded representative. The diagonal source-line edge above has a different actual meridian; its determinant-one sphere model does not justify silently replacing the horizontal model.

No worldwide novelty claim, independent whole-D2.53 proof claim, or conditional classification theorem is made. The explicit new local calculation is preserved in `code/III_OS45_local_maps_08.py`, with stdout and the full exact output `III_OS45_local_maps_08.json`. Its checks establish the named identities and the local model only; they do not turn a matrix certificate into the missing global source/collar or linking comparison.
