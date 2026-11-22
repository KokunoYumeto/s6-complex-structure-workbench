#!/usr/bin/env python3
"""Prepare GN complete block/guards only; never mutate canonical files."""
from pathlib import Path
import hashlib,json,datetime,re,difflib
B=Path(__file__).resolve().parents[3]
P=Path(__file__).resolve().parent
G=P/'GN_guard_blocks'
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def rel(p): return str(p.relative_to(B))
def bind(p): return {'path':rel(p),'sha256':h(p),'bytes':p.stat().st_size}
source=B/'S6_SERIES_PUBLISH_II.tex'
S=source.read_text()
source_sha=hashlib.sha256(S.encode()).hexdigest()
O=G/'S6_SERIES_PUBLISH_II_01GN_current_original_full_block.tex'
old=O.read_text(); assert S.count(old)==1
new=old; edits=[]
def edit(before,after,typ,reason):
    global new
    assert new.count(before)==1,(before[:90],new.count(before))
    off=new.index(before)
    edits.append({'before':before,'after':after,'type':typ,'reason':reason,
                  'sequential_before_offset':off})
    new=new[:off]+after+new[off+len(before):]

edit('of the actual Kodaira--Spencer matrix vanish',
     'of the Kodaira--Spencer matrix vanish','D08',
     'The statement already fixes the section sigma; remove the process adjective.')
edit(' No unspecified choice of a comb section is assigned a fixed root set.','',
     'D02/D11','The quantifier for a specified section and its determinant polynomial already give the complete scope.')
edit(r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
     r'\begin{enumerate}[label=\arabic*.,leftmargin=*]','D04',
     'Remove the run iteration marker while keeping the five proof items.')
edit('The lifted period map is its actual holomorphic pullback, not a change of frame with a pole.',
     'The lifted period map is its holomorphic pullback.','D02/D08',
     'Retain the stated holomorphic map and remove the contrastive reassurance.')
edit('At each of the two rank-one Mumford values, the limiting logarithmic derivative is the nonzero rank-one integral monodromy operator in the local torus frames.',
     r'''At the three Mumford values, the local period matrix has logarithmic
part $(\log q)/(2\pi i)\operatorname{diag}(1,\epsilon)$, where
$\epsilon=0$ at the two rank-one values and $\epsilon=1$ at the
hexagonal value; see \cite[equation~(3.1), p.~6]{Viaclovsky2026Two}.
Its value under $q\partial_q$ is
$(2\pi i)^{-1}\operatorname{diag}(1,\epsilon)$ at the centre.
Thus the logarithmic matrix has rank one at each of the two rank-one values.''',
     'D06/D25','Give the actual period-to-logarithmic-derivative map, including its 2 pi i factor; the rank is unchanged.')
edit(' This proves the two-parameter assertion without assuming a theta identity for its varying section.','',
     'D02/D08','The preceding divisor computation already establishes the assertion.')
edit(' In particular this calculation determines the value of the extended logarithmic boundary at the cusp, even though its fibre is not normal crossing.','',
     'D02/D08','The retained E14 logarithmic map and the nonzero determinant away from the root already include the cusp.')
needle=r''' \kappa_\sigma:\OO(-5)\longrightarrow V\otimes G.
\]
The determinant is a section'''
replacement=r''' \kappa_\sigma:\OO(-5)\longrightarrow V\otimes G.
\]
The comparison with the coarse period bundle is given on the finite
covers $t=w^n$ by
\[
 D_3(w)=\operatorname{diag}(1,1,w,w^2),\qquad
 D_4(w)=\operatorname{diag}(1,1,w,w^3),\qquad
 \Psi^\sharp(w)=D_n(w)\Psi(w^n)D_n(w)^{-1}.
\]
The fixed critical values give $\Psi(t)=I+O(t)$, so
$\Psi^\sharp(w)=I+O(w)$ is holomorphic and equivariant, with the
same central characters. These are the maps of
\cite[Proposition~6.2, pp.~22--23]{Viaclovsky2026Combs}.
The tautological sequence on the root curve has trivial determinant
for its middle cohomology bundle: the marked flat volume extends
through the finite covers and through the determinant-one logarithmic
frame at the cusp. Taking determinants therefore identifies
$\det V$ with $\det G$. Each comb tooth contributes coarse degree
two to $G$, by \cite[equation~(5.5), p.~16]{Viaclovsky2026Combs}.
The unchanged finite characters make the determinant change the
pullback of $\mathcal O_{\mathbb P^1}(2m)$, which is
$\mathcal O_{\mathfrak B}(24m)$ on $\mathfrak B=\mathbb P(3,4)$.
The determinant is a section'''
edit(needle,replacement,'D06/D25',
     'Supply the exact coarse-to-root character maps and determinant transport used in the degree calculation; retain its original displayed result.')
