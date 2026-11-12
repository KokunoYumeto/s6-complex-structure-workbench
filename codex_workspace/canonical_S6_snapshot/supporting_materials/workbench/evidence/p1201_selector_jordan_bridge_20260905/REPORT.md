# The fifteen $p=1201$ selector rays and the fifteen-dimensional quaternionic Jordan algebra

## Verdict

There is an exact and useful selector-to-Jordan morphism, but it does **not** identify the fifteen selector states with fifteen independent directions of $\operatorname{Herm}_3(\mathbb H)$.  Each marked selector state gives a distinct projective rank-one point in the canonical real-symmetric corner

\[
C_{\mathbb R}:=\iota(\operatorname{Sym}_2(\mathbb R))
=e\operatorname{Herm}_3(\mathbb H)e\cap\operatorname{Herm}_3(\mathbb R),
\qquad e=\operatorname{diag}(1,1,0).
\]

The fifteen points span $C_{\mathbb R}$, so their linear span and their Jordan closure both have real dimension exactly $3$, not $15$.  The full Peirce corner $eJe\cong\operatorname{Herm}_2(\mathbb H)$ has real dimension $6$; $C_{\mathbb R}$ is its proper real-symmetric Jordan subalgebra.  Consequently, the shared number $15$—fifteen marked arithmetic rays and $\dim_{\mathbb R}\operatorname{Herm}_3(\mathbb H)=15$—is not presently a basis, coordinate, orbit, or incidence identification.  What has been proved is more precise: the selector census is a distinguished fifteen-point subset of one projective conic $\mathbb{RP}^1\subset\mathbb{HP}^2$ inside the fifteen-dimensional Jordan algebra.

The phrase “fifteen directions, each containing infinitely many primes” also has an exact meaning.  The complete $p=1201$ census consists of fifteen distinct oriented primitive rays $[r:t]$.  Holding such a ray and its selector marking fixed produces a reduced arithmetic progression of prime labels, and Dirichlet’s theorem gives infinitely many primes on every such marked affine family.  These fifteen families collapse to eleven unordered denominator triples at $p=1201$ and to ten distinct prime progressions after intersection with $p\equiv361\pmod{840}$.

## 1. Typed source object

Fix (p_0=1201).  A marked census state is

\[
s=(\chi,R,h,r,t),\qquad \chi\in\{E,M\},\quad
p_0=4rth-R,\quad \gcd(r,t)=1,
\]

with (r,t,h,R>0), together with the channel gate

\[
\begin{array}{ll}
E:&R\mid 4r^2h+1\quad\Longleftrightarrow\quad R\mid p_0r+t,\\[1mm]
M:&R\mid r+t\quad\Longleftrightarrow\quad R\mid 4r^2h+p_0.
\end{array}
\]

The equality in the exterior row follows without changing coordinates:

\[
p_0r+t=t(4r^2h+1)-Rr.
\]

Put

\[
(u,a,v)=(hr^2,hrt,ht^2),\qquad uv=a^2,qquad R=4a-p_0.
\]

For (E), let (\kappa_E=(p_0r+t)/R); for (M), let (m=(r+t)/R).  The ordered denominator maps are

\[
D_E(s)=(hrt,\;ht\kappa_E,\;p_0hr\kappa_E),
\]

\[
D_M(s)=(hrt,\;p_0hrm,\;p_0htm).
\]

Clearing their full common denominators gives (\sum_i1/D_{\chi,i}=4/p_0).  No unordered quotient is taken at this stage.

The exact reconstructed census is:

| tag | channel | (R) | (h) | ((r,t)) | ((u,a,v)) | hard step (L) | (\Delta h=L/(4rt)) | positive Koide orientation |
|---|:---:|---:|---:|---:|---:|---:|---:|:---:|
| E23a | E | 23 | 17 | (1,18) | (17,306,5508) | 57,960 | 805 | yes |
| M23a | M | 23 | 3 | (6,17) | (108,306,867) | 14,280 | 35 | no |
| M23b | M | 23 | 3 | (17,6) | (867,306,108) | 14,280 | 35 | no |
| E23b | E | 23 | 34 | (9,1) | (2754,306,34) | 57,960 | 1,610 | no |
| M31a | M | 31 | 2 | (1,154) | (2,308,47432) | 9,240 | 15 | yes |
| E31 | E | 31 | 77 | (4,1) | (1232,308,77) | 52,080 | 3,255 | no |
| M31b | M | 31 | 2 | (154,1) | (47432,308,2) | 9,240 | 15 | no |
| M39a | M | 39 | 2 | (1,155) | (2,310,48050) | 26,040 | 42 | yes |
| E39 | E | 39 | 62 | (5,1) | (1550,310,62) | 10,920 | 546 | no |
| M39b | M | 39 | 2 | (155,1) | (48050,310,2) | 26,040 | 42 | no |
| M47a | M | 47 | 1 | (8,39) | (64,312,1521) | 43,680 | 35 | no |
| M47b | M | 47 | 1 | (39,8) | (1521,312,64) | 43,680 | 35 | no |
| E71 | E | 71 | 53 | (1,6) | (53,318,1908) | 59,640 | 2,485 | no |
| E339 | E | 339 | 11 | (35,1) | (13475,385,11) | 94,920 | 678 | no |
| E1043 | E | 1043 | 17 | (33,1) | (18513,561,17) | 1,376,760 | 10,430 | no |

The fifteen ordered rays in the table are pairwise projectively distinct: for every two rows, (rt'-r't\ne0).

## 2. Exact affine meaning of “infinitely many primes”

For an exterior state, retain ((R,r,t)) and set

\[
h_k=h_0+Rk,\qquad p_k=p_0+4rtRk.
\]

Then (p_k=4rth_k-R) and (R\mid4r^2h_k+1).  The progression (p\equiv p_0\pmod{4rtR}) is reduced.  For a middle state, set

\[
h_k=h_0+k,\qquad p_k=p_0+4rtk.
\]

Then (R\mid r+t) is unchanged and (p\equiv p_0\pmod{4rt}) is reduced.  Intersecting either family with the hard class (p\equiv361\pmod{840}) gives

\[
p_n=1201+L_sn,\qquad h_n=h_0+\frac{L_s}{4rt}n,
\]

where

\[
L_s=
\begin{cases}
\operatorname{lcm}(4rtR,840),&\chi=E,\\
\operatorname{lcm}(4rt,840),&\chi=M.
\end{cases}
\]

Every displayed residue (1201\pmod{L_s}) is reduced; Dirichlet therefore supplies infinitely many prime (p_n), and the same ordered unit-fraction formula applies at each prime.  The projective matrix direction remains ([r^2:rt:t^2]), while its integral scale changes from (h_0) to (h_n).

This produces fifteen **marked ray families**, not fifteen disjoint sets of primes.  Four middle reversal pairs share their (L_s), and E23a and E23b both have (L_s=57960).  Hence:

\[
15\ \text{marked oriented rays}
\longrightarrow 11\ \text{unordered base triples}
\longrightarrow 10\ \text{hard-class progressions}.
\]

The two arrows are different quotients.  The first forgets middle orientation.  The second additionally identifies the two distinct exterior rays E23a and E23b because their least hard-preserving prime increments happen to agree.

## 3. The exact selector-to-Koide map

Define

\[
\Gamma(s)=
\begin{pmatrix}u&a\\a&v\end{pmatrix}
=h\binom r t(r\ t).
\]

It is positive semidefinite of ordinary rank one, and its Smith normal form is (\operatorname{diag}(h,0)).  Thus the unprojectivized matrix retains the scale (h).  Define Lorentz coordinates

\[
\mathcal L(\Gamma)=
\left(H,X,Y\right)
=\left(\frac{u+v}{2},a,\frac{u-v}{2}\right).
\]

They satisfy

\[
H^2-X^2-Y^2=uv-a^2=0.
\]

Let

\[
F(q_1,q_2,q_3)=
\left(
\frac{q_1+q_2+q_3}{\sqrt3},
\frac{q_1-q_3}{\sqrt2},
\frac{q_1+q_3-2q_2}{\sqrt6}
\right).
\]

This is an orthogonal map, and for

\[
Q_K(q)=\frac23(q_1+q_2+q_3)^2-(q_1^2+q_2^2+q_3^2)
\]

