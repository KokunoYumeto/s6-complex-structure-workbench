# Exact 4+4+4+1 continuation

The minimal continuation that preserves the old rank-three cubic is obtained by extending the same marked observation matrix

\[
P=\begin{pmatrix}1&-1&0\\0&1&-1\end{pmatrix}
\]

from complex to quaternionic Hermitian matrices, while requiring the observed block to remain in \(\operatorname{Herm}_2(\mathbb C)\).

## 1. The thirteen-dimensional pullback

Fix \(\mathbb H=\mathbb C\oplus\mathbb C\mathbf j\), with \(\mathbf j a=\bar a\mathbf j\). Define

\[
\mathcal J_{13,P}
=\left(\mathcal O_P^{\mathbb H}\right)^{-1}
  \bigl(\operatorname{Herm}_2(\mathbb C)\bigr)
\subset\operatorname{Herm}_3(\mathbb H),
\qquad
\mathcal O_P^{\mathbb H}(H)=PHP^*.
\]

Using the retained matrices

\[
R_P=P^*(PP^*)^{-1},\qquad
X=(R_P\;u),\qquad u=(1,1,1)^T,
\]

every element has unique coordinates

\[
H=X\begin{pmatrix}G&z+w\mathbf j\\(z+w\mathbf j)^*&\lambda\end{pmatrix}X^*,
\]

where

\[
G\in\operatorname{Herm}_2(\mathbb C),\qquad
z,w\in\mathbb C^2,\qquad \lambda\in\mathbb R.
\]

Hence

\[
\boxed{
\mathcal J_{13,P}
\cong_{\mathbb R}
\operatorname{Herm}_2(\mathbb C)\oplus\mathbb C^2\oplus\mathbb C^2\oplus\mathbb R,
}
\]

which is exactly

\[
4+4+4+1=13.
\]

The extraction maps are

\[
G=PHP^*,\qquad
z+w\mathbf j=\frac13PHu,\qquad
\lambda=\frac19u^*Hu.
\]

## 2. The cubic

The restricted quaternionic Moore determinant is

\[
\boxed{
\mathcal N_{13}(G,z,w,\lambda)
=\lambda\det G
-z^*\operatorname{adj}(G)z
-w^*\operatorname{adj}(G)w.
}
\]

Setting \(w=0\) gives the old nine-dimensional cubic exactly, not up to a factor:

\[
\mathcal N_{13}(G,z,0,\lambda)
=\lambda\det G-z^*\operatorname{adj}(G)z.
\]

Let

\[
\epsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
w=\epsilon\overline{\psi_R},\qquad z=\psi_L.
\]

Then

\[
\boxed{
\mathcal N_{13}
=\lambda\det G
-\psi_L^*\operatorname{adj}(G)\psi_L
-\psi_R^*G\psi_R.
}
\]

Thus the two four-real-dimensional spinors may be read as a left and right Weyl pair, i.e. a Dirac spinor.

## 3. Complete positivity

The positive cone is exactly

\[
G\succeq0,\qquad
z,w\in\operatorname{Ran}G,\qquad
\lambda\ge z^*G^\dagger z+w^*G^\dagger w.
\]

If

\[
s=\lambda-z^*G^\dagger z-w^*G^\dagger w,
\]

then

\[
\operatorname{rank}_{\mathbb H}H
=\operatorname{rank}_{\mathbb C}G+
\begin{cases}1,&s>0,\\0,&s=0.\end{cases}
\]

For fixed \(G\) of rank \(r\), the positive fibre is

\[
\mathbb C^{2r}\times[0,\infty),
\]

of real dimension \(4r+1\). In particular,

\[
\mathcal O_P^{-1}(0)\cap\mathcal C_{13,P}
=\{\lambda uu^*: \lambda\ge0\}.
\]

## 4. Exact symmetry

The action

\[
(g,k):(G,Z,\lambda)\longmapsto(gGg^*,gZk,\lambda),
\qquad
(g,k)\in SL_2(\mathbb C)\times SU(2),
\]

preserves the cone and cubic. Its kernel is the diagonal \(\mu_2\), so the effective group is

\[
\boxed{
(SL_2(\mathbb C)\times SU(2))/\mu_2.
}
\]

The first factor is Lorentz spin. The second is right multiplication by unit quaternions and rotates the two Weyl components.

## 5. Exact relation to the old 9D object

The inclusion and retraction are

\[
\iota_9(G,z,\lambda)=(G,z,0,\lambda),
\qquad
r_9(G,z,w,\lambda)=(G,z,\lambda).
\]

