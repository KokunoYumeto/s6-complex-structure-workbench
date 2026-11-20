# P1.19: exact top-degree finite-cap adapter and the smaller remaining gate

This is post-reading work. The receiving proof, previous arrays, earlier unsuccessful closure, and the reopened gate are all exposed. This document does not replace the frozen pre-reading record or claim a completed full geometric comparison.

## 1. Actual matrices and conventions

The global torus lattice uses the literal matrices `M_1=A^t`, `M_2=B^t`, with orders 5 and 4, and `M_0=(M_1M_2)^-1`. The genus-two deck orders 5 and 8 enter the earlier exterior-square construction; the actual six-dimensional maps used here are the supplied order-5/order-4 pair. All calculations below use their literal entries and the actual `S`, `P_i`, and `K_i` input matrices.

Use the original increasing exterior basis of `L_5=wedge^5 Lambda`. The Poincare-dual coorientation adapter is the matrix `J` from `P119_POLYHEDRAL_SUPPLEMENT_09.md`, defined by `J(z)(u)=vol(u wedge z)`. It satisfies

\[
J^{-1}=-J,\quad\det J=1,\quad
J\bigwedge^5M=M^{-t}J\quad(M\in SL_6(\mathbb Z)).
\]

Thus `1^t J=(-1,1,-1,1,-1,1)`.

## 2. An exact polyhedral composition identity

For a primitive covector `l`, the integral polyhedral six-chain `D_l` on the fundamental cube has coefficient `floor(l dot x)` on each cut polyhedron. Its boundary is

\[
\partial D_l=\sum_i l_iH_i-H_l.
\]

For any `Q in GL_6(Z)`, put `delta_Q=det Q` and `W_Q=delta_Q Q^-t` in cooriented coordinates. Define

\[
D_Q(c)=\delta_Q\sum_i c_iD_{Q^{-t}e_i}.
\tag{2.1}
\]

As an integer density on the half-open fundamental cube this is exactly

\[
D_Q(c)(x)=\delta_Q c^t\lfloor Q^{-1}x\rfloor,
\tag{2.2}
\]

with the floor taken coordinatewise. Hence

\[
\partial D_Q(c)=C(W_Qc)-Q_*C(c),
\quad C(c)=\sum_i c_iH_i.
\tag{2.3}
\]

This choice has an exact composition identity, including orientation-reversing basis changes:

\[
D_{PQ}(c)=D_P(W_Qc)+P_*D_Q(c).
\tag{2.4}
\]

To verify it, set `a=P^-1 x`, `m=floor(a)`, and `a0=a-m`. The integer matrix `Q^-1` gives the pointwise identity

\[
\lfloor Q^{-1}a\rfloor
=Q^{-1}m+\lfloor Q^{-1}a_0\rfloor.
\]

Multiply by `delta_P delta_Q c^t`. The first term is the density of `D_P(W_Qc)`; the second is the oriented pushforward density of `D_Q(c)`. The identity is exact on every open polyhedron of a common rational subdivision, and hence as integral chains. Boundaries of these polyhedra have the prescribed matching incidences. This argument is stronger than a zero-volume comparison: it specifies the composition chains themselves. In particular `D_I=0`, and applying (2.4) to `QQ^-1` gives the exact inverse comparison.

For an edge monodromy `M`, the geometric prism plus `D_M(c)` has boundary `C((M^-t-I)c)`. These are the explicit polyhedral lifts whose inverse-word volume cancellation was proved in the previous supplement.

## 3. Signed permutations give literal top-cell changes

Let

\[
Q_i=P_i\operatorname{diag}(1,K_i),\qquad
\widetilde M_i=Q_i^{-1}M_iQ_i.
\]

Both `Q_i` have determinant `-1`. The first `Mtilde` is a fixed first coordinate and a positive five-cycle. The second is a fixed first coordinate, a positive four-cycle, and a negative sixth coordinate.

For a positive signed-permutation coordinate, `floor(x_j)=0` in the open fundamental cube. For a negative coordinate, `floor(-x_j)=-1`. Thus (2.2) gives:

