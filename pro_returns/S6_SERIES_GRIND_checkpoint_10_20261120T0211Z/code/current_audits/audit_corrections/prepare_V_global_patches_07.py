from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

root=Path(__file__).parent.parent
body_path=root/'parts/V.body.linked.tex'
body=body_path.read_text()
global_data=json.loads((Path(__file__).parent/'code/reconstruct_V_global_06.json').read_text())
# These unchanged bridge matrices were already verified in the retained
# 756-check run; the current extended verifier additionally checks local
# relative homology and the unused even diagnostic.
bridge_path=Path(__file__).parent/'code/verify_V_global_saved_07_pass756.json'
bridges=json.loads(bridge_path.read_text())['homology_basis_bridges']
patches=[]
def add(label,old,new,reason):
    assert body.count(old)==1,(label,old[:100],body.count(old))
    assert old!=new
    patches.append({'label':label,'old_text':old,'new_text':new,'reason':reason})
def span(start,end):
    a=body.index(start);b=body.index(end,a)+len(end)
    return body[a:b]
def pm(M):
    return '\\begin{pmatrix}\n'+'\\\\\n'.join('&'.join(str(x) for x in row) for row in M)+'\n\\end{pmatrix}'
path=r'\path{code/current_audits/audit_corrections/code/}'

add('night:P1.12',span('The explicit conjugators were found in the bounded search','\\texttt{finite\\_permutation\\_models.py}.'),r'''The displayed conjugators are checked by exact multiplication in
\path{code/current_audits/audit_corrections/code/independent_V_topology_inputs_07.py}.
Its JSON output records the actual split bases, the two signed
permutation matrices and their cycles: one positive five-cycle, and
one positive four-cycle together with a negative fixed coordinate.''',
    'Replace the unavailable historical execution assertion by the fresh 33-check calculation of these exact displayed conjugators.')

add('night:P1.12',span('The full arrays are exported to \\texttt{complement\\_export.json}; its','decompositions.'),r'''The full arrays are reconstructed and exported in
\path{code/current_audits/audit_corrections/code/reconstruct_V_global_06.json}
by its accompanying Python program.  It verifies $d^2=0$ in all
degrees and carries out integral Smith reductions.  The separate
\path{code/current_audits/audit_corrections/code/verify_V_global_saved_07.py}
reconstructs the homology bases used below and checks the saved
integral maps.''',
    'The actual complement and finite-cap differentials have been reconstructed from (1.12.1–6), including their signs and primitive split maps.')

add('night:P1.12',span('In degrees two and three, the program','after tensoring with\n$\\mathbb Q$.'),r'''In degrees two and three, the saved-output verifier supplies integral
cycle bases of its free kernel represented in $L_k$ itself.  It
exports their full fibre coordinates and checks both their classes
in $H_k(B_0)$ and their images in $H_k(Y)$.  Their entire suspension
block in (1.12.2) is exactly zero over $\mathbb Z$.  In degree three
the additional order-two generator is also given as a fibre cycle
and its cusp image is checked to be zero.''',
    'Fresh integer solves construct actual vertical representatives of all free kernel generators; the separate torsion cycle is retained.')

add('night:P1.12',r'''For transparency, in the Smith bases exported with these cycles the
combined map in degree one is''',r'''Use the homology bases and actual cycle representatives exported in
\path{code/current_audits/audit_corrections/code/verify_V_global_saved_07.json}.
The boundary bases are computed from (1.12.2), the complement bases
from (1.12.6), and the cusp bases are those of the marked collapse
in P1.11.  In these bases the combined map in degree one is''',
    'State the exact freshly reconstructed source and target bases; the H1 matrix happens to agree literally with the old displayed matrix.')

old=span('In degree two $\\ker j_Y=\\mathbb Z^9$ and its map to $H_2(C)$ is','\\tag{1.12.8}\n\\]')
new='In degree two $\\ker j_Y=\\mathbb Z^9$ and its map to $H_2(C)$ is\n\\[\n'+pm(bridges['2']['kernel_collapse'])+r''',\qquad\det=1.
\tag{1.12.8}
\]'''
add('night:P1.12',old,new,'Replace the old unsupported basis display by the literal newly verified 9-by-9 collapse on exported vertical kernel cycles.')

