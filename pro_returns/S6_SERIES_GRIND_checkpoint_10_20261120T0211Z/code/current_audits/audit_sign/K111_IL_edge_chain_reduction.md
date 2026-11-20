# K111: the smallest remaining lower-star input

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (not separately exposed). Date: 19 November 2026. This is a scoped derivation record, with the exact unresolved matching stated below.

## The data still required

I2L.2 constructs all lower one-end cones by extracting the common upper boundary on

\[
3y-x-36r=0
\]

and joining each consecutive edge to the physical rays
\(E_l=(0,l,0,1),E_{l+1}=(0,l+1,0,1)\), for \(0\le l<12\).
Every primitive upper ray on that boundary has the form

\[
U(a,b)=(3a,a+12b,b,0),\qquad \gcd(a,b)=1.
\]

The embedding \((a,b)\mapsto U(a,b)\) is an isomorphism onto the original integral lattice in this boundary plane: its inverse reads \((x/3,r)\), and the defining boundary equation forces \(3\mid x\). Thus the consecutive primitive boundary rays of a regular common face have \(\det((a_i,b_i),(a_{i+1},b_{i+1}))=\pm1\). Their four-dimensional lower joins have determinant of absolute value three.

The smallest missing finite input for the original IL calculation is this **ordered primitive common-edge chain with its original period closure**. The finite quotient calculation below now proves that both possible initial quotient choices give the same complete physical lower star. The interior cones of the generic common fan are unnecessary for this particular lower-star reconstruction. The chain is part of the missing common-fan output. It has not been recovered from a supplied file: the supplied zip has no entry named for the zero-upper array, common-fan array, lower-star array, or corner-equivalence array.

The full compact CFL contribution still needs its separate whole-atlas fixed-face data. Reducing the IL input does not close that gate.

## Exact maps already reconstructed

The fresh program `code/K111_lower_parent_reconstruction.py` begins with the twelve printed raw parents

\[
\langle E_l,E_{l+1},(0,12,1,0),(3,13,1,0)\rangle.
\]

It resolves each complete finite-quotient cone, retains all eight regular children, and extracts every chart containing the physical face. Its two inserted rays are

\[
R_1=(1,l+13,1,1),\qquad R_2=(2,l+13,1,1).
\]

The three source charts have consecutive projected rays \((0,1),(1,1),(2,1),(3,1)\). The full period

\[
L:(X,Y,P,v)\longmapsto(P^3pX,PpY,P,v)
\]

identifies the first and last ends. Computing the original four-dimensional wall equations yields normal degrees \((-1,0,1)\) and \((-1,1,0)\), and the relative intersection triple \((-2/3,-1/3,-2/3)\). These are outputs, not construction inputs. All raw quotient invariant semigroup generators of degree at most three have nonnegative integral pullbacks on every child; the inverse on the original dense torus retains the original four characters. There are 2,018 successful exact checks across 96 regular full charts and 36 physical lower-face charts.

The separate `code/K111_small_one_corner.py` enumerates the complete compact fixed strata in these small raw-parent resolutions. It finds 60 isolated points and no compact curves, giving \((12,88)\). This is a value for the stated small resolution. It has not been identified with the common-boundary endpoint, so it is not substituted for CFL's one-end value \((2736,17092)\).

## Direct native normal characters

The full original meromorphic coefficients are

\[
\alpha_l=Yv^{-l},\qquad \beta_l=v^{l+1}Y^{-1},
\qquad \alpha_l\beta_l=v.
\]

Their physical weights are respectively \(+1,-1\). In the ordered lattice \((x,y,r,z)\), their rows are \((0,1,0,-l)\) and \((0,-1,0,l+1)\). These are the actual coefficient characters, including their stated Cartier types.

For an integral source vector \((x,r)\), define

\[
z(x)=\lceil x/3\rceil-\lfloor x/3\rfloor,\qquad
V_l(x,r)=\bigl(x,\lceil x/3\rceil+12r+l z(x),r,z(x)\bigr).
\]

The normal character evaluations on this explicitly defined lift are exactly

\[
\operatorname{ord}\beta_l=-\lfloor x/3\rfloor-12r,
\qquad
\operatorname{ord}\alpha_l=\lceil x/3\rceil+12r.
\]

Here is its actual raw-parent expression. Write

\[
(x,r)=\lambda_0(3a_0,b_0)+\lambda_1(3a_1,b_1)
\]

in a given consecutive source cone. Then

\[
V_l(x,r)=\lambda_0U(a_0,b_0)+\lambda_1U(a_1,b_1)
 +\{x/3\}E_l+(\lceil x/3\rceil-x/3)E_{l+1}.
\]

All coefficients are nonnegative on that source cone. Pairing any raw-parent dual-semigroup character with these columns gives its actual monomial pullback; integrality follows from the integral original-lattice column. This is the concrete semigroup-to-source map, rather than a change of an unmarked abstract lattice. The original source functions retain orders \(x\) and \(3r-x\), with the full coefficient \(p\) in \(Q/X=pP^3/X\).