Both preserve the positive cones and

\[
r_9\iota_9=\operatorname{id}.
\]

Their determinants obey

\[
\boxed{
\mathcal N_9(r_9H)-\mathcal N_{13}(H)
=w^*\operatorname{adj}(G)w\ge0.
}
\]

There is also a \(\mathbb{CP}^1\)-family of nine-dimensional slices. For a line \(L=[\ell]\subset\mathbb C^2\), set \(Z=\psi\ell^*\). On that slice,

\[
\mathcal N_{13}
=\lambda\det G-\psi^*\operatorname{adj}(G)\psi.
\]

The internal \(SU(2)\) acts transitively on these slices.

## 6. The new rank-defect carrier

The spectral-floor map identifies the rank-defect boundary with the trace-free twelve-dimensional vector space:

\[
K\longmapsto K-\lambda_{\min}(K)I_3.
\]

Therefore

\[
\boxed{
\mathcal C_{13,P}^+\cong B^{13},\qquad
(\partial\mathcal C_{13,P})^+\cong S^{12}.
}
\]

The involution \(w\mapsto-w\) fixes the old complex cone. On compactified boundaries it gives the standard pair

\[
\boxed{(S^{12},S^8).}
\]

Its complement is

\[
\boxed{S^{12}\setminus S^8\cong S^3\times\mathbb R^9.}
\]

The linking \(S^3\) is the unit sphere in the new four-dimensional spinor direction and is the unit-quaternion group \(\operatorname{Sp}(1)\cong SU(2)\).

## 7. Exact Jordan completion

The thirteen-dimensional slice is not closed under the quaternionic Jordan product. An explicit product produces an off-diagonal \(\mathbf j\)-component in the observed \(2\times2\) block. A second product produces the missing \(\mathbf k\)-component. Hence

\[
\boxed{
\operatorname{Jord}\langle\mathcal J_{13,P}\rangle
=\operatorname{Herm}_3(\mathbb H).
}
\]

The exact closure is

\[
4+4+4+1\longrightarrow6+4+4+1=15.
\]

The two added coordinates complete the Lorentz vector from signature \((1,3)\) to the quaternionic spin factor of signature \((1,5)\); the two spinors and scalar are unchanged.

## 8. The other 13D model

The same coordinates define a complex \(4\times4\) Hermitian matrix

\[
\mathcal K_{13}(G,Z,\lambda)
=\begin{pmatrix}G&Z\\Z^*&\lambda I_2\end{pmatrix}.
\]

Its determinant is

\[
\boxed{
\det\mathcal K_{13}
=\lambda\mathcal N_{13}+|\det Z|^2.
}
\]

This gives the exact distinction:

- the quaternionic \(3\times3\) model preserves the old cubic exactly;
- the complex \(4\times4\) model is quartic and adds the Pluecker term.

The quaternionic positive cone injects into the complex one, but the injection is not onto. At

\[
G=I_2,\qquad Z=I_2,\qquad\lambda=1,
\]

the complex block is positive semidefinite, while the quaternionic scalar condition would require \(1\ge2\).

On the diagonal \(Z=0\), the quartic is \(\lambda^2xy\), so two of four branches have merged into one multiplicity-two branch. Four independent simple diagonal branches require a second scalar coordinate and at least fourteen dimensions.

## 9. Exact relation to the existing colour S12

For \(A\in\operatorname{Mat}_{3\times2}(\mathbb C)\), define

\[
F_{13}(A)
=X\begin{pmatrix}A^*A&0\\0&0\end{pmatrix}X^*.
\]

This is proper and factors through the existing Gram quotient:

\[
S^{12}_{\mathrm{col}}
\longrightarrow B^4
\longrightarrow S^{12}_{13}.
\]

The map is based null-homotopic because it factors through the based-contractible ball \(B^4\). This is the exact morphism relating the two \(S^{12}\) carriers; it is not a homeomorphism between them.

## 10. Exact finite-dimensional threshold

For \(p=\alpha G\), \(\alpha>0\), let \(m^2=\alpha^2\det G\). Fix

\[
\lambda=\lambda_0>0,
\qquad
\mathcal N_{13}=\nu_0>0.
\]

Then

\[
\boxed{
m^2\ge\frac{\alpha^2\nu_0}{\lambda_0}.
}
\]

Equality holds exactly at zero Dirac spinor. Above threshold, the spinor fibre at fixed \(G\) is an ellipsoidal \(S^7\), collapsing to one point at threshold.

This is an invariant finite-dimensional threshold, not a quantum-field-theoretic mass gap.
