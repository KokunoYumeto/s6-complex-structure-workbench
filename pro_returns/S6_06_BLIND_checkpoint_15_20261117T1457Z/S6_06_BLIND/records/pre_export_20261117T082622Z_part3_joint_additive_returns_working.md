# Actual joint additive pages and their signed returns

Proved as P3K.28 after the parent's complete independent audit. The maps below concern the actual
families constructed in P3F.36, P3F.38, P3F.46 and P3F.47, with their specified
whole-zero nodal completion and their retained annular line maps. No new
comparison between different cusp fans is asserted here.

## K28.1. The marked norm data and the actual parameter

Place the two capped source fibres at infinity and zero. Write their root
orders as \(m_\infty,m_0\), their signed norms as \(n_\infty,n_0\), and put
\[
 D=m_0n_\infty+m_\infty n_0.
 \tag{K28.1}
\]
The complete integral topology proofs F38, F46 and F47 show that their sphere
sector is exactly \(D=\varepsilon\), \(\varepsilon\in\{1,-1\}\). In particular
\(\gcd(m_\infty,m_0)=1\), and each local pair \((m_i,n_i)\) is primitive.
Throughout this proof put \(M=m_\infty m_0\).

The actual source line is denoted \(\mathcal M\), to distinguish it from the
integer \(M\). Its contracting lift \(B_\lambda\) covers translation by
\(-Q=-bG\). At each resolved root there are actual commuting maps
\[
 A_{i,0}^{m_i}=B_0^{n_i},\qquad [A_{i,0},B_0]=1 .
\]
The family in the topology proofs uses
\[
 \lambda=r^M,\qquad
 A_{i,r}=r^{M n_i/m_i}A_{i,0},\qquad
 B_\lambda=r^M B_0 .
 \tag{K28.2}
\]
This is the parameter used here. The positive return means one positive
loop in \(r\).

Let \(\gamma\) be the outward suspension coordinate, so a positive unit
of \(\gamma\) is the inverse contracting map \(B_\lambda^{-1}\). Write
\(\alpha=\arg(t)/(2\pi)\) on the ordinary annulus. The actual cap norm
coordinates, of periods \(m_i\), are
\[
 u_0=m_0\gamma-n_0\alpha,\qquad
 u_\infty=m_\infty\gamma+n_\infty\alpha.
 \tag{K28.3}
\]
Indeed, on the root \(q_i=z^{m_i}\), the defining cut is
\((z,u_i)\mapsto(\zeta_{m_i}z,u_i-n_i)\). Thus a positive source
meridian maps to \(-n_i h_i\), and \(\gamma\) maps to \(m_i h_i\),
where \(h_i\) is the positive primitive cap circle. This is the actual
marked meridian \(m_i\alpha_i+n_i\gamma\) of F38, F46 and F47.
The source translations and the integral line characters remain in the
other coordinates of these maps.

The norm-shell coordinate can be used with the prescribed boundary metric.
To justify this without supposing that a fibrewise lift has a constant
pointwise norm, use the actual strictly contracting primitive generator
\(H_i\), with \(H_i^{m_i}=B_\lambda\) and \(H_i^{n_i}=A_{i,r}\).
An equivariant radial coordinate is chosen on one norm shell and transported
by \(H_i\). On the overlap with the flat boundary norm, the increasing lift
of the circle-coordinate comparison has \(F(s+1)=F(s)+1\). The radial map
\(v\mapsto c^{F(s)-s}v\), in the notation of P3F.31, commutes with the
actual contraction and with the physical delta circle. It fixes the source
and base coordinates and carries the actual circle line. This gives the
same marked norm coordinates (K28.3) through the entire cap.

## K28.2. An exact map of the orbit base to the weighted three-sphere

