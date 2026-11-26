from S6_SERIES_PUBLISH_c3_foundations_sec11_helpers import *
from collections import Counter

main=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
anchor=r'\subsection{Maximal Hopf component reduction}\label{subsec:II:maximal-hopf-reduction}'
if anchor not in main:
    for g in json.loads((OUT/'S6_SERIES_PUBLISH_sec11_canonical_flat_guards.json').read_text()):
        assert main.count(g['old'])==1, g['key']
        main=main.replace(g['old'],g['new'],1)

pkg=Package('roots','subsec:II:rooted-generation')
old76=block(main,'cdp:st:C.2.UN.76')
old78=block(main,'cdp:st:C.2.UN.78')
old86=block(main,'cdp:st:C.2.UN.86')
for suffix,text in [('UN76_input',old76),('UN78_input',old78),('UN86_input',old86)]:
    (OUT/('S6_SERIES_PUBLISH_II_sec11_roots_'+suffix+'.tex')).write_text(text+'\n',newline='\n')

def part(text,a,b):
    aa=text.index(a); bb=text.index(b,aa); return text[aa:bb]

def display(text,label):
    p=text.index(r'\label{'+label+'}')
    a=text.rfind(r'\[',0,p); b=text.index(r'\]',p)+2
    assert a>=0
    return text[a:b]

def alias(text,primary,aliases):
    p=text.index(r'\label{'+primary+'}')
    a=text.rfind(r'\[',0,p)+2
    assert a>1
    hook='\n'+''.join(r'\hypertarget{tag-'+tag+'}{}' for tag,label,oldtag in aliases)+r'\SsixEquationAliases{'+''.join(r'\label{'+label+'}' for tag,label,oldtag in aliases)+'}\n'
    for tag,label,oldtag in aliases:
        pkg.equations.append(dict(old_tag=oldtag,label=label,owner='prop:II:cyclic-root-normalization'))
        pkg.record('D12,D19,D20','prop:II:cyclic-root-normalization',oldtag+' / '+label,primary+' with alias '+label,'The exact same root datum/equality is consolidated at the general owner; its consumer substitution is explicitly stated and all permanent targets remain.')
    return text[:a]+hook+text[a:]

root_diagram=display(old78,'cdp:eq:C.RK.2')
root_diagram=root_diagram.replace(r'\qquad G=\mu_N.',r'\qquad G=\mu_N,\qquad Y_N/G=Y.')
root_data=r'''\[
\begin{gathered}
D_I^\circ=\left(\bigcap_{i\in I}D_i\right)
          \setminus\bigcup_{j\notin I}D_j,\qquad
d_I=\gcd_{i\in I}m_i,\qquad
\nu_I=\frac{N^{|I|-1}d_I}{\prod_{i\in I}m_i},\\
R_N=\sum_I(d_I\nu_I-1)e_c(D_I^\circ),\qquad
\Delta_\pi=2p_\pi+\sum_\beta(2-2g(B_\beta)).
\end{gathered}
\tag{C.RK.6}\hypertarget{tag-0108}{}\label{cdp:eq:C.RK.6}
\]'''
orig_data=display(old86,'cdp:eq:C.AR.6')
cover_data=display(old78,'cdp:eq:C.RK.18')
threshold=display(old78,'cdp:eq:C.RK.19')

