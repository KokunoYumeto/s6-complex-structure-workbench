from S6_SERIES_PUBLISH_c3_foundations_sec11_helpers import *
from collections import Counter

main=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
old=block(main,'cdp:st:C.2.UN.71')
capture=OUT/'S6_SERIES_PUBLISH_II_sec11_toric_log_input.tex'
if capture.exists(): assert capture.read_text().rstrip()==old
else: capture.write_text(old+'\n',newline='\n')
p=Package('toric_log','subsec:II:toric-central-log-spaces')
new=p.clean(old,'cdp:st:C.2.UN.71')
for a,b in [('in an\ntriple chart','in a\ntriple chart'),('a proposed compact set','a fixed compact set'),('literally $\\C^3$','$\\C^3$'),('their literal quotient','their quotient')]:
    if a in new:new=p.edit(new,a,b,'D08,D23','cdp:st:C.2.UN.71','Use ordinary mathematical wording after the process qualifier is removed.')
for m in list(re.finditer(r'\\ref\{(cdp:[^{}]+)\}',new)):
    a=m.group(0);b=r'\cref{'+m.group(1)+'}'
    if a in new: new=p.edit(new,a,b,'D04','cdp:st:C.2.UN.71','Use the current statement type and number; all targets remain.')

oldscope='This is a proper local occurrence and central-log-space\nclassification. It does not identify the full analytic\ngerm of an arbitrary given degeneration with this\nchosen quotient, and it makes no compact-base\nglobalization assertion.'
new=p.edit(new,oldscope,'','D02,D11','cdp:st:C.2.UN.71','The statement already specifies the marked central log space and its proper occurrence over a small disc. Its complete local domain and nearby torus formula remain; the repeated exclusion of other conclusions is removed.')
for a,b in [
    ('The integral-affine charts.','Integral-affine charts.'),
    ('The angular lattices inject into the nearby torus.','The angular lattices in the nearby torus.'),
    ('The smooth toric threefold and its exact deck maps.','The toric threefold and its deck maps.'),
    ('Freeness, properness and the compact fibres.','Freeness, properness and compact fibres.'),
]:
    if a in new:new=p.edit(new,a,b,'D08','cdp:st:C.2.UN.71','Use a mathematical proof heading.')
new=p.edit(new,'This proves trivial linear\nholonomy by maps into the given smooth fibre; no\ninvariant-cycle surjectivity is being assumed.',
    'Thus the linear holonomy is trivial, by these injections into the given smooth fibre.',
    'D02','cdp:st:C.2.UN.71','The complete angular lattice and exterior-square argument proves the stated holonomy conclusion directly.')

