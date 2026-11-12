# Retained-angle mathematical audit

## Verdict

The mathematical mechanism passes this adversarial audit. For the original marked source and quotient, the complete regular inverse image has the stable Lie-torus framing, hence represents the nonzero class `eta^2`. Using the already established fixed based diffeomorphism `X ≅ S^6`, stabilization identifies the exact class with `eta_4 composed with eta_5` in `pi_6(S^4)`.

The initial source had a real ordering defect in the last smoothing paragraph: its distance bound was calculated before a subsequently mentioned basepoint modification. Root repaired that order, and this worker reread the complete repaired paragraph. Section 8 below supplies the corrected argument independently. Root also inserted and this worker checked the exact constant positive target-coordinate frame change proved in Section 3. The three literal TeX defects and Hatcher locator are corrected in the reread source. No unresolved defect remains from this audit.

Repaired theorem source SHA256 at the final reread:
`7F4BBF295A3DD2958B21F3C09ECFE9E2C51231B64501E06704D58221607A8EED`.

This is an audit of the retained-angle proof and its stated dependencies, not a fresh audit of the entire global complex-threefold/sphere-recognition proof. No conclusion below silently supplies that global result anew.

## 1. Exact map and original marking — PASS

The canonical native descent proof uses the real marking

\[
\Pi=[Z\mid I_2],\qquad
\zeta=Z(s)u+k,\qquad (u,k)\in\mathbb R^2\oplus\mathbb R^2.
\]

The first two coordinates are exactly the coefficients of
`(widehat gamma, widehat u)`, and the last two are the coefficients of
`(widehat w, widehat delta)`. The original clean transcription also explicitly states this column order. The quotient by the latter lattice therefore is `[u]`, with no implicit conjugacy or index. Since

\[
\operatorname{Im}s=-\ell/(2\pi),\quad
R(t)=-2\pi\operatorname{Im}C(t),\quad
A(t)=\ell B_0+R(t),
\]

the equality `log|x|=A(t)u` follows directly by taking imaginary parts of `zeta`. The deck transformation `Psi_n` changes this logarithm by `A(t)n`, so `[A(t)^{-1}log|x|]` is exactly the canonical native map. The inequality

\[
\|A(t)\xi\|\ge (|\ell|-\|R(t)\|)\|\xi\|
\]

proves invertibility at the chosen sufficiently small regular value. It does not change the cutoff disc defining the original map.

The source's `q_2` agrees literally with canonical equations
`cusp-cone-A-definition`, `cusp-cone-q2`, and `cusp-cone-q2-formula`:

\[
q_2:X\longrightarrow\operatorname{Susp}(S^1\times\overline T^2),
\qquad x\longmapsto[|t|,t/|t|,[u]],
\]

with `W` sent to the first suspension vertex and the exterior sent to the second. The two vertices are distinct in this unreduced suspension. The subsequent `p_3` identifies both of them, and the entire cylinder above `K^(2)`, with the single basepoint of the reduced suspension. Thus

\[
p_3:\mathcal A\longrightarrow\Sigma_r(T^3/K^{(2)})\cong S^4
\]

is well-defined and based. The product CW structure on `T^3` has precisely one open three-cell; collapsing its complete two-skeleton leaves `D^3/partial D^3`. The cotangent formulas in the source give a proper diffeomorphism from this open cell to `R^3`, since approaching any boundary face forces one coordinate to diverge. Their one-point extension is the required sphere identification. The same argument applies to the open four-cell after reduced suspension. Endpoint continuity follows from the quotient topology, not from an asserted smooth extension across the collapsed set.

## 2. Entire inverse image and injective chart — PASS

Retain exactly

\[
u_0=(-1/4,1/4)^T,\quad B_0u_0=(1/4,1/4)^T,
\quad t_0=r_0e^{i\pi},\quad \ell_0=\log r_0.
\]

The target value lies inside the open four-cell, so every inverse point has `t=t_0` and `[u]=[u_0]`; conversely these conditions suffice. A lift with `u=u_0+n` is taken by `Psi_{-n}` to the exact lift `u_0`. If two such lifts are equivalent, the intervening `Psi_n` changes `u` by `n`, forcing `n=0`. This proves that the selected representatives exhaust the fibre and have no residual identifications.

The toric characters `(t/(x_1x_2),x_1,x_2)` are dual to the original ordered primitive rays `(0,0,1),(1,0,1),(0,1,1)`. Their product is exactly `t`. With

\[
h_j(t)=\exp(-2\pi i(C(t)u_0)_j),
\]

the source's coordinate change `F` preserves that product, and its explicitly displayed reciprocal-unit inverse is evaluated at the identical `t`. Hence it is a genuine biholomorphic coordinate change, including at the origin. Since `log|h|=-R(t)u_0`, the inverse fibre has