p342=r'''\subsection{Cyclic roots, canonical orders and Euler corrections}\label{subsec:II:cyclic-root-normalization}

\begin{proposition}[Normalized cyclic roots of torus degenerations]\hypertarget{tag-P342}{}\label{prop:II:cyclic-root-normalization}
\StatementRecord{prop:II:cyclic-root-normalization}{proved}{P342}{\cref{lem:II:canonical-bimeromorphic-direct-image,lem:II:blowup-topology,cdp:st:C.2.UN.17}; \cite[\S0.2(2), pp.~3--4; Theorem~1.6 and Remarks~1.7, pp.~5--6; Theorem~1.10, p.~7]{BierstoneMilman1997}}
Let $f:X\to\Delta_t$ be a proper degeneration of connected complex
two-tori from a smooth threefold, with arbitrary full central fibre.
Choose a generator $\Omega$ of $f_*K_X$ and an embedded resolution
$\pi:Y\to X$ by smooth central point and curve blowups, so that
$\operatorname{div}(f\pi)=\sum_i m_iD_i$ has SNC support and
$\operatorname{div}(\pi^*\Omega)=\sum_i k_iD_i$.
Put $r_i=(k_i+1)/m_i$, and choose an integer $N$ divisible by all $m_i$.
There is a $G$-equivariant normalization and semistable resolution
'''+root_diagram+r'''
in which $Z$ is smooth with connected full reduced SNC central fibre.
The map $q$ is a composition of normalized monomial-ideal blowups,
with specified height-one subdivisions and inverse coarsening maps.
Every component added by $q$ is ruled or rational. The old component
and stratum labels, local unit-root choices and all transition maps
are part of these maps. The quotient in the diagram is the finite
analytic quotient.

For a primitive height-one ray $(v,1)$ the pulled canonical form has
order $\sum_i(k_i+1)v_i-1$. Its minimum is
$a_{\min}=N\min_i r_i-1$, and
$\Omega_Z=s^{-a_{\min}}q^*\rho^*\pi^*\Omega$ generates the canonical
direct image of $Z\to\Delta_s$. For
$\gamma:s\mapsto\zeta s$, its character is
$\gamma^*\Omega_Z=\zeta^{-a_{\min}}\Omega_Z$.

For each nonempty stratum define
'''+root_data+r'''
where $p_\pi$ counts the point centres and the $B_\beta$ are the
connected compact curve centres of $\pi$. Then $1\le |I|\le3$,
$\nu_I$ is a positive integer, and the central cover of $D_I^\circ$
in $Y_N$ is finite \'etale of degree $d_I$. The fibre of $q$ over
each point of that cover has Euler number $\nu_I$. With
$S=f^{-1}(0)_{\rm red}$, $S_Y=(f\pi)^{-1}(0)_{\rm red}$ and
$S_Z=(Z_0)_{\rm red}$, one has
$e(S_Z)-e(S_Y)=R_N$ and $e(S_Y)-e(S)=\Delta_\pi$.

Write the original full divisor and generator orders as
'''+orig_data+r'''
On the normalization $T_\alpha$ of $S_\alpha$, the following finite
algebras glue and have a finite normal cover $C_\alpha\to T_\alpha$:
'''+cover_data+r'''
Here $g_j$ is a local Cartier equation of $S_\alpha$ and
$u_j=f/g_j^{n_\alpha}$. The strict root components over $S_\alpha$
are proper birational resolutions of the connected components of
this cover, through $w_j=s^{N/n_\alpha}/g_j$. Every root component
with a Hopf minimal model is obtained from one of these original
component covers. The exceptional components of $\pi$ and their
finite normal covers are projective, and the additional components
of $q$ are ruled or rational.

The intrinsic density threshold
'''+threshold+r'''
satisfies $\tau=\min_i r_i$. The density $|\Omega|^2$ is the positive
top-degree density of the holomorphic three-form. The strict root
orders are $N(r_i-\tau)$, and the covers and threshold are independent
of the embedded resolution and the divisible exponent.

For a compact family over a compact curve, the same construction
can be made on a connected cyclic base cover ramified to order $N$
at the selected value and \'etale over all other critical values.
Its local root chart is equivariantly isomorphic to $t=s^N$.
The total root family is smooth away from the selected fibre,
where the same equivariant resolution applies.
\end{proposition}

\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
'''

root_prefix=part(old78,r'\item \par\medskip\noindent\textbf{Embedded resolution',r'\par\medskip\noindent\textbf{The actual finite birational action')
root_prefix=pkg.edit(root_prefix,r'''Use analytic embedded resolution by central
smooth centres, as in \ref{cdp:st:C.2.UN.39} and
\cite[Theorems~1.6 and1.10]{BierstoneMilman1997}.''',r'''Apply analytic embedded resolution to the central support
in the smooth threefold: \cite[\S0.2(2), pp.~3--4;
Theorem~1.6 and Remarks~1.7, pp.~5--6; Theorem~1.10, p.~7]{BierstoneMilman1997}.
The support is compact, so the relatively compact formulation of
Theorem~1.6 gives a finite sequence near this fibre. Its centres
lie over the central support and the maps are isomorphisms over
$\Delta_t^*$.''','D17,D18,D20','prop:II:cyclic-root-normalization','The freshly opened analytic category and exact finite-neighbourhood theorem are applied to this compact central support; no projective resolution premise is added.')
root_prefix=pkg.edit(root_prefix,r'''The actual pullback of $\Omega$ is the
canonical generator on $Y$: apply the
Hartogs direct-image comparison (C.KG.6)
to the ordinary blowup maps.''',r'''The pullback of $\Omega$ is a canonical generator on $Y$:
apply \cref{lem:II:canonical-bimeromorphic-direct-image} with
$(X,X',\phi)=(Y,X,\pi)$ and the corresponding two maps to the disc.''','D04,D12,D20','prop:II:cyclic-root-normalization','Use the unique earlier direct-image owner on exactly the chosen resolution.')
root_prefix=pkg.edit(root_prefix,r'''Since all
new components are ruled or rational,
\ref{cdp:st:C.2.UN.75}'s Hopf-minimum condition is
exactly \eqref{cdp:eq:C.RK.3} for the strict covers.
This proves both directions of the
test for the chosen resolution record.
It also retains the actual generator
character''',r'''For the deck generator the resulting character is''','D12,D14','prop:II:cyclic-root-normalization','Keep the unconditional canonical root formula here. The Hopf-minimum test remains at UN78, with this formula as its earlier input.')
root_prefix=root_prefix.replace(r'''\mathcal L_I=\left\{(v,h)\in\Z^r\oplus\Z:
                         \sum_i m_iv_i=Nh\right\}''',r'''\mathcal L_I=\left\{(v,h)\in\Z^r\oplus\Z:
                         \sum_i m_iv_i=Nh\right\},\qquad
 \sigma_I=\{(v,h)\in(\mathcal L_I)_{\R}:v_i\ge0\}''')
