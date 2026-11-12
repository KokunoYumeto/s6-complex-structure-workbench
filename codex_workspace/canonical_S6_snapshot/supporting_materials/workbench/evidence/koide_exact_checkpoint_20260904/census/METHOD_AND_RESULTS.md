# Exact fast enumeration and finite discrepancy evidence for the Koide reduced-root count

## 1. Scope

This directory is an independent, read-only audit of the reduced-root count

\[
R(X)=\#\left\{(a,q,n)\in\mathbb Z^3:
\begin{array}{l}
a^2-3q^2-18n^2=-2,\\
a>0,\ q\geq0,\ n\geq0,\ a+4n>q,\\
4a+17n\leq X
\end{array}\right\}.
\]

It preserves the canonical inverse coordinates

\[
(x,y,z)=\left(\frac{a+4n-q}{2},\frac{a+4n+q}{2},4a+17n\right)
\]

and rechecks

\[
\Delta(x,y,z)=4(xy+xz+yz)-(x^2+y^2+z^2)=-1,
\quad 0<x\leq y\leq z,
\quad z\geq4(x+y)
\]

for every emitted point.  The canonical files were not edited.

The computation supplies finite evidence through every integer `1 <= X <= 100,000,000`.  It does **not** prove, disprove, fit, or infer an asymptotic discrepancy law.  In particular, survival of any finite envelope below is not evidence that the same constant works for larger `X`.

## 2. Fixed-`n` Pell decomposition

For fixed `n`, retain the original `a`, `q`, and `n` and put

\[
N_n:=18n^2-2=2(3n-1)(3n+1).
\]

The ternary equation is exactly

\[
a^2-3q^2=N_n. \tag{2.1}
\]

For `n >= 1`, `N_n>0`.  Therefore every solution with `a>0` and `q>=0` satisfies

\[
a^2>3q^2,\qquad a>\sqrt3q>q
\]

when `q>0`, and `a>q` also holds when `q=0`.  Thus the strict chamber inequality `a+4n>q` is automatic for `n>=1`; it is nevertheless checked point by point.  The height condition is the exact upper bound

\[
a\leq A_n(X):=\left\lfloor\frac{X-17n}{4}\right\rfloor. \tag{2.2}
\]

Equation (2.1) also forces

\[
a\geq\left\lceil\sqrt{18n^2-2}\right\rceil.
\]

Consequently no solution is omitted when the `n` loop stops after the largest integer satisfying

\[
17n+4\left\lceil\sqrt{18n^2-2}\right\rceil\leq X. \tag{2.3}
\]

The left side of (2.3) is strictly increasing for `n>=1`, so the endpoint is found by exact integer binary search.  At `X=100,000,000` it is `n_max=2,943,725`.

For `n=0`, (2.1) is `a^2-3q^2=-2`.  Its positive solutions are

\[
a+q\sqrt3=(1+\sqrt3)(2+\sqrt3)^k,\qquad k\geq0.
\]

The term `k=0`, `(a,q)=(1,1)`, fails `a>q`; every `k>=1` is retained.  The first retained point is `(a,q,n)=(5,3,0)`, which maps to `(x,y,z)=(1,4,20)`.

For completeness, this classification has an elementary descent.  If `q>=2`, then `a^2=3q^2-2` implies

\[
\frac32q<a<2q.
\]

Thus multiplication by `2-sqrt(3)`, namely `(a,q)->(2a-3q,2q-a)`, has two positive coordinates and a strictly smaller second coordinate.  Descent reaches `q=1`, where the equation forces `a=1`; reversing the steps gives precisely the displayed sequence.

## 3. Exact unit-orbit reduction

Let

\[
\varepsilon=2+\sqrt3,
\qquad
\varepsilon^{-1}=2-\sqrt3.
\]

Multiplication by these norm-one units gives the integer maps

\[
U(a,q)=(2a+3q,a+2q),
\qquad
U^{-1}(a,q)=(2a-3q,2q-a). \tag{3.1}
\]

### Lemma 3.1 — unique positive seed

For `N>0`, every unit orbit of solutions to `a^2-3q^2=N` that contains a point with `a>0`, `q>=0` has exactly one representative `(A,Q)` satisfying

