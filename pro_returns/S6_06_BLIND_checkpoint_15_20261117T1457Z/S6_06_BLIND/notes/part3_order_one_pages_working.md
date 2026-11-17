# Exact order-one redistribution on the orbit base and its pages

This is a complete working derivation for independent audit. It uses the
actual families and line maps in F36--49 and the page/trace maps K26--28.
It concerns their fixed marked logarithmic clutches: elliptic and delta
coefficients and annular units are fixed while the suspension scalar varies.
The only global phase change below is on the three-dimensional orbit base.
The source and line arrows are constructed separately on its actual page.

## O1. The marked base and its integer framing

Put the surviving capped source values at infinity and zero. In a one-cap
case zero is an ordinary disc with `(m0,n0)=(1,0)`. Let the orders and norms
be `(mi,ni)=(m_infty,n_infty)` and `(m0,n0)`. Added sites `c_j` are away
from zero, infinity, and the selected zero fibre `t_c`. F48 makes their
effective orders one in a sphere member. Retain their signed norms `n_j`
and every elliptic and delta coefficient.

With the physical outward gamma coordinate, the actual cap norm is

    h_j=gamma-n_j alpha_j,  alpha_j=arg(t-c_j)/(2pi).       (O1.1)

Its source meridian maps to `-n_j h_j`, gamma maps to `h_j`, and its killed
meridian is `alpha_j+n_j gamma`. Retain an initial base framing in

    sum alpha_i+b0 gamma=0.                              (O1.2)

At the level of the base atlas, this is represented by an additional
ordinary disc with transition `h=gamma+b0 alpha`, hence signed order-one
norm `-b0`: eliminating its meridian gives exactly (O1.2). This is an
equality of circle-base atlases, with no new elliptic or line clutch on
the total space. In the displayed annular atlases of F38/F46/F47, `b0=0`.
Use the additional framing chart when retaining (O1.2). Put

    N=sum n_j-b0,  ni'=ni+mi N,
    D=m0 ni'+mi n0.                                     (O1.3)

The minus sign on `b0` follows by eliminating the order-one meridians:
`alpha0+alphai+(b0-sum n_j)gamma=0`.

## O2. An exact diffeomorphism of the three-dimensional bases

First take `b0=0`. On the punctured ordinary base set

    u(t)=product(t-c_j)^(n_j),
    gamma'=gamma-arg u(t)/(2pi).                         (O2.1)

Its circle-valued phase is globally defined. Near `c_j`, write
`u=(t-c_j)^(n_j)v_j`, with `v_j` an extending unit. Then
`gamma'=h_j-arg(v_j)/(2pi)` extends over the actual solid torus; its inverse
adds the same unit phase. At infinity, `q=1/t` gives `u=q^(-N)v_i(q)`, so
`gamma'=gamma+N alphai-arg(v_i)/(2pi)`. Retain the unit as the extending
change of cap coordinate. On the marked boundary loops this gives

    alphai'=alphai-N gamma,
    mi alphai+ni gamma=mi alphai'+ni' gamma.              (O2.2)

At zero `u` is a unit and the same extending phase transports its marking.
The framing chart from O1 gives the identical calculation with exponent
`-b0`. Thus the displayed maps and inverses give an actual diffeomorphism
to the two-cap base with norms `(ni',n0)`.

The infinity-cap generator change is literal on the total quotient:

    Ai'=Ai B^N,  (Ai')^mi=B^ni',
    <Ai',B>=<Ai,B>.                                    (O2.3)

For `B_r=r^L B0` and `Ai,r=r^(L ni/mi)Ai,0`, it holds for every `r`,
with the new exponent `L ni'/mi`. It retains the actual quotient, line
characters, and extending units. It is independent of any proposed lift
of (O2.1) across the ordinary total space.

The marked base abelianization has determinant `D`. It is a quotient of
the orbit group, so a sphere member has `D=epsilon=+1` or `-1`. The two
orders are therefore coprime; put `M=mi m0`, so `lambda=r^M`.

## O3. The physical closing cochain

