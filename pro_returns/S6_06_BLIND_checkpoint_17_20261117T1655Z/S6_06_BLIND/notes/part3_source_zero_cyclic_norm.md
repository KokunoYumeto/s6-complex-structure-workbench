# The successive chosen-sheet norm at the source-zero collision

This working calculation retains the actual Tate and Cartier maps of
Section 27 of `part3_source_zero_completion_working.md`. It computes
continuation of those chosen-sheet maps. It does not supply a closed
finite root-sheet action or the missing collision-to-cap attachment.

## CN.1. Literal winding at the two discriminant branches

Use the fixed holomorphic units in
\[
 Q=q_1q_2u_Q,\qquad P=q_2^{-1}u_P,\qquad c_X=q_2u_X,
 \qquad g_V=2(-1)^{b+1}\lambda_0v^Nq_1c_X^{-2}.
\]
They are nonzero on the two-node polydisc, and their fixed logarithms
have zero continuation. Put \(\mathcal B=QP^2\). Around the strict
\(q_1=0\) branch, with \(v\ne0\) fixed, the windings of
\(\mathcal B\), \(g_V/P\), and \(P^{m-1}g_V\) are all one.
The winding of \(P\) is zero. Around the strict \(q_2=0\) branch,
their windings are respectively \(-1,-1,-m-1\), while that of
\(P\) is \(-1\).

These are winding statements about the literal chosen meromorphic
representatives. All integral periods and the finite cap character
remain in the maps.

## CN.2. The successive maps and their cyclic products

In the good case \((a,b)=(1,2)\), \(m=4p\), the source translation
of \(A\) is multiplication by \(\mathcal B^{-n/m}\), and its line
multiplier is \((g_V/P)^{n/m}\). Write \(\zeta=e^{2\pi i/m}\).
After \(j\) positive continuations around \(q_1\), the ratio of the
continued chosen-sheet map to the initial one is exactly
\[
       A_jA_0^{-1}:(Z,V)\longmapsto
                    (\zeta^{-jn}Z,\zeta^{jn}V).
\]
These torus multipliers commute. Their product, with the actual
same-sheet norm retained, is therefore
\[
 \prod_{j=0}^{m-1}A_j
 =((-1)^{n(m-1)},(-1)^{n(m-1)})\,h^{-n}g^n
 =(-1,-1)\,h^{-n}g^n
 \qquad(n=\pm1).
\]
The remaining map is the actual two-torsion source-and-line
translation \((Z,V)\mapsto(-Z,-V)\). It cannot be dropped as a
physical scalar, since its source multiplier is also \(-1\).

In the reduced case \((a,b)=(2,1)\), \(m=4p-1\), the division
representative is
\[
 R=P\mathcal B^{-(m-1)/(2m)},
\]
and the line multiplier is \((P^{m-1}g_V)^{n/m}\). The same
continuation gives
\[
       A_jA_0^{-1}:(Z,V)\longmapsto
            (\zeta^{jn(m-1)/2}Z,\zeta^{jn}V).
\]
Since \(m\) is odd, both total exponents are multiples of \(m\):
\[
 \frac{n(m-1)}2\sum_{j=0}^{m-1}j
       =\frac{nm(m-1)^2}{4},\qquad
 n\sum_{j=0}^{m-1}j=\frac{nm(m-1)}2.
\]
Consequently
\[
       \prod_{j=0}^{m-1}A_j=h^{n(m-1)/2}g^n.
\]
Around \(q_2\), the good ratios are the inverse ones. The reduced
source ratio has exponent \(jn(m+1)/2\), and the reduced line ratio
has exponent \(-jn\). The resulting residual is again \((-1,-1)\)
in the good even case and the identity in the reduced odd case.

## CN.3. The retained line conjugacy and the scope of the calculation

Before comparing a given root-line lift with these Tate formulas,
retain its actual finite averaging. For two lifts with the same
source map and norm, their ratio is initially a cyclic norm-one
base unit. It need not have pointwise \(m\)-th power one. After
matching its central character \(\chi\), choose
\(f=\log(r/\chi)\) with zero cyclic sum and put
\[
       \psi(z)=\frac1m\sum_{j=0}^{m-1}j f(D^jz).
\]
Then \(\psi(Dz)-\psi(z)=f(z)\). Conjugation by the actual
multiplier \(e^{-\psi}\), with its annular restriction retained,
makes the lift deck-invariant. Only at that stage does its ratio
with the normalized Tate lift become the specified constant finite
character. The products in CN.2 refer to these explicitly carried
coordinates.

A loop enclosing both discriminant branches has zero winding of
\(\mathcal B\). In particular the central E annulus
\(v=0,\ q_1=q_2=T\) has \(\mathcal B=1\) and does not carry
the strict-\(q_1\) division monodromy just computed. Thus the even
residual does not by itself assign the E-component permutation,
nor does the odd cancellation prove an attachment. A proposed
root-sheet action must state its base deck, its continuation of
the division section and line, its successive cyclic norm, and
the actual quotient on the protected cusp boundary.

The exact certificate `code/part3/source_zero_cyclic_norm.py` checks
the winding exponents and both cyclic products. Fourfold has
independently confirmed the two residual products. This note assigns
no numerical source-family return.

## CN.4. The protected-I multiplicity of the direct root-quotient attempt

