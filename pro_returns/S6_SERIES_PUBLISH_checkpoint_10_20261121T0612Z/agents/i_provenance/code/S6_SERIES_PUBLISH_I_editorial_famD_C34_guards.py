import pathlib,json,re,hashlib,datetime
R=pathlib.Path('/workspace/scratch/653608133b22/work/agents/i_provenance')
meta=json.loads((R/'S6_SERIES_PUBLISH_I_editorial_intake.json').read_text())
S=pathlib.Path(meta['snapshot']).read_text(); C=(R/'S6_SERIES_PUBLISH_I_editorial_famD_C34_old.tex').read_text(); changes=[]
def add(id,old,new,scope,reason,defects='D01,D02,D04,D05,D08,D09,D13'):
    assert S.count(old)==1,(id,S.count(old)); assert old in C,id
    changes.append(dict(id=id,old=old,new=new,expected_count=1,statement_id=scope,reason=reason,defect_types=defects))
titles=[('proposition','01QR','D.1.1','The distinguished elliptic projection'),('proposition','01QS','D.1.2','The torsion locus and its degrees'),('proposition','01QU','D.1.4','The Neron--Severi lattice'),('proposition','01QV','D.1.5','Generic and projective fibres'),('theorem','01QW','D.1.6','Elliptic quotients and algebraic dimension'),('proposition','01QX','D.1.7','An explicit locus of algebraic dimension one'),('proposition','01QY','D.2.1','Vertical compact subspaces'),('proposition','01QZ','D.2.2','Curves in the special fibres'),('theorem','01R0','D.2.3','All compact curves'),('proposition','01QM','C.3.1','Rank-three period quotients'),('proposition','01QN','C.3.2','The quotient at the parameter boundary'),('proposition','01QP','C.3.4','The natural boundary of the Albanese invariant'),('theorem','01QQ','C.4.1','Gluing classification of the cusp surface')]
for env,tag,key,title in titles:
    old='\\begin{'+env+'}\\hypertarget{tag-'+tag+'}{}\\label{fam:src:'+key+'}'
    new='\\begin{'+env+'}['+title+']\\hypertarget{tag-'+tag+'}{}\\label{fam:src:'+key+'}'
    add('I-DC-title-'+key,old,new,'fam:src:'+key,'Add a short mathematical title without changing the statement or its identifiers.','D13')
