# Full physical-energy asymptotics of the original electric covariance

This continuation uses the original open box and the fixed-box actual-vacuum theorem of Sections 17--18. It calculates all modes of the original weight \(n_2^2\) in direction one. The magnetic terms remain in the actual Hamiltonian throughout its final transport. The asymptotic scalar factors below are recorded explicitly; no physical vector is divided by its norm in the construction.

## Exact original operator and the component trace

Let \(N=2L+1\), \(\ell=aN\), and let \(\mathsf E_L\) be every oriented positive edge of \(\{-L,\ldots,L\}^3\). Retain
\[
 H_g=\frac{2g^2}{a}\sum_e E_e+
 \frac1{2g^2a}\sum_p(2-W_p),\quad
 A_g=H_g-E_g,\quad
 \Gamma=\sum_{e=(n,1)}n_2^2E_e,\quad
 v_{\Gamma,g}=(\Gamma-\langle\Gamma\rangle_g)\psi_g .
 \tag{T1}
\]
Here \(\psi_g\) is the actual positive unit physical vacuum. The original period, covering, coordinate, and Haar maps are those of the cumulative manuscript. If \(D^E_h=(2g^2/a)\sum_{e\parallel1}h(am(e))E_e\), then on this entire finite box the physical weight \(h(x)=x_2^2\) gives the exact identity
\[
 D^E_{x_2^2}=2g^2a\Gamma,\qquad
 g^2v_{\Gamma,g}=\frac1{2a}
       (D^E_{x_2^2}-\langle D^E_{x_2^2}\rangle_g)\psi_g .
 \tag{T2}
\]
This growing-box weight is not a fixed compact test function. We prove its limit directly below.

Let \(\mathscr R\), \(\Lambda=\operatorname{diag}\sigma_\nu\), and
\(D=\mathscr R^{\mathsf T}\mathsf W\mathscr R\) have exactly their Section 18 meanings, with \(\mathsf W_{(n,1)}=n_2^2\) and its other entries zero. The ordered form of its full comparison measure is
\[
 m^\Gamma_{L,a}=\frac3{32}\sum_{\nu,\eta}
   \sigma_\nu\sigma_\eta D_{\nu\eta}^2
              \delta_{(\sigma_\nu+\sigma_\eta)/a}.
 \tag{T3}
\]
The factor \(3/32\) includes three colours, both pair contractions and the original coefficient \(-1/8\) in the pair vector. For \(t\ge0\), set
\[
 T_t=\mathscr R\Lambda e^{-t\Lambda/a}\mathscr R^{\mathsf T},
 \qquad C^\Gamma_{L,a}(t)=\int e^{-t\omega}\,dm^\Gamma_{L,a}(\omega)
           =\frac3{32}\operatorname{Tr}(\mathsf W T_t\mathsf W T_t).
 \tag{T4}
\]
Moving the finite rectangular matrices cyclically proves this equality without a missing projection term.

Write the original exact one-dimensional vertex and edge modes as
\[
 \begin{split}
 v_r(n)&=\sqrt{\frac{2-\delta_{r0}}N}
   \cos\frac{\pi r(n+L+1/2)}N,\quad 0\le r<N,\\
 s_r&=2\sin\frac{\pi r}{2N},\\
 w_r(n)&=-\sqrt{\frac2N}
   \sin\frac{\pi r(n+L+1)}N,\quad 1\le r<N .
 \end{split}\tag{T5}
\]
Finite geometric sums and \(d_0v_r=s_rw_r\) give orthonormality and the full tensor decomposition. In a frequency block \(\boldsymbol r\), its one-form space has components only where \(r_i>0\); the gradient is its line spanned by \(s=(s_{r_1},s_{r_2},s_{r_3})\). The transverse projection is \(I-ss^{\mathsf T}/|s|^2\) on this space. Consequently, the direction-one to direction-one block of \(T_t\), in the exact basis
\[
 w_{r_1}(n_1)v_{r_2}(n_2)v_{r_3}(n_3),
 \quad 1\le r_1<N,\quad 0\le r_2,r_3<N,
\]
is diagonal, with scalar
\[
 f_t(\boldsymbol r)=
 \frac{s_{r_2}^2+s_{r_3}^2}{\sigma_{\boldsymbol r}}\,
            e^{-t\sigma_{\boldsymbol r}/a},\qquad
 \sigma_{\boldsymbol r}=(s_{r_1}^2+s_{r_2}^2+s_{r_3}^2)^{1/2}.
 \tag{T6}
\]
The scalar is zero if \(r_2=r_3=0\). This includes the absent transverse block rather than counting a spurious polarization. Since \(\mathsf W\) has only direction-one entries, (T4) uses this component block twice. All original transverse modes and their exact polarization sums have therefore been retained.

