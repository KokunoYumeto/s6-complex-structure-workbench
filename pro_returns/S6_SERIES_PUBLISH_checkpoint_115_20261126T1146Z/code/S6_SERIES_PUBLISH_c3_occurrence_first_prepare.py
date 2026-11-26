"""Prepare the complete first occurrence units and the earlier support-blowup owner."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_occurrence_root'
prefix='S6_SERIES_PUBLISH_c3_occurrence_first_'
snapshot=(folder/'S6_SERIES_PUBLISH_II_occurrence_input.tex').read_text()
end=r'\begin{proposition}[Opposite logarithmic data produce a projective essential component]'
old=snapshot[:snapshot.index(end)]
text=old
rows=[]
counter=0

def edit(old_text,new_text,types,statement,reason):
    global text,counter
    assert text.count(old_text)==1,(statement,old_text[:150],text.count(old_text))
    text=text.replace(old_text,new_text,1)
    for kind in types:
        counter+=1
        rows.append(dict(change_id=f'II-C3-ROOT-OCCURRENCE-FIRST-{counter:03}',type=kind,
            statement_id=statement,old_location='Complete occurrence source prefix through UN13',
            old_page='checkpoint35 source; final concordance pending',
            new_location='Elliptic roots, Hopf threefolds, cuspidal self-products and Kummer occurrence subsections',
            new_page='integrated final build pending',old_text=old_text,new_text=new_text,reason=reason,
            review_status='Root read complete original statements/proofs and cited receiving owners; complete receiving rereading required before admission. No independent or final-page credit.'))

anchor=r'\begin{proposition}[Zero-Euler product fillings with essential Kodaira-dimension-one components]'
edit(anchor,r'\subsection{Elliptic root fillings}\label{subsec:II:elliptic-root-fillings}'+'\n\n'+anchor,
     ['D14'],'cdp:st:C.2.UN.6','Give the complete root construction its own actual subsection.')
edit('Thus a properly elliptic component of Kodaira\ndimension one is forced to survive in these examples, including\nafter finite base change. ', '',
     ['D03','D08'],'cdp:st:C.2.UN.6','The preceding exact degree-one component and bimeromorphic persistence assertions already state this conclusion.')
edit('\\item We give the construction as an actual hypersurface and a free\nquotient. Let',
     '\\item The occurrence of a Kodaira-dimension-one component in an abelian-surface degeneration appears in\n\\cite[Example~3.4(1), p.~99]{Fujimoto1988Log}. Let',
     ['D08','D13','D18'],'cdp:st:C.2.UN.6','Integrate the exact literature credit in the construction proof; the new proof continues to specify its own hypersurface and quotient maps.')
for a,b,types,reason in [
 ('\\item We verify properness and the local maps explicitly. With $y$ a','\\item With $y$ a',['D08'],'The following finite quotient itself supplies the properness argument.'),
 ('\\item The comparison with the punctured product is particularly simple.\nFor','\\item For',['D08'],'State the isomorphism and its inverse directly.'),
 ('actual isomorphism $(V\\setminus R)','isomorphism $(V\\setminus R)',['D08'],'Remove the process qualifier; both inverse maps remain.'),
 ('This calculation also retains the ramification at $J$.','The base equation has order $m$ along $Q_m$, including at $J$.',['D08','D22'],'State the exact order of the base function at the crossing.'),
 ('\\item We compute the canonical line without a classification assertion.\nChoose','\\item Choose',['D02'],'The invariant form and divisor prove the canonical line directly.'),
 ('\\item Here is also an integral topological check that this surface is\nnon-K\\"ahler. Choose','\\item Choose',['D08'],'The integral first-homology calculation is mathematical proof, not a check report.'),
 ('\\item The Euler calculation retains the multiple fibre. Over','\\item Over',['D08'],'The following strata include the reduced multiple fibre explicitly.'),
 ('The inverse-map resolution in (C.UC.1) applies\nand proves that neither can be contracted by a bimeromorphic\ncomparison of smooth fillings.',
  'Apply \\cref{lem:II:nonuniruled-divisors} to these compact central divisors in the smooth proper disc model $U_m$. Its strict-transform correspondence \\eqref{cdp:eq:C.UC.1} carries each one birationally onto a divisor in every smooth bimeromorphic filling.',
  ['D04','D12','D20','D22'],'Name the earlier general owner and its exact smooth-disc-model inputs instead of an unresolving literal equation number.'),
 ('Plurigenera are unchanged by a point blowup of a smooth compact\nsurface: a pluricanonical form descends off the centre and its\ncoefficients extend across that point by Hartogs. Resolution of\na surface bimeromorphism proves their birational invariance.',
  'Point blowups preserve the plurigenera of a smooth compact surface\n\\cite[Chapter~1, Proposition~2.2, p.~8]{Peters1990}. Resolving the graph of a surface bimeromorphism by such blowups therefore gives their birational invariance.',
  ['D12','D17','D18'],'Use the freshly read precise point-blowup statement, then name the graph comparison for the identical compact surfaces.'),
 ('This proves the asserted survival without imposing a description\non the other components of the base change.','This proves the asserted persistence of the component birational to $P_m$.',['D02','D08'],'The exact surviving component is the conclusion; no assertion about the other components is needed.'),
 ('The exact quotient-chart, canonical, homology, and plurigenus\ncalculations are retained in \\path{code/E_elliptic_roots.py} and\nits output.\n','',['D08','D09'],'The complete mathematical calculations remain in the proof; the verified program is cited once in the Programs appendix via addition160.')
]:edit(a,b,types,'cdp:st:C.2.UN.6',reason)

a=text.index(r'\paragraph{Literature comparison and an explicit source audit.}')
b=text.index(r'\paragraph{Credit and coordinate comparison.}',a)
orphan=text[a:b]
body=orphan[orphan.index('The action is free'):]
body=body[:body.index('\n\n\n\n')].rstrip() if '\n\n\n\n' in body else body.rstrip()
# Keep every construction and source-counterexample step, with the result numbered.
opening=r'''\subsection{Multiple elliptic fibrations on Hopf threefolds}\label{subsec:II:multiple-elliptic-hopf-threefolds}

\begin{proposition}[Multiple elliptic fibrations on Hopf threefolds]\hypertarget{tag-P328}{}\label{prop:II:multiple-elliptic-hopf-threefold}
\StatementRecord{prop:II:multiple-elliptic-hopf-threefold}{proved}{P328}{\cref{cdp:st:C.2.UN.6}; \cite[Theorem~2.8 and Corollary~2.10, pp.~96--97]{Fujimoto1988Log}}
For every $m\ge2$, put $q=e^{-2\pi}$ and define
\[
 \begin{split}
 H_m&=(\C^3\setminus\{0\})/
       \langle(a,b,c)\longmapsto(qa,q^m b,q^m c)\rangle,\\
 \Phi_m:H_m&\longrightarrow\PP^2,
       \qquad[a,b,c]\longmapsto[a^m:b:c].
 \end{split}                                             \tag{C.ER.17}\hypertarget{tag-00IV}{}\label{cdp:eq:C.ER.17}
\]
The threefold $H_m$ is smooth and compact, and $\Phi_m$ is a proper holomorphic map with connected fibres and smooth general fibre an elliptic curve. Every reduced fibre support is a smooth elliptic curve. For the line $B=(X=0)$ and its reduced inverse image $D=\{a=0\}$,
\[
             \Phi_m^*B=mD,\qquad B^2=\deg B=1,
             \qquad\pi_1(\PP^2\setminus B)=0.             \tag{C.ER.18}\hypertarget{tag-00IW}{}\label{cdp:eq:C.ER.18}
\]
These maps are counterexamples to the divisibility conclusion and the asserted surjection onto $\Z/m$ in
\cite[Theorem~2.8 and Corollary~2.10, pp.~96--97]{Fujimoto1988Log}.
They are the quotient construction \eqref{cdp:eq:C.ER.4}--\eqref{cdp:eq:C.ER.5} with $V=\PP^2$, $L=\OO(1)$ and $\sigma=X$.
\end{proposition}
\begin{proof}
'''
# The display is now in the statement, and the proof uses its local equation.
disp_start=body.index('It follows that\n\\[')
disp_end=body.index('\\]',disp_start)+2
body=body[:disp_start]+r'It follows that $\Phi_m^*B=mD$. The line has $B^2=\deg B=1$. Its complement is identified with $\C^2$ by $[X:Y:Z]\mapsto(Y/X,Z/X)$, with inverse $(u,v)\mapsto[1:u:v]$, and is simply connected.'+body[disp_end:]
body=body.replace('Thus \\eqref{cdp:eq:C.ER.17} is an explicit counterexample to both the asserted\ndivisibility and the asserted surjection to $\\Z/m$ in that theorem\nas printed. This conclusion follows from the verified map, rather\nthan from an inference that an incomplete proof makes a statement\nfalse.',
 r'Since $m\ge2$, the self-intersection $1$ is not divisible by $m$, and the trivial fundamental group has no surjection onto $\Z/m$. These give the two stated counterexamples.')
body=body.replace('In particular every fibre is connected and elliptic.', 'Every fibre is connected; its reduced support is the displayed elliptic curve, and the general fibre is smooth.')
body=body.replace('These are all\nthe hypotheses in the definition of an elliptic threefold in\n\\cite[pp.~91--92]{Fujimoto1988Log}.',r'''The smooth-complement and constant-modulus assertions are given by the inverse maps
\[
 [a,b,c]\longmapsto([a],b/a^m,c/a^m),\qquad
 ([a],u,v)\longmapsto[a,ua^m,va^m],
\]
between $\Phi_m^{-1}(\PP^2\setminus B)$ and $(\C^*/q^{\Z})\times\C^2$. They are well defined under the displayed contraction. Thus the map meets the elliptic-threefold definition of \cite[pp.~91--92]{Fujimoto1988Log} and the smooth-complement and constant-modulus premises of its Corollary~2.10.''')
body=body.replace('The problematic covering step can also be located exactly. For an',
 'The covering construction in \\cite[proof of Theorem~2.8, p.~96]{Fujimoto1988Log} has the following normalization. For an')
body=body.replace('It therefore supplies no connected branched covering of the\nbase.',
 r'The factorization $\xi^m-s_D^m=\prod_{\zeta^m=1}(\xi-\zeta s_D)$ shows that these are all its irreducible components. The normalization map is $(x,\zeta)\mapsto(x,\zeta s_D(x))$; on each component its inverse projection identifies it with the smooth original total space. The total normalization therefore has $m$ connected components.')
body=body.replace('giving an actual isomorphism of','giving an isomorphism of')
body=body.replace('A nonzero functional\n$\\ell$ on a projective line determines its unique vector $v$ with\n$\\ell(v)=1$; the equation $\\sigma=a^m\\ell$ becomes\n$v=(a^m,b,c)$. Under this identification \\eqref{cdp:eq:C.ER.5} is the inverse\nof the contraction in \\eqref{cdp:eq:C.ER.17}, giving an isomorphism of\nthe two quotient constructions.',r'''A point of $V$ is a line $\lambda\subset\C^3$, and $L_\lambda=\lambda^*$. A nonzero $\ell\in\lambda^*$ determines the unique vector $v\in\lambda$ with $\ell(v)=1$. The equality $\sigma=a^m\ell$ says $X(v)=a^m$, so write $v=(a^m,b,c)$. Conversely $(a,b,c)\ne0$ determines $\lambda=\C(a^m,b,c)$ and its unique functional taking that vector to one. These constructions are holomorphic inverse maps between the hypersurface and $\C^3\setminus\{0\}$. Under \eqref{cdp:eq:C.ER.5}, the vector $v$ changes to $q^{-m}v$ and $a$ to $q^{-1}a$, so $(a,b,c)$ changes to $(q^{-1}a,q^{-m}b,q^{-m}c)$. This is the inverse of the contraction in \eqref{cdp:eq:C.ER.17}, giving the asserted isomorphism of quotient constructions.''')
edit(orphan,opening+body+'\n\\end{proof}\n\n',
     ['D01','D02','D03','D08','D12','D13','D14','D18','D20','D22'],
     'prop:II:multiple-elliptic-hopf-threefold',
     'Promote the complete orphan Hopf-threefold construction and exact source counterexample to a numbered result; preserve both quotient maps, all hypotheses, the disconnected normalization and the inverse construction identification.')

a=text.index(r'\paragraph{Credit and coordinate comparison.}')
b=text.index(r'\begin{proposition}[A simply connected irreducible rational-normalized fibre]',a)
edit(text[a:b],r'\subsection{Cuspidal self-products}\label{subsec:II:cuspidal-self-products}'+'\n\n',
     ['D12','D13','D14'],'cdp:st:C.2.UN.8','Integrate the two duplicate source-credit paragraphs and their exact resolution map into the one construction proof.')
credit_start=text.index('The compact construction in this proof is the Namikawa')
credit_end=text.index(r'\begin{proposition}[A projective zero-Euler filling',credit_start)
edit(text[credit_start:credit_end],r'\subsection{Kummer components and vertical modifications}\label{subsec:II:kummer-occurrence}'+'\n\n',
     ['D12','D13','D14'],'cdp:st:C.2.UN.8;cdp:st:C.2.UN.13','Remove the second orphan credit after its integration and give the complete Kummer construction a subsection.')
edit('\\item Let $B=\\PP^1$, let $L=\\OO_B(1)$, and take the Weierstrass',
     '\\item The following self-product and projective small resolutions are the Namikawa construction described in\n\\cite[arXiv version~3, Proposition~4, pp.~10--12]{Rossi2017}. Let $B=\\PP^1$, let $L=\\OO_B(1)$, and take the Weierstrass',
     ['D18'],'cdp:st:C.2.UN.8','Credit the complete source construction at its exact preprint version and proof locus.')
edit('because the product fibres and every fibre of the two\nblowdowns are connected.',
     'because the product fibres and every fibre of the two\nblowdowns are connected.\n\n'+(ROOT/'agents/continuation3_provenance/final_sources/S6_SERIES_PUBLISH_rossi_comparison.tex').read_text().rstrip(),
     ['D12','D17','D18','D20','D22'],'cdp:st:C.2.UN.8',
     'Give the explicit graph-coordinate, factor-order, bundle-tensor and inverse maps to Rossi\'s displayed and global resolutions. The six local fibre collapse maps and integral computations remain because they are the receiving topological construction.')
comparison_start=text.index('The coordinate identification with the Weierstrass model of')
comparison_end=text.index('\\item The original central support',comparison_start)
comparison_old=text[comparison_start:comparison_end]
comparison_new=re.sub(r'(?<![A-Za-z\\])([RS])(?![A-Za-z])',lambda m:r'\mathcal '+m.group(1),comparison_old)
comparison_new=comparison_new.replace('Thus the actual maps are','Thus the maps are')
comparison_new=comparison_new.replace('Here is the identification of the resolved threefolds as well.\n','')
comparison_new=comparison_new.replace('The ambient Hodge numbers are those of\n\\cite[arXiv version~3, Remark~5, p.~20]{Rossi2017}.\n','')
edit(comparison_old,comparison_new,['D08','D20'],'cdp:st:C.2.UN.8',
     'Name the new projective graph coordinates calligraphic R,S so they remain distinct from the already fixed surface R and central support S. The coordinate and inverse maps are identical under this explicit change of symbols.')
edit('\\item The blowups globalize without an analytic gluing choice.',
     '\\item The two ideals are the ideals of global Weil divisors.',
     ['D02'],'cdp:st:C.2.UN.8','State the global divisor property that gives the projective blowups.')
edit('Set $f=g\\pi$, using the common projection of the fibre\nproduct.',
     'Write $p_1,p_2:X\\to R$ for the two projections and $g_X=g\\circ p_1=g\\circ p_2:X\\to B$. Set $f=g_X\\circ\\pi:Y\\to B$.',
     ['D20','D22'],'cdp:st:C.2.UN.8','Name the common base map on X separately from its composite on Y, with the exact projection and blowdown maps.')
edit(r'\omega_X=p_1^*K_R\otimes p_2^*K_R\otimes f^*T_B',
     r'\omega_X=p_1^*K_R\otimes p_2^*K_R\otimes g_X^*T_B',
     ['D20'],'cdp:st:C.2.UN.8','Use the explicitly named base map g_X on X in the adjunction formula; its pullback under pi is the map f on Y.')
edit('No exceptional divisor is introduced. Outside the origin',
     'The exceptional locus is this one-dimensional chain. Outside the origin',
     ['D02'],'cdp:st:C.2.UN.8','State the dimension of the computed exceptional locus directly.')
edit('\\cite[Proposition~4, pp.~10--11, and Remark~5, p.~20]{Rossi2017}',
     '\\cite[arXiv version~3, Proposition~4, pp.~10--12, and Remark~5, p.~20]{Rossi2017}',
     ['D18'],'cdp:st:C.2.UN.8','Match the hidden dependency citation to the exact version and complete proof pages.')
edit('This assertion is birational;\nwe do not discard the exceptional curves of the actual\nnormalization resolution.','',
     ['D02','D08','D11'],'cdp:st:C.2.UN.8','The function-field and finite birational map already prove the exact rationality assertion; the exceptional-chain calculation follows.')
edit('\\item We include the ambient groups, with their comparison\nmaps. A type-II','\\item A type-II',
     ['D08'],'cdp:st:C.2.UN.8','State the monodromy and its inclusion map directly.')
edit('The surface classification\ntherefore makes $R$ rational, so its Picard group has\nrank ten.',
     'Apply the compact surface classification\n\\cite[Chapter~VI, Theorem~1.1 and Table~10, pp.~243--244]{BHPV2004E}. The minimal model of this projective surface has $b_1=0$ and $\\kappa=-\\infty$, so it is rational. The point blowups comparing it with $R$ preserve the bimeromorphism class; thus $R$ is rational and its Picard group has rank ten.',
     ['D17','D18','D22'],'cdp:st:C.2.UN.8','Use the freshly opened exact classification table with the already proved projectivity, b1 and Kodaira dimension.')
edit('These rational Betti assertions\nmake no assertion about integral torsion in degrees\nnot already computed.','',
     ['D02','D11'],'cdp:st:C.2.UN.8','The statement already specifies rational coefficients for the ambient Betti numbers.')
old_final='''\\item Finally a sufficiently small compact fibre tube retracts
onto $S$. Its fundamental group is therefore trivial.
There is no nontrivial finite local system there, and
no nonzero integral degree-one class to restrict to
the nearby torus. The example consequently disproves
the proposed unrestricted replacement for the character
construction itself, with its actual comparison map.
The exact coordinate identities, intersection matrix,
and all displayed integer ranks are checked in
\\path{code/root_cusp_product.py} and its saved output.'''
new_final=r'''\item Restrict $f$ to a disc about any one of the six special values and apply \cref{lem:II:compact-analytic-tube}. Its inclusion and homotopy inverse identify a sufficiently small closed tube $U$ with $S$ up to homotopy. Hence $\pi_1(U)=1$ and $H^1(U,\Z)=0$. Every finite local system on $U$ is constant, and restriction to a nearby torus sends every integral degree-one class to zero. This gives the asserted obstruction to the nonzero local character of \cref{cdp:st:C.2.MH.2} in this example.'''
edit(old_final,new_final,['D03','D08','D09','D12','D20','D22'],'cdp:st:C.2.UN.8',
     'Apply the earlier full tube owner to the exact restricted proper map and state the induced group/cohomology morphisms. Remove the internal proposal and program report; addition160 cites the finite computation once.')

# The exact source identification permits citation of the known ambient Hodge result.
edit('Its generator pulls back to a nowhere-vanishing canonical\nform on $Y$ away from the small exceptional curves.\nIts coefficients and the coefficients of its inverse\nextend across that codimension-two set by Hartogs\'\ntheorem in a local canonical frame. Hence $K_Y=\\OO_Y$.',
     r'''The isomorphism over $X$ above identifies $Y$ with the Calabi--Yau resolution in \cite[arXiv version~3, proof of Corollary~2, pp.~19--20; Definition~1, p.~3]{Rossi2017}. Hence $K_Y\simeq\OO_Y$ and $h^1(Y,\OO_Y)=h^2(Y,\OO_Y)=0$, by the stated Calabi--Yau conditions and projective Hodge symmetry.''',
     ['D12','D17','D18'],'cdp:st:C.2.UN.8','Use the exact resolved-threefold isomorphism to apply the source Calabi--Yau assertion; retain the relative adjunction formula and singular-fibre duality computation.')
a=text.index('Projectivity and $K_Y=\\OO_Y$ give')
b=text.index('\\item Let $K=\\C(t)$',a)
edit(text[a:b],'\n',['D12','D17'],'cdp:st:C.2.UN.8',
     'The source now supplies the coherent vanishings. The rational-surface and Picard-rank detour was used only to re-derive the already cited ambient Hodge numbers and is removed from the body; the complete old argument remains in this defect record.')
a=text.index('\\item Let $K=\\C(t)$')
b=text.index('\\item Euler localization now gives',a)
generic_old=text[a:b]
matrix=re.search(r'\\\[\s*\\begin\{pmatrix\}.*?\\\]',generic_old,re.S).group(0)
generic_remark=r'''\begin{remark}[Generic divisor classes of the cuspidal self-product]\hypertarget{tag-P334}{}\label{rem:II:cuspidal-generic-divisors}
\StatementRecord{rem:II:cuspidal-generic-divisors}{proved}{P334}{\cref{cdp:st:C.2.UN.8}}
Let $K=\C(t)$, let $E_K$ be the generic elliptic curve of \eqref{cdp:eq:C.CP.3}, and fix a primitive cube root $\rho$. The two factors, the diagonal and the graph of $\rho$ on $A_K=E_K\times E_K$ span $\operatorname{NS}(A_K)\otimes\Q$. Their intersection matrix, in that order, is
'''+matrix+r'''
\end{remark}
\begin{proof}
Each curve has self-intersection zero. Each factor meets the other three in one point with multiplicity one. The diagonal meets the graph of $\rho$ in the kernel of $1-\rho$; on the triangular elliptic lattice this kernel has order three. These give \eqref{cdp:eq:C.CP.10}, whose determinant is $-3$, so the four classes are independent.

For the upper bound, use $K'=K(u)$ with $u^6=p(t)$. The inverse substitutions
\[
 (X,Y)\longmapsto(u^2X,u^3Y),\qquad
 (x,y)\longmapsto(x/u^2,y/u^3)
\]
identify $E_{K'}$ with the constant elliptic curve $E_0:Y^2=X^3+1$. Base change to an algebraic closure identifies its geometric N\'eron--Severi group with that of $(E_0\times E_0)_{\overline K}$. For the complex abelian surface $E_0^2$, the first Chern class embeds this group into its integral $(1,1)$ classes, and $h^{1,1}(E_0^2)=4$. The Picard scheme and its identity component commute with algebraically closed field extension, and its connected components over $\C$ remain geometrically connected; hence this extension preserves the N\'eron--Severi group. Pullback embeds the group of $K$-defined divisor classes into that geometric group. Its rank is therefore at most four, and the four independent classes already defined over $K$ prove the assertion.
\end{proof}

'''
edit(generic_old,'',['D12','D17'],'cdp:st:C.2.UN.8;rem:II:cuspidal-generic-divisors',
     'Remove the long divisor-restriction re-derivation of the known ambient Hodge numbers. Preserve the distinct exact generic NS matrix and field-extension maps as the following short numbered remark, rather than assigning them to the cited source.')
kummer_heading=r'\subsection{Kummer components and vertical modifications}\label{subsec:II:kummer-occurrence}'
edit(kummer_heading,generic_remark+kummer_heading,['D12','D13','D20'],
     'rem:II:cuspidal-generic-divisors','Give the existing generic divisor matrix and its exact constant-field comparison a single numbered owner; its permanent equation label remains at the matrix.')
edit('\\item Euler localization now gives $e(Y)=6\\cdot6=36$.\nPoincar\\\'e duality and $b_1=0$ yield $b_3=8$;\nthe remaining Betti numbers and Hodge numbers follow\nas displayed in \\eqref{cdp:eq:C.CP.2}. ',
     r'''\item For this same resolved threefold, \cite[arXiv version~3, Remark~5, p.~20]{Rossi2017} gives $h^{1,1}(Y)=21$ and $h^{2,1}(Y)=3$. Together with the Calabi--Yau conditions above, projective Hodge decomposition and duality give the ambient groups in \eqref{cdp:eq:C.CP.2}. The six computed singular-fibre supports also give $e(Y)=6\cdot6=36$ by Euler localization.''',
     ['D12','D17','D18'],'cdp:st:C.2.UN.8','Cite the known Hodge numbers after proving the exact isomorphism to the source resolution; retain the singular-support Euler computation and the coefficient conventions.')

edit('The maps to the base and the nearby tori are retained.',
     'Every blowup is vertical, so the composition has the same map on the complement of the two special fibres.',
     ['D08','D20'],'cdp:st:C.2.UN.13','State the precise open-set isomorphism preserved by the vertical blowups.')
for source_context in [
    r'\SeriesRef{cdp:st:C.2.UN.3}; \cite[Chapter~1, Example~1.3(iii)]{HuybrechtsK3Draft}',
    r'construction; see \cite[Chapter~1, Example~1.3(iii)]{HuybrechtsK3Draft}.']:
    edit(source_context,source_context.replace('Example~1.3(iii)]','Example~1.3(iii), pp.~8--9]'),
         ['D18'],'cdp:st:C.2.UN.13','Use the freshly read complete author-draft locus for the same arbitrary abelian surface A.')
edit('We verify its smoothness and its exact relation\nto the quotient before using it. Write the coordinates of a',
     'Write the coordinates of a',['D08'],'cdp:st:C.2.UN.13','The following invariant-ring charts prove smoothness and identify the quotient map directly.')
edit('Thus the asserted persistence concerns bimeromorphic comparison\nover the original base; its relation to base change is given\nby this specified map.','',
     ['D02','D11'],'cdp:st:C.2.UN.13','The statement has already specified both original-base bimeromorphic persistence and the exact quadratic normalization map.')
edit('Here the two required properties can also be checked in the\nsame charts.','The two-form and coherent cohomology maps in these charts are as follows.',
     ['D08','D17'],'cdp:st:C.2.UN.13','The classical Kummer result is cited; the displayed maps are retained for the actual subsequent ambient/support computations.')
edit('Hence the actual inclusion--exclusion\ncomparison','Hence inclusion--exclusion',
     ['D08'],'cdp:st:C.2.UN.13','The explicit component and intersection Euler numbers give the computation.')
edit('\\item We give the ambient cohomology maps as well. For the finite',
     '\\item For the finite',['D08'],'cdp:st:C.2.UN.13','Apply the already proved finite invariant-sheaf map directly.')
edit('To verify this\nwithout suppressing the quotient singularity, filter the',
     'Filter the',['D02'],'cdp:st:C.2.UN.13','The formal-functions calculation already uses the exact quotient resolution.')
edit('Every operation starts at a fresh smooth point on the',
     'Every operation starts at a smooth point on the',['D08'],'cdp:st:C.2.UN.13','The explicit exclusions from the other components specify the admissible centre.')
edit('The exact charts of \\ref{cdp:st:C.2.UN.4} retain simple\nnormal crossings',
     'The charts of \\cref{cdp:st:C.2.UN.4} preserve simple\nnormal crossings',['D08'],'cdp:st:C.2.UN.13','Describe the geometric SNC property under the same explicit maps.')

general_start=text.index('\\item We retain the support comparison under each of these blowups,')
general_end=text.index('A point step therefore adds',general_start)
general_old=text[general_start:general_end]
support_application=r'''\item For one of these blowups write $\sigma:\widehat W\to W'$, let $C$ be its smooth centre of ambient codimension $c$, and let $S$ be the current reduced support. Apply \cref{lem:II:blowup-topology} with
\[
 (Y,Z,r,\pi_Z,S,S')
  =(W',C,c,\sigma,S,\sigma^{-1}(S)_{\rm red}).
\]
Its restricted ambient Gysin map in \eqref{cdp:eq:C.KM.S2} identifies the cohomology of this full inverse image. This includes the four intersections of the quartic with the other support component.
'''
edit(general_old,support_application,['D08','D12','D17','D20','D22'],'cdp:st:C.2.UN.13;lem:II:blowup-topology',
     'Transfer the entire general full-support blowup cohomology result and its label to the earlier P234 owner. The application names every geometric input and the restricted ambient Gysin morphism.')
edit('The inverse-map resolution in \\ref{cdp:st:C.2.UN.3} therefore\nprevents its contraction by any bimeromorphic comparison\nbetween smooth threefold fillings. The finite-base-change\ncomparison is different and explicit:',
     'Apply \\cref{lem:II:nonuniruled-divisors} to this compact central divisor in the given smooth threefold filling. Its strict-transform correspondence prevents contraction under a bimeromorphic comparison of smooth fillings. For the quadratic base change,',
     ['D04','D12','D20','D22'],'cdp:st:C.2.UN.13','Use the full earlier general divisor owner with the Kummer component and name the separate quadratic map explicitly.')
program_start=text.index('The construction is based on the classical Kummer quotient.')
program_end=text.index('\\end{enumerate}',program_start)
edit(text[program_start:program_end],'\n',
     ['D03','D08','D09'],'cdp:st:C.2.UN.13',
     'The mathematical construction, quotient maps and all cohomology computations remain; addition160 names its verified generator once, with the output represented through that generator.')

# Local equation numbers are now section-based while all existing targets survive.
for match in list(re.finditer(r'\\\[(.*?)\\\]',text,re.S)):
    block=match.group(0)
    if re.search(r'\\tag\{[^}]+\}',block):
        converted='\\begin{equation}'+re.sub(r'\\tag\{[^}]+\}','',match.group(1))+'\\end{equation}'
        edit(block,converted,['D04','D19'],'cdp:st:C.2.UN.6;prop:II:multiple-elliptic-hopf-threefold;cdp:st:C.2.UN.8;cdp:st:C.2.UN.13',
             'Replace the inherited manual equation number by the section equation counter; retain the full formula, label and permanent tag.')

text+=r'\subsection{Paired roots and projective elliptic components}\label{subsec:II:paired-root-occurrence}'+'\n\n'

# Prepare the full earlier topology owner, including its explicit support map.
current=SOURCE.read_text()
mark=r'\begin{lemma}[Topology of a blowup]'
a=current.index(mark); b=current.index(r'\end{proof}',a)+len(r'\end{proof}')
owner_old=current[a:b]
owner_new=owner_old.replace("its full inverse image $S'=\\pi_Z^{-1}(S)$ satisfies \\eqref{cdp:eq:C.VR.4}.",
 "its full inverse image $S'=\\pi_Z^{-1}(S)$ satisfies \\eqref{cdp:eq:C.VR.4} and the rational cohomology isomorphism \\eqref{cdp:eq:C.KM.S2}.")
anchor='For the fundamental group, choose a tubular neighbourhood'
support_proof=r'''For the full inverse image of a compact analytic $S\supset Z$, let $\iota:S'\hookrightarrow Y'$ and $j_S:E_Z\hookrightarrow S'$ be the inclusions, and put $\pi_S=\pi_Z|_{S'}$. The support cohomology map is
\begin{equation}
 \begin{aligned}
 H^q(S,\Q)\oplus\bigoplus_{i=1}^{r-1}H^{q-2i}(Z,\Q)
   &\xrightarrow{\ \simeq\ }H^q(S',\Q),\\
 (\alpha,\beta_1,\ldots,\beta_{r-1})
   &\longmapsto\pi_S^*\alpha+
     \sum_{i=1}^{r-1}\iota^*j_*(\xi^{i-1}p^*\beta_i).
 \end{aligned}
 \hypertarget{tag-00PU}{}\label{cdp:eq:C.KM.S2}
\end{equation}
The proper map induces a continuous bijection $S'/E_Z\to S/Z$. These are compact Hausdorff spaces, so it is a homeomorphism. Compatible triangulations make $(S,Z)$ and $(S',E_Z)$ cofibrations. Their relative cohomology is consequently identified by pullback. Comparing the two relative exact sequences gives
\[
 \begin{aligned}
 \cdots\longrightarrow H^q(S,\Q)
 &\xrightarrow{(\pi_S^*,i_Z^*)}H^q(S',\Q)\oplus H^q(Z,\Q)\\
 &\xrightarrow{\ j_S^*-p^*\ }H^q(E_Z,\Q)
 \longrightarrow H^{q+1}(S,\Q)\longrightarrow\cdots,
 \end{aligned}
\]
where $i_Z:Z\hookrightarrow S$. The $i=0$ projective-bundle summand is the image of the second factor under $-p^*$. For every $i>0$, the restriction of $\iota^*j_*(\xi^{i-1}p^*\beta_i)$ to $E_Z$ is $-\xi^i p^*\beta_i$. Thus the middle map is surjective in every degree, and the displayed sequence becomes short exact in every degree.

Pullback $\pi_S^*$ is injective: if $\pi_S^*\alpha=0$, restriction to $E_Z$ gives $p^*i_Z^*\alpha=0$. The projective-bundle decomposition makes $p^*$ injective, so $i_Z^*\alpha=0$ as well; injectivity of $(\pi_S^*,i_Z^*)$ then gives $\alpha=0$. For an arbitrary class on $S'$, subtract the displayed Gysin terms to remove all its positive powers of $\xi$ on $E_Z$. The remaining restriction has the form $p^*\gamma$, and exactness makes that remaining class a pullback from $S$. Restriction to $E_Z$ also shows that a sum in \eqref{cdp:eq:C.KM.S2} can vanish only when each $\beta_i=0$; injectivity of $\pi_S^*$ then gives $\alpha=0$. This proves the stated isomorphism for the full inverse image, including centres meeting several components of $S$.

'''
assert owner_new.count(anchor)==1
owner_new=owner_new.replace(anchor,support_proof+anchor,1)
preserve_identifiers(old+owner_old,text+owner_new)
for old_ids,new_ids in zip(identifiers(old+owner_old),identifiers(text+owner_new)):
    assert all(new_ids[k]==v for k,v in old_ids.items())
    assert all(new_ids[k]==1 for k in new_ids-old_ids)
assert text.count(r'\label{prop:II:multiple-elliptic-hopf-threefold}')==1
for n,kind in enumerate(['D12','D17','D20','D22'],1):
    rows.append(dict(change_id=f'II-C3-ROOT-SUPPORT-BLOWUP-{n:02}',type=kind,
        statement_id='lem:II:blowup-topology',old_location='General support-cohomology proof inside UN13',
        old_page='checkpoint35 source; final concordance pending',new_location='Complete earlier topology-of-blowup owner P234',
        new_page='integrated final build pending',old_text=general_old,new_text=support_proof,
        reason='Give the general full-inverse-image result its single earlier owner. The relative exact square, pullback injection and restricted ambient Gysin splitting prove the precise direct-sum morphism; all original ambient integral and fundamental-group arguments remain.',
        review_status='Complete original owner and application read; complete receiving rereading required before admission. Exposed editorial comparison only.'))

(folder/(prefix+'replacement.tex')).write_text(text,newline='\n')
(folder/(prefix+'P234.tex')).write_text(owner_new,newline='\n')
(folder/(prefix+'guards.json')).write_text(json.dumps([
    {'key':'first-occurrence-units','old':old,'new':text},
    {'key':'full-support-blowup-owner','old':owner_old,'new':owner_new}],ensure_ascii=False,indent=2)+'\n',newline='\n')
write_tsv(folder/(prefix+'defects.tsv'),read_tsv(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv')[0],rows)
print('Prepared',len(text.splitlines()),'occurrence lines;',len(owner_new.splitlines()),'owner lines;',len(rows),'defects. Root receiving rereading pending.')
