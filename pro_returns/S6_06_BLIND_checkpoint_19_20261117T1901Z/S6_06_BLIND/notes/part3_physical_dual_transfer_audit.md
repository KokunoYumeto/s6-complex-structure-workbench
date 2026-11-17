# Actual physical circle, meridian dual, and Hopf transfer

17 November 2026. Independent checks audit of the sign gate in K66.
This note retains both complex lines and the actual gluing relation.
It does not edit the active proofs or assign an integer refinement to
K66 before the global audits are reconciled.

## PD.1. The two actual line bundles

Use the first-resolution normal coordinates
\((c_0,c_1)\), of physical delta weights \((-1,+1)\), and
\[
 q_H=c_0+j\overline{c_1},\qquad
 q_H\longmapsto q_He^{-i\phi},\qquad z=q_Hiq_H^{-1}.
\]
The map from the ordered real complex coordinates of \((c_0,c_1)\)
to quaternion coordinates \((1,i,j,k)\) preserves orientation.
At \(q_H=1\), the circle vector is \(-i\), and the horizontal
derivatives \(j,k\) are respectively \(-2k,2j\). Consequently
\[
 [S^3_q]=-[S^1_\delta][S^2_z],\qquad
 \Omega_{\mathbb C^2}=d\delta\wedge dr\wedge\Omega_{S^2_z}.
 \tag{PD.1}
\]
Thus \(S^2_z\) is the actual outward circle-first normal meridian
when the fixed complex curve keeps its complex orientation.

Let \(M\) be the nonzero-vector complex line of the physical
principal circle. A local unit vector has connection
\(\nabla=d+2\pi i A\), with \(A(\partial_d)=1\), so
\[
 x_M=c_1(M)=-dA,\qquad
 U=M^*,\qquad x_U=c_1(U)=dA.
 \tag{PD.2}
\]
The explicit Hopf section gives
\(\int_{S^2_z}dA=1\). Hence \(M\) has meridian value \(-1\)
and \(U\) has meridian value \(+1\). This calculation uses
the Chern connection and the displayed circle vector, not an
assigned numerical return value.

The actual dual arrow is the Hermitian map
\[
 v\longmapsto
 \left(w\longmapsto\frac{\langle v,w\rangle}{\langle v,v\rangle}\right),
 \tag{PD.3}
\]
with the inner product linear in the second variable. It reverses
the circle character. It extends over the two product caps with
the same formula; any scalar boundary gauge is inverted pointwise.
Its restriction to the regular source slice is \(M\to M^*\).

For a fixed oriented mapping torus this gives the exact identities
\[
 (k_M,\ell_M,A_M)=-(k_U,\ell_U,A_U).
 \tag{PD.4}
\]
They follow from \(x_M=-x_U\) in the two odd characteristic
expressions. The orientation of that mapping torus has not changed.

## PD.2. The corrected Cartier-to-Cox map and the K42 cap pair

We independently checked PS.2--5 of
\(\texttt{part3_euler_cube_peer_sign_audit.md}\). The positive
spinor coefficients are
\((p,q)=(\overline{c_0},c_1)\). With \(x=s-\rho\),
\(y=s+\rho\), and \(Y=y/|y|\), the actual Cartier vector frames
\((1/x,y)\) give
\[
 (p,q)=\operatorname{diag}(\overline Y,Y)(a,b),\qquad
 (c_0,\overline{c_1})
     =\operatorname{diag}(Y,\overline Y)(\overline a,\overline b).
\]
After the first normalized Cox factor, the full coefficient map is
\[
 q_H=g(x,y)\overline{(a,b)},\qquad
 g(x,y)=\frac1{\sqrt{|x|^2+|y|^2}}
 \begin{pmatrix}y&-\overline x\\x&\overline y\end{pmatrix}.
 \tag{PD.5}
\]
The conjugation in this formula is essential. An additional order
swap gives an anti-linear swap, whose adjoint map is
\((\gamma,\ell)\mapsto(-\gamma,\ell)\), of real determinant
\(-1\). The linear swap would instead give
\((-\gamma,\overline\ell)\).