## Discrete weight estimates including both boundaries

Let \(Z\) be multiplication by \((n_2/N)^2\) on the vertex coordinate \(n_2=-L,\ldots,L\). In its cosine basis denote \(Z_{rs}=\langle v_r,Zv_s\rangle\). There is a constant independent of odd \(N\ge3\) such that
\[
 |Z_{rs}|\le\frac{C}{(1+|r-s|)^2},
 \quad \sum_{|r-s|>M}|Z_{rs}|^2\le CM^{-3},
 \quad \sum_s|Z_{rs}|^2\le\frac1{16}.
 \tag{T7}
\]
We give the boundary proof. For \(d=2,4\), define
\[
 q^{(d)}_h=\frac1N\sum_{n=-L}^L
       (n/N)^d\cos\frac{\pi h(n+L+1/2)}N .
\]
Reflect the \(N\) samples evenly at the two endpoint half-cells to a \(2N\)-periodic sequence. In its interior the absolute second differences of the polynomial samples are at most \(C_d/N^2\). At each of the two reflection junctions the second difference is bounded by \(C_d/N\), by the bound on the first derivative of \(x^d\) on \([-1/2,1/2]\). Thus the sum of the absolute second differences around the periodic sequence is at most \(C_d/N\). The Fourier multiplier of minus the periodic second difference is \(4\sin^2(\pi h/(2N))\). Even reflection identifies its Fourier coefficient, up to a unit phase, with \(q^{(d)}_h\). Division by the \(2N\) in that coefficient gives
\[
 |q^{(d)}_h|\le
 \frac{C_d}{N^2\sin^2(\pi h/(2N))}
 \le\frac{C'_d}{\operatorname{dist}(h,2N\mathbb Z)^2}
 \quad(h\notin2N\mathbb Z).
 \tag{T8}
\]
The second inequality uses \(\sin u\ge 2u/\pi\) for \(0\le u\le\pi/2\), after reflection. The zero coefficient is bounded directly by \(2^{-d}\). The product-of-cosines identity gives
\[
 Z_{rs}=\frac{\sqrt{(2-\delta_{r0})(2-\delta_{s0})}}2
                  (q^{(2)}_{r-s}+q^{(2)}_{r+s}).
 \tag{T9}
\]
For \(0\le r,s<N\), both \(r+s\) and \(2N-r-s\) are at least \(|r-s|\). Thus (T8) proves the first inequality in (T7), including the high-frequency boundary alias \(r+s\) near \(2N\). Summing the fourth-power tail proves the second; the last follows from \(Z^2\le I/16\).

The diagonal of \(Z^2\) is
\[
 A_r:=\langle v_r,Z^2v_r\rangle
 =\begin{cases}\mu_N,&r=0,\\
 \mu_N+q^{(4)}_{2r},&1\le r<N,\end{cases}
 \qquad
 \mu_N=\frac{L(L+1)(3L^2+3L-1)}{15N^4}
                 \longrightarrow\frac1{80}.
 \tag{T10}
\]
Indeed \(\sum_{n=-L}^Ln^4=L(L+1)(2L+1)(3L^2+3L-1)/15\), obtained by summing the fourth finite difference of a fifth-degree polynomial. The formula for \(v_r^2\) proves the diagonal identity. In particular
\[
 |A_r-\mu_N|\le
 \frac{C}{(1+\min(r,N-r))^2}\quad(1\le r<N).
 \tag{T11}
\]

## Full positive-time trace

For every simultaneous \(a\downarrow0\), \(\ell=aN\to\infty\), and fixed \(t>0\), we prove
\[
 C^\Gamma_{L,a}(t)
   \sim\frac{3\ell^7}{12800\pi^2a^2t^5}.
 \tag{T12}
\]
Let \(S_t\) be the direction-one diagonal matrix whose entries are \(f_t/a\), and extend \(Z\) on that component edge space as the identity in coordinates one and three. For finite self-adjoint matrices,
\[
 \operatorname{Tr}(Z^2S_t^2)-\operatorname{Tr}(ZS_tZS_t)
              =\frac12\|[Z,S_t]\|_{\rm HS}^2.
 \tag{T13}
\]
Expansion of the squared Hilbert--Schmidt norm and cyclicity of the finite trace prove the equality; its right side is nonnegative.

Put \(p_i=s_{r_i}/a\), \(\omega_{\boldsymbol r}=|p|\). The scalar of \(S_t\) is
\[
 d_t(p)=\frac{p_2^2+p_3^2}{|p|}e^{-t|p|},\qquad d_t(0)=0.
 \tag{T14}
\]
This is a continuous Lipschitz function. Away from zero, differentiating its homogeneous degree-one prefactor bounds its gradient by \(C(1+t|p|)e^{-t|p|}\le C_t e^{-t|p|/2}\). The same bound along segments follows by integration, since a point at the origin has one-dimensional measure zero and the function is Lipschitz there. Also
\[
 \frac{2|\boldsymbol r|}{\ell}\le\omega_{\boldsymbol r}
 \le\frac{\pi|\boldsymbol r|}{\ell},\qquad
 \left|\frac{\partial (s_r/a)}{\partial r}\right|\le\frac\pi\ell.
 \tag{T15}
\]
The number of nonnegative integer triples in a shell \(m\le|\boldsymbol r|<m+1\) is at most \(C(m+1)^2\): associate their disjoint unit cubes to an annulus whose radii differ by at most \(1+2\sqrt3\), and bound its volume. Equations (T15), followed by comparison of the resulting polynomial-exponential series with its integral on each unit interval, prove
\[
 \sum_{\boldsymbol r}\omega_{\boldsymbol r}^k
                 e^{-u\omega_{\boldsymbol r}}\le C_{k,u}\ell^3,
 \quad \ell\ge1,\quad k=0,1,2,\ldots,\quad u>0 .
 \tag{T16}
\]
Excluding \(\boldsymbol r=0\) when necessary only decreases these sums. The same argument after factoring out \(e^{-uR/2}\) proves a tail bound \(C_{k,u}\ell^3e^{-uR/2}\) on \(\omega_{\boldsymbol r}>R\), with an adjustment of the constant and a smaller exponent if needed.

In the commutator, only \(r_2,s_2\) differ. Split at \(1\le |r_2-s_2|\le M\), where \(M/\ell\le1\). Integration of the derivative bound and (T15) gives
\[
 |d_t(p_{\boldsymbol r})-d_t(p_{r_1,s_2,r_3})|
       \le C_t\frac M\ell e^{-t\omega_{\boldsymbol r}/4}.
\]
Here the frequency changes by at most \(\pi M/\ell\le\pi\), so replacing the minimum frequency along the segment by the initial one costs only a constant depending on \(t\). Using the last bound of (T7) and then (T16), the squared commutator contribution of these entries is at most \(C_t\ell M^2\). On \(|r_2-s_2|>M\), use \(|d-d'|^2\le2d^2+2(d')^2\), the symmetry of \(Z\), and its tail bound in (T7). The result is at most \(C_t\ell^3M^{-3}\). Choose \(M=\lfloor\sqrt\ell\rfloor\) for sufficiently large \(\ell\). Then
\[
 \|[Z,S_t]\|_{\rm HS}^2=o(\ell^3).
 \tag{T17}
\]
Both boundaries and all high-frequency modes have been controlled in this estimate.

