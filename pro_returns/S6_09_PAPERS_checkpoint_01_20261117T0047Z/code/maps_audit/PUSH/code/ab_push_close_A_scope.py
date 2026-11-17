"""One-time integration of root-refereed A.2.5 and A.4.9.

Superseded scope passages are retained verbatim in evidence.
"""
from pathlib import Path
import re,csv

root=Path(__file__).resolve().parents[1]
texpath=root/'sections'/'AB_push.tex'
tex=texpath.read_text()
replacement={
'A.2.3':r'''\begin{remark}[A.2.3; Refuted; the literal blow-up shape]\label{push:A23}
The unrestricted request that every normalized component
be a blow-up of $R$ is false. The first maximal-cone
star already contributes a $\mathbb P^3$ component,
which admits no proper bimeromorphic map to $R$, since
such a map would inject a rank-eleven rational $H^2$
into a rank-one group. A.2.4 gives every normalization
by explicit star charts; A.2.5 supplies the terminating
blow-up and blow-down algorithm with centres, order,
exceptional bundles and gluing maps. Thus the literal
shape is refuted and its general algorithmic
replacement is proved.
\end{remark}''',
'A.4.5':r'''\begin{corollary}[A.4.5; Proved; unrestricted toroidal topology]\label{push:A45}
For every output of A.2.4, A.4.7--A.4.9 determine the
Euler number, fundamental group, all integral homology
groups with torsion, nearby Euler function and marked
monodromy. The integral normalization computation is
given by the finite algorithm and the primitive
central pushforward matrices of A.4.9; the independent
ambient computation is A.4.8, and the torus-stratum
Euler count is A.4.7. The non-K\"ahler limitation on
classical Clemens--Schmid is the explicit one in
A.4.4; no polarized limiting Hodge structure is
asserted.
\end{corollary}''',
'B.2.2':r'''\begin{corollary}[B.2.2; Proved; general plain-cusp normalization]\label{push:B22}
For $n=2$ and $n=12$, A.2.4--A.2.5 give all
finite-orbit smooth invariant plain-cusp refinements,
their proper flat families, normalization charts,
finite blow-up and blow-down presentations,
multiplicities and all multiple loci. A.4.7--A.4.9
give their complete integral topology and nearby
Euler function. These statements concern the plain
untwisted cusp. They assert no compatibility with
the finite logarithmic-transform pieces of B.1.
\end{corollary}'''
}
retained=[]
for ident,new in replacement.items():
    pattern=r'\\begin\{problem\}\['+re.escape(ident)+r';[\s\S]*?\\end\{problem\}'
    found=re.findall(pattern,tex)
    assert len(found)==1,(ident,len(found))
    retained.append('## '+ident+' (superseded after root referee)\n\n```latex\n'+found[0]+'\n```\n')
    tex=tex.replace(found[0],new)
anchor=r'\subsection{A.3. The virtual Euler obstruction and the conjecture}'
assert tex.count(anchor)==1
tex=tex.replace(anchor,r'\input{sections/ab_push_normalization_algorithm}'+'\n\n'+anchor)
anchor=r'\input{sections/ab_push_all_fan_homology}'
assert tex.count(anchor)==1
tex=tex.replace(anchor,anchor+'\n'+r'\input{sections/ab_push_central_pushforward}')
texpath.write_text(tex)
(root/'evidence'/'ab_push_superseded_scope_passages.md').write_text(
    '# Superseded scope passages, retained verbatim\n\n'
    'A.2.3 was replaced by a proved refutation and the stronger finite normalization algorithm. '
    'A.4.5 was completed by the central-space sheaf and normalization computation. '
    'B.2.2 is the corresponding substitution n=2,12. Root independently refereed '
    'A.2.5 and A.4.9; boundary_d did not referee these two supplements.\n\n'+'\n'.join(retained))

catalogue=root/'code'/'ab_push_catalogue.py'
lines=catalogue.read_text().splitlines()
newrows={
'A.2.3':"('A.2.3','A universal normalization as blow-ups of R is false; the first point star has a P3 component, while A.2.5 gives the terminating correct blow-up/down algorithm.','Refuted','A.2.4; A.2.5; A.4.6','A.2','Lead 2(ii)-(iii)','No proper bimeromorphic map P3 to R can inject rank11 H2 into rank1; no unrestricted pure-blow-up claim is retained.'),",
'A.4.5':"('A.4.5','All toroidal central topology and nearby data are computed, with an integral normalization-stratification route and an independent ambient route.','Proved','A.2.4; A.4.7; A.4.8; A.4.9','A.4','Lead 2(iii)','The finite normalization algorithm and unit Gysin matrices close the second-computation scope; classical Kahler Clemens-Schmid remains explicitly inapplicable, as in A.4.4.'),",
'B.2.2':"('B.2.2','For n=2 and12 all plain-cusp normalized components, multiplicities, multiple loci and finite blow-up/down presentations are algorithmic; full integral topology is determined.','Proved','A.2.4; A.2.5; A.4.7; A.4.8; A.4.9','B.2','Lead 2; Lead 5','Plain untwisted cusp only; no compatibility with finite logarithmic-transform pieces is inferred.'),"
}
for ident,new in newrows.items():
    hit=[i for i,line in enumerate(lines) if line.startswith("('"+ident+"',")]
    assert len(hit)==1
    lines[hit[0]]=new
