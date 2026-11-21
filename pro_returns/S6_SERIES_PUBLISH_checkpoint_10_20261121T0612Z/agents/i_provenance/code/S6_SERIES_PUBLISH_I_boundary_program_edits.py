from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,csv,re
ROOT=Path('/workspace/scratch/653608133b22'); OUT=ROOT/'work/agents/i_provenance'
source=ROOT/'work/S6_SERIES_PUBLISH_I.tex'; original=source.read_text(); current=original
sha=hashlib.sha256(original.encode()).hexdigest(); now=datetime.now(timezone.utc).isoformat()
changes=[]
def change(i,sid,old,new,reason,defect='D05/D13'):
 global current
 n=current.count(old); assert n==1,(i,n)
 changes.append({'id':i,'statement_id':sid,'old':old,'new':new,'reason':reason,'defect':defect})
 current=current.replace(old,new,1)

change('I-boundary-program-B12','push:src:B.1.2',r'''The identity $R_j\Pi_c=\Pi'_c A_j$ and the fixed-vector
identities $A_jv_j=v_j$ are checked symbolically in
\texttt{ab\_push\_finite\_decks.py}.''',r'''The identities $R_j\Pi_c=\Pi'_c A_j$ and $A_jv_j=v_j$
follow by substitution of the displayed matrices; their symbolic
certificate is listed in \cref{tab:I:programs}.''','Retain exact covariance/fixed-vector identities and executable certificate, with the path in the end table.','D01/D05')
change('I-boundary-descent-B12','push:src:B.1.2',r'''Period covariance says
exactly that it defines the required bundle isomorphism
after quotient by $\ker\gamma$; it is not being treated
as a scalar function on the elliptic curve when it is not
one.''',r'''Period covariance gives the descent rule for $U_j$ and
therefore the required bundle isomorphism after quotient
by $\ker\gamma$.''','State the positive bundle descent map; preserve the exact quotient and unit data.')
change('I-boundary-gauge-domain-B12','push:src:B.1.2',r'''This local gauge is not
asserted to extend across $r=0$ on overlaps with other
base neighbourhoods.''',r'''This gauge identifies the local pullbacks on the
punctured overlaps $r\ne0$.''','Keep the actual domain of the displayed identification without adding an extension claim.')
change('I-boundary-program-B21','push:src:B.2.1',r'''The determinant, intersection and volume assertions
for both requested exponents are certified in
\texttt{ab\_push\_basechange\_fan.py} using rational
arithmetic.''',r'''For $n=2$ and $n=12$, the determinant, intersection and
volume calculations have exact rational certificates
listed in \cref{tab:I:programs}.''','The authenticated program covers n=2,12; the preceding structural proof retains its general n scope.','D01/D05')
change('I-boundary-section-B3','push:section:B.3',r'\subsection{The prescribed pieces do not glue}',r'\subsection{Component monodromy and trace obstructions}','Use the mathematical mechanisms as the section title.','D04')
change('I-boundary-title-B31','push:src:B.3.1',r'\begin{theorem}[counterexample to simultaneous gluing]',r'\begin{theorem}[Peripheral component obstruction]','Give the exact obstruction a mathematical title.','D04')
change('I-boundary-scope-B31','push:src:B.3.1',r'''neighbourhoods. In particular the proposed simultaneous gluing is false. This conclusion does
not rule out a different cusp model of the same
punctured $S^6$ family.''',r'''neighbourhoods. The obstruction is the peripheral component
monodromy of these prescribed finite and plain cusp models.''','Preserve the precise model scope and remove the repeated rejection/alternative discussion.')
change('I-boundary-cover-B31','push:src:B.3.1',r'''This
description constructs the cover and requires
no conjecture about components at the missing
three points.''',r'''This description constructs the component cover over
$B^\circ$.''','Give the exact base of the constructed cover.')
change('I-boundary-program-B31','push:src:B.3.1',r'''The four residues and the finite
component cycles are checked exactly by
\texttt{ab\_push\_finite\_decks.py}.''',r'''The exact residue and component-cycle calculation is
listed in \cref{tab:I:programs}.''','Keep one operative program citation for the finite peripheral computation.','D01/D05')
change('I-boundary-title-B33','push:src:B.3.3',r'\begin{proposition}[obstruction to a specified repair]',r'\begin{proposition}[Cusp-root multiplicities]','Title the proved multiplicity formula.','D04')
change('I-boundary-diagnostic-B33','push:src:B.3.3',r'''this gives the final
lower bound. The residue calculations
and examples for the requested
exponents are independently recorded
in \texttt{ab\_push\_cusp\_root\_repair.py}.
This rules out the specified repair,
not a cusp model with a different
geometry or a different comparison
to the punctured family.''',r'''this gives the final lower bound.''','The proof already establishes the bound for all d. The script enumerates d=1,…,60 only and remains a historical diagnostic, without independent/general-certificate credit.','D01/D05/D13')
change('I-boundary-title-B34','push:src:B.3.4',r'\begin{theorem}[split-normalization trace obstruction]',r'\begin{theorem}[Trace on the split elliptic normalization]','Retain the exact split scope in the mathematical title.','D04')
change('I-boundary-scope-B34','push:src:B.3.4',r'''
This conclusion is restricted to the
stated split normalization. A ruled
normalization over a nontrivial genus-one
torsor need not admit a section or such
an expression for its affine deck lift;
it is not excluded by this theorem.
''','\n','The statement already specifies the split ruled normalization and conductor map; the actual nontrivial torsor construction is proved in B3.6. The repeated defensive paragraph supplies no additional proof step.')
change('I-boundary-program-B34-sections','push:src:B.3.4',r'''The ansatz that produced these sections,
its other solutions, and this line
identity are checked symbolically in
\texttt{ab\_push\_trace\_sections.py}.''',r'''The section equations and the line identity have an
exact symbolic certificate listed in \cref{tab:I:programs}.''','Archive exploration/other ansatz solutions; cite the operative section and collinearity identities.','D01/D05')
change('I-boundary-matrix-B34','push:src:B.3.4',r'''or from the integral
intersection matrix recorded in
\texttt{ab\_push\_trace\_obstruction.py}.''',r'''or from the integral
intersection matrix specified by the following entries.''','Retain the alternative integral determinant calculation with its actual entries; executable mapping is cited once at the end of this computation.','D01/D05')
change('I-boundary-program-B34-trace','push:src:B.3.4',r'''The exact matrices, local series,
torsion test, and all relevant residue
classes are verified in
\texttt{ab\_push\_trace\_obstruction.py}.''',r'''An executable certificate for the exact matrices, local
series, torsion test and residue classes is listed in
\cref{tab:I:programs}.''','Keep the actual operative certificate scope.','D01/D05')
change('I-boundary-title-B35','push:src:B.3.5',r'\begin{corollary}[exact Mordell--Weil lattice]',r'\begin{corollary}[Integral Mordell--Weil lattice]','Use a mathematical title.','D04')
change('I-boundary-program-B35','push:src:B.3.5',r'''The pole-basis calculation, coefficient
equations and three half-class heights
are included in the exact certificate
\texttt{ab\_push\_trace\_obstruction.py}.''',r'''The pole-basis calculation, coefficient equations and
three half-class heights are included in the exact
certificate listed in \cref{tab:I:programs}.''','Map the saturation computation to its authenticated shared program.','D01/D05')
change('I-boundary-title-B36','push:src:B.3.6',r'\begin{proposition}[an unramified torsor alternative]',r'\begin{proposition}[Unramified torsors with prescribed transgression]','Name the actual torsor invariant.','D04')
change('I-boundary-scope-B36','push:src:B.3.6',r'''In particular the trace obstruction of
\ref{push:src:B.3.4} does not obstruct all genus-one
torsors. Such a class has a relatively''',r'''Such a class has a relatively''','The positive existence assertion and transgression formula prove the exact torsor result directly.')
change('I-boundary-scope-end-B36','push:src:B.3.6',r'''This is an existence statement for a
possible normalization base, not a
construction of a threefold central
fibre or of its smoothing.''',r'''Thus $(V,A)$ is a genus-one normalization base with the
specified affine twelfth power.''','Retain exactly the constructed datum and affine map.')
change('I-boundary-torsor-description-B36','push:src:B.3.6',r'''This use of torsors and local
twists is the one in
\cite[Sections 3--4]{Xiao91}; it does
not assert an explicit equation for
the selected torsor.''',r'''The local translation gluing specifies $V$ as in
\cite[Sections 3--4]{Xiao91}.''','State the actual analytic construction and retain the cited source.')
change('I-boundary-program-B36','push:src:B.3.6',r'''The finite carry-cocycle identities,
its exact order two modulo twelve,
and the three local component checks
are recorded in
\texttt{ab\_push\_torsor\_cocycles.py}.''',r'''The finite carry-cocycle identities, its order two
modulo twelve and the three local component calculations
have an executable certificate listed in
\cref{tab:I:programs}.''','Restrict the program claim to finite cochains and component arithmetic; existence uses the displayed exact sequences.','D01/D05')
change('I-boundary-required-data-B36','push:src:B.3.6',r'''\item Neither this cohomological construction
nor local triviality specifies the
normal line bundles, the threefold
cusp charts, or a smoothing with the
given punctured-family identification.
Those remain requirements of \ref{push:src:B.4.1}.''',r'''\item To form the threefold filling of \ref{push:src:B.4.1},
the datum $(V,A)$ must be supplemented by its normal line
bundles, cusp charts and specified punctured-family
identification.''','Keep every further geometric input as a positive requirement.')
change('I-boundary-title-B37','push:src:B.3.7',r'\begin{proposition}[an auxiliary family with the wrong cusp]',r'\begin{proposition}[Auxiliary torsor plumbing with cusp multiplicity twelve]','Name the proved cusp invariant.','D04')
change('I-boundary-plumbing-B37','push:src:B.3.7',r'''\item We spell out the comparison with \ref{push:src:A.1.2}
to identify the family actually obtained.''',r'''\item Apply the plumbing maps of \ref{push:src:A.1.2}
to the data $(V,M,A)$.''','State the exact substitution used in the comparison.')
change('I-boundary-family-scope-B37','push:src:B.3.7',r'''No identification with the requested
punctured $S^6$ family is being made.
''','','The actual family maps have been specified; the following Euler and multiplicity arguments prove the precise difference from the prescribed sphere family.')
change('I-boundary-conductor-B37','push:src:B.3.7',r'''The double locus is $V$, not $V/A$.''',r'''Thus the double locus is parametrized by $V$.''','Keep the double-locus identification proved by the immediately preceding disjoint-collar argument.')
change('I-boundary-program-B37','push:src:B.3.7',r'''The finite Euler, polynomial and
multiplicity checks are in
\texttt{ab\_push\_auxiliary\_plumbing.py}.''',r'''The characteristic-polynomial identity and both Euler
calculations have an executable certificate listed in
\cref{tab:I:programs}.''','The program verifies the polynomial and finite Euler arithmetic; it records the cusp multiplicity as data. The displayed valuation argument proves the geometric multiplicity scope.','D01/D05')

