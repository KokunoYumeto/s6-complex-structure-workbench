# Original finite-angle native states at weak coupling

This proof retains the original unmodified cusp angle at each spatial regulator. It first proves a fixed-box theorem for every fixed nontrivial angle. The subsequent simultaneous sequence retains the original depth \(T_j=j^2\), periods, metric, cover and native state. Its strictly positive couplings are selected from proved limits; they are not identified with either prescribed coupling trajectory.

## 1. Exact operator, gauge space and translated faces

Fix \(L\ge2\), \(a>0\), and all positive edges and elementary faces of the original open box \(\{-L,\ldots,L\}^3\). Write
\[
 N_E=3(2L)(2L+1)^2,\quad M=12L^2(2L+1),\quad
 W(U)=\sum_p(2-\operatorname{tr}U_p),
\]
\[
 H_g=\frac{2g^2}{a}H_0+\frac{W}{2g^2a},\quad
 H_0=\sum_eE_e,\quad E_e=-\sum_{\alpha=1}^3X_{e,\alpha}^2,
 \quad T_\alpha=-i\sigma_\alpha/2 .
 \tag{N1}
\]
The full potential includes every original face and its scalar \(2bM\). All spectral projections below are on the physical subspace fixed by every original vertex gauge transformation. The operator and form domains are the intersections of that subspace with the product Sobolev spaces \(H^2,H^1\). Its actual positive unit vacuum is \(\psi_g\), with energy \(E_g\), and \(A_g=H_g-E_g\). The previously proved variational estimate gives
\[
 0\le E_g\le K:=\frac{3\sqrt{N_EM}}a,\qquad
 \|H_0^{1/2}\psi_g\|^2\le\frac{aK}{2g^2}.
 \tag{N2}
\]
The second inequality follows directly from (N1), since \(W\ge0\).

The native links are \(h_1(n)=\exp(-\theta n_2H_c)\), \(h_2=h_3=I\), \(H_c=-2T_3=i\sigma_3\). Since \(n_2\) is integral, their period in \(\theta\) is exactly \(2\pi\). Choose a representative with \(0<|\theta|\le\pi\). For every edge \(e=(n,1)\) with \(n_2\ne0\), let \(q_e\in SU(2)\) be independent with Haar probability. Put \(h_e^q=q_eh_eq_e^{-1}\); identity edges remain identity. There are
\[
 m=4L^2(2L+1)
 \tag{N3}
\]
such edges. The exact physical average established earlier is the positive-kernel self-adjoint contraction
\[
 K_\theta F(U)=\int F(((h_e^q)^{-1}U_e)_e)\,dq,\qquad
 \chi_{\theta,g}=K_\theta\psi_g-c_{\theta,g}\psi_g,\quad
 c_{\theta,g}=\langle\psi_g,K_\theta\psi_g\rangle>0.
 \tag{N4}
\]
Each direction-one translated edge has a different source vertex, which is why the source gauge averages give precisely these independent conjugacy averages. Their central convolution factors commute with every edge Casimir and with the full gauge action. Each vector in (N4) is therefore smooth and physical, and \(\chi_{\theta,g}\perp\psi_g\).