On the ordinary annulus set
\[
 \phi_1=\varepsilon(m_0\gamma-n_0\alpha),\qquad
 \phi_2=\varepsilon(m_\infty\gamma+n_\infty\alpha).
 \tag{K28.4}
\]
The phase matrix, with columns \((\gamma,\alpha)\), has determinant
\(D=\varepsilon\). Its entries are integers, so it is an actual
automorphism of the marked two-torus. Moreover
\[
 m_0\phi_2-m_\infty\phi_1=\alpha.
 \tag{K28.5}
\]
Choose the unique positive radii satisfying
\[
 r_1^2+r_2^2=1,\qquad
 \frac{r_2^{m_0}}{r_1^{m_\infty}}=|t|.
\]
The ratio is strictly increasing as \(r_2\) increases from zero to one.
The map \(z_j=r_j e^{2\pi i\phi_j}\) therefore identifies the actual
ordinary orbit-base annulus with the corresponding annulus in
\(S^3\subset\mathbb C^2\), with
\[
                         t=\frac{z_2^{m_0}}{z_1^{m_\infty}}.
 \tag{K28.6}
\]

Here are its extensions across the two actual cap solid tori. At infinity,
\(q_\infty=1/t=z^{m_\infty}\), let \(R>0\) be defined by
\[
 R^2+|z|^2R^{2m_0/m_\infty}=1.
\]
The extending map is
\[
 (z,u_\infty)\longmapsto
 \left(
 zR^{m_0/m_\infty}e^{2\pi i\varepsilon m_0u_\infty/m_\infty},
 Re^{2\pi i\varepsilon u_\infty}
 \right).
 \tag{K28.7}
\]
Under the actual \(A_\infty\) cut the first phase changes by
\[
 \frac{1-\varepsilon m_0n_\infty}{m_\infty}
       =\varepsilon n_0,
\]
and the second by \(-\varepsilon n_\infty\). Both are integers.
Thus (K28.7) descends through the actual marked quotient. Its inverse first
recovers \(R=|z_2|\), then a lift of \(\arg(z_2)/(2\pi)\), and finally
\(z\). The possible lifts are identified by precisely the powers of
the displayed \(A_\infty\) cut. The derivative of the radial equation
with respect to \(R\) is positive, so the map and inverse are smooth.

At zero, \(q_0=t=z^{m_0}\), use
\[
 R^2+|z|^2R^{2m_\infty/m_0}=1
\]
and the map
\[
 (z,u_0)\longmapsto
 \left(
 Re^{2\pi i\varepsilon u_0},
 zR^{m_\infty/m_0}e^{2\pi i\varepsilon m_\infty u_0/m_0}
 \right).
 \tag{K28.8}
\]
The two phase changes under \(A_0\) are
\(-\varepsilon n_0\) and
\((1-\varepsilon m_\infty n_0)/m_0=\varepsilon n_\infty\).
The same inverse argument applies. Substitution of (K28.3) shows that
(K28.7) and (K28.8) agree exactly with (K28.4) on both ordinary overlaps.
These formulas, rather than the abstract Seifert invariants alone,
give the required global marked orbit-base identification.

The positive weighted Hopf angle, of weights
\((m_0,m_\infty)\), is
\[
                              \beta=\varepsilon\gamma.
 \tag{K28.9}
\]

## K28.3. The physical parameter cochain and the complex page

The annular arrow is ordinary-to-cap, as fixed in the construction proofs.
If \(c=\log\lambda/(2\pi i)\) and \(s_i=\log q_i/(2\pi i)\), its scalar
variation is \(n_i(c-c_0)s_i\delta/m_i\). For a positive \(r\)-loop put
\[
 k_\infty=m_0n_\infty,\qquad k_0=m_\infty n_0.
\]
The actual inverse closing multiplier is
\[
                      f(t)=t^{k_0}(t-t_c)^{-(k_\infty+k_0)}.
 \tag{K28.10}
\]
Its orders at zero and infinity are \(k_0,k_\infty\), respectively.
In the sphere sector \(k_\infty+k_0=\varepsilon\).
At the selected cusp \(q=t-t_c\), the positive deck is therefore the
inverse of (K28.10), and its logarithmic part is
\(+\varepsilon\log q\,\delta/(2\pi i)\).
The remaining factor is a specified nonvanishing unit. Its logarithm is
added to both compared origins, so it cancels in their difference.