* `D_(Mtilde_1)=0` exactly.
* `D_(Mtilde_2)(c)=-c_6[T^6]` exactly, in cooriented coordinates.

This is a literal integer multiple of the product top cell. In the increasing exterior basis the five-cell omitting the negative sixth coordinate is `z=e_1 wedge ... wedge e_5`, whose cooriented column is `-e_6`. Its upper boundary generator `sigma` has differential `-2z`. The polyhedral lift is the product lift plus the fibre top cell:

\[
\sigma_{\rm poly}=\sigma_{\rm prod}+[T^6].
\tag{3.1}
\]

No fractional chain is used in (3.1).

Transport (3.1) through the literal `Q_i`. In the original increasing `L_5` basis define

\[
\beta_i=\tfrac12\mathbf1^tQ_i^tJ,
\qquad h_i=\beta_i(W_{i,5}-I).
\tag{3.2}
\]

The resulting rows are integral:

\[
h_1=0,\qquad h_2=(1,-1,-1,1,-1,0).
\tag{3.3}
\]

The individual rational rows are

\[
\beta_1=(-1/2,-1/2,0,1/2,0,1/2),
\quad
\beta_2=(-1,-1/2,0,0,3/2,1/2).
\]

The source change in degree six is the integral automorphism

\[
U_{i,6}(f,x)=(f+h_ix,x),
\tag{3.4}
\]

and identity in every other degree. Its inverse changes the plus sign to minus. The square-zero matrix of (3.4) and every chain-map equation are checked exactly in `top_chain_adapter.py`.

The composition identity (2.4) accounts explicitly for the orientation signs in transport by `Q_i`. It proves the top-degree polyhedral compatibility of these linear marking maps and their inverse words. It does not, by itself, assert a complete simultaneous transfer of all the other degrees of the finite-cap diagram.

## 4. Actual finite affine map and the coefficient-two homotopy

In the supplied split coordinates write `v=epsilon_i v_i` and `x=t v+y`, with `y in T_K`. The normalized actual collar and finite affine quotient give the cap map

\[
q_i(t,y,\theta)=[y,\theta+\epsilon_i m_i t].
\tag{4.1}
\]

Its source and target mapping-torus identifications are the ones used in P1.12. The deck shift in the root chart changes `y` by `R_i` and the second target coordinate by one, so (4.1) respects that identification. Changing the fibre coordinate `t` by one changes the second target coordinate by `epsilon_i m_i`; `R_i^(m_i)=I` makes this well-defined. At `t=0,y=0`, the based affine meridian is exactly `[0,theta]`, one positive target base circuit in the supplied cellular convention. No extra translation is introduced by (4.1).

The two relevant top-degree values of the actual cellular map `b_i` are therefore

\[
b_i([T^6])=\epsilon_i m_i[E_i],\qquad
b_i(g_i\wedge \bigwedge^5K)=[E_i].
\tag{4.2}
\]

The first is the signed `m_i`-strip norm, and the second is one strip. The product involving both base directions maps through their one-dimensional sum and gives the zero row specified in (1.12.5). This retains the given actual affine meridian and its sign.

For the order-four cap, `epsilon_2 m_2=-4`. Equation (3.1) changes the cap image of `sigma` by `-4[E_2]`. The actual boundary differential is `d sigma=-2z`, so the integral homotopy

\[
H(z)=2[E_2]
\tag{4.3}
\]

has `H(d sigma)=-4[E_2]`, exactly the required correction. In cooriented coordinates its value on the corresponding `H_6=-z` is `-2[E_2]`. This specifies both signs and the basis in which the coefficient is written.

Transporting (4.3) to the original exterior basis gives the simple row

\[
H_2=2h_2=(2,-2,-2,2,-2,0):L_5\longrightarrow E_{2,6}.
\tag{4.4}
\]

Extend it by zero on the suspension `L_4` part of `B_{2,5}` and in every other degree. It satisfies

\[
H_2(W_{2,5}-I)=-4h_2,
\qquad d_EH_2=0.
\tag{4.5}
\]

