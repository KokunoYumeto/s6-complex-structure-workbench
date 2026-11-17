# P3K.24. The actual reduced-III page and positive parameter return

Status: proved. The physical-character arrow, actual page and line
maps, and signed Thom comparison have passed root and independent
audits. This note continues P3F.37's construction and complete
integral topology. The earlier working statuses and origin convention
are retained in the dated historical records cited below.

Fix m=4l+3, l>=0, and the source
\[
 S:\ y^2=x^3+tx+1,\quad G=(0,1),\quad
 M=\mathcal O(2G-O),\quad Q=G.
\]
Use the single reduced-III cap with A_r^m=B_{r^m}, in the marked
single-A cut convention, and choose one of the three I1 fibres as
the simple whole-fibre zero. The parameter is r, with lambda=r^m.
The same argument below also treats the explicit second source
\[
 S':\ y^2=x^3+tx-t,\quad G=(1,1),
\]
whose fibres are III* at infinity, II at zero, and I1 at -27/4.
The precise root and source-complement extension for this second
source is recorded at the end.

## III-R.1. The exact positive angular clutch

Let t_c be the selected I1 value, q=t-t_c,
s=log(q)/(2pi i), and v=log(r)/(2pi i). The actual multiplier
of the suspension line in the chosen cusp frame is
exp(2pi i C(q)) q r^m. Use the physical source Abel coordinate
a=zeta_1 and the physical line character V=exp(2pi i zeta_2).
Let g(q) be the holomorphic Tate logarithm of +G. The contracting
line map and its inverse act exactly by
\[
 \begin{aligned}
 B(a,V)&=(a-g,\ e^{2\pi i C}q r^m V),\\
 B^{-1}(a,V)&=(a+g,\ e^{-2\pi i C}q^{-1}r^{-m}V).
 \end{aligned}
\]
The positive outward suspension period is consequently
\[
 \gamma_{\rm out}(s,v)=\binom{g(q)}{-C(q)-s-mv},\qquad
 \delta=\binom01,
\]
and it represents B^{-1}, exactly the positive gamma used in the
norm-shell meridian and the weighted Seifert page. Delta is the
positive physical scalar rotation; neither circle has been silently
inverted. The actual ordinary-to-cap cochain square in the
construction note makes the positive parameter deck
(v,zeta)->(v+1,zeta+s delta). Its inverse closing map multiplies
the physical line by (t-t_c)^{-1}. Indeed F_c:ordinary->cap has
g_c(s_infty+1)=Dg_c(s_infty)+a_c, hence its scalar change is
(c-c_0)s_infty delta/m. The identity cap closing gives
F_c^{-1}F_{c+m}=+s_infty delta. Its global multiplier is
(t-t_c)^{-1}; the positive deck is the inverse multiplier.

Use the auxiliary cusp cover q=Q_0^{2m}. The two extending origins
are
\[
 o(s,v)=\binom{-g s/m}{Cs/m+s^2/(2m)+sv},\qquad
 \sigma(s,v)=\binom{g v}{-Cv-m(v^2-v)/2}.
\]
Their exact differences are
\[
 \begin{aligned}
 o(s,v+1)-o(s,v)&=s\delta,\\
 \sigma(s,v+1)-\sigma(s,v)&=s\delta+\gamma_{\rm out}(s,v),\\
 o(s+2m,v)-o(s,v)&=-2\gamma_{\rm out}(s,v)+2m\delta,\\
 \sigma(s+2m,v)-\sigma(s,v)&=0.
 \end{aligned}                                                   \tag{III-R.1}
\]
The factor 2 in this auxiliary cusp cover is retained: m is odd,
and the difference for s->s+m would contain +m delta/2.
The discrepancies in (III-R.1) are actual integral periods.
The cusp origin sigma has bounded characters in q and hence extends
in the actual unimodular cusp charts. Subtracting o removes the
parameter deck on the ordinary collar. For every nonzero q its
remaining multiplier is an invertible unit times r^m; the actual
m-node parameter chain, with charts X_iY_i=r and
X_i=V/r^i, Y_i=r^{i+1}/V, gives the other extending origin.
These are two collar comparisons, with no asserted two-variable
proper analytic corner.

