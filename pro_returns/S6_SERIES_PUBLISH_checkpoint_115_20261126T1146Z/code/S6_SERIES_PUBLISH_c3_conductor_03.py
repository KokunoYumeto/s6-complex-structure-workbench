#!/usr/bin/env python3
"""Prepare the read-and-compared normalization section, without central edits."""
from pathlib import Path
import csv
import re
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_conductor'
PRE='S6_SERIES_PUBLISH_c3_conductor_03'
source=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
start=source.index(r'\section{Normalization, conductor genus and local torus exclusions}')
next_heading=re.search(r'^\\section\{',source[start+10:],re.M)
end=start+10+next_heading.start()
original=source[start:end]
ms=list(re.finditer(r'^\\begin\{(?:definition|proposition|theorem|lemma|corollary|cited|remark|example)\}',original,re.M))
heading=original[:ms[0].start()].strip()+'\n\n'
blocks={}
for i,m in enumerate(ms):
    block=original[m.start():ms[i+1].start() if i+1<len(ms) else len(original)]
    ident=re.search(r'\\StatementRecord\{([^{}]+)\}',block).group(1)
    assert ident not in blocks
    blocks[ident]=block.strip()+'\n\n'
assert len(blocks) in (23,24), len(blocks)
if len(blocks)==24:assert 'lem:II:exceptional-intersection' in blocks
old_blocks=blocks.copy()
rows=[]
transfers=[]

def log(kind,owner,old,new,reason,newloc=None):
    p=source.find(old)
    line=source[:p].count('\n')+1 if p>=0 else ''
    rows.append(dict(change_id=f'II-C3-NOR-{len(rows)+1:04d}',type=kind,statement_id=owner,
        old_location=f'pre-admission source line {line}; {owner}',
        old_page='cp35 PDF omitted from supplied checkpoint; source locus given',
        new_location=newloc or owner,new_page='pending integrated final PDF',
        old_text=old,new_text=new,reason=reason,
        review_status='Complete original and receiving mathematical context read and compared; integrated page reading remains open.'))

def replace(ident,old,new,kind,reason):
    assert blocks[ident].count(old)==1,(ident,old[:100],blocks[ident].count(old))
    log(kind,ident,old,new,reason)
    blocks[ident]=blocks[ident].replace(old,new,1)

def piece(ident,first,last,include_last=False):
    text=blocks[ident];a=text.index(first);b=text.index(last,a)
    if include_last:b+=len(last)
    return text[a:b]

def move_log(old_owner,new_owner,text,reason):
    log('D14',old_owner,text,text,reason,new_owner)
    for lab in re.findall(r'\\label\{([^{}]+)\}',text):
        transfers.append(dict(label=lab,old_owner=old_owner,new_owner=new_owner,reason=reason))

# One owner for the exact finite-duality maps used in the genus arguments.
dual_id='lem:II:conductor-duality'
dual_local=piece('cdp:st:A.5.7',r'\item Write $R=',r'\item The ordinary-cusp hypothesis')
eq11=re.search(r'\\\[.*?\\tag\{A.J.11\}.*?\\\]',dual_local,re.S).group()
eq12=re.search(r'\\\[.*?\\tag\{A.J.12\}.*?\\\]',dual_local,re.S).group()
# The matches above start at the first bracket; select the individual display.
def tagged_display(text,tag):
    return next(m.group() for m in re.finditer(r'\\\[.*?\\\]',text,re.S) if r'\tag{'+tag+'}' in m.group())
eq11=tagged_display(dual_local,'A.J.11')
eq12=tagged_display(dual_local,'A.J.12')
eqrc=tagged_display(blocks['cdp:st:A.5.9'],'A.RC.3')
eqrt=tagged_display(blocks['cdp:st:A.5.16'],'A.RT.5')
blocks[dual_id]=r'''\begin{lemma}[Conductor duality and its section maps]\hypertarget{tag-P222}{}\label{lem:II:conductor-duality}
\StatementRecord{lem:II:conductor-duality}{proved}{P222}{\cite[Proposition~2.3, p.~703, and Theorem~2.6, pp.~704--705]{Reid1994Nonnormal}}
Let $\eta:T\to S$ be the finite normalization of a reduced Gorenstein complex surface. Put $\mathcal B=\eta_*\OO_T$, $\mathcal Q=\mathcal B/\OO_S$, $\mathfrak c=\operatorname{Ann}(\mathcal Q)$, and $\Gamma=\operatorname{Spec}_S(\OO_S/\mathfrak c)$. The conductor scheme $\Gamma$ is Cohen--Macaulay of pure dimension one wherever nonempty, and its dualizing sheaf gives the canonical normalization sequence and comparison
'''+eqrc+r'''
For a local ring $R=\OO_{S,p}$, its semilocal normalization $\overline R$, $A=R/\mathfrak c$ and $Q=\overline R/R$, the local comparisons are
'''+eq11+'\n'+eq12+r'''
The endomorphism equality is the multiplication map. On $T$, with $\mathfrak c_T$ the conductor ideal, finite duality gives
'''+eqrt+r'''
For compact $S$, these maps induce
\begin{equation}
 H^0(S,\mathcal Q)^\vee\simeq H^1(\Gamma,\omega_S|_\Gamma).
 \label{eq:II:conductor-section-duality}
\end{equation}
\end{lemma}
\begin{proof}
The finite-duality and subadjunction maps are those of
\cite[Proposition~2.3 and its proof, p.~703; Theorem~2.6 and its proof, pp.~704--705]{Reid1994Nonnormal}.
Their local form applies to the analytic rings here as follows. The normalization $\overline R$ is maximal Cohen--Macaulay over the two-dimensional Gorenstein ring $R$. A homomorphism $\overline R\to R$ is multiplication in the total quotient ring, and its multipliers are exactly $\mathfrak c$. Applying $\operatorname{Hom}_R(-,R)$ to $0\to R\to\overline R\to Q\to0$ gives \eqref{cdp:eq:A.J.11}; the positive Ext groups of $\overline R$ vanish. The depth lemma makes the nonzero $Q$ Cohen--Macaulay of dimension one. Gorenstein biduality in that dimension is $M\mapsto\operatorname{Ext}_R^1(M,R)$, so it makes $A$ Cohen--Macaulay and gives \eqref{cdp:eq:A.J.12}. Duality identifies its endomorphism ring with $\operatorname{End}_A(A)=A$, through multiplication. Applying the same duality to $0\to\mathfrak c\to R\to A\to0$ identifies the first arrow of \eqref{cdp:eq:A.RC.3} with the original inclusion $R\hookrightarrow\overline R$. Tensoring by the invertible dualizing sheaf supplies exactly the displayed global twists and \eqref{cdp:eq:A.RT.5}.

Finally $\mathcal Ext^1_S(\mathcal Q,\omega_S)=\omega_S|_\Gamma$, and the other sheaf Ext groups vanish. The local-to-global Ext sequence gives
$\operatorname{Ext}^2_S(\mathcal Q,\omega_S)=H^1(\Gamma,\omega_S|_\Gamma)$.
Serre duality on compact $S$ identifies its left side with $H^0(S,\mathcal Q)^\vee$, proving \eqref{eq:II:conductor-section-duality}.
\end{proof}

'''
log('D12',dual_id,'Conductor-duality calculations in A.5.7, A.5.9, A.5.14 and A.5.16',blocks[dual_id],
    'One proved owner now gives the exact multiplier, Ext, canonical-module, endomorphism and global section maps. The compact section comparison retains its compactness condition; the local ring comparisons retain their analytic generality.')
for ident,text in [('cdp:st:A.5.7',eq11+'\n'+eq12),('cdp:st:A.5.9',eqrc),('cdp:st:A.5.16',eqrt)]:
    move_log(ident,dual_id,text,'Transferred the labelled duality identity to its common proved owner; applications retain their own hypotheses and maps.')
new_local=r'''\item Write $R=\mathcal O_{S,p}$, let $\overline R$ be its finite semilocal normalization, and put
\[
 A=R/\mathfrak c,\qquad \overline A=\overline R/\mathfrak c,
 \qquad Q=\overline R/R=\overline A/A.
\]
The normalization is a product of regular two-dimensional local analytic rings. The local maps in \cref{lem:II:conductor-duality} give $Q\simeq\omega_A$ and $\operatorname{End}_A(Q)=A$ by \eqref{cdp:eq:A.J.11}--\eqref{cdp:eq:A.J.12}.

'''
replace('cdp:st:A.5.7',dual_local,new_local,'D12','Replaced the repeated duality proof by the exact common local maps on the same rings R, normalization, A and Q.')
oldrc=piece('cdp:st:A.5.9',r'\item Write $\mathcal B=',r'Adjunction makes $\omega_S$')
replace('cdp:st:A.5.9',oldrc,r'''\item Write $\mathcal B=\eta_*\OO_T$ and $\mathcal Q=\mathcal B/\OO_S$. Apply \cref{lem:II:conductor-duality} to this normalization. Equation~\eqref{cdp:eq:A.RC.3} identifies $\mathcal Q$ with $\omega_\Gamma\otimes\omega_S^{-1}|_\Gamma$ through the original inclusion $\OO_S\hookrightarrow\mathcal B$.
''','D12','The conductor normalization inclusion and dualizing twist are applied from their unique earlier owner.')
oldrt=piece('cdp:st:A.5.16',r'\item We first prove a useful fact',r'A nonzero global section of $\omega_T$')
replace('cdp:st:A.5.16',oldrt,r'''\item Apply the finite-duality inclusion \eqref{cdp:eq:A.RT.5} of \cref{lem:II:conductor-duality} to $\eta:T\to S$.
''','D12','Moved the common normal dualizing-sheaf inclusion to the duality owner and retained its torsion-line vanishing application here.')
old14=piece('cdp:st:A.5.14','To identify the conductor-duality map,','Taking dimensions gives')
replace('cdp:st:A.5.14',old14,
        r'The section-duality isomorphism \eqref{eq:II:conductor-section-duality}, for this $\eta$ and $\Gamma$, identifies $H^0(S,\mathcal Q)^\vee$ with $H^1(\Gamma,\omega_S|_\Gamma)$. ',
        'D12','The common Ext and global Serre-duality derivation now has one owner. The injection from constants and the numerical bound remain in this proof.')
