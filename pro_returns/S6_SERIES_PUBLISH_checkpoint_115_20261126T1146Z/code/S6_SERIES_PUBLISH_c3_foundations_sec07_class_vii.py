from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

p=Package('class_vii','subsec:II:class-vii-canonical-boundaries')
blocks={f'cdp:st:C.2.VII.{i}':block(ORIGINAL,f'cdp:st:C.2.VII.{i}') for i in range(1,5)}
originals=dict(blocks)
k='cdp:st:C.2.VII.1';s=blocks[k]
for old,new in [
 (r'\cite[Theorem~0.2, Proposition~2.29 and Theorem~2.38]{Dloussky2006}',r'\cite[arXiv v3, Theorem~0.2, p.~2; Proposition~2.29, p.~19; Theorem~2.38, pp.~24--25]{Dloussky2006}'),
 (r'\cite[Corollary~2.25 and Proposition~2.27]{Dloussky2006}',r'\cite[arXiv v3, Corollary~2.25 and Proposition~2.27, pp.~16--19]{Dloussky2006}'),
 (r'\cite[Lemma~2.22 and the following paragraph; Proposition~2.27]{Dloussky2006}',r'\cite[arXiv v3, Lemma~2.22 and the following paragraph, p.~15; Proposition~2.27, pp.~17--19]{Dloussky2006}')
]:s=p.edit(s,old,new,'D18',k,'The exact primary arXiv v3 loci and complete relevant proofs were opened; the receiving bibliography already identifies that version.')
s=p.edit(s,'We specify the established surface results used in this\ncomparison. For a minimal class VII surface with positive','For a minimal class VII surface with positive','D08',k,'Begin with the hypothesis to which the cited theorem applies.')
s=p.edit(s,'These are consequences of the proved theorem about\nanticanonical divisors; no classification assertion about\nclass VII surfaces without such a divisor is used.','', 'D02,D11',k,'The effective torsion anticanonical divisor is already a hypothesis, and the exact cited NAC applications are retained.')
s=p.edit(s,'This deduction uses the torsion relation, not merely\nthe vanishing of its real first Chern class.','', 'D02',k,'The complete torsion-trivializing power and meromorphic-function argument already proves the coefficient k=1.')
s=p.edit(s,'We verify the transfer through the actual blowdowns.','Let us transfer these conclusions through point blowups.','D08',k,'Name the geometric operation directly.')
old='At each individual blowup\nthe canonical divisor formula and the pushforward section\ngive the exact divisor equality'
new='At each point blowup, \\cref{lem:II:canonical-boundary-blowup} applies to the effective boundary and its torsion canonical line. Its coefficient identity gives'
s=p.edit(s,old,new,'D12',k,'P232 owns the canonical-boundary blowup calculation. Keep the torsion-line descent and the divisor equality at this class-VII application.')
old='The coefficient of $E$ is\n$\\operatorname{mult}_pD_{\\mathrm{old}}-1$.\nEffectivity forces the centre to lie on $D_{\\mathrm{old}}$.'
new='Thus the coefficient of $E$ is $\\operatorname{mult}_pD_{\\mathrm{old}}-1\\ge0$, as in that lemma.'
s=p.edit(s,old,new,'D12',k,'Use the earlier owner for multiplicity and effectivity, retaining the subsequent graph and rational-curve-count argument.')
old='For a minimal model with $b_2=0$, the nonzero effective\ndivisor excludes the curve-free Inoue surfaces.'
new='For a minimal model with $b_2=0$, \\cref{lem:II:negative-kodaira-models} applies to its nonzero effective divisor and makes the surface Hopf.'
s=p.edit(s,old,new,'D14,D18',k,'P244 supplies the full minimal class-VII b2=0 classification input and its nonempty-curve hypothesis; C.3.8 is retained only for the explicit Hopf contraction construction.')
blocks[k]=s