pkg.record('D12,D20','prop:II:cyclic-root-normalization','C.WF.5 lattice L and cone sigma','C.RK.10 lattice L_I and cone sigma_I','The UN76 substitution N=M identifies both the lattice and its exact positive cone; the cone is retained in the common display.')
p342+=root_prefix

quotient=part(old78,'Its quotient\nis literally $Y$.','This argument applies to the\nnormalization on the connected')
quotient_tail=part(old78,'This argument applies to the\nnormalization on the connected','The retained\nordinary blowdowns')
p342+=r'''\item \par\medskip\noindent\textbf{The finite analytic quotient.}
The quotient of the normal root is $Y$.
'''+quotient[quotient.index('Indeed on a'):]+quotient_tail+'\n'

euler=part(old78,r'\par\medskip\noindent\textbf{The root correction',r'\item The original resolution has')
p342+=r'\item '+euler+r'''
\item For each arrow in $\pi$, apply \cref{lem:II:blowup-topology}
to its smooth compact centre and the compact reduced support
containing it. The full reduced inverse image is the next support.
The Euler increment is two for a point and $2-2g(B_\beta)$
for a connected smooth curve. Their sum is $\Delta_\pi$ in
\eqref{cdp:eq:C.RK.6}, proving $e(S_Y)-e(S)=\Delta_\pi$.

'''
intrinsic=part(old78,r'\par\medskip\noindent\textbf{Intrinsic covers',r'\par\medskip\noindent\textbf{Compact scope.}')
intrinsic=intrinsic.replace(r'''Together with \eqref{cdp:eq:C.RK.21} and the
exceptional-component comparison,
\eqref{cdp:eq:C.RK.22} proves exactly
\eqref{cdp:eq:C.RK.20} and the stated
choice independence.''',r'''Together with \eqref{cdp:eq:C.RK.21} and the exceptional-component
comparison, this proves the stated choice independence. Subtracting
$a_{\min}=N\tau-1$ from the strict ray order gives
'''+display(old86,'cdp:eq:C.AR.16')+r'''
with the original strict components retaining
$(k_i,m_i)=(a_\alpha,n_\alpha)$.''')
p342+=r'\item '+intrinsic
compact=part(old86,r'\par\medskip\noindent\textbf{Compact data and the extent',r'\item The finite action is conjugated')
compact=compact.replace(r'\textbf{Compact data and the extent of the core parametrizations.}',r'\textbf{A compact cyclic base cover with the specified local root.}')
p342+=r'\item '+compact+r'''
The normalization and resolution maps are proper and equivariant.
Their quotient and the original smooth-centre blowdowns recover
the given compact family through the same local invariant-ring map.
\end{enumerate}
\end{proof}
'''

p342=alias(p342,'cdp:eq:C.RK.2',[('00A1','cdp:eq:C.AR.10','C.AR.10'),('016T','cdp:eq:C.WF.6','C.WF.6')])
p342=alias(p342,'cdp:eq:C.RK.6',[('0109','cdp:eq:C.RK.7','C.RK.7'),('00A8','cdp:eq:C.AR.2','C.AR.2'),('00A9','cdp:eq:C.AR.3','C.AR.3')])
p342=alias(p342,'cdp:eq:C.RK.9',[('016R','cdp:eq:C.WF.4','C.WF.4')])
p342=alias(p342,'cdp:eq:C.RK.10',[('016S','cdp:eq:C.WF.5','C.WF.5'),('00A2','cdp:eq:C.AR.11','C.AR.11')])
p342=alias(p342,'cdp:eq:C.RK.16',[('00A5','cdp:eq:C.AR.14','C.AR.14')])
p342=alias(p342,'cdp:eq:C.RK.22',[('00A6','cdp:eq:C.AR.15','C.AR.15')])

