# Independent scalar--Gauss audit, 5 September 2026

## Verdict

**PASS.** The candidate's classified-frame parameterization and phase inverse are correct. The full scalar and Gauss residuals retain the literal constants and all signs. The literal two-cross scalar--Gauss domain is nonempty at every specified original coupling \(t=g^2>0\). Neither spatial equation is used in the construction or its completeness proof.

There is no mathematical defect in the stated classified-frame bijection or literal existence theorem. There is one integration requirement for a *complete parameterization of the literal domain*: the candidate's parameter theorem begins with \(C=ie\operatorname{diag}(1,0,-1)\), and does not reproduce the argument forcing arbitrary literal temporal matrices into that form. The current canonical source proves this from scalars and Gauss alone. That argument is independently checked and reproduced below.

The resulting full raw literal parameter map is exactly two-to-one. Its only identification is

\[
 (\zeta,p_+,p_-)\sim(-\zeta,-p_+,-p_-).
\]

The candidate does not claim this larger raw map is a bijection, so the identification does not contradict its theorem. The quotient is in bijection with the entire literal domain, as proved below without selecting a square-root branch.

The one permitted serial symbolic replay passed all 25 exact check groups, process exit code 0, checker time 0.5722749999986263 seconds, with no floating-point acceptance. Analytic proofs, not the replay, establish positivity, completeness, and the inverse domains.

## Audited inputs

All paths are relative to the repository root.

| Input | SHA-256 |
|---|---|
| agent_work/two_cross_scalar_gauss_domain_20260905/scalar_gauss_domain.tex | 7974E5D3501D36F232AE0CB6D68A1161DB97102D78945B40ABA2D323FD27CDCA |
| agent_work/two_cross_scalar_gauss_domain_20260905/check_scalar_gauss_domain.py | AB9E8D9A8091533AD39FEBD1BFA106DBE31E1A5D973C2213631A940CB89A45AB |
| output/s6_consolidated_canonical_2026-08-26/supporting_materials/workbench/research/two_cross_exceptional_shared.tex | 5FC550D251C0AD93A5CCC535A7CAB3A08C3B9E81A40CA5FB52D754A300BC176C |
| output/s6_consolidated_canonical_2026-08-26/supporting_materials/workbench/research/quaternionic_4441_reconciliation.tex | 261881D4B3245F083723EE91B39C91991E171A114DF43447816726E665EC6FC9 |

The complete candidate TeX, checker, and canonical shared proof were read. In the parent, the retained-system section and exact field reduction near lines 3959--4049, and complete scalar-coordinate equivalence near lines 4593--4733, were read. The parent labels q444:cx:eq:phi, q444:cx:eq:b, q444:cx:eq:gauss agree exactly with the candidate. The canonical labels q444:twocross:temporal-form, q444:twocross:eq:first-scalar, q444:twocross:eq:second-frame, q444:twocross:eq:second-scalar, q444:twocross:eq:gauss-block give the classification and full entries audited here.

## 1. Literal equations and constants

The original real vector space is

\[
 \mathfrak{su}(3)=\{X\in M_3(\mathbb C):X^*=-X,\ \operatorname{tr}X=0\},
 \qquad \langle X,Y\rangle=-\operatorname{tr}(XY).
\]

The retained matrices and constants are

\[
 H_0=\begin{pmatrix}0&0&0\\0&-1/2&1/(2\sqrt2)\\
 0&1/(2\sqrt2)&1/2\end{pmatrix},\quad
 q=\frac1{2\sqrt2}\begin{pmatrix}1\\0\\0\end{pmatrix},\quad
 A_0=\sqrt2\begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix},
 \qquad m^2=\Gamma=1,\quad\kappa=6.
\]

For \(Y_{\rm tf}=Y-(\operatorname{tr}Y)I_3/3\), define