replace('cdp:st:A.5.16',r'The exact conductor-duality isomorphism proved in \ref{cdp:st:A.5.9} is',
        r'The conductor-duality map of \cref{lem:II:conductor-duality}, applied to this normalization, is',
        'D14','Updated the proof-owner citation after transferring its complete duality derivation.')

# The published duality typo is a numbered mathematical remark, with one exact
# source locator. Its unrelated retrospective synopsis is removed.
orphan=blocks['cdp:st:A.5.1'][blocks['cdp:st:A.5.1'].index('The line in the printed proof'):].strip()
remark_id='rem:II:normal-duality-endpoint'
blocks[remark_id]=r'''\begin{remark}[The top dualizing-sheaf group]\hypertarget{tag-P223}{}\label{rem:II:normal-duality-endpoint}
\StatementRecord{rem:II:normal-duality-endpoint}{proved}{P223}{}
For a connected compact normal complex surface $T$, Serre duality gives
$H^2(T,\omega_T)^\vee\simeq H^0(T,\OO_T)=\C$.
This is the group printed as zero in the proof of
\cite[Proposition~7.3, Step~1, p.~693]{CDP2020}.
Replacing $\omega_T$ there by $\OO_T$ recovers the vanishing stated at the start of that step. The genus-one ruled case and its twisted cotangent sections are computed in \cref{cdp:st:A.4.2}; the unitary local-system proof of the proposition is \cref{cdp:st:A.4.9}.
\end{remark}

'''
replace('cdp:st:A.5.1',orphan,'','D13','Moved the exact published Serre-duality comparison into a numbered remark; removed the retrospective W/(11) synopsis and the incorrect future-direction wording.')
log('D18',remark_id,orphan,blocks[remark_id],'Visually opened journal p.693, Proposition 7.3 Step 1. The stated duality morphism proves the nonzero group; the genus-one and local-system results remain their earlier owners.')

# The parent prepared and exposed-read this common analytic intersection proof.
matrix_id='lem:II:exceptional-intersection'
blocks[matrix_id]=(ROOT/'agents/continuation3_root/S6_SERIES_PUBLISH_exceptional_intersection.tex').read_text().strip()+'\n\n'
# Root records its own admission as II-C3-EXCEPTIONAL-OWNER-01/02.
# Keep the exposed receiving event below, without a duplicate insertion row.
old3dual=piece('cdp:st:A.5.3',r'\item Finite duality gives',r'On a normal surface a rank-one maximal Cohen--Macaulay module is reflexive')
replace('cdp:st:A.5.3',old3dual,
        r'''\item Apply the finite-duality map of \cref{lem:II:conductor-duality} to the normalization component $T_i$. It identifies $\omega_{T_i}$ with $\mathfrak c_i\otimes\eta^*\omega_S$, where $\mathfrak c_i$ is the conductor ideal on $T_i$. The multiplier identification there makes $\mathfrak c_i$ maximal Cohen--Macaulay. ''',
        'D12','The same multiplier and maximal-Cohen--Macaulay calculation now has the common proved owner P222. Its application retains the conductor ideal on the same normalization component and the codimension-one definition of the effective divisor.')
oldsign=piece('cdp:st:A.5.3',r'To see that $a\ge0$',r'Thus $D_i=')
replace('cdp:st:A.5.3',oldsign,
        r'By \cref{lem:II:exceptional-intersection}, $a=-M^{-1}v$ has nonnegative entries on each connected exceptional block. ',
        'D12','The exact same exceptional matrix equation now uses the common proved inverse-positivity statement, removing the duplicate sign argument.')
replace('cdp:st:A.5.3',r"The conductor duality and effective exceptional comparison also appear, for projective surfaces with trivial dualizing sheaf, in \cite[Lemma~1.1 and Corollary~1.4]{Furushima1993}; the argument here supplies the maps and does not use that paper's additional K3-type hypothesis $h^1(\OO_S)=0$.",
        r'For projective surfaces with trivial dualizing sheaf, the conductor and effective exceptional comparisons are \cite[Lemma~1.1 and Corollary~1.4]{Furushima1993}. The preceding finite-duality and exceptional-matrix maps apply to the analytic Gorenstein surface of the statement.',
        'D02','Replaced the defensive hypothesis contrast by the exact source class and the displayed analytic maps establishing the present scope.')

# Cite the opened exact-curvature theorem instead of repeating its proof.
oldflat=piece('cdp:st:A.5.4',r'\item We record the precise flatness implication.',r'\item The divisor $D_i$')
newflat=r'''\item Let $F_G$ be the Chern curvature of a Hermitian metric on $h_i^*G$. Since $H^2(Y,\Z)=0$, the real closed form $\mathrm iF_G$ is exact. Its pairing with $\omega$ is zero by the degree calculation. The second exact sequence in \cite[Lemma~2.3(1), p.~5, arXiv v3]{Teleman2006} therefore gives a real function $u$ with $\mathrm iF_G=\mathrm i\partial\bar\partial u$. With the Chern-curvature convention $F=-\partial\bar\partial\log h$, replacing the line metric $h$ by $e^u h$ changes its curvature to $F_G-\partial\bar\partial u=0$. Its Chern connection is consequently flat and unitary.

'''
replace('cdp:st:A.5.4',oldflat,newflat,'D17','Opened the complete Teleman Lemma 2.3 and proof on author-version pp.5–6. The exact-curvature kernel-to-potential map is used with the same Gauduchon metric; the metric change is explicit. Removed the repeated anti-selfdual/Stokes proof.')
replace('cdp:st:A.5.4',r'The degree of a line bundle is the integral of its real Chern curvature against $\omega$;',
        r'For Chern curvature $F_G$, use $\deg_\omega G=(2\pi)^{-1}\int_{Z_i}\mathrm iF_G\wedge\omega$;',
        'D20','Specified the same curvature-to-degree map used in A.5.6. Multiplication by the fixed positive factor does not change any zero-degree or nonnegativity assertion.')
replace('cdp:st:A.5.4',r'This is \cite[Lemma~2.3(2)]{Teleman2006} after multiplication by the fixed scalar $\mathrm i$, or follows from the pluriharmonic maximum principle.',
        r'The injective map is \cite[Lemma~2.3(2), pp.~5--6, arXiv v3]{Teleman2006}, after multiplication by the fixed scalar $\mathrm i$ to match the convention $u\mapsto\exp(2\pi\mathrm i u)$.',
        'D18','The source tangent map and the exact scalar identifying the exponential conventions are specified at their opened locus.')
replace('cdp:st:A.5.6','It follows directly in a holomorphic frame by differentiating the Hermitian norm; thus no Kähler identity is being assumed.',
        'Differentiating the Hermitian norm in a holomorphic frame gives this pointwise Chern-connection identity.',
        'D02','The positive local frame calculation states the reason for the identity; removed the defensive comparison.')
replace('cdp:st:A.5.6',r'The Chern curvature is therefore exact, and the exact-curvature argument in \ref{cdp:st:A.5.4} again produces a flat unitary connection.',
        r'The Chern curvature is therefore exact. Apply the kernel-to-potential map of \cite[Lemma~2.3(1), p.~5, arXiv v3]{Teleman2006} and the explicit metric change in \cref{cdp:st:A.5.4} to obtain a flat unitary Chern connection.',
        'D17','Uses the same opened exact-curvature result after the integral class becomes torsion; real exactness is the hypothesis used by the source.')
replace('cdp:st:A.5.6',r'''Indeed the difference from this constant has integral zero, and the image of $u\mapsto\mathrm i\Lambda_\omega\partial\bar\partial u$ is precisely the mean-zero functions for a Gauduchon metric; this is the scalar equation used in \cite[Lemma~2.3]{Teleman2006}. The Hermitian line metric may therefore be rescaled by the corresponding $e^{-u}$.''',
        r'''The proof of \cite[Lemma~2.3(1), p.~5, arXiv v3]{Teleman2006} identifies the image of $u\mapsto\mathrm i\Lambda_\omega\partial\bar\partial u$ with the functions of integral zero for a Gauduchon metric. Solve
\[
 \mathrm i\Lambda_\omega\partial\bar\partial u
       =c_P-\mathrm i\Lambda_\omega F_P.
\]
For the curvature convention $F=-\partial\bar\partial\log h$, replacing $h$ by $e^{-u}h$ adds $\partial\bar\partial u$ to the curvature, giving the stated constant.''',
        'D18','Applied the opened scalar elliptic equation with its exact mean-zero right side and metric-rescaling map. The sign now follows directly from the same Chern-curvature convention as A.5.4.')