a=new.index(r'\par\medskip\noindent\textbf{The exact logarithmic gluing comparison.}')
b=new.index(r'\par\medskip\noindent\textbf{The toric threefold and its deck maps.}',a)
oldgluing=new[a:b]
newgluing=r'''\par\medskip\noindent\textbf{Logarithmic gluing.}
Use the exact toric strata just obtained. The divisorial log structure of $(X,S)$ restricted to $S$ has chart $\mathbb N^3$ at a triple point, with base generator $(1,1,1)$, chart $\mathbb N^2$ along an open double curve, and the one-factor chart elsewhere. The equations $xyz=t$ and $xy=t$ make the log morphism smooth everywhere. Its conductor square is the SNC square, its normalization is the disjoint union of the complete toric $V_i$, and it is Gorenstein.

The gluing classification is \cite[version~3, Theorems~4.14, 5.2 and~5.4, pp.~114--116 and~128--134]{GrossSiebert2006I}. We give the comparison for this analytic central space. Identify every normalization stratum with its toric model. A double curve is $\PP^1$ with its two labelled corner points. Its identification between the two components fixes those points, and hence has the form $z\mapsto a z$ with $a\in\C^*$. Thus all closed-stratum identifications are algebraic toric maps.

\item At a triple point, the log chart restricts on each toric affine plane to a monoid map $p\mapsto h_pz^p$, where $h_p$ is an invertible convergent germ and $h_{p+q}=h_ph_q$ whenever the monomials lie on the same component. Take residues at that corner:
\begin{equation}
       p\longmapsto h_pz^p
          \quad\longmapsto\quad
       p\longmapsto h_p(0)z^p.
\hypertarget{tag-0134}{}\label{cdp:eq:C.TG.9}
\end{equation}
Restriction to a shared axis commutes with this residue map. Consequently the constant monomial maps intertwine the same closed gluing diagram. Apply the colimit construction in the proof of \cite[version~3, Theorem~4.14, pp.~114--116]{GrossSiebert2006I} to these maps. Its identity on the labelled strata gives a toric chart $V(\sigma)$ and the chart map to $S$. For the present standard simplex, the local conductor identity is the equality of $\C\{x,y,z\}/(xyz)$ with the triples of functions on its three planes having equal restrictions on their pairwise axes. Thus this chart map is a local analytic isomorphism; the same two-plane identity applies on an edge.

On overlaps the chart maps differ by the constant monomial maps induced by those closed identifications. The resulting finite algebraic atlas and its algebraic \'etale equivalence relation define an algebraic space $S_{\mathrm{alg}}$, together with the displayed analytic isomorphism $S_{\mathrm{alg}}^{\mathrm{an}}\simeq S$. Its normalization is the same finite union of complete toric surfaces. The inverse image of its diagonal under the product normalization map is the union of the component diagonals and the closed graphs of the conductor identifications, so the diagonal is closed. The finite surjective normalization and the completeness of those surfaces then give properness. This establishes the underlying-space hypotheses of the cited theorem through the specified maps.

\item The log section also descends through this comparison. On a double curve $C$, with corner points $p,q$, its smoothing line is
\[
             N_{C/V_i}\otimes N_{C/V_j}\otimes\OO_C(p+q).
\]
Its degree is zero by \eqref{cdp:eq:C.TG.6}. The given smooth-total equation supplies a nowhere-zero section. In a global trivialization of this algebraic degree-zero line on $\PP^1$, that holomorphic section is a nonzero constant. At a triple point the three restrictions have the multiplicative compatibility of \cite[version~3, Theorem~3.22 and Example~3.23(1), pp.~95--97; Example~3.30, p.~106]{GrossSiebert2006I}: in the standard simplex it is exactly equality of their values at the common point. Thus these same constants and identifications define an algebraic section of the log-smooth-structure torsor.

To check that its analytification is the given log structure, use the units quotient in that theorem: the tuples $(h_p)$ are taken modulo multiplicative unit maps, and their edge ratios are the just specified smoothing sections. The kernel calculation and the gluing of units on the coordinate planes work in the convergent local rings by the same conductor identity. Moreover the ghost group is generated by the base class at generic points. A unit homomorphism killing that class is therefore one on a dense open set and hence everywhere on the reduced space. The local isomorphisms consequently glue uniquely. This is the map underlying \cite[version~3, Proposition~3.20 and its proof, pp.~92--94]{GrossSiebert2006I}; its local invertible-Jacobian step here is the holomorphic inverse function theorem on these SNC charts. The algebraic section thus gives $S_{\mathrm{alg}}^\dagger$ with $(S_{\mathrm{alg}}^\dagger)^{\mathrm{an}}\simeq S^\dagger$ over the standard log point.

The hypotheses of \cite[version~3, Definition~4.3, pp.~108--109]{GrossSiebert2006I} now hold with $k=\C$ and empty log-singular set. The affine singular locus is empty, so every local monodromy coefficient is zero; the positivity condition of Definition~1.54, p.~41, and the simplicity condition of Definition~1.60, pp.~45--46, hold with $p=0$. The nowhere-zero smoothing sections are positive log sections as well.

\item Choose the chart changes \eqref{cdp:eq:C.TG.9} so that the values of the log section at each corner are one, as in \cite[version~3, Definitions~4.23--4.24, p.~120]{GrossSiebert2006I}. Its Proposition~4.25, pp.~120--123, gives Condition~(LC) for these open gluing data. Theorems~5.2 and~5.4, pp.~128--134, then identify the marked log space with lifted gluing data for the constant sheaf $N\otimes\C^*=T_N$ on $B$. The chart comparison of Proposition~4.30, pp.~127--128, makes the isomorphisms explicit: a coboundary has
\[
 s'_{\alpha\beta}=a_\alpha^{-1}s_{\alpha\beta}a_\beta,
\]
and the map on the chart indexed by $\alpha$ is its torus multiplication by $a_\alpha$. The pullback log section is normalized; uniqueness in Theorem~5.2 identifies it with the same section. These are therefore isomorphisms of the marked central log spaces, including their given log structures.

On the contractible universal cover $N_{\R}$, path products trivialize this constant-sheaf cocycle. Changing a path by a deck element records its holonomy, so
\begin{equation}
 H^1(B,N\otimes\C^*)
       =\operatorname{Hom}(\Gamma,T_N).
\hypertarget{tag-012R}{}\label{cdp:eq:C.TG.10}
\end{equation}
The two commuting deck holonomies are exactly the marked values of \eqref{cdp:eq:C.TG.1}.

'''
new=new[:a]+newgluing+new[b:]
p.record('D12,D17,D18,D20,D25','cdp:st:C.2.UN.71',oldgluing,newgluing,
    'After opening the complete exact v3 theorem proofs, use the cited gluing classification and retain its needed analytic conductor/monoid comparison. Explicitly normalize the given log section before applying Condition LC and the lifted-gluing theorem; identify the same section by its unit quotient and the reduced-space kernel. This supplies the exact source-domain/application map without changing any theorem conclusion.')

