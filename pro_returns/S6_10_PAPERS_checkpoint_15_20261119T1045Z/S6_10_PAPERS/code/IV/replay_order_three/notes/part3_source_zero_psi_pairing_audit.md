# Relative Xi/Psi and inserted-cap calibration for the source-zero return

Recovery record, 2026-11-17: this is a mathematical reconstruction of the complete PS.1–7 proof from the retained pre-outage messages. The original file and its exact bytes were absent from restored checkpoint19. The original proof received the root and checks audits used by P3K.89. No earlier source is overwritten.

## PS.1. The actual source level and its line

Retain the marked source, Cartier line, finite-root maps, and positive physical circle of P3K.80 and P3K.83. In the fixed-scalar source loop let
\[
 \Omega_+=dr_q\wedge d\alpha\wedge du\wedge dt\wedge d\gamma\wedge d\theta.
\]
The ordinary coefficient frame is the actual marked Tate frame. Choose a regular gamma level outside the prescribed decreasing short fixed-sphere arc. This level is the original nodal source neighbourhood \(E\), and misses the fixed-tube surgery and its connection changes. The map to the base is \(q\); its unique singular point has exact coordinates \(q=xy\).

Let \(U=M^{-1}\) denote the dual of the physical nonzero-vector line. The exact physical/dual and parameter arrows of P3K.68 give, in this comparison,
\[
 k_M=\int_{\Omega_+}F_U^3,\qquad
 \ell_M=\int_{\Omega_+}p_1F_U.
\]
These equalities retain the specified parameter reversal; they do not identify the two line representations.

Choose the actual graph maps \(b,\gamma\) with the prescribed boundary values \(t,\gamma_j\), constant on a nested neighbourhood \(U_2\) containing all surgery and connection changes in \(U_1\). Their theta-cut coefficient arrows are \(\exp(2\pi ib)\) and \(\exp(2\pi i\gamma)\). Write
\[
 \Xi=d\theta\wedge db,\qquad \Psi=d\theta\wedge d\gamma.
\]
Their products vanish because they share \(d\theta\).

## PS.2. The determinant frame and the relative source Pontryagin class

On the nodal chart use the extending complex volume \(\Omega=dx\wedge dy\), which is the literal expression of \(\omega_{\mathrm{ell}}\wedge dq\). Put
\[
 V=(x,-y),\qquad
 H=\frac{(\bar y,\bar x)}{R^2},\qquad R^2=|x|^2+|y|^2.
\]
Then \(dq(H)=\Omega(V,H)=1\). The actual logarithmic horizontal lifts on the two source charts are
\[
 H_x=(0,1/x)=H-\frac{\bar y}{xR^2}V,\qquad
 H_y=(1/y,0)=H+\frac{\bar x}{yR^2}V.
\]
Each is a determinant-one shear of \((V,H)\). Multiplying its off-diagonal coefficient by a real collar parameter contracts the shear while keeping the determinant frame and the vertical vector. Thus this is an actual frame comparison on each overlap.

The normalized frame on the small normal sphere is
\[
 (V/R,RH)=\frac1R
 \begin{pmatrix}x&\bar y\\-y&\bar x\end{pmatrix}.
\]
In the complex boundary orientation this is the degree-one unitary clutch. Hence the determinant-trivial relative bundle has \(c_2=1\).

The outer marked source frame uses the outward base polar vector. Its horizontal vector is \(qH\), and its determinant relative to \(\Omega\) is exactly \(q\). Consequently
\[
 c_{1,\mathrm{rel}}=\operatorname{PD}(\text{fibre}),\qquad
 c_{1,\mathrm{rel}}^2=0.
\]
The square vanishes by taking two distinct parallel fibres with the actual boundary framing. The determinant winding has therefore been retained, rather than discarded. It follows that
\[
 \langle p_{1,\mathrm{rel}}(TE),[E,\partial E]\rangle
 =c_{1,\mathrm{rel}}^2-2c_{2,\mathrm{rel}}=-2.
\]
Replacing \(q\) by the full Tate parameter \(Q=\kappa(q,v)q\) changes the horizontal frame by the extending factor
\(\kappa/(\kappa+q\partial_q\kappa)\). It has an extending logarithm on the chosen source bidisc. The real period frame differs by the displayed determinant-one shears and the positive period matrix. These are the full relative boundary comparisons.

