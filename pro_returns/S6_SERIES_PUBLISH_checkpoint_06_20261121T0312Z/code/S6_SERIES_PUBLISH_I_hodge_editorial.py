from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor,block
r=Path(__file__).resolve().parents[1]
ed=Editor('I'); reviewed={}
def within(label,old,new,reason,kind='D08'):
 global ed
 whole=block(ed.text,label)
 assert whole.count(old)==1,(label,old[:80])
 reviewed.setdefault(label,{'old':whole})
 ed.replace(whole,whole.replace(old,new),kind,reason,label)

within('inv:A2.4',r'''Under the same direct-image and
sheaf-surjectivity hypotheses a rank-zero global map would instead
give $h^{1,2}=2$, $h^{1,1}=3$; that alternative does not occur here.''',r'''The same direct-image exact sequence expresses the two Hodge numbers
in terms of the global rank $r$ as
$h^{1,2}=2-r$ and $h^{1,1}=3-r$; here $r=1$.''',
 'Express the retained rank-zero and rank-one linear-algebra calculations by their exact rank formula, preserving both values.')
within('inv:A2.4',r'''If its rank were zero, the long exact cohomology sequence of
$0\to\mathcal K\to\OO^2\oplus\OO(-1)^2\to\OO\to0$
would give $h^0(\mathcal K)=2$, $h^1(\mathcal K)=1$.
The residue calculation in \ref{inv:A1.3} and Leray would then give exactly
the two counterfactual Hodge numbers stated in the claim.''',r'''For the global rank $r$, the long exact cohomology sequence of
$0\to\mathcal K\to\OO^2\oplus\OO(-1)^2\to\OO\to0$
gives $h^0(\mathcal K)=2-r$ and $h^1(\mathcal K)=1-r$.
The residue calculation in \cref{inv:A1.3} and Leray give
$h^{1,2}=2-r$ and $h^{1,1}=3-r$, as stated.''',
 'Retain the complete exact-sequence calculation as a polynomial in the global rank.')
ed.replace('''The value of that integer is determined here by the nonzero direct-image
scalar. The full calculations of both the pattern and its value are retained.''','''The nonzero direct-image scalar in \\cref{inv:A2.4} determines that integer.''','D08','Replace production narration by the exact mathematical input.','inv:A3.1')
ed.replace('''each admissible $c$, including every point arbitrarily close to the
strict boundary; no manifold at the excluded boundary is asserted.''','''each $c$ in the stated open parameter domain.''','D02','State the unchanged open-domain scope positively.','inv:A3.1')
within('inv:A3.2',r'''Its ambiguity is exactly
$\C\alpha$; the statement does not claim a canonical global form.''',r'''Its preimages form the affine space $Q+\C\alpha$.''',
 'Specify the exact affine space of Leray lifts.')
within('inv:A3.2',r'''This defines $\upsilon$ with no choice of a negative
degree summand.''',r'''This specifies $\upsilon$ through the displayed injection.''',
 'Name the actual defining map.')
within('inv:A3.2',r'''The associated-graded descriptions are
canonical with the named choices; the splitting of Leray vector
spaces is not asserted canonical.''',r'''The named trace pairings determine the associated-graded bases;
the choices of preimages determine the corresponding Leray splittings.''',
 'Describe the precise dependence of the bases on their chosen lifts.')
within('inv:A4.1',r'''$(a,b)\mapsto xa-yb$ after an immaterial change of sign of one
basis vector.  More explicitly one may use
$(a,b)\mapsto xa-yb$ with relation $(y,x)$; its kernel is precisely
that relation, since $x,y$ are relatively prime.''',r'''$(a,b)\mapsto xa-yb$. Its kernel is exactly $R(y,x)$:
the equality $xa=yb$ gives $a=yh$ and $b=xh$ by relative primality.''',
 'Use the displayed exact module morphism, with no unnecessary normalization claim.')
within('inv:A4.1',r'''The polynomial maps and all six annihilator identities are also
verified over $\Z[x,y,z]$ in
\path{code/current_audits/audit_paper_i/code/priority_rows_exact.py};
its output retains both presentation matrices.  ''','',
 'Move the corroborating program report to the check records; the complete module calculation remains.', 'D09')