change('I-boundary-title-B11','push:src:B.1.1',r'\begin{proposition}[counterexample and corrected]',r'\begin{proposition}[Finite-root plumbing and ruled central fibres]','Name the actual local model.','D04')
change('I-boundary-opening-B11','push:src:B.1.1',r'''The assertion that the filling is the product of the smooth elliptic
family with a twelve-gon Tate model is false on the whole root disc. There is, however, a proper flat holomorphic filling of
the marked root family over''',r'''The marked root family admits a proper flat holomorphic filling over''','State the constructed proper flat local model directly; all equations and quotient maps in the proof remain unchanged.')
change('I-boundary-ruled-scope-B11','push:src:B.1.1',r'''They are not generically products with $\mathbb P^1$.''',r'''Whenever $P_s-O_s$ is non-torsion, no finite isogeny of the
elliptic base makes these ruled normalizations into products.''','The exact norm argument and the ruled-bundle triviality criterion prove this quantified assertion; retain the morphism relating the models.')
change('I-boundary-height-cite-B11','push:src:B.1.1',r'''in Engel's Lemma 2.1.''',r'''in \cite[proof of Lemma~2.1, pp.~3--4]{Engel2026}.''','Use the actually viewed primary height calculation, rather than the unrelated cusp quotient Proposition2.7.','D09')
change('I-boundary-isogeny-B11','push:src:B.1.1',r'''This disproves the
product assertion, even after an arbitrary fixed finite
isogeny of the elliptic factor. The special torsion
isogenies at $s_j=0$ used in \cref{fam:src:E.2.1} remain valid.''',r'''For each such $s$, the ruled normalization remains nontrivial
after every finite isogeny of the elliptic factor, by the norm
argument above. The torsion isogenies at $s_j=0$ are those
in \cref{fam:src:E.2.1}.''','Retain the exact non-torsion/norm conclusion and the special central isogenies with their distinct stated parameter scopes.')

