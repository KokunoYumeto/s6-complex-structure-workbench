from pathlib import Path
import re,json,datetime
from S6_SERIES_PUBLISH_editing import Editor,block
r=Path(__file__).resolve().parents[1]
ed=Editor('I')
old=block(ed.text,'inv:A2.3')
new=r'''\begin{proposition}[The elliptic logarithm at the finite points]
\hypertarget{tag-01RW}{}\label{inv:A2.3}
\StatementRecord{inv:A2.3}{proved}{01RW}{\SeriesRef{fam:src:B.1.1}, \SeriesRef{fam:src:B.1.3}; \citet{DukeImamoglu2008}}
Let $[\mu]$ be the generator identified in
Propositions~\ref{fam:src:B.1.1} and \ref{fam:src:B.1.3} with
one of the two sections
$P_*=(0,\sqrt2t^2(t-1))$ and $-P_*$ of
$y^2=x^3-3t^3(t-1)x+2t^4(t-1)^2$.
Along the branch in \eqref{inv:eq:A-s-branch}, put $x_0=1-1/t$.
Then
\begin{equation}\hypertarget{tag-01SY}{}\label{inv:eq:A-DI-branch}
\mu=\frac{1-\tau}{2}
 +\frac{i\sqrt6}{3\pi}
 \frac{x_0^{1/4}\,{}_3F_2(1/3,2/3,1;3/4,5/4;x_0)}
 {{}_2F_1(1/12,5/12;1;1-x_0)}.
\end{equation}
The difference $\mu-(2-\tau)/3$ has exact order two at the
order-three point in the coordinate $r^3=t$.
\end{proposition}
\begin{proof}
The pointed Weierstrass isomorphism in
Proposition~\ref{fam:src:B.1.1} and the section calculation in
Proposition~\ref{fam:src:B.1.3} give $\wp(\mu,\tau)=0$.
In \cite[Theorem~1, equation~(5), author preprint p.~2]{DukeImamoglu2008},
write $z_0$ for the displayed zero. The exact affine map
$\mu=1-z_0$ preserves the zero identity, since
$\wp(1-z_0,\tau)=\wp(z_0,\tau)$, and gives
\eqref{inv:eq:A-DI-branch}. At $t=1+s^4$ its initial value is
$(1-i)/2$. The coefficient of $s$ is
\[
 \frac{i\sqrt6}{3\pi\,{}_2F_1(1/12,5/12;1;1)}
 =\frac{i\sqrt6}{3\pi E_4(i)^{1/4}}.
\]
It has positive imaginary part and therefore selects the branch of
\eqref{inv:eq:A-s-branch}. Continuation gives the chosen bounded
lift at the cusp.

The chord-and-tangent formulas applied to $P_*$ give
\[
 x(2P_*)=\frac{9t^2}{8},\qquad
 y(2P_*)=\frac{t^2(32-5t)}{16\sqrt2},\qquad
 x(3P_*)=\frac{16}{81}(t-1)(5t-32).
\]
The last expression tends to $512/81$ at $t=0$.
Let $F=f_{\rm sc}$ be the elliptic scale of
Proposition~\ref{fam:src:B.1.1}; it has exact order two in $r$.
For $\nu=\mu-(2-\tau)/3$, the point $3P$ has local logarithm
$3\nu$ modulo its period, and
$x(3P)=F^2\wp(3\nu,\tau)$.
The expansion $\wp(3\nu,\tau)=(3\nu)^{-2}+O(\nu^2)$
therefore proves that $\nu$ has exact order two. Its leading
coefficient is $\pm3F_2/(16\sqrt2)$, where
$F_2=\lim_{r\to0}F/r^2$; the sign is fixed by the same logarithm branch.
\end{proof}'''
ed.replace(old,'','D12','The first five proof steps repeat the complete section-generation and height arguments in fam:src:B.1.1 and fam:src:B.1.3. Replace them by exact references and retain the unique primary hypergeometric branch and order-two conclusion, already checked independently. Relocate this proposition before its uses.','inv:A2.3')
mark=ed.text.index('\\begin{proposition}[The complete raw period determinant]')
ed.text=ed.text[:mark]+new+'\n\n'+ed.text[mark:]
ed.record('D14','',new,'Place the elliptic logarithm immediately after its coordinate definition and before the modular derivative calculation.','inv:A2.3')

