# Marked determinant and toroidal structures: bounded evidence note

Date: 2026-09-04. Scope: independent comparison of the five named research modules, with new elementary observation/period calculations below. No canonical files were edited. This note does not independently certify the original candidate's claimed complex structure or sphere recognition.

All source filenames below are relative to
output/s6_consolidated_canonical_2026-08-26/supporting_materials/workbench/research/.
Line numbers describe the files read on this date; named equation and theorem labels are the durable anchors.

## 1. Strongest common lead

The strongest algebraic host is the rank-three Hermitian determinant geometry, ultimately the full Jordan algebra \(\operatorname{Herm}_3(\mathbb H)\), together with a **retained complex structure and marked rank-two observation**. Its geometric connection to the native cusp is the actual marked \(A_2\) quotient, toric morphism, and period/filling map below. Thus the lead is not one common sphere: it is a marked determinant/positive-cone system supplied with integral period and filling data.

The quaternionic completion has an exact observation onto the \(3+1\) Lorentz cone without imposing the thirteen-dimensional slice. Section 4 proves this stronger statement, including the hidden-coordinate inequality. The native cusp reaches the same marked matrix \(P\) through a genuine integral and local holomorphic morphism, not through matching dimensions. Section 6 constructs an additional explicit period-to-Gram map and determines its actual cusp limit.

## 2. The fixed marking and the genuine toroidal morphism

Retain
\[
 P=\begin{pmatrix}1&-1&0\\0&1&-1\end{pmatrix},\quad
 u=(1,1,1)^{\mathsf T},\quad
 C=PP^*=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},
\]
\[
 R=P^*C^{-1}=\frac13
 \begin{pmatrix}2&1\\-1&1\\-1&-2\end{pmatrix},\qquad
 X=(R\ u),\qquad X^{-1}=\binom P{u^*/3}.
\]
Direct multiplication gives \(PR=I_2\), \(RP=I_3-uu^*/3\), \(\det X=1\), and
\[
 X^*X=D=\operatorname{diag}(C^{-1},3),\qquad
 C^{-1}=\tfrac13\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]
In particular, the marking is not unitary and \(R\) is not an integral lattice section.

The local rank-three toroidal successor has angular/deck lattice
\(\Lambda_3=\mathbb Z^3\oplus\mathbb Z^3\), monodromy
\[
 M_3=\begin{pmatrix}I_3&I_3\\0&I_3\end{pmatrix},
 \qquad c_3(a,b)=b.
\]
The retained native cusp marking is \(A_F\oplus B_F\), with
\[
 B_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
 M_F=\begin{pmatrix}I_2&B_0\\0&I_2\end{pmatrix},\quad
 c_F(a,b)=b.
\]
Use \(Q_{\rm latt}=B_0^{-1}P\), explicitly
\[
 Q_{\rm latt}=\begin{pmatrix}0&-1&1\\1&-1&0\end{pmatrix},\qquad
 \Phi=P\oplus Q_{\rm latt}.
\]
Then
\[
 \Phi M_3=M_F\Phi,\qquad c_F\Phi=Q_{\rm latt}c_3,
 \qquad\ker\Phi=\mathbb Z(u,0)\oplus\mathbb Z(0,u).
\]
These equalities follow by multiplying the displayed matrices; both \(P\) and \(Q_{\rm latt}\) are surjective integral maps. The kernel is an elliptic rank-two local system, with \(M_3\) restricting to \(\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\).

This lattice map is realized locally. The Kuhn tetrahedron with successive vertices \(m,m+e_{\pi_1},m+e_{\pi_1}+e_{\pi_2},m+u\) maps under \(P\) to the triangle with vertices
\[
 Pm,\quad Pm+n_{\pi_1},\quad Pm-n_{\pi_3},
 \qquad(n_1,n_2,n_3)=(\widehat w,\widehat\delta-\widehat w,-\widehat\delta).
\]
These are native \(A_2\) triangles. Thus \(\widehat P(x,r)=(Px,r)\) is a map of height-one fans, giving \(F:Y_3\to Y_2\), \(tF=t\). Locally at a deepest point it is the four-to-three-branch map
\[
 (z_0,z_1,z_2,z_3)\longmapsto (z_0z_3,z_1,z_2),
 \qquad z_0z_1z_2z_3=t.
\]

