#!/usr/bin/env python3
"""Prepare the complete E11 publication pair; no canonical mutation."""
from pathlib import Path
import re,json,hashlib,datetime,difflib
R=Path(__file__).parents[3];D=Path(__file__).parent;B=D/'GI_guard_blocks'
op=B/'S6_SERIES_PUBLISH_II_01GI_original_full_block.tex';old=op.read_text()
assert hashlib.sha256(op.read_bytes()).hexdigest()=='c81d7360859f8f5c4f1326b1431d3f876753a3a5e1db80b419c7c7c444643dc3'
src=(R/'S6_SERIES_PUBLISH_II.tex').read_text();assert src.count(old)==1
new=old;edits=[]
def change(before,after,typ,reason):
 global new
 assert new.count(before)==1,(before,new.count(before))
 i=new.index(before);edits.append({'before':before,'after':after,'type':typ,'reason':reason,'sequential_before_offset':i})
 new=new[:i]+after+new[i+len(before):]
change(r'; \cite[Theorem labelled \texttt{t:main}]{Viaclovsky2026Log}}',
       r'; \cite[Theorem~1.1, p.~1]{Viaclovsky2026Log}}','D06','Use the exact printed public-v1 theorem locator, verified on the full page image.')
change(r'\cite[Theorem labelled \texttt{t:main}]{Viaclovsky2026Log},',
       r'\cite[Theorem~1.1, p.~1]{Viaclovsky2026Log},','D06','Bind the construction statement to its actual printed theorem and page.')
change(r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
       r'\begin{enumerate}[label=\arabic*.,leftmargin=*]','D04','Remove the production iteration marker, preserving all four mathematical items.')
change('coarse $\\mathbb P^1$ sends the two root sections to their $k$th and\n$l$th powers. In line notation',
       'coarse $\\mathbb P^1$ sends the two root sections to their $k$th and\n$l$th powers. In weighted homogeneous coordinates it is\n$[x:y]\\mapsto[x^l:y^k]$. In line notation',
       'D25','Supply the exact global root morphism matching the two stated local powers and the line-bundle pullback.')
change('This specifies the comparison rather than identifying the two\nhorizontal tangent lines. At the cusp',
       'At the cusp','D11','Remove the distinction/reassurance after the exact horizontal and vertical transition maps already supplied.')
change('\\item We compute degree three independently. On the smooth torus locus,',
       '\\item On the smooth torus locus,','D08','Remove the proof announcement; retain the full degree-three argument.')
change(' This computation does not require the integral homology\nto be that of a sphere.','',
       'D11','The retained direct calculation already proves the stated arbitrary-admissible-affine-twist scope.')
before=r'''\item The scale derivative changes the fourth torus period by a nonzero
constant multiple of the parameter derivative in \SeriesRef{fam:st:A.5.2}, so its
restricted torus class is nonzero. A first-order trivialization of'''
after=r'''\item Use the period quotient and reference linearization of
\SeriesRef{fam:st:B.1.1} and \SeriesRef{fam:st:B.1.4}. They give
$u=e^{-2\pi ic}$ and
$[\zeta_1,\zeta_2]\mapsto[\zeta_1,e^{2\pi i\zeta_2}]$.
Thus $e=\partial_{\zeta_2}$ maps to $2\pi i$ times the line-bundle
Euler field $\Xi$. The integral marking of \SeriesRef{push:src:E.1.1}
gives $\gamma=-\psi$, where $\psi$ counts the forward generator
$\Phi_u=u\phi$ covering translation by $-6P$.
For $\kappa(\Phi)=(\partial\Phi)\Phi^{-1}$, differentiation gives
\[
 \kappa(\partial_u)=u^{-1}\Xi\otimes[\psi]
       =-(2\pi iu)^{-1}e\otimes[\gamma],\qquad
 \kappa(\partial_c)=e\otimes[\gamma].
\]
Here the fibre classes extend by the coherent Leray comparison of
\SeriesRef{fam:st:A.5.2}; they are nonzero on every regular torus
fibre. A first-order trivialization of'''
change(before,after,'D06/D25','Replace an unspecified scalar comparison by the exact period, exponential-vector, integral-covector, arrow and parameter maps, retaining the printed global nontriviality argument.')
change('The one-dimensional tangent space and the analytic local-algebra\nargument at the end of \\SeriesRef{fam:st:A.5.2} prove smoothness, reducedness and\nminiversality.',
       'Write the Kuranishi local ring as $\\mathbb C\\{z\\}/I$. The scale\nclassifying map has nonzero derivative, so before quotienting its\nsubstitution into $\\mathbb C\\{u-u_0\\}$ is a local analytic\nisomorphism. Every element of $I$ maps to zero; hence $I=0$. The\nclassifying map is locally an isomorphism, proving smoothness,\nreducedness and miniversality.',
       'D06/D25','Supply the exact one-dimensional local-algebra argument instead of an unspecified end-of-proof locator.')
