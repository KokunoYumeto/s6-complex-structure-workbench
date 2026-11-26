from S6_SERIES_PUBLISH_c3_foundations_sec11_helpers import *

main = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
p = Package('nc_alignment', 'subsec:II:elliptic-alignment')
key = 'lem:II:vertical-elliptic-alignment'
old = block(main, key)
new = old
new = p.edit(new,
 r'Let $f:U\to\Delta$ be a proper holomorphic degeneration of connected complex two-tori from a smooth threefold, with full reduced SNC central fibre $S$. Let $T$ be a component and let $D\subset T$ be its boundary, the union of its intersections with the other components. Let $q:T\to B$ be a proper holomorphic map to a smooth compact connected curve, with connected fibres and smooth elliptic general fibre. Suppose every component of $D$ is vertical for $q$.',
 r'Let $f:U\to\Delta$ be a proper holomorphic degeneration of connected complex two-tori from a smooth threefold, with full reduced normal-crossing central fibre $S$. Let $\nu:T\to S_i$ be the smooth normalization of a component and put $D=(\nu^{-1}(\operatorname{Sing}S))_{\mathrm{red}}$. Both inverse branches of a self-double curve are included in $D$. Let $q:T\to B$ be a proper holomorphic map to a smooth compact connected curve, with connected fibres and smooth elliptic general fibre. Suppose every component of $D$ is vertical for $q$.',
 'D20,D25', key,
 'Extend the proved alignment input to a smooth normalization of a full reduced NC component. The receiving proof specifies the degree-one component resolution, the birational field transport, the exact polar set and the unchanged smooth-fibre monodromy map. The original embedded SNC domain is included by the identity normalization.')
old_first = r'''The root change of \cref{cdp:st:C.2.UN.16} has degree one here, and the smooth total space with SNC support needs no further resolution. Thus its covering component is this same $T$. The saturation and restriction maps \eqref{cdp:eq:C.CF.3}--\eqref{cdp:eq:C.CF.7} give a complex basis $V_1,V_2$ of commuting meromorphic fields on $T$, every constant linear combination semicomplete on its holomorphic locus. Their ambient representatives are holomorphic relative fields multiplied by meromorphic functions of the base. Their only polar divisors lie over zero. Cancellation of the generic order along $T$ removes that polar divisor; away from the other components every coefficient is holomorphic in codimension one and extends across the remaining codimension-two set by Hartogs. Thus the poles of the restricted fields are contained in $D$.'''
new_first = r'''Apply \cref{lem:II:cyclic-component-cover,cdp:st:C.2.UN.16} with $m_i=1$. The root change is the identity. The resolution $\rho:U'\to U$ has a smooth strict multiplicity-one component $E$ and a proper birational factorization
\[
 E\xrightarrow{\ r\ }T\xrightarrow{\nu}S_i,
 \qquad \rho|_E=\nu\circ r.
\]
The map $r$ is a composition of point blowups by \cite[Proposition~3.12, p.~20]{PopescuPampu2016}. In particular $r_*\OO_E=\OO_T$, and it is an isomorphism off finitely many points of $T$.

The saturation and restriction maps \eqref{cdp:eq:C.CF.3}--\eqref{cdp:eq:C.CF.7} give a two-dimensional complex space of commuting meromorphic fields on $E$. Transport them through $r$ on the common open isomorphism. This identifies the meromorphic function fields and derivations, so it preserves their complex-linear independence and brackets. By \cref{lem:II:semicomplete-transport}, every constant linear combination of the resulting fields $V_1,V_2$ on $T$ is semicomplete on its full holomorphic locus.

To locate their poles, push the ambient representatives through $\rho$. They are meromorphic vertical fields on $U$, holomorphic over $\Delta^*$; all their polar divisors are therefore central. The map $\rho$ is an isomorphism at the generic point of $S_i$, where the saturation makes their coefficient orders nonnegative. Thus $S_i$ is not a polar divisor. On $S_i\setminus\operatorname{Sing}S$, this is the only central branch, so the pushed fields are holomorphic near it, by extension of their coefficient functions across codimension two. Their restrictions pull back through the local isomorphism $\nu:T\setminus D\to S_i\setminus\operatorname{Sing}S$ to $V_1,V_2$. Hence their polar curves on $T$ are contained in $D$.'''
new = p.edit(new, old_first, new_first, 'D12,D17,D20,D25', key,
 'Apply the existing cyclic-component and semicomplete-transport owners at degree one, with the explicit maps rho, r and nu. The Hartogs polar-locus comparison takes place on the original smooth threefold, including self-double NC branches. No SNC hypothesis is silently imposed on T.')
