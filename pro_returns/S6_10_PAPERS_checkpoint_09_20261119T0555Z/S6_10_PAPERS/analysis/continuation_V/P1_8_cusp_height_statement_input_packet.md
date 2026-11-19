# P1.8 isolated cusp height asymptotic: statement and construction data only

Review target: derive h(q)=Im(log(q)/(2*pi*i))+O(1) as q tends to0, uniformly on a branch strip of bounded real part of log(q)/(2*pi*i). Do this before opening P1.8's printed proof or its earlier producing computation.

The real rank-four flat lattice has the companion matrices Cf,Cg below. Put D=Cf*Cg^-1-I. Its exterior-square quotient W is obtained by quotienting out the invariant vector q_inv=(1,1,1,1,1,1) in the displayed lexicographic exterior basis. To specify exact coordinates, Q is I6 with its first column replaced by q_inv; pi(w) is the last five coordinates of Q^-1*w. Equivalently use the primitive representative w-contr(w)*q_inv/2. These two representations are related by that actual projection. The contraction contr on an exterior vector is the displayed row functional, and contr(q_inv)=2.

The real six-dimensional extension V has invariant vector e=(1,0,...,0), quotient the final five coordinates, and cusp logarithm N_V below. Its induced quotient logarithm is N_W, the last5x5 block. These are actual nilpotent integral matrices, and all matrix identities relevant to the asymptotic must be derived from the data.

```json
{
  "Cf": [
    [
      0,
      0,
      0,
      -1
    ],
    [
      1,
      0,
      0,
      -1
    ],
    [
      0,
      1,
      0,
      -1
    ],
    [
      0,
      0,
      1,
      -1
    ]
  ],
  "Cg": [
    [
      0,
      0,
      0,
      -1
    ],
    [
      1,
      0,
      0,
      0
    ],
    [
      0,
      1,
      0,
      0
    ],
    [
      0,
      0,
      1,
      0
    ]
  ],
  "N_V": [
    [
      0,
      0,
      0,
      -1,
      1,
      -1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      1,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      1,
      0,
      0,
      0
    ],
    [
      0,
      -1,
      1,
      0,
      0,
      0
    ]
  ],
  "invariant_q": [
    1,
    1,
    1,
    1,
    1,
    1
  ],
  "wedge_lex_order": [
    "01",
    "02",
    "03",
    "12",
    "13",
    "23"
  ],
  "contraction_row": [
    1,
    -1,
    1,
    1,
    -1,
    1
  ]
}
```

Let s=log(q)/(2*pi*i), y=Im(s), and let a(q) be a holomorphic4-vector on a disk with a_0(0) nonzero. The line ell in H is generated in the real flat frame by u=(I+sD)*a(q). Define P=pi(ell wedge H). Its unipotent canonical extension is obtained by untwisting with I-sN_W. The given holomorphic splitting sigma of its pullback to V has a bounded holomorphic expression in these canonical frames; its projection to W is the inclusion of P. In flat frames it is obtained by untwisting the input, applying this canonical splitting, and restoring with I+sN_V.

Set r=i*pi(u wedge conjugate(u)), a real vector in W. Its unique lift to ell wedge H is i*u wedge conjugate(u); define A=contr(i*u wedge conjugate(u)). The chosen polarization has A positive. Define the real height h by

sigma(r)-conjugate(sigma(r))=2*i*A*h*e.

Changing the bounded holomorphic splitting is permitted, and the target asymptotic is required for every such splitting. All bars here refer to the specified real flat frames. The residue nonvanishing a_0(0) is supplied by the nodal differential; its proof is outside this isolated review. No expansion, evaluated contraction, or leading coefficient calculation is supplied in this packet.
