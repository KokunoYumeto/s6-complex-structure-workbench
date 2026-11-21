# Boundary topology — actual proof comparisons

## push:src:D.4.3 [032L]

The preread derivation constructs the exact open quotient map and the character map Phi(Ax)=(exp(2πi m_j·x)) to prove closure(AZ4)=A(Z4+V_k) and the Hausdorff quotient R×(S1)^r. The printed first step uses the equivalent annihilator description in the image hyperplane. Its initial period-specific rank assertion was checked directly: the last three columns (τ,μ),(1,0),(0,1) are real independent because Imτ>0; vanishing of the independently expanded determinant gives rank exactly3.

The printed second step's rational/discrete criterion agrees with the preread saturated-annihilator argument. A discrete subgroup of real3-space has rank≤3, forcing an integral kernel; a rational kernel can be completed to an integral basis. Irrational kernels give a countable, nonclosed subgroup whose closure has a positive-dimensional vector component. The Chabauty containment follows from limits of each fixed integral period and closedness. The preread diagonal example proves that equality need not hold and provides the actual nontrivial quotient map between the two limits. The fresh program checks exact annihilator examples of ranks3,2,1,0 and the nearest-integer estimate in this example; those illustrative checks do not replace the general proof.

**Outcome:** both printed steps agree with the saved derivation. No source fault, and no identification of the fixed quotient with a generally larger Chabauty limit.

## push:src:D.4.1 [032J]

Both printed steps agree with the saved derivation. The local radial implicit argument gives |h|²=epsilon/3+O(epsilon²), with uniform angular error, and the finite quotient is explicitly the order-four punctured-disc quotient. The strict maximum plus the negative cusp asymptotic supplies the compact-complement gap, so the local curve is the full level. The printed Ramanujan route and my E6²/Delta route give the same coefficient (9π⁴E4(i)/4)h⁴, then (π⁴E4(i)/4)epsilon². The fresh rational polynomial computation checks the coefficients9/4 and1/4 and their signs. The global maximum certificate and E4(i) value are cited inputs and are not independently certified here.

## push:src:D.4.2 [032K]

Step1 agrees with the preread norm-level identity, finite-root analyticity, compactness away from the cusp, and bounded-inverse proper-action proof. The source's finite affine action remains free for the same actual noninteger invariant-circle translation regardless of the sign of D. The irrational case fails Hausdorffness in the fibre. The rational case uses exactly the preread first-nonzero-period Taylor coefficient and unbounded integer multiples, producing nonseparated central points in the full attempted quotient. This proves the word “precisely”; it does not confuse a discrete central rank-three quotient with a neighbourhood in the total quotient.

Step2 is the identical independently derived superharmonic formula. The fresh polynomial program verifies the cleared-denominator identity 2T³∂∂bar(m²/T)=|Tμ_z−mτ_z|². Multiplication by−6 gives the printed factor−3/T. The root-cover minimum principle excludes every compact negative component, and the connected negative cusp neighbourhood joins the remaining ones. No global radial certificate is required for this connectedness proof.

## push:src:D.4.8 [032Q]

Step1 translates the exact previously stated global level theorem by c(H)=log(2sqrt3)−πH/6. The hypotheses H>H* and c<log sqrt2 are exactly equivalent. The unique C1 curve and its nonzero derivative at0 are precisely within the input's stated scope.

Step2 gives H0=3log48/(2π), the correct signs and nesting, shrinking to1 and exhaustion of every compact subset. The fresh coefficient-vector computation in (log2,log3) verifies H*=(3,3)/π, H0=(6,3/2)/π and their difference=(3,−3/2)/π. The C1 crossing is the separately stated D.4.5, not a fresh certification of that expansion in this check.

Step3 agrees with the fresh full4-by4 determinant expansion in the fixed real row order: det_R Π=T Imβ−6(Imμ)²=T D. Absolute value is the covolume. The retained last three columns give rank3 at the boundary, and the exact quotient is D.4.3's. The maximal two-disc domain follows from the already checked proper-action/nonseparation argument of D.4.2. All hypotheses and orientations agree.

**Overall scope:** all four target proofs were opened after their respective derivations were frozen. Every printed step has now been compared. The independent program uses sparse rational polynomials, all24 determinant terms, integer elimination on exact algebraic-number coefficient representations, and nearest-integer inequalities. No retained program was opened or reused. The original global ari:C.8.15 analytic certificate is retained as an input, with no duplicate independent credit.

Files: `S6_SERIES_PUBLISH_I_D43_preread_derivation.md`, `S6_SERIES_PUBLISH_I_D41_D42_D48_preread_derivation.md`; exact first-open JSON files; `code/S6_SERIES_PUBLISH_I_boundary_exact.py`; `output/S6_SERIES_PUBLISH_I_boundary_exact.json`.

Saved UTC: 2026-11-21T01:20:20.855494+00:00
