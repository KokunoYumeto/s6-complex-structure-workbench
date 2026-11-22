#!/usr/bin/env python3
"""Prepare E13 full-owner guards only. Never writes canonical source or ledgers."""
from pathlib import Path
import hashlib,json,re,datetime,difflib
R=Path(__file__).parents[3]
D=Path(__file__).parent
B=D/'GK_guard_blocks'
oldpath=B/'S6_SERIES_PUBLISH_II_01GK_current_original_full_block.tex'
old=oldpath.read_text()
assert hashlib.sha256(oldpath.read_bytes()).hexdigest()=='c9ab0f09825338aa735059c7d7182e192afd8bd3f3627627bcaa8c337a1a5cfd'
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
assert source.count(old)==1
edits=[]; new=old
def change(before,after,kind,reason):
    global new
    assert new.count(before)==1,(before,new.count(before))
    k=new.index(before)
    edits.append({'before':before,'after':after,'type':kind,'reason':reason,'sequential_before_offset':k})
    new=new[:k]+after+new[k+len(before):]

change(r'\SeriesRef{cdp:eq:E13-residue}, \SeriesRef{cdp:st:E11}, \SeriesRef{cdp:st:E1}',
       r'\SeriesRef{cdp:eq:E13-residue}, \SeriesRef{cdp:st:E1}',
       'D06','Remove the dependency whose needed local rank calculation is now supplied completely within this proof.')
change(r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
       r'\begin{enumerate}[label=\arabic*.,leftmargin=*]','D04','Remove the iteration marker while retaining every proof item and its order.')
change('We work with the equation and section used in the construction,',
       'The construction uses the equation and section','D08','State the actual input directly.')
change('We spell out the bundles and the residue map, since their ranks alone\nwould not determine the answer. The vertical logarithmic Lie bundle\nis',
       'The vertical logarithmic Lie bundle is','D08/D11','Remove the announcement and reassurance; retain the complete explicit connection, extension, and residue calculation.')
change('Thus these calculations prove\nthe claimed splitting on the entire root curve, with the specified\ncomparison maps.',
       'These connection and transition maps give the splitting on the\nentire root curve.','D08','Retain the actual global gluing conclusion with its morphisms.')
change('Here is the extension check. On a marked smooth fibre',
       'On a marked smooth fibre','D08','Remove the proof announcement.')
change('This identifies the comparison, including its value at\nthe special fibres. Cup product and the normalization sequences',
       'Cup product and the normalization sequences','D08','Remove the recap after the complete extension and descent arguments.')
change('There are no uncomputed differentials in these equalities: the base\nhas dimension one, and the groups of the first displayed row in\ndegrees two and three vanish.',
       'The base has dimension one, and the groups of the first displayed\nrow in degrees two and three vanish.','D11','Retain the exact vanishing justification without the completeness reassurance.')
change('It remains to compute the boundary\n$H^1(Q)\\to H^2(T_X(-\\log D))$, between two-dimensional spaces.',
       'The boundary $H^1(Q)\\to H^2(T_X(-\\log D))$ is a map between\ntwo-dimensional spaces.','D08','Identify the map directly before computing its exact matrix.')

before=r'''\item The rank-two cusp implies
$\bar f_*\Omega_X^1=\Omega_{\mathfrak B}^1$, by the generic
Kodaira--Spencer boundary and extension across the local models,
as in \ref{cdp:st:E11}. It follows that
$h^3(T_X)=h^0(\Omega_X^1\otimes K_X)
=h^0(\mathcal O(-9))=0$. The long exact sequence with quotient
$Q$ now gives $h^0(T_X)=1$, $h^1(T_X)=2$, and $h^2(T_X)=2$.'''
after=r'''\item Near the rank-two Mumford fibre put $q=t-p_3$. In the two
multiplicative coordinates its nonconstant periods are
$(qA_1(q),B_1(q))$ and $(A_2(q),\lambda qB_2(q))$, where all four
functions are holomorphic units; see
\cite[Proposition labelled \texttt{mum}]{Viaclovsky2026Two}.
Normalize the two circle periods to the identity matrix. The remaining
period matrix is $(2\pi i)^{-1}\log q\,I_2+H(q)$ with $H$ holomorphic,
and its derivative is $(2\pi iq)^{-1}I_2+H'(q)$, of rank two for
nonzero $q$ sufficiently close to zero. In these period frames this
derivative is the cotangent Kodaira--Spencer connecting map.
The vertical part of a holomorphic one-form is therefore zero on
this open set and hence throughout the regular locus.
At a reduced singular fibre, a smooth point of one component away
from the conductor is a submersion point, so the coefficient of
the resulting base one-form extends holomorphically. At infinity
the same argument applies on the smooth root cover, and invariance
under the free affine deck action gives descent. Thus
$\bar f_*\Omega_X^1=\Omega_{\mathfrak B}^1$.
It follows that
$h^3(T_X)=h^0(\Omega_X^1\otimes K_X)
=h^0(\mathcal O(-9))=0$. The long exact sequence with quotient
$Q$ now gives $h^0(T_X)=1$, $h^1(T_X)=2$, and $h^2(T_X)=2$.'''
change(before,after,'D06/D25','Supply the exact local period matrix, connecting map, and extension needed for the displayed h3 calculation; remove reliance on the still separately checked E11 target.')
change('Every element of $I$ vanishes under it, so $I=0$. This proves the\nKuranishi assertion. \\ref{cdp:st:E1} and \\ref{cdp:st:E6} give the algebraic-dimension assertion.',
       'Every element of $I$ vanishes under it, so $I=0$. The classifying\nmap is a local analytic isomorphism. \\ref{cdp:st:E1} and \\ref{cdp:st:E6} give the algebraic-dimension assertion.',
       'D08','Replace the recap with the actual miniversality consequence of the proved inverse-function map.')

