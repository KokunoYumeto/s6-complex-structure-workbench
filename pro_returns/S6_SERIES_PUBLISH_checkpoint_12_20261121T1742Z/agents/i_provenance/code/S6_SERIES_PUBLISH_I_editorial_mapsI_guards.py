import pathlib,re,json,hashlib,datetime
R=pathlib.Path('/workspace/scratch/653608133b22/work/agents/i_provenance'); src=R.parent.parent/'S6_SERIES_PUBLISH_I.tex';S=src.read_text();sha=hashlib.sha256(S.encode()).hexdigest()
snap=R/('S6_SERIES_PUBLISH_I_mapsI_editorial_source_'+sha[:12]+'.tex');snap.write_text(S)
C=(R/'S6_SERIES_PUBLISH_I_editorial_real_forms_old.tex').read_text();C=C[:C.index('\\begin{cited}[The coherent closing translation]')]
Q=(R/'S6_SERIES_PUBLISH_I_editorial_circle_quotient_old.tex').read_text();changes=[];internal=[]
def add(id,old,new,scope,reason,defects='D01,D02,D04,D05,D08,D09,D13'):
    assert S.count(old)==1,(id,S.count(old)); changes.append(dict(id=id,old=old,new=new,expected_count=1,statement_id=scope,reason=reason,defect_types=defects))
def bchange(id,old,new,reason):
    global B
    assert B.count(old)==1,(id,B.count(old));B=B.replace(old,new);internal.append(dict(id=id,old=old,new=new,statement_id='fam:src:B.4.2',reason=reason))