replace('cdp:st:A.5.4',r'\cite[Lemma~2.3(1)--(2)]{Teleman2006}; \cite[Lemma~2.3(2)]{Teleman2006}',
        r'\cite[Lemma~2.3(1)--(2), pp.~5--6, arXiv v3]{Teleman2006}',
        'D18','Removed the duplicate Teleman citation in the hidden dependency record and identified the exact opened author-version locus; the displayed statement-header form remains unchanged.')

# The elementary ruled rigidity argument is common to the cusp, tacnode and
# triple conclusions. Keep its entire geometric proof once.
rigid_id='lem:II:elliptic-ruled-boundary'
blocks[rigid_id]=r'''\begin{lemma}[A square-zero elliptic section and its conductor]\hypertarget{tag-P226}{}\label{lem:II:elliptic-ruled-boundary}
\StatementRecord{lem:II:elliptic-ruled-boundary}{proved}{P226}{\cref{lem:II:exceptional-intersection}}
Let $\mu:Z\to T$ be the minimal resolution of a normal compact complex surface, with an irrational ruling $p:Z\to B$ over an elliptic curve. Suppose that every $\mu$-exceptional curve is vertical. Let $C$ be a section with $C^2=0$, and let $V$ be an effective vertical divisor disjoint from $C$, with $c_1(K_Z+2C+V)=0$ in rational cohomology. Then $V=0$, $Z$ is a minimal ruled bundle, and $\mu$ is an isomorphism.
\end{lemma}
\begin{proof}
Contract the vertical ruling $(-1)$-curves to a bundle $\rho:Z\to Z_0$ over $B$, and put $C_0=\rho(C)$, $V_0=\rho_*V$. The image $C_0$ is a section. Its self-intersection is $C_0^2=C^2+n=n\ge0$, where $n$ counts the blowup centres on the successive section transforms. Pushing the canonical-boundary class forward and using adjunction on the elliptic section gives
\[
 0=(K_{Z_0}+2C_0+V_0)\cdot C_0
   =n+V_0\cdot C_0.
\]
The divisor $V_0$ is an effective sum of fibres, so $n=0$ and $V_0=0$. Thus $C=\rho^*C_0$ and $V$ is $\rho$-exceptional. In
$K_Z=\rho^*K_{Z_0}+E_\rho$, the divisor $E_\rho$ is effective and positive on every exceptional prime. The class of $E_\rho+V$ is numerically zero. The total transforms of the point-blowup exceptional curves form an orthogonal basis with square $-1$, so their intersection matrix is negative definite. Therefore $E_\rho+V=0$. Effectivity gives $E_\rho=V=0$, and $\rho$ is an isomorphism.

Every vertical irreducible curve of this bundle is a fibre and has square zero. By \cref{lem:II:exceptional-intersection}, an exceptional curve of $\mu$ belongs to a negative-definite block, so no such fibre is exceptional. The proper map $\mu$ has finite fibres and is bimeromorphic. It is therefore finite, and normality of $T$ makes it an isomorphism.
\end{proof}

'''
log('D12',rigid_id,'A.5.20 proof Steps 3–4 and repeated final ruled comparisons in A.5.18/A.5.19',blocks[rigid_id],
    'Collected the common minimal-resolution, square-zero section and effective vertical-boundary argument with its exact hypotheses. The point-blowup and normal finite-birational morphisms are retained.')
old20=piece('cdp:st:A.5.20',r'\item Contract the vertical $(-1)$-curves',r'\item Finite duality on the smooth normalization')
new20=r'''\item Apply \cref{lem:II:elliptic-ruled-boundary} to $\mu:Z'\to T$, $p':Z'\to B$, $C'$ and $V'$. The previous step gives every hypothesis: $B$ is elliptic, $(C')^2=0$, $V'$ is effective, vertical and disjoint from $C'$, the canonical-boundary class is zero, and the exceptional curves of the minimal resolution are vertical. Thus $V'=0$ and $T=Z'$ is a smooth minimal ruled bundle.

'''
replace('cdp:st:A.5.20',old20,new20,'D12','Moved the complete common ruled argument to P226 and its repeated analytic Mumford proof to the earlier P243. The application specifies the same minimal resolution, section and vertical divisor.')
replace('cdp:st:A.5.18',r'''The nef-generation argument of
\cite[Proposition~4.14(ii), pp.~102--103, and the lemma in
\S4.17, p.~105]{Reid1997Chapters} has the following analytic
form on this minimal resolution.''',r'''The degree map on exceptional cycles and nef generation over an affine rational surface singularity are \cite[Proposition~4.14(ii), pp.~91--92, and the lemma in \S4.17, pp.~94--95, arXiv v1]{Reid1997Chapters}. On the present analytic minimal resolution the relative evaluation map is obtained as follows.''',
        'D18','Opened the complete Artin degree-map proposition and nef-generation lemma with proofs in arXiv alg-geom/9602006v1. The cited source has an affine algebraic base. Retained the complete Stein-neighbourhood, curvette, exponential-sequence and evaluation-map argument needed to identify the analytic pullback conductor ideal; it cannot be replaced by a numerical divisor equality alone.')

# Keep the labelled blowdown identity A.T.22 in its actual application, but
# obtain minimality once from the common lemma.
oldcollapse=piece('cdp:st:A.5.18',r'No ruling $(-1)$-curve can meet $C_{\min}$:',r'Finally $\eta$ is an isomorphism away from')
eqt22=tagged_display(oldcollapse,'A.T.22')
newcollapse=r'''For a ruling blowdown $\sigma:W\to W'$, with exceptional coefficient $a$ and centre multiplicity $d$ of $D'=\sigma_*D_W$, the canonical-divisor comparison is
'''+eqt22+r'''
Intersection with $E$ gives $a=d-1$. Applied to the minimal-resolution data above, \cref{lem:II:elliptic-ruled-boundary} gives $V_{\min}=0$, makes $Z_{\min}$ a minimal ruled bundle and makes $\pi_{\min}$ an isomorphism. Every hypothesis is supplied by $C_{\min}^2=0$, disjointness from $V_{\min}$, the canonical class just identified, and the vertical exceptional curves.
'''
replace('cdp:st:A.5.18',oldcollapse,newcollapse,'D12','Retained the exact labelled point-blowup identity for later applications. The common proof of minimality and the absence of exceptional curves is now P226, with all its receiving hypotheses listed.')

# The explicit conductor-pole example is a mathematical example, not the final
# paragraph of the ordinary-triple proof item.
example_id='ex:II:conductor-pole'
jet_example=piece('cdp:st:A.5.5','The pole allowance in \\eqref{cdp:eq:A.J.5}',r'\end{enumerate}')
blocks[example_id]=r'''\begin{example}[A conductor pole on a singular critical curve]\hypertarget{tag-P224}{}\label{ex:II:conductor-pole}
\StatementRecord{ex:II:conductor-pole}{proved}{P224}{}
Put $h=z^2-x^3$, $D=(h,w)=0$ in $\mathbb C^3$, and
\[
 f=xw^2+2zwh+x^2h^2+h^3.
\]
Its radical cubic on the normalization of $D$ has a pole of order two, and multiplication by the square of the conductor generator gives the holomorphic jet in \eqref{cdp:eq:A.J.4}.
\end{example}
\begin{proof}
On the normalization $x=s^2,z=s^3$, the quadratic class is $s^2(w+sh)^2$. Completing the square on $D_{\rm reg}$ gives
\[
 f=x\left(w+\frac zx h\right)^2+
                   \left(1-\frac1x\right)h^3.
\]
Thus the radical cubic has a pole of order two at $s=0$. The conductor generator is $d=x=s^2$, and
\[
 x^2f-x(xw+zh)^2=x(x-1)h^3\in I_D^3.
\]
This is the conductor-cleared cubic of \eqref{cdp:eq:A.J.4} for the specified map and generator.
\end{proof}

'''
replace('cdp:st:A.5.5',jet_example,'','D13','Moved the entire local example out of the last proof item into its own numbered statement and proof; its equation, normalization, conductor generator and pole order are retained.')
log('D14',example_id,jet_example,blocks[example_id],'The subsidiary local example has its own owner following the conductor-cleared jet theorem.')
reid_orphan=blocks['cdp:st:A.5.5'][blocks['cdp:st:A.5.5'].index('The local calculation below'):].strip()
replace('cdp:st:A.5.5',reid_orphan,'','D13','Moved the Reid credit into the proof that uses the conductor derivation; removed the orphan process/scope paragraph.')
replace('cdp:st:A.5.7',r'\begin{proof}',
        r'''\begin{proof}
The graph of a rational derivation on a square-zero conductor extension is the comparison of \cite[\S3.9, pp.~716--717; \S4.4--4.8, pp.~720--724]{Reid1994Nonnormal}. The following local maps identify that graph and its canonical module in the analytic rings of the statement.
''','D18','Opened Reid’s complete derivation proposition and characteristic-zero pole/trace calculation. The semilocal analytic canonical-module proof is retained with its exact rings and maps; no projective classification is asserted for it.')