for oldcitation,newcitation in [
    (r'\cite[Theorems 4.14, 5.2 and 5.4]{GrossSiebert2006I}',r'\cite[version~3, Theorems~4.14, 5.2 and~5.4, pp.~114--116 and~128--134]{GrossSiebert2006I}'),
    (r'\cite[Example 3.30 and Theorem 3.22]{GrossSiebert2006I}',r'\cite[version~3, Theorem~3.22, pp.~95--97, and Example~3.30, p.~106]{GrossSiebert2006I}'),
]:
    if oldcitation in new:new=p.edit(new,oldcitation,newcitation,'D18','cdp:st:C.2.UN.71','Name the exact opened arXiv v3 and its printed PDF pages. The existing journal metadata remains distinct in the bibliography.')

header=r'\subsection{Toric central log spaces}\label{subsec:II:toric-central-log-spaces}'
unit_clause=r'''The construction also permits a holomorphic family of homomorphisms $\lambda\mapsto c_\lambda(t)$ from $\Gamma$ to $T_N$, defined on a disc and satisfying $c_\lambda(0)=c_\lambda$. It gives the same marked central log space, smooth proper torus fibres over the puncture and a nowhere-zero canonical form. In \eqref{cdp:eq:C.TG.2}, its period matrix is obtained by replacing $C$ with a holomorphic matrix $C(t)$ of logarithms of the two values $c_{Qe_j}(t)$. The constant family gives the preceding occurrence.'''
new=p.edit(new,'The central Euler number is $2[N:\\Gamma]$.','The central Euler number is $2[N:\\Gamma]$.\n\n'+unit_clause,
 'D12,D20','cdp:st:C.2.UN.71','Transfer the full holomorphic-unit extension already proved in UN73 to the single earlier cone construction. Its fixed-constant occurrence and central classification remain as the explicit constant specialization.')