For a fixed realization \(q\), write \(V_e=(h_e^q)^{-1}U_e\). Consider a \(12\) face with \(n_2=0\). Its bottom direction-one link is unchanged, and only its top direction-one link is translated. In the original positive face word,
\[
 V_p=U_p\bigl(U_2(n)h_{(n+e_2,1)}^qU_2(n)^{-1}\bigr).
 \tag{N5}
\]
For a \(12\) face with \(n_2=-1\), only its bottom direction-one link is translated, and instead
\[
 V_p=(h_{(n,1)}^q)^{-1}U_p .
 \tag{N6}
\]
The extra factor in either formula has eigenvalues \(e^{i\theta},e^{-i\theta}\), possibly interchanged. If \(B\) is such a factor and \(S\in SU(2)\), write \(B=B_{1/2}^2\) with eigenvalues of \(B_{1/2}\) equal to \(e^{\pm i\theta/2}\). Then
\[
 I+B=2\cos(\theta/2)B_{1/2},\qquad
 \operatorname{tr}S+\operatorname{tr}(SB)
       =2\cos(\theta/2)\operatorname{tr}(SB_{1/2})
       \le4\cos(\theta/2).
 \tag{N7}
\]
Here \(\cos(\theta/2)\ge0\), and every \(SU(2)\) trace is at most two. Cyclicity handles the left factor in (N6). There are exactly \(2L(2L+1)\) faces in each selected plane. Summing their nonnegative defects, and retaining all other faces in \(W\), proves the global nonlinear separation
\[
 \boxed{W(U)+W(((h_e^q)^{-1}U_e)_e)
    \ge\Delta_{L,\theta}:=
       16L(2L+1)(1-\cos(\theta/2))>0.}
 \tag{N8}
\]
It holds for every configuration and every twirl realization, not just near a flat configuration.

Let \(\delta=\Delta_{L,\theta}/3\) and \(Q=\mathbf1_{\{W\le\delta\}}\), as a bounded multiplication projection. It preserves the physical subspace because \(W\) is gauge invariant. Equation (N8) implies the exact support identity
\[
 QK_\theta Q=0.
 \tag{N9}
\]
Indeed two arguments with potential at most \(\delta\) would have sum at most \(2\Delta/3\), contradicting (N8). In particular \(K_\theta Q\) has support in \(W\ge2\delta\).

## 2. All potential moments on the actual finite-energy space

For a unit eigenfunction \(u_g\) of the full physical \(H_g\), with eigenvalue \(\lambda_g\le E_*\), set \(I_n=\int W^n|u_g|^2dU\). The original derivative estimate is \(\sum_{e,\alpha}|X_{e,\alpha}W|^2\le16W\). Haar integration by parts gives
\[
 \operatorname{Re}\langle W^nu_g,H_0u_g\rangle
 =\sum_{e,\alpha}\|X_{e,\alpha}(W^{n/2}u_g)\|^2
       -\frac{n^2}{4}\int W^{n-2}
                  \sum_{e,\alpha}|X_{e,\alpha}W|^2|u_g|^2
 \ge-4n^2I_{n-1}.
 \tag{N10}
\]
The identity is valid for complex eigenfunctions. At zeros of \(W\), apply it first with \(W+\varepsilon\). Its derivative obeys the same bound by \(16(W+\varepsilon)\); dominated convergence and the form norm give (N10). This also supplies the domain justification for odd \(n\).

Using (N1), \(I_0=1\), and nonnegativity of the kinetic energy for \(I_1\), we obtain
\[
 I_n\le B_n(E_*)g^{2n},\qquad
 B_0=1,\quad B_1=2aE_*,\quad
 B_{n+1}=2aE_*B_n+16n^2B_{n-1}\quad(n\ge1).
 \tag{N11}
\]
Every constant is fixed before \(g\to0\). For the vacuum, take \(E_*=K\).

Fix \(\Omega>0\), and let \(P_g=\mathbf1_{(0,\Omega]}(A_g)\) on the physical subspace. Its rank is bounded by an integer \(R\) for all sufficiently small positive \(g\). Here is precisely the fixed-box input: Section 17 proves convergence of each ordered physical eigenvalue of \(H_g\) to the corresponding eigenvalue of its compact-resolvent oscillator on the adjoint-invariant chord space. Choose a comparison eigenvalue strictly greater than \(K+\Omega+1\). Its actual eigenvalue is greater than \(K+\Omega\) for all sufficiently small \(g\). Equation (N2) then bounds the number of physical eigenvalues below \(E_g+\Omega\) by this fixed index. This argument is not a claim about the rank on the full nongauge-invariant configuration Hilbert space.