The elliptic and delta parts of the fixed annular clutches are independent
of `r`. The gamma part has the exact ordinary-to-cap scalar variation
`n_j(c-c0)s_j delta/m_j`, with `c=log(lambda)/(2pi i)` and
`s_j=log(q_j)/(2pi i)`. For a positive `r`-loop set
`ki=m0 ni`, `k0=mi n0`, and `k_j=M n_j`. In the zero-framing atlas the
actual inverse closing multiplier is

    f_old=t^k0 product(t-c_j)^(M n_j)(t-t_c)^(-D).        (O3.1)

Its orders at all the capped sites, including infinity, are exactly the
recorded integers. Include exponent `-M b0` at the framing chart for
(O1.2). The redistributed multiplier and the ratio are

    f_new=t^k0(t-t_c)^(-D),  f_old/f_new=u^M.             (O3.2)

These are identities of scalar cochains. Choose the regular binding and
the selected cusp away from the additional sites. There `u` is a unit.
Add its logarithm to both compared cusp origins, retaining it in each.
It cancels in their difference, giving exactly K28's identity

    F_epsilon(v+theta)-F_epsilon(v)
      =epsilon theta gamma-epsilon M theta(theta-1)delta/2. (O3.3)

The quadratic gauge vanishes at both endpoints. The positive weighted
base coordinate is `beta=epsilon gamma'`; its vector field is the same
as `epsilon gamma`, because (O2.1) changes its origin by a fixed base
function. Thus the physical positive return has the same signed angular
coordinate as the trace in K28. The fixed elliptic and delta clutches
glue the product comparison throughout the parameter interval. Their
endpoint maps agree; (O3.2) is the added parameter-closing cochain.

## O4. The actual page pullback and its source torsor

Apply the explicit weighted three-sphere map K28.4--8 to the base of O2.
The regular-binding page has complex base

    C: eta^m0-tau xi^mi=1,  t=tau+xi^(-mi).              (O4.1)

It has degree `M`, with the same ramification as K28 at zero, infinity,
and the binding. It is unramified over the added order-one sites.
Define the actual page by pulling this page back through the original
orbit projection and the displayed base diffeomorphism. All original
elliptic and line transitions are part of this pullback.

On an ordinary simply connected chart choose a real lift of the prescribed
gamma graph. Its source arrow is `p -> [p,gamma_graph(t(p))]`. Overlaps
change that lift by an integer and change the source by the corresponding
actual power of `t_(-Q)`, followed by the given elliptic translation.
These are holomorphic fibre translations with their actual annular
descent laws. They define the source translation torsor on (O4.1).

At an added site (O2.1) gives an extending graph of `h_j`. Its order is
one, and its sheet map is the literal original local source. A relation
preserving a representative level has `n_j k+h=0`; the identity
`A_j^k B^h=1` proves that no residual quotient remains. At the surviving
roots use K28.20 with (O2.3). Its corresponding relation is
`(k,h)=(m_j l,-n_j' l)`, so its uniqueness proof remains exact. These maps
extend across every resolved component. At the selected nodes use F9's
actual orbit/source maps, retaining the Hopf charge in the compression.

Translations do not change the integral linear monodromy, and the cover
(O4.1) is unchanged. Thus K26/K28's integral coinvariant calculations
apply with the same maps. In the joint cases the two closed lifted nodal
loops have images `Zv` and `ZAv`, with `|<v,Av>|=1`. In the single-cap
case all retained source meridians lift with trivial sheet permutation,
and the proved torsion-free source Mordell--Weil group gives zero integral
coinvariants by K26's invariant-torsion-section argument. The added
translation coefficients change none of these linear maps.

For `j:C_reg->C` and the actual lattice Lambda, this proves

    H^2(C,partial C;j_*Lambda)=0.                        (O4.2)

Compact-support duality gives the coinvariants for `j_!`; the quotient
`j_*Lambda/j_!Lambda` is a skyscraper with zero first cohomology. The
finite component quotient of extending translations is also a skyscraper.
Remove its cocycle, lift the remaining translations to the smooth Lie
sheaf, and use (O4.2) to remove the lattice two-cocycle. A partition of
unity vanishing on the binding collar removes the remaining Lie cocycle.
Exponentiating gives the actual smooth translation isomorphism to the
sectioned elliptic page, fixed on that collar. The I2 invariant lattice
and component group are included, as in K28.

