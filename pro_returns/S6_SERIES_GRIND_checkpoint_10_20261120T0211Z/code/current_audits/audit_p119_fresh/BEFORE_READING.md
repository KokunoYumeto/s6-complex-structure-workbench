# P1.19: fresh derivation before the receiving proof

## Scope, inputs, and exposure

This derivation was written before reading the proof of `night:P1.19`, any earlier proof of that target, the current global reconstruction program, its saved arrays, other audit derivations, `parts/V.body.linked.tex`, or the current paper PDF.

The permitted inputs actually read were:

1. `audit_root/packets/P119_statement_and_cited_inputs_07.tex` and `P119_packet_receipt_07.json`.
2. The subsequently requested `P119_additional_raw_inputs_07.tex`, `P119_raw_AB_vectors_07.tex`, and their separate receipts.
3. Hatcher, *Algebraic Topology* (2002), Theorem 3.43, printed page 254, in the supplied author PDF `audit_corrections/primary_sources/Hatcher2002_author_07.pdf`.

The first packet includes the statement and proof of P1.12, including its global homology conclusion. That is an exposure, not a fresh conclusion. The derivation below uses P1.12's constructive marked torus, complement, boundary, finite-cap, and collar models. It does not use P1.12's global homology conclusion, its last duality argument, or Poincare duality for the closed eight-manifold. The target statement itself also supplied the expected answer and ranks. Thus the computation below is a fresh reconstruction and derivation from the isolated inputs, not an experiment conducted without knowledge of the expected answer.

The precise comparison with the particular pre-existing saved global matrix file is deferred until after this document is frozen. The mathematical derivation below produces a fully specified integral complex, proves its comparison to the geometric gluing, and computes its homology. No claim of equality of independently chosen integer bases is made before that comparison.

## 1. The marked geometric pieces

Write `W` for the compact smooth cusp cap, `B` for its boundary, and `Y` for the complement assembled with the two finite caps. The isolated raw definitions identify their common boundary as the mapping torus of

\[
M_0=(M_1M_2)^{-1},\qquad M_1=A^t,\quad M_2=B^t.
\]

The symbols `A` and `B` in this displayed formula are the literal 6-by-6 matrices in the raw input packet; the boundary space will continue to be denoted `B`. The code uses the literal entries, not a pre-existing output file. The vectors are

\[
v_1=(1,3,-2,-1,2,0)^t,\qquad v_2=(-1,0,0,0,0,0)^t,
\]

with multiplicities 5 and 4 and `ell(x)=x_0`. The matrix `S` in P1.1 gives the integral basis

\[
(a_1,a_2,a_3,b_1,b_2,b_3),\qquad
S^{-1}M_0S=\begin{pmatrix}I_3&I_3\\0&I_3\end{pmatrix}.
\]

All three local pieces glue through the actual collars in the packet. P1.12's evaluation inverse identifies the varying complex torus with the marked real torus; its collar isotopy removes exactly the term `L J_c(u)v_i` while fixing the outer collar. The finite collar becomes `x-a v_i`. Consequently the finite cap and boundary maps used below concern the actual gluing. The index-one cusp is the actual Kuhn cap in P1.9. P1.11's logarithmic mapping-cylinder comparison identifies its boundary-to-cap retraction on a nearby fibre with the marked collapse `kappa` and identifies the cap's deformation retraction with its central fibre `C`.

The cap `W` is a compact oriented smooth real eight-manifold with boundary `B`: its orientation is the complex orientation, and the boundary is taken over a small regular parameter circle. Its homology is the homology of `C`, namely free groups of ranks

\[
c_k=(1,3,9,9,10,3,1,0,0).
\]

The geometric input used from P1.11 is stronger than these ranks. For

\[
L_k=\bigwedge^k\Lambda,\qquad T_k=\bigwedge^k M_0-I,
\]

it gives

\[
\ker\kappa_k=\operatorname{sat}(\operatorname{im}T_k),
\]

and the image of `kappa_k` is primitive, with ranks

\[
r_k=(1,3,9,9,9,3,1).
\]

Thus the target groups and the integral quotient maps are fixed, up to explicitly allowed integral changes of basis in the image and the extra degree-four summand.

## 2. The actual complement complex and its exact fibre fillers

Set `W_{i,k}=wedge^k M_i`. I use precisely the constructive models supplied in P1.12:

\[
G_k=L_k\oplus L_{k-1}\oplus L_{k-1},
\]