Next,
\(\operatorname{Tr}(Z^2S_t^2)=\sum_{\boldsymbol r}A_{r_2}d_t(p_{\boldsymbol r})^2\).
On \(\omega_{\boldsymbol r}\le R\), each coordinate index is at most \(R\ell/2\), and for sufficiently small \(a\) this is less than \(N/2\). Equation (T11), summation in \(r_2\), and the \(O_R(\ell^2)\) possible pairs \((r_1,r_3)\) bound the error in replacing \(A_{r_2}\) by \(\mu_N\) by \(C_R\ell^2\). The error on the complement divided by \(\ell^3\) tends uniformly to zero as \(R\to\infty\), since \(A_{r_2}\) and \(\mu_N\) are bounded and (T16) gives the exponential tail. Thus
\[
 \operatorname{Tr}(Z^2S_t^2)
       =\mu_N\sum_{\boldsymbol r}d_t(p_{\boldsymbol r})^2+o(\ell^3).
 \tag{T18}
\]
On every fixed bounded physical frequency region,
\(s_{r_i}/a-(\pi r_i/\ell)\to0\) uniformly, using the sine Taylor remainder bounded by its cubic term. The continuous function (T14), the grid step \(\pi/\ell\), and the tail estimate give
\[
 \begin{split}
 \ell^{-3}\sum_{\boldsymbol r}d_t(p_{\boldsymbol r})^2
 &\longrightarrow
 \frac1{\pi^3}\int_{\mathbb R_+^3}
     |p|^2(1-p_1^2/|p|^2)^2 e^{-2t|p|}\,dp\\
 &=\frac1{5\pi^2t^5}.
 \end{split}\tag{T19}
\]
Coordinate planes contribute \(O_R(\ell^2)\) in each bounded region and have zero limiting measure. The angular integral on the full sphere is
\(2\pi\int_{-1}^1(1-u^2)^2du=32\pi/15\), and the positive octant gives one eighth of it. Four integrations by parts give
\(\int_0^\infty r^4e^{-2tr}dr=24/(2t)^5=3/(4t^5)\).
These constants prove the second line. Finally,
\[
 C^\Gamma_{L,a}(t)
       =\frac3{32}N^4a^2\operatorname{Tr}(ZS_tZS_t).
\]
Insert (T10), (T13), (T17)--(T19) and \(N=\ell/a\) to prove (T12).

