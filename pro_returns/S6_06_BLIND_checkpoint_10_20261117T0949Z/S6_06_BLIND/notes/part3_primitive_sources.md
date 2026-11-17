# Primitive-translation sources and the exact orbit filling

## P3K.22. Proved: ten primitive-translation sphere families and their smooth-cap obstruction

For the following ten source profiles, let \(G\) be the marked
primitive Mordell--Weil generator, put \(d=1/h(G)\), and choose
\(M=\mathcal O(dG-O)\), translation \(Q=G\), a simple whole-fibre
zero at an \(I_1\), and one order-one logarithmic gluing with gamma
coefficient \(+1\) at a smooth source fibre.  Use the standard
vertical-edge unimodular cusp fan.  These are compact complex
threefolds diffeomorphic to \(S^6\).  Their positive scalar-parameter
loops have the indicated Jin integer and oriented \(\Theta_7\) class.

| OS row | Source profile | d | Jin integer A | Class mod28 |
|---|---|---|---|---|
|45|\(I_8+4I_1\), \(I_8+II+2I_1\)|8|−3|25|
|47|\(I_7+I_2+3I_1\), \(I_7+I_2+II+I_1\), \(I_7+III+2I_1\)|14|−6|22|
|55|\(I_5+I_4+3I_1\), \(I_5+I_4+II+I_1\)|20|−9|19|
|56|\(I_5+I_3+I_2+2I_1\), \(I_5+I_3+III+I_1\), \(I_5+IV+I_2+I_1\)|30|−14|14|

The compact page is the indicated rational elliptic surface itself.
Its line is \(M\), with square \(-d\), and
\((dG)\cdot O=(d-2)/2\).  Every displayed mapping torus is therefore
not diffeomorphic to \(S^1\times S^6\), by the same oriented
mapping-torus detection used in P3K.10 and P3F.25.

There is also a restriction on additional smooth-site caps for these
primitive sources.  After the actual finite-kernel cancellation of
P3K.19, let their primitive cap data be
\((m_i,n_i,\lambda_{ai},\lambda_{bi})\), with
\(\gcd(m_i,n_i)=1\).  The exact orbit Mayer--Vietoris computation
below gives, whenever its first-homology gluing matrix is unimodular,
\[
        H_2(Y;\mathbb Z)=\bigoplus_i(\mathbb Z/m_i)^2.       \tag{P3K.22.1}
\]
Consequently a sphere member with only such smooth-site modifications
has \(m_i=1\) at every site.  For order-one sites the total gamma
coefficient \(\sum n_i=\pm1\) gives sphere topology, including
arbitrary integral source and delta collar coefficients.  The
individual index table above specifies the one-site positive-gamma
family; it does not identify uncomputed singular-source cap choices
with this family.

**Proof: the source automorphisms and the line lift.**
P3F.1 constructs the source surfaces, and P3F.2 fixes their component
markings and proves \(G\cdot O=0\).  Translation and inversion
extend over their resolved singular fibres.  One direct proof keeps
the actual rational maps.  On the generic Weierstrass fibre use its
chord-and-tangent addition and \((x,y)\mapsto(x,-y)\).  Both preserve
the invariant differential up to the constant sign of inversion.
On a rational minimal elliptic surface the form
\((dx/y)\wedge dt\) has canonical divisor \(-F_\infty\), after a
base frame is chosen; the local minimal resolutions preserve this
relative differential.  Resolve the graph of either rational map,
with projections \(p,q:Z\to S\).  They are maps over the same base.
Pulling back that differential gives
\[
 -p^*F_\infty+E_p=-q^*F_\infty+E_q,
 \qquad p^*F_\infty=q^*F_\infty.
\]
Here the Jacobian discrepancy divisors have strictly positive
coefficient on every exceptional curve of their respective
compositions of point blowups.  Thus \(E_p=E_q\), so both
projections contract exactly the same curves and connected fibres.
The graph maps descend in both directions, giving mutually inverse
holomorphic automorphisms of \(S\).  This proves the required
extension, including II, III and IV fibres.  On an \(I_N\) chain
the actual Tate map is multiplication by the section unit and a
shift by its component label.  On III and IV, translation acts on
the dense smooth parts by addition in the component groups of
orders two and three; it therefore permutes the resolved components
by those same labels.  Inversion conjugates translation by \(G\)
to translation by \(-G\) on the whole surface.

