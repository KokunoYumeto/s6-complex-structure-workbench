# P1.19: integral geometric comparison of the complete marked diagram

## 0. Scope, chronology, and the maps being constructed

This is **post-reading work**. The receiving proof, its saved arrays, the earlier frozen derivation, and the subsequently identified comparison gap have all been read. No historical producer is rerun or attributed to this work. The original pre-reading record and the unsuccessful degree-six guard remain unchanged. This document continues `PROGRESS_PROOF_01.md` by constructing its previously missing relative extension in every degree.

The geometric inputs are the actual marked finite collar maps and cusp cap in the isolated P1.19 packets. In particular, the normalized finite boundary-to-cap map is

\[
q_i(t,y,\theta)=[y,\theta+\mu_i t],\qquad
\mu_i=\varepsilon_i m_i,\quad (m_1,m_2)=(5,4),\quad
(\varepsilon_1,\varepsilon_2)=(1,-1).
\tag{0.1}
\]

The signed-permutation conjugators are the literal matrices supplied in P1.12. This proof uses its actual constructive models and collar formula; it does not use its global homology or global-duality conclusion. The local cusp homology, marked collapse, and local relative-duality calculation are the inputs already retained in the frozen derivation.

Write `L_k=wedge^k Z^6`, with zero differential, and `W_(i,k)=wedge^k M_i`. The numerical graph, boundary, cap, and complement complexes are exactly those reconstructed in `derive_chain.py`. We construct integral chain maps from them to geometric polyhedral chains, including the homotopies for every finite cap square and for the cusp inverse-word square. These maps fix the based meridians. The degree-six cusp generator is identified by an explicit boundary, not by a volume comparison.

The new exact checker `geometric_diagram_check_02.py` supplies 154 checks. It also saves all integer triangles used in the construction, the literal finite-cap source/target adapters, and the free-word homotopy coefficients. The earlier `top_chain_adapter.py/json` supplies the separate 113 checks of the resulting full finite matrices, their inverses, and the global cone adapter. Neither certificate is a substitute for the geometric construction below.

## 1. Integral polyhedral chains and an explicit torus homotopy

### 1.1 The chain complex and its products

Let `P_*(T^n)` be integral rational polyhedral chains on `R^n/Z^n`. Concretely, cut each affine rational simplex at the finitely many integer coordinate hyperplanes it meets, project the resulting simplices to a fundamental cube, and identify opposite faces. Chains are identified under oriented subdivision. A common rational subdivision makes every equality below an equality of finite integer simplex chains. A dimension-dropping affine image is zero in that dimension.

This chain complex computes integral homology of the torus: a finite set of its chains lies in a common rational triangulation, and subdivision induces the usual integral simplicial chain equivalence. There is a countable cofinal sequence of rational subdivisions. In each degree the subdivision inclusion is a split injection of free abelian groups: for each old open simplex choose one of its subdividing simplices, and recover that old coefficient from the chosen coefficient. Thus `P_k` is free abelian as well. These observations permit the integral chain-homotopy comparisons used below; no real or rational coefficient replacement is made.

Addition on the torus defines the Pontryagin product

\[
u*v=\operatorname{add}_*(u\times v).
\]

Triangulating products defines this on the preceding polyhedral chains. It satisfies the exact Leibniz rule

\[
\partial(u*v)=(\partial u)*v+(-1)^{\deg u}u*(\partial v),
\tag{1.1}
\]

and interchanging the two factors gives the orientation sign `(-1)^(deg u deg v)`. All of these statements are identities after the product subdivision.

Let `gamma_j` be the oriented coordinate circle and let `ell_v` be the straight lattice loop `t -> tv mod Z^n`, for `v in Z^n`. Define

\[
C_k(e_{i_1}\wedge\cdots\wedge e_{i_k})
 =\gamma_{i_1}*\cdots*\gamma_{i_k},\qquad C_0(1)=[0].
\tag{1.2}
\]

Repeated coordinate factors have dimension-dropping image and give zero. Consequently `C` is an integral algebra map from the exterior algebra, and its basis cycles are exactly the product-cell generators of the torus. It is an integral homology isomorphism.

