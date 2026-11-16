# Periods and maximum: notation concordance

These are literal notation changes in statements and proofs. No change is made to a parameter range, quantifier, equality, inequality or equality locus. Source equation labels receive the namespace `fam:`, `ari:` or `push:`. The retained source statement numbers remain visible.

| Source notation | Paper notation | Meaning and reason |
| --- | --- | --- |
| FAM `a=5+2√6` | `a_cusp=5+2√6` | Cusp logarithmic constant, distinguished from affine twist variables. |
| FAM C.1 proof `u=e^(2πiμ₀)` | `v_cusp` | Multiplicative cusp value; avoids Engel's global `u=w²`. |
| FAM C.1 proof scalar `f` | `f_sc` | The Weierstrass scaling factor already named `f_sc` in FAM B.1.1; avoids the threefold projection `f`. |
| FAM and ARI modular nome `q=e^(2πiτ)` | `q_τ` | Distinguishes the elliptic modulus from the Albanese nomes. |
| ARI `q₁,q₂` | unchanged | `q₁=-w²/48³`, `q₂=iw/216`; `q₁=(27/64)q₂²`. |
| ARI `η` | `η_D` | Dedekind function; first-run notation, distinguished from the integral cohomology class. |
| ARI `N` | `𝒩` | The Gaussian-normalized theta norm; FAM C.2 uses `𝒩`. |
| ARI `L(t)=log N(P_t)` | `𝓛(t)=log 𝒩(P_t)` | Distinguished from a line bundle. `U_Λ` retains the full torus Green function. |
| ARI elliptic lattice `Λ,Λ′` | `Λ_ell,Λ′_ell` | Distinguished from FAM's marked rank-four period lattice. |
| ARI `Δ₀` | `Δ_mod` | The modular discriminant `q_τ∏(1−q_τⁿ)²⁴`. |
| ARI rational model `E_t`, coordinates `x,y`, point `P` | `E_t^div`, `x_div,y_div`, `P^div` | Auxiliary division-polynomial coordinates, not the FAM cubic coordinates. |
| ARI `Δ(t)=27t⁸(t−1)³` | `Δ_div(t)` | Discriminant of the auxiliary rational model. Generic `Δ_E` and `Δ_Λell` mean the discriminant of their named Weierstrass model/lattice. |
| ARI C.4.3 radicals `W,V` | `W_rad,V_rad` | Products of discriminants and division values, distinguished from the cusp fibre and the integral lattice. |
| ARI C.3.1 `G=g₂(i)` | `G_square` | Square-lattice invariant, distinguished from the local function `G(h,τ)` in the maximum proof. |
| ARI C.3.1 Taylor coefficients `A₂,A₄` | `α₂,α₄` | Avoids the monodromy matrices `A₁,A₂`. |
| ARI C.3.1/C.8.2 scalar `E=π²E₂/3` | `𝓔₂` | Scaled quasimodular scalar, distinguished from the rank-one lattice endomorphism `E`. |
| ARI C.8.2 Fourier sums `A_k` | `𝒮_k` | Scalar theta-series bounds, distinguished from monodromy matrices and duplication polynomials. |
| ARI C.8.4 coefficient bound `M` | `M_coeff` | Bound for five polynomial coefficients, distinguished from the global admissibility maximum `M`. |
| ARI C.8.4 local `u=t−1` | `v_t` | Avoids Engel's multiplicative family parameter. |
| ARI C.8.4 duplication polynomials `A_k` | `𝒜_k` | Avoids the first-run monodromy matrices. |
| ARI C.8.6 integral coordinate `u=1/℘(z)` | `v_℘` | Avoids the Engel parameter and the ladder coordinate. |
| ARI C.8.9 local base coordinate `w` | `z_B` | Avoids the global moduli parameter `w=e^(−πic)`. |
| ARI C.8.11 `W` | `𝒲` | Logarithmic theta derivative; avoids the cusp fibre `W`. |
| ARI C.8.11 `R=μ′−a` | `ℛ_μ` | Derivative defect; distinguished from radii and the theta quotient. |

## Cubic normalization and section sign

FAM B.1.1 uses `y_F²=x_F³−3t³(t−1)x_F+2t⁴(t−1)²`. FAM B.1.4 fixes the cusp branch with distinguished section `(0,−√2 t²(t−1))`. ARI C.4 uses `y_div²=x_div³−(3/4)t³(t−1)x_div+(1/4)t⁴(t−1)²` and section `(0,t²(t−1)/2)`. The coordinate substitution `x_F=2x_div`, `y_F=−2√2 y_div` identifies both equations and these distinguished sections. This is a coordinate dictionary, not a new geometric theorem. The norm is independent of the Weierstrass homothety and is even in the point, as in the ARI C.4 setup and C.1.1 proof. Generic sigma/division-polynomial arguments retain their explicitly stated normalization `x=℘`, `y=℘′/2`, `ψ₁=1`, `ψ₂=2y`.

## Special source conventions

`ρ=(1+i√3)/2=e^(πi/3)`, not the other primitive cube root. The finite values are `μ(z₁)=(2−ρ)/3`, `μ(z₂)=(1−i)/2`; the cusp value is `μ₀=1/2−i log(5+2√6)/(2π)`. All phases are continued from that branch. The period half-plane is `Im c<−M` with `M=−(3/π)log6`; the positive-imaginary Albanese representatives are `−κ₁` and `−κ₂/2`. The interval cover uses `0≤Re τ≤1/2`, `|τ|≥1` and not a change of root-deck orientation.

The current convention is exactly the corrected ARI C.8.9 convention: `ddᶜ=(i/π)∂∂̄`, positive Betti measure `db∧da`, total mass `1/12`, probability measure `12m_P`. No sign is changed in the mathematical statements.