The local period correction is also retained, rather than discarded. Write
\[
 Z_2(t)=sB_0+C_2(t),\quad
 S=\begin{pmatrix}1&1\\0&1\\0&0\end{pmatrix},\quad
 C_3(t)=S C_2(t)Q_{\rm latt},\quad Z_3(t)=sI_3+C_3(t),
\]
where \(t=e^{2\pi i s}\), \(C_2\) is holomorphic and bounded at the cusp, and \(PS=I_2\). Hence
\[
 PZ_3=Z_2Q_{\rm latt}.
\]
The induced map on the compact regular complex tori has connected elliptic kernel
\(\mathbb Cu/(\mathbb Zu+s\mathbb Zu)\). The source proves equivariance of the corrected toric actions and descent over the cusp disc, including the filling square.

Sources: higher_rung_toroidal_elliptic_bridge.tex, equations TEB.16--TEB.35 and propositions on the fan morphism and period correction; higher_rung_fourfold_toric_degeneration.tex, local fan construction and peripheral topology.

## 3. What exactly connects this to the complex \(4+4+1\)

The observation and section are
\[
 \mathcal O_P(H)=PHP^*,\qquad \jmath_P(G)=RGR^*,\qquad
 \mathcal O_P\jmath_P=I.
\]
They preserve positivity. Every \(H\in\operatorname{Herm}_3(\mathbb C)\) has the unique marked expression
\[
 H=X\begin{pmatrix}G&z\\z^*&\lambda\end{pmatrix}X^*,\qquad
 \det H=\lambda\det G-z^*\operatorname{adj}(G)z.
\]
This is the exact \(9=4+4+1\), not a counting analogy. On the positive cone its full fibre is
\[
 G\succeq0,\quad z\in\operatorname{Ran}G,\quad
 \lambda\ge z^*G^\dagger z.
\]
The source proves this by triangular congruence, including singular \(G\).

Under the retained Pauli convention
\[
 G=\begin{pmatrix}p_0+p_3&p_1-ip_2\\p_1+ip_2&p_0-p_3\end{pmatrix},
 \qquad\det G=p_0^2-p_1^2-p_2^2-p_3^2,
\]
positivity is exactly the future cone \(p_0\ge\sqrt{p_1^2+p_2^2+p_3^2}\).
The faithful ambient lift
\[
 T_P(g)=RgP+uu^*/3=X(g\oplus1)X^{-1}
\]
satisfies \(PT_P(g)=gP\), giving \(G\mapsto gGg^*\), \(z\mapsto gz\), \(\lambda\mapsto\lambda\). For \(g\in SL_2(\mathbb C)\), the vector action is the usual double cover of \(SO^+(1,3)\); the full vector-plus-spinor action is faithful.

There are two different exact toroidal connections here.

First, let \(\nu_i=E_{ii}-I_3/3\), and let \(\jmath_A:A_{F,\mathbb R}\to\operatorname{Herm}_3^0(\mathbb C)\) be the linear map \(\jmath_A(n_i)=\nu_i\). Its image is the diagonal Cartan space. The six projected Kuhn chambers are the six eigenvalue-order chambers. The map
\[
 H\longmapsto H-\lambda_{\min}(H)I_3
\]
is linear on each chamber and maps its two extremal rays to the indicated rank-one/rank-two diagonal projections. This is an exact \(S_3\)-equivariant chamber correspondence. The induced lattice-realification map
\[
 (a,b)\longmapsto
 \jmath_A(Pa)-\lambda_{\min}(\jmath_A(Pa))I_3
\]
forgets every deck coordinate and the angular \(u\)-direction. It is not additive, not proper, and does not descend to the compact torus: \(a=0\) and \(a=e_1\) represent the same point modulo the integral lattice but have different images.