k='cdp:st:C.2.VII.2';s=blocks[k]
s=p.edit(s,'The conductor scheme may be nonreduced and its generic\ntransverse exponent is unrestricted.','', 'D11',k,'The statement defines the full conductor-image scheme and imposes no reducedness or exponent restriction; both stay in the finite-duality proof.')
s=p.edit(s,'The actual conductor duality of \\SeriesRef{cdp:st:A.5.12} is','The finite conductor duality of \\cref{lem:II:conductor-duality} is','D12,D04',k,'P222 owns the general Gorenstein finite-normalization duality with exactly these hypotheses; the cohomological application remains here.')
a=s.index('Let $n$ be the number of irreducible');b=s.index('\n\\item The only possible negative value',a)
old=s[a:b]
new=r'''Apply \cref{lem:II:curve-euler-delta}, with $n_0$ the number of rational-normalized components and $r_x=s_x$ the number of branches at $x$. Its formulas \eqref{cdp:eq:C.VII.5}, together with \eqref{cdp:eq:C.VII.3}, give $e(C)\ge n_0-1$.
'''
s=p.edit(s,old,new,'D12,D14,D20',k,'Move the coherent/topological normalization identities and the branch-constant proof of δ≥s−1 to P290 before both this application and VII.4. Explicitly identify the old local branch notation r_x with s_x.')
s=p.edit(s,'specified hypersurface and resolution maps','hypersurface and resolution maps','D08',k,'Keep the actual branch-reception argument and all maps, expressed directly.')
s=p.edit(s,'Both possibilities contradict C.2.VII.1:',r'Both possibilities contradict \cref{cdp:st:C.2.VII.1}:','D04',k,'Use the current in-paper statement number.')
blocks[k]=s

k='cdp:st:C.2.VII.3';s=blocks[k]
s=p.edit(s,'No restriction on the singularity type or conductor\nmultiplicity of $S$ is made.','', 'D02,D11',k,'The irreducible nonnormal fibre and its full multiplicity m are the statement’s complete singularity domain.')
a=s.index(r'\item The canonical evaluation');b=s.index(r'\item We compute',a);old=s[a:b]
new=r'''\item Let $\eta:T\to S$ be normalization, let $\pi:Z\to T$ be its minimal resolution, and let $D>0$ be the resolution conductor. By \cref{lem:II:torus-tube-numerical}, $\omega_S$ is torsion, $\chi(\OO_S)=0$ and $K_Z+D=(\eta\pi)^*\omega_S$. Put $C=\Gamma_{\mathrm{red}}$ and $A=(\eta^{-1}C)_{\mathrm{red}}$. Thus \cref{cdp:st:C.2.VII.1,cdp:st:C.2.VII.2} apply to these maps and divisors.

'''
s=p.edit(s,old,new,'D12,D14',k,'Use P281 at the same smooth proper full-fibre data; retain the original compact b2=0 statement while obtaining its numerical inputs from the earlier local owner.')
s=p.edit(s,'Their negative-definite intersection matrix makes','Their intersection matrix is negative definite by \\cref{lem:II:exceptional-intersection}; this makes','D12',k,'P243 owns negative definiteness, while the specific −2-curve/tree inference stays in this proof.')
blocks[k]=s

k='cdp:st:C.2.VII.4';s=blocks[k]
s=p.edit(s,'Retain the irreducible class VII situation of','Use the irreducible class VII situation of','D08',k,'State the inherited hypotheses directly.')
s=p.edit(s,'both directions of \\eqref{cdp:eq:C.VII.9}, using actual\nbranch numbers rather than an assumption\nabout a local singularity type.','both directions of \\eqref{cdp:eq:C.VII.9} for these normalization branch numbers.','D02,D08',k,'Keep the exact branch-count formula and both directions of the criterion.')
s=p.edit(s,'These are exact consequences for fibres which\nsatisfy the criterion; no separate claim\nthat all such abstract curve patterns admit\na torus smoothing is used.','', 'D02,D11',k,'The theorem is stated for the given full fibre, and no realization statement is added.')
s=p.edit(s,'The exact formula (C.INT.26) now implies','Lemma~\\ref{lem:II:curve-euler-delta} and \\eqref{cdp:eq:C.INT.26} imply','D12,D14',k,'P290 extracts the complete formula and equality proof from INT.3 before this use, with the same normalized genera and χ≥0 hypothesis.')
s=p.edit(s,'This contradicts\nnegative definiteness of a resolution\'s\nexceptional intersection matrix.','This contradicts \\cref{lem:II:exceptional-intersection}, since its nonzero exceptional divisor has square zero.','D12',k,'Apply P243 to the explicit total transform of the rational cycle; its pullback square remains zero.')
old='As in the\nlast paragraph of \\ref{cdp:st:C.2.INT.3}, a nonempty\nblowup sequence would have a last\n$(-1)$ curve, contradicting minimality\nof the resolution.'
new='For the point-blowup map $\\sigma:Z\\to Z_0$ to this Hopf minimal model, every $\\sigma$-exceptional curve is therefore $\\pi$-exceptional. Lemma~\\ref{lem:II:last-blowup-minimal-resolution} makes $\\sigma$ an isomorphism.'
s=p.edit(s,old,new,'D12,D14',k,'P291 owns the last-blowup argument at the exact pair of maps; remove the forward INT.3 proof reference while preserving the smooth minimal Hopf conclusion.')
old='makes $\\sigma$ an isomorphism. Thus the normalization\nis already a smooth minimal Hopf surface.'
new='makes $\\sigma$ an isomorphism. Every curve on the minimal Hopf surface $Z$ has square zero, as proved in \\cref{night:P4R.5}. Lemma~\\ref{lem:II:exceptional-intersection} therefore excludes every $\\pi$-exceptional curve. Thus $\\pi$ is an isomorphism, and the normalization is already a smooth minimal Hopf surface.'
s=p.edit(s,old,new,'D14,D25',k,'State separately the two maps: P291 makes the point-blowup map sigma an isomorphism, then the square-zero curves on that Hopf source and P243 make the normal-surface resolution pi an isomorphism. This supplies the asserted smooth normalization without identifying the two maps.')
s=p.edit(s,r'\SeriesRef{cdp:st:C.2.INT.3}',r'\cref{lem:II:curve-euler-delta,lem:II:last-blowup-minimal-resolution}','D14',k,'Update the hidden dependency to the earlier owners of the only INT.3 inputs.')
blocks[k]=s

