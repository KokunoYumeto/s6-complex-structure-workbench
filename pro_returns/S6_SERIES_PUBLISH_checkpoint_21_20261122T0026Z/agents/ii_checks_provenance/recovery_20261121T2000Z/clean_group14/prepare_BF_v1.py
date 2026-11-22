from pathlib import Path
import json,hashlib,re,datetime
R=Path.cwd();D=R/'agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group14'
def b(p):return {'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
p=R/'agents/ii_infra/released_proofs/01BF/d353b72d683f1cf3/S6_SERIES_PUBLISH_full_owning_block.tex';old=p.read_text();src=R/'S6_SERIES_PUBLISH_II.tex';assert src.read_text().count(old)==1
original=D/'S6_SERIES_PUBLISH_II_01BF_original.tex';assert not original.exists();original.write_bytes(p.read_bytes());s=old;guards=[]
def add(typ,a,z,why,n=1):
 global s
 assert s.count(a)==n,(a,s.count(a));guards.append({'change_id':f'II-REC-C14-01BF-{len(guards)+1:02}','defect_type':typ,'old':a,'new':z,'expected_occurrences_in_owning_block':n,'reason':why});s=s.replace(a,z)
add('D08',r'''triple point at every point of $D$;
in particular no degeneration of that type occurs along $D$.''',r'''triple point at every point of $D$.''','Remove the immediate restatement of the retained everywhere-constant transverse type.')
add('D02,D08',r'''In the cusp case the proof constructs, on $C$, the actual
meromorphic cubic on the radical of the Hessian and bounds its
pole divisor by twice the conductor. In the tacnode case the
corresponding fourth-order invariant has poles bounded by four
times the conductor. These intermediate jets need not extend
holomorphically before the conductor correction.''',r'''In the cusp case, the intrinsic cubic on the radical of the Hessian
extends to a meromorphic section on $C$ whose pole divisor is bounded
by twice the conductor. The tacnode fourth-order invariant extends
with poles bounded by four times the conductor.''','State the actual meromorphic-extension conclusions and retain both pole bounds; remove proof narration and the redundant negative extension clause.')
add('D04,D23',r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',r'\begin{enumerate}[label=\arabic*.,leftmargin=*]','Replace iteration labels by ordinary proof-step numbering.')
add('D08',' It is the bundle\nneeded in the following jet calculation.','','Remove the roadmap after the complete definition and exact normalization-pullback description.')
add('D08',r'\item First treat an ordinary cusp. Choose a local defining section',r'\item For an ordinary cusp, choose a local defining section','Keep the mathematical case and choice in one sentence.')
add('D08',r'''\item We now extend precisely this section across $C\setminus
\nu^{-1}(D_{\rm reg})$. Work at a point of $D$ and choose
two generators $X,Y$ of $I$.''',r'''\item At a point of $D$, choose two generators $X,Y$ of $I$.''','The construction is performed at an arbitrary point of D and the subsequent gluing proves the full extension. Remove the preceding announcement without changing the domain or any lift.')
add('D08','where $a=q_{XX}$ is the pullback of an actual coefficient','where $a=q_{XX}$ is the pullback of a coefficient','Remove the process adjective; preserve the exact coefficient and pullback.')
add('D02,D08','This proves the claimed pole control without a splitting of\nthe formal neighbourhood of the singular curve.\n','','Remove the closing proof-status and negative-splitting clauses; the conductor construction and displayed bound remain complete.')
add('D08','times $x$ gives the actual local equation $y^2+x^3=0$.\nThis proves the asserted constant transversal type.','times $x$ gives the local equation $y^2+x^3=0$.','Retain the exact cusp coordinate change and equation; remove the process adjective and closing recap.')
add('D08,D13',r'''\item Next treat an ordinary tacnode. Retain $N,M,R,Q,q,a,h,d,P$
from the cusp calculation, with
$P=\widehat d X+\widehat{dh}Y$ and
$G=\widehat d^{\,2}f-\widehat aP^2\in I^3$.''',r'''\item In the tacnode case, put $P=\widehat d X+\widehat{dh}Y$ and
$G=\widehat d^{\,2}f-\widehat aP^2\in I^3$.''','Introduce P exactly where it is first named; all earlier bundles and coefficients retain their definitions. Remove the inaccurate instruction to retain a previously unnamed P.')
add('D08','an actual holomorphic quadratic $C_2$','a holomorphic quadratic $C_2$','Remove the process adjective from the explicit polynomial-division result.')
add('D08',r'''produces the actual equation $y^2+x^4=0$ at every point of
$D$. This proves the tacnode assertion.''',r'''produces the equation $y^2+x^4=0$ at every point of $D$.''','Retain the exact equation and its every-point quantifier; remove the process adjective and recap.')
add('D08','is an honest global section','is a global section','Remove the process adjective; preserve the global section and its bundle.')
q=D/'S6_SERIES_PUBLISH_II_01BF_proposed_v1.tex';assert not q.exists();q.write_text(s)
display=lambda z:re.findall(r'\\\[(.*?)\\\]',z,re.S)
tags=lambda z:re.findall(r'\\(?:label|tag|hypertarget)\{[^}]*\}',z)
assert display(old)==display(s);assert tags(old)==tags(s)
code=D/'S6_SERIES_PUBLISH_II_BF_prereading_invariant_certificate.py'
row=r'Binary-cubic exterior-product discriminant, tacnode quadratic-form congruence and conductor-clearing identities (\cref{cdp:st:A.5.5}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/S6_SERIES_PUBLISH_II_BF_prereading_invariant_certificate.py}{\nolinkurl{S6_SERIES_PUBLISH_II_BF_prereading_invariant_certificate.py}} \\[3pt]'
a={'schema_version':1,'paper':'II','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checker':'i_provenance_recovery','source_at_preparation':b(src),'targets':[{'tag':'01BF','statement_owner':'cdp:st:A.5.5','original_full_block':b(original),'proposed_full_block':b(q),'guards':guards,'all_original_display_math_unchanged':True,'all_labels_tags_hypertargets_unchanged':True,'mathematical_statement_and_values_unchanged':True}],'program_table_entry_proposal':{'code':b(code),'output':b(D/'S6_SERIES_PUBLISH_II_BF_prereading_invariant_output.json'),'execution_receipt':b(D/'S6_SERIES_PUBLISH_II_BF_prereading_execution_receipt.json'),'proposed_code_copy_path':'code/'+code.name,'exact_row':row,'scope':'Root may append this once to the current Programs table and bind byte-identical code/output/receipt copies. No canonical table change has been made.'},'canonical_mutations':False,'events_added':0,'full_proposed_reading_pending':True}
p=D/'S6_SERIES_PUBLISH_II_clean_group14_BF_preparation_v1.json';assert not p.exists();p.write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'preparation':b(p),'guards':len(guards),'proposed':b(q)}))
