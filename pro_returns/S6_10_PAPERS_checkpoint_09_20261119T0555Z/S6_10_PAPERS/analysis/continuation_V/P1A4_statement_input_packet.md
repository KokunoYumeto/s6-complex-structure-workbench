# P1A.4 statement and construction packet

This packet contains only statements of existing inputs and explicit construction data. It does not contain the target proof, centralizer calculation, translation exact sequence, or conclusions about its stalks.

## night:P1.1

```latex
\begin{theorem}\label{night:P1.1}

The finite homology monodromies have orders $5,4$, respectively, and
characteristic polynomials
$(T-1)^2\Phi _5(T)$ and $(T-1)^2(T+1)^2(T^2+1)$.
For $N=M_0-I$ we have $N^2=0$, $\operatorname{rank}N=3$, and
nonzero Smith factors $1,1,1$.  Moreover
\[
 \Lambda^{\langle M_1,M_2\rangle}=0,\qquad
 \Lambda_{\langle M_1,M_2\rangle}=\mathbb Z,
\]
where the quotient homomorphism is $\ell(x)=x_0$.
On the cohomology lattice the corresponding groups are $\mathbb Ze_0$
and $\mathbb Z/2$.  Every nonidentity power of each specified affine
action $\tau_i$ is free.
\end{theorem}
```

## night:P1.4

```latex
\begin{theorem}\label{night:P1.4}

The genus-two pencil has one nodal fibre away from $0,\infty$, at
$\lambda_*=-256/3125$.  Good reduction at $0,\infty$ requires root
orders $8,5$.  On this root orbifold its Hodge bundle is
$\mathcal H=T^3\oplus T$, where
\[
T=\mathcal O\bigl((2/5)[\infty]-(3/8)[0]\bigr),\qquad
\deg T=1/40,
\]
and $T^3$ is the line generated meromorphically by $dx/y$.
\end{theorem}
```

## night:P1.5

```latex
\begin{theorem}\label{night:P1.5}

The formula in the prompt with $P$ the image of
$\ell_0\wedge\mathcal H$, and $\mathcal H$ the rank-two Hodge bundle,
cannot produce a rank-three subbundle.  The required rank-three image
is instead the image of $\ell_0\wedge\mathcal H_{\mathrm{dR}}$, where
$\mathcal H_{\mathrm{dR}}$ is the full rank-four de Rham bundle.
\end{theorem}
```

## night:P1.8

```latex
\begin{theorem}\label{night:P1.8}

With the corrected rank-three bundle $P$ of P1.5, the supplied rank-six
system admits a holomorphic lifted family
$F_c=(\sigma+ic\alpha e)(P)$ on the punctured base.
For a specified splitting $\sigma$ there is a real analytic function
$h$ with finite attained minimum $h_{\min}$, and the exact domain of
real parameters giving $F_c\cap\overline{F_c}=0$ everywhere is
$c>-h_{\min}$.
At the cusp its periods have the form
$Z(q)=(\log q/(2\pi i))I_3+C(q)$ with $C$ holomorphic and bounded.
The construction extends to the two finite root charts and descends to
orders $5,4$ on the rank-six system.
\end{theorem}
```

## night:P1.9

```latex
\begin{theorem}\label{night:P1.9}

The periodic Kuhn fan, in the marking $S$, gives a smooth proper
holomorphic filling of the periods $Z(q)=sI_3+C(q)$ for a sufficiently
small disk.  Its central fibre is reduced with normal crossings.
Modulo the index-one period lattice it has respectively $1,7,12,6$
strata of dimensions $3,2,1,0$, each isomorphic to the corresponding
complex torus $(\mathbb C^*)^d$, and Euler number $6$.
An index-$d$ period sublattice gives $d$ times these stratum counts and
Euler number $6d$.
\end{theorem}
```

## night:P1.10