old_rank = r'''If $Z_1=Z_2=0$, both fields are vertical. On a regular elliptic fibre they are translation fields, so their ratio is constant there. Proper descent gives
$V_2=(q^*H)V_1$ for a meromorphic function $H$ on $B$. It is nonconstant because the fields are independent over $\C$. The Stein factor of this ratio is again $T\xrightarrow q B\xrightarrow H\PP^1$, with identity graph resolution. Apply \cref{cdp:st:C.2.UN.29} to the same multiplicity-one component, its ambient saturated fields and this ratio. Its return-period identity \eqref{cdp:eq:C.RG.12} is proved on this Stein map before the relative contraction. The period-injection step there gives identity integral monodromy for this same $q$.'''
new_rank = r'''If $Z_1=Z_2=0$, both fields are vertical. On a regular elliptic fibre they are translation fields, so their ratio is constant there. Proper descent gives
$V_2=(q^*H)V_1$ for a meromorphic function $H$ on $B$. It is nonconstant because the fields are independent over $\C$. Put $q_E=q\circ r$. The equality $r_*\OO_E=\OO_T$ makes $q_E$ a connected-fibre map, and the ratio of the original saturated fields on $E$ is $q_E^*H$. Its graph is already defined, and its Stein factor is exactly $E\xrightarrow{q_E}B\xrightarrow H\PP^1$. Apply \cref{cdp:st:C.2.UN.29} to the multiplicity-one component $E$, these ambient saturated fields and this ratio. Its return-period identity \eqref{cdp:eq:C.RG.12} and period-injection step give identity integral monodromy for $q_E$. Remove also the finitely many images under $q$ of the centres of $r$. On the remaining base, $r$ restricts to biholomorphisms $r_b:(q_E)^{-1}(b)\to q^{-1}(b)$, and their maps $(r_b)_*$ identify the integral homology local systems. The inclusion of this base into the full smooth base of $q$ is surjective on fundamental groups. Thus the integral monodromy of $q$ is the identity as well.'''
new = p.edit(new, old_rank, new_rank, 'D12,D14,D20,D25', key,
 'Use the exact UN29 domain on the embedded covering component E. The map q_E=q composed with r, its Stein factor and the common smooth-fibre homology identify the monodromy on T; no direct use of UN29 on a nonembedded normalization is made.')
new = p.edit(new, r'p_g(T)=g(B)\le1.' , r'p_g(T)=g(B)\le1,', 'D23', key, 'Join the displayed conclusion grammatically to its following coherent-Euler clause.')
new = p.clean(new, key)
p.guard('P260 full NC normalization alignment',old,new.rstrip(), 'Complete original/receiving statement and proof comparison; exact degree-one resolution, field transport, polar-locus and monodromy maps prove the displayed NC scope.')
(OUT/'S6_SERIES_PUBLISH_II_sec11_nc_alignment_P260_input.tex').write_text(old+'\n',newline='\n')
(OUT/'S6_SERIES_PUBLISH_II_sec11_nc_alignment_P260.tex').write_text(new,newline='\n')

key = 'cdp:st:C.2.UN.67'
old67 = block(main,key)
n67 = old67
n67 = p.edit(n67,
 '''reduced SNC central fibre. Let \\(P\\) be a rational
component, with no minimality assumption. It cannot
have a smooth elliptic boundary curve \\(J\\) whose normal
line \\(N_{J/P}\\) is torsion and which is disjoint from
every other boundary curve on \\(P\\).''',
 '''reduced normal-crossing central fibre \\(S\\). Let
\\(\\nu:P\\to S_i\\) be a smooth rational normalization, and
let \\(D=(\\nu^{-1}(\\operatorname{Sing}S))_{\\mathrm{red}}\\),
including both inverse branches of each self-double curve.
There is no smooth elliptic component \\(J\\) of \\(D\\) whose
normal line \\(N_{J/P}\\) is torsion and which is disjoint
from every other component of \\(D\\).''',
 'D02,D20,D25',key,
 'The same complete rational pencil proof now applies to the explicitly defined smooth normalization and labelled boundary, using the receiving NC alignment owner. The original rational embedded component domain remains included.')
n67 = p.edit(n67,
 '''In particular a rational component, including a rational
elliptic surface and any point blowups of a rational
surface, cannot be adjacent to an elliptic Hopf component
or a nonlinear Hopf component. No Hopf leaf can have a
rational parent.''',
 '''In particular a component with rational smooth normalization,
including a rational elliptic surface and any point blowups
of a rational surface, cannot be adjacent to a component
whose smooth normalization is elliptic Hopf or nonlinear Hopf.
No Hopf leaf can have a parent with rational smooth normalization.''',
 'D20,D25',key,
 'State the exact normalization domain for the Hopf interface consequence. The receiving final comparison identifies the two normalized branches through xy=t and uses disjointness of Hopf curves to exclude triples on that interface.')