Second, the actual four-branch chart has the holomorphic diagonal seed
\[
 K(z)=\operatorname{diag}(z_0z_3,z_1z_2),\qquad
 \det K(z)=z_0z_1z_2z_3.
\]
It is a positive Hermitian matrix only on the explicitly retained locus
\(z\in\mathbb R_{\ge0}^4\), not on the entire complex chart. For each retained \(\mu>0\),
\[
 \Psi_\mu(G)=\mu uu^*+\jmath_P(G),\quad
 \det\Psi_\mu(G)=\mu\det G,\quad
 \operatorname{rank}\Psi_\mu(G)=1+\operatorname{rank}G.
\]
The map \((g,z)\mapsto\Psi_\mu(gK(z)g^*)\) from
\(SL_2(\mathbb C)\times\mathbb R_{\ge0}^4\) surjects onto \(\Psi_\mu(\mathcal P_2)\), by diagonalizing each positive \(G\). This supplies a local determinant-compatible Lorentz orbit completion, but no global period/filling descent.

Sources: higher_rung_lorentz_observation_bridge.tex, lines 15--177, 239--435, 489--551 and 674--746; higher_rung_toroidal_elliptic_bridge.tex, chamber subsection; higher_rung_rank_six_lattice.tex, exact Gram map subsection. The latter also proves the integral sequence does not split \(S_3\)-equivariantly: an invariant integral retraction of the diagonal generator would send \(u\) to \(3a\), never to \(1\).

## 4. Exact full quaternionic observation, independently checked

