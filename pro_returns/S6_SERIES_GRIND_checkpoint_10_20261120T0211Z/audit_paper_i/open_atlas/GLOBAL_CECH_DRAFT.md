# Explicit Čech construction on the original atlas — receiving draft for independent review

**Status at writing:** the displayed local factors and connection identities have fresh exact certificates. This document supplies the complete proposed global construction for review. It is not yet an instruction to change `inv:C3.8` to proved. In particular, the exact interpretation of the evaluated, countable refinement of the supplied common atlas must be reviewed together with the formula, rather than silently replacing the requested coefficient atlas by an existence assertion.

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family. These are new calculations after reading the earlier operator argument. They are not a statement-first re-proof. No historical checker is imported.

## 0. Actual input and refinement maps

Keep the original marked threefold `X`, its original middle torus family, the two original free affine root quotients, the original toric cusp fan and all the supplied holomorphic unit factors. Keep the original disjoint special-fibre discs and their overlap collars with the middle region. The base cover consists of the middle region `V_*` and the three discs `V_0,V_1,V_2`. The three discs are pairwise disjoint; their overlaps with `V_*` are annuli. The only base refinements used below are inclusions of smaller coordinate domains in these original pieces, with identity map to `X`.

Use all the original uniformizing coordinate domains as an étale atlas: ordinary torus covers in `(t,zeta_1,zeta_2)`, finite root covers in `(s,zeta_1,zeta_2)`, and all the original toric affine charts of the periodic cusp fan. The finite quotients are free on total spaces. The toric period quotient is free and properly discontinuous on its original domain. Thus each of these charts maps locally biholomorphically to `X`, including over the special fibres. An atlas chart need not be globally injective; every overlap below is a fibre product of these actual étale maps. This keeps every possible deck branch.

The finite affine data are exactly
\[
A_1=\begin{pmatrix}1&0&0&0\\6&0&1&0\\-6&-1&-1&0\\-2&1&0&1\end{pmatrix},
\quad A_2=\begin{pmatrix}1&0&0&0\\0&0&-1&0\\-6&1&0&0\\3&0&1&1\end{pmatrix},
\]
\[
v_1=(1,2,-4,0)^t,\quad v_2=(-1,-3,3,0)^t,
\qquad m_1=3,\ m_2=4.
\]
The source order is `(gamma,u,w,delta)`, with period matrix
\[
 \Pi=[Z\mid I_2],\quad
 Z=\begin{pmatrix}6\mu&\tau\\\beta&\mu\end{pmatrix},
 \quad T=\begin{pmatrix}\tau&6\mu\\\mu&\beta\end{pmatrix},
 \quad D=\operatorname{diag}(1,6),\quad
 K=\begin{pmatrix}0&6\\1&0\end{pmatrix}.
\]
Here `beta=beta_part+c` includes the full original parameter. If `lambda=(n_gamma,n_u,m_w,m_delta)`, put `n=(n_gamma,n_u)`, and if `v` is an affine vector put `v_q=(v_u,v_gamma)` and `v_p=(v_w,v_delta)`. These are explicit permutation maps, not a change of unnamed convention.

## 1. The regular line and its twelfth power

On a simply connected regular base chart use the line factors
\[
 a_\lambda(\zeta)
 =\exp\left(2\pi i\left[n^tK\zeta+
              \tfrac12 n^tKZn\right]\right).
 \tag{1}
\]
The logarithm defect for composition by another lattice vector is an integer. This follows from the symmetry of `KZ`; explicitly it is `n^t K m'`. Thus (1) defines an actual holomorphic line, denoted `L_eta`, on that local torus family. With `Y=Im T`, `q_B=Y^{-1}Im zeta`, the metric coefficient
\[
 h=\exp\varphi,\qquad \varphi=2\pi q_B^tDYq_B
\]
is compatible with these factors. Its Chern form, with the supplied convention `c_1=iF/(2pi)` and `F=bar partial partial log h`, is
\[
 Q_{\rm sf}=-\frac{i}{2\pi}\partial\bar\partial\varphi
 =-\frac i2\bigl(d\zeta-dTq_B\bigr)^t
 DY^{-1}\wedge\overline{\bigl(d\zeta-dTq_B\bigr)}.
 \tag{2}
\]
The exact real inverse of `zeta=p_B+Tq_B` identifies (2) with
`dr_u wedge dr_w+6dr_gamma wedge dr_delta`. Its restriction is the original `eta`, including its square integral `-12`. This sign is checked by the full alternating-matrix pullback in `exact_regular_atlas.py`.