# Subsidiary Milnor homotopy and boundary calculations now have one statement.
rank_id='prop:II:binomial-milnor-rank'
rank_proof=piece('cdp:st:A.5.15',r'\item When $\gcd(a,b,c)=1$',r'\item Let $j:M\hookrightarrow Y_t$')
blocks[rank_id]=r'''\begin{proposition}[The homotopy and intersection form of an irreducible binomial Milnor fibre]\hypertarget{tag-P225}{}\label{prop:II:binomial-milnor-rank}
\StatementRecord{prop:II:binomial-milnor-rank}{proved}{P225}{\cite[Theorem~L1 and Example~2.4(a), pp.~2--3]{Nemethi1991Join}; \cite[Theorem~4.1 and Lemma~4.6]{MPW2005Hirzebruch}}
Let $a\ge2$, $b,c\ge1$, $\gcd(a,b,c)=1$, and $d=\gcd(b,c)$. For the Milnor fibre $M$ of $x^a-y^bz^c$, the homotopy type is \eqref{cdp:eq:A.J.35}, and its rational intersection morphism has rank $a-1$. Every class in $H_2(M,\Z)$ is a sum of spherical classes. For $a=2$, $b=1$, $c=\ell\ge1$, its boundary is $L(2\ell,1)$ and the rank-one integral intersection form has absolute determinant $2\ell$.
\end{proposition}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
'''+rank_proof+r'''\end{enumerate}
\end{proof}

'''
replace('cdp:st:A.5.15',rank_proof,'','D14','Separated the subsidiary join, boundary and full intersection-rank calculation from the explicit sphere proof of exclusion. Its exact gcd hypothesis, all conclusions and every labelled formula are retained in a proved proposition.')
move_log('cdp:st:A.5.15',rank_id,rank_proof,'The full homotopy/boundary calculation and its stable equation identities now belong to P225.')
oldcw=piece(rank_id,'The quotient map\n'+r'$J\to J/\operatorname{Cone}_1H$','This proves\n\\[')
newcw=r'''The quotient map $J\to J/\operatorname{Cone}_1H$ collapses a contractible CW subcomplex and is a homotopy equivalence by \cite[Propositions~0.16--0.17, pp.~15--16]{Hatcher2002}. Its quotient is a wedge of $a-1$ unreduced suspensions of $H$. Each suspension has two vertices, $d$ meridian edges and $d$ two-cells attached along a meridian followed by its reverse. Collapse one meridian by the same quotient theorem. The remaining $d-1$ edges are loops, and the backtracking attaching maps are homotopic to constants; \cite[Proposition~0.18, p.~16]{Hatcher2002} identifies the resulting attachment with $d$ spheres. '''
replace(rank_id,oldcw,newcw,'D17','Visually opened the complete Hatcher Propositions 0.16–0.18 and proofs on pp.15–16. Replaced their repeated homotopy-extension proof by the exact quotient and attachment maps; retained the explicit CW cells used to compute this Milnor fibre.')

# The two-branch delta-two classification is also used by the triple proof.
curve_id='lem:II:delta-two-curve-rings'
curve_begin=r'\item For a unibranch'
curve_end='The local reduced equation $f_0$ lies in $I^2$ in each case.'
curve_part=piece('cdp:st:A.5.18',curve_begin,curve_end)
blocks[curve_id]=r'''\begin{lemma}[Curve rings of delta at most two with at most two branches]\hypertarget{tag-P228}{}\label{lem:II:delta-two-curve-rings}
\StatementRecord{lem:II:delta-two-curve-rings}{proved}{P228}{}
A reduced analytic curve germ in a smooth threefold, of delta invariant at most two and with at most two normalization branches, is planar or has one of the two rings and embedded ideals in \eqref{cdp:eq:A.T.14}. Every planar case is a local complete intersection in the threefold. Each of the two nonplanar cases has delta invariant two.
\end{lemma}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
'''+curve_part.replace('Three branches are excluded by $\\beta\\le1$.','')+r'''\end{enumerate}
\end{proof}

'''
replace('cdp:st:A.5.18',curve_part,r'''\item By \cref{lem:II:delta-two-curve-rings}, the remaining non-lci cases are the two analytic rings in \eqref{cdp:eq:A.T.14}. Each consumes the whole delta budget at one point. Use the ambient coordinates and ideals specified there.

''','D14','The complete local ring classification and embedding maps have a single proved owner before both the tacnode and ordinary-triple uses.')
move_log('cdp:st:A.5.18',curve_id,curve_part,'Moved the complete classification, its ambient coordinate maps and equation A.T.14 to the shared curve-ring lemma.')
replace('cdp:st:A.5.19',r'''The one- and two-branch analytic
classification is proved in \ref{cdp:st:A.5.18},
preceding \eqref{cdp:eq:A.T.14}.''',
        r'The one- and two-branch analytic classification is \cref{lem:II:delta-two-curve-rings}, with its embedded ideals in \eqref{cdp:eq:A.T.14}.',
        'D14','Directs the ordinary-triple proof to the exact shared classification owner.')
replace('cdp:st:A.5.19',r'''so their lifts
are ambient coordinates as in \ref{cdp:st:A.5.18}.''',
        r'so their lifts are ambient coordinates by the inverse-function argument of \cref{lem:II:delta-two-curve-rings}.',
        'D14','Preserves the explicit cotangent-basis-to-coordinate map at the third, three-axis germ.')

# The rational-cover extension at the end of the tacnode proof is a distinct
# conclusion with its own precise hypotheses and proof.
cover_id='cor:II:nonplanar-tacnode-cover'
cover_part=piece('cdp:st:A.5.18',r'\paragraph{Connected double covers',r'\end{enumerate}')
blocks[cover_id]=r'''\begin{corollary}[Connected double covers of the nonplanar delta-two images]\hypertarget{tag-P227}{}\label{cor:II:nonplanar-tacnode-cover}
\StatementRecord{cor:II:nonplanar-tacnode-cover}{proved}{P227}{\cref{cdp:st:A.5.18,cdp:st:A.5.17}}
Let $f:Y\to C_0$ be a proper map from a smooth compact complex threefold with $b_2(Y)=0$, connected fibres and smooth general fibre a complex two-torus. Let $mS$ be a full fibre with irreducible reduced support. Let $D\subset\operatorname{Sing}S$ have generic ordinary-tacnode transversal, normalization $\Sigma\simeq\PP^1$, and one singular point, of one of the two types in \eqref{cdp:eq:A.T.14}. The normalized conductor over $D$ has no connected component mapping to $\Sigma$ with degree two.
\end{corollary}
\begin{proof}
Use the same conormal-image bundle
$K=\operatorname{im}(\nu^*(I_D/I_D^2)\to\nu^*\Omega_Y^1)$ and $N=K^*$ as in \eqref{cdp:eq:A.T.18}. The quartic invariant gives the degree-two function-field extension by $\sqrt{-\Delta}$, as in the comparison preceding \eqref{cdp:eq:A.T.7}. For a connected cover $C\to\Sigma$, Riemann--Hurwitz gives branch degree $2g(C)+2$.

In the cusp-plus-line case, \eqref{cdp:eq:A.T.19} and the pole correction \eqref{cdp:eq:A.T.21} give a square line of degree $2q_0\le0$. Its nonzero section has no odd divisor, contradicting the positive branch degree. In the space-cusp case, \eqref{cdp:eq:A.T.20} gives
\[
 2g(C)+2\le4+2q_0,\qquad
 2g(C)+2\le-2q_0+1.
\]
Their sum forces $g(C)=0$, and the two inequalities then force the integer $q_0=-1$. The cleared quartic has degree two and exactly two simple branch points. Only one lies over the singular image point. The other is a smooth simple branch point, whose exact coordinate reduction \eqref{cdp:eq:A.T.10}--\eqref{cdp:eq:A.T.12} contradicts \cref{cdp:st:A.5.15}. The nonzero-Hessian input in this branch count is \cref{cdp:st:A.5.17}; all these local maps are those of the stated full torus fibre.
\end{proof}

'''
replace('cdp:st:A.5.18',cover_part,'','D13','Promoted the additional connected rational-cover conclusion, which was hidden in a paragraph at the end of the tacnode proof, to a corollary with its full compact-curve and torus-fibre hypotheses. Removed the repeated final quotient-versus-normalization commentary; the exact map A.T.2 remains in the proof.')
log('D14',cover_id,cover_part,blocks[cover_id],'The two already proved pole inequalities now show the exclusion for every covering genus in one separate proof. No ruling or positive-genus hypothesis is silently transferred to the rational-cover case.')

# Break the former oversized last item into the actual stages of its proof.
for old,new in [
 ('At these non-lci points, put','\\item At these non-lci points, put'),
 ('We bound its poles using transverse affine','\\item We bound its poles using transverse affine'),
 ('For the cusp-plus-line germ, the corresponding','\\item For the cusp-plus-line germ, the corresponding'),
 ('Factor $\\pi$ through the minimal','\\item Factor $\\pi$ through the minimal'),
]:
    replace('cdp:st:A.5.18',old,new,'D14','Separated the conormal determinant, pole estimates, second local ring, and minimal-resolution conclusion into their own proof steps without altering their mathematical content.')

