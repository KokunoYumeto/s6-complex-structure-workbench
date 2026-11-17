# Arbitrary marked rational sources in the additive sphere sectors

Proved as P3F.51, with root and checks independent full-text audits.
The statement concerns every fixed rational
elliptic source with Mordell--Weil group \(\mathbb Z\) in the surviving
Oguiso--Shioda profiles, its specified whole-zero scalar construction,
and the cap and scalar-loop data of F36--49 and K26--30.
It does not identify a loop varying the source in its moduli space
with a scalar loop.

## S1. Exact marked normal forms for the two starred source entries

Let \(S\to\mathbb P^1\) be a relatively minimal rational elliptic
surface with zero section \(O\), and choose a primitive generator
\(G\) of its torsion-free Mordell--Weil group. A minimal short
Weierstrass equation has coefficients in
\(H^0(\mathcal O(4))\), \(H^0(\mathcal O(6))\), and its section
coordinates, when disjoint from \(O\), are polynomials of degrees
at most two and three. These coordinates are the restrictions
of the actual relative Weierstrass functions \(x,y\), whose pole
orders along \(O\) are two and three.

For the E7 entry the source height is \(1/2\). The only nonzero
component correction is \(3/2\) at \(III^*\), and the height
identity
\[
 \frac12=2+2(G\cdot O)-\operatorname{cor}_{III^*}(G)
\]
forces \(G\cdot O=0\) and the nonidentity component. Put this
fibre at infinity. The actual short equation is
\[
                 y^2=x^3+(a t+b)x+(c t+d),\qquad a\ne0.
 \tag{S51.1}
\]
Indeed the local \(III^*\) valuations are
\(v_\infty(f)=3\), \(v_\infty(g)\ge5\), so these degree bounds
are exact.

Here is the component arrow used to control the marked section,
including its minimal-model map. Put \(q=1/t\),
\(x_0=q^2x,y_0=q^3y\), then make the fourth root
\(q=z^4,x_0=z^6X,y_0=z^9Y\). Its good central fibre is
\(Y^2=X^3+aX\), and its deck is
\((X,Y,z)\mapsto(-X,-iY,iz)\). The two order-four fixed points
are \(O\) and \((0,0)\). At either, the actual tangent weights
are \((3,1)\). The quotient's minimal toric resolution is the
A3 chain in the lattice
\(\mathbb Z^2+\mathbb Z(3,1)/4\). The remaining order-two
orbit contributes its A1 chain. The resolved quotient maps
properly to the original Weierstrass model by the displayed
invariant monomials \(q,x_0,y_0\). Its invariant two-form
\(dX\wedge dz/Y\) descends crepantly; each compact rational
vertical curve has self-intersection minus two by adjunction.
Thus no exceptional minus-one curve remains, and this proper
birational model is the minimal regular elliptic model of
(S51.1). In each A3 chart the successive primitive rays are
\((3,1)/4,(2,2)/4,(1,3)/4\); the divisor of the actual base
function \(q=z^4\) has multiplicities \(1,2,3\) on them.
The order-two chart contributes multiplicity two, and the
central quotient curve has multiplicity four. Thus the two
multiplicity-one leaves are precisely the leaves over the two
order-four fixed points. An equivariant section through either
point has local equation \(w=z^3h(z^4)\), so its strict transform
meets that first ray's leaf, including \(h\equiv0\). The zero
section meets the leaf over \(O\). Hence a section on the
nonidentity component lifts to the finite fixed point \((0,0)\),
not \(O\). The displayed invariant monomials generate the
invariant function field. Consequently the map to the original
Weierstrass model is birational, and the minimal-resolution
comparison is a map of the original source, not a replacement
by a surface with merely the same fibre graph.

Consequently the actual root coordinates of \(G\) are
\[
              X_G=z^2x_G(z^{-4}),\qquad
              Y_G=z^3y_G(z^{-4}),
\]
and are holomorphic at zero. Since \(x_G,y_G\) were polynomials
of degrees at most two and three, both must be constant,
say \(r_0,s_0\). The nonconstant coefficient in the section
equation gives \(a r_0+c=0\). Also \(s_0\ne0\), since a
section with \(y\equiv0\) is a nonzero two-torsion section.
Translate \(x\) by \(r_0\), choose a constant scaling making
\(s_0=1\), and use the remaining nonconstant linear coefficient
of \(x\) as the affine base coordinate. These are explicit
holomorphic coordinate maps with nonzero constant Jacobian.
They give
\[
                  y^2=x^3+3r x^2+t x+1,\qquad G=(0,1).
 \tag{S51.2}
\]
Thus (S51.2) captures every marked E7 source, rather than only
the displayed \(r=0\) example.