one has (Q_K(q)=H^2-X^2-Y^2) whenever (F(q)=(H,X,Y)).  Therefore the exact Koide vector is

\[
\begin{aligned}
q_1&=\frac{u+v}{2\sqrt3}+\frac a{\sqrt2}+\frac{u-v}{2\sqrt6},\\
q_2&=\frac{u+v}{2\sqrt3}-\frac{u-v}{\sqrt6},\\
q_3&=\frac{u+v}{2\sqrt3}-\frac a{\sqrt2}+\frac{u-v}{2\sqrt6},
\end{aligned}
\]

and (Q_K(q)=0) exactly.  This is a coefficient-preserving map over (\mathbb Q(\sqrt2,\sqrt3)), not a numerical fit.  In the retained orientation, all three (q_i) are positive exactly for E23a, M31a, and M39a.  Positivity does not descend through the unordered middle quotient: the reversals M31b and M39b are not in that chamber.

## 4. The exact embedding into $\operatorname{Herm}_3(\mathbb H)$

Let $J=\operatorname{Herm}_3(\mathbb H)$ with Jordan product $A\circ B=(AB+BA)/2$.  Define

\[
\iota:\operatorname{Sym}_2(\mathbb R)\hookrightarrow J,
\qquad
\iota\begin{pmatrix}u&a\\a&v\end{pmatrix}
=
\begin{pmatrix}
u&a&0\\
a&v&0\\
0&0&0
\end{pmatrix}.
\]

This is an injective real-linear Jordan homomorphism because direct block multiplication gives

\[
\iota(A\circ B)=\iota(A)\circ\iota(B).
\]

Its image is the real-symmetric Jordan corner

\[
C_{\mathbb R}:=\iota(\operatorname{Sym}_2(\mathbb R))
=eJe\cap\operatorname{Herm}_3(\mathbb R),
\qquad e=\operatorname{diag}(1,1,0).
\]

It has real dimension $3$.  The full Peirce corner $eJe\cong
\operatorname{Herm}_2(\mathbb H)$ has real dimension $6$, so the two
corners are not being identified.

It preserves trace, the trace pairing, positivity, and ordinary matrix rank.  In the Moore-coordinate convention

\[
\begin{pmatrix}
d_1&q_3&\bar q_2\\
\bar q_3&d_2&q_1\\
q_2&\bar q_1&d_3
\end{pmatrix},
\]

the selector image has `$d_1=u,d_2=v,d_3=0$`, `$q_3=a\in\mathbb R$`, and `$q_1=q_2=0$`.  Thus its full fifteen-coordinate vector is explicitly specified, with exactly three nonzero real coordinates and twelve zero coordinates; the Moore cubic is zero.

After projectivizing the scale, define

\[
P_{r,t}=\frac1{r^2+t^2}
\begin{pmatrix}
r^2&rt&0\\rt&t^2&0\\0&0&0
\end{pmatrix}.
\]

Then $P_{r,t}^2=P_{r,t}$ and $\operatorname{tr}P_{r,t}=1$.  It is the rank-one quaternionic projector associated to the line $[r:t:0]_{\mathbb H}$.  Hence the composition is the explicit injection

\[
\Sigma_{1201}\longrightarrow\mathbb{RP}^1\longrightarrow\mathbb{HP}^2,
\qquad
s\longmapsto[r:t]\longmapsto[r:t:0]_{\mathbb H}.
\]

For the fixed base prime, the unprojectivized image retains every marking.  From its entries recover $(u,a,v)$, then

\[
h=\gcd(u,a,v),\quad r=\sqrt{u/h},\quad t=\sqrt{v/h},\quad
R=4a-1201,\quad j=(R-3)/4.
\]

The channel is recovered by testing the two gates.  They cannot overlap on this census: overlap would imply $R\mid1200$, whereas none of $23,31,39,47,71,339,1043$ divides $1200$.  This inverse is specific to the fixed-$p$, marked census.  Projectivization loses $h$, and without retaining $p$, the formula $R=4a-p$ is unavailable.

## 5. Exact span and Jordan closure

In the coordinate basis

\[
\begin{pmatrix}x&y\\y&z\end{pmatrix}\longleftrightarrow(x,y,z)
\]

