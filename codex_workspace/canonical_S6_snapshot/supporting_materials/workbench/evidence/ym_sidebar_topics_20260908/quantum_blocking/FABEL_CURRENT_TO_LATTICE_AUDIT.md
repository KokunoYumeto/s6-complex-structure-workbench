# Mathematical correction — 8 September 2026

This corrected edition supersedes the earlier draft at this path. It is extracted from the complete Section 13 of extensive_quantum_blocking.tex/.md. The full proof, source inputs, boundary derivation and scope are in [FABEL_TENSOR_TRANSFER.md](FABEL_TENSOR_TRANSFER.md). Equation numbers refer to the cumulative manuscript. No four-dimensional mass-gap disproof is claimed.

## Transport conventions and the vacuum-moment correction

For the column-section connection $d+\mathcal A$, ordinary parallel transport along an oriented edge $e:[0,a]\to\mathbb R^3$ solves 

$$
P_e'(s)=-\mathcal A(e(s))(\dot e(s))P_e(s),\qquad P_e(0)=I.
$$

 Its gauge transform is $P_e^h(s)=h(e(s))^{-1}P_e(s)h(e(0))$. Differentiating this formula verifies the transformed ODE and its initial value; uniqueness gives the assertion. The links in Section 1 have the opposite endpoint convention and are therefore *inverse* transports: 

$$
\qquad\text{(94)}
 U_e=P_e(a)^{-1},\quad
 U_e^h=h(e(0))^{-1}U_eh(e(a)),\quad U'(s)=U(s)\mathcal A(e(s))(\dot e(s)).
$$

 Inverses and concatenations follow by multiplication of the corresponding transport maps. Thus this is an exact gauge-equivariant map for arbitrary noncommuting connection components. It is not a global inverse from finite links to connections.

The Cartan specialization $\mathcal A_i=\lambda u_iT$, $T=-i\sigma_3/2$, has 

$$
U_e=\exp\left(\lambda T\int_e u\cdot dx\right),\qquad
 U_p=\exp(\vartheta_pT),\quad
 \vartheta_p=\lambda\oint_{\partial p}u\cdot dx .
$$

 With positively oriented $(i,j)$ faces, Stokes' theorem gives $\vartheta_p=\lambda\int_p(\partial_i u_j-\partial_j u_i)\,dx^i dx^j$. For a fixed smooth field on a compact region it equals $a^2\lambda(\partial_i u_j-\partial_j u_i)+O(a^3)$. In the general non-Abelian case the four edge expansions to second order give $U_p=I+a^2F_{ij}+O(a^3)$: the differentiated terms are $\partial_i\mathcal A_j-\partial_j\mathcal A_i$ and the four products give $[\mathcal A_i,\mathcal A_j]$, with this positive sign. For uniform $C^2$ bounds the remainder is uniform on that compact region. As $\operatorname{tr}e^{\vartheta T}=2\cos(\vartheta/2)$, the exact magnetic value is 

$$
\qquad\text{(95)}
 b(2-W_p)=\frac{2-2\cos(\vartheta_p/2)}{2g^2a}
       =\frac{\vartheta_p^2}{8g^2a}
          +O_g(\vartheta_p^4/a).
$$

 For fixed $g,\lambda$ and a fixed smooth field, summation on a regular mesh of a bounded region yields $\lambda^2(8g^2)^{-1}\int|\operatorname{curl}u|^2dx$. This follows by a Riemann sum; each leading cell term is $a^3$ times the displayed density and each uniform cell error is $O(a^4)$. Pointwise curvature growth alone does not imply growth of this integral: the volume of the concentrating region must also be accounted for.

In Lorentzian coordinates $X^0=ct,X^i=x^i$, the same Cartan field with $\mathcal A_0=0$ has the complete conserved current 

$$
\begin{aligned}
 j_0&=0,\\
 j_i&=\frac{\lambda}{g^2}
       (\Delta u_i-c^{-2}\partial_t^2u_i)T\\
 &=\frac{\lambda}{g^2}\left[
 \Delta u_i-c^{-2}\left(\nu\Delta w_i
 -\sum_jw_j\partial_ju_i-\sum_ju_j\partial_jw_i
 -\partial_i\partial_tp+\partial_tf_i\right)\right]T,\qquad w_i=\partial_tu_i.
\end{aligned}
$$

 This is obtained by differentiating the original Navier--Stokes equation, not by changing its viscosity or force. $D^\nu j_\nu=0$ follows from incompressibility and the common Cartan factor. The field solves that sourced classical equation. It can be used as data for a quantum trial state without claiming it solves source-free Yang--Mills. Proving source-free classical dynamics is not a prerequisite for defining a trial state; its physical Hilbert and spectral properties must instead be proved.

There is a separate important correction concerning Wilson observables. Evaluating $W_C$ at the links of a background gives a number $W_C(U[\mathcal A])$. The functional $W_C(U)$ on the full configuration space has no dependence on the chosen background until an additional prescription supplies it. The generic centered state $\psi(W_C-\mu W_C)$ is physical and nonzero, but naming a background does not make it a background-dependent state map. Moreover $r_C=\mu(W_C^2)$ is the actual quantum second moment. It is not $W_C(U[\mathcal A])^2$.

Keep the exact bound from Section 7, $\alpha\le r_C\le4-3\alpha$, with $\alpha=(9\,12^{16/g^4})^{-1}>0$. Then 

$$
\qquad\text{(96)}
 \frac{3\alpha}{4}\kappa\ell\le
 a_C=\kappa\ell(1-r_C/4)
 \le(1-\alpha/4)\kappa\ell .
$$

 For physical perimeter $P_C=a\ell$ this bounds the *bare* loop numerator between the displayed constants times $2g^2P_C/a^2$ at fixed $g$; it does not give asymptotic ratio one. The reconstructed numerator and norm remain $a_C-M_1(0)$ and $d_C+M_2(0)$. The lower bound $\Delta_{\rm sc}$ for these reconstructed states is used only for $\xi\le1/49152$. In a spatial continuum path $a\downarrow0$, $\kappa\to0$ would imply $g^2=(a/2)\kappa\to0$ and thus $\xi\to\infty$. Without $a\downarrow0$ the latter implication is not valid.