Write \(q=a+b\mathbf j\), \(a,b\in\mathbb C\), with
\(\mathbf j a=\bar a\mathbf j\). Define
\[
 B(b)=\begin{pmatrix}
 0&\bar b_3&-\bar b_2\\-\bar b_3&0&\bar b_1\\
 \bar b_2&-\bar b_1&0
 \end{pmatrix},\qquad H=\Theta(A,b)=A+B(b)\mathbf j.
\]
This is a real-linear bijection
\(\operatorname{Herm}_3(\mathbb C)\oplus\mathbb C^3\to\operatorname{Herm}_3(\mathbb H)\), and the Moore cubic is
\[
 N(H)=\det A-b^*Ab.
\]
Put \(X^*b=(\chi,\rho)^{\mathsf T}\), so \(\rho=u^*b\). The exact skew identity
\[
 PB(b)P^{\mathsf T}=\bar\rho
 \begin{pmatrix}0&1\\-1&0\end{pmatrix}
\]
shows that the two packets' Lorentz thirteen-spaces are the same embedded space \(\rho=0\). Its marked spinor dictionary is
\[
 w=-\varepsilon\bar\chi,\quad \chi=\varepsilon\bar w,\quad
 \varepsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
Its cubic is
\[
 N_{13}=\lambda\det G-z^*\operatorname{adj}(G)z-w^*\operatorname{adj}(G)w.
\]
The full cubic is
\[
 N_{15}=\lambda\det G-z^*\operatorname{adj}(G)z-\chi^*G\chi
          -2\operatorname{Re}(\rho\chi^*z)-\lambda|\rho|^2.
\]
Thus \(6+4+4+1\) is the actual full quaternionic block system; \(4+4+4+1\) removes the two real coordinates of \(\rho\).

The observation need not remove them. For a quaternionic Hermitian matrix \(K\), define
\[
 \pi_{\mathbb C}(K)=\frac{K-(iI)K(iI)}2
 =\frac{K+(iI)^*K(iI)}2,\qquad
 \mathcal O_{\rm full}(H)=\pi_{\mathbb C}(PHP^*).
\]
For each entry \(a+b\mathbf j\), \(i(a+b\mathbf j)i=-a+b\mathbf j\), so \(\pi_{\mathbb C}\) keeps exactly the complex part. It is positive because it is the average of the identity and a unitary congruence. Compression is also positive. Consequently
\[
 \mathcal O_{\rm full}(\Theta(A,b))=PAP^*,
 \qquad \mathcal O_{\rm full}(RGR^*)=G.
\]
This is a positive split real-linear epimorphism from the full fifteen-space to \(\operatorname{Herm}_2(\mathbb C)\), with kernel dimension \(15-4=11\).

Write \(G=\left(\begin{smallmatrix}a&c\\\bar c&d\end{smallmatrix}\right)\).
The quaternionic observed block is
\[
 PHP^*=
 G+\bar\rho\varepsilon\mathbf j
 =\begin{pmatrix}a&c+\bar\rho\mathbf j\\
 \bar c-\bar\rho\mathbf j&d\end{pmatrix}.
\]
Its off-diagonal squared norm is \(|c|^2+|\rho|^2\), so its Moore determinant is
\[
 ad-|c|^2-|\rho|^2=\det_{\mathbb C}G-|\rho|^2.
\]
The positive-semidefinite criterion for this two-by-two Hermitian matrix is \(a,d\ge0\) and this determinant nonnegative: for \(a>0\) complete the square; if \(a=0\), the determinant condition forces its off-diagonal entry to vanish, leaving \(\operatorname{diag}(0,d)\). Interchanging \(a,d\) covers the other degenerate presentation. It follows that
\[
 H\succeq0\quad\Longrightarrow\quad
 G\succeq0,\qquad |\rho|^2\le\det_{\mathbb C}G.
\]
Conversely, every such \(G,\rho\) has a positive lift:
\[
 H=X\operatorname{diag}_{\mathbb H}
       (G+\bar\rho\varepsilon\mathbf j,\lambda)X^*,\qquad\lambda\ge0.
\]
Invertible congruence preserves positivity, and \(PX=(I_2\ 0)\), proving the converse exactly. Therefore the Lorentz-null observation forces \(\rho=0\), while a timelike observation permits the full closed disk \(|\rho|\le\sqrt{\det G}\). This is an algebraic inequality, not a mass quantization or mass-gap theorem.

For complex \(g\), complex-component projection commutes with \(K\mapsto gKg^*\), because the discarded coefficient transforms as \(B\mapsto gBg^{\mathsf T}\). Thus the same \(T_P(g)\) makes \(\mathcal O_{\rm full}\) equivariant under the congruence action. This action generally does not preserve the original trace-free condition or the retained kinetic metric.

The thirteen-space generates the full fifteen-space under the original Jordan product. Under \(H=XMX^*\), that product is
\[
 M\circ_D N=(MDN+NDM)/2,
\]
not the ordinary block product. The source's explicit off-diagonal spinors \((1,0)^{\mathsf T}\) and \((0,\mathbf j)^{\mathsf T}\) generate the missing upper block
\(\tfrac32\left(\begin{smallmatrix}0&-\mathbf j\\\mathbf j&0\end{smallmatrix}\right)\); replacing \(\mathbf j\) by \(\mathbf k\) gives the other missing direction. Hence the full completion is algebraically forced by that specified product.

Source for the embedded dictionaries, cubics and Jordan calculation: quaternionic_4441_reconciliation.tex, lines 17--222 (q444:pair-cubic, q444:identification, q444:cubics), lines 224--284 (positive fibres and sphere pair), and lines 288--323 (q444:jordan). The full positive observation and disk-fibre calculation above were independently derived for this note.

## 5. Trace-free dynamics is not the positive cone

The scalar fourteen-space is \(\operatorname{Herm}_3^0(\mathbb H)\), equivalently \(\operatorname{Herm}_3^0(\mathbb C)\oplus\mathbb C^3\). A positive semidefinite trace-free Hermitian matrix is zero: all its eigenvalues are nonnegative and their sum is zero. Therefore a nonzero scalar trajectory on the fourteen-space is not automatically a trajectory in the positive fifteen-cone.

The linear observation restricted to the fourteen-space is still onto the full Minkowski vector space, with exact section
\[
 \jmath_0(G)=RGR^*-\frac{\operatorname{tr}(C^{-1}G)}3uu^*.
\]
Indeed its trace is zero, since \(\operatorname{tr}(uu^*)=3\), and its compression is \(G\), since \(Pu=0\). Its kernel has dimension ten; this section is not positive.

For a positive boundary observation one can instead use the exact spectral-floor map
\[
 Q\longmapsto H=Q-\lambda_{\min}(Q)I_3,\qquad
 G=P\Phi P^*-\lambda_{\min}(Q)C,\qquad
 Q=\Theta(\Phi,b),\quad\operatorname{tr}\Phi=0.
\]
This is nonlinear and retains the nonidentity \(C\). The spectral-floor map is a homeomorphism from the full fourteen-space onto the singular positive fifteen-cone, with inverse \(H\mapsto H-(\operatorname{tr}H/3)I_3\). Hence its compactified boundary is \(S^{14}\); the complex and Lorentz thirteen-slice boundaries give \(S^8\) and \(S^{12}\) by the same exact construction. None of these homeomorphisms identifies a sphere's native toroidal fibration.

The equal-diagonal thirteen-space is another embedded slice: its intersection with the complex nine-space has dimension seven, whereas the Lorentz thirteen-space contains that entire nine-space. Their exact common host is the full quaternionic algebra, not equality of slices.

## 6. A further explicit local period-to-Gram bridge

The period identity of Section 2 supplies a new positive map, retaining the choice of metric. On the universal cusp cover define
\[
 \Omega_3=(I_3\ Z_3),\qquad\Omega_2=(I_2\ Z_2).
\]
Then \(P\Omega_3=\Omega_2\Phi\). For every retained real symmetric positive-definite \(6\times6\) matrix \(W_3\), put
\[
 H_3=\Omega_3W_3\Omega_3^*,\qquad W_2=\Phi W_3\Phi^{\mathsf T}.
\]
Since \(\Phi\) is surjective, \(\Phi^{\mathsf T}\) is injective; thus \(W_2\) is positive definite. Both period matrices contain an identity block, so both Gram matrices are positive definite. Multiplication proves the commuting identity
\[
 \boxed{PH_3P^*=\Omega_2W_2\Omega_2^*.}
\]
For \(W_3=I_6\) this reads
\[
 PH_3P^*
 =C+Z_2\begin{pmatrix}2&1\\1&2\end{pmatrix}Z_2^*,
\]
because \(Q_{\rm latt}Q_{\rm latt}^{\mathsf T}
=\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)\).
This is an exact period-to-Gram morphism on the marked cover, not an inverse reconstruction of periods or an observation of points inside a torus fibre.