new78=old78
new78=pkg.edit(new78,part(new78,'Form\nthe actual normalization and a toric semistable', 'The following is an explicit finite-cover condition'),r'''Apply \cref{prop:II:cyclic-root-normalization} with this
resolution $\pi$ and this exponent $N$. Let $Y_N$, $Z$, $q$,
$\rho$ and $G=\mu_N$ be its maps in \eqref{cdp:eq:C.RK.2}.
Then $Z$ is smooth with full reduced SNC central fibre,
and every component added by $q$ is ruled or rational.

''','D12,D14,D19,D20','cdp:st:C.2.UN.78','Keep the same chosen least common multiple and resolution; the exact general root construction now precedes this application.')
new78=pkg.edit(new78,part(new78,'The Euler correction for the root is explicit.', 'Let\n$\\Delta_K$'),r'''Use the strata, integers $d_I,\nu_I$, and Euler corrections
$R_N,\Delta_\pi$ of \eqref{cdp:eq:C.RK.6} for this resolution.
''','D12,D19,D20','cdp:st:C.2.UN.78','The exact root/ordinary-blowup corrections have a single earlier definition, including every original centre and full multiplicity.')
intrinsic_statement=part(new78,r'On the normalization $T_\alpha$ of $S_\alpha$', r'Then \eqref{cdp:eq:C.RK.3} is equivalent to')
new78=pkg.edit(new78,intrinsic_statement,r'''Use the finite normal covers $C_\alpha\to T_\alpha$
and the density threshold $\tau$ of
\eqref{cdp:eq:C.RK.18}--\eqref{cdp:eq:C.RK.19}, constructed by
\cref{prop:II:cyclic-root-normalization} on this same original family.
''','D12,D19,D20','cdp:st:C.2.UN.78','Transfer the full cover equations, cocycle, density definition and proof to their general owner. The exact Hopf-minimum equality remains here.')
proof78=r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Apply \cref{prop:II:cyclic-root-normalization} with
$(f,X,\pi,Y,N)$ as in \eqref{cdp:eq:C.RK.1}. Its root charts,
height-one subdivisions, compact support and canonical generator
are exactly those in \eqref{cdp:eq:C.RK.2} and
\eqref{cdp:eq:C.RK.9}--\eqref{cdp:eq:C.RK.13}.
The primitive strict orders are $N(r_i-\tau)$, where
$\tau=\min_jr_j$. All additional semistable components are
ruled or rational. Consequently every Hopf-birational prime of
$Z$ has minimum canonical order exactly when \eqref{cdp:eq:C.RK.3}
holds. Apply \cref{cdp:st:C.2.UN.75} to this full reduced SNC
torus family. Its equivalence proves both directions of the
stated canonical-flat criterion.

'''
action=part(old78,r'\par\medskip\noindent\textbf{The actual finite birational action',r'\par\medskip\noindent\textbf{The root correction')
old_q=part(action,'Its quotient\nis literally $Y$.','These exact maps\nprove')
action=pkg.edit(action,old_q,r'''Apply the invariant-ring comparison
\eqref{cdp:eq:C.RK.14} to this same normal root:
$A=\OO_Y$, and $B$ is the integral closure of
$A[s]/(s^N-f\pi)$. It gives $B^G=A$, including the local
split branches permuted by $G$. Thus $Y_N/G=Y$.
The prescribed ordinary blowdowns $\pi$ recover $X$.
''','D12,D19,D20','cdp:st:C.2.UN.78','Use the earlier full finite-normalization invariant-ring proof on the identical algebra after reversing phi and coarsening q.')
action=pkg.edit(action,'An equivariant replacement of\n$\\phi$ has not been used.','The action on the core is the displayed birational conjugate,\nand reversal restores its original regular action on $Z$.','D02','cdp:st:C.2.UN.78','State the exact action and the order of the inverse and quotient maps positively.')
proof78+=r'\item '+action+r'''
\item The Euler comparison of \cref{prop:II:cyclic-root-normalization}
gives $e(S_Z)-e(S_Y)=R_N$ and $e(S_Y)-e(S)=\Delta_\pi$
for these exact proper maps. By definition of the forward
modification defect, $e(S_0)-e(S_Z)=\Delta_K$.
Adding the three equalities proves \eqref{cdp:eq:C.RK.8}.
The values of $e(S_0)$ are those of \cref{cdp:st:C.2.UN.75}.
This is the same original support as in
\cref{cdp:st:C.2.UN.39}, so the two proper-map formulas compute
its same Euler number.