Choose a physical orthonormal eigenbasis of \(\operatorname{ran}P_g\) and apply (N11) with \(E_*=K+\Omega\). The squared Hilbert--Schmidt bound obtained by summing its at most \(R\) columns yields
\[
 \|(I-Q)P_g\|
 \le\sqrt{R B_n(K+\Omega)}\,\delta^{-n/2}g^n,\qquad
 \|(I-Q)\psi_g\|\le\sqrt{B_n(K)}\,\delta^{-n/2}g^n.
 \tag{N12}
\]
These hold for every integer \(n\ge1\), after possibly reducing the fixed-box positive coupling threshold for the rank assertion.

The support identity (N9), contraction of \(K_\theta\), and adjoints in (N12) give
\[
 \|P_gK_\theta\psi_g\|
 \le\left[\sqrt{R B_n(K+\Omega)}+\sqrt{B_n(K)}\right]
                  \delta^{-n/2}g^n .
 \tag{N13}
\]
To see the decomposition explicitly, write the input as \(Q\psi+(I-Q)\psi\); the first image equals \((I-Q)K_\theta Q\psi\), and the second has norm at most \(\|(I-Q)\psi\|\). Since \(P_g\psi=0\), the left side equals \(\|P_g\chi_{\theta,g}\|\). Also, by splitting the first argument and then the second in the scalar overlap and using (N9),
\[
 0<c_{\theta,g}\le2\|(I-Q)\psi_g\|
       \le2\sqrt{B_n(K)}\,\delta^{-n/2}g^n .
 \tag{N14}
\]
Thus the raw low-energy vector and the uncentered vacuum overlap decrease faster than every power of \(g\), at each fixed box, angle and energy cutoff.

## 3. A polynomial lower bound for the unchanged raw norm

A relative spectral conclusion requires a lower bound for the same native state. Positivity of the actual vacuum provides it without replacing that vacuum by a trial function. Let \(T_hF(U)=F((h_e^{-1}U_e)_e)\), so \(\|T_h\psi_g\|=1\). Put
\[
 \eta=\frac1{2(1+\sqrt{2maK})},\qquad
 b_*=\frac{\eta^3}{3\pi^3},\qquad c_*=\frac12 b_*^m .
 \tag{N15}
\]
Restrict \(0<g\le1\). For each twirl variable restrict \(q_e=\exp(Y_e)\), where \(|Y_e|\le\eta g\) in the metric making \(T_\alpha\) orthonormal. The curve \(q_e(t)=\exp(tY_e)\) conjugates \(h_e\). Its left or right logarithmic velocity has norm at most \(2|Y_e|\), because it is a difference of two orthogonal adjoint images. Differentiating the product translation along this curve and applying Cauchy--Schwarz in its edge and Lie indices gives
\[
 \|T_{h^q}\psi_g-T_h\psi_g\|
 \le2\eta g\sqrt m\,\|H_0^{1/2}\psi_g\|
 \le\eta\sqrt{2maK}\le\frac12 .
 \tag{N16}
\]
Every product left translation preserves the full electric form, since each edge Laplacian is bi-invariant. This proves the uniform gradient bound along the entire curve used in (N16).

Both translated vacua are positive real unit vectors. Their inner product equals one minus half the squared distance, so it is at least \(7/8\) in this neighborhood. At all other twirl parameters their inner product remains nonnegative. The exact Haar density in exponential coordinates is
\[
 \frac1{16\pi^2}
       \left(\frac{\sin(|Y|/2)}{|Y|/2}\right)^2d^3Y.
 \tag{N17}
\]
For \(r\le1\), the inequality \(\sin u/u\ge2/\pi\) on \(0\le u\le\pi/2\) and the Euclidean ball volume give Haar measure at least \(r^3/(3\pi^3)\). Thus the product neighborhood in (N16) has probability at least \(b_*^m g^{3m}\). Integrating only its positive contributions and using Cauchy--Schwarz with the unit test vector \(T_h\psi_g\) proves
\[
 \boxed{\|K_\theta\psi_g\|
 \ge \langle T_h\psi_g,K_\theta\psi_g\rangle
 \ge c_*g^{3m}.}
 \tag{N18}
\]
The factor \(1/2\) in \(c_*\) is smaller than the proved \(7/8\); it provides a uniform displayed lower bound.