The point \(dG\) is in the identity component at every reducible
fibre in the table.  Thus \(M\) has multidegree zero there.
The height identity gives
\((dG)\cdot O=(d-2)/2\), and its actual divisor class satisfies
\[
 (t_G)_*[M]-[M]=[F],\qquad t_G^*M\cong M(-F).           \tag{P3K.22.2}
\]
These equalities are also checked directly in the integer matrices
below.  The numerical equality is an equality of line bundles
because the rational surface has \(\operatorname{Pic}^0(S)=0\).
The resulting Hom line is \(\pi^*\mathcal O_{\mathbb P^1}(1)\).
Choose its section with its unique zero at the selected nodal fibre.
This gives the actual holomorphic lift with a simple whole-fibre
zero.

For an explicit meromorphic frame of that lift, put \(P_j=jG\).
On the generic cubic the quotient of the chord through
\(P_d,-G\) by the vertical line through \(P_{d-1}\) has divisor
\(P_d+(-G)-P_{d-1}-O\).  It is exactly the fibre divisor of
\(M\otimes(t_G^*M)^{-1}\).  Its remaining vertical orders form
whole fibres, since the component degrees vanish.  Multiplying by
the rational base function that moves this degree-one divisor to the
chosen \(I_1\) supplies the preceding section.  Thus its frame and
all local multipliers are obtained from the stated rational addition
map, rather than from an unspecified linearization.

For sufficiently small \(|\lambda|\), multiply this lift by
\(\lambda\).  In a fixed Hermitian metric it is uniformly strictly
contracting, away from its prescribed zero where the Mumford charts
are used.  Quotienting the nonzero line by its iterates is therefore
free and proper.  At the zero the actual valuation periods are
\((1,0),(0,1)\); the standard vertical-edge fan gives the smooth
index-one filling with its one fixed \(\mathbb P^1\), of normal
weights \((-1,+1)\).  The chart and line-gluing formulas are the
same ones used in P3K.10, with the present holomorphic unit logarithms
\(\Gamma,C\).  In particular, on a universal scalar-parameter
chart its cusp period and two origins are
\[
 \begin{aligned}
 \gamma&=(\Gamma,C+s+v),\\
 \sigma&=(\Gamma v,Cv+(v^2-v)/2),\\
 o&=(-\Gamma s,-Cs-s^2/2-sv),
 \end{aligned}                                                     \tag{P3K.22.3}
\]
and the closing ordinary line gauge is \(-s\delta\).  The exact
identities
\[
 \sigma(v+1)-\sigma(v)=\gamma-s\delta,
 \quad (\sigma-o)(v+\theta)-(\sigma-o)(v)
      =\theta\gamma+\tfrac12\theta(\theta-1)\delta
\]
hold for these actual units.  The degree-two cusp root used in
P3K.10 retains the half-integral ordinary-origin term and its integral
deck.  The smooth order-one cap is glued by
\((\log q)/(2\pi i)\,\gamma\); its scalar closing gauge is the
same actual base function used above.  Thus the gluing is holomorphic
in the scalar parameter and closes on its positive loop.  All filled
pieces are proper over their base discs; the contraction shell gives
properness on their common complement.  The compact base gives
compactness.  This establishes the analytic construction and the
positive-gamma parameter direction needed for the index calculation.

