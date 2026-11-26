from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

p = Package('nodal_hessian', 'local rigidity / P4.41')
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
old = block(source, 'night:P4.41')
start = old.index('We claim that $A(0)$ cannot be a unit.')
end = old.index(r'\item If $g_z(0)$ is a unit, both saturated Hessian lines', start)
replacement = r'''We claim that $A(0)$ cannot be a unit. Suppose it is. If $g_z(0)\ne0$, then $dg(0)\ne0$ and the ambient Hessian of (4.41c) is $2A(0)\,dg(0)\otimes dg(0)\ne0$. Apply \cref{night:P4R.15} to this original reduced generator and its original full fibre. Its exact product coordinates make the entire reduced critical curve smooth, contradicting the node. This application includes the original suspension construction: straightening $g$ and completing the square gives the plane residual obtained from $k^4$; the finite-gradient and nonzero-critical-value construction is the one in \cref{cdp:st:A.5.17}. The full-function comparison is supplied by the two exact cases in \cref{night:P4R.15}.

\item Suppose $g_z(0)=0$. Its $xy$ coefficient is a unit, and take $k=z$. The square-root coordinate in the first factor of (4.41c) gives
\[
       G=\sqrt A\,g+\frac{B}{2\sqrt A}z^2,\qquad
       f=G^2+Dz^4,\qquad D=C-\frac{B^2}{4A},
\]
and the conductor is still $I=(G,z^2)$. Here $G(x,y,0)$ is $xy$ times a unit and $dG(0)=0$. We determine the local factors from this conductor before deforming the full function.

Put $R=\C\{x,y,z\}/(f)$. Since $z$ divides neither $G$ nor $f$, it is a nonzerodivisor in $R$. The finite-duality multiplier identification and Gorenstein biduality of \cref{lem:II:conductor-duality} give $\overline R=\operatorname{Hom}_R(I,R)$ for the normalization, with every homomorphism represented by multiplication in the total quotient ring. Set $t=G/z^2$. Then $t^2=-D$, $tz^2=G$, and $tG=-Dz^2$, so $R+Rt\subset\overline R$. Conversely, for a multiplier $\theta$ write $\theta z^2=r$ and $\theta G=s$ in $R$. Lift these elements to the regular ambient ring. The relation $rG-sz^2=0$ in $R$ has the form
\[
          rG-sz^2=v(G^2+Dz^4).
\]
Thus $G(r-vG)=z^2(s+vDz^2)$. The regular sequence $(G,z^2)$ implies $r-vG\in(z^2)$, so division by the nonzerodivisor $z^2$ gives $\theta=v t+w$. We have proved the equality of algebras
\[
                    \overline R=R+Rt,\qquad t^2=-D.
\]
Its nonzero fibre algebra at the origin is a quotient of $\C[t]/(t^2+D(0))$. If $D(0)=0$, it has just one maximal ideal. The semilocal normalization is therefore local and normal, hence a domain; $R$ embeds in it, so the original reduced germ is locally irreducible. If $D(0)\ne0$, choose $s=\sqrt{-D}$. The two coprime nonunit factors are $G-z^2s$ and $G+z^2s$. The normalization has at most two points over the origin by its displayed fibre algebra, and each factor has a normalization point there. Thus these are exactly its two local irreducible factors.

\item In the locally irreducible case, the full map is $Vf^M$. Take its exact root $f_0=V^{1/M}f$, writing
\[
 f_0=G_0^2+z^4D_0,\qquad
 G_0=V^{1/(2M)}G,\quad D_0=V^{1/M}D.
\]
It still has $G_0(x,y,0)=xy$ times a unit and $dG_0(0)=0$. The first deformation is $D_0\mapsto D_0+\delta$, with $\delta$ arbitrarily small and chosen so that this is a unit. The coordinate $Z=z(D_0+\delta)^{1/4}$, keeping $x,y$, is invertible; its inverse is the unique small solution for $z$, whose derivative at the origin is nonzero. Parameter Morse coordinates in $x,y$, keeping $Z$, then give $G_0=XY+a(Z)$, where $a\in(Z^2)$. This is the same square-completion construction as in \cref{cdp:st:A.5.17}: the plane Hessian is invertible, and its successive square-root coordinates and their implicit inverses depend holomorphically on $Z$.

A small change $a\mapsto a+\alpha Z^2$ makes $a''(0)\ne0$. Shift $G_0$ by $-\varepsilon$. The resulting root function is
\[
                    (XY+a(Z)-\varepsilon)^2+Z^4.
\]
At the origin its critical value is $\varepsilon^2$, its $XY$ Hessian entry is $-2\varepsilon$, and its $ZZ$ entry is $-2\varepsilon a''(0)$. It is a Morse point. These are the original suspension and moving-node formulas, now applied with the established full-map equality $F=f_0^M$.

\item In the two-factor case, take $Z=zs^{1/2}$ with $s^2=-D$, keeping $x,y$; its implicit inverse is again holomorphic. The reduced function is $G^2-Z^4$, and the full function has its original multiplicities:
\[
                F=U(G-Z^2)^a(G+Z^2)^b,
                \qquad a,b\ge1.
\]
Parameter Morse coordinates in $x,y$, keeping $Z$, give $G=XY+A(Z)$ with $A\in(Z^2)$ and transport the unit to a holomorphic unit still denoted $U$. Retain this unit and both factors. Deform $A$ to $A_\alpha=A+\alpha Z^2$ and choose an arbitrarily small $\alpha$ such that, writing $A_\alpha=cZ^2+O(Z^3)$,
\[
          N=a+b,\qquad T=a(c-1)+b(c+1)=Nc+b-a\ne0.
\]
The full deformation is exactly
\[
 F_{\alpha,\varepsilon}
 =U(X,Y,Z)(XY+A_\alpha(Z)-Z^2-\varepsilon)^a
                (XY+A_\alpha(Z)+Z^2-\varepsilon)^b.
\]
These are holomorphic deformations of the two original analytic factors, with their multiplicities fixed.

For the selected $\alpha$, put $(X,Y,Z)=\varepsilon(r_1,r_2,r_3)$. Each of the two parenthesized factors, divided by $-\varepsilon$, is a holomorphic function of $(\varepsilon,r)$ equal to $1$ at $\varepsilon=0$. Its linear term in $\varepsilon$ is
\[
                 -r_1r_2-(c\mp1)r_3^2.
\]
Consequently the logarithmic gradient
\[
 \mathcal L(\varepsilon,r)
       =\nabla_{X,Y,Z}\log F_{\alpha,\varepsilon}(\varepsilon r)
\]
extends holomorphically to $\varepsilon=0$. If $\ell_j=(\partial_j\log U)(0)$, its limiting value is
\[
            (\ell_1-Nr_2,\ \ell_2-Nr_1,\ \ell_3-2Tr_3).
\]
It has the unique zero
$r_0=(\ell_2/N,\ell_1/N,\ell_3/(2T))$, and its derivative in $r$ is
\[
          \begin{pmatrix}0&-N&0\\-N&0&0\\0&0&-2T\end{pmatrix},
          \qquad \det=2N^2T\ne0.
\]
The implicit-function theorem supplies $r(\varepsilon)$ with $\mathcal L(\varepsilon,r(\varepsilon))=0$ and $r(0)=r_0$. Thus $p_\varepsilon=\varepsilon r(\varepsilon)$ is a critical point of the full function. Its value is $(-\varepsilon)^N U(0)(1+O(\varepsilon))\ne0$. At that critical point the exact Hessian identity is
\[
 \operatorname{Hess}F_{\alpha,\varepsilon}(p_\varepsilon)
   =\frac{F_{\alpha,\varepsilon}(p_\varepsilon)}{\varepsilon}
             D_r\mathcal L(\varepsilon,r(\varepsilon)).
\]
The displayed limiting matrix is invertible, so this is a holomorphic Morse point for sufficiently small nonzero $\varepsilon$.

\item We specify the transport for both constructions. Choose an outer ball transverse to the original zero-divisor strata, small enough that its original critical values are all zero. In the root case, the first family $G_0^2+z^4(D_0+\delta)$ has fixed transverse $A_3$ charts near the boundary. After the selected $\delta$ and its invertible coordinate changes, choose an inner ball about the origin inside that outer ball. The family $(XY+a(Z)+\alpha Z^2-\varepsilon)^2+Z^4$ has the same boundary product charts, along the moving smooth parts of $Z=0,XY=\varepsilon$. The nested transports of \cref{lem:II:boundary-deformation-transport} take its local Morse sphere first to the selected $\delta$ root fibre, then to an original root fibre, and finally into $F^{-1}(b^M)$.

For the two-factor family, near each boundary intersection link use $v=XY+A_\alpha(Z)-\varepsilon$ and $Z$ as the two normal coordinates. A complementary coordinate runs along the moving curve and is transverse to the boundary. The full transverse function is $U(v-Z^2)^a(v+Z^2)^b$. The weighted unit map and inverse from \cref{prop:II:smooth-branch-contact}, with $k=2$, give the fixed function $(v-Z^2)^a(v+Z^2)^b$. At smooth component points, the corresponding charts are powers of a normal coordinate. These charts verify every boundary hypothesis of \cref{lem:II:boundary-deformation-transport} for $g_{\alpha,\varepsilon}=F_{\alpha,\varepsilon}$ and $m=1$.

In each case the local Morse sphere from \cref{cdp:st:A.5.17} has square $-2$ and is carried into an original torus fibre with the same square. Its sphere map lifts to the contractible universal cover of that torus, so its class has square zero. This contradiction proves $A(0)=0$ at the original point.

'''
new = old[:start] + replacement + old[end:]
new = new.replace(
    r'\StatementRecord{night:P4.41}{proved}{02XF}{\SeriesRef{night:P4.28}, \SeriesRef{night:P4R.10}, \SeriesRef{night:P4R.14}}',
    r'\StatementRecord{night:P4.41}{proved}{02XF}{\cref{lem:II:conductor-duality,cdp:st:A.5.17,night:P4R.10,night:P4R.15,prop:II:smooth-branch-contact,lem:II:boundary-deformation-transport}}')