Choose an integer \(n>3m\) in (N14). For all sufficiently small positive \(g\), that overlap is at most \(c_*g^{3m}/2\). Orthogonal centering gives the exact equality
\[
 d_{\theta,g}:=\|\chi_{\theta,g}\|^2
       =\|K_\theta\psi_g\|^2-c_{\theta,g}^2
       \ge\frac34c_*^2g^{6m}>0.
 \tag{N19}
\]
In particular, every raw low-energy mass from (N13) is being compared with the actual nonzero norm, not an assumed unit excitation.

Combining (N13) and (N19), for each fixed real \(p>0\) choose an integer \(n\) with \(2n-6m\ge p\). The full physical native probability obeys
\[
 \boxed{
 \frac{\langle\chi_{\theta,g},
      \mathbf1_{(0,\Omega]}(A_g)\chi_{\theta,g}\rangle}
      {d_{\theta,g}}
       =O_{L,a,\theta,\Omega,p}(g^p),\qquad g\downarrow0 .}
 \tag{N20}
\]
The raw numerator bound, with its explicit constants, remains (N13) squared, and the raw denominator lower bound remains (N19). No statement uniform in the growing box is hidden in (N20).

## 4. The unfiltered raw mass and the central endpoint

For \(0<|\theta|<\pi\), the raw norm also tends to zero. We prove a rate that suffices for later simultaneous selection. Choose the original edge \(e=((0,1,0),1)\). Its central factor in \(K_\theta\) is \(C_{e,\theta}\), with exact spin-\(s\) multiplier
\[
 c_s(\theta)=\frac{\sin((2s+1)\theta)}
                    {(2s+1)\sin\theta},\qquad
 |c_s(\theta)|\le\frac1{(2s+1)|\sin\theta|}.
 \tag{N21}
\]
This is used only when \(\sin\theta\ne0\). All other central factors commute with it and are contractions.

Let \(P_d^e\) be the projection onto edge spins with \(2s+1\le d\), \(d\) a positive integer. Its one-edge projection kernel has constant diagonal
\(D_d=\sum_{r=1}^dr^2=d(d+1)(2d+1)/6\le d^3\).
For fixed other links, the original face \(p=((0,0,0),12)\) has word \(U_p=A B U_e^{-1}D_0^{-1}\), where \(A=U_1(0,0,0)\), \(B=U_2(1,0,0)\), and \(D_0=U_2(0,0,0)\) are fixed by the exterior. Cyclicity gives \(\operatorname{tr}U_p=\operatorname{tr}(D_0^{-1}ABU_e^{-1})\). Haar invariance and inversion therefore make the volume of its defect cap independent of the exterior. If \(W\le u\), its face defect is at most \(u\). The Haar class angle \(\phi\in[0,\pi]\) has density \(2\sin^2\phi/\pi\), so the exact defect \(w=2-2\cos\phi\) has density
\[
 \frac1\pi\sqrt{w-w^2/4}\,dw,\qquad 0\le w\le4 .
\]
Consequently the allowed subset of \(U_e\) has Haar measure at most
\[
 C_{\rm cap}u^{3/2},\qquad C_{\rm cap}=\frac2{3\pi},
                         \quad u>0.
 \tag{N22}
\]
Indeed integrate the displayed density over \(0\le w\le\min(u,4)\), bound \(\sqrt{w-w^2/4}\le\sqrt w\), and enlarge the upper integration limit to \(u\). This proves the estimate also when \(u>4\).

For any such fiber subset \(B\), the Hilbert--Schmidt norm squared of \(P_d^e\mathbf1_B\) is \(\int_BD_d\,dU_e\). Apply this bound fiberwise to \(\mathbf1_{\{W\le u\}}\psi_g\), and apply (N11) to its complementary part. The triangle inequality squared gives the full edge-spin cumulative probability
\[
 F_g(d):=\|P_d^e\psi_g\|^2
       \le2C_{\rm cap}d^3u^{3/2}
                  +2B_n(K)g^{2n}u^{-n}.
 \tag{N23}
\]
The fiberwise argument uses the full original Haar space; its input is the actual physical vacuum. It requires no factorization of the vacuum measure.

