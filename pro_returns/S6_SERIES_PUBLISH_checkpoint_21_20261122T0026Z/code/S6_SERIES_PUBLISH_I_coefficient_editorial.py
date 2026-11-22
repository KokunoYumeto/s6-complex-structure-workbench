from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor,block
r=Path(__file__).resolve().parents[1];ed=Editor('I');before=ed.text
def rep(old,new,why,lab='inv:C3.8',kind='D08'):
 ed.replace(old,new,kind,why,lab)

# The full boundary-cover argument is the same unimodular toric map as in
# the attached compendium, now included in the single proper-family proof.
old=r'''The same chart-pair bound applies to sequences tending to that
fibre. Compact sets meet finitely many charts, so the action is
free and properly discontinuous on the entire toric family.'''
new=r'''These charts cover the entire toric space, including its boundary.
On the dense torus the duality identity is
\[
 \log|z_i|=\log|t_c|\,\theta_i^\sigma(y),
\]
where $\theta_i^\sigma$ are the barycentric coordinates of the
height-one triangle. A triangle containing $y$ therefore gives
$|z_i|\le1$. For a boundary point in the orbit of the cone over a
cell $P$, the coordinates belonging to vertices of $P$ vanish.
The remaining characters are dual to the image cones of triangles
containing $P$ in the quotient lattice by $\operatorname{span}(P,1)$.
Those cones cover the quotient real space: lift a vector, add a
sufficiently small positive multiple of it to a relative interior
point of $(P,1)$, and rescale to height one. Local finiteness places
that point in a triangle containing $P$. Applied to the negative
logarithm of the orbit coordinates, this gives the same closed
unit-polydisc bound. Thus the open radius-two charts cover the
boundary as well. Every compact set has a finite subcover.
The chart-pair estimate applies to an intersection meeting the
boundary because that intersection is open and meets the dense
torus. It therefore proves freeness and proper discontinuity on
the entire toric family.'''
rep(old,new,'Include the exact boundary orbit/quotient-cone cover used by the existing properness argument, resolving the later compendium chart dependency.','fam:src:A.3.1','D03')

start=ed.text.index('The Green representative of \\cref{inv:C3.1}')
end=ed.text.index('\\begin{proposition}[A specified global coefficient atlas]',start)
old=ed.text[start:end]
new=old.replace('\\paragraph{Relation to the source constructions.}\n','')
new=new.replace('The proof supplies the actual local theta and Cartier lines, their\nannular holomorphic connections, the resulting one-form cocycle,\nand a specified locally finite coordinate weight system with every\nderivative evaluated.  Thus the general cohomological conversion and\nthe scalar input are credited together with the original family data.\n','')
new=r'''\begin{remark}[Sources and coefficient conventions]
\hypertarget{tag-PI16}{}\label{I:rem:coefficient-sources}
'''+new.rstrip()+'\n\\end{remark}\n\n'
rep(old,new,'Number the precise source comparison and Cech--Dolbeault convention; remove the proof-production recap.','I:rem:coefficient-sources','D15')
rep('\\subsection{A literal coefficient atlas for the two generators}','\\subsection{A coefficient atlas for the two generators}','Use a mathematical heading.')

oldproof=block(ed.text,'inv:C3.8')
newproof=oldproof
repls=[
 (r'''Retain the standard marked family of \cref{wb:thm:retained-period-deformation},
its original vectors''',r'''Use the standard marked family of \cref{fam:src:A.3.1},
with vectors'''),
 (r'''Use the ordinary and finite covering charts in
\cref{fam:src:A.1.2,wb:thm:retained-period-deformation}, and the cusp
charts of \CompendiumRef{I}{wb:lem:toric-chart-control} and
\CompendiumRef{I}{wb:thm:candidate-cusp-geometry}.''',r'''Use the ordinary, finite and cusp covering charts of
\cref{fam:src:A.1.2,fam:src:A.3.1}, with their specified affine,
toric and exponential transition maps.'''),
 (r'''These are precisely the chart and properness bounds in the cited cusp
construction and in the proof of
\cref{wb:thm:retained-period-deformation}.''',r'''These are the chart and properness bounds in
Proposition~\ref{fam:src:A.3.1}.'''),
 (r'''These domains cover the cusp space before quotient, including its
boundary, by the cited chart-control lemma.''',r'''The toric orbit calculation in that proof shows that these domains
cover the cusp space before quotient, including its boundary.'''),
 (r'''These are refinements and inverse maps inside the
given $X$, not a replacement compactification.''',r'''These maps specify the refinement and its local inverse branches
inside the given $X$.'''),
 (r'''Thus
$\det T'$ is nonzero at every point of every annular cover used
here.  No inverse is taken at a special fibre.''',r'''Thus $\det T'$ is nonzero throughout the three annular domains
of the inverse.'''),
 (r'''with no missing base term.''',r'''with the displayed base term.'''),
 (r'''This is the tensor-dual map, including its sign; no line factors are
discarded.''',r'''This is the tensor-dual connection, with all transition factors
inverted and the displayed sign.'''),
 (r'''We have glued a cocycle of holomorphic one-forms.  We have not
specified cross-piece functions with those logarithmic derivatives:
the connections are not assumed closed.  In particular no global
line with nonzero fibre Chern class is being glued.''',r'''The result is the holomorphic one-form cocycle $c_{ab}$.
Its construction uses the connection transformation law; the
connections may have the $(2,0)$ curvature $dA$ displayed above.'''),
 (r'''Thus no unspecified smooth correction is hidden in the coefficients.''',r'''Together with the inverse-chart Jacobians, this evaluates every
weight derivative in the coefficient formulas.'''),
 (r'''This is \CompendiumRef{I}{wb:eq:bcpr-gamma-form}; injectivity in
\cref{inv:C3.1} gives $[G]=g_\gamma$.''',r'''This is \eqref{I:eq:fibre-gamma}; injectivity in
\cref{inv:C3.1} gives $[G]=g_\gamma$.'''),
 (r'''\item \emph{Why the correction is complex.}''',r'''\item \emph{The fibre square of a closed real form.}'''),
 (r'''This proves the assertion and shows why the complex connection
correction above cannot be replaced by gluing real curvatures.''',r'''This contradicts the exact fibre square and proves the last assertion.''')]
for old,new in repls:
 assert newproof.count(old)==1,old[:100]
 newproof=newproof.replace(old,new)