of $C_{\mathbb R}\cong\operatorname{Sym}_2(\mathbb R)$, the projective selector vector is

\[
g_{r,t}=(r^2,rt,t^2).
\]

All images lie in the three-dimensional subspace $C_{\mathbb R}$.  Conversely, the fixed exterior states E31, E39, and E339 have rows

\[
\begin{pmatrix}
16&4&1\\
25&5&1\\
1225&35&1
\end{pmatrix},
\qquad
\det=-930\ne0.
\]

Therefore the fifteen images span $C_{\mathbb R}$ exactly.  Direct block multiplication shows that $C_{\mathbb R}$ is a Jordan subalgebra, so the Jordan subalgebra generated by the fifteen images is contained in $C_{\mathbb R}$; since every Jordan subalgebra is a real linear subspace and the images span $C_{\mathbb R}$, it contains $C_{\mathbb R}$.  Thus

\[
\operatorname{span}_{\mathbb R}\{\iota\Gamma(s):s\in\Sigma_{1201}\}
=\langle\iota\Gamma(\Sigma_{1201})\rangle_{\mathrm{Jordan}}
=C_{\mathbb R},
\]

and both dimensions are $3$.

This is the sharp obstruction to reading the count $15$ as fifteen Jordan-algebra directions.  The map produces fifteen distinct **rays**, but a three-dimensional space contains infinitely many rays.  It does not produce a basis of the fifteen-dimensional algebra.

The state count is not constant even after the hard residue class is fixed.
The independent complete enumerator gives

\[
\begin{array}{c|rrrr}
p&1201&4561&8761&9601\\ \hline
\#E&7&26&16&17\\
\#M&8&28&20&12\\
\#(E\sqcup M)&15&54&36&29\\
\#\{\text{unordered denominator triples}\}&11&40&26&23.
\end{array}
\]

All four primes satisfy \(p\equiv361\pmod{840}\).  Consequently the number
\(15\) is neither a hard-residue-class invariant nor a fixed cardinality of
the selector construction.

## 6. Orientation symmetry and finite-geometry tests

Normalized orientation reversal fixes all seven exterior states and exchanges the four middle pairs.  Consequently its cycle type is

\[
1^7,2^4.
\]

The transvection

\[
\tau(x_1,x_2,x_3,x_4)=(x_1+x_2,x_2,x_3,x_4)
\]

on (\mathbb F_2^4\setminus\{0\}) has the same cycle type.  One explicit equivariant bijection is

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
s&E23a&E23b&E31&E39&E71&E339&E1043&M23a&M23b&M31a&M31b&M39a&M39b&M47a&M47b\\\hline
\phi(s)&1&4&5&8&9&12&13&2&3&6&7&10&11&14&15.
\end{array}
\]

Here integers (1,\ldots,15) encode their four binary coordinates, with (x_1) the low bit.  The displayed map proves an equivalence of (C_2)-sets and nothing stronger.  It is highly noncanonical: the automorphism group of a set with cycle type (1^7 2^4) has order

\[
7!\,2^4\,4!=1,935,360.
\]

There is also a sharp incidence obstruction.  The selector images lie on the nonsingular conic (xz-y^2=0) in (\mathbb P^2(\mathbb R)), so no three distinct images are collinear.  The projective geometry on (\mathbb F_2^4\setminus\{0\}=PG(3,2)) has (35) three-point lines.  No bijection can preserve those two natural collinearity relations.

The normalized reversal is not induced by a linear or Jordan automorphism on the canonical real-symmetric corner either.  It fixes E31, E39, and E339, whose images span (C_{\mathbb R}); any linear map fixing those three vectors is the identity on (C_{\mathbb R}).  But reversal must exchange each nonidentical middle pair.  This contradiction rules out such a realization.

The other proposed finite models fail earlier:

- type (A_3) has (12) oriented roots and (6) unoriented root lines;
- its three nonzero minuscule-weight orbits have (4+6+4=14) elements;
- adjoining a zero vector to obtain (15) introduces a distinguished fixed element for which the selector census has no canonical counterpart;
- an arbitrary (15)-vector basis of (J) has the right count, but the canonical selector map has rank (3);
- the rank-one idempotents of (J) form the continuum (\mathbb{HP}^2), of real dimension (8), and the selector images lie in the proper submanifold (\mathbb{RP}^1\subset\mathbb{HP}^2).