\[
d_G(f,x_1,x_2)=((W_{1,k-1}-I)x_1+(W_{2,k-1}-I)x_2,0,0),
\]

\[
B_{i,k}=L_k\oplus L_{k-1},\qquad
d_{B_i}(f,x)=((W_{i,k-1}-I)x,0).
\]

The finite boundary maps to `G` by identity on the fibre and inclusion in its corresponding edge. The cusp map is the actual inverse-word map

\[
j_G(f,x)=(f,-W_{2,k-1}W_{0,k-1}x,-W_{0,k-1}x).
\tag{2.1}
\]

Its differential identity is

\[
-(W_1-I)W_2W_0-(W_2-I)W_0=W_0-I.
\]

For the finite cap put `epsilon_i=ell(v_i)`, `P_i=(epsilon_i v_i,e_1,...,e_5)`, and `P_i^{-1}M_iP_i=1 direct-sum R_i`. Then

\[
E_{i,k}=\bigwedge^kK\oplus\bigwedge^{k-1}K,
\quad d_{E_i}(f,x)=((\bigwedge^{k-1}R_i-I)x,0).
\]

In the split basis, the four rows of the boundary map are

\[
x\mapsto(x,0),\quad
v\wedge x\mapsto(0,\epsilon_i\sum_{j=0}^{m_i-1}(\bigwedge R_i)^jx),
\quad g_i\wedge x\mapsto(0,x),\quad g_i\wedge v\wedge x\mapsto0.
\tag{2.2}
\]

The change to the original lattice is the block diagonal matrix with `wedge^k P_i^{-1}` and `wedge^{k-1}P_i^{-1}`. These are integral maps of the supplied actual cellular models: P1.12 gives the signed-permutation conjugators, the product circle cells, and the swept-strip explanation of (2.2), including its sign. Its based marking and edge-cylinder comparison gives (2.1). No finite-cap torsion is discarded.

The complement is the cone of the two maps `(j_G,-j_E)`:

\[
Y_k=G_k\oplus E_{1,k}\oplus E_{2,k}\oplus B_{1,k-1}\oplus B_{2,k-1}.
\tag{2.3}
\]

The fresh program `derive_chain.py` builds (2.1)--(2.3) directly from the raw matrices, calculating exterior powers by minors. Its exact calculation gives chain ranks

\[
(3,22,71,132,155,118,57,16,2)
\]

and free homology ranks

\[
(1,1,3,9,12,9,3,0,0).
\]

Here is the map needed for the geometric comparison, beyond merely listing those ranks. Let

\[
J_k:L_k\longrightarrow Y_k
\]

be the fibre block of `j_Y`, where `j_Y` is (2.1) followed by the inclusion `G -> Y`. The fresh integral homology projections give

\[
(J_k)_*=0\quad(k=2,3,4,5).
\tag{2.4}
\]

In the independently chosen degree-one and degree-six target homology bases the other relevant fibre maps are

\[
(J_1)_*=(20,0,0,0,0,0),\qquad
(J_6)_*=(0,-20,0)^t.
\tag{2.5}
\]

The nonzero degree-six map is why a separate geometric check of the degree-six suspension is required.

Equation (2.4) is certified at chain level, not only over the rationals. The saved file contains integral matrices

\[
F_k:L_k\longrightarrow Y_{k+1}\quad(k=2,3,4,5)
\]

with the exact identities

\[
d_YF_k=J_k.
\tag{2.6}
\]

The construction of every such matrix is explicit. For a differential `d_k`, let `U d_k V=D` be the program's integral Smith decomposition, and let `r=rank(d_k)`. Set `Z=V[:,r:]`, so `Z` is an integral basis of the kernel. Write `d_{k+1}=Z A`, and let `P A Q=D'` be its Smith decomposition. Let `a=rank(A)`. On a fibre column `j`, its cycle coordinates are `V^{-1}[r:,:]j`. The bottom `dim ker-a` coordinates of `P V^{-1}[r:,:]j` are zero by (2.4). The filler is

\[
Q[:,0:a]\,\operatorname{diag}(D'_{00}^{-1},\ldots,D'_{a-1,a-1}^{-1})
\,(P V^{-1}[r:,:]j)[0:a].
\tag{2.7}
\]

The nonzero `D'` entries for `Y` are units; thus (2.7) is integral. Both the producing program and the separate saved-array verifier multiply (2.6) exactly. This supplies the explicit morphisms used in the later normalization.