**Proof: every integer matrix of the source mapping torus.**
Use the divisor basis
\[
 O,F,\{C_{i,j}:1\le j<N_i\},G,
\]
where \((N_i,k_i)\) is respectively
\((8,3)\), \((7,2),(2,1)\), \((5,2),(4,1)\), or
\((5,1),(3,1),(2,1)\).  A root \(A_1\) may denote III and
a root \(A_2\) may denote IV; their displayed component intersection
and permutation matrices are unchanged.  The Gram matrix has
\(O^2=G^2=-1\), \(O\cdot F=G\cdot F=1\),
\(G\cdot C_{i,j}=\delta_{j,k_i}\), root blocks
\(-A_{N_i-1}\), and all other entries zero.  Its determinant is
minus one in every case.  Since \(H_2(S;\mathbb Z)\) is free
unimodular of rank ten, these classes are an integral basis.

Let \(R_j\) be the vector whose \(i\)-th root block is column
\(jk_i\bmod N_i\) of \(A_{N_i-1}^{-1}\), or zero for component
zero.  Put
\[
 \varphi=G-O-F+R_1,\quad
 P_j=O+(P_j\cdot O+1)F+j\varphi-R_j,
 \quad
 P_j\cdot O=\frac{j^2/d-2+\sum_i\operatorname{contr}_i(jG)}2.
\]
The actual pushforward matrix \(T=(t_G)_*\) is now specified
column by column: \(O\mapsto G\), \(F\mapsto F\),
\(G\mapsto P_2\), and
\(C_{i,j}\mapsto C_{i,j+k_i}\), with
\(C_{i,0}=F-\sum_{j>0}C_{i,j}\).  All columns are integral.
The executed program verifies \(T^t\mathcal G T=\mathcal G\) and
\[
 \operatorname{Smith}(T-I)=(1,1,1,1,1,1,1,1,1,0),
 \quad\ker(T-I)=\mathbb ZF,
 \quad\operatorname{coker}(T-I)=\mathbb Z[O].             \tag{P3K.22.4}
\]
It exports every ten-by-ten matrix in
`code/part3_fourfold/primitive_source_translation.json`.

There is also a direct primitive-presentation check.  In the
coinvariants the components of each fibre become one class \(c_i\),
with \(N_i c_i=F\), and \(G=O\).  The remaining section relation
has coefficient \(P_2\cdot O-1\) on \(F\) and coefficient
\(\sum_j(2R_1-R_2)_{i,j}\) on \(c_i\).  Its Schur complement is
\(1/d\), while \(\prod_iN_i=d\).  The resulting determinant is
therefore \(\pm1\), not merely nonzero rationally.  For the four
rows the determinants are respectively \(-1,1,1,-1\).

The actual contracting lift covers \(t_{-G}\).  Its source matrix
has the same image and kernel, since
\(T^{-1}-I=-T^{-1}(T-I)\).  The mapping torus
\(W=T_{-G}(S)\) has the cellular cone complex with groups
\(\mathbb Z,\mathbb Z,\mathbb Z^{10},\mathbb Z^{10},
\mathbb Z,\mathbb Z\) in degrees zero through five; the sole
nonzero differential is \(T^{-1}-I:C_3\to C_2\).
Thus each \(H_i(W)\), \(0\le i\le5\), is \(\mathbb Z\),
and \(\pi_1(W)=\mathbb Z\gamma\).

The actual delta quotient before logarithmic gluing is this marked
mapping torus.  On its ordinary part the Hermitian logarithmic norm
is the suspension coordinate, as in P3K.13.  At the chosen \(I_1\),
the section \(G\) has a nonzero holomorphic Tate-unit representative
\(g(q)\).  Choose its logarithm on the disc.  The isotopy
\(Z\mapsto g(q)^u Z\) has node-chart formula
\((x,y)\mapsto(g(q)^u x,g(q)^{-u}y)\), so it extends through the
node for every real \(u\).  It identifies the source mapping torus
with the same \(I_1\)-surface-times-circle product of P3F.9, on
the actual boundary collar.  The bounded line units alter only the
logarithmic-norm coordinate and give the same product map.  This
supplies the comparison across the cusp, including its source
translation, rather than replacing that piece by a different fill.

