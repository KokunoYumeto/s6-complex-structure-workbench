from S6_SERIES_PUBLISH_c3_foundations_sec11_helpers import *
from collections import Counter

main=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
old=block(main,'cdp:st:C.2.UN.79')
(OUT/'S6_SERIES_PUBLISH_II_sec11_compact_minuscurve_input.tex').write_text(old+'\n',newline='\n')
pkg=Package('compact_minuscurve','subsec:II:compact-negative-curve')
owner='cdp:st:C.2.UN.79'
new=old
def change(a,b,kinds,reason):
    global new
    new=pkg.edit(new,a,b,kinds,owner,reason)

line=next(x for x in new.splitlines() if x.startswith(r'\StatementRecord'))
change(line,r'\StatementRecord{cdp:st:C.2.UN.79}{proved}{01EQ}{\cref{lem:II:canonical-bimeromorphic-direct-image,lem:II:blowup-topology}}','D10,D12,D14','Keep hidden dependency metadata and identify the exact earlier general maps used by the construction; UN70 is an interpretation of the example rather than a premise of its proof.')
change(r'''The construction retains an actual point-blowdown map from \(P\)
to \(\PP^1\times E\), where \(E\) is an elliptic curve.''',r'''There is a composite point-blowdown map
$P\to\PP^1\times E$, where $E$ is an elliptic curve.''','D08,D20','State the surface comparison map directly.')
change(r'''The specified exceptional locus of this surface map
does not contain \(F\). This records the scope relevant to \ref{cdp:st:C.2.UN.70}:
the example concerns an arbitrary nonboundary \((-1)\)-curve,
with its exact comparison to the chosen elliptic minimalization.''',r'''The restriction of the surface blowdown to $F$ is the
displayed isomorphism, so $F$ is not one of its exceptional curves.''','D02,D08,D11','Keep the exact non-exceptional conclusion through the restriction map; remove the repeated scope commentary.')
change(r'''\textbf{An actual compact elliptic surface with a toric \(I_3\) chart.}''',r'''\textbf{A compact elliptic surface with an \(I_3\) chart.}''','D08,D16','Use a mathematical construction heading.')
change(r'''Take a compact rational elliptic surface with a simple nodal fibre.
Such a surface, with an explicit cubic-pencil construction, was
used in \ref{cdp:st:C.2.UN.41}. Alternatively the Weierstrass equation''',r'''Consider the projective Weierstrass surface over $\PP^1_t$
with coefficient sections in $\OO(4)$ and $\OO(6)$ and equation''','D01,D08,D12','Use the one explicit construction proved here instead of an optional earlier construction.')
change(r'''gives one: its discriminant, up to a nonzero constant, is
\(31t^{12}+12t^8+12t^4+4\), which is square-free and has no
zero at infinity. Choose one nodal value, put it at \(t=0\)
by a base coordinate, and take the global cubic base change''',r'''Its discriminant, up to a nonzero constant, is
$31t^{12}+12t^8+12t^4+4=h(t^4)$, where
$h(q)=31q^3+12q^2+12q+4$.
The identities $h-(q/3)h'=4(q+1)^2$ and $h'(-1)=81$
show that $h$ is square-free; $h(0)=4$ makes its pullback
under $t\mapsto t^4$ square-free as well.
At infinity the equation in coordinates
$(T,X,Y)=(t^{-1},x/t^2,y/t^3)$ is
$Y^2=X^3+(1+T^4)X+1$, with the same discriminant factor
equal to $31$ at $T=0$.
The singular fibres are therefore simple nodal cubics,
and the total surface is smooth.
Translate the coordinate so that one nodal value is $t=0$,
keeping infinity a smooth value, and take the global cubic base change''','D20,D22','Give the exact discriminant, square-freeness and infinity coordinate checks that justify the selected nodal and regular branch values.')
change(r'''Here is the required local comparison, with its entire two-chart
neighbourhood retained.''',r'''The local comparison is given by two charts covering a
neighbourhood of the whole exceptional curve.''','D05,D08','State the entire analytic neighbourhood map directly.')
change(r'''The displayed monomials satisfy \(xy=s^3\), glue on their
overlap, and are the successive point-resolution charts,
so this comparison does not identify a neighbourhood merely
from its normal degree.''',r'''The displayed monomials satisfy $xy=s^3$, glue by the stated
transition and are the successive point-resolution maps.
Their union identifies the entire neighbourhood and its function $s$.''','D02,D20','Retain the exact chart isomorphism and function, with no contrast to an unproved normal-degree argument.')
change(r'''\item The two-form \(dx\wedge ds/x\) is \(db\wedge dz\)''',r'''\item On a disc about the chosen nodal value the original
Weierstrass surface is a smooth cubic hypersurface in
$\PP^2\times\Delta_t$. Adjunction gives its canonical line
as $\OO(-3+3)\otimes K_{\Delta_t}$, so its residue two-form
is a nowhere-zero generator on this whole neighbourhood.
At the node it is a nonvanishing multiple of $dx\wedge dy$.
The two-form $dx\wedge ds/x$ is $db\wedge dz$''','D20,D25','Make the global-to-local generator comparison explicit on the same smooth cubic family; the original nowhere-zero generator assertion is justified without changing the construction.')
change(r'''An original canonical generator is a nonvanishing
holomorphic multiple of \(dx\wedge dy\) at the node.
Pull it back and divide by \(s^2\);''',r'''Pull back that residue form and divide by $s^2$;''','D12','Use the exact original generator just constructed once.')
change(r'''\(J\) near this fibre are zero.''',r'''$J$ near this fibre are zero. Properness and connectedness
make every holomorphic function on this neighbourhood a base
function; its nowhere-zero canonical form therefore generates
the canonical direct image.''','D20','Follow the rank-one direct image through the actual nonvanishing form on the elliptic surface.')
change(r'''Blow up the complete smooth
rational curve''',r'''Let $\pi_0:X_1\to X_0$ be the blowup of the smooth
rational curve''','D20','Name the actual first blowup for its canonical-direct-image application.')
change(r'\textbf{One global curve blowup produces the required germ and orders.}',r'\textbf{The curve blowup and its canonical orders.}','D05,D08','Name the geometric operation and its conclusion directly.')
change(r'''The inverse chart of \ref{cdp:st:C.2.UN.74}, or the following direct
calculation, shows that the new fibre is full reduced SNC.''',r'''The following charts show that its full central fibre is
reduced SNC.''','D12','Keep the actual local full-function charts needed by this construction without a duplicate alternative application.')
change(r'''with the entire
map retained.''',r'''with the function $s$ and both transition maps.''','D08,D20','State exactly which analytic maps identify the normal neighbourhood.')
change(r'''Up to its retained nonvanishing holomorphic factor, the actual
product canonical form pulls back as''',r'''Up to the same nonvanishing holomorphic factor, the product
canonical form pulls back as''','D08','Use the same explicit residue form in the pullback calculation.')
change(r'''This is the requested
canonical tuple for the actual direct-image generator.
It remains a generator: the curve blowup has the actual
canonical pushforward \(\pi_*K=K\) through its Jacobian,
or directly through Hartogs across its smooth codimension-two
centre.''',r'''This gives the canonical tuple for the direct-image generator:
apply \cref{lem:II:canonical-bimeromorphic-direct-image} to
$(X,X',\phi)=(X_1,X_0,\pi_0)$ and the maps to the same disc.
Its pullback is a generator, and the displayed Jacobian
has order one exactly on $R_0$.''','D05,D08,D12,D20','Replace the repeated canonical pushforward/Hartogs argument by its earlier complete owner with the identical first blowup and full product family.')
change(r'''\textbf{Exact zero-Euler balancing away from the entire curve.}''',r'''\textbf{Further blowups away from the curve.}''','D08','Name the geometric operations.')
change(r'''The four quadratic factors have respectively discriminants
\(-4,-59,-31,-11\), are pairwise coprime, and have
nonzero leading coefficients.''',r'''The four quadratic factors have respectively discriminants
$-4,-59,-31,-11$ and nonzero leading coefficients.
A common root of two factors would satisfy $P=Q=0$;
from $P=0$ one gets $z^2=-1$ and $Q=z+2$, which is impossible.
They are therefore pairwise coprime.''','D20,D22','Give the exact common-root calculation for the eight branch points of the genus-three curve.')
change(r'''since these zeros are simple it gives the same smooth
double cover, not additional components.''',r'''choose its local parameter $\tau$ so that
$x=\tau^{-2}A(\tau)$ and $y=\tau^{-3}B(\tau)$,
where $A(0)=B(0)=1$. The equation $Px=Q$ gives
$P=Q\tau^2/A(\tau)$ and
$Y=Q^2B(\tau)\tau/A(\tau)^2$.
Since $P$ has a simple zero and $Q$ is nonzero there,
these equations express $z$ holomorphically in $\tau$
and make $Y$ a local parameter. They give the same smooth
double cover at each zero of $P$.''','D02,D20','Give the exact local parameter map and its implicit inverse at the infinity point instead of a scope contrast.')
change(r'''For a smooth curve centre contained in the fibre,
the actual blowup replaces that curve by its
\(\PP^1\)-bundle exceptional divisor and is an
isomorphism on the complement. Its reduced-fibre
Euler defect is therefore exactly \(e\) of the
centre. Consequently our three operations give''',r'''Apply \cref{lem:II:blowup-topology} successively with
the smooth centres $B_0,B_1,D$ and the compact reduced
support containing each centre. At every step the next
support is the full reduced inverse image. The codimension
is two, so the Euler increment is the Euler number of
that same centre. Consequently the three blowups give''','D08,D12,D20','Use the single compact full-support Euler owner with all three exact centres and maps.')
change(r'''For an independent stratum check, the six final components
have Euler numbers \(0,4,4,6,6,-8\). The double curves
have total Euler characteristic \(24\), and there are
\(12\) triple points. Thus their actual SNC
inclusion--exclusion gives \(12-24+12=0\), in
agreement with \eqref{cdp:eq:C.BC.13}.''',r'''The six final components have Euler numbers $0,4,4,6,6,-8$:
$P_0$ is unchanged, $P_1$ and $P_2$ each acquire four point
blowups, the first two ruled exceptional surfaces each acquire
two point blowups, and the last is ruled over the genus-three
curve $D$. The double curves have total Euler number $24$.
The first two blowups contribute $12$ in total; the last adds
$e(D)=-4$ and eight exceptional rational fibres, contributing
$-4+16=12$. The first four triple points persist, and the
eight boundary intersections of $D$ give eight further triple
points. Thus the final support has twelve triple points.''','D07,D12,D20,D21','Keep all exact stratum conclusions and their geometric counts at the same owner; remove the second Euler proof and independent-check rhetoric.')
change(r'''the stated horizontal
qualification on the final zero-Euler model.''',r'''the horizontal section asserted on the final zero-Euler model.''','D08','Conclude with the exact degree-one map.')
# Current-number references and equation counters.
def cref(m):
    oldref=m.group(0); newref=r'\cref{'+m.group(1)+'}'
    pkg.record('D04',owner,oldref,newref,'Use the current statement number with its stable label.')
    return newref
new=re.sub(r'\\ref\{(cdp:st:[^{}]+)\}',cref,new)
new=pkg.clean(new,owner)
fragment='\\subsection{A compact zero-Euler fibre with a negative rational curve}\\label{subsec:II:compact-negative-curve}\n\n'+new+'\n\\subsection{Vertical elliptic fields and surface models}\\label{subsec:II:vertical-elliptic-models}\n'
pkg.guard('UN79-complete-compact-negative-curve',old,fragment,'Complete construction unit, with every map, multiplicity, canonical order, stratum number and compact horizontal comparison retained. The following surface-model unit stays open.')
replayed=main.replace(old,fragment,1)
for pat in [r'\\label\{([^{}]+)\}',r'\\hypertarget\{([^{}]+)\}']:
    a=Counter(re.findall(pat,main));b=Counter(re.findall(pat,replayed))
    assert all(b[k]==v for k,v in a.items())
pkg.write(fragment)

