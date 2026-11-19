"""Replace the unresolved-premise formulation by exact ratios and scalar models.

The unchanged S6_09 proof remains the source compendium. The receiving proof
retains its division/height/function-field calculations with explicit maps.
"""
from pathlib import Path
import json
P=Path(__file__).resolve().parents[2]
J=json.loads((P/'analysis/inventory_source_index.json').read_text())
S=(P.parents[1]/'sources/s6_09/S6_09_PAPERS_I.tex').read_text()
d=J['S6_05_ARITHMETIC:C.7.12'];old=S[d['start']:d['end']]
statement=r'''
\begin{proposition}[division ratios, scalar models and translated functions]\label{ari:C.7.12}
Let $E:y^2+y=x^3-38x+90$, $Q=(4,-2)$ and $N_0=N(Q)$.
Use the positive real logarithm $u$ and period $\omega_1$ of
\ref{ari:C.7.9}. Put
\[
 \delta=19^{1/4},\qquad b=\eta_1/\omega_1,\qquad
 g(z)=\delta\sigma(z)e^{-bz^2/2}.
\]
Thus $|g(z)|=N(\exp_Ez)$ on the real axis. Let $\mathcal D$
be the CM division hull of $Q$. For $R\in\mathcal D$, the
equations $[n]R=[\alpha]Q$, $n>0$, determine a unique
$\kappa_R=\alpha/n\in\operatorname{End}(E)\otimes\Q$.
Set $w_R=\kappa_R\bar\kappa_R$. For $R\ne O$,
\[
 A_R:=\frac{N(R)}{N_0^{w_R}}\in\overline\Q_{>0}.
\]
In particular, for $[n]R=[m]Q$ with $m\ne0$,
\begin{equation}\label{ari:eq:division-ratio-model}
 A_R^{n^2}=\delta^{n^2-m^2}
                  \frac{|\psi_m(Q)|}{|\psi_n(R)|}.
\end{equation}
For each positive algebraic number $\lambda$, define
\[
 N_\lambda(R)=A_R\lambda^{w_R}
       =N(R)\left(\frac{\lambda}{N_0}\right)^{w_R}.
\]
All these values are algebraic. For $[n]R=[m]Q$, $|m|\le n$,
$R\ne O$, there are constants $D,H$ depending on $\lambda,E,Q$
such that
\[
 h(N_\lambda(R))\le H,\qquad
 [\Q(R,N_\lambda(R)):\Q]\le
 \begin{cases}Dn^4,&R\in E(\R),\\2Dn^6,&R\in E(\C).
 \end{cases}
\]
The transformation is exact for every positive real parameter:
$N_\lambda(R)/N_\mu(R)=(\lambda/\mu)^{w_R}$ and
$N_{N_0}(R)=N(R)$.

For any finite collection of real division-hull logarithms $a$,
the functions $g(z)$ and $g(z+a)/g(a)$, with $\exp_Ea\ne O$,
have function-field transcendence degree at most three over
$\overline\Q$ after adjoining the elliptic coordinates.
The three functions $g(z),g(z+v)/g(v),g(z-v)/g(v)$, $v=u/q$,
attain three. The normalized holomorphic extensions
$F_a(z)/N(a)^2$ of $N(\exp_E(z+a))^2$ for fixed complex
division-hull shifts belong to the same type of field.
The unnormalized translates have the same upper bound, attained by
the displayed triple, over the algebraic closure $L$ of $\overline\Q(N_0)$ in $\C$.

For the scalar models on the real division grids
$z=(mu+k\omega_1)/n$, $|m|\le Cn$, $k$ modulo $n$, with
fixed $C$, every fixed finite family of these values has a common
degree envelope $O(n^5)$ and bounded heights. For the actual values the same construction
gives a relative degree envelope over a fixed finite extension
of $\Q(N_0)$. The algebraicity of $N_0$ remains the open question
of \ref{ari:C.7.4}. The explicit interpolation and tangent
calculations below record what these bounds establish.
\end{proposition}
\Uses{\cref{ari:C.4.2}; \cref{ari:C.7.1}; \cref{ari:C.7.6};
\cref{ari:C.7.9}; \cref{ari:C.7.11}; the exact divisor and
height computations below; the cited criteria at their stated scopes}
\begin{proof}
\emph{The algebraic ratios and their exact change of parameter.}
Two equations $[n]R=[\alpha]Q$ and $[n']R=[\alpha']Q$
give $[n'\alpha-n\alpha']Q=O$. A nonzero elliptic endomorphism
has finite kernel, whereas $Q$ is nontorsion. Thus
$\alpha/n=\alpha'/n'$, proving uniqueness. The resulting
map $R\mapsto\kappa_R$ is additive, and its kernel is the
torsion subgroup. Every such $R$ is algebraic, since it lies
in a finite isogeny fibre above an algebraic point.

The division identity and the squared CM law give, for
$d=\alpha\bar\alpha$ and $\alpha\ne0$,
\[
 N(R)^{n^2}=\frac{N(nR)\delta^{n^2-1}}{|\psi_n(R)|},
 \qquad
 N(\alpha Q)^2=\delta^{2-2d}|F_\alpha(Q)|N_0^{2d}.
\]
Consequently
\[
 A_R^{2n^2}=\frac{\delta^{2n^2-2d}|F_\alpha(Q)|}
                         {|\psi_n(R)|^2}\in\overline\Q_{>0}.
\]
The positive root proves $A_R\in\overline\Q$. For integral
$\alpha=m$, the usual multiplication identity is
$N(mQ)=N_0^{m^2}|\psi_m(Q)|/\delta^{m^2-1}$;
substitution proves \eqref{ari:eq:division-ratio-model}.
For nonzero $n$-torsion $R$, take the limit at the simple zero
of $\psi_n$ in the uniformizing coordinate. Since
$N(z)=\delta|z|+o(|z|)$ at zero,
\[
 A_R^{n^2}=N(R)^{n^2}
       =\frac{n\delta^{n^2}}{|\partial_z\psi_n(R)|}.
\]
The invariant derivation is algebraic, so this also is algebraic.
All exponents $w_R$ are rational. The asserted scalar models,
their parameter-change identity and the specialization at $N_0$
follow directly. In particular their definition is independent
of every presentation of $R$ by a division equation.

Put $K_\lambda=\Q(\delta,\lambda)$ and
$D=[K_\lambda:\Q]$. For integral $m\ne0$,
\[
 N_\lambda(mQ)=\lambda^{m^2}
                     |\psi_m(Q)|/\delta^{m^2-1}\in K_\lambda,
\]
because $Q$ is rational. The fibre of $[n]$ has $n^2$ points,
so adjoining $R$ costs at most $n^2$. For real $R$ the absolute
value of $\psi_n(R)$ differs from it by a sign. The division
equation for $N_\lambda(R)$ costs at most another $n^2$.
For complex $R$, adjoin $R$ and $\bar R$, at cost at most
$n^4$, and use
\[
 N_\lambda(R)^{2n^2}
 =\frac{N_\lambda(mQ)^2\delta^{2(n^2-1)}}
              {\psi_n(R)\psi_n(\bar R)}.
\]
This gives $2Dn^6$. At nonzero torsion points the derivative
formula proves the same bounds.

'''
heights=old[old.index(r'\emph{Uniform heights.}'):old.index(r'\emph{The translate count')]
heights=heights.replace(r'\citep[Lemma 1.0]{gramain1986values} now gives',
 r'now gives')