within('inv:A4.1','All local modules needed to distinguish degrees one and two','Relative differentials in the three local models','Use a mathematical title.')
within('inv:A4.2','Refuted: The claimed degree-one torsion along the cusp','The support of relative torsion','Remove a status word from the proved correction.','D11')
within('inv:A4.2',r'''The assertion in AC26 Remark 9.21, PDF page 81, that
$\Omega_{X/B}^1$ has torsion along $W\cup S_1\cup S_2$ is false.
Its torsion is supported precisely on $S_1\cup S_2$; its degree-one
cusp modules are torsion-free but not locally free on the double
locus.  The plural statement in Remark 1.3, PDF page 5, must be
qualified by degree: $\Omega^2_{X/B}$ does have torsion on the cusp
double locus.  The workbench's degree-one correction is correct;
it must not be extended to degree two.''',r'''The torsion of $\Omega_{X/B}^1$ is supported precisely on
$S_1\cup S_2$. Its cusp modules inject into the free logarithmic
relative modules, and their minimal number of generators exceeds
their rank at the double locus. In degree two, the torsion also
has support on the cusp double locus.
This corrects \cite[Remark~9.21, p.~81]{AC2026}, where
degree-one torsion is asserted on $W\cup S_1\cup S_2$;
the support statement in \cite[Remark~1.3, p.~5]{AC2026}
therefore depends on the degree.''',
 'State the proved supports and exact module evidence, retaining the neutral correction of published work.', 'D01')

start=ed.text.index('In this section $X$ is the standard marked $(3,4)$ threefold')
end=ed.text.index('\\begin{proposition}',start)
old=ed.text[start:end]
eq=old[old.index('\\begin{equation}'):old.index('\\end{equation}')+len('\\end{equation}')]
new=r'''\begin{definition}[Cohomological conventions]
\hypertarget{tag-PI13}{}\label{I:def:hodge-conventions}
For the standard marked threefold, put $h=h^{1,2}(X)$.
Proposition~\ref{inv:A3.1} gives $h=1$. We write the dimensions
below as functions of $h$ in the common Hodge pattern
'''+eq+r'''
The numerical tables of this family are obtained by the evaluation
map $\mathbb Z[h]\to\mathbb Z$, $h\mapsto1$.
We use $d=\partial+\bar\partial$ on complex-valued smooth forms
and the complex orientation for integration.
\end{definition}

'''
ed.replace(old,new,'D15','Number the cohomological conventions, resolve the Hodge-table reference and specify the exact evaluation map.','I:def:hodge-conventions')
within('inv:C1.2',r'''Statements \ref{inv:A1.3} and \ref{inv:A3.2} prove these hypotheses for $X$,
so this geometric choice applies to the threefold in the stated problem.''',r'''Propositions~\ref{inv:A1.3} and \ref{inv:A3.2} supply these data
for every member of the marked family.''','Replace a problem reference by the exact family scope.','D05')
within('inv:C1.2',r'''The extension used in this last choice is the actual Leray lift in
Statement \ref{inv:A3.2}.  This argument uses that extension; it does not infer
it from a calculation on the smooth fibre alone.''',r'''The lift in Proposition~\ref{inv:A3.2} maps to $\eta$ under the
Leray restriction, and hence supplies the class $q$ used here.''',
 'State the supplying Leray morphism positively.')
old=r'''With
\[
H^{p,q}_{BC}=
\frac{\ker\partial\cap\ker\bar\partial\subset A^{p,q}}
{\im\partial\bar\partial},\qquad
H^{p,q}_{A}=
\frac{\ker\partial\bar\partial\subset A^{p,q}}
{\im\partial+\im\bar\partial},
\]
the complete tables are'''
definition=r'''\begin{definition}[Bott--Chern and Aeppli cohomology]
\hypertarget{tag-PI14}{}\label{I:def:BC-Aeppli}
On the double complex $A^{p,q}(X)$ of smooth forms, set
\[
H^{p,q}_{BC}(X)=
\frac{\ker\partial\cap\ker\bar\partial\subset A^{p,q}(X)}
{\operatorname{im}(\partial\bar\partial:A^{p-1,q-1}\to A^{p,q})},
\quad
H^{p,q}_{A}(X)=
\frac{\ker(\partial\bar\partial:A^{p,q}\to A^{p+1,q+1})}
{\partial A^{p-1,q}+\bar\partial A^{p,q-1}}.
\]
Complex conjugation sends bidegree $(p,q)$ to $(q,p)$.
\end{definition}

'''
anchor='\\begin{proposition}[Bott--Chern and Aeppli tables as functions of $h$]'
ed.replace(anchor,definition+anchor,'D15','Define both cohomology quotients in a numbered definition before their use.','I:def:BC-Aeppli')
within('inv:C2.1',old,'The complete dimension tables are','Move the definitions before the proposition.','D15')
within('inv:C2.1',r'''In particular, substitution of the value $h=1$ proved in \ref{inv:A3.1} gives
the workbench's numerical tables.''',r'''At the value $h=1$ of Proposition~\ref{inv:A3.1},''',
 'Remove a working-file reference from the numerical conclusion.','D01')