\[
A>2Q\geq0. \tag{3.2}
\]

Every positive-quadrant member of that orbit is `U^k(A,Q)` for a unique `k>=0`.

### Proof

Norm positivity and `a>0` give `a>sqrt(3)|q|`; hence both real embeddings `a+q sqrt(3)` and `a-q sqrt(3)` are positive.  If `q<0`, repeated multiplication by `epsilon` eventually makes the coefficient of `sqrt(3)` nonnegative, while total positivity is preserved.

Now suppose `a>0`, `q>=0`.  If `a<=2q`, then `a>sqrt(3)q` and (3.1) give

\[
2a-3q>(2\sqrt3-3)q\geq0,
\qquad
2q-a\geq0.
\]

The first coordinate is strictly positive, including when `q=0` (where the reduction condition cannot hold).  Moreover

\[
2a-3q<a
\]

because `a<3q`.  Thus each permitted inverse step preserves the nonnegative quadrant, preserves the norm exactly, and strictly decreases the positive integer first coordinate.  The descent terminates at a point satisfying (3.2).

At a point satisfying (3.2), the second coordinate of `U^{-1}(A,Q)` is `2Q-A<0`, so no further inverse step stays in the nonnegative quadrant.  Conversely, for every `k>=1`, the point `U^k(A,Q)` has a nonnegative predecessor; indeed, if `(a_1,q_1)=U(a,q)`, then `2q_1-a_1=q>=0`.  Hence no forward iterate with `k>=1` can satisfy the terminal property (3.2).  Two terminal representatives in one orbit would differ by a nonzero power of `U`, contradicting this observation.  This proves existence and uniqueness. ∎

The same argument proves that all units of `Z[sqrt(3)]` are `+/- epsilon^k`.  A norm-minus-one unit is impossible because `A^2-3Q^2=-1` would give `A^2=2 (mod 3)`.  After choosing an overall sign and conjugating if necessary, a unit can be placed in the nonnegative quadrant and reduced to (3.2).  If its reduced second coordinate were `Q>=1`, then `A^2=3Q^2+1<=4Q^2`, contradicting `A>2Q`; hence the reduced unit is `(1,0)`, and reversing the unit descent gives the asserted unit group.

Because `Q>=0`, condition (3.2) is also equivalent to choosing the unique totally positive generator `alpha=A+Q sqrt(3)` in the half-open interval

\[
\sqrt N\leq\alpha<\varepsilon\sqrt N.
\]

Indeed, `Q>=0` is equivalent to `alpha>=sqrt(N)`, and after dividing the inequality `alpha<epsilon sqrt(N)` by the positive conjugate and squaring, its boundary is

\[
\frac{A+\sqrt3Q}{A-\sqrt3Q}<\varepsilon^2
=\frac{2+\sqrt3}{2-\sqrt3},
\]

which is equivalent to `A>2Q`.

## 4. Complete enumeration of unit orbits

Let `O=Z[sqrt(3)]`, the full ring of integers of `Q(sqrt(3))`.  Its discriminant is `12`.  Minkowski's bound says that every ideal class contains an integral ideal of norm at most

\[
\frac{2!}{2^2}\sqrt{12}=\sqrt3<2.
\]

The norm is a positive integer, so that ideal has norm `1`.  Hence every ideal class is principal and `O` has class number one.

For a positive integer `N`, define

\[
\mathcal P(N)=\left\{(C,D,E):
C,D>0,\ C^2D=N,\ 0\leq E<D,\ E^2\equiv3\pmod D\right\}. \tag{4.1}
\]

Each element defines the Hermite-normal-form lattice

\[
I_{C,D,E}=C\left(D\mathbb Z+(E+\sqrt3)\mathbb Z\right). \tag{4.2}
\]

It is an ideal: multiplication of its two displayed generators by `sqrt(3)` stays in the lattice because

\[
\sqrt3D=D(E+\sqrt3)-DE,
\]

and

\[
\sqrt3(E+\sqrt3)=E(E+\sqrt3)+(3-E^2),
\]

with `D | (E^2-3)`.  Its index, hence its norm, is `C^2D=N`.

