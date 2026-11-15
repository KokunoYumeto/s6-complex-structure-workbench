# Independent referee of B.4.9

## Verdict

PASS for the exact scope of `ab_push_torus_log_cocycles.tex`: fixed-cocharacter logarithmic cocycles, their zero ordinary torsor class, the full punctured cusp torsor group, and the actual affine section. No arbitrary compactification or classification of all descent data follows, and the source correctly makes neither claim.

## Positive-loop sign and actual section

The period convention is Pi(c+h)=Pi(c) S_h, where S_h=I+h delta tensor gamma. A translation F_h,c from X_c to X_(c+h) has derivative the identity in the covering vector coordinates and acts on marked lattice columns by S_h inverse. After w=r^6, a positive r-loop changes c by -12. The descent deck on the logarithmic cover is therefore F_(-12,c), whereas the return identification after transport is F_(12,c-12). The latter gives the actual homology monodromy S_(-12)=I-12 delta tensor gamma. This distinguishes the deck identification from the closing return and validates the displayed N_r sign.

Substitute Pi_c gamma=(6mu,-s+C0+c) and ell=-s/12+kappa0 in C.3.5. The s terms cancel exactly, giving the bounded cusp logarithm

    bar_b(h,c)=(-h*mu/2, -h*(c+D)/12 - h*h/24),
    D=C0-12*kappa0.

The proposed section

    sigma(c)=(-c*mu/2, -c*c/24 - c*D/12)

satisfies sigma(c+h)-sigma(c)=bar_b(h,c) as an exact equality of vector coordinates. In particular its positive-loop difference is (6mu,c+D-6), precisely F_(-12,c). All coefficients are single-valued holomorphic functions of q, including at q=0. The original cusp's affine q defect is zero. Thus the q and r affine lifts commute already before quotienting by periods, and sigma is an actual holomorphic section over the punctured parameter product. Its exponential gives extending toric units for each nonzero r. Quadratic logarithmic dependence on r is retained, so no extension across r=0 is inferred.

## Linear and sheaf computations

A holomorphic group homomorphism C* to a varying complex torus lifts to t times a vector in the relative Lie bundle. Periodicity makes the vector a lattice period; its integral coefficients are locally constant. The common invariant lattice for the actual q and r monodromies is exactly Z*w plus Z*delta. Exponentiation gives the two asserted monomials. Extending torus-unit multiplication preserves every fan orbit and component, so it cannot change the previously computed component permutation.

The product of two punctured discs retracts to T2. The last cellular differential for the commuting local system has image N_q Lambda+N_r Lambda. Since N_q already has primitive image Z*w plus Z*delta, its quotient is free on gamma,u and is Z2. The analytic exponential sequence and Cartan theorem B on this Stein base give the asserted H1 of the torus-section sheaf. Naturality sends a Cartier Chern class times either invariant cycle into zero in this quotient. This proves only the fixed-cocharacter construction's zero class. The independent explicit sigma proves the actual affine family's zero class.

## Source and verification scope

The local polynomial calculation is checked separately in `ab_push_hopf_winding.py`. This referee uses the actual closing formula C.3.5 and the integral monodromy conventions, not an inference from linear monodromy alone. Fujimoto's one-dimensional formula is used as the stated model; the proof itself supplies the higher-dimensional group-homomorphism argument and retains the non-polarized case.