For clarity the full cusp origin computation is retained. Put
\[
 s=\frac{\log q}{2\pi i},\qquad
 v=\frac{\log r}{2\pi i},\qquad
 \gamma=(g,-C-s-Mv).
\]
The physical line coordinate is \(V=e^{2\pi i\zeta_2}\), the source
Abel coordinate is \(\zeta_1\), and
\[
 B_\lambda(a,V)=(a-g,e^{2\pi iC}q r^M V).
\]
Thus the displayed \(\gamma\) is exactly \(B_\lambda^{-1}\).
Use the two origins
\[
 \begin{split}
 o_\varepsilon&=\varepsilon
       \left(-\frac{gs}{M},\frac{Cs}{M}+\frac{s^2}{2M}+sv\right),\\
 \sigma_\varepsilon&=\varepsilon
       \left(gv,-Cv-\frac{M(v^2-v)}2\right).
 \end{split}
 \tag{K28.11}
\]
They have the actual parameter deck just found, and their difference
\(F_\varepsilon=\sigma_\varepsilon-o_\varepsilon\) satisfies
\[
 F_\varepsilon(v+\theta)-F_\varepsilon(v)
   =\varepsilon\theta\gamma
      -\frac{\varepsilon M\theta(\theta-1)}2\,\delta .
 \tag{K28.12}
\]
The quadratic delta gauge is zero at both endpoints. On the auxiliary
cusp root \(q=Q^{2M}\), the whole angular difference changes by
\(-2\varepsilon M\theta\delta\) under \(s\mapsto s+2M\); this is the
retained degree-\(2M\) boundary gauge. That auxiliary source root does
not change the parameter. One positive \(r\)-loop moves by
\(\varepsilon\gamma=\beta\), with the same positive sign for either
sphere determinant.

Choose a regular value \(\tau\), distinct from the capped sites and
the selected cusp. The actual complex page is
\[
 \mathcal C^\circ:\quad \eta^{m_0}-\tau\xi^{m_\infty}=1.
 \tag{K28.13}
\]
Its weighted radial embedding into the above three-sphere is
\[
 (\xi,\eta)\longmapsto
       (\rho^{m_0}\xi,\rho^{m_\infty}\eta),
 \qquad
 \rho^{2m_0}|\xi|^2+\rho^{2m_\infty}|\eta|^2=1 .
 \tag{K28.14}
\]
It is the positive-argument page of the weighted homogeneous polynomial
\(z_2^{m_0}-\tau z_1^{m_\infty}\), and its map to the source base is
\[
                      t=\tau+\xi^{-m_\infty}.
 \tag{K28.15}
\]
The affine curve is smooth: its two partial derivatives cannot both
vanish on (K28.13). Its map has degree \(M\). Over infinity there are
\(m_0\) points, each of ramification order \(m_\infty\); over zero there
are \(m_\infty\) points, each of order \(m_0\); over the regular binding
\(\tau\) there is one point of order \(M\). The last assertion follows
also from \(\gcd(m_\infty,m_0)=1\): the expansion
\(\xi\sim c w^{-m_0}\), \(\eta\sim d w^{-m_\infty}\)
has one place at infinity. Riemann--Hurwitz gives
\[
                  g(\overline{\mathcal C})
                    =\frac{(m_\infty-1)(m_0-1)}2.
 \tag{K28.16}
\]
The selected source \(I_1\) is unramified and has \(M\) separate
nodal inverse images.

