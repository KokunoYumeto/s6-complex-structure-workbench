# Paper I: preread derivation of the sigma–theta constant in ari:C.7.1

Scope: only the exact sigma–theta/discriminant normalization and actual differential/lattice scalings. No claim is made here about the already checked extension interpretation or the full lift/branch transport. This derivation is frozen before opening the printed proof of ari:C.7.1 or the analytic agent's comparison/correction.

Exposure: the current proposition statement was extracted alone. I have previously derived the theta product and endpoint norms for C.1.1/C.1.2 and have read the main theorem's definition of N and its displayed pointed coordinate maps. The parent disclosed that another preread had a constant-step slip; its content and correction were not opened.

## 1. Conventions and derivative at the origin

Let the actual period lattice of the chosen differential be
\(\Lambda=\omega_1\mathbb Z+\omega_2\mathbb Z\), with
\(\tau=\omega_2/\omega_1\) and \(T=\Im\tau>0\). Put \(v=u/\omega_1\).
The odd Jacobi theta function has periods1 and tau in its first variable:
\[
\vartheta_1(v,\tau)=2q^{1/8}\sin(\pi v)
\prod_{n\ge1}(1-q^n)(1-2q^n\cos(2\pi v)+q^{2n}),\quad q=e^{2\pi i\tau}.
\]
With \(\eta_D(\tau)=q^{1/24}\prod_{n\ge1}(1-q^n)\), differentiating the convergent product at zero gives the exact identity
\[
\vartheta_1'(0,\tau)=2\pi q^{1/8}\prod_{n\ge1}(1-q^n)^3=2\pi\eta_D(\tau)^3.
\]
The factor is 2pi, with theta's first variable of period1.

