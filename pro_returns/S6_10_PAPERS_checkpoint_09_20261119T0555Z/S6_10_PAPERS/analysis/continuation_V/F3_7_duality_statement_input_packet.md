# F3.7 finite and cusp dual-convention review: statement and construction only

## Existing statements

```latex
\begin{theorem}[a global nonpolarized period family]\label{maps:src:F.3.6}


The integral rank-six system with cohomology monodromies $A,B$
admits a holomorphic subbundle $\mathcal F$ of rank three over
$U$ satisfying $\mathcal F\cap\overline{\mathcal F}=0$.
It extends holomorphically on the finite root charts.  At the
cusp an integral marking puts its periods in the form
\[
 Z(t)=\frac{\log t}{2\pi i}I_3+C(t),
 \tag{F.13}\label{maps:eq:F.13}
\]
where $C$ is holomorphic at zero and bounded there.

\end{theorem}

\begin{theorem}[compact holomorphic filling]\label{maps:src:F.3.7}


The smooth eight-manifold of Theorem \ref{maps:src:F.2.6} carries an integrable
complex structure.  There is a proper holomorphic map to
$\mathbb P^1$ whose regular fibres are complex three-tori,
whose two finite reduced fibres are the free affine quotients
of orders five and four specified in Theorem \ref{maps:src:F.2.5}, and whose
remaining fibre is the index-one Kuhn degeneration.

\end{theorem}
```

## Exact construction conventions

The base U=P1 minus{0,infinity,a}, a=-256/3125, has its usual complex structure. Choose real based peripheral paths to infinity and zero, with their positive small loops g1,g2 and g0=(g1*g2)^-1. The supplied flat cohomology lattice V_Z has monodromies A,B on column vectors. The F3.6 holomorphic plane F in V_C is real-transverse and is extended over the finite roots. The torus associated to a plane F is F^dual modulo evaluation of the dual integral lattice V_Z^dual. All cohomology/homology conversions must use this exact evaluation map.

The target homology matrices are M1=A^t and M2=B^t; they and the prescribed affine numerators and cusp marking are in the JSON below. The target finite affine quotients use (t,x)->(zeta_m*t,M_i*x+v_i/m), orders5,4 and zero clutch. The issue to review is the exact passage from the given cohomology convention to these target homology conventions, including the effect of conjugating the base and fibres, the actual holomorphic charts, and the cusp marking/period/fan maps. Do not infer the dual representation by merely renaming A,B.

The logarithmic graph in F3.6 has period matrix(I3,Z(q)) with Z(q)=log(q)/(2*pi*i)I3+C(q), C bounded holomorphic. The local target cusp coordinate is real-normalized q=lambda/a-1. Its fixed fan is the cone at height1 over the periodic Kuhn triangulation: a simplex at v∈Z³ for a permutation s has vertices v,v+e_s1,v+e_s1+e_s2,v+(1,1,1). The multiplicative period action is (x,q)->(exp(2*pi*i*C(q)*nu)*q^nu*x,q). These formulas define the chart gluing to be compared.

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
  "M2": [
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
      0,
      0,
      0,
      1,
      0
    ],
    [
      0,
      -1,
      -1,
      -1,
      -1,
      -1
    ],
    [
      0,
      0,
      0,
      0,
      0,
      1
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
    ]
  ],
  "A": [
    [
      1,
      0,
      0,
      1,
      -1,
      1
    ],
    [
      0,
      1,
      -1,
      -1,
      1,
      0
    ],
    [
      0,
      1,
      0,
      -1,
      0,
      0
    ],
    [
      0,
      2,
      -1,
      -1,
      0,
      1
    ],
    [
      0,
      2,
      0,
      -1,
      0,
      0
    ],
    [
      0,
      1,
      1,
      -1,
      0,
      0
    ]
  ],
  "B": [
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
      0,
      -1,
      0,
      1,
      0
    ],
    [
      0,
      0,
      -1,
      0,
      0,
      1
    ],
    [
      0,
      0,
      -1,
      0,
      0,
      0
    ],
    [
      0,
      1,
      -1,
      0,
      0,
      0
    ],
    [
      0,
      0,
      -1,
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
  "v2": [
    -1,
    0,
    0,
    0,
    0,
    0
  ],
  "S": [
    [
      0,
      0,
      0,
      1,
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
      -1,
      0,
      0,
      0,
      1,
      0
    ],
    [
      1,
      0,
      0,
      0,
      0,
      1
    ],
    [
      -1,
      0,
      0,
      0,
      0,
      0
    ]
  ]
}
```

This packet contains no F3.7 proof, evaluated dual/conjugation result, or fan-comparison outcome. The preceding data are the existing construction to be related by explicit maps.