It cannot retain a constant positive metric and simultaneously descend through the nontrivial cusp monodromy. Indeed
\(\Omega_3(s+1)=\Omega_3(s)M_3\).
Invariance of a fixed positive \(W_3\) as a lattice metric would require \(M_3W_3M_3^{\mathsf T}=W_3\). Then \(W_3^{-1/2}M_3W_3^{1/2}\) would be orthogonal, so its powers would be bounded. But \(M_3^n=I+n(M_3-I)\) is unbounded. This contradiction proves the constant-positive-metric obstruction. Even the resulting Gram matrix alone cannot be periodic for a fixed positive \(W_3\): writing \(W_3\) in \(3+3\) blocks, \((I_3\ Z_3+nI_3)W_3(I_3\ Z_3+nI_3)^*\) has coefficient \(W_{3,bb}\succ0\) at \(n^2\), and therefore cannot be constant in the integer \(n\).

A nonflat equivariant metric can be constructed explicitly. For real \(x\), let
\[
 M_3(x)=\begin{pmatrix}I_3&xI_3\\0&I_3\end{pmatrix},
 \quad x=\operatorname{Re}s,\quad
 W_3(s)=M_3(-x)M_3(-x)^{\mathsf T}.
\]
It is positive definite and satisfies
\[
 W_3(s+1)=M_3^{-1}W_3(s)M_3^{-\mathsf T}.
\]
Thus its Gram matrix descends to the punctured cusp:
\[
 H_3(t)=I_3+(iyI_3+C_3(t))(iyI_3+C_3(t))^*,
 \quad y=\operatorname{Im}s=-\frac{\log|t|}{2\pi}.
\]
The target weight descends compatibly because \(\Phi M_3=M_F\Phi\). This supplies an actual real, metric-dependent period-to-positive-cone map over the punctured disc.