\item The original-cover comparison of
\cref{prop:II:cyclic-root-normalization} is the map
$w_j=s^{N/n_\alpha}/g_j$ with exactly the transition
$w_k=(g_j/g_k)|_{T_\alpha}w_j$.
It accounts for every strict root component and proves that
all Hopf root components come from these original covers.
The original strict transform keeps
$(k_i,m_i)=(a_\alpha,n_\alpha)$, while
$\tau=\min_i(k_i+1)/m_i$ by the same density calculation.
Thus \eqref{cdp:eq:C.RK.3} is exactly \eqref{cdp:eq:C.RK.20}.
The covers and density are defined on the original family,
which proves the stated independence of the resolution,
semistable subdivision and divisible root exponent.

\item For an original compact family, use the compact cyclic
cover in \cref{prop:II:cyclic-root-normalization}. It has the
same selected local root model and is \'etale over every other
critical value. Perform the normal base change and equivariant
resolution globally, and the \cref{cdp:st:C.2.UN.75} modification
near the selected root fibre. Its punctured isomorphism glues
on an annulus to the unchanged complement. Conjugate the global
finite action through this proper bimeromorphism. Reversing
the record makes the action regular, and the proper coarsening,
finite quotient and ordinary blowdowns in \eqref{cdp:eq:C.RK.5}
recover the original compact family. The converse uses these
same maps on the given compact core and its specified analytic
neighbourhood. This retains all transverse terms in that input.
\end{enumerate}
\end{proof}'''
oldproof78=new78[new78.index(r'\begin{proof}'):]
new78=pkg.edit(new78,oldproof78,proof78,'D02,D08,D12,D14,D17,D20','cdp:st:C.2.UN.78','Complete proof consolidation: unconditional root, quotient, canonical, cover and Euler calculations move to P342; the exact canonical-flat criterion, conjugate action, ordered reconstruction and compact inverse remain proved here.')

# The short weighted marking datum is a definition, and its complete owner moves after P342.
orphan76start=main.rfind('In this subsection the marked weighted data include',0,main.index(old76))
assert orphan76start>=0
orphan76=main[orphan76start:main.index(old76)]
p349=r'''\begin{definition}[Marked weighted toric support]\hypertarget{tag-P349}{}\label{def:II:marked-weighted-toric-support}
\StatementRecord{def:II:marked-weighted-toric-support}{proved}{P349}{}
The marked weighted data of a central fibre consist of its reduced
central analytic space, its component multiplicities, the central
log space of its normalized cyclic root, and the old cone cells
before their semistable subdivision. A coarsening in these data
is a proper toric morphism between the specified monoid charts.
The component gluing maps and the normalized-root/coarsening
maps are included in the datum.
\end{definition}
'''
pkg.record('D02,D08,D13','def:II:marked-weighted-toric-support',orphan76,p349,'Number the entire existing marked analytic/root/coarse-cone datum before its first theorem; retain all its maps.')
new76=old76
old_root76=part(new76,r'\item \par\medskip\noindent\textbf{The actual normalized-root',r'\item \par\medskip\noindent\textbf{The canonical orders')
new_root76=r'''\item \par\medskip\noindent\textbf{The normalized root and its coarsening.}
Choose $M$ divisible by all $m_i$ and put $t=s^M$.
Apply \cref{prop:II:cyclic-root-normalization} with
$(\pi,Y,N,Z,Y_N)=(\operatorname{id}_X,X,M,\widetilde X,X_M)$.
The original support is already SNC. Its local coordinates and
lattice are \eqref{cdp:eq:C.WF.4}--\eqref{cdp:eq:C.WF.5}, with
the general root exponent $N$ replaced by $M$; all unit roots
and tangent-dependent transition maps are the ones of this $f$.
The same height-one monomial-ideal subdivisions give the proper
equivariant map in \eqref{cdp:eq:C.WF.6}. The finite quotient
$X_M/\mu_M=X$ is its invariant-ring comparison. The subdivision
and its inverse coarsening, all original component labels, and
each new ray's old stratum and lattice position stay in these
maps. In particular the support on $\widetilde X$ is globally
embedded SNC, as proved by that labelled-ray comparison.

