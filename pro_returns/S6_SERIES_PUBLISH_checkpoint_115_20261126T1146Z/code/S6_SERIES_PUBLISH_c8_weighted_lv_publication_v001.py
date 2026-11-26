"""Whole-read weighted OS45 publication edit, preserving every permanent identity."""
import csv
from datetime import datetime, timezone
import difflib
import hashlib
from pathlib import Path
import re
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation
import S6_SERIES_PUBLISH_c8_integrate_units as units
root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
p=root/'agents/continuation8_iii_integration/units/weighted/weighted_os45.tex'
original=p.read_text();text=original
assert hashlib.sha256(p.read_bytes()).hexdigest()=='3c6510b005b92d3cb1ab7800a1fcce613fb67d69d8e8e6cac16bcd4a77fd61c8'
receiver=(root/'agents/continuation8_iii_lv/S6_SERIES_PUBLISH_III_02LV_receiving.tex').read_text()
assert [s for s in original.splitlines() if s.strip()]==[s for s in receiver.splitlines() if s.strip()]
print('REPAIRED_INPUT_VS_RECEIVER_DIFF')
print(''.join(difflib.unified_diff(receiver.splitlines(True),original.splitlines(True),fromfile='admitted1365',tofile='repaired1365')),end='')
edits=[]
def change(old,new,kinds,why,count=1):
 global text
 assert text.count(old)==count,(old[:180],text.count(old),count)
 for _ in range(count):
  at=text.index(old);edits.append((kinds,text.count('\n',0,at)+1,old,new,why))
  text=text[:at]+new+text[at+len(old):]
def between(start,stop):
 at=text.index(start);return text[at:text.index(stop,at)]
def eqblock(label):
 at=text.index('\\label{'+label+'}')
 a=text.rfind('\\[',0,at);b=text.index('\\]',at)+2
 return text[a:b]

# The exact datum is stated once, at its existing permanent equation.
datum=eqblock('maps:eq:D.PC3')
intro=between(r'\begin{theorem}',r'\[')
definition=r'''\subsection{The weighted OS45 manifold}

\begin{definition}[Weighted OS45 data]\hypertarget{tag-Q251}{}\label{maps:def:weighted-os45-data}
{\normalfont\scriptsize tag Q251}\par
Use the OS45 base profile and its ordered markings in
Definition~\ref{mapsIII:def:elliptic-marked-data}, with generator $G$,
initial sections and whole-fibre weights
'''+datum.replace(r'\mathrm{OS45/default}',r'\mathrm{OS45/base}')+r'''
The weight two is supported at the $I_8$ site. Fill all multiplicative
sites by the prescribed Mumford caps and use the ordinary clutch $e=1$.
Write $X$ for this marked member with its complex orientation.
These are the \emph{weighted OS45 data}.
\end{definition}

\begin{theorem}[Invariants of the weighted OS45 manifold]\hypertarget{tag-02LV}{}\label{maps:src:D.2.53}
{\normalfont\scriptsize tag 02LV}\par
The manifold $X$ of Definition~\ref{maps:def:weighted-os45-data}
is simply connected and has
'''
change(intro,definition,'D04;D05;D10;D12;D13;D14;D16;D26',
       'Give the same actual OS45 base profile, initial sections, ordered weight vector, prescribed caps and ordinary clutch in Q251. Preserve D.PC3 at this retained identity and every construction choice.')
old=between(r'\item  Now take the exact marked data',r'\ref{maps:src:D.2.46} gives')
change(old,r'''\item \emph{The marked returns and period lattice.}
For the data of Definition~\ref{maps:def:weighted-os45-data},
''','D12;D13;D14',
       'Cite the single numbered input definition; D.PC3 is retained there with unchanged mathematical data and its existing anchors.')
change(r'''Together with the displayed primitive cubic and the complete
fundamental-class coordinates, this gives the full invariant package
for this marked weighted OS45 member.''',r'''Here $P_{\mathrm{ref}}\in H_2(X;\mathbb Z)$ is the refined class.
The cap-product map $\mathcal D_X:H^4(X;\mathbb Z)\to H_2(X;\mathbb Z)$,
$c\mapsto c\frown[X]$, has inverse Poincar\'e duality.
The primitive cubic and the finite coordinates above determine the
complete fundamental-class invariant of this marked member.''',
       'D08;D20;D22','Declare the actual homological refined class and cap-product isomorphism/inverse; replace workflow package wording by the precise complete invariant statement.')
