#!/usr/bin/env python3
from pathlib import Path
import sys,json,hashlib,re,datetime
D=Path(__file__).resolve().parent;ROOT=D.parents[2]
sys.path.insert(0,str(ROOT/'code'))
from S6_SERIES_PUBLISH_II_packets import parse_source
src=parse_source(ROOT/'S6_SERIES_PUBLISH_II.tex','II');source=src['text']
folder=D/'SX_033C_033O_blocks';folder.mkdir(exist_ok=True)
sha=lambda s:hashlib.sha256(s if isinstance(s,bytes) else s.encode()).hexdigest()
guards=[]

def owning(label):
    a=src['statement_labels'][label]
    return source[a['start']:max([a['end']]+[z['end'] for z in a['proofs']])]

def save(tag,label,old,edits,reason,preservation):
    new=old;steps=[]
    for before,after,kind,why in edits:
        assert new.count(before)==1,(tag,before,new.count(before))
        at=new.index(before);new=new[:at]+after+new[at+len(before):]
        steps.append({'before':before,'after':after,'type':kind,'reason':why,'sequential_before_offset':at})
    inverse=new
    for step in reversed(steps):
        a=step['sequential_before_offset'];b=step['after'];assert inverse[a:a+len(b)]==b
        inverse=inverse[:a]+step['before']+inverse[a+len(b):]
    assert inverse==old
    assert source.count(old)==1
    for cmd in ['label','hypertarget']:
        assert re.findall(r'\\'+cmd+r'\{([^}]+)\}',old)==re.findall(r'\\'+cmd+r'\{([^}]+)\}',new)
    for suffix,t in [('before',old),('after',new)]:
        (folder/f'S6_SERIES_PUBLISH_II_{tag}_{suffix}.tex').write_text(t)
    g={'id':'II-infra-recovery-'+tag,'tag':tag,'statement_id':label,'source_sha256':src['sha256'],
       'before':old,'after':new,'type':'/'.join(sorted(set(k for e in steps for k in e['type'].split('/')))),
       'reason':reason,'literal_edits':steps,
       'original_full_block':str((folder/f'S6_SERIES_PUBLISH_II_{tag}_before.tex').relative_to(ROOT)),
       'original_full_block_sha256':sha(old),
       'proposed_full_block':str((folder/f'S6_SERIES_PUBLISH_II_{tag}_after.tex').relative_to(ROOT)),
       'proposed_full_block_sha256':sha(new),
       'comparison_record':str((D/'S6_SERIES_PUBLISH_II_SX_033C_033O_comparison.json').relative_to(ROOT)),
       'preservation':{'exact_forward_and_inverse':True,'all_labels_and_hypertargets_identical':True,**preservation},
       'mathematical_statement_scope_changed':False}
    guards.append(g)

old=owning('inv:E2.4');proof=old[old.index('\\begin{proof}'):]
newproof=r'''\begin{proof}
Proposition~\ref{inv:E2.2} gives $h^0(T_{X_m})=2m+1\ge25$ for $m\ge12$.
In the proof of \citet[Corollary~1.3, preprint p.~2]{HKP2000},
a third field is expressed as a meromorphic linear combination of two fields;
the coefficients are then declared constant using the
Campana--Demailly--Peternell assertion about meromorphic functions on a
complex six-sphere. For the combs, the surjective algebraic reduction
$f_m$ induces an injection $f_m^*:\C(t)\hookrightarrow\mathcal M(X_m)$,
so its pullback of $t$ is nonconstant.
\end{proof}'''
edits=[]
for occurrence in ['\\StatementRecord{inv:E2.4}{proved}{01SX}{\\SeriesRef{inv:E2.2}; \\citet[Corollary 1.3; verified preprint p.~2]{HKP2000}; \\citet[Remarks 1.2 and 9.26]{AC2026}}',
                   '\\citet[Corollary 1.3; verified preprint p.~2]{HKP2000}\nand repeated']:
    edits.append((occurrence,occurrence.replace('Corollary 1.3; verified preprint','Corollary~1.3, preprint'),'D08/D18','Remove verification-status prose and use the precise cited preprint locator.'))