The separate `part3_order_one_cech_working.md` also supplies holomorphic
source cochains for the elliptic-only gluing before taking this page.
Its maps `p_i -> p_i-s_i` commute with `t_(-Q)` and transport every root
deck, and can be chosen once independently of `r`. The page argument
does not require (O2.1) to lift globally to that source surface.

## O5. The actual line arrows and whole-fibre remainder

On each surviving root the norm-sphere map sends a vector in the actual
line `N_j=O(aG_j'-O_j)` to the graph level. It is delta-equivariant and
identifies its associated complex line. Use the Cartier maps in
F36/F38/F41--43/F46--47. The quadratic root in particular uses

    beta^*N_*=pi^*O(aG-O-L0)+E0+E1,

including F49's transported four-point blowup diagram. Good-starred toric
corrections, good III/IV exceptional differences, cancelling good-II
coefficients, and reduced-root whole-fibre factors are all retained.

At an added order-one site the norm-sphere map has no root quotient and
carries its actual local line. Every component degree there is zero.
For a retained multiplicative fibre, the actual line norm preserves its
component-degree vector, and translation is transitive on components.
The degrees are therefore equal and their total degree is zero. Smooth
fibres have degree zero by construction. At the additive and quadratic
roots the individual zero degrees are the checked degrees in the cap
proofs. Thus the actual page line has degree zero on every fibre component.

Perform the source translation comparison of O4 through K26/K28's
rigidified relative Picard map. Here is its exact remaining line. On a
holomorphic translation-parameter chart, form the ratio of the two lines
before pulling back by the smooth translating section. It is trivial on
every smooth elliptic fibre. Proper direct image and evaluation give a
base line and an effective vertical evaluation divisor. Both lines have
zero degrees on every fibre component, so that divisor intersects every
component by zero. The actual connected Kodaira intersection matrix has
kernel the whole-fibre multiplicity vector. Hence the divisor is an
integral sum of whole fibres. Their base equations give a nowhere-zero
Hom section after division. This supplies the evaluation isomorphism at
singular as well as smooth fibres. Rigidify at the zero section, then
pull back by the smooth translating section; the result is the actual
smooth line map, holomorphic along the fibres.

Glue these evaluations with every delta transition and finite character
retained. The remaining ratio is a line pulled back from the page base;
on the compactification its class is `kF`. This processes the exact
unrooted source output `M_tilde=M tensor f^*L tensor O(D_vert)` through
the actual corrected root diagrams. It does not assert that `D_vert`
vanishes on the unrooted source. It is the corrected page line whose
vertical remainder has just been proved to be a sum of whole fibres.
Finite root characters may leave base holonomy and are retained in that
pulled-back line. The characteristic identities are

    (c1(N_page)+kF)^2=c1(N_page)^2,
    c1(N_page)F=F^2=0.                                  (O5.1)

On the regular binding collar the comparison is the prescribed one, up
to this base line. The base line extends over the ordinary disc and the
fibre degree is zero; hence the boundary first Chern class is zero.
K5's relative boundary-gauge formula gives zero square ambiguity even for
odd gauges. The source diffeomorphism also carries the stable tangent
pairing.

## O6. The characteristic comparison and scope

The fixed source and delta clutches glue the page and its rotating trace
by the same maps throughout the parameter interval. The source maps
commute with the suspension translation. The degree-zero line lifts
commute with its lift on smooth fibres by constant-factor uniformization,
and extension gives that identity on the resolved roots. The dependent
parameter cochain is exactly O3. At the selected nodes and binding its
ratio is the extending unit `u^M`. Transport the source and line charts
by that unit over the whole local parameter trace. Both origins receive
the same logarithm, so the angular difference and the positive Hopf
normal sphere remain (O3.3). These are precisely the boundary arrows
of K7 and K28's signed Thom calculation. O4's relative comparison is
fixed on that boundary.

Through the actual characteristic bordism this gives

    A^Jin=(12 c1(N_page)^2-p1(TS_page))/24
         =chi(O_Spage)-M a^2/(2d),                     (O6.1)

