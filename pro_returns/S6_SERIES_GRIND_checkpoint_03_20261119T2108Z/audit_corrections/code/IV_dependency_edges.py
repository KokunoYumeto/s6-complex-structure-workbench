"""Record literal body-level uses for the seven IV front theorems."""
from pathlib import Path
import json
here=Path(__file__).resolve().parents[1]
src=here.parents[1]/'S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15/S6_10_PAPERS_IV.tex'
lines=src.read_text().splitlines()
specs=[
('A','B','night:P3K.69','iv:correction:P3K.10',74726,74737,
 'The physical formula A_M=d/2−1 with d=8 gives 3; the P3K.68 gluing arrow identifies this integer modulo 28 with the oriented sphere.'),
('A','B','night:P3K.68','iv:correction:P3K.23',74812,74820,
 'The literal line/gluing comparison gives native increment n=6A_M, hence the directed flop value A_M+n=7A_M.'),
('A','C','night:P3K.68','night:P3K.73',30114,30126,
 'Physical Hopf transfer converts the computed free characteristic pair of the actual shorter cover into the single-loop integer seed.'),
('A','D','night:P3K.68','night:P3K.86',38036,38045,
 'The full anti-linear physical-normal comparison is composed with the displayed complex-linear positive-cap spinor map.'),
('A','E','night:P3K.68','night:P3K.99',44973,44983,
 'PL.1–6 fix the physical dual line, both cap arrows, and first-to-second inverse-clutch convention used for the order-three inner-to-physical pair.'),
('A','F','night:P3K.68','night:P3K.101',51512,51524,
 'The actual dual-line map carries inner U pair (−4,8) to physical inner pair (4,−8), before the literal outer-boundary arrow.'),
('D','E','night:P3K.96','night:P3K.99',44976,44984,
 'The original E6 good-root and annular maps of P3K.96–98 are retained as geometric inputs to the source-line suspension.'),
('D','F','night:P3K.96','night:P3K.101',51525,51534,
 'The E6 reference orbit and actual finite-cap comparison of P3K.96–98 supply the retained root/character data of the selected-infinity computation.'),
('D','G','night:P3K.98','night:P3K.108',68678,68690,
 'The source, Cartier, root and reference maps extend along the compact arc, including its unselected type-III endpoint, with the actual M6 translation and selected-height data.'),
('E','G','night:P3K.103','night:P3K.108',68450,68461,
 'The full OC.4 and OC.6 translation/inverse-chord/identity-component field maps are applied to ICAP.4; unit denominators give jointly analytic cap coefficients.'),
('F','G','night:P3K.104','night:P3K.108',68665,68675,
 'The complete signed meridian arrows HC.27 and SN.24a identify the higher-root cap with the same ordinary generators and retain determinant/norm sign.'),
('A','G','night:P3K.68','night:P3K.108',68718,68727,
 'The selected fixed tube and physical Hopf completion are disjoint from the changed infinity cap and retain their literal line, quaternion, selected height and interval convention.'),
]
edges=[]
for a,b,s,t,start,end,use in specs:
    evidence='\n'.join(lines[start-1:end])
    assert s in evidence or s.split(':')[-1] in evidence,(s,start)
    edges.append(dict(from_main='series:IV:'+a,to_main='series:IV:'+b,
                      supplying_body_label=s,using_body_label=t,
                      source_file=str(src),source_lines=[start,end],
                      used_conclusion=use,evidence_tex=evidence))
out={'method':'Each edge is a literal use in a proof body, not a shared-input or chronology inference.',
     'edges':edges,
     'suggested_transitively_reduced_main_edges':[['A','B'],['A','C'],['A','D'],['D','E'],['D','F'],['E','G'],['F','G']],
     'scope':'Edges describe the proved conclusions represented in the seven theorem groups. They do not claim all their component statements depend on every predecessor.'}
(here/'IV_dependency_edges.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'literal_edges':len(edges),'diagram_edges':out['suggested_transitively_reduced_main_edges']}))