Its limit is computable without dropping constants:
\[
 H_3(t)=y^2I_3+iy(C_3(t)^*-C_3(t))
               +I_3+C_3(t)C_3(t)^*.
\]
Boundedness of \(C_3\) gives \(y^{-2}H_3(t)\to I_3\),
\(y^{-2}PH_3(t)P^*\to C\), and
\[
 y^{-4}\det(PH_3(t)P^*)\longrightarrow\det C=3.
\]
Therefore this explicit bridge approaches a full-rank positive direction, not a Lorentz-null or determinant-rank-deficient direction. Unscaled \(H_3\) escapes to infinity. The exact next geometric problem is extension of a specified observation with the actual finite-order overlaps and singular fillings; if rank loss is intended, the construction must additionally explain how to obtain it, since the displayed natural positive Gram construction does not.

## 7. Global-open status and proven obstructions

The successor's global period and overlap construction remains expressly open in higher_rung_toroidal_elliptic_bridge.tex, subsection “The remaining global problem,” lines 1057--1105. It calls for an actual proper \(\widetilde X^8\to\mathbb P^1\), an actual map to the native candidate, agreement with the local elliptic extension and finite affine fillings, and the based van Kampen/integral Mayer--Vietoris maps induced by those inclusions. Matrix compatibility and free finite affine lifts alone do not provide these maps.

The direct successor has cusp Euler contribution \(6\), while the two free finite torus quotients have contribution zero. With only those special fibres, the total Euler characteristic is \(6\), not \(2\). Thus that direct globalization cannot be \(S^8\). The fourfold source independently gives the almost-complex obstruction for a homotopy \(S^8\). Its displayed Mayer--Vietoris sphere criterion is a criterion, not a calculation for a constructed global successor.

This does **not** mean the repository currently marks all original-candidate Mayer--Vietoris work open. topology_reduction.tex claims the original cusp collapse and two actual Mayer--Vietoris stages closed, culminating in its candidate-specific corollary at lines 1241 onward. This bounded comparison has not independently audited that proof chain and does not promote its original \(S^6\) validity claims. The literal symbol \(C_W\) was not found as a named global-open object in the five requested bridge modules; the successor-specific open seam above is unambiguous. The original-candidate source also contains a different symbol \(\mathbb C_W\) for a constant sheaf, which must not be conflated with a missing geometric collapse.

The source also proves specific obstructions to proposed identifications:

- Native deepest three-branch \(z_0z_1z_2\), successor four-branch \(z_0z_1z_2z_3\), and the rank-one Hermitian normal determinant \(uv-x^2-y^2\) have different multiplicities and branch structures. They are not the same singularity germ.
- The complex Gram pair has complement \(\mathbb R^9\times S^1\), whereas the native regular fibration retains a rank-four fibre lattice and a free-group base. The real Gram pair \((S^6,S^5)\) likewise does not identify the native candidate's deleted fibres.
- The “rank six” toroidal lattice \(H_1(T^6)\) is not the defect lattice \(H_4(U)\) merely because both have rank six. The source supplies different domains and markings and no geometric component-permuting \(S_3\) action on the three different native fibre types.
- The usual alternating form \(E_3((a,b),(a',b'))=a^{\mathsf T}b'-b^{\mathsf T}a'\) has \(E_3((u,0),(0,u))=3\), whereas every pullback through \(\Phi\) vanishes on the kernel. Thus \(\Phi\) is not a morphism preserving that chosen principal alternating form.