start=new.index(r'\par\medskip\noindent\textbf{The toric threefold and its deck maps.}')
fixed=new[start:]
variable=fixed.replace(r'\textbf{The toric threefold and its deck maps.}',r'''\textbf{The toric threefold and its deck maps.}
For the construction take the holomorphic homomorphism $c(t)$ of the statement. All maps below keep the base coordinate $t$ fixed; their restrictions at zero use exactly $c(0)=c$.''')
variable=variable.replace(r'g_\lambda(z,t)=(c_\lambda t^\lambda z,t)',r'g_\lambda(z,t)=(c_\lambda(t)t^\lambda z,t)')
variable=variable.replace('Multiply this map by\n$c_\\lambda$ on the torus factor.','Multiply this map by\n$c_\\lambda(t)$ on the torus factor.')
variable=variable.replace('The $c_\\lambda$ are a homomorphism, and\nconstant torus multiplication commutes with\nthe shears.',
 'For each $t$, the values $c_\\lambda(t)$ are a homomorphism in $\\lambda$. Their torus multiplications commute with the shears, since they depend only on the fixed base coordinate.')
variable=variable.replace(r'''Extend the homomorphism
$\lambda\mapsto\log|c_\lambda|$ real-linearly
to a map $K:N_{\R}\to N_{\R}$.''',r'''For each $t$, extend $\lambda\mapsto\log|c_\lambda(t)|$ real-linearly to $K(t):N_{\R}\to N_{\R}$. The two generator values are holomorphic and nowhere zero on a smaller closed disc, so $K(t)$ is uniformly bounded there.''')
variable=variable.replace('I+K/L','I+K(t)/L')
variable=variable.replace('Taking logarithms gives exactly \\eqref{cdp:eq:C.TG.2},\nwhose four real periods are independent\nbecause $LQ+\\operatorname{Re}C$ is invertible.',
 'Taking holomorphic logarithms of the two generator values gives \\eqref{cdp:eq:C.TG.2} with $C$ replaced by $C(t)$. Its four real periods are independent because $LQ+\\operatorname{Re}C(t)$ is invertible by this same bound. For constant $c$, choose $C(t)=C$.')
variable=variable.replace('because all\nadditional terms are multiples of $dt$.','because every additional term, including $d\\log c_\\lambda(t)$, is a multiple of $dt$.')
assert variable!=fixed
new=new[:start]+variable
p.record('D12,D20,D22','cdp:st:C.2.UN.71',fixed,variable,
 'The full occurrence proof now treats holomorphic c(t) once: exact shears, group law, uniformly bounded K(t), real periods C(t), compact barycentric representatives and invariant dt-wedge. The old c is the constant-family specialization; its central data and all fifteen targets remain.')
new=p.edit(new,'The exact central-space comparison and\n\\cref{cdp:st:C.2.UN.68} give its Euler number and complete\nboth the occurrence and exhaustion\nassertions in the stated local scope.',
 'The exact central-space comparison and \\cref{cdp:st:C.2.UN.68} give the Euler number $2[N:\\Gamma]$.',
 'D08','cdp:st:C.2.UN.71','Replace the proof recap by its direct Euler conclusion, retaining the substantive central-space comparison.')
p.guard('Complete UN71 central log classification',old,header+'\n\n'+new.rstrip(),'Complete old/receiving comparison; retain fixed-constant conclusions and the exact stronger holomorphic-unit construction transferred from UN73, with all15 equation labels/targets.')

old73=block(main,'cdp:st:C.2.UN.73')
assert (OUT/'S6_SERIES_PUBLISH_II_sec11_toric_log_UN73_input.tex').read_text().rstrip()==old73
new73=p.clean(old73,'cdp:st:C.2.UN.73')
for m in list(re.finditer(r'\\ref\{(cdp:[^{}]+)\}',new73)):
 a=m.group(0);b=r'\cref{'+m.group(1)+'}'
 if a in new73:new73=p.edit(new73,a,b,'D04','cdp:st:C.2.UN.73','Use statement-type navigation to the unchanged current owner.')