### 1.2 Explicit triangle chains

For `v=(v_1,...,v_n)` put `s_j=sum_(r<=j) v_r e_r`, with `s_0=0`, and set

\[
A_v=\sum_{j=1}^n [0,s_{j-1},s_j]
\quad\text{in }P_2(T^n).
\tag{1.3}
\]

The triangle is oriented in the displayed order and is projected to the torus with its integral multiplicities. Its edge from `s_(j-1)` to `s_j` is the same torus chain as `ell_(v_j e_j)`, since its initial point is integral. Therefore the intermediate diagonal edges cancel and

\[
\partial A_v=\sum_j v_j\gamma_j-\ell_v=C_1(v)-\ell_v.
\tag{1.4}
\]

Negative coordinates and repeated windings are included: `ell_(a e_j)=a gamma_j` as oriented polyhedral chains. Degenerate triangles give zero. The new JSON records (1.3) for every column of the two actual conjugators.

For an actual integral matrix `Q`, write `q_j=Qe_j`. On a basis exterior vector define

\[
\begin{split}
\widehat H_{Q,k}(e_{i_1}\wedge\cdots\wedge e_{i_k})
 =\sum_{r=1}^k(-1)^{r-1}
 &C_1(q_{i_1})*\cdots*C_1(q_{i_{r-1}})*A_{q_{i_r}}\\
 &*\ell_{q_{i_{r+1}}}*\cdots*\ell_{q_{i_k}}.
\end{split}
\tag{1.5}
\]

The boundary sign in (1.1) cancels `(-1)^(r-1)`. Substituting (1.4) makes the sum telescope, giving the exact integral identity

\[
\partial\widehat H_{Q,k}=C_k\bigwedge^kQ-Q_*C_k.
\tag{1.6}
\]

There is no unspecified cellular approximation in (1.3)--(1.6). They are finite sums of specified projected triangles and products. Formula (1.6) is verified symbolically by the checker before any commutation of factors is used.

### 1.3 The prescribed degree-five replacement

For `n=6`, orient the torus by `e_1 wedge ... wedge e_6` and use the exact Poincare-dual adapter

\[
J(z)(u)=\operatorname{vol}(u\wedge z),\qquad
J\bigwedge^5Q=(\det Q)Q^{-t}J.
\tag{1.7}
\]

In increasing exterior order its rows/columns are the matrix retained in the first supplement. In particular `1^t J=(-1,1,-1,1,-1,1)`. Cooriented coordinate five-tori are denoted `H_j`, so `C_5(z)=sum_j (Jz)_j H_j`.

For a primitive covector `l`, the integer density `floor(l dot x)` on the fundamental cube defines a six-chain `D_l` with

\[
\partial D_l=\sum_j l_jH_j-H_l,
\tag{1.8}
\]

where `H_l` is the cooriented subtorus `l dot x=0 mod 1`. The oriented jumps across the cuts and opposite cube faces prove this boundary formula directly.

For `delta_Q=det Q` define, on cooriented columns,

\[
D_Q(c)(x)=\delta_Q c^t\lfloor Q^{-1}x\rfloor.
\tag{1.9}
\]

Equivalently this is `delta_Q sum_j c_j D_(Q^-t e_j)`. Thus

\[
\partial D_Q(c)=C((\delta_QQ^{-t})c)-Q_*C(c).
\tag{1.10}
\]

We now specify the homotopy used in this proof in **every degree**:

\[
H_{Q,k}=\widehat H_{Q,k}\ (1\leq k\leq4),\qquad
H_{Q,5}(z)=D_Q(Jz),\qquad H_{Q,0}=H_{Q,6}=0.
\tag{1.11}
\]

Equations (1.6), (1.7), and (1.10) give

\[
\partial H_Q=C\bigwedge Q-Q_*C
\tag{1.12}
\]

in every degree. In degree six both maps send the fundamental chain to `det(Q)` times that chain, so the zero value in (1.11) has the required boundary. The source complex `L` has zero differential. Hence there are no additional adjacent-degree terms in (1.12). In particular replacing precisely its degree-five component introduces **no condition on any retained lower component**. This equation is the promised relative extension, with all components specified by (1.3), (1.5), and (1.11).