\[
|w_1|=|w_2|=r_0^{1/4},\quad |w_0|=r_0^{1/2},
\quad \arg w_0=\pi-a-b.
\]

The two independent angles `a,b` have their original period `2pi`. The coordinates `w_1,w_2` recover these angles, so the displayed parametrization is an embedding of the native torus, not a cover.

Free proper discontinuity at the original toric origin supplies an injective quotient neighborhood. Take a `w`-ball with closure inside it after applying `F`. All three radii tend uniformly to zero, so this *entire* torus lies in that ball for sufficiently small `r_0`. No inverse point remains elsewhere in `X`, because the selected representatives were already shown to be complete.

## 3. Differential, actual normal frame, and target-coordinate change — PASS

In the notation of the source,

\[
v=\ell B_0u+R(t)(u-u_0),\qquad
u=u_0+A(t)^{-1}(v-\ell p_0).
\]

Differentiating gives

\[
du=-A^{-1}(dA)A^{-1}(v-\ell p_0)
   +A^{-1}(dv-p_0d\ell).
\]

The first term is exactly zero on the inverse torus. This justifies the absence of all derivatives of the retained period functions from the restricted differential. On the displayed lifts one calculates:

- `N_ell` has `dell=1`, `dphi=0`, and `dv=p_0`, hence `du=0`.
- `N_phi=Q_0` has `dphi=1`, `dell=dv=0`, hence `du=0`.
- `N_i` has `dell=dphi=0` and `dv=A_0 e_i`, hence `du=e_i`.
- `T_a=-Q_0+Q_1` and `T_b=-Q_0+Q_2` have every target differential zero.

Thus the derivative table is exact, and the four classes in `TX|_M/TM` are a normal framing. An orthogonal projection changes a lift by a tangent vector; it does not change these normal classes. The path replacing a complement vector `N` by `N-s proj_TM(N)` preserves its quotient class for all `s`, so the choice of complement has no framing obstruction.

The sphere target's cotangent open-cell coordinates are not literally `(ell,phi,u_1,u_2)`. At the chosen value their differential is the positive diagonal matrix

\[
K=\operatorname{diag}\left(
 \frac{\pi r_0}{\epsilon}\csc^2\frac{\pi r_0}{\epsilon},
 \frac12,2\pi,2\pi\right)
\]

times `d(ell,phi,u_1,u_2)`. Here the open-cell lift of the first quotient coordinate is `3/4`, differing from `-1/4` by exactly one, so its derivative is unchanged. The literal derivative-dual frame for these cotangent coordinates therefore is `N K^{-1}`. The path

\[
N\bigl((1-s)K^{-1}+sI_4\bigr),\qquad 0\le s\le1,
\]

is through normal frames because every interpolating diagonal entry is positive. Alternatively one can declare `(ell,phi,u_1,u_2)` themselves to be the target coordinates near the value; their transition is a local orientation-preserving diffeomorphism. Either method supplies the exact omitted coordinate comparison. This is an explicitness repair, not a counterexample to the theorem.

## 4. Orientation and the full comparison matrix — PASS

In the real complex-coordinate frame, each ordered pair `(L_j,Q_j)` has determinant `|w_j|^2`. Passing from the interleaved order to the three radial followed by three angular directions has sign `-1`. Moving `N_phi` past `N_1,N_2` has sign `+1`. The angular block is upper triangular with diagonal `(1,1,1)`. Adding the last two rows to the first in the radial block gives first row `(1,0,0)` and lower-right block `A_0`. Therefore

\[
\det(N_\ell,N_\phi,N_1,N_2,T_a,T_b)
  =-\det(A_0)r_0^2.
\]

The path `ell_0 B_0+sR(t_0)` is invertible by the already proved norm bound. Its initial determinant is `ell_0^2>0`, so `det(A_0)>0`. The source correctly uses `(-T_a,T_b)` as its induced positive tangent frame. The positive target-coordinate factor above preserves this sign.

All coefficients of this full frame are constant on the fibre, because `t=t_0`. Every coordinate radial and angular vector varies by

\[
D(a,b)=\operatorname{diag}(e^{-i(a+b)},e^{ia},e^{ib}).
\]

Hence the exact full frame is `D(a,b)G_0` for one constant `G_0 in GL^+(6,R)`. There is no residual matrix depending on derivatives of `C`.

## 5. Periodic contraction in SU(3) — PASS

For real `s_v=sin(pi v/2)` and `c_v=cos(pi v/2)`, the source matrix

\[
Q_v(\theta)=
\begin{pmatrix}s_ve^{-i\theta}&-c_v\\c_v&s_ve^{i\theta}\end{pmatrix}
\]