old=span('Its collapse matrix, with the torsion generator first, is','\\tag{1.12.9}\n\\]')
C3=[[0]+row for row in bridges['3']['kernel_collapse']]
new='Its collapse matrix, with the torsion generator first, is\n\\[\n'+pm(C3)+r'''.
\tag{1.12.9}
\]'''
add('night:P1.12',old,new,'The zero torsion column and nine free columns now have actual exported boundary cycles; their determinant is checked to be one.')

add('night:P1.19',r'''and its differentials, after the explicit integral chain equivalences
below, are the matrices of case one in
\path{code/part1/global_ext_cases.json}.''',r'''and its differentials, after the explicit integral chain equivalences
below, are the matrices in
\path{code/current_audits/audit_corrections/code/reconstruct_V_global_06.json}.
The accompanying program reconstructs them from the displayed marked
maps; the separate saved-output verifier supplies their integral
cycle and incoming-map checks and the basis comparisons below.''',
    'Replace unavailable historical output by the freshly executed full global cellular model, with its exact degree-four correction.')

add('night:P1.19',r'''collapse $\kappa_k$ already exported in
\texttt{cusp\_marked\_collapse.json}.''',r'''collapse $\kappa_k$ reconstructed in
\path{code/current_audits/audit_corrections/code/reconstruct_V_cusp_06.json}.
Its source basis is $(a_1,a_2,a_3,b_1,b_2,b_3)$; the actual matrix $S$
from P1.7 changes it to the original lattice by
$\kappa_k^{\rm orig}=\kappa_k\bigwedge^kS^{-1}$.
These transported matrices are included in the global reconstruction.''',
    'Explicitly retain the actual source marking rather than rename an old collapse export.')

add('night:P1.19',r''' \psi=(0,0,0,1,-1,1,1,-1,-1,1)''',r''' \psi=(1,-1,1,1,-1,-1,1,0,0,0)''',
    'Use the primitive annihilator of the actual new degree-four cusp matrix, in its explicitly exported target basis.')

add('night:P1.19',span('The exact multiplication $\\psi\\kappa_4=0$ and the primitive Smith','computed in \\texttt{cusp\\_relative\\_candidate.json}.'),r'''The exact multiplication $\psi\kappa_4=0$ and the primitive Smith
factors are checked in the global reconstruction.  Setting
$\varepsilon=0$ gives relative cusp homology
$H_4(C,\partial)=\mathbb Z^{10}\oplus\mathbb Z/2$.
The two-term Smith-pair splitting in the preceding item gives this
split extension directly.  The saved-output verifier also constructs
the relative cone and checks its degree-four integral homology.''',
    'Preserve the exact local relative assertion and identify the fresh verification, without a missing historical JSON claim.')

add('night:P1.19',r'''Its cokernel is free of rank four. In its exported cokernel basis,
the map from $H_4(C)$ is''',r'''Its cokernel is free of rank four.  The saved-output verifier exports
the actual boundary cycle basis and complement homology projection
used to form $j_4$.  If $U_4j_4V_4$ is its exported Smith reduction,
take the last four rows of $U_4$ and interchange their first and
fourth rows.  This is the explicitly verified unimodular cokernel
adapter.  In the resulting cokernel basis the map from $H_4(C)$ is''',
    'Supply the actual source/target basis and concrete cokernel row adapter for equation (1.19.5).')

add('night:P1.19',r'''$[e_4,K]$ is unimodular.  The file
\texttt{cusp\_ext\_reduction.json} gives integral lifts $W$ satisfying''',r'''$[e_4,K]$ is unimodular.  The saved-output verifier gives the exact
unimodular change from the Smith kernel basis to these nine columns,
and exports the resulting integral lifts $W$ satisfying''',
    'The new 9-by-9 basis transport, W, X and T are actually computed; the simple literal kernel basis is retained.')

