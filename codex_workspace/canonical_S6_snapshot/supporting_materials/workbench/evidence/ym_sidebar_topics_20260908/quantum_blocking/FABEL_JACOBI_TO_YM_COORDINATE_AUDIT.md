# Fabel/Jacobi coordinate audit and Yang–Mills transfer boundary

This file keeps the original coordinates and coefficients. It separates exact identities from the additional map that would be needed for a Navier–Stokes or Yang–Mills counterexample.

## 1. The polynomial map and its typed certificate

Let
\[
F=(F_1,F_2,F_3):\mathbb C^3_{(x,y,t)}\to\mathbb C^3_{(a,b,c)},
\]
\[
\begin{aligned}
F_1&=(1+xy)^3t+y^2(1+xy)(4+3xy),\\
F_2&=y+3x(1+xy)^2t+3xy^2(4+3xy),\\
F_3&=2x-3x^2y-x^3t.
\end{aligned}
\]
Direct polynomial differentiation gives the typed differential
\(DF_p:T_p\mathbb C^3\to T_{F(p)}\mathbb C^3\) and
\[
\det DF_p=-2\qquad(p\in\mathbb C^3).
\]
Thus every differential is invertible. This is local coordinate nondegeneracy; it does not imply global injectivity.

The three distinct source points
\[
p_1=(0,0,-1/4),\quad p_2=(1,-3/2,13/2),\quad p_3=(-1,3/2,13/2)
\]
satisfy, by substitution,
\[
F(p_1)=F(p_2)=F(p_3)=q=(-1/4,0,0).
\]
The exact fibre has at least three points. The value \(-1/4\) is the first target coordinate \(a(q)\); it is not an eigenvalue, a mass, an energy, or a time coordinate by this certificate alone.

## 2. Exact comparison with the retained Navier–Stokes orbit

The inherited root chart uses the original spatial third coordinate under the name \(w\), while \(\tau\) is evolution time. On the \(b=c=0\) sheet,
\[
P_{a,b,c}(r)=cr^3-2r^2+br-2a,\qquad \alpha=P_r(r)/2,
\]
\[
(x,y,w)=(\alpha^{-1},r-\alpha,5\alpha^2-3r\alpha-c\alpha^3),\qquad \alpha\ne0.
\]
At \(b=c=0\), \(a=-r^2\). With the retained notation \(a=2s\), one has the exact scalar relation
\[
s=-r^2/2.
\]
Therefore \(s=-1/4\) occurs at \(r^2=1/2\). This is a root-sheet coordinate value, not a singularity statement.

The separately retained material trajectory is
\[
z=\sqrt{1-8\tau}>0,\qquad \tau=(1-z^2)/8,
\]
\[
\gamma(\tau)=(z^{-1},-3z/2,13z^2/2),\qquad F(\gamma(\tau))=(-1/4+2\tau,0,0).
\]
Hence
\[
a(0)=-1/4,\qquad a(1/8)=0.
\]
The collision image \(a=-1/4\) is reached by this orbit at the initial time \(\tau=0\), whereas the escaping endpoint is \(\tau\uparrow1/8\) and has target first coordinate \(a\uparrow0\). These are exact different events. Identifying them would change the coordinate map.

## 3. The exact transported direction

At \(q_0=(1,-3/2,13/2)\), write \(J_0=DF(q_0)\), and along \(\gamma\) write \(J_\gamma=DF(\gamma(\tau))\). The target shear is
\[
B_\tau=I+6\tau E_{23}=\begin{pmatrix}1&0&0\\0&1&6\tau\\0&0&1\end{pmatrix}.
\]
The coordinate-level material map and its inverse are
\[
A_\tau=J_\gamma^{-1}B_\tau J_0:T_{q_0}\mathbb R^3\to T_{\gamma(\tau)}\mathbb R^3,
\quad
C_\tau=J_0^{-1}B_\tau^{-1}J_\gamma=A_\tau^{-1}.
\]
All entries are the rational functions displayed in `material_generator_endpoint.md`; the factored products prove \(C_\tau A_\tau=A_\tau C_\tau=I\), \(\det A_\tau=1\), and \(A_0=I\). The full variational equation is
\[
\frac{dA_\tau}{d\tau}=DU(\gamma(\tau))A_\tau.
\]