# Move the complete B4.2 proof into the real-forms section, with its section aliases.
ba=S.index('\\subsection{Automorphisms and the remaining real-structure calculation}')
bp=S.index('\\begin{proposition}\\hypertarget{tag-01QG}',ba)
be=S.index('\\end{proof}',bp)+len('\\end{proof}')
B=S[bp:be];(R/'S6_SERIES_PUBLISH_I_editorial_B42_old.tex').write_text(B)
bchange('I-B42-title','\\begin{proposition}\\hypertarget{tag-01QG}{}','\\begin{proposition}[Conjugate members and antiholomorphic automorphisms]\\hypertarget{tag-01QG}{}','Title the retained classification.')
bchange('I-B42-period-prose','All reflection identities for the periods can be checked before invoking uniqueness. Denote their affine transformation formulas','Denote the affine period transformations','State the algebraic calculation directly; retain both rational substitutions and the subsequent uniqueness argument.')
bchange('I-B42-H-label',r''' H=\begin{pmatrix}1&0&0&0\\0&1&0&0\\-6&0&-1&0\\0&-1&0&-1\end{pmatrix}.
\]''',r''' H=\begin{pmatrix}1&0&0&0\\0&1&0&0\\-6&0&-1&0\\0&-1&0&-1\end{pmatrix}.
 \label{I:eq:real-reflection-matrix}
\]''','Give the retained integral reflection matrix a reference for its later application.')
bchange('I-B42-middle-deck-prose','This proves exact compatibility, not merely an equality of fibre lattices.','Thus the reflection intertwines the middle deck actions.','State the full compatibility supplied by the displayed period-matrix identity.')
bchange('I-B42-affine-label',r''' w'_2=-H(-\varepsilon')=\varepsilon'-3d.
\]''',r''' w'_2=-H(-\varepsilon')=\varepsilon'-3d.
 \label{I:eq:real-reflected-affine-data}
\]''','Name the exact target affine datum to avoid repeating its construction.')
bchange('I-B42-target-prose','to the actual target datum with parameter','to the target datum with parameter','Remove process emphasis.')
bchange('I-B42-splitting-prose','It remains to verify the group extension rather than infer its square from $H^2$.','We construct an involutive splitting of the group extension.','Keep the full square-translation correction proof and state its purpose positively.')
bchange('I-B42-square-translation-name','Its square is a holomorphic translation $d$. Commuting $J$ with $J^2$ shows $d=\\bar d$ in $\\mathbb C/\\mathbb Z$. This equality forces the imaginary part of a representative of $d$ to vanish, so take $d\\in\\mathbb R$. Replacing $J$ by the composition of translation by $-d/2$ with $J$ changes its square to $d-d/2-d/2=0$.','Its square is a holomorphic translation $b_0$. Commuting $J$ with $J^2$ shows $b_0=\\bar b_0$ in $\\mathbb C/\\mathbb Z$. This equality forces the imaginary part of a representative of $b_0$ to vanish, so take $b_0\\in\\mathbb R$. Replacing $J$ by the composition of translation by $-b_0/2$ with $J$ changes its square to $b_0-b_0/2-b_0/2=0$.','Use b_0 for the scalar translation class so the fixed lattice vector d keeps its meaning after moving this proof into the real-form section.')
bchange('I-B42-aut-reference','the full group is the holomorphic group of \\ref{fam:src:B.4.1}.','the full group is the holomorphic automorphism group of Theorem~\\ref{fam:src:B.4.1}.','Refer to the parent-consolidated theorem through the preserved alias.')
(R/'S6_SERIES_PUBLISH_I_editorial_B42_new.tex').write_text(B)
add('I-real-move-B42',S[ba:be],'','fam:src:B.4.2','Move the complete B4.2 statement and proof beside the real-form calculation; relocate the section tag/label too. Remove only the obsolete B4.1 appendix navigation paragraph, whose full credited theorem is already retained under its alias.','D05,D12')
a=C.index('\\begin{proposition}[Two conjugacy classes');old=C[:a]
new=r'''\section{Real structures and their fixed three-spheres}\hypertarget{tag-02P9}{}\label{mapsI:real-forms}
\hypertarget{tag-01PJ}{}\label{fam:section:B.4}

\begin{definition}[Real-period data]\hypertarget{tag-IP04}{}\label{I:def:real-period-data}
Use the lattice, period matrix and clockwise root generators of
Definition~\ref{def:common-conventions}, and the affine vectors of
Definition~\ref{I:def:family-parameter}. In this section write
$d=\widehat\delta$, $g=\widehat\gamma$, $u=\widehat u$ and
$w_\Lambda=\widehat w$. An unadorned $w$ in a lattice expression denotes
$w_\Lambda$; the scalar parameter remains $w=e^{-\pi ic}$. Put
\[
 e=\Pi_c d=(0,1)^{\mathsf t},\qquad E=d\otimes\gamma,
 \qquad M_0=(A_1A_2)^{-1},\qquad D_c=D_{\rm part}+\Im c<0.
\]
The circle $\rho(s)$ is translation by $se$, $s\in\mathbb R/\mathbb Z$.
In cusp coordinates $q=1/t$ and $s=(2\pi i)^{-1}\log q$, define the
bounded matrix $C_c(q)$ by $Z_c=sB_0+C_c(q)$, where
$B_0=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$.
Thus $\Pi_cg=(6\mu,-s+C_{c,21})^{\mathsf t}$.
The cusp double curves $D_1,D_2,D_{12}$ belong to the edge directions
$e_1,e_2,e_1-e_2$. The action $\rho$ fixes $D_2$, while the literal
character has a limit along $D_1$, as located by the explicit toric
coordinates in Proposition~\ref{mapsI:src:A.1.2}.
\end{definition}

'''+B+'\n\n'
add('I-real-number-data-and-B42',old,new,'fam:src:B.4.2; I:def:real-period-data','Use the one common marking/period/finite-data definition; retain all local real notation and cusp formulas, and place the complete conjugation proof before its uses.','D04,D05,D12,D13')
a=C.index('\\item The real comparison');b=C.index('\n\\item At a fixed point',a)
new=r'''\item Proposition~\ref{fam:src:B.4.2} identifies the full holomorphic group
with $\mathbb C^*$ and gives the conjugation action $z\mapsto1/\bar z$.
Thus the square of $z\sigma$ is $z/\bar z$, and it is an involution
exactly for $z\in\mathbb R^*$. Conjugation by $y\in\mathbb C^*$ changes
this coefficient to $|y|^2z$, giving exactly the two sign classes.
'''
add('I-real-two-class-proof',C[a:b],new,'mapsI:src:A.3.1','Use the retained complete automorphism/reflection proof, then preserve the distinct two-class conjugacy calculation.','D12')
add('I-real-semifree-prose','Its stabilizers are inherited from the checked semifree action\non $X$ and hence are either trivial or the whole circle.','Its stabilizers are inherited from the semifree action on $X$ and are\ntherefore either trivial or the whole circle.','mapsI:src:A.3.1','Remove check-history wording.','D08')
a=C.index('We now fix a representative');b=C.index('\\begin{theorem}[Explicit real involutions',a);old=C[a:b]
new=old.replace('We now fix a representative of each sign class, instead of leaving the\nsymbol $\\sigma$ unspecified. Put','Put')
new='\\begin{definition}[Representatives of the real involutions]\\hypertarget{tag-IP05}{}\\label{I:def:real-representatives}\n'+new.rstrip()+'\n\\end{definition}\n\n'
add('I-real-number-representatives',old,new,'I:def:real-representatives','Number the exact roots/logarithms/branch choice and representative table, retaining both equation labels and the existing tag.','D02,D13')
a=C.index('\\item We first verify the global map.');b=C.index('The normalization from this',a)
new=r'''\item Start with the reflection $(z,\zeta)\mapsto(\iota z,-\bar\zeta)$
and the integral matrix $H$ of \eqref{I:eq:real-reflection-matrix}.
Proposition~\ref{fam:src:B.4.2} proves its period compatibility and gives
the target affine datum \eqref{I:eq:real-reflected-affine-data}.
'''
add('I-real-reflection-application',C[a:b],new,'mapsI:src:A.3.2','Refer to the single complete reflection proof and its exact integral/affine maps; retain every normalization and filling-extension step below.','D12')
add('I-real-cusp-application-prose','The displayed translation has integral affine defects on the ordinary cover, holomorphic finite-chart corrections, and a nonvanishing toric-unit expression at the cusp; it represents the even shift of Proposition~\\ref{fam:src:A.3.1}. Its cusp expression is checked immediately below. Indeed put','The displayed translation represents the even shift of Proposition~\\ref{fam:src:A.3.1}. Its finite-chart corrections are holomorphic. For its cusp expression, put','mapsI:src:A.3.2','Keep the explicit ordinary defects, finite-root comparison and full cusp cancellation calculation, avoiding anticipatory check prose.','D08')
add('I-real-arithmetic-intro','For completeness, the finite arithmetic deciding existence can be\nperformed without approximating the periods.','Existence of fixed points is decided by integral affine congruences.','mapsI:src:A.3.2','State the exact mathematical method.','D02,D08')
old='''This proves the coset counts and offsets; the complete exact computation
is in \\texttt{code/maps\\_audit/MAPS/code/real\\_involutions.py}. In particular the lift on
the left arc is $g_0^{-1}$, not $g_0$; the latter would give a nonintegral
square vector and is the wrong continuation convention.'''
new='''This proves the coset counts and offsets. The Hermite and Smith
computations are listed in \\cref{tab:I:programs}. The left-arc lift
$g_0^{-1}$ follows from the reflected upper-half-plane path above.'''
add('I-real-ordinary-program',old,new,'mapsI:src:A.3.2','Retain the integral solvability criterion, all square vectors/Smith factors and the correctly derived lift; cite the operative program once.','D02,D08,D09')
add('I-real-odd-root-conclusion','also follows by solving the limiting affine equations, and checks the\nfull multiplicity-three quotient rather than treating it as a reduced\nunramified fibre.','also follows by solving the limiting affine equations on the full\nmultiplicity-three root quotient.','mapsI:src:A.3.2','Keep the full root quotient scope in positive mathematical language.','D02,D08')
old='''torus downstairs, not a Klein bottle. The exhaustive congruence check
\\texttt{code/maps\\_audit/MAPS/code/real\\_finite\\_four.py} uses denominator $24$: translation
denominators divide $12$, and the nonzero Smith factors are $1,2$, so
every component has such a representative. It checks the component
permutation, not just the dimension of the fixed eigenspace.'''
new='''torus downstairs. The congruence enumeration uses denominator $24$:
translation denominators divide $12$, and the nonzero Smith factors are
$1,2$, so every component has such a representative. The component
permutation is included in the exact enumeration listed in
\\cref{tab:I:programs}.'''
add('I-real-finite-program',old,new,'mapsI:src:A.3.2','Retain the exhaustive-denominator argument and deck permutation; cite the operative finite enumeration once.','D02,D08,D09')
add('I-real-parameter-signs','parities are: both for negative $w$ and $\\epsilon=0$; only even for\nnegative $w$ and $\\epsilon=1$; neither for positive $w$ and $\\epsilon=0$;\nonly odd for positive $w$ and $\\epsilon=1$.','parities are: both for negative imaginary $w$ and $\\epsilon=0$; only even for\nnegative imaginary $w$ and $\\epsilon=1$; neither for positive imaginary $w$ and $\\epsilon=0$;\nonly odd for positive imaginary $w$ and $\\epsilon=1$.','mapsI:src:A.3.2','Make the already specified imaginary-parameter signs explicit.','D04')
add('I-real-cusp-intro','It remains to compute the cusp, which also excludes hidden real\ncomponents confined to a singular fibre. Put','We compute the cusp fixed set. Put','mapsI:src:A.3.2','The final totally-real argument still proves that no component is confined to a special fibre.','D02,D08')
add('I-real-odd-transport','Thus the actual odd-root transport is $C$, not merely an arbitrary\nmatrix conjugating the two reflections. It satisfies','Thus the odd-root transport is $C$. It satisfies','mapsI:src:A.3.3','Keep the unique k=2 root-lift derivation and its exact transport matrix.','D02,D08')
add('I-real-integral-conclusion','integral assertions, beyond the mod-two information.','fundamental-group and integral-homology assertions.','mapsI:src:A.3.3','Name the conclusions established by the explicit Heegaard gluing.','D02')
add('I-real-quotient-title','\\begin{proposition}[Restrictions of the repaired circle quotient]','\\begin{proposition}[Restrictions of the circle quotient]','mapsI:src:A.3.4','Use a mathematical title.','D01,D13')
add('I-real-quotient-statement','The repaired map $e_{\\rm q}$ of Theorem~\\ref{mapsI:src:A.2.1} may be chosen $\\rho$-invariant.','The map $e_{\\rm q}$ of Theorem~\\ref{mapsI:src:A.2.1} has a $\\rho$-invariant\ncusp replacement.','mapsI:src:A.3.4','State the property proved by averaging the circle lift.','D01')
old='''The formulas specify the embedded fixed sets by their torus cosets and
their actual finite and toric attachments. No ambient-isotopy
classification or value of the Haefliger knot invariant of these
embedded three-spheres is asserted here.'''
add('I-real-concluding-process',old,'','mapsI:src:A.3.4','Remove a scope disclaimer; the statements already give the exact fixed-set and smooth-type conclusions.','D02,D08')
# Circle quotient: number the existing data and the actual cusp cohomology input.
a=Q.index('We write $g,u,w,d$');b=Q.index('\\begin{proposition}',a);old=Q[a:b]
new='\\begin{definition}[Circle-quotient conventions]\\hypertarget{tag-IP06}{}\\label{I:def:circle-quotient-conventions}\n'+old.replace('section, and $\\gamma$ for its first dual covector.  Thus $d$ is a\nvector, whereas $\\gamma$ is a covector.  The cusp coordinate is','section, and $\\gamma$ for its first dual covector. The cusp coordinate is').rstrip()+'\n\\end{definition}\n\n'
add('I-circle-number-conventions',old,new,'I:def:circle-quotient-conventions','Number the existing exact basis and orientation conventions.','D13')
a=Q.index('For the markings and the clockwise');b=Q.index('The common invariant vectors',a)
new=r'''Use the monodromy matrices of \eqref{wb:pshift:eq:finite-data} and the
standard affine vectors of Definition~\ref{I:def:family-parameter}. Put
\[
 M_0=(A_1A_2)^{-1}=
 \begin{pmatrix}1&0&0&0\\0&1&0&0\\0&1&1&0\\-1&0&0&1\end{pmatrix}.
\]
'''
add('I-circle-common-matrices',Q[a:b],new,'mapsI:src:A.1.1','Use the canonical matrices and affine vectors once; retain the explicit cusp monodromy needed for the kernel calculation.','D12')
add('I-circle-matrix-proof','The first two displayed matrices are the inverse transposes of\nthe matrices printed on page 2 of \\cite{AC2026}; their product\nhas inverse $M_0$.  Direct integral multiplication gives','For the matrices of \\eqref{wb:pshift:eq:finite-data}, direct integral\nmultiplication gives','mapsI:src:A.1.1','Reference the established common marking; retain all exact kernel and fixed-covector arithmetic.','D05,D12')
add('I-circle-program-record','The exact checks, including the exhaustive mod-two fixed-vector\ncalculation used below, are in \\texttt{code/maps\\_audit/MAPS/code/maps\\_exact.py}.\n','','mapsI:src:A.1.1','The complete integral calculation is printed; retain the independent diagnostic program in check records.','D08,D09')
a=Q.index("Engel's primitive invariant covector");b=Q.index('\\begin{proposition}[Pointwise cusp',a);old=Q[a:b]
new=r'''\begin{remark}[Comparison of the quotient characters]\hypertarget{tag-IP08}{}\label{I:rem:circle-character-comparison}
Engel's primitive invariant covector $\psi$
\cite[Lemma~3.8]{Engel2026} is related to the present character by
\[
 P_E=P_{\rm mark},\qquad \psi P_E=-\gamma,
 \hypertarget{tag-02OZ}{}\label{mapsI:quotient-eq-2}
\]
where $P_{\rm mark}$ is the integral isomorphism of
Proposition~\ref{inv:B1.0}. Thus the quotient characters agree after the
target-circle map $\theta\mapsto-\theta$. Inverting the root generators
gives the translation vectors $a_{j-1}=-P_Ev_j/m_j$, as in
Proposition~\ref{fam:src:B.2.2}.
\end{remark}

'''
add('I-circle-character-comparison',old,new,'I:rem:circle-character-comparison','Number the comparison, use the identical existing matrix by its exact lattice isomorphism, and specify the target-circle orientation map.','D02,D12,D13')
add('I-circle-cusp-title','\\begin{proposition}[Pointwise cusp obstruction and the corrected double curve]','\\begin{proposition}[Pointwise cusp limits and the fixed double curve]','mapsI:src:A.1.2','Give a mathematical title.','D01,D13')
add('I-circle-fixed-curve-conclusion','Its fixed curve is $z_0=z_2=0$.  This directly locates the\nincorrect identification of the family construction.  Edge direction,\ntorus stabilizer, and coordinate on the quotient polygon must\nnot be interchanged.','Its fixed curve is $z_0=z_2=0$, while the character extends along\n$z_0=z_1=0$ by the preceding limit formula. The displayed action and\nlimit formula give these two loci in the same toric chart.','mapsI:src:A.1.2','Replace an unattributed correction claim by the explicit morphism and limit calculation already proved.','D01,D02')
a=Q.index('The nonextension above is local');b=Q.index('\\begin{proposition}[The filled',a);old=Q[a:b]
new=r'''\begin{lemma}[The cusp neighbourhood and its circle classes]\hypertarget{tag-IP07}{}\label{I:lem:cusp-fundamental-group}
For the cusp neighbourhood $N_0$ and the vanishing lattice
$K=\mathbb Z\langle w,d\rangle$,
\[
 \pi_1(N_0)=\overline\Lambda=\Lambda/K.
 \hypertarget{tag-02P2}{}\label{mapsI:quotient-eq-5}
\]
The punctured-cusp map to this group kills $K$ and the base meridian.
Both long-period covectors extend in integral $H^1(N_0;\mathbb Z)$.
The literal character on an ordinary fibre has no extension to all of
$X\simeq S^6$.
\end{lemma}
\begin{proof}
The toric covering has rays $(v,1)$ for all $v\in\mathbb Z^2$.
Meridians about its toric divisors kill the whole cocharacter lattice:
$(0,1)$ is a ray and $(e_i,1)-(0,1)=(e_i,0)$. Hence the toric cover is
simply connected. Its free period deck group is
$\overline\Lambda=\Lambda/K$, proving the displayed isomorphism.
The base meridian bounds the disc given by a point of the dense orbit
on a central component. Both long-period covectors kill these
relations and therefore extend in integral $H^1$.
An extension of $\theta_\gamma$ to all of $X\simeq S^6$ would give a
nonzero homomorphism $H_1(F)\to\mathbb Z$ factoring through
$H_1(X)=0$, which is impossible.
\end{proof}

'''
add('I-circle-number-cusp-input',old,new,'I:lem:cusp-fundamental-group','Turn the already proved cusp π1/cohomology input into a numbered lemma before A2.1 uses it, preserving its group, exact relations, equation tag and global factorization obstruction.','D02,D13')
add('I-circle-meridian-convention','by actual meridians, including orientations.','by the displayed oriented meridians.','mapsI:src:A.1.3','State the specified orientation data directly.','D08')
old='''above.  A regular orbit is the $(3,4)$ torus knot, up to
the harmless exchange of the two coordinates.  This
identifies the manifold with its peripheral structure;
the abstract presentation $\\langle x,y\\mid x^3=y^{-4}\\rangle$
alone would not have justified that identification.'''
new=r'''above. A regular orbit is the $(3,4)$ torus knot under the coordinate
exchange $(z_1,z_2)\mapsto(z_2,z_1)$ when the opposite ordering is used.
The displayed orbit map and meridian slopes identify the manifold
with its peripheral structure.'''
add('I-circle-knot-comparison',old,new,'mapsI:src:A.1.3','Give the exact coordinate exchange and preserve the peripheral identification proved by the Seifert data.','D02')
add('I-circle-section-title','\\subsection{The repaired map and its relative uniqueness}','\\subsection{The cusp replacement and its relative uniqueness}','mapsI:src:A.2.1','Use a mathematical section title.','D01')
add('I-circle-theorem-title','\\begin{theorem}[The repaired map and its relative homotopy class]','\\begin{theorem}[The cusp replacement and its relative homotopy class]','mapsI:src:A.2.1','Use a mathematical theorem title.','D01,D13')
add('I-circle-smooth-product','This proves smoothness even at the critical points of $f$:\nthe product map is smooth without any submersion assertion.',"Both components of $(f,\\theta')$ are smooth on $N_0$, so the\nproduct map is smooth at the critical points of $f$ as well.",'mapsI:src:A.2.1','State the smooth-product argument positively.','D02')
# Apply in memory only, checking uniqueness and preservation of all source labels.
N=S
for c in changes:
    assert N.count(c['old'])==1,(c['id'],N.count(c['old']));N=N.replace(c['old'],c['new'])