Use \(n=4\), and choose \(u_d=g^2(dg)^{-6/11}>0\) separately for each spin cutoff. This cutoff is used only in (N23), which is valid for every positive \(u\); it does not change the fixed separation cutoff in (N9). Substitution gives
\[
 F_g(d)\le A_4(dg)^{24/11},\qquad
 A_4=\frac4{3\pi}+2B_4(K).
\]
The recurrence (N11), with \(x=2aK\), gives exactly \(B_2=x^2+16\), \(B_3=x^3+80x\), and \(B_4=x^4+224x^2+2304\). If \(\mathsf d=2s_e+1\) denotes the positive integer edge-spin dimension in the actual squared coefficient distribution, Tonelli's theorem gives the exact identity
\[
 \mathbb E_{\psi_g}\mathsf d^{-2}
 =\int_1^\infty2t^{-3}F_g(\lfloor t\rfloor)\,dt .
 \tag{N24}
\]
For each integer \(d\), the contribution of its probability mass is \(\int_d^\infty2t^{-3}\,dt=d^{-2}\), proving the identity before summing. For \(0<g\le1\), split at \(g^{-1}\). On the first part use the displayed cumulative bound and \(\lfloor t\rfloor\le t\), and on the second use \(F_g\le1\). This gives
\[
 \mathbb E_{\psi_g}\mathsf d^{-2}
 \le2A_4g^{24/11}\int_1^{g^{-1}}t^{24/11-3}\,dt+g^2
 =11A_4(g^2-g^{24/11})+g^2.
\]
Parseval and (N21), with the commuting contraction factors retained, therefore prove
\[
 d_{\theta,g}\le\|K_\theta\psi_g\|^2
 \le\frac{1+44/(3\pi)+22B_4(K)}{\sin^2\theta}\,g^2,
 \qquad 0<g\le1.
 \tag{N25}
\]
For every sufficiently small positive \(g\), (N19) supplies the simultaneous strictly positive lower bound for this same raw norm. The angle-dependent constant and every original norm remain explicit.

At \(\theta=\pi\), every direction-one link is central, \(h_1(n)=(-1)^{n_2}I\). Then \(K_\pi=T_h\) is a unitary involution. Equations (N14) and (N19) are still valid, but now
\[
 d_{\pi,g}=1-c_{\pi,g}^2\longrightarrow1 .
 \tag{N26}
\]
The complete low-energy probability still satisfies (N20). At \(\theta=0\) modulo \(2\pi\), \(K_\theta=I\) and the centered state is exactly zero. These branches preserve the discrete center endpoint and the original continuous path; they do not identify the initial cusp exhaustion with its endpoint.

## 5. Original geometry on one common actual sequence

Let \(j\) range over an eventual dyadic tail \(j=2^s\), on which the original cusp domain is defined and \(0<\theta_j<\pi\). Retain exactly
\[
 T_j=j^2,\quad L_j=j^2,\quad a_j=\frac1{100j},\quad
 D_j=L_{j^2}q_{j^2}+6m_{j^2}^2,\quad
 \theta_j=\frac{2\pi}{10^4j^2D_j},
 \quad v_j=e^{-2\pi j},\quad t_{c,j}=v_j^j .
 \tag{N27}
\]
The original period entries, \(B_T\), coordinate permutation, cover \(j\), pullback metric and signed determinant \(-j^2D_j\) remain those of Section 2. Its proved estimate \(D_j=j^4+O(j^2)\) is used only after the exact angle in (N27); in particular \(\theta_j\sim(2\pi/10^4)j^{-6}\), and \(0<\theta_j<\pi\) on an eventual tail.

For a fixed \(j\), (N20),(N25) are actual \(g\downarrow0\) results at that box and its original angle. Set
\[
 R_j=\frac{4\sqrt3}{a_j}+1.
 \tag{N28}
\]
The comparison covariance measure (228) has pair energies at most \(4\sqrt3/a_j\), because every \(\sigma_\nu\le\sqrt{12}\). The fixed-box convergence (231) therefore implies that the actual covariance probability of \((R_j,\infty)\) tends to zero.