The floor chains also satisfy the exact composition identity

\[
D_{PQ}(c)=D_P((\det Q)Q^{-t}c)+P_*D_Q(c).
\tag{1.13}
\]

Indeed, for `a=P^-1x`, `m=floor(a)`, and `a_0=a-m`, the pointwise integer identity is

\[
\lfloor Q^{-1}a\rfloor=Q^{-1}m+\lfloor Q^{-1}a_0\rfloor.
\]

Multiplication by `det(P)det(Q)c^t` gives (1.13), including the sign of the oriented pushforward. A common subdivision by these finitely many rational cuts gives the equality as integral chains. It also gives `D_I=0` and the corresponding exact inverse identity.

## 2. Mapping cylinders, signed product cells, and the based finite maps

For an actual linear torus automorphism `M`, use the geometric cylinder complex

\[
\mathscr B(M)_k=P_k(T^6)\oplus P_{k-1}(T^6),\qquad
\partial(a,x)=(\partial a+(M_*-I)x,-\partial x).
\tag{2.1}
\]

The explicit map to the actual mapping torus sends `(a,x)` to the fibre chain `a` plus its oriented interval prism on `x`. The prism has boundary `(M_*-I)x` minus the prism on `partial x`, giving (2.1). Cutting the mapping torus along its fibre proves that this is an integral homology equivalence. The same construction with the two actual edge cylinders gives `mathscr G` with two suspension summands. These are the actual geometric chain models used below.

Let

\[
Q_i=P_i\operatorname{diag}(1,K_i),\qquad
\widetilde M_i=Q_i^{-1}M_iQ_i.
\]

Both `det Q_i=-1`. The first signed monodromy is a fixed first coordinate and a positive five-cycle. The second is a fixed first coordinate, a positive four-cycle, and a negative sixth coordinate. Their product-cell actions are literally their exterior powers in every degree. Define the raw-marked signed-product cycles

\[
\widetilde C_i=Q_{i*}C\bigwedge Q_i^{-1}.
\tag{2.2}
\]

They satisfy `M_(i*) Ctilde_i=Ctilde_i W_i` exactly. The numerical boundary complex therefore maps to its actual cylinder by

\[
\widetilde\Phi_i(f,x)=(\widetilde C_if,\widetilde C_ix).
\tag{2.3}
\]

For the cap let `e_i:E_i -> P_*(E_i^geom)` be its signed product-cell inclusion, transported back by `K_i`. The actual map (0.1), applied to the cells in (2.3), gives exactly

\[
q_i\widetilde\Phi_i=e_i b_i,
\tag{2.4}
\]

where `b_i` is the literal map (1.12.5). Here and below `q_i` includes the actual prism map from (2.1). To check (2.4), a cell without either base direction remains the same fibre cell. The `t` circle sweeps `m_i` oriented strips and produces `epsilon_i sum_(j=0)^(m_i-1)(wedge R_i)^j`. The `theta` interval gives one strip. The cell containing both `t` and `theta` has image of dimension one less, because their image depends on their single sum in (0.1); its polyhedral pushforward is zero in that degree. These are all four rows of (1.12.5).

At `t=y=0`, (0.1) is `[0,theta]`. This is the prescribed one positive cap-base circuit. The `t` circle at `y=theta=0` has degree `mu_i`. The checker verifies these exact two degree-one columns in the original marking, as well as the entire conjugacy identity

\[
b_{i,k}\operatorname{diag}(\bigwedge^kQ_i,\bigwedge^{k-1}Q_i)
=\operatorname{diag}(\bigwedge^kK_i,\bigwedge^{k-1}K_i)\widetilde b_{i,k}
\tag{2.5}
\]

in every degree. Thus the affine meridian and norm signs are retained in the actual source and target bases.

## 3. The common-fibre comparison and its exact cap homotopy

Use the all-degree maps (1.11) to put

\[
H_i=H_{Q_i}\bigwedge Q_i^{-1},\qquad
\partial H_i=C-\widetilde C_i,
\qquad K_i^Q=H_iW_i-M_{i*}H_i.
\tag{3.1}
\]