edit('Here is the exact computation of that polynomial for any of the period sections in the construction. ',
     '', 'D08','Remove the announcement; the marked matrix definition begins the argument directly.')
edit('frame the Hodge subbundle of the canonical flat extension.',
     'frame the Hodge subbundle of the marked cohomology extension.',
     'D25','Identify the extension constructed by the finite-character and logarithmic frames, whose connection is used in the formula.')
edit('Let $\\nabla$ be its explicitly marked Gauss--Manin connection,',
     'Let $\\nabla$ be its marked Gauss--Manin connection,',
     'D08','Remove an emphasis word while retaining the fixed marking.')
needle='The first expression uses the quotient frame of $G$ and the dual frame of $V=F^*$; it specifies every matrix entry and therefore also the rank-zero test.'
replacement=r'''The first expression uses the quotient frame of $G$ and the dual frame
of $V=F^*$; it specifies every matrix entry and therefore also the
rank-zero test. On a Grassmann chart with invertible upper block $A$
of $U$, the frame change $U\mapsto UA^{-1}$ gives
$\binom{I}{Z}$. Write $A_{ij}$ for the four blocks of the connection
matrix contracted with $D$. Projection to the quotient by
$(u,v)\mapsto v-Zu$ gives the matrix
\[
 DZ+A_{21}+A_{22}Z-ZA_{11}-ZA_{12}Z.
\]
In this chart its determinant is the four-column determinant in
\eqref{cdp:eq:E.16.3}.'''
edit(needle,replacement,'D25',
     'Derive all four matrix entries by the explicit Hodge-frame and quotient maps; the determinant identity is independently checked by graph projection and six two-minors.')
before='Changing the Hodge frame multiplies the determinant by the square of its determinant, exactly its transition in $\\det V\\otimes\\det G\\otimes T_{\\mathfrak B}(-p_0)^{-2}$. Changing a root parameter gives the inverse square of the tangent-frame change. Thus the local calculations glue to the stated global section and determine $P_\\sigma$ from the actual period data.'
after=r'''For a Hodge-frame change $U'=UC$, one has
$\nabla_DU'=(\nabla_DU)C+U(DC)$; wedging the four columns
multiplies the coefficient by $(\det C)^2$.
For a tangent-frame change $D'=aD$, the coefficient is multiplied
by $a^2$, while the dual differential frame is multiplied by
$a^{-1}$. Their tensor product therefore gives the same section of
$\det V\otimes\det G\otimes T_{\mathfrak B}(-p_0)^{-2}$.
These transition maps determine $P_\sigma$ from the marked period data.'''
edit(before,after,'D25/D08',
     "Correct the tangent-frame coefficient rule and exhibit its reciprocal differential-frame compensation; for D'=2D the coefficient is four times the original, not one quarter.")
before='In the cusp comparison of \\ref{cdp:st:E7} and \\ref{cdp:st:E15}, the logarithmic derivative has the fixed invertible integral leading matrix; its determinant is nonzero. This proves both the nonzero-polynomial assertion and the exact rank-divisor description.'
after=r'''In the cusp comparison of \ref{cdp:st:E7} and \ref{cdp:st:E15},
the marked frame satisfies
$\nabla e_i=f_i\,dq/(2\pi iq)$ and $\nabla f_i=0$,
and the Hodge plane is the graph $(I,H_\sigma(q))$;
see \cite[Proposition~4.1, p.~12]{Viaclovsky2026Combs}.
Projection along this graph sends the logarithmic derivative to
$(2\pi i)^{-1}I+qH_\sigma'(q)$. At the cusp its determinant is
$(2\pi i)^{-2}\ne0$.'''
edit(before,after,'D06/D08/D25',
     'Relate integral monodromy to the stated q d/dq derivative by its exact 2 pi i factor and remove the closing recap.')

