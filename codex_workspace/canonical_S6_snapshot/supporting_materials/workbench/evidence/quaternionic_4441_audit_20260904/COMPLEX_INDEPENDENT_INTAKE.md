# Independent intake of the complex rotating-gauge continuation

Date: 4 September 2026. This report concerns only the pending rotating-gauge continuation. It does not edit, certify, or delay the separate homogeneous quantum draft. No canonical or remote file was changed.

## 1. Decision and exact scope

**Accept the mathematical exclusion as stated, with a narrow correction to the description of checker coverage.** I found no incorrect sign, lost scalar branch, discarded complex phase, unjustified nonzero division, or hidden positivity assumption in the two contradictions.

The accepted assertion is that the five finite equations below have no solution with

\[
C\in\mathfrak p,\qquad Z_1\in\mathfrak p,\qquad Z_2\in\mathfrak k,
\]

or with a constant real spatial rotation putting the ordered pair into that form while retaining \(C\in\mathfrak p\). Here the splitting is defined by the **fixed matter line**, not by an arbitrarily chosen decomposition:

\[
P=\frac{qq^*}{q^*q}=\operatorname{diag}(1,0,0),\qquad Q=I_3-P,
\]

\[
\mathfrak p=\{X\in\mathfrak{su}(3):PXP=QXQ=0\},\qquad
\mathfrak k=\{X\in\mathfrak{su}(3):[X,P]=0\}.
\]

Both are real four-dimensional subspaces. Their exact projections are

\[
\pi_{\mathfrak p}X=PXQ+QXP,\qquad
\pi_{\mathfrak k}X=PXP+QXQ,
\]

so \(\mathfrak{su}(3)=\mathfrak p\oplus\mathfrak k\), with no deleted coordinates. The accepted spatial saturation means precisely that there is a real \(\theta\) such that

\[
\cos\theta\,\pi_{\mathfrak k}Z_1-\sin\theta\,\pi_{\mathfrak k}Z_2=0,
\qquad
\sin\theta\,\pi_{\mathfrak p}Z_1+\cos\theta\,\pi_{\mathfrak p}Z_2=0.
\]

It does not mean that an arbitrary complex pair has this property. In particular, neither \(\pi_{\mathfrak k}C=0\) nor either displayed pair relation is proved for an unrestricted solution. The unrestricted constant-\(C\), two-spatial-rotation finite system remains unresolved. This report proves an exact further reduction of that unrestricted system in Section 8; it does not assert existence or nonexistence there.

## 2. Sources and verification receipt

The complete proposed TeX, checker, and receipt were read:

- `agent_work/quaternionic_complex_rotation_20260904/complex_rotation_partial.tex`;
- `agent_work/quaternionic_complex_rotation_20260904/check_complex_rotation.py`;
- `agent_work/quaternionic_complex_rotation_20260904/CHECK_RESULTS.md`.

The retained equations and coordinate maps were compared with the canonical module `output/s6_consolidated_canonical_2026-08-26/supporting_materials/workbench/research/quaternionic_4441_reconciliation.tex`, especially `q444:gauge-eom`, `q444:static-lift-system`, `q444:real-no-lift`, and `q444:static-complex-no-lift`, and with Section 8 of the corresponding evidence directory's `PRO_FEEDBACK.md`.

The only calculation process executed for this intake was

```text
python -u agent_work/quaternionic_complex_rotation_20260904/check_complex_rotation.py
```

It returned exit code 0 in approximately 1.7 seconds:

```text
PASS: literal H,q,A, couplings and exact inverse coordinate map
PASS: complete scalar block classification without phase restrictions
PASS: exact complex SU(2) map and inverse in the nonzero-phase branch
PASS: full Gauss and both spatial residuals in diagonal matter frame
PASS: full Gauss and both spatial residuals in off-diagonal matter frame
PASS: both scalar branches, exact inertia factors and contradiction ratio
PASS: universal scalar, Gauss and spatial pairing identities on full complex data
ALL EXACT CHECKS PASSED. The unrestricted finite su(3)^3 system remains OPEN.
```