back=new
for e in reversed(edits):
 i=e['sequential_before_offset'];assert back[i:i+len(e['after'])]==e['after'];back=back[:i]+e['before']+back[i+len(e['after']):]
assert back==old
assert re.findall(r'\\(?:label|hypertarget)\{[^}]+\}',old)==re.findall(r'\\(?:label|hypertarget)\{[^}]+\}',new)
assert old.count('\\item')==new.count('\\item')==4
np=B/'S6_SERIES_PUBLISH_II_01GI_proposed_full_block.tex';assert not np.exists();np.write_text(new)
dp=B/'S6_SERIES_PUBLISH_II_01GI_full_block.diff';dp.write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='original',tofile='proposed')))
def rec(p):return {'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
g={'id':'II-infra-recovery-01GI-publication','statement_id':'cdp:st:E11','tag':'01GI','source_sha256':hashlib.sha256(src.encode()).hexdigest(),'type':'D04/D06/D08/D11/D25','before':old,'after':new,'literal_edits':edits,'reason':'Publish the completely compared E11 proof with exact coordinate/KS maps and verified public locators; preserve its logarithmic-normal/RR route and its full affine-twist scope.','original_full_block':str(op.relative_to(R)),'original_full_block_sha256':hashlib.sha256(old.encode()).hexdigest(),'proposed_full_block':str(np.relative_to(R)),'proposed_full_block_sha256':hashlib.sha256(new.encode()).hexdigest(),'preservation':{'exact_forward_inverse':True,'all_four_items_preserved':True,'all_stable_labels_and_hypertargets_identical':True,'all_original_mathematical_assertions_retained':True,'removed_math':['iteration marker \\langle1\\rangle only'],'added_math':['Exact root morphism [x:y] -> [x^l:y^k]','Exact u/c, exponential vector and integral covector transport; displayed KS formulas','Explicit Kuranishi local ring and analytic isomorphism argument'],'reference_map':{'same_key_public_locator':'Viaclovsky2026Log: t:main -> Theorem1.1,p1 in both occurrences','added_series_inputs':['fam:st:B.1.1','fam:st:B.1.4','push:src:E.1.1'],'retained_support':'fam:st:A.5.2 coherent comparison','removed_locator':'Vague end-of-proof reference replaced by complete local-algebra argument'}},'input_evidence':rec(D/'S6_SERIES_PUBLISH_II_01GI_prereading_input_receipt.json'),'different_method_output':rec(D/'S6_SERIES_PUBLISH_II_01GI_postrelease_hilbert_certificate_output.json'),'public_pdf':rec(D/'GI_primary_pdf/S6_SERIES_PUBLISH_Viaclovsky2026Log_v1.pdf')}
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':g['source_sha256'],'guards':[g],'guard_count':1,'literal_edit_count':len(edits),'status':'PREPARED; complete final-pair reading is recorded separately before handback','events_added':0,'canonical_files_modified':False}
q=D/'S6_SERIES_PUBLISH_II_01GI_guards.json';assert not q.exists();q.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'guard':rec(q),'proposed':rec(np),'literal_edits':len(edits)}))
