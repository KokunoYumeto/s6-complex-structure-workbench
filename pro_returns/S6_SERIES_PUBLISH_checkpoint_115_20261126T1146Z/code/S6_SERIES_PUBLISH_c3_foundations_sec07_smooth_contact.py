from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

p = Package('smooth_contact', 'local rigidity / P298 before the cusp owner and P4R.15')
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
r15 = block(source, 'night:P4R.15')
a517 = block(source, 'cdp:st:A.5.17')

owner = r'''\begin{proposition}[Contact of two smooth branches]\hypertarget{tag-P298}{}\label{prop:II:smooth-branch-contact}
\StatementRecord{prop:II:smooth-branch-contact}{proved}{P298}{\cref{prop:II:weighted-two-branch-sphere,cdp:st:A.5.17,lem:II:boundary-deformation-transport}}
Let $F$ be a holomorphic map from a smooth complex threefold to a smooth curve, with nearby smooth fibres complex two-tori. Suppose its full local expression is
\[
 F(X,Y,Z)=U(X,Y,Z)(X-H(Y,Z))^a(X+H(Y,Z))^b,
 \qquad a,b\ge1,
\]
where $U$ is a holomorphic unit and $H\ne0$ vanishes at the origin. Then $\{H=0\}_{\mathrm{red}}$ is smooth. If $k$ is its multiplicity in $H$, an invertible holomorphic coordinate change puts the full function in the form
\[
                   (X-Y^k)^a(X+Y^k)^b.
\]
Every reduced local generator of its support has the exact product form $X^2-Y^{2k}$ in holomorphic coordinates.
\end{proposition}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Factor $H=\nu\prod_i h_i^{k_i}$ in $\C\{Y,Z\}$, with $\nu$ a unit and the $h_i$ distinct reduced irreducible factors. We use holomorphic deformations $H_s$ which retain these exponents near the boundary, and keep the full family
\[
          F_s=U(X-H_s)^a(X+H_s)^b
\]
with the original $U,a,b$. Choose a small closed ball transverse to the smooth strata of $F_0^{-1}(0)$, meeting the plane curves $h_i=0$ in their smooth disjoint links. Every critical value of $F_0$ in this ball is zero after shrinking: its critical germ has finitely many components, and the function is constant zero on each component through the origin.

We verify the boundary data of \cref{lem:II:boundary-deformation-transport} for this full family. Off the intersection of the two branches, a normal coordinate and a root of the unit give $w^a$ or $w^b$. On the intersection link belonging to $h_i$, write $H_s=\nu_s h_{i,s}^{k_i}$ with $\nu_s$ a unit, and take the coordinate $y=\nu_s^{1/k_i}h_{i,s}$, with a complementary coordinate $z$. The inverse is the unique local solution of these two coordinate equations; their Jacobian is nonzero on the link. Thus
\[
 F_s=U_s(X-y^{k_i})^a(X+y^{k_i})^b.
\]
The polynomial on the right has weights $(k_i,1)$ in $(X,y)$ and degree $d_i=k_i(a+b)$. Multiplying $X$ by $U_s^{1/(a+b)}$ and $y$ by $U_s^{1/d_i}$, keeping $z$, removes the unit exactly. Its inverse is
\[
 (X',y',z)\longmapsto(\tau^{-k_i}X',\tau^{-1}y',z),\qquad
 \tau^{d_i}=U_s(\tau^{-k_i}X',\tau^{-1}y',z),
\]
with the selected nonzero root at the link. The implicit derivative is $d_i\tau^{d_i-1}\ne0$ there. These charts depend holomorphically on $s$ and on the source. Along the link their $z$ direction is tangent to the same smooth curve, which is transverse to the boundary; this transversality persists nearby. The weighted Euler identity shows that the fixed transverse polynomial has only the critical value zero. The smooth-branch charts give the same boundary property when $a>1$ or $b>1$. A finite collection covers the boundary critical set. Hence \cref{lem:II:boundary-deformation-transport}, with $g_s=F_s$ and $m=1$, carries every compact local spherical class constructed below into a fibre of the original $F$, preserving its square.

\item Suppose at least two factors occur. Apply the finite local-degree construction in the proof of \cref{cdp:st:A.5.17} to $(h_i,h_j)$. A small regular value $(s_i,s_j)$ has a nonempty finite inverse image, and the functions $h_i-s_i,h_j-s_j$ are transverse coordinates there. Choose the remaining constants to avoid their zero sets at one selected point. The deformation
\[
                H_s=\nu\prod_i(h_i-s_i)^{k_i}
\]
has there the form $\mu v^{k_i}w^{k_j}$, with $\mu$ a unit. Replacing $v$ by $\mu^{1/k_i}v$, keeping $w$, is invertible and gives $H_s=v^{k_i}w^{k_j}$ exactly. The full $F_s$ is therefore the function of \cref{prop:II:weighted-two-branch-sphere}, with the same $a,b$. Its compact sphere has nonzero square, and the preceding full-family transport gives a contradiction. There is only one factor. Absorb its plane unit and write $H=h^k$, with $h$ reduced and irreducible.

\item We show that $h$ is smooth, retaining the unit $U$ in the full function. Put $N=a+b$ and introduce an independent variable $q$ for a value of $H$. Write $L_X=\partial_X\log U$. The equation
\[
 NC+(a-b)+q(C^2-1)L_X(qC,Y,Z)=0,
 \qquad C(0,Y,Z)=c_0=\frac{b-a}{N},
\]
has a unique holomorphic solution $C=C(q,Y,Z)$ near the origin, since its derivative in $C$ at $q=0$ is $N$. Both $c_0-1=-2a/N$ and $c_0+1=2b/N$ are nonzero. For $q\ne0$, the point $X=qC$ is precisely the nearby solution of
\[
 \partial_X\log\bigl(U(X,Y,Z)(X-q)^a(X+q)^b\bigr)=0
\]
off the two zero factors. Define the holomorphic unit and coordinate
\[
 W(q,Y,Z)=U(qC,Y,Z)(C-1)^a(C+1)^b,\qquad
 \Lambda(q,Y,Z)=qW(q,Y,Z)^{1/N}.
\]
The derivative $\partial_q\Lambda$ at $q=0$ is the nonzero chosen root of $W(0,Y,Z)$. Thus $v=\Lambda(q,Y,Z)$ has a holomorphic inverse $q=R(v,Y,Z)$, characterized by
\[
 \Lambda(R(v,Y,Z),Y,Z)=v,\qquad
 R(\Lambda(q,Y,Z),Y,Z)=q.
\]
In particular $R(v,Y,Z)=vR_1(v,Y,Z)$ with $R_1$ a unit. The value of the full function at its $X$-critical centre is exactly $\Lambda(q,Y,Z)^N$.

\item Put
\[
       \widetilde h=h\,W(H,Y,Z)^{1/(kN)},\qquad
       \Lambda(H,Y,Z)=\widetilde h^{\,k}.
\]
Choose the roots compatibly in these two equalities. The germ $\widetilde h$ is reduced, and it is singular precisely when $h$ is singular. For a singular $h$, apply the finite-gradient construction in the proof of \cref{cdp:st:A.5.17} to $\widetilde h$: small linear terms and a constant give
\[
 \widetilde h_s=\widetilde h-\lambda_1Y-\lambda_2Z-\lambda_0
\]
with an interior Morse critical point $p$, nonzero value $v=\widetilde h_s(p)$, and invertible Hessian $Q$. Define
\[
                 H_s=R(\widetilde h_s^{\,k},Y,Z).
\]
At $s=0$ this is $H$, by the two inverse identities. Since $R(v,Y,Z)=vR_1(v,Y,Z)$, this is a deformation of one reduced plane factor with its original exponent $k$. Its boundary charts are exactly those of the first step. Both analytic factors $X-H_s$ and $X+H_s$ and their full multiplicities remain in $F_s$.

Let $A_s=H_sC(H_s,Y,Z)$. The defining equation for $C$ gives $(F_s)_X(A_s,Y,Z)=0$, and the critical value function is the exact identity
\[
                   F_s(A_s,Y,Z)=\widetilde h_s^{\,kN}.
\]
At $(A_s(p),p)$ the full gradient therefore vanishes and the value is $v^{kN}\ne0$. Moreover
\[
 (F_s)_{XX}(A_s,Y,Z)
 =H_s^{N-2}W(H_s,Y,Z)
 \left(H_s^2\partial_X^2\log U(A_s,Y,Z)
              -\frac{a}{(C-1)^2}-\frac{b}{(C+1)^2}\right).
\]
The bracket has value $-N^3/(4ab)\ne0$ at the origin; at the selected point $H_s\ne0$, so $(F_s)_{XX}\ne0$. Differentiating $(F_s)_X(A_s,Y,Z)=0$ identifies the Schur complement of this entry in the full Hessian with the Hessian of $F_s(A_s,Y,Z)$. At $p$ it is $kN v^{kN-1}Q$. Consequently
\[
 \det\operatorname{Hess}F_s
    =(F_s)_{XX}(kN)^2v^{2kN-2}\det Q\ne0.
\]
The explicit Morse-coordinate and sphere construction in the proof of \cref{cdp:st:A.5.17} gives a local sphere of square $-2$. All parameters, its critical value and its support can be chosen inside the transport neighbourhood of the first step. Its image in the original torus fibre has the same square, a contradiction. Thus $h$ is smooth.

\item Take $Y=h$ and a complementary plane coordinate $Z$, so that $H=Y^k$ exactly. This coordinate map has nonzero Jacobian, and its inverse is the unique local solution of these two equations. The weighted unit map of the first step, now with $d=k(a+b)$, changes the full function to $(X-Y^k)^a(X+Y^k)^b$, with its stated inverse. Any reduced local generator in these coordinates is $V(X^2-Y^{2k})$ for a unit $V$. The further map
\[
             (X,Y,Z)\longmapsto(V^{1/2}X,V^{1/(2k)}Y,Z)
\]
changes that generator to $X^2-Y^{2k}$. Its inverse is the same displayed implicit map with weights $(k,1)$ and degree $2k$. This proves both asserted normal forms.
\end{enumerate}
\end{proof}
'''

