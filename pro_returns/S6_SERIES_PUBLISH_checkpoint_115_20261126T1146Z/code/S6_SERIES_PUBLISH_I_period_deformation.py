from pathlib import Path
import re,json,datetime,hashlib
from S6_SERIES_PUBLISH_editing import Editor,block
r=Path(__file__).resolve().parents[1];ed=Editor('I')
a3=block(ed.text,'fam:src:A.3.1');a4=block(ed.text,'fam:src:A.4.2')
wb=block(ed.text,'wb:thm:retained-period-deformation')
a=ed.text.index(r'\subsection{The retained period constant is an effective deformation parameter}')
b=ed.text.index(r'\subsection{Integral classification of the parameter}',a)
whole=ed.text[a:b]
oldproper=a3[a3.index(r'\item \emph{Properness'):a3.rindex(r'\end{enumerate}')]

proper=r'''\item \emph{The holomorphic family.}
Let $Q$ be a disc with $\overline Q\subset\mathcal P$.
On an ordinary lifted base chart use the period matrix
\eqref{wb:pshift:eq:periods}, jointly holomorphic in $(z,c)$.
Its real determinant is $\Im\tau\,D_c$, and its inverse is
uniformly bounded on compact base-parameter sets. Thus the lattice
action is free and properly discontinuous there. A fixed closed
real lattice parallelotope gives compact surjective representatives
over each compact subset of the base chart times $Q$.
The quotient is holomorphic and its projection to $Q$ is a submersion.
The covariance convention of \cref{I:def:affine-covariance} is
\[
 R_g(z)\Pi(z,c)=\Pi(gz,c)A_g,
 \qquad M_g=A_g^{-1},\qquad
 \Pi(gz,c)=R_g(z)\Pi(z,c)M_g.
\]
Consequently the base deck quotient is jointly holomorphic; its
proper discontinuity follows from that of the lifted base action.

At a finite root chart the family action is
\[
 (z,c,\zeta)\longmapsto
 \left(g_jz,c,R_{g_j}(z)\zeta+
             \Pi(g_jz,c)\frac{v_j}{m_j}\right),
 \qquad (m_1,m_2)=(3,4).
 \tag{PD7}
\]
In the real marking it is $(z,c,u)\mapsto(g_jz,c,A_ju+v_j/m_j)$.
The invariant-covector freeness test in \cref{fam:src:A.1.2}
is independent of $c$, so these quotients are local biholomorphisms
and submersions to $Q$. The same parallelotope proves properness
over the finite base disc times $Q$. Their punctured connectors are
\[
 \frac{\log s_j(z)}{2\pi i}\Pi(z,c)v_j.
 \tag{PD8}
\]
A logarithm change adds a period, so this is a jointly holomorphic
torus section. Substitution in the finite affine action gives the
overlap conjugacy used in the preceding local maps.

\item \emph{Uniform cusp charts and properness.}
On the fixed unimodular fan write the full cusp period matrix as
\[
 C(t_c,c)=\begin{pmatrix}6\mu(t_c)&h(t_c)\\
 b^{\rm part}(t_c)-h(t_c)+c&\mu(t_c)\end{pmatrix},
 \qquad B_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
 \tag{PD9}
\]
Choose a closed cusp disc $|t_c|\le r_1$ on which these functions
are holomorphic, and set
\[
 K_Q=\max_{|t_c|\le r_1,\ c\in\overline Q}
               \|-2\pi\Im C(t_c,c)\|,
 \qquad 0<\epsilon<\min(r_1,1),\quad
               |\log\epsilon|>2K_Q.
 \tag{PD10}
\]
The lattice acts on the toric family times $Q$ by
\[
 (x,t_c,c)\longmapsto
 \bigl(e^{2\pi iC(t_c,c)\lambda}t_c^{B_0\lambda}x,t_c,c\bigr),
 \qquad\lambda\in\mathbb Z^2.
 \tag{PD11}
\]
The fan translation and nowhere-zero torus multiplier extend this
map across every toric stratum. With Euclidean operator norm,
$B_0^{\mathsf t}B_0=I$, and
\[
 B_{t_c,c}=B_0+\frac{-2\pi\Im C(t_c,c)}{\log|t_c|},
 \quad \|B_{t_c,c}-B_0\|<\tfrac12,
 \quad \tfrac12\|\lambda\|<\|B_{t_c,c}\lambda\|
                    \le\tfrac32\|\lambda\|\quad(\lambda\ne0).
 \tag{PD12}
\]
These inequalities exclude stabilizers on the dense torus.
For a height-one triangle, use its three dual unimodular cone
coordinates $z_0,z_1,z_2$, with $t_c=z_0z_1z_2$.
In the open chart $|z_i|<2$, $|t_c|<\epsilon$, the normalized
logarithmic barycentric coefficients have sum one and are bounded
below by $-\log2/|\log\epsilon|$. Thus the logarithmic positions
in each fixed chart lie in a bounded set, uniformly in $c$.
For a fixed pair of charts, (PD12) bounds the finitely many
$\lambda$ which can translate one into the other. At the central
fibre a nonzero $B_0\lambda$ moves every bounded fan cell.
The same chart-pair bound applies to sequences tending to that
fibre. Compact sets meet finitely many charts, so the action is
free and properly discontinuous on the entire toric family.

For properness, fix $\epsilon_1<\epsilon$ and let $K_0$ be the
finite union of closed unit polydiscs for height-one triangles
meeting the closed radius-$\sqrt2$ ball, intersected with
$|t_c|\le\epsilon_1$. For $t_c\ne0$, choose $\lambda$ with
$\|B_{t_c,c}^{-1}y+\lambda\|_\infty\le1/2$.
The translated logarithmic position has norm at most
$3/(2\sqrt2)<\sqrt2$. A triangle containing it has nonnegative
barycentric coordinates of sum one, so each corresponding cone
coordinate has modulus at most one. This gives a representative
in $K_0$. At $t_c=0$, translate the height-one component and use
the six closed toric bidiscs covering $E_0\simeq\mathrm dP_6$.
The multiplier $\exp(2\pi iC(0,c)B_0v)$ is included in this
translation; the bidiscs cover the resulting whole compact component.
For each compact $K\subset Q$, the compact set $K_0\times K$
therefore maps onto the full inverse image of
$\{|t_c|\le\epsilon_1\}\times K$. This proves properness.
The quotient charts are open subsets of a smooth toric variety
times $Q$, so projection to $Q$ is a submersion.

\item Exponentiating the logarithmic coordinates gives the cusp
connector with period identity $Z=sB_0+C(t_c,c)$.
Glue it and (PD8) to the middle family. The distinguished base
discs are disjoint. Points with distinct $(t,c)$ values separate
on the base; points with the same value lie in one Hausdorff local
piece. The resulting total space is therefore Hausdorff and smooth.
The local proper maps give a proper map $F$ to $B\times Q$:
cover a compact subset by finitely many relatively compact sets
inside the displayed base pieces. Compactness of $B$ proves
properness of $\pi=\operatorname{pr}_QF$.
The fibres and overlaps are the specified $X_c$ and $f_c$.
These local families agree on smaller cusp radii and glue over
$\mathcal P$. The coherent $2\mathbb Z$ action is properly
discontinuous because its action on $\mathcal P$ is.
Local inverse logarithms for $w=e^{-\pi ic}$ identify its quotient
with the proper local families just proved.
Proposition~\ref{fam:src:A.2.1} gives pairwise non-biholomorphic fibres.
'''
newa3=a3.replace(oldproper,proper)
endstatement=r'\end{proposition}'
newa3=newa3.replace(endstatement,r'''
Before the quotient, every disc $Q$ with $\overline Q\subset\mathcal P$
has the proper holomorphic submersion and proper base map
\[
 \pi:\mathcal X_Q\longrightarrow Q,\qquad
 F:\mathcal X_Q\longrightarrow B\times Q,\qquad
 \pi=\operatorname{pr}_Q\circ F.
 \tag{PD2}
\]
Their restrictions to $c$ are $X_c$ and $f_c$, and their three
distinguished values are the constant sections $0,1,\infty$.
\end{proposition}''',1)

