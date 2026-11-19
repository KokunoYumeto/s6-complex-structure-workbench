# Fresh derivation of the P1.17 order-five affine-cap obstruction

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation, 19 November 2026.

Only `analysis/continuation_V/P1_17_finite_cap_statement_input_packet.md` has been read. Neither P1.17's printed proof nor another reviewer's evaluated obstruction has been opened. The packet gives the exact integral lattice, M=M1, v=v1, G, and ell=(1,0,0,0,0,0). Put T=Lambda_R/Lambda, a=v/5 and d(t,x)=(zeta_5 t,Mx+a).

The integral covector ell defines the actual continuous group homomorphism chi:T→R/Z, [x]↦ell(x) mod Z. The first rows of the supplied M and G both equal ell. Thus ell M=ell and ell G=ell, as literal integral equalities. The first coordinate of v is one, so chi(a)=1/5. In particular chi(M^{-1}x)=chi(x), since M is an integral automorphism.

Suppose an anti-biholomorphism over conjugation extends across the cap. For any lift with root-coordinate multiplier eta, its base map is t↦eta bar(t). Complex conjugation sends zeta_5 to zeta_5^{-1}; therefore equivariance with the given deck generator is exactly Fd=d^{-1}F. This exponent is fixed by the root coordinate and is independent of eta. On the central real torus write F(x)=Gx+c for an arbitrary c∈T. The two sides are

Fd(x)=GMx+Ga+c,

d^{-1}F(x)=M^{-1}Gx+M^{-1}c−M^{-1}a.

The linear parts require GM=M^{-1}G. The exact supplied matrices satisfy this relation, as the fresh integer multiplication below will verify. The translation equality in T is

(G+M^{-1})a=(M^{-1}−I)c.

Apply chi. Its right side is zero for every translation c. Its left side is 1/5+1/5=2/5 in R/Z, which is nonzero. This is a contradiction. No translation was set to zero and no preferred lift was chosen.

For completeness, a different lift differs by d^k. Its linear part is M^kG and its translation is M^kc+Σ_{j=0}^{k−1}M^j a. The integral equality ell M^k=ell shows that chi(M^kGx)=chi(x) for every k. Its base multiplier changes from eta to zeta_5^k eta, but still conjugates the root generator to its inverse. The same chi calculation therefore still gives 2/5=0 as the necessary condition. The obstruction is independent of the lift and keeps the supplied lattice and marked generator unchanged.

The exact deck action is consistent with its order-five quotient: direct integer multiplication gives M^5=I and Mv=v, so d^5 translates by v∈Lambda and is the identity on T. The accompanying new standard-library script verifies these matrix identities, the homology conjugacy, all five lift covectors, and the nonintegral obstruction. These are finite arithmetic statements; the preceding map comparison supplies the universal argument for all translations and all lifts.