Since \(\Psi=d\theta\wedge d\gamma\), its last two factors have the opposite order from \(d\gamma\wedge d\theta\) in \(\Omega_+\). Therefore
\[
 \langle p_1,\Psi\rangle_{\Omega_+}=2.
\]

## PS.3. The Xi slice and the full tangent collar

At fixed theta, all four source-period units have their actual \(q\)-disc logarithms. Apply the full source, graph, line and Hopf collar maps of the BW calibration, with the same closing exponent and coefficient boundary frame. The P3K.62 comparison retains its two actual normal arrows and its inner cap gauge. Their separate characteristic corrections vanish by those extending maps. The full boundary calibration is \(3B-3\), with \(B=1\) on this source slice. Thus
\[
 \int F_U^2\Xi=1.
\]
No global logarithm of the parameter-winding function \(g\) is used here.

For the vertical change write
\[
 Q(q',v)=Q(q,v)g(q,v)^j,\qquad
 c=\frac{g(q',v)}{g(q,v)}.
\]
The unique logarithm of \(c\) is zero on \(q=0\). The actual suspension map is
\[
 (Z,\gamma_j)\longmapsto(c^{\gamma_j}Z,\gamma_j).
\]
Its period square is the identity
\(c^{\gamma_j+1}g(q)=g(q')c^{\gamma_j}\).
On the two node branches this is multiplication by opposite unit factors, so it extends their equations and fixes the fixed locus.

Put \(\tau=\log Q/(2\pi i)\), \(G=\log g/(2\pi i)\), and
\(\Delta G=\log c/(2\pi i)\). Only the last logarithm is asserted periodic. The exact pulled-back coframe satisfies
\[
 \omega'=\omega+\Re(\Delta G)(d\gamma-jdt),\quad
 dt'=dt,\quad d\gamma'=d\gamma-jdt .
\]
In the order \((\omega,\gamma,t)\) its matrix is upper triangular with diagonal one. The full derivative is block triangular, with this source block, the actual base derivative, and the retained off-diagonal base/source entries. The trace of curvature-square is the sum of the diagonal block traces. The strictly triangular source block has zero trace-square. The base comparison depends only on \(\alpha,\theta\) and one collar coordinate, so its curvature-square vanishes by dimension. The full tangent collar consequently has zero Pontryagin transgression.

A regular \(b\)-level misses \(U_2\) and is relatively cobordant to the original source three-level times the gamma circle. The original source-pulled four-form restricts to zero on this level, and the just-described comparison collar has zero transgression. Therefore
\[
 \langle p_1,\Xi\rangle=0.
\]

## PS.4. The actual relative line arrow

The full period and meridian evaluations give
\[
 U_j\simeq U_{0,q'}\otimes
 T_b^{-(3j+bj^2)}\otimes T_\gamma^{-2bj}.
\]
Here the letter \(b\) in the exponent is the integer source weight; the map \(b\) in \(T_b\) is the prescribed graph coordinate. These data are fixed by the preceding coefficient arrows.

After those evaluations, the only remaining possible boundary obstruction is the \(q\)-angle. The actual nodal monodromy kills the source vanishing circle primitively; the theta, graph and gamma characters extend. At one theta choose the literal section disc with \(|Z_*|=1\), \(Z_*=-1\), and \(\gamma=t=0\), avoiding the Cartier sections and the fixed graph. Both tensor frames and the prescribed \(Z_*^{-j}\) Cartier arrow extend across this disc. The boundary ratio has zero \(q\)-degree.

For completeness, write the surviving line transitions as
\(e_l=\exp(2\pi i r_{il})e_i\). Remove their integral cocycle using the already verified meridian evaluations. A partition of unity produces \(r_{il}=a_l-a_i\); the frame changes
\(e_i\mapsto\exp(-2\pi ia_i)e_i\) trivialize the line. Remove the extending theta, graph and gamma characters. The remaining real logarithm on the boundary extends over a collar, with the specified original value. Inverting these maps gives precisely the prescribed outer line arrow and leaves the inner cap arrow unchanged.

## PS.5. The flat Psi restriction

On the gamma level from PS.1, the actual boundary connection is
\[
 dd-a\theta\,dt.
\]
It is closed. Its \(q\)-holonomy is zero because the \(q\)-deck changes \(d\) by \(-\gamma\), and this level has \(\gamma=0\). Its integral Chern class vanishes: its degree on the sole normalization sphere of the nodal source is zero.

The actual graph map \(b\) extends over the vanishing-circle handle and is constant there. The flat line with holonomy \(\exp(-2\pi ia\theta)\) along that graph has boundary connection \(dd-a\theta\,db\). Its relative comparison with the prescribed line has zero \(q\)-winding on the section disc of PS.4, including all full Cartier units and the \(q'\) source map. The same Cech trivialization, extending graph character and final real collar logarithm make the boundary value exact. This constructs a flat extension with the required coefficient arrow, not merely a line with the same first Chern class. Therefore
\[
 \int F_U^2\Psi=0.
\]
Terms containing \(d\theta\) disappear after multiplication by \(\Psi\).

## PS.6. The inserted cap and its directed clutch

The actual normal source map is
\((Z,A,B)\mapsto(Z,a_jA,B)\), with \(a_j(0,v)=g(0,v)^j\).
Its Hopf comparison is \(F\circ C^{-1}\), where
\[
 F(q_H)=e^{h\alpha/2}q_H e^{i\alpha/2},\qquad
 C(q_H)=e^{i\alpha/2}q_H e^{i\alpha/2}.
\]
Thus the coordinate clutch is
\[
 v_{\rm ref}=A_j v_j,\qquad
 A_j=e^{h\alpha/2}e^{-i\alpha/2},
\]
of degree \(N=bj\).

The complex fixed sphere is \(-S^2_h\). The quotient tube orientation is
\(-S^2_h\wedge dr\wedge S^2_\eta\); the deleted tube has inner boundary
\(+S^2_h\times S^2_\eta\). Hence the inserted cap is
\(-D^3_h\times S^2_\eta\).
The directed clutch base is
\[
 -(D^3_j\cup -D^3_{\rm ref})\times S^1.
\]
For the positive spinor quaternion representation the Maurer–Cartan trace integral is \(-24\pi^2\deg(A_j)\). The radial connection with the displayed coordinate-clutch direction gives
\(c_2=-N\), hence \(p_1(\operatorname{ad}E)=4N\), on that actual base. The physical tautological line has fibre degree \(-1\). Its positive-parameter characteristic pair is \((-N,-4N)\). The literal Jin parameter reversal therefore gives the inserted-cap contribution
\[
 (N,4N)=(bj,4bj).
\]
All extending constant, positive and logarithmic factors above remain in the map.

## PS.7. The outward collar and the resulting calibration

The exact boundary connection and its difference are
\[
 A_{\rm ext}=dd_j+(\alpha-2\theta)d\gamma+jdu+
       [j\alpha-(2j+a)\theta]dt,
\]
\[
 \beta=-j\{du+[\alpha+(1+bj)\theta]dt+b\theta\,d\gamma\}.
\]
In \(\Omega_B=d\alpha\wedge du\wedge dt\wedge d\gamma\wedge d\theta\),
\[
 3\int_0^1\beta(F_{\rm ext}+s\,d\beta)^2\,ds
 =-(6aj+9j^2+2bj^3)\Omega_B.
\]
The actual outward collar runs from one to zero, so its Euler-cube contribution is \(6aj+9j^2+2bj^3\). Its Pontryagin contribution is zero by PS.3.

The four calibrated pairings are therefore
\[
 \int F_U^2\Xi=1,\quad \int F_U^2\Psi=0,\quad
 \langle p_1,\Xi\rangle=0,\quad \langle p_1,\Psi\rangle=2.
\]
The tensor-line bulk contributes
\((-9j-3bj^2,-4bj)\), the cap contributes \((bj,4bj)\), and the collar contributes the displayed Euler cube. Since \(a+b=3\),
\[
 \Delta k_M=6P_b(j),\quad\Delta\ell_M=0,\qquad
 P_b(j)=2b\binom{j+1}{3}+(3-b)\binom{j+1}{2}.
\]
These are the relative calculations used by P3K.89.