change(r'\begin{proof}\leavevmode\par',r'\begin{proof}','D10;D23','Use the standard proof opening.')
change(r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=0pt,labelsep=.5em]',
       r'\begin{enumerate}[leftmargin=*]','D10;D23','Replace machine hierarchy markers by ordinary proof-stage numbering.')
change(r'\begin{enumerate}[label={$\langle2\rangle$\arabic*.},leftmargin=1.3em,labelsep=.5em]',
       r'\begin{enumerate}[label=(\alph*),leftmargin=*]','D10;D23','Give the component-lattice subproof ordinary alphabetic numbering.')
change(r'\begin{enumerate}'+'\n'+r'\item \emph{The source line',
       r'\begin{enumerate}[label=(\alph*),leftmargin=*]'+'\n'+r'\item \emph{The source line','D10;D23','Use the same alphabetic style for the source-sphere subproof.')
for old,new in [
 ('The primitive component lattice and cubic in the sixteen-component OS45 example','The primitive lattice, cubic and critical cycle'),
 ('The actual torsion coordinate and complete fundamental-class\ninvariant of the sixteen-component OS45 manifold','The cyclic coordinate and component evaluations'),
 ('The remaining finite-coefficient evaluations for OS45','The finite-coefficient evaluations'),
 ('The source sphere and refined characteristic class','The source sphere and refined class')]:
 change('\\textbf{'+old+'}','\\emph{'+new+'}','D08;D13;D16','Use a concise mathematical proof-stage title without internal comparison language.')
change(r'\hypertarget{tag-03LK}{}\label{maps:proof:D.OS.refined}',
       r'\hypertarget{tag-03LK}{}\label{maps:proof:D.OS.refined}'+'\n'+r'{\normalfont\scriptsize tag 03LK}\par',
       'D10','Keep the permanent refined-proof anchor at its complete subproof and display its small tag.')
for title in ['Integral vanishing of the critical class.','The specified core cochain.','A full boundary comparison for finite-coefficient supports.','Extension through the other caps.','The complete coordinate values.']:
 change('\\paragraph{'+title+'}','\\medskip\\noindent\\emph{'+title+'}',
        'D13;D23','Keep this mathematical stage within the single proof rather than creating an unnumbered document-level paragraph unit.')

# Actual lattice and component-coordinate inverses.
change(r'''This is an equality of sublattices, not merely a comparison of
indices. The determinant is sixteen and the Smith factors are two
and eight.''',r'''The equality of sublattices follows from the exact factorization
\[
 \begin{pmatrix}8&24\\-6&-16\end{pmatrix}
 =\operatorname{diag}(8,2)T_{\rm per},\qquad
 T_{\rm per}=\begin{pmatrix}1&3\\-3&-8\end{pmatrix},\quad
 T_{\rm per}^{-1}=\begin{pmatrix}-8&-3\\3&1\end{pmatrix}.
\]
Both products of the last two matrices are identity. The two
resulting long periods are $-8e_2+3\gamma$ and $-3e_2+\gamma$.
The determinant is sixteen and the Smith factors are two and eight.''',
       'D02;D20;D22','Print the exact period-coordinate map and inverse already admitted in the complete comparison; prove the lattice equality rather than invoking the common index alone.')
change(r'''These are the asserted primitive markings.''',r'''Equivalently, the relative kernel consists of integer vectors $n$
with $\sum n_i=0$ and $\sum_{i\ {\rm odd}}n_i$ even.
Its basis consists of $e_i-e_{14}$ for even $i<14$,
$e_i-e_{15}$ for odd $i<14$, and $2e_{15}-2e_{14}$.
The inverse reads $n_0,\ldots,n_{13}$ and half the odd-coordinate
sum. Dual evaluation gives exactly \eqref{maps:eq:D.PC10}.''',
       'D20;D22','Give the full primitive-kernel basis and inverse, not just the Smith index; these are the exact admitted comparison coordinates.')
change(r'''in the ray order of \ref{maps:src:D.2.47}. The four nonhorizontal boundary classes''',r'''on the ordered rays
$(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)$
of \ref{maps:src:D.2.47}. The four nonhorizontal boundary classes''',
       'D20;D22','State the actual six ordered rays used by every subsequent wall and Picard formula.')