# Each local comparison is a numbered example, with its whole coordinate and
# conductor calculation. Program locations move to the independently prepared
# end-of-paper table, whose repository scopes have been verified.
nodal_id='ex:II:nodal-triple-affine-fibre'
nodal_orphan=blocks['cdp:st:A.5.19'][blocks['cdp:st:A.5.19'].index('The singular rational possibilities cannot be'):].strip()
nodal_math=nodal_orphan[:nodal_orphan.index('Exact ideal, normal-coordinate')].strip()
ua6=tagged_display(nodal_math,'A.U.6')
ua7=tagged_display(nodal_math,'A.U.7')
blocks[nodal_id]=r'''\begin{example}[A nodal triple curve with an aspherical affine fibre]\hypertarget{tag-P229}{}\label{ex:II:nodal-triple-affine-fibre}
\StatementRecord{ex:II:nodal-triple-affine-fibre}{proved}{P229}{}
The polynomial
'''+ua6+r'''
has ordinary-triple transversals along the smooth part of the nodal curve $D=(x,yz)=0$, and ordinary-double transversals along the punctured line $y=z=0$. Every fibre $f^{-1}(t)$ with $t\ne0$ is aspherical. Writing $f=P(x,yz)$ gives $P(X,V)=XV(X-V)$ and $P(1,0)=0$.
\end{example}
\begin{proof}
Put $v=yz$. The critical equations are
\[
 f_x=v(2x-v),\qquad f_y=zx(x-2v),\qquad f_z=yx(x-2v).
\]
Their common zero set is $D\cup\{y=z=0\}$. Near a point of $D\setminus\{0\}$, either $y$ or $z$ is a coordinate unit, so $(x,v)$ are transverse coordinates and $f=xv(x-v)$ has three distinct tangent lines. At $(x,0,0)$ with $x\ne0$, its quadratic normal term is $x^2yz$, giving the ordinary double transversal.

For $t\ne0$, let $B_t=\{(x,v):xv(x-v)=t\}$. The maps
'''+ua7+r'''
are inverse holomorphic maps because $t\ne0$ forces $v$, $y$ and $z$ to be nonzero. The equations $v(2x-v)=x(x-2v)=0$ have no solution on $B_t$, so $B_t$ is a smooth affine curve. It and $\C^*$ are aspherical, and their product proves the assertion.

The deformation obtained by replacing $yz$ by $yz-s$ is
$f_s=x(yz-s)(x-yz+s)$. Along $y=z=0$ one has
$\partial f_s/\partial x=-s(2x+s)$. At a fixed nonzero $x$ this is nonzero for sufficiently small $s\ne0$, whereas that point belongs to the critical line for $s=0$. Thus this deformation changes that critical line on the boundary; the fixed-boundary comparison in \cref{cdp:st:A.5.17} requires the critical curves to remain there.
\end{proof}

'''
replace('cdp:st:A.5.19',nodal_orphan,'','D13','Moved the complete nodal ordinary-triple example to a numbered owner in the earlier local-obstruction subsection. The inverse product maps, transverse singularity types and boundary-deformation comparison are retained; the new displayed derivative gives the exact reason for the boundary change.')
move_log('cdp:st:A.5.19',nodal_id,nodal_math,'The aspherical nodal-triple model has one numbered statement and proof before the higher-jet consumers; equations A.U.6 and A.U.7 retain their identities.')
for name,owner in [('E_triple_images.py',nodal_id),('E_triple_images.out',nodal_id),('A_low_delta_cusp.py','cdp:st:A.5.19')]:
    log('D09','cdp:st:A.5.19',r'\path{code/'+name+'}',
        'Programs table: '+name+'; scope '+owner,
        'Removed the body path. The exact repository bytes and appendix row are prepared in agents/continuation3_provenance/S6_SERIES_PUBLISH_c3_provenance_extra_program_rows.tex; the .out is associated with its producing E_triple_images.py row.',
        'Programs table')
log('D11',nodal_id,'This is a local model, not a compact $b_2=0$ example.',
    'The statement specifies the polynomial, its critical curves and its regular affine fibres.',
    'The numbered statement states the local affine scope positively; no compact example is claimed.')
orphan21=blocks['cdp:st:A.5.21'][blocks['cdp:st:A.5.21'].index('The condition $P(1,0)'):].strip()
first21=orphan21[orphan21.index('The homogeneous germ'):orphan21.index('The following different scalar-zero model')]
second21=orphan21[orphan21.index('The following different scalar-zero model'):]
sphere_id='ex:II:vanishing-cubic-sphere'
aspherical_id='ex:II:vanishing-cubic-aspherical'
bp9=tagged_display(first21,'A.BP.9');bp10=tagged_display(first21,'A.BP.10')
bp11=tagged_display(second21,'A.BP.11');bp12=tagged_display(second21,'A.BP.12')
blocks[sphere_id]=r'''\begin{example}[A vanishing cubic jet with a spherical fibre class]\hypertarget{tag-P230}{}\label{ex:II:vanishing-cubic-sphere}
\StatementRecord{ex:II:vanishing-cubic-sphere}{proved}{P230}{\cref{cdp:st:A.5.21}}
The homogeneous polynomial
'''+bp9+r'''
has a cubic normal tensor along $(x,y)=0$ which vanishes at $z=0$. Its regular affine fibre $h=1$ contains a spherical class of square $-2$. Consequently every germ $u h^m$, where $u$ is a holomorphic unit and $m\ge1$, is excluded from a map with nearby smooth fibres complex two-tori.
\end{example}
\begin{proof}
On $xy\ne0$ put
\[
 v=x-y,\qquad Z=y(y+v)z+y^2(2y+v).
\]
Together with $y$ these are holomorphic coordinates, with inverse
$x=y+v$, $z=(Z-y^2(2y+v))/(y(y+v))$. Substitution gives
'''+bp10+r'''
Choose an arc between two roots of $y^4=1$ avoiding $y=0$ and the other roots. For continuous choices with $AB=1-y^4$ and $|A|=|B|=|1-y^4|^{1/2}$, the circles
\[
 v=\rho A e^{\mathrm i\theta},\qquad Z=\rho^{-1}B e^{-\mathrm i\theta}
\]
collapse at the endpoints to a matching sphere. Choose the positive constant $\rho$ small enough that $|v|<|y|/2$ along the arc. The sphere then lies in the stated coordinate chart. Each endpoint has linking number $-1$ by the coordinate calculation in \eqref{cdp:eq:A.BP.3}, so its square is $-2$.

Since $h$ has degree four, homothety shrinks the compact sphere into arbitrarily small neighbourhoods of the origin and sends its fibre value to the corresponding fourth power. For a unit $u$, choose a holomorphic root $a=u^{1/(4m)}$. The map $\Phi(x,y,z)=a(x,y,z)(x,y,z)$ satisfies $h(\Phi)^m=u h^m$ and has invertible derivative $a(0)I$ at the origin, so it is a local biholomorphism. Thus every full multiplicity has the same small spherical cycle. Its embedding in a nearby torus preserves its square, whereas its image in $H_2$ is zero because the torus has contractible universal cover. This contradicts the square $-2$.
\end{proof}

'''
blocks[aspherical_id]=r'''\begin{example}[A vanishing cubic jet with aspherical affine fibres]\hypertarget{tag-P231}{}\label{ex:II:vanishing-cubic-aspherical}
\StatementRecord{ex:II:vanishing-cubic-aspherical}{proved}{P231}{}
For
'''+bp11+r'''
the cubic normal tensor along $x=y=0$ vanishes at $z=0$, and every fibre $h^{-1}(t)$ with $t\ne0$ is aspherical. The quadratic surface branch has normalization $(v,u)\mapsto(v,vu,u^2)$ and conductor divisor $2(v=0)+2(u=0)$ in the full reduced surface. The conductor divisors on the other two normalization branches are $2(y=0)+(z=0)$ on $x=0$ and $(x=0)+2(y=0)$ on $z=0$.
\end{example}
\begin{proof}
For $h=t\ne0$, both $x$ and $z$ are nonzero. The coordinate substitution $u=y/x$, with inverse $y=xu$, gives $h=x^3z(u^2-z)$. Forgetting $x$ is a finite etale triple cover of $E=\{(z,u):z(u^2-z)\ne0\}$, since $x^3=t/[z(u^2-z)]$ has three distinct nonzero roots. The map
'''+bp12+r'''
is a finite etale double cover, with inverse branches given by $s^2=z$, $v=u/s$, and deck involution $(s,v)\mapsto(-s,-v)$. Its source is aspherical. Covering maps identify the universal covers, proving the same assertion for $E$ and for $h^{-1}(t)$.

The quadratic branch $y^2=x^2z$ has image ring $R=\C\{v,u^2,vu\}$ in $B=\C\{v,u\}$. It is finite because $u^2=z$, and birational because $u=y/x$ off $x=0$. Write $B=\C\{v,u^2\}\oplus u\C\{v,u^2\}$. Membership of both $b$ and $ub$ in $R$ is equivalent to divisibility of both coefficients by $v$, so the intrinsic conductor is $vB$.

For a reduced hypersurface $\prod_i f_i=0$, the conductor on the normalized $i$th branch is its intrinsic conductor multiplied by $\prod_{j\ne i}f_j$ restricted to that branch. Indeed, an ambient function vanishing on every other branch is divisible by that product, since the $f_j$ are distinct irreducibles in the regular local ring. Dividing its $i$th component by this nonzerodivisor identifies the conductor condition with the intrinsic condition $bB_i\subset R_i$. On the quadratic branch the other factors pull back to $vu^2$, giving $v^2u^2B$. On $x=0$ their product is $zy^2$, and on $z=0$ it is $xy^2$. These ideals give the stated divisors; their reduced supports are normal-crossing pairs.
\end{proof}

'''
replace('cdp:st:A.5.21',orphan21,'','D13','Moved both complete cubic-jet examples into numbered statements and proofs. Deleted the repeated scope synopsis after the grid proof; its exact polynomial relation P(X,V)=XV(X-V), P(1,0)=0 now stands in P229.')
move_log('cdp:st:A.5.21',sphere_id,first21,'The degree-four coordinate identity and matching sphere, including all units and full-fibre multiplicities, have one numbered owner.')
move_log('cdp:st:A.5.21',aspherical_id,second21,'The two finite covering maps, normalization map and all three conductor divisors have one numbered owner; the branchwise conductor multiplication map is made explicit.')
log('D12','cdp:st:A.5.21',orphan21[:orphan21.index(r'\paragraph{')],
    'P229 states the exact polynomial relation; the fixed-boundary and weighted-scaling arguments remain in A.5.21.',
    'Removed the repeated post-proof synopsis; the actual hypotheses and boundary maps remain in their statement and proof.')