whole=block(ed.text,'inv:C2.1');a=whole.index('\\item The program');b=whole.index('\\end{enumerate}',a)
within('inv:C2.1',whole[a:b],'','Archive the finite corroborating calculation; the complete decomposition proof already establishes every table entry.','D09')
within('inv:C2.1','the two definitions in the statement','Definition~\\ref{I:def:BC-Aeppli}','Resolve the relocated definitions.')
within('inv:C2.2','agree.  No correction to these specific formulas is required.','agree through the displayed specialization formulas.','State the comparison positively.')
within('inv:C2.2',r'''This comparison concerns exactly the formulas
used here; it does not certify every assertion in either article.''','',
 'Remove a production disclaimer after the exact compared formulas.','D02')

generators=r'''\begin{definition}[The nine positive-degree Bott--Chern classes]
\hypertarget{tag-PI15}{}\label{I:def:BC-generators}
For $h=1$, choose $\bar\partial$-closed representatives $G,Q$
of $g,q$ as in Proposition~\ref{inv:C1.2}, and choose a smooth
top-degree form $\nu$ with $\int_X\nu=1$. Define
\[
\begin{array}{c|c|c}
\text{class}&\text{representative}&\text{bidegree}\\\hline
\mathsf A&\partial G&(1,1)\\
\mathsf B&\bar\partial\bar G&(1,1)\\
\mathsf C&\partial Q&(2,1)\\
\overline{\mathsf C}&\bar\partial\bar Q&(1,2)\\
\mathsf D&\partial(G\wedge Q)&(2,2)\\
\overline{\mathsf D}&\bar\partial(\bar G\wedge\bar Q)&(2,2)\\
\mathsf E&\partial(Q^2)&(3,2)\\
\overline{\mathsf E}&\bar\partial(\bar Q^2)&(2,3)\\
\mathsf T&\nu&(3,3).
\end{array}
\label{I:eq:BC-generators}
\]
\end{definition}

'''
anchor='\\begin{proposition}[The complete Bott--Chern algebra, for every $h$]'
ed.replace(anchor,generators+anchor,'D03','Restore the nine exact generator formulas from the attached compendium as a local numbered definition, before the algebra theorem.','I:def:BC-generators')
within('inv:C3.3',r'\CompendiumRef{I}{wb:eq:bcpr-generators}',r'\eqref{I:eq:BC-generators}','Resolve the external internal-label pointer to the explicit local table.','D03')
within('inv:C3.4',r'Non-K\"ahler degrees and the precise degreewise statement',r'Non-K\"ahler degrees and comparison maps','Use the mathematical objects in the title.')
within('inv:C3.4',r'''This distinguishes the two meanings of a
``$\partial\bar\partial$-lemma in a degree''; a vanishing Bott--Chern
group in degree one does not make $\Delta^1$ vanish.''',r'''In degree one the first comparison map is $0\to0$, while the
second is $0\to\mathbb C^2$; the formula gives $\Delta^1=2$.''',
 'Replace a categorical wording distinction by the exact two maps and their dimensions.')
within('inv:C3.5','Metric obstructions that do not require $h$','Obstructions from exact positive forms','Give the title the proved mechanism.')
whole=block(ed.text,'inv:C3.7');a=whole.index('The exact determinant and exterior square are verified in');b=whole.index('\\item The explicit invariant',a)
within('inv:C3.7',whole[a:b],'\n\n','Archive the corroborating rational example and program output; retain the exact determinant, signature and integral calculations.','D09')
within('inv:C3.7',r'''\Gamma=\frac{i}{2\Delta}
\left(d\bar\zeta_2-\frac myd\bar\zeta_1\right).
\]''',r'''\Gamma=\frac{i}{2\Delta}
\left(d\bar\zeta_2-\frac myd\bar\zeta_1\right).
\label{I:eq:fibre-gamma}
\]''','Give the invariant representative a local equation reference.','D03')
within('inv:C3.7',r'''Writing $Q_F$ for the invariant $(1,1)$ representative of $\eta$,
direct exterior multiplication gives''',r'''Its invariant $(1,1)$ representative is
\[
Q_F=\frac1{2iy\Delta}\bigl(
\operatorname{Im}\beta\,d\zeta_1\wedge d\bar\zeta_1
-6m\,d\zeta_1\wedge d\bar\zeta_2
-6m\,d\zeta_2\wedge d\bar\zeta_1
+6y\,d\zeta_2\wedge d\bar\zeta_2\bigr).
\label{I:eq:fibre-eta-form}
\]
Direct exterior multiplication gives''',
 'Print the exact invariant form already used by the Hermitian matrix and the attached compendium, resolving the later coefficient-gauge reference.','D03')
for label,data in reviewed.items():data['new']=block(ed.text,label)
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_hodge_editorial_comparison.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Root read each affected full old proof and compared the new exact replacements. All unchanged calculations and scopes are retained. New generator and fibre-form displays are the explicit formulas read in the attached compendium. This is exposed-text editorial comparison, not independent rederivation.',
 'proofs':reviewed},indent=2)+'\n')