has unit columns, zero cross inner product, and determinant `s_v^2+c_v^2=1`. Thus `K_v(theta)=Q_v(theta)Q_v(0)^*` is in `SU(2)` for every parameter. Direct endpoint evaluation gives `K_0=I`, `K_1(theta)=diag(e^{-i theta},e^{i theta})`, and `K_v(0)=I`. Every entry is periodic in `theta` with period `2pi`.

The ordered product of its embeddings in the `(0,1)` and `(0,2)` coordinate planes is a continuous `SU(3)` map on `[0,1] times T^2`. The factors need not commute in the interior of the homotopy; multiplication is nevertheless continuous. At `v=1` both are diagonal and their product is exactly `D(a,b)`. At `v=0` the product is `I`. Both phase seams agree for all `v`. This proves a full two-variable contraction, not merely independent contractions of the generating loops.

Multiplying this contraction by `G_0` contracts the full frame comparison to a constant. Constant positive matrices are path connected to the identity by polar/Gram–Schmidt deformation and rotations. Consequently the induced stable tangent framing is the stable framing of the intrinsic Lie frame `(-partial_a,partial_b)`.

## 6. Spin structure and Arf obstruction — PASS

The stable Lie frame gives the trivial, disconnected spin double cover along either coordinate circle: its oriented tangent and its oriented normal inside the surface are constant in that frame. By contrast, the outward normal and tangent of the boundary of a framed disk make one full rotation, whose lift in `Spin(2)` changes sign. Thus the disk-induced spin circle is the connected cover and the two Lie circles are nonbounding.

Writing `e,f` for the original two primitive circle classes gives

\[
e\cdot f=1\pmod2,\qquad q(e)=q(f)=1,
\qquad q(xe+yf)=x+xy+y,
\quad \operatorname{Arf}(M)=1.
\]

The replacement of `partial_a` by `-partial_a` reverses orientation but is constant; it introduces no loop of frames. Both induced spin circle covers and every displayed mod-two value remain unchanged. In particular, the diagonal circle has value `1`, as follows both from the quadratic formula and its constant tangent and normal in the Lie frame.

The handle proof of bordism invariance has the correct meridian: in a three-dimensional index-one handle `D^1 times D^2`, the new boundary meridian is the boundary of `{0} times D^2`. Its normal inside the boundary agrees, up to a constant sign, with the `D^1` normal of that cocore disk. Hence its induced spin circle is bounding and its quadratic value is zero. The added hyperbolic pair contributes zero to Arf. A handle joining components adds the forms orthogonally, index-two handles reverse index-one handles, and sphere creation/removal contributes zero. Thus an oriented spin three-manifold has boundary of total Arf zero. Forgetting a stable framing supplies precisely such a spin structure, so the computed torus cannot be a stably framed boundary.