Then

\[
\partial K_i^Q=CW_i-M_{i*}C.
\tag{3.2}
\]

The common-fibre numerical boundary and graph comparisons are

\[
\Phi_i^Q(f,x)=(Cf+K_i^Qx,Cx),
\quad
\Phi_G^Q(f,x_1,x_2)=(Cf+K_1^Qx_1+K_2^Qx_2,Cx_1,Cx_2).
\tag{3.3}
\]

Equations (3.2) and (2.1) prove the chain-map identities directly. On the finite boundary graph square they commute exactly. There is an explicit homotopy from (2.3) to the first map in (3.3):

\[
\mathcal H_i(f,x)=(H_if,-H_ix),\qquad
\Phi_i^Q-\widetilde\Phi_i=\partial\mathcal H_i+\mathcal H_i d_{B_i}.
\tag{3.4}
\]

In fact its first component on `(f,x)` is

`(C-Ctilde_i)f + H_i(W_i-I)x - (M_i-I)H_ix`,

and its second component is `(C-Ctilde_i)x`, exactly the difference in (3.4). Applying the actual finite map gives

\[
q_i\Phi_i^Q-e_i b_i=\partial Z_i+Z_i d_{B_i},\qquad
Z_i=q_i\mathcal H_i.
\tag{3.5}
\]

This constructs the full finite-cap comparison in every degree. Formula (3.4) uses the prescribed top component of (1.11) and the explicit triangle components in lower degrees at once. There is no requirement to extend an unspecified cellular homotopy afterward.

## 4. The top correction and the actual coefficient-two homotopy

For the signed permutation `Mtilde_1`, (1.9) is zero. For `Mtilde_2`, its positive coordinates contribute zero and its negative sixth coordinate contributes `floor(-x_6)=-1`, so

\[
D_{\widetilde M_2}(c)=-c_6[T^6].
\tag{4.1}
\]

The increasing five-vector `z=e_1 wedge ... wedge e_5` has coorientation `Jz=-e_6`. Its suspension has differential `-2z`, and (4.1) adds one product fibre top cell to its lift.

Using `M_iQ_i=Q_i Mtilde_i`, the exact composition identity (1.13) gives, on every five-vector,

\[
D_{M_i}J-K_i^Q
 =Q_{i*}D_{\widetilde M_i}J\bigwedge^5Q_i^{-1}.
\tag{4.2}
\]

The right side is an actual integer multiple of the raw fibre top cell, with row

\[
h_1=0,\qquad h_2=(1,-1,-1,1,-1,0).
\tag{4.3}
\]

For clarity, its signed-basis row is `(1,0,0,0,0,0)`, and transport multiplies it by `det(Q_2) wedge^5 Q_2^-1`. The checker verifies this exact adapter. Equivalently `h_i=beta_i(W_(i,5)-I)`, with `beta_i=(1/2)1^tQ_i^tJ`; the geometric formula (4.2) establishes the integer row without using those rational rows as a chain map.

Let `U_i` be identity except for

\[
U_{i,6}(f,x)=(f+h_ix,x).
\tag{4.4}
\]

Define `K_i` to equal `K_i^Q` outside source degree five and to equal `D_(M_i)J` in degree five. The new comparisons satisfy

\[
\Phi_i=\Phi_i^QU_i,\qquad
\Phi_G=\Phi_G^Q U_G,
\tag{4.5}
\]

where `U_G,6(f,x_1,x_2)=(f+h_1x_1+h_2x_2,x_1,x_2)`.

The actual finite cap sends its fibre top cell to `mu_i` times its cap top cell. For `i=2` this degree is `-4`. Thus the one-cell change in (4.1) changes the cap image by `-4[E_2]`. Since the source differential is `-2z`, the exact integral cap homotopy is

\[
H^{\mathrm{cap}}_2(z)=2[E_2].
\tag{4.6}
\]

Transport through the source `Q_2` and target `K_2` gives the row

\[
H^{\mathrm{cap}}_2=2h_2=(2,-2,-2,2,-2,0)
\tag{4.7}
\]

