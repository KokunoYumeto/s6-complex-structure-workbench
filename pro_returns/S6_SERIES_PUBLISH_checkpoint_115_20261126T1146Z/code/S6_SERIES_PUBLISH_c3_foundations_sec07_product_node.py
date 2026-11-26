from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

p = Package('product_node', 'early smooth-curve intersection owner / contracted-section node input')
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
un9 = block(source, 'cdp:st:C.2.UN.9')
r14 = block(source, 'night:P4R.14')

intersection = r'''\begin{lemma}[Two hypersurfaces meeting along a smooth curve]\hypertarget{tag-P299}{}\label{lem:II:smooth-curve-intersection}
\StatementRecord{lem:II:smooth-curve-intersection}{proved}{P299}{}
Let two reduced hypersurface germs $\phi=0$ and $\psi=0$ in a smooth complex threefold have common zero set equal to the smooth curve $\Gamma=\{x=y=0\}$. Let $z$ be its coordinate and let $r$ be their intersection multiplicity on a generic transverse plane. Then
\[
 A=\C\{x,y,z\}/(\phi,\psi)
\]
is a finite free $\C\{z\}$-module of rank $r$, and its fibre at $z=0$ has complex dimension $r$. For $r=1$, $(\phi,\psi,z)$ is a holomorphic coordinate system. For $r=2$, one factor is smooth; after interchanging them if necessary, there are holomorphic coordinates $(X,Y,z)$ in which
\[
                     \phi=X,\qquad \psi=Y^2+XH(X,z).
\]
\end{lemma}
\begin{proof}
The zero fibre of $A$ over $z=0$ is isolated, so the analytic map to the $z$-disc is finite after taking a sufficiently small representative. The two equations form a regular sequence in the regular ambient local ring. Their quotient is therefore a one-dimensional complete intersection, and its parameter $z$ is a nonzerodivisor. A finite torsionfree module over the discrete valuation ring $\C\{z\}$ is free. Its rank is the generic transverse intersection multiplicity $r$, proving the fibre-length assertion.

For $r=1$, the quotient $\C\{x,y\}/(\phi(x,y,0),\psi(x,y,0))$ has length one, so its ideal is $(x,y)$. The two linear parts are independent. Thus $(x,y,z)\mapsto(\phi,\psi,z)$ has invertible Jacobian and its inverse is the unique local solution of these coordinate equations.

For $r=2$, the two generators of this plane ideal cannot both lie in $(x,y)^2$, since the quotient would retain the three independent classes $1,x,y$. Thus one factor, say $\phi$, is smooth. Set $X=\phi$ and choose a complementary normal coordinate $y$, keeping $z$. On $X=0$ the zero set of $\psi$ is exactly $y=0$; its generic multiplicity is two, so $\psi|_{X=0}$ is a unit times $y^2$. The parameter Morse construction in $y$, keeping $X,z$, gives $Y=(y-\mu(X,z))\sqrt{V(X,y,z)}$, with $V$ a unit and with inverse the unique small solution for $y$. Its centre satisfies $\mu(0,z)=0$, and its remaining critical value vanishes on $X=0$. It is therefore $XH(X,z)$, which proves the exact displayed form.
\end{proof}
'''

old_algebra = r'''Their common zero set is exactly the axis. The quotient
\[
                A=\C\{x,y,z\}/(\phi,\psi)
\]
is finite over $\C\{z\}$, by the isolated zero of its fibre at $z=0$. It is a one-dimensional complete intersection, so the parameter $z$ is a nonzerodivisor. Thus it is a finite free module over the discrete valuation ring $\C\{z\}$. Its rank is two, the intersection multiplicity of the two generic $A_3$ branches. Consequently
\[
             \dim_{\C}\C\{x,y\}/(\phi(x,y,0),\psi(x,y,0))=2.
\]
Both generators cannot belong to $(x,y)^2$, since that quotient would still contain the three independent classes $1,x,y$. Hence one factor, say $\phi$, is smooth.'''
new_algebra = r'''Their common zero set is exactly the axis, and their generic transverse intersection multiplicity is two. Apply \cref{lem:II:smooth-curve-intersection} to these same factors and the same curve coordinate $z$. Its finite free intersection algebra has rank two and special-fibre length two; one factor, say $\phi$, is smooth.'''
assert old_algebra in r14