Consequently the entire top map difference is the exact integral homotopy identity

\[
b_2U_2-b_2=d_EH_2+H_2d_B.
\tag{4.6}
\]

The alternative row `-4 beta_2=(4,2,0,0,-6,-2)` gives the same differential; its difference from (4.4) annihilates `W_2-I`. For the order-five cap both the source change and homotopy are zero. All these identities are verified against the literal finite-cap matrices, not only their induced homology maps. The source changes are identity in degree one, so the based meridian in (4.1) remains fixed. They also fix the fibre top cell and all lower source groups.

## 5. Complete algebraic source/target adapter for the complement

Define `U_G` to be identity except in degree six, where

\[
U_G(f,x_1,x_2)=(f+h_1x_1+h_2x_2,x_1,x_2).
\]

It satisfies the exact squares `U_G j_(G,i)=j_(G,i) U_i`. The complement is the supplied cone of `(j_G,-b_i)`. In this cone, extend `U_G`, the two `U_i`, and the two homotopies (4.6) to an automorphism `S_Y` as follows:

* on the unshifted graph part use `U_G`;
* on the unshifted caps use identity;
* on the two shifted finite-boundary parts use `U_i`;
* from the shifted `B_(i,5)` part to the `E_(i,6)` part add `+H_i`.

The plus sign is fixed by the cone differential `(d_A,F;0,-d_B)`. Indeed

\[
U_AF-FU_B=d_AH+Hd_B
\]

has cap row `b_i(U_i-I)=H_i d_B`, while its graph row is zero. Therefore `S_Y` is an integral chain automorphism. Its corrections in degrees six and seven square to zero, and its inverse is identity minus those corrections.

For the actual inverse-word map put

\[
h_0=-h_1W_{2,5}W_{0,5}-h_2W_{0,5}
=(-1,1,1,-3,-1,0),
\]

and let `U_0(f,x)=(f+h_0x,x)` in boundary degree six. Then the source/target relation is exactly

\[
S_Yj_Y=j_YU_0.
\tag{5.1}
\]

In particular `j_Y` is tracked explicitly; it is not silently kept fixed after a changed splitting. On the actual three invariant five-torus columns, `h_0` evaluates as `(0,-2,-2)`. The top suspension correction in the literal coordinates can therefore be nonzero.

At the full global-cone level set

\[
P_k=\operatorname{diag}(S_{Y,k},I_{C,k},U_{0,k-1}).
\]

This identifies the complex with zero degree-six cusp suspension with the complex whose degree-six cap map is `j_C U_0^-1`, that is, whose extra suspension row is `-kappa_6 h_0`. Every inverse and every full differential identity is checked. Thus this particular possible top correction is absorbed by an explicit integral diagram automorphism, without changing the already established degree-four secondary class.

The saved output contains 113 exact checks, including all finite source squares, the literal cap homotopies, the full complement differential equations, (5.1), and all eight global differential intertwinings.

## 6. Precisely smaller remaining gate

The calculations above establish an actual local top-cell comparison in the signed-permutation product models, its affine-cap coefficient-two homotopy, the coherent polyhedral linear-marking identity, and the full integral candidate adapter in the literal matrices. These are retained progress beyond the earlier volume-only result.

The unfinished step is to assemble these degree-five/six polyhedral comparison maps as a **simultaneous integral chain comparison of the actual full gluing diagram**, extending the retained lower-degree chain comparisons and their finite-cap norm maps, with the chosen based affine meridians fixed. The exact upper-degree maps and all their necessary matrix identities have now been supplied; the remaining proof must show that the chosen top-degree replacements extend relative to those lower-degree maps, rather than introduce an unrecorded coherence term from the common subdivision or its contraction.

A proof of that relative extension has not yet been completed in this document. Therefore no mathematical closure of P1.19 or shared-row promotion is claimed here. The next step is an explicit relative cellular/singular-chain construction, or an exact common subdivision and contraction, that realizes the already checked adapter while retaining every lower-degree attaching map.
