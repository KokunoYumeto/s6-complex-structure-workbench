#!/usr/bin/env python3
"""Prepare one bounded Paper II proposal; never write the shared manuscript.

The reviewed switch records an exposed complete old/receiving reading, not
an independent derivation. Published-source bytes remain outside the checkpoint.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import argparse
import csv
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
TMP=ROOT.parents[1]/'tmp'
OUT=ROOT/'agents/continuation3_provenance/analytic_lr'
OUT.mkdir(parents=True,exist_ok=True)
snapshot=TMP/'c3_provenance_analytic_lr_old.tex'
original=snapshot.read_text()
owner_re=re.compile(r'\\begin\{(proposition|lemma|theorem|corollary|definition|remark|example|cited)\}')

def digest(s): return hashlib.sha256(s.encode()).hexdigest()
def write_tsv(p,rows):
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,list(rows[0]),delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)
def block(s,start):
    m=owner_re.match(s,start);env=m.group(1)
    end=s.index(r'\end{'+env+'}',start)+len(r'\end{'+env+'}')
    p=s.find(r'\begin{proof}',end);n=owner_re.search(s,end)
    if p>=0 and (not n or p<n.start()): end=s.index(r'\end{proof}',p)+len(r'\end{proof}')
    return s[start:end]
units={};old_blocks={}
for m in owner_re.finditer(original):
    b=block(original,m.start());label=re.search(r'\\label\{([^}]+)\}',b).group(1)
    assert label not in units
    units[label]=b;old_blocks[label]=b
assert len(units)==25
rows=[]
def record(owner,old,new,types,reason,location='statement and proof'):
    rows.append(dict(change_id=f'II-C3-ANALYTIC-{len(rows)+1:03d}',type=types,statement_id=owner,
      old_location=location,old_page='cp35; final page concordance pending',new_location=location,
      new_page='integrated build pending',old_text=old,new_text=new,reason=reason,
      review_status='Complete receiving comparison pending --reviewed.'))
def edit(owner,old,new,types,reason,all_matches=False):
    count=units[owner].count(old)
    assert count==1 or (all_matches and count>0),(owner,count,old[:100])
    for i in range(count if all_matches else 1):
        record(owner,old,new,types,reason,f'statement and proof; occurrence {i+1}' if count>1 else 'statement and proof')
    units[owner]=units[owner].replace(old,new) if all_matches else units[owner].replace(old,new,1)
def between(owner,start,end):
    t=units[owner];a=t.index(start);b=t.index(end,a);return t[a:b]
def add(owner,new,old,types,reason):
    assert owner not in units
    units[owner]=new;record(owner,old,new,types,reason)

# One cited duality owner, preserving both original scopes and all targets.
owner='wbII:thm:cartier-duality'
dual=r'''\begin{cited}[Duality for compact Cartier divisors and full fibres]
\hypertarget{tag-03IY}{}\label{wbII:thm:cartier-duality}
\StatementRecord{wbII:thm:cartier-duality}{cited}{03IY}{\cite[\S4, Theorem~2, pp.~82--84; \S7, Proposition~2 and complete-intersection calculation, p.~91]{RR70push}}
\hypertarget{tag-03IJ}{}\label{wbII:prop:cartier-duality-absolute}
\StatementRecord{wbII:prop:cartier-duality-absolute}{cited}{03IJ}{\SeriesRef{wbII:thm:cartier-duality}}
Let $X$ be a smooth complex threefold, let $i:W\hookrightarrow X$
be a compact effective Cartier divisor, and let $E$ be a holomorphic
vector bundle on $X$. Put $F=E|_W$ and
\[
 \omega_W=(\omega_X\otimes\mathcal O_X(W))|_W.
\]
For $q=0,1,2$ the trace pairing gives natural isomorphisms
\[
 H^q(W,F)^\vee\simeq H^{2-q}(W,F^\vee\otimes\omega_W),
 \tag{W.11}\hypertarget{tag-03EB}{}\label{wbII:eq:W:5.11}
\]
and $H^q(W,F)=0$ for $q>2$.

For the full scheme-theoretic fibre $W=f^{-1}(b)$ of a holomorphic
map $f:X\to B$ to a smooth curve, choose a nonzero vector in
$\mathcal O_B(b)|_b$. It identifies $\omega_W$ with $\omega_X|_W$
and gives a functorial perfect pairing
\[
 H^2(W,E|_W)\times
 H^0(W,E^\vee|_W\otimes\omega_X|_W)\longrightarrow\mathbb C,
\]
or, equivalently,
\[
 H^2(W,E|_W)^\vee\simeq
 H^0(W,E^\vee|_W\otimes\omega_X|_W).
 \tag{W.12}\hypertarget{tag-03EC}{}\label{wbII:eq:W:5.15a}
\]
A different nonzero vector rescales this last pairing by a nonzero
scalar. All statements use the full analytic structure of $W$.
\end{cited}

\begin{proof}
Apply \cite[\S7, Proposition~2 and complete-intersection calculation,
p.~91]{RR70push} to the codimension-one inclusion $i$. It identifies
the dualizing complex with $\omega_W[2]$. The trace duality of
\cite[\S4, Theorem~2, pp.~82--84]{RR70push}, with the locally free
first argument $F$, then identifies
\[
 H_c^q(W,F)^\vee
 =\operatorname{Ext}^{-q}_W(F,\omega_W[2])
 =H^{2-q}(W,F^\vee\otimes\omega_W).
\]
Compactness of $W$ gives $H_c^q=H^q$ and finite-dimensional coherent
cohomology. The formula is therefore a perfect pairing; negative
Ext degree gives the stated vanishing for $q>2$. Precomposition in
$F$ gives its variance. For a full fibre,
$\mathcal O_X(W)|_W=f|_W^*(\mathcal O_B(b)|_b)$; applying the chosen
vector to this constant line is exactly the asserted adjunction
identification and yields \eqref{wbII:eq:W:5.15a}.
\end{proof}'''
record(owner,old_blocks[owner]+'\n\n'+old_blocks['wbII:prop:cartier-duality-absolute'],dual,
       'D12;D17;D18','Consolidate both complete known duality statements into one cited result. Compact W in arbitrary smooth X includes both original hypotheses. Retain q=0,1,2, q>2, full-fibre pairing, trace choice, variance, all tags and equations; apply the opened RR70 theorem rather than repeat its hypersurface and duality proofs.')
units[owner]=dual;del units['wbII:prop:cartier-duality-absolute']
old=original[original.index('The next two results are explicit'):original.index(r'\begin{theorem}[Duality')]
record(owner,old,'','D01;D03;D12;D13','Remove process narration before the single cited duality owner.')

# The base-change theorem is a cited q=3 specialization, with its canonical map.
owner='wbII:prop:analytic-base-change'
edit(owner,r'\begin{proposition}[Analytic base change in degree two]',r'\begin{cited}[Analytic base change in degree two]','D17','Mark the exact known q=3 specialization as a cited result.')
edit(owner,r'\end{proposition}',r'\end{cited}','D17','Close the cited-result environment.')
edit(owner,r'\StatementRecord{wbII:prop:analytic-base-change}{proved}{03II}{\cite[pp.~120--121]{BS76push}; \cite[Lemma~1.5]{CDP98}}',
 r'\StatementRecord{wbII:prop:analytic-base-change}{cited}{03II}{\cite[Chapter~III, \S3, Theorem~3.4 and Corollary~3.5, pp.~116--121]{BS76push}}',
 'D17;D18','Use the fully opened source theorem and corollary for canonical base change, without attributing the false general local-freeness statement of CDP98 Lemma 1.5.')
edit(owner,r'\cite[pp.~120--121]{BS76push}',r'\cite[Chapter~III, \S3, Corollary~3.5, pp.~120--121]{BS76push}',
 'D18','State the exact theorem locus whose q=3 specialization is being applied.')

# Canonical normalization maps replace the repeated normal-crossing ring proof.
owner='wbII:prop:conductor'
edit(owner,r'\SeriesRef{wbII:eq:W:5.3}, \SeriesRef{wbII:eq:W:5.5}, \SeriesRef{wbII:eq:W:5.4}',
 r'\SeriesRef{cdp:st:A.1.2}, \SeriesRef{cdp:st:A.2.2}, \SeriesRef{wbII:lem:torsion-identification}; \cite[Lemma~10.3, pp.~87--88]{AC26}',
 'D12;D17;D18','Name the canonical earlier normalization owner and the known compact-fibre construction.')
old=between(owner,r'For the conductor square, write',r'\item On $S\setminus D$')
new=r'''By \cref{cdp:st:A.1.2}, the normal-crossing normalization gives
the canonical isomorphism
\[
 \eta_*\eta^*N^*_{S/\mathcal X}
 \xrightarrow{\ \sim\ }
 K=\ker(\Omega^1_{\mathcal X}|_S\to\widetilde\Omega^1_S).
\]
In the coordinates \eqref{wbII:eq:W:5.3}, it sends the tuple
$[g]\otimes(a_i)$ to
$u\sum_i a_i(\prod_{j\ne i}x_j)\,dx_i$.
The conductor ideals are $(x,y)$ in the double model and
$(xy,xz,yz)$ in the triple model, with radical pullbacks to the
smooth branches, by the local conductor calculation in
\cite[Lemma~10.2, proof, p.~87]{AC26}. Thus the conductor sequence of
\cref{cdp:st:A.2.2} specializes to
\[
0\longrightarrow\mathcal O_S
\xrightarrow{\alpha}
\eta_*\mathcal O_{\widetilde S}\oplus\mathcal O_D
\xrightarrow{\beta}
\eta_*\mathcal O_{\widetilde D}
\longrightarrow0,
\tag{W.5}\hypertarget{tag-03HY}{}\label{wbII:eq:W:5.5}
\]
where
\[
 \alpha(h)=(\eta^*h,h|_D),\qquad
 \beta(\widetilde h,k)=\widetilde h|_{\widetilde D}-\eta^*k.
\]
Tensor the canonical isomorphism by $A$ and use the finite
projection formula. The normalized section $[g]\otimes e$ maps to
a unique section $s$ of $K\otimes A$. Its displayed branch formula
gives $\eta^*s=\eta^*(dg|_S)\otimes e$ and $s|_D=0$; it is nonzero
on the smooth locus because $e$ and the conormal vector are nonzero.
Uniqueness also follows from \eqref{wbII:eq:W:5.5} tensored by
$\Omega^1_{\mathcal X}|_S\otimes A$: its two restrictions are the
specified compatible pair $(\eta^*(dg|_S)\otimes e,0)$.
For proper $g$ this is the construction in
\cite[Lemma~10.3, pp.~87--88]{AC26}.

'''
edit(owner,old,new,'D12;D17','Apply the earlier canonical map [g]⊗(a_i)↦uΣ a_i(∏x_j)dx_i, retaining the conductor square maps and every uniqueness/nonzero clause. Compactness remains confined to the original final clause.')
edit('wbII:cor:normal-crossing-kernel',r'N^*_{S/X}',r'N^*_{S/\mathcal X}',
 'D20','Use the ambient space named in the immediately preceding conductor theorem.',all_matches=True)

# A numbered definition contains precisely the marked construction data.
start=original.index('Here $f:X\\to B=')
end=original.index(r'\subsection{Boundary cocycles',start)
old=original[start:end].rstrip()
new=old.replace('Here $f:X\\to B=', 'Let $f:X\\to B=',1)
new=new.replace('$ is the standard family of Paper I,','$ be the standard family of Paper I,',1)
new=new.replace('At the cusp use the unchanged zero-section gluing, with no additional\nvertical translation.', 'At the cusp use the zero-section gluing, whose vertical translation is zero.')
stale=r'''\CompendiumRef{I}{wb:prop:period-input-audit}, \CompendiumRef{I}{wb:thm:candidate-cusp-geometry}, \CompendiumRef{I}{wb:prop:candidate-finite-fillings}. The arguments
below do not replace these data by a topologically equivalent model.'''
receiving=r'''\SeriesRef{fam:src:A.1.2}, \SeriesRef{fam:src:A.3.1} and
\SeriesRef{push:src:E.3.1}. In the notation of
\cref{def:II:marked-conventions}, $\beta=\beta^{\rm part}+c$,
$(v_1,v_2)=(\varepsilon,-\varepsilon')$, and the marking
$\Xi$ is induced by the same period matrix $\Pi_c$.
The normalized finite base change is
$y\mapsto(q_j(y),s_j(y))$ over $t_j=s_j^{m_j}$, with deck
$(s_j,\zeta)\mapsto(e^{-2\pi i/m_j}s_j,
R_j(s_j)\zeta+\Pi_c(g_js_j)v_j/m_j)$.
Here
\[
 R_1=\begin{pmatrix}-1/\tau&0\\(1-\mu)/\tau&1\end{pmatrix},
 \qquad R_2=\begin{pmatrix}1/\tau&0\\-\mu/\tau&1\end{pmatrix},
\]
and $R_j(z)\Pi_c(z)=\Pi_c(g_jz)A_j$.
The finite deck and overlap translations are
\SeriesRef{pub:I:eq:PD7} and \SeriesRef{pub:I:eq:PD8}.
At the cusp, use the coordinates $Z=sB_0+C(t)$ of
\SeriesRef{fam:src:A.3.1} and the period action $\Psi_\lambda$
in \SeriesRef{pub:I:eq:PD11}; $\eta$ is the restriction of that
quotient map to the divisor $E_0$.'''
assert stale in new
new=new.replace(stale,receiving)
new=r'''\begin{definition}[Marked periods and cusp normalization]
\hypertarget{tag-P309}{}\label{def:II:analytic-picard-data}
\StatementRecord{def:II:analytic-picard-data}{proved}{P309}{\SeriesRef{def:II:marked-conventions}, \SeriesRef{fam:src:A.1.2}, \SeriesRef{fam:src:A.3.1}, \SeriesRef{push:src:E.3.1}}
'''+new+'\n'+r'\end{definition}'
add('def:II:analytic-picard-data',new,old,'D04;D06;D08;D13;D20','Number the construction data and replace all three obsolete compendium targets by current numbered owners, with the exact period matrix, root quotient, overlap and normalization maps verified in the attached pre-split construction and current cross-paper metadata.')
owner='wbII:prop:local-cusp-picard-obstruction'
edit(owner,r'''Use the cusp coordinates of
\CompendiumRef{I}{wb:prop:period-input-audit}; \CompendiumRef{I}{wb:thm:candidate-cusp-geometry}:''',
 r'''Use the cusp coordinates and quotient maps of
\cref{def:II:analytic-picard-data}:''','D04;D06;D12','The numbered definition now names the exact current construction and its explicit coordinate maps; remove two obsolete compendium references.')

owner='wbII:prop:analytic-ah-boundary'
edit(owner,'orient its boundary meridians clockwise, and retain the zero-section lifts',
     'orient its boundary meridians clockwise, and use the zero-section lifts',
     'D08','State the marked zero-section choice without process language.')
edit(owner,r'''this integer with the exponential connecting class of \(L|_F\); this is
the Appell--Humbert convention used in
\eqref{wbII:eq:W:5.17av}--\eqref{wbII:eq:W:5.17ax}, and agrees with the standard factor-of-automorphy
calculation''',
 r'''this integer with the exponential connecting class of \(L|_F\),
with the factor-of-automorphy convention of''',
 'D12;D14;D17','State the exact primary convention at its first use; the later cusp calculation uses the same already-established connecting map, without a forward premise.')

# Exact known applications in the vanishing criteria.
owner='wbII:lem:cdp-generic-endpoints'
edit(owner,r'''By \cite[Proposition~1.1, p.~78]{CDP98}, applied to the connected smooth
space \(Y\), the divisor \(D\), and the locally free sheaf \(B\), one has''',
 r'''Apply \cref{cdp:st:E17} with $Z=Y$, $\mathcal V=B$ and the divisor $D$.
The smooth connected space $Y$ has one irreducible component and no
embedded associated components, and $D$ meets that component. Thus''',
 'D12;D17;D25','Use the corrected divisor-vanishing owner with its verified associated-component hypotheses. CDP98 Proposition 1.1 is valid for this smooth application; no nonreduced generalization is inferred.')
edit(owner,r'\cite[Proposition~1.1, p.~78]{CDP98}; ',r'\SeriesRef{cdp:st:E17}; ',
 'D12;D17','Name the exact earlier premise actually applied by the proof.')
old=original[original.index('The following endpoint argument is a re-derivation'):original.index(r'\begin{lemma}[Generic endpoints on')]
record(owner,old,'','D01;D03;D12;D13','Delete process commentary; the numbered lemma retains the arbitrary-dimensional Picard-space application and its local universal-family proof.')

owner='wbII:thm:corrected-cdp-global'
edit(owner,r'\SeriesRef{wbII:lem:cdp-generic-endpoints}, \SeriesRef{wbII:eq:W:5.28}',
 r'\SeriesRef{wbII:lem:cdp-generic-endpoints}, \SeriesRef{cdp:st:C.1.1}, \SeriesRef{wbII:eq:W:5.28}',
 'D12','Name the earlier index and Picard owner.')
edit(owner,r'''\item The exponential sequence and the two integral vanishings give''',
 r'''\item Tensoring the integral vanishings with $\mathbb Q$ gives
$b_1(X)=b_2(X)=0$. Apply \cref{cdp:st:C.1.1} with $Y=X$;
its Picard component map and $H^2(X;\mathbb Z)=0$ give''',
 'D12;D17','Replace the repeated Picard-component argument by the earlier exact owner and the integral-to-rational specialization.')
old=between(owner,r'\item Every \(M\in\operatorname{Pic}(X)\)',r'\end{enumerate}')
new=r'''\item The same proposition, with $L=M$ and the complex orientation
of $X$, gives
\[
 \chi(X,T_X\otimes M)
 =\frac12\left\langle c_3(T_X),[X]\right\rangle.
\]
Together with \eqref{wbII:eq:W:5.28}, this proves
\eqref{wbII:eq:W:5.26}.

'''
edit(owner,old,new,'D12;D17','Replace the repeated HRR degree-six calculation by C.1.1, with Y=X, L=M and the same complex orientation; every original conclusion is preserved.')
owner='wbII:thm:corrected-cdp-fibrewise'
old=between(owner,'The map \\(f\\) is flat:',r'The uniform top-degree')
new=r'''Apply \cref{wbII:lem:curve-flatness} to $f$: the total space is
connected and smooth, and the algebraic reduction is nonconstant.
Thus $f$ and $E=T_X\otimes L$ are flat over the curve.
The fibre is compact and Cartier, so
\cref{wbII:prop:cartier-duality-absolute}, with this $E$ and a
nonzero vector in $T_cC$, gives
\[
 H^2(W_c,E|_{W_c})^\vee
 \simeq H^0(W_c,\Omega_X^1|_{W_c}\otimes A_c)=0.
\]
'''
edit(owner,old,new,'D12;D17','Apply the earlier flatness and compact Cartier-fibre duality owners to the full W_c with the stated twist and trace choice; remove their duplicated proofs.')

# Mathematical consequences outside proofs receive their own numbered owners.
start=original.index(r'\paragraph{scope and sharpness')
mid=original.index('The restandard family',start)
end=original.index(r'\paragraph{The exact monodromy repair.}',mid)
scope=r'''\begin{remark}[The connecting map on a reduced full fibre]
\hypertarget{tag-P311}{}\label{rem:II:reduced-fibre-connecting-scope}
\StatementRecord{rem:II:reduced-fibre-connecting-scope}{proved}{P311}{\SeriesRef{cdp:st:A.1.1}, \SeriesRef{wbII:thm:corrected-cdp-fibrewise}}
Under the two endpoint vanishings in \eqref{wbII:eq:W:5.31}, the
section-kernel isomorphism of \cref{cdp:st:A.1.1} identifies the
ambient group in \eqref{wbII:eq:W:5.32} with $\ker\delta_c$.
Consequently ambient vanishing is equivalent to injectivity of
$\delta_c$, computed on the whole reduced Cartier fibre.
For a nonreduced full fibre $W$, let
$\mathcal J=\ker(\mathcal O_W\to\mathcal O_{W_{\rm red}})$ and
$E_W=(\Omega_X^1\otimes\omega_X\otimes L^\vee)|_W$.
The filtration $E_W\mathcal J^j$ has graded terms
$E_W\otimes_{\mathcal O_W}(\mathcal J^j/\mathcal J^{j+1})$;
its connecting maps enter the computation of $H^0(W,E_W)$.
For $W=mS$, these are the conormal powers and connecting maps of
\cref{cdp:st:A.3.1}, and \cref{cdp:st:A.3.3} gives the finite
Picard-translation vanishing criterion.
The global and relative criteria
\cref{wbII:thm:corrected-cdp-global,wbII:cor:corrected-cdp-relative}
apply to full fibres with their nilpotents and multiplicities.
\end{remark}'''
add('rem:II:reduced-fibre-connecting-scope',scope,original[start:mid],
 'D02;D11;D13','Number the exact equivalence and state positively the reduced/full-fibre scope through the kernel map and the nilpotent filtration.')
record('wbII:test:cdp-comparison',original[mid:end],'','D01;D02;D08;D11;D12;D13','Delete the repeated nonvanishing argument; both full conclusions and the cusp construction already stand in the following numbered corollary and its complete proof.')

start=end;end=original.index(r'\begin{corollary}[Positive Euler',start)
mono=r'''\begin{remark}[The invariant-lattice spanning condition]
\hypertarget{tag-P312}{}\label{rem:II:invariant-lattice-spanning}
\StatementRecord{rem:II:invariant-lattice-spanning}{proved}{P312}{\SeriesRef{cdp:st:D.1.10}, \SeriesRef{cdp:st:D.1.7}, \SeriesRef{cdp:st:C.3.11}}
For the algebraic reduction in \cref{cdp:st:D.1.10}, put
$C^\circ=C\setminus\Delta$ and let $F$ be a general smooth fibre.
The coefficient map $\mathbb Z_F\hookrightarrow\mathcal O_F$
gives the map in that proposition. The complex span of its invariant
integral domain equals the whole target precisely when
\[
 \operatorname{Span}_{\mathbb C}\operatorname{im}\!\left(
 H^1(F;\mathbb Z)^{\pi_1(C^\circ)}
 \longrightarrow H^1(F,\mathcal O_F)\right)
 =H^1(F,\mathcal O_F).
\tag{W.60}\hypertarget{tag-03HW}{}\label{wbII:eq:W:5.33}
\]
This is the exact final spanning condition in
\cite[Theorem~3.1, proof, final paragraph, p.~86]{CDP98}.
Trivial monodromy on $H_1(F;\mathbb Z)$ suffices: by
\cref{cdp:st:C.3.11}, the smooth fibre is a two-torus or belongs to
the branch $b_1(F)=h^1(F,\mathcal O_F)=1$.
For a two-torus the complexified coefficient map is the surjective
projection $H^1(F;\mathbb C)\to H^{0,1}(F)$, and the integral
lattice spans its source. In the second branch,
\cref{cdp:st:D.1.7} sends a nonzero integral generator to a nonzero
vector of the one-dimensional complex target, which therefore spans it.
For the standard marked family, write
$v=a\gamma+bu+cw+d\delta$ in the basis of
\cref{def:II:analytic-picard-data}.
The equation $T_2v=v$ gives $c=b$ and $d=2b$, and the first row of
$T_1v=v$ gives $2d=6c$. Hence $b=c=d=0$, so the common invariant
lattice is $\mathbb Z\gamma$.
Here $h^1(F,\mathcal O_F)=2$, whereas the invariant image has
complex span of dimension one by \cref{cdp:st:D.1.7}.
This family has the integral cohomology and holomorphic algebraic
reduction assumed in \cite[Theorem~2.2, p.~680]{CDP2020}, and its
displayed monodromy matrices are nonidentity. Thus those hypotheses
do not imply either \eqref{wbII:eq:W:5.33} or trivial monodromy.
\end{remark}'''
add('rem:II:invariant-lattice-spanning',mono,original[start:end],
 'D02;D04;D12;D13;D17;D22','Keep W.60 in one numbered application of the earlier invariant-lattice owner. Prove the trivial-monodromy consequence through the torus projection or the injective real coefficient map in the q=1 branch, and give the actual standard-family counterexample to implication.')

# The restriction map on relative differentials is an isomorphism to intrinsic forms.
start=original.index(r'\paragraph{scope of the local correction}')
end=original.index(r'\section{The Liu--Rollenske parameter covering}',start)
local=r'''\begin{remark}[Restriction and finite \texorpdfstring{\'etale}{etale} base change]
\hypertarget{tag-03IR}{}\label{wbII:rem:relative-local-scope}
\StatementRecord{wbII:rem:relative-local-scope}{proved}{03IR}{\SeriesRef{wbII:prop:relative-local}, \SeriesRef{cdp:st:B1}}
For $S=\{t=0\}$ in the two normal-crossing charts of
\cref{wbII:prop:relative-local}, the natural base-change map is
\[
 M_i\otimes_{R_i}R_i/(t)\xrightarrow{\ \sim\ }\Omega^1_S,
 \qquad d x_j\otimes1\longmapsto d(x_j|_S).
\]
Its inverse sends each intrinsic coordinate differential to the
same generator in the displayed quotient: both modules have the
presentation with relations $t=0$ and $dt=0$.
In the node $xy=0$, the image of $x\,dy=-y\,dx$ is nonzero and is
annihilated by both $x$ and $y$, as computed in \cref{cdp:st:B1}.
Thus this fibre restriction of the torsion-free total-space module
has the stated conductor-supported torsion.

For a finite surjective \'etale map $h:U'\to U$ over the base curve,
the map $h^*\Omega^1_{U/B}\to\Omega^1_{U'/B}$ induced by
$da\mapsto d(h^*a)$ is an isomorphism. Flat pullback preserves the
kernel of multiplication by a nonzerodivisor, and faithful
flatness reflects its nonvanishing; it therefore transports the
torsion calculation for the multiple-fibre module in
\eqref{wbII:eq:CN:6.4}. For a ramified quotient the transitivity
sequence has the additional term $\Omega^1_{U'/U}$, so the
quotient module is computed with that term and the group action.
\end{remark}'''
add('wbII:rem:relative-local-scope',local,original[start:end],
 'D02;D11;D13;D20','Replace the informal total-space/fibre distinction by the quotient map and the exact canonical isomorphism between restricted relative and intrinsic fibre differentials, with its inverse. The old paragraph did not assert that those two fibre modules were unequal. Keep the nodal torsion example and the finite étale faithful-flatness statement; state the ramified transitivity term explicitly.')
old=original[original.index('The following computation concerns the relative cotangent'):original.index(r'\begin{proposition}[Crossing and multiple-fibre modules]')]
record('wbII:prop:relative-local',old,'','D03;D11;D13','The numbered proposition already states the total-space ring and base function; remove its orphan introduction.')

# Apply the earlier field-isomorphism owner inside the LR covering proof.
owner='ii:LR:covering'
old=between(owner,'Let $f:Y\\to\\mathbb P^1$ be the resulting proper connected torus',
            'A biholomorphism of two members')
new=r'''Let $f:Y\to\mathbb P^1$ be the resulting proper connected torus
fibration. Its smooth fibres are compact complex tori, with
translation-invariant K\"ahler forms. The preceding sphere
calculation gives $H^2(Y;\mathbb R)=0$, so \cref{cdp:st:E1}
applies with this same $Y$ and $f$. Its pullback isomorphism is
\[
                   \mathbb C(Y)=f^*\mathbb C(t).      \tag{LR.12}
\]
'''
edit(owner,old,new,'D12;D17','Remove the repeated vertical-divisor and descended-meromorphic-function proof. The receiving E1 hypotheses are checked by the retained explicit source comparison, sphere calculation and torus Kähler forms; retain the exact field map and all subsequent intrinsic-fibre and double-turn arguments.')

# Readable local arguments keep their maps while removing process framing.
owner='wbII:prop:analytic-ah-boundary'
edit(owner,r'''Indeed, before naming \(\widetilde d_j(\alpha)\), the quotient of the two
sides of \eqref{wbII:eq:W:5.17-A14c} is central because both cover the same translation.''',
 r'''The two lifts in \eqref{wbII:eq:W:5.17-A14c} cover the same translation,
so their quotient is central.''','D08','State the central-quotient reason directly; the additive exponent and its unique pairing remain unchanged.')
edit(owner,'the based total-space loop retained in', 'the based total-space loop in',
 'D08','Remove process language from the fixed based-loop identity.')
edit(owner,r'''\(\widehat\delta\) in the \(\phi\)-direction.  The latter fixed-base loop
does \emph{not} itself bound the \(x_2\)-disc.  To identify the correct
meridian, put''',
 r'''\(\widehat\delta\) in the \(\phi\)-direction. Its \(u\)-winding is
$-1$. Put''','D02;D08','State the fixed-base loop through its nonzero winding and retain the complete unimodular change to the disc meridian.')
edit(owner,r'''Its exactness follows from the existence of a holomorphic logarithm locally
for every nonvanishing holomorphic function, and from the integral kernel
of the exponential. Cartan's theorem~B gives''',
 r'''Cartan's theorem~B gives''','D17','Remove the repeated local proof of the exponential sequence; retain its maps and the exact Cartan-B application to the Stein neighbourhood.')
edit(owner,r'''Thus the alternating cocycle is frame-invariant without assuming that its
central-extension lifts commute.''',
 r'''Thus the alternating cocycle is frame-invariant because $gh=hg$
in the underlying deck group.''','D02','Keep the proved coboundary identity and its exact deck-group hypothesis.')
owner='wbII:prop:conductor'
edit(owner,'specified compatible pair', 'compatible pair','D08','Remove process emphasis from the displayed pair defining uniqueness.')
owner='wbII:lem:analytic-support-specialization'
edit(owner,'isomorphism, not merely numerical equivalence.', 'isomorphism.',
 'D02','The preceding explicit blow-up-basis calculation and H1(O)=0 already prove the stated isomorphism.')
edit(owner,r'''Thus \(U_\sigma\) is not contained in \(U_{\rho_v}\cap U_{\rho_w}\), and
the coordinate discs in \(S_\sigma\) cannot be applied directly to the
ratio \(e_w/e_v\).''',
 r'''The ratio \(e_w/e_v\) is defined on \(U_0\cap Y_\epsilon\).
We compare it with a frame on \(S_\sigma\) as follows.''',
 'D02','State the exact common domain and introduce the extending frame; all localization inclusions and winding computations remain.')
owner='ii:LR:covering'
edit(owner,r'\cite[Lemma~2.7]{LiuRollenske2026}',r'\cite[Lemma~2.7(ii)--(iii), p.~6]{LiuRollenske2026}',
 'D18','The opened full lemma gives the extending good-root action and its nonzero central scalar at this exact locus.')
edit(owner,'Thus $u=r^4=w^2$ literally.', 'Thus $u=r^4=w^2$.','D08','Remove process emphasis from the exact parameter map.')
edit(owner,r'''We distinguish the global coordinate $t$ from the normal-form
coordinate on the fixed good root. Write that root coordinate as
$\zeta$, put $\theta=\zeta^4$, and write $t=T(\theta)$ with''',
 r'''Write $\zeta$ for the normal-form coordinate on the fixed good root
and put $\theta=\zeta^4$. The global coordinate satisfies $t=T(\theta)$ with''',
 'D02;D20','Name both coordinates through the exact map T and retain the full inverse and equivariance comparison.')
edit(owner,'This is a specified scalar change of the lift $C_0$;', 'This scalar change of the lift $C_0$ gives $C$;',
 'D08','State the chosen scalar map directly.')
edit(owner,'over the literal\ncover $u=w^2$', 'over the\ncover $u=w^2$', 'D08','Retain the parameter map without process emphasis.')
owner='night:P3K.36'
edit(owner,r'\StatementRecord{night:P3K.36}{false}{02UH}{}',
 r'\StatementRecord{night:P3K.36}{proved}{02UH}{\SeriesRef{ii:LR:covering}}',
 'D25','Correct the hidden legacy status of the current proved double-cover remark; the complete 01RO proof supplies its claim and the printed tag-only renderer is unchanged.')
for old,new in [
 ('the actual period', 'the period'),
 ('the actual overlap', 'the overlap'),
 ('The actual', 'The'),
 ('the actual', 'the'),
 ('actual local', 'local'),
 ('actual marked', 'marked'),
 ('actual cusp', 'cusp'),
]:
    for owner in list(units):
        if old in units[owner]:edit(owner,old,new,'D08','Remove process emphasis while retaining the displayed mathematical map.',all_matches=True)

# Remove explicit re-proof framing and mathematical preview paragraphs.
old=original[original.index(r'\subsection{The corrected theorem that survives'):original.index(r'\begin{lemma}[Generic endpoints in')]
record('sec:II:analytic-vanishing',old,'','D01;D02;D03;D08;D13;D14','Replace the process title and preview by the mathematical section title; the complete criteria and their counterexample remain numbered.')

# Automatic equation numbering with every existing mathematical target preserved.
equation_map={}
manual=re.compile(r'(?<!\\)\\\[((?:(?!(?<!\\)\\\]).)*?)\\tag\{([^}]+)\}((?:(?!(?<!\\)\\\]).)*?)(?<!\\)\\\]',re.S)
for owner in list(units):
    while True:
        m=manual.search(units[owner])
        if not m:break
        old=m.group();a,num,b=m.groups()
        labels=re.findall(r'\\label\{([^}]+)\}',a+b)
        label=labels[0] if labels else 'eq:II:analytic-'+re.sub(r'[^A-Za-z0-9]+','-',num).strip('-')
        equation_map[num]=label
        suffix='' if labels else r'\label{'+label+'}'
        new='\\begin{equation}'+a+b+suffix+'\\end{equation}'
        new=re.sub(r'\n[ \t]*\n', '\n',new)
        edit(owner,old,new,'D19','Number the equation by its final section counter, retaining the full display and all existing labels/targets; add a stable equation label where needed.')
    for m in list(re.finditer(r'\\begin\{align\*\}((?:(?!\\end\{align\*\}).)*?)\\end\{align\*\}',units[owner],re.S)):
        old=m.group();body=m.group(1)
        tags=list(re.finditer(r'\\tag\{([^}]+)\}',body))
        if not tags:continue
        assert len(tags)==1,(owner,'multiple manual tags in one align block')
        tag=tags[0];a=body[:tag.start()];num=tag.group(1);b=body[tag.end():]
        labels=re.findall(r'\\label\{([^}]+)\}',b)
        assert labels
        equation_map[num]=labels[0]
        new=r'\begin{equation}\begin{aligned}'+a+r'\end{aligned}'+b+r'\end{equation}'
        new=re.sub(r'\n[ \t]*\n', '\n',new)
        edit(owner,old,new,'D19','Give the multiline identity one section-numbered equation while preserving its tag and label outside the aligned mathematical block.')
for owner in list(units):
    for num,label in equation_map.items():
        if '('+num+')' in units[owner]:
            edit(owner,'('+num+')',r'\eqref{'+label+'}','D04;D19','Resolve the reference through its preserved or new equation label.',all_matches=True)

# Exact dependency order; long explicit maps retain one complete proof each.
specs=[
 ('duality','Analytic duality and base change','P307','sec:II:analytic-duality',
  ['wbII:lem:curve-flatness','wbII:thm:cartier-duality','wbII:prop:analytic-base-change','wbII:cor:surface-top-base-change']),
 ('differentials','Conormal and relative cotangent maps','P308','sec:II:conormal-relative-maps',
  ['wbII:lem:torsion-identification','wbII:prop:conductor','wbII:cor:normal-crossing-kernel','wbII:prop:relative-local','wbII:rem:relative-local-scope']),
 ('boundary','Marked Picard restrictions and boundary cocycles','P310','sec:II:analytic-picard-boundary',
  ['def:II:analytic-picard-data','wbII:prop:pic0-pullback','wbII:prop:analytic-ah-boundary']),
 ('cusp','Line bundles on the toric cusp','03IU','wbII:subsec:local-cusp-picard-obstruction',
  ['wbII:prop:local-cusp-picard-obstruction','wbII:lem:analytic-support-specialization']),
 ('global_picard','Global Picard restrictions','03IT','wbII:subsec:global-picard-restriction',
  ['wbII:thm:analytic-all-picard','wbII:rem:local-cusp-picard-obstruction']),
 ('vanishing','Tangent cohomology and vanishing criteria','P315','sec:II:analytic-vanishing',
  ['wbII:thm:candidate-conductor','wbII:cor:candidate-conductor-actual','wbII:lem:generic-endpoints','wbII:lem:cdp-generic-endpoints',
   'wbII:thm:corrected-cdp-global','wbII:cor:corrected-cdp-relative','wbII:thm:corrected-cdp-fibrewise',
   'rem:II:reduced-fibre-connecting-scope','rem:II:invariant-lattice-spanning','wbII:test:cdp-comparison']),
 ('lr_covering','The Liu--Rollenske parameter covering','P316','sec:II:lr-parameter-covering',
  ['ii:LR:covering','night:P3K.36']),
]
# Preserve the pre-existing global-Picard section label exactly.
old_global=original[original.index(r'\subsection{Global restriction and conductor nonvanishing}'):original.index(r'\begin{theorem}[Global restriction of line bundles]')]
old_global_labels=re.findall(r'\\label\{([^}]+)\}',old_global)
assert len(old_global_labels)==1
specs[4]=(specs[4][0],specs[4][1],specs[4][2],old_global_labels[0],specs[4][4])
pieces=[];placements=[]
for key,title,tag,label,owners in specs:
    heading=r'\section{'+title+r'}\hypertarget{tag-'+tag+r'}{}\label{'+label+'}'
    text=heading+'\n\n'+'\n\n'.join(units[o] for o in owners)+'\n'
    name='S6_SERIES_PUBLISH_analytic_'+key+'_proposed.tex'
    (OUT/name).write_text(text,newline='\n');pieces.append(text)
    placements.append(dict(section=label,title=title,tag=tag,owners=owners,file=name))
combined='\n'.join(pieces)+'\n\\clearpage\n'
record('sec:II:analytic-duality','\n'.join(re.findall(r'\\(?:sub)?section\{[^\n]+',original)),
       '\n'.join(p.split('\n',1)[0] for p in pieces),'D13;D14',
       'Place flatness, duality and base change before their conductor applications; make marked boundary data, local cusp maps and global Picard restriction separate readable sections; place the full global/relative/fibrewise criteria and LR covering after their premises. All long construction proofs remain single owners.','complete bounded order')
(OUT/'S6_SERIES_PUBLISH_analytic_lr_proposed.tex').write_text(combined,newline='\n')

# These are direct source-proposal guards, not a refreshed paper inventory.
for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{(tag-[^}]+)\}']:
    before=Counter(re.findall(pattern,original));after=Counter(re.findall(pattern,combined))
    assert not(before-after),(pattern,before-after)
    for key in before:assert before[key]==after[key],(key,before[key],after[key])
assert r'\CompendiumRef' not in combined
assert r'\tag{' not in combined
assert all(combined.count(r'\label{'+o+'}')==1 for o in units)
# This bounded guard catches a conversion that crosses an earlier untagged
# align* block or mistakes the second slash of \\[2pt] for a display opener.
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',combined):
    action,env=m.groups()
    if action=='begin':stack.append(env)
    else:
        assert stack and stack[-1]==env,(m.start(),env,stack[-3:])
        stack.pop()
assert not stack,stack
for m in re.finditer(r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}(.*?)\\end\{\1\}',combined,re.S):
    assert not re.search(r'\n[ \t]*\n',m.group(2)),('blank math paragraph',m.start(),m.group(1))
ap=argparse.ArgumentParser();ap.add_argument('--reviewed',action='store_true');args=ap.parse_args()
if args.reviewed:
    for row in rows:row['review_status']='Complete old/receiving statement-and-proof comparison read; used and rechecked in this run.'
write_tsv(OUT/'S6_SERIES_PUBLISH_analytic_defects.tsv',rows)
status=dict(scope='Analytic duality through LR covering; stops before the following part.',
    snapshot=str(snapshot),structure=placements,old_complete_reading=True,
    receiving_complete_reading=args.reviewed,source_admission=False,shared_writes=False,
    source_comparison='Exposed old and receiving proofs; used and rechecked in this run.',
    preserved_labels=len(Counter(re.findall(r'\\label\{([^}]+)\}',original))),
    unused_reserved_tags=['P280','P313','P314'],
    pdf_pages='Parent integrated build and complete page reading pending.')
(OUT/'S6_SERIES_PUBLISH_analytic_status.json').write_text(json.dumps(status,indent=2,ensure_ascii=False)+'\n',newline='\n')
print(f'Prepared {len(rows)} exact instance rows, {len(units)} owners and {len(specs)} sections; reviewed={args.reviewed}. Shared source unchanged.')