new_r15 = r15[:r15.index(r'\begin{proof}')]
new_r15 = new_r15.replace(
    r'\StatementRecord{night:P4R.15}{proved}{02Y8}{\SeriesRef{night:P4.18}, \SeriesRef{night:P4.28}}',
    r'\StatementRecord{night:P4R.15}{proved}{02Y8}{\cref{cdp:st:A.5.17,prop:II:smooth-branch-contact}}')
new_r15 += r'''\begin{proof}
A nonzero symmetric Hessian has a direction of nonzero quadratic value. Parametrized holomorphic Morse coordinates give the reduced generator $f=X^2+g(Y,Z)$, where $g\ne0$ because $f$ is reduced. The full local map is a unit times the product of its irreducible factors with their original positive multiplicities.

If $f$ is locally irreducible, the full map is $Uf^M$. The root $H=U^{1/M}f$ satisfies $F=H^M$ exactly, and at the critical point $\operatorname{Hess}H=U(0)^{1/M}\operatorname{Hess}f$. Apply the nonzero-Hessian conclusion of \cref{cdp:st:A.5.17}. It gives $H=X_1^2+Y_1^m$ with $m\ge2$, after multiplying the transverse coordinate by a constant whose $m$th power is $-1$. In these coordinates $f=V(X_1^2+Y_1^m)$ for a unit $V$. The weighted coordinate map
\[
       (X_1,Y_1,Z_1)\longmapsto
          (V^{1/2}X_1,V^{1/m}Y_1,Z_1)
\]
gives the exact stated generator. Its inverse is obtained by solving
\[
 \tau^{2m}=V(\tau^{-m}X',\tau^{-2}Y',Z'),
 \qquad (X_1,Y_1,Z_1)=(\tau^{-m}X',\tau^{-2}Y',Z'),
\]
with the selected nonzero root; the implicit derivative is $2m\tau^{2m-1}\ne0$ at the origin.

If $f$ is reducible, Weierstrass factorization of its monic quadratic in $X$ gives two monic linear factors. Their $X$ coefficients sum to zero, so $g=-H(Y,Z)^2$ and the factors are exactly $X-H$ and $X+H$. Both are smooth. The full map is therefore $U(X-H)^a(X+H)^b$ for its original $a,b$. Apply \cref{prop:II:smooth-branch-contact}. Its full-function transport retains these multiplicities and proves that $H=h^k$ with $h$ smooth after absorbing its plane unit. Thus the original reduced generator is exactly $X^2-Y^{2k}$; multiplying $Y$ by a chosen constant whose $2k$th power is $-1$ gives $X^2+Y^{2k}$.

Both cases give $m\ge2$ and reduced critical curve $X=Y=0$. The factor and gradient deformations used in the two earlier owners permit the different initial exponents on the different branches, so no equality of their generic transverse types has been imposed. The explicit Hessian and moving-node calculation for their uniform-power suspension is recorded in the proof of \cref{cdp:st:A.5.17}.
\end{proof}'''

