# Minimal recognition theorem: typed proof obligations

## Conditional theorem

Let `X` be the compact smooth six-manifold underlying the proposed complex threefold, and let

`p = 12 ell_0 - 4 ell_1 - 3 ell_2`.

Assume the obligations `(G)`, `(V1)`, `(B1)`, `(F1)`, and `(L1)` below. If `p = -1`, then `pi_1(X)=1` and `H_*(X;Z)=H_*(S^6;Z)`. Standard Hurewicz-Whitehead recognition and `Theta_6=0` then give `X diffeomorphic to S^6`. This route does not require Proposition 7.2 or the first Mayer-Vietoris computation.

## Theorem-critical obligations

### (G) Global analytic construction

The period family, cusp filling, finite cyclic fillings, and gluing define a Hausdorff, second-countable, compact complex manifold with the stated proper holomorphic map to `P^1`.

**Falsifiers:** failure of proper discontinuity; non-Hausdorff quotient; incompatible gluing cocycle; singularity in a claimed smooth chart; failure of compactness or properness.

### (V1) Based van Kampen data

The three based meridians are primitive and induce exactly

`xy=c^{ell_0}`, `x^3=c^{ell_1}`, `y^4=c^{ell_2}`,

with the stated orientations, affine drifts, central fibre loop, and cusp null-homotopy.

**Falsifiers:** a nonprimitive meridian; reversed relative sign; extra lattice generator; nonzero cusp meridian in `pi_1(N_0)`; drift not equal to the stated `ell_i`.

### (B1) Integral cusp specialization

For `0 <= q <= 4`, the nearby-cycle specialization

`H^q(W;Z) -> H^q(F;Z)^{T_0}`

is an isomorphism of integral lattices, with the stated cup-product and saturation properties.

**Falsifiers:** hidden torsion; nonsaturated image; rank mismatch; incorrect normalization differential; failure of the supported Gysin class to map to the claimed primitive sublattice.

### (F1) Finite-fibre specialization lattices

At the order-three and order-four fibres, the pullback lattices and indices in degrees one through four are exactly those in Proposition 7.14, including the degree-two parity condition and degree-three index at the order-four fibre.

**Falsifiers:** incorrect extension class; failure of pullback injectivity; different Smith invariants; wrong parity class or transfer normalization.

### (L1) Leray transgression comparison

The first transgression is the based gluing obstruction

`d_2^{0,1}(12 gamma)=+/- p omega`,

and the cup-product identifications on the `E_2` page are geometric and sign-compatible, so multiplicativity forces the same integer in degrees two and three.

**Falsifiers:** a different obstruction integer; incompatibility between coefficient-pairing duality and cup product; relative sign failure; noncommuting comparison between local lifts and the global Leray edge map.

## Additional obligations for the first topology route

- **(C1)** finite equivariant CW model and continuous global cusp-collapse retraction;
- **(C2)** integral collapse matrix with orientations, torsion, and saturation;
- **(C3)** equality of collapse specialization and nearby-cycle specialization;
- **(MV1)** geometric identification of the printed Mayer-Vietoris map.

These are required for the explicit collapse claims and first homology computation, but not for the minimal recognition route above. Lemma A.3 must first be rewritten with cohomological variance.