for name,owner in [('E_binary_products.py','cdp:st:A.5.21'),('E_cubic_double.py',sphere_id+'; '+aspherical_id)]:
    log('D09','cdp:st:A.5.21',r'\path{code/'+name+'}',
        'Programs table: '+name+'; scope '+owner,
        'Removed the body program path; the exact repository row and mathematical scope were prepared and read by the provenance agent.',
        'Programs table')
log('D11',aspherical_id,'This is an exact local model, not a construction of a compact $b_2=0$ fibre. It shows why a vanishing cubic coefficient alone does not justify a local spherical-cycle exclusion.',
    'The numbered example states the polynomial, its finite covering maps, affine fibres and branch conductors.',
    'The complete affine scope and exact morphisms stand in the statement and proof; removed the repeated negative comparison.')

# Positive formulations of the exact scope already expressed by the hypotheses
# and maps. Each occurrence is logged separately.
cleanups=[
 ('cdp:st:A.5.8','We verify\nholomorphic descent, rather than only descending the\nunderlying continuous map.','The equality $\\pi_*\\OO_Z=\\OO_T$ gives holomorphic descent as follows.'),
 ('cdp:st:A.5.9',r'The proof forces $B$ and $\Gamma$ to be smooth elliptic curves,',r'The curves $B$ and $\Gamma$ are smooth elliptic curves,'),
 ('cdp:st:A.5.9',r'$Z=T$ to be minimal ruled,',r'$Z=T$ is minimal ruled,'),
 ('cdp:st:A.5.9','Thus no local-complete-intersection assumption on the original\nconductor image curve is needed in this reduced-scheme case.',''),
 ('cdp:st:A.5.11','fundamental groups, without any assertion that a finite\npoint-identification quotient has the same fundamental\ngroup as $\\Sigma$.','fundamental groups.'),
 ('cdp:st:A.5.12','The conductor image scheme itself is allowed to be\nnonreduced, and no local-complete-intersection assumption\nis imposed on its reduced components.','Here $\\Gamma$ denotes the full conductor image scheme, and its components are arbitrary reduced irreducible curves.'),
 ('cdp:st:A.5.12','First we determine exactly the needed canonical line on\nthe reduced support, without a multiplicity formula for\nthe direct image.','The canonical line on the reduced support is determined by evaluation.'),
 ('cdp:st:A.5.12','In particular no assertion $k=m-1$ is used.',''),
 ('cdp:st:A.5.13','each positive-genus component is smooth elliptic,\nwithout any lci or conductor-reducedness hypothesis.','each positive-genus component is smooth elliptic.'),
 ('cdp:st:A.5.7','No complete-intersection hypothesis on $D$ is required.',''),
 ('cdp:st:A.5.10','No local\ncomplete-intersection hypothesis on the image curve is\nrequired.',''),
 ('cdp:st:A.5.16',' No $\\OO_S$-module\nstructure on $\\mathcal V$ is asserted or needed.',''),
 ('cdp:st:A.5.16','We identify its support, rather than discarding exceptional\ncomponents.','The support is determined by the exceptional intersection equations.'),
 ('cdp:st:A.5.16','For completeness the bound on its arithmetic genus follows','The bound on its arithmetic genus follows'),
 ('cdp:st:A.5.21','The comparison with its constant\ninitial form is the explicit analytic family below.',''),
]
for ident,old,new in cleanups:
    if old in blocks[ident]:
        replace(ident,old,new,'D02','The unchanged statement hypotheses and explicitly constructed maps establish this scope. Removed a repeated negative or proof-process clause.')

replace('cdp:st:A.5.15',r'''The finite rank-drop hypothesis of
Proposition~\ref{night:P4.15} fails for this morphism.''','',
        'D14','This was only a closing comparison with a later finite-rank-drop hypothesis. The complete obstruction is already proved, and the exact normalization, conductor and maximal-minor ideal (u) calculation remain. Removing the comparison leaves no forward proof input; the parent approved this scope-preserving deletion.')
replace('cdp:st:A.5.2',r'In particular the assertion of CDP20 Proposition~4.11 holds without its monodromy-dependent restrictions on the smooth fibre.',
        r'The normal-surface smoothness step in \cite[proof of Proposition~4.11, p.~687]{CDP2020} follows under these numerical hypotheses.',
        'D18','Freshly opened the full printed Proposition 4.11 and proof on pp.686–687. Its full conclusion also excludes smooth normal fibre components using a further Picard argument; the present proposition supplies precisely the normal-surface smoothness step. Retained every stated geometric conclusion and corrected the scope of the literature comparison.')
oldcrepant=piece('cdp:st:A.5.9','Such a singularity is crepant on its minimal resolution:',r'Thus \eqref{cdp:eq:A.RC.1}')
replace('cdp:st:A.5.9',oldcrepant,
        r'The local rational-duality and exceptional-matrix comparison in the proof of \cref{cdp:st:A.5.2}, applied to this Gorenstein germ and its minimal resolution, gives $\omega_Z=\pi^*\omega_T$ there. ',
        'D12','The exact same local crepancy argument has already been proved in A.5.2. Its application here supplies rationality, the Gorenstein germ and the same minimal-resolution map, removing the repeated zero-divisor/intersection proof.')
replace('cdp:st:A.5.12',r'''\item The conductor is Cohen--Macaulay of dimension one,
and the exact duality comparison (A.RC.3) applies
without a reducedness assumption on $\Gamma$:
$\mathcal Q=\omega_\Gamma\otimes\omega_S^{-1}|_\Gamma$.
Serre duality on that curve therefore gives''',
        r'''\item Apply \cref{lem:II:conductor-duality} to the full conductor scheme $\Gamma$. Its section-duality map \eqref{eq:II:conductor-section-duality} gives''',
        'D12','Replaced the repeated curve-duality derivation by the earlier exact section-duality map on this full conductor scheme; the numerical inequality and restriction-to-component argument remain unchanged.')
replace('cdp:st:A.5.20',r'\SeriesRef{cdp:st:A.5.18}',r'\cref{lem:II:elliptic-ruled-boundary}',
        'D14','Updated the hidden dependency declaration to the actual earlier common ruled-boundary proof. The receiving proof no longer uses the later tacnode result.')
old9rigid=piece('cdp:st:A.5.9',r'\item Adjunction in',r'\item The constant-cusp computation')
replace('cdp:st:A.5.9',old9rigid,r'''\item Adjunction in \eqref{cdp:eq:A.RC.1} gives $V\cdot C=0$. Since $V$ is effective and vertical, it is disjoint from the section $C$. Apply \cref{lem:II:elliptic-ruled-boundary} to the minimal resolution $\pi:Z\to T$, its ruling, $C$ and $V$. The preceding step gives the elliptic base and $C^2=0$, the statement assumes vertical exceptional curves, and \eqref{cdp:eq:A.RC.1} gives the zero canonical-boundary class. Hence $V=0$, $Z$ is a minimal ruled bundle and $\pi$ is an isomorphism.

''','D12','The same square-zero elliptic-section and vertical-boundary argument now has one proved owner. This application gives every hypothesis on the exact original resolution, ruling, section and divisor, retaining Z=T and D_Z=2C.')

# The ruled descent proof is required first in the normal-surface argument.
old2descent=piece('cdp:st:A.5.2','The ruling is constant on each connected fibre of $\\pi$',
                  'This proves rationality of all singularities.',True)
replace('cdp:st:A.5.2',old2descent,
        r'Apply \cref{cdp:st:A.5.8} to this ruling and the resolution $\pi:Z\to S$. The verticality just proved gives its hypotheses, so $R^1\pi_*\OO_Z=0$, contradicting $\ell>0$. Thus every singularity of $S$ is rational.',
        'D12','Moved A.5.8 before this first use and applied its exact holomorphic descent and Leray maps to the same resolution and ruling. Removed the repeated descent and finite-support direct-image proof.')
replace('cdp:st:A.5.2','We give the crepancy argument to specify the comparison of canonical bundles.',
        r'The canonical-cycle conclusion is \cite[Theorem~4.20, p.~99, arXiv v1]{Reid1997Chapters}. Its local analytic canonical-bundle comparison here is as follows.',
        'D18','Opened the complete canonical-cycle theorem and proof. Retained the local analytic duality and effective-divisor map, which is also the exact later application in A.5.9.')