add('I-D11-addition-description','The two roots displayed above are simple\nand avoid \\(0,1\\). We computed the same equation independently by the\nchord-and-tangent addition algorithm, obtaining','The two roots displayed above are simple\nand avoid \\(0,1\\). Chord-and-tangent addition gives the rational function','fam:src:D.1.1','Keep the exact rational function needed at the special fibres, and remove check-history narration.','D08')
old='''The division-polynomial recurrence and the addition algorithm are in
separate supplied programs; all polynomial operations use exact rational
arithmetic. Thus the denominator has no unverified numerical root or
cancellation. The decimal values \\(1.36510950191\\) and
\\(545.543981407\\) are only convenient approximations to the exact roots.'''
new='''The division-polynomial recurrence and chord-and-tangent calculation use
exact rational arithmetic; their executable formulas are listed in
\\cref{tab:I:programs}.'''
add('I-D11-program-reference',old,new,'fam:src:D.1.1','Replace program/run narration by one operative program-table citation. The exact roots and complete x(6P) formula remain.','D08,D09')
add('I-D12-height-locator','For the degree statement we use the height computation actually read in\n\\cite[Lemma 2.1 and proof]{Engel2026}:','For the degree statement, \\cite[Lemma~2.1, pp.~3--4, with the height computation on p.~4]{Engel2026} gives','fam:src:D.1.2','Cite the exact primary location and remove source-reading narration.','D08')
add('I-D12-height-conclusion','occur on \\(B^\\circ\\). This derives the cited height input in precisely\nthe form needed here; the first five degrees and the correction matrices\nare checked exactly in \\texttt{cd\\_torsion\\_independent.py}.','occur on \\(B^\\circ\\), so their total degree is \\(3k^2-1\\).','fam:src:D.1.2','Preserve the height application and all special-fibre exclusions; archive the independent degree/correction-matrix diagnostic in the program record.','D08,D09')
add('I-D12-appendix-pointer','This specializes the elliptic-surface height and specialization results cited in the re-derivation. A complete re-derivation is given in Appendix~\\ref{app:rederive:fam-src-D.1.2}.\n','', 'fam:src:D.1.2','Remove an obsolete appendix pointer: the complete application already appears in the immediately preceding proof, with its old label preserved.','D05,D12')
add('I-D13-positive-title','\\begin{theorem}[counterexample]\\hypertarget{tag-01QT}{}','\\begin{theorem}[A second elliptic quotient]\\hypertarget{tag-01QT}{}','fam:src:D.1.3','Title the constructed quotient.','D01,D02,D13')
old='''The proposed assertion that \\emph{existence of a surjection onto the
specified \\(E_t\\) with elliptic kernel} is equivalent to \\(6P(t)=O\\)
is false. It remains true for the specified projection in \\ref{fam:src:D.1.1}.'''
new='''At \\(t=32/5\\) there is an admissible parameter for which
\\(L(\\zeta_1,\\zeta_2)=3\\zeta_1+4\\zeta_2\\) induces a surjective
holomorphic group homomorphism \\(F_t\\to E_t\\) with connected elliptic
kernel, while \\(P(t)\\) has exact order four. The distinguished
projection of \\ref{fam:src:D.1.1} descends exactly at the order-dividing-six
locus specified there.'''
add('I-D13-positive-statement',old,new,'fam:src:D.1.3','State the precise quotient map and torsion order supplied by the unchanged construction.','D01,D02')
add('I-D13-remove-numeric-check','This inequality proves admissibility without using the numerical estimate\n\\(c=-2.25-34.02109724218209472308\\,i\\).','Thus the displayed parameter is admissible.','fam:src:D.1.3','Keep the analytic bound and remove an unnecessary numerical/check comparison.','D02,D08')
old='''The program \\path{cd_torsion_independent.py} checks the displayed
division polynomials and four lattice images by exact arithmetic; its
command and retained output are in \\CompendiumRef{I}{app:I:programs}.
The admissibility inequality is proved analytically above.'''
new='''The exact division-polynomial calculation is recorded in
\\cref{tab:I:programs}.'''
add('I-D13-program-reference',old,new,'fam:src:D.1.3','Keep the four explicit lattice images and their gcd proof; cite the operative polynomial calculation once.','D08,D09')
# Move the exact existing sign convention before its first use; no new mathematical assertion.
anchor='\\begin{proposition}\\hypertarget{tag-01QU}{}\\label{fam:src:D.1.4}'
setup=r'''\begin{definition}[The Hermitian form of an integral class]\hypertarget{tag-IP03}{}\label{I:def:Hermitian-form}
At a smooth fibre the real vector-space isomorphism
$\Pi:\mathbb R^4\to\mathbb C^2$ transfers an alternating form $E$ to
$\widetilde E(v,w)=E(\Pi^{-1}v,\Pi^{-1}w)$. For a $J$-invariant
$\widetilde E$, put
\[
 H_E(v,w)=\widetilde E(v,Jw)-i\widetilde E(v,w).
\]
Here $H_E$ is complex-linear in the first argument. Direct substitution
gives $H_E(Jv,w)=iH_E(v,w)$ and
$H_E(w,v)=\overline{H_E(v,w)}$. Its real Chern form is
$-\operatorname{Im}H_E=\widetilde E$, since
$(i/2)(H_E(v,w)-H_E(w,v))=\widetilde E(v,w)$.
\end{definition}

'''
# Insert at the same unique opener as the D1.4 title guard, avoiding overlap.
definition_guard=next(c for c in changes if c['id']=='I-DC-title-D.1.4')
definition_guard['new']=setup+definition_guard['new']
definition_guard['reason']+=' Move the existing explicit Pi/H_E/Chern-form comparison before its first use; preserve every sign and verification.'
definition_guard['defect_types']='D04,D05,D13'
old='''particular the expression ``\\(\\eta^2=12\\)'' in AC26, Lemma 9.4 is correct
as its displayed coefficient of \\(\\gamma\\wedge u\\wedge w\\wedge\\delta\\),
and has the opposite sign as a complex-oriented numerical
self-intersection. We retain the coefficient identity and record the
orientation comparison explicitly.'''
new='''particular \\cite[Lemma~9.4, pp.~66--67]{AC2026} gives the coefficient
identity \\(\\eta\\wedge\\eta=12\\gamma\\wedge u\\wedge w\\wedge\\delta\\).
The real period isomorphism above takes this integral orientation to the
negative of the complex orientation, yielding
\\(\\int_{F_t}\\eta^2=-12\\).'''
add('I-D14-orientation-citation',old,new,'fam:src:D.1.4','Give the verified primary coefficient identity and retain the explicit orientation comparison instead of process language.','D02,D08')
add('I-D14-Hermitian-reference','For the precise Hermitian convention $H_E$ defined in \\ref{fam:src:D.1.6}, direct','For the Hermitian form $H_E$ of Definition~\\ref{I:def:Hermitian-form}, direct','fam:src:D.1.4','Remove the forward construction dependence by referring to the relocated exact definition.','D05')
a=C.index('\\item We verify the required independence'); b=C.index('\n\\item For the second assertion',a)
old=C[a:b]
new=r'''\item By \cite[Lemma~9.3, p.~66]{AC2026}, the functions
$1,\tau,\mu,\beta^{\rm part},6\mu^2-\tau\beta^{\rm part}$ are linearly
independent. For $\beta=\beta^{\rm part}+c$, the relation
$A+B\tau+C\mu+D\beta+E(6\mu^2-\tau\beta)=0$ has coefficient vector
\[
 (A+Dc,\ B-Ec,\ C,\ D,\ E)
\]
in that ordered list. This coefficient change is invertible, with inverse
$(A',B',C',D',E')\mapsto(A'-D'c,B'+E'c,C',D',E')$.
Thus every integral class outside $\mathbb Z\eta$ has a
nonidentically-zero holomorphic left side in \eqref{fam:eq:cd-NS}; its
zeros are discrete. Taking the countable union over $\mathbb Z^6$ proves
the assertion for each fixed $c$, as in the application
\cite[Proposition~9.5, p.~67]{AC2026}.
'''
add('I-D15-known-independence',old,new,'fam:src:D.1.5','Replace the repeated AC9.3 proof by the opened primary result and exact invertible coefficient map for beta_part+c; retain the discrete-zero/countability application. The old proof is retained in the comparison record.','D12')
old='''Together with \\eqref{fam:eq:cd-NS}, these are an exact classification for every
$t$, by countable unions of explicitly given analytic zero sets; they do
not assert that the loci have a finite algebraic description. They include
all quotient maps, without requiring preservation of the first coordinate.'''
new='''Together with \\eqref{fam:eq:cd-NS}, these classify every smooth fibre
by countable unions of explicit analytic zero sets. The saturated null
lattices in the proof determine all connected elliptic kernels and their
quotient maps.'''
add('I-D16-positive-statement',old,new,'fam:src:D.1.6','State the exact classification and quotient construction positively.','D02')
a=C.index('We apply the Appell--Humbert correspondence');b=C.index('The complex-oriented square computed in',a)
old=C[a:b]
new=r'''We apply the Appell--Humbert correspondence and Riemann projectivity
criterion \cite[Theorem~4.1, p.~1, and Theorem~4.4, p.~3]{Schnell19}.
Equation \eqref{fam:eq:cd-NS} gives $J$-invariance, so
Definition~\ref{I:def:Hermitian-form} identifies the integral class $E$
with the real Chern form $-\operatorname{Im}H_E=\widetilde E$.
The Appell--Humbert integrality condition is therefore exactly the
integrality of $E$. '''
add('I-D16-Hermitian-use',old,new,'fam:src:D.1.6','Use the relocated exact definition and preserve the integral-sign comparison and both directions of the polarization criterion.','D05,D12')
add('I-D16-end-prose','without any marking ambiguity. Each individual matrix and every locus\nis specified; no expected identification is left in these formulas.','as the stated subsets of $B^\\circ$.','fam:src:D.1.6','Give the base of the descended loci without editorial reassurance.','D02,D08')
add('I-D16-appendix-pointer','This is the Appell--Humbert and Riemann criterion in the present lattice. A complete re-derivation is given in Appendix~\\ref{app:rederive:fam-src-D.1.6}.\n','', 'fam:src:D.1.6','Remove the obsolete appendix pointer to the proof already printed here; retain its label.','D05,D12')
add('I-D17-end-prose','of that neighbourhood. This supplies actual members and fibres, with\nall their parameter functions specified.','of that neighbourhood.','fam:src:D.1.7','Keep the explicit locus and torsion exclusion, removing process emphasis.','D08')
add('I-D21-normalization-prose','equality. This uses the full map into \\(X_c\\), not a transfer of a\nvanishing claim from its normalization.','equality.','fam:src:D.2.1','The full normalization/composition and Cartier-divisor arguments already specify the maps; remove defensive comparison.','D02')
add('I-D23-quotient-prose','that every holomorphic line bundle and every section on this actual\nquotient has this form.','that every holomorphic line bundle and every section on this quotient\nhas this form.','fam:src:D.2.3','Remove process emphasis.','D08')
add('I-D23-Hermitian-reference','from \\ref{fam:src:D.1.6};\nwe choose the sign of $E$ making $H_E$ positive.','from Definition~\\ref{I:def:Hermitian-form};\nwe choose the sign of $E$ making $H_E$ positive.','fam:src:D.2.3','Use the exact relocated sign convention.','D05')
add('I-D23-effective-source','A divisor class with positive Hermitian rank two gives exactly\nthese positive theta sections.','The effective line-bundle criterion \\cite[pp.~2--3]{Schnell19} shows that\na divisor class with positive Hermitian rank two gives exactly\nthese positive theta sections.','fam:src:D.2.3','Supply the opened primary effective-section/nullspace-quotient criterion at the operative application.','D05')
add('I-D23-finite-map-conclusion','closed embeddings, so they preserve compactness and give one-dimensional\nimages; no assertion is transferred from a normalization in an invalid\ndirection.','closed embeddings, so they preserve compactness and give one-dimensional\nimages.','fam:src:D.2.3','Retain the exact finite/closed morphism argument and remove defensive commentary.','D02')
add('I-D23-appendix-pointer','This is the effective line-bundle criterion for compact complex tori in the present lattice. A complete re-derivation is given in Appendix~\\ref{app:rederive:fam-src-D.2.3}.\n','','fam:src:D.2.3','Remove the obsolete appendix pointer to the complete printed proof; retain its label.','D05,D12')
add('I-C32-boundary-prose','The unique degenerate base point at the actual admissibility boundary is','The unique degenerate base point at the admissibility boundary is','fam:src:C.3.2','Remove process emphasis.','D08')
add('I-C32-end-prose','We have described the torus cover of the order-four filling, including\nthe actual quotient and its topology.\n','','fam:src:C.3.2','The exact coordinate change and degree-four morphism already give the result.','D08')
a=C.index('\\paragraph{Local boundary obstruction}');b=C.index('\\begin{proposition}\\hypertarget{tag-01QP}',a)
old=C[a:b]
header=old[old.index('\\hypertarget'):old.index('\n\nThe local')]
new='\\begin{remark}[The local boundary obstruction]'+header+r'''

The only degenerate base fibre at the parameter boundary lies over $t=1$.
By \ref{fam:src:C.3.2}, its rank-three period quotient is noncompact for
rational $x+3/2$ and non-Hausdorff for irrational $x+3/2$; neither quotient
can be a fibre of a proper family of complex spaces.
Proposition~\ref{fam:src:C.3.4} proves that the elliptic Albanese model
also has no holomorphic Weierstrass continuation across this boundary.
The obstruction to a general proper holomorphic extension is proved in
\cref{push:src:D.1.2,push:src:D.1.3} by recovering the intrinsic divisor.
\end{remark}

'''
add('I-C33-numbered-obstruction',old,new,'fam:src:C.3.3','Number the existing local-obstruction discussion, preserve both labels and the tag, and state each proved scope and its exact source positively.','D01,D02,D13')
add('I-C34-end-scope','obstruction concerns the stated Albanese construction; it does not\nsilently assume that every possible compact threefold filling preserves\nan Albanese model of its special surface.','obstruction applies to continuation of the displayed elliptic Albanese\nfamily.','fam:src:C.3.4','State the exact scope of the rational-invariant argument positively.','D02')
old='''The complete enumeration in
\\path{code/current_audits/audit_paper_i/code/cusp_hexagon_exact.py}
examines all $36$ possible ray images of an integral basis and finds exactly
$12$ fan automorphisms. If $Av_j=\\alpha v_k$ and $r_kA=\\beta r_j$, the
transported equation is $(g'_k)^{\\alpha\\beta}=g_j$; this gives exactly the
six displayed actions. The original side and character signs, all matrices,
and the resulting constant sign or power obstruction for each nonidentity
action are recorded in \\path{cusp_hexagon_exact.output.json}.'''
new='''Enumerate the $36$ ordered pairs of ray images of an integral basis,
retain those with determinant $\\pm1$, and require preservation of the six
rays. This gives the $12$ fan automorphisms. For
$Av_j=\\alpha v_k$ and $r_kA=\\beta r_j$, the transported equation is
$(g'_k)^{\\alpha\\beta}=g_j$, yielding the six displayed actions.
The exact enumeration and sign transport are listed in
\\cref{tab:I:programs}.'''
add('I-C41-program-reference',old,new,'fam:src:C.4.1','Keep the complete finite enumeration rule and character-sign transport, with one operative program-table citation.','D08,D09')
N=C
for c in changes:
    assert N.count(c['old'])==1,(c['id'],N.count(c['old'])); N=N.replace(c['old'],c['new'])
(R/'S6_SERIES_PUBLISH_I_editorial_famD_C34_new.tex').write_text(N)
out=dict(source=meta['source'],source_sha256=meta['source_sha256'],created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),changes=changes,new_tags=['IP03'],verification='Original complete D/C3/C4 statements and proofs read; proposed exact substitutions require final rereading recorded separately. No independent-check credit.')
(R/'S6_SERIES_PUBLISH_I_editorial_famD_C34_guards.json').write_text(json.dumps(out,indent=2)+'\n')
oldlabels=re.findall(r'\\label\{([^}]+)\}',C);newlabels=re.findall(r'\\label\{([^}]+)\}',N)
assert sorted(oldlabels)==sorted(x for x in newlabels if x!='I:def:Hermitian-form')
current=pathlib.Path(meta['source']).read_text()
print(json.dumps({'guards':len(changes),'old_labels_preserved':True,'current_unique':all(current.count(c['old'])==1 for c in changes),'not_unique':[c['id'] for c in changes if current.count(c['old'])!=1],'new_sha256':hashlib.sha256(N.encode()).hexdigest()},indent=2))
