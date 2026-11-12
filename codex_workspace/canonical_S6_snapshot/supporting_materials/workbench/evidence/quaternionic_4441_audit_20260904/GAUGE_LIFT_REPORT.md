# Homogeneous SU(3) gauge lifts: exact equations, obstruction and constructions

This is a bounded independent audit dated 2026-09-04. No canonical or remote files were edited. The ready-to-input proof fragment is gauge_lift_fragment.tex; the portable exact checker is verify_gauge_lift.py.

## 1. Retained objects and local primary source

The spacetime signature is \(\eta=\operatorname{diag}(1,-1,-1,-1)\). All \(\mathcal A_\mu\) belong to \(\mathfrak{su}(3)\), so they are anti-Hermitian and trace-free. The scalar variables are \(\Phi=\Phi^*\), \(\operatorname{tr}\Phi=0\), and \(b\in\mathbb C^3\). Retain
\[
 s=\operatorname{tr}\Phi^2+2b^*b,\quad a=m^2+\Gamma s,\quad
 V=\frac{m^2}{2}s+\frac{\Gamma}{4}s^2-\kappa(\det\Phi-b^*\Phi b),
\]
where \(m^2\ge0,\Gamma>0,\kappa\in\mathbb R,g^2>0\). The complete density is
\[
 \mathcal L=\frac{\operatorname{tr}(\mathcal F_{\mu\nu}\mathcal F^{\mu\nu})}{2g^2}
 +\frac12\operatorname{tr}(D_\mu\Phi D^\mu\Phi)
 +(D_\mu b)^*D^\mu b-V.
\]
Here \(\mathcal F_{\mu\nu}=\partial_\mu\mathcal A_\nu-\partial_\nu\mathcal A_\mu+[\mathcal A_\mu,\mathcal A_\nu]\), \(D_\mu\Phi=\partial_\mu\Phi+[\mathcal A_\mu,\Phi]\), and \(D_\mu b=\partial_\mu b+\mathcal A_\mu b\). For any square matrix \(Z\), \(Z_{\rm tf}=Z-(\operatorname{tr}Z)I_3/3\).

Homogeneity means all fields depend only on time. These are full field configurations on a finite-volume flat \(\mathbb T^3\), or locally on \(\mathbb R^3\). A nonzero spatially constant density is not assigned finite total energy on all of \(\mathbb R^3\).

Read local primary source: literature_primary/Tong_Gauge_Theory_20260904/gt.txt, lines 2085–2147, corresponding to David Tong, *Lectures on Gauge Theory*, §2.2.1, printed page 40, equations (2.25)–(2.28). The source explains why the \(\mathcal A_0\) equation must still be imposed after temporal gauge. Its Hermitian-generator conventions were not imported into this calculation. The PDF SHA-256 is 4e5a6238aa6578cd4ade5f80c8b74ef2f70f0275483cb6b81ea1c6de859c21a1. The exact canonical potential and orbit were read from research/quaternionic_4441_reconciliation.tex under the consolidated workbench, labels q444:potential, q444:moving-family, q444:moving-data, q444:periodic-instance and q444:charge.

## 2. Every homogeneous Euler–Lagrange equation

Define
\[
 E_i=\dot{\mathcal A}_i+[\mathcal A_0,\mathcal A_i],\quad
 F_{ij}=[\mathcal A_i,\mathcal A_j],\quad
 X=\dot\Phi+[\mathcal A_0,\Phi],\quad v=\dot b+\mathcal A_0b,
\]
\[
 J_0=[\Phi,X]+bv^*-vb^*,\qquad
 J_i=[\Phi,[\mathcal A_i,\Phi]]-bb^*\mathcal A_i-\mathcal A_i bb^*.
\]
The full equations are
\[
 D_0X-\sum_i[\mathcal A_i,[\mathcal A_i,\Phi]]
       +a\Phi-\kappa(\operatorname{adj}\Phi-bb^*)_{\rm tf}=0,
\tag{S-Phi}
\]
\[
 D_0v-\sum_i\mathcal A_i^2b+(aI_3+\kappa\Phi)b=0,
\tag{Sb}
\]
\[
 \frac2{g^2}\sum_i[\mathcal A_i,E_i]-(J_0)_{\rm tf}=0,
\tag{G}
\]
\[
 D_0E_i-\sum_j[\mathcal A_j,[\mathcal A_j,\mathcal A_i]]
       -\frac{g^2}{2}(J_i)_{\rm tf}=0,\qquad i=1,2,3.
\tag{Y}
\]
Here \(D_0E_i=\dot E_i+[\mathcal A_0,E_i]\), and similarly for \(X\); \(D_0v=\dot v+\mathcal A_0v\).