## Entire raw mass and the exact finite-energy fraction

Define the positive finite lattice integral
\[
 I_{\rm lat}=\frac1{\pi^3}\int_{[0,\pi]^3}
 \frac{(s_2^2+s_3^2)^2}{s_1^2+s_2^2+s_3^2}\,dk_1\,dk_2\,dk_3,
 \qquad s_i=2\sin(k_i/2),
 \tag{T20}
\]
with the integrand set to zero at the single origin. Then
\[
 C_L^\Gamma=C^\Gamma_{L,a}(0)
       \sim \frac{3N^7}{2560}I_{\rm lat},\qquad
                       \frac83<I_{\rm lat}<4.
 \tag{T21}
\]
For the trace proof use the direction-one matrix with scalar
\(d_0(s)=(s_2^2+s_3^2)/|s|\), extended continuously at zero. It is globally Lipschitz on the bounded cube. Repeat (T13) with index derivative at most \(C/N\). The near-diagonal bound is \(CNM^2\), and the far bound is \(CN^3M^{-3}\), since the dimension is less than \(N^3\) and the scalar is bounded. Choosing \(M=\lfloor\sqrt N\rfloor\) makes the commutator squared \(o(N^3)\). Equation (T11) gives total diagonal-weight error \(O(N^2)\), including \(r_2\) near \(N\). The Riemann sum of the continuous symbol squared divided by \(N^3\) tends to (T20). Multiplication by \(3N^4/32\) and by \(\mu_N\to1/80\) proves the asymptotic.

To prove the bounds, take expectation for uniform \(k\) on the cube, put \(X=s_1^2\), \(S=s_1^2+s_2^2+s_3^2\), and use \(\mathbb EX=2\), \(\mathbb ES=6\). The integral is
\(\mathbb E(S-2X+X^2/S)=2+\mathbb E(X^2/S)\).
Cauchy--Schwarz applied to \(X/\sqrt S\) and \(\sqrt S\) gives \(\mathbb E(X^2/S)\ge 4/6\), with strict inequality because \(X/S\) is not constant almost everywhere. Also \(X^2/S<X\) almost everywhere since the two other coordinates have positive squares almost everywhere. This proves both strict bounds without replacing the integral by an estimated coefficient.