for item in changes:
 if item['id'] in ['I-boundary-program-B31','I-boundary-program-B34-sections','I-boundary-program-B34-trace','I-boundary-program-B35','I-boundary-program-B36','I-boundary-program-B37']:
  current=current.replace(item['new'],'',1)
  item['new']=''
  item['reason']+=' The complete input, calculation and conclusion remain in the proof; the explicit statement-to-program mapping is in the end table.'
 if item['id']=='I-boundary-program-B12':
  replacement=r'''The identities $R_j\Pi_c=\Pi'_c A_j$ and $A_jv_j=v_j$
follow by substitution of the displayed matrices.'''
  current=current.replace(item['new'],replacement,1);item['new']=replacement
 if item['id']=='I-boundary-program-B21':
  replacement=r'''For $n=2$ and $n=12$, the determinant, intersection and
volume calculations use exact rational arithmetic.'''
  current=current.replace(item['new'],replacement,1);item['new']=replacement
 if item['id']=='I-boundary-gauge-domain-B12':
  current=current.replace(item['new'],'',1);item['new']=''
  item['reason']+=' The preceding sentence already states that the identification is over r!=0.'

def block(s,sid):
 pos=s.index('\\label{'+sid+'}')
 m=list(re.finditer(r'\\begin\{(?:theorem|lemma|proposition|corollary|remark|definition|cited)\}',s[:pos]))[-1]
 end=s.index('\\end{proof}',pos)+len('\\end{proof}')
 return s[m.start():end]