Proof with all coefficients: index raising and antisymmetric-pair counting give
\[
 \mathcal L_{\rm hom}=-\frac1{g^2}\sum_i\operatorname{tr}E_i^2
 +\frac1{g^2}\sum_{i<j}\operatorname{tr}F_{ij}^2
 +\frac12\operatorname{tr}X^2+v^*v
 -\frac12\sum_i\operatorname{tr}[\mathcal A_i,\Phi]^2
 -\sum_i|\mathcal A_i b|^2-V.
\]
The scalar derivative is
\[
 \delta V=\operatorname{tr}\!\left[
 (a\Phi-\kappa(\operatorname{adj}\Phi-bb^*)_{\rm tf})\delta\Phi\right]
 +2\operatorname{Re}\!\left[\delta b^*(aI_3+\kappa\Phi)b\right].
\]
Covariant integration by parts gives \(D_\mu D^\mu\Phi+\nabla_\Phi V=0\) and \(D_\mu D^\mu b+(aI_3+\kappa\Phi)b=0\), hence (S\(\Phi\)) and (Sb).

For the gauge term,
\[
 \delta\mathcal L_{\rm gauge}=\frac2{g^2}
 \operatorname{tr}((D_\mu\delta\mathcal A_\nu)\mathcal F^{\mu\nu}).
\]
Integration by parts gives coefficient \(-2D_\mu\mathcal F^{\mu\nu}/g^2\). The two matter kinetic terms give
\[
 J^\nu=[\Phi,D^\nu\Phi]+b(D^\nu b)^*-(D^\nu b)b^*.
\]
The first follows from trace cyclicity. For the second, anti-Hermiticity gives
\(2\operatorname{Re}(w^*\delta\mathcal A_\nu b)
=\operatorname{tr}((bw^*-wb^*)\delta\mathcal A_\nu)\).
Variation over trace-free anti-Hermitian matrices yields
\[
 D_\mu\mathcal F^{\mu\nu}=\frac{g^2}{2}(J^\nu)_{\rm tf}.
\]
For \(\nu=0\), \(\mathcal F^{i0}=E_i\). For \(\nu=i\), \(\mathcal F^{0i}=-E_i\), \(\mathcal F^{ji}=[\mathcal A_j,\mathcal A_i]\) and \(J^i=-J_i\). These give (G) and (Y). This also proves that fixing \(\mathcal A_0=0\) before variation would omit a necessary equation.

## 3. Exact temporal-gauge obstruction for the literal periodic orbit

Retain \(u=(1,1,1)^{\mathsf T}\), \(v_0=(1,-1,0)^{\mathsf T}\), \(w_0=(1,1,-2)^{\mathsf T}\), and
\[
 K=(v_0/\sqrt2,\ w_0/\sqrt6,\ u/\sqrt3).
\]
This is the specified orthogonal coordinate map, not a replacement kinetic metric. In that frame the canonical moving family has
\[
 H=K^*\Phi_0K=
 \begin{pmatrix}0&0&0\\0&-x&d\\0&d&x\end{pmatrix},\quad
 K^*b_0=Be_1,\quad
 A=K^*\Omega K=
 \begin{pmatrix}0&-\sqrt a&0\\\sqrt a&0&0\\0&0&0\end{pmatrix},
\]
with \(B,d>0,x\ne0,a>0\), \(r^2=x^2+d^2\), \(s=2(r^2+B^2)\), and \(a=m^2+\Gamma s\). The original functions are \(b(t)=O(t)b_0\), \(\Phi(t)=O(t)\Phi_0O(t)^*\), \(\dot O=\Omega O\). The canonical parameter equations \(B^2+d^2=3ax/\kappa-x^2\), \(m^2=a(1-6\Gamma x/\kappa)\) ensure these solve the scalar equations with gauge fields omitted.

Now impose \(\mathcal A_0=0\), but allow every homogeneous spatial \(\mathcal A_i(t)\). Subtract the already-satisfied scalar equations from (S\(\Phi\)), (Sb):
\[
 \sum_i[\mathcal A_i,[\mathcal A_i,\Phi]]=0,\qquad
 \sum_i\mathcal A_i^2b=0.
\]
Pairing with \(\Phi\) and \(b\), respectively, gives
\[
 -\sum_i\operatorname{tr}[\mathcal A_i,\Phi]^2=0,\qquad
 -\sum_i|\mathcal A_i b|^2=0.
\]
Every commutator in the first sum is Hermitian. Thus every summand vanishes:
\[
 [\mathcal A_i,\Phi]=0,\qquad \mathcal A_i b=0.
\]