No exploratory script, numerical optimizer, large elimination, Lean process, TeX build, or remote operation was run. The mathematical review below is independent of the checker's printed descriptions.

## 3. Original fields, five equations, and signs

Retain

\[
H=\begin{pmatrix}0&0&0\\0&-1/2&1/(2\sqrt2)\\0&1/(2\sqrt2)&1/2\end{pmatrix},
\quad q=\frac{e_1}{2\sqrt2},
\quad A=\sqrt2\begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix},
\]

\[
(m^2,\Gamma,\kappa)=(1,1,6),\quad s=\operatorname{tr}H^2+2q^*q=1,
\quad a=2,\quad g^2>0,\quad\omega\in\mathbb R\setminus\{0\}.
\]

For a matrix \(M\), write \(M_{\mathrm{tf}}=M-\operatorname{tr}(M)I_3/3\). Set

\[
\mathcal IX=([H,[H,X]]+qq^*X+Xqq^*)_{\mathrm{tf}},\qquad
\mathcal KX=-\sum_{j=1}^2[Z_j,[Z_j,X]],
\]

\[
F=[A,[A,H]]=-2H+\operatorname{diag}(-2,1,1).
\]

The equations under review are exactly

\[
[C,[C,H]]-\sum_j[Z_j,[Z_j,H]]=F, \tag{S_H}
\]

\[
(C^2-Z_1^2-Z_2^2)q=-2q, \tag{S_q}
\]

\[
(g^2\mathcal I+2\mathcal K)C=4\omega[Z_1,Z_2], \tag{G}
\]

\[
-\omega^2Z_1-2\omega[C,Z_2]+[C,[C,Z_1]]+\mathcal KZ_1+(g^2/2)\mathcal IZ_1=0, \tag{Y_1}
\]

\[
-\omega^2Z_2+2\omega[C,Z_1]+[C,[C,Z_2]]+\mathcal KZ_2+(g^2/2)\mathcal IZ_2=0. \tag{Y_2}
\]

Every unknown lies in the real Lie algebra of traceless anti-Hermitian complex matrices \(\mathfrak{su}(3)\). Equation (G) is obtained by multiplication by the retained positive number \(g^2\), not by setting a coupling to one.

To verify the original map, retain

\[
u=(1,1,1)^T,\quad v_0=(1,-1,0)^T,\quad w_0=(1,1,-2)^T,
\quad K=(v_0/\sqrt2,w_0/\sqrt6,u/\sqrt3),
\]

\[
\Phi_0=\tfrac14\begin{pmatrix}1&1&1\\1&1&1\\1&1&-2\end{pmatrix},\quad
b_0=v_0/4,\quad
\Omega=\sqrt{2/3}\begin{pmatrix}0&-1&1\\1&0&-1\\-1&1&0\end{pmatrix},\quad O(t)=e^{t\Omega}.
\]

The three columns before length factors have squared lengths \(2,6,3\), zero pairwise inner products, and determinant 6. Thus \(K\in SO(3)\). Also

\[
\Phi_0v_0=0,\quad\Phi_0w_0=(0,0,3/2)^T,\quad
\Phi_0u=(3/4,3/4,0)^T,
\]

which give \(K^*\Phi_0K=H\) and \(K^*b_0=q\). The identities
\(\Omega v_0=\sqrt{2/3}w_0\), \(\Omega w_0=-3\sqrt{2/3}v_0\), and \(\Omega u=0\) give \(K^*\Omega K=A\).

For

\[
Y_1=\cos(\omega t)Z_1-\sin(\omega t)Z_2,\quad
Y_2=\sin(\omega t)Z_1+\cos(\omega t)Z_2,\quad Y_3=0,
\]

the original connection is

\[
\mathcal A_0=OKCK^*O^*-\Omega,\qquad
\mathcal A_i=OKY_iK^*O^*.
\]