Conversely, the Hermite normal form of an integral ideal of norm `N`, after extracting the common content `C`, has exactly the form (4.2); closure under multiplication by `sqrt(3)` forces `E^2=3 (mod D)`, and its determinant forces `C^2D=N`.  Thus (4.1) enumerates all integral ideals of norm `N` exactly once.

For a solution `alpha=a+q sqrt(3)` of norm `N`, set

\[
C=\gcd(a,q),\quad A=a/C,\quad B=q/C,\quad D=N/C^2.
\]

If `D=1`, take `E=0`.  If `D>1`, then `gcd(B,D)=1`: a prime dividing both would also divide `A^2=D+3B^2`, contrary to `gcd(A,B)=1`.  Therefore

\[
E\equiv AB^{-1}\pmod D
\]

is defined and satisfies `E^2=3 (mod D)`.  The element `alpha` lies in `I_{C,D,E}` because `A-BE` is divisible by `D`.  The principal ideal `(alpha)` and `I_{C,D,E}` have the same norm `N`, so they are equal.  This is the inverse of (4.2).

Every ideal in (4.2) is principal.  A generator cannot have norm `-N_n`, because `N_n=1 (mod 3)` and

\[
r^2-3s^2=-N_n
\]

would give `r^2=2 (mod 3)`, which is impossible.  Its norm is therefore `+N_n`.  Generators differ by the units `+/- epsilon^k`; changing the overall sign and applying Lemma 3.1 gives one and only one seed satisfying (3.2).  Hence the ideal/HNF list is a complete, duplicate-free list of positive unit orbits for each `n>=1`.

### Exact principal-generator calculation

The implementation obtains a generator of (4.2) by the specialized Lagrange–Mollin–Matthews `P,Q` continued fraction.  For every `C^2D=N` and every root `E^2=3 (mod D)`, replace `E` by its symmetric residue and start

\[
P_0=E,\qquad Q_0=D.
\]

All recurrences are integral.  In the signed `P,Q` convention used by LMM, define

\[
c_i=\operatorname{floor\_div}(P_i+\lfloor\sqrt3\rfloor,Q_i)
=\operatorname{floor\_div}(P_i+1,Q_i),
\quad
P_{i+1}=c_iQ_i-P_i,
\quad
Q_{i+1}=\frac{3-P_{i+1}^2}{Q_i}. \tag{4.3}
\]

Thus (4.3) is computed exactly as Python integer division `(P_i+1)//Q_i`, including for signed `Q_i`; no numerical square root occurs.  With

\[
B_{-2}=1,\ B_{-1}=0,\qquad
G_{-2}=-P_0,\ G_{-1}=Q_0,
\]

and

\[
B_i=c_iB_{i-1}+B_{i-2},
\qquad
G_i=c_iG_{i-1}+G_{i-2}, \tag{4.4}
\]

direct induction gives the exact invariant

\[
G_i^2-3B_i^2=(-1)^{i+1}Q_0Q_{i+1}. \tag{4.5}
\]

The complete-quotient states `(P_i,Q_i)` are precisely the standard continued-fraction reductions of the ideal in (4.2).  Reduction is finite up to a repeated state, and an ideal is principal exactly when its cycle reaches `|Q_i|=1`.  At that point (4.5) makes `(G_{i-1},B_{i-1})` a generator of norm `+D` or `-D`.  The negative case would require a norm-minus-one unit to reverse the sign; here `r^2-3s^2=-1` is impossible modulo `3`, while principality and the preceding norm argument guarantee the positive case.  Multiplication by `C` gives a generator of norm `N`.  The implementation records visited integer `(P_i,Q_i)` states, stops on the first repeat, verifies the returned norm explicitly, and then applies the integral seed descent of Lemma 3.1.

The modular roots in (4.1) are also exact.  Prime-power roots are constructed by Tonelli–Shanks and Hensel lifting, then joined by the Chinese remainder theorem.  Every root is re-squared modulo `D`.  The special local facts used by the code are

- modulo `2^e`, a root exists only for `e<=1`;
- modulo `3^e`, a root exists only for `e<=1`;
- for odd `p` not equal to `3`, `3` is a square exactly when `p=1` or `11 (mod 12)`.

### Independent orbit-count identity

Let `chi_12` be the primitive quadratic character modulo `12`, and set