The simultaneous stabilizer is not assumed trivial. In the retained frame, an element of \(\mathfrak{su}(3)\) killing \(Be_1\) has zero first row and column, with a lower \(\mathfrak{su}(2)\) block. The lower block of \(H\) has distinct eigenvalues \(\pm r\); its anti-Hermitian trace-free commutant is its real multiple times \(i\). Thus
\[
 \mathfrak{stab}(\Phi(t),b(t))=\mathbb R\,i\Phi(t),
 \qquad \mathcal A_i=i c_i(t)\Phi(t),\quad c_i(t)\in\mathbb R.
\]
The full group stabilizer is exactly
\[
 \left\{P_b+\cos\theta(I_3-P_b)+\frac{i\sin\theta}{r}\Phi(t):
 \theta\in\mathbb R\right\},\quad P_b=b(t)b(t)^*/B^2.
\]
It fixes \(b\), has eigenvalues \(1,e^{i\theta},e^{-i\theta}\), and exhausts the unitary commutant with determinant one fixing \(b\) rather than merely its line.

Directly, \(H^2=r^2\operatorname{diag}(0,1,1)\) and \(HAH=0\), so
\[
 [H,[A,H]]=-r^2A,\qquad
 Be_1(ABe_1)^*-(ABe_1)(Be_1)^*=-B^2A.
\]
Returning with \(O(t)K\) proves
\[
 [\Phi,\dot\Phi]=-r^2\Omega,\quad
 b\dot b^*-\dot b b^*=-B^2\Omega,\quad
 J_0=-(r^2+B^2)\Omega.
\]
Moreover \(F_{ij}=0\), \(E_i=i\dot c_i\Phi+i c_i\dot\Phi\), and
\[
 \sum_i[\mathcal A_i,E_i]=r^2\sum_i c_i^2\,\Omega.
\]
Therefore the exact residual of (G) is
\[
 \boxed{\left(\frac{2r^2}{g^2}\sum_i c_i^2+r^2+B^2\right)\Omega\ne0.}
\]
This proves impossibility for every homogeneous spatial connection in temporal gauge retaining these literal scalar functions.

The spatial equations supply a compatible stronger restriction: \(J_i=F_{ij}=0\), so (Y) becomes \(i(\ddot c_i\Phi+2\dot c_i\dot\Phi+c_i\ddot\Phi)=0\). In the retained moving frame, the \((1,1)\) entries of \(H,[A,H],[A,[A,H]]\) are \(0,0,-2ax\). Thus \(c_i=0\) pointwise. The residual then reduces to \((r^2+B^2)\Omega\).

## 4. Arbitrary nonzero \(\mathcal A_0\): what is and is not excluded

Subtracting the same scalar orbit's original equations, with arbitrary \(\mathcal A_0\), gives exactly
\[
 [\dot{\mathcal A}_0,\Phi]+2[\mathcal A_0,\dot\Phi]
 +[\mathcal A_0,[\mathcal A_0,\Phi]]
 -\sum_i[\mathcal A_i,[\mathcal A_i,\Phi]]=0,
\]
\[
 \dot{\mathcal A}_0b+2\mathcal A_0\dot b+\mathcal A_0^2b
 -\sum_i\mathcal A_i^2b=0.
\]
The norm identities now are
\[
 \sum_i\operatorname{tr}[\mathcal A_i,\Phi]^2
 =\operatorname{tr}X^2-\operatorname{tr}\dot\Phi^2,\qquad
 \sum_i|\mathcal A_i b|^2=|v|^2-|\dot b|^2.
\]
For the first, trace pairing kills the \(\dot{\mathcal A}_0\) term, the double commutator contributes \(-\operatorname{tr}[\mathcal A_0,\Phi]^2\), and the mixed term contributes \(-2\operatorname{tr}([\mathcal A_0,\Phi]\dot\Phi)\). For the second use \(\operatorname{Re}(b^*\dot{\mathcal A}_0b)=0\) and anti-Hermiticity. The right-hand sides need not vanish.