change(r'''Its torsion value is the unit \(-1\), unchanged from \eqref{maps:eq:D.OF2};
we choose the opposite torsion generator to normalize it to one.
Choose free lifts of the homology basis dual to \eqref{maps:eq:D.PC10}
which are annihilated by \(u\). This fixes the splitting''',r'''It has $u(g)=-1$ for $g=-[e_1\wedge e_2]$.
Put $\tau=-g=[e_1\wedge e_2]$; negation is its own inverse,
and $u(\tau)=1$. Let $h_i$ be free lifts dual to the fifteen
classes in \eqref{maps:eq:D.PC10}. Send the $i$th free basis vector
to $h_i-u(h_i)\tau$ and $1\bmod8$ to $\tau$.
Changing an integer representative of $u(h_i)$ changes this image
by $8\tau=0$. The inverse reads the fifteen integral evaluations
and then $u$. Both composites are identity, giving the splitting''',
       'D20;D22','Replace unproved normalization wording by the exact cyclic negation and full free/cyclic marking with inverse, retaining the actual class u and area value+1.')

# Distinguish the ambient graph row and the kernel embedding from boundary angles.
old=between(r'\medskip\noindent\emph{The specified core cochain.}',r'\medskip\noindent\emph{A full boundary comparison')
new=old.replace(r'K=\ker_{\mathbb Z}D',r'\mathcal K=\ker_{\mathbb Z}D')
new=new.replace('Take the integral cycle embedding $K$ and its integral left inverse',
                'Let $K:\\mathbb Z^{17}\\to\\mathbb Z^{20}$ be the integral basis embedding of $\\mathcal K$, with integral left inverse')
new=new.replace(r'\theta',r'\theta_{\rm gr}')
new=new.replace('r={}&',r'r_{\rm gr}={}&').replace(r'+8r,',r'+8r_{\rm gr},').replace(r'\(8r\)',r'\(8r_{\rm gr}\)')
change(old,new,'D20','Distinguish the graph cochain and correction row from the positive boundary angle and component index; identify the cycle lattice separately from its exact basis embedding. Coordinates are unchanged.')

# Consolidate duplicated displayed identities by retaining both old aliases at the same formula.
for source,target in [('maps:eq:D.OL1','maps:eq:D.OF1'),('maps:eq:D.OL2','maps:eq:D.OF11'),('maps:eq:D.OL3','maps:eq:D.OF18'),('maps:eq:D.OL12','maps:eq:D.OF16')]:
 block=eqblock(source)
 anchors=''.join(re.findall(r'\\hypertarget\{[^}]+\}\{\}|\\label\{[^}]+\}',block))
 assert anchors and anchors.count('\\label')==1
 change(block,'','D12;D19','The entire displayed identity is already proved and retained at '+target+'; move the existing permanent aliases to that same mathematical identity.')
 dest=eqblock(target)
 change(dest,dest[:-2]+anchors+'\n'+dest[-2:],'D10;D12;D19','Retain the exact old '+source+' label/hypertarget multiplicity as an alias of the same retained formula, with no changed scope or deleted identity.')
old=between(r'\item \emph{The finite-coefficient evaluations}', 'The scalar circle action is semifree.')
new=r'''\item \emph{The finite-coefficient evaluations.}
Use the global class $u$ and the entire boundary comparison just proved,
with support \eqref{maps:eq:D.OF1} and affine differences
\eqref{maps:eq:D.OF11}. Both differences have zero slope in the
scalar $s$ direction. Let $y$ be the primitive class in
\eqref{maps:eq:D.PC9}. It remains to prove the last three evaluations
in \eqref{maps:eq:D.OF18}, including the full order-sixteen value.

'''
change(old,new,'D02;D08;D12;D13','Cite the retained support, affine cocycle and full evaluations once after their permanent aliases are moved; preserve the complete coefficient-extension input and the unresolved full-modulus conclusions to be proved next.')
old=between('The same support gives all component mixed evaluations.','In particular \\(y^2=0\\) integrally.')
new=r'''The component restrictions in \eqref{maps:eq:D.OF16} and their
Cartier pairings give \eqref{maps:eq:D.OF17}; the preceding localization
completes \eqref{maps:eq:D.OF18} in its full coefficient groups.

'''
change(old,new,'D12;D14','Remove the second copy of the same component-square/mixed calculation after retaining D.OL12 at D.OF16. All16 component values, including the two omitted components and four mixed exceptions, remain in the first calculation.')
change(r'''Opposite wall restrictions agree modulo eight. Changes of integral
representative by eight times a class preserve its square modulo
sixteen. The six wall differences specify every component restriction and its
integral lift; changing a lift by $8z$ changes its square by''',r'''Opposite wall restrictions agree modulo eight. The six wall differences
specify every component restriction and its integral lift. Changing
a lift by $8z$ changes its square by''','D12;D23','State the full integral-lift independence once, retaining its exact16/64 polynomial and all component values.')

