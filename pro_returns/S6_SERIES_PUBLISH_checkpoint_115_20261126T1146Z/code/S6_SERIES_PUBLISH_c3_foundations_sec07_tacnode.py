from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

p = Package('tacnode', 'local rigidity / P4R.14')
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
old = block(source, 'night:P4R.14')
statement = old[:old.index(r'\begin{proof}')]
statement = statement.replace(
    r'\StatementRecord{night:P4R.14}{proved}{02Y7}{\SeriesRef{night:P4.16}, \SeriesRef{night:P4.28}}',
    r'\StatementRecord{night:P4R.14}{proved}{02Y7}{\cref{cdp:st:A.5.15,cdp:st:A.5.17,night:P4.28,lem:II:boundary-deformation-transport}}')
example = old[old.index(r'\item The following reduced hypersurface'):old.index(r'\end{enumerate}')]
proof = r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Choose a coordinate $z$ on the critical curve and normal coordinates $x,y$. Its quadratic transverse Hessian has generic rank one. Diagonalization over $\C\{z\}$, with the coordinate maps of \cref{night:P4.28}, gives the quadratic term $h(z)x^2$. The cubic coefficient on the null direction vanishes identically. With weights two for $x$ and one for $y$, the weight-four terms are
\[
 h(z)x^2+a(z)xy^2+b(z)y^4,\qquad
 \Delta(z)=4h(z)b(z)-a(z)^2.\tag{P4R.14.2}
\]
The remaining terms have larger weight, and $\Delta$ is generically nonzero.

\item We prove that $\Delta$ is a unit, keeping track of the irreducible factors of the full fibre. Every local component of the reduced support contains the critical axis: its intersection with another component has dimension at least one and lies on that axis. The generic transverse germ has two branches, so there are at most two local components.

First consider a locally irreducible reduced equation. The full map is $Uf^M$, and the exact root $f_0=U^{1/M}f$ satisfies $F=f_0^M$. Its critical germ is the same axis: every critical component through the origin has value zero, and on the zero set $df_0=U^{1/M}df$. Its quartic discriminant is the preceding $\Delta$ multiplied by the square of a unit on the axis. We may use this root for the following deformation.

A zero of $\Delta$ persists, counted with multiplicity, under small independent constant changes of $h,a,b$, by the argument principle on a small parameter disc. Generic such changes make its zeros simple and avoid $h=0$: the equations $h=\Delta=0$ require $a=0$, while for $h\ne0$ the derivative with respect to the constant in $b$ is $4h\ne0$. At a simple zero with $h\ne0$, parameter Morse coordinates give
\[
                X^2+y^4V(y,z),\qquad V_z(0,0)\ne0.
\]
The coordinate $Z=V(y,z)$ gives $X^2+y^4Z$. Its local sphere from \cref{cdp:st:A.5.15} has nonzero square. On the fixed boundary the root functions retain the product charts $X^2+Y^4$, by the parameter Morse map and a fourth root of a unit. Apply \cref{lem:II:boundary-deformation-transport} to these root functions, with the original exact equality $F=f_0^M$. The sphere reaches an original torus fibre, a contradiction. Thus the discriminant is a unit in this case.

\item In the reducible case write $f=\phi\psi$ with the two local reduced factors, absorbing the generator unit into $\psi$. Their common zero set is exactly the axis. The quotient
\[
                A=\C\{x,y,z\}/(\phi,\psi)
\]
is finite over $\C\{z\}$, by the isolated zero of its fibre at $z=0$. It is a one-dimensional complete intersection, so the parameter $z$ is a nonzerodivisor. Thus it is a finite free module over the discrete valuation ring $\C\{z\}$. Its rank is two, the intersection multiplicity of the two generic $A_3$ branches. Consequently
\[
             \dim_{\C}\C\{x,y\}/(\phi(x,y,0),\psi(x,y,0))=2.
\]
Both generators cannot belong to $(x,y)^2$, since that quotient would still contain the three independent classes $1,x,y$. Hence one factor, say $\phi$, is smooth. Its linear term on the axis is a unit times $x$. Write its weight-two term as $\alpha x+\beta y^2$ and that of $\psi$ as $\gamma x+\delta y^2$, with coefficients in $\C\{z\}$ and $\alpha$ a unit. On the smooth surface $\phi=0$, the only zero set of $\psi$ is $y=0$. Therefore the restricted function is a unit times $y^2$, its generic contact order being two. Its leading coefficient $\delta-\gamma\beta/\alpha$ is a unit. Comparing the product with the preceding quartic gives
\[
                 \Delta=-(\alpha\delta-\beta\gamma)^2,
\]
so $\Delta$ is a unit also here. This argument changes neither factor nor its full multiplicity.