Its inverse is \(C=K^*O^*\mathcal A_0OK+A\), \(Y_i=K^*O^*\mathcal A_iOK\). Under the gauge transformation \(G(t)=K^*O(t)^*\), the temporal inhomogeneous term is \(-\dot GG^*=A\). This establishes the displayed inverse without deleting the temporal connection. The prescribed scalar fields remain \(O\Phi_0O^*\), \(Ob_0\), with their original frequency \(\sqrt2\), independently of \(\omega\).

In constant-matter coordinates, \(E_i=\dot Y_i+[C,Y_i]\) and the projected currents are \((J_0)_{\mathrm{tf}}=-\mathcal IC\), \((J_i)_{\mathrm{tf}}=-\mathcal IY_i\). The canonical Gauss equation is

\[
(2/g^2)\sum_i[Y_i,E_i]+\mathcal IC=0.
\]

Now \(\dot Y_1=-\omega Y_2\), \(\dot Y_2=\omega Y_1\), so
\(\sum_i[Y_i,\dot Y_i]=-2\omega[Z_1,Z_2]\). Also
\(\sum_i[Y_i,[C,Y_i]]=\mathcal KC\). These give (G), including the positive \(4\omega\) on its right. Applying \((\partial_t+\operatorname{ad}C)^2\) to the spatial pair gives exactly the opposite gyroscopic signs in (Y_1) and (Y_2). The third spatial equation is zero. The source therefore agrees with the canonical sign and coefficient conventions.

## 4. Universal identities are correct

On \(\mathfrak{su}(3)\), use \(\langle X,Y\rangle=-\operatorname{tr}(XY)\) and \(\|X\|^2=-\operatorname{tr}X^2\). Cyclicity proves

\[
\langle X,\mathcal IX\rangle=\operatorname{tr}[X,H]^2+2\|Xq\|^2\ge0,
\qquad
\langle X,\mathcal KX\rangle=\sum_j\|[Z_j,X]\|^2\ge0.
\]

In the first formula \([X,H]\) is Hermitian. The vector term is \(-2q^*X^2q=2\|Xq\|^2\); the trace projection pairs to zero against traceless \(X\).

Write

\[
c=\langle C,\mathcal IC\rangle,\quad z=\sum_j\langle Z_j,\mathcal IZ_j\rangle,
\quad k=\sum_j\|[C,Z_j]\|^2,
\]

\[
d=\|[Z_1,Z_2]\|^2,\quad z_0=\|Z_1\|^2+\|Z_2\|^2,
\quad\beta=\langle C,[Z_1,Z_2]\rangle.
\]

Pair (S_H) with \(H\) by ordinary trace and (S_q) with \(2q^*\) by real part. The left sides sum to \(-c+z\), and the right sides sum to
\(\operatorname{tr}(HF)-4q^*q=-3/2-1/2=-2\). Pairing (G) with \(C\) and dividing by 2 gives the second identity below. The spatial pairings contribute respectively \(-\omega^2z_0\), \(+4\omega\beta\), \(-k\), \(+2d\), and \((g^2/2)z\). Thus

\[
c-z=2,\qquad (g^2/2)c+k=2\omega\beta,
\qquad\omega^2z_0=k+2d+g^2c+(g^2/2)z.
\]

Since \(c\ge2\), the second identity forces \(\omega\beta>0\). Consequently \(d,z_0>0\). Invariance of the inner product gives
\(\beta=\langle[C,Z_1],Z_2\rangle=-\langle[C,Z_2],Z_1\rangle\), so also \(k>0\). Cauchy–Schwarz applied to the two ordered pairs gives \(4\beta^2\le kz_0\). It follows that

\[
\omega^2z_0\ge (k+g^2c/2)^2/k,
\]

and substitution of the third identity gives

\[
8kd+2g^2kz\ge g^4c^2.
\]

Every division here has a proved positive denominator. These identities are necessary conditions, not a proof of exclusion of a general noncommuting complex triple.

## 5. Scalar branch classification is exhaustive

Let \(x=1/2\), \(d_0=1/(2\sqrt2)\), \(r=\sqrt6/4\), and