statement=wb[wb.index('Fix a regular base point'):wb.index(r'\end{theorem}')]
statement=statement.replace('one of its original lifts','one of its lifts')
statement=statement.replace('the original period lattice onto the new period lattice','the marked period lattice at $c_*$ onto that at $c$')
statement=statement.replace('from (PD2)',r'from \cref{fam:src:A.3.1}')
newa4=r'''\subsection{The effective period parameter}
\hypertarget{tag-03CV}{}\label{wb:sec:retained-period-deformation}
\begin{proposition}[Exact period variation and the Kodaira--Spencer class]
\hypertarget{tag-01Q4}{}\label{fam:src:A.4.2}\label{fam:st:A.4.2}
\hypertarget{tag-03DP}{}\label{wb:thm:retained-period-deformation}
\StatementRecord{fam:src:A.4.2}{proved}{01Q4}{\cref{fam:src:A.1.1,fam:src:A.3.1}}
Use the proper family of \cref{fam:src:A.3.1} over a disc
$Q$ with $\overline Q\subset\mathcal P$.
'''+statement+r'''\end{proposition}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
'''
proof=wb[wb.index(r'\item \emph{The exact variation on a regular fibre.}'):]
proof=proof.replace('the original ordered lattice basis','the ordered lattice basis')
proof=proof.replace('Neither the nonholomorphic part nor the original marking is dropped.','')
proof=proof.replace('This contradiction proves nonzero Dolbeault class without a dimension\ncount or an appeal to numerical period variation.',
 'This proves that the Dolbeault class is nonzero.')