change(r'; \cite[Proposition labelled \texttt{family}]{Viaclovsky2026Two}}',
       r'; \cite[Proposition~6.4, pp.~19--20]{Viaclovsky2026Two}}',
       'D06','Bind the metadata citation to the actually read public v1 PDF proposition and pages.')
change(r'\cite[Proposition labelled \texttt{family}]{Viaclovsky2026Two}, on the parameter',
       r'\cite[Proposition~6.4, pp.~19--20]{Viaclovsky2026Two}, on the parameter',
       'D06','Replace the private source label with the verified printed proposition/pages.')
change(r'\cite[Proposition labelled \texttt{mum}]{Viaclovsky2026Two}.',
       r'\cite[equation~(3.1) and Proposition~3.1, p.~6]{Viaclovsky2026Two}.',
       'D06','Bind the exact multiplicative periods and Mumford filling to the public PDF locator actually read by root.')

back=new
for e in reversed(edits):
    k=e['sequential_before_offset'];assert back[k:k+len(e['after'])]==e['after']
    back=back[:k]+e['before']+back[k+len(e['after']):]
assert back==old
assert re.findall(r'\\(?:label|hypertarget)\{[^}]+\}',old)==re.findall(r'\\(?:label|hypertarget)\{[^}]+\}',new)
assert old.count('\\item')==new.count('\\item')==9
for key in ('cdp:eq:E13-connection','cdp:eq:E13-residue'):
    def eqn(txt):
        k=txt.index('\\label{'+key+'}');a=txt.rfind('\\begin{equation}',0,k);z=txt.index('\\end{equation}',k)+len('\\end{equation}');return txt[a:z]
    assert eqn(old)==eqn(new)

newpath=B/'S6_SERIES_PUBLISH_II_01GK_proposed_full_block_v2.tex'
assert not newpath.exists();newpath.write_text(new)
diffpath=B/'S6_SERIES_PUBLISH_II_01GK_full_block_v2.diff'
diffpath.write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='original',tofile='proposed')))
def rec(p):
    return {'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
guard={'id':'II-infra-recovery-01GK-publication','statement_id':'cdp:st:E13','tag':'01GK',
       'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'type':'D04/D06/D08/D11/D25',
       'before':old,'after':new,'literal_edits':edits,
       'reason':'Publish the completely compared E13 proof, preserving its logarithmic-normal route and supplying the exact rank-two local period dependency.',
       'original_full_block':str(oldpath.relative_to(R)),'original_full_block_sha256':hashlib.sha256(old.encode()).hexdigest(),
       'proposed_full_block':str(newpath.relative_to(R)),'proposed_full_block_sha256':hashlib.sha256(new.encode()).hexdigest(),
       'preservation':{'exact_forward_inverse':True,'all_nine_items_preserved':True,'stable_labels_and_hypertargets_identical':True,
          'both_labelled_equations_exactly_identical':True,
          'removed_inline_math':['\\langle1\\rangle (iteration marker only)'],
          'added_math':'Item8 only: q=t-p3, four unit periods, logarithmic period matrix and its derivative. All original mathematical assertions remain.',
          'reference_map':{'removed':['\\SeriesRef{cdp:st:E11}','\\ref{cdp:st:E11}'],
                           'added':['\\cite[Proposition labelled \\texttt{mum}]{Viaclovsky2026Two}'],
                           'reason':'Exact local rank and extension argument supplied in the owner; primary construction locator replaces the E11 dependency.'}},
       'input_evidence':rec(D/'S6_SERIES_PUBLISH_II_01GK_prereading_input_receipt.json'),
       'fresh_different_method':rec(D/'S6_SERIES_PUBLISH_II_01GK_postrelease_inverse_certificate_output.json')}
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':guard['source_sha256'],
     'guards':[guard],'guard_count':1,'literal_edit_count':len(edits),
     'status':'PREPARED; complete final-pair actual reading recorded separately before handback',
     'events_added':0,'canonical_files_modified':False,'supersedes':{'path':'agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_01GK_guards.json','sha256':'1300a54cec62465bcb701ae08e616c5cf4a90ee306f7f493f4420a3d4c0abcd2','scope':'Only verified public-PDF citation locators added; v1 preserved'}}
path=D/'S6_SERIES_PUBLISH_II_01GK_guards_v2.json';assert not path.exists();path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'guard':rec(path),'full_pair':[rec(oldpath),rec(newpath)],'literal_edits':len(edits)}))