Keep all finite-stage tests defining Section 25's actual coupling selection, including Sections 18 and 22--24 and the retained full local-energy tests. Add
\[
 \begin{split}
 &\zeta_{\theta_j,g}([0,R_j])<a_j^5/j,\qquad
    \tfrac34c_{*,j}^2g^{6m_j}\le d_{\theta_j,g}<j^{-2},\\
 &\zeta_{\Gamma,L_j,a_j,g}((R_j,\infty))<j^{-2},
                       \qquad 0<g<j^{-5}.
 \end{split}\tag{N29}
\]
Here \(\zeta_{\theta,g}\) denotes precisely the probability in (N20); it has no vacuum atom. Here \(m_j=4L_j^2(2L_j+1)\) and \(c_{*,j}\) is exactly (N15) at \(L_j,a_j\); it does not depend on \(g\). The first two new inequalities hold throughout a sufficiently small positive interval by (N19),(N20),(N25). The third holds by the fixed-box covariance convergence and its stated comparison support. Every previous stage test also holds on a sufficiently small interval by its proved fixed-box limit. Their finite intersection is nonempty. Define \(k_j\) as the least positive integer such that all dyadics \(2^{-q}\), \(q\ge k_j\), meet this list, and set \(g_j=2^{-k_j}\). This gives a single exact actual sequence, retaining all original physical coefficients
\[
 \kappa_j=200j\,2^{-2k_j},\quad
 b_j=50j\,2^{2k_j},\quad
 \xi_j=2^{4k_j-2},\quad
 2b_jM_j=100j\,2^{2k_j}M_j.
 \tag{N30}
\]
There is no claimed numerical uniform-volume rate for the least exponent.

Write \(\chi_j=\chi_{\theta_j,g_j}\), retaining the original, unchanged depth (N27). The same physical Hamiltonians have closing gaps by the retained Section 18 tests. Meanwhile, for each fixed \(\Omega>0\),
\[
 \begin{split}
 &0<\|\chi_j\|^2<j^{-2},\qquad
   \zeta_{\theta_j,g_j}([0,\Omega])\le a_j^5/j
                                     =o(a_j^5),\\
 &\zeta_{\Gamma,L_j,a_j,g_j}([0,\Omega])
       \sim a_j^5\frac{\Omega^5}{600\pi^2I_{\rm lat}},\\
 &\frac{\zeta_{\theta_j,g_j}([0,\Omega])}
           {\zeta_{\Gamma,L_j,a_j,g_j}([0,\Omega])}
                                  \longrightarrow0 .
 \end{split}\tag{N31}
\]
The first estimate uses \(\Omega<R_j\) eventually; the second is the retained all-mode theorem of Section 25 on this refined sequence. The explicit raw lower bound for the first line is (N19) at its actual \(L_j,a_j,\theta_j,g_j\), with its full \(m_j,c_{*,j}\); the raw spectral numerator is bounded by \(\|\chi_j\|^2a_j^5/j\). Thus both raw factors accompany the probability assertion.

There is a stronger exact spectral relation at the growing cutoff (N28). By (N29),
\[
 \sup_{B\ {\rm Borel}}|\zeta_{\theta_j,g_j}(B)
                  -\zeta_{\Gamma,L_j,a_j,g_j}(B)|
       \ge1-j^{-2}-a_j^5/j\longrightarrow1 .
 \tag{N32}
\]
The supremum is at most one, so its limit is one; the total variation mass norm tends to two. Splitting the scalar product at the same physical projection and using Cauchy--Schwarz gives, with all raw norms displayed,
\[
 \frac{|\langle\chi_j,v_{\Gamma,g_j}\rangle|}
           {\|\chi_j\|\,\|v_{\Gamma,g_j}\|}
       \le\sqrt{a_j^5/j}+j^{-1}\longrightarrow0 .
 \tag{N33}
\]
Thus the native state and its electric angular coefficient become orthogonal in their common actual Hilbert space on this selected original geometry, despite both probabilities escaping fixed physical energies.

