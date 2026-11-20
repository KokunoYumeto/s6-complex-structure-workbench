"""Prepare exact P1.19 source guards without editing a shared source.

The proposed theorem status is for root review and later integration only.
This producer reads the current root-owned source and writes only here.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re

HERE=Path(__file__).parent
ROOT=HERE.parent.parent
src_path=ROOT/'parts/V.body.linked.tex'
src=src_path.read_text()
marker='\\clearpage\n\\part{Results not yet established}\n\\section{The marked global cellular diagram}\n\n'
assert src.count(marker)==1
old_final=src[src.index(marker):]
assert old_final.count('\\label{night:P1.19}')==1
start=old_final.index('\\begin{proof}[Established calculations and the remaining comparison]')
end=old_final.index('\\end{proof}',start)+len('\\end{proof}')
old_proof=old_final[start:end]
items=re.split(r'(?m)^\\item ',old_proof)[1:]
assert len(items)==13,len(items)
cusp_item='\\item '+items[1]
tail=''.join('\\item '+x for x in items[6:])
replacements={
 'We next give the integral equivalence which reduces every class\nsatisfying (1.19.4) to one displayed matrix.  Write the degree-four gluing map of the displayed algebraic complex\nin the plus-sign convention as':
 'We next give the integral equivalence which reduces the actual class\nsatisfying (1.19.4) to one displayed matrix. Write the degree-four\ngluing map after the preceding marked comparison and shears, in the\nplus-sign convention, as',
 'the algebraic attaching map to the canonical correction':
 'the actual transferred attaching map to the canonical correction',
 'These formulas give the explicit integral chain equivalence between\nthe stated algebraic complexes.':
 'Together with the geometric comparison and the preceding suspension\nshears, these formulas give the explicit integral chain equivalence\nfrom the actual gluing diagram to the stated full complex.',
 'over $\\mathbb Z$ and exports every differential.  The resulting algebraic model has the integral chain equivalences\njust displayed. Its geometric identification requires the marked\ncomparison below.':
 'over $\\mathbb Z$ and exports every differential. The geometric\nsource and target comparisons, the actual finite-cap homotopies,\nthe cusp inverse-word homotopy, and the integral suspension and\nsecondary-class reductions above identify this full complex with\nthe actual global cellular chains.',
 'relative torsion retains the distinction needed in item~9.':
 'relative torsion is the obstruction measured in (1.19.4).',
 'and its JSON output.  This completes the integral homology calculation of the explicit\nalgebraic complex. The remaining geometric comparison is stated next.':
 'and its JSON output. The separate fresh-to-receiving integral\nchain isomorphism, including every differential equation, is retained\nin \\path{code/current_audits/audit_p119_fresh/receiving_chain_adapter.json}.\nThe actual polyhedral source maps, finite-cap transports and\nfree-word homotopy coefficients are specified in\n\\path{code/current_audits/audit_p119_fresh/comparison_09/geometric_diagram_check_02.py}\nand its JSON output; the full numerical $S_Y,U_0$ and cone adapters\nare in \\path{code/current_audits/audit_p119_fresh/comparison_09/top_chain_adapter.json}.\nThese respectively check the stated 154 geometric-diagram identities,\n113 top-adapter identities and the earlier 140 array-comparison\nidentities at their recorded scopes. The chain construction above\nprovides their geometric identification. This completes the integral\nglobal calculation without using global Poincare duality or the\nhomology conclusion of P1.12.'
}
for old,new in replacements.items():
    assert tail.count(old)==1,old
    tail=tail.replace(old,new,1)

header=r'''\begin{theorem}[The full marked global cellular complex]\label{night:P1.19}
\StatementRecord{night:P1.19}{proved}{}{\cref{night:P1.11}, \cref{night:P1.12}, \cref{night:P1.9}; \cite[Theorem~3.43, p.~254]{Hatcher2002}}
The actual global cellular diagram has an integral chain-homotopy
equivalence with the full complex whose chain ranks in degrees zero
through eight are
\[
 (4,26,87,162,200,156,79,23,3)
\]
and whose differentials are the matrices in
\path{code/current_audits/audit_corrections/code/reconstruct_V_global_06.json}.
The marked comparison below includes the actual finite norm maps,
the based affine meridians, the cusp inverse-word map and its
secondary chain term. Its integral Smith calculation gives
\[
 H_k(M;\mathbb Z)=
 \begin{cases}
 \mathbb Z,&k=0,8,\\
 \mathbb Z^4,&k=4,\\
 0,&\text{otherwise}.
 \end{cases}
\]
The calculation uses local Poincar\'e--Lefschetz duality of the
actual smooth cusp cap. It uses neither global Poincar\'e duality
nor the homology conclusion of P1.12. The full-zero cusp suspension
map has the explicit relative torsion obstruction identified below;
the actual secondary term is retained.
\end{theorem}
\begin{proof}
\begin{enumerate}[label=\arabic*.]
'''
core=(HERE/'P119_GEOMETRIC_CORE_02.tex').read_text()
proposal=header+cusp_item+core+tail+'\n'
assert proposal.count('\\begin{proof}')==proposal.count('\\end{proof}')==1
assert proposal.count('\\begin{enumerate}')==proposal.count('\\end{enumerate}')==1
for j in range(1,9):assert proposal.count('\\tag{1.19.'+str(j)+'}')==1,j
assert 'remains open' not in proposal
assert 'remaining geometric comparison' not in proposal
(HERE/'P119_PROPOSED_COMPLETE_02.tex').write_text(proposal)

anchor='\\section{The genus-two pencil and the lifted period planes}'
assert src.count(anchor)==1
diag_start=src.index('\\paragraph{The retained diagnostic complex.}')
diag_end=src.index('\\begin{theorem}\\label{night:P1.13}',diag_start)
old_diag=src[diag_start:diag_end]
new_diag=r'''\paragraph{The retained diagnostic complex.}
The earlier file \texttt{global\_candidate\_complex.py} sets the entire
cusp suspension map to zero and has the same free Betti numbers.
That file and its output remain a diagnostic record.
Theorem~\ref{night:P1.19} supplies the full actual marked cellular
comparison and its local secondary term. Its relative cusp
calculation identifies the omitted torsion extension explicitly.
The actual manifold homology used here is also established in P1.12.

'''
guards=[
 {'id':'p119_remove_superseded_final_open_block','old':old_final,'new':'','expected_occurrences':1,
  'reason':'Remove the superseded open-problem block and its now-vacant final-part heading only after root accepts the complete replacement.'},
 {'id':'p119_insert_complete_marked_proof','old':anchor,'new':proposal+'\n\n'+anchor,'expected_occurrences':1,
  'reason':'Restore the permanent theorem and all original formula tags in its integral-topology position, with the full actual diagram construction and retained algebra.'},
 {'id':'p119_update_diagnostic_cross_reference','old':old_diag,'new':new_diag,'expected_occurrences':1,
  'reason':'Replace the stale open-gate reference with the precise completed-comparison statement in the proposed integrated source.'}
]
preview=src
for guard in guards:
    assert preview.count(guard['old'])==guard['expected_occurrences'],guard['id']
    guard['old_sha256']=hashlib.sha256(guard['old'].encode()).hexdigest()
    guard['new_sha256']=hashlib.sha256(guard['new'].encode()).hexdigest()
    preview=preview.replace(guard['old'],guard['new'],1)
assert preview.count('\\label{night:P1.19}')==1
assert preview.count('\\StatementRecord{night:P1.19}{proved}')==1
assert '\\StatementRecord{night:P1.19}{open}' not in preview
for j in range(1,9):assert preview.count('\\tag{1.19.'+str(j)+'}')==src.count('\\tag{1.19.'+str(j)+'}')==1
report={'utc':datetime.now(timezone.utc).isoformat(),'path':'parts/V.body.linked.tex','target_label':'night:P1.19',
 'status':'PROPOSAL ONLY. Root and receiving review pending. No shared source or canonical assessment changed.',
 'source_before_sha256':hashlib.sha256(src.encode()).hexdigest(),
 'in_memory_after_sha256':hashlib.sha256(preview.encode()).hexdigest(),
 'complete_proposal_path':'audit_p119_fresh/comparison_09/P119_PROPOSED_COMPLETE_02.tex',
 'complete_proposal_sha256':hashlib.sha256(proposal.encode()).hexdigest(),
 'guards':guards,'dry_run_checks':'All3 guards match once; permanent label and all8 original formula tags retained exactly once; source only transformed in memory.'}
(HERE/'P119_SOURCE_GUARDS_02.json').write_text(json.dumps(report,indent=2)+'\n')
receipt={'utc':report['utc'],'scope':report['status'],'source_guard_dry_run':report['dry_run_checks'],
 'files':{p.name:{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in [HERE/'P119_GEOMETRIC_CORE_02.tex',HERE/'P119_PROPOSED_COMPLETE_02.tex',HERE/'P119_SOURCE_GUARDS_02.json',Path(__file__)]}}
(HERE/'SOURCE_PROPOSAL_RECEIPT_02.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
