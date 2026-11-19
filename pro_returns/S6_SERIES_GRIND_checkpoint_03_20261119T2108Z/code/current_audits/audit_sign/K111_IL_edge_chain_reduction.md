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

The smallest missing finite input for the IL calculation is this **ordered primitive common-edge chain with its original period closure**, together with the choices in its prescribed quotient regularization. The interior cones of the generic common fan are unnecessary for this particular lower-star reconstruction. The chain is part of the missing common-fan output. It has not been recovered from a supplied file: the supplied zip has no entry named for the zero-upper array, common-fan array, lower-star array, or corner-equivalence array.

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

## Matching still required

The floor/ceiling evaluations and contraction table above are algebraic identities on the explicitly defined lifts. The entire actual 324-chart common-refinement star has **not** yet been identified with the resulting lifted source chain. The next finite certificate must reconstruct the actual common-edge chain and its quotient subdivision, match every native lift and period arrow, then compute its contraction histogram or solve its full cyclic intersection matrix. Neither the values 49,45,133,94 nor the compact seed totals are assumed by that reconstruction.

The 2,018-check minimal-parent certificate establishes the three-chart starting configuration and exact morphisms. It does not assert the missing 324-chart matching or the absolute seed.