```latex
\begin{theorem}\label{night:P1.10}

For every real parameter $c>-h_{\min}$ the corrected construction gives
a compact smooth complex fourfold $M_c$ and a proper holomorphic map
to $\mathbb P^1$ with the two specified multiple fibres and the
index-one Kuhn cusp.  With its complex orientation,
$\pi_1(M_c)=1$ and $\chi(M_c)=6$.
\end{theorem}
```

## night:P1.15

```latex
\begin{theorem}\label{night:P1.15}

The rank-six flat extension, as a complex flat bundle with its invariant
line, has the following explicit algebraic connection model.  Set
$\omega_k=x^kdx/y$, $0\leq k\leq3$, and use the quotient frame
\[
(w_2,w_1,w_0,w_{-1},w_{-2})
 =(\omega_{01},\omega_{02},\omega_{03},\omega_{13},\omega_{23}),
\qquad \omega_{12}=-3\omega_{03}.
\]
These are meromorphic frames of
$(L^2,L,\mathcal O,L^{-1},L^{-2})$, where $L=T^2$ on the root
orbifold of orders $5,4$.  If a frame is written as a row of vectors,
its derivative is right multiplication by
\[
\Gamma_6=\begin{pmatrix}0&b\\0&\Gamma_W\end{pmatrix},\qquad
b=\frac1{\lambda-\lambda_*}
 \left(-\frac{25}{6\lambda^2},-\frac{125}{48\lambda},0,1,0\right),
\tag{1.15.1}
\]
where
\[
\resizebox{\textwidth}{!}{$\displaystyle
\Gamma_W=\frac1{3125\lambda+256}
\begin{pmatrix}
-8(625\lambda+48)/\lambda&-8&10\lambda&75\lambda^2/2&0\\
-125/(2\lambda)&-4(625\lambda+48)/\lambda&8&0&75\lambda^2/2\\
300/\lambda^2&-375/\lambda&0&-48&60\lambda\\
120/\lambda^3&0&125/(2\lambda)&4(625\lambda+48)/\lambda&-8\\
0&120/\lambda^3&50/\lambda^2&-125/(2\lambda)&8(625\lambda+48)/\lambda
\end{pmatrix}.$}
\tag{1.15.2}
\]
This model specifies a canonical algebraic splitting, denoted
$\sigma_b$.  The compatible contraction used for the real parameter is
$\alpha=(625\pi i/128)\alpha_{\rm alg}$, where
$\alpha_{\rm alg}(w_0)=4/3$ and it vanishes on $w_1,w_2$.
\end{theorem}
```

## night:P1A.1

```latex
\begin{theorem}\label{night:P1A.1}

For every admissible member, its vertical translation bundle on
$\widehat B$ and its first coherent direct image are
\[
 E_0=F^\vee=\mathcal O\oplus L^{-1}\oplus L^{-2},\qquad
 G=R^1h_*\mathcal O_M=\mathcal O\oplus L^{-1}\oplus L^{-2}.
\]
Moreover $R^qh_*\mathcal O_M=\bigwedge^qG$ for $0\le q\le3$,
$K_M=h^*L^{-6}$, and
\[
 (h^0(\mathcal O_M),\ldots,h^4(\mathcal O_M))=(1,1,0,0,0).
\]
\end{theorem}
```

## Definitions fixing the local family

Write a=-256/3125. The base is the root curve Bhat with order5 at infinity and order4 at zero; the reduced root divisors are D_infinity,D_zero. Set L=O(4D_infinity-3D_zero). Its degree is1/20 and the degree of the coarse pushforward of L^r is floor(4r/5)+floor(-3r/4). The cusp point a has no stack stabilizer. The rank-five quotient has holomorphic splitting L^2 directsum L directsum O directsum L^-1 directsum L^-2 in the ordered meromorphic frame (w2,w1,w0,w-1,w-2) of P1.15. The flat rank-six bundle adds its invariant vector e as the first coordinate. For a real admissible c, the holomorphic three-plane is the span of the lifted w2,w1,w0-(625*pi/96)c e. Equivalently, it is the image of P=O directsum L directsum L^2 under sigma_b+i c alpha e. The complex parameter uses sigma_b+xi alpha e. The model in P1.15 fixes its connection and normalization.

