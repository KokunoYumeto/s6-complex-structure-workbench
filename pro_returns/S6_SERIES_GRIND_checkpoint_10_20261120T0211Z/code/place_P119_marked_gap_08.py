"""Preserve P1.19's proved algebra and place its unresolved geometric map last."""
from pathlib import Path
from collections import Counter
import csv, datetime, hashlib, json, re

R=Path(__file__).resolve().parents[1]
p=R/'parts/V.body.linked.tex'; source=p.read_text(); before=source
start=source.index(r'\begin{theorem}\label{night:P1.19}')
end=source.index(r'\end{proof}',start)+len(r'\end{proof}')
block=source[start:end]
original_block=block
sup=json.loads((R/'audit_p119_fresh/GUARD_SUPERSESSION_09.json').read_text())
old=sup['rollback_guard']['old']; assert block.count(old)==1
block=block.replace(old,'',1)
proof=block[block.index(r'\begin{proof}'):]
replacements=[
 ('\\begin{proof}',r'\begin{proof}[Established calculations and the remaining comparison]'),
 ('This construction fixes the suspension representatives\nused in the Wang complex and is compatible with the based\nproduct-cell comparison in P1.12.',
  'This construction specifies filtered suspension representatives.\nTheir integral comparison with the particular based finite-cap\ndiagram in P1.12 is the remaining obligation described below.'),
 ('Thus the homology maps\nagree with those of the chain map $f_0=(\\kappa,0)$, in every degree.',
  'Thus, in this chosen filtered boundary model, the local cusp\nhomology maps are those of $f_0=(\\kappa,0)$. The global\nmarked-diagram comparison remains to be supplied.'),
 ('Write the degree-four homology gluing map in the plus-sign convention\nas',
  'Write the degree-four gluing map of the displayed algebraic complex\nin the plus-sign convention as'),
 ('the actual global attaching map to the canonical correction',
  'the algebraic attaching map to the canonical correction'),
 ('These formulas prove the chain equivalence; they do not merely\ncompare the ranks of the two complexes.',
  'These formulas give the explicit integral chain equivalence between\nthe stated algebraic complexes.'),
 ('The corrected case\nis the actual global model by the preceding explicit chain\nequivalence.',
  'The resulting algebraic model has the integral chain equivalences\njust displayed. Its geometric identification requires the marked\ncomparison below.'),
 ('This completes the full cellular comparison\nwithout using the global duality conclusion of P1.12.',
  'This completes the integral homology calculation of the explicit\nalgebraic complex. The remaining geometric comparison is stated next.')
]
for old,new in replacements:
    pattern=r'\s+'.join(re.escape(token) for token in old.split())
    matches=list(re.finditer(pattern,proof))
    assert len(matches)==1,(old,len(matches))
    proof=re.sub(pattern,lambda match:new,proof,count=1)