on the fibre `L_5` part of `B_(2,5)`, zero on its suspension part and in all other degrees. Put `Hcap_1=0`. These maps satisfy

\[
b_iU_i-b_i=d_{E_i}H^{\mathrm{cap}}_i+H^{\mathrm{cap}}_id_{B_i}.
\tag{4.8}
\]

The only nonzero equation is `Hcap_2(W_(2,5)-I)=-4h_2`; also `d_E Hcap_2=0`. The checker verifies both the geometric basis transport of (4.6) and its equality with the literal matrices. This is an actual chain homotopy whose value is the specified cap fundamental chain.

Combining (3.5) and (4.8), the full polyhedral finite-cap square has the homotopy

\[
q_i\Phi_i-e_i b_i=\partial Z_i^{\rm poly}+Z_i^{\rm poly}d_{B_i},
\qquad Z_i^{\rm poly}=Z_i+e_iH_i^{\rm cap}.
\tag{4.9}
\]

Indeed `mathcal H_i(U_i-I)=0` because its only possible value uses `H_(i,6)=0`. Thus `Z_iU_i=Z_i`, giving (4.9) without further terms. All the modifications fix degree zero and degree one. The based affine meridian in (2.4) remains precisely the original one.

## 5. The actual complement map and the retained numerical automorphism

Let `Y_num=Cone((j_G,-b_1,-b_2))` be the literal complement complex. Let `mathscr Y` be the corresponding geometric cone of the two actual boundary maps to the graph and the actual finite maps `q_i`. Prisms on the attaching collars give its map to chains of the actual complement. A cut along the collars, or the associated relative chain sequences, proves that map is an integral homology equivalence.

The all-degree map `Psi_Y:Y_num -> mathscr Y` has:

* `Phi_G` on the unshifted graph summand;
* `e_i` on the two unshifted cap summands;
* `Phi_i` on the shifted finite-boundary summands;
* `+Z_i^poly` from the shifted boundary summand into its unshifted cap summand.

This is an exact formula on every chain group. The plus sign follows from (4.9) and the cone differential `(d_D,F;0,-d_B)`: the relevant equality is

\[
\Phi_DF-F^{\rm geom}\Phi_B=\partial Z+Zd_B.
\tag{5.1}
\]

Every component of `Psi_Y` is therefore specified by triangles, floor chains, actual prisms, the cap map (0.1), and the single top chain (4.6). Its graph and boundary diagonal maps are homology equivalences by the cylinder relative sequence and the equivalence `C`; the cap maps `e_i` are the product cellular equivalences. The cone relative sequence then proves that `Psi_Y` is an integral homology equivalence.

These equivalences can also be used as integral chain-homotopy equivalences. For completeness the required inverse/contraction construction is as follows. A free complex with free homology and specified cycle inclusion `i:H->P` admits the integral decomposition

\[
P_k=B_k\oplus iH_k\oplus s_{k-1}B_{k-1},\qquad
\partial s_{k-1}=I_{B_{k-1}}.
\]

Here the boundary subgroups are free, and both indicated quotient sequences split over `Z`. On this decomposition set