The period maps retain their full units. The lattice part of \(L\) sends \(V_l(x,r)\) to \(V_l(x+3r,r)\), and its coefficient factors are \(Pp\) and \((Pp)^{-1}\) on \(\alpha_l,\beta_l\). The period \(T\), with the label change \(l\mapsto l+12\), has factors \(P^{12}c_{12}\) and \(P^{-12}c_{12}^{-1}\). The change \(Y'=Yv^{-l}\) has integral matrix \(y'=y-lz\), determinant one and inverse \(Y=Y'v^l\). In the genuine point-line coefficient this retains the additional factor \(v^l\):

\[
v_2=\frac{\eta_2P^2v^lY'}{Xf_{P^2}(pP^3/X)}.
\]

No factor of the physical line is discarded.

## Exact contraction rule on these written lifts

For an ordinary source blowup, the new source ray is the sum of its two neighbors. Write their first coordinates as \(x_0,x_1\). The full normal wall degrees obtained from the written lifts are

\[
d_- =\lfloor x_0/3\rfloor+\lfloor x_1/3\rfloor
       -\lfloor(x_0+x_1)/3\rfloor,
\]
\[
d_+ =\lceil(x_0+x_1)/3\rceil
       -\lceil x_0/3\rceil-\lceil x_1/3\rceil.
\]

The linear original-height terms cancel in this wall equality. Consequently the two residues of the neighboring first coordinates determine the following pairs:

| Neighbor residues modulo 3 | \((d_-,d_+)\) |
|---|---|
| \((1,1)\) | \((0,-1)\) |
| \((2,2)\) | \((-1,0)\) |
| \((1,2)\) or \((2,1)\) | \((-1,-1)\) |
| At least one residue zero | \((0,0)\) |

The actual source maps of this ordinary blowup are \((u,w)\mapsto(u,uw)\) and \((u,w)\mapsto(uw,w)\), with the reciprocal divisions on their principal overlaps. The line comparison multiplies by \(u^{d_\pm}\), or the corresponding second-chart power, exactly as in IL.11-12. Thus the displayed rule retains the reciprocal chart maps and fixes the direction of both normal degrees.

## Complete determinant-three local reduction

Orient an adjacent interval so that \(D=a_0b_1-a_1b_0=-1\), and first take \(l=0\). Put
\(B=(E_0,E_1,U(a_0,b_0),U(a_1,b_1))\). Direct inversion gives

\[
B^{-1}\mathbb Z^4=\mathbb Z^4+\mathbb Z q,
\quad q=\bigl(1/3,2/3,\{-b_1/3\},\{b_0/3\}\bigr).
\]

The right side has index three over \(\mathbb Z^4\), as does the left side; its generator maps to an integral vector under \(B\). This proves the equality. The pair \((b_0,b_1)\) cannot be \((0,0)\) modulo three, since \(D=-1\). Thus there are precisely eight coefficient-lattice cases.

For the representative matrix \(B_*\) with the same residues, the explicit map
\(F=B B_*^{-1}\) has integral entries and integral inverse: both coefficient lattices are the displayed \(\mathbb Z^4+\mathbb Zq\). It maps each of the four named parent rays to its named actual ray, and fixes the physical vector \(E_1-E_0\). Its induced character map is the transpose. This supplies the exact lattice morphism used in the finite calculation. The actual source monomials continue to be evaluated in the actual columns \(B\), by the formulas above.

The two nonzero quotient representatives are \(Bq\) and \(B\{2q\}\), divided by their gcd. Their two insertion orders have been executed for all eight cases. After the first insertion every singular child has determinant two, and its unique remaining primitive quotient ray is the other original representative. The final complete physical stars agree for both orders. Their source rays are as follows; the two endpoints are always the primitive reductions of \((3a_i,b_i)\).

| Residues of \(b_0,b_1\) | Interior source rays | Full regular four-charts | Physical lower charts |
|---|---|---:|---:|
| Equal and nonzero | \((2a_0+a_1,(2b_0+b_1)/3)\), \((a_0+2a_1,(b_0+2b_1)/3)\) | 8 | 3 |
| Opposite and nonzero | \((a_0+a_1,(b_0+b_1)/3)\) | 7 | 2 |
| Exactly one zero | None; the corresponding endpoint is divided by three | 5 | 1 |

Every surviving four-dimensional ray is exactly \(V_l(x,r)\). The certificate checks the full degree-at-most-three invariant semigroup on every chart, all twelve integral label maps, the original negative and positive normal rows and the primitive source determinants. Thus the local floor/ceiling matching is complete for every adjacent primitive common edge.

## Exact ordered-chain replay

`code/K111_replay_edge_chain.py` accepts the ordered primitive edge chain with endpoints \((0,1),(1,1)\). It constructs all physical source charts using the three rows of the table, verifies the raw-parent barycentric maps and original wall relations, and solves the entire cyclic divisor-intersection matrix with the marked component coefficient fixed to zero. A second route contracts only a source ray which is the sum of its two current neighbors, retains each reciprocal ordinary blowup map and normal coefficient power, and computes the contraction histogram. The two routes agree on all four supplied example chains, with 651 exact checks. These examples include the minimal chain, an ordinary insertion, endpoint division by three and the full Farey chain of order ten.

The original 324-chart common-refinement chain remains absent. Its evaluation requires only that actual ordered edge input; the local quotient choices and normal-lift formulas are now determined. Neither the values 49,45,133,94 nor the compact seed totals enter the reconstruction.

## A newly constructed auxiliary edge

The fresh regular common fan constructed directly from the three original convex periodic cells has 1,926 cones, and its extracted one-end edge is exactly \((0,1),(1,1)\). The chain replay verifies its completed lower pair \((1,-2)\) with 31 checks. The complete new one-end atlas has 2,022 regular four-charts and 15,217 checks, including all full period facet maps and reciprocal unit columns, all twelve lower stars and all sixty compact corner points. Its compact one-end sum is \((12,88)\).

These are values for the explicitly constructed auxiliary atlas. Its complete zero and infinity extensions, full point/O comparison and whole compact fixed-stratum calculation remain separate. The file `K111_auxiliary_resolution_comparison.md` states the actual character maps and exact scope of that comparison. The old 324-chart chain and absolute seed are not assigned those new values.