For the standard background correspondence used here, the author-hosted [Debray–Gunningham paper](https://adebray.github.io/papers/arf_brown.pdf), Theorem 3.2, Remark 3.3, Theorem 3.6 and Example 3.8, confirms the quadratic-refinement convention, spin bordism invariant, and the Lie torus value used in this audit.

## 7. Hopf identification, stabilization, and global dependency — PASS

On the complex Hopf fibre `(z_1,z_2)=(e^{ia},0)`, the target coordinate `z_2/z_1` has derivative-dual horizontal vectors `(0,e^{ia})` and `(0,i e^{ia})`. The tangent is `(i e^{ia},0)` and the outward radial vector is `(e^{ia},0)`. Relative to their values at `a=0`, the full frame varies by `diag(e^{ia},e^{ia})` on `C^2`.

The source's fixed real involution `J(z_1,z_2)=(z_1,conjugate(z_2))` conjugates this loop to `diag(e^{ia},e^{-ia})=K_1(-a)`. Thus `J K_v(-a) J` is an explicit real-linear contraction of the original full frame loop. This establishes that the Hopf class induces the stable Lie-circle framing. Product tubular coordinates identify the smash of the two Pontryagin collapse maps with the product framed manifold; therefore the Lie torus is the product `eta^2`. Its nonzero Arf invariant already proved this stable product is nonzero.

The derivative-framed inverse image in a chart determines an abstract stable framed torus using that chart's ambient trivialization. To identify it with stabilization of the global `H`, use the source's already fixed based diffeomorphism `d:X to S^6` and the standard stable trivialization `TS^6 plus R ≅ R^7`. On the contractible `w`-ball this differs from the coordinate trivialization plus a line by a map to `GL(7,R)` extending over that entire ball. Contraction of the ball contracts this comparison to a constant. Thus it contributes no varying stable framing on `M`; a possible orientation sign acts by negation, which is trivial on this order-two class.

This is the exact point where the existing global sphere-recognition theorem is used. Merely placing a normally framed torus in one ball of an arbitrary six-manifold would not by itself identify `[X,S^4]` with `pi_6(S^4)`.

Freudenthal gives an isomorphism when `i<2n-1`. Here `i=n+2`, so the inequality holds for every `n>=4`, including `6<7` at the initial step. Consequently

\[
\pi_6(S^4)\xrightarrow{\;E^\infty\;}\pi_2^{\mathrm S}
\]

is an isomorphism. The map `eta_4 composed with eta_5:S^6 to S^4` stabilizes to `eta^2`, proving the asserted exact equality. The stable two-stem is `Z/2`, so the source's orientation signs do not affect it. The [Hatcher text](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf) states the used suspension range in Corollary 4.24 on printed page 360; the stable-group discussion/table is on printed pages 384–385. A citation that assigns Corollary 4.24 to page 339 should be corrected; page 339 is the opening unstable group table.

## 8. Required smoothing order repair — PROVED REPAIR

The initial text calculates the positive distance for `H`, then says that one may first modify it near the basepoint. That modification is harmless but can change the calculated distance. The following is the complete correct order.

Choose a target coordinate neighborhood of the basepoint whose coordinate image is a ball, contains the origin at the basepoint, and excludes `y_0`. By continuity take a source neighborhood `U` of `x_base` mapped inside it, with closure disjoint from `M`. Choose a smooth bump `beta` supported in `U` and equal to one on a smaller basepoint neighborhood. In these target coordinates apply multiplication by `1-s beta(x)`. It stays in the ball, remains based, is fixed off `U` and near `M`, and introduces no preimage of `y_0`. Denote its endpoint by `H_b`; it is constant on a basepoint neighborhood.

Next choose a closed tubular neighborhood `C` of the entire `M`, lying in the smooth submersion region, with `M subset int(C)` and disjoint from the basepoint neighborhood. Compactness now gives

\[
d_0=\min_{x\in X\setminus\operatorname{int}C}
 d(H_b(x),y_0)>0.
\]

Apply relative smooth approximation to `H_b`, fixed on the whole closed `C` and a smaller closed basepoint neighborhood, with error below `d_0/2` on `X minus int(C)` and below a uniform injectivity radius on the target. The input is already smooth on open neighborhoods of both fixed sets, as required. The smooth map has exactly the same inverse image and derivative on `C`, and has no inverse image outside because the distance remains above `d_0/2`. There is no intervening region left uncontrolled. Short target geodesics give a based homotopy to `H_b`. Pontryagin–Thom is therefore applicable to exactly the derivative-framed torus already calculated.

## 9. Consequences and limits checked

Postcomposition gives the exact function

\[
(p_3)_*:[X,\mathcal A]_*\longrightarrow[X,S^4]_*,
\qquad [q_2]\longmapsto[H].
\]

The nonzero value proves that `q_2` is not based null-homotopic. The source correctly does not infer the complete class of `q_2` in its richer target, or any complete class of its smash powers. The original angle-forgetting sphere map has a different target projection and a three-dimensional inverse torus. Its proven nullity neither contradicts nor is used to prove this retained-angle result. The two projections can discard different components of the same conical-target homotopy class.

No hidden obstruction was found in the complete-fibre argument, normal-to-tangent conversion, periodic contraction, spin calculation, or stable-to-unstable identification. The conclusion is justified by the now-repaired proof and the already recorded global source theorem. Root retains ownership of canonical integration and propagation of mathematical status.

## 10. Immediate exact quotient detected by the original q_2

Let `d:S^6 to X` be the fixed based diffeomorphism and put

\[
\alpha=[q_2\circ d]\in\pi_6(\mathcal A,v_0).
\]

Postcomposition by the fixed based `p_3` is a group homomorphism

\[
\varepsilon=(p_3)_*:
\pi_6(\mathcal A,v_0)\longrightarrow
\pi_6(S^4,*)\cong\mathbb Z/2.
\]

Indeed, the group operation is the pinch sum on the source sphere, and postcomposition distributes over that same pinch sum. The theorem gives `epsilon(alpha)=eta_4 eta_5`, the nonzero element of the target. Thus `epsilon` is surjective, and the exact first-isomorphism identification is

\[
\pi_6(\mathcal A,v_0)/\ker\varepsilon
 \xrightarrow{\;[\beta]\mapsto\varepsilon(\beta)\;}
\mathbb Z/2.
\]

This quotient sends the coset of the *original* `q_2` to its nonzero element. For every integer `n`,

\[
\varepsilon(n\alpha)=(n\bmod2)\,\eta_4\eta_5.
\]

Hence every odd multiple of `alpha` is nonzero. If `alpha` has finite order, that order is even: applying `epsilon` to `m alpha=0` forces `m=0 mod 2`. The alternatives left by this calculation are infinite order or an even finite order. Neither a precise order of two nor a splitting of the quotient map is inferred. This immediate corollary is stronger than bare nonnullity and requires no computation of any smash power.