# One point-blowup comparison owns all three formerly repeated formulas.
blowup_id='lem:II:canonical-boundary-blowup'
eqrc5=tagged_display(blocks['cdp:st:A.5.9'],'A.RC.5')
eqat22=tagged_display(blocks['cdp:st:A.5.18'],'A.T.22')
eqrt11=tagged_display(blocks['prop:II:minimal-boundary-complements'],'A.RT.11')
alias_hypertargets=''.join(re.findall(r'\\hypertarget\{[^}]+\}\{\}',eqat22+eqrt11))
alias_labels=''.join(re.findall(r'\\label\{[^}]+\}',eqat22+eqrt11))
alias_targets=alias_hypertargets+r'\SsixEquationAliases{'+alias_labels+'}'
blowup_equation=eqrc5[:-2].rstrip()+'\n'+alias_targets.strip()+'\n'+eqrc5[-2:]
blocks[blowup_id]=r'''\begin{lemma}[Canonical boundaries under point blowups]\hypertarget{tag-P232}{}\label{lem:II:canonical-boundary-blowup}
\StatementRecord{lem:II:canonical-boundary-blowup}{proved}{P232}{}
Let $\sigma:Z_1\to Z_2$ be the blowup of a point on a smooth compact complex surface, with exceptional curve $E$. Let $D_1$ be an effective integral divisor with $c_1(K_{Z_1}+D_1)=0$ in rational cohomology. Put $D_2=\sigma_*D_1$, let $a$ be the coefficient of $E$ in $D_1$, and let $m$ be the multiplicity of $D_2$ at the centre. Writing canonical line bundles additively, their Jacobian comparison is
'''+blowup_equation+r'''
One has $a=m-1$, $m\ge1$, and $K_{Z_2}+D_2$ also has zero rational Chern class. The support of $D_1$ is connected exactly when the support of $D_2$ is connected. The complement Euler numbers satisfy
\[
 e(Z_1\setminus(D_1)_{\rm red})-e(Z_2\setminus(D_2)_{\rm red})
 =\begin{cases}1,&m=1,\\0,&m\ge2.\end{cases}
\]
\end{lemma}
\begin{proof}
In a blowup chart $(u,v)\mapsto(u,uv)$, pullback of the local two-form multiplies it by $u$. These Jacobian maps glue to $K_{Z_1}\simeq\sigma^*K_{Z_2}\otimes\OO_{Z_1}(E)$. Pullback of a local equation of $D_2$ has order $m$ on $E$, while $D_1$ has order $a$, proving the line-bundle identity \eqref{cdp:eq:A.RC.5}. Intersecting with $E$, whose square is $-1$ and whose intersection with a pulled-back divisor is zero, gives $1+a-m=0$ in the numerically trivial case. The formula then identifies the rational class upstairs with the pullback of the class downstairs; injectivity of that pullback gives its vanishing downstairs.

Since $a\ge0$, the centre belongs to $D_2$. For $m=1$ it is a smooth point of one component of coefficient one, $a=0$, and the strict boundary maps isomorphically to the old boundary. For $m\ge2$, $a>0$ and $(D_1)_{\rm red}=\sigma^{-1}((D_2)_{\rm red})$; its proper map to the old boundary has connected fibres, with $\PP^1$ over the centre. These descriptions prove the connectedness assertion. For $m=1$ the surface Euler number increases by one and the boundary Euler number is unchanged. For $m\ge2$, $\sigma$ is an isomorphism on the two complements. This proves the Euler formula.
\end{proof}

'''
for owner,eq in [('cdp:st:A.5.9',eqrc5),('cdp:st:A.5.18',eqat22),('prop:II:minimal-boundary-complements',eqrt11)]:
    move_log(owner,blowup_id,eq,'Moved the same point-blowup identity to one proved owner; all three old labels and permanent targets are aliases on the common formula. The applications state the exact variable renaming.')
log('D12',blowup_id,eqrc5+'\n'+eqat22+'\n'+eqrt11,blocks[blowup_id],
    'The three point-blowup computations now have one complete proof. The local Jacobian maps glue to an intrinsic canonical-line-bundle isomorphism; connectedness comes from the same proper boundary maps, and complement Euler numbers from the explicit isomorphism or multiplicity-one boundary transform.')
equation_aliases=[dict(old_tag='A.T.22',target_label='cdp:eq:A.T.22',statement_id=blowup_id),
                 dict(old_tag='A.RT.11',target_label='cdp:eq:A.RT.11',statement_id=blowup_id)]
for r,old in zip(equation_aliases,[eqat22,eqrt11]):
    log('D19',blowup_id,old,blowup_equation,'The same blowup formula now has one section equation number; its original label and permanent target remain exact aliases. The old-tag map retains this individual identity.')
old9blow=piece('cdp:st:A.5.9',r'\item We next prove that $\Gamma$ is connected.',r'\item Every positive exceptional component')
replace('cdp:st:A.5.9',old9blow,r'''\item Contract ruling $(-1)$-curves from $Z$ to a minimal ruled bundle $Z_0\to B$. Every pushed-forward boundary is effective. Apply \cref{lem:II:canonical-boundary-blowup} at each contraction, with $D_1$ and $D_2$ the boundaries before and after contraction. It gives $a=m-1$, numerical triviality downstairs and equivalence of connectedness of their supports. On $Z_0$ the boundary is $2C_0+V_0$, with $C_0$ a section and $V_0$ an effective sum of fibres. Its support is connected, so the support of $D_Z$ is connected.

''','D12','The common blowup lemma proves the same coefficient and support claims once. The application identifies the exact successive boundaries and starts from the connected section-plus-fibres support.')
old18blow=piece('cdp:st:A.5.18','For a ruling blowdown',r'Finally $\eta$ is an isomorphism away from')
replace('cdp:st:A.5.18',old18blow,r'''For a ruling blowdown $\sigma:W\to W'$, apply \cref{lem:II:canonical-boundary-blowup} with $Z_1=W$, $Z_2=W'$, $D_1=D_W$, $D_2=\sigma_*D_W$ and $m=d$. Its formula \eqref{cdp:eq:A.T.22} gives $a=d-1$. The minimal-resolution data above satisfy \cref{lem:II:elliptic-ruled-boundary}: the section has square zero, the effective vertical divisor is disjoint from it, the canonical-boundary class is zero and every exceptional curve is vertical. Hence $V_{\min}=0$, $Z_{\min}$ is a minimal ruled bundle and $\pi_{\min}$ is an isomorphism.
''','D12','Replaced the repeated blowup identity with the exact map and variable renaming to its common owner. The ruled-rigidity application retains every established hypothesis and conclusion.')
old210blow=piece('prop:II:minimal-boundary-complements',r'\item Use the specified contraction sequence.', 'Thus\n',True)
replace('prop:II:minimal-boundary-complements',old210blow,r'''\item At the contraction $\sigma:Z_i\to Z_{i-1}$ apply \cref{lem:II:canonical-boundary-blowup} with $Z_1=Z_i$, $Z_2=Z_{i-1}$, $D_1=D_i$, $D_2=D_{i-1}$ and $m=r$. Both canonical-boundary lines are trivial, so \eqref{cdp:eq:A.RT.11} gives $a=r-1$. Its complement formula increases the Euler number by one exactly when $r=1$ and leaves it unchanged when $r\ge2$. Iterating along the chosen contraction sequence proves the equality below, where $N_0$ counts the centres of multiplicity one. ''',
        'D12','The exact coefficient and complement-Euler proof has one earlier owner. The application retains its contraction sequence, anticanonical line bundles, multiplicity-one count and all subsequent boundary classifications.')
replace('prop:II:minimal-boundary-complements',r'''This local
argument is needed: on an abstract minimal $\mathbb F_2$,
its exceptional $(-2)$-section can be disjoint from an
anticanonical divisor without having arisen from one of the
$N_0$ blowups.''',r'''For the minimal surface $\mathbb F_2=\PP(\OO\oplus\OO(2))$, its two disjoint bundle sections satisfy $C_0^2=-2$ and $C_\infty\sim C_0+2F$. The divisor $2C_\infty\sim2C_0+4F=-K_{\mathbb F_2}$ is disjoint from $C_0$, while the contraction sequence to this minimal model is empty and $N_0=0$.''',
        'D02','Replaced the defensive comparison by the exact bundle sections and anticanonical divisor realizing the stated possibility. The empty point-blowup sequence gives N_0=0 explicitly, preserving the reason that the torus-specific off-conductor exclusion is separately applied.')

# Known topological quotient fact: retain the actual map, cite its opened owner.
oldtree=r'''The quotient
$q:D\to D/J$ is a homotopy equivalence: a contractible
CW subcomplex is a cofibration, and the homotopy
extension property extends its contraction.'''
replace('cdp:st:A.5.18',oldtree,r'''The quotient $q:D\to D/J$ contracts the contractible CW subcomplex $J$, so it is a homotopy equivalence by \cite[Propositions~0.16--0.17, pp.~15--16]{Hatcher2002}.''',
        'D17','The quotient map and its contractible subcomplex are explicit; the opened Hatcher theorem supplies the known homotopy-extension conclusion.')
oldtree11=r'''A contractible subcomplex is a
cofibration; contracting it gives a homotopy equivalence
of this CW pair. Concretely the homotopy extension
property extends a contraction of $J$ and supplies a
homotopy inverse to the quotient map.'''
replace('cdp:st:A.5.11',oldtree11,r'''The quotient map $q$ is a homotopy equivalence by \cite[Propositions~0.16--0.17, pp.~15--16]{Hatcher2002}, since $J$ is a contractible CW subcomplex.''',
        'D17','Applied the opened contractible-subcomplex quotient theorem to the stated tree and triangulated surface. The actual quotient, normalization factorization and fundamental-group map are retained.')