The page is also the exact graph in each actual root cap. At infinity
its phase-\(\phi\) graph is
\[
 \varepsilon m_0 u_\infty+
     \frac{\arg(1-\tau z^{m_\infty})}{2\pi}
           =\frac{\phi}{2\pi}\pmod{\mathbb Z},
 \tag{K28.17}
\]
and at zero it is
\[
 \varepsilon m_\infty u_0+
     \frac{\arg(z^{m_0}-\tau)}{2\pi}
           =\frac{\phi}{2\pi}\pmod{\mathbb Z}.
 \tag{K28.18}
\]
There are \(M\) sheets before quotienting. The actual \(A_\infty\)
changes the sheet index by \(-\varepsilon m_0n_\infty\);
there are exactly \(m_0\) orbits of length \(m_\infty\).
The \(A_0\) sheet step is \(-\varepsilon m_\infty n_0\),
giving \(m_\infty\) orbits of length \(m_0\). For phase zero the
holomorphic coordinates are, respectively,
\[
 \begin{array}{ll}
 \displaystyle \xi^{m_\infty}
       =\frac{z^{m_\infty}}{1-\tau z^{m_\infty}},
 &\displaystyle \eta^{m_0}
       =\frac1{1-\tau z^{m_\infty}},\\[6pt]
 \displaystyle \xi^{m_\infty}
       =\frac1{z^{m_0}-\tau},
 &\displaystyle \eta^{m_0}
       =\frac{z^{m_0}}{z^{m_0}-\tau}.
 \end{array}
 \tag{K28.19}
\]
Thus these local complex maps do not depend on the signs of the norms.

## K28.4. The exact line on the page, including the quadratic starred cap