\[
p(b+ih+s b')=h,\quad
T(b+ih+s b')=s_kb.
\]

Then `pi=I` and `partial T+T partial=I-ip` exactly. Applying these choices to `C` gives a chain inverse on the fibre. Alternatively the cone of each of the displayed quasi-isomorphisms is a free acyclic complex; choose its boundary basis and sections and use the same formula with `H=0`. This supplies integral chain homotopy inverses. These auxiliary contractions introduce no change to any prescribed map: the maps being inverted are already the explicit maps above, with all diagram homotopies fixed.

To compare with the first progress certificate, construct `Psi_Y^Q` from (3.3), (3.5). Then the exact equality is

\[
\Psi_Y=\Psi_Y^Q S_Y,
\tag{5.2}
\]

where `S_Y` is the retained numerical automorphism: `U_G` on the graph, identity on caps, `U_i` on shifted finite boundaries, and `+Hcap_i` from shifted `B_(i,5)` to `E_(i,6)`. This is exactly the matrix tested in all degrees in the 113-check certificate. Its correction squares to zero, and its inverse is `I-(S_Y-I)`. Thus the new geometry realizes the already checked automorphism; it does not replace the prescribed literal finite-cap diagram by an untracked splitting.

## 6. The cusp inverse-word comparison in every degree

Let `g_0=g_2^-1 g_1^-1`, and let `M_g,W_g` denote the actual target and source actions for a word. Extend the chosen two homotopies `K_1,K_2` by the explicit free-word rules

\[
K_{gh}=K_gW_h+M_{g*}K_h,\qquad
K_{g^{-1}}=-M_{g^{-1}*}K_gW_{g^{-1}},\qquad K_e=0
\tag{6.1}
\]

where `e` means the identity word. Free cancellation preserves the formula. Direct differentiation gives `partial K_g=CW_g-M_(g*)C` in every degree. In source degree five, (1.13) implies

\[
K_g=D_{M_g}J.
\tag{6.2}
\]

The cusp boundary comparison is therefore

\[
\Phi_0(f,x)=(Cf+K_{g_0}x,Cx):B_0\longrightarrow\mathscr B(M_0).
\tag{6.3}
\]

The actual inverse-edge traversal on geometric cylinder chains is

\[
\mathcal J_0(a,x)=(a,-M_{2*}M_{0*}x,-M_{0*}x).
\tag{6.4}
\]

This is obtained by cutting the source prism into its two inverse-edge strips and transporting the chain to the initial end of each strip. It has no extra fibre part. It is the actual based boundary map because the supplied clutch translation is zero. Its numerical analogue is the literal `j_(0,G)` in (1.12.3).

The entire square is related by the explicit degree-one chain homotopy

\[
\mathcal R(f,x)=(0,K_{g_1^{-1}}x,K_{g_0}x),\qquad
\Phi_Gj_{0,G}-\mathcal J_0\Phi_0
 =\partial\mathcal R+\mathcal R d_{B_0}.
\tag{6.5}
\]

For the two edge components this is exactly `partial K_g=CW_g-M_g C`, with the minus sign in the cylinder differential. The fibre component is the identity

\[
-K_1W_2W_0-K_2W_0-K_{g_0}
=(M_{1*}-I)K_{g_1^{-1}}+(M_{2*}-I)K_{g_0},
\tag{6.6}
\]

which follows by expanding (6.1). The checker verifies (6.6) as an exact free-word expression with the literal exterior matrices in every source degree. Also `mathcal R d_B=0`, because `mathcal R` vanishes on the fibre summand. Formula (6.5), followed by graph inclusion into the geometric complement cone, is the required actual cusp-to-complement square.

For the earlier numerical adapters, (6.1) gives the exact top row

\[
h_0=-h_1W_{2,5}W_{0,5}-h_2W_{0,5}
=(-1,1,1,-3,-1,0).
\tag{6.7}
\]

Writing `U_0,6(f,x)=(f+h_0x,x)`, one has

\[
\Phi_0=\Phi_0^QU_0,\qquad S_Yj_Y=j_YU_0.
\tag{6.8}
\]

The saved matrix certificate verifies the second equality on every source group. On the three actual invariant columns `X`, `h_0X=(0,-2,-2)`. This nonzero value is recorded explicitly. The correct geometric comparison is (6.3)--(6.5), and (6.8) gives its precise relation to the former marked comparison.

## 7. The actual degree-six cusp cycles, with their integral bounding chains

Let `x_j` be the three literal five-vectors

\[
x_j=a_1\wedge a_2\wedge a_3\wedge
b_1\wedge\cdots\widehat{b_j}\cdots\wedge b_3.
\]

Their original columns are the retained matrix `X=(wedge^5 S)[:,(3,2,1)]` in one-based exterior coordinates. Put `l_j=Jx_j`. The checker verifies that these are primitive covectors and `M_0^-t l_j=l_j`. The torus `H_(l_j)` is the actual invariant five-dimensional torus `{b_j=0}`, with the corresponding orientation.

Use the exact six-chain `D_(l_j)` from (1.8). Invariance of `l_j` gives the identity of integer densities

\[
D_{M_0}(l_j)=(I-M_{0*})D_{l_j}.
\tag{7.1}
\]

To check it, write `m=floor(M_0^-1x)`. The coefficient of the right side is

\[
\lfloor l_j^tx\rfloor-
\lfloor l_j^t(M_0^{-1}x-m)\rfloor
=l_j^tm,
\]

which is (1.9). Thus (6.2)--(6.3) imply the exact boundary relation in the actual cusp cylinder complex

\[
\Phi_0(0,x_j)-(0,H_{l_j})
=\big((I-M_{0*})D_{l_j},\partial D_{l_j}\big)
=\partial(0,-D_{l_j}).
\tag{7.2}
\]

The rightmost term is a specified integral seven-chain. Formula (7.2) proves the marked comparison with the geometric invariant-subtorus mapping torus. Together with (6.5), it tracks that same class into the complement. It requires neither a flat-volume inference nor a new unrecorded fibre summand.

Under the actual cusp retraction, the pure toric formula is

\[
(b,a,\theta)\longmapsto[b,a+\theta(b-v)]
\tag{7.3}
\]

on the cell indexed by `v`, with the angular quotient specified in the input. For the mapping torus of `{b_j=0}`, its image has base dimension at most two and angular dimension at most three. Subdivision by the finite moment-cell stratification therefore gives an image of dimension at most five. Its sixth homology is zero. Consequently the actual cusp map sends each class in (7.2) to zero in `H_6(C;Z)`. The permitted deformation of the bounded units transports the marked map by homotopy, so this remains its value for the actual cusp cap.

The other delicate marking is degree one. By (1.11), all `K_(g,0)=0`; hence (6.3) sends `(0,1)` to the actual based zero-section meridian. That meridian bounds the given zero-section disc in the cusp cap. It also has zero image. Both degree-one and degree-six values used in the frozen normal form have now been proved in the precise simultaneous marked diagram.

## 8. From this actual diagram to the saved full global complex

The preceding construction supplies the missing input for the already retained integral reduction. To make its use explicit, the actual cusp map transported by (6.3) and a free-homology contraction of the cusp complex has fibre part `kappa`. Its suspension values in degrees one and six vanish by Section 7. In degrees two, three, and five its values lie in the collapse image because that image is all of cusp homology. In degree four the local relative-duality and pair-sequence calculation proves that the actual boundary image is the primitive rank-nine collapse image; this is Section 5 of `BEFORE_READING.md` and does not use global duality.

The saved integral matrices `F_k` satisfy `d_Y F_k=J_k` for `k=2,3,4,5`, where `J_k` is the literal common-fibre inclusion. They therefore remove those suspension values by the explicit boundary shears and complement homotopies in the frozen derivation. Their geometric interpretation is now fixed: `Psi_Y` sends that literal fibre inclusion to `C` in the actual common fibre. The degree-four secondary value has odd projection to the rank-one quotient by the collapse image, by local relative Poincare--Lefschetz duality. The retained integral shears and homotopies reduce it to the displayed single degree-four term.

The cusp-to-complement homotopy in (6.5) is incorporated by the same explicit cone rule used in Section 5: a homotopy `F'-F=dT+Td` gives the cone map `(a,b)->(a-Tb,b)`. Thus its presence records the actual boundary marking throughout the final gluing; it does not impose literal equality of two different choices of geometric cycle representatives.

The resulting finite complex is exactly `global_complex()` in the frozen fresh reconstruction. Its full integral comparison with the receiving arrays is the separately retained 140-check adapter. The new geometric construction does not change either set of arrays. The previously checked source/target relation `S_Y j_Y=j_Y U_0`, the cap homotopy (4.8), and the full global block adapter provide their explicit relation to the previous common-fibre comparison.

Accordingly this document fills the actual integral geometric-diagram gate identified in the supersession record: it gives all-degree geometric source maps, finite-cap homotopies with the actual based affine meridians, the exact cap-top-cell correction, the cusp inverse-word homotopy, and the integral boundary identifying the required invariant cusp cycles. The earlier saved integer homology and array comparisons retain their original computational scopes. No shared source, canonical assessment, or completion state is changed by this document; root review and the source/PDF integration remain separate actions.