new = p.clean(new, 'night:P4.41')
new = p.edit(new, 'An coordinate change', 'A coordinate change', 'D23', 'night:P4.41',
             'Use the grammatical article after removing production emphasis; the coordinate map is unchanged.')
for equation in re.findall(r'\\begin\{equation\}([\s\S]*?)\\end\{equation\}', new):
    assert not re.search(r'\n[ \t]*\n', equation), 'Blank paragraph inside a numbered equation'
p.guard('P441 exact full-function conductor proof', old, new,
        'Retain the entire original defect inequality, equality normalization and all conductor matrices. Resolve the A-unit contradiction by the actual normalization algebra and original full-factor deformations.')
p.record('D10,D12,D14,D16,D25', 'night:P4.41', old[start:end], replacement,
         'The complete original proof was read. Its nonzero ambient Hessian case applies the proved R15 at the original domain. In the remaining case, actual conductor duality and the explicit multiplier map give normalization R+R(G/z²); its fibre algebra proves exactly when a uniform full root is justified and when there are exactly two analytic factors. The original root deformation and Hessian formulas are retained at their established scope. The unequal-power case keeps U,a,b and constructs a full Morse point through an explicit rescaled logarithmic gradient with invertible limit. Both boundary transports identify their exact initial full maps. No hypothesis of the original inequality or equality conclusion changes.')
for row in p.rows:
    row['old_location'] = row['statement_id'] + ' / complete current statement and proof'
p.write(new)
