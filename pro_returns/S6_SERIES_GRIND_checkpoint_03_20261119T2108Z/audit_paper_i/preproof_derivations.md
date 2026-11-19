# Paper I: derivations written before reading the target proofs

Date: 19 November 2026. Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited reasoning effort. This is another run in the same model family. It supplies an independent derivation in the procedural sense; it supplies no different-family check.

## I:weierstrass-comparison

Input statement: C=t^3(t-1), D=t^4(t-1)^2, arithmetic cubic y²=x³−3Cx/4+D/4, geometric cubic Y²=X³−3CX+2D. The proposed pointed map is Φ(x,y)=(2x,−2√2 y).

Direct substitution gives Y²=8y²=8x³−6Cx+2D=X³−3CX+2D. The inverse is (X,Y)↦(X/2,−Y/(2√2)), so both maps extend to the smooth projective cubic and fix the identity. The cubic discriminant in the elliptic-curve convention is −16(4A³+27B²). Arithmetic A=−3C/4, B=D/4 give Δ_ar=27(C³−D²); geometric A=−3C, B=2D give Δ_geom=1728(C³−D²)=64Δ_ar. Here C³−D²=t^8(t−1)^3, so the stated exclusion t≠0,1 is exactly what ensures smoothness. The marked point transports directly.

For the invariant differentials ω_ar=dx/(2y), ω_geom=dX/(2Y), Φ*ω_geom=−ω_ar/√2. The induced lattice morphism is z↦λz with λ=−1/√2 and Λ_geom=λΛ_ar. Thus τ is unchanged after transporting the same oriented basis, while z/ω_1 is unchanged. In the definition N=|θ_1(z/ω_1;τ)/η(τ)| exp(−π(Im(z/ω_1))²/Imτ), every factor is unchanged. This proves exact norm invariance with an explicit morphism, without identifying an untransported coordinate convention.

## I:monodromy-fundamental-set

Inputs: matrices g(B,x,t) with g(B,x,t)g(C,y,u)=g(BC,x+By,t+u−6xᵀJBy); Γ is the congruence kernel t+6Q(x)−α(B)=0 mod 12; Q(x)=x_1+x_2+x_1x_2.

For a matrix in SL₂(R), reduce its Iwasawa τ to the classical modular region. The remaining center of SL₂(Z) identifies angles differing by π, so choose 0≤θ<π. Each chosen modular A has lift g(A,0,α̃(A))∈Γ, where α̃(A) is any integer representative. Its left action is (B,x,t)↦(AB,Ax,t+α̃(A)), since the Heisenberg cross term vanishes for zero x in the multiplier. This verifies the stated S,T,−I actions with 9,1,6.

After the modular step, reduce x modulo Z² by left multiplication by g(I,m,−6Q(m)), whose membership in Γ follows exactly from the displayed congruence. This transforms x to x+m and t to t−6Q(m)−6mᵀJx. The center g(I,0,12k) then reduces t to [0,12). The order of these reductions matters and is fixed here. The resulting set intersects every orbit. In its interior, two points can be equivalent only when their SL₂ coordinates are equivalent through ±I; the angle range removes the nontrivial center, and the ordinary modular domain removes the rest. The surviving m must be zero because the two x coordinates lie in [0,1)², and then k=0 because both t lie in [0,12). On paired edges and the elliptic fixed-point strata, use the actual Γ lifts. Those sets have Haar measure zero; their stated identifications give the fundamental-set interpretation rather than a globally unique rectangular coordinate chart.

Boundary translations, using J=[[0,1],[-1,0]], are m=(1,0): (x_1,x_2,t)↦(x_1+1,x_2,t−6−6x_2) and m=(0,1): (x_1,x_2,t)↦(x_1,x_2+1,t−6+6x_1). Their commutator shifts t by −12. These signs must be compared with the paper's actual J convention and Figure I:monodromy-domain before certification.

## night:P2.2: the displayed differences

Let L=s+12v. The given F=a(μL/2, CL/12−L²/24+6v). Taking s↦s+12m gives Δ_QF=(6amμ,am(C−L)−6am²)=amγ−6am²δ. Taking v↦v+n gives Δ_RF=(6anμ,an(C−L)−6an²+6an)=anγ−6an(n−1)δ. With a=−p the radial coefficient in the quotient by Zδ is −pnγ. These are exact polynomial identities, independent of extension arguments. Deriving F=σ−o also requires the explicit z_γ convention; that has not yet been read or checked. Holomorphic extension of the origins and the no-filling conclusions P2.7/P2.9 require additional geometric proofs; these algebraic identities alone do not certify them.

## night:P2.7/P2.9: proof obligations before reading

The statements permit arbitrary proper Hausdorff analytic fillings after every finite cover. The dependency P2.4 must therefore prove meromorphic extension of the marked base map without presupposing a model of the filling. P2.6 then uses a smooth resolution to force a vanishing normal-meridian class on components dominating the base. A contradiction must propagate this class to a component meeting the cusp, using connectedness, the normal-crossing corner, and the exact origin difference P2.2. The p≠0 condition must be deduced from admissibility, and the (3k,4l) family must explicitly establish the corresponding marked-base recovery and nonzero corner coefficient. These are obligations to verify, not a claimed derivation of the theorems.

## inv:C3.8: harmonic formula

On the finite-dimensional harmonic space H with Hermitian inner product linear in the first argument, any nonzero complex-linear functional ℓ has Riesz vector v=Σ overline(ℓ(e_j)) e_j in an orthonormal basis, so ℓ(v)=Σ|ℓ(e_j)|²>0. Hence Q=v/||v||² satisfies ℓ(Q)=1 and is basis independent. If the restriction map has image Cη and ∫_Fη²=−12, its coefficient functional is exactly ℓ(e)=−(1/12)∫_F i_F*e∧η. The formula thus fixes the harmonic representative with restriction class η. This gives the stated finite-dimensional normalization; it does not evaluate the harmonic forms as atlas coefficient functions.

## ari:C.7.4

The supplied statement explicitly leaves hypothesis H open, including at the CM point. No unconditional theorem is asserted in this audit. The current task is to verify exact transports and seek an unconditional way to decide the actual norm, while preserving its present open status.