# Explicit character twists and coefficient-ring inverse.
change(r'''The existence of integral fixed-point weights forces $c$ odd;
changing the lift of $y$ changes $c$ by an even integer. Normalize
$c=-1$. Then''',r'''The existence of integral fixed-point weights forces $c$ odd.
Replace $\widehat y$ by $\widehat y-(c+1)t/2$; this is integral,
and its inverse adds $(c+1)t/2$. It sends $c$ to $-1$ and leaves
the ordinary class $y$ fixed. The resulting weights are''',
       'D20;D22','Give the exact integral character twist and its inverse instead of a normalization assertion; preserve the canonical component weights and all possible lifts.')
change(r'''Each connecting orbit curve has scalar tangent weight $1$ or $-1$.''',r'''Subtracting $Lt$ from $\widehat u$, with inverse addition,
chooses the displayed characters without changing $u$.
Each connecting orbit curve has scalar tangent weight $1$ or $-1$.''',
       'D20;D22','Give the global finite-coefficient character twist and its inverse, after the connected orbit graph proves the shift is common.')
change(r'''complement of the fixed locus is free and all normal weights are
units. Taking the coefficient of $x$ after division by $-t^2$ gives''',r'''complement of the fixed locus is free and all normal weights are
units. The inverse of restriction after inverting $t$ is
$\sum i_{r,s*}(z_{r,s}/(-t^2))$, by the normal Thom formula;
the free complement is killed by a power of $t$.
Taking the coefficient of $x$ gives''','D22',
       'Retain the finite-ring localization proof and write its actual Thom inverse, with the already proved free complement and primitive normal weights.')

# Carry the earlier complete LP target through the actual marking.
change(r'''Finally \ref{maps:src:D.2.48}'s primary coefficient-group calculation and
the integral Kunneth decomposition give''',r'''Apply the complete primary calculation of \ref{maps:src:D.2.48}
with $r=15$ and $d=8$. Its $D_2=16$ and $D_3=8$, and
its positive cyclic generator is carried to $\tau$ by the splitting
\eqref{maps:eq:D.OF15}, with the evaluation inverse given there.
The integral K\"unneth decomposition therefore gives''',
       'D06;D20;D22','Match the entire LP coefficient-target proof to the actual rank15/order8 marking, including the full moduli and cyclic-generator inverse.')
change(r'''last by \(u^3\). Hence this determines the complete
fundamental-class invariant \(\mu\), not merely its image
under ordinary triple cup products.''',r'''last by \(u^3\). More explicitly, write $e_0,\ldots,e_{14}$ for
the marked free generators, dual to $x_0,\ldots,x_{13},y$, and
write $g_8$ for $1\bmod8$. The classifying map for the inverse
homology marking takes values in $K(\mathbb Z^{15}\oplus\mathbb Z/8,2)$.
The inverse coordinate map sends $(T_\alpha,J_\beta,K_i,L)$ to
\[
 \sum_{|\alpha|=3}T_\alpha\gamma_\alpha(e)
 +\sum_{|\beta|=2}J_\beta\gamma_\beta(e)g_8
 +\sum_{i=0}^{14}K_i e_i\gamma_2(g_8)+L\gamma_3(g_8).
\]
The forward map is the four displayed detector families, whose
pairings with this cross-product basis are identity. Here $T$ is
the primitive cubic, $J$ is \eqref{maps:eq:D.OF17},
$(K_0,\ldots,K_{14})=(7,\ldots,7,0)$ in $(\mathbb Z/16)^{15}$,
and $L=0$. This gives the complete $\mu$ and both coordinate maps.''',
       'D20;D22;D27','Write the exact full H6 cross-basis reconstruction and its four inverse detectors through the already established homology marking; no classification or coefficient scope is weakened.')