\[
S=\frac1{\sqrt{2r(r+x)}}
\begin{pmatrix}d_0&-(r+x)\\r+x&d_0\end{pmatrix},\qquad U=\operatorname{diag}(1,S).
\]

The denominator is positive. The two columns of \(S\) have squared length \(2r(r+x)\), are orthogonal, and have determinant numerator \(2r(r+x)\). Multiplication with the lower block of \(H\) gives eigenvalues \(r,-r\), in that order. Hence
\(U^*HU=\operatorname{diag}(0,r,-r)\), \(U^*q=q\), and \(U\in SO(3)\). Conjugation of every matrix and the force by \(U^*\), with inverse conjugation by \(U\), preserves all equations and the subspaces defined by \(P\).

Write

\[
C=X(v),\quad Z_1=X(w),\qquad
X(v)=\begin{pmatrix}0&-v^*\\v&0_{2\times2}\end{pmatrix},\quad v,w\in\mathbb C^2,
\]

\[
Z_2=i\operatorname{diag}(\eta,B),\qquad
B=-\frac\eta2I_2+\begin{pmatrix}z&x_1-ix_2\\x_1+ix_2&-z\end{pmatrix},
\]

where \(\eta,z,x_1,x_2\) are real. This retains every coordinate of \(\mathfrak k\). Set \(U_v=vv^*-ww^*\), \(D=\operatorname{diag}(r,-r)\). The lower scalar block is

\[
-\{U_v,D\}+[B,[B,D]]=I_2-2D,
\]

\[
[B,[B,D]]=4r\begin{pmatrix}
x_1^2+x_2^2&-z(x_1-ix_2)\\-z(x_1+ix_2)&-(x_1^2+x_2^2)
\end{pmatrix}.
\]

It gives

\[
z(x_1-ix_2)=0,\quad u_{11}-u_{22}=-1/r,
\quad\operatorname{tr}U_v=2+4(x_1^2+x_2^2).
\]

The vector equation gives \(\operatorname{tr}U_v=2+\eta^2\). The scalar residual has zero cross block; its upper entry is determined by the lower trace because both the scalar commutator expression and \(F\) are traceless. Thus no extra scalar entry was omitted.

If \(x_1=x_2=0\), then \(\eta=0\), giving branch I:

\[
H=\operatorname{diag}(0,r,-r),\quad
Z_2=i\operatorname{diag}(0,\sigma,-\sigma),\quad
u_{11}=1-\delta,\quad u_{22}=1+\delta,
\quad\delta=1/(2r)=\sqrt{2/3}.
\]

Both prescribed diagonal differences are strictly positive. This does not assert that \(U_v\) is positive definite: its complex off-diagonal entry remains unrestricted by those scalar equations, and \(U_v\) remains exactly \(vv^*-ww^*\).

If \((x_1,x_2)\ne(0,0)\), then \(z=0\), \(e:=\eta\ne0\), and
\(\gamma=2(x_1-ix_2)/e\) has unit modulus. Choose either square root \(\zeta^2=-\bar\gamma\), which also has unit modulus, and put

\[
W=\frac\zeta{\sqrt2}\begin{pmatrix}\gamma&\gamma\\1&-1\end{pmatrix}.
\]

The columns are orthonormal, \(\det W=-\zeta^2\gamma=1\), and direct multiplication gives