Up to the conventional factor16 the discriminant is
\[
 -4t^3+9r^2t^2+54rt-108r^3-27.
 \tag{S51.3}
\]
Its roots are distinct for \(r^3\ne1\). At \(r^3=1\) there
is a type II fibre at \(t=3r^2\) and a separate \(I_1\).
For example, translating to short form gives
\(f=t-3r^2\), \(g=2r^3-rt+1\), so at that value both vanish
and \(g\) has a simple zero. No additional double nodal
discriminant root is possible: at a double root of the cubic
in \(x\), the derivative with respect to \(t\) is that root
\(x\), which cannot be zero because the cubic's constant
term is one. The certificate also verifies the discriminant
of (S51.3). When \(r^3=1\), constant cube-unit scaling makes
\(r=1\), then \(x_{\rm old}=x+1\),
\(t_{\rm old}=t-3\) gives exactly
\[
             y^2=x_{\rm old}^3+t_{\rm old}x_{\rm old}
                       -t_{\rm old},\qquad G=(1,1).
 \tag{S51.4}
\]
This identifies all three cusp parameters with the E7-B
source by actual coordinate maps.

For the E6+A1 entry, \(h(G)=1/6\). The maximum possible
component corrections are \(4/3\) and \(1/2\). Hence
\[
                 \frac16=2+2(G\cdot O)-4/3-1/2
\]
forces \(G\cdot O=0\) and nonidentity components at both
reducible sites. Put \(IV^*\) at infinity. The short
Weierstrass coefficients have degrees at most one and two.
On the minimal cubic good root
\(q=z^3,x_0=z^4X,y_0=z^6Y\), the central deck is
\((X,Y)\mapsto(\zeta_3^2X,Y)\). Its three fixed points are
\(O,(0,\pm\sqrt{g_4})\), with tangent weights \((2,1)\).
Resolving their actual A2 quotient charts and using the
same invariant two-form argument gives the minimal \(IV^*\)
model. The actual rays \((2,1)/3,(1,2)/3\) have base
multiplicities one and two under \(q=z^3\), and the central
quotient curve has multiplicity three. An equivariant section
through a fixed point has equation \(w=z^2h(z^3)\) and meets
its first ray. Hence the three multiplicity-one leaves
correspond exactly to these three fixed points; \(O\) determines
the identity leaf. Thus \(G\) has a finite nonzero three-torsion
limit. The root coordinates are
\[
                 X_G=z^2x_G(z^{-3}),\qquad
                 Y_G=z^3y_G(z^{-3}).
\]
It follows that \(x_G\) is constant and \(y_G\) is linear
with nonzero leading coefficient. Set the new affine base
coordinate equal to \(y_G\), and translate \(x_G\) to zero.
The marked section is now \(G=(0,t)\), and the equation has
the form
\(y^2=x^3+3r x^2+(A t+B)x+t^2\).
The nonidentity A1 section maps to the singular point of
its finite Weierstrass fibre. There \(y_G=0\), so its base
value is \(t=0\); the derivative with respect to \(x\)
then forces \(B=0\). We have proved the full marked form
\[
                   y^2=x^3+3r x^2+A t x+t^2,\qquad G=(0,t).
 \tag{S51.5}
\]
Its discriminant, up to factor16, is
\[
 t^2\{9r^2(A^2-12r)+(54rA-4A^3)t-27t^2\}.
 \tag{S51.6}
\]
The discriminant of the bracket is \(16(A^2-9r)^3\).
Accordingly the retained-\(I_1\) E6+A1 sectors are exactly
\[
 \begin{array}{ll}
 r\ne0,\ A^2\ne9r,12r &: IV^*+I_2+2I_1,\\
 r=0,\ A\ne0 &: IV^*+III+I_1 .
 \end{array}
 \tag{S51.7}
\]
The case \(A^2=9r\ne0\) is \(IV^*+I_2+II\), with no
\(I_1\) whole-zero site. The case \(A^2=12r\ne0\) has
\(I_3\) in place of \(I_2\), so its root rank is eight
and it is outside the Mordell--Weil-\(\mathbb Z\) entry.
The case \(r=A=0\) is also outside that entry.
For the III sector the literal scaling
\(x=s^2X,y=s^3Y,t=s^3T\), with \(s=A\), makes \(A=1\).
Thus every E6-B source is actually the displayed model.
The I2 sector retains its coefficient \(A\); it is not
identified with the \(A=0\) representative by assertion.