anchor = source[source.index(r'\begin{proposition}[Local rigidity of a transverse cusp]'):].splitlines()[0]
p.guard('P298 before cusp', anchor, owner + '\n' + anchor,
        'Put the complete full-function two-smooth-branch owner after P295, before every later Hessian and tacnode consumer.')
p.record('D10,D14,D16,D25', 'prop:II:smooth-branch-contact',
         'R15 used a reduced-function deformation under a broad standing domain which permits unequal full component multiplicities.', owner,
         'Prove the exact full family U(X−H_s)^a(X+H_s)^b. Its product boundary charts include the smooth component strata, its unit is retained in the critical-centre calculation, and Lambda/R provide explicit inverse maps for the factor-preserving Morse deformation. The Schur complement gives a nonzero full Hessian and P295 transports with m=1. The original component multiplicities and broad R15 domain are retained.')
p.guard('R15 exact full-function applications', r15, new_r15,
        'Replace the incomplete reduced/full comparison by the complete irreducible A.5.17 and reducible P298 applications, preserving the original statement.')
p.record('D04,D12,D14,D16,D25', 'night:P4R.15', r15, new_r15,
         'Read the full old proof. Its locally irreducible case uses the exact root H=U^(1/M)f and the existing A.5.17 construction, retaining M separately from the transverse exponent m. Its reducible monic quadratic has the exact factors X±H and uses P298 with the original positive a,b. The weighted inverse removes the final generator unit. All original conclusions remain; the explicit suspension Hessian and moving-node formulas move to their common gradient-construction owner A.5.17.')