proof=proof.replace('Both conventions therefore give a nonzero class; they are not identified\nwithout this sign conversion.',
 'Thus the two conventions are related by the displayed sign and both give a nonzero class.')
proof=proof.replace('on each original chart','on each chart')
proof=proof.replace('The finite determinant characters $\\chi_j$, their correcting units\n$e^{\\varphi_j(s_j)}$, and the modular function $\\Theta$ used in\n(HL.9.4)--(HL.9.6) are independent of $c$, since $R_g,\\tau,\\mu$ are.',
 'The finite determinant characters and the holomorphic units in\nthe canonical calculation of \\cref{fam:src:A.1.1} are independent\nof $c$, since $R_g,\\tau,\\mu$ are.')
proof=proof.replace('by the actual same transition functions and divisors','by these transition functions and divisors')
proof=proof.replace('In particular (PD16) is a relative line-bundle isomorphism, not a\ncollection of separately chosen isomorphisms of its fibres.',
 'The joint transition identities prove (PD16) over the whole parameter disc.')
proof=proof.replace('We need its complete degree-two system after an infinitesimal base\nchange, and prove this explicitly. Put',
 'For its complete degree-two system over the dual numbers, put')
proof=proof.replace('This proves the required base-change statement without presuming that\npointwise dimensions alone imply it.',
 'This is the base-change isomorphism for the complete degree-two system.')
proof=proof.replace('The hypothesized trivialization','The proposed trivialization')
proof=proof.replace('the explicitly recorded conversion','the displayed conversion')
newa4+=proof
ed.replace(whole,'','D12',
 'Split the repeated WB argument along its exact content: the proper family and uniform cusp bounds join the coherent-family proof; the real-linear transport and intrinsic-pencil argument form the sole deformation proof. Preserve every PD display and the WB section/theorem identities.',
 'wb:thm:retained-period-deformation')
ed.replace(a4,'','D12','Move the deformation statement to the credited appendix immediately after the proper-family construction and use the fuller exact variation proof once.','fam:src:A.4.2')
ed.replace(a3,newa3+'\n\n'+newa4,'D12',
 'Consolidate duplicate parameter-family and Kodaira–Spencer arguments while retaining all quantitative cusp estimates, exact graph/inverse formulas and dual-number critical-scheme calculations. The covariance conventions are related explicitly by M_g=A_g^{-1}.',
 'fam:src:A.3.1')
# The two repeated defining displays receive their old display markers at the
# single definitions; equation renumbering later supplies the final numbers.
old=block(ed.text,'I:def:family-parameter')
new=old.replace(r'\qquad w=e^{-\pi ic}.'+'\n'+r'\]',r'\qquad w=e^{-\pi ic}.\tag{PD1}'+'\n'+r'\]')
assert old!=new
ed.replace(old,new,'D12','Attach the former repeated admissible-half-plane display marker to its one numbered definition.','I:def:family-parameter')
old=block(ed.text,'def:common-conventions')
needle=r'\qquad (\beta^{\rm part}+\tau)(p_0)=0.'
new=old.replace(needle,needle+r'\tag{PD6}')
assert old!=new
ed.replace(old,new,'D12','Attach the former repeated period-matrix display marker to the single defining period matrix.','def:common-conventions')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_period_deformation_comparison.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'read_scope':'Root read the complete 17,257-character WB statement/proof, the complete 3,782-character A4.2 statement/proof, the A3.1 properness step and the agent’s complete sixteen-step comparison before editing.',
 'correspondence':{'WB1–6':'A3.1 proper-family proof with the full local F/submersion statement, PD2,PD7–12; exact barycentric chart bound restored from its former proof.',
 'WB7–10':'Single A4.2 exact marked real-linear variation, inverse, plus-graph and tangent-extension sign.',
 'WB11–16':'Single A4.2 joint relative canonical transitions, exact dual-number section basis, critical-scheme fixed sections and Cech trivialization.',
 'PD1 and PD6':'The unique numbered parameter and marking definitions.',
 'covariance':'M_g=A_g^{-1} converts Pi(gz)=R_gPi(z)M_g to R_gPi(z)=Pi(gz)A_g.'},
 'scope':'Consolidation/re-read; no new independent derivation credit claimed.'},indent=2)+'\n')