catalogue.write_text('\n'.join(lines)+'\n')

fields=['id','statement','status','where_proved','depends_on','item_of_the_prompt','R_items_and_Leads_used','notes']
rows=[
 ['A.2.5','Every fan certificate has a terminating explicit normalization and birational-comparison algorithm by smooth strata blow-ups/down; a universal blow-up-of-R shape is false and the nonreduced deformation sheaf is the cotangent-complex Jacobian quotient.','Proved','sections/ab_push_normalization_algorithm.tex, A.2.5','A.2.4; A.4.6; A.4.8','A.2; B.2','Lead 2','Root independently refereed. Exact two-step search, inverse moves and720 local chart substitutions passed; no strong factorization is assumed.'],
 ['A.4.9','The central pushforward of every star blow-up splits integrally as the old constant complex plus shifted centre-support complexes; the explicit normalization matrices give the second complete central homology computation.','Proved','sections/ab_push_central_pushforward.tex, A.4.9','A.2.5; A.4.7; A.4.8','A.4; B.2','Lead 2','Root independently refereed. All36 local projective-subspace normalization row complexes have primitive Smith factors1. The global maps are proved by exceptional Gysin and proper base change.']
]
with (root/'sections'/'ab_push_A_completion_results.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(fields);w.writerows(rows)

report=root/'sections'/'AB_push_report.md'
t=report.read_text()
t=t.replace('A uniform conversion of every normalization into the requested blow-up description remains open.',
            'The literal requirement that all normalized components be blow-ups of R is refuted; a terminating explicit blow-up/down algorithm supplies the correct general description.')
t=t.replace('| A.2.1–A.2.4; A.4.6 |','| A.2.1–A.2.5; A.4.6 |')
t=t.replace('The formula uses integral reference maps and toroidal weak factorization. A second direct normalization-stratification chain computation for every arbitrary fan remains a verification task.',
            'The integral reference/factorization computation and the independent central normalization-stratification computation agree; every local matrix has a primitive integral splitting.')
t=t.replace('| A.4.1–A.4.8 |','| A.4.1–A.4.9 |')
t=t.replace('Uniform blow-up normalizations and a second direct integral chain computation remain to be supplied.',
            'The explicit normalization algorithm and second central integral computation are now proved.')
t=t.replace('| B.2.1–B.2.3; A.2.4; A.4.7–A.4.8 |','| B.2.1–B.2.3; A.2.4–A.2.5; A.4.7–A.4.9 |')
t=t.replace('A uniform blow-up presentation and a second direct integral incidence computation for every arbitrary output remain to be supplied.',
            'A.2.5 supplies a terminating blow-up/down algorithm and refutes the literal blow-up-of-R shape. A.4.9 supplies the second integral normalization-stratification computation for every input fan.')
t=t.replace('The direct normalization/stratification incidence matrices of every arbitrary fan remain a second-computation task.',
            'A.4.9 now completes the second computation by central proper pushforward and the explicit ordered-branch/projective-subspace matrices. The root agent independently refereed A.2.5 and A.4.9.')
t += '\n\n## Completion of the toroidal A/B2 scope\n\nA.2.5 and A.4.9 complete the normalization-algorithm and second-integral-computation requirements. The three former Open scope passages are retained verbatim in `evidence/ab_push_superseded_scope_passages.md`, with their replacement rationale. The new scripts are `ab_push_normalization_algorithm.py` (two-star search, inverse contractions,720 exact local substitutions) and `ab_push_central_pushforward.py` (all36 local normalization row complexes). Their outputs and JSON data are saved. The latter initially passed its mathematical checks but failed JSON serialization of a SymPy integer; `ab_push_central_pushforward_initial_failure.out` preserves the output and diagnosis, and the corrected run passes. A partial-line text patch during the cotangent-complex wording correction also failed validation before changing files. No mathematical claim was changed by either implementation correction.\n\nB.4.6 separately excludes the specified affine-torsor horizontal block plus hyperbolic toric Kato caps with invariant or rational overlaps. Its proof and original-source hypotheses were independently checked by boundary_d. This is a restricted additional obstruction; the existence of an arbitrary analytic S6 cap remains open.\n'
report.write_text(t)
print('Integrated A.2.5/A.4.9; retained3 former scope passages; wrote2 new statement rows.')
print('A.2.3 Refuted; A.4.5 Proved; B.2.2 Proved. Main B filling remains Open.')