'''
new76=pkg.edit(new76,old_root76,new_root76,'D02,D08,D12,D14,D19,D20','cdp:st:C.2.UN.76','Exact N=M, pi=id specialization of the common root owner; all branches, unit transitions, old rays, proper equivariant maps, finite quotient and global embeddedness are retained.')
new76=pkg.edit(new76,r'''At a height-one ray \((v,1)\), direct differentiation of
\eqref{cdp:eq:C.WF.4} gives''',r'''Under that same substitution, the canonical ray formula
\eqref{cdp:eq:C.RK.11} gives, at every height-one ray $(v,1)$,''','D12,D20','cdp:st:C.2.UN.76','Keep the full common-ratio specialization at its owner, applying the earlier exact Jacobian formula.')
new76=pkg.edit(new76,r'''For an old ray this is \(M(k_i+1)/m_i-1\).
For every new ray it is the affine interpolation of those
old values.  This also proves the formula in a two-factor
chart after wedging the unchanged tangent differential.
The pulled-back nonzero coefficient is a unit throughout
each normalization chart.  Hence''',r'''The equality uses $\sum_i m_iv_i=M$ and
$k_i+1=\lambda m_i$. The common value applies to old and new
rays and includes the unchanged tangent differential in a
two-factor chart. The nonzero pulled coefficient is a unit;
the primitive form in \eqref{cdp:eq:C.RK.13} is therefore''','D12,D20','cdp:st:C.2.UN.76','The scalar lambda substitution is fully explicit, with the coefficient and every ray type retained.')

# Number the complete finite reconstruction datum at the beginning of its actual unit.
orphan86start=main.rfind('The data in the following construction include analytic',0,main.index(old86))
assert orphan86start>=0
orphan86=main[orphan86start:main.index(old86)]
data86=orphan86[orphan86.index(r'\begin{enumerate}'):]
data86=data86[:data86.rfind('This is the compact\nversion of the same definition.')]+ 'This is the compact\nversion of the same definition.\n' if 'This is the compact\nversion of the same definition.' in data86 else data86
p341=r'''\begin{definition}[Finite rooted reconstruction data]\hypertarget{tag-P341}{}\label{def:II:finite-rooted-reconstruction}
\StatementRecord{def:II:finite-rooted-reconstruction}{proved}{P341}{\cref{def:II:overlap-compatible-modification,prop:II:cyclic-root-normalization,cdp:st:C.2.UN.85}}
Finite rooted reconstruction data comprise the following analytic
neighbourhoods, arrows and transition maps, including the full
transverse terms used by each inverse operation.
'''+data86+r'''\end{definition}
'''
pkg.record('D02,D08,D13','def:II:finite-rooted-reconstruction',orphan86,p341,'Number the full existing admissible construction input, preserving all core atlases, inverse sigma arrows, cyclic-action regularization, invariant charts and smooth blowdowns.')

new86=old86
new86=pkg.edit(new86,'is the output of the finite admissible construction\nabove.',r'is the output of the finite construction in\n\cref{def:II:finite-rooted-reconstruction}.'.replace('\\n','\n'),'D04,D13','cdp:st:C.2.UN.86','Refer to the numbered full analytic input instead of an unnumbered preceding construction.')
root_def86=part(new86,'Here is an explicit formula selecting precisely the',r'Let \(\Delta_\sigma\)')
new86=pkg.edit(new86,root_def86,r'''For the data of \cref{def:II:finite-rooted-reconstruction},
put $S_*=f_*^{-1}(0)$ and use the quotient components $D_i$
of \eqref{cdp:eq:C.AR.1}. Define $D_I^\circ,d_I,\nu_I,R_N$
and $\Delta_\pi$ by the common formulas
\eqref{cdp:eq:C.AR.2}--\eqref{cdp:eq:C.AR.3} in
\cref{prop:II:cyclic-root-normalization}, with the same $N,m_i$
and ordinary blowup record $\pi$.
''','D12,D19,D20','cdp:st:C.2.UN.86','The exact root and resolution corrections have one earlier definition; all full multiplicities and centre genera are retained.')
new86=pkg.edit(new86,display(new86,'cdp:eq:C.AR.6'),'Use the full original divisor and generator coefficients\nin \\eqref{cdp:eq:C.AR.6}.','D12,D19,D20','cdp:st:C.2.UN.86','The full original coefficient display is at P342, with the same a_alpha,n_alpha used for this intrinsic branch test.')

old_root86=part(new86,r'\item \par\medskip\noindent\textbf{The actual forward construction',r'\item Apply the complete reduced theorem')
root86=r'''\item \par\medskip\noindent\textbf{Forward construction from the original fibre.}
Apply \cref{cdp:st:C.2.UN.17} and
\cref{prop:II:cyclic-root-normalization} to the given proper
smooth-threefold torus degeneration. Choose its embedded
resolution $\pi:Y\to X$ and $N=\operatorname{lcm}_i m_i$.
The resolved full divisor and canonical orders are
'''+display(old86,'cdp:eq:C.AR.9')+r'''
The maps in \eqref{cdp:eq:C.AR.10}, with the lattice
\eqref{cdp:eq:C.AR.11}, are precisely that owner's normalization
and equivariant height-one resolution. The labelled monomial-ideal
maps retain the original units and glue to a proper $q$.
Their root $Z$ is connected, smooth and full reduced SNC,
and every map is an isomorphism off the selected fibre.