An explicit scalar-compatible counterexample to the stabilizer deduction is
\[
 \mathcal A_0=(\alpha-1)\Omega,\qquad
 \mathcal A_i=\beta_i\Omega,\qquad
 \alpha^2-\sum_i\beta_i^2=1.
\]
All coefficients are real constants and all curvatures vanish. Covariant time derivatives multiply the orbit generator by \(\alpha\); spatial derivatives multiply it by \(\beta_i\). Hence both covariant wave operators equal the original second derivative, and both scalar equations hold exactly. The choice \(\alpha=5/3,\beta_1=4/3,\beta_2=\beta_3=0\) gives \(\mathcal A_1b\ne0\). However \(J_0=\alpha J_{\rm sc}\ne0\) and \(E_i=0\), so these flat connections fail Gauss. They are not claimed as full gauge solutions.

There is an exact general equation determining \(\mathcal A_0\) pointwise. Define
\[
 J_{\rm sc}=[\Phi,\dot\Phi]+b\dot b^*-\dot b b^*,
\quad
 \mathscr I Z=([\Phi,[\Phi,Z]]+bb^*Z+Zbb^*)_{\rm tf},
\quad
 \mathscr K Z=-\sum_i[\mathcal A_i,[\mathcal A_i,Z]].
\]
Expansion of (G) gives
\[
 \boxed{(\mathscr I+2\mathscr K/g^2)\mathcal A_0
 =(J_{\rm sc})_{\rm tf}-\frac2{g^2}\sum_i[\mathcal A_i,\dot{\mathcal A}_i].}
\tag{I}
\]
Indeed \(J_0=J_{\rm sc}-\mathscr I\mathcal A_0\), after projection, and the electric commutator sum adds \(\mathscr K\mathcal A_0\).

With \(\langle Z,W\rangle=-\operatorname{tr}(ZW)\) on \(\mathfrak{su}(3)\),
\[
 \langle Z,\mathscr I Z\rangle
 =\operatorname{tr}[Z,\Phi]^2+2|Zb|^2,\qquad
 \langle Z,\mathscr K Z\rangle=\sum_i\|[\mathcal A_i,Z]\|_{\mathfrak{su}}^2.
\]
Cyclicity proves these equalities and the full bilinear identities
\[
 \langle Z,\mathscr I W\rangle
 =\operatorname{tr}([Z,\Phi][W,\Phi])+2\operatorname{Re}((Zb)^*Wb),\quad
 \langle Z,\mathscr K W\rangle
 =\sum_i\langle[\mathcal A_i,Z],[\mathcal A_i,W]\rangle.
\]
The latter are symmetric in \(Z,W\), proving self-adjointness without inferring it merely from quadratic values. The kernel of the left operator in (I) is exactly \([Z,\Phi]=0,Zb=0,[Z,\mathcal A_i]=0\) for all \(i\). Each such \(Z\) annihilates the matter moment because its infinitesimal scalar variation is zero, and annihilates the electric right-hand term because \(\operatorname{tr}(Z[\mathcal A_i,\dot{\mathcal A}_i])=\operatorname{tr}([Z,\mathcal A_i]\dot{\mathcal A}_i)=0\). Therefore the right side is orthogonal to the kernel. A finite-dimensional self-adjoint operator has image equal to that orthogonal complement, so (I) always has a pointwise solution, unique modulo the displayed kernel. This is not a smooth-selection theorem across kernel-rank changes, nor a solution of the other field equations.

One additional complete obstruction follows when every spatial \(\mathcal A_i=0\), even with arbitrary \(\mathcal A_0\). On the orbit \(J_{\rm sc}=-\mathscr I\Omega\), so (I) says \(\mathscr I(\mathcal A_0+\Omega)=0\). Its kernel characterization gives \(D_0\Phi=D_0b=0\). Equation (Sb) would require \(ab=0\), since \(\Phi b=0\), contradicting \(a>0,B>0\). This proves the zero-spatial case for all \(\mathcal A_0\). Neither it nor the temporal-gauge result excludes the general coupled case with nonzero temporal and spatial connections.

## 5. Constructive full homogeneous gauge solutions

Keep \(D=\operatorname{diag}(-2,1,1)\), \(\Phi=x(t)D\), \(b=\beta(t)e_1\), with real \(x,\beta\), and set every \(\mathcal A_\mu=0\). Then every current is exactly zero: \([\Phi,\dot\Phi]=0\), \(b\dot b^*-\dot b b^*=0\), and all spatial currents vanish. Every curvature is zero. Thus all gauge equations hold identically.