statement = un9[:un9.index(r'\begin{proof}')]
statement = statement.replace(
    r'\StatementRecord{cdp:st:C.2.UN.9}{proved}{01EZ}{\SeriesRef{cdp:eq:C.UNNODE.2}, \SeriesRef{cdp:st:A.5.15}, \SeriesRef{cdp:eq:C.UNNODE.3}}',
    r'\StatementRecord{cdp:st:C.2.UN.9}{proved}{01EZ}{\cref{lem:II:smooth-curve-intersection,cdp:st:A.5.15,lem:II:boundary-deformation-transport}}')
matrix = un9[un9.index(r'\item Suppose instead that $Q(0)$ is singular.'):un9.index(r'\item Consider the actual perturbation')]
matrix = matrix.replace(r'\item Suppose instead that $Q(0)$ is singular.', r'\item Suppose $Q(0)$ is singular.')
new_un9 = statement + r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item The entire reduced critical curve is a smooth axis $\Gamma$. Each local irreducible component of a reducible support meets every other component in a curve contained in $\Gamma$, and therefore contains $\Gamma$. The generic ordinary node has two branches, so there are at most two local components. If the generator is reducible, write $f=V\phi\psi$ with the two reduced factors and a unit $V$. Their common zero set is $\Gamma$ and their generic transverse intersection multiplicity is one. Apply \cref{lem:II:smooth-curve-intersection} with $r=1$: $(\phi,\psi,z)$ is a coordinate system. Replacing its first coordinate by $V\phi$, keeping the other two, is invertible, with inverse the unique solution of $X=V(\phi,\psi,z)\phi$. It gives $f=XY$ exactly. This argument permits every original positive full multiplicity on the two components.

\item In the locally irreducible case the full map has the form $F=Uf^M$. Choose the root $f_0=U^{1/M}f$, so $F=f_0^M$ exactly. Its critical-set germ is still $\Gamma$: every critical component through the point has constant value zero, and on that zero set $df_0=U^{1/M}df$. Choose coordinates $(x,y,z)$ with $\Gamma=\{x=y=0\}$. The transverse quadratic term of $f_0$ is
\[
                       (x,y)Q(z)(x,y)^{\mathsf t},
\]
where $Q$ is symmetric and has determinant not identically zero. Shrink so that $\det Q(z)\ne0$ for $z\ne0$. If $Q(0)$ is invertible, the parameter Morse map gives $f_0=X^2+Y^2$. The linear coordinates $X+\mathrm iY,X-\mathrm iY$ give its product form. Absorbing the remaining unit $U^{-1/M}$ into the first factor by the same invertible map as above gives the product form of the original generator. It remains to exclude singular $Q(0)$.

''' + matrix + r'''\item Use the full-root perturbation
\[
                  f_E=f_0+(x,y)E(x,y)^{\mathsf t}.
\]
At $(0,0,z_0)$ the rank-one parameter Morse map gives $f_E=X^2+y^2h(y,z)$. The factor $y^2$ follows from vanishing of the function and its normal first derivative along the unchanged axis. Equation~\eqref{cdp:eq:C.UNNODE.2} says that $h(0,z_0)=0$ and $h_z(0,z_0)\ne0$, up to the nonzero coefficient of the split quadratic direction. Thus the invertible coordinate $Z=h(y,z)$ gives
\[
                           f_E=X^2+y^2Z.
\tag{C.UNNODE.3}\hypertarget{tag-015F}{}\label{cdp:eq:C.UNNODE.3}
\]
The substitution $Z\mapsto-Z$ identifies this with the $(a,b,c)=(2,2,1)$ binomial of \cref{cdp:st:A.5.15}. Its compact spherical class has square $-2(2/\gcd(2,1))(1/\gcd(2,1))=-4$. This class is represented by a continuous map from $S^2$; embeddedness is not required.