sids=['push:src:B.1.1','push:src:B.1.2','push:src:B.2.1','push:src:B.3.1','push:src:B.3.3','push:src:B.3.4','push:src:B.3.5','push:src:B.3.6','push:src:B.3.7']
review=[]
for sid in sids:
 old,new=block(original,sid),block(current,sid)
 name=sid.replace(':','_').replace('.','_')
 oldp=OUT/f'S6_SERIES_PUBLISH_I_boundary_{name}_original.tex';newp=OUT/f'S6_SERIES_PUBLISH_I_boundary_{name}_proposed.tex'
 oldp.write_text(old+'\n');newp.write_text(new+'\n')
 anchors=lambda q:re.findall(r'\\(?:label|hypertarget|tag)\{[^}]+\}',q)
 displays=lambda q:re.findall(r'\\\[.*?\\\]|\\begin\{(?:align\*?|equation\*?|gather\*?)\}.*?\\end\{(?:align\*?|equation\*?|gather\*?)\}',q,re.S)
 assert anchors(old)==anchors(new),sid
 assert displays(old)==displays(new),sid
 review.append({'statement_id':sid,'original':str(oldp),'proposed':str(newp),'original_sha256':hashlib.sha256(old.encode()).hexdigest(),'proposed_sha256':hashlib.sha256(new.encode()).hexdigest(),'anchors_preserved_in_order':True,'all_displayed_equations_unchanged':True,'changes':[x['id'] for x in changes if x['statement_id']==sid]})