The remaining scalar equations are exactly
\[
 \ddot x=-a x-\kappa x^2+\frac{\kappa}{3}\beta^2,\quad
 \ddot\beta=-(a-2\kappa x)\beta,\quad
 a=m^2+\Gamma(6x^2+2\beta^2).
\]
This follows by multiplying the diagonal matrices:
\[
 (\operatorname{adj}(xD)-\beta^2e_1e_1^*)_{\rm tf}
 =(-x^2+\beta^2/3)D.
\]
The conserved energy density is
\[
 \mathcal E=3\dot x^2+\dot\beta^2+V,\quad
 V=\frac{m^2}{2}s+\frac{\Gamma}{4}s^2-2\kappa x(\beta^2-x^2),
 \quad s=6x^2+2\beta^2.
\]
Differentiation with the two real equations proves conservation, retaining the kinetic coefficient \(3\). The estimates \(|x|\le\sqrt{s/6}\), \(\beta^2+x^2\le s/2\) give
\[
 |2x(\beta^2-x^2)|\le s^{3/2}/\sqrt6,\qquad
 V\ge\Gamma s^2/4-|\kappa|s^{3/2}/\sqrt6.
\]
Hence \(V\) is coercive and globally bounded below. Energy bounds positions and velocities; the polynomial first-order vector field is locally Lipschitz and bounded on this compact range, so no finite-time escape occurs. Every real initial datum gives a global full gauge–scalar solution. Finite total energy is asserted on finite-volume \(\mathbb T^3\), not on all of \(\mathbb R^3\).

## 6. Exact equilibrium, fixed-observer variation and gauge averaging

The nonzero branch \(\beta=3x>0\) is an equilibrium precisely when
\[
 24\Gamma x^2-2\kappa x+m^2=0.
\]
For \((\Gamma,m^2,\kappa)=(1,1,6)\), take \(x_0=(3+\sqrt3)/12\). In the retained quaternion convention,
\[
 Q=\Theta(x_0D,3x_0e_1)=
 \begin{pmatrix}-2x_0&0&0\\0&x_0&3x_0\mathbf j\\0&-3x_0\mathbf j&x_0\end{pmatrix}.
\]
Its eigenvalues are \((4x_0,-2x_0,-2x_0)\); the lower block has eigenvalues \(x_0\pm3x_0\). This is a global minimum: for eigenvalues summing to zero,
\[
 s^3-54N^2=2\prod_{i<j}(\lambda_i-\lambda_j)^2\ge0.
\]
At the stated couplings this bounds the potential below by \(r^2/2+r^4/4-2r^3/\sqrt6\), \(r=\sqrt s\), with equality at \((2y,-y,-y)\), \(r=\sqrt6y\), \(y\ge0\). On this family \(V=3y^2+9y^4-12y^3\), whose derivative is \(6y(1-6y+6y^2)\). The larger critical root \(y=(3+\sqrt3)/6=2x_0\) is the unique positive local minimum; its value is negative because the potential at \(y=2/3\) is \(-4/9\). The derivative signs and coercivity therefore prove it is the global minimum.