## 3. Reducing the cusp boundary over the integers

For each `k`, take a Smith decomposition

\[
U_kT_kV_k=D_k.
\]

The fibre basis in degree `k` is `U_k^{-1}` and the suspension basis in degree `k+1` is `V_k`. In these bases the boundary differential is a direct sum of two-term blocks

\[
\sigma_{k,j}\longmapsto (D_k)_{jj}\tau_{k,j}.
\]

The fresh calculation gives the following nonzero Smith factors:

| `k` | nonzero factors of `T_k` | free quotient rank |
|---:|:---|---:|
| 0 | none | 1 |
| 1 | `1,1,1` | 3 |
| 2 | six copies of `1` | 9 |
| 3 | ten copies of `1`, then `2` | 9 |
| 4 | six copies of `1` | 9 |
| 5 | `1,1,1` | 3 |
| 6 | none | 1 |

All unit blocks contract integrally. After their contraction the boundary complex has:

* fibre cycles `F^B_k` of ranks `r_k` in degree `k`;
* free suspension cycles `S^B_{k-1}` of ranks `r_{k-1}` in degree `k`;
* one additional two-term block `t in degree 4 -> 2 z in degree 3`.

In particular

\[
H_k(B)_{\rm free}\cong F^B_k\oplus S^B_{k-1},
\]

with ranks `(1,4,12,18,18,12,4,1)`, and the only torsion is the class of `z`, of order two in `H_3(B)`.

The supplied primitive-kernel statement identifies the collapse in exact integral coordinates. Choose the first `r_k` target basis vectors as the images under the actual collapse of the last `r_k` columns of `U_k^{-1}`. At degree four extend these nine primitive vectors by one vector `e`. In the original fibre coordinates,

\[
K_k=U_k[\operatorname{rank}T_k:,:]
\]

is the collapse matrix onto its image, with an extra zero row in degree four. This is a matrix of the actual collapse because its kernel and primitive image are the ones proved in P1.11. Both arrows identifying the quotient are explicit: the quotient projection is `K_k`, and a section on the chosen image basis is the corresponding block of `U_k^{-1}`.

The cap has free homology, so its finite free cellular chain complex can be contracted integrally onto this homology with zero differential. Explicitly choose in each degree

\[
C_k(W)=B_k\oplus\widetilde H_k\oplus S_k,
\]

where `B_k=im d_{k+1}`, `ker d_k=B_k direct-sum Htilde_k`, and `d:S_k -> B_{k-1}` is an isomorphism. Projection to `Htilde`, inclusion of `Htilde`, and

\[
h(b,\widetilde x,s)=(0,0,(d|_{S_{k+1}})^{-1}b)
\]

satisfy `dh+hd=id-ip`. These are integral maps. Transfer the actual boundary map through this contraction. Its fibre part is `K_k`; its remaining suspension part is an initially unspecified integral map. Contracting the boundary's unit blocks and applying chain homotopies removes their values. On the remaining complex write the map as:

\[
F^B_k\xrightarrow{\;1\;}\operatorname{im}\kappa_k,
\qquad S^B_{k-1}\xrightarrow{h_k}H_k(C),
\qquad z\mapsto0,\qquad t\mapsto w+a e,
\tag{3.1}
\]

where `w` belongs to the collapse image in degree four. This notation records actual transferred maps; it makes no assertion that an unspecified suspension map is zero.

## 4. The two geometric suspension values that must be retained

### Degree one

The generator of `S^B_0` is the cusp meridian along the zero section. P1.10's zero section extends over the cusp disk. It bounds that actual section disk in `W`, so

\[
h_1=0.
\tag{4.1}
\]

The marking is fixed: this is `(f,x)=(0,1)` in the boundary cone, not an unspecified lift of its quotient class.

### Degree six

In the basis `(a,b)`, the invariant lattice in `L_5` has the integral basis

\[
x_j=a_1\wedge a_2\wedge a_3\wedge b_1\wedge\cdots
\widehat{b_j}\cdots\wedge b_3,\qquad j=1,2,3,
\tag{4.2}
\]

with the signs fixed by the displayed exterior order. This follows directly from `M_0(a,b)=(a+b,b)`; equivalently `wedge^5` is the determinant-twisted dual representation, and the invariant covectors are precisely the three `b`-coordinate covectors. The determinant is one. The integer statement follows as well because these covectors are a basis of the full fixed integral lattice.