edits.append((proof,newproof,'D04/D06/D08/D11','Replace the one-item iteration wrapper by the direct argument, retain the published-error diagnosis with its exact citation, and exhibit the pullback injection; remove the closing recap and neighbouring-scope disclaimer.'))
save('01SX','inv:E2.4',old,edits,'State the published counterexample and its exact source diagnosis directly.',{
 'numerical_counterexample_preserved':'h^0(T_Xm)=2m+1>=25 for m>=12 is unchanged. The removed second 2m+1 mention repeated this same witness.',
 'new_exact_map':'Surjectivity of f_m gives the displayed injective pullback of rational functions; the primary comb theorem states that f_m is the algebraic reduction.',
 'primary_diagnosis':'HKP v1, Corollary 1.3 and its complete proof, actual PDF page 2, have been opened after target release.',
 'removed_scope_sentence':'The statement only refutes the universal bound; the deleted algebraic-dimension-zero disclaimer adds no assertion needed to obtain the counterexample.'})

old=owning('push:src:E.2.4');proof=old[old.index('\\begin{proof}'):]
newproof=r'''\begin{proof}
Replacing the analytic base by its reduction preserves its underlying
topological space and every complex fibre, as well as properness and
smoothness of the family. Theorem~\ref{push:src:E.2.23} therefore makes
the ordered multiplicity pair constant throughout each connected family.
At each join in a finite chain, the common member has the pair of both
adjacent families, so the pair is constant along the chain. The converse
for two constructed members with the same pair is also part of that theorem.

By Corollary~\ref{push:src:E.2.24}, the locus in the $C^\infty$ space of
integrable complex structures corresponding to a fixed pair is open and
closed. Its inverse image under a continuous family is open and closed
in the connected parameter space; if it contains one parameter, it
contains every parameter.
\end{proof}'''
save('033C','push:src:E.2.4',old,[(proof,newproof,'D02/D04/D06/D08/D12','Replace the repeated roadmap and defensive methodological caveats by the exact corollary deduction; explicitly handle reduction of the base.')],
 'Give the proof of the corollary from the two cited separation statements, including nonreduced analytic bases.',{
 'statement_identical':True,
 'removed_roadmap_references':['push:src:E.2.5','push:src:E.2.21','push:src:E.2.22'],
 'retained_operating_inputs':['push:src:E.2.23','push:src:E.2.24'],
 'reference_map':'E.2.23 supplies constancy and the complete chain equivalence; E.2.24 supplies the clopen locus. The deleted E.2.5/E.2.21/E.2.22 summary describes the upstream proof of those retained inputs and is not a further hypothesis of this corollary.',
 'new_base_change_map':'X x_B B_red -> B_red has exactly the same point fibres; connectedness, properness and smoothness are preserved as detailed in the prerelease derivation.',
 'no_claim_of_global_inline_or_reference_identity':True})