scope73='The assertion preserves\nthe specified central log spaces; it does not assert\nthat an arbitrary given full degeneration germ is\nthe germ of this compact construction.'
new73=p.edit(new73,scope73,'','D02,D11','cdp:st:C.2.UN.73','The complete marked-central-log-space scope, two full fibres and explicit base coordinates are stated positively; the repeated disclaimer is removed.')
new73=p.edit(new73,'This changes only a recorded base scale; the\ncoordinate maps undo it at both ends.\nWe do not commute this imaginary shift through\nthe real-linear operation used next.',
 'The base-coordinate maps below undo this scale at both ends. The periods apply the real-linear map to the fixed shifted vectors $b\'_j$; their logarithmic coefficients multiply outside that map.',
 'D02,D08,D20','cdp:st:C.2.UN.73','Keep the precise shifted-vector convention positively, including the fact that the complex logarithmic coefficient stays outside the real-linear map.')
new73=p.edit(new73,'This is holomorphic in $t$ for every fixed $w$.','This is the map $V_{t^k}$ of \\cref{lem:II:logarithmic-period-family}, and is holomorphic in $t$ for every fixed $w$.',
 'D12,D20','cdp:st:C.2.UN.73','Identify the same anti-linear coordinate construction by the explicit base substitution z=t^k; retain the full rank-two logarithmic period calculation here.')
new73=p.edit(new73,'This is an equality of holomorphic\nmaps, not a replacement of its limiting\nconstant by a numerical invariant.','',
 'D02','cdp:st:C.2.UN.73','The displayed exact identity and c-valued central specialization already state the mathematical result.')
a=new73.index(r'\item Apply the cone-chart construction of')
b=new73.index(r'\par\medskip\noindent\textbf{The exact conjugate filling at infinity.}',a)
oldfill=new73[a:b]
newfill=r'''\item Apply the holomorphic-unit construction of \cref{cdp:st:C.2.UN.71} with base $u$, the same $(N,\Gamma,\mathscr P)$ and $c_\lambda(u)=d^0_\lambda(u)$ from \eqref{cdp:eq:C.TX.10}. The values are holomorphic and nowhere zero, their multiplicative extension is a homomorphism in $\lambda$, and $d^0_\lambda(0)=c_\lambda$. The resulting full reduced SNC filling is smooth and proper. Equation \eqref{cdp:eq:C.TX.8} divides by exactly its angular lattice, and \eqref{cdp:eq:C.TX.9} identifies its remaining deck maps with the middle period family. It therefore gives the punctured-family biholomorphism, while \eqref{cdp:eq:C.TX.10} identifies the marked central log space in the coordinate $u$ with the prescribed one.

'''
new73=new73[:a]+newfill+new73[b:]
p.record('D12,D20','cdp:st:C.2.UN.73',oldfill,newfill,'The full variable-unit cone proof is now stated and proved once at UN71. Apply it through exactly u=κt, d⁰λ(u)=κ^−λc⁰λ(u/κ), and the unchanged exponential/deck maps; no limiting-only comparison is substituted.')
oldinf=r'''Use the same integral fan $\Sigma$ and
its variable-constant cone quotient
at this end. All its monomial chart
maps are defined over $\Z$, while its
central torus gluing constants are
the complex conjugates of the given
ones. Hence its marked central log
space is exactly the conjugate of
the prescribed one, with the stated
local base coordinate.'''
newinf=r'''Apply the same holomorphic-unit clause of \cref{cdp:st:C.2.UN.71}, now with base $v$ and homomorphism $d^\infty(v)$. Its value at zero is $\overline c$. The fan and its monomial chart maps are defined over $\Z$, so complex conjugation changes precisely these gluing constants and the log section. This is the conjugate marked central log space in the stated coordinate $v$.'''
new73=p.edit(new73,oldinf,newinf,'D12,D20','cdp:st:C.2.UN.73','Apply the identical earlier owner to the full explicit infinity homomorphism after the generator reversal and base rescaling; the integral monomial atlas identifies the conjugate central log section.')
a=new73.index(r'\item In both end fillings the form')
b=new73.index('Thus both end neighbourhoods',a)
oldvol=new73[a:b]
newvol=r'''\item The canonical form in the holomorphic-unit construction of \cref{cdp:st:C.2.UN.71} is $du\wedge d\log z_1\wedge d\log z_2$ at zero, and $dv\wedge d\log(z_\infty)_1\wedge d\log(z_\infty)_2$ at infinity. Under the two exponential identifications these are the forms on the same end fillings just constructed. That proposition proves their invariance for the homomorphisms $d^0(u)$ and $d^\infty(v)$ and their nowhere-zero extension in every unimodular cone chart.
'''
new73=new73[:a]+newvol+new73[b:]
p.record('D12,D20','cdp:st:C.2.UN.73',oldvol,newvol,'Apply the common invariant form to the same two holomorphic-unit actions and retain both displayed differentials and their exact end coordinates.')
for a,b in [
 ('The exact initial periods and a positive symmetric part.','Initial periods and a positive symmetric part.'),
 ('The exact chart and prescribed log section at zero.','The chart and log section at zero.'),
 ('The exact conjugate filling at infinity.','The conjugate filling at infinity.'),
 ('they are literal holomorphic coordinates','they are holomorphic coordinates'),
 ]:
 if a in new73:new73=p.edit(new73,a,b,'D08','cdp:st:C.2.UN.73','Use mathematical wording; all period generators, sign reversals and base-coordinate inverses remain.')