Let `T_j={b_j=0}` be the invariant five-dimensional subtorus. Its mapping torus represents the suspension cycle `(0,x_j)`. Here is the cellular comparison underlying that assertion. The three subtori and all their intersections are product subcomplexes of the `(a,b)` product torus. The linear monodromy preserves every one. Cellular approximation can therefore be performed on this finite family, first on their intersections, then on their union, and then on the remaining cells. The approximation homotopy stays in each designated subtorus. The top cell of each `T_j` supplies a suspension top cell, and there is no six-dimensional fibre cell in `T_j`. Consequently the inclusion on the mapping-torus chains has fibre component zero and suspension component (4.2).

This degree-six marking also agrees with the marked complement map (2.1). The map of this mapping torus into the graph bundle traverses the two inverse edge cylinders; on each segment its fibre support is the flatly transported five-dimensional subtorus. Its edge coordinates are exactly `-W_2W_0x_j` and `-W_0x_j`. Its possible six-dimensional fibre coordinate is measured by the flat fibre volume form

\[
\omega=dx_0\wedge\cdots\wedge dx_5.
\]

Both finite monodromies have determinant one, so this form agrees under every transport. On the product cells of the supplied graph model it evaluates as one on the marked fibre top cell and zero on an edge times a five-cell. Its integral on the displayed geometric mapping torus is zero, since the fibre tangent space there has dimension five. Thus the fibre coordinate is zero. More concretely, the graph Wang sequence in degree six has fibre summand `Z` and quotient the edge invariant lattice; invariant five-subtori provide integral lifts of a basis of that quotient. The volume functional is one on the fibre generator and zero on those lifts, so it determines this coordinate integrally. This proves the required agreement, not just equality after tensoring with the rationals.

Now compute the cusp image of this specific cycle. At `C(q)=0`, use the toric moment model of P1.11. Write a nearby point as `(theta,b)` with `y=G b`, and write `t=arg(q)/(2 pi)`. Over the cell `P_v`, the full boundary forgetful map is

\[
[\theta,b,t]\longmapsto [G b,\theta+t(b-v)].
\tag{4.3}
\]

This is obtained by taking arguments of the component coordinate `z q^{-v}`. It is also checked directly from the input's monomial marking. On an overlap the two angular expressions differ by `t(w-v)`, an element of the subtorus collapsed on that face. Replacing `b` by `b+nu` replaces `v` by `v+nu`, leaving the expression unchanged. At `t=1` it agrees with the value at `t=0` after the mapping-torus identification `(theta,b,1)~(theta+b,b,0)`, since `v` is integral. Thus (4.3) is an actual well-defined map of the marked boundary, with fibre restriction equal to `kappa`.

The base coordinate in (4.3) is independent of `t`. On the mapping torus of `T_j`, the image lies over the two-dimensional base subtorus `b_j=0`. Its angular fibres have dimension at most three. After subdivision by the finite moment-cell stratification, this image is a finite stratified cell space of real dimension at most five. Its sixth homology is zero. Therefore its fundamental six-cycle maps to zero in `H_6(C)`. The stratified deformation in P1.11 transports the entire marked boundary forgetful map, so the same conclusion holds for the original bounded period matrix. Together with (4.2), this gives

\[
h_6=0.
\tag{4.4}
\]

The map (4.3), the specific cycles (4.2), and the complement volume coordinate supply the local and global comparison required in this degree.

## 5. Local relative duality and the secondary class

Apply Hatcher Theorem 3.43 to the actual smooth cap `W`, taking the cohomology-side relative subset empty and the homology-side relative subset its entire boundary. Cap product with its relative orientation class gives the integral isomorphisms

\[
H_i(W,B;\mathbb Z)\cong H^{8-i}(W;\mathbb Z)
\cong\operatorname{Hom}(H_{8-i}(C),\mathbb Z).
\tag{5.1}
\]

The last equality is the integral universal coefficient sequence with the `Ext` terms zero because all the absolute groups of `C` are free. Thus all relative groups are free, and their ranks are

\[
(0,0,1,3,10,9,9,3,1).
\tag{5.2}
\]

This is an application to the local cap only.

The collapse is onto `H_5(C)`, so the actual boundary map is onto there. The pair exact sequence consequently contains an injection

\[
0\longrightarrow H_5(W,B)\longrightarrow H_4(B)
\longrightarrow H_4(C).
\]

