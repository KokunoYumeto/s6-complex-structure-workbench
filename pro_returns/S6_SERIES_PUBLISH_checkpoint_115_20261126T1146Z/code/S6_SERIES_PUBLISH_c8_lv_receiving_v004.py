#!/usr/bin/env python3
"""Assemble 02LV as one statement/proof and retain exact edit records.

This is a text assembler. Its substitutions are read mathematical text;
it performs no new independent theorem check and edits no canonical file.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv,json,re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation8_iii_lv'; OUT.mkdir(exist_ok=True)
canonical=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
start=canonical.index(r'\begin{theorem}[complete primitive cubic, fundamental-class and refined invariants of the weighted OS45 example]')
stop=canonical.index(r'\subsection{Moving the zero of the linearization}',start)
old=canonical[start:stop].rstrip()+'\n'
statement_end=old.index(r'\end{theorem}')+len(r'\end{theorem}')
statement=old[:statement_end]+'\n'
proof=old[statement_end:].strip()+'\n'
edits=[]
def change(oldtext,newtext,kind,reason):
    global proof
    if proof.count(oldtext)==0 and '$' in oldtext:
        chunks=oldtext.split('$')
        oldtext=''.join(chunk if i%2==0 else r'\('+chunk+r'\)' for i,chunk in enumerate(chunks))
    assert proof.count(oldtext)==1,(reason,proof.count(oldtext))
    proof=proof.replace(oldtext,newtext,1)
    edits.append(dict(defect_type=kind,location='02LV / '+reason,old_text=oldtext,new_text=newtext,reason=reason))
def cut_between(a,b,kind,reason,replacement=''):
    i=proof.index(a);j=proof.index(b,i)
    change(proof[i:j],replacement,kind,reason)

statement=re.sub(r'\\StatementRecord\{maps:src:D.2.53\}.*\n','',statement)
statement=statement.replace('[complete primitive cubic, fundamental-class and refined invariants of the weighted OS45 example]','[Invariants of the marked weighted OS45 manifold]')
statement=statement.replace('The complete integral cubic is \\eqref{maps:eq:D.PC11}--\\eqref{maps:eq:D.PC12} below.','The integral cubic is \\eqref{maps:eq:D.PC11}--\\eqref{maps:eq:D.PC12}.')
statement=statement.replace('for this exact marked weighted OS45 member.  The embedded odd sphere,\nits actual source-line transport, and the critical-chain intersection\nparity are computed in the concluding proof below.','for this marked weighted OS45 member.  Its source-line circle bundle\nembeds as a primitive torsion sphere.  For the differential reference\nframe its framed parity is one, and its intersection with an integral\nnullchain of the complete critical cycle is odd.')

# Specialize the preliminary lattice argument to the actual member.
change('We first record a saturation calculation which uses the actual component\nmeridians. Let $X$ be simply connected, let $N$ be a single rank-two\nMumford cusp with $D$ components, and put $E=X\\setminus\\operatorname{int}N$.\nAssume $b_2(X)=D-1$, $H_3(N;\\mathbb Z)$ is free, and',
r'''Let $N$ be the sixteen-component cusp of the marked manifold in the
statement and put $E=X\setminus\operatorname{int}N$.  The integral
cap maps of \ref{maps:src:D.2.46}, evaluated on its five marked
returns and the ordinary clutch, give $\pi_1(X)=1$,
$b_2(X)=15$ and the following complement marking, with
$D=16$, $A=\mathbb Z/2$ and $a_{r,s}=s\bmod2$:''','D14','specialize component saturation to the stipulated manifold')
change('The relative exact sequence therefore injects $L$ into $H^2(X)$.\nSince $X$ is simply connected, the latter group is free; its rank is\n$D-1$ by hypothesis.','The relative exact sequence therefore injects $L$ into $H^2(X)$.\nSince $X$ is simply connected, the latter group is free, of rank fifteen.','D14','remove unused general-hypothesis wording')
change('$H^3(X,E;\\mathbb Z)=H_3(N;\\mathbb Z)$ is free. The connecting',r'''$H^3(X,E;\mathbb Z)=H_3(N;\mathbb Z)$ is free by the
normalization complex for this triangular cusp in
\ref{maps:src:D.2.43}. The connecting''','D22','cite the actual cusp relative group')
change('The coefficient exact sequences identify its exterior restriction\nwith the corresponding torsion Bockstein, up to the harmless common\nconnecting-map sign. Since these characters give the full torsion\nof $H^2(E)$, they give the full primitive extension.',r'''With the connecting map given by the positive normal-disc boundary,
the coefficient exact sequence identifies its exterior restriction
with the corresponding torsion Bockstein.  Reversing that connecting
map negates both the character and its rational component coefficients,
and the two negations give inverse descriptions of the same extension.
These characters exhaust the torsion of $H^2(E)$ and therefore give
the full primitive extension.''','D22','fix the connecting-map transport')
change('The full original presentation,\nSmith change of basis and all sixteen meridian images are saved\nin the executable below.',r'''The inverse sends the free generator to the cusp meridian and the
order-two generator to $\delta$.  In the marked peripheral presentation
the first rank-one cap kills $e_1$, the next return gives
$e_2=-2\delta$, and the cusp relations give $2\delta=0$.
The remaining relations impose no further relation on $\delta$.
The four other meridians vanish, and the ordinary clutch and the
peripheral product identify $\gamma$ with the cusp meridian.
These substitutions verify both inverse composites.''','D09','replace executable presentation reference by inverse maps')
change('In particular it would\nbe incorrect to declare any fifteen of the component classes a\nprimitive basis. A convenient actual basis is','An integral primitive basis is','D02','state the primitive basis directly')
cut_between('The supplied program\n\\path{code/III_OS45_primitive_cubic_independent.py}',r'\paragraph{Integral vanishing of the critical class.}','D09','remove cubic implementation and assertion-count paragraph')

# Express the old critical representative by actual specialization and prisms.
cut_between('We construct the twenty-three-row core matrix of',r'\end{enumerate}', 'D09','replace machine-indexed critical witness by the full geometric nullchain',r'''For the second rank-one site take the transverse elliptic period
$r=e_1$, for which $\det(2e_1-e_2,r)=1$; its fixed long period is
$\gamma-8e_1$.  For the third take $r=e_2$.  These choices give
the last four rows of \eqref{maps:eq:D.OS6} by the primitive nodal
specialization maps in \ref{maps:src:D.2.46}.

Let $T_i(v)$ be the marked monodromy prism with boundary
$(\bigwedge^2A_i-I)v$.  In the ordered bivectors of
\eqref{maps:eq:D.OS6}, put
\[
\begin{aligned}
q_0&=(48,0,-16,0,2,0),&q_1&=(0,0,0,8,2,0),\\
q_2&=(-2,-52,-8,0,0,0),&q_3&=(0,0,2,0,0,0),&q_4&=0.
\end{aligned}
\]
Direct exterior multiplication of the five marked returns gives
\[
 \sum_{i=0}^4(\bigwedge^2A_i-I)q_i+10\delta\wedge\gamma=z.
 \tag{D.OS8}\hypertarget{tag-022V}{}\label{maps:eq:D.OS8}
\]
The pure $\delta\wedge\gamma$ term has an actual global bounding
chain.  At each nonordinary cap the origin $\delta$-normal chain
has boundary $T(\delta,\mu_i)$; at the ordinary cap it has boundary
$T(\delta,\mu_o)+\delta\wedge\gamma$.  The product of the
$\delta$ circle with the punctured base has boundary
$-\sum_iT(\delta,\mu_i)$, including the ordinary boundary.
Their sum $D_\delta$ therefore bounds $\delta\wedge\gamma$.
The inverse coordinates read the physical scalar angle, the marked
origin section and each peripheral collar.

For the five critical-specialization chains $S_i$, the retained
local charts give $\partial S_i=C_i-v_i$, with $v_i$ the rows of
\eqref{maps:eq:D.OS6}.  Thus
\[
 B_C=\sum_i S_i+\sum_iT_i(q_i)+10D_\delta,\qquad
                          \partial B_C=C.
\]
The cusp chain is the degree-sixteen transfer of the primitive
three-curve chain: every lifted simplex is taken once, and the marked
cover projection reads its inverse.  The two long periods are
$-8e_2+3\gamma$ and $-3e_2+\gamma$, whose valuations are
$(8,0)$ and $(0,2)$.  Their reciprocal unit-period maps retain the
source line units.  This proves the integral critical-class
vanishing in \eqref{maps:eq:D.OS1} with the full cycle and its chain.

''')

# Remove program interfaces while preserving the complete finite boundary proof.
change('Choose the integral cycle embedding $K$ and its integral left\ninverse $K^+$ recorded in \\path{code/III_OS45_core_independent.py}.',r'''Take the integral cycle embedding $K$ and its integral left inverse
$K^+$ obtained from the marked graph differential in
\ref{maps:src:D.2.46}; thus $DK=0$ and $K^+K=1$.''','D09','replace core program reference by the marked graph maps')
change('the matrix used in \\eqref{maps:eq:D.OS8}. The saved integral maps\n$U,V$ give $UMV=\\operatorname{diag}(1^{22},8)$, with the\nremaining columns zero.',r'''the marked relation matrix of that construction.  Integer row and
column reduction gives $UMV=\operatorname{diag}(1^{22},8)$, with
the remaining columns zero.  The quotient map is $z\mapsto Uz$
modulo this diagonal and its inverse sends a standard generator to
$U^{-1}e_j$; the relation $D_{jj}U^{-1}e_j$ is bounded by the
actual prism and cap chain whose coefficients are $Ve_j$.''','D09','replace saved Smith maps by quotient and chain inverses')
change('The program verifies every degree-three boundary column and gives','Substitution in the marked bar-prism and cap boundary maps gives','D09','state the coefficient calculation mathematically')
change('it gives $\\varphi(g)=-1\\pmod8$. Hence this cochain is','one obtains $\\varphi(g)=-1\\pmod8$. Hence this cochain is','D08','remove program antecedent')
cut_between('The complete matrices, integral cochain and all exact checks are in',r'\paragraph{A full boundary comparison', 'D09','remove core output path')
change('The full exact component table is retained in\n\\path{code/outputs/III_OS45_annulus_independent.json}.',r'''The six wall differences specify every component restriction and its
integral lift; changing a lift by $8z$ changes its square by
$16\eta z+64z^2$, zero modulo sixteen.''','D09','replace component output table by the full lift identity')

# Correct the literal line character; the zero evaluations are retained.
change('The scalar fibre character supplied by the support is its vertical\nslope, up to a single common sign. Thus one may take',r'''On a cone, let $m_\sigma$ be the integral affine function agreeing
with the divisor coefficients $\Psi$ at its three rays.  The local
Cartier frame is $\chi^{-m_\sigma}$ and its inverse is
$\chi^{m_\sigma}$.  The physical scalar vector is the difference
of the two vertical ray vectors.  Its line weight is therefore
$-\bigl(\Psi(r,s+1)-\Psi(r,s)\bigr)$.  In this fixed convention
the characters are''','D25','correct support-to-fibre character sign')
change('\\lambda_{r,0}=0,\\qquad\n                 \\lambda_{r,1}=3r .','\\lambda_{r,0}=0,\\qquad\n                 \\lambda_{r,1}=-3r .','D25','correct D.OL7 literal characters')
change('with a common sign\nconvention and one common additive character $L\\in\\mathbb Z/8$.\nNo global integral line lifting $u$ is assumed.',r'''with one common additive character $L\in\mathbb Z/8$.
Each connecting orbit curve has scalar tangent weight $1$ or $-1$.
Its integral equivariant degree-two group has the two generators
given by the curve class and the character class, so reduction
modulo eight is onto.  The endpoint character difference is its
degree times that tangent weight; the inverse reads the degree
and either endpoint character.  These exact maps prove the same
assertion for the finite coefficient class $u$.  The horizontal
and diagonal connections above form a connected graph: one changes
$r$ with $s$ fixed and the other changes both $r$ and the parity of
$s$.  Hence their differences leave exactly one common character.''','D22','prove finite-character comparison on the connected orbit graph')
change('\\sum d_{r,s}\\lambda_{r,s}=336,','\\sum d_{r,s}\\lambda_{r,s}=-336,','D25','correct signed localization sum')
change('The three values in \\eqref{maps:eq:D.OL9} are consequently $-16632$, $672$,\nand $-32$,','The three values in \\eqref{maps:eq:D.OL9} are consequently $-16632$, $-672$,\nand $-32$,','D25','correct signed quadratic evaluation representative')
change('-120L^2-2016\\epsilon L-16632,\\\\\n -80LV+64L-672\\epsilon V+672\\epsilon,','-120L^2+2016\\epsilon L-16632,\\\\\n -80LV+64L+672\\epsilon V-672\\epsilon,','D25','correct the complete character polynomials')
change('For completeness, under the replacements\n$\\lambda\\mapsto L+\\epsilon\\lambda$ and $\\mu\\mapsto V+\\mu$,\nwhere $\\epsilon=\\pm1$, the exact values are',r'''Adding characters sends $\lambda\mapsto L+\lambda$ and
$\mu\mapsto V+\mu$.  The following integer identities also record
the algebraic substitution $\lambda\mapsto L+\epsilon\lambda$,
$\epsilon=\pm1$:''','D22','separate character addition from the algebraic sign substitution')
change('Every coefficient is divisible by eight, sixteen, and eight,\nrespectively. Thus the results are independent of all global\nlinearization choices, not only of the displayed normalization.',r'''Every coefficient is divisible by eight, sixteen, and eight,
respectively.  In particular all global character additions preserve
the three evaluations in their full coefficient groups.  Replacing
the lift of $y$ by its character-one twist gives the equally explicit
weights $(1,0)$ in place of $(0,-1)$; the inverse subtracts that
single character.''','D22','retain the full-modulus independence and exact half-class twist')
cut_between('The supplied exact program\n\\path{code/III_weighted_OS45_checks.py}',r'In particular \(y^2=0\) integrally.', 'D09','remove localization implementation paragraph')
cut_between('The program \\path{code/III_OS45_boundary_prisms_07.py}',r'\end{enumerate}', 'D09','remove boundary and final implementation paragraphs')

# Merge the permanent refined auxiliary into the single proof.
change(r'''\end{enumerate}
\end{proof}
\begin{proof}[The refined class of the weighted OS45 member]''',r'''\item \textbf{The source sphere and refined characteristic class}''','D12','consolidate the two proofs')
change('We retain the exact source sections, fan, line linearization and peripheral\nmarkings in the statement.  In particular, no translation of a selected fan\nedge, and no replacement of a period unit by its valuation, is made below.\nWrite $C$ for the integral sum of the actual complex critical curves.',
'Use the source sections, fan, line linearization and peripheral\nmarkings in the statement.  Write $C$ for the integral sum of the\ncomplex critical curves, with the chain $B_C$ constructed above.','D02','state the marked refined setup directly')
cut_between('The cusp period lattice has columns',r'\item \emph{The based collar', 'D02','remove unused hypothetical edge translation')
change('The core Jacobians are respectively $c_0/b$ and $c_1$, hence nonzero.',r'''The inverse at the cusp reads
$b=c_0^6/x$, $a=xy/c_0^6$, $d=c_0^5z$ and
$c=(ad-1)/b$.  At the other end it reads
$a=Wf^6$, $b=Y/a$, $c=-Xa/c_1$ and $d=f/a$.
The inverse base coordinate determines $f$ in each formula.
Along the two central core circles the Jacobians are respectively
$c_0/b$ and $c_1$, hence nonzero; the endpoint neighborhoods are
chosen small enough to retain this property.''','D22','give the selected source chart inverses with its units')
change('Its right group is free, so the sequence splits as a sequence of\nabelian groups. The displayed mod-two character therefore extends\nto $H_2(\\partial U;\\mathbb Z)$.',r'''Its right group is the literal fixed lattice
$\mathbb Z(e_1,\delta)$.  On these two columns the ordered bar
quadratic correction of $A_0$ is zero.  Their marked prism sweeps
therefore split the sequence: the forward map reads the fixed
sweep, and the inverse subtracts that sweep to recover the fibre
coinvariant.  Extend the displayed mod-two character by zero on
these two fixed-sweep generators.  It is then a homomorphism on
all of $H_2(\partial U;\mathbb Z)$.''','D22','make the whole boundary mod-two detector explicit')

# Retain the labeled Borel pair as geometry fixing the Hopf generator;
# use the integral Thom-Gysin map for the actual chain intersection.
cut_between('The stable spin tangent bundle of $X$ has a global stable frame',r'\item \emph{The complete critical-chain intersection.}', 'D12','replace the second framed-parity route by the Hopf pair orientation',r'''Orient $N$ by its positive scalar circle followed by the positive
orientation of the quotient sphere $\Sigma$.  Use the character
generator $t$ for which $\langle t,[\Sigma]\rangle=1$ under the
displayed Hopf identification.  The inverse chart of the collapsed
pair above retains the corresponding relative unit.  All tangent
and normal quotient maps here come from the explicit equivariant
embedding \eqref{maps:eq:D.OR6}--\eqref{maps:eq:D.OR9}.

''')
cut_between('The preceding global/local comparison also determines the required',r'\item \emph{The refined class.}', 'D22','compute the complete integral critical link by Thom and Gysin',r'''Write $B=X_{S^1}$ and $B^\circ=(X\setminus C)_{S^1}$.
The scalar section is nonzero in the abstract differential kernel,
including its $xy$ and $xyz$ syzygy frames.  Its quotient line and
the corrected target line have ordinary first Chern class zero.
Their fixed-point weights are zero, so their equivariant first
Chern classes vanish as well: the kernel of restriction to
ordinary degree-two cohomology is the character line, and its
coefficient is read at a fixed point.  The equivariant critical-ideal
sequence therefore gives
\[
 [C]_{S^1}=c_{2,S^1}(TX)=-t^2.
\]
This identity is integral.  At $xy$ the two normal columns are
$(x,-y)$ and $(\overline y,\overline x)/(|x|^2+|y|^2)$;
their determinant is one and their inverse is
\[
 \begin{pmatrix}
 \overline x/(|x|^2+|y|^2)&-\overline y/(|x|^2+|y|^2)\\
 y&x
 \end{pmatrix}.
\]
Positive column rescaling gives the unit Bott map.  It has second
Chern residue $+1$ on the positive complex normal sphere of each
critical component.  At $xyz$ the syzygies
$(x,-y,0)$ and $(x,0,-z)$ give the same unit residue on each
axis.  The finitely many triple strata have real codimension six,
so their relative cohomology below degree six vanishes.  They
contribute no degree-four term.  This proves the equivariant
Thom equality, including its torsion part; the final equality
uses \eqref{maps:eq:D.OR12}.

Let $a_C\in H^3(X\setminus C;\mathbb Z)$ be the residue class
obtained by intersecting with the complete chain $B_C$.
Its residue on every positive normal three-sphere is one.
For the actual principal circle bundle
$X\times ES^1\longrightarrow B$, fibre integration sends its
restriction over $B^\circ$ to a class extending uniquely to
$b\in H^2(B;\mathbb Z)$.  Indeed deleting the codimension-four
critical strata induces an isomorphism in degree two; the
triple strata do not change that range.

The Thom-pair construction of the integral Gysin sequence
\cite[\S4.D, pp.~438,442--444]{Hatcher2002} gives the exact
boundary equation
\[
                           t b=[C]_{S^1}.
\]
More explicitly its cochain cone has differential
$D(\alpha,\beta)=(d\alpha+t\smile\beta,-d\beta)$, and fibre
integration reads $\beta$.  The positive Hopf connection
$\eta=(2\pi)^{-1}\operatorname{Im}(\overline z_0dz_0+
\overline z_1dz_1)$ has fibre integral one and fixes the sign
of this cone.  The first component extends across the critical
strata with their positive Thom boundary, and the second extends
to $b$.  Their boundary is exactly the displayed cup product.
The relative pullback from the Borel pair is an isomorphism in
degree four because the lower relative Thom groups vanish;
its inverse extends the same oriented normal-disc cochain.

Multiplication by $t$ on $H^2(B;\mathbb Z)$ is injective.
Its kernel in the Gysin sequence is the image of
$H^3(X;\mathbb Z)=\mathbb Z/8$, while
\eqref{maps:eq:D.OR11} makes $H^2(B;\mathbb Z)$ free.
Consequently $b=-t$.  Naturality for the actual Hopf sphere gives
\[
 \ell(N,C)=\langle a_C,[N]\rangle
 =\langle b,[\Sigma]\rangle=-1.
\]
This is the intersection with the entire prescribed chain $B_C$.
Changing that chain by a closed integral three-cycle changes the
intersection by zero, since $[N]$ is torsion in $H_3(X)$.
Reversing the sphere orientation gives $+1$ and preserves the
odd intersection parity used below.

''')
cut_between('The even induced framing in step~5 gives the same conclusion',r'\end{enumerate}', 'D12','remove the repeated concluding refined proof')

# Final mathematical review against the staged 1,304-line receiver.
staged=statement+'\n'+proof.rstrip()[:-len(r'\end{proof}')].rstrip()+'\n\\end{enumerate}\n\\end{proof}\n'
assert sha256(staged.encode()).hexdigest()=='7e1ae7d3eaf9d78c3377bcfc07da4993fb10328cd8d0ca5cf3d3782a41ed521c'

change('three-curve chain: every lifted simplex is taken once, and the marked\ncover projection reads its inverse.',r'''three-curve chain: every lifted simplex is taken once.  On each lifted
simplex the covering chart and its inverse identify its coefficient;
globally $p_*\operatorname{tr}=16\,\mathrm{id}$.''','D22','state the actual degree-sixteen transfer map')
change('$UMV=\operatorname{diag}(1^{22},8)$, with\nthe remaining columns zero.',r'''$UMV=\Delta$, where $\Delta$ has diagonal $(1^{22},8)$ and
its remaining columns are zero.''','D22','name the Smith diagonal independently of the graph differential')
change('$D_{jj}U^{-1}e_j$','$\Delta_{jj}U^{-1}e_j$','D22','use the actual Smith diagonal in the bounding relation')
change(r'''For the negative Smith generator \(g=-U^{-1}e_{22}\), with zero-based
indices, one obtains $\varphi(g)=-1\pmod8$. Hence this cochain is''',r'''The core quotient has order eight, and the actual fibre class
$g=-[e_1\wedge e_2]$ has $\varphi(g)=-1\pmod8$.
Its order is therefore eight.  Hence this cochain is''','D22','fix the primitive core generator by its actual fibre class')
change('The relative component Thom cochains identify',r'''Let $e_v$ be the positive relative Thom class of the component $v$.
Our support coordinate is the explicit involution
$\Psi\longmapsto-\sum_v\Psi(v)e_v$, with inverse the negative
of the Thom coefficient at each component.  Thus these coordinates
identify''','D25','identify support with negative positive-Thom coefficients')
change(r'''from \(H^1(\widetilde M;k)\) sends a covector \((c,m_1,m_2)\) to
the affine function \(c+m_1v_1+m_2v_2\). By \eqref{maps:eq:D.OF5}, the relative''',r'''from \(H^1(\widetilde M;k)\) sends a covector \((c,m_1,m_2)\) to
the support function $-(c+m_1v_1+m_2v_2)$: its positive Thom
coefficients are $c+m_1v_1+m_2v_2$.  Negation is its own inverse,+and the image is exactly $\operatorname{Aff}$. By \eqref{maps:eq:D.OF5}, the relative''','D25','transport the relative connecting map without changing its affine image')
change(r'''\(\operatorname{Aff}\): evaluating a covector on
\(\theta+v\) produces its affine function, and translating \(v\)
gives the deck action.''',r'''\(\operatorname{Aff}\): a covector $\alpha$ corresponds to the
function $v\mapsto-\alpha(\theta+v)$.  Evaluation and negation give
its inverse, and translating $v$ gives the deck action.''','D25','use the same negative-evaluation identification on the full boundary module')
change(r'''\eqref{maps:eq:D.OF6} in that resolution, or by choosing the relative Thom
cochain \(\Psi\): its deck difference is the boundary one-cocycle
whose value on \(\theta+v\) is precisely \(a_l(v)\).''',r'''\eqref{maps:eq:D.OF6} in that resolution, or by choosing the relative
cochain with positive Thom coefficients $-\Psi$.  Its deck difference
has Thom coefficients $-a_l$, so the boundary covector has value
$-a_l(v)$ on $\theta+v$.  Under the negative-evaluation identification
just specified, its function is exactly $a_l(v)$.''','D25','retain the full boundary cocycle under the coefficient involution')
change(r''' a_{l_j}(v)=-E(v,b_j)+c_j,\qquad j=1,2,''',r''' a_{l_j}(v)=-E(v,b_j)-c_j,\qquad j=1,2,''','D25','transport both gradient and constant of the affine boundary cocycle')
change(r'''For a direct verification, translate the marked \(\theta,b_j\)
strip from component zero to component \(v\). Its change is the
oriented short-long torus with value \(-E(v,b_j)\).
The initial strip contributes \(c_j\). There is no additional
angular-area term, since that coefficient is zero. The literal
basis-loop prism correction is the one already included in
\eqref{maps:eq:D.OF3}. This gives \eqref{maps:eq:D.OF10} at the cochain level, including
its constant term.''',r'''Here is the actual line comparison fixing both signs.  Put $h=-\Psi$
and $D_h=\sum_v h(v)D_v$.  Write $r=8a+r_0$, $0\leq r_0<8$.
For $l_1=(8,-6)$ and $l_2=(24,-16)$ the exact integral identities are
\[
\begin{array}{c|cc}
 j&m_j(v)&k_j(v)\\\hline
 1&r-4&r_0-a\\
 2&-4&3r_0-1
\end{array},\qquad h(v+l_j)-h(v)=m_j(v)+8k_j(v).
\]
Let $F_j$ be the marked period map on the common cover, retaining
its actual unit factors.  Pullback gives the equality of divisor
line bundles
\[
 F_j^*\mathcal O(D_h)=\mathcal O(D_h)\otimes
 \mathcal O(\operatorname{div}\chi^{m_j})\otimes
 \mathcal O(D_{k_j})^{\otimes8}.
\]
The explicit line map is
\[
 \chi^{-m_j}:\mathcal O(D_h)\otimes\mathcal O(D_{k_j})^{\otimes8}
                  \longrightarrow F_j^*\mathcal O(D_h),
\]
and its inverse is multiplication by $\chi^{m_j}$.  Local frames
retain reciprocal eighth powers from the displayed tensor factor.
Its first Chern class contributes zero modulo eight; no integral
descent of the finite class is required.  The two period comparisons
commute with their full tensor factors: for example
$\Delta_{l_2}m_1=24$ and $\Delta_{l_2}k_1=-3$, whose sum with
the factor eight is zero.

For the oriented short-angle/long rectangle $(\vartheta,t)$,
an end-to-start transition $\exp(\mathrm i k\vartheta)$ has
connection $A=\mathrm i kt\,d\vartheta$ and curvature
$F=-\mathrm i k\,d\vartheta\wedge dt$.  Its Chern form
$\mathrm iF/(2\pi)$ evaluates to $k$.  The normal-angle/long
rectangle reads the constant in $m_j$ by the same formula.
Consequently the positive Thom potential has difference
$E(v,b_j)+c_j$, and the support $\Psi=-h$ has difference
$-E(v,b_j)-c_j$.  This is the full boundary cocycle in
\eqref{maps:eq:D.OF10}.  The ordinary fibre and strip classes
are unchanged; in particular $u(e_1\wedge e_2)=1$.
The already included basis-loop prism correction gives
$c_1=c_2=4$, for which $-c_j=c_j$ in $k$.''','D25','give the exact marked period line map and oriented clutch including eighth powers')
change(r'''On a cone, let $m_\sigma$ be the integral affine function agreeing
with the divisor coefficients $\Psi$ at its three rays.  The local
Cartier frame is $\chi^{-m_\sigma}$ and its inverse is
$\chi^{m_\sigma}$.  The physical scalar vector is the difference
of the two vertical ray vectors.  Its line weight is therefore
$-\bigl(\Psi(r,s+1)-\Psi(r,s)\bigr)$.  In this fixed convention
the characters are''',r'''The circle used here is generated by $\delta$, the difference
of the upper and lower vertical ray vectors.  In the actual source
coordinate $W$ it acts by $W\mapsto g^{-1}W$, as verified in
\eqref{maps:eq:D.OR3}; this fixes its relation to physical line rotation.
The positive divisor coefficients on the common cover are $h=-\Psi$,
as proved by the full boundary comparison.  On a cone let $m_\sigma$
take these values $h$ on its three rays.  The rational Cartier frame
is $e_\sigma=\chi^{-m_\sigma}$.  The canonical fibre map is
\[
 g\,e_\sigma(p)=\chi^{m_\sigma}(g)e_\sigma(gp);
\]
it follows by applying $(g\cdot s)(p)=s(g^{-1}p)$ to sections.
Its inverse is the same formula with $g^{-1}$.  Therefore the
scalar weight is $m_\sigma(\delta)$, which here equals
$-\bigl(\Psi(r,s+1)-\Psi(r,s)\bigr)$.  The eighth tensor factors
in the period comparison do not change this weight modulo eight.
The characters are''','D25','derive the character from the canonical fibre action after the exact support map')
change(r'''The endpoint character difference is its
degree times that tangent weight; the inverse reads the degree
and either endpoint character.''',r'''For a coordinate $z\mapsto gz$ at the first endpoint, the degree-$d$
frames satisfy $e_0=z^{-d}e_\infty$, with inverse
$e_\infty=z^d e_0$.  Equivariance gives
$\lambda_0-\lambda_\infty=d$.  Reversing the coordinate gives the
same relation multiplied by its tangent weight.  The inverse
reads the degree and either endpoint character.  For example the
horizontal curve through $(1,0)$ has degree six and endpoint
characters $0,-6$; their difference is six.''','D22','give the exact invariant-curve transition and its inverse')

# Correct nesting after bringing the refined block into the outer proof.
proof=proof.rstrip()
assert proof.endswith(r'\end{proof}')
proof=proof[:-len(r'\end{proof}')].rstrip()+'\n\\end{enumerate}\n\\end{proof}\n'
receiver=statement+'\n'+proof

oldlabels=re.findall(r'\\label\{([^}]+)\}',old)
newlabels=re.findall(r'\\label\{([^}]+)\}',receiver)
oldtargets=re.findall(r'\\hypertarget\{([^}]+)\}',old)
newtargets=re.findall(r'\\hypertarget\{([^}]+)\}',receiver)
assert sorted(oldlabels)==sorted(newlabels),(set(oldlabels)-set(newlabels),set(newlabels)-set(oldlabels))
assert sorted(oldtargets)==sorted(newtargets)
assert receiver.count(r'\begin{theorem}')==receiver.count(r'\end{theorem}')==1
assert receiver.count(r'\begin{proof}')==receiver.count(r'\end{proof}')==1
assert receiver.count(r'\begin{enumerate}')==receiver.count(r'\end{enumerate}'),(receiver.count(r'\begin{enumerate}'),receiver.count(r'\end{enumerate}'))
assert '\r' not in receiver
path=OUT/'S6_SERIES_PUBLISH_III_02LV_receiving.tex'
path.write_text(receiver,newline='\n')
(OUT/'S6_SERIES_PUBLISH_III_02LV_receiving_statement.tex').write_text(statement,newline='\n')
(OUT/'S6_SERIES_PUBLISH_III_02LV_receiving_proof.tex').write_text(proof,newline='\n')
with (OUT/'S6_SERIES_PUBLISH_III_02LV_edit_records.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['defect_type','location','old_text','new_text','reason'],delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(edits)
print('UTC',datetime.now(timezone.utc).isoformat())
print('OLD_RANGE',canonical[:start].count('\n')+1,canonical[:stop].count('\n'))
print('OLD_SHA256',sha256(old.encode()).hexdigest(),'NEW_SHA256',sha256(receiver.encode()).hexdigest())
print('LINES',len(receiver.splitlines()),'LABELS',len(oldlabels),'TARGETS',len(oldtargets),'EDITS',len(edits))
print('ONE_THEOREM_ONE_PROOF',True)
import difflib
(OUT/'S6_SERIES_PUBLISH_III_02LV_post_whole_read.diff').write_text(''.join(difflib.unified_diff(staged.splitlines(True),receiver.splitlines(True),fromfile='staged_receiver_1304_lines',tofile='final_receiver')),newline='\n')