heights=heights.replace(r'h(N(mQ))\leq m^2h(N(Q))',r'h(N_\lambda(mQ))\leq m^2h(\lambda)')
heights=heights.replace('Divide the height of the division identity by $n^2$.',
 r'Apply the same division identity to $N_\lambda$ and divide its height by $n^2$.')
heights=heights.replace(r'$h(N(R))$',r'$h(N_\lambda(R))$')
heights=heights.replace('The polynomial evaluation height inequality\nnow gives',
 'At each nonarchimedean place the ultrametric inequality bounds a\npolynomial value by its largest monomial; at each archimedean\nplace use the sum of the monomials. Summing these logarithmic\nbounds by the product formula gives the polynomial evaluation\nheight inequality, and hence')
translates=r'''
\emph{Normalized translates and their algebraic scalars.}
For a real logarithm $a$ of a nonzero division point put
\[
 h_a(z)=\frac{\sigma(z+a)}{\sigma(z)\sigma(a)}e^{-baz}.
\]
The exact identities are
\[
 g(z+a)=\delta^{-1}g(z)g(a)h_a(z),\qquad
 h_a(z+\omega_1)=h_a(z),\quad
 h_a(z+\omega_2)=e^{-2\pi ia/\omega_1}h_a(z).
\]
They follow by substitution from sigma automorphy and Legendre's
relation. A real point in the CM division hull lies in the
ordinary division hull: conjugating $[n]R=[\alpha]Q$ gives
$[\alpha-\bar\alpha]Q=O$, hence $\alpha=\bar\alpha\in\Z$.
The real group is connected because the discriminant is negative.
Its division logarithms are therefore exactly
$\widetilde{\mathcal D}=\Q u+\Q\omega_1$.
The coefficient map
\[
 \nu:\widetilde{\mathcal D}\longrightarrow\Q,
 \qquad \nu(ru+s\omega_1)=r
\]
is well defined and additive: a rational relation between $u$
and $\omega_1$ would make $Q$ torsion.

For any positive real $\lambda$ define, on this additive group,
\[
 \widetilde g_\lambda(z)
   =g(z)(\lambda/N_0)^{\nu(z)^2},\qquad
 h_{a,\lambda}(z)
   =h_a(z)(\lambda/N_0)^{2\nu(z)\nu(a)}.
\]
At nonzero division values, the absolute value of
$\widetilde g_\lambda$ is $N_\lambda$ and its sign is the real
sign of $g$. Thus these values are algebraic for algebraic
$\lambda$. The identity
\[
 h_{a,\lambda}(z)=
 \frac{\delta\widetilde g_\lambda(z+a)}
      {\widetilde g_\lambda(z)\widetilde g_\lambda(a)}
\]
is proved by expanding $(\nu(z)+\nu(a))^2$.
It specifies the exact transformation on the sampling group.

Choose a common denominator $q$ for finitely many shifts,
write $a_j=(m_ju+k_j\omega_1)/q$, and put $v=u/q$.
The quotient $h_{a_j}/h_v^{m_j}$ is elliptic for
$\Lambda_q=\Z\omega_1+\Z q\omega_2$. This finite isogeny
of $E$ has a model over $\overline\Q$ with the stated
differential. The quotient has an algebraic divisor, hence
is a rational function over $\overline\Q$ times a scalar.
The scalar is algebraic. Indeed the parameter factors cancel:
\[
 \frac{h_{a_j}(z)}{h_v(z)^{m_j}}
  =\frac{h_{a_j,1}(z)}{h_{v,1}(z)^{m_j}}
       \qquad(z\in\widetilde{\mathcal D}).
\]
Choose a real division point avoiding the finite zeros and poles.
The right side and the value of the chosen rational function
are algebraic and nonzero, so their quotient is algebraic.
This proves that $g(z)$ and all normalized real translates are
algebraic over $\overline\Q(E)(g,h_v)$, after the fixed finite
isogeny. The upper transcendence-degree bound is three.

For the lower bound, work even over $\C$. The multiplier of
$h_v$ under $q\omega_2$ is $e^{-2\pi iu/\omega_1}$,
which has infinite order. A polynomial relation over the elliptic
field, evaluated at a generic $z$ and translated by $mq\omega_2$,
would have infinitely many distinct roots obtained by these
powers. Thus $h_v$ is transcendental over that field. Moreover
\[
 |g(z+mq\omega_2)|=\exp(c m^2+O(|m|)),
 \qquad c=\pi q^2\Im(\omega_2/\omega_1)>0.
\]
In a proposed polynomial relation for $g$ over the elliptic field
and $h_v$, clear denominators. The nonzero leading coefficient
is a polynomial evaluated along an irrational rotation; it is
bounded away from zero on a subsequence, and all other
coefficients remain bounded there. Quadratic growth makes the
highest power of $g$ dominate, a contradiction. Finally
\[
 \wp(z)=\wp(v)-
 \frac{\delta^2g(z+v)g(z-v)}{g(z)^2g(v)^2}
\]
recovers the elliptic coordinate from the three stated translates,
and $h_v=\delta g(z+v)/(g(z)g(v))$. They therefore attain three.
The constants $g(a)$ lie in $L$, by the already proved ratios.
Multiplication by these constants gives the exact map from
normalized to raw translates, proving the assertion over $L$.

For a complex CM division shift $a$, the holomorphic extension
from the real axis is
\[
 F_a(z)=\frac{N(a)^2}{\delta^2}g(z)^2h_a(z)h_{\bar a}(z).
\]
Its multiplier depends on $a+\bar a\in\Q u+\Q\omega_1$.
Choose $q,m$ with $a+\bar a=(mu+k\omega_1)/q$.
Then $h_ah_{\bar a}/h_v^m$ is elliptic on $\C/\Lambda_q$
with algebraic divisor. Its scalar is algebraic by the same
evaluation argument, using the exact identity on real division
points
\[
 h_a(z)h_{\bar a}(z)(\lambda/N_0)^{2\nu(z)m/q}
 =\frac{\delta^2N_\lambda(\exp_E(z+a))^2}
        {N_\lambda(\exp_Ea)^2\widetilde g_\lambda(z)^2}.
\]
Here $w_{\exp_E(z+a)}=|\kappa_{\exp_Ea}+\nu(z)|^2$;
expanding the square proves the identity. Set $\lambda=1$
and divide by $h_{v,1}^m$. This proves the normalized complex
translate assertion with all scalar factors accounted for.

\emph{Joint degrees and heights on the sampling group.}
In the algebraic meromorphic section coordinate of
\ref{ari:C.7.1},
\[
 z\longmapsto(\exp_Ez,h_v(z))
   =\exp_{G_V}\bigl(z,(\zeta(v)-bv)z\bigr),\qquad
 V=\exp_Ev.
\]
For the scalar model, multiply its torus coordinate by
$(\lambda/N_0)^{2\nu(z)\nu(v)}$. This factor is a character
of the additive sampling group, so the resulting map
$\Phi_\lambda:\widetilde{\mathcal D}\to G_V(\C)$ is an
abstract group homomorphism. Its real period is $\omega_1$,
because $\nu(\omega_1)=0$ and the displayed analytic map
has that period. For algebraic $\lambda$, its values in the displayed section
chart are algebraic by the formula for $h_{v,\lambda}$ above.
For an exceptional sampling point at a zero or pole of that
section, write $z=z_1+z_2$ with both $z_j$ avoiding the finite
exceptional set modulo the elliptic lattice. Such a choice exists
in the infinite division group. Then
$\Phi_\lambda(z)=\Phi_\lambda(z_1)\Phi_\lambda(z_2)$ is
algebraic by the algebraic group law. This also covers the identity.

For $z=(mu+k\omega_1)/n$,
$[n]\Phi_\lambda(z)=[m]\Phi_\lambda(u)$.
Choose a fixed number field containing the coefficients of
$G_V$, the point $\Phi_\lambda(u)$ and the finitely many
fixed constants. Multiplication by $n$ on $G_V$ has degree
$n^3$, since its kernel is an extension of $E[n]$ by
$\mathbb G_m[n]$. Adjoining $\widetilde g_\lambda(z)$ costs
at most $n^2$ by the norm division equation. Passing to the
fixed isogeny and adjoining fixed constants changes only the
constant in $O(n^5)$. The same argument for any positive real
$\lambda$ works over a fixed finite extension of $\Q(\lambda)$,
because all the fixed division values are algebraic over that
field. At $\lambda=N_0$ it gives the claimed relative envelope.

The height proof above applies with $|m|\le Cn$ for any fixed
$C$, changing only its constant. It bounds the model values at
$z$ and every fixed real translate $z+a$. Their quotients bound
$h_{v,\lambda}(z)$. Coordinates on the fixed isogenous elliptic
curve have bounded height by the fixed isogeny height comparison.
The normalized complex translates are fixed rational functions
of those coordinates, $\widetilde g_\lambda^2$ and a fixed power
of $h_{v,\lambda}$, with algebraic coefficients just proved.
The polynomial evaluation inequality bounds their heights.
Any removable zero or pole in these expressions lies in a fixed
finite set and is handled by its actual model value. Taking the
positive square root for a fixed complex-shifted norm divides
height by two and costs at most a factor two in degree.

'''
audit=r'''
\emph{The exact numerical and tangent checks.}
The sufficient inequality in Gramain--Mignotte--Waldschmidt
\citep[Theorem2.1,pp.101--102]{gramain1986values} has the form
\[
 d(N)\prod_{j=1}^k\max\{d(N)\psi_j(N),\theta_j(R(N))\}
 \le c_0\mu(N)^{k-1}\varphi(N)^k,
\]
\[
 \varphi(N)=\log\frac{R(N)^2+r(N)r(N+1)}
                         {R(N)(r(N)+r(N+1))}.
\]
On fixed nested discs the growth and geometric factors are
constant. The scalar-model height envelopes are constant too.
The numerical comparison of these envelopes is therefore
$d^{k+1}\ll\mu^{k-1}$. At denominator $n$ the real group
has $O(n^2)$ sample points, and through denominator $N$ it
has $O(N^3)$. Substitution of the proved envelopes gives
$N^{12}$ against $N^3$ for two functions and $N^{20}$ against
$N^6$ for three. These upper-envelope calculations provide
no such inequality and assert no lower bound for the actual
degrees. For actual analytic samples the base field is the
displayed extension of $\Q(N_0)$; its number-field status is
exactly the unresolved algebraicity issue. Extra normalized
translates remain in the function field of transcendence degree
three proved above.

The arithmetic-germ criteria
\citep[Theorem6.1]{herblot2012meromorphic}
\citep[Theorem4.16]{gasbarri2010analytic}
can be compared with the actual logarithmic tangent. At a real
nontorsion division point $z$, the exact formula is
\[
 \frac1{g(z)}\frac{dg}{dx}
       =\frac{\zeta(z)-bz}{\wp'(z)}.
\]
Its numerator is transcendental by the period-line proof of
\ref{ari:C.7.9}, applied to this algebraic nontorsion point;
its denominator is nonzero algebraic. A formal graph defined
over $\overline\Q$ would have an algebraic nonzero constant
value and algebraic first derivative, contradicting their
displayed ratio. The scalar change on the sampling group has
not changed this exact tangent of the analytic graph.

For the Mahler system in
\citep[Theorem1.1 and system(1.2)]{adamczewski2017mahler},
the needed algebraic Taylor coefficients and algebraic regular
argument can be tested directly: the coefficient of $z^3$ in
$g$ is $-\delta b/2$, and $b=s_2+k$ is transcendental by
\ref{ari:C.7.11}. The logarithm $u$ is transcendental too:
an algebraic $u\ne0$ would give an algebraic point $(u,Q)$
on the diagonal Lie line of $\mathbb G_a\times E$; the analytic
subgroup theorem would produce an algebraic one-dimensional
subgroup projecting nontrivially to both factors, which is
impossible since an elliptic curve has no nonconstant map to
$\mathbb G_a$ and $\mathbb G_a$ has no nonzero group map to $E$.
The duplication identity acts by the explicit elliptic
multiplication map. The entropy identity in
\citep[Theorem5.1]{einsiedler2001entropy} uses the sequence
built from the denominators of $x(2^nQ)$ with scale $4^n$.
These precise inputs supply no evaluation of $N_0$ here.

Finally the period-refined rank comparison
\citep[Theorem4.1 and Corollary4.3]{waldschmidt1988periodrank}
\citep[main theorem,p.363]{roy1993periodrank}
has coefficient $\alpha(G)=2\dim G-2d_0(G)-d_1(G)$,
where the last terms count additive and multiplicative
quotients. Both vanish for $G_Q$. An additive homomorphism
vanishes on its torus and then on the proper quotient $E$;
a nonzero torus character extending to $G_Q$ would kill a
nonzero integer multiple of its nontorsion extension class.
Thus $\alpha(G_Q)=4$.

The line $\ell_c$ has period rank one. A general period is
$(\omega,\zeta(u)\omega-\eta(\omega)u+2\pi i j)$.
Writing $\omega=a\omega_1+d\omega_2$, membership in
$\ell_c$ gives $du/\omega_1\in\Z$ by Legendre's relation.
Since $u/\omega_1$ is irrational, $d=j=0$. The numerical
rank bound in the cited theorem is
$(4-1)\dim\ell_c=3$. The period and the actual logarithm
$(u,cu)$ are independent over $\Q$ and span rank two;
the algebraicity of the latter's exponential remains exactly
the point-algebraicity question in \ref{ari:C.7.9}. These
explicit ranks leave that question open.
\end{proof}
'''
(P/'papers/I/revisions/ari_C.7.12.tex').write_text(statement+heights+translates+audit)
print('Wrote complete algebraic-ratio/scalar-model and translated-function proof.')