\[
 \mathcal I_{H_0}Y=([H_0,[H_0,Y]]+qq^*Y+Yqq^*)_{\rm tf},
 \qquad \mathcal K Y=-\sum_{j=1}^2[Z_j,[Z_j,Y]].
\]

Direct multiplication gives \(H_0q=0\), \(H_0^2=(3/8)\operatorname{diag}(0,1,1)\), \(q^*q=1/8\). Hence the parent's \(s=\operatorname{tr}H_0^2+2q^*q=1\), and its scalar coefficient \(a=m^2+\Gamma s=2\). Moreover

\[
 \operatorname{adj}H_0=\operatorname{diag}(-3/8,0,0),\quad
 6(\operatorname{adj}H_0-qq^*)_{\rm tf}=\operatorname{diag}(-2,1,1),
\]

\[
 F_0=[A_0,[A_0,H_0]]=-2H_0+\operatorname{diag}(-2,1,1).
\]

Thus the parent's scalar equations are exactly

\[
 [C,[C,H_0]]-\sum_j[Z_j,[Z_j,H_0]]-F_0=0,\qquad
 (C^2-Z_1^2-Z_2^2)q+2q=0.
\]

The parent's Gauss equation is

\[
 (\mathcal I_{H_0}+2\mathcal K/g^2)C=(4\omega/g^2)[Z_1,Z_2].
\]

For the original \(t=g^2>0\), multiplication and division by that same \(t\) are inverse, giving precisely

\[
 (t\mathcal I_{H_0}+2\mathcal K)C-4\omega[Z_1,Z_2]=0.
\]

The two scalar codomains are respectively the trace-free Hermitian matrices and \(\mathbb C^3\); Gauss has codomain \(\mathfrak{su}(3)\). No spatial equation has been substituted into these residuals.

## 2. Complete temporal classification from only scalars and Gauss

Set \(P=\operatorname{diag}(1,0,0)\). The selected spatial class and its complementary block space are

\[
 \mathfrak p=\left\{X(v)=\begin{pmatrix}0&-v^*\\v&0_2\end{pmatrix}:
 v\in\mathbb C^2\right\},\qquad
 \mathfrak k=\{X\in\mathfrak{su}(3):[X,P]=0\}.
\]

Block multiplication gives the orthogonal direct sum \(\mathfrak{su}(3)=\mathfrak k\oplus\mathfrak p\), with \([\mathfrak p,\mathfrak p]\subset\mathfrak k\), \([\mathfrak k,\mathfrak p]\subset\mathfrak p\). The inverse of \(v\mapsto X(v)\) is its lower first column. Since \(H_0,qq^*\) are block diagonal, \(\mathcal I_{H_0}\) preserves both summands. Specifically \(H_0X(v)H_0=0\), the two \(H_0^2\) products sum to \((3/8)X(v)\), and the two \(qq^*\) products sum to \(X(v)/8\), with all terms traceless. Therefore

\[
 \mathcal I_{H_0}|_{\mathfrak p}=\tfrac12\operatorname{id}_{\mathfrak p}.
\]

When \(Z_j\in\mathfrak p\), the bracket inclusions make \(\mathcal K\) preserve both summands. Cyclicity gives

\[
 \langle Y,\mathcal K Y\rangle
 =-\sum_j\operatorname{tr}([Z_j,Y]^2)
 =\sum_j\|[Z_j,Y]\|^2\ge0.
\]

The \(\mathfrak p\) projection of Gauss is

\[
 (\tfrac t2\operatorname{id}+2\mathcal K|_{\mathfrak p})C_{\mathfrak p}=0.
\]

Its inner product with \(C_{\mathfrak p}\) is a sum of nonnegative terms, the first \((t/2)\|C_{\mathfrak p}\|^2\). As \(t>0\), \(C_{\mathfrak p}=0\). Thus every literal scalar--Gauss solution has \(C\in\mathfrak k\); this is a consequence, not a hypothesis.

Retain exactly