guard={'source_sha256':sha,'created_utc':now,'changes':changes,'scope':'Guarded editorial/program-scope proposal only. All eight original proofs were read. Proposed proof rereading and events are recorded separately. No root source write.'}
(OUT/'S6_SERIES_PUBLISH_I_boundary_program_guards.json').write_text(json.dumps(guard,ensure_ascii=False,indent=2)+'\n')
(OUT/'S6_SERIES_PUBLISH_I_boundary_program_comparison.json').write_text(json.dumps({'created_utc':now,'source_sha256':sha,'proofs':review,'code_scope':'Seven pinned sources read in full; none executed in this source-authentication pass.','new_independent_or_computational_events':0},ensure_ascii=False,indent=2)+'\n')
receipt=json.loads((OUT/'S6_SERIES_PUBLISH_I_boundary_program_receipt.json').read_text())
mapping={
'ab_push_finite_decks.py':(['push:src:B.1.2','push:src:B.3.1'],'Finite period covariance, affine deck formulas, component cycles and peripheral residues','operative'),
'ab_push_basechange_fan.py':(['push:src:B.2.1'],'Rational fan certificates for the base changes $n=2$ and $n=12$','operative'),
'ab_push_cusp_root_repair.py':(['push:src:B.3.3'],'Bounded diagnostic residues for n=2,12 and root degrees1–60; the general multiplicity result is proved in the text','diagnostic in records only'),
'ab_push_trace_sections.py':(['push:src:B.3.4'],'Section equations and collinearity identities on $b^3=a^4+1$','operative'),
'ab_push_trace_obstruction.py':(['push:src:B.3.4','push:src:B.3.5'],'Node series, height and intersection lattices, trace congruences and integral saturation','operative'),
'ab_push_torsor_cocycles.py':(['push:src:B.3.6'],'Finite cyclic carry cocycles and local component arithmetic','operative'),
'ab_push_auxiliary_plumbing.py':(['push:src:B.3.7'],'Characteristic polynomial, integral inverse identity and both Euler calculations','operative')}
rows=[];tex=[]
for r in receipt['programs']:
 ids,purpose,disposition=mapping[r['filename']]
 r.update(source_read_in_full=True,program_executed_in_this_pass=False,statement_ids=ids,purpose=purpose,disposition=disposition)
 row={k:r[k] for k in ['filename','commit','path','bytes','sha256','url']}
 row.update(statement_ids=';'.join(ids),purpose=purpose,disposition=disposition,verification_basis='Raw primary bytes equal observed pinned Git blob and size; full code read, no execution')
 rows.append(row)
 if disposition=='operative':
  label=r['filename'].replace('_',r'\_')
  url='https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\\SsixRepositoryCommit/'+r['path']
  tex.append(purpose+r' (\cref{'+','.join(ids)+r'}) & \href{'+url+r'}{\texttt{'+label+r'}} \\')
receipt['scope_read_completed_utc']=now;receipt['mathematical_events_added_for_authentication']=0
(OUT/'S6_SERIES_PUBLISH_I_boundary_program_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
with (OUT/'S6_SERIES_PUBLISH_I_boundary_program_map.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
(OUT/'S6_SERIES_PUBLISH_I_boundary_program_rows.tex').write_text('\n'.join(tex)+'\n')
print(json.dumps({'guards':len(changes),'full_proof_blocks':len(review),'operative_programs':len(tex),'diagnostic_programs':1,'source_sha256':sha,'new_math_events':0}))