where `h(G)=1/d`. The Euler and height computations are exactly K26/K28
with the unchanged root orders and the redistributed signed determinant
`D=epsilon`. Added order-one sites are unramified in the page and retain
their local source model, so there is no additional Euler replacement.
The line computation includes every correction in O5. Thus the previously
proved single- and joint-cap tables apply with the actual norms (O1.3),
retaining all their order and primitivity restrictions.

This is the return comparison for actual sphere members of the listed
constructed families with their fixed marked order-one clutches. It uses
no unproved total-space lift of (O2.1). The source vertical divisor and all
delta data remain until O5's exact corrected page comparison. No external
source was opened for this note; its primary-source imports are the ones
already verified in the numbered statements it cites.

## O7. The full normal frame and relative integers

The now-proved K30 supplies the full normal comparison, and its maps retain
the added unit explicitly. In radian coordinates, the new two-cap page
has phase

    arg P = M epsilon gamma + arg(t-tau)
            -epsilon mi n0 arg t -epsilon M arg u(t).

Near the regular binding use the literal holomorphic coordinate

    q_b=(t-tau)(t/tau)^(-epsilon mi n0)
                    (u(t)/u(tau))^(-epsilon M).         (O7.1)

It has derivative one at `tau`; every exponent is an integer and every
other factor is a specified extending holomorphic unit. After retaining
the constant phase of `tau` and `u(tau)` in the page angle `phi`, (O7.1)
gives exactly `alpha=phi-M beta`, with `beta=epsilon gamma`. Thus this
coordinate retains the variable added phase, rather than replacing it by
its value at the binding. In a one-cap chart the `t/tau` factor is absent.

The actual source-preserving graph has `beta=theta+g(p)` on the binding,
where `p` is its source two-torus and `g` is its fixed circle-valued graph
phase. This includes the retained elliptic/delta gauges and the unit just
displayed. Apply K30's literal quotient of the common tangent
`(cos alpha,sin alpha,rho,0)`, `rho>0`. It removes the graph derivatives
by the explicit triangular shear and gives the same oriented normal matrix

    G(alpha,theta)=
      [-sin alpha, cos theta cos alpha, sin theta cos alpha;
        cos alpha, cos theta sin alpha, sin theta sin alpha;
                0,           sin theta,          -cos theta].

The transported compression frame is `h(p)`, independent of `theta`.
The exact resulting clutch factorization is

    h(p)^(-1)G(phi-M(theta+g(p)),theta)
      =[h(p)^(-1)Rz(-M g(p))]
         [Rz(phi-M theta)G(0,theta)].                   (O7.2)

Both factors are global: the first comes from the source two-torus, the
second from the parameter circle. The integer `M` retains graph winding.
The normal Pontryagin transgression is zero by K30's exact two-factor
calculation, including its one-dimensional frame classes. The bounded Cox
comparison in K27/K30 is transported by the fixed source and line maps of
O4--O5. It adds only the extending constant rotation loop already retained
there. Hence `p1(normal)=0` for these actual order-one clutches as well.

Write `H=M a^2/d=-c1(N_page)^2` and `chi=chi(O_Spage)`. The full actual
characteristic pair and relative group coordinates are therefore

    k=-3H,  ell=-24chi,
    (m_rel,n_rel)=(6chi,3H-6chi),
    A=chi-H/2.                                         (O7.3)

These retain the same normal and Jin sign conventions as K23/K30. In
particular `-(m_rel+n_rel)=k` and `(4k-ell)/24=A` are literal identities.

## O8. The primitive sector with no distinguished additive cap

This sector is included by choosing a regular infinity disc with order
one. Use an ordinary zero disc `(m0,n0)=(1,0)` as above. All effective
added orders are one by F45, so O1--O3 move their actual base phase to
`mi=1`, `ni'=epsilon`; the effective determinant is still the retained
sum minus `b0`. Nothing is ramified in its degree-one page. Its compact
sectioned page is exactly the rational elliptic source of K22, and its
line is the actual `O(dG-O)` after the evaluated base-line remainder of
O5. K22 and K27 give `chi=1` and `H=d`. Their source monodromy argument
supplies O4.2, and their actual rotating/Cox normal maps give O7.2.