Retain
\[
 P=\begin{pmatrix}1&-1&0\\0&1&-1\end{pmatrix},\quad
 C=PP^*=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\quad u=(1,1,1)^{\mathsf T}.
\]
The spectral-floor matrix is \(H=Q+2x_0I_3\), positive quaternionic rank one. Its complex part is \(3x_0\operatorname{diag}(0,1,1)\), so
\[
 G=3x_0\begin{pmatrix}1&-1\\-1&2\end{pmatrix},\quad
 \rho=u^*b=3x_0,\quad \det G=9x_0^2=|\rho|^2.
\]
For its \(SU(3)\) orbit write \(e=ge_1\), \(\|e\|=1\). Exact complex congruence under \(\Theta\) gives
\[
 \Phi=x_0(I_3-3ee^*),\quad b=3x_0e,\quad
 G=3x_0P(I_3-ee^*)P^*,\quad
 \det G=9x_0^2|u^*e|^2=|\rho|^2.
\]
Indeed \(P^*C^{-1}P=I_3-uu^*/3\), and the rank-one determinant formula gives
\[
 \det(C-(Pe)(Pe)^*)=3(1-e^*P^*C^{-1}Pe)=|u^*e|^2.
\]
Unit vectors \(e\perp u\) give null observations; \(e=e_1\) gives a timelike observation. They are on the same \(SU(3)\) orbit, since a unit vector can be completed to a unitary basis and a remaining column phase adjusted to determinant one. Thus the fixed-\(P\) determinant is not a gauge-invariant mass. The exact covariance map is \(H'=gHg^*,P'=Pg^*\), for which \(P'H'P'^*=PHP^*\). Likewise \(u'=gu,b'=gb\) preserves \(u^*b\).

A distinct, genuine invariant is obtained by Haar averaging. Retain the Haar mass \(V_\mu>0\), without setting it to one. The signed \(2\times2\) minors of \(P\) give exactly \(u\); Cauchy–Binet therefore proves
\[
 \det(PAP^*)=u^*\operatorname{adj}(A)u
\]
for every complex Hermitian \(A\). Since \(\operatorname{adj}(gAg^*)=g\operatorname{adj}(A)g^*\), Haar averaging its conjugates gives \(V_\mu\operatorname{tr}(\operatorname{adj}A)I_3/3\): diagonal determinant-one phase matrices force the average to be diagonal, cyclic determinant-one permutations make its diagonal entries equal, and the trace fixes their value. Therefore
\[
 \int_{SU(3)}\det(PgAg^*P^*)\,d\mu(g)
 =V_\mu\operatorname{tr}\operatorname{adj}(A).
\]
If \(H=\Theta(A,b)\) is positive quaternionic rank one, then \(\operatorname{adj}(A)=bb^*\). To prove it in the retained signs, write \(r=b^*b\). Direct skew-matrix multiplication gives \(B(b)\overline{B(b)}=bb^*-rI_3\). Hence the complex part of \(H^2\) is \(A^2-bb^*+rI_3\) and \(e_2(H)=e_2(A)-r\). Rank one gives \(H^2=(\operatorname{tr}H)H\), \(e_2(H)=0\); its complex part becomes \(A^2-(\operatorname{tr}A)A+e_2(A)I_3=bb^*\), precisely the adjugate identity. The averaged observation is consequently
\[
 \boxed{V_\mu\|b\|^2.}
\]

Finally let \(\chi=2x_0>0\), \(v_\theta=(\cos\theta,\sin\theta\,\mathbf j,0)^{\mathsf T}\), \(Q_\theta=\chi(3v_\theta v_\theta^*-I_3)\), \(0\le\theta\le\pi/4\). All have spectrum \((2\chi,-\chi,-\chi)\), hence the same minimum energy. The \((1,2)\) entry is \(-3\chi\cos\theta\sin\theta\,\mathbf j\), so the original \(B(b)\) convention gives
\[
 b_\theta=(0,0,-3\chi\cos\theta\sin\theta)^{\mathsf T},\qquad
 \|b_\theta\|^2=\frac{9\chi^2}{4}\sin^2(2\theta).
\]
The norm is strictly increasing on the specified interval and \(SU(3)\) preserves it; thus these are pairwise gauge-inequivalent, equal-energy minima. This explicitly validates the \(9\chi^2/4\) coefficient already supplied by the packet. No identification of its full global orbit parameter \(\delta\) is inferred without that parameter's definition; on this displayed family the corresponding scalar factor is exactly \(\sin^2(2\theta)\).

## 7. Reproducibility and exact scope

Run python verify_gauge_lift.py in any directory with SymPy available. The checker uses no repository paths, files or network. It differentiates the raw homogeneous Lagrangian along all 46 real field-coordinate variations at an exact generic two-jet, separately checks all fourteen potential derivatives with generic symbolic coordinates, and replays the moment, inertia, temporal residual, nonzero-\(\mathcal A_0\) scalar counterexample, radial equations, equilibrium and observation identities.

Final run result: PASS: 89 exact checks, including all 46 real homogeneous field variations. Executed successfully with the existing Miniconda Python and its installed SymPy. The bundled desktop Python lacked SymPy, so no package was installed and that runtime was not used for the successful check. The generic two-jet replay supplements, rather than replaces, the complete symbolic variational proof above. No TeX compilation or new visual recertification is claimed for the uninserted fragment.

The proof fragment provides the requested labels q444:gauge-eom, q444:temporal-no-lift, q444:gauss-inertia, q444:radial-gauge, q444:vacuum-observation, with additional q444:vacuum-average. It is not inserted into the canonical module by this audit.

The established obstruction concerns the literal periodic orbit in temporal gauge, and separately all its zero-spatial lifts. The general nonzero-temporal/nonzero-spatial coupled lift is not excluded. The real radial family and its equilibria are constructive full homogeneous solutions. None of these results proves a continuum quantum mass gap or assigns physical units or measured mass to the determinant.
