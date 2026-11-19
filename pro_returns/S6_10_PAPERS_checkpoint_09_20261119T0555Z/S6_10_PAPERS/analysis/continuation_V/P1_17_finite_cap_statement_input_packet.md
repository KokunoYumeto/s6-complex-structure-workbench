# P1.17 isolated finite-cap step: clean review packet

Review scope: independently derive the finite-cap obstruction for the positive homology reflection G below, before opening the target proof. The target assertion is that a putative anti-biholomorphism of completed fourfolds covering complex conjugation of the marked base cannot extend over the order5 affine cap with induced homology map G. The full theorem also uses a separate cusp-fan obstruction; that proof and its outcome are excluded from this packet.

The order5 cap is the quotient of a holomorphic torus family over a root disk with coordinate t by the cyclic generator

(t,x) -> (zeta_5 t, M1 x+v1/5).

Here x is an additive coordinate on the real torus Lambda_R/Lambda, Lambda=Z^6. At t=0 this describes the deck action on the central complex torus. The coarse base coordinate is t^5. An anti-biholomorphism covering conjugation lifts on the punctured root disk to t -> eta*conjugate(t), eta^5=1; its induced map on the central torus, if extended, is affine with integral linear part G and an unspecified translation. All translation identities are read in Lambda_R/Lambda. The task is to derive the resulting obstruction from equivariance with the root deck generator. Do not assume a translation value or a preferred lift.

Exact input matrices and vectors:

```json
{
  "M1": [
    [
      1,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      1,
      1,
      2,
      2,
      1
    ],
    [
      0,
      -1,
      0,
      -1,
      0,
      1
    ],
    [
      1,
      -1,
      -1,
      -1,
      -1,
      -1
    ],
    [
      -1,
      1,
      0,
      0,
      0,
      0
    ],
    [
      1,
      0,
      0,
      1,
      0,
      0
    ]
  ],
  "v1": [
    1,
    3,
    -2,
    -1,
    2,
    0
  ],
  "G": [
    [
      1,
      0,
      0,
      0,
      0,
      0
    ],
    [
      2,
      0,
      0,
      0,
      -1,
      0
    ],
    [
      -1,
      0,
      -1,
      0,
      0,
      0
    ],
    [
      -1,
      0,
      0,
      -1,
      0,
      0
    ],
    [
      2,
      -1,
      0,
      0,
      0,
      0
    ],
    [
      -1,
      1,
      1,
      1,
      1,
      1
    ]
  ],
  "ell": [
    1,
    0,
    0,
    0,
    0,
    0
  ]
}
```

The integral marking and generator above are part of the construction, so their effect must be computed explicitly; changing their signs or replacing the torus by a rational lattice is not permitted. No proof step or evaluated obstruction is supplied.