\[
W^*BW=\operatorname{diag}(0,-e),\qquad W^*DW=r\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Conjugation by \(\operatorname{diag}(1,W)^*\) is invertible, fixes \(q\), and yields branch II:

\[
H=\begin{pmatrix}0&0&0\\0&0&r\\0&r&0\end{pmatrix},\quad
Z_2=i\operatorname{diag}(e,0,-e),\quad e\ne0,
\]

\[
\operatorname{tr}U_v=2+e^2,\qquad\operatorname{Re}u_{12}=-\delta.
\]

Indeed the lower scalar equation is
\(-r\{U_v,\sigma_x\}+e^2r\sigma_x=I_2-2r\sigma_x\), and
\(\{U_v,\sigma_x\}=\bigl(\begin{smallmatrix}2\operatorname{Re}u_{12}&\operatorname{tr}U_v\\\operatorname{tr}U_v&2\operatorname{Re}u_{12}\end{smallmatrix}\bigr)\).
This proves necessity and sufficiency of the stated scalar relations in both branches, with all complex phases retained.

## 6. Gauge equations and all exceptional cases in the contradictions

In either branch, write \(Z_2=i\operatorname{diag}(\eta,d_1,d_2)\), \(n_j=\eta-d_j\),

\[
V_j=|v_j|^2,\quad W_j=|w_j|^2,\quad V=V_1+V_2,\quad W_0=W_1+W_2,\quad N=V+W_0,
\]

\[
v^*w=\alpha+ib,\quad b_j=\operatorname{Im}(\bar v_jw_j),\quad
A_j=g^2/4+n_j^2+W_0,\quad P_j=3b+2\omega n_j,\quad B_j=A_j-(\omega^2+N).
\]

Here \(b\) is not the universal pairing \(\beta\). Since \(r^2+q^*q=3/8+1/8=1/2\), one has \(\mathcal IX(v)=X(v)/2\) in either frame. Direct multiplication gives

\[
-[X(w),[X(w),X(v)]]=X\bigl(W_0v+w(\bar p-2p)\bigr),\quad p=v^*w,
\]

\[
[X(v),Z_2]=X(i\operatorname{diag}(n_1,n_2)v).
\]

Consequently (G) and (Y_1) are exactly

\[
A_jv_j=(\alpha+iP_j)w_j,\qquad
B_jw_j=-(\alpha-iP_j)v_j. \tag{C_j}
\]

There are no omitted blocks: those two residuals belong to \(\mathfrak p\). Write \(\mathcal IZ_2=i\operatorname{diag}(\ell_0,\ell_1,\ell_2)\). The full (Y_2) residual belongs to \(\mathfrak k\); its independent entries are

\[
-\omega^2d_j+2n_j(V_j-W_j)+4\omega b_j+(g^2/2)\ell_j=0,\tag{D_j}
\]

\[
-\omega^2\eta-2\sum_j n_j(V_j-W_j)-4\omega b+(g^2/2)\ell_0=0,\tag{D_0}
\]

\[
i(n_1+n_2)(v_1\bar v_2-w_1\bar w_2)+2\omega(-v_1\bar w_2+w_1\bar v_2)=0.\tag{O_{12}}
\]

The remaining lower off-diagonal entry is minus the conjugate. The trace relation among the three diagonal entries is an identity, not a missing equation. The source checker verifies these complete residual formulas symbolically with arbitrary real and imaginary parts of \(v,w\).

Because \(A_j>W_0\ge0\), conjugating the first equation in (C_j), multiplying by \(w_j\), and summing gives

\[
\alpha=\alpha\sum_jW_j/A_j.
\]

If \(W_0=0\), the sum is zero. If \(W_0>0\), the sum is strictly less than 1. Thus \(\alpha=0\), including the zero-spatial-vector case. Pairing the resulting equations gives

\[
A_jV_j=-P_jb_j,\qquad B_jW_j=P_jb_j,
\quad A_j(V_j+W_j)=(\omega^2+N)W_j.
\]

Summation and rearrangement, without discarding any term, yield

\[
\omega^2W_0=(g^2/4)N+\sum_jn_j^2(V_j+W_j),\tag{E}
\]

\[
V_j-W_j=\frac{V_j+W_j}{\omega^2+N}
\left(\omega^2+V-W_0-g^2/2-2n_j^2\right).\tag{U_j}
\]

The denominator \(\omega^2+N\) is strictly positive.

### Branch I

Here \(n_1=-\sigma\), \(n_2=\sigma\), \(\mathcal IZ_2=0\), and \(V_j-W_j=1\mp\delta>0\). The case \(\sigma=0\) is handled before division: (G) paired with \(C\) forces \(C=0\) because \(\mathcal IC=C/2\), contradicting those positive differences.

For \(\sigma\ne0\), both \(v_j\ne0\). The first (C_j) with \(A_j>0\) forces both \(w_j\ne0\) and \(P_j\ne0\). Therefore

\[
w_j=it_jv_j,\qquad t_j=-A_j/P_j\in\mathbb R\setminus\{0\},\qquad A_1=A_2.
\]

Equation (O_12) is \(2i\omega(t_1+t_2)v_1\bar v_2=0\). Each factor other than \(t_1+t_2\) has already been proved nonzero. Hence \(t_1+t_2=0\), which gives \(P_1+P_2=6b=0\). But (D_0) gives

\[
b=\frac{\sigma((1-\delta)-(1+\delta))}{2\omega}
=-\frac{\sigma\delta}{\omega}\ne0.
\]

The contradiction is exact. In particular the sign in the upper diagonal equation is essential and is correct.

### Branch II

Here \(n_1=e\), \(n_2=2e\), \(V-W_0=2+e^2\), and
\(\operatorname{Re}(v_1\bar v_2-w_1\bar w_2)=-\delta\ne0\). Thus both \(V_j+W_j>0\). Direct substitution shows that \((Z_1,Z_2)\mapsto(-Z_1,-Z_2)\) and \((C,\omega)\mapsto(-C,-\omega)\) separately preserve all five equations. They are involutions, preserve the scalar fields, and permit working with \(e>0\), \(\omega>0\). The proof therefore covers both signs without changing either frequency magnitude or the original scalar time scale.

In this frame,

\[
\mathcal IZ_2=ie\operatorname{diag}(1/6,2/3,-5/6).
\]

The adjoint term is \(ie\operatorname{diag}(0,2r^2,-2r^2)\), and the projected vector term is \(ie\operatorname{diag}(1/6,-1/12,-1/12)\); their sum gives the displayed coefficient exactly.

Equation (E) forces \(W_0>0\), since \(N\ge V-W_0=2+e^2>0\). Since \(N=2W_0+2+e^2>2W_0\) and \(n_j^2\ge e^2\), it also gives

\[
\omega^2>g^2/2+2e^2.
\]

Equation (U_1) now yields \(V_1-W_1>0\), because its final factor is
\(\omega^2+2-e^2-g^2/2>2+e^2>0\). Equation (D_1) is

\[
2e(V_1-W_1)+4\omega b_1+eg^2/3=0,
\]

so \(b_1<0\). From (C_1), \(b_1=-P_1W_1/A_1\); hence \(W_1>0\) and \(P_1>0\). Then \(P_2=P_1+2e\omega>0\). Since \(V_2+W_2>0\), (C_2) forces both \(V_2,W_2>0\): either vanishing term would force the other to vanish.

The imaginary part of the same summed Gauss formula is

\[
b\left(1+3\sum_jW_j/A_j\right)=-2\omega\sum_j n_jW_j/A_j<0.
\]

Thus \(b<0\), and \(0<P_j<2\omega n_j\). Define \(\rho_j=A_j/P_j>0\). Since \(A_j>n_j^2\),

\[
\rho_1+\rho_2>\frac{n_1+n_2}{2\omega}=\frac{3e}{2\omega}.\tag{L}
\]

Gauss also gives \(w_j=-i\rho_jv_j\). All of \(v_1,v_2,P_1,P_2,e,\omega\) have now been proved nonzero. Substitution in (O_12) and division by \(iv_1\bar v_2\) are consequently valid and yield

\[
3e(1-\rho_1\rho_2)-2\omega(\rho_1+\rho_2)=0.
\]

As \(\rho_1\rho_2>0\), this gives \(\rho_1+\rho_2<3e/(2\omega)\), contradicting (L). No division by a possibly zero phase or amplitude occurs.

Finally, a constant \(SO(2)\) rotation preserves \(\sum_jZ_j^2\), the double-commutator sums, and \([Z_1,Z_2]\), and commutes with the spatial rotation generator. Therefore the equations transform invertibly by that same rotation. This proves exactly the saturation stated in Section 1.

## 7. Required wording correction, not a mathematical gap

The final TeX sentence saying that the checker “verifies all matrix identities” overstates its literal program coverage. Its first status message also uses “exact inverse coordinate map” more broadly than the tests support.

The checker verifies the original \(H,q,A\) identities and the constant \(U\) diagonalizing map; it does not construct \(K,O(t),\Omega,\Phi_0,b_0\), or symbolically verify the time-dependent inverse gauge transformation. Those identities are proved analytically, including in Section 3 above. Its branch transformation check uses reciprocal symbols for the inverse and the algebraic determinant relation; unit modulus and adjoint equality are established analytically. Its final full-\(\mathfrak{su}(3)\) pairing check is one exact noncommuting test triple, not a symbolic proof over all 24 matrix coordinates. The general pairing and inequality proofs are analytic, as Section 4 and the source TeX state.

A precise replacement for the TeX's last paragraph is:

> The companion checker verifies the displayed constant-frame matrix reductions with arbitrary complex block coordinates, the two branch inertia formulas, and the ratio identity by exact arithmetic. It also checks the universal pairing formulas on an exact full-algebra test triple. The universal proofs, branch inequalities, symmetry arguments, and original time-dependent gauge-map equivalence are established in the text. The checker does not solve the unrestricted finite system.

The existing `CHECK_RESULTS.md` already correctly describes the full-algebra test as a test triple and identifies the analytic proof. No theorem repair is required. No canonical source was edited by this intake.

## 8. Exact next computation without another restricted color ansatz

The natural next calculation is an exact Gauss elimination in the unrestricted finite system, followed by evaluation of all remaining matrix residuals. The following reduction is proved here, not assumed.

For arbitrary \(Z_1,Z_2\in\mathfrak{su}(3)\) and \(g^2>0\), set

\[
\mathscr B=[Z_1,Z_2],\qquad L=g^2\mathcal I+2\mathcal K.
\]

### 8.1. Invertibility on every possible solution

The quadratic-form proof in Section 4 gives

\[
\ker L=\{X:[X,H]=0,\ Xq=0,\ [X,Z_1]=[X,Z_2]=0\}.
\]

Indeed vanishing of the sum of nonnegative terms forces every displayed condition, and those conditions directly give \(LX=0\). Explicitly, the bilinear trace identities are

\[
\langle X,\mathcal IY\rangle
=\operatorname{tr}([X,H][Y,H])+2\operatorname{Re}((Xq)^*Yq),\qquad
\langle X,\mathcal KY\rangle
=\sum_j\langle[Z_j,X],[Z_j,Y]\rangle.
\]

Both right sides are symmetric real bilinear forms in \(X,Y\), proving that \(L\) is self-adjoint.

Because \(H\) has simple eigenvalues \(0,r,-r\) and \(q\) spans its zero eigenline, an anti-Hermitian traceless matrix commuting with \(H\) and annihilating \(q\) is exactly a real multiple of \(iH\). To see this, conjugate by the explicit \(U\) of Section 5. Commutation with the diagonal matrix with three distinct eigenvalues forces every off-diagonal entry to vanish; anti-Hermiticity gives three imaginary diagonal entries, annihilation of \(q\) sets the first to zero, and trace zero makes the remaining two opposite.

Suppose \(\mathscr B\ne0\). If \(\ker L\) contained a nonzero multiple of \(iH\), both \(Z_j\) would commute with \(H\). The same distinct-eigenvalue argument would make both diagonal in its eigenbasis, so they would commute with each other, contrary to \(\mathscr B\ne0\). Thus \(L\) is positive definite and invertible whenever \(\mathscr B\ne0\).

Every possible solution has \(\mathscr B\ne0\), either by the strict \(d>0\) proved in Section 4, or directly: if \(\mathscr B=0\), (G) paired with \(C\) gives \(c=0\), contradicting \(c-z=2\). Hence no solution is lost by this invertibility domain.

Define, for each such pair,

\[
T=4L^{-1}\mathscr B\in\mathfrak{su}(3).
\]

Then (G) is equivalent to \(C=\omega T\). This is an exact inverse of an eight-dimensional real positive-definite operator; it does not impose \(C\in\mathfrak p\), delete a gauge equation, or choose a color frame for the unknowns.

### 8.2. The frequency is also fixed by an exact retained contraction

Pair (S_q) with \(q^*\). Because all connection matrices are anti-Hermitian,

\[
\omega^2\|Tq\|^2=2q^*q+\|Z_1q\|^2+\|Z_2q\|^2
=\tfrac14+\|Z_1q\|^2+\|Z_2q\|^2>0.
\]

Therefore every solution satisfies \(Tq\ne0\). On the explicit domain

\[
\mathcal D=\{(Z_1,Z_2,g^2):Z_j\in\mathfrak{su}(3),\ g^2>0,
\ [Z_1,Z_2]\ne0,\ Tq\ne0\},
\]

define

\[
\tau=\frac{1/4+\|Z_1q\|^2+\|Z_2q\|^2}{\|Tq\|^2}>0.
\]

The constant \(1/4\) is \(2q^*q\) for the original retained vector; no field has been rescaled. The scalar contraction is used only to determine \(\tau\). It does not replace the full vector equation.

### 8.3. Exact reduced zero set and its inverse

Retain all four remaining full matrix/vector residuals:

\[
R_H=\tau[T,[T,H]]-\sum_j[Z_j,[Z_j,H]]-F,
\]

\[
R_q=(\tau T^2-Z_1^2-Z_2^2)q+2q,
\]

\[
R_1=\tau\bigl(-Z_1-2[T,Z_2]+[T,[T,Z_1]]\bigr)
+\mathcal KZ_1+(g^2/2)\mathcal IZ_1,
\]

\[
R_2=\tau\bigl(-Z_2+2[T,Z_1]+[T,[T,Z_2]]\bigr)
+\mathcal KZ_2+(g^2/2)\mathcal IZ_2.
\]

Let \(\mathcal Z\subset\mathcal D\) be their common zero set. There is an exact bijection between \(\mathcal Z\times\{+1,-1\}\) and the solution set of all five finite equations:

\[
(Z_1,Z_2,g^2,\varepsilon)\longmapsto
\bigl(C=\varepsilon\sqrt\tau\,T,\ Z_1,Z_2,
\ \omega=\varepsilon\sqrt\tau,\ g^2\bigr).
\]

Proof: starting from a solution, Sections 8.1–8.2 put its pair in \(\mathcal D\), give \(C=\omega T\), and identify \(\omega^2=\tau\). Substitution in the original scalar and spatial equations gives exactly the four displayed residuals, hence an element of \(\mathcal Z\) and the unique sign \(\varepsilon=\operatorname{sign}\omega\). Conversely, start at a point of \(\mathcal Z\) and either sign. The definition of \(T\) gives
\(LC=\varepsilon\sqrt\tau\,LT=4\omega\mathscr B\), which is (G). Substitution of \(C=\omega T\), \(\omega^2=\tau\) in each of the other four equations gives exactly its vanishing residual. These constructions are inverse. This proves the correspondence with all domains and signs retained.

Thus the next finite search can work with the 16 real coordinates of an unrestricted spatial pair and the positive parameter \(g^2\), rather than guessing a subfamily of \(C,Z_1,Z_2\). It must retain \(\pi_{\mathfrak p}Z_j\) and \(\pi_{\mathfrak k}Z_j\) simultaneously and evaluate every entry of \(R_H,R_q,R_1,R_2\). Each inverse and denominator has a proved domain; clearing denominators without retaining that domain would reintroduce false cases. Any exact zero reconstructs both frequency signs and all original fields by the explicit maps above. No zero or exclusion of this reduced zero set is asserted here.

## 9. Final intake status

The pending TeX supplies a sound, genuinely complex restricted exclusion and correct universal necessary identities. The unrestricted task requested in feedback Section 8 is still open, so this intake is a partial mathematical acceptance, not completion of that task. The next calculation now has a proved unrestricted Gauss-and-frequency elimination, with no additional color ansatz. The only requested source correction is to make checker coverage wording match its actual assertions.