Their difference is
\[
 F(s,v)=\binom{g(s/m+v)}
 {-C(s/m+v)-(s+mv)^2/(2m)+mv/2}.
\]
Direct subtraction gives
\[
 F(s,v+\theta)-F(s,v)
   =\theta\gamma_{\rm out}(s,v)-\frac m2\theta(\theta-1)\delta.
                                                               \tag{III-R.2}
\]
The last coefficient is zero at both endpoints. Its exponential is
a periodic unitary gauge, homotopic through endpoint-fixed gauges
to the constant gauge. It disappears in the delta-circle quotient.
Under the retained cusp deck s->s+2m, this angular difference changes
by -2m theta delta. Its line transition has winding -2m. Consequently
the actual positive r-loop makes one positive gamma turn, with the
outward B^{-1} marking verified above. It is not an m-fold positive
gamma turn. The earlier inward-character origins and inverse-closing
paragraph are retained verbatim in
records/pre_gamma_dictionary_20261117T070909Z_part3_reduced_iii_return.md;
the complete physical-character square in this section supersedes
them. No earlier family's closing arrow is used to select this sign.

## III-R.2. The marked Seifert space and its page

The ordinary quotient by the source elliptic direction has coordinates
(t,gamma). At the cap put q_infty=1/t and use the actual root variable
z, q_infty=z^m, and compatible positive norm coordinate u. The
single-A cut convention is
\[
 (z,u)\sim(\zeta_m z,u-1),\qquad
 u=m\gamma-\arg(q_\infty)/(2\pi).
\]
This is precisely the weighted circle fibration on the standard
three-sphere with weights (1,m). Here is an explicit map retaining
the sign and meridian. Let R(z)>0 be the unique solution of
\[
 R^2+|z|^2R^{2/m}=1.
\]
Send (z,u) to
\[
 (z_1,z_2)=
 \bigl(zR^{1/m}e^{2\pi i u/m},\ R e^{2\pi i u}\bigr)\in S^3.
                                                               \tag{III-R.3}
\]
The two factors from (z,u)->(zeta_m z,u-1) cancel exactly.
The inverse on the cap is obtained by choosing a real argument of
z_2 and then recovering z; a different choice is exactly that
equivalence. The base coordinate is t=z_2/z_1^m and the positive
gamma action is (z_1,z_2)->(e^{2pi i theta}z_1,
e^{2pi i m theta}z_2). Thus q maps to -h and gamma to m h,
as in the construction's degree-one gluing matrix.

Choose a regular binding at t=t_* close to, but distinct from,
t_c. Its positive Milnor function is z_2-t_*z_1^m. The affine
page is the graph
\[
 b-t_*a^m=1,
\]
embedded in S^3 by (a,b)->(rho a,rho^m b), where rho>0 is
the unique solution of rho^2|a|^2+rho^{2m}|b|^2=1.
Its inverse divides by the positive m-th root of the Milnor
function on the selected argument page. Its projection is exactly
\[
                         t=t_*+a^{-m}.                \tag{III-R.4}
\]
The compactification is P1_a. It is branched to order m at a=0
(the additive cap) and a=infinity (the regular binding). The open
page C^o is a disc, with one boundary circle at the binding. The
chosen cusp and every other finite source critical value are
unramified. Each has m preimages. This retains the regular-binding
cover; a cover branched instead at the cusp is a different map.

## III-R.3. The actual cap slice and line on the page