# Replace source-array indices by the same geometric prism and cap maps.
change(r'''In the actual full core matrix, its
exterior null witness is column9, and the positive-cap
fixed-exterior relation is column36 with coefficient minus one
(the saved arrays use zero-based indices).
These are the two explicit images of the same marked class.''',r'''The prism $T_1(e_2\wedge\delta)$ in the finite-filled exterior
has boundary $\alpha$ by the second displayed equality.
At the weighted cusp the fixed lattice is
$\mathbb Ze_1\oplus\mathbb Z\delta$. In the order $(\delta,e_1)$,
its exterior generator is $-\alpha$. The angular-area sweep in
\eqref{maps:eq:D.OF5}, projected from the common cover, bounds this
fixed torus in the cusp; reversing that chain bounds $\alpha$.
The maps read the two marked angular coordinates and the radial
sweep coordinate, with the inverse parametrizations of
\ref{maps:src:D.2.43}. Thus the exterior and cusp images of this
same boundary class are both zero with their explicit chains.''',
       'D09;D20;D22','Replace saved-array positions9/36 by their exact I1 monodromy prism and oriented cusp fixed-area sweep, using the same negative fixed-exterior generator and the complete admitted cap map/inverse.')

# Keep finite u distinct from the integral Borel character.
old=between(r'\item \emph{The integral equivariant characteristic class.}',r'\item \emph{The Borel pair')
new=re.sub(r'(?<![A-Za-z])u(?![A-Za-z])','t',old)
new=new.replace('Put $t=c_1', 'Use $t=c_1')
change(old,new,'D20','Use t consistently for the integral circle character through OR11/OR12; the finite class u, all weights and the actual circle generator are unchanged. The symbol transport is identity on H2(BS1;Z).')
old=r''' \ell(N,C)=\langle a_C,[N]\rangle
 =\langle b,[\Sigma]\rangle=-1.
'''
new=old+r''' \tag{Q252}\hypertarget{tag-Q252}{}\label{maps:eq:weighted-os45-total-link}
'''
change(old,new,'D10;D19','Give the already proved exact integral critical link its reserved Q252 permanent equation identity for the final reference.')
change(r'''The reference parity is odd by step~3 and the total link is odd by
step~6.  The integral relative transgression giving
\eqref{maps:eq:D.WI13} applies to this genuinely embedded torsion sphere:
its proof uses the same unit Thom residues and an admissible sphere
frame.''',r'''The reference parity is one by the Bott degree-four calculation
\eqref{maps:eq:D.OR10}, and the total link is $-1$ by
\eqref{maps:eq:weighted-os45-total-link}. Apply the integral relative
transgression \eqref{maps:eq:D.WI13} to this embedded sphere $N$,
the differential reference $\rho$ and the complete chain $B_C$.
These are the same type of input as in that formula: the Bott residues
are the positive unit, the admissible sphere frame is the one specified
there, and the coefficient map is
$\mathcal D_X:c\mapsto c\frown[X]$, with its declared inverse.
The substitution is identity on this sphere, frame and chain.''',
       'D06;D20;D22;D26','Replace fragile local step numbers by exact permanent identities and match the complete relative transgression input, including its actual frame, chain, unit residue and cap-product convention.')
change(r'\operatorname{lk}(N,\operatorname{PD}P_{\rm ref})',r'\operatorname{lk}(N,P_{\rm ref})','D20',
       'Use linking on H3-by-H2 under the declared cap-product map, consistently with the preceding LP proof and its inverse identification.')
change(r'Also $2P_{\rm ref}=\lambda=0$ kills the',r'Also $2P_{\rm ref}=\mathcal D_X(\lambda)=0$ kills the','D20',
       'Write the complete doubling identity in its actual homological group without changing the class or its vanishing.')