## 6. The angular comparison and its precise nonuniformity

Define the actual relative Taylor remainder at the original angle by
\[
 \eta_j^{\rm orig}
  =\frac{\|\chi_j+(2/3)\theta_j^2v_{\Gamma,g_j}\|}
          {(2/3)\theta_j^2\|v_{\Gamma,g_j}\|}.
 \tag{N34}
\]
The retained all-mode mass theorem and \(N_j=2j^2+1\) give
\[
 \frac23\theta_j^2\|v_{\Gamma,g_j}\|
 \sim
 \frac{8\pi^2}{3\cdot10^8}
       \sqrt{\frac{3I_{\rm lat}}{20}}\,
               g_j^{-2}j^{-5}\longrightarrow\infty,
 \tag{N35}
\]
since \(g_j<j^{-5}\). Every factor follows from the exact original \(D_j\), with its asymptotic applied at this final step. Because \(\|\chi_j\|\le1\), the reverse triangle inequality proves
\[
 |\eta_j^{\rm orig}-1|
       \le\frac{\|\chi_j\|}
                 {(2/3)\theta_j^2\|v_{\Gamma,g_j}\|}
           \longrightarrow0 .
 \tag{N36}
\]
This establishes actual failure of the small relative Taylor approximation on this selected sequence, rather than merely divergence of one certified upper bound. It makes no assertion of that failure on the logarithmic or fixed-electric-coefficient paths.

The strengthened cusp of Section 25 is still defined on these same Hamiltonians and couplings, using its exact \(\theta_j^\ddagger\) and actual centered state \(\chi_j^\ddagger\). Its proved relative error is \(o(a_j^5)\); the exact probability comparison (167) therefore bounds its spectral probability distance from the covariance probability by that error. Equations (N32)--(N33) therefore imply
\[
 \sup_B|\zeta_{\theta_j,g_j}(B)-\zeta_j^\ddagger(B)|
       \longrightarrow1,\qquad
 \frac{|\langle\chi_j,\chi_j^\ddagger\rangle|}
                 {\|\chi_j\|\,\|\chi_j^\ddagger\|}
       \longrightarrow0 .
 \tag{N37}
\]
For the second assertion, the normalized strengthened state converges in norm to the negative normalized covariance vector by the exact relative norm remainder in (447); applying (N33) and the triangle inequality proves the limit. This comparison records ratios only after retaining each original raw vector and the raw estimates (448),(N19),(N31).

There is also an exact unscaled map between the two angular presentations. Let
\(\mathcal R_\theta=K_\theta-I+(2/3)\theta^2\Gamma\), on \(D(\Gamma^2)\), and let \(P_\psi^\perp=I-|\psi\rangle\langle\psi|\). For any two nonzero real angles,
\[
 \begin{split}
 \chi_\theta-\frac{\theta^2}{\phi^2}\chi_\phi
 &=P_\psi^\perp
       \left(\mathcal R_\theta-\frac{\theta^2}{\phi^2}
                       \mathcal R_\phi\right)\psi,\\
 \left\|\chi_\theta-\frac{\theta^2}{\phi^2}\chi_\phi\right\|
 &\le\frac29\theta^2(\theta^2+\phi^2)\|\Gamma^2\psi\|.
 \end{split}\tag{N38}
\]
Subtract the two exact centered expansions and use the all-angle graph remainder from Section 15 to prove these identities. They retain both amplitude factors and identify the map whose relative behavior (N36)--(N37) now determines on the selected sequence.

The original cusp state thus has a proved full-Hamiltonian spectral escape sequence at weak positive coupling without changing its external cusp depth. This result extends the original-state calculation beyond the earlier strengthened-cusp theorem. The prescribed coupling paths and an interacting spatial continuum with nonzero original native low-energy weight remain unresolved; (N29) is an explicitly selected sequence, not a substitute definition of those remaining targets.
