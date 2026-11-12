# S6 workbench feedback for ChatGPT Pro mode

Last updated: 2026-09-06 (Europe/Berlin)

The current lattice/triality continuation, including a bounded next exact
calculation, is in [the 6 September handoff](WEB_PRO_TRIALITY_LEECH_FEEDBACK_20260906.md).
The dated material below retains the earlier toroidal, spectral and operator
work. It is not a replacement for the newer retained-coordinate morphisms.

This is the transfer note from the local Codex validate/repair/disprove
workbench to the ChatGPT Pro web session.  Treat it as mathematical feedback
on the T1/T2/T3 packets, not as an instruction to trust the workbench without
checking it.  When continuing the calculation, preserve the exact canonical
basis, signs, domains, codomains, metric choices, and operator domains below.

## 3 September 2026 later exact update: what the local workbench has now proved

This block supplies the mathematics completed after the earlier handoff. It
should be used to push the next Pro calculation beyond a repetition of the
Gram quotient. The rank-three toroidal degeneration, the cyclic-six defect
map, and the Hermitian Gram boundary are now exact objects, but they are three
different objects. No identification among them follows from a shared
dimension, the integer six, or an $SU(3)$-action.

### The rank-three toroidal successor is constructed, including its filling map

Let $L=\mathbb Z^3$. The $L$-periodic Kuhn triangulation of
$\mathbb R^3$, coned at height one, gives a smooth toric fourfold; quotienting
a neighbourhood of the central divisor by the integral shear action gives a
proper analytic family

\[
 \pi_3:N_3\longrightarrow\Delta.
\]

For $q=e^{2\pi i\tau}\ne0$,

\[
 N_{3,q}\cong
 \mathbb C^3/(\mathbb Z^3+\tau\mathbb Z^3)\cong E_\tau^3,
\]

and at every deepest toric point the map is literally

\[
 (z_0,z_1,z_2,z_3)\longmapsto t=z_0z_1z_2z_3.
\]

In the ordered basis $(a_1,a_2,a_3,b_1,b_2,b_3)$ of the smooth-fibre
lattice, the positive cusp loop has

\[
 M_3=
 \begin{pmatrix}I_3&I_3\\0&I_3\end{pmatrix},
 \qquad
 R=M_3-I,
 \qquad
 R^2=0,
 \qquad
 \ker R=\operatorname{im}R
   =\mathbb Z\langle a_1,a_2,a_3\rangle.
\]

The local filling is not represented only by this matrix. Its fundamental
group and the inclusion from a smooth fibre have been computed:

\[
 \pi_1(N_3)\cong L\cong\mathbb Z^3,
 \qquad
 a_i\longmapsto0,
 \qquad
 b_i\longmapsto e_i.
\]

The central fibre $W_3=\pi_3^{-1}(0)$ is globally irreducible. Its
normalization is the smooth $A_3$-permutohedral toric threefold, and its open
strata are forced by the quotient triangulation:

\[
 \begin{array}{c|c|c|c}
 \text{cell}&\text{number}&\text{open stratum}&\text{local branches}\\ \hline
 \text{vertex}&1&(\mathbb C^*)^3&1\\
 \text{edge}&7&(\mathbb C^*)^2&2\\
 \text{triangle}&12&\mathbb C^*&3\\
 \text{tetrahedron}&6&\mathrm{pt}&4.
 \end{array}
\]

Thus four branches meet locally at each of six points; there are not four
global components or four canonically split line bundles. In particular,

\[
 \chi(W_3)=6.
\]

If $g:M^8\to S^2$ is a proper triangulable map, is a locally trivial
$T^6$-bundle away from finitely many critical values, has $W_3$ as one
singular fibre, and has only finite free quotients of $T^6$ as its other
singular fibres, then Euler additivity gives

\[
 \chi(M)=\sum_{p\in\Sigma}\chi(g^{-1}(p))=6.
\]

Hence the literal Fabel three-special-fibre pattern cannot have total space
$S^8$, whose Euler characteristic is two. Retaining $W_3$ in a real $S^8$
candidate requires additional genuinely singular fibres whose Euler
characteristics sum to $-4$. A smooth complex $S^8$ total space is also
impossible because a homotopy eight-sphere has no almost-complex structure.

### Exact content of the new $6=3!\det$ and Weyl-chamber observation

The latest partial Pro continuation noticed a relation between the six
quadruple points and the cubic determinant.  Its strongest correct form is as
follows.  Replace the unit rank-three shear by an integral injection

\[
 \mathcal B:\overline L_3\hookrightarrow L_3,
 \qquad d=[L_3:\mathcal B\overline L_3]<\infty.
\]

The quotient has $d$ vertex orbits and $6d$ tetrahedron orbits.  Since all
positive-dimensional torus strata have Euler characteristic zero,

\[
 \boxed{
 \chi(W_{3,\mathcal B})=6d
 =3!\,[L_3:\mathcal B\overline L_3]
 =3!\,|\det\mathcal B|.}
\]

The absolute determinant is invariant under independent unimodular changes of
the two marked lattice bases.  If a polarization identifies $\mathcal B$ with
a positive-definite symmetric matrix, then $\det\mathcal B$ is literally the
cubic Jordan norm on that real symmetric subcone.  Without that additional
symmetry and positivity, it is only the ordinary determinant of an integral
lattice map; it is not a point of
$\operatorname{Herm}_3(\mathbb C)_{\geq0}$.  Even in the polarized case the
single number $\det\mathcal B$ does not recover the fan, period correction,
singular filling, or global total space.

There is also an exact $S_3$-equivariant chamber correspondence.  In the
diagonal Cartan subspace

\[
 \mathfrak a={\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3):
 \lambda_1+\lambda_2+\lambda_3=0\},
 \qquad \nu_i=E_{ii}-\frac13I_3,
\]

send the target $A_2$ vectors $n_i=P(e_i)$ to $\nu_i$.  For
$\pi=(\pi_1,\pi_2,\pi_3)\in S_3$, the fan map sends the Kuhn tetrahedron
$\sigma_{0,\pi}$ onto

\[
 \operatorname{conv}\{0,n_{\pi_1},-n_{\pi_3}\},
\]

and the cone on its Cartan image is exactly

\[
 \boxed{
 \mathbb R_{\geq0}\nu_{\pi_1}
 +\mathbb R_{\geq0}(-\nu_{\pi_3})
 =\{\lambda_{\pi_1}\geq\lambda_{\pi_2}
       \geq\lambda_{\pi_3}\}.}
\]

Thus the six labeled toroidal quadruple-point strata and the six diagonal
$A_2$ Weyl chambers are the same $S_3$-torsor after the chosen lattice/Cartan
marking.  This is a genuine combinatorial bridge.  It is not an equivalence of
the analytic singularities: after the target lattice quotient, those six
triangles form only two global triangle orbits, and the determinant's
rank-one normal germ remains an irreducible quadratic rather than a
four-branch normal crossing.

### The rank-three cusp maps exactly onto the reconstructed rank-two cusp

Write the candidate cusp monodromy in the decomposed basis
$A_F\oplus B_F$, where
$A_F=\mathbb Z\langle\widehat w,\widehat\delta\rangle$ and
$B_F=\mathbb Z\langle\widehat\gamma,\widehat u\rangle$:

\[
 M_F(a,b)=(a+B_0b,b),
 \qquad
 B_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

Its filling map is

\[
 c_F:A_F\oplus B_F\longrightarrow B_F,\qquad c_F(a,b)=b.
\]

Define

\[
 P=
 \begin{pmatrix}1&-1&0\\0&1&-1\end{pmatrix},
 \qquad
 Q=B_0^{-1}P=
 \begin{pmatrix}0&-1&1\\1&-1&0\end{pmatrix}.
\]

Both are integral epimorphisms and

\[
 \ker P=\ker Q=\mathbb Z(1,1,1),
 \qquad B_0Q=P.
\]

For $\Lambda_3=L_3\oplus\bar L_3\cong\mathbb Z^6$, put

\[
 \Phi=P\oplus Q:\Lambda_3\longrightarrow A_F\oplus B_F.
\]

Then the exact monodromy and filling identities are

\[
 \boxed{\Phi M_3=M_F\Phi}
\]

and

\[
 \begin{CD}
 H_1(T^6)=L_3\oplus\bar L_3 @>{\Phi}>>
 H_1(T^4)=A_F\oplus B_F\\
 @V{c_3}VV @VV{c_F}V\\
 \bar L_3 @>{Q}>> B_F ,
 \end{CD}
 \qquad c_3(a,b)=b.
\]

The quotient is also toric, not only a lattice calculation. If
$\mathcal T_3$ is the Kuhn triangulation, then $P$ maps each tetrahedron

\[
 \operatorname{conv}\{m,\,
 m+e_{\pi_1},\,
 m+e_{\pi_1}+e_{\pi_2},\,
 m+(1,1,1)\}
\]

onto one triangle of the candidate's periodic $A_2$ triangulation. Hence

\[
 \widehat P:L_3\oplus\mathbb Z\longrightarrow L_2\oplus\mathbb Z,
 \qquad \widehat P(x,r)=(Px,r),
\]

is a fan map and gives a toric morphism $F:Y_3\to Y_2$ satisfying
$t\circ F=t$.

The candidate's bounded period correction can be retained exactly. Write

\[
 Z_2(t)=sB_0+C(t),
 \qquad
 S=\begin{pmatrix}1&1\\0&1\\0&0\end{pmatrix},
 \qquad PS=I_2,
\]

and set

\[
 C_3(t)=S\,C(t)\,Q,
 \qquad
 Z_3(t)=sI_3+C_3(t).
\]

Then

\[
 \boxed{PZ_3(t)=Z_2(t)Q.}
\]

After shrinking the cusp disc, this gives a surjective holomorphic
homomorphism of smooth fibres

\[
 \mathbb C^3/(Z_3(t)\mathbb Z^3+\mathbb Z^3)
 \longrightarrow
 \mathbb C^2/(Z_2(t)\mathbb Z^2+\mathbb Z^2)
\]

with elliptic kernel. For the source and target toric shear actions,

\[
 F\Psi^{(3)}_\lambda
 =\Psi^{(2)}_{Q\lambda}F,
\]

so the map extends across every toric stratum and descends to a holomorphic
map of actual local cusp families

\[
 \boxed{\overline F:N_3^C\longrightarrow N_0}
\]

over the same disc. Its smooth-fibre homology map is $\Phi$, and its cusp
filling square is the displayed commutative square. This solves the local
monodromy/fan/period/filling bridge. It depends on maximal-torus/root-lattice
data and is canonical only up to the target Weyl action; it does not arise
from the determinant rank strata or the $\mathbb{CP}^2$ normal cones.

The finite orders also admit a rank-six lift. With

\[
 C_1=\begin{pmatrix}-1&-1\\1&0\end{pmatrix},
 \qquad
 C_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
 \qquad
 C_0=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\]

one has

\[
 C_1^3=C_2^4=I,\qquad C_1C_2C_0=I.
\]

Therefore

\[
 \widetilde A_1=A_1\oplus C_1,\qquad
 \widetilde A_2=A_2\oplus C_2,\qquad
 \widetilde M_0=M_F\oplus C_0
\]

have orders $3$, $4$, and unipotent infinity monodromy and satisfy
$\widetilde A_1\widetilde A_2\widetilde M_0=I$. Translations
$(v_j,0)/m_j$ lift the candidate's two free affine actions: a fixed point
upstairs would project to a forbidden fixed point downstairs. Thus the
integer monodromies and finite-fibre freeness do not obstruct a global
elliptic extension.

The required integral identification with the local Kuhn cusp is also
explicit. Set

\[
 A=\begin{pmatrix}
 1&-1&0\\0&1&-1\\0&0&1
 \end{pmatrix},
 \qquad
 B=\begin{pmatrix}
 0&-1&1\\1&-1&0\\0&0&1
 \end{pmatrix},
 \qquad
 D=B_0\oplus(1).
\]

Then

\[
 \det A=\det B=1,\qquad A=DB,\qquad AB^{-1}=D.
\]

Consequently $J=\operatorname{diag}(A,B)\in SL_6(\mathbb Z)$ sends
$M_3$ to

\[
 JM_3J^{-1}=
 \begin{pmatrix}I_3&D\\0&I_3\end{pmatrix}.
\]

After reordering
$(A_F,\mathbb Z;\,B_F,\mathbb Z)$ as
$(A_F,B_F;\,\mathbb Z,\mathbb Z)$, this is exactly

\[
 \boxed{M_F\oplus C_0.}
\]

Projection onto the first two coordinates in each three-block is
$P\oplus Q=\Phi$. Thus the local elliptic kernel and the added $C_0$ summand
in the global monodromy lift are the same integral subquotient, not merely
two rank-compatible constructions. What remains is the analytic
period-and-overlap gluing at both finite fillings.

### The original $S^6$ candidate has an exact cyclic-six defect quotient

For the reconstructed candidate's regular locus $U$, let

\[
 L_4=H^4(U;\mathbb Z)
 =\mathbb Z\langle a_0,b_0,a_1,b_1,a_2,b_2\rangle
\]

in the marked orientation, and let $F\cong T^4$ be a smooth fibre. The
restriction/evaluation map

\[
 \kappa_F:L_4\longrightarrow H^4(F;\mathbb Z)\cong\mathbb Z
\]

has the computed row

\[
 \boxed{
 \kappa_F(n_0a_0+r_0b_0+n_1a_1+r_1b_1+n_2a_2+r_2b_2)
 =12n_0+4n_1-3n_2,}
\]

so

\[
 [\kappa_F]=(12,0,4,0,-3,0),
\]

and its saturated kernel is

\[
 \ker\kappa_F=
 \mathbb Z\langle b_0,b_1,b_2,a_0-3a_1,3a_1+4a_2\rangle.
\]

It factors through the actual collar maps. If

\[
 q_{\mathrm{col}}:L_4\longrightarrow H_1(X^\circ;\mathbb Z)
\]

sends $a_0,a_1,a_2$ to $c,\bar g_1,\bar g_2$ and kills the three $b_i$,
while

\[
 \Phi_1(nc+r\bar g_1+s\bar g_2)=12n+4r-3s,
\]

then

\[
 \boxed{\kappa_F=\Phi_1\circ q_{\mathrm{col}}.}
\]

For the cusp attaching meridian, the same functional gives

\[
 \Phi_1(\ell_0c-\bar g_1-\bar g_2)
 =12\ell_0-4\ell_1-3\ell_2=p,
\]

and at $(\ell_0,\ell_1,\ell_2)=(0,1,-1)$ it gives $p=-1$.

Writing

\[
 \rho_m(k)=e^{-2\pi ik/m},
 \qquad
 \chi_6=\rho_6\circ\kappa_F,
\]

one obtains

\[
 \boxed{L_4/\ker\chi_6\cong\mu_6\cong\mathbb Z/6\mathbb Z.}
\]

The exact order-three projection selected by the same candidate data is

\[
 \boxed{\chi_3:=\chi_6^2=\rho_3\circ\kappa_F.}
\]

On the marked generators,

\[
 \chi_3(a_1)=e^{-2\pi i/3},
 \qquad
 \chi_3(a_0)=\chi_3(a_2)=
 \chi_3(b_0)=\chi_3(b_1)=\chi_3(b_2)=1.
\]

This is an explicit $\mu_3$ quotient of the degree-four defect lattice.  It is
not thereby a class in $H^2(U;\mu_3)$, a bundle-lifting obstruction, or a
connection holonomy.  Comparing it with determinant-page monodromy requires a
phase-retaining lift and an explicit degree-changing morphism.

This is a characteristic-lattice character. It is not automatically the
centre holonomy of an $SU(6)$ bundle and it is not the Standard-Model lifting
class in $H^2(-;\mu_6)$. Those live in different degrees and on different
spaces; identifying them requires an explicit Gysin, transgression, or
differential-cohomology morphism compatible with the line-operator pairing.

### The adjoint $S^8$ and the Gram-boundary $S^8$ are explicitly identified

Put

\[
 \mathfrak p=\operatorname{Herm}_3^0(\mathbb C),
 \qquad
 \mathcal C_{\mathrm{sing}}
 =\{Q\in\operatorname{Herm}_3(\mathbb C):Q\succeq0,\ \det Q=0\}.
\]

The maps

\[
 \Phi_{\mathrm G}(H)=H-\lambda_{\min}(H)I_3,
 \qquad
 \Psi_{\mathrm G}(Q)=Q-\frac{\operatorname{tr}Q}{3}I_3
\]

are inverse $SU(3)$-equivariant, positively homogeneous homeomorphisms.
Indeed, $\lambda_{\min}(\Psi_{\mathrm G}(Q))=-\operatorname{tr}(Q)/3$, so
both composites are the identity. They extend to

\[
 \boxed{
 \Phi_{\mathrm G}^+:\mathfrak p^+\xrightarrow{\cong}
 \mathcal C_{\mathrm{sing}}^+.}
\]

Under the left-$U(3)$ Gram quotient $A\mapsto Q=A^\dagger A$, the residual
right $SU(3)$-action is conjugation on $Q$. Hence this identifies the adjoint
representation sphere with the compactified rank-loss boundary of the
three-column Gram cone, including its two walls:

\[
 \Phi_{\mathrm G}\bigl(t\operatorname{diag}(2,-1,-1)\bigr)
 =3t\operatorname{diag}(1,0,0),
\]

\[
 \Phi_{\mathrm G}\bigl(t\operatorname{diag}(1,1,-2)\bigr)
 =3t\operatorname{diag}(1,1,0).
\]

This bridge identifies the two $S^8$ carriers, but not the toroidal cusp. A
generic conjugacy orbit is $SU(3)/T^2$, which is simply connected, whereas the
required regular fibre of a Fabel-style higher-rung map is $T^6$, with
fundamental group $\mathbb Z^6$.

### An exact pointwise map from the candidate period form to the Gram boundary

Retain the unnormalized Appell--Humbert inverse-dual matrix on a regular cusp
fibre:

\[
 G_{\eta,T}=
 \begin{pmatrix}2L_T&2m_T\\2m_T&-q_T/3\end{pmatrix},
 \qquad
 \det G_{\eta,T}=-\frac23D_T<0.
\]

Embed it without altering its entries by

\[
 \iota(K)=\operatorname{diag}(K,-\operatorname{tr}K)
 :\operatorname{Herm}_2(\mathbb C)longrightarrow
  \operatorname{Herm}_3^0(\mathbb C),
\]

and use the already proved equivariant homeomorphism to define

\[
 \boxed{
 \Psi_T=\Phi_{\mathrm G}(\iota(G_{\eta,T}))
 =\iota(G_{\eta,T})
  -\lambda_{\min}(\iota(G_{\eta,T}))I_3
 \in\partial\operatorname{Herm}_3(\mathbb C)_{\geq0}.}
\]

This is a literal pointwise map; no descent to the base or compatibility with
any singular filling is being assumed.  The exact cusp limits
$L_T/T\to1$, $m_T/T\to0$, and $q_T/T\to1$ give

\[
 \frac1T\iota(G_{\eta,T})
 \longrightarrow\operatorname{diag}\!\left(2,-\frac13,-\frac53\right),
\]

and hence

\[
 \boxed{
 \frac1T\Psi_T
 \longrightarrow
 \operatorname{diag}\!\left(\frac{11}{3},\frac43,0\right).}
\]

If one additionally records, without replacing the preceding unnormalized
limit, the trace-one section, then

\[
 \frac{\Psi_T}{\operatorname{tr}\Psi_T}
 \longrightarrow
 \operatorname{diag}\!\left(\frac{11}{15},\frac4{15},0\right).
\]

The two positive eigenvalues are distinct, so the candidate cusp ray lands in
the principal rank-two stratum, with conjugacy orbit $SU(3)/T^2$, and not in
either $\mathbb{CP}^2$ focal stratum.  This gives an exact candidate-derived
point of the Gram boundary, not an identification of a $T^4$ or $T^6$ fibre.

For later comparison, if $K\in\operatorname{Herm}_2(\mathbb C)$,
$s=\operatorname{tr}K$, $p=\det K$, and $H=\iota(K)$, then direct expansion
without diagonalizing $K$ gives

\[
 c_2(H)=s^2-p,
 \qquad c_3(H)=-sp,
 \qquad
 \boxed{\Delta(H)=(s^2-4p)(2s^2+p)^2},
\]

where $c_2(H)=\tfrac12\operatorname{tr}(H^2)$,
$c_3(H)=\det H$, and $\Delta=4c_2^3-27c_3^2$.  On the future determinant-null
cone $p=0$, $s=2h>0$, one has

\[
 c_3=0,
 \qquad \Delta=256h^6>0.
\]

Thus the $(3,1)$ determinant-null cone maps to the regular
cubic-Casimir-zero locus, not to the repeated-eigenvalue wall.  The
non-Cartan spectrum of $-\operatorname{ad}_{iH}^2$ closes at $\Delta(H)=0$,
not merely at $c_3(H)=0$; this remains a classical adjoint
Yang--Mills--Higgs mass matrix, not a pure quantum Yang--Mills Hamiltonian.

### What the nine-dimensional packet adds, and what it cannot identify

The independently checked additive content of
"Nine_Dimensional_Color_Gram_Cone_20260903.zip" is as follows.

- The determinant phase gives an open book on the phase-retaining quotient
  $S^{10}$, with binding the rank-defect $S^8$ and closed page $B^9$. Upstairs,
  the interior of the angle-zero page is $SL(3,\mathbb C)$, and one circuit
  has geometric monodromy $A\mapsto\zeta_3A$; this scalar lies in the left
  $SU(3)$ centre, so the monodromy becomes the identity after quotienting.
- The real fixed form gives a standard quotient sphere
  $\operatorname{Mat}_{3\times3}(\mathbb R)^+/SO(3)\cong S^6$, with
  determinant binding $S^5$. This is a topological real-form sphere, not the
  reconstructed complex $S^6$, its $T^4\to X\to\mathbb P^1$ fibration, or its
  singular fillings. Indeed, the Gram binding has codimension one and
  disconnected complement, while the candidate's three special fibres have
  codimension two and connected complement.
- The complex Gram complement has fundamental group $\mathbb Z$; the
  candidate regular locus surjects onto
  $\pi_1(\mathbb P^1\setminus\{p_0,p_1,p_2\})\cong F_2$. The two complements
  cannot be the same torus-bundle geometry.
- The rank-one locus is $\mathbb{CP}^2$. Its transverse Hessian for the
  determinant is $\det K=t^2-x_1^2-x_2^2-x_3^2$ on
  $\operatorname{Herm}_2(\mathbb C)$, and the maximal faces form the
  nontrivial bundle $\operatorname{Herm}(Q)\to\mathbb{CP}^2$, with
  $w_2(\mathfrak{su}(Q))\equiv h\pmod2$ and
  $p_1(\mathfrak{su}(Q))=-3h^2$. This is a twisted family of exact $(3,1)$
  normal cones, not a spacetime or a $T^6$-fibration.
- The quadratic irreducible normal equation at $\mathbb{CP}^2$ is not the
  three-branch candidate germ $z_0z_1z_2=0$, and the Gram multiplicities two
  and three do not supply the candidate's transverse multiplicities three
  and four.
- The homogeneous split $SU(3)$ connection on
  $\mathcal O(-1)\oplus Q\cong\underline{\mathbb C}^3$ over
  $\mathbb{CP}^2$ is a classical Yang--Mills critical point with action
  $6\pi^2/g_{\mathrm{YM}}^2$ in the packet's normalization, and its explicit
  action-drop path makes it an unstable classical saddle. The affine chart
  is $\mathbb C^2$, but its restricted Fubini--Study metric is not Euclidean;
  no flat-space quantum mass-gap claim follows.

### Next bounded Pro calculation: globalize the elliptic extension

The next task is no longer to identify the Gram cone with the candidate; the
natural stratified identification is obstructed. Start instead from the
proved local map $\overline F:N_3^C\to N_0$ and the lifted
$(3,4,\infty)$ integral monodromy triple. Construct, or prove impossible, a
proper complex or explicitly stratified-real map

\[
 \widetilde f:\widetilde X^8\longrightarrow\mathbb P^1
\]

and a map over the same base

\[
 \Pi:\widetilde X\longrightarrow X
\]

such that:

1. on every regular fibre, $\Pi$ is the elliptic extension induced by
   $\Phi=P\oplus Q$;
2. at the cusp, $\Pi$ is the toric morphism
   $\overline F:N_3^C\to N_0$ with the displayed filling square;
3. at the order-three and order-four fibres, its affine monodromies are
   $\widetilde A_j=A_j\oplus C_j$, its translations are $(v_j,0)/m_j$, and
   the quotient maps project exactly to the candidate fillings;
4. all period matrices, overlap maps, cocycles, freeness, properness, and
   extension identities are written explicitly;
5. the based van Kampen pushout and all integral Mayer--Vietoris maps are
   computed from the actual boundary inclusions.

Two exact subsidiary calculations now feed this globalization problem.  First,
derive the transformation law of $G_\eta$ from the full marked period law
$\Pi(gz)=R_g(z)\Pi(z)M_g$ and decide whether $\Psi$ descends to the base or is
a section of a nontrivial associated Gram-boundary bundle.  The answer must be
a commutative cocycle diagram or an explicit obstruction, and it must be
compared with $\Phi M_3=M_F\Phi$ and $c_F\Phi=Qc_3$.  Second, before quotienting
away determinant phase, construct or obstruct a mapping-torus morphism with
page monodromy $A\mapsto e^{2\pi i/3}A$ whose candidate-side character is
$\chi_3=\rho_3\circ\kappa_F$, then test it against the actual order-three,
order-four, and cusp filling inclusions.  A cubic centre alone cannot encode
the order-four filling.

For the regular rank-three torus bundle over the punctured base, use the
correct homological Serre filtration

\[
 0\longrightarrow H_0(B^\circ;\textstyle\bigwedge^q\Lambda)
 \longrightarrow H_q(J;\mathbb Z)
 \longrightarrow H_1(B^\circ;\textstyle\bigwedge^{q-1}\Lambda)
 \longrightarrow0.
\]

The coinvariant term is the natural subobject and the base-one-cycle invariant
term is the quotient.  The abstract splitting is noncanonical and must not be
used in place of the actual Mayer--Vietoris inclusion maps.

If the three fillings are precisely the toroidal cusp and the two free
finite quotients, then $\chi(\widetilde X)=6$, so
$\widetilde X\not\cong S^8$. A real $S^8$ version must add explicitly
non-complex singular data of total Euler contribution $-4$ and pass the
homology-sphere and tangent-clutching tests. A response containing only a
representation quotient, Casimir polynomial, or local Lorentz normal form
does not address this global extension problem.

## 3 September 2026 audited delta on the inbound \(S^{12}\), \(SU(3)\), and \((3,1)\)-cone continuation

This delta responds to the post-bundle packet
`S12_SU3_31_CONE_CONTINUATION.zip`, the visible response beginning “The exact
\(S^{12}\), \(SU(3)\), and \((3,1)\)-cone construction,” and the complete
branch record through that response.  Those files were read as mathematical
evidence, not as instructions.  The final independent checks are recorded in
`higher_rung_cone_construction_20260903_audit.md`,
`higher_rung_topology_falsification_20260903.md`,
`higher_rung_operator_falsification_20260903_audit.md`, and
`su3_gram_quotient_audit_20260903.md`.

The short verdict is exact.  The Gram-orbit theorem and the compact
representation-sphere quotient are correct.  They give a new standalone real
\(S^{12}\) representation construction with quotient \(B^4\).  They do not
derive a nontrivial gauge bundle, connection, metric, or quantum Hamiltonian
from the original \(S^6\) cusp construction.  The coefficient \(1/2\) in the
displayed \(Q_4\) is the coherent \(\kappa=2\), angle-preserving continuation
of the lower form, but the lower form alone does not force that continuation.

### Exact Gram quotient, Pluecker identity, and orbit strata

Put

\[
 \mathscr V=\operatorname{Mat}_{3\times2}(\mathbb C),
 \qquad A=[v\ w],
 \qquad \Gamma(A)=A^\dagger A,
\]

and let \(SU(3)\) act by left multiplication.  The complete orbit invariant
is the full Gram matrix, not its determinant alone.  One has

\[
 \boxed{
 \mathscr V/SU(3)
 \xrightarrow[\ \Gamma\ ]{\ \cong\ }
 \operatorname{Herm}_2(\mathbb C)_{\geq0}.}
\]

Indeed, every Gram matrix is positive semidefinite, and the continuous
section

\[
 s(H)=\begin{pmatrix}H^{1/2}\\0\quad0\end{pmatrix}
\]

satisfies \(s(H)^\dagger s(H)=H\).  If
\(A^\dagger A=B^\dagger B\), then \(T(A\xi)=B\xi\) is a well-defined
isometry \(\operatorname{im}A\to\operatorname{im}B\).  Extend it to
\(U_0\in U(3)\).  Because \(\operatorname{rank}A\leq2\), a nonzero
orthogonal complement remains; changing \(U_0\) on that complement by
\(\det(U_0)^{-1}\) gives \(U\in SU(3)\) with \(B=UA\).  Thus the Gram
fibres are exactly the \(SU(3)\)-orbits, and the displayed section gives the
continuous inverse on the orbit space.

Writing

\[
 \Gamma(A)=
 \begin{pmatrix}
  \|v\|^2&\langle v,w\rangle\\
  \langle w,v\rangle&\|w\|^2
 \end{pmatrix}
 =
 \begin{pmatrix}
  h+y&x+iz\\x-iz&h-y
 \end{pmatrix},
\]

the determinant is exactly

\[
 \boxed{
 \det\Gamma(A)
 =\|v\|^2\|w\|^2-|\langle v,w\rangle|^2
 =\sum_{1\leq i<j\leq3}|v_iw_j-v_jw_i|^2
 =\|v\wedge w\|^2.}
\]

This is the \(2\times2\) Cauchy--Binet, or Gram--Pluecker, identity.  It
vanishes exactly at complex rank at most one.  It does **not** classify
orbits by itself: for example, the matrices with upper \(2\times2\) blocks
\(I_2\) and \(\operatorname{diag}(\sqrt2,1/\sqrt2)\) both have Gram
determinant one but have different Gram matrices.

On the full-rank locus \(\mathscr V_{(2)}\), the action is free and the
principal bundle is explicitly globally trivial:

\[
 \Phi:SU(3)\times\operatorname{Herm}_2(\mathbb C)_{>0}
 \xrightarrow{\ \cong\ }\mathscr V_{(2)},
 \qquad
 \Phi(U,H)=U\begin{pmatrix}H^{1/2}\\0\quad0\end{pmatrix}.
\]

For its inverse, take \(H=A^\dagger A\), set
\(Q=AH^{-1/2}=[q_1\ q_2]\), and complete the ordered orthonormal two-frame
by the unique \(q_3\) for which \([q_1\ q_2\ q_3]\in SU(3)\).  In
particular,

\[
 c_2\bigl(\mathscr V_{(2)}\to
 \operatorname{Herm}_2(\mathbb C)_{>0}\bigr)=0.
\]

The finite orbit types are

\[
\begin{array}{c|c|c|c}
 \operatorname{rank}_{\mathbb C}A&
 \dim_{\mathbb R}\mathscr V_{(r)}&
 \operatorname{Stab}_{SU(3)}(A)&
 \dim_{\mathbb R}(\mathscr V_{(r)}/SU(3))\\ \hline
 2&12&\{1\}&4\\
 1&8&SU(2)&3\\
 0&0&SU(3)&0.
\end{array}
\]

For \(n\geq3\), the same Gram argument gives
\(\operatorname{Mat}_{n\times2}(\mathbb C)/SU(n)
\cong\operatorname{Herm}_2(\mathbb C)_{\geq0}\).  What is special about
\(n=3\) is that it is the minimal value which absorbs the determinant phase
and makes the rank-two action free; for \(n>3\) the full-rank stabilizer is
\(SU(n-2)\).

### The \(Q_4\) coefficient is the \(\kappa=2\) choice, not a forced extension

With the coefficient of \(-\sum r_i^2\) fixed to one, every
permutation-invariant member of the relevant family can be written

\[
 Q_{n,\kappa}(r)
 =\frac{\kappa}{n}\left(\sum_{i=1}^n r_i\right)^2
  -\sum_{i=1}^n r_i^2.
\]

Let \(e_n=(1,\ldots,1)/\sqrt n\) and write
\(r=\alpha e_n+u\) with \(u\perp e_n\).  Then, without rescaling,

\[
 Q_{n,\kappa}(r)=(\kappa-1)\alpha^2-\|u\|^2.
\]

The lower Koide form is \(Q_{3,2}\), because its displayed coefficient is
\(2/3\).  Preserving \(\kappa=2\) in four variables gives

\[
 Q_{4,2}(r)=\frac12\left(\sum_{i=1}^4r_i\right)^2-sum_{i=1}^4r_i^2.
\]

This preserves the Euclidean null-cone angle: on a null ray,
\(\|u\|/|\alpha|=\sqrt{\kappa-1}=1\), so the angle from the diagonal is
\(\pi/4\).  It is also the unique coefficient for which the stated
orthogonal Hadamard coordinates give unit Lorentz coefficients:

\[
 Q_{4,2}=h^2-x^2-y^2-z^2.
\]

That makes \(1/2\) a natural, precisely specified choice.  It is not forced
by the three-variable formula without the extra rule “preserve \(\kappa\),”
or equivalently “preserve the cone angle.”  Preserving instead the literal
coefficient \(2/3\) gives \(\kappa=8/3\) in four variables, another
Lorentz-signature form with a different cone angle.  Do not call
\(Q_{4,2}\) the unique or unavoidable extension of \(Q_{3,2}\).

The slice \(z=0\) is exactly the old real-symmetric **coefficient** space.
It is not the coordinate inclusion of the old nonnegative three-mass-root
space into \(\mathbb R_{\geq0}^4\), and the unchanged \(S^6\) period matrix
does not acquire \(z\): its determinant is independent of the real parts of
\(\tau,\mu,\beta\).  Also, nonnegative \(r_i\) do not automatically land in
the Gram cone; \(r=(1,0,0,0)\) gives \(Q_{4,2}(r)=-1/2\).

The exact morphism between the two coefficient presentations is nevertheless
available.  If \(\mathcal F_3:\mathbb R^3\to\mathbb R^{1,2}\) is the
existing orthogonal Koide transform, \(\mathcal F_4\) is the displayed
Hadamard transform, and \(j(h,x,y)=(h,x,y,0)\), then

\[
 \iota=\mathcal F_4^{-1}\circ j\circ\mathcal F_3:
 \mathbb R^3\hookrightarrow\mathbb R^4,
 \qquad
 Q_{4,2}\circ\iota=Q_{3,2}.
\]

Thus the old form is related to the new one by a specified isometric
coefficient-space embedding; that embedding is not
\((r_1,r_2,r_3)\mapsto(r_1,r_2,r_3,0)\).

### The quotient is the future PSD cone, not all of \(\operatorname{Herm}_2(\mathbb C)\)

For

\[
 H=\begin{pmatrix}h+y&x+iz\\x-iz&h-y\end{pmatrix},
\]

the eigenvalues are

\[
 h\pm\sqrt{x^2+y^2+z^2}.
\]

Thus the determinant is the Lorentz quadratic form
\(h^2-x^2-y^2-z^2\) on the **ambient** real vector space
\(\operatorname{Herm}_2(\mathbb C)\cong\mathbb R^4\).  With positive
directions listed first, its signature is \((1,3)\); its negative has
signature \((3,1)\).  The Gram image is only

\[
 \operatorname{Herm}_2(\mathbb C)_{\geq0}
 =\{h\geq\sqrt{x^2+y^2+z^2}\},
\]

the closed future causal cone.  Its rank-two principal stratum is

\[
 \operatorname{Herm}_2(\mathbb C)_{>0}
 =\{h>\sqrt{x^2+y^2+z^2}\},
\]

the open future timelike cone.  Past-timelike and spacelike Hermitian
matrices are not Gram matrices.  The matrix logarithm is a diffeomorphism

\[
 \log:\operatorname{Herm}_2(\mathbb C)_{>0}
 \xrightarrow{\ \cong\ }
 \operatorname{Herm}_2(\mathbb C)\cong\mathbb R^4;
\]

it supplies global coordinates on the principal quotient but does not make
the PSD cone equal to all Hermitian matrices.

### The exact compact quotient is \(B^4\), and it is not the older cusp map

Let

\[
 S^{12}_{\mathrm{col}}=\mathscr V^+
\]

be the one-point compactification of the real twelve-dimensional
representation and fix the added point under \(SU(3)\).  Since

\[
 \|A\|_F^2=\operatorname{tr}\Gamma(A),
\]

the Gram map is proper and extends continuously to the added point.  It
therefore induces the exact homeomorphism

\[
 \boxed{
 S^{12}_{\mathrm{col}}/SU(3)
 \cong
 \bigl(\operatorname{Herm}_2(\mathbb C)_{\geq0}\bigr)^+
 \cong B^4.}
\]

Here the closed cone is homeomorphic to
\([0,\infty)\times\mathbb R^3\), whose one-point compactification is a
closed four-ball.  Its boundary orbit types are

\[
\begin{array}{c|c|c}
 \text{source stratum}&\text{quotient stratum}&\text{stabilizer}\\ \hline
 \operatorname{rank}A=2&\operatorname{int}B^4&\{1\}\\
 \operatorname{rank}A=1&\partial B^4\setminus\{p_0,p_\infty\}&SU(2)\\
 A=0&\{p_0\}&SU(3)\\
 A=\infty&\{p_\infty\}&SU(3).
\end{array}
\]

The identities

\[
 (\mathbb C^3)^+\wedge(\mathbb C^3)^+
 \cong(\mathbb C^3\oplus\mathbb C^3)^+
 =S^{12}_{\mathrm{col}}
\]

and \(S^6\wedge S^6\cong S^{12}\) are exact.  They do not identify this
action or orbit map with the previously constructed cusp-supported smash
map.  Transport to the proposed complex-threefold carrier
\(X\wedge X\) first requires an arbitrarily chosen based diffeomorphism
\(X\cong(\mathbb C^3)^+\).  The transported action depends on that choice
and carries neither the torus fibration, cusp monodromy, full-flux class
\(\eta\), nor the prior map \(q_2^{\wedge2}\).  The earlier sphere-valued
map \(S^{12}\to S^6\) is based null-homotopic; the new map has the different,
contractible codomain \(B^4\).  Neither \(S^{12}\) nor \(S^{24}\) is an
almost-complex successor sphere.

Do not conflate three different operations:

\[
 \bigl(\operatorname{Herm}_2(\mathbb C)_{\geq0}\bigr)^+\cong B^4,
 \qquad
 \bigl(\operatorname{Herm}_2(\mathbb C)_{>0}\bigr)^+\cong S^4,
 \qquad
 D(B^4)\cong S^4.
\]

The first retains the finite rank-one boundary.  The second replaces all
directions escaping the open principal stratum by one point and discards
that finite boundary.  The third doubles the ball along its orbit-type
boundary.  A homeomorphism of the resulting underlying spaces does not
supply a principal-bundle gluing map.

### The flat \(\mathbb R^4\) Yang--Mills Hessian is standard and uses an added metric

The response chooses \(X=\log H\) and declares

\[
 g_{\log}=\frac12\operatorname{tr}(dX\,dX).
\]

This is a valid complete flat Euclidean metric on the quotient after the
chosen logarithmic identification.  It is not induced from the Frobenius
metric on \(\mathscr V\), and it is not the Lorentz determinant form.  The
difference is already exact on \(H(s)=sI_2\).  For the horizontal lift
\(A(s)=\sqrt s\,(e_1\ e_2)\),

\[
 \|\dot H\|_{\mathrm{Frob\ quotient}}^2
 =\frac{\dot s^2}{2s},
 \qquad
 \|\dot H\|_{\log}^2
 =\frac{\dot s^2}{s^2}.
\]

Their ratio is not constant.  The flat metric is therefore additional
geometric input, not an inherited metric consequence of the orbit theorem.
It sends approach to the rank-deficient boundary to infinite logarithmic
distance and is not a smooth metric extension over the compact orbit ball.
A compact \(B^4\) metric would therefore define a different operator problem,
including a required choice of boundary realization.

With that metric and the explicit product bundle, the zero connection is a
classical solution of the usual nonlinear \(SU(3)\) Yang--Mills functional.
Its Coulomb Hessian is the standard transverse free Laplacian

\[
 \mathcal L_0=g_{\mathrm{YM}}^{-2}d^*d,
 \qquad
 \operatorname{Dom}\mathcal L_0
 =H^2(\mathbb R^4;\Lambda^1\otimes\mathfrak{su}(3))
  \cap\ker d^*,
\]

and Fourier transformation gives

\[
 \operatorname{Spec}(\mathcal L_0)
 =\operatorname{Spec}_{\mathrm{ess}}(\mathcal L_0)
 =\operatorname{Spec}_{\mathrm{ac}}(\mathcal L_0)=[0,\infty),
 \qquad
 \operatorname{Spec}_{\mathrm p}(\mathcal L_0)=\varnothing,
 \qquad
 \ker\mathcal L_0=0.
\]

That calculation is correct, but it is the standard zero-charge classical
flat-vacuum linearization.  It is not the spectrum of an interacting quantum
Yang--Mills Hamiltonian.  It is not placed on the nonzero-flux torus bundle,
and neither its bundle nor its connection is inherited from the \(S^6\)
cusp or earlier \(S^{12}\) construction.  The number \(24\) here counts
Euclidean Coulomb one-form components at nonzero Fourier momentum; without a
Lorentzian or Osterwalder--Schrader reconstruction it is not a count of
physical Minkowski particle polarizations.

### Exact \(c_2\) status and the next calculations Pro should perform

The present Gram construction already answers one possibility: on the open
principal stratum its bundle is trivial.  If its displayed product framing
is extended across the point at infinity using that same framing, the
clutching map is constant, so

\[
 [g]=0\in\pi_3(SU(3))\cong\mathbb Z,
 \qquad \langle c_2,[S^4]\rangle=0.
\]

A nonzero class on \(S^4\) requires a new transition map
\(g:S^3\to SU(3)\).  It is not selected by \(A^\dagger A\), the Pluecker
norm, or the existing global section.  The full \(B^4\) orbit projection
cannot simply be doubled as a principal bundle because its boundary has
\(SU(2)\) and \(SU(3)\) stabilizers.

The native cusp construction supplies a different, genuinely nontrivial
fibrewise bundle on \(F_T\cong T^4\): for a trace-zero weight
\(\mathbf m=(m_1,m_2,m_3)\),

\[
 \mathscr E_{\mathbf m,T}
 =\bigoplus_{j=1}^3\mathscr L_{\eta,T}^{m_j},
 \qquad
 c_2(\mathscr E_{\mathbf m,T})
 =-\frac12\left(\sum_jm_j^2\right)[\eta_T]^2.
\]

Its Chern number is \(-6\sum_jm_j^2\) in the marked orientation and
\(+6\sum_jm_j^2\) in the physical complex orientation.  For
\((1,0,-1)\), these are \(-12\) and \(+12\), respectively.  This class
does not extend over \(X\cong S^6\) or either \(S^{12}\) sphere, whose
degree-four cohomology vanishes.  Every map \(f:S^{12}\to S^4\) satisfies
\(f^*H^4(S^4)=0\), so it cannot transfer a nonzero \(c_2\) back to
\(S^{12}\).

There is a strongest noncanonical comparison which should not be understated
or promoted.  After choosing a degree-one collapse
\(c_T:F_T\to S^4\), classification of \(SU(3)\)-bundles over a
four-complex by \(c_2\) gives a topological isomorphism

\[
 \mathscr E_{\mathbf m,T}\cong c_T^*P_{k_{\mathbf m}},
 \qquad
 k_{\mathbf m}=-6\sum_jm_j^2
\]

in the marked orientation.  The collapse and the target bundle are extra
choices; this is not a canonical descent from \(S^6\) or the representation
sphere.  Moreover, the native constant-curvature connection cannot equal the
smooth pullback of a connection on \(S^4\) along any smooth map
\(F_T\to S^4\).  Its Chern--Weil four-form is nowhere zero; such a pullback
would force the map to have rank four everywhere, hence to be a covering
\(T^4\to S^4\), which is impossible.

The next useful Pro calculation is therefore not another repetition of the
flat Fourier Hessian.  Carry out the following exact constructions in order:

1. Fix which \(S^4\) is meant: the one-point compactification of the open
   cone, the boundary collapse \(B^4/\partial B^4\), or the double
   \(D(B^4)\).  Write the actual continuous maps from the Gram quotient and
   from any proposed total space; do not identify these three operations by
   dimension alone.
2. On two four-ball charts, derive an actual transition map
   \(g:S^3\to SU(3)\) from the proposed compactification, boundary
   resolution, or double.  Compute its signed class in
   \(\pi_3(SU(3))\cong\mathbb Z\).  The existing global section gives the
   constant class; any nonzero answer must exhibit and justify genuinely new
   boundary data and its independence from the arbitrary transport
   \(X\cong(\mathbb C^3)^+\).
3. If a nonzero class is obtained, give the full bundle map and commutative
   classifying diagram that proves
   \(c_2(\mathscr E_{\mathbf m,T})=c_T^*c_2(P_k)\), with the marked and
   physical orientations both recorded.  Equality of the integers \(12\)
   is only a numerical match unless this morphism is constructed.  A route
   through \(S^{12}\to S^4\) is already ruled out by \(H^4(S^{12})=0\).
4. Define the connection as well as the bundle.  Compute whether it extends
   over the chosen compactification or double and whether its curvature and
   Chern--Weil form pull back to the native cusp connection.  The smooth
   pullback of that native connection to or from \(S^4\) is already ruled
   out, so a surviving object must be explicitly new, singular, or governed
   by a different map.
5. If a canonical geometric Yang--Mills claim is intended, compute the
   Frobenius-induced quotient metric and its Levi-Civita/Hodge data rather
   than silently replacing it by \(g_{\log}\).  If a quantum mass-gap claim
   is intended, the still-missing objects are a reflection-positive
   Euclidean measure or transfer matrix, the physical gauge-invariant
   Hilbert space and Hamiltonian, and controlled state/energy maps.  The
   classical flat Hessian supplies none of them.

Until those computations produce an actual clutching and connection map, the
correct boundary is:

\[
 \boxed{
 \begin{array}{c}
 \text{four-dimensional future Gram quotient: proved;}\\
 S^{12}_{\mathrm{col}}/SU(3)\cong B^4:\text{ proved;}\\
 \text{explicit full-rank bundle: trivial, }c_2=0;\\
 \text{nontrivial native fibrewise }SU(3)\text{ flux: proved on }T^4;\\
 \text{canonical nontrivial clutching/connection transfer to }S^4:
 \text{ not constructed.}
 \end{array}}
\]

## Current homotopy-status correction

Both full sphere carriers are based null-homotopic while remaining surjective
quotient maps.  The two nullity proofs are different.  For every based map
\(f:S^6\to S^2\), there is an exact factorization

\[
 S^{12}=S^6\wedge S^6
 \xrightarrow{\ f\wedge\operatorname{id}_{S^6}=\Sigma^6f\ }
 S^2\wedge S^6=S^8
 \xrightarrow{\ \operatorname{id}_{S^2}\wedge f\ }
 S^2\wedge S^2=S^4.
\]

Freudenthal stability gives
\(\pi_{12}(S^8)\cong\pi_4^{\mathrm S}=0\), so the first arrow and hence
\(f\wedge f\) are based null-homotopic.  Associativity gives

\[
 f^{\wedge r}=(f\wedge f)\wedge f^{\wedge(r-2)},
 \qquad
 [f^{\wedge r}]=0\in\pi_{6r}(S^{2r})
 \quad(r\ge2).
\]

Consequently
\([\widehat q_\gamma^{\wedge2}]=0\in\pi_{12}(S^4)\), every
\(f^{\wedge r}\) with \(r\ge2\) is null, and the full surjective quotient
\[
 \widehat q_\gamma^{\wedge4}:S^{24}\twoheadrightarrow S^8
\]
is globally based null-homotopic.  Its point-set surjectivity and exact
moving-slice geometry are unchanged.

For every based map \(g:S^6\to S^3\), bifunctoriality gives the exact
factorization
\[
 g\wedge g=(\Sigma^3g)\circ(\Sigma^6g):
 S^{12}\longrightarrow S^9\longrightarrow S^6.
\]
Let \(\operatorname{st}\) denote stabilization.  The exact data
\[
 \pi_6(S^3)\cong\mathbb Z/12,\qquad
 \pi_3^{\mathrm S}=\mathbb Z/24\langle\nu\rangle,\qquad
 \pi_6^{\mathrm S}=\mathbb Z/2\langle\nu^2\rangle,
\]
\[
 \pi_{12}(S^6)=\mathbb Z/2\langle\nu_6\circ\nu_9\rangle,\qquad
 \operatorname{st}:\pi_{12}(S^6)\xrightarrow{\cong}\pi_6^{\mathrm S}
\]
use the group table in Hatcher, p. 339, and the signed smash/stabilization
calculation in Toda, Propositions 3.1 and 5.11.  Since \(12[g]=0\),
\(\operatorname{st}([g])=2a\nu\) for some \(a\in\mathbb Z/12\), and
multiplicativity gives
\[
 \operatorname{st}([g\wedge g])
 =\operatorname{st}([g])^2
 =4a^2\nu^2=0.
\]
The displayed stabilization isomorphism forces
\([g\wedge g]=0\in\pi_{12}(S^6)\).  Taking \(g=\widehat q_3\) proves that
\[
 \widehat q_3^{\wedge2}:S^{12}\twoheadrightarrow S^6
\]
is also globally based null-homotopic.  Associativity makes every
\(g^{\wedge r}\), \(r\ge2\), null as well.  The one-copy classes
\([\widehat q_3]\in\pi_6(S^3)\) and
\([\widehat q_\gamma]\in\pi_6(S^2)\) remain uncomputed.  The unstable
classes of the conical-target maps
\(q_2^{\wedge2}:S^{12}\to\mathcal A^{\wedge2}\) and
\(q_1^{\wedge4}:S^{24}\to\mathcal C^{\wedge4}\) remain **OPEN**, and the
class of
\(q_{1,\mathrm{cusp}}^{\wedge4}:S^{24}\to\mathcal B^{\wedge4}\) is likewise
uncomputed.  Nullity of the sphere-valued postcompositions does not imply
nullity of any of those maps before postcomposition.

## Temporal order and response to the inbound construction

The response beginning “There are three exact constructions” was produced
before this feedback was supplied to ChatGPT Pro mode. Its verbatim text is
preserved in
`WEB_PRO_MODE_PRE_FEEDBACK_RESPONSE_2026-09-03.md`; the present section is
the local workbench's independent answer to that pre-feedback baseline.

The transcript shows a precise near miss.  The response's doubled construction

\[
 F_T^2\xrightarrow{\ \pi_T\times\pi_T\ }Q_T^2
 \longrightarrow\mathbb R^4
\]

is the correct local seed.  It then dismissed an (S^{12}) interpretation by
observing that (X\times X\not\simeq S^{12}).  That observation is true but
tests the wrong global object.  The based quotient
(q_2:(X,x_0)\to(\mathcal A,v_0)) is constant on the global fat wedge, so its
smash square has source
(X\wedge X\cong S^6\wedge S^6\cong S^{12}); the radial subspace (F_T^2)
does not meet that global fat wedge and the smash quotient restricts there to
the displayed product map.  This is not a claim that the torus map
(\pi_T\times\pi_T), based at the fibre identity, factors through
(F_T\wedge F_T): it does not.  The distinction between the global basepoint
(x_0\in W) and a regular-fibre identity is essential.

## Three distinct theorems: native, sphere-carried, and covered

These constructions have different domains and must not be substituted for
one another.

1. **Native unchanged-fibre theorem.**  For the original regular fibres
   \(F_T=\mathbb R^4/P_T\mathbb Z^4\), the periods \(e_1,e_3\) retain length
   one, so
   \[
    \operatorname{sys}(F_T)\leq1,\qquad
    (F_T,o_T)\longrightarrow
    (\mathbb T^2_{\mathrm{re}}\times\mathbb R^2,(0,0)).
   \]
   Every fixed-radius ball is eventually exactly isometric to the
   corresponding ball in \(\mathbb T^2\times\mathbb R^2\).  Equivalently,
   there is an exact sequence
   \[
    0\longrightarrow\mathbb T^2_{\mathrm{re}}
    \longrightarrow F_T\xrightarrow{\ \pi_T\ }
    Q_T\longrightarrow0,
    \qquad \operatorname{sys}(Q_T)\geq T-C_{\mathrm{sys}}.
   \]
   This uses neither a fibre cover nor a base change and is the result
   directly derived from the original \(S^6\)-candidate family.

2. **Requested no-cover \(S^{12}/S^{24}\) theorem.**  Keep those same fibres.
   After a based choice \(X\cong_{\mathrm{diff}}S^6\), the two-copy
   cusp-supported quotient and four-copy full-base quotient give
   \[
    q_2^{\wedge2}:S^{12}\cong X^{\wedge2}
       \twoheadrightarrow\mathcal A^{\wedge2},
    \qquad
    q_1^{\wedge4}:S^{24}\cong X^{\wedge4}
       \twoheadrightarrow\mathcal C^{\wedge4}.
   \]
   Composing with explicit angle-forgetting quotients gives
   \(\widehat q_3^{\wedge2}:S^{12}\twoheadrightarrow S^6\) and
   \(\widehat q_\gamma^{\wedge4}:S^{24}\twoheadrightarrow S^8\).  Both full
   maps are based null-homotopic, as proved in the current homotopy-status
   correction above, while their one-copy classes remain uncomputed.  Their
   radial restrictions are
   \[
    F_T^2\longrightarrow Q_T^2\longrightarrow
       S_T^2\wedge S_T^2,
    \qquad
    F_T^4\longrightarrow C_T^4\longrightarrow C_T^{\wedge4}.
   \]
   The two moving four-spheres have pointed local
   \(\mathbb R^4\) limits, and deleting their smash basepoints gives literal
   embedded open cells \(\mathbb R^4\hookrightarrow S^6\) and
   \(\mathbb R^4\hookrightarrow S^8\).  No covering lattice or cyclic base
   change occurs.  Two copies are minimal for the native cusp-local
   rank-four quotient; four are minimal for a rank-four quotient surviving
   full-base monodromy, with the unscaled induced quotient metric.
   The copies of \(\mathbb R^4\) are open only in those moving four-spheres,
   not in the ambient \(S^6\) or \(S^8\); under every fixed compatible
   compact-target metric the unrescaled slices collapse, and no
   almost-complex or Yang--Mills conclusion follows.

3. **Ancillary finite-cover theorem.**  Replacing the lattice by
   \(S_N\mathbb Z^4\), \(S_N=\operatorname{diag}(1,1,N,N)\), gives a
   degree-\(N^2\) holomorphic cover
   \[
    \widetilde F_{T,N}=
    \mathbb R^4/P_TS_N\mathbb Z^4\longrightarrow F_T.
   \]
   It assembles around the punctured cusp only after the cyclic base change
   \(t=v^N\), because
   \[
    S_N^{-1}M_0^NS_N=M_0,
    \qquad
    \operatorname{sys}(\widetilde F_{T,N})
       \geq\min\{T-C_{\mathrm{sys}},N\}.
   \]
   Thus \(T,N\to\infty\) gives a pointed local
   \(\mathbb R^4\) limit.  The later Kummer repair extends this construction
   through the central fibre as a finite map of completed **local** cusp
   families, but it constructs neither a cover over the full original base
   nor a cover of compact \(X\).  This theorem is mathematically valid, but
   it changes both the fibre lattice and the cusp base and therefore is not
   the requested no-cover \(S^{12}/S^{24}\) construction.

The rest of this section supplies the exact target geometry and limitations
for item 2, then audits item 3 against the pre-feedback response.

### Exact target geometry for the \(S^{12}/S^{24}\) construction

The finite-cover theorem answers an easier question than the one asked.  The
requested construction starts with the native
\(\mathbb T^2\times\mathbb R^2\) cusp quotient and asks whether copies of the
completed \(S^6\)-candidate produce a global sphere-carried
\(\mathbb R^4\) decompactification.  That question now has the following exact
answer.  After a based choice \(X\cong_{\mathrm{diff}}S^6\), there are
continuous surjective based quotient maps

\[
 q_2^{\wedge2}:X^{\wedge2}\cong S^{12}
 \twoheadrightarrow\mathcal A^{\wedge2},
 \qquad
 q_1^{\wedge4}:X^{\wedge4}\cong S^{24}
 \twoheadrightarrow\mathcal C^{\wedge4},
\]

and further continuous surjective based quotient maps

\[
 \widehat q_3^{\wedge2}:S^{12}\twoheadrightarrow S^6,
 \qquad
 \widehat q_\gamma^{\wedge4}:S^{24}\twoheadrightarrow S^8.
\]

Both full sphere-target quotients are based null-homotopic, while their
one-copy classes remain uncomputed.  The unstable conical-target classes of
\(q_2^{\wedge2}\) and
\(q_1^{\wedge4}\) remain **OPEN**; the class of
\(q_{1,\mathrm{cusp}}^{\wedge4}\) is likewise uncomputed.  The exact
factorization and vanishing group proving these assertions are recorded in
the current homotopy-status correction above.

The first sphere target contains moving based topologically embedded
four-spheres
\(S_T^2\wedge S_T^2\), obtained from two copies of the native expanding
quotient, and the second contains \(C_T^{\wedge4}\), obtained from four copies
of the unique full-monodromy-invariant expanding circle.  Equip these
topological subspaces separately with the quotient length metrics induced by
the Euclidean \(\ell^2\)-product metrics.  With midpoint basepoints, every
radius-\(R\) ball is exactly a
Euclidean four-ball once \(T-C_{\mathrm{sys}}>4R\), respectively once
\(\ell_T>4R\).  Hence both moving four-spheres converge to
\(\mathbb R^4\) in pointed local-isometric and pointed Gromov--Hausdorff
senses, with smooth convergence on the eventual exact Euclidean
neighborhoods.  The lattice ranks prove that two copies are minimal
for the cusp-local construction and four are minimal for a quotient defined
over the full regular base, using the unscaled quotient of the marked
Euclidean fibre metric.

There is also a literal global topological \(\mathbb R^4\) in each sphere
target.  Removing the smash basepoint gives
\[
 (Q_T\setminus K_T^{(1)})^2
 \cong(S_T^2\wedge S_T^2)\setminus\{*\}
 \cong\mathbb R^4\hookrightarrow S^6,
\]
\[
 (C_T\setminus\{0\})^4
 \cong C_T^{\wedge4}\setminus\{*\}
 \cong\mathbb R^4\hookrightarrow S^8.
\]
These are nonclosed open cells in the embedded four-spheres, not open subsets
of the ambient \(S^6\) or \(S^8\), and not globally Euclidean-isometric under
a fixed compatible compact-target metric.

The same calculation has an exact decompactification-space formulation.
There are Hausdorff second-countable topological five-manifolds with boundary
\(\mathfrak E_{12}\) and \(\mathfrak E_{24}\) whose positive fibres are
\(Q_{1/s}^2\) and \(C_{1/s}^4\), whose zero fibres are literally
\(\mathbb R^4\), and in which every fixed Euclidean ball embeds isometrically
in all sufficiently small positive fibres.  Continuous surjective comparison
maps to the compact cone carriers are homeomorphisms off the zero fibre and
collapse the entire \(\mathbb R^4\) boundary fibre to the cone vertex.  These
maps are nonproper and nonquotient, so they are not topological blow-downs or
resolutions and the compact carriers are not the quotients
\(\mathfrak E_\nu/\mathbb R^4\) via these maps.  The five-manifolds are
decompactification comparison spaces, not new compactifications or covers of
\(X\).

The limitations are equally exact.  The based inclusion maps
\[
 S_T^2\wedge S_T^2\hookrightarrow S^6,
 \qquad
 C_T^{\wedge4}\hookrightarrow S^8
\]
are null-homotopic.  These slice-inclusion statements are separate from the
global equalities
\([\widehat q_3^{\wedge2}]=0\in\pi_{12}(S^6)\) and
\([\widehat q_\gamma^{\wedge4}]=0\in\pi_{24}(S^8)\).  The compact cone targets are not
four-manifolds at their vertices.  For every fixed compatible metric on a
compact target the unrescaled slices collapse to the vertex.  A fixed
cusp-adapted length metric can recover the slice limits after moving-point
blow-up, but its full ambient bubbles are \(\mathbb R^8\) and
\(\mathbb R^{12}\), not \(\mathbb R^4\).  No metric on the source spheres,
almost-complex structure on \(S^{12}\) or \(S^{24}\), physical spacetime, or
interacting Yang--Mills mass-gap theorem follows from these quotient maps.

The auxiliary cover calculation is retained below because it proves a
different, valid local theorem.  In canonical notation, put

\[
 S_M=\operatorname{diag}(1,1,M,M),\qquad
 \Lambda^{(M)}=S_M\mathbb Z^4.
\]

The identity of \(\mathbb R^4\) induces a holomorphic local-isometric cover

\[
 \mathbb R^4/P_TS_M\mathbb Z^4\longrightarrow
 \mathbb R^4/P_T\mathbb Z^4
\]

of degree \(M^2\), with deck group \((\mathbb Z/M\mathbb Z)^2\). If
\(M_0=I+R\), then \(R^2=0\) and

\[
 S_M^{-1}M_0^MS_M=M_0.
\]

Consequently the fibre cover assembles after the cyclic base change
\(t_c=v^M\) over \(v\ne0\). Its systole is bounded below by
\(\min\{T-C,M\}\), so every sequence \(T_j,M_j\to\infty\) converges locally,
through eventual exact biholomorphic isometries on fixed bounded domains, to
\(\mathbb C^2\cong\mathbb R^4\).

The exact cover characters are

\[
 \widetilde\chi_{T,M,k}([x])
 =\exp\!\left(
  2\pi i\left\langle P_T^{-\mathsf T}S_M^{-1}k,x\right\rangle
 \right),\qquad k\in\mathbb Z^4.
\]

Pullback from the original fibre is precisely the deck-invariant sector
\(k\in S_M\mathbb Z^4\), equivalently
\(k_3\equiv k_4\equiv0\pmod M\). The other characters are genuinely new
cover modes. The norms of a basis of the cover momentum lattice are
\(O(T^{-1}),O(T^{-1}),O(M^{-1}),O(M^{-1})\); hence those momentum lattices
become locally dense in \(\mathbb R^4\) as \(T,M\to\infty\).

The following qualifications applied to that inbound construction as it
stood before the local Kummer repair below.

1. The response proved the relative cover only after base change over the
   punctured cusp.  At that stage it had no valid extension across the central
   fibre and no cover of the completed threefold \(X\).  For \(M=2\), it is a
   four-sheeted fibre
   cover after a two-sheeted base change; if one regards the composite over
   the original punctured base as a finite total-space map, its degree is
   \(2\cdot4=8\), not \(4\).
2. The unconditional pointed-\(\mathbb R^4\) statement uses the unscaled
   Euclidean quotient metric \(g_T\). For the pullback of
   \(\widehat g_T=D_T^{-1/2}g_T\), it requires
   \(M/D_T^{1/4}\sim M/\sqrt T\to\infty\). If every covering torus is instead
   normalized separately to volume one, no choice of \(M(T)\) gives a pointed
   smooth \(\mathbb R^4\) limit.
3. After exact Euclidean Coulomb reduction and deletion of harmonic
   one-forms, the cover Hessian eigenvalues are

   \[
    \frac{4\pi^2}{g_{\mathrm{YM}}^2}
    \left\lVert P_T^{-\mathsf T}S_M^{-1}k\right\rVert^2,
    \qquad k\ne0.
   \]

   The phrase “transverse polarization” here means a three-dimensional
   Euclidean Coulomb fibre, not the two physical polarizations of a
   reconstructed Minkowski particle.
4. The original \(k=e_1,e_2\) modes already close the scalar and reduced
   classical-Hessian gaps at order \(T^{-2}\). The covers repair the local
   geometry and add the two missing momentum directions; they are not needed
   merely to obtain an auxiliary eigenvalue tending to zero.
5. “Gaussian-quantized gap” was not a defined theorem in the inbound response:
   no Gaussian/Fock Hilbert space, Hamiltonian, Gauss-law quotient, treatment
   of zero modes, or quantization map was supplied there. Likewise the displayed Wick substitution
   is a correct identity of complexified bilinear forms, but it is not
   Osterwalder--Schrader reconstruction and supplies no physical Hamiltonian.

### Subsequent local Kummer repair

The local workbench subsequently constructed the missing central action.  For
an integer \(N\geq1\), set \(t=v^N\) and
\[
 C_N(v)=\frac1N C(v^N),\qquad
 c^{(N)}_{\bar\lambda}(v)
 =\exp\!\left(2\pi iC_N(v)\bar\lambda\right).
\]
On a copy of the same toric variety use
\[
 \Psi^{(N)}_{\bar\lambda}(\xi,v)
 =\left(c^{(N)}_{\bar\lambda}(v)
 v^{B_0\bar\lambda}\xi,v\right).
\]
This is the correct source action.  It is free and properly discontinuous.
Writing
\[
 f_N:N_0^{\langle N\rangle}\longrightarrow\Delta_v
\]
for the quotient map, \(f_N\) is proper and holomorphic with smooth
threefold source, and its reduced irreducible nonnormal central fibre
\[
 W_N=(f_N^{-1}(0))_{\mathrm{red}}
\]
has normalization \(\mathrm{dP}_6\).  The toric power map
\[
 P_N(\xi_1,\xi_2,v)=(\xi_1^N,\xi_2^N,v^N)
\]
is equivariant because
\((c^{(N)}_{\bar\lambda}(v))^N=c_{\bar\lambda}(v^N)\).  It therefore descends
to a finite flat degree-\(N^3\) map
\[
 \kappa_N:N_0^{\langle N\rangle}\longrightarrow N_0,
 \qquad \kappa_N^*W=NW_N,
 \qquad \operatorname{Ram}(\kappa_N)=(N-1)W_N.
\]
After factoring through the normal base change
\(N_0[N]=N_0\times_{\Delta_t}\Delta_v\), the relative map \(Q_N\) has
generic degree \(N^2\).  For \(N>1\) it is quasi-étale but not flat: its
non-étale and nonflat loci are exactly the inverse images of the double and
triple strata.  At those strata the closed-fibre lengths are respectively
\(2N-1\) over local generic rank \(N\), and
\(3N^2-3N+1\) over generic rank \(N^2\).  On the central normalization it is
the toric map
\([N]:\mathrm{dP}_6\to\mathrm{dP}_6\), of degree \(N^2\), ramified with
index \(N\) along all six toric boundary curves.  Over \(v\ne0\), this is
exactly the original degree-\(N^2\) cover with deck group
\((\mathbb Z/N\mathbb Z)^2\).

This repairs the completed *local cusp family*.  It is not a degree-\(N^2\)
self-map over the unchanged disc, is not a normalization map, and supplies no
cover over the entire base \(B\): the sublattice still fails to be invariant
under the full original monodromy for \(N>1\), and compatibility with both
finite fillings would require an additional construction.

Independently of that local Kummer repair, there is an exact full-regular-base
quotient result.  Put
\[
 K_\Lambda=\mathbb Z\langle\widehat w,\widehat\delta\rangle,\qquad
 L_\Lambda=\mathbb Z\langle\widehat u,\widehat w,\widehat\delta\rangle.
\]
The first lattice is the two-dimensional compact kernel in the native cusp,
but it is not preserved by the full monodromy:
\[
 A_1\widehat w=\widehat u-\widehat w,\qquad
 A_2\widehat w=-\widehat u+\widehat\delta.
\]
The smallest full-monodromy-invariant lattice containing \(K_\Lambda\) is
\(L_\Lambda\); both lattices are primitive.  Moreover,
\[
 \operatorname{Hom}(\Lambda,\mathbb Z)^\Delta
 =\mathbb Z\varepsilon_\gamma,\qquad
 \varepsilon_\gamma(a\widehat\gamma+b\widehat u+
 c\widehat w+d\widehat\delta)=a.
\]
Thus the regular family is a genuine family of complex Lie groups and has a
monodromy-compatible real group quotient with connected three-torus kernel.
In the quotient metric its circle circumference is
\[
 \ell_T=\frac1{\lVert P_T^{-\mathsf T}e_\gamma\rVert}
     =\frac{D_T}{\sqrt{L_T^2+m_T^2}}
     =T+H-B+O(T^{-1}).
\]
The fourfold fibre product of \(X^\circ=f^{-1}(B^\circ)\) therefore has a
real fibrewise-group \(\mathbb T^4\) quotient over the full regular base, and its
synchronized radial fibres converge pointed-smoothly to \(\mathbb R^4\).
Four copies are minimal for a monodromy-invariant quotient whose kernel kills
each native compact \(K_\Lambda\).

The two finite fillings extend after simultaneous-root normalization to
explicit Seifert targets; the normalization degrees on their reduced central
fibres are \(3^3=27\) and \(4^3=64\).  The toric cusp is different.  Two
explicit paths approach the same triple point while the circle character is
constantly \(3/4\) on one and \(1/2\) on the other.  Therefore neither the
literal circle map nor its fourfold product extends continuously through the
cusp.  Moreover, no finite base cover globalizes the native two-copy quotient:
for \(H_*=A_2A_1=I+N_*\), \(N_*^2=0\), one has
\[
 H_*^n\widehat w=\widehat w+n(\widehat u-\widehat\delta),
\]
so every positive power still moves the native compact kernel.

The literal fixed-target quotient is therefore not an \(S^{24}\) construction.
One has
\[
 X^4\simeq(S^6)^4\not\simeq S^{24}.
\]
Although \(X^{\wedge4}\cong S^{24}\), the unmodified four-circle quotient on
the product is nonconstant on the fat wedge and therefore does not factor
through the smash product.  Borel--Serre, §15, Proposition 15.1, also proves that neither
\(S^{12}\) nor \(S^{24}\), with any differentiable structure, admits an
almost-complex structure.  These facts remain exact restrictions on any
literal product-target or almost-complex-sphere interpretation.

### The actual cone/smash answer to S12 and S24

The later cone construction answers the sphere-carrier question by changing
the codomain at the collapsed loci, so it does not contradict the literal
nonextension just proved.

For the native cusp quotient, let
\[
 \mathcal A=\operatorname{Susp}(S^1\times\overline T^2)
 \cong\operatorname{Susp}(T^3).
\]
There is a continuous surjective based quotient
\(q_2:(X,x_0)\to(\mathcal A,v_0)\) which retains the native quotient on
\(N_0\setminus W\), collapses \(W\) to one suspension vertex, and collapses
\(X\setminus\operatorname{int}N_0\) to the other.  Hence
\[
 q_2^{\wedge2}:X\wedge X\cong S^{12}
 \longrightarrow\mathcal A\wedge\mathcal A
\]
is a global based map after a based choice of the diffeomorphism
\(X\cong S^6\).  On two synchronized positive radial fibres it is
exactly
\[
 \pi_T\times\pi_T:F_T^2\longrightarrow Q_T^2,
 \qquad \operatorname{sys}(Q_T^2)\geq T-C,
\]
and \((Q_T^2,0)\to(\mathbb R^4,0)\) in pointed local-isometric, pointed
smooth, and pointed Gromov--Hausdorff topology.  The global codomain
\(\mathcal A^{\wedge2}\) is explicitly not a sphere or a compact
four-manifold: its reduced homology has ranks
\(9,18,15,6,1\) in degrees \(4,5,6,7,8\).

For the full-base invariant circle quotient, glue the regular target
\(P\times S^1\) to the two finite Seifert targets and cone the remaining cusp
boundary torus.  This produces a compact Hausdorff finite CW space
\(\mathcal C\) and a continuous surjective based quotient
\[
 q_1:(X,x_0)\longrightarrow(\mathcal C,c_0),
 \qquad
 q_1^{\wedge4}:X^{\wedge4}\cong S^{24}
 \longrightarrow\mathcal C^{\wedge4}.
\]
Here again the sphere identification uses a based choice of
\(X\cong S^6\).  On four synchronized radial fibres, the latter map is exactly
\[
 \chi_{\gamma,T}^{\times4}:F_T^4\longrightarrow C_T^4,
 \qquad
 \operatorname{sys}(C_T^4)=\ell_T=T+H-B+O(T^{-1}),
\]
and \((C_T^4,0)\to(\mathbb R^4,0)\) in the same three pointed senses.  Here
the entire cusp boundary two-torus, including its target circle, is collapsed
to the cone vertex.  The reduced homology of \(\mathcal C^{\wedge4}\) has
ranks \(1,4,6,4,1\) in degrees \(8,9,10,11,12\), so again the codomain is a
specified stratified carrier, not a sphere.  The strengthened construction
also composes the one-copy maps with explicit angle-forgetting quotients to
give
\[
 \widehat q_3^{\wedge2}:S^{12}\twoheadrightarrow S^6,
 \qquad
 \widehat q_\gamma^{\wedge4}:S^{24}\twoheadrightarrow S^8,
\]
whose target spheres contain the moving four-spheres described in the scope
correction above.  Those four-spheres are null-homotopic in their ambient
spheres, and the two sphere-to-sphere maps induce zero on positive-degree
integral homology and cohomology.  Both full sphere-target maps are based
null-homotopic, while their one-copy classes remain uncomputed.  This does not
settle the unstable classes of the conical-target maps \(q_2^{\wedge2}\) and
\(q_1^{\wedge4}\), which remain **OPEN**; the class of
\(q_{1,\mathrm{cusp}}^{\wedge4}\) is likewise uncomputed.  These cone/smash
maps are the mathematically responsive
\(S^{12}/S^{24}\) answer; they do not turn either source sphere into an
almost-complex sphere or a physical spacetime.  The interacting
four-dimensional Yang--Mills conclusion remains **OPEN**.

### Exact compact-link and Gaussian corrections

The compact-link calculation now fixes the following points exactly.

1. For \(N_{\mathrm{mesh}}\geq2\), transporting the standard
   \(N_{\mathrm{mesh}}\)-cubical subdivision by
   \(P_{T,M_{\mathrm{cov}}}\) gives a cell decomposition of the entire cover
   torus, but its vertex map is a bijection only onto the finite torsion
   subgroup
   \[
    (\mathbb Z/N_{\mathrm{mesh}}\mathbb Z)^4
    \xrightarrow{\ \cong\ }
    \widetilde F_{T,M_{\mathrm{cov}}}[N_{\mathrm{mesh}}],
    \qquad[n]\mapsto
    [P_{T,M_{\mathrm{cov}}}n/N_{\mathrm{mesh}}].
   \]
   The vertices are not the whole torus.
2. With \(U_A'(t)=-A(\dot\gamma(t))U_A(t)\) and
   \(A^g=g^{-1}Ag+g^{-1}dg\), the forced endpoint order is
   \[
    \operatorname{Hol}(A^g)_{n,j}
    =g(\gamma_{n,j}(1))^{-1}\operatorname{Hol}(A)_{n,j}
      g(\gamma_{n,j}(0)).
   \]
   For inverse-transport variables \(\mathcal U=\operatorname{Hol}^{-1}\),
   it becomes
   \(\mathcal U(A^g)=g(\gamma(0))^{-1}\mathcal U(A)g(\gamma(1))\).
   This endpoint-reversed correction is essential to the plaquette gauge law.
3. The cover index \(M_{\mathrm{cov}}\) and mesh count
   \(N_{\mathrm{mesh}}\) are independent.  Cover decompactification requires
   \(T,M_{\mathrm{cov}}\to\infty\), while resolution of the varying physical
   torus requires the distinct condition
   \[
    \max_r\frac{\|P_{T,M_{\mathrm{cov}}}e_r\|}
                    {N_{\mathrm{mesh}}}\longrightarrow0,
   \]
   equivalently \(N_{\mathrm{mesh}}/\max\{T,M_{\mathrm{cov}}\}\to\infty\)
   along the stated radial bounds.  The exact example
   \(T_j=j^2\), \(M_{\mathrm{cov},j}=j\),
   \(N_{\mathrm{mesh},j}=j^3\) satisfies both requirements.
4. The periodic diagonal \(SU(2)\) links have
   \(U_{12}(n)=\exp(2\pi H_{\mathrm{link}}/N_{\mathrm{mesh}}^2)\) at every
   plaquette and all
   other positively ordered plaquettes trivial.  Their exact logarithmic
   action is
   \[
    S^{\log}=
    \frac{2\pi^2M_{\mathrm{cov}}^2}{g_{\mathrm{YM}}^2D_T},
   \]
   and the explicitly defined continuum-matched \((1,2)\)-sector Wilson
   functional converges to the same value as
   \(N_{\mathrm{mesh}}\to\infty\).
5. On the finite real Coulomb space with harmonic cochains removed, the exact
   Hessian eigenvalues are
   \[
    \lambda(k)=g_{\mathrm{YM}}^{-2}
    \left\|P_T^{-\mathsf T}S_{M_{\mathrm{cov}}}^{-1}
    \mathfrak d_{N_{\mathrm{mesh}}}(k)\right\|^2,
   \]
   with complex transverse multiplicity nine.  The Friedrichs Gaussian
   oscillator on the corresponding Lebesgue \(L^2\)-space has a unique ground
   state and gap \(\sqrt{\lambda_{\min}}\); on the displayed diagonal sequence
   that gap and the logarithmic action both tend to zero while the cover tends
   pointed-locally to \(\mathbb R^4\) and the mesh resolves it.
6. The finite Gaussian theorem instead lives on a noncompact linear Coulomb
   slice with Lebesgue measure.  It is not a theorem about either compact-link
   Haar space
   \[
    L^2(\mathrm{SU}(2)^E,dU)
    \quad\text{or}\quad
    L^2(\mathrm{SU}(2)^E,dU)^{\mathrm{SU}(2)^V}.
   \]
   Both displayed spaces use product normalized Haar measure; the latter
   additionally imposes the nonlinear vertex Gauss law.  The exponential map
   is only a local chart,
   has derivative \(N_{\mathrm{mesh}}^{-1}\) at zero, is not globally
   injective or measure preserving, and supplies no unitary identification.
   A link configuration gives a Dirac distribution, not an \(L^2\) Haar
   vector.  No nonlinear compact-link Hamiltonian, Gauss-law spectral problem,
   transfer matrix, or Osterwalder--Schrader reconstruction has been proved.

Preserve canonical notation: \(B_T=\operatorname{Im}b_T\) is a scalar, so
the response's projected \(2\times2\) matrix is called \(Y_T\); the
base-change coordinate is \(v\), because \(s=\tau-h\) is already fixed.

## Canonical cusp notation

The proved period matrix is

\[
 Z_T=
 \begin{pmatrix}
 6\mu_T&h_T+iT\\
 b_T-h_T-iT&\mu_T
 \end{pmatrix},
 \qquad
 \Pi_T=[Z_T\mid I_2].
\]

Write

\[
 \mu_T=\alpha_T+i m_T,
 \quad h_T=\eta_T+iH_T,
 \quad b_T=\xi_T+iB_T,
 \quad c_T=\xi_T-\eta_T,
\]

\[
 L_T=T+H_T,
 \qquad q_T=L_T-B_T,
 \qquad D_T=L_Tq_T+6m_T^2>0.
\]

In the ordered real coordinates
\((\operatorname{Re}\zeta_1,\operatorname{Im}\zeta_1,
\operatorname{Re}\zeta_2,\operatorname{Im}\zeta_2)\),

\[
 P_T=
 \begin{pmatrix}
 6\alpha_T&\eta_T&1&0\\
 6m_T&L_T&0&0\\
 c_T&\alpha_T&0&1\\
 -q_T&m_T&0&0
 \end{pmatrix},
 \qquad \det P_T=-D_T.
\]

Do not reuse `L_T` for a line bundle; the magnetic line bundle is
\(\mathscr L_T\).  Do not reuse `H` for either Lie-algebra generator:
\(H_{\mathrm{mag}}=\operatorname{diag}(i,-i)\) belongs to the magnetic
calculation, while
\(H_{\mathrm{link}}=\operatorname{diag}(i,-i)\) belongs to the compact-link
calculation.

## Verified exact results extending T1/T2/T3

1. The full matrix \(P_T^{-\mathsf T}\), not merely its first two columns,
   has been derived and checked symbolically.  For
   \(k=(r,s,0,0)^{\mathsf T}\),

   \[
   P_T^{-\mathsf T}k
   =\left(0,\frac{m_Tr+q_Ts}{D_T},0,
             \frac{-L_Tr+6m_Ts}{D_T}\right)^{\mathsf T}.
   \]

   Hence the two coordinate squared lengths are

   \[
   a_{\gamma,T}=\frac{L_T^2+m_T^2}{D_T^2},
   \qquad
   a_{u,T}=\frac{q_T^2+36m_T^2}{D_T^2}.
   \]

2. With the explicitly chosen Euclidean quotient metric on the regular
   fibre, the exact first scalar eigenvalue is

   \[
   \lambda_1(F_T,g_T)=4\pi^2\min\{a_{\gamma,T},a_{u,T}\}
   \]

   for all sufficiently large \(T\), and

   \[
   \lambda_1(F_T,g_T)
   =\frac{4\pi^2}{T^2}
   \left(1+\frac{-2H+2\min\{B,0\}}{T}+O(T^{-2})\right),
   \]

   where \(H=\operatorname{Im}h(0)\) and
   \(B=\operatorname{Im}b(0)\).  The unit-volume metric
   \(\widehat g_T=D_T^{-1/2}g_T\) also closes the gap, but at the different
   rate

   \[
   \lambda_1(F_T,\widehat g_T)
   =\frac{4\pi^2}{T}\bigl(1+O(T^{-1})\bigr).
   \]

   Thus the exact rates belong to specified metric families; neither is an
   invariant of the complex family alone.

   The complete fixed-energy law is stronger than the first-eigenvalue
   statement.  If \(N_T(E)\) counts scalar eigenvalues with Fourier
   multiplicity, then for every fixed \(E\geq0\),
   \[
    N_T(E)=\pi D_T\sum_{n\in\mathbb Z^2}
      \left(\frac{E}{4\pi^2}-\lVert n\rVert^2\right)_+
      +O_E(T).
   \]
   In the first transverse band \(0<E<4\pi^2\), this becomes
   \[
    N_T(E)=\frac{ED_T}{4\pi}+O_E(T)
          =\frac{ET^2}{4\pi}+O_E(T).
   \]
   Thus a two-dimensional density of low modes, not merely one soft mode,
   grows on the order of the fibre covolume.

3. The single auxiliary direct-integral operator

   \[
   \mathscr L_{\mathrm{aux}}
   =\int_{T_0}^{\infty}{}^\oplus\Delta_{F_T}\,dT
   \]

   on the mean-zero normalized-Haar spaces is now defined with its exact
   self-adjoint multiplication domain.  The disjoint-support vectors
   \(\mathbf1_{[n,n+1]}(T)e^{2\pi i y_1}\) are an orthonormal singular
   sequence, so

   \[
   0\in\sigma_{\mathrm{ess}}(\mathscr L_{\mathrm{aux}}),
   \qquad \ker\mathscr L_{\mathrm{aux}}=0.
   \]

   This is a genuine proved gapless operator statement.

4. The continuum Yang--Mills Hessian at the trivial connection, after
   removal of harmonic modes and exact Coulomb reduction, is

   \[
   g_{\mathrm{YM}}^{-2}d^*d,
   \]

   and its first reduced eigenvalue is

   \[
   \gamma_T=\frac{4\pi^2}{g_{\mathrm{YM}}^2}
   \min\{a_{\gamma,T},a_{u,T}\}.
   \]

   A finite cubical cochain model has also been defined with its Hilbert
   metric, adjoint, exact Fourier symbol, Coulomb projection, and all mesh
   regimes.  It is a finite quadratic gauge operator; it has not been
   identified with an interacting Wilson transfer matrix or a quantum
   Yang--Mills Hamiltonian.

5. The integral coframe obeys

   \[
   \theta_T^1\wedge\theta_T^2=D_T^{-1}dy_1\wedge dy_2.
   \]

   The unit-flux line bundle is \(\mathscr L_T\), and
   \(E_T=\mathscr L_T\oplus\mathscr L_T^{-1}\) is topologically trivial as
   a rank-two complex bundle.  The seam trivialization must use the correct
   endpoint convention: if \(K(0)=I\) and \(K(1)=\gamma\), then the
   well-defined map on the mapping-torus presentation uses \(K(t)^{-1}w\),
   not \(K(t)w\).

   More generally, every fixed nondegenerate integral alternating form
   \(\mathsf E\) on the marked four-torus defines an explicit Hermitian line
   bundle and constant-curvature magnetic Laplacian.  Its spectrum is
   \[
    \{(2n_1+1)b_1+(2n_2+1)b_2:
      n_1,n_2\in\mathbb Z_{\geq0}\},
   \]
   where
   \[
    b_1b_2=\frac{4\pi^2|\operatorname{Pf}(\mathsf E)|}{D_T}.
   \]
   Hence the first distinct level spacing obeys
   \[
    2\min\{b_1,b_2\}
    \leq4\pi\sqrt{\frac{|\operatorname{Pf}(\mathsf E)|}{D_T}}
    =O(T^{-1}).
   \]
   This is fibrewise in the marked cusp and does not assert that the flux
   class globalizes through the full monodromy.

6. The reducible nonflat \(SU(2)\) connection is a classical Yang--Mills
   critical point with action

   \[
   \operatorname{YM}_T(\nabla^T)
   =\frac{2\pi^2}{g_{\mathrm{YM}}^2D_T}.
   \]

   The explicit theta section in the \(X_+\)-root line produces a
   background-gauge Jacobi eigenform with

   \[
   \mathcal J_Ta=-\frac{4\pi}{D_T}a.
   \]

   Thus this reducible critical point is unstable; the negative eigenvalue
   tends to zero as \(T\to\infty\).  This is a classical Hessian statement,
   not a physical particle-mass statement.

7. The Koide quadratic relation admits an exact ambient coefficient-space
   identity.  In orthogonal coordinates

   \[
   h=\frac{r_1+r_2+r_3}{\sqrt3},
   \quad
   x=\frac{r_1-r_3}{\sqrt2},
   \quad
   y=\frac{r_1-2r_2+r_3}{\sqrt6},
   \]

   one has

   \[
   Q_K(r)=\frac23(r_1+r_2+r_3)^2-(r_1^2+r_2^2+r_3^2)
         =h^2-x^2-y^2.
   \]

   Under

   \[
   (\operatorname{Im}\tau,\operatorname{Im}\mu,
     \operatorname{Im}\beta)
   =\left(h+y,\frac{x}{\sqrt6},h-y\right),
   \]

   the canonical real period determinant equals \(Q_K(r)\).  This is an
   isomorphism of ambient real coefficient spaces and quadratic forms.  It
   is not a map to regular fibres: on the Koide cone the determinant is zero,
   whereas the actual radial cusp satisfies
   \(\det P_T=-D_T\sim-T^2\ne0\).

8. The exceptional first-coordinate elliptic quotient has now been proved on
   the actual period image.  For

   \[
   \mathcal A_z=\mathbb C^2/
   \mathbb Z\langle(6\mu,\beta),(\tau,\mu),(1,0),(0,1)\rangle,
   \]

   the first coordinate induces a surjective holomorphic homomorphism
   \(\mathcal A_z\to\mathbb C/(\mathbb Z\tau+\mathbb Z)\) if and only if

   \[
   6\mu=a\tau+b,
   \qquad (a,b)\in\mathbb Z^2.
   \]

   The pair is unique; the kernel is connected and is

   \[
   \mathbb C/\bigl(\mathbb Z+\mathbb Z(a\mu-\beta)\bigr),
   \qquad
   \operatorname{Im}(a\mu-\beta)=-D_{\mathrm{can}}>0.
   \]

   The marked labels transform exactly as

   \[
   g_0:(a,b)\mapsto(a,a+b),
   \qquad
   g_2:(a,b)\mapsto(-b,6+a).
   \]

   Their union is monodromy invariant, has finite image in the completed
   orbifold base, and misses a punctured cusp neighborhood.  Therefore this
   particular elliptic quotient cannot be the cusp gap-closing sector.  It
   does not follow that there are no other elliptic quotients, elliptic
   subtori, Neron--Severi classes, or smooth integral magnetic fluxes.

## T1 Koide arithmetic audit

The following exact arithmetic is valid but independent of the S6 fibre
construction.  For

\[
 \Delta(x,y,z)=4(xy+xz+yz)-(x^2+y^2+z^2),
\]

the reduced positive solutions

\[
 0<x\le y\le z,\qquad \Delta=-1,\qquad z\ge4(x+y)
\]

are in bijection with

\[
 a>0,\quad q,n\ge0,\quad a+4n>q,\quad
 a^2-3q^2-18n^2=-2
\]

through

\[
 n=z-4(x+y),\quad q=y-x,\quad a=x+y-4n,
\]

with inverse

\[
 x=\frac{a+4n-q}{2},\qquad
 y=\frac{a+4n+q}{2},\qquad
 z=4a+17n.
\]

The local densities and real chamber factor also check:

\[
 \sigma_2=\frac32,
 \qquad \sigma_3=2,
 \qquad
 \sigma_p=
 \frac{1-p^{-2}}{1-\left(\frac3p\right)p^{-1}}\quad(p\ge5),
\]

\[
 \mathfrak S
 =\frac92\frac{\log(2+\sqrt3)}{\sqrt3\,\zeta(2)},
 \qquad
 I_\infty=\frac1{2\sqrt3}\log\frac3{2\sqrt2}.
\]

The missing normalization step has now been completed, so one may present

\[
 R(X)\sim C_0X,
 \qquad
 C_0=\frac9{2\pi^2}\log(2+\sqrt3)
                 \log\frac3{2\sqrt2}
\]

as an unconditional theorem.  The proof uses the genuine norm

\[
 \|(a,q,n)\|_*=\max\{|4a+17n|,|q|,|a|\};
\]

on the stated chamber it equals \(4a+17n\).  The Satake-boundary
admissibility and genericity required by Gorodnik--Oh--Shah are proved
directly, and comparison of their invariant measure with Borovoi's theorem
on the same Euclidean balls gives the exact calibration
\(\kappa=\mathfrak S(\mathscr X)\).

The explicit \(2\)-adic matrix \(g\in\operatorname{SO}(F,\mathbb Z_2)\)
has spinor norm \(-17\), with \((-17,3)_2=-1\), and therefore gives a
measure-preserving sign-reversing bijection of the two finite adelic sign
sets.  Writing out Borovoi's orbit convention proves
\(c_{\mathscr X}=1\).  The argument needs a sign-reversing bijection, not an
involution; indeed \(g^2\ne I\).  The finite computation
\(R(200000)=7109\) is reproducible.  Only the proposed
\(O_\varepsilon(X^{1/2+\varepsilon})\) discrepancy remains **OPEN**.
None of this arithmetic supplies a morphism from a regular abelian-surface
fibre of the \(S^6\) family to the
defect-one integral shell, so it belongs in the separate Koide draft, with
only the determinant-boundary relation cross-referenced here.

## Exact Erdős--Straus/S6 terminal-matrix crosswalk

There is a separate exact bridge to the earlier divisor-shell work.  For a
prime \(p\equiv1\pmod{12}\), put

\[
 R_j=4j+3,\qquad a_j=\frac{p+R_j}{4},\qquad
 0\le j<\frac{p-1}{4}.
\]

For a selector state \(u\mid a_j^2\) satisfying
\(R_j\mid4u+p^\varepsilon\), \(\varepsilon\in\{0,1\}\), set

\[
 T=\frac{4u+p^\varepsilon}{R_j},\qquad
 \ell_0=\frac{T+1}{4},\qquad
 \ell_1=u-jT,\qquad \ell_2=1.
\]

Then \(T\equiv3\pmod4\),

\[
 12\ell_0-4\ell_1-3=p^\varepsilon,
\]

and the exact matrix identity is

\[
 \begin{pmatrix}1&-j\\0&1\end{pmatrix}
 \begin{pmatrix}R_j&-u\\4&-T\end{pmatrix}
 =\begin{pmatrix}3&-\ell_1\\4&1-4\ell_0\end{pmatrix}.
\]

The inverse is \(T=4\ell_0-1\), \(u=\ell_1+jT\).  Retaining
\(p,j,\varepsilon\), the positive orientation, and \(u\mid a_j^2\) gives a
literal bijection between the complete two-channel selector and this
normalized terminal slice.  The \(\varepsilon=0\) branch has terminal
parameter \(1\); the \(\varepsilon=1\) branch has terminal parameter \(p\).
This is an \(\operatorname{SL}_2(\mathbb Z)\) change of integral relators.  It
does not construct a geometric map from the reciprocal cubic to the S6
threefold and does not prove that the selector is nonempty for every prime.

## 3 September 2026 audit of the completed Jordan--toric Euler packet

The completed packet strengthens the earlier partial `6 = 3!` observation in
one precise direction.  Its determinant and order-cone calculations have now
been independently replayed and are correct after two typing repairs.

Fix the oriented cross-product matrix

\[
[a]_{\times}=
\begin{pmatrix}
0&-a_3&a_2\\
a_3&0&-a_1\\
-a_2&a_1&0
\end{pmatrix}.
\]

Every \(H\in\operatorname{Herm}_3(\mathbb C)\) is uniquely
\(H=S+i[a]_{\times}\), and exact expansion gives

\[
\boxed{\det\bigl(S+i[a]_{\times}\bigr)=\det S-a^{\mathsf T}Sa.}
\]

For \(S>0\), congruence by \(S^{-1/2}\) gives eigenvalues

\[
1-\sqrt{\frac{a^{\mathsf T}Sa}{\det S}},\quad
1,\quad
1+\sqrt{\frac{a^{\mathsf T}Sa}{\det S}},
\]

so

\[
S+i[a]_{\times}\succeq0
\iff a^{\mathsf T}Sa\leq\det S.
\]

For each **marked** positive symmetric monodromy form \(B\), the injective
real-linear section

\[
\ell_B(\lambda,a)=\lambda B+i[a]_{\times}
\]

satisfies

\[
\det\ell_B(\lambda,a)
=\lambda\bigl(\lambda^2\det B-a^{\mathsf T}Ba\bigr)
\]

and

\[
\boxed{
\ell_B^{-1}\!\left(\operatorname{Herm}_3(\mathbb C)_{\geq0}\right)
=\{(\lambda,a):\lambda\geq0,
  a^{\mathsf T}Ba\leq\lambda^2\det B\}.}
\]

The \(\lambda<0\) case is excluded exactly because
\(\operatorname{tr}\ell_B(\lambda,a)=\lambda\operatorname{tr}B<0\).
Thus the section is a literal future \((3+1)\)-Lorentz cone.

In the existing Lorentz coordinates

\[
H_2(t,x_1,x_2,x_3)=
\begin{pmatrix}
t+x_3&x_1-i x_2\\
x_1+i x_2&t-x_3
\end{pmatrix},
\]

the exact order-cone lift is

\[
\Theta(H_2)=
\begin{pmatrix}
t&-i x_3&-i x_2\\
i x_3&t&-i x_1\\
i x_2&i x_1&t
\end{pmatrix}.
\]

Its spectra are

\[
\operatorname{Spec}H_2=\{t-r,t+r\},\qquad
\operatorname{Spec}\Theta(H_2)=\{t-r,t,t+r\},
\]

where \(r^2=x_1^2+x_2^2+x_3^2\).  Hence

\[
H_2\succeq0\iff\Theta(H_2)\succeq0,
\qquad
\boxed{\det_3\Theta(H_2)=\frac{\operatorname{tr}H_2}{2}\det_2H_2.}
\]

On the positive cone it sends ranks \(2,1,0\) to \(3,2,0\).  In
particular a rank-one projection maps to a matrix with eigenvalues
\(0,1/2,1\), so \(\Theta\) is not a Jordan homomorphism.

Two corrections are essential:

1. The map \(\iota\) must be stated on the full real Jordan algebras
   \(\operatorname{Sym}_3(\mathbb R)\hookrightarrow
   \operatorname{Herm}_3(\mathbb C)\), and only then restricted to positive
   cones.  A positive cone is neither a vector space nor a Jordan algebra.
2. The asserted index-three translation-lattice compression is not
   constructed.  The exact six-to-two map is the already proved saturated
   rank drop

   \[
   P=\begin{pmatrix}1&-1&0\\0&1&-1\end{pmatrix}:
   \mathbb Z^3\twoheadrightarrow\mathbb Z^2,
   \qquad\ker P=\mathbb Z(1,1,1).
   \]

   The even Kuhn labels \((123),(231),(312)\) map to translates of one
   unimodular target triangle and the odd labels
   \((132),(213),(321)\) to translates of the other.  This changes lattice
   rank.  A unimodular triangulation of any rank-three lattice fundamental
   domain still contains \(3!=6\) maximal tetrahedra.
3. The stratum vector \((1,7,12,6)\) belongs to the nonnormal quotient
   central fibre \(W_3\).  Its smooth permutohedral normalization has toric
   orbit vector \((1,14,36,24)\); the normalization map has generic degrees
   \(2,3,4\) over the double, triple, and quadruple strata.
4. The globalization formula must retain its hypotheses: the map is proper
   and triangulable, it is locally trivial with regular fibre \(T^6\) away
   from finitely many critical values, and Euler additivity is applied with
   compact supports on the open base stratum.  Under those hypotheses an
   \(S^8\) total space requires the remaining singular fibres to contribute
   \(-4\).

The result is therefore an exact determinant/Lorentz section and an exact
Euler scalar identity,

\[
\chi(W_{3,B})=6\det B=6q_B(1,0),
\]

under the marked positive symmetric hypotheses.  It is **not** a morphism
from the Jordan cone to the toroidal family.  Neither \(\ell_B\) nor
\(\Theta\) contains an integral period lattice, monodromy action, or filling
homomorphism.  In the actual toric degeneration, the local parameter in
\(z_0z_1z_2z_3=t\) tends to zero while \(B=I_3\) stays fixed; this is not the
rank-drop operation \(\det B\to0\).

A useful next Pro calculation would have to supply a new typed object, not
another determinant identity: either construct a map from Jordan rank data
to the explicit period/lattice/filling square
\(\Phi M_3=M_F\Phi\), \(c_F\Phi=Qc_3\), and
\(PZ_3(t)=Z_2(t)Q\), or prove that no map satisfying those three equations
can arise from the determinant stratification.  The scalar identity alone
cannot decide that problem.

Packet SHA-256:
`8BA0BD7FD7BADEAAF2C44E2F2B4EFD42C25DA9119DA3180017FC488CA364E96F`.

## Corrections to avoid in subsequent Pro turns

- A complex structure, variation of Hodge structure, Leray page, or coherent
  direct image does not select a Riemannian metric or a self-adjoint spectral
  operator.  Do not infer a gap from those data alone.
- \(\lambda_1(T)\to0\) along a family does not make any one compact fibre
  gapless.  The direct-integral construction above is the proved single
  gapless auxiliary operator.
- A classical Hessian eigenvalue, magnetic Laplacian level, or finite-cochain
  eigenvalue is not the spectrum of the four-dimensional quantum theory.
- To transfer an auxiliary Rayleigh sequence, construct one fixed
  gauge-invariant positive-metric physical Hilbert space, its nonnegative
  self-adjoint Hamiltonian \(H\), the full zero-energy projection
  \(P_0=\mathbf1_{\{0\}}(H)\), and maps \(J_n\) for which the excitation norm
  does not collapse and the physical energy is uniformly bounded by the
  auxiliary quadratic form after all continuum, infinite-volume, and
  renormalization limits.  No such construction is presently in the S6
  corpus.  Therefore the auxiliary spectral statements are verified and the
  physical Yang--Mills implication is **OPEN**.
- Keep `conditional` for a theorem depending on an explicitly named known
  hypothesis.  Use **OPEN** for this missing physical construction.

## Reproducibility pointers

- Canonical exact sections:
  `supporting_materials/workbench/research/cusp_spectral_geometry.tex`,
  `cusp_toric_cover_completion.tex`, `cusp_cone_sphere_routes.tex`,
  `cusp_sphere_route_strengthening.tex`,
  `cusp_sphere_fixed_metric.tex`,
  `cusp_globalization_replacement.tex`, `cusp_compact_link_gaussian.tex`,
  `cusp_gauge_operators.tex`, `cusp_su2_magnetic.tex`,
  `koide_period_discriminant.tex`, `koide_counting_repair.tex`, and
  `cusp_spectral_interpretation.tex`; the exact selector crosswalk is
  `erdos_straus_selector_crosswalk.tex`.
- Shareable proof-bearing drafts:
  `s6_spectral_degeneration_preprint.tex`,
  `s6_cone_sphere_routes_preprint.tex`,
  `s6_compact_link_gaussian_preprint.tex`, and
  `koide_arithmetic_preprint.tex`.
- Exact symbolic verifier:
  `supporting_materials/reproducibility/verify_cusp_spectral_relations.py`.
- T1 packet SHA-256:
  `302909E18ED3930515256A05449C2B122E10E788A0AABC3E299B724CF4A89379`.
- T2 packet SHA-256:
  `397F5E9C3E1FB4020C94793099A5294057B53C3B0CB3AB014D9D188316269B5B`.
- Web-session transcript SHA-256:
  `D1229BF64322D9EFC74FDDC6979C9FA91864C3228A7F032F85BD55B70CC86D4B`.
- Pasted Turn-3 calculation SHA-256:
  `9F4B1430D09B04171F8858E6DA994E69B86E06CB02BC40A97062EA30D0214DAA`.

Inventory audited at the timestamp above: the workbench tree contains 48
files—three at its root, two under `comparative_context/`, three under
`reproduction/t1_koide_exact/`, 32 directly under `research/` (31
TeX components and its README), and eight under `research/ledgers/`.  The
current claim ledger has 65 VERIFIED, four OPEN, six REFUTED, and zero
CONDITIONAL entries.

## 3 September 2026 audit of the native full-flux magnetic packet

The packet `Native_T1_T2_Magnetic_Upgrade_Corrected.zip` contains a
substantial correct algebraic core, but three of its operator theorems are
not yet proved at the precision asserted.  The following formulas have been
recomputed independently from the displayed period matrix and integral
alternating form:

\[
 E_\eta=
 \begin{pmatrix}
 0&0&0&6\\0&0&1&0\\0&-1&0&0\\-6&0&0&0
 \end{pmatrix},
 \qquad
 \operatorname{Pf}(E_\eta)=6,
 \qquad
 \operatorname{SNF}(E_\eta)=\operatorname{diag}(1,1,6,6),
\]

\[
 \delta_R=6m_R^2-p_RT_R>0,
 \qquad
 \det P_R=-\delta_R,
\]

\[
 \mathcal B_{R,+}
 =\frac{\pi(S_R+\Xi_R)}{\delta_R},
 \qquad
 \mathcal B_{R,-}
 =\frac{\pi(\Xi_R-S_R)}{\delta_R},
 \qquad
 \mathcal B_{R,+}\mathcal B_{R,-}
 =\frac{24\pi^2}{\delta_R},
\]

\[
 \mathcal B_{R,+}=\frac{12\pi}{R}+O(R^{-2}),
 \qquad
 \mathcal B_{R,-}=\frac{2\pi}{R}+O(R^{-2}).
\]

The line-bundle cocycle and curvature are also correct, as are the exact
classical action identities and the algebraic Jacobi-band formula

\[
 \nu_{R,n}
 =2\bigl((2n+1)\mathcal B_{R,-}-\mathcal B_{R,+}\bigr)
 =\frac{4\pi}{\delta_R}
   \bigl(n\Xi_R-(n+1)S_R\bigr).
\]

For sufficiently large (R), the ratio
(5<\mathcal B_{R,+}/\mathcal B_{R,-}<7) makes precisely
(n=0,1,2) negative within this polarization branch, with leading terms
(-20\pi/R,-12\pi/R,-4\pi/R); the (n=3) term is (+4\pi/R+O(R^{-2})).

The characteristic number must be stated with its orientation.  In the
marked (y)-orientation,

\[
 \frac12\int_Y\eta^2=6,
 \qquad
 \left\langle c_2(L_\eta\oplus L_\eta^{-1}),[Y]_{\rm mark}\right\rangle=-12.
\]

Because (det P_R=-\delta_R<0), the marking is orientation reversing
relative to the standard complex orientation of the physical period torus.
Consequently the same bundle has complex-oriented Chern number (+12).
The action and spectral formulas are orientation independent.  Do not write
simply “(c_2=-12)” without naming the fundamental class.

Three proof repairs are required before the packet's strongest statements
can be used:

1.  Prove that every joint Landau level has complex multiplicity
    (lvert\operatorname{Pf}(E_\eta)\rvert=6), and that doubled root
    charge gives multiplicity
    (lvert\operatorname{Pf}(2E_\eta)\rvert=24).  The Pfaffian calculation
    alone is not the proof; one needs the compatible holomorphic/theta or
    Heisenberg representation, the ground-space dimension, ladder
    completeness, and the complex-versus-real multiplicity conversion.
2.  Define the full self-adjoint gauge-fixed Jacobi realization from its
    closed form, define the maximal covariant codifferential, prove that its
    kernel is a closed reducing Coulomb slice by the exact
    (\mathcal J^{\rm gf}d_A=d_A\Delta_A) resolvent intertwining, and only
    then deduce the claimed real Morse index (3\cdot(2\cdot24)=144).
3.  Form the radial direct integral over ((R_0,\infty)), not an endpoint at
    which the source family was never defined.  Define the varying-fibre
    operator by conjugation from the fixed measurable field and verify that
    the fibrewise resolvent lands in the maximal domain using
    \[
      \widetilde\Delta_R(\widetilde\Delta_R-z)^{-1}
      =I+z(\widetilde\Delta_R-z)^{-1}.
    \]

After the third repair, the Weyl sequence supported on ([j,j+1]) does
prove a precise auxiliary statement:

\[
 0\in\sigma_{\rm ess}(\mathscr M_\eta)
       \cap\sigma_{\rm c}(\mathscr M_\eta),
 \qquad \ker\mathscr M_\eta=0.
\]

It does not establish a result about the nonlinear quantum Yang--Mills
Hamiltonian.  The packet constructs a positive finite-fibre magnetic
Laplacian, a classical reducible Yang--Mills saddle and its Jacobi operator,
and an externally assembled radial direct integral.  It does not construct
the gauge-invariant positive-metric physical Hilbert space, Gauss-law
quotient, reflection-positive Euclidean measure, Osterwalder--Schrader
Hamiltonian, or renormalized comparison maps required to transfer these
spectra to four-dimensional quantum Yang--Mills theory.

The other new packet, `S12_Smash_Pairing_Null_Theorem.zip`, is correct but
does not change the canonical result: the workbench already proves the
stronger all-pairs identity

\[
 \pi_6(S^3)\times\pi_6(S^3)\longrightarrow\pi_{12}(S^6),
 \qquad(g,h)\longmapsto[g\wedge h],
 \qquad g\wedge h\simeq *,
\]

and the resulting nullity of every higher smash power.  This still does not
determine the one-copy class of the constructed map
(\widehat q_3:S^6\to S^3), nor the distinct conical-target homotopy class.

## 4 September 2026 bounded continuation request: construct the exact Lorentz observation bridge

Please take the following as the next calculation, not as a conclusion to
repeat.  Preserve every displayed matrix, scale, sign, action, domain, and
codomain.  Do not replace a failed identification by a claim of nonrelation:
if a proposed map fails, prove the scoped obstruction and construct the
strongest surviving morphism.

Retain

\[
 P=\begin{pmatrix}1&-1&0\\0&1&-1\end{pmatrix},\qquad
 u=\begin{pmatrix}1\\1\\1\end{pmatrix},\qquad
 C=PP^*=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},
\]

\[
 R_P=P^*C^{-1}
 =\frac13\begin{pmatrix}2&1\\-1&1\\-1&-2\end{pmatrix},
 \qquad
 \Pi_u=\frac{uu^*}{3},
 \qquad
 X=(R_P\;u).
\]

The local audit gives

\[
 PR_P=I_2,\qquad R_PP=I_3-\Pi_u,\qquad
 u^*R_P=0,\qquad \det X=1.
\]

The requested theorem should prove or falsify, line by line, the following
candidate bridge.

1. Define
   \[
   \mathcal O_P:\operatorname{Herm}_3(\mathbb C)\longrightarrow
   \operatorname{Herm}_2(\mathbb C),\qquad
   \mathcal O_P(H)=PHP^*,
   \]
   and
   \[
   \jmath_P(G)=R_PGR_P^*.
   \]
   Prove the exact split relation
   \(\mathcal O_P\jmath_P=\mathrm{id}\), classify the complete fibres of
   \(\mathcal O_P\) on the positive-semidefinite cone, and prove that its
   zero fibre is precisely the distinguished ray
   \(\{\lambda uu^*: \lambda\geq0\}\).

2. Use the unique block coordinates
   \[
   H=X
   \begin{pmatrix}G&z\\z^*&\lambda\end{pmatrix}X^*,
   \qquad
   G\in\operatorname{Herm}_2(\mathbb C),\ z\in\mathbb C^2,
   \ \lambda\in\mathbb R,
   \]
   and prove, without suppressing any coefficient,
   \[
   \mathcal O_P(H)=G,
   \qquad
   \det H=\lambda\det G-z^*\operatorname{adj}(G)z.
   \]
   Determine the exact positivity inequalities, including singular (G),
   and prove whether
   \[
   \operatorname{Herm}_3(\mathbb C)
   \cong
   \operatorname{Herm}_2(\mathbb C)\oplus\mathbb C^2\oplus\mathbb R
   \]
   becomes, under the action below, a Lorentz vector plus a Weyl spinor plus
   a real scalar.  This is the full (9=4+4+1) statement; none of the five
   remaining real directions may be discarded.

3. For (g\in SL_2(\mathbb C)), set
   \[
   T_P(g)=R_PgP+\Pi_u
   =X(g\oplus1)X^{-1}.
   \]
   Prove that (T_P:SL_2(\mathbb C)\to SL_3(\mathbb C)) is a homomorphism,
   that it fixes (u), and that congruence gives
   \[
   (G,z,\lambda)\longmapsto(gGg^*,gz,\lambda),
   \qquad
   \mathcal O_P(T_P(g)HT_P(g)^*)
   =g\mathcal O_P(H)g^*.
   \]
   Identify the induced (PSL_2(\mathbb C)\cong SO^+(1,3)) action on (G)
   and retain the nontrivial action of the central element (-I_2) on (z).

4. Prove the two determinant relations
   \[
   e_2(\jmath_P(G))=\frac13\det G,
   \qquad
   \det(uu^*+\varepsilon\jmath_P(G))
   =\varepsilon^2\det G,
   \]
   and determine exactly how the future timelike cone, null cone, and zero
   map into the rank-three positive cone and its rank-deficient boundary.
   Decide which maps are proper and which therefore extend to the actual
   one-point compactifications (B^4\) and (S^8\); do not assert a
   compactified map where properness fails.

5. Rewrite the already proved (SU(3))-orbit space
   \[
   \mathcal Y_3
   =\{(H,\omega):H\succeq0,
                   |\omega|^2=\det H\}
   \]
   in these block coordinates:
   \[
   |\omega|^2
   =\lambda\det G-z^*\operatorname{adj}(G)z.
   \]
   Prove the induced (SL_2(\mathbb C)) action and state exactly how the
   (omega=0) locus produces the rank-deficient (S^8) inside the
   compactified ten-real-dimensional carrier.  Relate this to the toroidal
   degeneration only through the marked angular map (P); (P) is not the
   filling map, (Q\beta) is not typed, and the previously proposed
   post-filling map (p_*:H_1(X^\circ)\to H_1(B^\circ)) does not exist.

6. Then continue beyond invariant theory.  Give the strongest explicit
   physical translation supported by the construction: specify the
   configuration or state space, gauge and Lorentz actions, observable map,
   action/Hamiltonian or constraint, engineering dimensions with every
   conversion constant retained, and a mathematically falsifiable spectral
   or dynamical consequence.  In particular, test the exact composite
   momentum candidate
   \[
   p(Z)=\alpha Z^*Z\in\operatorname{Herm}_2(\mathbb C)_{\succeq0},
   \qquad
   m^2(Z)=\det p(Z)
   =\alpha^2\sum_{a<b}|Z_{a1}Z_{b2}-Z_{a2}Z_{b1}|^2,
   \]
   for (alpha>0) retained.  Determine what dynamics can or cannot select
   a positive spectral threshold from this continuum.  “Not physics yet” is
   the start of this construction, not its endpoint; equally, do not call a
   formal resemblance a physical theorem before the state, dynamics,
   observables, and comparison regime have been proved.

Return a self-contained TeX theorem/proof module, an exact symbolic replay,
and a short list of any remaining maps together with the best construction
attempt for each one.

## 4 September 2026 bounded continuation request: audit the constrained threshold as a dynamical system

The returned `Exact_Lorentz_Observation_Bridge_20260904` packet proves the
finite-dimensional (9=4+4+1) decomposition and the hard algebraic bound

\[
 \det p\geq \frac{\alpha^2|\omega_0|^2}{\lambda_0}
 \quad\text{on}\quad
 \phi^*\phi=\lambda_0,
 \quad \det[Z\ \phi]=\omega_0\neq0.
\]

Do not repeat that calculation.  Adversarially determine whether the packet's
worldline action and Hilbert space actually realize the stated constrained
spectral model.  Retain (\alpha,c,\hbar,\lambda_0,\omega_0), every sign,
and every domain.

1. Starting from
   \[
   S=\int\!\left[
   p_\mu(Z)\dot x^\mu
   -\rho(\phi^*\phi-\lambda_0)
   -2\operatorname{Re}\!\left(
   \overline\chi(\det[Z\ \phi]-\omega_0)
   \right)\right]d\tau,
   \qquad p(Z)=\alpha Z^*Z,
   \]
   derive the complete Euler--Lagrange equations for
   (x,Z,\phi,\rho,\chi).  Compute the pulled-back presymplectic one-form,
   two-form, rank, characteristic distribution, all stabilizers, and the
   quotient by local left (SU(3)).  Decide exactly which trajectories are
   allowed and whether the equations force the lower threshold, allow every
   mass above it, or impose additional algebraic restrictions.

2. Compare that reduced classical system with the separately declared space
   \[
   L^2(\mathcal S_{\lambda_0,\omega_0},
       d\mu_{\lambda_0,\omega_0})^{SU(3)}.
   \]
   Either construct a genuine quantization map from the reduced phase space
   and show that the displayed multiplication operators are its observables,
   or prove the precise obstruction.  Determine the exact pushforward density
   in the global (\mathbb H^3\times\mathbb B^4) coordinates rather than
   invoking only full support, and prove essential ranges and absence or
   presence of point spectrum from that density.

3. Re-audit the claimed (SL_2(\mathbb C))-equivariant associated-ball model,
   proper momentum projection, little-group torsors, fixed-mass strata, and
   global section.  Check especially every square-root choice, action on the
   spinor coordinate, orientation, Jacobian, and the behavior at the threshold
   orbit.  Supply explicit inverse maps and commuting diagrams.

4. State the strongest theorem that survives with the correct evidential
   label.  A lower endpoint created by fixing (\lambda=\lambda_0) and
   (\omega=\omega_0\neq0) is a hard-selected kinematic threshold unless a
   dynamics or variational principle selects those constants.  Prove the exact
   morphism to any field-theoretic Hilbert space before making a Yang--Mills
   statement; otherwise give an obstruction theorem and the next admissible
   comparison map.

5. As a control, contrast the regular (\omega_0\neq0) stratum with the
   massless rank-one locus.  Since
   \[
   \det(\alpha Z^*Z)
   =\alpha^2\sum_{a<b}|\Delta_{ab}(Z)|^2,
   \]
   its differential vanishes at every rank-at-most-one (Z).  Determine the
   intrinsic rank-one tangent equations, the four real rank-opening ambient
   directions, the (SU(2)) stabilizer, the apex (Z=0), and whether a
   determinant-multiplier action is a regular constraint there.

Return a self-contained corrected TeX module, a line-numbered claim audit of
the supplied packet, exact symbolic checks, and explicit counterexamples for
every failed identification.  A separation between the action and the
postulated Hilbert space must be followed by the strongest exact relation
that can actually be constructed.