For the initial covector \(e_3\), the exact dual map is
\[
\zeta_\tau=A_\tau^{-\mathsf T}e_3=C_\tau^{\mathsf T}e_3,
\qquad |\zeta_\tau|\sim\frac94 z^{-3}=\frac94(1-8\tau)^{-3/2}.
\]
The diffusion tensor \(K_\tau=C_\tau C_\tau^{\mathsf T}\) obeys
\[
\det K_\tau=1,\quad \lambda_1\sim(64/121)z^6,\quad
\lambda_2\to121/337,\quad \lambda_3\sim(337/64)z^{-6}.
\]
Thus a dual material direction blows up and a primal direction collapses, while every finite \(\tau<1/8\) remains strictly positive definite. This proves endpoint loss of uniform ellipticity, not a finite-time singularity of \(u\), \(\nabla u\), or curvature.

## 4. Exact gauge encoding and the missing transfer morphism

For a real velocity field \(u=(u_1,u_2,u_3)\) and fixed nonzero \(T\in\mathfrak{su}(2)\), define on a spatial slice
\[
\mathcal A_i=\lambda u_iT,
\qquad
\mathcal F_{ij}=\partial_i\mathcal A_j-\partial_j\mathcal A_i+[\mathcal A_i,\mathcal A_j]
 =\lambda(\partial_i u_j-\partial_j u_i)T.
\]
The commutator vanishes because all components lie in the one-dimensional span of \(T\). With \(-2\operatorname{tr}(T^2)=1\),
\[
-2\sum_{i<j}\operatorname{tr}(\mathcal F_{ij}^2)
 =\lambda^2|\nabla\times u|^2.
\]
The map from a proven fluid profile to this connection is therefore typed and gauge invariant. If one proves, for the same transported direction, that \(|\nabla\times u(\gamma(\tau),\tau)|\to\infty\), then this displayed invariant curvature norm diverges. The exact divergence of \(|\zeta_\tau|\) alone does not prove that implication: \(\zeta_\tau\) is a material covector, not the velocity or vorticity.

On the quantum lattice, the physical state space is \(L^2(\mathrm{SU}(2)^E,\psi^2\lambda)\) after gauge projection. A complex Fabel tangent vector has no map into this real gauge-invariant Hilbert space until one specifies (i) a real lattice observable, (ii) its edge variables and gauge action, (iii) the state \(\Psi\) and operator domain, and (iv) the exact continuum/volume limit. For every invariant \(\Psi\), the projector satisfies \(P_{\mathcal G}(O\Psi)=O\Psi\), but this identity does not create the missing Fabel-to-state map.

The raw mass-gap counterexample required by the project is a sequence of physical states with \(\|\Psi_n\|>0\) and
\[
\frac{\langle\Psi_n,H_{\mathrm{YM}}\Psi_n\rangle}{\langle\Psi_n,\Psi_n\rangle}\longrightarrow0.
\]
No division by a coordinate norm, no sign of a target coordinate, and no anisotropic Jacobian limit supplies this sequence. CPT pairing or a negative-mass interpretation likewise requires an explicitly constructed state and Hamiltonian symmetry; it is not a consequence of \(a=-1/4\).

## 5. Propagation result

The exact Fabel certificate propagates to the Navier–Stokes material calculation through the typed maps \(DF\), \(A_\tau\), and \(A_\tau^{-\mathsf T}\), and it identifies a sharply anisotropic direction. It does **not** identify the collision target with the heat endpoint, and it does **not** yet produce a Yang–Mills physical state or a vanishing raw Rayleigh quotient. The next mathematically decisive object is an explicit real, gauge-invariant state map whose curvature and energy are computed before any quotient or limiting claim.