For the two linear monodromies, period covariance gives
\[
\begin{array}{c|ccc|c}
 &\tau_g&\mu_g&\beta_g&R_g\\\hline
1&1-1/\tau&(1-\mu)/\tau&\beta-6(\mu-1)^2/\tau+2&
 \left(\begin{smallmatrix}-1/\tau&0\\(1-\mu)/\tau&1\end{smallmatrix}\right)\\
2&-1/\tau&1+\mu/\tau&\beta-6\mu^2/\tau-3&
 \left(\begin{smallmatrix}1/\tau&0\\-\mu/\tau&1\end{smallmatrix}\right).
\end{array}
\tag{3}
\]
The exact Gaussian comparison is `F_g(zeta)=-zeta_1^2/(2tau)` for both generators. For the four original lattice generators the differences
\[
 \log a_{A_j\lambda}(R_j\zeta)/(2\pi i)
 -\log a_\lambda(\zeta)/(2\pi i)
 -F_j(\zeta+\Pi\lambda)+F_j(\zeta)
\]
are respectively `(24,0,1/2,0)` and `(-9,0,0,0)`. Since the ratio is a character, checking these four generators checks every lattice vector. Multiplying by 12 makes every defect integral. The line `L_*=L_eta^12` therefore has the exact linear lift
\[
 (\zeta,v)\longmapsto(R_j\zeta,
              e^{2\pi i\,12F_j(\zeta)}v).
 \tag{4}
\]
The Gaussian sums vanish on the original order-three and order-four relations. For the cusp product, applying generator 2 and then generator 1 gives `tau->tau+1`, `mu->mu`, `beta->beta-1`, `zeta->zeta`, and Gaussian sum zero. Thus (4) descends on the original middle quotient with trivial fibre multiplier for that logarithm turn. No new theta characteristic is substituted.

## 2. Both actual finite affine quotients

On the root cover set `b_j=v_j/m_j` in the original Betti order. The actual affine generator is
\[
 g_j(s,\zeta)=(e^{-2\pi i/m_j}s,
               R_j(s)\zeta+\Pi(g_js)b_j).
 \tag{5}
\]
For a rational vector `b` define `a_b` by the same polynomial logarithm as (1); the twelfth power is compatible with all integral lattice maps because `12b` is integral. A lift of (5) to `L_eta^12` is
\[
 k_j(s,\zeta)=\exp\left(2\pi i
 \left[12F_j(\zeta)+12\log a_{b_j}(R_j\zeta)/(2\pi i)
                 +\kappa_j\right]\right),
 \quad \kappa_1=32/3,\quad\kappa_2=81/8.
 \tag{6}
\]
Here `a_b` uses the target period `Z(g_js)`. Literal composition of (5) gives `g_j^{m_j}(zeta)=zeta+Pi v_j`. Literal composition of the uncorrected line lift differs from `a_{v_j}^{12}` by logarithms `-32` and `-81/2`; adding the stated constants in (6) cancels these differences exactly. Therefore the corrected lift has precisely the original lattice action as its power. It defines an honest line `L_j` on the full free affine quotient. Its fibre Chern class is `12eta`.

All functions in (3) and (6) are holomorphic through the root centre: `tau` lies in the upper half-plane, the original period functions are holomorphic in `s`, and the exponential factors never vanish. The phase corrections are constants; they do not alter a local differential form. This verifies extension over both full multiple fibres, rather than replacing them by reduced fibres.

## 3. A cusp line with every extending unit retained

In the actual cusp coordinates
\[
 q=e^{2\pi is},\qquad Z=sB+C(q),\qquad
 B=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
 \quad C(q)=\begin{pmatrix}6\mu&\tau-s\\\beta+s&\mu\end{pmatrix},
 \tag{7}
\]
the matrix `C` is the original holomorphic bounded matrix; it contains the parameter and all nonconstant units. The period `n` acts by
\[
 x\longmapsto q^{Bn}\exp(2\pi i Cn)x.
\]
Use the line factor
\[
 A_n=x^{K^tn}q^{h(n)}\exp(\pi i n^tKCn),
 \qquad h(n)=-3n_\gamma^2+n_u(n_u-1)/2.
 \tag{8}
\]
Both `KB=diag(-6,1)` and `KC` are symmetric. Direct multiplication proves the exact cocycle law in (8), including its unit. The exponent of `q` is integral. For a fixed punctured fibre, the ratio of (8) to (1) is `q^{-n_u/2}`, independent of `x`, so its fibre Chern class is still `eta`. For the twelfth powers this ratio is the single-valued factor `q^{-6n_u}`.

