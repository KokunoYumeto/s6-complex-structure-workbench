"""Record the source audits and actual visual inspection through UN62/64."""
from pathlib import Path
from datetime import datetime, timezone
import csv

root = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
record = r'''# Reduced trees, quasibundle cycles and exceptional leaves

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

## Verified source additions

UN60 completes the full reduced all-Hopf SNC support criterion. The proof retains the exact one- and two-point root-curve torsor classes, the secondary integer, every marked elliptic map, the inverse leaf charts and the complement fundamental-group maps. Its construction reverses those charts inside the compact diagonal Hopf/ruled core family. The affine-base estimates prove properness of the replacements. Root and the independent A and D audits accepted the complete source and executed certificates. The source frozen in checkpoint10 was promoted byte for byte to part_C2_hopf_tree_occurrence.tex; the frozen draft remains present.

UN61 supplies the corresponding rooted-tree criterion with an arbitrary smooth distinguished component, nonroot Hopf surfaces or the specified identity-monodromy elliptic quasibundles. The original Hopf-only source is preserved at records/versions/UN61_hopf_only_20261115.tex. The extension retains the actual root-chart restriction maps. The triangular coherent-incidence comparison gives H2 of the support equal to H2 of the root, the residue maps identify its canonical minimum, and the actual normal-root comparison identifies the root's elliptic fibration. Pruning produces a principal elliptic torsor over an elliptic curve. The integral commutator is its Chern class; its vanishing gives an actual complex two-torus with all original torsor data retained. The reverse period construction restores every component compactly. Root and the independent E and D audits accepted the extended full source and both programs.

UN62 gives the complete unicyclic criterion in the specified quasibundle/nonlinear-Hopf class. The exact root chart makes R1q_*O equal to O and makes every boundary restriction nonzero in the same fibre cohomology frame. This supplies the weighted incidence computation without identifying maps solely by dimensions. The canonical period orders, full torsor pruning and reversed compact construction retain every original properly elliptic component. The explicit example has four triple elliptic fibres on one component: its line is O(D1+...+D4) on the four-point order-three root curve. The frame comparison y=sW proves the positive divisor sign. The exact plurigenus formula gives P_(3b)=2b+1. Root and the independent A and E audits accepted the full source and executed output.

UN64 gives exact necessary terminal ruled and plane pair restrictions in an actual full reduced SNC torus fibre. The section and plane-line cases have holomorphic ordinary blowdowns, with the descended map and full reduced fibre verified in local coordinates. A curve contraction retains the full extension 0 -> K_B -> V -> O_B -> 0 and changes the reduced fibre Euler number by 2-2g(B); a point contraction changes it by 2. The bisection over an elliptic base is excluded by the actual residue and finite-trace maps. The anticanonical alternatives are pair restrictions only; no realization of arbitrary such pairs is asserted. Both elliptic extension types are realized by ordinary blowups in the compact twistor family. Varying the actual period coefficient a in w+a*t*J(conjugate(w)) prescribes any nonzero extension class with both endpoint frames and df fixed. The Laurent constant obstruction proves nonsplitting. Root and the independent A audit accepted the full proof, the exact computations and the corrected primary contraction source. The initial draft and pre-parameter code/output are retained. UN64 was promoted to part_C2_exceptional_leaves.tex after that precision was applied.

## Executed calculations

E_hopf_tree_pruning.py checks 120 primitive bases, 400 root Picard lattices, 215 weighted maps, 19 cap drops and a nested reconstruction record. A_rooted_hopf_trees.py and A_tree_periods.py check the rooted incidence, integral Chern commutator, torsor period matrix and exact height/period identities. D_quasibundle_trees.py checks 60 root maps, 9600 pole bounds, the example's incidence rank and 40 exact plurigenera. root_exceptional_leaves.py checks all terminal degree alternatives, the ordinary blowup Jacobians, the extension cocycle and coboundary matrices, 61 Laurent monomials, 61 positive/negative normal deck iterates, the fixed-endpoint scaling, the real period determinant and the Euler changes. Every actual output is retained beside its program.

## Build and actual visual inspection

The source assembler was corrected to use the same part_*.tex entry points as the manuscript assembler. Previously its broader glob counted the retained UN60 historical draft and the promoted source twice. No historical source was removed. The first compile of the enlarged UN61 source exposed three TeX errors from an unbraced determinant subscript; the source was corrected to det_{C}. Both failed build records remain present.

The clean build root_build_2252.out contains 215 numbered statements in 418 pages, through UN62. All four compiler/bibliography passes returned zero; the final log has zero TeX errors, zero overfull boxes, zero unresolved references and zero missing glyph warnings. render_qa_2254.out and the associated manifest record the actual raster renders. Root subsequently viewed full-page images 204, 205, 208, 262, 265, 292 and 295 in small batches. They show no clipping, overlap or truncated formulas. An earlier seven-image call was truncated by the tool response and was not counted as visual inspection. This record concerns the 418-page PDF; later additions require their own compile and rendered-page checks.

## Remaining main question

The unrestricted classification of all reducible zero-Euler supports remains undecided. These statements close their specified support classes and provide actual maps for the broader reduction. The active next steps are the arbitrary-multiplicity root reconstruction, the complete equal-canonical-order branch, and reduction of minimal-component SNC supports with no triple points. No general equivalence to a chosen core is asserted without its actual comparison maps.
'''
(root/'records/root_research_reduced_trees.md').write_text(record+'\nRecorded: '+stamp+'\n')

path = root/'records/root_results.csv'
with path.open(newline='') as f:
    reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)
for row in rows:
    if row['id']=='C.2.UN.64':
        row['where_proved']='sections/part_C2_exceptional_leaves.tex; C.EL.1–11; code/root_exceptional_leaves.py and .out'
        row['notes']=row['notes'].replace('Full source audits requested.','Root and independent A full-source, exact-computation and primary-source audits passed. The actual period parameter realizes every nonzero class with fixed endpoint frames and fixed df. Initial source and pre-parameter program/output are retained.')
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(rows)

report=root/'S6_03_CDP_report.md'
text=report.read_text()
text=text.replace('C.2.UN.1–59; C.2.UN.60 (source);','C.2.UN.1–62; C.2.UN.64 (source);',1)
needle='The remaining unresolved clause is the unrestricted geometric classification of all reducible zero-Euler supports;'
addition='UN60 completes every full reduced all-Hopf SNC support by exact leaf pruning and compact reinsertion. UN61 completes rooted trees with an arbitrary smooth central component and the specified Hopf/quasibundle branches, retaining the full analytic torsors and integral Chern class. UN62 completes the specified unicyclic quasibundle/Hopf class and gives a compact example with a properly elliptic component and four triple elliptic fibres. UN64 gives exact exceptional-leaf restrictions, actual holomorphic blowdowns, their full normal extensions and exact Euler changes. '
assert needle in text
if addition not in text:
    text=text.replace(needle,addition+needle,1)
heading='## Reduced trees and quasibundle cycles after checkpoint 10'
if heading not in text:
    text+='\n\n'+heading+'\n\n'+record.split('## Verified source additions\n\n',1)[1]
report.write_text(text)
print('Recorded full-source audits UN60–62/64, exact computations, retained corrections and actual 418-page visual QA.')
print('Report remains INCOMPLETE; UN64 source added pending next compiled cutoff.')