## S2. Every starred root map with all coefficients retained

For (S51.2), at infinity the exact equation and section are
\[
 y_0^2=x_0^3+3r q^2x_0^2+q^3x_0+q^6,\qquad
                         G=(0,q^3).
\]
The actual substitutions of F41 give
\[
 \begin{array}{ll}
 m=4l,\ k=3l:
 &Y^2=X^3+3r z^{2l}X^2+X+z^{6l},
       \quad G'=(0,z^{3l}),\\
 m=4l+3,\ k=3l+2:
 &Y^2=X^3+3r z^{2l+2}X^2+zX+z^{6l+6},
       \quad G'=(0,z^{3l+3}).
 \end{array}
 \tag{S51.8}
\]
Here \(q=z^m,x_0=z^{2k}X,y_0=z^{3k}Y\).
The good range has \(l\ge1\), and the reduced range \(l\ge0\).
The good central deck is exactly \((-X,-iY)\), and the
nonidentity fixed point is still \((0,0)\). In the reduced
root the A1 tangent cone \(Y^2-zX\) is unchanged; its actual
blowup gives the same two reduced III component labels and
the same marked nonidentity section.

For the full E6 form (S51.5), the infinity equation is
\[
 y_0^2=x_0^3+3r q^2x_0^2+Aq^3x_0+q^4,\qquad G=(0,q^2).
\]
The actual root maps give
\[
 \begin{array}{ll}
 m=3l,\ k=2l:
 &Y^2=X^3+3r z^{2l}X^2+A z^lX+1,\quad G'=(0,1),\\
 m=3l+2,\ k=2l+1:
 &Y^2=X^3+3r z^{2l+2}X^2+A z^{l+2}X+z^2,
       \quad G'=(0,z).
 \end{array}
 \tag{S51.9}
\]
The good central deck is \((X,Y)\mapsto(\zeta_3^2X,Y)\).
At a reduced root the blowup \(X=zX_1,Y=zY_1\) gives
the two nonidentity labels \(Y_1=\pm1\), and its deck
fixes them because its \(Y_1\) character is
\(\zeta_m^{-(3k+1)}=\zeta_m^{-2m}=1\).
The additional coefficient terms vanish to the displayed
orders and do not change these resolved charts.