On the original periodic unit-square triangulation interpolate the integer values
\[
 L(i,j)=i(i-1)/2-3j^2.
\]
Both triangles in the square with lower corner `(i,j)` have the same affine interpolation
\[
 m_{ij}=(i,-6j-3),\qquad
 l_{ij}=-i(i+1)/2+3j(j+1),\qquad
 f_{ij}=x^{m_{ij}}q^{l_{ij}}.
 \tag{9}
\]
These are Cartier frames, interpreted as formal local frames of a line, not as nonvanishing functions on the whole chart. Adjacent-square frame ratios are the actual monomials `x_1 q^{-i-1}` and `x_2^{-6}q^{6(j+1)}`; they are units on the corresponding toric overlap, since their exponents vanish on its common face. The diagonal inside a square has ratio 1. Reciprocals give the inverse maps.

For `v=Bn`, the identity
\[
 L(u+v)-L(u)=(K^tn)\cdot u+h(n)
\]
implies that the action on frame coordinate `w=z/f_{ij}` is multiplication by exactly
\[
 U_{n,ij}(q)=\exp\left(\pi i n^tKC(q)n
       -2\pi i\,m_{i+v_1,j+v_2}^tC(q)n\right).
 \tag{10}
\]
Every `x`- and `q`-power has cancelled. These are holomorphic nonzero units at `q=0`, and their full cocycle is verified in the fresh program. The original properly discontinuous toric action therefore descends this line over the actual cusp filling. Its twelfth power is `L_0`. The exact ratio to the middle line on the punctured cusp is `q^{-6n_u}`. No positivity or projectivity of this line is required.

## 4. Exact connection equation and invertibility locus

For a relative degree-zero line whose normalized lattice factors on a marked torus chart are
\[
 1\quad\text{on the real periods},\qquad
 \exp(2\pi i n^tl(t))\quad\text{on the columns of }T,
\]
the one-form `A=a(t)^t dzeta`, with
\[
 T'(t)^t a(t)=-2\pi i l'(t),\qquad
 (T'^t)^{-1}=\frac1{\tau'\beta'-6\mu'^2}
 \begin{pmatrix}\beta'&-\mu'\\-6\mu'&\tau'\end{pmatrix},
 \tag{11}
\]
satisfies the exact line-connection transformation. Indeed translating `zeta` by `Tn` adds `a^tT'n dt=-dlog factor`.

Every inverse in this construction is used only on one of the three annuli, after pullback to the specified root or logarithm chart. These annuli omit all three special base points. Statement `inv:A2.1` gives
`6mu_z^2-tau_z beta_z=tau_z^2 E4(tau)^2/E6(tau)`, with the apparent poles removed, and establishes its exact zero set: order two at the order-three point and order zero at the order-four point, with no other zeros on the regular locus. A change between local base coordinates multiplies the determinant by the square of its nonzero derivative. Thus `det T'` is nonzero at every point of every annular region used here. No inverse is evaluated at a root centre or at `q=0`. In the cusp coordinate its leading term is `1/(4pi^2 q^2)`, consistent with (7).

The connection is holomorphic. It is not assumed flat: its curvature can contain the nonzero `(2,0)` term `a'(t)^t dt wedge dzeta`. This is exactly why the construction below does not glue the local lines to a global line with fibre Chern class `12eta`.

## 5. The cusp annular connection