At zero use lambda=t^4 and the regular frame multiplier diag(1,t^6,t^3,1,t^-3,t^-6), with e first. At infinity use lambda=u^-5 and multiplier diag(1,u^-8,u^-4,1,u^4,u^8). The finite cyclic charts are quotients of the corresponding holomorphic torus family by the root rotation together with the marked affine action M_j x+v_j/m_j from P1.1. The action on the total space is free. These charts define the two multiple fibres without introducing a branch singularity in the total space.

For the cusp fix its P1.1 integral marking S. In additive coordinates on C^3/Z^3 the periods are Z(q)=log(q)/(2*pi*i) I3+C(q). In multiplicative coordinates x_j=exp(2*pi*i*z_j), the deck action indexed by nu in Z^3 is
(x,q) -> (exp(2*pi*i*C(q)nu) q^nu x,q).
The fan is the cone at height1 over the periodic Kuhn triangulation of R^3 with integer vertices. Its maximal simplex at v in Z^3 for a permutation sigma of {1,2,3} has vertices
v, v+e_sigma(1), v+e_sigma(1)+e_sigma(2), v+e1+e2+e3.
Thus each maximal toric chart has four coordinates z0,z1,z2,z3, with q=z0*z1*z2*z3. Every overlap map is the monomial map obtained by the change between these unimodular height-one bases, followed by the displayed holomorphic deck multiplier. The central reduced divisor is D=(q=0); its normalization and all conductor intersections are determined by this explicitly specified fan and deck action. These chart definitions are the construction underlying P1.9 and the arbitrary-dimensional periodic quotient theorem of supplied Yang, Theorem8.7, Corollary8.8 (source labels thm:higher-dimensional-periodic and cor:kuhn-euler).

For sheaf conventions, Omega^p_M means the ordinary holomorphic p-form sheaf. Omega^p_M(log D) is defined branchwise by the local generators dz_j/z_j on divisor branches and dz_j on the other coordinates, with the monomial transition maps above; residues use Res(dz_j/z_j)=1. Relative logarithmic forms quotient by dq/q=sum dz_j/z_j. These define the maps to be derived, without asserting their global ranks. On the smooth locus the relative cotangent is F, and P1A.1 supplies the coherent direct-image input G and its exterior powers.

The input supplied to the fresh reviewer is the exact construction/connection data above. This packet does not contain the target proof's chosen resolutions, resulting connecting maps, or their ranks.

## Exact integral affine construction data

The integral homology lattice is Lambda=Z^6 in column-vector coordinates. The root chart of order5 uses M1 and v1; the order4 chart uses M2 and v2. Their deck maps are (t,x) -> (zeta_m t, M_i x+v_i/m) on the corresponding torus family. The root charts are glued to the punctured family using these fixed marked transformations, and the clutch translation is zero. The root rotations specify the chosen generators. The cohomology convention is A=M1^t, B=M2^t. No centralizer or translation-section answer is included in this packet.

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
  "m1": 5,
  "m2": 4,
  "cusp_marking_S": [
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

The torus fibre attached to a three-plane F is F^dual modulo the evaluation image of Lambda. A translation section therefore means a local holomorphic section of F^dual modulo that lattice image, compatible with all displayed finite affine quotient and cusp deck maps. At the cusp, extension is defined by the actual monomial chart maps in the fan construction above. The marking fixes all identifications, so fibrewise linear or translation automorphisms must be compared using these maps.

## Target

```latex
\begin{theorem}\label{night:P1A.4}
The fourfold has algebraic dimension one and
\[
\Aut^0(M)=\mathbb C,\qquad
\Aut(M)=\mathbb C\times\mathbb Z/2.
\]
In a fixed holomorphic splitting, two members of the full
admissible complex parameter half-plane are biholomorphic
exactly when their parameters are equal.
\end{theorem}
```