Its first group has rank 9 by (5.1), and `H_4(B)` is free of rank 18 by Section 3. Hence the actual boundary image in degree four has rank 9. It contains the primitive rank-nine collapse image. It is therefore exactly that image. In (3.1),

\[
h_4(S^B_3)\subset\operatorname{im}\kappa_4.
\tag{5.3}
\]

For degrees 2, 3, and 5 the same inclusion for `h_k` follows directly from surjectivity of the collapse in that degree.

Use the primitive inverse of the collapse on `F^B_k` to replace each free suspension generator, in degrees 2 through 5, by

\[
s'=s-\iota_k h_k(s).
\tag{5.4}
\]

These are integral automorphisms of the reduced boundary complex, with inverses obtained by changing the minus sign to plus. They fix all fibre generators. They make the cap map vanish on these suspension cycles. They also preserve the complement map up to a specified integral chain homotopy: its difference is `-J_k iota_k h_k`, and (2.6) supplies the homotopy `-F_k iota_k h_k`. This homotopy is zero on the fibre generators, including `z`, so its composition with the remaining boundary differential is zero. Thus it has exactly the required chain-homotopy identity, with no residual term.

Likewise replace `t` by `t-iota_4 w`. Its differential remains `2z`, and the complement map changes by the boundary `-d_Y F_4 iota_4 w`. After these changes, (3.1) has only the extra value

\[
t\longmapsto a e.
\tag{5.5}
\]

The values in degrees one and six remain zero by (4.1) and (4.4), and the target groups above degree six are zero.

Now form the actual relative cone `Cone(B -> C)`. Cancel the identity fibre-to-collapse-image pairs. The middle part remaining in degrees five and four is exactly

\[
\mathbb Z\langle\widehat t\rangle
\xrightarrow{\ (a,-2)^t\ }
\mathbb Z\langle e\rangle\oplus\mathbb Z\langle\widehat z\rangle.
\tag{5.6}
\]

The other degree-four cycles are the nine free suspended cycles coming from `S^B_2`. The torsion subgroup of the cokernel in (5.6) has order `gcd(a,2)`. Equation (5.1) says that this cokernel contributes no torsion. Therefore `a` is odd.

A chain homotopy on the cap map, with its only extra value on `z` in degree three, changes `a` by an arbitrary multiple of two. The integer `(a-1)/2` therefore changes (5.5) to

\[
t\longmapsto e.
\tag{5.7}
\]

This is the full secondary attaching datum required for the global calculation. The exact relative middle relation is now `e-2 zhat=0`; the absolute extra generator maps to twice the corresponding free relative generator, up to the orientation sign in the chosen relative basis.

For comparison, the all-zero suspension map gives the explicit middle differential `(0,-2)^t` in place of `(1,-2)^t`. Its relative fourth homology contains `Z/2`. The map from the two complexes to their relative fourth homology therefore distinguishes them: one has this torsion subgroup and the actual local duality group is free. This is the precise omitted term and the exact integral obstruction to erasing it.

All chain homotopies used here produce explicit cone isomorphisms. For two actual chain maps with `F'-F=dK+Kd`, the map