new73=p.edit(new73,'This completes the compact\noccurrence construction.','',
 'D08','cdp:st:C.2.UN.73','Remove the final pure recap sentence; the complete compact occurrence and Euler proof immediately preceding it remains.')
header73=r'\subsection{Compact occurrence of toric fibres}\label{subsec:II:compact-toric-occurrence}'
p.guard('Complete UN73 compact occurrence',old73,header73+'\n\n'+new73.rstrip(),'Complete old/receiving proof comparison, with the same full two-end log markings and all14 TX displays, including the unchanged WF18 alias. Its variable-unit filling is the exact earlier UN71 application.')
p.record('D13,D14','cdp:st:C.2.UN.71','UN71 and UN73 follow UN69 within the same unresolved section.',header+'\n'+header73,'Give the complete central-log classification and its complete compact-occurrence consumer separate descriptive actual subsections, with the common holomorphic-unit construction first.')

old76=block(main,'cdp:st:C.2.UN.76')
assert (OUT/'S6_SERIES_PUBLISH_II_sec11_toric_log_UN76_input.tex').read_text().rstrip()==old76
new76=old76
oldapp=r'''preserved.  Apply the variable-unit toric chart
construction of \cref{cdp:st:C.2.UN.73}, first with the subdivision
and then with its proper coarsening.  The monomial
maps \eqref{cdp:eq:C.WF.22} extend to both atlases and commute
with the coarsening morphism.'''
newapp=r'''preserved. Apply the holomorphic-unit construction of \cref{cdp:st:C.2.UN.71} to the subdivided fan with base $u$ and the period homomorphism $d_\gamma(u)=\kappa^{-\gamma}c^0_\gamma(u/\kappa)$ determined by \eqref{cdp:eq:C.WF.21}. Its value at zero is the same $c_\gamma$. Descend this filling through the marked proper toric coarsening, using the identical units on both atlases. The monomial maps \eqref{cdp:eq:C.WF.22} extend to both and commute with that coarsening morphism.'''
new76=p.edit(new76,oldapp,newapp,'D12,D20','cdp:st:C.2.UN.76','Use the single earlier holomorphic-unit filling with the exact WF21 exponential holonomies and u=κs; keep the same marked proper coarsening and finite monomial action. All full-fibre exponents and invariant-ring maps remain.')
oldapp2=r'''on every compact annulus.  The bounded-unit
toric filling argument of \cref{cdp:st:C.2.UN.73} gives proper
fillings at both ends.  A toric coarsening has'''
newapp2=r'''on every compact annulus. The holomorphic-unit clause of \cref{cdp:st:C.2.UN.71}, applied to the period homomorphisms from \eqref{cdp:eq:C.WF.21} and \eqref{cdp:eq:C.WF.23} after the displayed base rescalings, gives the proper fillings on $\mathscr P$ and its reflected fan. The torus inversion already specified identifies the latter with the conjugate marked data. A toric coarsening has'''
new76=p.edit(new76,oldapp2,newapp2,'D12,D20','cdp:st:C.2.UN.76','The same exact two homomorphisms and reflected/inverted fan comparison supply the proper fillings. The subsequent coarse quotient, finite stabilizer averaging and multiplicity proof are unchanged.')
p.guard('UN76 exact holomorphic-unit owner applications',old76,new76,'Complete original/current and receiving proof comparison required for this bounded two-paragraph transfer. Statement, all equations and every other proof paragraph are byte-identical.')
(OUT/'S6_SERIES_PUBLISH_II_sec11_toric_log_UN71.tex').write_text(header+'\n\n'+new,newline='\n')
(OUT/'S6_SERIES_PUBLISH_II_sec11_toric_log_UN73.tex').write_text(header73+'\n\n'+new73,newline='\n')
(OUT/'S6_SERIES_PUBLISH_II_sec11_toric_log_UN76_receiving.tex').write_text(new76+'\n',newline='\n')