'''
new86=pkg.edit(new86,old_root86,root86,'D02,D08,D12,D14,D19,D20','cdp:st:C.2.UN.86','Apply the complete general root construction to exactly this original family and its chosen lcm, preserving the displayed resolved divisor data and the complete root/cone maps.')
q86=part(new86,r'For a normal local ring \(A\) of \(Y\),','and the full comparison is')
new86=pkg.edit(new86,q86,r'''The local invariant algebra is exactly
\eqref{cdp:eq:C.RK.14}: $A=\OO_Y$, and $B$ is the integral
closure of $A[s]/(s^N-f\pi)$, including any split local branches.
Thus $B^{\mu_N}=A$ by the common root owner,
''','D12,D20','cdp:st:C.2.UN.86','Use the same proved finite-normalization quotient only after the inverse record and equivariant coarsening.')
e86=part(new86,r'\par\medskip\noindent\textbf{Original support Euler numbers',r'\item The ordinary blowups give')
new86=pkg.edit(new86,e86,r'''\par\medskip\noindent\textbf{The Euler changes of the specified maps.}
Apply \cref{prop:II:cyclic-root-normalization} with the
resolution $\pi$, exponent $N$ and coarsening $q$ in
\eqref{cdp:eq:C.AR.10}. Its stratum cover has degree $d_I$,
its toric fibre has Euler number $\nu_I$, and its determinant
and fixed-point computations include every global sheet
permutation. This is exactly
\eqref{cdp:eq:C.AR.14}, $e(S_Z)-e(S_Y)=R_N$.

''','D02,D08,D12,D19,D20','cdp:st:C.2.UN.86','The complete stratum, normalized-volume and quotient Euler proof has one owner with the same finite covers and full weights.')
i86=part(new86,r'\par\medskip\noindent\textbf{Intrinsic root data',r'\par\medskip\noindent\textbf{Compact data and the extent')
new86=pkg.edit(new86,i86,r'''\par\medskip\noindent\textbf{The intrinsic endpoint test.}
Use the finite covers $C_\alpha\to T_\alpha$ and threshold
$\tau$ of \cref{prop:II:cyclic-root-normalization} on the same
original family and generator. The strict-cover map is
$w_j=s^{N/n_\alpha}/g_j$, with transitions
$w_k=(g_j/g_k)w_j$. It gives a proper birational resolution
of every connected component of $C_\alpha$. The owner's
projective exceptional-cover and ruled semistable-component
comparisons account for all Hopf root components.

The density equality \eqref{cdp:eq:C.AR.15} and the strict-order
formula \eqref{cdp:eq:C.AR.16} apply with
$(k_i,m_i)=(a_\alpha,n_\alpha)$ on each original strict component.
Their maximum over precisely those Hopf covers is
$N(H-\tau)$, proving \eqref{cdp:eq:C.AR.8} and its integrality.
When there is no Hopf root component, \cref{cdp:st:C.2.UN.75}
applies. Otherwise all its Hopf orders vanish exactly when
$H=\tau$; this is that same canonical-flat criterion. For
$H>\tau$, \cref{cdp:st:C.2.UN.84,cdp:st:C.2.UN.85} give the
positive-Hopf core. Both the covers and the density are defined
on the original family, so this test is independent of the
resolution, subdivision and divisible exponent.