\[
 r=\frac{\sqrt6}{4},\quad\delta=\frac1{2r}=\sqrt{\frac23},\quad
 x=\frac12,\quad d_0=\frac1{2\sqrt2},\quad
 S=\frac1{\sqrt{2r(r+x)}}\begin{pmatrix}d_0&-(r+x)\\r+x&d_0\end{pmatrix},
 \qquad U=\operatorname{diag}(1,S).
\]

Since \(r^2=x^2+d_0^2\), the numerator columns are orthogonal with squared length \(2r(r+x)\), and its determinant is \(2r(r+x)>0\). Multiplication by the lower block of \(H_0\) gives ordered eigenvalues \(r,-r\). Hence \(U^*U=I_3\), \(\det U=1\), \(U^*H_0U=\operatorname{diag}(0,r,-r)\), and \(Uq=q\).

In this first frame the arbitrary temporal block has the exact coordinates

\[
 C_d=\begin{pmatrix}
 ia&0&0\\0&i(h-a)/2&z\\0&-\bar z&-i(a+h)/2
 \end{pmatrix},\qquad a,h\in\mathbb R,\ z\in\mathbb C.
\]

Let the spatial vectors here be \(\widetilde v,\widetilde w\), and write \(\widetilde M=\widetilde v\widetilde v^*+\widetilde w\widetilde w^*\). The complete vector residual is

\[
 (-a^2+\operatorname{tr}\widetilde M+2)q.
\]

The complete adjoint residual is

\[
 \begin{pmatrix}
 2-2r(\widetilde M_{11}-\widetilde M_{22})&0&0\\
 0&-4r|z|^2+2r\widetilde M_{11}-1+2r&-2irhz\\
 0&2irh\bar z&4r|z|^2-2r\widetilde M_{22}-1-2r
 \end{pmatrix}.
\]

For verification, put \(D=\operatorname{diag}(r,-r)\). The lower scalar spatial contribution is \(\widetilde M D+D\widetilde M\), with diagonal entries \(2r\widetilde M_{11},-2r\widetilde M_{22}\) and zero off-diagonal entries. The temporal double commutator has diagonal entries \(-4r|z|^2,4r|z|^2\) and off-diagonal entries \(-2irhz,2irh\bar z\). The lower force is \(I_2-2D\), and the upper residual is \(-2r(\widetilde M_{11}-\widetilde M_{22})+2\). Squaring \(C_d\) and the two spatial blocks gives the displayed vector residual. These account for all entries.

The full scalar zero set is consequently

\[
 a^2=2+\operatorname{tr}\widetilde M,\quad
 2|z|^2-\widetilde M_{11}=1-\delta,\quad
 2|z|^2-\widetilde M_{22}=1+\delta,\quad hz=0.
\]

The upper matrix entry is minus the lower trace. Adding the middle equations gives \(4|z|^2=2+\operatorname{tr}\widetilde M=a^2\). As \(\widetilde M_{22}\ge0\) and \(1+\delta>0\), \(z\ne0\), so \(h=0\) and \(a\ne0\).

Set \(e=a\), \(\gamma=-2iz/e\), and choose either root \(\zeta^2=-\bar\gamma\). Then \(|\gamma|=|\zeta|=1\), and \(\gamma=-\zeta^{-2}\). Define

\[
 W(\zeta)=\frac{\zeta}{\sqrt2}\begin{pmatrix}\gamma&\gamma\\1&-1\end{pmatrix}
 =\frac1{\sqrt2}\begin{pmatrix}-\zeta^{-1}&-\zeta^{-1}\\\zeta&-\zeta\end{pmatrix},
 \quad V=\operatorname{diag}(1,W),\quad B(\zeta)=UV.
\]

The entries give \(W^*W=I_2\), \(\det W=-\zeta^2\gamma=1\). The lower Hermitian block of \(-iC_d\) is

