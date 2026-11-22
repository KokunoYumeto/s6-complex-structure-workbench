from pathlib import Path
import hashlib,json,re,datetime,difflib
r=Path('.');a=r/'agents/ii_infra/recovery_20261121';b=a/'FQ_guard_blocks';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
op=b/'S6_SERIES_PUBLISH_II_01FQ_current_original_full_block.tex';before=op.read_text();assert before.endswith('\\end{proof}\n');before=before[:-1];after=before;ed=[]
def change(old,new,typ,reason):
 global after
 assert after.count(old)==1,(old,after.count(old));at=after.index(old);after=after[:at]+new+after[at+len(old):];ed.append({'before':old,'after':new,'type':typ,'reason':reason,'sequential_before_offset':at})
change(r'label={$\langle1\rangle$\arabic*.}',r'label=\arabic*.','D04','Remove the nonmathematical proof-iteration marker.')
change('Those proofs construct the actual\nlocal spaces and their identifications over the punctured\nbase discs. Thus the normalization of $W$ in each case is\nthe stated smooth rational surface.','These local fillings identify the normalization of $W$ in each case\nwith the stated smooth rational surface.','D08','State the geometric consequence of the cited filling identifications directly.')
change('It requires no surjectivity\nof the global normalization cohomology map. Indeed \\ref{cdp:st:C5b}\ncomputes the actual exceptions to that surjectivity in\nthe original family.','\\ref{cdp:st:C5b} gives the rank of the global normalization\ncohomology map for each integral twist in the original family.','D08/D11','Replace the proof-scope disclaimer with the precise retained mathematical cross-reference.')
change(' This proves \\eqref{cdp:eq:C.TEST.2}.','','D08','Remove the recap after all three Euler contributions have been computed. The complete equation and all its values remain in the statement and the preceding calculation.')
change('\\item Finally the explicit good-reduction covers','\\item The explicit good-reduction covers','D08','Remove the sequencing filler from the mathematical cover argument.')
old=r'''\ref{cdp:st:A.3.4} applies to their actual full fibres, proving the
asserted generic ambient vanishing.'''
new=r'''The full-fibre group in \ref{cdp:st:A.3.4} injects under
pullback by the finite \'etale quotient $\pi:\widetilde U\to U$.
Write $t=u^m$ on this cover, with central torus $T$.
Each Picard component contains a finite-order line bundle $A$:
for a representative $A_0$, choose $N>0$ killing its first Chern class,
write $A_0^N=\exp(\alpha)$, and take $A=A_0\exp(-\alpha/N)$.
For the transgression class $\beta$ of \ref{cdp:st:D.1.9}, put
$A_r=A\exp(2\pi i r\beta)$ with $r$ real and irrational.
The nonzero integral transgression character stays nonzero on the
finite torus cover, since transfer composed with pullback is its
degree. Hence $(\pi^*A_r)|_T$ is a nontrivial unitary line bundle.
The conormal sequence is
\[
 0\longrightarrow\OO_T\,du
 \longrightarrow\Omega^1_{\widetilde U}|_T
 \longrightarrow\OO_T^{\oplus2}\longrightarrow0.
\]
Tensoring it by $(\pi^*A_r)|_T$ gives zero in degree zero.
Every conormal power of $T$ is trivialized by a power of $u$;
induction through the $u$-adic filtration therefore gives
$H^0(mT,(\Omega^1_{\widetilde U}\otimes\pi^*A_r)|_{mT})=0$.
Faithfully flat pullback gives the same vanishing on the full fibre
downstairs. Proper semicontinuity, intersected over the finitely many
multiple values, gives the simultaneous dense open set in every
Picard component.'''
change(old,new,'D25','Correct the unsupported use of the integral-CDP input for |p|>1. The new direct finite-etale torus-cover and full-thickening proof was derived before target release; the original statement is unchanged.')
change(' This is the required test of the proposed additional\nnonreduced-fibre necessity.','','D02/D08','Remove the task-facing closing sentence; all concrete fibre conclusions and Euler identities remain.')
# Exact inverse uses recorded offsets, including empty replacement strings.
back=after
for e in reversed(ed):
 p=e['sequential_before_offset'];assert back[p:p+len(e['after'])]==e['after'];back=back[:p]+e['before']+back[p+len(e['after']):]