statement=r'''\begin{problem}[The marked global cellular comparison]\label{night:P1.19}
\StatementRecord{night:P1.19}{open}{}{\cref{night:P1.11}, \cref{night:P1.12}, \cref{night:P1.9}; \cite[Theorem~3.43, p.~254]{Hatcher2002}}
Determine the integral comparison between the actual global cellular
diagram and the explicit complex $D_\bullet$ in
\path{code/current_audits/audit_corrections/code/reconstruct_V_global_06.json},
including the based finite-cap and affine-meridian maps. Its algebraic
chain ranks are
\[
 (4,26,87,162,200,156,79,23,3),
\]
and its integral homology has been computed exactly:
\[
 H_k(D_\bullet)=
 \begin{cases}
 \mathbb Z,&k=0,8,\\
 \mathbb Z^4,&k=4,\\
 0,&\text{otherwise}.
 \end{cases}
\]
The local cusp secondary class and the algebraic basis changes below
are established. The integral identification with every map in the
geometric global diagram remains open at the final marked comparison.
The homology of the actual fourfold is independently established in
\cref{night:P1.12}.
\end{problem}
'''
addition=r'''
\paragraph{The exact degree-six correction and the remaining map.}
Orient the original torus by $e_1\wedge\cdots\wedge e_6$ and define
$J(z)(u)=\operatorname{vol}(u\wedge z)$ on five-vectors.
The cooriented torus $H_i=\{x_i=0\}$ has class
$(-1)^{i-1}e_1\wedge\cdots\widehat e_i\cdots\wedge e_6$.
Thus $J$ is an integral isomorphism, $J\bigwedge^5M=M^{-t}J$,
and in the increasing exterior basis
$\mathbf1^tJ=(-1,1,-1,1,-1,1)$.

For a primitive integral covector $l$, subdivide the fundamental cube
by $l(x)\in\mathbb Z$ and give each polyhedron coefficient
$\lfloor l(x)\rfloor$. The resulting integral chain $D_l$ satisfies
\[
 \partial D_l=\sum_i l_iH_i-H_l,\qquad
 \int_{D_l}dx_1\wedge\cdots\wedge dx_6
       ={\sum_i l_i-1\over2}.
\]
The boundary identity follows from the unit jumps on interior cuts
and the differences $l_i$ on opposite cube faces. The integral follows
by subtracting the mean fractional part $1/2$ from the mean
$\sum_i l_i/2$; integration in a coordinate with nonzero integer
coefficient proves the fractional-part formula, including negative
coefficients. For $C(c)=\sum_i c_iH_i$, set
$D_M(c)=\sum_i c_iD_{M^{-t}e_i}$. Then
\[
 \partial D_M(c)=C(M^{-t}c)-M_*C(c),\qquad
 \int D_M(c)\,\omega={1\over2}\mathbf1^t(M^{-t}-I)c.
\]
Adding this chain to the geometric edge prism realizes the minimal
graph differential by an explicit integral polyhedral map.

Let $X$ be the three columns of the invariant five-tori $b_j=0$ in
the original marking, and put
$X_1=-W_{2,5}W_{0,5}X$, $X_2=-W_{0,5}X$.
The actual inverse word gives
\[
 (W_{1,5}-I)X_1+(W_{2,5}-I)X_2=0.
\]
The two volume rows are exactly $(0,-3,0)$ and $(0,3,0)$.
Their sum is zero. The same computation gives
\[
 \eta_i={1\over2}\mathbf1^tJ(W_{i,5}-I),\qquad
 \eta_i\sum_{j=0}^{m_i-1}W_{i,5}^j=0.
\]
All orientation, word, column and norm identities are computed in
\path{code/current_audits/audit_p119_fresh/polyhedral_volume_check.py}
and its JSON output. The geometric invariant-subtorus lifts and these
polyhedral lifts have the same edge coordinates and zero volume;
their difference in the integral fibre summand is therefore zero,
since the marked fibre generator has volume one.

The remaining task is to construct an integral comparison of this
polyhedral realization with the particular finite-cap diagram of
P1.12, including its based affine meridian, and to track $j_Y$ under
that comparison. The row $\eta_1$ has half-integral entries on some
chains, so it is not itself an integral chain automorphism. The norm
and inverse-word identities above establish their stated maps but
leave this diagram adapter unconstructed. Relative cellular
approximation alone did not justify its prescribed fibre coordinate.
The full array-to-array chain isomorphism, including all eight
differential equations, is retained in
\path{code/current_audits/audit_p119_fresh/receiving_chain_adapter.json};
its domain and codomain are the two explicit algebraic complexes.
'''
newblock=statement+proof+addition
source=source[:start]+source[end:]
tail='\\part{Results not yet established}\nThere are no statements in this part.'
assert source.count(tail)==1
source=source.replace(tail,'\\part{Results not yet established}\n\\section{The marked global cellular diagram}\n\n'+newblock,1)
old='P1.19 supplies the requested independent full global cell computation.\nIt proves that the local secondary cusp term is nonzero, gives the\nexplicit integral reduction to the corrected global matrix, and\nrecovers every homology group without global Poincar\\\'e duality.'
new='The final-part problem \\ref{night:P1.19} retains the exact algebraic\ncomplex and local secondary-class calculation. Its integral comparison\nwith the based finite-cap diagram remains open. The actual manifold\nhomology used here is the conclusion of P1.12.'
assert source.count(old)==1; source=source.replace(old,new,1)
assert Counter(re.findall(r'\\(?:tag|label)\{[^}]+\}',source))==Counter(re.findall(r'\\(?:tag|label)\{[^}]+\}',before))
p.write_text(source)

ip=R/'S6_SERIES_GRIND_inventory.csv'
with ip.open() as f:
    reader=csv.DictReader(f); cols=list(reader.fieldnames); rows=list(reader)
selected=[r for r in rows if r['label']=='night:P1.19']; assert len(selected)==1
inventory_before=selected[0].copy(); selected[0]['status']='open'
selected[0]['notes']+=' Current root precision review places the independent geometric-global-complex identification in the final part. The local cusp parity and all displayed algebraic computations remain proved; the exact integral finite-cap/affine-meridian diagram adapter remains open. See analysis/P119_marked_gap_placement_08.json.'
with ip.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)
ap=R/'audit_corrections/row_assessments.json'; assessments=json.loads(ap.read_text()); assessment_before=assessments['night:P1.19']
assessments['night:P1.19']=json.loads((R/'audit_p119_fresh/whole_row_proposal_09.json').read_text())['row']
assessments['night:P1.19']['format_check']='Moved to Results not yet established as an open marked-diagram problem. Every existing formula tag and the proved algebraic/local calculations are retained; the superseded degree-six claim is replaced by the explicit polyhedral calculation and exact remaining adapter. Build and current-page QA pending.'
ap.write_text(json.dumps(assessments,indent=2,ensure_ascii=False)+'\n')
receipt={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'label':'night:P1.19',
 'status_change':{'before':'proved','after':'open'},'source_before_sha256':hashlib.sha256(before.encode()).hexdigest(),
 'source_after_sha256':hashlib.sha256(source.encode()).hexdigest(),'old_block_sha256':hashlib.sha256(original_block.encode()).hexdigest(),
 'new_block_sha256':hashlib.sha256(newblock.encode()).hexdigest(),'inventory_before':inventory_before,
 'assessment_before':assessment_before,'assessment_after':assessments['night:P1.19'],
 'superseded_guard':sup,'preserved':'Every original label and formula tag; S locator, plus-sign correction, full integer computations and local secondary class.',
 'scope':'The independent geometric identification is open. P1.12 separately proves the actual manifold homology; no main fourfold homology theorem is downgraded by this alternative-comparison gap.',
 'pending':'Clean rebuild, regenerated references and actual final-part page inspection.'}
(R/'analysis/P119_marked_gap_placement_08.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'P119':'open in final part','all_labels_and_formula_tags_preserved':True}))