old=owning('push:src:E.5.2')
edits=[
 (r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',r'\begin{enumerate}[leftmargin=*]','D04','Remove the historical proof-iteration prefix.'),
 ('\\item \n\\noindent\\textbf{Step 1.} The matrices are Proposition 4.2 of \\cite{ViaTwo26push}, whose','\\item The matrices are those of \\citet[Proposition~4.2]{ViaTwo26push}, whose','D04/D18/D23','Use the published locator and remove a duplicate step heading.'),
 ('the initially undetermined winding integer by the saturation\nindex $d^2=1$, rather than assuming this winding from the\ndesired topology.','the winding integer by the saturation index $d^2=1$.','D02/D08','Retain the mathematical determination and remove the defensive contrast.'),
 ('For clarity the homological matrices used in our calculation are','The dual homology matrices are','D08','State the displayed objects directly.'),
 ('gives $C=aI+bE_{41}$ with free $a,b$; the retained exact\nrow-reduction program displays a basis and verifies its\ndimension two.  Inverse transpose gives the stated\ncohomological centralizer.','gives $C=aI+bE_{41}$ with free $a,b$. Transposition gives the\nlinear bijection between the two centralizers: the equation\n$CH_i=H_iC$ is equivalent to $C^tT_i=T_iC^t$, and\n$E_{41}^t=E_{14}$.','D09/D25','Keep the rational row-reduction result in the proof and replace the undefined inverse-transpose operation on singular centralizer elements by the correct linear transpose map.'),
 ('Each $K_i$ is the actual integral image of','Each $K_i$ is the integral image of','D08','Remove the process contrast while preserving the integral assertion.'),
 ('lattices.  All products, rational row reductions, Hermite forms,\nand Smith forms are executed in\n\\texttt{code/e\\_push\\_two\\_parameter.py}.','lattices.','D09','Move the pinned program citation and its computation scope to the single end table.')]
save('033O','push:src:E.5.2',old,edits,'Preserve every matrix and lattice, clarify the exact centralizer transport, and move the program reference to the end table.',{
 'every_display_identical':True,
 'D25_exact_error_scope':'Inverse transpose is undefined at singular centralizer elements such as E41. Transposition is the required linear bijection on the entire rational matrix algebra centralizers; the theorem and all lattice conclusions remain unchanged.',
 'new_commuting_map':'C maps to C^t; CH_i=H_iC iff C^t T_i=T_i C^t using H_i=T_i^{-t}; inverse is transposition.',
 'fresh_and_prior_computation':'Prerelease Fraction computation and exact postrelease formal-polynomial check agree with the pinned SymPy monodromy/lattice slice; precise ordering maps are recorded separately.'})

# The full current table is archived; this guard only appends one positively verified source.
at=source.index(r'\label{tab:II:programs}');a=source.rfind(r'\begin{longtable}',0,at);b=source.index(r'\end{longtable}',at)+len(r'\end{longtable}');old=source[a:b]
row=r'''Integral monodromy matrices, rational centralizers, fixed lattices, norm lattices and primitive vanishing cycles (\cref{push:src:E.5.2}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/pro_returns/S6_02_PUSH_final_20261115T2217Z/S6_02_PUSH/code/e_push_two_parameter.py}{\nolinkurl{e_push_two_parameter.py}} \\[3pt]
'''
save('033O_program_table','tab:II:programs',old,[(r'\end{longtable}',row+r'\end{longtable}','D09','Add the once-per-computation source link at the pinned commit; only positively fetched source bytes are cited.')],
 'Move the old program citation out of the proof and bind its exact computational scope to the verified source file.',{'all_existing_rows_verbatim':True,'program_receipt':str((D/'S6_SERIES_PUBLISH_II_033O_prior_program.json').relative_to(ROOT)),'program_sha256':'5ad9d8627cc7b88cbe4d92d18314b13be07188f6b0e5b409dc9b20d4bf17c312','read_and_executed_scope':'Only the complete monodromy/lattice slice, lines 1–43; no execution of later classification computations is asserted.'})

# The existing journal/DOI fields remain verbatim; pin the edition used for page 2.
m=next(m for m in re.finditer(r'\\bibitem(?:\[[^\n]*\])?\{([^}]+)\}',source) if m.group(1)=='HKP2000');a=m.start();b=source.find('\\bibitem',m.end());old=source[a:b]
before='\\newblock URL \\url{https://arxiv.org/abs/math/9812076}.\n\\newblock \\emph{Verified}.'
after='\\newblock URL \\url{https://arxiv.org/abs/math/9812076v1}.\n\\newblock Cited preprint edition: arXiv:math/9812076v1, 13 December 1998;\npreprint page locators refer to this edition.'
save('HKP2000','bib:HKP2000',old,[(before,after,'D08/D18','Pin the actual preprint edition used by the proof locator and remove verification-status prose.')],
 'Keep the published journal and DOI data while explicitly identifying the cited preprint page edition.',{'citation_key_authors_title_journal_doi_identical':True,'primary_receipt':str((D/'SX_033C_033O_primary_inputs/S6_SERIES_PUBLISH_II_HKP_v1_receipt.json').relative_to(ROOT))})

for g in guards:
    if g['tag']=='033O':
        assert re.findall(r'\\\[(.*?)\\\]',g['before'],re.S)==re.findall(r'\\\[(.*?)\\\]',g['after'],re.S)
out=D/'S6_SERIES_PUBLISH_II_SX_033C_033O_guards.json'
out.write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':src['sha256'],'guards':guards,'guard_count':len(guards),'literal_edit_count':sum(len(g['literal_edits']) for g in guards),'status':'Prepared only; actual complete proposed-block reading is recorded separately.','events_added':0,'canonical_files_modified':False},indent=2)+'\n')
print(json.dumps({'path':str(out.relative_to(ROOT)),'sha256':sha(out.read_bytes()),'source_sha256':src['sha256'],'guards':len(guards),'literal_edits':sum(len(g['literal_edits']) for g in guards)}))
for g in guards:
    print('\nCOMPLETE PROPOSED BLOCK '+g['tag']+'\n'+g['after'])