newproof=newproof.replace(r'\cref{wb:thm:retained-period-deformation}',r'\cref{fam:src:A.3.1}')
rep(oldproof,newproof,'Resolve every visible internal compendium pointer through the exact retained chart/fibre morphisms; preserve all thirteen coefficient construction steps and numerical identities.','inv:C3.8','D03')

a=ed.text.index('\\paragraph{Exact algebra checks.}')
b=ed.text.index('\\Uses{',a)
rep(ed.text[a:b],'','Move the diagnostic programs, outputs and check counts to the research records; all universal coefficient identities remain in the proof.','inv:C3.8','D09')

a=ed.text.index('\\subsection{Comparison with the Green and harmonic representatives}')
b=ed.text.index('\\subsection{Changes of the specified coefficient gauge}',a)
old=ed.text[a:b]
head,rest=old.split('\\hypertarget{tag-03LI}',1)
content='\\hypertarget{tag-03LI}'+rest
statement,tail=content.split('\\begin{proof}',1)
proof,post=tail.split('\\end{proof}',1)
post=post[:post.index('\\Uses{')].strip()
new=head+r'''\begin{proposition}[Green and harmonic representatives]
'''+statement.rstrip()+'\n\n'+post+'\n\\end{proposition}\n\\begin{proof}'+proof+'\\end{proof}\n\n'
rep(old,new,'Number the complete operator comparison and place its exact cohomology relation in the statement; retain the full unitary-change calculation.','inv:C3.8:operator-comparison','D15')

a=ed.text.index('\\paragraph{The representative and its fibre restriction.}')
b=ed.text.index('\\paragraph{The exact changes between coefficient gauges.}',a)
old=ed.text[a:b]
content=old[old.index('\\hypertarget'):old.index('\\Uses{')]
content=content.replace(r'\CompendiumRef{I}{wb:eq:bcpr-q-fibre-expanded}',r'\eqref{I:eq:fibre-eta-form}')
content=content.replace('choose actual global smooth','choose global smooth')
new='\\begin{remark}[Fibre restriction of the coefficient representative]\n'+content.rstrip()+'\n\\end{remark}\n\n'
rep(old,new,'Number the fibre-restriction comparison and resolve the invariant representative locally.','wb:rem:bcpr-literal-gauge','D15')
a=ed.text.index('\\paragraph{The exact changes between coefficient gauges.}')
b=ed.text.index('\\clearpage\n\\section{Arithmetic periods and compact subgroups}',a)
old=ed.text[a:b]
content=old[old.index('\\hypertarget'):old.index('\\Uses{')].rstrip()
new='\\begin{remark}[Changes of coefficient gauge]\n'+content+'\n\\end{remark}\n\n'
rep(old,new,'Number the exact gauge coboundaries; retain both weight-change and cocycle-change maps in full.','wb:rem:bcpr-global-gauge-boundary','D15')

# Primary source metadata and explicit versioned receiving locators.
p=r/'agents/i_provenance/S6_SERIES_PUBLISH_I_primary_citation_guards_04.json'
for x in json.loads(p.read_text())['changes']:rep(x['old'],x['new'],x['reason'],x['id'],'D20')
ed.text=ed.text.replace('Theorem 6.3, Proposition 6.4, (7), pp. 20--25','arXiv v4, Theorem~6.3, pp.~20--23; Proposition~6.4 and (7), p.~23; \\S7.1, pp.~24--25')
ed.text=ed.text.replace('Section 4, pp. 13--16]{Angella2018}','arXiv v2, \\S4, pp.~13--15; Figure~5, p.~16]{Angella2018}')
ed.record('D20','Unversioned McHugh/Angella locators','Explicit arXiv v4/v2 statement and page locators','The primary-page receipt verifies exactly these receiving formulas.','inv:C2.2')
ed.save()
bp=r/'agents/i_provenance/S6_SERIES_PUBLISH_I_shared_bib_guards_04.json'
bib=r/'S6_SERIES_PUBLISH_references.bib';s=bib.read_text()
for x in json.loads(bp.read_text())['changes']:
 assert s.count(x['old'])==x.get('expected_count',1),x['id'];s=s.replace(x['old'],x['new'])
bib.write_text(s)
(r/'records/S6_SERIES_PUBLISH_I_coefficient_editorial_comparison.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Root read the complete old C3.8 proof, operator comparison and both gauge passages, plus the exact attached-compendium chart-control proof and invariant fibre/generator displays. New replacements were read against those sources. No independent targeted derivation is claimed for this editorial work.',
 'old_C38':oldproof,'new_C38':newproof,
 'root_input_maps':'The chart-control proof is supplied inside the same proper-family theorem fam:A3.1; all coefficient domains and inverse chart maps remain unchanged. The invariant fibre formulas are exactly those printed under C3.7.',
 'before_sha256':hashlib.sha256(before.encode()).hexdigest(),'after_sha256':hashlib.sha256(ed.text.encode()).hexdigest()
},indent=2)+'\n')