Write \(\eta_j=\zeta_\Lambda(z+\omega_j)-\zeta_\Lambda(z)\).
The positively oriented fundamental-parallelogram residue calculation for zeta gives
\(\eta_1\omega_2-\eta_2\omega_1=2\pi i\).
Sigma is fixed by its standard simple zero and \(\sigma_\Lambda'(0)=1\).

## 2. Exact entire-function identity

Define
\[
F(u)=\frac{\omega_1}{2\pi\eta_D(\tau)^3}
\exp\!\left(\frac{\eta_1u^2}{2\omega_1}\right)
\vartheta_1(u/\omega_1,\tau).
\]
It has exactly the simple zeros Lambda and derivative1 at zero. Theta's shifts
\(\vartheta_1(v+1)=-\vartheta_1(v)\) and
\(\vartheta_1(v+\tau)=-e^{-\pi i\tau-2\pi i v}\vartheta_1(v)\), together with the displayed Legendre identity, give
\[
F(u+\omega_j)=-e^{\eta_j(u+\omega_j/2)}F(u),\quad j=1,2.
\]
These are sigma's shifts. Thus sigma/F extends through every lattice zero to a nowhere-zero entire doubly periodic function. It is constant on the compact torus and has limit1 at zero. Consequently
\[
\boxed{\sigma_\Lambda(u)=\frac{\omega_1}{2\pi\eta_D^3}
 e^{\eta_1u^2/(2\omega_1)}\vartheta_1(v,\tau).}
\]
Equivalently, theta divided by eta_D is
\((2\pi/\omega_1)\eta_D^2\sigma_\Lambda(u)e^{-\eta_1u^2/(2\omega_1)}\).
All constants here are fixed by sigma'(0)=1.

## 3. Discriminant scale

For the Weierstrass invariants of the actual lattice,
\[
g_2=\frac{4\pi^4}{3\omega_1^4}E_4(\tau),\qquad
 g_3=\frac{8\pi^6}{27\omega_1^6}E_6(\tau).
\]
The discriminant identity \(E_4^3-E_6^2=1728\eta_D^{24}\), with its constant fixed by the leading q coefficient, yields
\[
\Delta_\Lambda=g_2^3-27g_3^2
=\left(\frac{2\pi}{\omega_1}\right)^{12}\eta_D^{24}.
\]
The exact coefficient check is \((4/3)^3\cdot1728=4096=2^{12}\).
Therefore
\[
|\Delta_\Lambda|^{1/12}=|2\pi/\omega_1|\,|\eta_D|^2.
\]
For a short equation \(y^2=x^3+Ax+B\) and differential \(dx/(2y)\), uniformization is \(x=\wp_\Lambda(u),y=\wp_\Lambda'(u)/2\). Thus \(g_2=-4A,g_3=-4B\), and the algebraic discriminant \(-16(4A^3+27B^2)\) equals \(\Delta_\Lambda\) exactly.
For \(y_0^2=4x_0^3-g_2x_0-g_3\), the differential is \(dx_0/y_0\) and the same lattice/invariant identity holds.

## 4. The real-linear quasiperiod map and the norm

Define the real-linear map eta by
\(\eta(a\omega_1+b\omega_2)=a\eta_1+b\eta_2\), for real a,b.
Since \(b=\Im v/T\), the actual identity is
\[
\eta(u)=\eta_1u/\omega_1-\frac{2\pi i}{\omega_1T}\Im v,
\qquad
\Re(u\eta(u))=\Re(\eta_1u^2/\omega_1)+2\pi(\Im v)^2/T.
\]
Substitution into the given theta norm therefore gives
\[
N(P)=\left|\frac{\vartheta_1(v,\tau)}{\eta_D(\tau)}\right|
 e^{-\pi(\Im v)^2/T}
=|\Delta_\Lambda|^{1/12}|\sigma_\Lambda(u)|
 e^{-\Re(u\eta(u))/2}.
\]
Hence
\[
\boxed{2\log N(P)=\frac16\log|\Delta_\Lambda|
 +2\log|\sigma_\Lambda(u)|-\Re(u\eta(u)).}
\]
For the proposition's \(\Lambda_1=2\log\sigma(u)-u\zeta(u)\), algebraic cancellation gives
\(\Lambda_1+u(\zeta(u)-\eta(u))=2\log\sigma(u)-u\eta(u)\).
Its real part is the displayed expression, giving the exact claimed normalization. This calculation uses only the nonzero point for the logarithm; the proposition's stronger2P≠O hypothesis belongs to its additional extension interpretation and is retained.

## 5. Actual scaling morphisms

For any nonzero complex r, the convergent lattice products give
\[
\sigma_{r\Lambda}(ru)=r\sigma_\Lambda(u),\quad
\zeta_{r\Lambda}(ru)=r^{-1}\zeta_\Lambda(u),\quad
\eta_{r\Lambda}(ru)=r^{-1}\eta_\Lambda(u),\quad
\Delta_{r\Lambda}=r^{-12}\Delta_\Lambda.
\]
Thus the two absolute scale factors cancel and u*eta(u) is unchanged. This proves the invariance under differential/lattice transport; it is not an assertion that different coordinate models are identical.

For the displayed arithmetic model
\(E_M:y^2=x^3-3t^3(t-1)x/4+t^4(t-1)^2/4\), take omega_M=dx/(2y). Its g2 and g3 are \(3t^3(t-1)\) and \(-t^4(t-1)^2\), and
\(\Delta_M=27t^8(t-1)^3\).

The pointed map from this model to Engel's short equation is
\((x,y)\mapsto(x_E,y_E)=(2x,-2\sqrt2y)\).
It pulls back \(dx_E/(2y_E)\) to \(-\omega_M/\sqrt2\).
Thus r=-1/sqrt2, Lambda_E=r Lambda_M, u_E=r u_M, and Delta_E=64Delta_M. The factor64^(1/12)=sqrt2 cancels |r| exactly.

The AC model is
\(y_0^2=4x_0^3-3t^3(t-1)x_0-t^4(t-1)^2\), with omega_0=dx_0/y_0.
The displayed pointed map \((x_0,y_0)\mapsto(x,y)=(-x_0,y_0/(2i))\) pulls back omega_M to -i omega_0.
Thus r=-i, Lambda_M=-i Lambda_0 and Delta_M=(-i)^(-12)Delta_0=Delta_0. The sigma absolute scale is1 and u*eta(u) is unchanged. In particular the explicit factor2 in y0/(2i) is accounted for by using dx/(2y), not dx/y, on the short equation.

## 6. Scope conclusion before comparison

The proposition's normalization follows exactly with discriminant coefficient1/6 in 2logN, sigma'(0)=1, and the actual differential/lattice morphisms above. I have not yet opened its printed proof. This frozen derivation does not claim to recheck the extension-class/relative-period portion or the full lattice-translation clause.