The source maps on the good central fibres retain their
precise section limits. For the E7 good root, direct doubling
in (S51.8) gives
\[
 \begin{split}
 X(2G')&=\frac1{4z^{6l}}-3r z^{2l},\\
 Y(2G')&=-\frac1{8z^{9l}}+\frac{3r}{2}z^{-l}-z^{3l},\\
 w(2G')&=-X(2G')/Y(2G')
                  =2z^{3l}+\text{higher terms}.
 \end{split}
 \tag{S51.10}
\]
Thus at the minimal fourth root its germ is exactly
\(z^3 h(z^4)\), with \(h(0)=2\).
For the E6 good root, put \(c=A^2/4-3r\).
Then \(X(2G')=c z^{2l}\) and
\(Y(2G')=-1-(Ac/2)z^{3l}\). Addition to \(G'\) gives
\[
 w(3G')=\frac{12r-A^2}{8}z^{2l}
                         +\text{higher terms}.
 \tag{S51.11}
\]
The leading coefficient is nonzero in the surviving
Mordell--Weil-\(\mathbb Z\) sector. At the minimal cubic
root this is exactly \(z^2 h(z^3)\).
These are actual section calculations, not only assertions
about central component groups.

## S3. The generic coefficient terms preserve the actual line maps

For a good starred root the local finite deck may be
linearized while retaining its marked section as follows.
Start with a holomorphic transverse coordinate vanishing
on that section and average it against the required finite
character. Its first derivative is nonzero. Together with
the unchanged root coordinate \(z\), this gives a local
holomorphic coordinate map with invertible Jacobian.
The weights are therefore literally \((r_0-1,1)\), with
\(r_0=4\) or \(3\), in the charts used in F41.
The invariant quotient monomials and the actual root
substitutions in (S51.8)--(S51.9) identify their resolved
quotients with the corresponding marked minimal source.

The section Cartier function is consequently still
\[
             h(v_w,v_z)=\max(v_w-(r_0-1)v_z,0).
\]
The common regular root refinements, their maps and their
exceptional pullback coefficients are exactly those of F41:
\[
 \begin{array}{c|c|c}
 r_0&\text{interior root rays}&
       \min(v_w,(r_0-1)v_z)\\ \hline
 4&(3,1),(2,1),(1,1),(1,2),(1,3)&(3,2,1,1,1)\\
 3&(2,1),(1,1),(1,2)&(2,1,1).
 \end{array}
\]
They give the actual equality
\[
                 \beta^*N=\pi^*\mathcal M+D_P-D_O.
 \tag{S51.12}
\]
The translation \(Q=pG'\), with \(p=2\) or \(3\), has
the formal germ just computed. In each fixed-section chart
it is
\[
          w\longmapsto w\,u(w,z)+z^{r_0-1}h_0(z^{r_0}),
 \tag{S51.13}
\]
where \(u\) is a nonzero holomorphic unit. The inverse
translation has the same form. Hence it preserves every
ideal \((w,z^j)\) and \((z,w^j)\), \(1\le j\le r_0-1\).
The normalized blowup of their invariant product is the
specified common refinement, so these literal ideal
equalities lift the actual translation and preserve each
Cartier correction in (S51.12).
For higher good root orders, pull back the entire diagram
through the additional root and resolve the fibre product.
The maps and equality pull back, with their ramification
coefficients retained.

At each reduced root the line point in the allowed pair
meets the identity component. The actual resolved
fibre-product map therefore pulls the source line to a
line of degree zero on every exceptional curve that is
contracted to reach the minimal root. The blowup Picard
decomposition descends it through each contraction.
Its difference from \(N=\mathcal O(aG'-O)\) is a vertical
divisor of zero component degrees; the actual reduced
III or IV intersection matrix has integral kernel the
whole fibre. Division by that exact base monomial gives
the required line isomorphism and retains its deck
character. The extra terms in (S51.8)--(S51.9) do not change
any of these component degrees or contraction maps.

The source division sections, actual commuting line norms,
strict contraction estimate and annular gluing of F41,
F44, F46 and F47 apply to these full-coefficient roots.
For clarity, this is a direct application to each source,
not a claim that its complex surface is isomorphic to the
special displayed representative. The source action is
lifted on the actual line just compared; its remaining
ratio is a base unit, finite deck averaging retains its
character, and the invariant analytic root gives
\(A_i^{m_i}=B^{n_i}\) and \([A_i,B]=1\) exactly.
The same norm-shell construction gives the smooth proper
caps and the physical delta action. Thus every coefficient
in the marked source forms has been carried through
the actual source, line and quotient maps.

## S4. The other source sectors are already coefficient-generic

The ordinary III, IV and II root proofs F42--43 were
written with the full holomorphic unit coefficients:
\[
 \begin{array}{ll}
 III:&y^2=x^3+q\,a(q)x+q^2b(q),\quad a(0)\ne0,\\
 IV:&y^2=x^3+q^2a(q)x+q^2b(q),\quad b(0)\ne0,\\
 II:&y^2=x^3+q\,a(q)x+q\,b(q),\quad b(0)\ne0 .
 \end{array}
 \tag{S51.14}
\]
The displayed root substitutions, finite-deck characters,
blowup centres, quotient maps and contractions in those
proofs use precisely these equations. The marked generator's
central point is fixed by the original component map:
nonidentity for III/IV and identity for II. Finite
linearization retaining the marked sections is the
explicit averaging map in S3. The good-III and good-IV
Cartier differences \(E_P-E_O\), and the cancellation
at the six-point good-II correspondence, are therefore
unchanged as actual divisor identities. Higher section
contact changes the finite point on the exceptional
curve, but every contracted centre is the recorded
infinity point, so the identities remain valid.

For the \(I_1^*\) sources the F36/F38/F49 proof is also
coefficient-generic. On the actual minimal quadratic
Tate root it retains
\[
 q_T=z^2u(z^2),\qquad Z_G=zv(z),\qquad
                  v(z)v(-z)=-u(z^2).
 \tag{S51.15}
\]
Here \(u,v\) are arbitrary nonvanishing holomorphic units.
The first equality follows from the analytic inverse
of the Tate \(j\)-series and the even source base; the
second is the marked odd component; the last is the
literal deck equation \(Z_G(-z)=q_T/Z_G(z)\).
Thus the source norm, root Picard character, four-point
blowup quotient and the equality
\(\beta^*N=\pi^*\mathcal M+E_0+E_1\) all retain arbitrary
source coefficients. The translation exchanging the
two indicated exceptional curves is the actual \(Q\)
translation, not a representative-model identification.
F49 then gives the exact affine and line conjugacies,
with the annular map and any moved blowup centres
transported as specified there.

At the selected whole-zero \(I_1\), the actual Tate
period and Picard characters are arbitrary nonzero
holomorphic units. The only vanishing scalar is its
specified simple base factor. K26--30 already retain
these units, their logarithms, the exact cusp-origin
difference and its bounded Cox extension. Thus their
cusp, page and normal-frame comparisons do not impose
a hidden special-source coefficient.

## S5. Why the integral topology computations apply to every source

No identification of whole source surfaces is required
for this step. The exact Oguiso--Shioda component
markings and primitive height determine the actual
intersection numbers of \(O,F,G\) and the labelled
nonidentity components. The same displayed Gram matrix
in each source proof has determinant minus one. Since
the source is rational, its rank-ten integral
Neron--Severi lattice is unimodular; those actual
classes therefore form a basis on every marked source.

The actual translation matrix is determined by its
action on \(O\), \(G\), the fibre and the labelled
components. The section \(2G\), or any required \(jG\),
has its integral vector given by the proved height
formula and root corrections. Thus the programs'
translation matrices are the matrices of the actual
maps on those actual classes, independently of all
Weierstrass coefficients. Component relabelling is
the corresponding explicit permutation of the rows
and columns; no biholomorphism of the whole source
is asserted from that relabelling.

The source-pair complexes used in F36--48 are obtained
from these actual component inclusions and the
Poincare--Lefschetz pairing. Their chain maps and
translation cones are functorial for the just
identified actual maps. Thus every differential,
Smith representative, finite torsion column and
retained collar coefficient in those proofs remains
the actual marked map for each source. The geometric
source-complement fundamental-group proofs likewise
use the actual section and the retained singular
fibres: the one-cap argument uses the abelian
elliptic-lattice quotient and its computed zero
abelianization, and the two-cap argument uses the
trace-unit pair of conjugate nodal vanishing cycles.
Neither argument assumes a special monodromy
factorization of a single displayed model.

This proves the same sphere criteria for every fixed
source in the surviving profiles. The actual page
maps of K26/K28 use these cap charts and retain their
line correspondences. Their integral relative
period obstruction vanishes by the same source
torsion or conjugate-nodal argument, and their
rigidified Picard comparison gives the same page
line up to the specified base pullback. Consequently
the exact height, Euler and signed-return formulas,
and the matched individual pair of K30, hold on
every such fixed source, with the actual parameter
\(\lambda=r^M\) retained.

## S6. Precise scalar and source-moduli loop scope

Remark8.5 specifies an elliptic source, a line bundle
and a translation, then scales the resulting
linearization. The theorem proved here covers every
choice of that fixed source and all the proved cap,
affine, character and annular data. It does not
replace a loop in source coefficients by a scalar
loop. A source-moduli loop can braid the nodal values
or change the marking of \(G\), the cap sites and
the fan lattice. Its return requires transport of
that additional actual marking before it can be
compared with the scalar return. No such comparison
is inferred merely from the coefficient-generic
calculation above.

The positive scalar parameter is exactly the one
specified in K26/K28, and no division by the root
degree is made. The shorter simultaneous-Cox scalar
descent remains the separately assigned problem.
Expansion is treated by the exact inverse-action
and parameter-inversion maps of F50, including its
positive-loop reversal; it is not absorbed into a
choice of a positive norm numerator.

## Certificate and audit state

The symbolic certificate code/part3/generic_source_models.py
checks both marked normal forms, their discriminants,
all four root substitutions, the exact doubling and
tripling expressions, and the original representative
coordinate maps. It executed PASS with 43 exact identities
on 2026-11-17 at 09:02:08 UTC. The first hand-entered
discriminant-of-discriminant constant/exponent was corrected
to \(314928(r^3-1)^3\); its failed assertion is preserved in
code/part3/attempts/generic_source_models_initial.txt.
The zero locus used in the proof was unchanged.
The topological certificates are the
actual source-pair programs already cited in F36--48.
Checks independently read the full geometric proof and reran all
43 identities on 2026-11-17. Its audit passes the exact quotient
component arrow, equivariant local coordinate maps, both families
of invariant refinement ideals, reduced-root descent, and the
actual NS/component source-cone identification. Root independently passed
the full proof, including the exact representative maps, every retained
generic root term and section germ, and the same source-cone
comparison. The proof is promoted and exported as F51.