Let \(a\to0,\ell\to\infty\). The locally finite raw spectral limit, with its full dimensional factor recorded, is
\[
 \frac{a^2}{\ell^7}m^\Gamma_{L,a}
      \longrightarrow \frac{\omega^4}{102400\pi^2}\,d\omega
 \quad\hbox{on bounded energy intervals}.
 \tag{T22}
\]
For a complete measure proof, multiply these measures by \(e^{-t\omega}\) for a fixed \(t>0\). Their masses and Laplace transforms converge by (T12). If their masses are \(M_j(t)\), then
\[
 (1-e^{-sR})\mu_j([R,\infty))
       \le M_j(t)-M_j(t+s).
\]
Continuity of \(3/(12800\pi^2t^5)\), first choosing small \(s>0\) and then large \(R\), proves tightness; finitely many initial measures cause no difficulty. On a bounded interval, \(z=e^{-\omega}\) and Bernstein polynomial approximation show that constants and finite linear combinations of \(e^{-n\omega}\) approximate every continuous function. Tightness and the convergent transforms therefore identify the weak limit. Its density is the one in (T22) times \(e^{-t\omega}\), because \(\int_0^\infty\omega^4e^{-t\omega}d\omega=24/t^5\). Multiplication by \(e^{t\omega}\) on a bounded interval proves (T22), including its interval masses since this density has no atoms. Applying weak convergence at time \(t/2\) to the bounded continuous function \(\omega^k e^{-t\omega/2}\) also proves every positive-time moment:
\[
 \frac{a^2}{\ell^7}\int\omega^k e^{-t\omega}dm^\Gamma_{L,a}
       \longrightarrow
         \frac{(k+4)!}{102400\pi^2t^{k+5}},
                  \quad k=0,1,2,\ldots .
 \tag{T23}
\]
For every fixed \(\Omega>0\), (T21)--(T22) give the full leading raw mass and probability,
\[
 \begin{split}
 m^\Gamma_{L,a}([0,\Omega])
       &\sim\frac{\ell^7}{a^2}\frac{\Omega^5}{512000\pi^2},\\
 \rho^\Gamma_{L,a}([0,\Omega])
       &\sim a^5\frac{\Omega^5}{600\pi^2 I_{\rm lat}} .
 \end{split}\tag{T24}
\]
Here the probability uses precisely the positive raw mass (T21); the first line remains part of the assertion. On \(L_j=j^2,a_j=1/(100j)\), the first mass grows as a fixed constant times \(j^9\), while the whole mass grows as a fixed constant times \(j^{14}\). Their vanishing fraction has exact order \(j^{-5}\). This refines, rather than contradicts, the previous uniform bound.

## Transport to one actual positive-coupling sequence

Retain every earlier finite-stage test from Sections 18 and 22--24, including the single-edge directional tests, and the supplied full local-spectrum sequence, and retain \(g<j^{-5}\). Enumerate the positive rational times \(t_1,t_2,\ldots\). At fixed \(j\), set \(N_j=2j^2+1\), \(a_j=1/(100j)\), \(\ell_j=a_jN_j\), and in addition require
\[
 \begin{split}
 |g^4\|v_{\Gamma,g}\|^2-C^\Gamma_{L_j}|&<N_j^7/j,\\
 \left|g^4\langle v_{\Gamma,g},e^{-t_rA_g}v_{\Gamma,g}\rangle
                  -C^\Gamma_{L_j,a_j}(t_r)\right|
                         &<\ell_j^7/(a_j^2j),\quad r\le j .
 \end{split}\tag{T25}
\]
The fixed-box graph and finite spectral projection theorem (231) proves convergence of the total mass and every bounded heat multiplier as \(g\downarrow0\). Each prior finite-stage test likewise holds throughout a sufficiently small positive interval by its proved fixed-box limit. Intersect these finitely many intervals. Define \(k_j\) as the least positive integer such that every dyadic \(g=2^{-q}\), \(q\ge k_j\), satisfies this finite list, and set \(g_j=2^{-k_j}\). The intersection proves existence. This is a refinement of the selected actual sequence, with all earlier results retained, and not a claim about either prescribed coupling path.