**Proof: the primitive rim bases and the decisive involution.**
Remove \(r\) disjoint regular-fibre tubes
\(N_i=T^2\times D^2\times S^1_\gamma\) from \(W\), and call
the complement \(V\).  Write their boundary bases
\((a_i,b_i,\alpha_i,\gamma)\), with \(\alpha_i\) the positive
base meridian.  The Thom maps
\(H_j(W)\to\bigoplus_iH_{j-2}(T^3)\) are, in descending degrees,
\[
 \begin{array}{c|c}
 j&\text{map}\\\hline
 5&1\longmapsto(1,\ldots,1)\text{ in the }ab\gamma\text{ columns}\\
 4&1\longmapsto(ab)_1+\cdots+(ab)_r\\
 3&0\\
 2&1\longmapsto(1,\ldots,1).
 \end{array}                                                     \tag{P3K.22.5}
\]
For the zero map, the dual inclusion \(H_2(N_i)\to H_2(W)\)
is zero: the invariant class \(F\), which pairs one with \([O]\),
is pulled back from the source base and restricts to zero on the
whole tube core.  The other maps follow from the oriented fibre and
section intersections.  They are primitive diagonal maps.

The Thom sequence now gives free groups
\[
 H_1(V)=\mathbb Z^r,\quad H_2(V)=\mathbb Z^{3r},
 \quad H_3(V)=\mathbb Z^{3r},\quad H_4(V)=\mathbb Z^{r-1}.
\]
In degree two an integral basis is exactly
\(A_i=a_i\alpha_i,B_i=b_i\alpha_i,C_i=\alpha_i\gamma\).
In degree one use \(\gamma,\alpha_1,\ldots,\alpha_{r-1}\), with
\(\alpha_r=-\sum_{i<r}\alpha_i\).  In degree three use
\(z=ab\gamma\), the \(r-1\) independent classes \(ab\alpha_i\),
and all \(a_i\alpha_i\gamma,b_i\alpha_i\gamma\).  In degree four
use \(r-1\) boundary fundamental classes with their one sum relation.

