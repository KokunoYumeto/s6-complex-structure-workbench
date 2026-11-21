from pathlib import Path
import json, hashlib, datetime
from S6_SERIES_PUBLISH_editing import Editor, block
r=Path(__file__).resolve().parents[1];ed=Editor('I');before=ed.text
labels=['night:P5.6','inv:C3.2','inv:A2.1']
old_blocks={lab:block(ed.text,lab) for lab in labels}
start=ed.text.index(r'\subsection{The intrinsic parameter space}')
end=ed.text.index(r'\end{proof}',start)+len(r'\end{proof}')
old_parameter=ed.text[start:end]
prefix=old_parameter[old_parameter.index('The analytically computed'):old_parameter.index('\nNow ')]
new=old_blocks['night:P5.6']
new=new.replace(r'\begin{theorem}',r'\begin{theorem}[Integral torsor classes and the parameter period]',1)
new=new.replace(r'''\item The intrinsic pencil argument and the centralizer computation give
$P=aI+bE_{41}$ with $a=\pm1$ and $b=a(c-c')$.  The same root-fibre
character excludes $a=-1$.  Thus $b=c-c'$ is an integer.''',
 r'''\item '''+prefix+r'''
The centralizer computation of \cref{wb:pshift:lem:centralizer}
then gives $P=aI+bE_{41}$ with $a=\pm1$ and $b=a(c-c')$.
The root-fibre character calculation in that proposition excludes
$a=-1$. Thus $b=c-c'$ is an integer.''')
new=new.replace(r'''The program
\path{code/current_audits/audit_paper_i/code/priority_rows_exact.py}
forms the resulting $28\times14$, $20\times28$ and $8\times20$
integer differentials and verifies both zero products.''',
 r'''The resulting integer differentials have sizes
$28\times14$, $20\times28$ and $8\times20$, and their consecutive
products vanish by the restriction identities.''')
new=new.replace(r'''The matrices and quotient invariants are in
\path{priority_rows_exact.output.json}.''','')
assert new!=old_blocks['night:P5.6'] and 'priority_rows_exact' not in new
ed.replace(old_blocks['night:P5.6'],new,'D03',
 'Keep the complete integral torsor classification in one proof; include the exact intrinsic-pencil map previously repeated in A5.1. Move program reporting to the end table.', 'night:P5.6')
new_parameter=old_parameter
a=new_parameter.index('The analytically computed');b=new_parameter.index('As a complex parameter space',a)
new_parameter=new_parameter[:a]+r'''For the standard twist data, Theorem~\ref{night:P5.6}
gives $X_c\simeq X_{c'}$ exactly when $c-c'\in2\mathbb Z$.
The explicit maps on the regular, finite, and cusp charts are
those in \cref{wb:pshift:lem:centralizer}.

'''+new_parameter[b:]
ed.replace(old_parameter,'','D23',
 'Place the quotient-parameter proof after its unique integral torsor classification; its exact exponential quotient and deformation conclusion remain.', 'app:rederive:fam-src-A.5.1')
ed.replace(new,new+'\n\n'+new_parameter,'D03',
 'Use the integral torsor theorem for the common classification, retaining the unique exponential quotient and its local inverse maps in A5.1.', 'app:rederive:fam-src-A.5.1')

old=old_blocks['inv:C3.2'];new=old
new=new.replace('[AC26, Section 7.5]',r'\cite[\S7.5, pp.~54--57, especially (7.10), p.~55]{AC2026}')
new=new.replace(r'\item We include the comparison that fixes the sign.  A degree-one integral',r'\item A degree-one integral')
new=new.replace('[AC26, Theorem~B.1 and Proposition 7.12]',r'\cite[Theorem~B.1, pp.~101--105; Proposition~7.12, pp.~51--53]{AC2026}')
new=new.replace(r'''This recovers the degree-one
part of [AC26, Proposition 7.26], without identifying the reduced and
non-reduced fibre: this is topological cohomology, unchanged by
nilpotents, whereas the coherent comparison uses the full fibre.''',
 r'''This is the degree-one calculation of
\cite[Proposition~7.26, pp.~61--62]{AC2026}.
The closed embedding $F_{\mathrm{red}}\hookrightarrow F$ is a
homeomorphism on underlying spaces and therefore induces the
isomorphism on integral topological cohomology used here.
The coherent restriction map has target $H^1(F,\mathcal O_F)$.''')
new=new.replace(r'''These are the explicitly oriented boundary evaluations in [AC26,
Proposition 7.27, pp. 62--63], not an unspecified sign of a spectral
sequence differential.''',r'''These boundary evaluations use the orientations in
\cite[Proposition~7.27, pp.~62--63]{AC2026}.''')
old_program=r'''  The integer intersection $3\mathbb Z\cap4\mathbb Z\cap\mathbb Z=12\mathbb Z$, the symbolic sum in
\eqref{inv:eq:C-collar-sum}, and the collar endpoint functional are recomputed in
\path{code/current_audits/audit_paper_i/code/adjacent_exact.py}. Its output \path{adjacent_exact.output.json} also records an exact polynomial cutoff example; the displayed endpoint calculation proves the formula for every permitted cutoff.'''
assert old_program in new;new=new.replace(old_program,'')
ed.replace(old,new,'D04',
 'Give the actual opened AC statement/page locators and the reduction embedding inducing topological cohomology; keep every collar sign, integral and coherent comparison. Relocate the diagnostic program report.', 'inv:C3.2')

old=old_blocks['inv:A2.1'];new=old
a=new.index('  Rational differentiation and cancellation verify these three');b=new.index('The kernel of',a)
new=new[:a]+'\n'+new[b:]
new=new.replace('''This kernel
argument is needed: mere equivariance of the separate period functions
would not prove descent.''','')
new=new.replace(''' and the exact two local orders, without the
workbench's degree count for the coarse determinant line.''',' and the exact two local orders.')
new=new.replace(r'\item For completeness we translate to the actual coarse lattices.  Choose',r'\item For the coarse lattices, choose')
ed.replace(old,new,'D01',
 'Keep the complete modular descent and local coarse-lattice determinant proof; remove history, defensive wording and program/output reporting.', 'inv:A2.1')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_classification_collar_comparison.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Root read the full original P5.6 proof and exact A5.1 deferred proof, C3.2 and A2.1 before rewriting; compared all replacements. The classification proof is consolidated, the exponential quotient is retained, and collar signs/constants are unchanged. This is an exposed editorial reread.',
 'old_proofs':old_blocks,'new_proofs':{lab:block(ed.text,lab) for lab in labels},
 'old_parameter_proof':old_parameter,'new_parameter_proof':new_parameter,
 'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest()},indent=2)+'\n')