\[
\rho(m)=\sum_{d\mid m}\chi_{12}(d).
\]

The prime-power ideal count above gives

\[
\#\mathcal P(m)=\rho(m):
\]

the local factor is `e+1` for a split prime to exponent `e`, `1` for a ramified prime, and `1` or `0` for an inert prime according as `e` is even or odd.  Since `gcd(3n-1,3n+1)` divides `2` and the `2`-local factor is always `1`,

\[
\rho(N_n)=\rho(3n-1)\rho(3n+1). \tag{4.6}
\]

For every one of the `2,943,725` positive values of `n` in the final run, the program independently checked that (i) the number of distinct reduced LMM seeds equals `rho(N_n)` and (ii) it equals the product in (4.6).

## 5. Algorithm and complexity

The exact algorithm is:

1. Find `n_max` from (2.3) by integer binary search.
2. Build a compact `uint32` smallest-prime-factor table through `3*n_max+1`.
3. For each `1<=n<=n_max`, factor `N_n` by separately factoring `3n-1` and `3n+1` in the table and adjoining the leading factor `2`.
4. Enumerate every `C^2D=N_n` for which `E^2=3 (mod D)` is locally possible, construct every such `E` by exact prime-power lifting and CRT, and run the integer `P,Q` recurrence (4.3)–(4.5).
5. Canonicalize each generator by Lemma 3.1, deduplicate the HNF descriptions to a set of seeds, and check its size against both sides of (4.6).
6. From each seed, iterate (3.1) until (2.2) fails.  Reconstruct `(x,y,z)` and recheck every equation, map, parity, ordering, wall, and height inequality using Python integers.
7. Stream all six coordinates to deterministic gzip.  Retain only an 8-byte unsigned height per root for sorting and residual analysis.

Let `Y=n_max=O(X)`.  The sieve takes `O(Y log log Y)` elementary operations and `O(Y)` compact memory.  For each `n`, the number of HNF starts is `rho(N_n)<=tau(N_n)=X^{o(1)}` by the classical divisor bound, and continued-fraction reduction in the fixed real quadratic field takes `O(log N_n)` steps per start.  Unit iteration costs one exact constant-size recurrence per emitted point.  Thus the arithmetic work is

\[
X^{1+o(1)}+O(R(X))
\]

integer operations, before the optional `O(R(X) log R(X))` height sort.  This is unconditionally subquadratic and replaces the former two-dimensional `(n,a)` scan.  This complexity statement uses no conjectural discrepancy estimate and no empirical fit.

At `X=100,000,000`, the measured main structures were:

| quantity | exact value |
|---|---:|
| `n_max` | 2,943,725 |
| SPF limit | 8,831,176 |
| SPF storage | 35,324,708 bytes |
| emitted roots | 3,536,002 |
| height storage | 28,288,016 bytes |
| canonical unit orbits | 2,327,513 |
| largest orbit count for one `n` | 216 at `n=2,801,231` |
| sieve time | 0.834 s |
| exact enumeration time | 75.749 s |
| total time including gzip, sorting, and discrepancy analysis | 182.292 s |

The compressed coordinate file is 76,560,603 bytes.  The computation did not retain millions of Python coordinate tuples in memory.

## 6. Independent validation

`validation_receipt.json` records a complete PASS for all of the following:

1. A literal exact `(n,a)` scan, structurally identical to the slow reference method but using no NumPy square proposals, gives exactly the same full point set through `X=20,000` (`715` roots).
2. For every `1<=n<=1000`, the canonical unit seeds agree exactly with SymPy's independent public generalized-Pell solver (`780` orbit sets compared).
3. Through `X=200,000`, all `7,109` six-coordinate records `(z,x,y,a,q,n)` agree as a set with the canonical reproduction implementation.
4. All eleven released counts from `10,000` through `200,000` agree, including the additional released `30,000` and `40,000` checkpoints not printed in the TeX table.
5. Every compared point passes the original `Delta=-1` polynomial and both coordinate-map compositions.
6. SHA-256 hashes of the canonical TeX, canonical script, and canonical JSON were identical before and after validation.