The full cap orbit is the actual mapping torus of a_0 on the
resolved root source, in the same norm coordinate u. In (III-R.3),
the page equation is
\[
 2\pi u+\arg(1-t_*z^m)=\varphi\pmod{2\pi}.
\]
Choose the small cap disc so the displayed argument has a single
real branch. Its lifts are the graphs
\[
 u=u_0(z)+j,\quad
 u_0(z)=\varphi/(2\pi)-\arg(1-t_*z^m)/(2\pi),\quad j\in Z.
\]
The actual A_r map sends one graph to the next while applying
a_0 to its source point. Every orbit has a unique representative
on j=0: the function u_0 is invariant under z->zeta_m z, so
two such representatives differing by A_r^j would satisfy
u_0(z)=u_0(z)-j, which forces j=0. Hence the map
\[
 p\longmapsto[p,u_0(z(p))]
\]
identifies the entire resolved III source tube with the actual
page near the exceptional core. It includes both components and
their tangency point. There is no residual stabilizer quotient.
The principal delta circle above that graph is the norm sphere
of N=O(2G'-O) with a prescribed smooth positive radius. Radial
normalization identifies it with the unit circle of that exact
line N. In particular its component degrees are zero.

On the other finite pieces the page is the unramified pullback of
the ordinary source and line. The fixed-cusp orbit product is the
actual P3F.9 comparison relative to the source and gamma boundary
marking. The page is chosen disjoint from the fixed sphere, as in
P3K.6 with degree m; its m phase values avoid the short compression
arc. These maps construct a locally translation-isomorphic affine
elliptic fibration over C^o, including the resolved III and the
actual nodal fibres. Its Jacobian is the minimal source pullback
under (III-R.4).

Here is a comparison that also fixes the actual binding collar.
Let Lambda be its elliptic period local system on the complement
of the critical values. In one sector of (III-R.4), the three
original nodal vanishing paths lift with their original marking.
Their vanishing cycles span Lambda integrally, by the trace-mod-d^2
calculation in the construction note. Each transvection image is
the primitive subgroup generated by its vanishing cycle. Thus the
global coinvariant group is zero. Poincare duality with compact
supports on the punctured oriented base gives
H_c^2(Lambda)=H_0(Lambda)=0. The quotient j_*Lambda/j_!Lambda is
a finite skyscraper sheaf and has H^1=0. Its exact sequence then
gives
\[
              H^2(C^o,\partial C^o;j_*\Lambda)=0.       \tag{III-R.5}
\]
For the source with II+I1, the two vanishing cycles in a morsification
of the actual II fibre meet once and already span the lattice, so
the same calculation applies. That local morsification is used only
to compute the two integral vanishing relations of the cusp fibre.

Use the sheaf of smooth sections of the Neron translation group,
whose translations extend to the actual minimal regular source.
Its identity part has the local exponential sequence with kernel
j_*Lambda and a fine Lie-algebra sheaf. Surjectivity at a reduced
III fibre follows from its additive identity group and the analytic
inverse-function theorem; at a node it is the corresponding
multiplicative exponential. Its component quotient is the
skyscraper Z/2 at the III value. Its H^1, also relative to the
ordinary binding collar, is zero. Consequently (III-R.5) removes
the translation cocycle relative to that collar. More explicitly,
remove its component cocycle by local component sections, lift its
remaining cocycle to the Lie bundle, remove the integral period
two-cocycle by (III-R.5), and solve the resulting smooth Lie cocycle
with a partition of unity vanishing on the binding collar. The
resulting translations are mutually inverse smooth isomorphisms
to the sectioned pullback, equal to the given comparison on that
collar. Their extensions across III are the extending source
translations already used in the cap.

The line comparison retains more than the generic fibre degree.
On the cap it is the actual N just identified. Everywhere else
its fibrewise Picard point is 2G', as fixed by the two elliptic
period multipliers. Translation acts trivially on this Picard
point, including its specialization at III. We use the rigidified
relative Picard isomorphism before pulling back by the smooth
translation, so that no holomorphic divisor is assigned to a merely
smooth total-space map. Concretely, on a holomorphic chart of the
extending translation group, let T be the universal source
translation and form Hom(N,T^*N) on the fibre product with that
chart. On each compact source fibre this line is trivial. For
ordinary elliptic fibres this is the degree-zero group law; at
the III value N itself is trivial (the explicit doubling below
puts 2G' at O), and at a node the normalization's multiplicative
translation preserves its gluing unit. At a retained II fibre,
the normalization coordinate u is translated by a constant; its
cusp coordinate w=1/u changes to w/(1+tw), preserving the first
jet that classifies the degree-zero Picard line. Thus H0 of this
Hom line is one-dimensional on every compact fibre. Cohomology
and base change makes its direct image a line, and the evaluation
map is an isomorphism on every fibre, hence an isomorphism. Its
evaluation along O rigidifies it and identifies that direct image
with the Hom line's restriction to O. This is the actual
Poincare-type line isomorphism on the holomorphic translation
chart. Pulling it back along the constructed smooth translation
section gives a smooth, fibrewise holomorphic line isomorphism.
The ratio line is therefore a base pullback. Its absolute Chern
class on C^o vanishes. Keeping the prescribed binding gauge can
leave an integral relative base class nF; it has square zero and
zero product with M, since M.F=F^2=0. No such gauge is discarded.

The actual circle line is flat on the boundary T3: on a regular
elliptic torus its degree-zero multipliers and the commuting
translation lift admit a unitary flat representative. It therefore
has zero boundary Chern class. P3K.5 supplies the same relative
square for every retained boundary gauge. This completes the
page, source, and line comparison required by the real trace.

## III-R.4. Exact characteristic data and the return

The compact sectioned pullback has a III fibre and 3m nodal fibres
for S; for S' it has a III fibre, m II fibres, and m I1 fibres.
In either case its Euler number is 3+3m and
\[
 \chi=\frac{m+1}{4}=l+1,\qquad \sigma=-8\chi.
\]
The pulled section 2G has height 2m. It lies in the identity
component of III, and all other fibres are irreducible. Hence
the actual height/intersection formula gives
\[
 P\cdot O=m-\chi=3l+2,\qquad
 M^2=(P-O)^2=-2\chi-2P\cdot O=-2m.               \tag{III-R.6}
\]
The intersections can be located directly. For S the root section
G'=(0,z^{3l+3}) has doubling slope 1/(2z^{3l+2}); consequently
the zero-section parameter of 2G' is
-X(2G')/Y(2G')=2z^{3l+2} times a unit. For S' the slope is
(1+3z^{4l+3})/(2z^{3l+2}), with the same leading zero-section
parameter. Thus all 3l+2 intersections in (III-R.6) occur at the
actual reduced III cap, with the stated multiplicity. No extra
intersection is inserted at the regular binding.

The regular cap of the page is T2 times D2, of zero signature.
The real compression cap in P3K.6 kills the nodal vanishing cycle
instead of the binding cycle; its H2 restriction to the marked T3
is injective. The line and determinant restrict trivially on that
boundary. The actual graph and compression therefore give exactly
the integral Euler-line comparison and square calculation in
P3K.6--7, with
\[
 s_\delta=-2m,\qquad p_{\rm rel}=3\sigma=-24\chi.
\]
All hypotheses there have now been supplied by maps: the orbit is
the proved S5, the action is semifree with one O(-1)^2 fixed curve,
the cusp translation is in the smooth identity component, the
degree-m page avoids the same short gamma compression arc, and
(III-R.2) identifies the physical positive r-loop with one positive
outward gamma turn.

The physical-character orientation needs an additional explicit
dictionary. With V=rho exp(i phi), delta=+partial_phi, the complex
orientation of the threefold is source4 wedge d rho wedge d phi.
The circle-first convention therefore gives
or(Y)=-or(source4) wedge d log(rho). In particular the identity
with the weighted S3 product in III-R.3 reverses the product
orientation when its circle is the outward gamma. This fact alone
does not determine the index sign, because the Thom meridian must
be transported with it.

Here is that transport in the actual trace. Write kappa for the
sign in boundary V=kappa E times S1_theta, using the complex
orientation on the source elliptic fibre. The explicit compression
has boundary F-E; its gluing to the page gives
boundary X=kappa F times S1_theta. In the outer collar the ambient
orientation is
\[
  \Omega_Z=\Omega_F\wedge\Omega_{\nu,\mathrm{Hopf}}
                   \wedge dr\wedge d\theta,
\]
whereas the trace orientation is
\[
  \Omega_X=\kappa\Omega_F\wedge dr\wedge d\theta.
\]
Thus its oriented normal sphere is kappa times the Hopf meridian,
and the actual extended Euler class satisfies pi_*x=kappa.
Put x_hat=kappa x and e_v=2x_hat-pi^*b. The framed section of the
graph gives b|V=2kappa c1(M), with the same retained boundary
correction as in P3K.5. Its square is 4M_rel^2. The fibre integration
and the two outer/Jin orientation reversals of P3K.7 therefore give
\[
 A(\Phi)=\kappa\frac{3\langle b^2,[\bar X]\rangle
                    -\langle p_1(T\bar X),[\bar X]\rangle}{24}.
\]
In the actual affine page b-t_*a^m=1, the complex boundary of a
large a-disc is +arg(a). Formula III-R.3 identifies this with the
outward gamma, and III-R.2 identifies the positive parameter theta
with that same outward gamma. Hence kappa=+1. This tracks the
normal meridian as well as the ambient reversal; it introduces
no unproved identification with an inward-circle model. We obtain
\[
 A(\Phi)=\frac{12s_\delta-p_{\rm rel}}{24}
          =\chi-m=-\frac{3m-1}{4}=-(3l+2).             \tag{III-R.7}
\]
With the Eells--Kuiper convention fixed in P3F.22, the Hopf transfer
has mu=A/28 and oriented sphere class -(3l+2) modulo28.
At m=3 this is A=-2 and class26. The mapping-torus conclusion for
each nonzero residue is the one proved in P3F.24. These formulas
are derived from the actual r-family, rather than assigned to a
sectioned cover without its torsor and angular comparison.

## III-R.5. The explicit second OS43 source

For y^2=x^3+tx-t the discriminant is a nonzero constant times
t^2(4t+27). At t=0 the orders of f,g,Delta are (1,1,2), giving
II; at -27/4 it is a simple I1. At infinity q=1/t the exact
minimal equation is
\[
 y_0^2=x_0^3+q^3x_0-q^5,\qquad G=(q^2,q^3),
\]
giving III*. The surface is rational by the explicit inverse
t=(y^2-x^3)/(x-1). The good fourth root sends G to the nonzero
fixed two-torsion point (0,0), so its III* component is nonzero.
The E7 discriminant and the section's disjointness from O give
h(G)=1/2 and prove that G is primitive with no Mordell--Weil
torsion, exactly as for the first source. In particular 2G.O=0
on the original rational surface, and its Hom line for Q=G has
degree one and zero component multidegrees. Its sole zero can be
the indicated I1.

For m=4l+3, k=3l+2, the actual substitution q=z^m,
x_0=z^{2k}X,y_0=z^{3k}Y gives
\[
 Y^2=X^3+zX-z^{2l+3},\qquad
 G'=(z^{2l+2},z^{3l+3}).
\]
Its quadratic singular part is Y^2-zX. The same one-point
resolution gives reduced III, with G' on the nonidentity component
and 2G' on the identity component. The deck and its exact m-division,
line norm, meridian, and primitive boundary maps are the ones in
the construction note. The integral source basis O,F,E7,G has the
same unimodular Gram matrix, and its translation on the complement
still sends M to M-F. The II fibre contributes the two primitive
vanishing cycles with intersection one; thus its source complement
is simply connected. This verifies all unchanged integral topology
maps for this explicit source, without identifying the two source
surfaces or their full singular-fibre maps with one another.