olds=re.findall(r'\\label\{([^}]+)\}',S);news=re.findall(r'\\label\{([^}]+)\}',N)
newlabels=['I:def:real-period-data','I:def:real-representatives','I:def:circle-quotient-conventions','I:lem:cusp-fundamental-group','I:rem:circle-character-comparison','I:eq:real-reflection-matrix','I:eq:real-reflected-affine-data']
assert sorted(olds)==sorted(x for x in news if x not in newlabels)
out=dict(source=str(src),source_sha256=sha,source_snapshot=str(snap),created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),changes=changes,moved_B42_internal_changes=internal,new_tags=['IP04','IP05','IP06','IP07','IP08'],new_labels=newlabels,structure_request='After application move the entire mapsI:circle-quotient section immediately before mapsI:real-forms, after fam:C4. This removes A3.4 dependence on the later e_q construction.',verification='Original complete real-form/B4.2/circle statements and proofs read; exact proposed changes constructed. Final proposed-text reread is logged separately. No root source written.')
(R/'S6_SERIES_PUBLISH_I_editorial_mapsI_guards.json').write_text(json.dumps(out,indent=2)+'\n')
# Keep bounded complete proposed sections for actual rereading.
a=N.index('\\section{Real structures');b=N.index('\\begin{cited}[The coherent closing translation]',a)
(R/'S6_SERIES_PUBLISH_I_editorial_real_forms_new.tex').write_text(N[a:b])
a=N.index('\\section{The integral circle quotient');b=N.index('\\end{proof}',N.index('\\label{mapsI:src:A.2.1}',a))+len('\\end{proof}')
(R/'S6_SERIES_PUBLISH_I_editorial_circle_quotient_new.tex').write_text(N[a:b]+'\n')
print(json.dumps({'guards':len(changes),'B42_internal_edits':len(internal),'all_labels_preserved':True,'source_sha256':sha},indent=2))