k='cdp:st:C.2.VII.1';s=blocks[k]
insert=r'''Let $\sigma:Z\to Z_0$ be a minimal-model blowdown and put $D_0=\sigma_*D$. Then $D_0>0$ and $K_{Z_0}+D_0$ is torsion. For $b_2(Z_0)=0$, the surface $Z_0$ is Hopf and $(D_0)_{\rm red}$ is a disjoint union of smooth elliptic curves. For $b_2(Z_0)>0$, the surface has a global spherical shell and exactly $b_2(Z_0)$ rational curves. Its boundary is one of the following:
\begin{enumerate}
\item an intermediate surface, whose boundary support is a connected rational cycle with rational trees attached;
\item an Inoue--Hirzebruch surface, on which $D_0$ is the reduced cycle or union of two reduced cycles;
\item a parabolic Inoue surface, with a smooth elliptic curve $E$ and a disjoint rational cycle $C$, on which $D_0=E+C$, $C^2=0$, $C\equiv0$ and $E^2=-b_2(Z_0)$.
\end{enumerate}
'''
old='first one.\n\\end{proposition}'
s=p.edit(s,old,'first one.\n\n'+insert+'\\end{proposition}','D12,D14',k,'Put the proved minimal-model alternatives and the exact Inoue–Hirzebruch/parabolic coefficient conclusions at the single general owner. They are extracted from the complete VII.1 and current P4.23 proofs, under the identical effective torsion-anticanonical input; no classification of surfaces without that divisor is asserted.')

# The torsion descent must precede the application on the minimal model.
a=s.index(r'\item Let us transfer');b=s.index('At each point blowup,',a)
old=s[a:b]
descent=r'''\item Let $\sigma:Z\to Z_0$ be the stated minimal-model blowdown. A torsion line is represented by a finite unitary character, and point blowups induce isomorphisms on fundamental groups by \cref{lem:II:boundary-blowup-groups}. Thus $K_Z+D$ descends to a torsion line on $Z_0$. Pushing forward a meromorphic canonical section with poles along $D$, or its torsion-trivializing power, gives the effective divisor $D_0$ and $K_{Z_0}+D_0$ torsion. The divisor $D_0$ is nonzero, since a torsion canonical bundle would give Kodaira dimension zero.

'''
s=s[:a]+r'\item '+s[b:]
first=s.index(r'\item For a minimal class VII surface')
s=s[:first]+descent+s[first:]
p.record('D12,D14',k,old,descent,'Place the exact torsion-character and pushed-forward meromorphic-section maps before the minimal-model classification to which they supply hypotheses.')
old='existence of a numerically\nanticanonical divisor implies existence of a global\nspherical shell by'
new=r'''put $L_0=\mathcal O_{Z_0}(K_{Z_0}+D_0)$. The numerically anticanonical datum of \cite[arXiv v3, Definition~2.20, p.~14]{Dloussky2006} is $m=1$ and $F=L_0^{-1}$, because $K_{Z_0}+D_0+F=0$ in $\operatorname{Pic}(Z_0)$. It gives a global spherical shell by'''
s=p.edit(s,old,new,'D12,D18',k,'Preserve P4.23’s exact NAC datum and its opened v3 definition at the common general owner.')
s=p.edit(s,'The rational\ncurve count is at most $b_2$, as stated and used in','A surface with a global spherical shell has exactly $b_2$ rational curves, and every minimal class VII surface has at most $b_2$, as stated in','D12,D18',k,'The exact GSS count and general upper bound are both stated on the opened DOT2003 p283; this retains the stronger minimal-model count used by P4.23.')
old=r'\item There is a coefficient issue in the parabolic Inoue case'+'\nwhich the torsion hypothesis resolves explicitly. Write'
new=r'''\item On an Inoue--Hirzebruch surface, the reduced cycle or union of two cycles is numerically anticanonical. Its curve intersection matrix is negative definite. Subtracting this divisor from $D_0$ and intersecting with every component gives a vector in the kernel of that matrix; hence all coefficient differences are zero, and $D_0$ is reduced nodal.

For the parabolic Inoue case, write'''
s=p.edit(s,old,new,'D12',k,'Transfer P4.23’s complete reduced-cycle coefficient argument to VII.1, followed by VII.1’s complete torsion proof forcing the parabolic coefficient to one.')
old='Consequently an effective integral divisor with\n$c_1(K_{Z_0}+D_0)_{\\mathbb R}=0$ has the form'
new=r'''The cycle has $C^2=0$ by \cite[arXiv v3, Remark~0.6, pp.~3--4]{Dloussky2006}. The negative-definite intersection form of the class VII surface, described in \cite[arXiv v3, \S1, p.~4]{Dloussky2006}, then gives $C\equiv0$; the canonical relation also gives $E^2=K_{Z_0}^2=-b_2(Z_0)$. Consequently an effective integral divisor with
$c_1(K_{Z_0}+D_0)_{\mathbb R}=0$ has the form'''
s=p.edit(s,old,new,'D12,D18',k,'Preserve P4.23’s stronger square-zero and numerical-triviality conclusions at the common owner. Opened and read Dloussky v3 Remark0.6 pp3–4 and Section1 p4; the morphism is the divisor class map into its negative-definite H2 intersection space.')
blocks[k]=s