\item Choose a small closed ball transverse to $\Gamma$ and to the smooth zero-fibre stratum. Its critical values at $E=0$ are all zero. Along the compact boundary link, $Q$ is invertible, and the parameter Morse maps give fixed product-node charts for all small $E$, retaining the curve coordinate. A real direction in that coordinate is tangent to every function level and transverse to the fixed boundary. On the remaining boundary, submersivity of the original zero level persists for small parameters and small target values. Thus these maps verify all boundary hypotheses of \cref{lem:II:boundary-deformation-transport} for $g_E=f_E$ and the established full-map equality $F=f_0^M$.

That lemma transports the compact class first through regular local values, then through a target path avoiding the finitely many critical values, and then along the parameter family at its common outer regular value $b$. Its final inclusion is into the original fibre $F=b^M$. It preserves the intersection with the compact parallel representative, so the transported sphere has square $-4$. In a complex two-torus its sphere map lifts to the contractible universal cover and has zero homology class, a contradiction. Hence $Q(0)$ is invertible and the product coordinates above apply. The root and final unit-coordinate maps also establish the stated conclusion for a unit times a common positive power.
\end{enumerate}
\end{proof}
'''
new_un9 = p.clean(new_un9, 'cdp:st:C.2.UN.9')
for equation in re.findall(r'\\begin\{equation\}([\s\S]*?)\\end\{equation\}', new_un9):
    assert not re.search(r'\n[ \t]*\n', equation)

anchor = source[source.index(r'\begin{proposition}[Contact of two smooth branches]'):].splitlines()[0]
p.guard('P299 before smooth-branch contact', anchor, intersection+'\n'+anchor,
        'Put the complete finite-free intersection owner after P295 and before the R14 and UN9 applications.')
p.record('D10,D12,D14,D16', 'lem:II:smooth-curve-intersection', old_algebra, intersection,
         'Extract the complete finite-free intersection argument from R14 with its generic rank r stated explicitly. The same proof gives the exact rank-one independent-coordinate map and the retained rank-two smooth-factor/Morse map. Every original rank-two conclusion remains at the single owner and is applied to the identical factors in R14.')
p.guard('R14 intersection application', old_algebra, new_algebra,
        'Apply P299 with the same factors, same smooth axis and generic multiplicity2; retain the complete following quartic determinant identity and every other R14 step.')
p.record('D12,D14', 'night:P4R.14', old_algebra, new_algebra,
         'The complete old/current R14 proof was read. Only the shared intersection proof moves; the exact rank-two specialization, smooth factor and following Delta determinant comparison remain. All newly proved full-multiplicity polar data and corrected equation whitespace are untouched.')
old_record = r'\StatementRecord{night:P4R.14}{proved}{02Y7}{\cref{cdp:st:A.5.15,cdp:st:A.5.17,night:P4.28,lem:II:boundary-deformation-transport}}'
new_record = r'\StatementRecord{night:P4R.14}{proved}{02Y7}{\cref{cdp:st:A.5.15,cdp:st:A.5.17,night:P4.28,lem:II:boundary-deformation-transport,lem:II:smooth-curve-intersection}}'
p.guard('R14 intersection dependency', old_record, new_record,
        'Record the exact new earlier owner used by the rank-two application.')
p.record('D10', 'night:P4R.14', old_record, new_record,
         'The proved status and all existing inputs remain; P299 records the shared intersection argument applied to the same two factors.')
p.guard('UN9 full-multiplicity node proof', un9, new_un9,
        'Retain the original broad statement and all node-matrix formula payloads. Prove the two-factor case by the exact rank-one intersection map, and use the original perturbation only after its full common root has been established.')
p.record('D10,D12,D14,D16,D25', 'cdp:st:C.2.UN.9', un9, new_un9,
         'The complete old proof transports a reduced-function family under a statement broader than its final common-power comparison. The exact rank-one intersection algebra resolves the two-factor case without changing its original multiplicities. In the remaining locally irreducible case the full root F=f0^M is justified before the matrix perturbation; the unchanged simple determinant zero and binomial sphere then meet P295 through their precise fixed product charts. Every original conclusion, constant matrix construction, tagged formula, square −4 class and final unit-coordinate map remains.')
for row in p.rows:
    row['old_location'] = row['statement_id']+' / complete current statement and proof'
p.write(intersection+'\n'+new_un9)
