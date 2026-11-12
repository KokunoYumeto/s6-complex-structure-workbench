# Gauge reduction and a proposed Navier–Stokes breakdown mechanism

8 September 2026. This note answers the user's conceptual question, taking an admissible Clay C/D obstruction as the premise of the discussion. It does not certify a Navier–Stokes breakdown proof or a four-dimensional quantum Yang–Mills counterexample. It preserves viscosity, forcing, gauge constraints, coordinates and raw state norms. The previously proved finite-lattice statements remain unchanged.

## Gauge representatives and the actual physical projection

On the existing finite box, retain the configuration space Q=SU(2)^E, the actual vacuum measure μ=ψ²λ, and the full vertex group G=SU(2)^V, including boundary vertices. The unitary representation is

\[
(T_hv)(U)=v((h_{s(e)}^{-1}U_eh_{t(e)})_{e\in E}),\qquad
P_Gv=\int_G T_hv\,dh.
\]

Here dh is the originally specified Haar probability measure; no state is divided by its norm. Invariance of μ proves unitarity by substitution. Group invariance of dh gives T_kP_G=P_G; inversion gives P_G*=P_G. Integrating the first identity gives P_G²=P_G. Thus this is an orthogonal projection onto the invariant functions. For every v in L²(μ),

\[
\|v\|^2=\|P_Gv\|^2+\|(I-P_G)v\|^2.
\]

The proof is the expansion of the squared norm with zero cross term: P_G(I-P_G)=0 and P_G*=P_G. Projection can change mass and annihilate a vector. It is not an invertible coordinate transformation on the whole kinematic space. It implements the particular original physical constraint; choosing a smaller sector because it improves a spectral estimate would require a different justification. In the existing calculation, the unitary between physical retained presentations is proved only after this original constraint has been specified.

A local gauge fixing, wherever a section of the orbit map exists, selects one representative of each gauge orbit. In that broad terminological sense it may be called coordinate normalization. There is no claim here that a smooth global section exists. The invariant-state projection and the choice of orbit representative have the different explicit maps just described.

In the Haar quantum space, multiplication by ψ identifies invariant functions with invariant states. For a gauge-invariant observable O whose product with ψ belongs to that space, T_h(Oψ)=Oψ because both factors are invariant. Consequently P_G(Oψ)=Oψ. In particular, projecting cannot discard a candidate already represented by such a physical state. This identity does not prove that an arbitrary fluid-derived vector has that form.

For a smooth continuum connection with the anti-Hermitian convention, write

\[
A^h=h^{-1}Ah+h^{-1}dh,\qquad F=dA+A\wedge A.
\]

On sections s, direct use of the product rule gives (d+A^h)s=h^{-1}(d+A)(hs). Squaring this equality gives (d+A^h)²s=h^{-1}(d+A)²(hs), hence F^h=h^{-1}Fh component by component. For any set of components,

\[
-2\sum_{\mu<\nu}\operatorname{tr}[(F^h_{\mu\nu})^2]
=-2\sum_{\mu<\nu}\operatorname{tr}(F_{\mu\nu}^2).
\]

Each equality uses (h^{-1}Fh)²=h^{-1}F²h and cyclicity of trace. With SU(2) anti-Hermitian components this sum is nonnegative. This is a Euclidean component norm, or a specified spatial magnetic norm if only spatial indices are included, not the indefinite Lorentzian action contraction. Divergence of this invariant norm along a sequence cannot be removed by any smooth gauge changes along that sequence. Divergence of connection coefficients A alone does not establish divergence of that norm.

## The specified fluid problem and its energy

The official [Fefferman statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf), equations (1)–(11), defines the C/D alternatives with admissible smooth initial data and smooth force. C uses R³; D uses the specified spatial torus and periodic pressure. The equation is