\item If $h(0)\ne0$, parameter Morse coordinates and a fourth root of the residual unit give the first form in (P4R.14.1). Suppose $h(0)=0$. Then $a(0)\ne0$. The function
\[
                    \frac{f(y^2v,y,z)}{y^4}
\]
is holomorphic and restricts at $y=0$ to $h(z)v^2+a(z)v+b(z)$. Its finite root $-b(0)/a(0)$ is simple. The implicit-function theorem gives a holomorphic root $v(y,z)$; division by its monic graph gives $X=x-y^2v(y,z)$ and $f=Xg$. On $X=0$, $g$ is $y^2$ times a unit. Its parameter Morse centre is zero there, and its critical value vanishes there. Parameter Morse coordinates in $y$, keeping $X,z$, therefore give exactly
\[
                  f=X\bigl(Y^2+XH(X,z)\bigr).\tag{P4R.14.3}
\]
Here $H(0,z)$ is not identically zero, because the generic transverse Hessian has rank one, while $H(0,0)=0$. This factorization also shows that the locally irreducible case considered above cannot occur. Both forms obtained from a unit discriminant are reducible.

\item Write the full map in these coordinates as
\[
                   F=U X^a\bigl(Y^2+XH(X,z)\bigr)^b,
                   \qquad a,b\ge1.
\]
The two factors are the two local components. In the second form the second factor cannot split further, since every local component contains the axis and there are at most two. Choose $V=U^{1/b}$ and apply the parameter Morse construction in $Y$ to $V(Y^2+XH)$, keeping $X,z$. If its centre is $Y=\mu(X,z)$ and its quadratic unit is $A$, the new coordinate is $\widetilde Y=(Y-\mu)\sqrt A$, with inverse the unique local solution of this equation. The centre vanishes on $X=0$, and the remaining critical value is $XK(X,z)$. Thus the full function becomes exactly
\[
                         F=X^a(\widetilde Y^2+XK)^b.
\]
Differentiating that critical value in $X$ at $X=0$ gives the exact identity
\[
                    K(0,z)=V(0,0,z)H(0,z).
\]
In particular $K_z(0,0)\ne0$ is equivalent to $H_z(0,0)\ne0$. The reduced critical germ of $X(\widetilde Y^2+XK)$ is still the same axis. Indeed its reduced zero divisor is unchanged under this invertible map and multiplication by a unit, and every critical component through the origin has constant value zero, as above. We now rename $\widetilde Y$ as $Y$.

\item Put $N=a+b$ and $G_{a,b}=NK+bXK_X$. Suppose $K_z(0,0)=0$. The germ $K_z$ is nonzero and not divisible by $X$, since $K(0,z)$ has finite order at least two. We prove that $(K_z,G_{a,b})$ has an isolated zero. On a parametrized irreducible branch of $K_z=0$, choose a parameter with $X=t^r$, $r\ge1$. The chain rule there gives
\[
                       XK_X=\frac{t}{r}\frac{dK}{dt}.
\]
If $G_{a,b}$ vanished identically, every coefficient of order $j$ in $K(t)$ would be multiplied by $N+bj/r>0$. Hence $K$ would vanish identically on that branch, and then so would $K_X$. This would give a critical-curve branch of the reduced function off $X=0$, contradicting the hypothesis. The intersection is therefore isolated and has positive local degree.

Deform $K$ to $K_s=K-\eta z-\varepsilon$, retaining the full function $F_s=X^a(Y^2+XK_s)^b$. Its off-divisor critical equations are
\[
       Y=0,\qquad K_z-\eta=0,\qquad
       G_{a,b}-N\eta z-N\varepsilon=0.
\]
The last two are the fibres of
\[
        \Psi_{a,b}(X,z)=
              \left(K_z,\frac{G_{a,b}-NzK_z}{N}\right).
\]
Its isolated zero has positive local degree. On a small compact representative this degree persists for small parameters. Choose a regular parameter value outside the images of $X=0$ and $K_X=0$. These images have real four-dimensional measure zero, by their countable smooth two-dimensional strata. The germ $K_X$ is not identically zero: otherwise $K$ would depend only on $z$ and $(K_z,G_{a,b})$ would vanish on the line $z=0$. Thus the exceptional images do not fill the open parameter ball, and the chosen fibre is nonempty and finite.