a=ed.text.index('\\subsection{An exact modular determinant and two numerical routes}')
b=ed.text.index('\\begin{proposition}[The elliptic logarithm at the finite points]',a)
old=ed.text[a:b]
new=r'''\subsection{The elliptic logarithm and the period determinant}

\begin{definition}[The finite local coordinates]
\hypertarget{tag-PI07}{}\label{I:def:finite-coordinates}
\StatementRecord{I:def:finite-coordinates}{proved}{PI07}{}
At the order-four point choose $t-1=s^4$ so that on the positive
$t>1$ arc toward the cusp, $\tau=iy$ with $y>1$, and
\begin{equation}\hypertarget{tag-01T5}{}\label{inv:eq:A-s-branch}
\tau=i+\frac{i}{\pi\sqrt{E_4(i)}}s^2+O(s^4),\qquad
\operatorname{Im}\mu_s(0)>0.
\end{equation}
Replacing $s$ by $i^js$ changes $\mu_s(0)$ by $i^{-j}$.
For any other local coordinate $z$ the derivative is transported
by $\mu_z=\mu_s s_z$. At the order-three point use $r^3=t$,
with $r>0$ on the arc $0<t<1$ along which $\tau$ travels from
$\rho$ to $i$ on the unit circle.
\end{definition}

'''
ed.replace(old,new,'D13','Make the branch choice a numbered definition with the exact chain-rule transport; remove the reference to an earlier edition and retain its entire coordinate dependence.','I:def:finite-coordinates')

# Keep one proof of the scalar, with the alternate geometric derivation in
# the check record preserved by this exact old/new edit log.
old=block(ed.text,'inv:A2.2')
new=old
p=r'\item There is also a geometric nonvanishing proof independent of this'
a=new.index(p);b=new.index(r'\item The real period also has the integral expression',a)
new=new[:a]+new[b:]
new=new.replace(r'\begin{proposition}[The evaluated scalar and the two local leading terms]',r'\begin{proposition}[The finite period coefficients]')
a=new.index('Numerically,\n');b=new.index('For $r^3=t$',a)
new=new[:a]+new[b:]
a=new.index('The leading coefficient has real and imaginary parts');b=new.index('\\end{proposition}',a)
new=new[:a]+r'''The exact expressions have the rational enclosures
\[
\begin{aligned}
0.2366093140807852&<C_4<0.2366093140807853,\\
0.0801022110875382&<\operatorname{Re}K_2<0.0801022110875383,\\
0.1387410994022233&<\operatorname{Im}K_2<0.1387410994022234.
\end{aligned}
\]
'''+new[b:]
a=new.index('For the displayed numerical values,');b=new.index('The elementary inequalities',a)
new=new[:a]+'''For the rational enclosures, evaluate the divisor-sum series of
$E_4(i)$ and $E_6(\\rho)$ by interval arithmetic with $N=100$ terms.
'''+new[b:]
a=new.index('All arithmetic roundoff is included');b=new.index('\\end{enumerate}',a)
new=new[:a]+'''Outward rounding in the finite sums, together with these tail bounds,
gives the three stated enclosures. The preceding modular calculation
proves the exact nonvanishing and the local orders.
'''+new[b:]
ed.replace(old,new,'D12','Keep the modular proof of the coefficient and move its second geometric proof to the exact comparison records. Replace long floating-point expansions by the same certified rational enclosures formerly in the proof. Preserve the elliptic integral, gamma evaluation, inputs, truncation and tail bounds; move program bookkeeping to the program table.','inv:A2.2')

ed.save()
(r/'records/S6_SERIES_PUBLISH_I_modular_consolidation_comparison.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'inv:A2.3':'Full old/new proof read. Repeated section-generation and primitive-height arguments point to the exact earlier proofs. The hypergeometric formula, coordinate branch, three addition formulas and exact order with leading coefficient are preserved. Primary preprint page is explicitly distinguished from journal pagination.',
 'inv:A2.2':'Full old/new proof read. Modular derivative proof, local series, elliptic-integral/gamma evaluation and certified intervals preserved. Alternate geometric nonvanishing proof and the longer decimal display are retained in the edit/check record, with no change to the exact value or enclosure.',
 'I:def:finite-coordinates':'Exact branch equation/label/tag preserved; derivative changes are the same chain-rule maps. No numerical identification of different local coordinates.',
 'new_computation':None},indent=2)+'\n')