n67 = p.edit(n67,
 r'''\item Apply \cref{lem:II:vertical-elliptic-alignment} to the original component $T=P$, the connected pencil $q:P\to B=\PP^1$ in \eqref{cdp:eq:C.RH.4}, and its boundary. The preceding intersection computation makes every boundary curve vertical. The ambient family is the given smooth threefold with full reduced SNC fibre, so its degree-one component construction uses $P$ itself. The lemma proves identity integral monodromy for this precise pencil, in both the transverse/vertical and the two-vertical-field cases of its proof.''',
 r'''\item Apply \cref{lem:II:vertical-elliptic-alignment} with $(T,\nu,D)=(P,\nu,D)$, the connected pencil $q:P\to B=\PP^1$ in \eqref{cdp:eq:C.RH.4}, and the given full reduced normal-crossing torus degeneration. The preceding intersection computation makes every inverse boundary curve vertical. The lemma uses the degree-one component resolution $r:E\to P$ and the fibre identification for $q\circ r$ to prove identity integral monodromy for this precise pencil.''',
 'D12,D14,D20,D25',key,
 'Replace the embedded-SNC identification by the proved NC normalization alignment map. This is the exact original rational pencil and full base, including the rank-one saturated-field case.')
n67 = p.edit(n67,
 r'''\item On an elliptic Hopf
component every curve''',
 r'''\item On a normalization that is an elliptic Hopf
surface every curve''',
 'D20,D25',key,'Apply the Hopf curve results on the smooth normalization named in the statement.')
n67 = p.edit(n67,
 '''The \\(xy=t\\)
normal-product map gives''',
 '''Along an interface between the two distinct global
components, each normalized branch maps isomorphically to
the double curve: the two global component labels preserve
the two local branches of the normal-crossing equation.
The \\(xy=t\\) derivative identification of their normal
lines therefore gives''',
 'D20,D25',key,
 'Specify the branch-to-double-curve maps and the derivative normal-product identification on the NC interface. The preceding absence of triple points makes the chosen elliptic boundary isolated on the rational normalization.')
step2a=n67.index(r'\item Use the Stein factor')
step2b=n67.index(r'\item Every other boundary',step2a)
step2=n67[step2a:step2b]
step2_new=step2.replace(r'\xrightarrow\nu',r'\xrightarrow\beta').replace(r'\deg\nu',r'\deg\beta').replace(r'\nu^{-1}',r'\beta^{-1}')
n67=p.edit(n67,step2,step2_new,'D20',key,'Name the finite map of the pencil Stein factor beta, preserving nu for the normalization throughout. The exact map and all torsion-order conclusions are unchanged.')
n67=p.edit(n67,'This constructs the required elliptic\nmap on the nonminimal surface $P$.','This constructs the connected elliptic\nmap on $P$.','D05,D08',key,'State the resulting map in mathematical language.')
n67=p.edit(n67,r"The root projection is finite \'etale, and the cited proof retains relative minimality by canonical intersection, the primitive smooth fibre, the free translation inertia and the invariant full-fibre coefficient functions.",r"The root projection is finite \'etale. The canonical-intersection argument in \cref{lem:II:identity-monodromy-elliptic} preserves relative minimality, and its primitive-fibre and translation-inertia maps give the invariant full-fibre coefficient functions.",'D08,D20',key,'Describe the exact maps used from the earlier owner without process vocabulary, naming P306 for its canonical-intersection and coefficient arguments.')
n67=p.edit(n67,r'The root chart in the proof of \cref{lem:II:identity-monodromy-elliptic}, used by the alignment lemma on',r'The root chart of \cref{def:II:elliptic-root-curve}, applied in \cref{lem:II:identity-monodromy-elliptic} and used by the alignment lemma on','D04,D12,D20',key,'Point to the newly admitted single root-chart owner. Its exact map w^m=u,s=wh is specialized at m=a and the identical full fibre; the P306 canonical and invariant direct-image applications remain.')
for ref in ['cdp:st:C.2.UN.37','cdp:st:C.2.UN.50','cdp:st:C.2.UN.53']:
 n67=p.edit(n67,r'\ref{'+ref+'}',r'\cref{'+ref+'}','D04',key,'Use statement-type navigation for the exact Hopf map or comparison owner.')
n67 = p.clean(n67,key)
p.guard('UN67 full NC normalization obstruction',old67,n67.rstrip(),'Complete original/receiving proof comparison. Every rational-pencil, torsion-order, root and direct-image calculation remains, with the exact normalization and NC alignment application made explicit.')
(OUT/'S6_SERIES_PUBLISH_II_sec11_nc_alignment_UN67_input.tex').write_text(old67+'\n',newline='\n')
(OUT/'S6_SERIES_PUBLISH_II_sec11_nc_alignment_UN67.tex').write_text(n67,newline='\n')
p.write(new+'\n'+n67)