\[
 \frac e2\begin{pmatrix}-1&\gamma\\\bar\gamma&-1\end{pmatrix}.
\]

Its products with \((\gamma,1)^T,(\gamma,-1)^T\) have eigenvalues \(0,-e\), respectively. The same columns give \(W^*DW=\left(\begin{smallmatrix}0&r\\r&0\end{smallmatrix}\right)\). Therefore the simultaneous change gives

\[
 C'=ie\operatorname{diag}(1,0,-1),\quad
 H'=\begin{pmatrix}0&0&0\\0&0&r\\0&r&0\end{pmatrix},\quad q'=q,\quad
 F'=-2H'+\operatorname{diag}(-2,1,1).
\]

For every datum the exact forward and inverse are \(Y'=B^*Y_0B\), \(Y_0=BY'B^*\). Since \(B^*B=I_3\), \(Bq=q\), and \([B,P]=0\), these preserve products, brackets, adjoints, trace projection, and the selected class. Every full matrix residual is conjugated, and the vector residual is multiplied by \(B^*\). Thus every literal solution has a classified representative, and each classified solution yields literal solutions for all retained \(\zeta\).

## 3. Full classified equations

For arbitrary \(v,w\in\mathbb C^2\), set \(Z_1=X(v)\), \(Z_2=X(w)\) and

\[
 M=vv^*+ww^*=\begin{pmatrix}u&m\\\bar m&v_0\end{pmatrix},\quad
 N=i(vw^*-wv^*),\quad b=\operatorname{Im}(v^*w),\quad
 Q=\operatorname{diag}(1,2),\quad E=\operatorname{diag}(2/3,-5/6).
\]

Here \(M\succeq0\), \(N=N^*\), and \(\operatorname{tr}N=2b\), since \(\operatorname{tr}(vw^*)=\overline{v^*w}\). Squaring the blocks gives \(X(v)^2=\operatorname{diag}(-v^*v,-vv^*)\). The complete scalar residuals are

\[
 Q_H=\begin{pmatrix}
 2-4r\operatorname{Re}m&0&0\\
 0&2r\operatorname{Re}m-1&r(\operatorname{tr}M-e^2+2)\\
 0&r(\operatorname{tr}M-e^2+2)&2r\operatorname{Re}m-1
 \end{pmatrix},\quad Q_q=(\operatorname{tr}M-e^2+2)q.
\]