After the `10^8` run, `coordinate_audit_receipt.json` independently decompressed all `3,536,002` rows, checked the gzip CRC and hashes, rechecked both equations and coordinate systems for every row, checked monotone grouping by `n`, checked no duplicate `(a,q)` within an `n` group, and recomputed every saved checkpoint count.  It also passed.

## 7. Exact finite results through `10^8`

Write

\[
C_0=\frac9{2\pi^2}\log(2+\sqrt3)\log\left(\frac3{2\sqrt2}\right)
=0.03536204779973185316918386545529207027808544313999\ldots
\]

and `E(X)=R(X)-C_0X`.  Integer counts are exact.  For signs and inequalities involving `C_0`, the script constructs an outward-rounded 90-decimal-digit binary interval for `C_0` and compares rational endpoints by integer cross multiplication.  No tested sign or candidate-bound comparison was interval-ambiguous.

Between consecutive occupied heights, `R(X)` is constant and `E(X)` strictly decreases.  On such a segment,

\[
\frac{E(X)}{\sqrt X}=\frac{R}{\sqrt X}-C_0\sqrt X
\]

also strictly decreases, because its derivative is

\[
-\frac{R}{2X^{3/2}}-\frac{C_0}{2\sqrt X}<0.
\]

Therefore checking both integer endpoints of every constant-count segment proves the reported raw and square-root-normalized extrema over **every** integer in the stated domain, not merely over selected checkpoints.

### Checkpoints

| `X` | `R(X)` | `E(X)` | `E(X)/sqrt(X)` |
|---:|---:|---:|---:|
| 200,000 | 7,109 | +36.590440053629 | +0.081818711287 |
| 250,000 | 8,854 | +13.488050067037 | +0.026976100134 |
| 500,000 | 17,695 | +13.976100134073 | +0.019765190359 |
| 1,000,000 | 35,381 | +18.952200268147 | +0.018952200268 |
| 2,000,000 | 70,637 | -87.095599463706 | -0.061585888992 |
| 5,000,000 | 176,943 | +132.761001340734 | +0.059372524752 |
| 10,000,000 | 353,598 | -22.477997318532 | -0.007108166877 |
| 20,000,000 | 707,458 | +217.044005362937 | +0.048532515010 |
| 50,000,000 | 1,768,230 | +127.610013407342 | +0.018046781166 |
| 100,000,000 | 3,536,002 | -202.779973185317 | -0.020277997319 |

### Extrema over every integer

On `1<=X<=100,000,000`:

- maximum signed residual: `+721.7934249571297569...` at `X=77,078,404`, `R=2,726,372`;
- minimum signed residual and maximum absolute residual: `-812.8300691488068897...` at `X=32,461,294`, `R=1,147,085`;
- maximum `|E(X)|/sqrt(X)`: `0.18515707693408214138...` at `X=160`, `R=8`;
- at the maximum raw positive residual, `E/(sqrt(X) log(2X))=0.004360688053921...`;
- at the maximum raw negative magnitude, `E/(sqrt(X) log(2X))=-0.007930798563363...`.

On the tail `10,000<=X<=100,000,000`:

- maximum `|E(X)|/sqrt(X)`: `0.17140019280881455973...` at `X=867,240`, `R=30,827`, with `E=+159.6176661605476576...`;
- the corresponding log-normalized value is `E/(sqrt(X) log(2X))=0.011930780268556...`.

The tail maximum occurs at the exact root

\[
(a,q,n)=(199997,115061,3956),
\qquad
(x,y,z)=(50380,165441,867240).
\]

The raw negative extremum is in an empty-height interval: the preceding occupied height is `32,461,199`, and the next is `32,461,295` (with two roots).  Thus no nonexistent root is attached to the count at `X=32,461,294`.

### Explicit tests of stated square-root constants

For the finite tail `10,000<=X<=100,000,000`, the candidate assertion is

\[
|E(X)|\leq K\sqrt X. \tag{7.1}
\]

The first certified counterexample, when one exists, is:

| rational `K` | decimal | first counterexample `(X,R(X))` | `E(X)` | `|E|/sqrt(X)` |
|---:|---:|---:|---:|---:|
| `4/25` | 0.160 | `(837185,29752)` | +147.424012781489 | 0.161122988675 |
| `17/100` | 0.170 | `(857640,30486)` | +158.093325037973 | 0.170710808662 |
| `171/1000` | 0.171 | `(867216,30826)` | +159.466355307741 | 0.171240082080 |
| `43/250` | 0.172 | none in tested tail | — | — |
| `7/40` | 0.175 | none in tested tail | — | — |
| `9/50` | 0.180 | none in tested tail | — | — |
| `37/200` | 0.185 | none in tested tail | — | — |
| `19/100` | 0.190 | none in tested tail | — | — |
| `1/5` | 0.200 | none in tested tail | — | — |

The first `K=0.171` counterexample is caused by two roots at height `867,216`:

\[
\begin{aligned}
(a,q,n)&=(174457,97721,9964),
&(x,y,z)&=(58296,156017,867216),\\
(a,q,n)&=(145727,73489,16724),
&(x,y,z)&=(69567,143056,867216).
\end{aligned}
\]

On the full domain starting at `X=1`, `K=0.185` already fails at `X=160`, while `K=0.190` and `K=0.200` have no counterexample through `10^8`.  Again, every “none” is only a bounded finite statement.

### Signs and runs

On `1<=X<=100,000,000`, exact interval-certified comparison gives:

- 12,917 maximal same-sign runs and 12,916 sign changes;
- longest positive run: `[70,376,904,83,300,605]`, length `12,923,702`;
- longest negative run: `[29,526,599,37,436,784]`, length `7,910,186`.

The main JSON contains every run endpoint.  Long runs are recorded as finite behavior only; they do not imply eventual bias.

### Height-shell multiplicities

The `3,536,002` roots occupy `2,472,015` distinct heights.  The largest shell multiplicity is `35`, at `z=92,923,120`.  The largest gap between consecutive occupied heights is `564`, from `71,586,276` to `71,586,840`.  The complete multiplicity histogram is in the main JSON, and all 35 original-coordinate roots on the maximal shell are in the coordinate file.

## 8. Reproduction and artifact manifest

From this directory:

```powershell
python validate_fast_enum.py --receipt validation_receipt.json
python koide_fast_enum.py --max-height 100000000 --output-directory final_100000000
python audit_coordinate_file.py final_100000000/koide_roots_through_100000000.csv.gz final_100000000/koide_discrepancy_100000000.json final_100000000/coordinate_audit_receipt.json
python supplemental_candidate_analysis.py final_100000000/koide_roots_through_100000000.csv.gz final_100000000/koide_discrepancy_100000000.json final_100000000/fine_candidate_analysis.json
```

SHA-256 receipts:

| artifact | SHA-256 |
|---|---|
| `koide_fast_enum.py` | `dddb73b828b63be08e2ff0b5346edb3231662005f83d5b2448c06fef6ba31017` |
| `validate_fast_enum.py` | `77b7718c2e964384a04cb3efacba1e3d98ffb6d13a43a5ffc7f684371c1ce0da` |
| `validation_receipt.json` | `da1f4bd39ae91df44e8da05f888883b50d9c221945317aacccca79fd2e6c8cf7` |
| `final_100000000/koide_discrepancy_100000000.json` | `da92f0866074e530b8174a48915caa0f65cd4cd8957e209306adc200739d1961` |
| `final_100000000/koide_roots_through_100000000.csv.gz` | `dfc313492aedb396dcfa10520bfefc699ba601357bc9933d921dfa3884310bd4` |
| `final_100000000/coordinate_audit_receipt.json` | `3010363108e7b460b7331a92f3263bbd77992aedfc3064973750e16d707da80f` |
| `final_100000000/fine_candidate_analysis.json` | `abd1b2f29a797a0ec9771d4cbd064d4a44c329e4ba5b940021557e91a727fbb3` |
| `final_100000000/selected_witnesses.json` | `3d58101f55f2996201e37705b19d3b1dcf03b6b9ffeb2661f15a1d9e52b5f53f` |

The main JSON contains the certified interval endpoints for `C_0`, all checkpoints, all raw and normalized extrema, every sign run, candidate-envelope receipts, shell statistics, timings, and source/data hashes.  The gzip contains every original `(x,y,z)` and ternary `(a,q,n)` coordinate, not merely counts.