## 7. What survives each quotient

| operation | retained | lost | resulting count |
|---|---|---|---:|
| unprojectivized (\iota\Gamma), fixed (p=1201) | (u,a,v,h,r,t,R,j), and channel by exclusive gate | no selector marking in this fixed census | 15 |
| projectivization (\Gamma\mapsto P_{r,t}) | oriented primitive ray ([r:t]) | (h,p,R,j), affine position | 15 |
| unordered denominator triple | solution denominators as a multiset | middle orientation; hence Koide chamber may change | 11 |
| hard-prime progression (1201\bmod L_s) | allowable prime labels | ray, channel, scale formula unless tag retained | 10 |
| (C_2)-set comparison with (\mathbb F_2^4\setminus0) | only reversal cycle type (1^7 2^4) | arithmetic, conic incidence, Jordan product | 15 |

## 8. Strongest next test

The next test should not seek another equality of counts.  It should ask whether the full selector data, as $p$ varies, canonically leaves the fixed real-symmetric Jordan corner inside $J$.  A falsifiable construction is:

1. keep the marked rank-one matrix (\Gamma(s)) and its residual/channel data;
2. define, from those arithmetic markings rather than from an arbitrary choice, an element (g_s\) of an explicitly named subgroup of the quaternionic structure group;
3. form (g_s\iota(\Gamma(s))g_s^*);
4. compute the real span and Jordan closure over a complete, independently verified multi-prime census;
5. require the construction to be equivariant under the actual selector involutions and to recover the denominator map from the Jordan coordinates.

If the resulting span remains in one common $3$-dimensional real-symmetric Jordan corner, the fifteen-dimensional interpretation is obstructed.  If the markings canonically move the rays among enough distinct conjugate corners and the closure becomes all of $J$, that would constitute a genuine higher-rung bridge.  No such marking-to-conjugation map is presently defined in the supplied corpus.

## 9. Reproducibility and source boundary

The standard-library certificate `verify_fifteen_bridge.py` reconstructs all fifteen states and checks:

1. every selector gate, primitive factorization, ordered denominator identity, and affine hard-class family;
2. the counts (15\to11\to10) and the three positive Koide orientations;
3. pairwise distinctness of all fifteen projective rays;
4. exact rank (3) in the full fifteen-coordinate (\operatorname{Herm}_3(\mathbb H)) model;
5. projector idempotence and the witness determinant (-930);
6. absence of collinear triples among the fifteen conic points;
7. the (1^7 2^4) reversal/transvection comparison and one explicit equivariant bijection.

The independent upstream family checker also runs successfully and reports

```text
PASS
states=15 canonical_triples=11 hard_progressions=10
results_sha256=828c13a517ddb4a34f1ac55e8e090bffdb63a341568adb01942bf366d8343799
```

Primary local sources, fixed for this audit by SHA-256, are:

- `erdos_straus_koide_s6_bridge.tex`: `505919728FE4062F271D425FBE964B2176C1A266391AD426838F3CB4A14A3D7A`;
- `erdos_straus_selector_crosswalk.tex`: `A7B6B48181F60120FD4816A79857B5F09B5426FA490AADFC18D29943921D8040`;
- `Koide_ES_exact_crosswalk_background.tex`: `73C79E63F8A89D4536D98AEE9CDE2977216989431ED9B9336317ECA3785A3D66`;
- quaternionic `model.tex`: `9E52D977A5D6C480D247553759ACABAA6AE90A0A54D42DF457AB7ECA0E999822`;
- `20260905_P1201_AFFINE_SELECTOR_FAMILIES.md`: `A6C78E8FFDA5CE02B476C79E2EECE7FF26777419AFCD655FCFDACBFCB6671091`;
- upstream checker: `B744ED96B5C9495F7CBC49F5199FE36E04E31FEBF61CFD8445B89C7D6CEAF78D`.

The theorem proved here is internal to those supplied definitions.  No unfinished web-session assertion is used as a premise, and no historical-novelty claim is made.