# Common mathematical verbs; no premise, morphism or numeric value is changed.
for ident in list(blocks):
    for old,new in [('the actual arrows','the arrows'),('the actual ring comparison','the ring comparison'),('the actual $A$-linear isomorphism','the $A$-linear isomorphism'),('the actual local-system','the local-system'),('the actual numerical','the numerical'),('the actual local comparison','the local comparison'),('the actual map','the map'),('the actual divisor comparison','the divisor comparison'),('this actual smooth curve','this smooth curve'),('an actual open','an open'),('an\nactual line-bundle comparison','a\nline-bundle comparison'),('the actual composite','the composite'),('the actual comparison','the comparison'),('the actual line comparison','the line comparison'),('actual nonzero holomorphic','nonzero holomorphic'),('an actual local comparison','a local comparison'),('The actual divisor comparison','The divisor comparison'),('the actual torus smoothing','the torus smoothing'),('The actual map','The map'),('an actual\n','a\n')]:
        while old in blocks[ident]:
            log('D08',ident,old,new,'Retained the specified morphism or equality; removed process emphasis.')
            blocks[ident]=blocks[ident].replace(old,new,1)

groups=[
 ('Duality and normal surface geometry','normalization-duality',[dual_id,'cdp:st:A.5.1',remark_id,matrix_id,'cdp:st:A.5.8','cdp:st:A.5.2','cdp:st:A.5.3']),
 ('Persistent Picard twists','normalization-picard',['cdp:st:A.5.4','cdp:st:A.5.6']),
 ('Ruled normalizations and conductor genus','normalization-genus',[blowup_id,rigid_id,'cdp:st:A.5.9','cdp:st:A.5.11','cdp:st:A.5.12','cdp:st:A.5.13']),
 ('Conductor jets and the genus bound','normalization-jets',['cdp:st:A.5.5',example_id,'cdp:st:A.5.14']),
 ('Cusp images on ruled normalizations','normalization-cusps',['cdp:st:A.5.7','cdp:st:A.5.10','cdp:st:A.5.20']),
 ('Binomial Milnor fibres','normalization-binomial',['cdp:st:A.5.15',rank_id]),
 ('Isolated singularities and suspension germs','normalization-suspensions',['cdp:st:A.5.17']),
 ('Binary products and cubic jets','normalization-local',['cdp:st:A.5.21',nodal_id,sphere_id,aspherical_id]),
 ('Tacnode conductor images','normalization-higher-jets',[curve_id,'cdp:st:A.5.18',cover_id]),
 ('Ordinary-triple conductor images','normalization-triple',['cdp:st:A.5.19']),
 ('Rational normalizations','normalization-rational',['cdp:st:A.5.16']),
 ('Minimal rational boundary complements','normalization-boundary',['def:II:minimal-boundary-data','prop:II:minimal-boundary-complements']),
]
assert sorted(blocks)==sorted(x for _,_,ids in groups for x in ids),(set(blocks)-set(x for _,_,ids in groups for x in ids))
owner_units={}
out=[heading]
for title,slug,ids in groups:
    out.append('\\subsection{'+title+'}\\label{subsec:II:'+slug+'}\n\n')
    for ident in ids:
        owner_units[ident]=slug;out.append(blocks[ident].strip()+'\n\n')
        if ident!=matrix_id:
            log('D14',ident,ident,'subsec:II:'+slug+'; position '+str(ids.index(ident)+1),
                'Placed the complete statement and proof together in mathematical prerequisite order. All original labels and hypotheses survive; extracted subsidiary conclusions have explicit proved owners.')
working=''.join(out)

# The existing global D19 proposal fixes exact labels for unlabelled tags.
known={}
with (ROOT/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    for r in csv.DictReader(f,delimiter='\t'):
        if r['old_tag']:known[r['old_tag']]=r['target_label']
equations=equation_aliases.copy()
def owner_at(text,pos):
    items=list(re.finditer(r'\\StatementRecord\{([^{}]+)\}',text[:pos]))
    return items[-1].group(1) if items else 'sec:II:05'
def equation(m):
    old=m.group();ts=re.findall(r'\\tag\{([^{}]+)\}',old)
    if not ts:return old
    assert len(ts)==1,ts
    labs=re.findall(r'\\label\{([^{}]+)\}',old)
    lab=labs[0] if labs else known[ts[0]]
    new=old.replace(r'\[',r'\begin{equation}',1);new=new[:-2]+r'\end{equation}'
    new=new.replace(r'\tag{'+ts[0]+'}', '' if labs else r'\label{'+lab+'}')
    ident=owner_at(working,m.start());equations.append(dict(old_tag=ts[0],target_label=lab,statement_id=ident))
    log('D19',ident,old,new,'The same display and all its labels/targets now use the ordinary section equation counter.')
    return new
working=re.sub(r'\\\[.*?\\\]',equation,working,flags=re.S)
for tag,lab in sorted(known.items(),key=lambda x:len(x[0]),reverse=True):
    old='('+tag+')'
    if len(tag)<2 or not re.fullmatch(r'[A-Za-z0-9.]+',tag):continue
    while old in working:
        pos=working.index(old);ident=owner_at(working,pos);new=r'\eqref{'+lab+'}'
        log('D19',ident,old,new,'The old literal equation citation now resolves through its unchanged exact equation label.')
        working=working[:pos]+new+working[pos+len(old):]
assert not re.search(r'\\tag\{',working)
for kind in ['label','hypertarget']:
    pat=r'\\'+kind+r'\{([^{}]+)\}'
    old=set(re.findall(pat,original));new=set(re.findall(pat,working))
    assert old<=new,(kind,old-new)
    values=re.findall(pat,working);assert len(values)==len(set(values)),(kind,'duplicate')
assert working.count(r'\begin{proof}')==working.count(r'\end{proof}')
assert not re.search(r'night:P4R\.13|night:P4\.40',working)

def tsv(suffix,fields,data):
    with (OUT/(PRE+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
(OUT/(PRE+'_replacement.tex')).write_text(working,newline='\n')
bp_start=working.index(r'\begin{lemma}[Canonical boundaries under point blowups]')
bp_end=working.index(r'\end{proof}',bp_start)+len(r'\end{proof}')
(OUT/'S6_SERIES_PUBLISH_c3_conductor_P232.tex').write_text(working[bp_start:bp_end]+'\n',newline='\n')
with (ROOT/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:df=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',df,rows)
tsv('_equations.tsv',['old_tag','target_label','statement_id'],equations)
tsv('_owner_transfers.tsv',['label','old_owner','new_owner','reason'],transfers)

with (ROOT/'CHECK_EVENTS.tsv').open() as f:ef=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc);events=[]
for ident,slug in owner_units.items():
    row={k:'' for k in ef}
    scope='Read the complete cp35 statement/proof and compared the receiving text, including every transferred conclusion and its hypotheses.'
    if ident not in old_blocks:scope='Read the complete originating proof passages and the complete extracted receiving statement/proof; compared hypotheses, conclusions, exact maps and all retained labels.'
    if ident==matrix_id:scope='Exposed reading of the complete parent-prepared P243 statement/proof, compared with the complete original A.5.20 analytic intersection argument; checked the weighted identity, connected graph and inverse spectral series.'
    row.update(statement_id=ident,date=now.date().isoformat(),date_utc=now.isoformat(),
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',
        type='used and rechecked in this run',outcome=scope+' Fresh source-opening credit is limited to the new or substituted locators specified in the comparison note; inherited citations are not newly certified by this event. P243 is an exposed receiving-proof reading of the parent-prepared lemma. This is an exposed editorial rereading, not an independent reproof or computation. Integrated page reading remains open.',
        event_id='publish:c3:conductor03:'+ident,phase='publication editorial comparison',
        source_file='agents/continuation3_conductor/'+PRE+'_replacement.tex',source_event_type='used and rechecked in this run',
        evidence_group='publish:c3:conductor03:'+slug,where='subsec:II:'+slug)
    events.append(row)
# The permanent binomial alias remains an actual reader target on A.5.15.
alias=events[[r['statement_id'] for r in events].index('cdp:st:A.5.15')].copy()
alias['statement_id']='night:P4.18';alias['event_id']='publish:c3:conductor03:night:P4.18';events.append(alias)
tsv('_CHECK_EVENTS.tsv',ef,events)
status=[]
for title,slug,ids in groups:
    for n in range(1,26):
        state='done';reason='Complete unit read for this defect class; all identified changes are logged per instance.'
        if n==18:state='open';reason='New Reid, Teleman, Hatcher and CDP locators opened exactly; inherited bibliography form and common primary-locator pass remain open.'
        if n==23:state='open';reason='Local list and display edits complete; integrated typography and final rendered-page reading remain open.'
        status.append(dict(unit='subsec:II:'+slug,title=title,criterion=f'D{n:02d}',status=state,reason=reason))
    status.append(dict(unit='subsec:II:'+slug,title=title,criterion='structure',status='done',reason='Local prerequisite order and common proof ownership completed. Euler/normal jets precede this section; A.5.8 precedes A.5.2; the three blowup identities share P232. The later P4.15 comparison has been removed. The current receiving fragment has no forward statement/equation references inside or outside this section. Whole-paper arrangement and integrated page spans remain under parent review.'))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],status)
print('Normalization replacement:',len(original),'->',len(working),'characters')
print('Owners:',len(owner_units),'; defects:',len(rows),'; exposed reread events:',len(events),'; old equation identities:',len(equations))
print('New own tags: P222, P223, P224, P225, P226, P227, P228, P229, P230, P231, P232. Parent-prepared shared lemma: P243.')
print('All pre-existing labels and hypertargets retained, with no duplicate owner targets.')
print('Open: inherited bibliography/locator pass, integrated typesetting and final page reading; whole-paper forward-premise order outside this scope.')