''','D02,D08,D12,D19,D20','cdp:st:C.2.UN.86','Retain the full intrinsic maximum/order criterion and both endpoint branches; apply the exact earlier finite-cover and density proof instead of repeating it.')
comp86=part(new86,r'\par\medskip\noindent\textbf{Compact data and the extent',r'\item The finite action is conjugated')
new86=pkg.edit(new86,comp86,r'''\par\medskip\noindent\textbf{Compact families and their prescribed neighbourhoods.}
Apply the compact-cover construction in
\cref{prop:II:cyclic-root-normalization} at the selected value $c$.
It uses the original critical set $\Sigma$, a pole point
$p\notin\Sigma\cup\{c\}$, and a meromorphic function $a$
with jet $t+O(t^2)$ at $c$ and value one at the other critical
points. The connected normalized cover $s^N=a$ is \'etale
over those other critical values. The explicit map
$\sigma=s/u(t)^{1/N}$, where $a=t u(t)$, identifies its
local root with $\sigma^N=t$, equivariantly and with inverse
$s=\sigma u(t)^{1/N}$. All additional branch values lie
over submersion charts, so the total root family is smooth
away from the selected fibre. Perform the root resolution
and modification there, using their specified identity maps
on the annulus and complement.

''','D12,D20','cdp:st:C.2.UN.86','Transfer the full common Riemann–Roch/compact cyclic-cover construction to P342 and retain its exact map and critical-value specialization here.')

exec(Path(__file__).with_name('S6_SERIES_PUBLISH_c3_foundations_sec11_roots_finish.py').read_text(), globals())

# Text cleanup is completed explicitly below before admitting any receiving unit.
for textname,owner in [('p342','prop:II:cyclic-root-normalization'),('new76','cdp:st:C.2.UN.76'),('new78','cdp:st:C.2.UN.78'),('new86','cdp:st:C.2.UN.86'),('p341','def:II:finite-rooted-reconstruction')]:
    val=locals()[textname]
    val=pkg.clean(val,owner)
    locals()[textname]=val

exec(Path(__file__).with_name('S6_SERIES_PUBLISH_c3_foundations_sec11_roots_polish.py').read_text(), globals())

# Place the complete weighted unit after the earlier root construction.
weighted_unit='\\subsection{Weighted toric descent and compact occurrence}\\label{subsec:II:weighted-toric-descent}\n\n'+p349+'\n'+new76
gen_unit='\\subsection{Finite rooted generation}\\label{subsec:II:rooted-generation}\n\n'+p341+'\n'+new86
flatroot_unit='\\subsection{Canonical-flat root descent}\\label{subsec:II:canonical-flat-root-descent}\n\n'+new78+'\n\\subsection{Contractions of no-triple fibres}\\label{subsec:II:no-triple-contractions}\n'
pkg.guard('remove-earlier-weighted-owner',orphan76+old76,'','Move the complete weighted construction after its earlier general root owner; all receiving text and maps are compared, with no movement-only completion credit.')
pkg.guard('P342-and-weighted-before-Hopfs',anchor,p342+'\n'+weighted_unit+'\n'+anchor,'The shared normalized-root construction follows UN75; the complete weighted construction follows it with exact N=M and pi=id applications.')
pkg.guard('UN78-canonical-flat-root',old78,flatroot_unit,'Replace the complete canonical-flat root criterion and reconstruction unit; the following no-triple unit is separately open.')
pkg.guard('P341-UN86-rooted-generation',orphan86+old86,gen_unit,'Number the complete reconstruction datum and replace the complete general rooted-generation proof through its exact earlier root applications.')

replayed=main
for g in pkg.guards:
    assert replayed.count(g['old'])==1,g['key']
    replayed=replayed.replace(g['old'],g['new'],1)
for pattern in [r'\\label\{([^{}]+)\}',r'\\hypertarget\{([^{}]+)\}']:
    before=Counter(re.findall(pattern,main)); after=Counter(re.findall(pattern,replayed))
    assert all(after[k]==v for k,v in before.items()),[(k,v,after[k]) for k,v in before.items() if after[k]!=v]

pkg.write(p342+'\n'+weighted_unit+'\n'+flatroot_unit+'\n'+gen_unit)
for suffix,text in [('P342',p342),('P349_UN76',weighted_unit),('UN78_receiving',flatroot_unit),('P341_UN86',gen_unit)]:
    (OUT/('S6_SERIES_PUBLISH_II_sec11_roots_'+suffix+'.tex')).write_text(text+'\n',newline='\n')
print('Five guards replay once; old labels and permanent targets exact. P341/P342/P349. Full receiving reading and final cleanup pending.')