\item Write $G_s=G_{a,b}-N\eta z-N\varepsilon$ and
\[
 J=\det\frac{\partial(G_s,K_z-\eta)}{\partial(X,z)}.
\]
At a chosen solution $K_s=-bXK_X/N\ne0$, so
\[
            F_s=\left(-\frac bN\right)^b
                         X^{a+2b}K_X^b\ne0.
\]
At $Y=0$, the logarithmic derivatives are
\[
 (\log F_s)_X=\frac{G_s}{XK_s},\qquad
 (\log F_s)_z=\frac{b(K_z-\eta)}{K_s},\qquad
 (\log F_s)_{YY}=\frac{2b}{XK_s}.
\]
The mixed $Y$ entries vanish at the critical point. The determinant of the $X,z$ logarithmic Hessian block is $bJ/(XK_s^2)$. Since the full gradient vanishes there, this gives
\[
                 \det\operatorname{Hess}F_s
                   =\frac{2b^2F_s^3J}{X^2K_s^3}\ne0.
\]
These are holomorphic Morse points with nonzero critical values, in the full original multiplicities.

For $a=b=1$ and $K=H$, this calculation gives the original equations, with $G=2H+XH_X$,
\[
                H_z-\eta=0,\qquad G-2\eta z-2\varepsilon=0,
                \tag{P4R.14.4}
\]
the map $\Psi=(H_z,(G-2zH_z)/2)$, and the critical value
\[
                       f_{\eta,\varepsilon}=-\frac{X^3H_X}{2}.
                       \tag{P4R.14.5}
\]
Its $Y$-Hessian entry is $2X$, its remaining block is
\[
 \begin{pmatrix}
 X(3H_X+XH_{XX})&X^2H_{Xz}\\
 X^2H_{Xz}&X^2H_{zz}
 \end{pmatrix},
\]
and its full determinant is $2X^4J$.

\item Choose a sufficiently small ball transverse to the smooth strata of the full zero divisor. Its original critical values are all zero, by the same critical-component argument. On its fixed boundary near the critical axis, $K_s(0,z)$ is a unit. The coordinate $T=XK_s(X,z)$, keeping $Y,z$, is invertible: its inverse is $X=\chi_s(T,z)$, the unique local solution of $T=XK_s(X,z)$. Write $\chi_s=T\kappa_s$ with $\kappa_s$ a unit. Then
\[
                   F_s=\kappa_s^a T^a(Y^2+T)^b.
\]
Weights $(2,1)$ in $(T,Y)$, of degree $2N$, remove this unit by multiplying $T$ by $(\kappa_s^a)^{1/N}$ and $Y$ by $(\kappa_s^a)^{1/(2N)}$, keeping $z$. Its inverse solves
\[
 \tau^{2N}=\kappa_s(\tau^{-2}T',z)^a,
 \qquad(T,Y,z)=(\tau^{-2}T',\tau^{-1}Y',z).
\]
The implicit derivative at the link is $2N\tau^{2N-1}\ne0$. This gives the fixed full transverse polynomial $T^a(Y^2+T)^b$. Its weighted Euler identity gives only critical value zero. The tangential coordinate is transverse to the chosen boundary. At smooth component points the corresponding fixed charts are a power of a normal coordinate. Hence \cref{lem:II:boundary-deformation-transport} applies to this full family with $m=1$. The Morse sphere constructed in \cref{cdp:st:A.5.17} has square $-2$ and transports into an original torus fibre, a contradiction.

Therefore $K_z(0,0)\ne0$, and the displayed relation between $K$ and $H$ gives $H_z(0,0)\ne0$. The coordinate $Z=H(X,z)$, keeping $X,Y$, puts the original reduced generator into the second form of (P4R.14.1); its inverse is the unique solution of $H(X,z)=Z$. Its normalization consists of the plane $X=0$ and the normal quadric $Y^2+XZ=0$, whose minimal resolution has one rational $(-2)$-curve. The first form has the two smooth factors $X\pm\mathrm iY^2$. No positive-genus exceptional curve occurs.

'''
new = statement + proof + example + '\\end{enumerate}\n\\end{proof}\n'
new = p.clean(new, 'night:P4R.14')
p.guard('R14 full-multiplicity tacnode proof', old, new,
        'Keep the original broad statement and all formula payloads. Use the common-root perturbation only at a locally irreducible point, a finite free rank-two intersection map for two factors, and the exact full weighted polar family with unit absorption and boundary inverse.')
p.record('D10,D12,D14,D16,D25', 'night:P4R.14', old, new,
         'The whole original proof was read. The reducible discriminant step now uses its actual two factor ideals, the finite free rank-two quotient, and the determinant identity. The full map U X^aQ^b is changed exactly to X^a(Y^2+XK)^b by a bth root and parameter Morse map; K(0,z)=U(0,0,z)^(1/b)H(0,z). The positive-coefficient branch valuation proves isolation of the weighted polar equations. Their full Hessian, all original a=b=1 formulas, the exact boundary maps, normalization conclusions and positive-genus example remain. No common-power assumption is imposed on unequal component multiplicities.')
for row in p.rows:
    row['old_location'] = row['statement_id'] + ' / complete current statement and proof'
p.write(new)