old_hessian = r'''The Hessian of $h_s^b$ is
$b v^{b-1}$ times the Hessian of $h_s$, and
is invertible. The holomorphic Morse lemma on
the two plane variables identifies the germ of
$H_s-H_s(p)$ with'''
new_hessian = r'''The Hessian of $h_s^b$ is
$b v^{b-1}$ times the Hessian of $h_s$, and
is invertible. For $a=2$, the coordinate $x=\mathrm iX$
and target negation give the sign convention $X^2+h_s^b$.
Writing $Q=\operatorname{Hess}h_s(p)$, its critical value,
Hessian and determinant are exactly
\[
 v^b,\qquad
 \begin{pmatrix}2&0\\0&b v^{b-1}Q\end{pmatrix},\qquad
              2b^2v^{2b-2}\det Q\ne0.
\]
This identity holds for every positive integer $b$. In particular
for $X^2+(YZ-\varepsilon)^b$, the origin has critical value
$(-\varepsilon)^b$ and plane Hessian
$\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$,
so the full Hessian determinant is $-2b^2\varepsilon^{2b-2}\ne0$.
The holomorphic Morse lemma on
the two plane variables identifies the germ of
$H_s-H_s(p)$ with'''
assert old_hessian in a517
p.guard('A517 exact Hessian and moving-node formulas', old_hessian, new_hessian,
        'Retain R15 full Hessian and moving-node calculation at its existing common gradient-construction owner, with the exact sign coordinate map.')
p.record('D12,D16', 'cdp:st:A.5.17', old_hessian, new_hessian,
         'This is the same plane Morse construction as old R15 steps4–5. The explicit morphism x=iX and target negation identifies its sign convention. Both old formulas for every positive exponent remain, and no A.5.17 hypothesis or conclusion changes.')

for row in p.rows:
    row['old_location'] = row['statement_id'] + ' / complete current statement and proof'
p.write(owner + '\n' + new_r15 + '\n')
