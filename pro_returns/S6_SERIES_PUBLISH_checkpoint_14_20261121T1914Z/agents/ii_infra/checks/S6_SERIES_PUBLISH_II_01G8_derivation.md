# Frozen-before-target derivation: 01G8 / cdp:st:D.2.1

I read the exact target statement and its cited statements D.1.2 and C.3.4, with the empty supplement. I have not read D.2.1's printed proof. C.3.4 has already been independently derived and compared, exposing that its proof uses smoothness of the ambient Y. The present derivation therefore records the intended smooth ambient scope explicitly; root has requested a corresponding hypothesis guard for both statements. No conclusion for a broader singular reading is claimed.

For the given proper connected-fibre map from the smooth compact threefold Y to the compact curve C, the connected-fibre condition identifies f_*Q with the constant sheaf Q on C. The beginning of the Leray sequence injects H^1(C;Q) into H^1(Y;Q). Since b1(Y)=0, H^1(C;Q)=0. The compact Riemann surface C has genus g=0.

The smooth general fibre is a complex two-torus, so H1(F;Q) has dimension four. The stated rational monodromy is the identity. Thus its coinvariant quotient is the whole four-dimensional vector space and the invariant subspace in the dual also has dimension four. In the notation of the exact component-count input D.1.2, t'=4.

For any prescribed nonempty finite set Delta containing all critical values, D.1.2 supplies the exact identity r=2g+s-1+t'-b1(Y). Substitution of g=0, t'=4 and b1(Y)=0 gives r=s+3. Each of the s nonempty fibres contributes at least one irreducible component. The strict inequality r>s forces at least one reducible support. This argument applies to every allowed Delta, retaining precisely its finite-set and critical-value hypotheses.

Apply the already derived smooth-ambient C.3.4 separately to each reducible fibre. Every component of any such fibre lacks a compact Kahler resolution, by pulling back a distinct component divisor to a resolution and pairing its nonzero effective zero divisor with a Kahler form while its real first Chern class vanishes. Therefore a fibration in this intended smooth scope cannot have every component of every fibre admitting such a resolution.

The only numerical step is the four-dimensional torus coinvariant count and its substitution in D.1.2; a new exact symbolic arithmetic certificate is included with the comparison. The statement's visible text currently omits “smooth”; the row remains open for root review of the explicit hypothesis guard and every receiving use. This file records the before-proof derivation, not completion of the broad wording and not a check event.