For every such primitive sphere family with its arbitrary fixed order-one
source and delta clutches, the resulting values are thus

    k=-3d, ell=-24,
    (m_rel,n_rel)=(6,3d-6), A=1-d/2.                    (O8.1)

Both signs of the total gamma determinant are covered by O3's positive
physical angle and O7's signed normal frame. Every remaining source fibre,
including an ordinary II, III, IV, or multiplicative fibre, is retained in
the actual source and page; choosing the regular infinity disc does not
delete or replace any of them.

## O9. Sufficiency of the signed determinant with every clutch retained

We now prove the topology before invoking the normal-frame construction.
The data are all the effective order-one clutches above and either a
previously constructed additive core or the regular order-one core of K22.
Their topology is a sphere exactly when `D=+1` or `-1`.

Let W0 be the actual original source exterior with only the chosen core
tubes removed. Remove the additional ordinary tubes U_j to obtain W, and
write E_j for their boundaries. First fill them by their ordinary maps.
The ordinary maps `H2(E_j)->H2(U_j)` are surjective, with primitive kernel
K_j generated by the three smooth rims or the two multiplicative classes
R_j,L_j. All old degree-three representatives can be chosen away from the
new tubes: old source-boundary and local-rim representatives remain in old
collars, and the common generic-fibre trace is placed over a regular value
outside the tubes. Thus `H3(W)->H3(W0)` is onto.

The next ordinary boundary map `H2(W0)->sum H1(E_j)` lands in the free
meridian kernels. Its target is inversion-even, whereas its source is
inversion-odd rationally by the actual source inversion calculations in
F45/F48. Its rational map is zero, and a homomorphism into this free target
cannot have a nonzero torsion image. It is therefore zero integrally.
Ordinary Mayer--Vietoris, followed by the actual cap surjections, gives

    0 -> K=direct_sum K_j -> H2(W) -> H2(W0) -> 0.        (O9.1)

No division by two is used. The source involution is odd on K and on
`H2(W0;Q)`, hence is odd on `H2(W;Q)` as well: over Q the involution is
semisimple and both ends of (O9.1) have only its negative eigenspace.
Every even boundary core column therefore has torsion image in H2(W).

Use next the *actual* old core cap maps. Their combined D2 map projects
isomorphically onto `H2(W0) plus H2(old caps)`, by F36/F38/F41--47, or by
F45/K22 for the regular primitive core. Thus its image is an exact graph
over that whole target and intersects K trivially. Quotienting it out
leaves exactly the free group K, together with the new cap targets. In
this quotient all the preceding torsion core columns vanish. This proves
the needed integral vanishing even at primes dividing the weighted source
integer b; it requires no extension of inversion over any nonordinary cap.

For a smooth order-one cap keep its actual primitive meridian

    mu=alpha+n gamma+lambda_a a+lambda_b b.

The map to the cap is the exterior square of its actual primitive H1
quotient. After eliminating the cap target, its kernel maps to the three
rims by the matrix

    [1,0,0,-lambda_a; 0,1,0,-lambda_b; 0,0,1,n].

The four displayed generators have their one relation `mu wedge mu=0`.
More precisely they are `(a wedge mu,b wedge mu,mu wedge gamma,alpha wedge mu)`
in the ordered rims `(a wedge alpha,b wedge alpha,alpha wedge gamma)`.
Their primitive relation is
`lambda_a col1+lambda_b col2-n col3+col4=0`. Thus the first three columns
form an actual integral basis of the kernel and map to the rim basis.
The kernel is a rank-three free group and the displayed map is an integral
isomorphism. For a multiplicative
order-one cap retain the actual Tate integer A and the complete F40 rows.
Its isotropy relation and basis change put them in the exact form
`[1,-A,0,0;0,0,1,A]`. Together with the exterior R,L rows the integral
matrix reduces to `diag(1,1,-1,-1)`, as in F48 with m=1. The K_j are
independent summands of K. Thus the entire degree-two Mayer--Vietoris map
is an integral isomorphism, with all elliptic and delta collar coefficients
retained.