assert back==before
pp=b/'S6_SERIES_PUBLISH_II_01FQ_proposed_full_block_draft_v1.tex';assert not pp.exists();pp.write_text(after+'\n')
diff=b/'S6_SERIES_PUBLISH_II_01FQ_full_pair_draft_v1.diff';diff.write_text(''.join(difflib.unified_diff((before+'\n').splitlines(True),(after+'\n').splitlines(True),fromfile=str(op),tofile=str(pp))))
labels=lambda x:re.findall(r'\\(?:label|hypertarget)\{([^}]+)\}',x)
assert labels(before)==labels(after)
assert before[:before.index('\\end{proposition}')]==after[:after.index('\\end{proposition}')]
origdis=re.findall(r'\\\[(.*?)\\\]',before,re.S);newdis=re.findall(r'\\\[(.*?)\\\]',after,re.S)
it=iter(newdis);assert all(any(y==x for y in it) for x in origdis)
refs=lambda x:re.findall(r'\\(?:ref|eqref|cref|Cref|SeriesRef)\{[^}]+\}|\\CompendiumRef\{[^}]+\}\{[^}]+\}',x)
oldrefs=refs(before);newrefs=refs(after);oldrefs.remove(r'\eqref{cdp:eq:C.TEST.2}');newrefs.remove(r'\ref{cdp:st:D.1.9}');assert oldrefs==newrefs
srcsha=json.loads((b/'S6_SERIES_PUBLISH_II_01FQ_current_original_receipt.json').read_text())['source_sha256']
g={'id':'II-infra-recovery-01FQ-publication-draft-v1','statement_id':'cdp:st:C4g','tag':'01FQ','source_sha256':srcsha,'type':'D02/D04/D08/D11/D25','before':before,'after':after,'literal_edits':ed,'original_full_block':str(op),'original_full_block_sha256':sha(op),'proposed_full_block':str(pp),'proposed_full_block_sha256':sha(pp),'reason':'Complete FQ proof comparison, unchanged mathematical statement, direct proof of smooth-multiple vanishing on the actual rational-homology families.','preservation':{'statement_byte_identical':True,'all_labels_and_hypertargets_identical':True,'all_original_displayed_math_in_identical_order':True,'all_original_references_except_exact_named_recap_retained':True,'removed_reference':r'\eqref{cdp:eq:C.TEST.2}','removed_reference_witness':'The full C.TEST.2 table remains in the unchanged statement; proof step4 retains e(W)=2, e(W_i)=0, e(C_cusp)=0.','added_reference':r'\ref{cdp:st:D.1.9}','removed_inline_math':'Only the nonmathematical enumeration iteration marker.','mathematical_statement_changed':False,'proof_input_scope_repaired':True},'unresolved_D06':['Bare E19 in proof step2 has no verified current receiving owner.','CompendiumRef{II}{cdp:st:E19} in proof step3 has no verified current receiving owner.'],'review_status':'Draft complete pair generated; final actual rereading and root receiver audit still pending. No canonical application.'}
out=a/'S6_SERIES_PUBLISH_II_01FQ_guards_draft_v1.json';assert not out.exists();out.write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':srcsha,'guards':[g],'events_added':0,'canonical_mutations':0},indent=2)+'\n')
v=a/'S6_SERIES_PUBLISH_II_01FQ_full_pair_validation_draft_v1.json';v.write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guard':str(out),'guard_sha256':sha(out),'original_full_file_sha256':sha(op),'proposed_full_file_sha256':sha(pp),'literal_edit_count':len(ed),'forward_inverse_exact':True,'statement_byte_identical':True,'labels_tags_identical':True,'original_displays_order_identical':True,'reference_differences_exactly_declared':True,'status':'D06 remains unresolved; no certification or event append.'},indent=2)+'\n')
print(json.dumps({'guards':str(out),'guards_sha256':sha(out),'proposed_block':str(pp),'proposed_sha256':sha(pp),'validation_sha256':sha(v),'literal_count':len(ed)},indent=2))