Indeed the upper spatial contribution is \(-4r\operatorname{Re}m\), the lower one is \(MH'_{\rm lower}+H'_{\rm lower}M\), and the temporal lower double commutator has off-diagonal entries \(-e^2r\); adding \(-F'\) gives precisely the displayed entries. Thus the entire scalar zero set is

\[
 e^2=2+u+v_0,\qquad m=\delta+iy,\quad y\in\mathbb R.
\]

In particular \(m\ne0\), \(e\ne0\). The Gauss blocks follow from

\[
 [C',X(v)]=X(-ieQv),\quad [X(v),X(w)]=\operatorname{diag}(-2ib,iN),
\]

\[
 \mathcal I_{H'}C'=ie\operatorname{diag}(1/6,2/3,-5/6),\quad
 \mathcal K C'=\operatorname{diag}(2ie\operatorname{tr}(QM),-ie(QM+MQ)).
\]

The two inertia contributions are \(ie\operatorname{diag}(0,3/4,-3/4)\) and \(ie\operatorname{diag}(1/6,-1/12,-1/12)\). These retain \(r^2=3/8\), \(q^*q=1/8\), and the trace projection factor \(1/3\). Consequently the entire Gauss residual is

\[
 Q_G=i\operatorname{diag}(\gamma_0,\mathcal G),\quad
 \gamma_0=et/6+4e(u+2v_0)+8\omega b,\quad
 \mathcal G=etE-2e(QM+MQ)-4\omega N.
\]

There are no off-block entries. Since \(\operatorname{tr}E=-1/6\), \(\operatorname{tr}(QM+MQ)=2(u+2v_0)\), and \(\operatorname{tr}N=2b\), the identity \(\operatorname{tr}\mathcal G=-\gamma_0\) holds before imposing any equation. Thus full Gauss is equivalent to the full lower block.

With \(k=e/\omega\ne0\), this equation is exactly

\[
 N=kT,\qquad
 T=\frac t4E-\frac12(QM+MQ)
 =\begin{pmatrix}t/6-u&-3m/2\\-3\bar m/2&-5t/24-2v_0\end{pmatrix}.
\]

## 4. Necessity and exclusion of every singular case

Let \(D=(v\ w)\) and \(J=\left(\begin{smallmatrix}0&i\\-i&0\end{smallmatrix}\right)\). Multiplication gives

\[
 M=DD^*,\quad N=DJD^*,\quad
 M+N=(v-iw)(v-iw)^*,\quad M-N=(v+iw)(v+iw)^*.
\]

If \(M\) had rank one, then \(\ker D^*=\ker M\) implies \(N\) annihilates the orthogonal complement of \(\operatorname{ran}M\), and its range is in that line. A Hermitian operator supported on this line is a real multiple of \(M\), so \(N=\nu M\) with \(\nu\in\mathbb R\). Because \(m\ne0\), its off-diagonal Gauss entry gives \(\nu=-3k/2\). The first diagonal entry then gives

\[
 k(t/6-u)=-3ku/2,\qquad t/6=-u/2.
\]

This is impossible: positivity of \(M\) and \(|m|^2\le uv_0\) imply \(u,v_0>0\), while \(t>0\). Rank zero is excluded by \(m\ne0\). Hence \(M>0\), and

\[
 d=\det M=uv_0-\delta^2-y^2>0.
\]

Now \(D\) is invertible, and

\[
 M^{-1}N=D^{-*}JD^*,\qquad
 \operatorname{tr}(M^{-1}N)=0,\qquad \det N=-\det M=-d.
\]

The inverse \(M^{-1}=d^{-1}\left(\begin{smallmatrix}v_0&-m\\-\bar m&u\end{smallmatrix}\right)\) gives the exact trace equation

\[
 \begin{aligned}
 0=d\operatorname{tr}(M^{-1}T)
 &=v_0(t/6-u)+u(-5t/24-2v_0)+3|m|^2\\
 &=\frac{t(4v_0-5u)}{24}-3d.
 \end{aligned}
\]

Thus \(c=4v_0-5u>0\), \(t=72d/c\). The determinant equation \(k^2\det T=-d\) gives \(\det T<0\) and exactly the two signs

\[
 e=\epsilon\sqrt{2+u+v_0},\quad
 k=\sigma\sqrt{\frac d{-\det T}},\quad
 \omega=e/k,\qquad \epsilon,\sigma\in\{1,-1\}.
\]

Every solution therefore lies in the candidate's exact domain

\[
 \mathcal D=\{(u,v_0,y)\in\mathbb R^3:
 u>0,\ d=uv_0-\delta^2-y^2>0,\ c=4v_0-5u>0\}.
\]

No \(d=0\), \(c=0\), \(e=0\), or \(\det T=0\) case is discarded without an impossibility proof.

## 5. Sufficiency and the full phase inverse

Start with any point of \(\mathcal D\) and the displayed formulas. The invertible matrix

\[
 L=\begin{pmatrix}\sqrt u&0\\\bar m/\sqrt u&\sqrt d/\sqrt u\end{pmatrix}
\]

satisfies \(LL^*=M\), \(\det L=\sqrt d>0\). In particular \(v_0=(d+|m|^2)/u>0\). The specified \(t=72d/c>0\) makes \(\operatorname{tr}(M^{-1}T)=0\).

Put \(R=L^{-1}TL^{-*}\). It is Hermitian of trace zero, so \(R=\left(\begin{smallmatrix}a&z\\\bar z&-a\end{smallmatrix}\right)\) with real \(a\). Since \(T_{12}=-3m/2\ne0\), \(R\ne0\). Therefore

\[
 \det R=-a^2-|z|^2<0,\qquad \det T=d\det R<0.
\]

Both displayed signs of \(k\) are well defined and nonzero. The Hermitian \(J_0=kR\) has trace zero and determinant \(-1\). Multiplying its two-by-two form gives \(J_0^2=I_2\). For every \(z_0\in\mathbb C^2\),

\[
 z_0^*(I_2\pm J_0)z_0=\tfrac12\|(I_2\pm J_0)z_0\|^2\ge0.
\]

Each \(I_2\pm J_0\) has determinant zero and trace two, hence rank one. Invertible congruence therefore gives positive rank-one matrices

\[
 A_\pm=M\pm kT=L(I_2\pm J_0)L^*.
\]

Write \(h_s=(A_s)_{11}\), \(s\in\{1,-1\}\). If \(h_s=0\), its determinant forces \((A_s)_{12}=0\). But

\[
 (A_s)_{12}=m(1-3sk/2),\qquad
 h_s=u+sk(t/6-u).
\]

As \(m\ne0\), this would imply \(sk=2/3\) and then \(h_s=u/3+t/9>0\), a contradiction. Hence \(h_+,h_->0\) everywhere on \(\mathcal D\).

Define

\[
 a_\pm=\begin{pmatrix}\sqrt{h_\pm}\\(A_\pm)_{21}/\sqrt{h_\pm}\end{pmatrix}.
\]

The rank-one determinant identity gives \((A_\pm)_{22}=|(A_\pm)_{21}|^2/h_\pm\), and thus \(a_\pm a_\pm^*=A_\pm\). For arbitrary \(p_\pm\in U(1)\), let

\[
 v=\frac{p_+a_++p_-a_-}{2},\qquad
 w=\frac{i(p_+a_+-p_-a_-)}{2}.
\]

These signs give exactly \(v-iw=p_+a_+\), \(v+iw=p_-a_-\). Their outer products, added and subtracted, give \(vv^*+ww^*=M\), \(i(vw^*-wv^*)=N=kT\). The scalars hold by construction, and the complete lower Gauss block vanishes:

\[
 etE-2e(QM+MQ)-4\omega kT
 =etE-2e(QM+MQ)-4e\left(\frac t4E-\frac12(QM+MQ)\right)=0.
\]

The upper entry vanishes by its trace identity. This proves sufficiency for every entry of all three residuals.

Conversely a classified solution recovers \(M\), hence \(u,v_0,y\), then \(\epsilon=\operatorname{sign}e\), \(\sigma=\operatorname{sign}(e/\omega)\). These recover \(A_\pm,h_\pm>0\), and the phases are exactly

\[
 p_+=\frac{(v-iw)_1}{\sqrt{h_+}},\qquad
 p_-=\frac{(v+iw)_1}{\sqrt{h_-}}.
\]

To prove the inverse on both vector coordinates, if \(cc^*=a_\pm a_\pm^*\), then \(|c_1|=\sqrt{h_\pm}\), so \(c_1=p\sqrt{h_\pm}\) for a unique unit \(p\). The \((2,1)\) entry gives \(c_2\overline{c_1}=(a_\pm)_2\sqrt{h_\pm}\), hence \(c_2=p(a_\pm)_2\). Thus the displayed inverse recovers both components, with no remaining phase or zero denominator.

This proves the candidate's precise bijection

\[
 \mathcal D\times\{1,-1\}^2\times U(1)^2
 \longleftrightarrow
 \{(t,\omega,e,v,w):\text{all classified scalar--Gauss entries vanish}\}.
\]

## 6. Complete literal parameter map and its fibres

Let \(\mathcal S_{\rm lit}\) be the entire literal domain of tuples \((t,\omega,C_0,Z_{1,0},Z_{2,0})\) with \(t>0\), \(\omega\ne0\), \(Z_{j,0}\in\mathfrak p\), and all three residuals zero. Define

\[
 \mathcal P=\mathcal D\times\{1,-1\}^2\times U(1)^2\times U(1)
\]

with coordinates \((u,v_0,y,\epsilon,\sigma,p_+,p_-,\zeta)\). The raw map \(F:\mathcal P\to\mathcal S_{\rm lit}\) uses Section 5 for \(t,\omega,e,v,w\) and sets

\[
 C_0=B(\zeta)ie\operatorname{diag}(1,0,-1)B(\zeta)^*,\quad
 Z_{1,0}=B(\zeta)X(v)B(\zeta)^*,\quad
 Z_{2,0}=B(\zeta)X(w)B(\zeta)^*.
\]

It is surjective by Sections 2 and 5: from a literal tuple compute \(C_d=U^*C_0U\), recover \(e=-i(C_d)_{11}\ne0\), \(z=(C_d)_{23}\), \(\gamma=-2iz/e\), choose either root \(\zeta^2=-\bar\gamma\), and conjugate all matrices by \(B(\zeta)^*\). The classified inverse then recovers all remaining parameters in their specified domains.

For the exact fibre, \(W(-\zeta)=-W(\zeta)\). With \(D_0=\operatorname{diag}(1,-I_2)\), this gives \(B(-\zeta)=B(\zeta)D_0\). Block multiplication gives

\[
 D_0C'D_0=C',\qquad D_0X(v)D_0=X(-v).
\]

Replacing \((p_+,p_-)\) by \((-p_+,-p_-)\) replaces \((v,w)\) by \((-v,-w)\). Therefore \(F\) is invariant under

\[
 \iota(u,v_0,y,\epsilon,\sigma,p_+,p_-,\zeta)
 =(u,v_0,y,\epsilon,\sigma,-p_+,-p_-,-\zeta).
\]

Suppose two parameters give the same literal tuple. Its common \(C_d\) determines the same \(e,z,\gamma\); therefore their roots satisfy \(\zeta_2=\zeta_1\) or \(\zeta_2=-\zeta_1\). In the first case the classified matrices coincide and the classified bijection makes all other parameters equal. In the second case their classified spatial vectors differ by common minus sign. Their \(M,N\) are unchanged, so \(u,v_0,y,\epsilon,\sigma\) coincide; the phase inverse forces \(p_{+,2}=-p_{+,1}\), \(p_{-,2}=-p_{-,1}\). These are precisely the two points in the displayed orbit. Since \(\zeta\in U(1)\), \(\zeta=-\zeta\) is impossible. Thus every fibre has exactly two elements and

\[
 \mathcal P/\langle\iota\rangle\longleftrightarrow\mathcal S_{\rm lit}
\]

is a bijection with the complete inverse just proved. This closes literal completeness without deleting any phase.

## 7. Every prescribed original positive coupling

For \(\rho>1/\sqrt2\), choose

\[
 M_\rho=\delta\begin{pmatrix}\rho&1\\1&2\rho\end{pmatrix},\quad
 u=\delta\rho,\quad v_0=2\delta\rho,\quad y=0.
\]

Then \(u>0\), \(d=\delta^2(2\rho^2-1)>0\), \(c=3\delta\rho>0\). Thus this is in \(\mathcal D\), with original coupling

\[
 t=\frac{72d}{c}=\frac{24\delta(2\rho^2-1)}{\rho}.
\]

For every prescribed \(\tau=g^2>0\), put

\[
 \rho(\tau)=\frac{\tau+\sqrt{\tau^2+4608\delta^2}}{96\delta}.
\]

Because \(\sqrt{4608\delta^2}=48\sqrt2\delta\), the strict positivity of \(\tau\) implies \(\rho(\tau)>1/\sqrt2\). Direct substitution, or the positive quadratic root formula, gives

\[
 48\delta\rho(\tau)^2-\tau\rho(\tau)-24\delta=0.
\]

Since \(\rho(\tau)>0\), dividing by it gives exactly \(t=\tau\). Sections 5 and 6 therefore produce literal solutions for all independent \(\epsilon,\sigma,p_+,p_-,\zeta\). The signs are \(\operatorname{sign}e=\epsilon\), \(\operatorname{sign}\omega=\epsilon\sigma\), so each temporal sign and each frequency sign occurs independently. At fixed \(\zeta\), distinct phase pairs give distinct classified tuples and hence distinct literal tuples under the same invertible conjugation. This proves continuous phase families at every specified coupling.

The candidate's explicit short example is \(\rho=1\), with

\[
 M=\delta\begin{pmatrix}1&1\\1&2\end{pmatrix},\quad
 t=24\delta,\quad d=\delta^2,\quad
 T=\frac{3\delta}{2}\begin{pmatrix}2&-1\\-1&-6\end{pmatrix},
\]

\[
 \det T=-117\delta^2/4,\quad k=\frac{2\sigma}{3\sqrt{13}},\quad
 e=\epsilon\sqrt{2+3\delta},\quad \omega=\frac{3\sigma\sqrt{13}}2e,\quad
 N=\frac{\sigma\delta}{\sqrt{13}}\begin{pmatrix}2&-1\\-1&-6\end{pmatrix}.
\]

For either sign \(s\), the first entry of \(A_s\) is \(\delta(1+2s\sigma/\sqrt{13})>0\), and the exact identity

\[
 (1-s\sigma/\sqrt{13})^2
 =(1+2s\sigma/\sqrt{13})(2-6s\sigma/\sqrt{13})
\]

verifies its entire rank-one factor. Its scalars vanish because \(2r\delta=1\), \(\operatorname{tr}M=3\delta\), \(e^2=2+3\delta\). Its full lower Gauss block vanishes since

\[
 tE-2(QM+MQ)=\delta\begin{pmatrix}12&-6\\-6&-36\end{pmatrix}
 =\frac{4\omega}{e}N.
\]

Finally \(b=(\operatorname{tr}N)/2=-2\sigma\delta/\sqrt{13}\), and the upper entry is

\[
 \gamma_0=4e\delta+20e\delta+
 8\left(\frac{3\sigma\sqrt{13}}2e\right)
 \left(-\frac{2\sigma\delta}{\sqrt{13}}\right)=0.
\]

Thus both the explicit point and the entire every-coupling family are verified with all coefficients retained.

## 8. Checker audit and integration consequence

The checker treats all eight real components of \(v,w\) as independent symbols and constructs all three full residuals directly from the retained matrices. Its phase calculations use exactly \(\overline z=z^{-1}\) on \(U(1)\), with no phase set to one. Its comparison function applies exact symbolic expansion, rational cancellation over algebraic extensions, and radical rationalization, then requires each entry to equal zero. Timing floats have no role in acceptance.

The replay checks all general residual entries, the trace condition including \(y\), determinant and factor identities, both explicit signs, both continuous vector phases, every frame phase, and the inverse for the prescribed coupling. The general rank exclusion, positivity, inverse phase surjectivity, and full literal temporal classification are analytic statements proved above rather than inferred from that replay.

The canonical quantitative certificate's sentence that it does not assert scalar--Gauss nonemptiness can now be followed or replaced by the every-positive-coupling result. Its bound and its exclusion of full solutions remain consistent: the new domain imposes the two scalar equations and Gauss, whereas the full-solution exclusion additionally imposes both spatial equations. No full rotating-ansatz solution or quantum conclusion is asserted here.

All review writes were confined to this review directory. No canonical source, candidate source, PDF, remote state, Lean process, or other user task was changed.
