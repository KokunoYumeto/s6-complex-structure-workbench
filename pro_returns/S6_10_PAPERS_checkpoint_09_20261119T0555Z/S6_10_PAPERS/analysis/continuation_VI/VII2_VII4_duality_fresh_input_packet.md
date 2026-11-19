# Clean inputs for two isolated conductor-duality bounds

This packet contains the hypotheses, desired isolated assertions, and cited inputs. It contains neither target proof nor a review of either target. The reviewer is asked to write the complete derivation before opening the isolated printed steps.

## Common definitions and supplied situation

S is a compact irreducible reduced hypersurface surface in a smooth complex threefold. Its invertible dualizing sheaf L=omega_S is torsion, and chi(S,O_S)=0. Let eta:T to S be its finite normalization. Let Q=eta_*O_T/O_S, let I be the conductor ideal Ann(Q), let Gamma be the conductor image scheme defined by I in S, and put C=Gamma_red. The conductor can be nonreduced. The normalization and S are connected. Include the empty-conductor case in the first assertion.

The normalization square is the actual finite conductor square; none of these schemes is to be replaced by its reduction without specifying the sheaf map. Canonical sheaves mean dualizing sheaves. The standard cited analytic duality inputs are finite/proper duality for the finite normalization and Serre duality for a compact Cohen--Macaulay curve or the hypersurface surface. In local algebra, the normalization canonical module is Hom_A(B,omega_A) for the finite normal extension A subset B. Torsion line bundles have degree zero on every reduced curve component. Curve Riemann--Roch and the exact curve-normalization sequence are available classical inputs.

Primary opening locators: Van Straten1987 original thesis section2.2.2--2.2.5 printedpp60--61, local original PDF `analysis/continuation_VI/source_scans/vanStraten1987_original.pdf`, scans `vanStraten_pdf63.png` and `vanStraten_pdf64.png`. The proper-duality isomorphism is on printedp60. Root reopened Serre1955 Theorem4 printedp22 and its pairing p23; ask root for the primary file if an additional opening is needed. A.5.12's statement, without proof, is in `analysis/continuation_VI/VII_duality_input_statement.json`; its original stronger ambient assumptions are retained in that input. The two receiving assertions below state their own ambient scope.

## VII.2 isolated assertion

Under the common hypotheses, prove chi(C,O_C) at least -1, with the actual normalization quotient, conductor scheme and curve restriction maps retained. Only this coherent-conductor bound is requested; the remainder of VII.2's class-VII topological argument is outside the requested scope.

## VII.4 isolated refinement

In addition, S is the irreducible reduced support of a full fibre of a proper torus fibration f:Y to a compact curve, with smooth compact complex threefold Y and H^2(Y,Q)=0. Let pi:Z to T be the minimal resolution. The actual holomorphic pullback homomorphism Pic^0(Y) to Pic^0(Z), induced by restriction to S, eta and pi, is nonconstant. The curve C is nonempty. Each component of its normalization has genus zero or one, as supplied by the proved anticanonical-support input VII.1. Prove chi(C,O_C) at least zero from this nonconstant pullback, and prove that e(C)=0 then forces C to be a disjoint union of smooth elliptic curves. Conversely such a union has e(C)=0.

The Picard varieties here denote the connected complex Lie groups of topologically trivial holomorphic line bundles, and their tangent spaces at the identity are H^1(O) with the usual pullback maps. No nonzero-rank conclusion or dimension estimate is supplied in this packet; those are part of the requested derivation. The resolution map and all the intermediate pullbacks remain the ones specified above. The rest of VII.4's Hopf classification is outside this isolated request.