These obstructions do not erase the explicit fan, period, chamber, local determinant and positive-observation maps proved above.

## 8. Interpretation boundary

The strongest defensible synthesis is therefore **the full rank-three Hermitian determinant carrier with its marked rank-two Lorentz observation, linked to the native cusp by the exact \(A_2\) fan/period quotient**. This gives an actual common target and several actual morphisms.

No cited map by itself identifies the Lorentz coordinates with measured spacetime or momentum, gives \(\rho\) an integral charge, selects physical units, intertwines the scalar Hamiltonian with a geometric dynamics, or proves an interacting Yang--Mills spectral gap. The positive-cone inequality allows arbitrarily small timelike determinant and includes null observations, so it provides no positive mass gap on its own. Those are concrete additional dynamical and observational identifications, not consequences of the sphere dimensions.

## 9. Source-location index

- higher_rung_lorentz_observation_bridge.tex: lines 15--119 fixed marking; 122--177 split observation; 239--305 block determinant/positive fibres; 362--435 lifted \(SL_2(\mathbb C)\) action; 500--551 boundary section and exact normal determinant; 674--746 four-branch diagonal seed and Lorentz orbit completion.
- higher_rung_toroidal_elliptic_bridge.tex: lines 15--202 native peripheral data and \(P,Q_{\rm latt}\); 203--255 fan morphism; 256--408 monodromy, filling and actual period-family morphism; 617--705 \(A_2\) chambers; 705--925 determinant/order-cone extensions and their precise limitations; 926--1055 Gram/fibration obstructions; 1057--1105 successor global-open problem.
- higher_rung_fourfold_toric_degeneration.tex: lines 132--207 rank-three toric degeneration; 302--352 peripheral map; 408--441 central-stratum counts; 557--644 Euler and almost-complex obstructions; 719--858 actual-filling, van Kampen and Mayer--Vietoris requirements; 889--1056 comparison to Gram strata.
- higher_rung_rank_six_lattice.tex: sections “The two rank-six lattices,” integral \(S_3\) sequence, “The exact map into the Gram boundary,” and alternating-form comparison, beginning respectively at lines 11, 62, 258 and 337.
- quaternionic_4441_reconciliation.tex: q444:pair-cubic, q444:identification, q444:cubics, q444:positive, q444:pair-topology, q444:jordan; the final scope paragraph distinguishes the equal-diagonal thirteen-space from the common Lorentz thirteen-space. This file was being appended during the comparison, so the theorem labels should be preferred.
- topology_reduction.tex: source-status comparison only, lines 1--8 and corollary cor:candidate-mv-sphere beginning at line 1241. Its original-candidate validity claims were not independently audited in this bounded task.

## Gauge and period-metric continuation — 4 September 2026

The common carrier is now supplemented by two exact selection tests.
The period map permits every smooth positive observed G through a
17-dimensional metric fibre; an explicit null limit costs unbounded
relative metric condition number. It is therefore not the dimensions,
period monodromy and positivity alone which select an observed trajectory.
Retained constants and full inverse maps are in q444:metric-fibre through
q444:rank-loss-metric.

The scalar rotating orbit has no homogeneous temporal-gauge completion,
but a distinct radial interacting family satisfies every field equation.
A fixed marked determinant varies within one gauge orbit; its Haar average
is V_mu tr(adj A), and on the positive quaternionic rank-one boundary this
equals V_mu||b||². Explicit scalar minima span a continuous range of that
invariant at fixed potential. This is an exact gauge-invariant relation to
the Lorentz observation, not a particle identification or a quantum gap.
The strongest current target remains the full carrier with an actual
period/metric/dynamics/observation map, rather than a sphere selected by
dimension alone. See PRO_FEEDBACK.md Sections10–12 for the next exact tasks.