The anti-linear quaternionic map
\[
 Q(a,b)=(\overline b,-\overline a)
 \tag{PD.6}
\]
commutes with every \(SU(2)\) clutch. Its projectivization is the
antipodal map of the adjoint sphere, and it extends over its disc.
Use this exact map on the inner Cartier cap and outer Cox cap.
The two line characters are dual, and the sphere orientation changes
at the same time. Thus these cap arrows preserve the integrated
odd characteristic expressions after both reversals are retained.
Moreover \(\overline g=JgJ^{-1}\) with constant \(J\in SU(2)\);
the actual clutch retains its relative \(c_2=-1\) and adjoint
Pontryagin number \(+4\).

For the meridian-one line \(U\), the normal sphere bundle over the
closed oriented four-sphere consequently has pair \((1,4)\).
The actual local Seifert cap has pair \((5,-4)\), with the
meridian-one line restricting to its oriented normal Euler class.
The boundary signs and the physical-to-Jin parameter reversal are
unchanged by the explicit cap maps above. Therefore the corrected
K42 conclusion in that precise line convention is
\[
 (k_U,\ell_U)=(6,0),\qquad (k_M,\ell_M)=(-6,0).
 \tag{PD.7}
\]
This is an audit of the explicit corrected cap maps, not an
identification of the two line conventions by a shared name.

## PD.3. The factor orientations and the gluing inverse

Keep K23's actual exterior \(E=D^3_y\times S^3_q\) with its
complex orientation. The complex six-sphere is
\[
 S^6_{\rm phys}=-\partial(D^3_y\times D^4_q).
 \tag{PD.8}
\]
F22 uses a circle bundle whose Euler class is positive on its
oriented two-sphere, total three-sphere oriented circle first,
and the boundary orientation of \(D^4_u\times D^3_{y_*}\).

For the physical line \(M\), set
\[
 S^2_M=-S^2_z,\qquad y_M=-y,\qquad u_M=+q.
 \tag{PD.9}
\]
The two base-factor reversals preserve the quotient five-manifold
orientation. Formula (PD.1) makes \(u_M\) exactly circle first
over the \(M\)-positive base. Formula (PD.8) identifies
\(\partial(D^4_{u_M}\times D^3_{y_M})\) with the physical
six-sphere, preserving its orientation.

For \(U\), the dual arrow reverses the circle and retains the
meridian-positive base \(S^2_U=S^2_z\). Thus
\[
 u_U=+q,\qquad y_U=y.
 \tag{PD.10}
\]
This product boundary has the opposite physical six-sphere
orientation. The quotient identification from the \(M\) marking
to the \(U\) marking reverses both sphere factors; its lift is
the anti-equivariant dual-line map. On the total product factors
it is the identity on \(q\) and the reflection on \(y_*\).
It extends over both four-ball factors with that same formula.

To retain the endpoint direction, write
\[
 \Sigma_F=(D^4_y\times S^3_q)\cup_F(S^3_y\times D^4_q),
 \qquad x_{\rm first}\sim F(x)_{\rm second}.
 \tag{PD.11}
\]
F22 has first piece \(H=D^4_u\times S^3_{y_*}\), second
piece \(K=S^3_u\times D^4_{y_*}\), and its actual relation is
\(h_{\rm first}\sim F(h)_{\rm second}\), after transporting the
displayed coordinate marking.

Under (PD.9), the literal piece maps are
\[
 H\longrightarrow -(S^3_y\times D^4_q),\qquad
 K\longrightarrow -(D^4_y\times S^3_q).
 \tag{PD.12}
\]
The products exchange. Rewriting the same equivalence relation
with the first \(\Sigma\) piece first replaces \(F\) by \(F^{-1}\).
The common orientation is reversed. Hence
\[
 \lambda_M(F)=-\Sigma_{F^{-1}}.
 \tag{PD.13}
\]
Under (PD.10), the piece maps have the same exchanged factors
and both positive signs:
\[
 H\longrightarrow +(S^3_y\times D^4_q),\qquad
 K\longrightarrow +(D^4_y\times S^3_q),
 \qquad \lambda_U(F)=+\Sigma_{F^{-1}}.
 \tag{PD.14}
\]
The inverse in both formulas is exactly the piece exchange; the
anti-equivariant line map does not itself reverse the return.

