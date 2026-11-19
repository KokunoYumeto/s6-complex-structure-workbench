# The complete three-step odd-ideal arrow in the M2 branch

This records the full coefficient matrix used in MB.3 at the
two remaining central two-torsion points. It keeps all three
source steps and the single suspension period separate.

## MI.1. The exact source composite

Write \((X_i,\zeta_i)\), \(i=0,1,2,3\), for the successive
points of the actual chord \(p\mapsto p-G\) in ASI.2. The
base functions \(\chi,\sigma,d\) are unchanged. All \(X_i\)
are nonzero on these charts. Define \(r_i=X_{i+1}/X_i\).
Then each complete source equation is
\[
 X_{i+1}=\frac d{X_i}+\frac{2\sigma(\zeta_i+\sigma)}{X_i^2},
 \qquad \zeta_{i+1}=-r_i\zeta_i+(1-r_i)\sigma .
                                                               \tag{MI.1}
\]
Multiplying the three actual triangular coefficient matrices gives
\[
 \zeta_3=K_3\zeta_0+S_3\sigma,\qquad
 K_3=-\frac{X_3}{X_0},\quad
 S_3=1-2\frac{X_3}{X_2}+2\frac{X_3}{X_1}-\frac{X_3}{X_0}.
                                                               \tag{MI.2}
\]
Every ratio is evaluated at its stated intermediate source point.
The inverse is the three reverse chords, so this is an invertible
source arrow. At either central point \(X_0=\pm i\), the
successive values alternate between \(i\) and \(-i\). Thus
\(K_3=1,S_3=6\). The full source mixing is retained by MI.2.

## MI.2. The whole line, finite quotient and neutral coordinate

In the actual line-chain chart \(X_jY_j=\sigma\), put
\(e_j=(-1)^{j+1}\). For odd j write \(W=X_j,u=Y_j\);
for even j write \(W=Y_j,u=X_j\). The involution-fixed ideal
is exactly \((\chi,\zeta_0,W)\), and \(\sigma=Wu\).
Let \(\mathcal C=\lambda H\mathcal B_2^{\rm pt}\) be the
full genuine coefficient of MB.5 and MB.9. The complete period
to chain index \(j+4\) is
\[
 \begin{pmatrix}\chi'\\\zeta'\\W'\end{pmatrix}
 =M_j\begin{pmatrix}\chi\\\zeta_0\\W\end{pmatrix},\qquad
 M_j=\begin{pmatrix}1&0&0\\0&K_3&S_3u\\0&0&\mathcal C^{e_j}\end{pmatrix},
 \qquad u'=\mathcal C^{-e_j}u.                          \tag{MI.3}
\]
This preserves \(Wu=\sigma\) literally, and its inverse uses
the inverse source composite and inverse genuine line map.
The physical weights of \(W,u\) are \((e_j,-e_j)\), so the
off-diagonal term \(S_3uW\) has weight zero as required.
The quarter action and its inverse are the original phases
\((1,-1,j,-j-1)\) on \((\chi,\zeta,X_j,Y_j)\); j changes
by four in MI.3, leaving each phase unchanged. The residual
period on a chosen representative of the exchanged two source
points is the full \(\gamma^{-1}B\), including those phases.

Blow up the displayed ideal, write its three odd coordinates
as \(w_i=t z_i\), and take the involution quotient
\(\rho=t^2\). Every coarse quadratic is
\(w_iw_k=\rho z_i z_k\). With \(L=M_jz\), the exact map
on the target-pivot chart is
\[
 \rho'=\rho L_\beta^2,\qquad
 z'_\gamma=L_\gamma/L_\beta,\qquad
 u'=\mathcal C^{-e_j}u.                                 \tag{MI.4}
\]
All entries of \(M_j\), including their full source dependence,
remain in this morphism and its inverse. The adjacent chain
arrow is \(u'=1/u,W'=u^2W\). Its source-mixing term
\(uW\) becomes \(u'W'\), so the coefficient extends on both
ends of each actual stabilizer P1, namely the pairs 1/2 and 3/4.
This proves the full normal-ideal extension used by MB, without
replacing the three-step source map by the single-step one.