add('night:P1.19',r'''In the ordered 35-dimensional boundary chain group it is
$r=-e_{17}^{t}-e_{18}^{t}$.  It satisfies''',r'''In the ordered boundary group
$B_{0,4}=\bigwedge^4\Lambda\oplus\bigwedge^3\Lambda$, with each
exterior basis lexicographically ordered in the original lattice,
it is
\[
r=e_{29}^{t}+e_{30}^{t}+e_{31}^{t}
  -e_{32}^{t}-e_{33}^{t}-e_{34}^{t}+e_{35}^{t}.
\]
The verifier checks that it is not an integral coboundary by the
augmented rank obstruction modulo two.  It satisfies''',
    'Replace the unsupported old cocycle coordinates by the newly constructed primitive order-two cocycle in the stated actual chain basis.')

old=span('The program \\texttt{global\\_ext\\_cases.py} inserts (1.19.8) into','global duality conclusion of P1.12.')
new=r'''The reconstruction program inserts (1.19.8) into the complete
main-piece/three-cap mapping cone, retaining every finite-cap
differential and every boundary map of P1.12.  It checks $d^2=0$
over $\mathbb Z$ and exports every differential.  The corrected case
is the actual global model by the preceding explicit chain
equivalence.

The separate saved-output verifier checks the integral inverse
matrices and cycle bases, the incoming matrices in those bases, and
their Smith left and right matrices.  It verifies the outgoing ranks
by their displayed integral kernels and exact rank witnesses modulo
$1009$.  It also exports the actual $W,X,T$ maps in the literal $K$
basis, checks every identity in (1.19.6)--(1.19.7), and verifies both
relative cusp degree-four groups.  The even case is recomputed as
an unused diagnostic and gives the same global homology; its local
relative torsion retains the distinction needed in item~9.
The differential ranks in degrees one through eight are
\[
                 (3,23,64,98,98,58,21,2).
\]
All nonzero incoming Smith factors in the cycle lattices are one.
Subtracting incoming and outgoing ranks from the displayed chain
ranks gives $(1,0,0,0,4,0,0,0,1)$, with no torsion.
The exact saved files are
\path{code/current_audits/audit_corrections/code/reconstruct_V_global_06.py},
\path{code/current_audits/audit_corrections/code/reconstruct_V_global_06.json},
\path{code/current_audits/audit_corrections/code/verify_V_global_saved_07.py}
and its JSON output.  This completes the full cellular comparison
without using the global duality conclusion of P1.12.'''
add('night:P1.19',old,new,'Replace all missing historical global/relative exports by the actually reconstructed model and independent saved-matrix verification, preserving the local Ext proof and unused even diagnostic.')

add('night:P1.19',r'''\StatementRecord{night:P1.19}{proved}{}{\cref{night:P1.11}, \cref{night:P1.12}, \cref{night:P1.9}}''',r'''\StatementRecord{night:P1.19}{proved}{}{\cref{night:P1.11}, \cref{night:P1.12}, \cref{night:P1.9}; \cite[Theorem~3.43, p.~254]{Hatcher2002}}''',
    'Freshly opened original author PDF, Theorem 3.43 printed page254: exact local cap-product specialization n8,k4,R=Z,A=empty,B=boundary.')
add('night:P1.19',r'''It retracts onto $C$.  Poincar\'e--Lefschetz duality and the already
computed free cusp homology give''',r'''Let $\rho$ be its retraction onto $C$.  Pullback by $\rho$, followed
by cap product with the relative fundamental class of this actual
oriented cusp cap, is the isomorphism of
\cite[Theorem~3.43, p.~254]{Hatcher2002}, with $n=8$, $k=4$,
$R=\mathbb Z$, $A=\varnothing$ and $B=\partial$.
The already computed free cusp homology therefore gives''',
    'Name the exact source theorem and the actual pullback/cap-product morphism; retain local scope.')

out=Path(__file__).with_name('V_P112_P119_guarded_patches_07.json')
out.write_text(json.dumps(patches,indent=2))
receipt={'utc':datetime.now(timezone.utc).isoformat(),'guards':len(patches),'body_sha256':hashlib.sha256(body_path.read_bytes()).hexdigest(),
         'patch_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'scope':'Only proposed exact guarded replacements. Shared manuscript unchanged. Final extended saved verifier PASS914 includes both local relative groups and the unused even global diagnostic; all 16 guards are ready for root review.'}
Path(__file__).with_name('V_P112_P119_patch_receipt_07.json').write_text(json.dumps(receipt,indent=2))
print(json.dumps(receipt))