There is a further exact test on the direct candidate obtained by
adjoining \(q_1=\xi^m\), using the fractional period
\(f_{\rm cap}\) for its root deck, and quotienting by that deck.
This paragraph concerns that specified candidate, rather than an
arbitrary collision filling.

At a fixed sufficiently small \(v\ne0\), the original I-boundary
period matrix is the identity. Its \(m\)-root pullback has period
matrix \(mI\). On a regular toric refinement its reduced central
components have labels
\[
                       j\in\mathbb Z^2/m\mathbb Z^2.
\]
This can also be read before refinement from the original rays
\((m j,1)\); all integral height-one vertices occur after a
regular refinement of its complete periodic two-dimensional
slice. The prescribed fractional-period deck acts on these
labels by the literal translations
\[
 j\longmapsto j+w,\qquad
 w=mf_{\rm cap}=
 \begin{cases}
  (n,-n),&m=4p,\ (a,b)=(1,2),\\
  (-n(m-1)/2,-n),&m=4p-1,\ (a,b)=(2,1).
 \end{cases}
\]
For \(n=\pm1\), the second coordinate alone shows that \(w\)
has exact order \(m\). Thus every component has an orbit of
length \(m\), and no nonidentity deck power below \(m\) fixes
its generic point.

In the reduced case the full cyclic norm in CN.2 is already an
integral period, so this accounts for the entire cyclic group on
the torus quotient. In the good case the \(m\)-th power retains
\((Z,V)\mapsto(-Z,-V)\). On the open torus of a component this
has no fixed point; its square is the identity. Thus the resulting
order-\(2m\) group also has trivial inertia at a generic point of
every such divisor. Constant finite characters and the extending
unit conjugations of CN.3 do not change this generic inertia.

The invariant base function is the original \(q_1=\xi^m\).
Since the quotient has generic ramification index one along the
divisor just described, the valuation formula is
\[
  \operatorname{ord}_{\widetilde D}(q_1)=m
   =1\cdot\operatorname{ord}_{D}(q_1).
\]
Equivalently, a sufficiently small neighbourhood of one generic
component point has disjoint translates, and the quotient is
identified with that neighbourhood, where the base map is still
\(\xi\mapsto\xi^m\). This particular quotient has a multiple
I-boundary of multiplicity \(m\). The original family retained
in K49 has multiplicity one there. Therefore the direct
fractional-period root quotient does not give its required
protected I-boundary map. A different attachment must give its
actual generic boundary identification; the E-annulus norm or
the finite order of \(f_{\rm cap}\) does not provide one.

## CN.5. The source translation at the protected nodal chart

The same issue is visible before considering the line or the fan.
At the strict \(q_1=0\) branch with \(v\ne0\), the actual
division representatives have
\[
 \operatorname{ord}_{q_1}R=
 \begin{cases}
  1/m,&m=4p,\\
  -(m-1)/(2m),&m=4p-1.
 \end{cases}
\]
Every integral Tate reindexing replaces this number by its sum
with an integer, since \(\operatorname{ord}_{q_1}Q=1\).
Neither fractional class vanishes. On the finite root cover,
choose its representative with valuation \(r\) strictly between
zero and one; it is \(1/m\) in the good case and
\((m+1)/(2m)\) in the reduced case. In the actual Tate-node
coordinates \((Z_0,W_0)=(R,Q/R)\), both coordinates therefore
tend to zero. The division section tends to the node of the
original irreducible nodal fibre.

An invertible extension of its translation on that original
fibre would send the smooth zero-section point to the node.
This is impossible for an isomorphism of the nodal fibre: the
local analytic rings at its smooth points are regular, whereas
the node has embedding dimension two. Thus the displayed
chosen-sheet source translation has no invertible extension
on the protected original I1 chart. The same conclusion holds
for its inverse and for either sign of \(n\). An extending
physical line scalar cannot change this source map.

After the root and resolution the translation does act on the
I_m source by shifting its components. CN.4 records the exact
failure of the direct quotient of that action to recover the
required multiplicity-one chart. These are scoped obstructions
to the displayed translation and quotient, not a classification
of all possible central attachments.

Audit: fourfold independently confirmed CN.2 and CN.4, including
the good order-two source/line residual and the generic-divisor
inertia calculation. CN.5 is the direct Tate-coordinate form
of the same protected-source obstruction.

## CN.6. Changes of the marked finite lift

The good residual cannot be removed by changing the already
allowed \(m\)-th-root character. Multiplying the division root
or its normalized line multiplier by a constant in \(\mu_m\)
contributes the \(m\)-th power of that constant to the cyclic
product, which is one. Integral Tate reindexing changes the
written integral \(h,g\) norm but leaves its class on the torus
quotient unchanged. An actual periodic extending gauge conjugates
the full cyclic product; in particular it cannot turn its
nontrivial source translation by \(-1\) into the identity.

A diagonal multiplier of order \(2m\), with \(m\)-th power
\((-1,-1)\), would cancel this residual in the successive
product. Its pointwise \(m\)-norm, however, also changes by
\((-1,-1)\). It changes the specified source division branch
and the actual cap norm rather than giving an automorphism of
the same marked cap data. This identifies the exact missing
comparison in that proposed adjustment; no such adjustment is
used in K49 or in CN.1–5.