For degree one, the original rational-source holomorphic Cech maps
`p_i -> p_i-s_i` identify the elliptic-only clutches with the same actual
source, commute with its suspension translation, and transport the root
line/finite-character diagrams. Alternatively, the same conclusion can
be read directly from van Kampen: an order-one cap retains its original
local vanishing cycles and changes only its meridian by the displayed
elliptic and gamma terms. Translations induce the identity on the fibre
lattice. Every source vanishing relation and its conjugates by the marked
linear monodromy is therefore the one in the complete source computations
F36/F38/F45--47. Their normal closure kills the full elliptic lattice. This
includes the graph generator of the quadratic I2 root. Adding an elliptic
term to a meridian does not change that normal closure, since conjugation
by a fibre translation is trivial on the abelian fibre lattice. The actual
component and finite torsion maps at the old caps remain the isomorphisms
already displayed in those proofs.

After these exact identifications, the only group relations are the marked
Seifert relations of O1. Each added order-one relation eliminates its own
meridian, leaving the two-core presentation

    <h_i,h_0 | h_i^mi=h_0^m0,
                  h_i^ni' h_0^n0=1>.                  (O9.2)

The common power is gamma. The existing primitive norm has `gcd(mi,ni)=1`,
and `ni'=ni+mi N` gives `gcd(mi,ni')=1`. Choose integers a,c with `a mi+c ni'=1`.
Then (O9.2) gives `h_i=h_0^(a m0-c n0)`, so the group is cyclic. Its
order is the absolute value of D, with the infinite cyclic interpretation
when D=0. All the source terms and retained line characters have been
processed through actual maps; none was declared absent.

The degree-one homology calculation has the same integral elimination.
The old torsion blocks are the retained cap isomorphisms. The order-one
elliptic coefficient terms are elementary shears of the cap quotient rows.
After the primitive source identifications just described, its free block
is the marked relation matrix with rows

    mi alpha_i+ni gamma,  m0 alpha_0+n0 gamma,
    alpha_j+n_j gamma,  sum alpha+b0 gamma.

The complete unimodular row and column changes, retaining b0 and every n_j,
are exported in `code/part3/order_one_pages.json`. They leave the two-core
matrix and order-one identity blocks, with determinant `-D`. Thus D=±1
makes the actual D1 map an isomorphism. Together with the degree-two map
this proves H1(Y)=H2(Y)=0. Van Kampen above gives pi1(Y)=0. Integral
Poincare duality and the universal coefficient theorem give H3(Y)=H4(Y)=0.
The connected closed oriented orbit Y is therefore a simply connected
integral homology five-sphere, and the already used smooth five-dimensional
sphere theorem identifies it with S5.

Finally apply the actual fixed-sphere Hopf gluing and circle Gysin argument
of F36/F38/K22, with its retained boundary line. The principal-circle part,
the primitive normal Hopf charge, and the fixed-sphere tube are carried by
the maps above. They give a simply connected integral homology six-sphere;
the proved vanishing of the group of smooth homotopy six-spheres gives S6.
F35's actual finite flop chain transfers this sphere topology to every
allowed cusp fan. Necessity of D=±1 was proved from the base quotient in
O2. This establishes sufficiency without using Y=S5 before the topology
calculation. The page, normal frame, and return calculations O3--O8 now
apply to exactly these sphere members.

There is also a direct check of injectivity of D1 which does not abbreviate
its source elimination. Use as reference the already proved core sphere
with norm `ni'`, and fill all new sites ordinarily. Its exterior is the
same W. Each new order-one cap has the same individual quotient as its
ordinary cap, and `Ai'=Ai B^N` gives the literal same old cap quotient.
Hence the domain and target of our D1 have the same free ranks as that
reference, and these ranks are equal. Its cokernel is zero by (O9.2).
Its kernel therefore has rank zero. The only torsion in its domain is in
the old boundary blocks; their maps into the corresponding cap torsion
groups are the unchanged actual isomorphisms in F36/F38/F41--47. New smooth
boundaries are free; new transitive multiplicative boundaries are free
because their Euler pair is primitive. Thus the torsion kernel is zero
as well. This verifies the full integral isomorphism used above.

The return and relative-coordinate formulas O6--O8 are for the vertical-edge
reference fan used in K26/K28/K30. O9's topology conclusion holds for every
allowed fan by F35; the return of a changed fan is transported by its actual
flop maps from these reference relative coordinates.