The remaining boundary coefficients are fixed by an actual smooth
involution.  Inversion on the source conjugates the suspension map
to its inverse, so
\[
                         I(p,u)=(-p,-u)                         \tag{P3K.22.6}
\]
is a well-defined diffeomorphism of its mapping torus and preserves
every removed tube.  In a tube choose a real lift of the local
section and write its mapping-torus trivialization as
\(p'=p+uQ\), where \(Q\) is its signed suspension translation.
Then (P3K.22.6) is literally \((p',\alpha,u)\mapsto(-p',\alpha,-u)\).
Thus \((a,b,\alpha,\gamma)\mapsto(-a,-b,\alpha,-\gamma)\).
Every degree-two rim basis vector is odd, whereas
\(ab,a\gamma,b\gamma\) are even.  Naturality forces each image
of an even class to be two-torsion in \(H_2(V)\).  This group is
free by the primitive Thom calculation, so every such image is zero.
In particular the previously undetermined boundary linking integers
are exactly zero integrally.

The same argument gives the full degree-three boundary map.
The three rim classes \(ab\alpha,a\alpha\gamma,b\alpha\gamma\)
are even.  Each \(ab\gamma\) is odd and projects to the same
generator of \(H_3(W)\).  Subtracting two of them gives both an
odd class and a class in the even rim subgroup; freeness again
forces equality.  This proves the basis description and every
boundary coefficient used next.

**Proof: the actual cap maps and all Mayer--Vietoris matrices.**
On the orbit boundary a primitive smooth cap has meridian
\[
 \mu_i=m_i\alpha_i+n_i\gamma+\lambda_{ai}a_i+\lambda_{bi}b_i.
\]
The coefficient vector is the full cyclic norm from P3K.15; no
source-period term is discarded.  The smooth root source, followed
by its extending translation and base rotation, is a mapping torus
of a disc-times-torus diffeomorphism isotopic to the identity by
those explicit rotations and translations.  It is therefore
\(T^2\times D^2\times S^1\), with the displayed marked meridian.
Choose integers \(r_i,s_i\) with \(r_im_i+s_in_i=1\).
The four columns
\[
 a_i,\ b_i,\ \mu_i,\ \kappa_i=-s_i\alpha_i+r_i\gamma
\]
form an integral determinant-one basis.  Let \(Q_i\) be the
matrix of its inverse with the meridian row deleted.  Then
\(Q_i:\mathbb Z^4\to\mathbb Z^3\) is the actual cap inclusion
on first homology, and its higher maps are exactly
\(\bigwedge^jQ_i\).

For the exterior, in boundary wedge order
\((ab,a\alpha,a\gamma,b\alpha,b\gamma,\alpha\gamma)\), the
degree-two block is
\[
 i_2=\begin{pmatrix}
 0&1&0&0&0&0\\0&0&0&1&0&0\\0&0&0&0&0&1
 \end{pmatrix}.
\]
The degree-one map sends \(a_i,b_i\) to zero, \(\gamma\) to
the common gamma generator, and \(\alpha_i\) to the meridians with
their stated one sum relation.  The degree-three map in wedge order
\((ab\alpha,ab\gamma,a\alpha\gamma,b\alpha\gamma)\) sends
these columns to the corresponding rim class, the common \(z\),
and the two displayed independent rim classes.  The degree-four
map is \((I_{r-1}\mid-\mathbf1)\).  These descriptions specify
every entry of the integral matrices \(i_j\).

The Mayer--Vietoris map in degree \(j\) is the block matrix
\(D_j=\begin{pmatrix}i_j\\-\bigoplus_i\bigwedge^jQ_i\end{pmatrix}\); in degree zero it
is the column-incidence matrix \((\mathbf1,-I_r)^t\).
For one positive order-one cap with zero source collar coefficients,
the three nontrivial square matrices are explicitly
\[
 D_1=\begin{pmatrix}
 0&0&0&1\\-1&0&0&0\\0&-1&0&0\\0&0&1&-1
 \end{pmatrix},\qquad
 D_3=\begin{pmatrix}
 0&1&0&0\\0&0&1&0\\0&0&0&1\\1&-1&0&0
 \end{pmatrix},
\]
\[
 D_2=\begin{pmatrix}
 0&1&0&0&0&0\\0&0&0&1&0&0\\0&0&0&0&0&1\\
 -1&0&0&0&0&0\\0&1&-1&0&0&0\\0&0&0&1&-1&0
 \end{pmatrix}.
\]
All three are unimodular.  The degree-four domain is \(\mathbb Z\)
with zero target, giving the oriented top class of \(Y\).  Thus
\(H_*(Y;\mathbb Z)=H_*(S^5;\mathbb Z)\).

For general smooth-site data, eliminating the cap degree-two groups
leaves the exact block presentation
\[
 \begin{pmatrix}
 m_i&0&0&\lambda_{ai}\\
 0&m_i&0&\lambda_{bi}\\
 0&0&m_i&-n_i
 \end{pmatrix}                                                   \tag{P3K.22.7}
\]
on \((A_i,B_i,C_i)\).  Its cokernel is
\((\mathbb Z/m_i)^2\), since \(n_i\) is a unit modulo \(m_i\).
The first-homology determinant is the signed Seifert determinant
\(D=\sum_i n_i\prod_{j\ne i}m_j\), and the degree-three
determinant has the same absolute value.  These identities, every
matrix \(D_0,\ldots,D_4\), and 196 primitive two-cap cases with
nonzero source collars are executed and exported by
`code/part3_fourfold/primitive_orbit_filling.py` and its JSON.
This proves (P3K.22.1), including its torsion.

For order-one sites the fundamental-group calculation is equally
explicit.  The complement of the source fibres has fundamental
group generated by their base meridians: all elliptic cycles die
as in the rational source, and the section supplies the only sum
relation.  Thus
\(\pi_1(V)=\langle\alpha_i,\gamma\mid
\alpha_1\cdots\alpha_r=1,[\alpha_i,\gamma]=1\rangle\).
The cap imposes \(\alpha_i\gamma^{n_i}=1\); its source loops
already die.  Hence \(\pi_1(Y)=\mathbb Z/|\sum_i n_i|\), which
is zero for the stated sphere data.  The source meridian assertion
can also be checked directly: the missing meridian of a single
regular fibre bounds the punctured zero section, and van Kampen
recovers \(\pi_1(S)=0\).

**Proof: the actual Hopf filling and its six-dimensional homology.**
In the one-site construction \(Y\) is simply connected with the
integral homology of \(S^5\), hence is the standard oriented
five-sphere by the same smooth classification used for P3F.9.
The fixed curve is the actual embedded sphere furnished by the
index-one cusp chart.  Its normal Hopf meridian has Euler value one.
For \(P=Y\setminus\operatorname{int}\nu F\), Alexander duality
gives \(H^*(P;\mathbb Z)=H^*(S^2;\mathbb Z)\); the circle
bundle on \(P\) therefore has \(H_*(E)=H_*(S^3)\) by the
integral Gysin sequence.  The meridian value one makes
\(\pi_2(P)\to\pi_1(S^1)\) surjective, so \(\pi_1(E)=0\).

The other piece of \(X\) is \(F\times D^4\), with boundary
\(F\times S^3\).  The positive-weight SU(2) normal trivialization
of the actual \(\mathcal O(-1)\oplus\mathcal O(-1)\) chart gives
this product and its Hopf map.  Its Mayer--Vietoris matrices are
\((1,-1)^t\) in degree zero, \((-1)\) in degree two,
\((1)\) in degree three, and the zero map from \(\mathbb Z\)
in degree five.  All omitted groups are zero.  Therefore
\(H_*(X;\mathbb Z)=H_*(S^6;\mathbb Z)\) and van Kampen gives
\(\pi_1(X)=0\).  The already used smooth six-sphere classification
and \(\Theta_6=0\) identify this actual smooth manifold with
\(S^6\).  The same calculation excludes the nonzero torsion in
(P3K.22.1) from a sphere member; the quotient of a semifree sphere
with this fixed sphere must have zero such torsion.

**Proof: the actual page and the signed return.**
The order-one gamma gluing makes the orbit base the ordinary Hopf
\(S^3\), by the signed meridian matrix of P3K.16.  Its regular
binding page has degree one over the source base.  The norm shell
of \(M^\times\) maps injectively into the orbit: a positive iterate
strictly decreases its norm, and a negative iterate increases it.
At the whole-zero cusp the line graph is horizontal and lies in
the chosen standard fan; its successive suspension translates have
strictly increasing graph defect one, so no new identification of
this shell occurs there.  It is disjoint from the delta fixed
sphere.  On the smooth logarithmic collar the displayed log-gamma
map is the exact inverse angular coordinate, so the shell closes
as the page \(S\setminus\operatorname{int}\nu F\), with its
original source line \(M\).  This is the same actual norm-shell
and binding-collar comparison proved for OS45 in P3K.10; all its
maps here use the present \(\Gamma,C\), and no finite cap or
component-supported zero is introduced.

Thus the capped page is \(S\), of \(\chi(\mathcal O)=1\) and
signature \(-8\), while its line square is
\(M^2=-2-2(dG\cdot O)=-d\).  The real compression, meridian-line
comparison and signed characteristic calculation of P3K.6--7 apply
to this actual page and give
\[
 A=\frac{12M^2-p_1(S)}{24}
   =1-\frac d2=-\frac{d-2}{2}.                        \tag{P3K.22.8}
\]
The identities (P3K.22.3) identify one positive scalar-parameter
loop with one positive gamma turn, retaining the integral line
gauge and the degree-two cusp-origin root.  Hence (P3K.22.8)
computes the stated actual loop, with no unproved division by a
parameter cover.  The orientation dictionary of P3K.7 and P3F.25
reduces this integer to the classes in the table.  This proves all
the asserted source, topology, page and return claims.
**End of proof.**

The statement supplies ten explicit sphere families and an exact
obstruction to additional smooth finite caps in this primitive-source
scope.  Singular-source cap replacements and arbitrary cusp-fan return
changes retain their separate actual comparisons; they have not been
identified with these examples by the source-lattice calculation.