# Publication prose: retain all mathematical content and source-specific maps.
replacements=[
 ('\\item  Poincare--Lefschetz duality identifies','\\item \\emph{The relative primitive extension.}\nPoincar\\\'e--Lefschetz duality identifies','D13;D23','Name the complete relative-lattice proof stage and correct the name.'),
 ('\\item  Here is also its precise embedding, rather than only its index.','\\item \\emph{The character embedding and its inverse.}','D02;D13','State the exact embedding stage positively.'),
 ('\\item  The actual cusp complement satisfies','\\item \\emph{The complement and component meridians.}\nThe cusp complement satisfies','D08;D13','Name the actual peripheral calculation.'),
 ('\\item  Applying \\eqref{maps:eq:D.PC2}, there is a unique integral class $y$ with','\\item \\emph{The primitive basis.}\nApplying \\eqref{maps:eq:D.PC2}, there is a unique integral class $y$ with','D13','Name the full primitive basis argument.'),
 ('\\item  Here is the complete cubic on that basis. For component classes,','\\item \\emph{The complete integral cubic.}\nFor component classes,','D08;D13','State the cubic proof stage directly.'),
 ('Thus no rational cubic has been silently substituted for the\nintegral form.','This proves the displayed form on the full integral primitive lattice.','D02;D11','Conclude the proved integral extension directly.'),
 ('These statements concern the free characteristic\npairings; they do not determine the torsion class of $c_2$, the\nrefined class, or the full finite-coefficient fundamental-class\ninvariant.','The torsion class of $c_2$, the refined class and the full\nfinite-coefficient invariant are computed in the following steps.','D02;D11;D14','Keep the precise logical dependency without repeated negative scope framing.'),
 ('We retain the actual integral specialization of this complete cycle.','The integral specialization of the complete cycle is as follows.','D08','State the complete geometric cycle directly.'),
 ('the first integral row of \\eqref{maps:eq:D.OS6}, without division in homology\nor an assumed covering of the global filled manifolds.','the first integral row of \\eqref{maps:eq:D.OS6}; each lifted simplex\nhas its integer transfer coefficient on this local period cover.','D02;D22','Preserve the exact local covering/transfer scope and the actual integral construction.'),
 ('We use exactly the datum','Use the datum','D08','Remove workflow emphasis from the fixed input.'),
 ('We prove this before using\nany support-function evaluations.','The full boundary comparison is proved below.','D08;D14','State the proof dependency plainly.'),
 ('We give the comparison explicitly, since this cusp has torsion in\nits boundary \\(H_1\\).','The cusp boundary has torsion in \\(H_1\\); its full comparison\nuses the following cochain maps.','D08;D22','Keep the mathematical reason for retaining the full coefficient-extension argument.'),
 ('Poincare--Lefschetz duality uses','Poincar\\\'e--Lefschetz duality uses','D23','Correct scholarly typography.'),
 ('No compact-support convention replaces the displayed product of\ncoefficient groups by a direct sum.','The locally finite component-chain map and its coefficient-reading\ninverse give this product of coefficient groups.','D02;D22','Preserve the exact product and its locally finite-chain map/inverse.'),
 ('There is a useful precise version of the boundary part of this\nargument. The boundary group is the split extension','The boundary group and the two marked long loops give the split extension','D08','State the complete boundary group directly.'),
 ('Here is the actual line comparison fixing both signs.','The line comparison fixes both signs as follows.','D08','Preserve the signed Thom/Cartier argument without workflow emphasis.'),
 ('Its first Chern class contributes zero modulo eight; no integral\ndescent of the finite class is required.','Its first Chern class contributes zero modulo eight, giving the\nfinite-coefficient descent with its eighth tensor factor.','D02;D22','State the actual coefficient map and retain the eighth-power factor.'),
 ('This is an identity for all integers, not a bounded numerical\ntest: write','For all integers, write','D02;D21','Retain the universal floor calculation without referring to a numerical test.'),
 ('For an independent check of the short-long marking, retain the\nactual annulus map from \\ref{maps:src:D.2.43}, not only its augmentation.','The short-long marking also follows from the annulus map\nof \\ref{maps:src:D.2.43}.','D01;D02;D08','Preserve the full shifted-annulus auxiliary proof without check-history framing.'),
 ('exactly an\nHilbert--Burch relation, so this checks the actual annulus\nmarking rather than a rational replacement.','a\nHilbert--Burch relation, which identifies the same integral annulus\nclass for every path choice.','D02;D20;D23','State exact path-independence in its integral group and correct the article.'),
 ('specified without a long matrix display by','specified by','D08','Remove presentation-process prose.'),
 ('are proved in the following localization input.','are proved in the following localization step.','D08;D14','Identify the internal proof dependency.'),
 ('Thus there are no\nunrecorded finite-stabilizer strata in this localization.','Thus the complement of these sixteen fixed curves is free.','D08;D22','State the proved stabilizer conclusion directly.'),
 ('For clarity the ordinary degrees and the fibre characters are\ncomputed separately.','The ordinary degrees and fibre characters have the following formulas.','D08','State the mathematical content directly.'),
 ('To justify the common character, rather than making a\nseparate choice on each normalized component, compare along the\nactual toric orbit curves.','The common character is determined by comparison along the\ntoric orbit curves.','D02;D22','Keep the connected-orbit proof of the global character without a hypothetical alternative.'),
 ('the manuscript coordinate is $V=W^{-1}$.','the quotient coordinate is $V=W^{-1}$, with inverse $W=V^{-1}$.','D04;D20;D22','Give the actual nonzero-line/dual coordinate map and inverse without manuscript-version wording.'),
 ('In particular the line winding has not been discarded.','The $W_{\\rm ext}$ coordinate therefore records the line winding.','D02;D22','Preserve the exact line-winding assertion positively.'),
 ('at the other endpoint it extends in the original source-node/line chart by','at the other endpoint it extends in the source-node/line chart by','D08','Refer to the actual preserved source chart without historical version wording.'),
 ('In particular no division of a torsion Pontryagin class is used.','This is an integral characteristic-class identity.','D02;D11','Conclude the proved integral result directly.')]