Every coefficient remains
\[
 \kappa_j=200j\,2^{-2k_j},\quad
 b_j=50j\,2^{2k_j},\quad
 \xi_j=2^{4k_j-2},\quad
 2b_jM_j=100j\,2^{2k_j}M_j .
 \tag{T26}
\]
Let \(\nu_{\Gamma,j}\) be the unchanged raw spectral measure of \(v_{\Gamma,g_j}\), so \(m^\Gamma_{L_j,a_j,g_j}=g_j^4\nu_{\Gamma,j}\). Equations (T25) and the trace theorem give the heat limits at rational times. Monotonicity of positive spectral heat integrals squeezes every real positive time between rational times, and continuity of the limit gives the same conclusion there. The preceding damped-measure and moment proof applies unchanged. Consequently
\[
 \begin{split}
 g_j^4\|v_{\Gamma,g_j}\|^2&\sim(3I_{\rm lat}/2560)N_j^7,\\
 \nu_{\Gamma,j}([0,\Omega])
   &\sim g_j^{-4}\frac{\ell_j^7}{a_j^2}
                         \frac{\Omega^5}{512000\pi^2},\\
 \zeta_{\Gamma,j}([0,\Omega])
   &\sim a_j^5\frac{\Omega^5}{600\pi^2I_{\rm lat}},\\
 \|e^{-tA_{g_j}/2}v_{\Gamma,g_j}\|^2
   &\sim g_j^{-4}\frac{3\ell_j^7}{12800\pi^2a_j^2t^5}.
 \end{split}\tag{T27}
\]
All positive-time energy moments carry the coefficient in (T23), multiplied by \(g_j^{-4}\ell_j^7/a_j^2\). In particular the quotient of first energy and squared norm of the displayed actual filtered vector tends to \(5/t\).

## Exact native magnetic transfer on the strengthened original cusp family

To transfer the leading finite-energy fraction, the old relative error \(O(j^{-4})\) is insufficient compared with \(a_j^5\). We explicitly strengthen the external cusp depth while retaining the full finite Hamiltonian, vacuum, coordinate order and cover:
\[
 \begin{split}
 F(\xi)&=\xi^{3/4}(6+64\xi),\\
 T_j^{\ddagger}
    &=2C+j^5 e^{8\pi\xi_j}F(\xi_j)^{1/4},\\
 D_j^{\ddagger}
    &=L_{T_j^{\ddagger}}q_{T_j^{\ddagger}}
                             +6m_{T_j^{\ddagger}}^2,\\
 \theta_j^{\ddagger}&=\frac{2\pi}{10^4j^2D_j^{\ddagger}},\quad
 v_j^{\ddagger}=e^{-2\pi T_j^{\ddagger}/j},\quad
 t_{c,j}^{\ddagger}=(v_j^{\ddagger})^j .
 \end{split}\tag{T28}
\]
The cover remains \(j\), its matrix is the original \(P_T\operatorname{diag}(1,1,j,j)\), its pullback metric is unchanged in form, its signed determinant is \(-j^2D_j^\ddagger\), and its positive volume is \(j^2D_j^\ddagger\). The original nonwrapping connection is \(h_1(n)=\exp(-\theta_j^\ddagger n_2H_c)\), \(h_2=h_3=I\). The previously proved embedding and systole estimates apply with this larger original cusp parameter.