On each orbit of the sheet permutation choose one representative graph
\(u_i=u_{i,j}(z)\). The map from the actual resolved root source is
\[
                        p\longmapsto [p,u_{i,j}(q_i(p))].
 \tag{K28.20}
\]
It extends across every resolved component, since the phase in
(K28.17) or (K28.18) is smooth there. A relation preserving this
representative norm level has \(n_i k+m_i h=0\). Primitivity gives
\(k=m_i j\), \(h=-n_i j\), and the actual identity
\(A_i^{m_i j}B_\lambda^{-n_i j}=1\) proves uniqueness. Thus no residual
stabilizer or further root quotient remains in (K28.20).
For a nonzero vector of the actual root line
\[
                         N_i=\mathcal O(aG_i'-O_i),
\]
normalize its norm to \(u_{i,j}(z)\). This is an explicit
delta-equivariant map to the principal circle over (K28.20).
Consequently its associated complex line is \(N_i\), including its
specified lift and all finite characters.

For F46 and F47 this uses the precise line maps of those propositions:
the reduced-root contractions with degree-zero exceptional restriction;
the good \(IV^*\) and \(III^*\) toric Cartier corrections; the good
III exceptional difference; and the cancelling good-II exceptional
coefficients. Each correction was proved invariant under the actual
translation \(Q\), so the comparison carries \(B_0\) and \(A_{i,0}\).
The sheet map does not replace these corrections by numerical degrees.

Here is the additional line map required for F36 and F38. On the
quadratic \(I_1^*\) root let \(S'\) be the minimal \(I_2\) model,
let \(\beta:\widehat S\to S'\) blow up the four inversion fixed
points, and let \(\pi:\widehat S\to S\) be the smooth resolved
quotient. The actual source line is
\(\mathcal M=\mathcal O(aG-O-L_0)\), with \(a=2\) or \(6\).
If \(E_0,E_1\) are the two exceptional curves at the section leaves,
the literal Cartier equalities are
\[
 \begin{split}
 \pi^*(aG-O-L_0)&=\widehat P-\widehat O-2E_0,\\
 \beta^*(P'-O')&=\widehat P-\widehat O+E_1-E_0,\\
 \beta^*N_*&=\pi^*\mathcal M+E_0+E_1 .
 \end{split}
 \tag{K28.21}
\]
The actual \(Q=bG\), \(b=2\) or \(6\), exchanges \(E_0,E_1\)
and exchanges the other two exceptional curves. Hence (K28.21)
is equivariant for the specified suspension and its affine norm lift.
The Tate character of \(N_*\) is
\[
             Z_P=v(z)^a/u(z^2)^{a/2},\qquad Z_P(0)=-1 .
 \tag{K28.22}
\]
Its transitions are units on both \(I_2\) components, and its degree is
zero on each. The full F36 norm
\(A_*^2=B_\lambda^{n_*}\) includes the retained line eigencharacter.
Applying (K28.20) with \(m_*=2\) therefore gives the actual line
\(N_*=\mathcal O(aG'-O')\), not the uncorrected pullback of
\(\mathcal M\). This proves the needed line identification even at
the two section points and all four fixed-point blowups.

On the ordinary part of the page the projection is the unramified
source pullback. At the selected nodes use the actual source-line/orbit
charts of P3F.9. The page comparison concerns that source line; the
Hopf charge around the fixed sphere is retained in the compression
and is not extended through the fixed sphere as a trivial line.
The regular-binding band construction of P3K.6 and P3F.31 applies
in the coordinate \(\beta\) of (K28.9); it keeps the base coordinate
and carries the line by the radial maps in K28.1.

We now trivialize the remaining finite-base source torsor relative
to this actual binding collar. The integral monodromy coinvariants
vanish for a direct reason in each two-cap case. For F46 and F47 let
\(v\) be the retained nodal vanishing cycle and let \(A\) be the
order-four source monodromy at III or \(III^*\). The trace calculation
in those topology proofs gives
\[
                          |\langle v,Av\rangle|=1.
 \tag{K28.23}
\]
For F38 the starred monodromy is \(-T_u\), and its product with
the retained nodal transvection \(T_v\) and the IV monodromy gives
\[
       -1=-2+\langle u,v\rangle^2,\qquad
       |\langle v,(-T_u)v\rangle|=1 .
 \tag{K28.24}
\]
The nodal meridian has trivial sheet permutation in the actual page
cover. Its conjugate by the starred or order-four meridian also
has trivial sheet permutation, even though that conjugating path
itself need not close on the page. Thus both nodal loops lift as
closed page loops. Their monodromies are \(T_v,T_{Av}\), with
images \(\mathbb Z v,\mathbb Z Av\) for \(T-1\). Equations
(K28.23)--(K28.24) make these images the entire integral elliptic
lattice. This proves zero page coinvariants without assuming that
an arbitrary branched cover preserves the original Mordell--Weil
torsion group.

Let \(C\) be the page base with its marked binding boundary,
\(j:C_{\rm reg}\to C\), and \(\Lambda\) its elliptic lattice.
The quotient \(j_*\Lambda/j_!\Lambda\) is supported at finitely
many singular points and has no first cohomology. Compact-support
Poincare duality and the preceding coinvariants give
\[
                  H^2(C,\partial C;j_*\Lambda)=0 .
 \tag{K28.25}
\]
The smooth identity-component Lie sheaf is fine. Its lattice
exponential sequence, together with the finite component sheaf
at the singular fibres, consequently gives a translation
trivialization of the actual torsor relative to the specified
binding collar. Every translation used is a section of the sheaf
of translations extending on the actual reduced resolved fibres.
The \(I_2\) root is included: its identity group is multiplicative,
its lattice at the node is the invariant \(j_*\Lambda\), and its
component quotient is the finite skyscraper just retained.

The line comparison through this smooth translation is the
rigidified fibrewise Picard comparison of P3K.26, rather than
a claimed holomorphic divisor for a merely smooth map. Over the
universal translating-section parameter, the actual Hom line
between \(N\) and its translate has trivial restriction to every
fibre. The constant-factor line uniformization proves this on the
smooth fibres. The reduced component degrees and the retained
unit transitions prove it on III, IV and \(I_2\) fibres, and
proper base change and evaluation give the relative isomorphism.
Rigidify at \(O\), then pull it back by the constructed smooth
translation section. The remaining ambiguity on the compact
base is a line pulled back from that base, with Chern class
\(kF\). Therefore
\[
                    (c_1(N)+kF)^2=c_1(N)^2,
 \qquad c_1(N)F=F^2=0 .
 \tag{K28.26}
\]
The binding restriction has zero first Chern class and extends over
the regular \(T^2\)-cap. The relative boundary gauges, including
the retained odd ones, have zero square ambiguity by P3K.5.
This completes the actual page-line comparison.

## K28.5. The signed trace and the characteristic calculation

Near the single point at infinity of (K28.13), write
\(\xi\sim c w^{-m_0}\), \(\eta\sim d w^{-m_\infty}\).
The complex boundary of the punctured page has parameter
\(-\arg w=\beta\). By (K28.12), the positive physical parameter
is exactly \(\theta=\beta\). Hence
\(\partial V=+E\times S^1_\theta\).
Orient the actual nodal compression by \(\partial W=F-E\).
Its rotated product attaches to give a trace with
\(\partial X=+F\times S^1_\theta\).

In the actual Hopf chart the ambient orientation is
\(\operatorname{or}(F)\operatorname{or}(\nu_{\rm Hopf})\,dr\,d\theta\),
whereas the trace orientation is
\(\operatorname{or}(F)\,dr\,d\theta\).
Moving the three normal directions past the last two is even.
The induced normal sphere is therefore the positive Hopf sphere
and its actual Euler line satisfies \(\pi_*x=+1\).
This is the full signed Thom comparison, for both
\(\varepsilon=1\) and \(\varepsilon=-1\). Any source-product
orientation reversal in the three-sphere map is already included
in this normal comparison and introduces no additional sign.

The two outer-boundary/Jin reversals are the ones proved in
P3K.7. Its actual trace bordism, with the page-line map just
constructed, gives
\[
            A^{\rm Jin}
              =\frac{12\,c_1(N)^2-p_1(TS_{\rm page})}{24}.
 \tag{K28.27}
\]
The compression cap and the regular elliptic cap have the exact
boundary line comparison of P3K.5--7, zero signature, and zero
line-square ambiguity. Thus the right side may be computed on
the compact sectioned elliptic page. This uses the displayed
relative maps, not a holomorphic compactification of the original
parameter family.

Let the original capped Euler numbers be \(e_\infty,e_0\),
and the actual minimal root Euler numbers be
\(e_\infty',e_0'\). There are \(m_0\) copies of the first root
and \(m_\infty\) of the second. Every other fibre is unramified.
Consequently
\[
 \chi(\mathcal O_{S_{\rm page}})
   =\frac{M(12-e_\infty-e_0)
            +m_0e_\infty'+m_\infty e_0'}{12}.
 \tag{K28.28}
\]
Its signature is \(-8\chi\) and its tangent Pontryagin number is
\(-24\chi\). The actual marked line section \(aG'\) meets the
identity component at every remaining reducible fibre and at
each reduced root in the listed cases; good roots are irreducible.
The height base-change formula, with \(h(G)=1/d\), gives
\[
 h(aG')=\frac{Ma^2}{d}
       =2\chi+2(P_{aG'}\cdot O),\qquad
 c_1(N)^2=-\frac{Ma^2}{d}.
 \tag{K28.29}
\]
For the quadratic starred line this formula uses \(N\) from
(K28.21), so no root correction from \(-L_0\) is omitted.
Combining the actual comparison with (K28.27) yields
\[
                    A^{\rm Jin}
                         =\chi-\frac{Ma^2}{2d}
                         =-P_{aG'}\cdot O .
 \tag{K28.30}
\]

## K28.6. All joint return values and the one-star specialization

The following tables are evaluated only on the sphere tuples
\(D=\pm1\), with the exact signed parameter (K28.2). For each
fixed row and fixed root orders, both determinant signs give
the displayed integer. The actual proof of this equality of
signs is (K28.4)--(K28.27).

For the E6 source of F46, \(d=6\), the other source fibre is
the selected \(I_1\), and the values are:

| \((a,b)\) | \(m_\infty\) at \(IV^*\) | \(m_0\) at III | Actual \(A^{\rm Jin}\) |
|---|---|---|---|
| \((1,6)\) | \(3l\), good | \(4k\), good | \(0\) |
| \((2,3)\) | \(3l\), good | \(4k+1\), reduced III | \(-3lk\) |
| \((3,2)\) | \(3l+2\), reduced IV | \(4k\), good | \(-4k(2l+1)\) |
| \((6,1)\) | \(3l+2\), reduced IV | \(4k+1\), reduced III | \(-35lk-8l-22k-5\) |

The good-root indices are positive and the reduced-root indices
are nonnegative. The unit determinant also retains every
coprimality restriction; for example the third row requires
\(3l+2\) odd. These restrictions are not removed from the table.

For the E7 source of F47, \(d=2\), the other source fibre is again
the selected \(I_1\):

| \((a,b)\) | \(m_\infty\) at \(III^*\) | \(m_0\) at II | Actual \(A^{\rm Jin}\) |
|---|---|---|---|
| \((2,1)\) | \(4l+3\), reduced III | \(6k+1\), reduced II | \(-22lk-3l-15k-2\) |
| \((2,1)\) | \(4l+3\), reduced III | \(6k\), good | \(-k(22l+15)\) |
| \((1,2)\) | \(4l\), good | \(6k+1\), reduced II | \(-4lk\) |

The fourth formal root combination, good \(III^*\) and good II,
has both orders even. Its determinant is even and it contains
no sphere tuple. No sphere return class is assigned to it.

For F38, the source is \(I_1^*+IV+I_1\), with \(d=12\).
At infinity \(m_\infty=2\), the actual root is \(I_2\),
and \(e_\infty'=2\). Its page consists of \(m_0\) copies of this
root and two copies of the IV root. The two sectors are:

| \((a,b)\) | \(m_\infty\) at \(I_1^*\) | \(m_0\) at IV | Actual \(A^{\rm Jin}\) |
|---|---|---|---|
| \((6,2)\) | \(2\), root \(I_2\) | \(6l+1\), reduced IV | \(-16l-2\) |
| \((2,6)\) | \(2\), root \(I_2\) | \(3k\), good, \(k\) odd | \(0\) |

Here the sphere equation is \(m_0n_\infty+2n_0=\pm1\).
It forces \(m_0\) odd; together with the reduced root domain
\(m_0\equiv1\pmod3\), this gives the stated \(6l+1\).
Equation (K28.28) is \(\chi=(2m_0+e_0')/6\).
In the reduced row (K28.29) gives
\(c_1(N)^2=-6m_0\), and hence
\(A=(2-8m_0)/3=-16l-2\). In the good row it gives
\(h(aG')=2m_0/3\) and \(\chi=m_0/3\), hence zero.

Finally consider the single quadratic \(I_1^*\) cap of F36
on either \(I_1^*+I_3+2I_1\) or \(I_1^*+IV+I_1\).
Here \((a,b)=(6,2)\), \(\lambda=r^2\), and \(n=\pm1\).
The exact one-cap map of K26, with \(m=2\), gives the complex
page \(\eta-\tau\xi^2=1\) and the positive Hopf angle \(n\gamma\).
The root sheet and its actual line are precisely (K28.20)--(K28.22).
The integral page coinvariants vanish by the one-cap argument
of K26: the retained meridians recover the whole source
monodromy, and a nonzero prime quotient of its coinvariants
would give a nonzero rational torsion section, contradicting
the proved source Mordell--Weil group \(\mathbb Z\).
Thus the same relative line and signed Thom maps apply.
The Euler count is
\[
              \chi=\frac{2(12-7)+2}{12}=1,\qquad
              h(6G')=\frac{2\cdot36}{12}=6 .
\]
The remaining \(I_3\) or IV component correction is zero for
\(6G'\). It follows that the actual return is
\[
                       A^{\rm Jin}=-2
 \tag{K28.31}
\]
for either norm sign and for both source profiles.

By the exact transfer P3F.22, the physical Hopf-gluing class of
every row is \(A^{\rm Jin}\bmod28\), with
\(\mu=A^{\rm Jin}/28\bmod\mathbb Z\). A nonzero residue has the
nonproduct mapping torus proved in P3F.24. The present proof
uses the actual norm, page, line and trace maps before applying
that transfer.

## Certificate and scope

The executed certificate code/part3/joint_additive_returns.py records
the exact phase matrix and determinant, both cap-cut identities,
the origin difference, the sheet-orbit gcd calculation, the
Riemann--Hurwitz genus, and every arithmetic polynomial in the
tables. Its JSON links the actual construction and integral topology
proofs. The proof of the global maps and line identification is
the text above; finite numerical samples do not replace it.