for args in replacements:change(*args)
for pattern,replacement,why in [
 (r'\bactual\s+','', 'Remove workflow emphasis while preserving every explicit object, unit, map and scope.'),
 (r'\bliteral\s+','', 'State the integral cochain or geometry directly.'),
 (r'\bretained\s+','', 'State the complete geometric object without comparison history.')]:
 for m in reversed(list(re.finditer(pattern,text))):
  edits.append(('D08',text.count('\n',0,m.start())+1,m[0],replacement,why))
  text=text[:m.start()]+replacement+text[m.end():]
change('equations (2.1), (3.4), pp.267--268','equations~(2.1), (3.4), pp.~267--268','D18;D23','Preserve the exact Thomas primary locus with scholarly citation spacing.')
before=text
text,changes,issues=presentation.statement_records_to_small_tags(text)
assert not issues
for c in changes:edits.append((c.kind,before.count('\n',0,c.start)+1,c.old,c.new,c.reason))
before=text
text,changes,issues,aliases=presentation.remove_manual_equation_tags(text)
assert not issues,issues
for c in changes:edits.append((c.kind,before.count('\n',0,c.start)+1,c.old,c.new,c.reason))
assert not presentation.unresolved_literal_equation_references(text,aliases)
for m in reversed(list(re.finditer(r'\n{3,}',text))):
 edits.append(('D23',text.count('\n',0,m.start())+1,m[0],'\n\n','Remove excess empty source lines after consolidation without changing any identity.'))
 text=text[:m.start()]+'\n\n'+text[m.end():]
units.check_permanent_identifiers(original,text,['maps:def:weighted-os45-data','maps:eq:weighted-os45-total-link'],['tag-Q251','tag-Q252'])
assert text.count(r'\begin{definition}')==text.count(r'\end{definition}')==1
assert text.count(r'\begin{theorem}')==text.count(r'\end{theorem}')==1
assert text.count(r'\begin{proof}')==text.count(r'\end{proof}')==1
assert r'\tag{' not in text and '\r' not in text
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
rows=[]
for i,(kinds,line,old,new,why) in enumerate(edits,1):
 for kind in kinds.split(';'):
  rows.append([f'III-C8-LV-PUB-{i:03d}-{kind}',kind,'maps:src:D.2.53',f'weighted_os45.tex sequential edit line{line}',
   'pending page concordance','weighted/weighted_os45.tex','pending final build',old,new,why,
   'whole repaired input/admitted comparison/source/root reading; candidate readback pending; global gates open'])
p.write_text(text,newline='\n')
with (lane/'S6_SERIES_PUBLISH_LV_publication_defects.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(fields);w.writerows(rows)
print('UTC',datetime.now(timezone.utc).isoformat(),'LINES',len(original.splitlines()),'TO',len(text.splitlines()),'EXACT_EDITS',len(edits),'DEFECT_ROWS',len(rows))
print('NEW_Q251_DEFINITION_Q252_LINK; ALL69_OLD_IDENTITIES_PRESERVED; NEXT_Q253; NO_NEW_MATHEMATICAL_REFUTATION; NO_INDEPENDENT_CREDIT')
print('SHA256',hashlib.sha256(p.read_bytes()).hexdigest(),'SHARED_WRITES0; AUTOMATIC_CRITERION_CREDIT0')