For `F_0=L_0 tensor L_*^{-1}`, its normalized factors are `q^{-6n_u}`. In the reordered `T` basis `l=(-6 log(q)/(2pi i),0)`. Hence an actual connection is
\[
 A_0=a_0(q)^t d\zeta,\qquad
 a_0(q)=\frac6q(T'^t)^{-1}\binom10
       =\frac{6}{q(\tau'\beta'-6\mu'^2)}
          \binom{\beta'}{-6\mu'}.
 \tag{12}
\]
It is single-valued on this annulus: the logarithm turn changes `T` by `diag(1,-1)` and leaves `T'` and `zeta` unchanged. Equation (11) is exactly its lattice transformation. In the actual cusp frame `f_{ij}^{12}` the connection is `A_0+12dlog f_{ij}`. Its period-unit frame transformations are precisely (10), not truncated units.

## 6. Both finite annular connections, including every logarithm turn

Write the original collar map from the finite root chart to the middle chart as
\[
 H(s,\zeta)=(s,\zeta+\sigma(s)),\qquad
 \sigma=h(s)\Pi(s)v_j,qquad
 h=\frac{\log s}{2\pi i}.
 \tag{13}
\]
This is the supplied map: `h(g_js)=h(s)-1/m_j`, `A_jv_j=v_j`, and (5) give the exact square `H g_aff=g_lin H`. Its inverse subtracts the entire `sigma`.

For the line `F=H^*L_* tensor L_j^{-1}`, the lattice factors are
\[
 \exp(2\pi i\,12 n_T^tD\sigma),
\]
where `n_T=(n_u,n_gamma)`. Define
\[
 S(s)=v_q^tD\Pi(s)v_j,
\]
\[
 A=a(s)^t d\zeta-12\pi i\,d\bigl(h(s)^2S(s)\bigr),
 \qquad a=-24\pi i(T'^t)^{-1}D\sigma'.
 \tag{14}
\]
The last differential is a base one-form. Equation (11) proves lattice descent. For an integer logarithm turn `h->h+k`, the middle argument changes by `kPi v_j` and the frame changes by `a_{kv_j}(zeta+sigma)^{12}`. The exact vertical change in (14) is `-24pi i k Dv_q`. Its base change is
\[
 -12\pi i\,d\bigl((2kh+k^2)S\bigr)
 =-d\log a_{kv_j}(\zeta+\sigma)^{12}
   +24\pi i k\,v_q^tD\,d\zeta.
 \tag{15}
\]
Together these give exactly the required `-dlog` of that full frame map. Thus (14) is already a holomorphic connection on the whole punctured root-chart line, not merely on a chosen slit.

The remaining finite cyclic descent is explicit. Its line multiplier is
\[
 k_F(s,\zeta)=
 \frac{\exp(2\pi i\,12F_j(\zeta+\sigma))}{k_j(s,\zeta)},
 \tag{16}
\]
with the actual phase in (6). Let `k_F^{(r)}` be its product over the first `r` iterates of the actual affine map (5). Then
\[
 A^{\rm inv}=\frac1{m_j}\sum_{r=0}^{m_j-1}
       \left((g_j^r)^*A+d\log k_F^{(r)}\right).
 \tag{17}
\]
Every term is a connection on this same line. The exact order relation already proved makes cyclic permutation of the summands valid; (17) is invariant and descends to the original annulus. This is a finite sum of known functions and their derivatives. It uses neither an unspecified Cousin solution nor a Green operator. For the consistent ratio `F_j=L_j tensor L_*^{-1}`, use its dual connection `-A^{inv}`. This tensor-dual map fixes the sign in the next step.

## 7. A global holomorphic one-form Čech cocycle, with no global line glued

Refine the original étale charts only enough that each belongs to one of the four base pieces and has one of the explicit line frames above. On a same-piece overlap, write the actual line-coordinate map as `v_b=g_{ba}v_a` and set
\[
 c_{ab}=\frac{i}{2\pi}\,d\log g_{ba}.
 \tag{18}
\]
This fixes the Chern sign: a Hermitian connection satisfies `A_a-A_b=dlog g_ba`, so `(i/2pi)bar partial A` has precisely this Čech class and equals (2) on a regular chart.

On an overlap from a middle chart `a` to a special chart `b`, use the connection of `F_j=L_j tensor L_*^{-1}` in the two named frames and put
\[
 c_{ab}=-\frac{i}{2\pi}A_{F_j,(a,b)},\qquad c_{ba}=-c_{ab}.
 \tag{19}
\]
All its coefficients are given by (12), or by the negative of (17), with the explicit changes of frame. On a triple with two middle charts, the ratio frame in `F_j` changes by the inverse middle transition, so its connection changes by `+dlog g_*`; equation (19) makes the Čech sum zero. On a triple with two special charts it changes by the special transition, so its connection changes by `-dlog g_j`; again the sum is zero. The three special base pieces do not intersect each other. These are all the possibilities. Thus `c_ab+c_bc=c_ac` on every component of every actual overlap.

This construction glues a cocycle with values in the sheaf of holomorphic one-forms. It does not supply cross-piece nonzero holomorphic functions with those logarithmic derivatives; the connections in (19) are not assumed closed. No global line with nonzero fibre Chern class is being asserted.

## 8. A specified partition with evaluated weights, including noninjective chart maps

Here is one deterministic smooth refinement and the literal coefficient formula. In every original uniformizing coordinate chart, enumerate all closed rational Euclidean balls `B(c,R)` compactly contained in its domain, using rational real and imaginary coordinates and positive rational `R`. Order the combined list by integer height, bounding both the chart index and all numerators and denominators by that height, then by the original piece/chart index, and then lexicographically; remove duplicates. Each height block is finite. Cusp charts have their original integer cone labels enumerated by increasing max(|i|,|j|) and then lexicographically; any additional original branch charts are enumerated by their finite deck words. This is a fixed countable refinement of the given atlas; its map to `X` is always the original chart map, restricted to that ball. No additional manifold or unspecified gauge is introduced.

Put
\[
 E(t)=\begin{cases}e^{-1/t}&t>0,\\0&t\le0,\end{cases}
 \quad\chi(t)=\frac{E(t)}{E(t)+E(1-t)}.
\]
For the `n`th ball, with coordinate `u`, define the compactly supported smooth function
\[
 b_n(u)=\chi\left(\frac{R_n^2-\|u-c_n\|^2}{3R_n^2/4}\right).
 \tag{20}
\]
It is one on the closed ball of radius `R_n/2` and zero outside the radius-`R_n` ball. For the actual étale map `pi_n`, define
\[
 S_n(x)=\sum_{u\in\pi_n^{-1}(x)}b_n(u),\qquad
 P_n(x)=\prod_{k<n}\bigl(1-\chi(2S_k(x))\bigr),
\]
\[
 w_n(u)=P_n(\pi_nu)\,
        \frac{\chi(2S_n(\pi_nu))}{S_n(\pi_nu)}\,b_n(u),
 \tag{21}
\]
where the quotient is assigned its smooth value zero at `S_n=0`. Its smoothness follows from the infinite-order zero of `chi(2s)` at `s=0`.

Each sum defining `S_n` is locally a finite sum: the support of `b_n` is compact and an étale map has discrete fibres. The extension across its support boundary is smooth because (20) is flat there. Every point has a lift in an inner rational ball, so some `S_N` is at least one on a neighbourhood. The corresponding factor `1-chi(2S_N)` is identically zero there. Consequently the entire family of nonzero weights is locally finite, even though the initial ball enumeration need not be locally finite. Telescoping the finite product gives
\[
 \sum_n\sum_{u\in\pi_n^{-1}(x)}w_n(u)=1.
 \tag{22}
\]
All quantities in (20)–(22) are explicit elementary functions of the actual chart coordinates and the original overlap maps. These are finite sums at every point, not formal elliptic inverses.

In a local chart `a`, let `c_{a,n}(x,u)` be (18) or (19) on the indicated component of the fibre product. Define
\[
 B_a=\sum_n\sum_{u\in\pi_n^{-1}(x)}w_n(u)c_{a,n}(x,u),
 \qquad Q=\frac1{12}\bar\partial B_a.
 \tag{23}
\]
Equation (22) and the cocycle identity give `B_a-B_b=c_ab`. Since `c_ab` is holomorphic, the forms in (23) agree exactly on every overlap and are `bar partial` closed. If `c_{a,n}=sum_k c_{a,n,k}dz_k`, the literal coefficient is
\[
 Q_{k\bar l}=-\frac1{12}
       \sum_n\sum_{u\in\pi_n^{-1}(x)}
              c_{a,n,k}(x,u)\,\frac{\partial w_n(u)}{\partial\bar z_l}.
 \tag{24}
\]
The derivatives in (24) differentiate the displayed products, quotients, cutoffs and actual chart maps in (20)–(21). No unknown cochain, metric, harmonic basis or differential-equation solution occurs in this expression.

On a regular fibre, the same-piece cocycle is that of `L_eta^12`. Restricting (23) therefore gives exactly the Dolbeault class `eta` after division by 12, independently of the partition. This is the required fibre class, not an assertion that (24) is pointwise translation invariant on each fibre. The possible global change by the base class is the original Leray ambiguity.

## 9. The generator G with its original primitive sign

The degree-one generator has an even simpler explicit scalar cocycle. For a parameter `z`, use the fibre lattice factors
\[
 e^{-2\pi iz\gamma(\lambda)}.
\]
The middle linear lifts have scalar factor 1 because `gamma A_j=gamma`. The original finite affine generator has factor
`exp(-2pi i z gamma(v_j)/m_j)`. Its `m_j`th power is exactly the factor of the actual period `v_j`. At the cusp the period factor is `exp(-2pi i z n_gamma)`, independent of toric coordinates, so it extends on every chart. The finite collar (13) has scalar comparison
\[
 \exp(-2\pi iz\,\gamma(v_j)h(s)).
 \tag{25}
\]
Its change under `h->h-1/m_j` cancels the affine factor, and its change under `h->h+k` is exactly the scalar factor of `kv_j`. These give an actual global holomorphic line family.

Let `f_ab` be its logarithmic coefficient: the transition is `exp(2pi i z f_ab)`. Thus the values are `-gamma(lambda)` on lattice arrows, `-gamma(v_j)/m_j` on finite generators, `-gamma(v_j)h` on the stated collar arrow, `-n_gamma` on cusp periods, and zero on pure toric changes. All other arrows use sums and the displayed inverse maps. Since the identities hold for every complex `z`, the `f_ab` satisfy the exact additive cocycle, not just a cocycle modulo integers. With the same weights (21), put
\[
 H_a=\sum_n\sum_u w_n(u)f_{a,n}(x,u),\qquad
 G=\bar\partial H_a.
 \tag{26}
\]
Then `H_a-H_b=f_ab`, so (26) is a global `bar partial`-closed `(0,1)` form. In the regular Betti chart `f_ab=-Delta r_gamma`; hence the induced fibre class is `bar partial r_gamma`, whose exact coefficients are
\[
 \frac{i}{2\Delta}
       \left(d\bar\zeta_2-\frac{m}{y}d\bar\zeta_1\right).
\]
This is precisely `wb:eq:bcpr-gamma-form`, so `[G]=g_gamma` by the injective fibre restriction in `inv:C3.1`.

At `z=1` the lattice and cusp factors are one, and the two finite factors are the actual root characters of `O(S_1-S_2)` for the standard vectors `gamma(v_1)=1`, `gamma(v_2)=-1`. Equation (25) is then the corresponding meromorphic-frame factor `s^{-gamma(v_j)}`. Thus the line is literally `O(S_1-S_2)`, and its twelfth power is
`O(12S_1-12S_2)=f^*O(4p_1-3p_2)`, which has degree one. This is the exact original normalization `exp(12g_gamma)=f^*O(1)`.

## 10. Reality and the scope of the proposed closure

The forms in (23) and (26) are not assumed real. In fact the `Q` of (23) cannot be real: reality plus `bar partial Q=0` would imply `dQ=0`; since `H^2(X,R)=0`, its fibre square would integrate to zero, whereas its Dolbeault restriction gives `-12`. The full contradiction is recorded in `NEW_ROUTE.md`. This also explains why a real semi-flat curvature could not simply be extended and glued globally.

The regular semi-flat representative itself has the exact divergence
`Q_sf(V,bar V)=-iS_11/(8pi^2epsilon^2)` along the actual cusp path
`z_0=z_1=z_2=epsilon`, `V=partial_z1-partial_z0`; its magnitude is asymptotic to `1/(8pi^2epsilon^2 T_0)`. The cocycle construction changes that representative by the complex corrections encoded in (19) and (23); it does not pretend that the singular coefficients extend.

The review must now check: the original annulus/atlas arrows in (13) and the refinement maps in section0; all constants/phases against the original conventions; the connection and Čech signs; and whether the explicitly enumerated, locally finite coefficient formula (24) satisfies the requested literal-atlas presentation without a further finite-chart expansion. The local algebra and all displayed scalar/period maps have been calculated. No status change should be inferred solely from the existence of this draft.