entry_start=main.index(r'\bibitem[Gross and Siebert(2006)]{GrossSiebert2006I}')
entry_end=main.index(r'\bibitem',entry_start+10)
oldentry=main[entry_start:entry_end]
oldurl=r'\newblock URL \url{https://arxiv.org/pdf/math/0309070}.'
newurl=r'''\newblock \doi{10.4310/jdg/1143593211}.

\newblock Cited version: \emph{arXiv:math/0309070v3}, 20 July 2005; page locators refer to the printed pagination of that PDF.

\newblock URL \url{https://arxiv.org/abs/math/0309070v3}.'''
assert oldentry.count(oldurl)==1
newentry=oldentry.replace(oldurl,newurl)
p.guard('Exact Gross-Siebert cited version',oldentry,newentry,'Retain the2006 journal metadata and name the exact v3 used by all UN71 locators; do not substitute journal pagination for the opened PDF.')
p.record('D18','GrossSiebert2006I',oldentry,newentry,'Fresh exact v3 PDF opening established the full source locators. Its title gives20July2005; the served PDF has167printed pages, although the abstract comment says144. The bibliography names the version without repeating that stale page-count comment. The author publication page and publisher-deposited DOI metadata verify10.4310/jdg/1143593211 and the retained2006 journal volume/issue/pages.')

p.write(header+'\n\n'+new+'\n'+header73+'\n\n'+new73)
state=main
for g in p.guards:
    assert state.count(g['old'])==1,g['key']
    state=state.replace(g['old'],g['new'],1)
for pat in [r'\\label\{([^{}]+)\}',r'\\hypertarget\{([^{}]+)\}']:
    a=Counter(re.findall(pat,old+old73+old76));b=Counter(re.findall(pat,new+new73+new76))
    assert a==b,(a-b,b-a)
for body in re.findall(r'\\begin\{equation\}([\s\S]*?)\\end\{equation\}',new+new73+new76):
    assert not re.search(r'\n[ \t]*\n',body)
    assert body.count(r'\SsixEquationAliases')<=1
assert old76.split(r'\end{proposition}',1)[0]==new76.split(r'\end{proposition}',1)[0]
print('Four bounded guards replay; complete old identifiers unchanged; UN76 statement byte-identical; complete receiving proof comparisons recorded by the companion log generator.')