The extending relative generators \(L,R\) give zero sphere class.
For the remaining disc-supported relative class, cancelling the
oppositely oriented product collars gives
\(\Sigma_{F^{-1}}=-\Sigma_F\). Thus, in the actual sphere group,
\[
 \lambda_M(F)=\Sigma_F,\qquad
 \lambda_U(F)=-\Sigma_F.
 \tag{PD.15}
\]
This also agrees directly with F8: its cut-out seven-ball lies
in \(H\), and its boundary point is glued to the exterior by
\(x_{\rm ball}\sim F(x_{\rm ball})_{\rm exterior}\).
The orientation choice (PD.9) is exactly its complex-oriented
initial sphere identification.

Combining the proved F22 formula with these actual arrows gives
\[
 28\mu(\Sigma_F)=A_M(F)=-A_U(F)\pmod {28}.
 \tag{PD.16}
\]

## PD.4. Relative integers and the old page dictionary

K23's connection and normal-clutch calculation uses the
meridian-one generator \(x_U=dA\). Its literal relative
generators therefore give
\[
 k_U=-(m+n),\qquad \ell_U=-4m,\qquad A_U=-n/6.
 \tag{PD.17}
\]
Applying the exact line duality, without changing the physical
relative maps \(L,R\), gives
\[
 k_M=m+n,\qquad \ell_M=4m,\qquad A_M=n/6.
 \tag{PD.18}
\]
In particular \(n=-6A_U=6A_M\). The central relative exponent
is the actual sphere class with K23's independently oriented
plumbing generator; it is \(A_M\), not \(A_U\).

K6's meridian-one Thom construction consequently restricts on
its page to \(-c_1(M)\). The exact comparison is the Hermitian
dual of its stated physical source-line arrow. K7 then has
\(b|_V=-2c_1(M)\); its square, normal Pontryagin term and
meridian-one index calculation are unchanged. Thus the previous
fixed-fan numerical calculation remains a calculation of
\(A_U\), and the physical Hopf-gluing sphere class is its
negative by (PD.16). No numerical sign is selected from a
previous sphere residue.

## PD.5. Actual location and orientation of the EC collar

The completed cusp piece is \(|q|\leq\epsilon\), with auxiliary
source-first orientation
\[
 \Omega_+=dr_q\,d\alpha\,du\,dv\,d\gamma_B\,d\theta.
 \tag{PD.19}
\]
Here \(\gamma_B\) is the contracting suspension coefficient.
The actual circle-first orbit orientation is
\(\Omega_S\,d\gamma_B\); the physical positive parameter has
orientation \(\Omega_+\), while Jin's endpoint reversal gives
\(-\Omega_+\).

The actual outward boundary of the piece has orientation
\(\Omega_B=d\alpha\,du\,dv\,d\gamma_B\,d\theta\).
Moving from the piece into its unchanged exterior increases
\(r_q\), so the gluing collar orientation is \(dt\,\Omega_B\).
The difference is precisely
\(\beta=A_{\rm piece}-A_{\rm ext}\), and the connection
\(A_{\rm ext}+\chi\beta\) has \(\chi:1\to0\) in that direction.
The independently checked identity
\[
 3\int_0^1\beta(F+s\,d\beta)^2\,ds=18n^2\Omega_B
\]
therefore contributes \(-18n^2\) to the auxiliary-oriented
integral of \((dA)^3\). This sign follows from the actual
location of the piece, not from a declaration of its boundary.

For \(U\), the Jin integral is the negative of that auxiliary
integral. For \(M\), its additional odd line reversal cancels
the Jin orientation reversal. Consequently the exact
second-difference conclusions of the EC affine-bulk/relative-line
calculation are
\[
 \begin{split}
 k_{U,n}-(1-n)k_{U,0}-nk_{U,1}&=+18n(n-1),\\
 k_{M,n}-(1-n)k_{M,0}-nk_{M,1}&=-18n(n-1).
 \end{split}
 \tag{PD.20}
\]
These formulas do not choose either endpoint value from a residue.
The active K66 proof remains unpromoted until its statement,
maps, certificate and all dependent dictionaries have been
reconciled with the actual conventions in this note.