owners=(OUT/'S6_SERIES_PUBLISH_II_sec07_curve_minimality.tex').read_text()
fragment=r'\subsection{Class VII canonical boundaries}\label{subsec:II:class-vii-canonical-boundaries}'+'\n\n'+owners+'\n'
for k in blocks:
    blocks[k]=p.clean(blocks[k],k)
    if k!='cdp:st:C.2.VII.1':fragment+=blocks[k]+'\n'
    p.guard('move '+k,originals[k],'','Its complete statement and proof now stand in the earlier class-VII prerequisite subsection.')
    p.record('D14',k,originals[k].splitlines()[0],blocks[k].splitlines()[0],'Place the class-VII canonical and coherent conductor inputs before CR.1, which uses VII.2; preserve all stronger equality criteria and their explicit maps.')

anchor=r'\subsection{Contracted ruled boundaries}\label{subsec:II:contracted-ruled-boundaries}'
p.guards.insert(0,dict(key='class VII prerequisite subsection',old=anchor,new=fragment.rstrip()+'\n\n'+anchor,reason='VII.2 precedes its first contracted-boundary consumer, and VII.4 now has earlier curve/minimality inputs.'))

early=blocks['cdp:st:C.2.VII.1']
(OUT/'S6_SERIES_PUBLISH_II_sec07_vii1_early.tex').write_text(early,newline='\n')
current=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
p423=block(current,'night:P4.23')
a=p423.index(r'\item Let $\beta:T\to T_0$');b=p423.index(r'\item At every point blowup',a)
old=p423[a:b]
new=r'''\item Let $\beta:T\to T_0$ be the blowdown map, let $D$ be the conductor and put $D_0=\beta_*D$. Proposition~\ref{night:P4.12} makes $K_T+D$ torsion. Apply \cref{cdp:st:C.2.VII.1} to the smooth class VII surface $T$, its effective conductor $D$, and this blowdown. It gives $D_0>0$, $L=\mathcal O_{T_0}(K_{T_0}+D_0)$ torsion, and the three minimal-model alternatives. The NAC datum in its proof is precisely $m=1$ and $F=L^{-1}$ in \cite[arXiv v3, Definition~2.20, p.~14]{Dloussky2006}; Theorem~0.2, Proposition~2.29 and Proposition~2.27 apply through that identity. The intermediate configuration and $\pi_1(T_0)=\mathbb Z$ are described in \cite[\S1, pp.~284--285]{DOT2003}.

\item In the Inoue--Hirzebruch case, \cref{cdp:st:C.2.VII.1} identifies $D_0$ with the reduced cycle or pair of cycles. In the parabolic Inoue case it gives $D_0=E+\Gamma$, using the torsion of $\mathcal O((k-1)\Gamma)$ to force $k=1$. Thus in both cases $D_0$ is reduced nodal, with the same pushed-forward conductor as in the preceding step.

'''
p.guard('P4.23 shared minimal-model input',old,new,'Apply the single earlier VII.1 owner to the exact blowdown and torsion conductor; preserve the entire later NC/tangent and one-relator proof unchanged.')
p.record('D12,D14','night:P4.23',old,new,'The complete old P4.23 proof and complete VII.1 proof were compared. Its two preliminary minimal-model/coefficient steps now apply the common earlier owner; the exact m=1,F=L^−1 datum and all downstream P232/P245/P246 references and group relations remain.')
firstline=p423.splitlines()[0]
p.guard('early VII1 before P4.23',firstline,early+'\n'+firstline,'The general canonical-boundary owner precedes its first torus-fibre application, within the existing class-VII-minimal-model subsection.')