\[
\partial_tu_i+\sum_{j=1}^3u_j\partial_ju_i
=\nu\sum_{j=1}^3\partial_j^2u_i-\partial_ip+f_i,
\qquad \sum_i\partial_iu_i=0,\qquad \nu>0.
\]

A C/D obstruction rules out a global solution in the stipulated class for the specified data. It must not silently be strengthened into a statement about zero forcing, a different viscosity, another spatial domain, or failure of every weak formulation.

For smooth solutions before a singular time, with the stated decay or periodicity allowing integration by parts, multiply the ith equation by u_i, sum and integrate over the original spatial domain D. The transport contribution is the integral of div(u|u|²/2), hence zero. The pressure contribution is the integral of div(pu)−p div u, hence zero. Integrating the viscosity term by parts gives the exact identity

\[
\frac12\frac{d}{dt}\int_D|u|^2\,dx
+\nu\int_D\sum_{i,j=1}^3|\partial_ju_i|^2\,dx
=\int_D f\cdot u\,dx.
\]

For R³, the same integrations are justified by cutoffs when the flux limits and integrability hold; no assertion about an arbitrary smooth nondecaying field is made. Equivalently, integrate this identity between two regular times. Cauchy–Schwarz and the nonnegative dissipation give, with Y_ε=(||u||²₂+ε)^{1/2}, Y_ε'≤||f||₂. Integrate and let ε decrease to zero to obtain

\[
\|u(t)\|_2\leq\|u(0)\|_2+\int_0^t\|f(s)\|_2\,ds.
\]

Thus concentration or breakdown of a strong norm does not require divergence of total kinetic energy. This energy identity alone does not prove global smoothness and does not identify which norm fails in a particular supplied construction.

## A concrete four-coordinate encoding, with its entire gauge source

There is an exact elementary map showing how a fluid field can be encoded into a gauge field. It is useful precisely because its source and limitations can be calculated. It is not a substitution of an abelian model for the full quantum Hamiltonian.

Fix c>0, g>0 and a nonzero calibration constant λ. Keep the original fluid coordinates and define X⁰=ct and X^i=x^i, with inverse t=X⁰/c, x^i=X^i. This identifies the fluid cylinder D×[0,T) with its image in spacetime, not with all Euclidean R⁴. For D=T³, the spatial quotient remains T³. The metric for the following calculation is diag(−1,1,1,1). No Wick rotation of a singular fluid solution is asserted.

Let T=−iσ₃/2, so −2 tr(T²)=1. Define a smooth su(2)-connection before the fluid singular time by

\[
A_0(X)=0,\qquad A_i(X)=\lambda u_i(x,t)T.
\]

If u has units length/time and A_i has units inverse length, λ has units time/length². Neither λ nor c, g or ν is set to one. This linear injection into the specified connection presentation has inverse

\[
u_i(x,t)=\frac{-2\operatorname{tr}(T A_i(ct,x))}{\lambda}
\]

on its image. The inverse is not gauge invariant on arbitrary transformed representatives, and that fact is not hidden. Since all A components are multiples of T, every commutator [A_μ,A_ν] vanishes on this exact image. Substitution into the full curvature formula gives

\[
F_{0i}=\frac{\lambda}{c}\partial_tu_i\,T,
\qquad F_{ij}=\lambda(\partial_iu_j-\partial_ju_i)T.
\]

The gauge-invariant spatial curvature norm is therefore exactly

\[
-2\sum_{i<j}\operatorname{tr}(F_{ij}^2)
=\lambda^2\sum_{i<j}(\partial_iu_j-\partial_ju_i)^2
=\lambda^2|\nabla\times u|^2.
\]

Thus a divergence of fluid vorticity in this encoding is a divergence of a genuine gauge-invariant curvature quantity. No assertion that every C/D obstruction necessarily has this particular vorticity divergence is needed or made.

The complete Yang–Mills equation with a source, in the convention D^μF_{μν}=g²j_ν, is also determined exactly. All [A,F] terms vanish on the displayed image, by their common T factor. Incompressibility and commuting derivatives give

