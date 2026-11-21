# Paper I: targeted check of ari:C.1.1

**Outcome: the complete stated distribution identity and kernel product agree with the derivation written before the printed proof was opened. No correction is proposed.**

The source is the frozen Paper I snapshot with SHA256 `d2e6c3bec1500144bfc0ef85e636ded534f2abc998cf58fdaf521b1e8a183169`, statement and proof at lines 7360–7418. The statement-only intake has SHA256 `364be972320f8dbaa9c4fb126fa94f98fcb1b7db111a0317d651722389617c2a`.

## Order and scope of the check

The derivation was saved at 00:48:20 UTC on 21 November 2026, before the target proof was displayed, in `S6_SERIES_PUBLISH_I_C11_preread_derivation.md` (SHA256 `3e85eeb7380f530a7b79d951cd4bf60e01074916beab3f650edf4c851c6f6af7`). The separate preread receipt preserves this order. The earlier exposure to C.4.2's use of the origin expansion is explicitly recorded; no claim of complete isolation from the target's surrounding mathematical context is made.

After saving that derivation, the entire printed proof was opened and read. It has one numbered step containing the following successive arguments. Each was compared with the already saved derivation.

| Printed argument | Prior derivation and comparison |
|---|---|
| Jacobi product and zero mean | The product has the same modulus as the sine form in preread Step 1. Its fixed complex unit disappears in the logarithmic modulus. Integration gives exactly `−πT/6 + πy − πy²/T`; its average in y is zero. Endpoint logarithms are integrable. |
| Euclidean Laplacian and isogeny degree | Preread Step 2 independently obtains `2πδ₀ − 2π/area(Λ)` and `d = |α|² area(Λ)/area(Λ′)`. The kernel is closed under negation, so the `z+v` translation convention produces the required singular support. |
| Equality without an additive constant | Both sides have the same logarithmic masses and constant Laplacian; their difference is harmonic on a compact torus. Each has zero Haar mean, including the pullback along the finite surjective isogeny. The constant therefore vanishes exactly. |
| Origin expansion and discriminant normalization | Preread Step 3 tracks the period-one theta derivative `2πη³`, the lattice scale `ω`, and `g₂³−27g₃²=(2π/ω)¹²η²⁴`. The coefficient of the origin constant is exactly `1/12 log|ΔΛ|`. |
| Kernel product and endomorphism specialization | Preread Step 4 subtracts the identity term and takes the limit, obtaining `log|α| + (log|ΔΛ′|−log|ΔΛ|)/12`. Exponentiating gives the full stated formula. For equal source and target lattices it gives `|α|`. The degree-one empty product is also consistent with lattice scaling. |

The argument is valid pointwise away from the kernel and as an identity of locally integrable functions at its logarithmic zeros. The finite kernel makes the translated sum finite. No positivity, realness or extra endomorphism condition on the nonzero complex number α was inserted.

The saved derivation and the printed proof use the same Green-function mechanism. This record claims a **targeted proof check derived before reading**, not a different proof method. There is no numerical or certificate step in the target, so no computational event is claimed. The final sentence referring to the special-value calculation in D.4.5 is a consequence/application of this result; it is not used as a premise in the proof checked here.

## Event

One event of type `targeted proof check` is recorded in `S6_SERIES_PUBLISH_I_C11_CHECK_EVENTS.tsv`, with the inherited, unexposed reasoning-effort wording. No independent-reproof, computation, background, editorial or page-reading event is added for this work. Canonical aggregate counts have not been refreshed.