out=G/'S6_SERIES_PUBLISH_II_01GN_proposed_full_block_v1.tex'
assert not out.exists();out.write_text(new)
def anchors(t):return re.findall(r'\\(?:label|hypertarget)\{[^}]*\}',t)
assert anchors(old)==anchors(new)
display=lambda t:re.findall(r'\\\[(.*?)\\\]',t,re.S)
od,nd=display(old),display(new)
pos=0
for x in od:
    pos=nd.index(x,pos)+1
refs=lambda t:re.findall(r'\\(?:ref|eqref|SeriesRef|cref|Cref)\{([^}]*)\}',t)
or_,nr=refs(old),refs(new); pos=0
for x in or_:pos=nr.index(x,pos)+1
assert new.count('\\begin{proposition}')==new.count('\\end{proposition}')==1
assert new.count('\\begin{proof}')==new.count('\\end{proof}')==1
assert old.count('\\item ')==new.count('\\item ')==5
patch=G/'S6_SERIES_PUBLISH_II_01GN_full_pair_v1.diff'
patch.write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=O.name,tofile=out.name)))
guard={'id':'II-infra-recovery-01GN-publication','statement_id':'cdp:st:E16','tag':'01GN',
 'source_sha256':source_sha,'type':'D02/D04/D06/D08/D11/D25','before':old,'after':new,
 'literal_edits':edits,'original_full_block':rel(O),'original_full_block_sha256':h(O),
 'proposed_full_block':rel(out),'proposed_full_block_sha256':h(out),
 'reason':'Complete E16 proof comparison: publication edits and explicit determinant/period-frame maps; mathematical statement and labelled formulas retained.',
 'preservation':{'all_labels_and_hypertargets_identical':True,'all_original_displayed_math_in_identical_order':True,
 'all_original_references_in_identical_order':True,'added_reference':'One receiving reference to existing E.16.3 in the graph-matrix explanation.',
 'removed_source_math':['Only the nonmathematical enumeration iteration marker $\\langle1\\rangle$.'],
 'added_math_scope':['Actual logarithmic period factor (2 pi i)^-1 at nodal/hexagonal values.','Finite-character lift and root determinant transport already in frozen derivation.','Graph projection formula for the same Kodaira--Spencer morphism.','Exact Hodge/tangent/differential frame maps.'],
 'statement_change':'Only deletion of process adjective and redundant disclaimer; all mathematical quantifiers/conclusions/formulas retained.'},
 'review_status':'Prepared; requires complete original/final rereading and root review before application.'}
j=P/'S6_SERIES_PUBLISH_II_01GN_guards_v1.json';assert not j.exists();j.write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':source_sha,'guards':[guard],'events_added':0,'canonical_mutations':0},indent=2)+'\n')
rows=[
 ('Weighted determinant polynomials, integral period pairings and the Grassmann quotient matrix',
  'S6_SERIES_PUBLISH_II_01GN_prereading_certificate_v2.py','S6_SERIES_PUBLISH_II_01GN_prereading_certificate_output_v2.json'),
 ('Hodge and tangent frame covariance and the expansion into two-by-two minors',
  'S6_SERIES_PUBLISH_II_01GN_postrelease_frame_certificate.py','S6_SERIES_PUBLISH_II_01GN_postrelease_frame_certificate_output.json')]
programs=[]
for title,script,output in rows:
    row=title+r' (\cref{cdp:st:E16}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/'+script+r'}{\nolinkurl{'+script+r'}} \\[3pt]'
    programs.append({'program':bind(P/script),'output':bind(P/output),'copy_program_to':'code/'+script,'copy_output_to':'code/'+output,'table_row_tex':row})
table=P/'S6_SERIES_PUBLISH_II_01GN_program_table_proposal_v1.json';assert not table.exists();table.write_text(json.dumps({'scope':'Two new code rows only; root rebases against its final Programs table. No canonical write.','rows':programs},indent=2)+'\n')
print(json.dumps({'guards':bind(j),'literal_edit_count':len(edits),'final_block':bind(out),'diff':bind(patch),'program_table_proposal':bind(table)},indent=2))
