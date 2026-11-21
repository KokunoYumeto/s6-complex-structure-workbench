# Paper I: root derivations before opening the four target proofs

Targets: ari:C.1.2, inv:A1.1, inv:A4.2 and inv:C1.2. The target statements were extracted in `S6_SERIES_PUBLISH_I_root_statement_intake.json`; the four target proof environments have not yet been opened. These derivations use the cited statement inputs and the precise previously read material described below. They are not claims of an independent model family.

## Exposure and inputs

The introduction, marking dictionary and family propositions B.1.1–B.1.4 and C.1.1 were read during structural planning. In particular, C.1.1 already gives a square-lattice theta evaluation. That is an explicitly known input to this derivation of ari:C.1.2; no claim is made that the formula was previously unseen. The statements (not proofs) of inv:A1.3, A4.1, C1.1, A3.2, C3.7 and D1.1 were extracted separately. The first Jacobi-product step of ari:C.1.1 was accidentally exposed during a definition read. That target has been reassigned for a separate derivation-before-proof check; no root event is claimed for it.

## ari:C.1.2

Let ρ=(1+i√3)/2, so ρ²=ρ−1. On the Eisenstein lattice, α=1+ρ has degree 3 and kernel {0,±μ}, where μ=(2−ρ)/3: αμ=1. The distribution-product statement ari:C.1.1 and the symmetry N(−μ)=N(μ) give N(μ)²=|α|=√3. Thus N(μ)=3^(1/4). On the square lattice, α=1+i has kernel {0,(1−i)/2}; the same statement gives N((1−i)/2)=√2.

The defining Gaussian factor now gives |θ₁(μ,ρ)/η(ρ)|=3^(1/4) exp(π/(6√3)) and |θ₁((1−i)/2,i)/η(i)|=√2 exp(π/4). For the phases, use the Jacobi product in q=exp(2πiτ), X=exp(2πiz). At ρ, q is negative real and X=−exp(π/√3). Every paired product factor is positive: for odd n, the largest positive qⁿX is exp(−2π/√3)<1; even factors are sums of positive quantities. With the branch continued from the specified cusp, the prefactor i q^(1/12) X^(−1/2) has phase π/12. At τ=i the corresponding prefactor and all remaining factors are positive. These calculations give exactly the two complex ratios in the statement, not merely their absolute values.

Insert these ratios into β=(6i/π)log(R/(2√3)). The Eisenstein value is −1/2+i(1/√3−3 log48/(2π)); the square value is i(3/2−3 log6/π). Finally (6/π)log(N/(2√3)) gives −3 log48/(2π) and −3 log6/π respectively. The exact kernel and phase computations resolve the choices of sign and branch. A new direct product computation will be compared with the target's actual computational steps after its proof is opened; this derivation alone adds no computation event.

## inv:A1.1

On a node chart xy=t, Ω¹_X(log D) has frame dx/x, dy/y, dz, and the base logarithmic differential maps to dx/x+dy/y. On a triple chart xyz=t, the frame is dx/x,dy/y,dz/z and dt/t maps to their sum. At a finite root chart t=s^m, the frame is ds/s,dy₁,dy₂ and dt/t maps to m ds/s. The integer m is invertible over C. Each quotient is therefore locally free of rank two. On the ordinary locus this is the usual rank-two relative cotangent sequence. Free finite étale quotient charts preserve the vector-bundle conclusion.

The invariant fibre vector ξ=∂/∂ζ₂ is nonzero on the smooth torus and finite root covers. In a toric cusp chart it is the invariant one-parameter logarithmic vector associated to the nonzero marked vertical direction. A unimodular toric change gives a nonzero constant coefficient vector in the logarithmic frame; the base character evaluates to zero on it. Thus it stays nonzero in the vertical logarithmic tangent bundle at boundary strata. Pairing with ξ is surjective E→O_X and has a line-bundle kernel N.

The determinant calculation is exact: det A=K_X(D), f*Ω¹_B(logΣ)=f*K_B(f*Σ), and f*Σ=W+3S₁+4S₂, whereas D=W+S₁+S₂. Hence det E=K_X⊗f*K_B^(−1)⊗O(D−f*Σ)=ω_f(−2S₁−3S₂). For the short exact sequence with quotient O_X, exterior product canonically identifies the kernel with det E. No numerical approximation enters this calculation. The comparison must check that the paper's actual cusp charts use the same nonzero marked logarithmic vector; this is a stated scope to verify, not an assumed result of a metadata link.

## inv:A4.2

The explicit local maps establish the degree-one assertion. For xy=t, send the class of (a,b,c) to (xa−yb,c) in (x,y)⊕R. The relation (y,x,0) maps to zero, the map is onto, and xa=yb implies (a,b)=(yh,xh), since x and y are relatively prime. It is an isomorphism. The ideal (x,y) is torsion-free and fails to be free at the double locus.

For xyz=t, the relation vector is (yz,xz,xy). Its coordinate gcd is 1 in the convergent power-series UFD. If a fraction h multiplies all three coordinates into R, every denominator prime divides all three, so h lies in R. The relation submodule is saturated, and R³/R(yz,xz,xy) is torsion-free. At the triple point its minimal number of generators is 3 while its rank is 2; at an ordinary double point one reduces to the preceding node map. It is therefore not locally free along that locus.

For t=s^m, quotienting by dt=m s^(m−1)ds gives the direct summand R/(s^(m−1))ds, supported exactly on the reduced multiple fibre. The other summands are free. The free finite-root covering of the total space is faithfully flat, so torsion and its support descend to precisely S₁∪S₂. Degree two has the nonzero R/(x,y) summand on a node chart, and the displayed triple-point module in inv:A4.1 extends that support through the triple strata. Consequently the original external degree-one assertion must be corrected by degree. Its exact published locators must be checked against the opened AC26 primary PDF before the citation wording is finalized.

## inv:C1.2

The ranks in inv:C1.1 give the basis statement by elementary linear algebra. The nonzero image a=d₁g spans the kernel in H^(1,1). A complementary h-dimensional space maps isomorphically to H^(2,1), so its images c_j form a basis. The map from H^(1,2) is injective with h-dimensional image in H^(2,2). A complementary e has nonzero image spanning H^(3,2). Squaring d₁ gives zero, so the four displayed two-term chains have precisely the indicated endings.

For the actual h=1 threefold, take the global q restricting to η, supplied by inv:A3.2. Its class is complementary to a, because on a complex torus the first Frölicher differential is zero and η is nonzero. The restriction of g is γ^(0,1), which is nonzero by the displayed period-covector formula. The real (1,1) form η has nonzero square, namely integral −12. In complex dimension two its wedge map from (0,1)-forms to (1,2)-forms is invertible: in coordinates its matrix is the cofactor matrix of the nondegenerate Hermitian coefficient matrix. Thus γ^(0,1)η≠0, proving gq≠0 and hence that it is a basis of the one-dimensional H^(1,2).

The restriction of q² is η²≠0. Every d₁-image restricts to zero on the torus, so q² is outside the one-dimensional image in H^(2,2). It can be chosen as e. Rescaling g changes the associated basis representatives compatibly. This argument uses the explicit restriction morphism and the nonzero determinant of η; it does not use the later metric-obstruction proposition.

## Remaining root targets

The target proofs of inv:A2.3, inv:D1.2 and inv:D4.2 remain unopened. Their preread derivations require, respectively, the precise Duke–Imamoğlu hypergeometric branch, the root-chart characters and cusp direct-image extension, and the full cusp tangent/normalization complex. Those input identifications are still being worked out and receive no completed event here.