\[
\operatorname{Cone}(F)\longrightarrow\operatorname{Cone}(F'),
\qquad (x,b)\longmapsto(x-Kb,b)
\tag{5.8}
\]

is an integral chain isomorphism; its inverse uses `+Kb`. Direct multiplication with `d(x,b)=(dx+Fb,-db)` verifies (5.8). Boundary basis changes use the corresponding block diagonal source changes in the cone. Contracted unit blocks can then be reinserted. Consequently these operations give the comparison from the actual gluing complex to the displayed full-size normal form, not merely an agreement of some homology ranks.

## 6. The resulting full integral complex

Return from the reduced boundary basis to the original exterior basis using the Smith changes. Let `j` be the Smith slot of the factor 2 of `T_3`; in the fresh decomposition it is zero-based slot 10. Let `e` be the last cap basis vector in degree four. The normalized cusp map is

\[
j_{C,k}(f,x)=K_k f+H_{k-1}x,
\]

where

\[
H_3=e\,\bigl(V_3^{-1}[j,:]\bigr),\qquad H_q=0\ (q\ne3).
\tag{6.1}
\]

The formula for `K_k` is in Section 3. In particular `K_k T_k=0` exactly. Equation (6.1) is a map on every chain group, not only on invariant suspension cycles. It sends the Smith suspension generator with differential `2z` to `e`, while vanishing on the free suspension cycles. This distinction between a noncycle in the boundary chain complex and a free suspension homology class is recorded by their explicit differential `t -> 2z`.

The full complex has

\[
\mathcal M_k=Y_k\oplus H_k(C)\oplus B_{k-1},
\]

and differential

\[
d_{\mathcal M,k}=
\begin{pmatrix}
d_{Y,k}&0&j_{Y,k-1}\\
0&0&-j_{C,k-1}\\
0&0&-d_{B,k-1}
\end{pmatrix}.
\tag{6.2}
\]

Every entry is now determined by the displayed raw monodromies, the finite norm maps, exterior minors, and the Smith matrices of `T_k`. The normalizing shears and their inverses are integral, the necessary complement homotopies are the matrices (2.6), and the secondary normalization uses the actual cap's free relative homology. Sections 1--5 therefore identify (6.2) with the cellular gluing of the actual manifold through integral chain homotopy equivalences.

Its ranks are obtained before any homology calculation by

\[
\operatorname{rank}\mathcal M_k=
\operatorname{rank}Y_k+c_k+\binom6{k-1}+\binom6{k-2}.
\]

They are

\[
(4,26,87,162,200,156,79,23,3).
\]

The construction directly verifies `d^2=0` in every degree.

## 7. Integral calculation and saved-output verification

The fresh program wrote `fresh_candidate_chain.json`. The word `candidate` in that filename reflects its initial creation before the geometric comparison was completed; Sections 1--6 supply that comparison. The file contains the actual reconstructed differential arrays, the cusp projection and secondary matrices, the integral cycle bases, incoming matrices, cycle-coordinate changes, homology projections, and the complement fibre fillers. It contains no imported matrix from the pre-existing global reconstruction.

For each degree the producer verifies the full Smith identities `U d V=D`, with both basis changes unimodular. On the integral kernel basis `Z`, it forms the incoming matrix from the identity `Z A=d_next` and reduces that matrix integrally. The outcome is:

| degree | chain rank | outgoing rank | cycle rank | incoming rank | homology rank | nonunit incoming factors |
|---:|---:|---:|---:|---:|---:|:---|
| 0 | 4 | 0 | 4 | 3 | 1 | none |
| 1 | 26 | 3 | 23 | 23 | 0 | none |
| 2 | 87 | 23 | 64 | 64 | 0 | none |
| 3 | 162 | 64 | 98 | 98 | 0 | none |
| 4 | 200 | 98 | 102 | 98 | 4 | none |
| 5 | 156 | 98 | 58 | 58 | 0 | none |
| 6 | 79 | 58 | 21 | 21 | 0 | none |
| 7 | 23 | 21 | 2 | 2 | 0 | none |
| 8 | 3 | 2 | 1 | 0 | 1 | none |

The separately written `verify_fresh_saved.py` reads only this newly saved output. It verifies `dZ=0`, that `Z` has the full kernel rank and primitive image, and `Z A=d_next`. It verifies the unimodularity of the stored cycle-coordinate matrix `P` and compares the exact integer image lattices by

\[
\operatorname{HNF}(P A)=\operatorname{HNF}(D').
\]

It also checks the homology projection identities and all four integral filler identities (2.6). Its saved report is `fresh_saved_verification.json`. Thus the table checks the actual integral quotient of cycles by incoming boundaries; it does not infer integral homology from rational ranks.

It follows from (6.2) and this calculation that the actual manifold has

\[
H_k(M;\mathbb Z)=
\begin{cases}
\mathbb Z,&k=0,8,\\
\mathbb Z^4,&k=4,\\
0,&\text{otherwise}.
\end{cases}
\]

The proof uses no duality statement for `M` and does not use P1.12's global homology conclusion. Local duality is used at the exact point (5.1)--(5.7), where it supplies the parity of the noncycle suspension attaching class in the cusp cap.

## 8. Precise status at the freeze

The geometric and integral-chain derivation above is complete relative to the admitted constructive input models. The new arrays have been produced and verified. The receiving proof and its saved matrices have still not been read. Their comparison, including the relationship of chosen bases and the treatment of the degree-six marked cycle, is the next task after the UTC/hash receipt for this file has been saved.

No shared TeX, shared assessment, or another owner's output has been modified. All new programs, arrays, this derivation, and its verification report are in `audit_p119_fresh`.