\[
j_0=\frac{-\lambda}{g^2c}\partial_t\sum_i\partial_iu_i\,T=0,
\qquad
j_i=\frac{\lambda}{g^2}
\left(\Delta u_i-\frac1{c^2}\partial_t^2u_i
-\partial_i\sum_j\partial_ju_j\right)T
=\frac{\lambda}{g^2}\left(\Delta u_i-\frac1{c^2}\partial_t^2u_i\right)T.
\]

To retain the fluid dynamics explicitly, differentiate its full equation once in time. With w_i=∂_tu_i, the current is

\[
j_i=\frac{\lambda}{g^2}\left[
\Delta u_i-\frac1{c^2}\left(
\nu\Delta w_i-\sum_jw_j\partial_ju_i-\sum_ju_j\partial_jw_i
-\partial_i\partial_tp+\partial_tf_i\right)\right]T.
\]

This calculation keeps the nonlinear transport, pressure, force and viscosity. Moreover D^νj_ν=0, because the commutators vanish and div u=0 implies the spatial divergence of the displayed current is zero. It is an exact map from each regular fluid segment to a gauge connection and its conserved source. The current has not been proved zero for a proposed breakdown example. A sourced classical connection is not yet a vacuum state of source-free quantum Yang–Mills; this specific map proves a curvature transfer, not such a state identification. Other encodings are not ruled out by its source term.

## What would affect a quantum mass gap

The [Jaffe–Witten statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf), Sections 3–4, asks for a nontrivial quantum theory with the specified axioms and a positive vacuum spectral gap. Its fields are operator-valued generalized functions, so it does not require every quantum configuration to be a smooth classical field. A failure of one classical smooth construction does not by itself contradict those axioms.

Retain an actual physical quantum Hamiltonian H and vacuum ψ of energy E₀, and its excitation form q. A positive gap Δ is the inequality

\[
q[v]\geq\Delta\|v\|^2\quad
\text{for every physical }v\in D(q)\text{ with }\langle\psi,v\rangle=0.
\]

This follows from the spectral theorem by integrating E−E₀≥Δ against the vector's raw spectral measure. Conversely, the form inequality excludes spectrum in (E₀,E₀+Δ) on that vacuum-orthogonal space: any nonzero vector in a spectral interval lying below E₀+Δ would violate the inequality by spectral integration.

Consequently actual nonzero physical vectors v_n in this same form domain, orthogonal to ψ, with q[v_n]/||v_n||²→0 would refute a positive gap: a fixed Δ would bound every one of these quotients below. No normalization of v_n is required. A sequence whose energy or some derivative instead becomes arbitrarily large does not supply this conclusion.

For an exact counterexample to the inference from unbounded high energies to zero gap, fix an energy scale ε>0 and let K on ℓ²(N₀) have domain {a:Σ_n n²ε²|a_n|²<∞} and action (Ka)_n=nεa_n. Its form domain is {a:Σ_n nε|a_n|²<∞}, with q_K[a]=Σ_n nε|a_n|². On a₀=0 it obeys q_K[a]≥ε||a||², with equality for a vector supported at n=1. For any unchanged nonzero vector supported at n=N, q_K[a]=Nε||a||². This operator has gap ε and arbitrarily high energy simultaneously. It is a logical example, not a claimed Yang–Mills construction or a model of fluid blowup.

The direct research implication of an admissible fluid obstruction is therefore its mechanism: whether a transferred, gauge-invariant concentration invalidates estimates required by a proposed quantum construction, or produces physical quantum states violating the displayed gap inequality. The concrete map above already transfers vorticity into invariant curvature, but preserves a computed gauge source and has not constructed those vacuum states. Failure of a particular continuum construction is narrower than nonexistence of every theory satisfying the axioms. The previous lattice bound likewise remains restricted to g⁴≥12288; it contains no assertion that an arbitrary continuum path stays in this range.