# Transfer the general curve equality argument and last-blowup application from INT.3.
old_block=block(ORIGINAL,'cdp:st:C.2.INT.3')
a=old_block.index(r'\item Each normalized component of $C$');b=old_block.index(r'\item We finish the topological comparison',a)
old=old_block[a:b]
new=r'''\item Every normalized component of $C$ has genus zero or one, since it is dominated by a curve of $(D_i)_{\rm red}$. Apply \cref{lem:II:curve-euler-delta} with \eqref{cdp:eq:C.INT.25}. Its formula \eqref{cdp:eq:C.INT.26} gives $e(C)\ge0$, with equality precisely for a disjoint union of smooth elliptic curves.

'''
p.guard('INT3 curve equality application',old,new,'P290 owns the complete normalization formula and equality argument at exactly these genus and coherent Euler hypotheses.')
p.record('D12,D14','cdp:st:C.2.INT.3',old,new,'The equality criterion is proved once at P290 before VII.4 and this reducible-fibre application; C.INT.26 is retained there.')
old='If $N_i>0$, the last point blowup in\n$\\sigma_i$ supplies a $(-1)$ curve on $Z_i$.\nIts being $\\pi_i$-exceptional contradicts the\nminimality of that resolution. Hence $N_i=0$.'
new='Every curve exceptional for $\\sigma_i$ is consequently $\\pi_i$-exceptional. Lemma~\\ref{lem:II:last-blowup-minimal-resolution} applies to these two maps and gives $N_i=0$.'
assert old in old_block
p.guard('INT3 last-blowup application',old,new,'Apply the same earlier minimal-resolution lemma used in VII.4.')
p.record('D12,D14','cdp:st:C.2.INT.3',old,new,'The full minimality conclusion is unchanged, and the precise exceptional-curve inclusion is stated before applying P291.')
old=r'\eqref{cdp:eq:C.INT.26}--\eqref{cdp:eq:C.INT.27}'
new=r'\eqref{cdp:eq:C.INT.26} and \eqref{cdp:eq:C.INT.27}'
p.guard('INT3 explicit separated Euler references',old,new,'The shared curve formula now stands earlier; name exactly the two equations used rather than the intervening numbering interval.')
p.record('D19','cdp:st:C.2.INT.3',old,new,'Preserve the exact two-formula scope after moving C.INT.26 to its earlier owner.')
old=r'\eqref{cdp:eq:C.MH.10}--\eqref{cdp:eq:C.MH.12}'
new=r'\eqref{cdp:eq:C.MH.10} and \eqref{cdp:eq:C.MH.12}'
p.guard('UN7 explicit character descent references',old,new,'MH.11 is an alias at MH.12; the two displays are the exact descent and composed-isomorphism maps used.')
p.record('D19','cdp:st:C.2.UN.7',old,new,'After the admitted shared character owner, cite the exact two displays instead of a numbering interval that includes the interposed purity formula.')
for oldtag,label in [('C.VII.5','cdp:eq:C.VII.5'),('C.INT.26','cdp:eq:C.INT.26')]:
    p.equations.append(dict(old_tag=oldtag,label=label,owner='lem:II:curve-euler-delta'))
    p.record('D19',label,oldtag,label,'The moved normalization identity keeps its permanent label and target with section equation numbering.')

fragment=re.sub(r'\n{3,}','\n\n',fragment).strip()+'\n'
for pattern in (r'\\label\{([^{}]+)\}',r'\\hypertarget\{([^{}]+)\}'):
    ids=re.findall(pattern,early+'\n'+fragment)
    assert len(ids)==len(set(ids)),[x for x in ids if ids.count(x)>1]
    for identity in re.findall(pattern,'\n'.join(originals.values())):
        assert identity in ids,identity
p.write(fragment)