Relative to (242), the fourth power of \(T-C\) has an extra factor \(j^4\) in the denominator of the angle error. Thus the all-angle estimate, with its original constant \(A_{\rm rel}=138240\pi^2/10^8\), proves
\[
 \eta_j^\ddagger\le A_{\rm rel}j^{-8},
                  \qquad \eta_j^\ddagger/a_j^5\longrightarrow0 .
 \tag{T29}
\]
Let
\(\chi_j^\ddagger=(K_{\theta_j^\ddagger}-\langle K_{\theta_j^\ddagger}\rangle)\psi_{g_j}\),
and let \(n_j^\ddagger\) be its unchanged raw excitation measure. The exact norm remainder and raw measure comparison from Section 15 are
\[
 \begin{split}
 \|\chi_j^\ddagger+(2/3)(\theta_j^\ddagger)^2v_{\Gamma,g_j}\|
  &\le\eta_j^\ddagger(2/3)(\theta_j^\ddagger)^2
                    \|v_{\Gamma,g_j}\|,\\
 \|n_j^\ddagger-(4/9)(\theta_j^\ddagger)^4\nu_{\Gamma,j}\|_{\rm TV,1}
  &\le\eta_j^\ddagger(2+\eta_j^\ddagger)
          (4/9)(\theta_j^\ddagger)^4\|v_{\Gamma,g_j}\|^2 .
 \end{split}\tag{T30}
\]
Multiplying the second line by
\(9g_j^4a_j^2/[4(\theta_j^\ddagger)^4\ell_j^7]\)
makes its bound asymptotic to a fixed constant times
\(\eta_j^\ddagger/a_j^5\), which tends to zero by (T27) and (T29).
It follows, with every raw factor retained, that for \(\Omega>0\), \(t>0\),
\[
 \begin{split}
 \|\chi_j^\ddagger\|^2
    &\sim\frac{I_{\rm lat}}{1920}
       (\theta_j^\ddagger)^4g_j^{-4}N_j^7,\\
 n_j^\ddagger([0,\Omega])
    &\sim\frac{(\theta_j^\ddagger)^4g_j^{-4}\ell_j^7}{a_j^2}
                                      \frac{\Omega^5}{1152000\pi^2},\\
 \frac{n_j^\ddagger([0,\Omega])}{\|\chi_j^\ddagger\|^2}
    &\sim a_j^5\frac{\Omega^5}{600\pi^2I_{\rm lat}},\\
 \|e^{-tA_{g_j}/2}\chi_j^\ddagger\|^2
    &\sim
      \frac{(\theta_j^\ddagger)^4g_j^{-4}\ell_j^7}
                       {9600\pi^2a_j^2t^5},\\
 \frac{\langle e^{-tA_{g_j}/2}\chi_j^\ddagger,
          A_{g_j}e^{-tA_{g_j}/2}\chi_j^\ddagger\rangle}
             {\|e^{-tA_{g_j}/2}\chi_j^\ddagger\|^2}
    &\longrightarrow 5/t .
 \end{split}\tag{T31}
\]
For the energy assertion, every \(\omega^ke^{-t\omega}\) is a bounded multiplier; use (T30) with its supremum norm and (T23). No unbounded-moment conclusion is taken from unweighted weak convergence.

The raw native mass still vanishes. For example the original cusp bounds give \(D_j^\ddagger\ge c(T_j^\ddagger-C)^2\) for a fixed \(c>0\) on the proved tail. Thus \((\theta_j^\ddagger)^4g_j^{-4}N_j^7\) is at most a fixed power of \(j,\xi_j\) times \(e^{-64\pi\xi_j}\), since \(g_j^{-4}=4\xi_j\). This tends to zero; expansion of the exponential into its positive power series bounds it against every fixed inverse power. The finite-energy and time-filtered masses in (T31) also vanish, either from that bound or because they are bounded above by the total raw mass.

For completeness there is a rigorously selected low-quotient family of actual filtered native vectors. For each integer \(n\ge1\), apply the proved fixed-time norm and first-moment limits at \(t=n\), and choose the least \(j_n>j_{n-1}\) for which both relative errors in (T31) are less than \(1/n\). Existence follows from the two limits and their positive leading constants. The actual vectors \(e^{-nA_{g_{j_n}}/2}\chi_{j_n}^\ddagger\) then have quotient \(5/n+o(n^{-1})\), with their raw masses given by the fourth line of (T31) on this subsequence. The filter is an explicit operation, not an identification with the original unfiltered state.

This theorem establishes the exact leading finite-energy fraction of the original weighted covariance and its proved native magnetic transfer on an explicitly strengthened cusp and coupling selection. It does not identify that selection with \(g_j^2=1/\log j\) or \(g_j^2=\kappa_*/(200j)\); it supplies no uniform-volume rate on those prescribed paths. It also does not identify the depth \(T_j^\ddagger\) with the initial depth \(T_j=j^2\), or prove survival of a nonabelian interaction in a spatial continuum. Those original targets remain part of the active assignment.
